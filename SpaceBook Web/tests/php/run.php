<?php
// API tests: migrations, auth hardening, rate limits, devices. Runs the real endpoints through PHP's built-in
// web server against a THROWAWAY database (dropped and recreated each run). Compatible with PHP 7.4.
//   php tests/php/run.php
// Database: SB_TEST_DB_HOST (127.0.0.1), SB_TEST_DB_USER (root), SB_TEST_DB_PASS (empty), SB_TEST_DB_NAME (spacebook_test).
// Refuses to run against a database whose name does not start with "spacebook_test".

$root = realpath(__DIR__ . '/../..');
$api  = $root . '/api';
$host = getenv('SB_TEST_DB_HOST') ?: '127.0.0.1';
$user = getenv('SB_TEST_DB_USER') ?: 'root';
$pass = getenv('SB_TEST_DB_PASS') !== false ? getenv('SB_TEST_DB_PASS') : '';
$name = getenv('SB_TEST_DB_NAME') ?: 'spacebook_test';
if (strpos($name, 'spacebook_test') !== 0) { fwrite(STDERR, "refusing to touch database '$name'\n"); exit(2); }

$pass_n = 0; $fail_n = 0;
function check(string $label, bool $cond, string $detail = ''): void
{
    global $pass_n, $fail_n;
    if ($cond) { $pass_n++; echo "PASS  $label\n"; }
    else { $fail_n++; echo "FAIL  $label" . ($detail !== '' ? "  -> $detail" : '') . "\n"; }
}

