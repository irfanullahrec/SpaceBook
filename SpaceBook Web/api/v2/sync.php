<?php
// Offline-safe synchronisation of student records (v2). Compatible with PHP 7.4.
//
//   POST api/v2/sync.php   {"events":[{eventId, type, payload, clientTs, schema}, ...]}   (<= 500 events, <= 1 MB)
//     -> {ok, accepted:[eventId...], rejected:[{eventId, code}...], cursor, coins}
//   GET  api/v2/sync.php?since=<cursor>      (0 or missing = everything)
//     -> {ok, cursor, more, coins, progress, plans, plansDeleted, tp}      (see api/lib/pull.php)
//
// Each event is applied at most once per user (the client's eventId is the idempotency key), so a client can
// resend a batch after any failure. `accepted` includes events the server had already applied. `rejected`
// events are permanently invalid (the client drops them); anything transient is an HTTP error and the whole
// batch stays in the client's outbox. Coins are decided here from facts ("step 3 of activity X is done"), never
// from amounts sent by the browser; rules and limits are in api/lib/rewards.php.
//
// Event types and payloads:
//   step          {key, title, total, step}            reward progress
//   again         {key}                                 a completed activity done again
//   plan.save     {plan, baseRev}                       study plan (merge rules: api/lib/plans.php)
//   plan.delete   {id}
//   tp.answer     {mcqId, track, day, correct, ms, ts} one Tests Preps answer
//   tp.session    {session}                             a finished Tests Preps session
//   tp.run        {run}                                 the unfinished session (run.savedAt decides)
//   tp.run.clear  {clearedAt}
//
// Authentication: 'Authorization: Bearer <device token>' (issued by api/auth.php with want_device), or the
// session cookie (then the request must be same-site).

require __DIR__ . '/../db.php';
require_once __DIR__ . '/../lib/security.php';
require_once __DIR__ . '/../lib/rewards.php';
require_once __DIR__ . '/../lib/changes.php';
require_once __DIR__ . '/../lib/plans.php';
require_once __DIR__ . '/../lib/testprep.php';
require_once __DIR__ . '/../lib/pull.php';

const SB_SYNC_MAX_EVENTS = 500;
const SB_SYNC_MAX_BYTES  = 1048576;
const SB_SYNC_MAX_EVENT  = 65536;
const SB_SYNC_RATE       = 60;      // requests per minute per user

// events that may be larger than the default 64 KB
$SB_SYNC_BIG = ['plan.save' => 524288, 'tp.session' => 200000, 'tp.run' => 200000];

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function sync_reply(int $code, array $body, int $retryAfter = 0): void
{
    if ($retryAfter > 0) header('Retry-After: ' . $retryAfter);
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_PARTIAL_OUTPUT_ON_ERROR);
    exit;
}

function sync_fail(int $code, string $msg, int $retryAfter = 0): void
{
    sync_reply($code, ['ok' => false, 'error' => $msg], $retryAfter);
}

$method = $_SERVER['REQUEST_METHOD'];
if ($method !== 'POST' && $method !== 'GET') sync_fail(405, 'GET or POST required');

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    sync_fail(500, 'Database connection failed');
}

// ---- who is calling
$uid = 0;
$deviceId = '';
$dev = sb_device_from_request($pdo);
if ($dev) {
    $uid = $dev['user_id'];
    $deviceId = $dev['device_id'];
} elseif (sb_bearer_token() === '' && isset($_COOKIE['spacebook_sid'])) {
    require __DIR__ . '/../session.php';
    if (!empty($_SESSION['uid'])) {
        if ($method === 'POST' && !sb_request_is_same_site()) sync_fail(403, 'Request not allowed');
        $uid = (int)$_SESSION['uid'];
        $deviceId = 'cookie';
    }
}
if ($uid <= 0) sync_fail(401, 'Sign in again to sync');

$rl = sb_rate_hit($pdo, 'sync:u:' . $uid, SB_SYNC_RATE, 60);
if (!$rl['ok']) sync_fail(429, 'Too many sync requests', $rl['retry']);

// ---- pull
if ($method === 'GET') {
    try {
        $pdo->beginTransaction();
        sb_tp_import_legacy($pdo, $uid);          // first v2 contact: bring the old test-prep record in
        $pdo->commit();
        sync_reply(200, sb_pull($pdo, $uid, isset($_GET['since']) ? max(0, (int)$_GET['since']) : 0));
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        error_log('SpaceBook pull: ' . $e->getMessage());
        sync_fail(500, 'Could not load, try again', 5);
    }
}

// ---- push: body
$len = isset($_SERVER['CONTENT_LENGTH']) ? (int)$_SERVER['CONTENT_LENGTH'] : 0;
if ($len > SB_SYNC_MAX_BYTES) sync_fail(413, 'Batch is too large');
$raw = (string)file_get_contents('php://input', false, null, 0, SB_SYNC_MAX_BYTES + 1);
if (strlen($raw) > SB_SYNC_MAX_BYTES) sync_fail(413, 'Batch is too large');
$in = json_decode($raw, true);
if (!is_array($in) || !isset($in['events']) || !is_array($in['events'])) sync_fail(422, 'Bad request');
$events = $in['events'];
if (count($events) > SB_SYNC_MAX_EVENTS) sync_fail(413, 'Too many events in one batch (max ' . SB_SYNC_MAX_EVENTS . ')');

