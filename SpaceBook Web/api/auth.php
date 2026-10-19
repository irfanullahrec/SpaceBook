<?php
// Account API.
//   POST api/auth.php?action=register  {name, father_name, user_type, whatsapp, password}
//   POST api/auth.php?action=login     {whatsapp, password}
//   POST api/auth.php?action=logout
//   GET  api/auth.php?action=me
// Responses are JSON: {ok:true, user:{...}} or {ok:false, error:"..."}.

require __DIR__ . '/db.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

require __DIR__ . '/session.php';
require __DIR__ . '/lib/security.php';

const USER_TYPES   = ['school', 'teacher', 'student'];
const MAX_FAILS    = 5;   // per number, per window
const FAIL_WINDOW  = 15;  // minutes
const MAX_FAILS_IP = 20;  // failed logins per address in the window (higher: a school shares one address)
const MAX_REGISTER = 10;  // new accounts per address per hour

// a valid-looking hash, verified against when the number is unknown, so unknown and known numbers take equally long
const DUMMY_HASH   = '$2y$10$uJ.pH2MUDX6ZsZaX9E./M.485elKQnxIArOQeD1GqPfOjXxFT0S2O';

function reply(int $code, array $body): void
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function fail(int $code, string $msg, int $retryAfter = 0): void
{
    if ($retryAfter > 0) header('Retry-After: ' . $retryAfter);
    reply($code, ['ok' => false, 'error' => $msg]);
}

function input(): array
{
    $raw = file_get_contents('php://input');
    $data = json_decode($raw ?: '', true);
    return is_array($data) ? $data : $_POST;
}

// Accepts 03001234567, +92 300 1234567, 0092..., 923001234567 → 923001234567.
// Other international numbers are kept as their digits.
function normalize_whatsapp(string $raw): ?string
{
    $d = preg_replace('/\D+/', '', $raw);
    if (strpos($d, '00') === 0) $d = substr($d, 2);
    if (preg_match('/^03\d{9}$/', $d)) $d = '92' . substr($d, 1);
    elseif (preg_match('/^3\d{9}$/', $d)) $d = '92' . $d;
    return preg_match('/^\d{10,15}$/', $d) ? $d : null;
}

function clean_name($v): string
{
    return trim(preg_replace('/\s+/u', ' ', (string)$v));
}

function public_user(array $u): array
{
    return [
        'id'          => (int)$u['id'],
        'name'        => $u['name'],
        'father_name' => $u['father_name'],
        'user_type'   => $u['user_type'],
        'whatsapp'    => $u['whatsapp'],
        'created_at'  => $u['created_at'],
    ];
}

function start_user_session(array $u): void
{
    session_regenerate_id(true);
    $_SESSION['uid'] = (int)$u['id'];
}

function client_ip(): string
{
    return sb_client_ip();
}

// a device token for sync, only for clients that ask for one (want_device)
function maybe_device(PDO $pdo, array $user, array $in): array
{
    if (empty($in['want_device'])) return [];
    return ['device' => sb_device_issue($pdo, (int)$user['id'], (string)($in['device_name'] ?? ''))];
}

$action = $_GET['action'] ?? '';
$method = $_SERVER['REQUEST_METHOD'];

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    fail(500, 'Database connection failed');
}

