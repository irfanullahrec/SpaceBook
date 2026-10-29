<?php
// The management page's logic (manage/index.php): administrator sign-in and sessions, the dashboard numbers, lists and exports.
// These administrators live in their own table (admins), apart from the users of the site: nothing the public site does can sign one in
// or make one. Compatible with PHP 7.4. Not reachable over HTTP by itself (api/lib is denied).
//
// Metric definitions (also printed on the dashboard):
//  * Registered account       a users row that is not deleted. New registrations: created in the chosen dates.
//  * Active / expired / suspended subscription   active: not suspended and not past its end. expired: not suspended, past its end. suspended: stopped by an administrator.
//  * Verified revenue         the amount of payments an administrator APPROVED, counted on the day of approval (not the day of submission).
//  * Activity (a "hit")       one tracked action sent by the website or the app: a question answered in a limited module, a chapter or tool opened.
//  * Daily / weekly / monthly active users   distinct registered people with at least one hit on that day / in the 7 / 30 days ending on the last chosen date.
//    Administrators (admins table, or users.role admin) and known bots (crawler or empty browser name) are not counted.
//  * Anonymous visitors       distinct browsers or phones with hits that never signed in. An ESTIMATE: clearing the browser's data or using two
//    devices makes one person count twice.
//  * Registration-to-purchase conversion   registered accounts created in the chosen dates that have at least one approved payment, over all created in them.

require_once __DIR__ . '/security.php';
require_once __DIR__ . '/billing.php';

const SB_M_IDLE_SECONDS = 1800;      // sign out after 30 idle minutes
const SB_M_MAX_SECONDS  = 43200;     // and after 12 hours whatever happens

