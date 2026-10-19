<?php
// Study plans of the signed-in student.
//   GET  api/study_plans.php?action=list                  → {ok, plans:[{...plan}], deleted:[id…]}
//   POST api/study_plans.php?action=save   {plan:{id,updatedAt,…}}   newer copy wins
//   POST api/study_plans.php?action=delete {id}
// The browser keeps its own copy too, so plans work offline and for guests.

require __DIR__ . '/db.php';
require __DIR__ . '/session.php';
require __DIR__ . '/lib/security.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const MAX_PLAN_BYTES = 2000000;
const MAX_PLANS      = 50;

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

function valid_id($id): ?string
{
    $id = (string)$id;
    return preg_match('/^[A-Za-z0-9_-]{4,40}$/', $id) ? $id : null;
}

if (empty($_SESSION['uid'])) fail(401, 'Log in to keep your plans on every device');
$uid = (int)$_SESSION['uid'];

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    fail(500, 'Database connection failed');
}

$action = $_GET['action'] ?? '';
if ($action !== 'list' && $_SERVER['REQUEST_METHOD'] !== 'POST') fail(405, 'POST required');
if ($action !== 'get' && $action !== 'load' && $action !== 'list' && !sb_request_is_same_site()) fail(403, 'Request not allowed');

try {
    switch ($action) {

    case 'list':
        $st = $pdo->prepare('SELECT plan_id, plan_json, deleted FROM study_plans WHERE user_id = ? ORDER BY updated_ms DESC');
        $st->execute([$uid]);
        $plans = [];
        $deleted = [];
        foreach ($st as $r) {
            if ($r['deleted']) { $deleted[] = $r['plan_id']; continue; }
            $p = json_decode($r['plan_json'], true);
            if (is_array($p)) $plans[] = $p;
        }
        reply(200, ['ok' => true, 'plans' => $plans, 'deleted' => $deleted]);

    case 'save':
        $plan = input()['plan'] ?? null;
        if (!is_array($plan)) fail(422, 'Bad plan');
        $id = valid_id($plan['id'] ?? '');
        if (!$id) fail(422, 'Bad plan id');
        $json = json_encode($plan, JSON_UNESCAPED_UNICODE);
        if (strlen($json) > MAX_PLAN_BYTES) fail(413, 'Plan is too large');
        $ms = max(0, (int)($plan['updatedAt'] ?? 0));
        $st = $pdo->prepare('SELECT COUNT(*) FROM study_plans WHERE user_id = ? AND deleted = 0 AND plan_id <> ?');
        $st->execute([$uid, $id]);
        if ((int)$st->fetchColumn() >= MAX_PLANS) fail(409, 'You can keep up to ' . MAX_PLANS . ' plans');
        // keep the newer copy when two devices edit the same plan
        $pdo->prepare('INSERT INTO study_plans (user_id, plan_id, plan_json, updated_ms, deleted) VALUES (?, ?, ?, ?, 0)
                       ON DUPLICATE KEY UPDATE
                         plan_json  = IF(VALUES(updated_ms) >= updated_ms, VALUES(plan_json), plan_json),
                         deleted    = IF(VALUES(updated_ms) >= updated_ms, 0, deleted),
                         updated_ms = GREATEST(updated_ms, VALUES(updated_ms))')
            ->execute([$uid, $id, $json, $ms]);
        reply(200, ['ok' => true]);

    case 'delete':
        $id = valid_id(input()['id'] ?? '');
        if (!$id) fail(422, 'Bad plan id');
        $pdo->prepare('UPDATE study_plans SET deleted = 1, plan_json = \'{}\', updated_ms = ? WHERE user_id = ? AND plan_id = ?')
            ->execute([(int)round(microtime(true) * 1000), $uid, $id]);
        reply(200, ['ok' => true]);

    default:
        fail(400, 'Unknown action');
    }
} catch (Throwable $e) {
    error_log('SpaceBook plans: ' . $e->getMessage());
    fail(500, 'Could not save the plan');
}