switch ($action) {

case 'register':
    if ($method !== 'POST') fail(405, 'POST required');
    if (!sb_request_is_same_site()) fail(403, 'Request not allowed');
    $rl = sb_rate_hit($pdo, 'reg:ip:' . client_ip(), MAX_REGISTER, 3600);
    if (!$rl['ok']) fail(429, 'Too many new accounts from this connection. Try again later', $rl['retry']);
    $in = input();
    $name     = clean_name($in['name'] ?? '');
    $father   = clean_name($in['father_name'] ?? '');
    $type     = strtolower(trim((string)($in['user_type'] ?? '')));
    $whatsapp = normalize_whatsapp((string)($in['whatsapp'] ?? ''));
    $password = (string)($in['password'] ?? '');

    if (mb_strlen($name) < 2 || mb_strlen($name) > 100)     fail(422, 'Please enter your name');
    if (mb_strlen($father) < 2 || mb_strlen($father) > 100) fail(422, 'Please enter father name');
    if (!in_array($type, USER_TYPES, true))                 fail(422, 'Choose School, Teacher or Student');
    if (!$whatsapp)                                         fail(422, 'Enter a valid WhatsApp number');
    if (strlen($password) < 6)                              fail(422, 'Password must be at least 6 characters');

    $st = $pdo->prepare('SELECT id FROM users WHERE whatsapp = ?');
    $st->execute([$whatsapp]);
    if ($st->fetch()) fail(409, 'An account with this WhatsApp number already exists');

    $st = $pdo->prepare('INSERT INTO users (name, father_name, user_type, whatsapp, password_hash, last_login_at)
                         VALUES (?, ?, ?, ?, ?, NOW())');
    $st->execute([$name, $father, $type, $whatsapp, password_hash($password, PASSWORD_DEFAULT)]);

    $st = $pdo->prepare('SELECT * FROM users WHERE id = ?');
    $st->execute([$pdo->lastInsertId()]);
    $user = $st->fetch();
    start_user_session($user);
    sb_audit($pdo, (int)$user['id'], 'register');
    reply(201, ['ok' => true, 'user' => public_user($user)] + maybe_device($pdo, $user, $in));

case 'login':
    if ($method !== 'POST') fail(405, 'POST required');
    if (!sb_request_is_same_site()) fail(403, 'Request not allowed');
    $in = input();
    $whatsapp = normalize_whatsapp((string)($in['whatsapp'] ?? ''));
    $password = (string)($in['password'] ?? '');
    if (!$whatsapp || $password === '') fail(422, 'Enter WhatsApp number and password');

    $st = $pdo->prepare('SELECT COUNT(*) FROM login_attempts
                         WHERE whatsapp = ? AND success = 0
                           AND attempted_at > NOW() - INTERVAL ' . FAIL_WINDOW . ' MINUTE');
    $st->execute([$whatsapp]);
    if ((int)$st->fetchColumn() >= MAX_FAILS) {
        fail(429, 'Too many failed attempts. Try again in ' . FAIL_WINDOW . ' minutes', FAIL_WINDOW * 60);
    }
    // the same ceiling per address, so rotating through numbers from one connection does not help
    $st = $pdo->prepare('SELECT COUNT(*) FROM login_attempts
                         WHERE ip = ? AND success = 0 AND attempted_at > NOW() - INTERVAL ' . FAIL_WINDOW . ' MINUTE');
    $st->execute([client_ip()]);
    if ((int)$st->fetchColumn() >= MAX_FAILS_IP) {
        fail(429, 'Too many failed attempts. Try again in ' . FAIL_WINDOW . ' minutes', FAIL_WINDOW * 60);
    }
    if (mt_rand(1, 100) === 1) {      // housekeeping: login_attempts used to grow forever
        $pdo->exec('DELETE FROM login_attempts WHERE attempted_at < NOW() - INTERVAL 30 DAY');
    }

    $st = $pdo->prepare('SELECT * FROM users WHERE whatsapp = ?');
    $st->execute([$whatsapp]);
    $user = $st->fetch();
    $good = $user ? password_verify($password, $user['password_hash']) : (password_verify($password, DUMMY_HASH) && false);

    $pdo->prepare('INSERT INTO login_attempts (whatsapp, ip, success) VALUES (?, ?, ?)')
        ->execute([$whatsapp, client_ip(), $good ? 1 : 0]);

    if (!$good) fail(401, 'Wrong WhatsApp number or password');
    if ($user['status'] !== 'active') fail(403, 'This account is blocked');

    if (password_needs_rehash($user['password_hash'], PASSWORD_DEFAULT)) {
        $pdo->prepare('UPDATE users SET password_hash = ? WHERE id = ?')
            ->execute([password_hash($password, PASSWORD_DEFAULT), $user['id']]);
    }
    $pdo->prepare('UPDATE users SET last_login_at = NOW() WHERE id = ?')->execute([$user['id']]);
    start_user_session($user);
    sb_audit($pdo, (int)$user['id'], 'login');
    reply(200, ['ok' => true, 'user' => public_user($user)] + maybe_device($pdo, $user, $in));

case 'logout':
    if ($method !== 'POST') fail(405, 'POST required');
    if (!sb_request_is_same_site()) fail(403, 'Request not allowed');
    $dev = sb_device_from_request($pdo);               // a device token in the request ends that device's sync access
    if ($dev) { sb_device_revoke($pdo, $dev['device_id'], $dev['user_id']); sb_audit($pdo, $dev['user_id'], 'device_revoke'); }
    if (!empty($_SESSION['uid'])) sb_audit($pdo, (int)$_SESSION['uid'], 'logout');
    $_SESSION = [];
    session_destroy();
    setcookie(session_name(), '', ['expires' => time() - 3600, 'path' => '/']);
    reply(200, ['ok' => true]);

case 'me':
    if (empty($_SESSION['uid'])) reply(200, ['ok' => true, 'user' => null]);
    $st = $pdo->prepare("SELECT * FROM users WHERE id = ? AND status = 'active'");
    $st->execute([$_SESSION['uid']]);
    $user = $st->fetch();
    reply(200, ['ok' => true, 'user' => $user ? public_user($user) : null]);

default:
    fail(400, 'Unknown action');
}