function sb_m_h($s): string
{
    return htmlspecialchars((string)$s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function sb_m_session(): void
{
    if (session_status() === PHP_SESSION_ACTIVE) return;
    $dir = sys_get_temp_dir() . DIRECTORY_SEPARATOR . 'spacebook_admin_sessions';
    if (!is_dir($dir)) @mkdir($dir, 0700, true);
    if (is_dir($dir) && is_writable($dir)) session_save_path($dir);
    ini_set('session.use_strict_mode', '1');
    ini_set('session.gc_maxlifetime', (string)SB_M_MAX_SECONDS);
    $path = rtrim(str_replace('\\', '/', dirname(isset($_SERVER['SCRIPT_NAME']) ? $_SERVER['SCRIPT_NAME'] : '/manage/index.php')), '/');
    session_name('spacebook_admin');
    session_set_cookie_params(['lifetime' => 0, 'path' => $path === '' ? '/' : $path, 'httponly' => true, 'samesite' => 'Strict',
        'secure' => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off']);
    session_start();
}

function sb_m_csrf(): string
{
    if (empty($_SESSION['m_csrf']) || !is_string($_SESSION['m_csrf'])) $_SESSION['m_csrf'] = bin2hex(random_bytes(20));
    return $_SESSION['m_csrf'];
}

function sb_m_csrf_ok($t): bool
{
    return is_string($t) && !empty($_SESSION['m_csrf']) && hash_equals($_SESSION['m_csrf'], $t);
}

// The signed-in administrator or null. Re-reads the row on every request; enforces the idle and absolute limits.
function sb_m_current(PDO $pdo): ?array
{
    if (empty($_SESSION['m_admin'])) return null;
    $now = time();
    if ($now - (int)($_SESSION['m_last'] ?? 0) > SB_M_IDLE_SECONDS || $now - (int)($_SESSION['m_start'] ?? 0) > SB_M_MAX_SECONDS) { sb_m_logout(); return null; }
    $st = $pdo->prepare("SELECT id, username, must_change_password FROM admins WHERE id = ? AND status = 'active'");
    $st->execute([(int)$_SESSION['m_admin']]);
    $a = $st->fetch();
    if (!$a) { sb_m_logout(); return null; }
    $_SESSION['m_last'] = $now;
    return ['id' => (int)$a['id'], 'username' => $a['username'], 'must_change' => (int)$a['must_change_password'] === 1];
}

function sb_m_logout(): void
{
    $_SESSION = [];
    if (session_status() === PHP_SESSION_ACTIVE) session_regenerate_id(true);
}

function sb_m_dummy_hash(): string
{
    static $h = null;
    if ($h === null) $h = password_hash('sb-no-such-admin', PASSWORD_BCRYPT, ['cost' => 12]);
    return $h;
}

// Five wrong passwords for a name lock that name for 15 minutes; 30 attempts from one address in 15 minutes stop that address.
// The answer never says whether the name exists.
function sb_m_login(PDO $pdo, string $username, string $password): array
{
    $username = trim(mb_substr($username, 0, 40));
    $rl = sb_rate_hit($pdo, 'mlogin:ip:' . sb_client_ip(), 30, 900);
    $none = ['name' => '', 'id' => null, 'username' => $username === '' ? '?' : $username];
    if (!$rl['ok']) return ['ok' => false, 'code' => 429, 'error' => 'Too many attempts. Wait a few minutes and try again', 'retry' => $rl['retry']];
    $st = $pdo->prepare('SELECT * FROM admins WHERE username = ?');
    $st->execute([$username]);
    $a = $st->fetch();
    $now = sb_now();
    if ($a && $a['locked_until'] !== null && strtotime($a['locked_until'] . ' UTC') > strtotime($now . ' UTC')) {
        sb_admin_audit_write($pdo, ['id' => (int)$a['id'], 'username' => $a['username']], 'login_locked', 'admin', $a['id'], '', []);
        return ['ok' => false, 'code' => 429, 'error' => 'This account is locked for a few minutes after too many wrong passwords'];
    }
    $good = password_verify($password, $a ? $a['password_hash'] : sb_m_dummy_hash()) && $a && $a['status'] === 'active';
    if (!$good) {
        if ($a) {
            $fails = (int)$a['failed_logins'] + 1;
            if ($fails >= 5) $pdo->prepare('UPDATE admins SET failed_logins = 0, locked_until = ? WHERE id = ?')->execute([gmdate('Y-m-d H:i:s', strtotime($now . ' UTC') + 900), $a['id']]);
            else $pdo->prepare('UPDATE admins SET failed_logins = ? WHERE id = ?')->execute([$fails, $a['id']]);
        }
        sb_admin_audit_write($pdo, $a ? ['id' => (int)$a['id'], 'username' => $a['username']] : $none, 'login_fail', 'admin', $a ? $a['id'] : '', '', []);
        return ['ok' => false, 'code' => 401, 'error' => 'Wrong username or password'];
    }
    $pdo->prepare('UPDATE admins SET failed_logins = 0, locked_until = NULL, last_login_at = ? WHERE id = ?')->execute([$now, $a['id']]);
    session_regenerate_id(true);
    $_SESSION['m_admin'] = (int)$a['id'];
    $_SESSION['m_start'] = $_SESSION['m_last'] = time();
    unset($_SESSION['m_csrf']);
    sb_admin_audit_write($pdo, ['id' => (int)$a['id'], 'username' => $a['username']], 'login_ok', 'admin', $a['id'], '', []);
    return ['ok' => true, 'must_change' => (int)$a['must_change_password'] === 1];
}

function sb_m_password_problem(string $new, string $current, string $username): string
{
    if (strlen($new) < 12) return 'The new password needs at least 12 characters';
    if (!preg_match('/[A-Za-z]/', $new) || !preg_match('/\d/', $new)) return 'Use both letters and numbers';
    if (strcasecmp($new, $username) === 0 || stripos($new, $username) !== false) return 'The password must not contain your username';
    if ($new === $current) return 'Choose a different password';
    return '';
}

function sb_m_change_password(PDO $pdo, array $admin, string $current, string $new, string $again): array
{
    $rl = sb_rate_hit($pdo, 'mpw:a:' . $admin['id'], 10, 3600);
    if (!$rl['ok']) return ['ok' => false, 'error' => 'Too many attempts. Try again later'];
    $st = $pdo->prepare('SELECT password_hash FROM admins WHERE id = ?');
    $st->execute([$admin['id']]);
    $hash = $st->fetchColumn();
    if (!$hash || !password_verify($current, $hash)) return ['ok' => false, 'error' => 'The current password is not right'];
    if ($new !== $again) return ['ok' => false, 'error' => 'The two new passwords are different'];
    $p = sb_m_password_problem($new, $current, $admin['username']);
    if ($p !== '') return ['ok' => false, 'error' => $p];
    $pdo->prepare('UPDATE admins SET password_hash = ?, must_change_password = 0, password_changed_at = ? WHERE id = ?')
        ->execute([password_hash($new, PASSWORD_BCRYPT, ['cost' => 12]), sb_now(), $admin['id']]);
    session_regenerate_id(true);
    sb_admin_audit_write($pdo, $admin, 'password_change', 'admin', $admin['id'], '', []);
    return ['ok' => true];
}

// Command line only (php api/migrate.php admin-reset <username>): a new random temporary password, printed once; it must be changed at the next sign-in.
function sb_m_reset_password(PDO $pdo, string $username): ?string
{
    $st = $pdo->prepare('SELECT id, username FROM admins WHERE username = ?');
    $st->execute([$username]);
    $a = $st->fetch();
    if (!$a) return null;
    $pw = substr(strtr(base64_encode(random_bytes(12)), '+/=', 'xyz'), 0, 16) . 'Q9a';
    $pdo->prepare("UPDATE admins SET password_hash = ?, must_change_password = 1, failed_logins = 0, locked_until = NULL, status = 'active' WHERE id = ?")
        ->execute([password_hash($pw, PASSWORD_BCRYPT, ['cost' => 12]), $a['id']]);
    sb_admin_audit_write($pdo, ['id' => (int)$a['id'], 'username' => $a['username']], 'password_reset', 'admin', $a['id'], 'command line', []);
    return $pw;
}

// ---------------------------------------------------------------- dates

function sb_m_date($v, string $default): string
{
    $v = is_string($v) ? trim($v) : '';
    $d = DateTimeImmutable::createFromFormat('!Y-m-d', $v, new DateTimeZone('UTC'));
    return ($d && $d->format('Y-m-d') === $v) ? $v : $default;
}

// [from, to] inclusive 'Y-m-d'; default the last 30 days
function sb_m_range($from, $to): array
{
    $today = substr(sb_now(), 0, 10);
    $to = sb_m_date($to, $today);
    $from = sb_m_date($from, gmdate('Y-m-d', strtotime($to . ' UTC') - 29 * 86400));
    if ($from > $to) { $t = $from; $from = $to; $to = $t; }
    return [$from, $to];
}

function sb_m_next_day(string $d): string
{
    return gmdate('Y-m-d', strtotime($d . ' UTC') + 86400);
}

function sb_m_days(string $from, string $to): array
{
    $out = [];
    for ($t = strtotime($from . ' UTC'), $end = strtotime($to . ' UTC'); $t <= $end && count($out) < 400; $t += 86400) $out[] = gmdate('Y-m-d', $t);
    return $out;
}

// ---------------------------------------------------------------- the dashboard

function sb_m_series(PDO $pdo, string $sql, array $args, array $days): array
{
    $st = $pdo->prepare($sql);
    $st->execute($args);
    $by = [];
    foreach ($st->fetchAll(PDO::FETCH_NUM) as $r) $by[$r[0]] = (float)$r[1];
    $out = [];
    foreach ($days as $d) $out[] = isset($by[$d]) ? $by[$d] : 0;
    return $out;
}

function sb_m_one(PDO $pdo, string $sql, array $args = [])
{
    $st = $pdo->prepare($sql);
    $st->execute($args);
    return $st->fetchColumn();
}

function sb_m_pairs(PDO $pdo, string $sql, array $args = []): array
{
    $st = $pdo->prepare($sql);
    $st->execute($args);
    return $st->fetchAll(PDO::FETCH_NUM);
}

function sb_m_dashboard(PDO $pdo, string $from, string $to): array
{
    $end = sb_m_next_day($to);
    $days = sb_m_days($from, $to);
    $now = sb_now();
    $nonAdmin = "u.role <> 'admin' AND u.status <> 'deleted'";
    $d = ['from' => $from, 'to' => $to, 'days' => $days];

    // accounts
    $d['accounts'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users WHERE status <> 'deleted' AND role <> 'admin'");
    $d['newAccounts'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users WHERE status <> 'deleted' AND role <> 'admin' AND created_at >= ? AND created_at < ?", [$from . ' 00:00:00', $end . ' 00:00:00']);
    $d['newByDay'] = sb_m_series($pdo, "SELECT DATE(created_at), COUNT(*) FROM users WHERE status <> 'deleted' AND role <> 'admin' AND created_at >= ? AND created_at < ? GROUP BY DATE(created_at)", [$from . ' 00:00:00', $end . ' 00:00:00'], $days);
    $d['signupPlatform'] = sb_m_pairs($pdo, "SELECT signup_platform, COUNT(*) FROM users WHERE status <> 'deleted' AND role <> 'admin' AND created_at >= ? AND created_at < ? GROUP BY signup_platform", [$from . ' 00:00:00', $end . ' 00:00:00']);
    $d['suspendedAccounts'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users WHERE status = 'blocked' AND role <> 'admin'");

    // subscriptions (now)
    $d['subActive'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscriptions WHERE status = 'active' AND expires_at > ?", [$now]);
    $d['subExpired'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscriptions WHERE status = 'active' AND expires_at <= ?", [$now]);
    $d['subSuspended'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscriptions WHERE status = 'suspended'");
    $d['subByPlan'] = sb_m_pairs($pdo, "SELECT plan_type, COUNT(*) FROM subscriptions WHERE status = 'active' AND expires_at > ? GROUP BY plan_type", [$now]);
    $d['expiringSoon'] = sb_m_pairs($pdo, "SELECT s.id, u.name, s.plan_type, s.expires_at FROM subscriptions s JOIN users u ON u.id = s.user_id WHERE s.status = 'active' AND s.expires_at > ? AND s.expires_at <= ? ORDER BY s.expires_at LIMIT 20", [$now, gmdate('Y-m-d H:i:s', strtotime($now . ' UTC') + 7 * 86400)]);
    $d['expiringSoonCount'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscriptions WHERE status = 'active' AND expires_at > ? AND expires_at <= ?", [$now, gmdate('Y-m-d H:i:s', strtotime($now . ' UTC') + 7 * 86400)]);
    $d['renewals'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscription_events WHERE event = 'renewed' AND created_at >= ? AND created_at < ?", [$from . ' 00:00:00', $end . ' 00:00:00']);

    // payments
    $d['payStatus'] = ['pending' => 0, 'approved' => 0, 'rejected' => 0];
    foreach (sb_m_pairs($pdo, "SELECT status, COUNT(*) FROM payment_requests WHERE submitted_at >= ? AND submitted_at < ? GROUP BY status", [$from . ' 00:00:00', $end . ' 00:00:00']) as $r) $d['payStatus'][$r[0]] = (int)$r[1];
    $d['pendingNow'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM payment_requests WHERE status = 'pending'");
    $d['revenue'] = (int)sb_m_one($pdo, "SELECT COALESCE(SUM(amount_pkr), 0) FROM payment_requests WHERE status = 'approved' AND reviewed_at >= ? AND reviewed_at < ?", [$from . ' 00:00:00', $end . ' 00:00:00']);
    $d['revenueByDay'] = sb_m_series($pdo, "SELECT DATE(reviewed_at), SUM(amount_pkr) FROM payment_requests WHERE status = 'approved' AND reviewed_at >= ? AND reviewed_at < ? GROUP BY DATE(reviewed_at)", [$from . ' 00:00:00', $end . ' 00:00:00'], $days);
    $d['revenueByMonth'] = sb_m_pairs($pdo, "SELECT DATE_FORMAT(reviewed_at, '%Y-%m'), SUM(amount_pkr) FROM payment_requests WHERE status = 'approved' AND reviewed_at >= ? AND reviewed_at < ? GROUP BY DATE_FORMAT(reviewed_at, '%Y-%m') ORDER BY 1", [$from . ' 00:00:00', $end . ' 00:00:00']);
    $d['revenueByPlan'] = sb_m_pairs($pdo, "SELECT plan_type, SUM(amount_pkr) FROM payment_requests WHERE status = 'approved' AND reviewed_at >= ? AND reviewed_at < ? GROUP BY plan_type", [$from . ' 00:00:00', $end . ' 00:00:00']);

    // activity
    $act = "FROM activity_days a JOIN users u ON u.id = CAST(SUBSTRING(a.owner_key, 3) AS UNSIGNED) WHERE a.owner_key LIKE 'u:%' AND $nonAdmin";
    $d['dauSeries'] = sb_m_series($pdo, "SELECT a.day, COUNT(DISTINCT a.owner_key) $act AND a.day >= ? AND a.day <= ? GROUP BY a.day", [$from, $to], $days);
    $cnt = function (string $f, string $t) use ($pdo, $act) { return (int)sb_m_one($pdo, "SELECT COUNT(DISTINCT a.owner_key) $act AND a.day >= ? AND a.day <= ?", [$f, $t]); };
    $d['dau'] = $cnt($to, $to);
    $d['wau'] = $cnt(gmdate('Y-m-d', strtotime($to . ' UTC') - 6 * 86400), $to);
    $d['mau'] = $cnt(gmdate('Y-m-d', strtotime($to . ' UTC') - 29 * 86400), $to);
    $d['activeInRange'] = $cnt($from, $to);
    $d['activeByPlatform'] = sb_m_pairs($pdo, "SELECT a.platform, COUNT(DISTINCT a.owner_key) $act AND a.day >= ? AND a.day <= ? GROUP BY a.platform", [$from, $to]);
    $d['topUsers'] = sb_m_pairs($pdo, "SELECT u.id, u.name, SUM(a.hits) AS h, COUNT(DISTINCT a.day) AS dd $act AND a.day >= ? AND a.day <= ? GROUP BY u.id, u.name ORDER BY h DESC, u.id LIMIT 10", [$from, $to]);
    $anon = "FROM activity_days a LEFT JOIN visitors v ON v.id = SUBSTRING(a.owner_key, 3) WHERE a.owner_key LIKE 'v:%' AND (v.id IS NULL OR (v.user_id IS NULL AND v.is_bot = 0)) AND a.day >= ? AND a.day <= ?";
    $d['anonVisitors'] = (int)sb_m_one($pdo, "SELECT COUNT(DISTINCT a.owner_key) $anon", [$from, $to]);
    $d['anonByPlatform'] = sb_m_pairs($pdo, "SELECT a.platform, COUNT(DISTINCT a.owner_key) $anon GROUP BY a.platform", [$from, $to]);
    $d['anonSeries'] = sb_m_series($pdo, "SELECT a.day, COUNT(DISTINCT a.owner_key) $anon GROUP BY a.day", [$from, $to], $days);

    // popularity and the free limits
    foreach (['class', 'subject', 'module'] as $k) {
        $d['top_' . $k] = sb_m_pairs($pdo, "SELECT skey, SUM(hits) h FROM usage_stats WHERE kind = ? AND day >= ? AND day <= ? GROUP BY skey ORDER BY h DESC, skey LIMIT 10", [$k, $from, $to]);
    }
    $d['limitHits'] = sb_m_pairs($pdo, "SELECT skey, SUM(hits) FROM usage_stats WHERE kind = 'limit' AND day >= ? AND day <= ? GROUP BY skey", [$from, $to]);
    $d['prompts'] = sb_m_pairs($pdo, "SELECT skey, SUM(hits) FROM usage_stats WHERE kind = 'prompt' AND day >= ? AND day <= ? GROUP BY skey", [$from, $to]);
    $d['checkout'] = sb_m_pairs($pdo, "SELECT skey, SUM(hits) FROM usage_stats WHERE kind = 'checkout' AND day >= ? AND day <= ? GROUP BY skey", [$from, $to]);
    $atLimit = [];
    foreach (SB_FREE_LIMITS as $m => $lim) {
        $atLimit[$m] = (int)sb_m_one($pdo, 'SELECT COUNT(*) FROM (SELECT owner_key FROM free_usage WHERE metric = ? AND created_at >= ? AND created_at < ? GROUP BY owner_key HAVING COUNT(*) >= ?) t', [$m, $from . ' 00:00:00', $end . ' 00:00:00', $lim]);
    }
    $d['atLimit'] = $atLimit;

    // conversion
    $d['convBase'] = $d['newAccounts'];
    $d['convPaid'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users u WHERE $nonAdmin AND u.created_at >= ? AND u.created_at < ? AND EXISTS (SELECT 1 FROM payment_requests p WHERE p.user_id = u.id AND p.status = 'approved')", [$from . ' 00:00:00', $end . ' 00:00:00']);
    $d['convSubmitted'] = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users u WHERE $nonAdmin AND u.created_at >= ? AND u.created_at < ? AND EXISTS (SELECT 1 FROM payment_requests p WHERE p.user_id = u.id)", [$from . ' 00:00:00', $end . ' 00:00:00']);
    return $d;
}

// ---------------------------------------------------------------- lists

function sb_m_like(string $s): string
{
    return '%' . str_replace(['\\', '%', '_'], ['\\\\', '\\%', '\\_'], $s) . '%';
}

function sb_m_digits(string $q): string
{
    $digits = preg_replace('/\D+/', '', $q);
    if (strpos($digits, '00') === 0) $digits = substr($digits, 2);
    if (preg_match('/^0\d/', $digits)) $digits = '92' . substr($digits, 1);
    return $digits;
}

// A page of payments. Filters: q (TID, reference, name, number), status, plan, from, to (submission dates).
function sb_m_payments(PDO $pdo, array $f, int $page, int $per = 50): array
{
    $where = []; $args = [];
    $q = trim(mb_substr((string)($f['q'] ?? ''), 0, 60));
    if ($q !== '') {
        $digits = sb_m_digits($q);
        $or = ['p.trx_norm LIKE ?', 'p.ref LIKE ?', 'p.contact_name LIKE ?'];
        $args[] = sb_m_like(strtoupper($q)); $args[] = sb_m_like(strtoupper($q)); $args[] = sb_m_like($q);
        if (strlen($digits) >= 4) { $or[] = 'p.contact_whatsapp LIKE ?'; $args[] = '%' . $digits . '%'; }
        if (ctype_digit($q)) { $or[] = 'p.user_id = ?'; $args[] = (int)$q; }
        $where[] = '(' . implode(' OR ', $or) . ')';
    }
    if (in_array($f['status'] ?? '', ['pending', 'approved', 'rejected'], true)) { $where[] = 'p.status = ?'; $args[] = $f['status']; }
    if (in_array($f['plan'] ?? '', ['student', 'teacher', 'prep'], true)) { $where[] = 'p.plan_type = ?'; $args[] = $f['plan']; }
    if (!empty($f['from'])) { $where[] = 'p.submitted_at >= ?'; $args[] = sb_m_date($f['from'], '1970-01-01') . ' 00:00:00'; }
    if (!empty($f['to'])) { $where[] = 'p.submitted_at < ?'; $args[] = sb_m_next_day(sb_m_date($f['to'], '2999-12-31')) . ' 00:00:00'; }
    $w = $where ? ' WHERE ' . implode(' AND ', $where) : '';
    $total = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM payment_requests p$w", $args);
    $pages = max(1, (int)ceil($total / $per));
    $page = min(max(1, $page), $pages);
    $st = $pdo->prepare("SELECT p.* FROM payment_requests p$w ORDER BY (p.status = 'pending') DESC, p.id DESC LIMIT " . (int)$per . ' OFFSET ' . (int)(($page - 1) * $per));
    $st->execute($args);
    return ['rows' => $st->fetchAll(), 'total' => $total, 'pages' => $pages, 'page' => $page];
}

function sb_m_users(PDO $pdo, array $f, int $page, int $per = 50): array
{
    $where = ["u.status <> 'deleted'", "u.role <> 'admin'"]; $args = [];
    $q = trim(mb_substr((string)($f['q'] ?? ''), 0, 60));
    if ($q !== '') {
        $digits = sb_m_digits($q);
        if (ctype_digit($q) && strlen($q) <= 8) { $where[] = 'u.id = ?'; $args[] = (int)$q; }
        elseif (strlen($digits) >= 5 && strlen($digits) >= strlen($q) - 4) { $where[] = 'u.whatsapp LIKE ?'; $args[] = $digits . '%'; }
        else { $where[] = '(u.name LIKE ? OR u.father_name LIKE ?)'; $args[] = sb_m_like($q); $args[] = sb_m_like($q); }
    }
    if (in_array($f['status'] ?? '', ['active', 'blocked'], true)) { $where[] = 'u.status = ?'; $args[] = $f['status']; }
    if (in_array($f['platform'] ?? '', ['web', 'app'], true)) { $where[] = 'u.signup_platform = ?'; $args[] = $f['platform']; }
    $now = sb_now();
    $sub = (string)($f['sub'] ?? '');
    if ($sub === 'active')    { $where[] = "EXISTS (SELECT 1 FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'active' AND s.expires_at > ?)"; $args[] = $now; }
    if ($sub === 'expired')   { $where[] = "EXISTS (SELECT 1 FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'active' AND s.expires_at <= ?) AND NOT EXISTS (SELECT 1 FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'active' AND s.expires_at > ?)"; $args[] = $now; $args[] = $now; }
    if ($sub === 'suspended') { $where[] = "EXISTS (SELECT 1 FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'suspended')"; }
    if ($sub === 'none')      { $where[] = 'NOT EXISTS (SELECT 1 FROM subscriptions s WHERE s.user_id = u.id)'; }
    if (!empty($f['from'])) { $where[] = 'u.created_at >= ?'; $args[] = sb_m_date($f['from'], '1970-01-01') . ' 00:00:00'; }
    if (!empty($f['to'])) { $where[] = 'u.created_at < ?'; $args[] = sb_m_next_day(sb_m_date($f['to'], '2999-12-31')) . ' 00:00:00'; }
    $w = ' WHERE ' . implode(' AND ', $where);
    $total = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM users u$w", $args);
    $pages = max(1, (int)ceil($total / $per));
    $page = min(max(1, $page), $pages);
    $st = $pdo->prepare("SELECT u.id, u.name, u.father_name, u.whatsapp, u.status, u.signup_platform, u.created_at, u.last_login_at,
                                (SELECT COUNT(*) FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'active' AND s.expires_at > ?) AS subs_active,
                                (SELECT COUNT(*) FROM subscriptions s WHERE s.user_id = u.id) AS subs_all
                         FROM users u$w ORDER BY u.id DESC LIMIT " . (int)$per . ' OFFSET ' . (int)(($page - 1) * $per));
    $st->execute(array_merge([$now], $args));
    return ['rows' => $st->fetchAll(), 'total' => $total, 'pages' => $pages, 'page' => $page];
}

function sb_m_subscriptions(PDO $pdo, array $f, int $page, int $per = 50): array
{
    $where = []; $args = [];
    $now = sb_now();
    $st = (string)($f['status'] ?? '');
    if ($st === 'active')    { $where[] = "s.status = 'active' AND s.expires_at > ?"; $args[] = $now; }
    if ($st === 'expired')   { $where[] = "s.status = 'active' AND s.expires_at <= ?"; $args[] = $now; }
    if ($st === 'suspended') { $where[] = "s.status = 'suspended'"; }
    if (in_array($f['plan'] ?? '', ['student', 'teacher', 'prep'], true)) { $where[] = 's.plan_type = ?'; $args[] = $f['plan']; }
    $q = trim(mb_substr((string)($f['q'] ?? ''), 0, 60));
    if ($q !== '') {
        $digits = sb_m_digits($q);
        if (ctype_digit($q) && strlen($q) <= 8) { $where[] = 's.user_id = ?'; $args[] = (int)$q; }
        elseif (strlen($digits) >= 5) { $where[] = 'u.whatsapp LIKE ?'; $args[] = $digits . '%'; }
        else { $where[] = 'u.name LIKE ?'; $args[] = sb_m_like($q); }
    }
    if (!empty($f['from'])) { $where[] = 's.expires_at >= ?'; $args[] = sb_m_date($f['from'], '1970-01-01') . ' 00:00:00'; }
    if (!empty($f['to'])) { $where[] = 's.expires_at < ?'; $args[] = sb_m_next_day(sb_m_date($f['to'], '2999-12-31')) . ' 00:00:00'; }
    $w = $where ? ' WHERE ' . implode(' AND ', $where) : '';
    $total = (int)sb_m_one($pdo, "SELECT COUNT(*) FROM subscriptions s JOIN users u ON u.id = s.user_id$w", $args);
    $pages = max(1, (int)ceil($total / $per));
    $page = min(max(1, $page), $pages);
    $q2 = $pdo->prepare("SELECT s.*, u.name AS user_name, u.whatsapp FROM subscriptions s JOIN users u ON u.id = s.user_id$w ORDER BY s.expires_at DESC, s.id DESC LIMIT " . (int)$per . ' OFFSET ' . (int)(($page - 1) * $per));
    $q2->execute($args);
    return ['rows' => $q2->fetchAll(), 'total' => $total, 'pages' => $pages, 'page' => $page];
}

function sb_m_audit(PDO $pdo, array $f, int $limit = 200): array
{
    $where = []; $args = [];
    if (!empty($f['action'])) { $where[] = 'action = ?'; $args[] = substr((string)$f['action'], 0, 40); }
    if (!empty($f['admin'])) { $where[] = 'admin_name = ?'; $args[] = substr((string)$f['admin'], 0, 40); }
    if (!empty($f['target'])) { $where[] = 'target_id = ?'; $args[] = substr((string)$f['target'], 0, 40); }
    if (!empty($f['from'])) { $where[] = 'created_at >= ?'; $args[] = sb_m_date($f['from'], '1970-01-01') . ' 00:00:00'; }
    if (!empty($f['to'])) { $where[] = 'created_at < ?'; $args[] = sb_m_next_day(sb_m_date($f['to'], '2999-12-31')) . ' 00:00:00'; }
    $st = $pdo->prepare('SELECT * FROM admin_audit' . ($where ? ' WHERE ' . implode(' AND ', $where) : '') . ' ORDER BY id DESC LIMIT ' . (int)$limit);
    $st->execute($args);
    return $st->fetchAll();
}

// Everything about one person, for the administrator.
function sb_m_user_detail(PDO $pdo, int $uid): ?array
{
    $st = $pdo->prepare("SELECT id, name, father_name, user_type, whatsapp, status, signup_platform, created_at, last_login_at FROM users WHERE id = ? AND status <> 'deleted'");
    $st->execute([$uid]);
    $u = $st->fetch();
    if (!$u) return null;
    $u['subs'] = array_map(function ($r) use ($pdo) { return sb_sub_public($pdo, $r, true); }, sb_user_subscriptions($pdo, $uid));
    $st = $pdo->prepare('SELECT * FROM payment_requests WHERE user_id = ? ORDER BY id DESC LIMIT 100');
    $st->execute([$uid]);
    $u['payments'] = $st->fetchAll();
    $u['free'] = sb_free_state($pdo, $uid, '');
    $st = $pdo->prepare("SELECT target_type, action, reason, admin_name, created_at FROM admin_audit WHERE (target_type = 'user' AND target_id = ?) OR detail_json LIKE ? OR detail_json LIKE ? ORDER BY id DESC LIMIT 30");
    $st->execute([(string)$uid, '%"user":' . $uid . ',%', '%"user":' . $uid . '}%']);
    $u['audit'] = $st->fetchAll();
    return $u;
}

// ---------------------------------------------------------------- CSV export (a leading = + - @ is neutralised so a spreadsheet never runs a name as a formula)

function sb_m_csv_cell($v): string
{
    $s = (string)$v;
    if ($s !== '' && strpos("=+-@\t\r", $s[0]) !== false) $s = "'" . $s;
    return '"' . str_replace('"', '""', $s) . '"';
}

function sb_m_csv(array $head, array $rows): string
{
    $out = implode(',', array_map('sb_m_csv_cell', $head)) . "\r\n";
    foreach ($rows as $r) $out .= implode(',', array_map('sb_m_csv_cell', $r)) . "\r\n";
    return "\xEF\xBB\xBF" . $out;
}

function sb_m_export(PDO $pdo, string $kind, string $from, string $to): ?array
{
    $a = $from . ' 00:00:00'; $b = sb_m_next_day($to) . ' 00:00:00';
    if ($kind === 'users') {
        $st = $pdo->prepare("SELECT u.id, u.name, u.father_name, u.whatsapp, u.status, u.signup_platform, u.created_at, u.last_login_at,
              (SELECT COUNT(*) FROM subscriptions s WHERE s.user_id = u.id AND s.status = 'active' AND s.expires_at > UTC_TIMESTAMP()) AS active_subs,
              (SELECT COUNT(*) FROM payment_requests p WHERE p.user_id = u.id AND p.status = 'approved') AS approved_payments
              FROM users u WHERE u.status <> 'deleted' AND u.role <> 'admin' AND u.created_at >= ? AND u.created_at < ? ORDER BY u.id");
        $st->execute([$a, $b]);
        return ['users', sb_m_csv(['id', 'name', 'father_name', 'whatsapp', 'status', 'signup_platform', 'created_at_utc', 'last_login_utc', 'active_subscriptions', 'approved_payments'], array_map('array_values', $st->fetchAll()))];
    }
    if ($kind === 'payments') {
        $st = $pdo->prepare('SELECT p.ref, p.id, p.user_id, p.contact_name, p.contact_whatsapp, p.plan_type, p.class_id, p.subjects_json, p.amount_pkr, p.method, p.trx_id, p.paid_on, p.platform, p.status,
              p.submitted_at, p.reviewed_by_name, p.reviewed_at, p.review_note, p.subscription_id, p.activated_at, p.expires_at FROM payment_requests p WHERE p.submitted_at >= ? AND p.submitted_at < ? ORDER BY p.id');
        $st->execute([$a, $b]);
        return ['payments', sb_m_csv(['ref', 'id', 'user_id', 'name', 'whatsapp', 'plan', 'class', 'subjects', 'amount_pkr', 'method', 'transaction_id', 'paid_on', 'platform', 'status', 'submitted_utc', 'reviewed_by', 'reviewed_utc', 'note', 'subscription_id', 'activated_utc', 'expires_utc'], array_map('array_values', $st->fetchAll()))];
    }
    if ($kind === 'subscriptions') {
        $st = $pdo->prepare("SELECT s.id, s.user_id, u.name, u.whatsapp, s.plan_type, s.class_id, s.source, s.status, s.starts_at, s.expires_at, s.suspend_reason,
              CASE WHEN s.status = 'suspended' THEN 'suspended' WHEN s.expires_at > UTC_TIMESTAMP() THEN 'active' ELSE 'expired' END AS state
              FROM subscriptions s JOIN users u ON u.id = s.user_id WHERE s.starts_at >= ? AND s.starts_at < ? ORDER BY s.id");
        $st->execute([$a, $b]);
        return ['subscriptions', sb_m_csv(['id', 'user_id', 'name', 'whatsapp', 'plan', 'class', 'source', 'stored_status', 'starts_utc', 'expires_utc', 'suspend_reason', 'state_now'], array_map('array_values', $st->fetchAll()))];
    }
    return null;
}
