<?php
// Feedback: suggestions, bug reports, textbook mistakes, wrong answers / meanings / translations, with an optional picture. Compatible with PHP 7.4.
// The rules (what is kept, the picture checks, retention) are in api/lib/feedback.php.
//
//   POST api/feedback.php?action=submit    multipart/form-data (a picture can come along) or JSON (no picture)
//          client_id   a UUID made on the device; sending the same one again answers with the first report, it never makes a second
//          kind        suggestion | bug | content | translation | answer
//          message     5 to 2000 characters
//          context     JSON text: cls, subject, subjectName, book, edition, chapter, chapterTitle, page, screen, tab, question, version, app, platform, lang, online
//          image       (multipart only) a JPEG, PNG or WebP of at most 1.5 MB
//                                                          -> 201 {ok:true, id, duplicate:false}   200 {ok:true, id, duplicate:true}
//   GET  api/feedback.php?action=status&ids=<client_id>,<client_id>,...   (30 at most)
//                                                          -> {ok:true, status:{<client_id>: received|seen|fixed|wontfix|duplicate}}   text is never returned
//
// Signed-in students ('Authorization: Bearer <device token>' from the app, or the session cookie on the website) have the report linked to their account;
// anyone else may send too (the report is then anonymous). Errors are {ok:false, error:"text for the student"}; 429 carries Retry-After.

require __DIR__ . '/db.php';
require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/feedback.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

const FB_RATE_USER_HOUR = 20;
const FB_RATE_IP_HOUR   = 8;
const FB_RATE_IP_DAY    = 20;
const FB_RATE_ALL_DAY   = 2000;
const FB_RATE_STATUS    = 120;       // status reads per minute per address

function fb_reply(int $code, array $body, int $retryAfter = 0): void
{
    if ($retryAfter > 0) header('Retry-After: ' . $retryAfter);
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_PARTIAL_OUTPUT_ON_ERROR);
    exit;
}
function fb_fail(int $code, string $msg, int $retryAfter = 0): void { fb_reply($code, ['ok' => false, 'error' => $msg], $retryAfter); }

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    fb_fail(500, 'Database connection failed');
}

$method = $_SERVER['REQUEST_METHOD'];
$action = isset($_GET['action']) ? (string)$_GET['action'] : '';
if ($method !== 'GET' && $method !== 'POST') fb_fail(405, 'GET or POST required');

// ---- who is calling (optional: an unknown token or no sign-in simply means "anonymous")
$uid = 0;
$dev = sb_device_from_request($pdo);
if ($dev) {
    $uid = (int)$dev['user_id'];
} elseif (sb_bearer_token() === '' && isset($_COOKIE['spacebook_sid'])) {
    require __DIR__ . '/session.php';
    if (!empty($_SESSION['uid']) && ($method === 'GET' || sb_request_is_same_site())) {
        $st = $pdo->prepare("SELECT id FROM users WHERE id = ? AND status = 'active'");
        $st->execute([(int)$_SESSION['uid']]);
        $uid = (int)$st->fetchColumn();
    }
}
$ip = sb_client_ip();

if ($action === 'status' && $method === 'GET') {
    $rl = sb_rate_hit($pdo, 'fbr:ip:' . $ip, FB_RATE_STATUS, 60);
    if (!$rl['ok']) fb_fail(429, 'Too many requests. Try again in a moment.', $rl['retry']);
    $ids = isset($_GET['ids']) ? explode(',', substr((string)$_GET['ids'], 0, 1400)) : [];
    fb_reply(200, ['ok' => true, 'status' => (object)sb_fb_status($pdo, $ids)]);
}

if ($action !== 'submit' || $method !== 'POST') fb_fail(400, 'Unknown action');

// ---- read the request: multipart (a picture may come along) or JSON
$in = []; $image = null;
$ctype = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string)$_SERVER['CONTENT_TYPE']) : '';
if (strpos($ctype, 'multipart/form-data') === 0) {
    foreach (['client_id', 'kind', 'message', 'context', 'platform'] as $k) if (isset($_POST[$k]) && is_string($_POST[$k])) $in[$k] = $_POST[$k];
    if (isset($_FILES['image']) && is_array($_FILES['image']) && isset($_FILES['image']['error']) && !is_array($_FILES['image']['error'])) {
        $f = $_FILES['image'];
        if ($f['error'] === UPLOAD_ERR_INI_SIZE || $f['error'] === UPLOAD_ERR_FORM_SIZE) fb_fail(400, 'The picture is too big: 1.5 MB at most.');
        if ($f['error'] === UPLOAD_ERR_OK) {
            if (!is_uploaded_file($f['tmp_name']) || (int)$f['size'] > SB_FB_MAX_IMAGE) fb_fail(400, 'The picture is too big: 1.5 MB at most.');
            $image = (string)file_get_contents($f['tmp_name']);
        } elseif ($f['error'] !== UPLOAD_ERR_NO_FILE) {
            fb_fail(400, 'The picture could not be received. Try again without it, or with a smaller one.');
        }
    }
} else {
    $raw = (string)file_get_contents('php://input', false, null, 0, 30000);
    $data = json_decode($raw, true);
    if (is_array($data)) foreach (['client_id', 'kind', 'message', 'platform'] as $k) if (isset($data[$k]) && is_string($data[$k])) $in[$k] = $data[$k];
    if (is_array($data) && isset($data['context'])) $in['context'] = $data['context'];
}

// a retry of a report that is already stored is answered before any limit is counted
$cid = isset($in['client_id']) ? strtolower($in['client_id']) : '';
if (sb_fb_uuid_ok($cid) && sb_fb_status($pdo, [$cid])) {
    $r = sb_fb_create($pdo, $uid ?: null, $in, null);
    fb_reply(200, ['ok' => true, 'id' => $r['id'], 'duplicate' => true]);
}

// ---- limits: per student, per address, and one for the whole service so that nobody can fill the database
$buckets = $uid ? [['fbs:u:' . $uid, FB_RATE_USER_HOUR, 3600]] : [['fbs:ip:' . $ip, FB_RATE_IP_HOUR, 3600], ['fbs:ipd:' . $ip, FB_RATE_IP_DAY, 86400]];
$buckets[] = ['fbs:all', FB_RATE_ALL_DAY, 86400];
foreach ($buckets as $b) {
    $rl = sb_rate_hit($pdo, $b[0], $b[1], $b[2]);
    if (!$rl['ok']) fb_fail(429, 'You have sent a lot of reports. Please try again later.', $rl['retry']);
}

try {
    $r = sb_fb_create($pdo, $uid ?: null, $in, $image);
} catch (Throwable $e) {
    error_log('SpaceBook feedback: ' . $e->getMessage());
    fb_fail(500, 'Your report could not be saved. Please try again later.');
}
if (!$r['ok']) fb_fail((int)$r['code'], $r['error']);
fb_reply($r['duplicate'] ? 200 : 201, ['ok' => true, 'id' => $r['id'], 'duplicate' => $r['duplicate']]);
