<?php
// Student activity progress + reward coins.
//   GET  api/progress.php?action=get                     → {ok, coins, completed, activities:{key:{done,total,times,first,last}}}
//   POST api/progress.php?action=step   {key,title,total,step}  one step of an activity finished
//   POST api/progress.php?action=again  {key}                   a completed activity was done again
//   POST api/progress.php?action=sync   {items:[{key,title,total,done:[…]}]}  guest progress after login
// Coins are decided here, never by the browser (rules and daily limits: api/lib/rewards.php):
//   +1 for each step the first time it is finished, +5 when the whole activity is first completed,
//   +2 for doing a completed activity again (at most once per activity per day).
// This v1 endpoint stays for old clients; api/v2/sync.php is the offline-safe replacement.

require __DIR__ . '/db.php';
require __DIR__ . '/session.php';
require __DIR__ . '/lib/security.php';
require __DIR__ . '/lib/rewards.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

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
if ($action !== 'get' && $action !== 'load' && $action !== 'list' && !sb_request_is_same_site()) fail(403, 'Request not allowed');

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
                'done'  => sb_parse_done($r['steps_done']),
                'total' => (int)$r['steps_total'],
                'times' => (int)$r['times_completed'],
                'first' => $r['first_completed_at'],
                'last'  => $r['last_completed_at'],
            ];
            if ((int)$r['times_completed'] > 0) $completed++;
        }
        reply(200, ['ok' => true, 'coins' => sb_total_coins($pdo, $uid), 'completed' => $completed, 'activities' => (object)$acts]);

    case 'step':
        $in = input();
        $key = sb_reward_key($in['key'] ?? '');
        if (!$key) fail(422, 'Bad activity');
        $pdo->beginTransaction();
        $r = sb_reward_add_steps($pdo, $uid, $key, (string)($in['title'] ?? ''), (int)($in['total'] ?? 1), [(int)($in['step'] ?? -1)]);
        $pdo->commit();
        reply(200, ['ok' => true, 'earned' => $r['earned'], 'completed' => $r['completed'], 'times' => $r['times'], 'coins' => sb_total_coins($pdo, $uid)]);

    case 'again':
        $key = sb_reward_key(input()['key'] ?? '');
        if (!$key) fail(422, 'Bad activity');
        $pdo->beginTransaction();
        $r = sb_reward_again($pdo, $uid, $key);
        $pdo->commit();
        if ($r === null) fail(409, 'Activity not completed yet');
        reply(200, ['ok' => true, 'earned' => $r['earned'], 'times' => $r['times'], 'coins' => sb_total_coins($pdo, $uid)]);

    case 'sync':
        $items = input()['items'] ?? [];
        if (!is_array($items)) fail(422, 'Bad items');
        $pdo->beginTransaction();
        $earned = 0;
        foreach (array_slice($items, 0, 500) as $it) {
            $key = sb_reward_key($it['key'] ?? '');
            if (!$key || !is_array($it['done'] ?? null)) continue;
            $earned += sb_reward_add_steps($pdo, $uid, $key, (string)($it['title'] ?? ''), (int)($it['total'] ?? 1), array_slice($it['done'], 0, SB_MAX_STEPS))['earned'];
        }
        $pdo->commit();
        reply(200, ['ok' => true, 'earned' => $earned, 'coins' => sb_total_coins($pdo, $uid)]);

    default:
        fail(400, 'Unknown action');
    }
} catch (Throwable $e) {
    if ($pdo->inTransaction()) $pdo->rollBack();
    error_log('SpaceBook progress: ' . $e->getMessage());
    fail(500, 'Could not save progress');
}