// Returns null when applied, or a rejection code. Runs inside the batch transaction.
function sync_apply(PDO $pdo, int $uid, string $type, array $p): ?string
{
    switch ($type) {
    case 'step':
        $key = isset($p['key']) ? (string)$p['key'] : '';
        if (sb_reward_key_kind($key) === null) return 'bad_key';
        $total = isset($p['total']) ? (int)$p['total'] : 0;
        if ($total < 1 || $total > SB_MAX_STEPS) return 'bad_total';
        $step = isset($p['step']) && is_numeric($p['step']) ? (int)$p['step'] : -1;
        if ($step < 0 || $step >= SB_MAX_STEPS) return 'bad_step';
        $r = sb_reward_add_steps($pdo, $uid, $key, isset($p['title']) ? (string)$p['title'] : '', $total, [$step]);
        return $r['created'] ? null : 'activity_limit';
    case 'again':
        $key = isset($p['key']) ? (string)$p['key'] : '';
        if (sb_reward_key_kind($key) === null) return 'bad_key';
        return sb_reward_again($pdo, $uid, $key) === null ? 'not_completed' : null;
    case 'plan.save':
        if (!isset($p['plan']) || !is_array($p['plan'])) return 'bad_payload';
        return sb_plan_save($pdo, $uid, $p['plan'], isset($p['baseRev']) && is_numeric($p['baseRev']) ? max(0, (int)$p['baseRev']) : 0);
    case 'plan.delete':
        return sb_plan_delete($pdo, $uid, isset($p['id']) ? (string)$p['id'] : '');
    case 'tp.answer':
        return sb_tp_answer($pdo, $uid, $p);
    case 'tp.session':
        return isset($p['session']) && is_array($p['session']) ? sb_tp_session($pdo, $uid, $p['session']) : 'bad_payload';
    case 'tp.run':
        return isset($p['run']) && is_array($p['run']) ? sb_tp_run_save($pdo, $uid, $p['run']) : 'bad_payload';
    case 'tp.run.clear':
        return sb_tp_run_clear($pdo, $uid, $p);
    default:
        return 'unsupported_type';
    }
}

$accepted = [];
$rejected = [];
try {
    $pdo->beginTransaction();
    sb_tp_import_legacy($pdo, $uid);
    $ledger = $pdo->prepare('INSERT IGNORE INTO sync_events (user_id, event_id, device_id, type, client_ts) VALUES (?, ?, ?, ?, ?)');
    foreach ($events as $ev) {
        $id = is_array($ev) && isset($ev['eventId']) && is_string($ev['eventId']) ? strtolower($ev['eventId']) : '';
        if (!preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/', $id)) {
            $rejected[] = ['eventId' => $id, 'code' => 'bad_event_id'];
            continue;
        }
        $type = isset($ev['type']) && is_string($ev['type']) ? $ev['type'] : '';
        $payload = isset($ev['payload']) && is_array($ev['payload']) ? $ev['payload'] : null;
        if ($payload === null) { $rejected[] = ['eventId' => $id, 'code' => 'bad_payload']; continue; }
        if (isset($ev['schema']) && (int)$ev['schema'] !== 1) { $rejected[] = ['eventId' => $id, 'code' => 'bad_schema']; continue; }
        $max = isset($SB_SYNC_BIG[$type]) ? $SB_SYNC_BIG[$type] : SB_SYNC_MAX_EVENT;
        if (strlen(json_encode($payload)) > $max) { $rejected[] = ['eventId' => $id, 'code' => 'too_large']; continue; }
        $clientTs = isset($ev['clientTs']) && is_numeric($ev['clientTs']) ? max(0, (int)$ev['clientTs']) : 0;

        // 1) record the event id; if it was already there the work was done by an earlier request
        $ledger->execute([$uid, $id, $deviceId, substr($type, 0, 20), $clientTs]);
        if ($ledger->rowCount() === 0) { $accepted[] = $id; continue; }
        // 2) apply it; a permanent problem un-records the id again so nothing half-done stays behind
        $code = sync_apply($pdo, $uid, $type, $payload);
        if ($code !== null) {
            $pdo->prepare('DELETE FROM sync_events WHERE user_id = ? AND event_id = ?')->execute([$uid, $id]);
            $rejected[] = ['eventId' => $id, 'code' => $code];
            continue;
        }
        $accepted[] = $id;
    }
    $pdo->commit();
} catch (Throwable $e) {
    if ($pdo->inTransaction()) $pdo->rollBack();
    error_log('SpaceBook sync: ' . $e->getMessage());
    sync_fail(500, 'Could not save, try again', 5);
}

sync_reply(200, ['ok' => true, 'accepted' => $accepted, 'rejected' => $rejected, 'cursor' => sb_change_cursor($pdo, $uid), 'coins' => sb_total_coins($pdo, $uid)]);