function server_pdo(): PDO
{
    global $host, $user, $pass;
    return new PDO("mysql:host=$host;charset=utf8mb4", $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
}
function fresh_db(): void
{
    global $name;
    $p = server_pdo();
    $p->exec("DROP DATABASE IF EXISTS `$name`");
    $p->exec("CREATE DATABASE `$name` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
}
function test_pdo(): PDO
{
    global $host, $user, $pass, $name;
    return new PDO("mysql:host=$host;dbname=$name;charset=utf8mb4", $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
}

// config file that db_config() reads through SB_CONFIG
$cfg = sys_get_temp_dir() . '/spacebook_test_config_' . getmypid() . '.php';
file_put_contents($cfg, '<?php return ' . var_export([
    'db_host' => $host, 'db_name' => $name, 'db_user' => $user, 'db_pass' => $pass, 'db_port' => 3306,
    'health_token' => 'test-health-token',
], true) . ';');
putenv('SB_CONFIG=' . $cfg);

require $api . '/lib/migrate.php';
require $api . '/lib/security.php';

// ============================================================ 1. migrations
echo "--- migrations ---\n";
fresh_db();
$pdo = test_pdo();
$s = sb_migrate_status($pdo);
check('empty database is at version 0 with 2 pending', $s['current'] === 0 && count($s['pending']) === 2 && $s['latest'] === 2, json_encode($s));
$applied = sb_migrate_up($pdo);
check('up applies 001 and 002', count($applied) === 2, json_encode($applied));
$tables = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
foreach (['users', 'login_attempts', 'activity_progress', 'study_plans', 'test_prep_records', 'test_prep_sessions', 'devices', 'rate_limits', 'audit_log', 'sync_events', 'activity_catalog', 'schema_version'] as $t) {
    check("table $t exists", in_array($t, $tables, true));
}
check('second up changes nothing', sb_migrate_up($pdo) === []);

$pdo->exec("INSERT INTO users (name, father_name, user_type, whatsapp, password_hash) VALUES ('A','B','student','923001110001','x')");
$uid = (int)$pdo->lastInsertId();
$pdo->exec("INSERT INTO activity_progress (user_id, activity_key, steps_total, steps_done) VALUES ($uid, 'k1', 3, '0,1')");
$undone = sb_migrate_down($pdo, 1);
check('down 1 removes the 002 tables only', $undone === ['002_security_sync_v2.sql'] && !in_array('devices', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone));
check('down keeps student rows', (int)$pdo->query('SELECT COUNT(*) FROM activity_progress')->fetchColumn() === 1 && (int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn() === 1);
check('down refuses to go below version 1', sb_migrate_down($pdo, 5) === [] && sb_schema_version($pdo) === 1);
check('up again restores version 2', count(sb_migrate_up($pdo)) === 1 && sb_schema_version($pdo) === 2);

// a database created by the old db.php (tables, no schema_version) with data in it
fresh_db();
$pdo = test_pdo();
foreach (sb_sql_statements((string)file_get_contents($api . '/migrations/001_baseline.sql')) as $stmt) $pdo->exec($stmt);
$pdo->exec("INSERT INTO users (name, father_name, user_type, whatsapp, password_hash) VALUES ('Old','User','student','923001110002','x')");
$uid = (int)$pdo->lastInsertId();
$pdo->exec("INSERT INTO activity_progress (user_id, activity_key, steps_total, steps_done, coins_earned) VALUES ($uid, 'trace|a', 3, '0,1,2', 8)");
$pdo->exec("INSERT INTO study_plans (user_id, plan_id, plan_json, updated_ms) VALUES ($uid, 'p1', '{}', 5)");
$before = [(int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn(), (int)$pdo->query('SELECT SUM(coins_earned) FROM activity_progress')->fetchColumn(), (int)$pdo->query('SELECT COUNT(*) FROM study_plans')->fetchColumn()];
sb_migrate_up($pdo);
$after = [(int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn(), (int)$pdo->query('SELECT SUM(coins_earned) FROM activity_progress')->fetchColumn(), (int)$pdo->query('SELECT COUNT(*) FROM study_plans')->fetchColumn()];
check('migrating a legacy populated database loses no rows or coins', $before === $after && $after === [1, 8, 1], json_encode([$before, $after]));

// ============================================================ 2. helpers
echo "--- rate limiter, devices ---\n";
$pdo->exec('DELETE FROM rate_limits');
$r1 = sb_rate_hit($pdo, 't:a', 2, 60); $r2 = sb_rate_hit($pdo, 't:a', 2, 60); $r3 = sb_rate_hit($pdo, 't:a', 2, 60);
check('rate limiter allows the limit then blocks', $r1['ok'] && $r2['ok'] && !$r3['ok'] && $r3['retry'] >= 1 && $r3['retry'] <= 60, json_encode([$r1, $r2, $r3]));
check('buckets are independent', sb_rate_hit($pdo, 't:b', 2, 60)['ok']);
$pdo->exec("UPDATE rate_limits SET window_start = NOW() - INTERVAL 61 SECOND WHERE bucket = 't:a'");
check('window reset lets the bucket through again', sb_rate_hit($pdo, 't:a', 2, 60)['ok']);

$dev = sb_device_issue($pdo, $uid, 'Test phone');
$row = $pdo->query("SELECT * FROM devices WHERE id = '" . $dev['id'] . "'")->fetch();
check('device token is 64 hex and only its hash is stored', preg_match('/^[0-9a-f]{64}$/', $dev['token']) === 1 && $row['token_hash'] === hash('sha256', $dev['token']) && $row['token_hash'] !== $dev['token']);
$_SERVER['HTTP_AUTHORIZATION'] = 'Bearer ' . $dev['token'];
$d = sb_device_from_request($pdo);
check('valid bearer token resolves to its user and device', $d && $d['user_id'] === $uid && $d['device_id'] === $dev['id']);
$_SERVER['HTTP_AUTHORIZATION'] = 'Bearer ' . str_repeat('0', 64);
check('unknown token is rejected', sb_device_from_request($pdo) === null);
$_SERVER['HTTP_AUTHORIZATION'] = 'Bearer ' . $dev['token'];
sb_device_revoke($pdo, $dev['id'], $uid);
check('revoked token is rejected', sb_device_from_request($pdo) === null);
$dev2 = sb_device_issue($pdo, $uid, 'Second');
$pdo->exec("UPDATE users SET status = 'blocked' WHERE id = $uid");
$_SERVER['HTTP_AUTHORIZATION'] = 'Bearer ' . $dev2['token'];
check('token of a blocked account is rejected', sb_device_from_request($pdo) === null);
$pdo->exec("UPDATE users SET status = 'active' WHERE id = $uid");
sb_device_revoke_all($pdo, $uid);
check('revoke all', sb_device_from_request($pdo) === null);
unset($_SERVER['HTTP_AUTHORIZATION']);

foreach ([
    ['same-origin fetch metadata', ['HTTP_SEC_FETCH_SITE' => 'same-origin', 'HTTP_HOST' => 'a.test'], true],
    ['cross-site fetch metadata', ['HTTP_SEC_FETCH_SITE' => 'cross-site', 'HTTP_HOST' => 'a.test'], false],
    ['same-site (sibling subdomain) fetch metadata', ['HTTP_SEC_FETCH_SITE' => 'same-site', 'HTTP_HOST' => 'a.test'], false],
    ['matching Origin', ['HTTP_ORIGIN' => 'https://a.test', 'HTTP_HOST' => 'a.test'], true],
    ['matching Origin with port', ['HTTP_ORIGIN' => 'http://127.0.0.1:8790', 'HTTP_HOST' => '127.0.0.1:8790'], true],
    ['foreign Origin', ['HTTP_ORIGIN' => 'https://evil.test', 'HTTP_HOST' => 'a.test'], false],
    ['Origin null', ['HTTP_ORIGIN' => 'null', 'HTTP_HOST' => 'a.test'], false],
    ['no headers (curl, old browser)', ['HTTP_HOST' => 'a.test'], true],
] as $c) {
    foreach (['HTTP_SEC_FETCH_SITE', 'HTTP_ORIGIN', 'HTTP_HOST'] as $k) unset($_SERVER[$k]);
    foreach ($c[1] as $k => $v) $_SERVER[$k] = $v;
    check('same-site check: ' . $c[0], sb_request_is_same_site() === $c[2]);
}
foreach (['HTTP_SEC_FETCH_SITE', 'HTTP_ORIGIN', 'HTTP_HOST'] as $k) unset($_SERVER[$k]);

// ============================================================ 3. HTTP: the real endpoints
echo "--- endpoints (php -S) ---\n";
fresh_db();
$port = 18790 + (getmypid() % 500);
$proc = proc_open([PHP_BINARY, '-S', "127.0.0.1:$port", '-t', $api], [0 => ['pipe', 'r'], 1 => ['file', sys_get_temp_dir() . '/sb_php_server.log', 'w'], 2 => ['file', sys_get_temp_dir() . '/sb_php_server.log', 'a']], $pipes, $api, array_merge(getenv(), ['SB_CONFIG' => $cfg]));
$up = false;
for ($i = 0; $i < 50 && !$up; $i++) { $s = @fsockopen('127.0.0.1', $port, $en, $es, 0.2); if ($s) { fclose($s); $up = true; } else usleep(100000); }
check('test server started', $up);

function http(string $method, string $path, ?array $body = null, array $headers = [], ?string $jar = null): array
{
    global $port;
    $ch = curl_init("http://127.0.0.1:$port/$path");
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_HEADER => true, CURLOPT_CUSTOMREQUEST => $method, CURLOPT_TIMEOUT => 30]);
    if ($jar) { curl_setopt($ch, CURLOPT_COOKIEJAR, $jar); curl_setopt($ch, CURLOPT_COOKIEFILE, $jar); }
    $h = $headers;
    if ($body !== null) { curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body)); $h[] = 'Content-Type: application/json'; }
    curl_setopt($ch, CURLOPT_HTTPHEADER, $h);
    $raw = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $hs = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    curl_close($ch);
    $head = substr((string)$raw, 0, $hs);
    return ['code' => $code, 'head' => $head, 'json' => json_decode(substr((string)$raw, $hs), true), 'body' => substr((string)$raw, $hs)];
}
function reset_limits(): void { $p = test_pdo(); $p->exec('DELETE FROM login_attempts'); $p->exec('DELETE FROM rate_limits'); }
function reg(array $o = []): array
{
    static $n = 0; $n++;
    $jar = tempnam(sys_get_temp_dir(), 'sbj');
    $num = '92300' . str_pad((string)(2000000 + $n), 7, '0', STR_PAD_LEFT);
    $r = http('POST', 'auth.php?action=register', $o + ['name' => 'Test User', 'father_name' => 'Father', 'user_type' => 'student', 'whatsapp' => $num, 'password' => 'secret123'], [], $jar);
    $r['jar'] = $jar; $r['num'] = $num;
    return $r;
}

$h = http('GET', 'health.php');
check('public health shows only ok/db', $h['code'] === 200 && $h['json'] === ['ok' => true, 'db' => true], $h['body']);
$h = http('GET', 'health.php?token=wrong');
check('wrong health token gives the public report', $h['json'] === ['ok' => true, 'db' => true]);
$h = http('GET', 'health.php?token=test-health-token');
check('right health token adds PHP version and schema', isset($h['json']['php']) && $h['json']['schema']['current'] === 2 && $h['json']['schema']['pending'] === [], $h['body']);
check('deploy check pattern "db":true is still present', strpos(http('GET', 'health.php')['body'], '"db":true') !== false);

$r = reg(['want_device' => true, 'device_name' => 'Chrome']);
check('register works', $r['code'] === 201 && $r['json']['ok'] === true, $r['body']);
check('register without want_device returns no device', !isset(reg()['json']['device']));
check('register with want_device returns a token', isset($r['json']['device']['token']) && strlen($r['json']['device']['token']) === 64);
$tp = test_pdo();
check('raw token is not stored', (int)$tp->query("SELECT COUNT(*) FROM devices WHERE token_hash = '" . $r['json']['device']['token'] . "'")->fetchColumn() === 0);
check('cookie lasts 30 days', (bool)preg_match('/spacebook_sid=.*(Max-Age=2592000|Expires=)/is', $r['head']), $r['head']);
check('register and login are audited', (int)$tp->query("SELECT COUNT(*) FROM audit_log WHERE action = 'register'")->fetchColumn() >= 2);

// login failures: uniform message, per-number lock with Retry-After
reset_limits();
$a = reg(); $num = $a['num'];
$bad = http('POST', 'auth.php?action=login', ['whatsapp' => $num, 'password' => 'nope']);
$unk = http('POST', 'auth.php?action=login', ['whatsapp' => '923009999999', 'password' => 'nope']);
check('wrong password and unknown number look identical', $bad['code'] === 401 && $unk['code'] === 401 && $bad['json'] === $unk['json'], $bad['body'] . ' / ' . $unk['body']);
for ($i = 0; $i < 4; $i++) http('POST', 'auth.php?action=login', ['whatsapp' => $num, 'password' => 'nope']);
$lock = http('POST', 'auth.php?action=login', ['whatsapp' => $num, 'password' => 'secret123']);
check('number is locked after 5 failures, even with the right password, with Retry-After', $lock['code'] === 429 && stripos($lock['head'], 'Retry-After: 900') !== false, $lock['code'] . ' ' . $lock['head']);

// per-address ceiling: rotating through numbers from one address
reset_limits();
$last = null;
for ($i = 0; $i < 20; $i++) $last = http('POST', 'auth.php?action=login', ['whatsapp' => '92311' . str_pad((string)$i, 7, '0', STR_PAD_LEFT), 'password' => 'nope']);
check('first 20 failures from one address are answered 401', $last['code'] === 401);
$blocked = http('POST', 'auth.php?action=login', ['whatsapp' => '92311' . '9999999', 'password' => 'nope']);
check('21st failure from the address (new number) is rate limited', $blocked['code'] === 429, (string)$blocked['code']);

// registrations per address
reset_limits();
$codes = [];
for ($i = 0; $i < 11; $i++) $codes[] = reg()['code'];
check('10 registrations per hour per address, the 11th is 429', array_slice($codes, 0, 10) === array_fill(0, 10, 201) && $codes[10] === 429, json_encode($codes));

// cross-site POSTs
reset_limits();
$acct = reg();
$x = http('POST', 'auth.php?action=login', ['whatsapp' => $acct['num'], 'password' => 'secret123'], ['Origin: http://evil.example']);
check('login from a foreign Origin is refused', $x['code'] === 403, (string)$x['code']);
$x = http('POST', 'auth.php?action=login', ['whatsapp' => $acct['num'], 'password' => 'secret123'], ['Sec-Fetch-Site: cross-site']);
check('login with Sec-Fetch-Site cross-site is refused', $x['code'] === 403);
$x = http('POST', 'auth.php?action=login', ['whatsapp' => $acct['num'], 'password' => 'secret123'], ['Origin: http://127.0.0.1:' . $port], $acct['jar']);
check('login from the same Origin works', $x['code'] === 200 && $x['json']['ok'] === true, $x['body']);
$x = http('POST', 'progress.php?action=step', ['key' => 'trace|t1', 'title' => 't', 'total' => 3, 'step' => 0], ['Origin: http://evil.example'], $acct['jar']);
check('progress step from a foreign Origin is refused', $x['code'] === 403);
$x = http('POST', 'progress.php?action=step', ['key' => 'trace|t1', 'title' => 't', 'total' => 3, 'step' => 0], ['Origin: http://127.0.0.1:' . $port], $acct['jar']);
check('progress step from the same Origin still works (v1 clients unchanged)', $x['code'] === 200 && $x['json']['earned'] === 1, $x['body']);
$x = http('GET', 'progress.php?action=get', null, [], $acct['jar']);
check('progress get still works', $x['code'] === 200 && $x['json']['coins'] === 1, $x['body']);
$x = http('POST', 'test_prep.php?action=save', ['record' => ['updatedAt' => 1, 'q' => new stdClass()]], ['Origin: http://evil.example'], $acct['jar']);
check('test prep save from a foreign Origin is refused', $x['code'] === 403);
$x = http('POST', 'study_plans.php?action=delete', ['id' => 'p'], ['Origin: http://evil.example'], $acct['jar']);
check('study plan delete from a foreign Origin is refused', $x['code'] === 403);

// logout with a device token revokes that device
reset_limits();
$d = reg(['want_device' => true]);
$tok = $d['json']['device']['token']; $did = $d['json']['device']['id'];
$x = http('POST', 'auth.php?action=logout', [], ['Authorization: Bearer ' . $tok], $d['jar']);
check('logout succeeds', $x['code'] === 200);
check('logout with the device token revokes the device', (int)test_pdo()->query("SELECT revoked FROM devices WHERE id = '$did'")->fetchColumn() === 1);

// ============================================================ done
if (is_resource($proc)) { proc_terminate($proc); proc_close($proc); }
@unlink($cfg);
test_pdo()->exec('SELECT 1');
server_pdo()->exec("DROP DATABASE IF EXISTS `$name`");
echo "---\nphp tests: $pass_n passed, $fail_n failed\n";
exit($fail_n ? 1 : 0);
