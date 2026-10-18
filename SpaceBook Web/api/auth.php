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

const USER_TYPES   = ['school', 'teacher', 'student'];
const MAX_FAILS    = 5;   // per number, per window
const FAIL_WINDOW  = 15;  // minutes

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
    return substr($_SERVER['REMOTE_ADDR'] ?? '', 0, 45);
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
    reply(201, ['ok' => true, 'user' => public_user($user)]);

case 'login':
    if ($method !== 'POST') fail(405, 'POST required');
    $in = input();
    $whatsapp = normalize_whatsapp((string)($in['whatsapp'] ?? ''));
    $password = (string)($in['password'] ?? '');
    if (!$whatsapp || $password === '') fail(422, 'Enter WhatsApp number and password');

    $st = $pdo->prepare('SELECT COUNT(*) FROM login_attempts
                         WHERE whatsapp = ? AND success = 0
                           AND attempted_at > NOW() - INTERVAL ' . FAIL_WINDOW . ' MINUTE');
    $st->execute([$whatsapp]);
    if ((int)$st->fetchColumn() >= MAX_FAILS) {
        fail(429, 'Too many failed attempts. Try again in ' . FAIL_WINDOW . ' minutes');
    }

    $st = $pdo->prepare('SELECT * FROM users WHERE whatsapp = ?');
    $st->execute([$whatsapp]);
    $user = $st->fetch();
    $good = $user && password_verify($password, $user['password_hash']);

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
    reply(200, ['ok' => true, 'user' => public_user($user)]);

case 'logout':
    if ($method !== 'POST') fail(405, 'POST required');
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
