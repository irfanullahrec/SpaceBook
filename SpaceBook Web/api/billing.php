<?php
// Plans, free limits, payments and the account page. One endpoint for the website and the Android app.
//   GET  api/billing.php?action=plans          prices, what each plan includes and excludes, the free allowance, Easypaisa details
//   GET  api/billing.php?action=state          what this caller may use + the free allowance used (same answer as api/v2/entitlements.php)
//   POST api/billing.php?action=consume        {metric: prep_q|plan_q|paper, key, cls?, subject?}  spend one question or the paper; the SERVER decides
//   POST api/billing.php?action=ping           {module?, cls?, subject?, event?}  usage numbers for the management dashboard (no personal data)
//   POST api/billing.php?action=submit_payment {plan, cls?, subjects?, trx, paid_on?, idem}  sign-in required; a pending request, never an activation
//   GET  api/billing.php?action=account        the signed-in person's plans, payments, notices, reminders (only their own)
//   POST api/billing.php?action=read_notes     marks the notices as read
// The caller is the signed-in user (device token or cookie session) and/or a visitor id (header X-SB-Visitor or cookie sb_vid).
// Compatible with PHP 7.4.

require __DIR__ . '/db.php';
require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/billing.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function bill_reply(int $code, array $body): void
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function bill_fail(int $code, string $msg, array $extra = []): void
{
    bill_reply($code, ['ok' => false, 'error' => $msg] + $extra);
}

function bill_input(): array
{
    $raw = file_get_contents('php://input');
    $data = json_decode($raw ?: '', true);
    return is_array($data) ? $data : $_POST;
}

$action = isset($_GET['action']) ? (string)$_GET['action'] : '';
$method = $_SERVER['REQUEST_METHOD'];

if ($action === 'plans') {
    if ($method !== 'GET') bill_fail(405, 'GET required');
    header('Cache-Control: public, max-age=300');
    bill_reply(200, ['ok' => true] + sb_plans_public());
}

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook billing DB: ' . $e->getMessage());
    bill_fail(500, 'Database connection failed');
}

if ($method === 'POST' && !sb_request_is_same_site()) bill_fail(403, 'Request not allowed');

$uid = sb_actor_uid($pdo);
$givenVid = sb_visitor_from_request();
$vid = sb_visitor_touch($pdo, $givenVid, $uid, $action === 'state' || $action === 'consume' || $action === 'ping');
if ($vid !== '' && $vid !== $givenVid && PHP_SAPI !== 'cli') {
    setcookie('sb_vid', $vid, ['expires' => time() + 86400 * 365, 'path' => '/', 'httponly' => true, 'samesite' => 'Lax', 'secure' => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off']);
}

function bill_user(PDO $pdo, int $uid): array
{
    if ($uid <= 0) bill_fail(401, 'Sign in first', ['needSignIn' => true]);
    $st = $pdo->prepare("SELECT * FROM users WHERE id = ? AND status = 'active'");
    $st->execute([$uid]);
    $u = $st->fetch();
    if (!$u) bill_fail(401, 'Sign in first', ['needSignIn' => true]);
    return $u;
}

switch ($action) {

case 'state':
    if ($method !== 'GET') bill_fail(405, 'GET required');
    bill_reply(200, ['ok' => true, 'signedIn' => $uid > 0] + sb_state($pdo, $uid, $vid));

case 'consume':
    if ($method !== 'POST') bill_fail(405, 'POST required');
    $in = bill_input();
    $rl = sb_rate_hit($pdo, 'consume:' . ($uid > 0 ? 'u' . $uid : 'v' . $vid), 3000, 3600);
    if (!$rl['ok']) bill_fail(429, 'Too many requests', ['retry' => $rl['retry']]);
    $metric = isset($in['metric']) ? (string)$in['metric'] : '';
    $ctx = ['cls' => isset($in['cls']) ? (string)$in['cls'] : '', 'subject' => isset($in['subject']) ? (string)$in['subject'] : ''];
    $r = sb_consume($pdo, $uid, $vid, $metric, isset($in['key']) ? (string)$in['key'] : '', $ctx);
    if ($r['allowed']) sb_activity($pdo, $uid, $vid);
    bill_reply(200, ['ok' => true, 'metric' => $metric, 'signedIn' => $uid > 0] + $r);

case 'ping':
    if ($method !== 'POST') bill_fail(405, 'POST required');
    $in = bill_input();
    $rl = sb_rate_hit($pdo, 'ping:' . ($uid > 0 ? 'u' . $uid : 'v' . $vid), 1500, 3600);
    if (!$rl['ok']) bill_reply(200, ['ok' => true, 'dropped' => true]);
    $ua = isset($_SERVER['HTTP_USER_AGENT']) ? (string)$_SERVER['HTTP_USER_AGENT'] : '';
    if (sb_is_bot($ua)) bill_reply(200, ['ok' => true, 'dropped' => true]);
    $cat = sb_catalog();
    sb_activity($pdo, $uid, $vid);
    $cls = isset($in['cls']) ? (string)$in['cls'] : '';
    $sub = isset($in['subject']) ? (string)$in['subject'] : '';
    $mod = isset($in['module']) ? (string)$in['module'] : '';
    $ev  = isset($in['event']) ? (string)$in['event'] : '';
    if ($cls !== '' && isset($cat['classes'][$cls])) sb_stat($pdo, 'class', $cls);
    if ($sub !== '' && isset($cat['subjects'][$sub])) sb_stat($pdo, 'subject', $sub);
    if ($mod !== '' && preg_match('/^[a-z0-9_-]{2,24}$/', $mod)) sb_stat($pdo, 'module', $mod);
    if ($ev === 'prompt' && isset(SB_FREE_LIMITS[isset($in['metric']) ? (string)$in['metric'] : ''])) sb_stat($pdo, 'prompt', (string)$in['metric']);
    if ($ev === 'prompt' && isset($in['metric']) && $in['metric'] === 'chapter') sb_stat($pdo, 'prompt', 'chapter');
    if ($ev === 'checkout') sb_stat($pdo, 'checkout', preg_match('/^[a-z]{3,8}$/', isset($in['plan']) ? (string)$in['plan'] : '') ? (string)$in['plan'] : 'open');
    bill_reply(200, ['ok' => true]);

case 'submit_payment':
    if ($method !== 'POST') bill_fail(405, 'POST required');
    $user = bill_user($pdo, $uid);
    $r = sb_payment_submit($pdo, $user, bill_input());
    if (!$r['ok']) bill_fail($r['code'], $r['error']);
    sb_stat($pdo, 'checkout', 'submitted');
    bill_reply($r['repeat'] ? 200 : 201, ['ok' => true, 'repeat' => $r['repeat'], 'payment' => $r['payment'], 'message' => $r['message']]);

case 'account':
    if ($method !== 'GET') bill_fail(405, 'GET required');
    bill_user($pdo, $uid);
    bill_reply(200, ['ok' => true] + sb_account($pdo, $uid) + ['state' => sb_state($pdo, $uid, $vid)]);

case 'read_notes':
    if ($method !== 'POST') bill_fail(405, 'POST required');
    bill_user($pdo, $uid);
    $pdo->prepare('UPDATE notifications SET read_at = UTC_TIMESTAMP() WHERE user_id = ? AND read_at IS NULL')->execute([$uid]);
    bill_reply(200, ['ok' => true]);

default:
    bill_fail(400, 'Unknown action');
}
