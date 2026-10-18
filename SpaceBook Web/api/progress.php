<?php
// Student activity progress + reward coins.
//   GET  api/progress.php?action=get                     → {ok, coins, completed, activities:{key:{done,total,times,first,last}}}
//   POST api/progress.php?action=step   {key,title,total,step}  one step of an activity finished
//   POST api/progress.php?action=again  {key}                   a completed activity was done again
//   POST api/progress.php?action=sync   {items:[{key,title,total,done:[…]}]}  guest progress after login
// Coins are decided here, never by the browser:
//   +1 for each step the first time it is finished, +5 when the whole activity is first completed,
//   +2 for doing a completed activity again (at most once per activity per day).

require __DIR__ . '/db.php';
require __DIR__ . '/session.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const STEP_COIN     = 1;
const COMPLETE_COIN = 5;
const PRACTICE_COIN = 2;
const MAX_STEPS     = 200;

function reply(int $code, array $body): void
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function fail(int $code, string $msg): void
{
    reply($code, ['ok' => false, 'error' => $msg]);
}

function input(): array
{
    $data = json_decode(file_get_contents('php://input') ?: '', true);
    return is_array($data) ? $data : [];
}

function valid_key($k): ?string
{
    $k = (string)$k;
    return preg_match('/^[A-Za-z0-9_.:|\-]{1,190}$/', $k) ? $k : null;
}

function parse_done(string $s): array
{
    return $s === '' ? [] : array_map('intval', explode(',', $s));
}

function total_coins(PDO $pdo, int $uid): int
{
    $st = $pdo->prepare('SELECT COALESCE(SUM(coins_earned), 0) FROM activity_progress WHERE user_id = ?');
    $st->execute([$uid]);
    return (int)$st->fetchColumn();
}

function load_row(PDO $pdo, int $uid, string $key): ?array
{
    $st = $pdo->prepare('SELECT * FROM activity_progress WHERE user_id = ? AND activity_key = ? FOR UPDATE');
    $st->execute([$uid, $key]);
    return $st->fetch() ?: null;
}

// Adds finished steps to one activity; returns [coins earned, completed now?, times_completed].
function add_steps(PDO $pdo, int $uid, string $key, string $title, int $total, array $steps): array
{
    $total = max(1, min(MAX_STEPS, $total));
    $row = load_row($pdo, $uid, $key);
    if (!$row) {
        $pdo->prepare('INSERT INTO activity_progress (user_id, activity_key, title, steps_total, steps_done) VALUES (?, ?, ?, ?, \'\')')
            ->execute([$uid, $key, mb_substr($title, 0, 190), $total]);
        $row = ['steps_total' => $total, 'steps_done' => '', 'times_completed' => 0];
    }
    $total = (int)$row['steps_total'];               // the first report fixes the size of the activity
    $done = parse_done($row['steps_done']);
    $earned = 0;
    foreach ($steps as $s) {
        $s = (int)$s;
        if ($s < 0 || $s >= $total || in_array($s, $done, true)) continue;
        $done[] = $s;
        $earned += STEP_COIN;
    }
    sort($done);
    $times = (int)$row['times_completed'];
    $completedNow = false;
    if ($times === 0 && count($done) >= $total) {
        $earned += COMPLETE_COIN;
        $times = 1;
        $completedNow = true;
    }
    $pdo->prepare('UPDATE activity_progress SET steps_done = ?, coins_earned = coins_earned + ?, times_completed = ?,
                       first_completed_at = IF(? AND first_completed_at IS NULL, NOW(), first_completed_at),
                       last_completed_at  = IF(?, NOW(), last_completed_at)
                   WHERE user_id = ? AND activity_key = ?')
        ->execute([implode(',', $done), $earned, $times, $completedNow ? 1 : 0, $completedNow ? 1 : 0, $uid, $key]);
    return [$earned, $completedNow, $times];
}

if (empty($_SESSION['uid'])) fail(401, 'Log in to save your coins');
$uid = (int)$_SESSION['uid'];

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    fail(500, 'Database connection failed');
}

$action = $_GET['action'] ?? '';
$method = $_SERVER['REQUEST_METHOD'];
if ($action !== 'get' && $method !== 'POST') fail(405, 'POST required');

try {
    switch ($action) {

    case 'get':
        $st = $pdo->prepare('SELECT activity_key, steps_total, steps_done, times_completed, first_completed_at, last_completed_at
                             FROM activity_progress WHERE user_id = ?');
        $st->execute([$uid]);
        $acts = [];
        $completed = 0;
        foreach ($st as $r) {
            $acts[$r['activity_key']] = [
                'done'  => parse_done($r['steps_done']),
                'total' => (int)$r['steps_total'],
                'times' => (int)$r['times_completed'],
                'first' => $r['first_completed_at'],
                'last'  => $r['last_completed_at'],
            ];
            if ((int)$r['times_completed'] > 0) $completed++;
        }
        reply(200, ['ok' => true, 'coins' => total_coins($pdo, $uid), 'completed' => $completed, 'activities' => (object)$acts]);

    case 'step':
        $in = input();
        $key = valid_key($in['key'] ?? '');
        if (!$key) fail(422, 'Bad activity');
        $pdo->beginTransaction();
        [$earned, $completedNow, $times] = add_steps($pdo, $uid, $key, (string)($in['title'] ?? ''), (int)($in['total'] ?? 1), [(int)($in['step'] ?? -1)]);
        $pdo->commit();
        reply(200, ['ok' => true, 'earned' => $earned, 'completed' => $completedNow, 'times' => $times, 'coins' => total_coins($pdo, $uid)]);

    case 'again':
        $key = valid_key(input()['key'] ?? '');
        if (!$key) fail(422, 'Bad activity');
        $pdo->beginTransaction();
        $row = load_row($pdo, $uid, $key);
        if (!$row || (int)$row['times_completed'] === 0) { $pdo->commit(); fail(409, 'Activity not completed yet'); }
        $today = (new DateTime('today'))->format('Y-m-d');
        $earned = ($row['last_completed_at'] && substr($row['last_completed_at'], 0, 10) === $today) ? 0 : PRACTICE_COIN;
        $pdo->prepare('UPDATE activity_progress SET times_completed = times_completed + 1, coins_earned = coins_earned + ?, last_completed_at = NOW()
                       WHERE user_id = ? AND activity_key = ?')->execute([$earned, $uid, $key]);
        $pdo->commit();
        reply(200, ['ok' => true, 'earned' => $earned, 'times' => (int)$row['times_completed'] + 1, 'coins' => total_coins($pdo, $uid)]);

    case 'sync':
        $items = input()['items'] ?? [];
        if (!is_array($items)) fail(422, 'Bad items');
        $pdo->beginTransaction();
        $earned = 0;
        foreach (array_slice($items, 0, 500) as $it) {
            $key = valid_key($it['key'] ?? '');
            if (!$key || !is_array($it['done'] ?? null)) continue;
            $earned += add_steps($pdo, $uid, $key, (string)($it['title'] ?? ''), (int)($it['total'] ?? 1), array_slice($it['done'], 0, MAX_STEPS))[0];
        }
        $pdo->commit();
        reply(200, ['ok' => true, 'earned' => $earned, 'coins' => total_coins($pdo, $uid)]);

    default:
        fail(400, 'Unknown action');
    }
} catch (Throwable $e) {
    if ($pdo->inTransaction()) $pdo->rollBack();
    error_log('SpaceBook progress: ' . $e->getMessage());
    fail(500, 'Could not save progress');
}
