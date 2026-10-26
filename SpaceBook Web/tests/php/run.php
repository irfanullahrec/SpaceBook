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
check('empty database is at version 0 with 8 pending', $s['current'] === 0 && count($s['pending']) === 8 && $s['latest'] === 8, json_encode($s));
$applied = sb_migrate_up($pdo);
check('up applies all eight migrations', count($applied) === 8, json_encode($applied));
$tables = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
foreach (['users', 'login_attempts', 'activity_progress', 'study_plans', 'test_prep_records', 'test_prep_sessions', 'devices', 'rate_limits', 'audit_log', 'sync_events', 'activity_catalog', 'schema_version', 'sync_changes', 'user_sync_state', 'tp_answers', 'tp_days', 'tp_runs', 'sync_errors', 'user_items', 'feed_posts', 'feed_comments', 'feed_post_likes', 'feed_comment_likes', 'feed_reports'] as $t) {
    check("table $t exists", in_array($t, $tables, true));
}
check('second up changes nothing', sb_migrate_up($pdo) === []);

$pdo->exec("INSERT INTO users (name, father_name, user_type, whatsapp, password_hash) VALUES ('A','B','student','923001110001','x')");
$uid = (int)$pdo->lastInsertId();
$pdo->exec("INSERT INTO activity_progress (user_id, activity_key, steps_total, steps_done) VALUES ($uid, 'k1', 3, '0,1')");
$undone8 = sb_migrate_down($pdo, 1);
check('down 1 removes the 008 news feed tables only', $undone8 === ['008_feed.sql'] && !array_intersect(['feed_posts', 'feed_comments', 'feed_post_likes', 'feed_comment_likes', 'feed_reports'], $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN)) && in_array('user_items', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true) && in_array('users', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone8));
$undone7 = sb_migrate_down($pdo, 1);
check('down 1 removes the 007 user items table and its change-log rows only', $undone7 === ['007_user_items.sql'] && !in_array('user_items', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true) && in_array('sync_errors', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone7));
$undone6 = sb_migrate_down($pdo, 1);
check('down 1 removes the 006 role column and the sync error table', $undone6 === ['006_admin.sql'] && !in_array('role', $pdo->query('SHOW COLUMNS FROM users')->fetchAll(PDO::FETCH_COLUMN), true) && !in_array('sync_errors', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone6));
$undone5 = sb_migrate_down($pdo, 1);
check('down 1 removes the 005 column and the extra status value', $undone5 === ['005_account_lifecycle.sql'] && !in_array('deleted_at', $pdo->query('SHOW COLUMNS FROM users')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone5));
$undone = sb_migrate_down($pdo, 1);
check('down 1 removes the 004 column only', $undone === ['004_plan_device.sql'] && !in_array('last_device', $pdo->query('SHOW COLUMNS FROM study_plans')->fetchAll(PDO::FETCH_COLUMN), true) && in_array('rev', $pdo->query('SHOW COLUMNS FROM study_plans')->fetchAll(PDO::FETCH_COLUMN), true) && in_array('tp_answers', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true), json_encode($undone));
check('down 1 more removes the 003 tables and the plan rev column', sb_migrate_down($pdo, 1) === ['003_sync_state.sql'] && !in_array('tp_answers', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true) && in_array('devices', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true) && !in_array('rev', $pdo->query('SHOW COLUMNS FROM study_plans')->fetchAll(PDO::FETCH_COLUMN), true));
check('down 1 more removes the 002 tables', sb_migrate_down($pdo, 1) === ['002_security_sync_v2.sql'] && !in_array('devices', $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN), true));
check('down keeps student rows', (int)$pdo->query('SELECT COUNT(*) FROM activity_progress')->fetchColumn() === 1 && (int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn() === 1);
check('down refuses to go below version 1', sb_migrate_down($pdo, 5) === [] && sb_schema_version($pdo) === 1);
check('up again restores version 8', count(sb_migrate_up($pdo)) === 7 && sb_schema_version($pdo) === 8);

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
check('right health token adds PHP version and schema', isset($h['json']['php']) && $h['json']['schema']['current'] === 8 && $h['json']['schema']['pending'] === [], $h['body']);
check('deploy check pattern "db":true is still present', strpos(http('GET', 'health.php')['body'], '"db":true') !== false);

$r = reg(['want_device' => true, 'device_name' => 'Chrome']);
check('register works', $r['code'] === 201 && $r['json']['ok'] === true, $r['body']);
check('register without want_device returns no device', !isset(reg()['json']['device']));
check('register with want_device returns a token', isset($r['json']['device']['token']) && strlen($r['json']['device']['token']) === 64);
// the Android app has no cookie: `me` and the entitlements answer for a device token alone
$tok = $r['json']['device']['token'];
$me = http('GET', 'auth.php?action=me', null, ['Authorization: Bearer ' . $tok]);
check('me with only a device token answers the user', $me['code'] === 200 && isset($me['json']['user']['id']) && $me['json']['user']['id'] === $r['json']['user']['id'] && !isset($me['json']['user']['role']), $me['body']);
$me = http('GET', 'auth.php?action=me', null, ['Authorization: Bearer ' . str_repeat('0', 64)]);
check('me with an unknown token answers no user', $me['code'] === 200 && $me['json']['user'] === null, $me['body']);
$ent = http('GET', 'v2/entitlements.php');
check('entitlements for a guest: unlocked, not signed in', $ent['code'] === 200 && $ent['json']['ok'] === true && $ent['json']['signedIn'] === false && $ent['json']['unlocked'] === true && $ent['json']['features']['sync'] === false, $ent['body']);
$ent = http('GET', 'v2/entitlements.php', null, ['Authorization: Bearer ' . $tok]);
check('entitlements with a device token: signed in, sync on', $ent['json']['signedIn'] === true && $ent['json']['features']['sync'] === true && $ent['json']['plan'] === 'free', $ent['body']);
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

// ============================================================ 4. v2 sync + reward limits
echo "--- api/v2/sync.php ---\n";
function ev(string $type, array $payload, ?string $id = null): array
{
    return ['eventId' => $id ?: sb_uuid4(), 'type' => $type, 'payload' => $payload, 'clientTs' => 1700000000000, 'schema' => 1];
}
function stepEv(string $key, int $total, int $step): array { return ev('step', ['key' => $key, 'title' => 'T', 'total' => $total, 'step' => $step]); }
function sync_post(?string $token, array $events, array $extra = [], ?string $jar = null): array
{
    return http('POST', 'v2/sync.php', ['events' => $events], array_merge($token ? ['Authorization: Bearer ' . $token] : [], $extra), $jar);
}
function coins_of(int $uid): int
{
    $st = test_pdo()->prepare('SELECT COALESCE(SUM(coins_earned), 0) FROM activity_progress WHERE user_id = ?');
    $st->execute([$uid]);
    return (int)$st->fetchColumn();
}
function user_id_of(string $num): int { return (int)test_pdo()->query("SELECT id FROM users WHERE whatsapp = '$num'")->fetchColumn(); }
function fresh_user(): array
{
    reset_limits();
    $r = reg(['want_device' => true]);
    return ['token' => $r['json']['device']['token'], 'id' => user_id_of($r['num']), 'jar' => $r['jar'], 'num' => $r['num'], 'devId' => $r['json']['device']['id']];
}
function act_key(string $n): string { return 'cls2|math|u0|trace|' . $n . '|0'; }

$u = fresh_user();
$x = http('DELETE', 'v2/sync.php', null, ['Authorization: Bearer ' . $u['token']]);
check('only GET and POST are allowed', $x['code'] === 405);
$x = sync_post(null, []);
check('no credentials -> 401', $x['code'] === 401);
$x = sync_post(str_repeat('a', 64), []);
check('unknown token -> 401', $x['code'] === 401);
$x = sync_post($u['token'], []);
check('empty batch is fine', $x['code'] === 200 && $x['json']['accepted'] === [] && $x['json']['coins'] === 0, $x['body']);

// one step, replayed
$e1 = stepEv(act_key('aaa'), 3, 0);
$x = sync_post($u['token'], [$e1]);
check('step accepted, +1 coin, cursor moves', $x['code'] === 200 && $x['json']['accepted'] === [$e1['eventId']] && $x['json']['coins'] === 1 && $x['json']['cursor'] >= 1, $x['body']);
$cur1 = $x['json']['cursor'];
$x = sync_post($u['token'], [$e1]);
check('replaying the same event is accepted and changes nothing', $x['json']['accepted'] === [$e1['eventId']] && $x['json']['coins'] === 1 && $x['json']['cursor'] === $cur1 && coins_of($u['id']) === 1, $x['body']);
$x = sync_post($u['token'], [stepEv(act_key('aaa'), 3, 0)]);
check('same step under a new event id pays nothing again', $x['json']['coins'] === 1, $x['body']);
$x = sync_post($u['token'], [stepEv(act_key('aaa'), 3, 1), stepEv(act_key('aaa'), 3, 2)]);
check('finishing the activity pays steps + 5 bonus (1+1+1+5 = 8)', $x['json']['coins'] === 8, $x['body']);
$x = sync_post($u['token'], [ev('again', ['key' => act_key('aaa')])]);
check('finishing an activity today already counts as today\x27s practice (no extra coin)', $x['json']['coins'] === 8 && count($x['json']['accepted']) === 1, $x['body']);
test_pdo()->exec("UPDATE activity_progress SET last_completed_at = NOW() - INTERVAL 2 DAY WHERE user_id = {$u['id']}");
$x = sync_post($u['token'], [ev('again', ['key' => act_key('aaa')])]);
check('doing it again on a later day pays 2', $x['json']['coins'] === 10, $x['body']);
$x = sync_post($u['token'], [ev('again', ['key' => act_key('aaa')])]);
check('and not twice on the same day', $x['json']['coins'] === 10 && count($x['json']['accepted']) === 1, $x['body']);
$x = sync_post($u['token'], [ev('again', ['key' => act_key('never')])]);
check('again on an activity never completed is rejected', $x['json']['rejected'][0]['code'] === 'not_completed', $x['body']);

// validation
$bad = [
    ['bad_key', ev('step', ['key' => 'foo', 'title' => '', 'total' => 3, 'step' => 0])],
    ['bad_key', ev('step', ['key' => 'cls2|math|u0|trace|aaa|0|extra', 'title' => '', 'total' => 3, 'step' => 0])],
    ['bad_total', ev('step', ['key' => act_key('bbb'), 'title' => '', 'total' => 10000, 'step' => 0])],
    ['bad_total', ev('step', ['key' => act_key('bbb'), 'title' => '', 'total' => 0, 'step' => 0])],
    ['bad_step', ev('step', ['key' => act_key('bbb'), 'title' => '', 'total' => 3, 'step' => -1])],
    ['bad_step', ev('step', ['key' => act_key('bbb'), 'title' => '', 'total' => 3, 'step' => 5000])],
    ['bad_plan_id', ev('plan.save', ['plan' => []])],
    ['unsupported_type', ev('coins', ['amount' => 99999])],
    ['too_large', ev('step', ['key' => act_key('bbb'), 'title' => str_repeat('x', 70000), 'total' => 3, 'step' => 0])],
];
$x = sync_post($u['token'], array_map(function ($b) { return $b[1]; }, $bad));
$codes = array_map(function ($r) { return $r['code']; }, $x['json']['rejected']);
check('every invalid event is rejected with its reason', $codes === array_map(function ($b) { return $b[0]; }, $bad), json_encode($codes));
check('rejected events earn nothing and leave no ledger row', coins_of($u['id']) === 10 && (int)test_pdo()->query('SELECT COUNT(*) FROM sync_events WHERE user_id = ' . $u['id'])->fetchColumn() === 7, (string)coins_of($u['id']));
$x = sync_post($u['token'], [['eventId' => 'not-a-uuid', 'type' => 'step', 'payload' => []], ['type' => 'step'], 'junk']);
check('bad event ids and non-objects are rejected', count($x['json']['rejected']) === 3 && $x['json']['accepted'] === [], $x['body']);
$x = http('POST', 'v2/sync.php', ['events' => 'nope'], ['Authorization: Bearer ' . $u['token']]);
check('events must be a list', $x['code'] === 422);

// the Android app's Games tab: one key per game and page ending in the number of steps (GameKeys.rewardKey in the app)
$gk = 'cls5|g-word-match|u3|count|1a2b3c4d5e|3';
$before = coins_of($u['id']);
$x = sync_post($u['token'], [stepEv($gk, 3, 0), stepEv($gk, 3, 1)]);
check('game steps in the app key shape are accepted', count($x['json']['accepted']) === 2 && $x['json']['rejected'] === [], $x['body']);
check('and pay +1 per new step', coins_of($u['id']) === $before + 2, (string)(coins_of($u['id']) - $before));
$x = sync_post($u['token'], [stepEv($gk, 3, 2), stepEv($gk, 3, 1)]);
check('finishing pays +5 once; a repeated step pays nothing', coins_of($u['id']) === $before + 2 + 1 + 5, (string)(coins_of($u['id']) - $before));

// batch limits
$x = sync_post($u['token'], array_map(function ($i) { return stepEv(act_key('lim'), 200, $i % 200); }, range(1, 501)));
check('501 events -> 413', $x['code'] === 413, (string)$x['code']);
$x = sync_post($u['token'], [ev('step', ['key' => act_key('big'), 'title' => str_repeat('y', 1100000), 'total' => 3, 'step' => 0])]);
check('body over 1 MB -> 413', $x['code'] === 413, (string)$x['code']);

// 1,000 events in two batches, daily coin cap, crafted farming
$u2 = fresh_user();
$b1 = []; $b2 = [];
for ($i = 0; $i < 200; $i++) { $b1[] = stepEv(act_key('f1'), 200, $i); $b1[] = stepEv(act_key('f2'), 200, $i); }
for ($i = 0; $i < 100; $i++) $b1[] = stepEv(act_key('f3'), 200, $i);
for ($i = 100; $i < 200; $i++) $b2[] = stepEv(act_key('f3'), 200, $i);
for ($i = 0; $i < 200; $i++) $b2[] = stepEv(act_key('f4'), 200, $i);
for ($i = 0; $i < 200; $i++) $b2[] = stepEv(act_key('f5'), 200, $i);
$r1 = sync_post($u2['token'], $b1); $r2 = sync_post($u2['token'], $b2);
check('1,000 events in two batches of 500 are all accepted', $r1['code'] === 200 && $r2['code'] === 200 && count($r1['json']['accepted']) === 500 && count($r2['json']['accepted']) === 500 && $r2['json']['rejected'] === [], substr($r1['body'], 0, 200) . substr($r2['body'], 0, 200));
check('daily coin cap: 1,000 steps worth ~1,015 coins pay exactly 600', $r2['json']['coins'] === 600 && coins_of($u2['id']) === 600, (string)$r2['json']['coins']);
$steps = (int)test_pdo()->query("SELECT LENGTH(steps_done) - LENGTH(REPLACE(steps_done, ',', '')) + 1 FROM activity_progress WHERE user_id = {$u2['id']} AND activity_key = '" . act_key('f5') . "'")->fetchColumn();
check('progress itself is still recorded after the cap (200 steps)', $steps === 200, (string)$steps);
$r3 = sync_post($u2['token'], [stepEv(act_key('f6'), 200, 0)]);
check('nothing more is earned today', $r3['json']['coins'] === 600);
test_pdo()->exec("UPDATE rate_limits SET window_start = NOW() - INTERVAL 25 HOUR WHERE bucket = 'coins:u:{$u2['id']}'");
$r4 = sync_post($u2['token'], [stepEv(act_key('f6'), 200, 1)]);
check('the budget returns after 24 hours', $r4['json']['coins'] === 601, (string)$r4['json']['coins']);

// new-activity cap
$u3 = fresh_user();
$evs = [];
for ($i = 0; $i < 301; $i++) $evs[] = stepEv('cls2|math|u0|trace|n' . $i . '|0', 1, 0);
$x = sync_post($u3['token'], $evs);
check('301st new activity in a day is rejected as activity_limit', count($x['json']['accepted']) === 300 && count($x['json']['rejected']) === 1 && $x['json']['rejected'][0]['code'] === 'activity_limit', json_encode($x['json']['rejected']));
check('only 300 activities exist', (int)test_pdo()->query("SELECT COUNT(*) FROM activity_progress WHERE user_id = {$u3['id']}")->fetchColumn() === 300);

// two devices, any order, same result
$ua = fresh_user(); $ub = fresh_user();
$dA2 = sb_device_issue(test_pdo(), $ua['id'], 'second'); $dB2 = sb_device_issue(test_pdo(), $ub['id'], 'second');
$k = act_key('two');
sync_post($ua['token'], [stepEv($k, 3, 0), stepEv($k, 3, 1)]);
$ra = sync_post($dA2['token'], [stepEv($k, 3, 2), stepEv($k, 3, 1)]);
sync_post($dB2['token'], [stepEv($k, 3, 2), stepEv($k, 3, 1)]);
$rb = sync_post($ub['token'], [stepEv($k, 3, 0), stepEv($k, 3, 1)]);
$sa = test_pdo()->query("SELECT steps_done, times_completed FROM activity_progress WHERE user_id = {$ua['id']}")->fetch();
$sb = test_pdo()->query("SELECT steps_done, times_completed FROM activity_progress WHERE user_id = {$ub['id']}")->fetch();
check('two devices offline then online: same coins whatever the order (8)', $ra['json']['coins'] === 8 && $rb['json']['coins'] === 8, $ra['json']['coins'] . '/' . $rb['json']['coins']);
check('and the same final steps', $sa === $sb && $sa['steps_done'] === '0,1,2' && (int)$sa['times_completed'] === 1, json_encode([$sa, $sb]));
check('each event is attributed to its device', (int)test_pdo()->query("SELECT COUNT(DISTINCT device_id) FROM sync_events WHERE user_id = {$ua['id']}")->fetchColumn() === 2);

// revoked
$u4 = fresh_user();
sb_device_revoke(test_pdo(), $u4['devId'], $u4['id']);
check('revoked token -> 401', sync_post($u4['token'], [])['code'] === 401);

// cookie authentication: same-site required
$u5 = fresh_user();
$x = http('POST', 'auth.php?action=login', ['whatsapp' => $u5['num'], 'password' => 'secret123'], [], $u5['jar']);
$x = sync_post(null, [stepEv(act_key('ck'), 2, 0)], [], $u5['jar']);
check('cookie session works for sync (same-site / no Origin)', $x['code'] === 200 && $x['json']['coins'] === 1, $x['body']);
$x = sync_post(null, [stepEv(act_key('ck'), 2, 1)], ['Origin: http://evil.example'], $u5['jar']);
check('cookie session from a foreign Origin -> 403', $x['code'] === 403);
$x = sync_post(str_repeat('b', 64), [], [], $u5['jar']);
check('a wrong bearer token is not rescued by a cookie', $x['code'] === 401);

// rate limit
$u6 = fresh_user();
$last = null; $first429 = 0;
for ($i = 1; $i <= 62; $i++) { $last = sync_post($u6['token'], []); if ($last['code'] === 429 && !$first429) $first429 = $i; }
check('61st batch in a minute -> 429 with Retry-After', $first429 === 61 && preg_match('/Retry-After: \d+/i', $last['head']) === 1, "first429=$first429");

// v1 endpoint carries the same limits
$u7 = fresh_user();
$x = http('POST', 'auth.php?action=login', ['whatsapp' => $u7['num'], 'password' => 'secret123'], [], $u7['jar']);
$items = [];
for ($n = 0; $n < 5; $n++) $items[] = ['key' => 'farm' . $n, 'title' => 'f', 'total' => 200, 'done' => range(0, 199)];
$x = http('POST', 'progress.php?action=sync', ['items' => $items], [], $u7['jar']);
check('v1 progress sync is capped too: 5 x 205 coins pay 600', $x['code'] === 200 && $x['json']['coins'] === 600 && $x['json']['earned'] === 600, $x['body']);
$x = http('POST', 'progress.php?action=step', ['key' => 'huge', 'title' => 'h', 'total' => 100000, 'step' => 0], [], $u7['jar']);
check('v1 step still answers ok after the cap (earned 0)', $x['code'] === 200 && $x['json']['ok'] === true && $x['json']['earned'] === 0, $x['body']);
check('v1 total is clamped to 200 steps', (int)test_pdo()->query("SELECT steps_total FROM activity_progress WHERE user_id = {$u7['id']} AND activity_key = 'huge'")->fetchColumn() === 200);

// replaying a non-set event (a repeat) must not count twice: this is what the event ledger is for
$u8 = fresh_user();
sync_post($u8['token'], [stepEv(act_key('idem'), 1, 0)]);                       // completes: 1 + 5 coins
test_pdo()->exec("UPDATE activity_progress SET last_completed_at = NOW() - INTERVAL 2 DAY WHERE user_id = {$u8['id']}");
$eAgain = ev('again', ['key' => act_key('idem')]);
$x1 = sync_post($u8['token'], [$eAgain]);
$times1 = (int)test_pdo()->query("SELECT times_completed FROM activity_progress WHERE user_id = {$u8['id']}")->fetchColumn();
$x2 = sync_post($u8['token'], [$eAgain, $eAgain]);
$times2 = (int)test_pdo()->query("SELECT times_completed FROM activity_progress WHERE user_id = {$u8['id']}")->fetchColumn();
check('a replayed repeat (same event id, even twice in one batch) is applied once', $times1 === 2 && $times2 === 2 && $x1['json']['coins'] === 8 && $x2['json']['coins'] === 8 && $x2['json']['accepted'] === [$eAgain['eventId'], $eAgain['eventId']], json_encode([$times1, $times2, $x1['json']['coins'], $x2['json']['coins']]));

// ============================================================ 5. plans, test prep, pull
echo "--- plans, test prep, pull ---\n";
function pull(?string $token, int $since = 0, ?string $jar = null): array
{
    return http('GET', 'v2/sync.php?since=' . $since, null, $token ? ['Authorization: Bearer ' . $token] : [], $jar);
}
function mk_plan(string $id, string $name, array $tasks): array
{
    return ['id' => $id, 'name' => $name, 'updatedAt' => 1700000000000, 'sessions' => [['id' => 's1', 'date' => '2026-10-20', 'tasks' => $tasks]]];
}
function task(string $id, int $n, int $done): array { return ['id' => $id, 'n' => $n, 'done' => $done, 'cat' => 'rd']; }
function plan_of(array $pullJson, string $id): ?array
{
    foreach ($pullJson['plans'] as $p) if ($p['id'] === $id) return $p;
    return null;
}
function task_done(array $plan, string $tid): ?int
{
    foreach ($plan['sessions'] as $s) foreach ($s['tasks'] as $t) if ($t['id'] === $tid) return $t['done'];
    return null;
}
function ans(string $mcq, bool $correct, int $ms, int $ts, string $track = 'cls9-bio', string $day = '2026-10-20'): array
{
    return ev('tp.answer', ['mcqId' => $mcq, 'track' => $track, 'day' => $day, 'correct' => $correct, 'ms' => $ms, 'ts' => $ts]);
}

// ---- pull basics
$p = fresh_user();
check('GET without credentials -> 401', pull(null)['code'] === 401);
$g = pull($p['token']);
check('an empty account pulls an empty state', $g['code'] === 200 && $g['json']['cursor'] === 0 && $g['json']['more'] === false && $g['json']['progress'] === [] && $g['json']['plans'] === [] && $g['json']['tp']['q'] === [] && $g['json']['tp']['run'] === null, $g['body']);

// ---- the unfinished test is sent only when it changed
sync_post($p['token'], [ev('tp.run', ['run' => ['id' => 'runkeep', 'track' => 'pst', 'mode' => 'practice', 'ids' => [], 'answers' => [], 'i' => 0, 'savedAt' => 1000]])]);
$gr = pull($p['token']);
$cr = $gr['json']['cursor'];
check('a full pull carries the unfinished test', $gr['json']['tp']['run']['id'] === 'runkeep' && $gr['json']['tp']['runClearedAt'] === 0);
sync_post($p['token'], [ans('rk1', true, 10, 5)]);
$gi = pull($p['token'], $cr);
check('an incremental pull that did not touch the unfinished test does not mention it (so a client keeps what it has)', !array_key_exists('run', $gi['json']['tp']) && !array_key_exists('runClearedAt', $gi['json']['tp']) && isset($gi['json']['tp']['q']['rk1']), $gi['body']);

// ---- progress in a pull, incremental
sync_post($p['token'], [stepEv(act_key('pa'), 3, 0), stepEv(act_key('pa'), 3, 1)]);
$g1 = pull($p['token']);
check('a full pull lists progress with steps and total', isset($g1['json']['progress'][act_key('pa')]) && $g1['json']['progress'][act_key('pa')]['done'] === [0, 1] && $g1['json']['progress'][act_key('pa')]['total'] === 3 && $g1['json']['coins'] === 2, $g1['body']);
$c0 = $g1['json']['cursor'];
sync_post($p['token'], [stepEv(act_key('pb'), 2, 0)]);
$g2 = pull($p['token'], $c0);
check('an incremental pull returns only what changed since the cursor', array_keys($g2['json']['progress']) === [act_key('pb')] && $g2['json']['cursor'] > $c0, $g2['body']);
$g3 = pull($p['token'], $g2['json']['cursor']);
check('pulling again from the new cursor returns nothing', $g3['json']['progress'] === [] && $g3['json']['cursor'] === $g2['json']['cursor'] && $g3['json']['more'] === false);
check('pull is absolute: the same request twice gives the same answer', pull($p['token'])['json'] === pull($p['token'])['json']);

// ---- plans
$pl = fresh_user();
$A = $pl['token']; $B = sb_device_issue(test_pdo(), $pl['id'], 'second')['token'];
$x = sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_aaa1', 'Mine', [task('t1', 3, 0), task('t2', 2, 0)]), 'baseRev' => 0])]);
check('a new plan is accepted', count($x['json']['accepted']) === 1 && $x['json']['rejected'] === [], $x['body']);
$g = pull($A);
check('the pull shows the plan at revision 1', ($pp = plan_of($g['json'], 'plan_aaa1')) && $pp['rev'] === 1 && $pp['name'] === 'Mine');
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_aaa1', 'Mine v2', [task('t1', 3, 2), task('t2', 2, 0)]), 'baseRev' => 1])]);
$pp = plan_of(pull($A)['json'], 'plan_aaa1');
check('an edit based on the latest revision replaces the plan (rev 2)', $pp['rev'] === 2 && $pp['name'] === 'Mine v2' && task_done($pp, 't1') === 2);
// two devices edit revision 2 independently; A arrives first, then B
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_aaa1', 'Mine v2', [task('t1', 3, 3), task('t2', 2, 0)]), 'baseRev' => 2])]);
sync_post($B, [ev('plan.save', ['plan' => mk_plan('plan_aaa1', 'Renamed on B', [task('t1', 3, 1)]), 'baseRev' => 2])]);
$pp = plan_of(pull($A)['json'], 'plan_aaa1');
check('concurrent edit: the later arrival wins the fields, ticked work is never lost (t1 done = max(3,1))', $pp['name'] === 'Renamed on B' && task_done($pp, 't1') === 3 && $pp['rev'] === 4, json_encode($pp));
check('a task the later device removed stays removed', task_done($pp, 't2') === null);
// the same device edits again before it has seen its own save come back: a plain fast-forward, an un-tick sticks
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_seq01', 'Seq', [task('t1', 3, 0)]), 'baseRev' => 0])]);
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_seq01', 'Seq', [task('t1', 3, 3)]), 'baseRev' => 1])]);
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_seq01', 'Seq', [task('t1', 3, 1)]), 'baseRev' => 1])]);      // stale baseRev, same device
$pp = plan_of(pull($A)['json'], 'plan_seq01');
check('the same device with a stale baseRev is a fast-forward: un-ticking sticks (done 3 -> 1)', task_done($pp, 't1') === 1 && $pp['rev'] === 3, json_encode($pp));
sync_post($B, [ev('plan.save', ['plan' => mk_plan('plan_seq01', 'Seq B', [task('t1', 3, 0)]), 'baseRev' => 1])]);   // another device, stale baseRev
$pp = plan_of(pull($A)['json'], 'plan_seq01');
check('another device with a stale baseRev is merged: its name wins, ticked work is kept (done = max(0,1) = 1)', $pp['name'] === 'Seq B' && task_done($pp, 't1') === 1, json_encode($pp));
// delete + resurrect attempts
$x = sync_post($B, [ev('plan.delete', ['id' => 'plan_aaa1'])]);
$g = pull($A);
check('delete leaves a tombstone: gone from plans, listed in plansDeleted', plan_of($g['json'], 'plan_aaa1') === null && in_array('plan_aaa1', $g['json']['plansDeleted'], true));
$x = sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_aaa1', 'Offline edit', [task('t1', 3, 3)]), 'baseRev' => 4])]);
$g = pull($A);
check('an offline edit of a deleted plan does not bring it back', count($x['json']['accepted']) === 1 && plan_of($g['json'], 'plan_aaa1') === null);
sync_post($A, [ev('plan.delete', ['id' => 'plan_never'])]);
sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_never', 'Late', [task('t1', 1, 0)]), 'baseRev' => 0])]);
check('a delete that arrives before the plan blocks the plan', plan_of(pull($A)['json'], 'plan_never') === null);
$tomb = test_pdo()->query("SELECT plan_id, plan_json, rev, deleted FROM study_plans WHERE user_id = {$pl['id']} AND plan_id IN ('plan_aaa1', 'plan_never') ORDER BY plan_id")->fetchAll();
check('tombstones stay empty and keep their revision when a late save arrives', count($tomb) === 2 && $tomb[0]['plan_json'] === '{}' && (int)$tomb[0]['rev'] === 5 && $tomb[1]['plan_json'] === '{}' && (int)$tomb[1]['rev'] === 1 && (int)$tomb[0]['deleted'] === 1, json_encode($tomb));
$x = sync_post($A, [ev('plan.save', ['plan' => ['id' => 'x', 'sessions' => []], 'baseRev' => 0]), ev('plan.delete', ['id' => '../x'])]);
check('bad plan ids are rejected', array_column($x['json']['rejected'], 'code') === ['bad_plan_id', 'bad_plan_id']);
$x = sync_post($A, [ev('plan.save', ['plan' => mk_plan('plan_big1', str_repeat('n', 530000), [task('t1', 1, 0)]), 'baseRev' => 0])]);
check('a plan over 512 KB is rejected', $x['json']['rejected'][0]['code'] === 'too_large', $x['body']);

$many = fresh_user();
$evs = [];
for ($i = 0; $i < 51; $i++) $evs[] = ev('plan.save', ['plan' => mk_plan('plan_m' . str_pad((string)$i, 3, '0', STR_PAD_LEFT), 'P' . $i, [task('t1', 1, 0)]), 'baseRev' => 0]);
$x = sync_post($many['token'], $evs);
check('at most 50 plans: the 51st is rejected as plan_limit', count($x['json']['accepted']) === 50 && $x['json']['rejected'][0]['code'] === 'plan_limit', json_encode($x['json']['rejected']));

// v1 plan endpoints still work and v2 sees their changes
$v1 = fresh_user();
http('POST', 'auth.php?action=login', ['whatsapp' => $v1['num'], 'password' => 'secret123'], [], $v1['jar']);
$o = ['Origin: http://127.0.0.1:' . $port];
$x = http('POST', 'study_plans.php?action=save', ['plan' => mk_plan('plan_v1aa', 'From v1', [task('t1', 2, 1)])], $o, $v1['jar']);
check('v1 plan save still works', $x['code'] === 200 && $x['json']['ok'] === true, $x['body']);
$gv = pull($v1['token']);
check('v2 pull sees a plan saved through v1 (rev 1)', ($pp = plan_of($gv['json'], 'plan_v1aa')) && $pp['rev'] === 1 && $pp['name'] === 'From v1', $gv['body']);
$cv = $gv['json']['cursor'];
http('POST', 'study_plans.php?action=delete', ['id' => 'plan_v1aa'], $o, $v1['jar']);
$gv = pull($v1['token'], $cv);
check('v2 incremental pull sees a v1 delete', in_array('plan_v1aa', $gv['json']['plansDeleted'], true));
$x = http('GET', 'study_plans.php?action=list', null, [], $v1['jar']);
check('v1 list reports the same deletion', in_array('plan_v1aa', $x['json']['deleted'], true));

// ---- test prep
$t = fresh_user();
$T = $t['token']; $T2 = sb_device_issue(test_pdo(), $t['id'], 'second')['token'];
sync_post($T, [ans('m001', true, 4000, 1000), ans('m001', false, 6000, 2000), ans('m001', true, 5000, 3000)]);
$q = pull($T)['json']['tp']['q'];
check('answers are added up per MCQ: attempts 3, correct 2, last at 3000, last right, 15,000 ms', $q['m001'] === [3, 2, 3000, 1, 15000], json_encode($q));
sync_post($T2, [ans('m001', true, 1000, 4000), ans('m001', true, 1000, 5000)]);
$q = pull($T)['json']['tp']['q'];
check('a second device answering the same MCQ adds to it (5 attempts) instead of overwriting', $q['m001'][0] === 5 && $q['m001'][1] === 4 && $q['m001'][2] === 5000, json_encode($q));
sync_post($T, [ans('m002', true, 100, 200), ans('m002', false, 100, 100)]);   // the older answer arrives last
$q = pull($T)['json']['tp']['q'];
check('last_correct follows the newest answer even when delivered out of order', $q['m002'] === [2, 1, 200, 1, 200], json_encode($q['m002']));
sync_post($T, [ans('m003', true, 99999999, 10, 'cls9-bio', '2026-10-21')]);
$g = pull($T)['json']['tp'];
check('one answer counts at most an hour, and at most 5 minutes of daily time', $g['q']['m003'][4] === 3600000 && $g['days']['cls9-bio']['2026-10-21'][0] === 300000);
sync_post($T, [ans('m004', true, 1000, 10, 'cls9-phy', '2026-10-22'), ans('m005', false, 2000, 11, 'cls9-bio', '2026-10-22')]);
$g = pull($T)['json']['tp'];
check("daily numbers per track, plus an 'all' track that is their sum", $g['days']['cls9-phy']['2026-10-22'] === [1000, 1, 1] && $g['days']['cls9-bio']['2026-10-22'] === [2000, 1, 0] && $g['days']['all']['2026-10-22'] === [3000, 2, 1], json_encode($g['days']));
$x = sync_post($T, [ans('', true, 1, 1), ans('m1', true, 1, 1, 'all'), ans('m1', true, 1, 1, 'cls9-bio', '2026-1-1'), ev('tp.answer', ['mcqId' => 'bad id!', 'track' => 'cls9-bio', 'day' => '2026-10-20'])]);
check('bad MCQ id, track "all", bad day are rejected', array_column($x['json']['rejected'], 'code') === ['bad_mcq', 'bad_track', 'bad_day', 'bad_mcq'], json_encode($x['json']['rejected']));

$sess = ['id' => 'sess_one1', 'track' => 'cls9-bio', 'mode' => 'practice', 'ts' => 1700000000000, 'n' => 10, 'c' => 7, 'ms' => 60000, 'items' => [1, 2, 3]];
sync_post($T, [ev('tp.session', ['session' => $sess]), ev('tp.session', ['session' => $sess])]);
$g = pull($T)['json']['tp'];
check('a session is stored once however often it is sent', count($g['sessions']) === 1 && $g['sessions'][0]['id'] === 'sess_one1' && (int)test_pdo()->query("SELECT COUNT(*) FROM test_prep_sessions WHERE user_id = {$t['id']}")->fetchColumn() === 1);
$x = sync_post($T, [ev('tp.session', ['session' => ['id' => 'x', 'track' => 'a', 'mode' => 'practice']]), ev('tp.session', ['session' => ['id' => 'sess_two2', 'track' => 'cls9-bio', 'mode' => 'cheating']])]);
check('a malformed session is rejected', array_column($x['json']['rejected'], 'code') === ['bad_session', 'bad_session'], json_encode($x['json']));

// the unfinished session
$runA = ['id' => 'run1', 'track' => 'cls9-bio', 'mode' => 'practice', 'ids' => ['m001'], 'answers' => [null], 'i' => 0, 'savedAt' => 1000];
sync_post($T, [ev('tp.run', ['run' => $runA])]);
check('an unfinished session is stored', pull($T)['json']['tp']['run']['id'] === 'run1');
sync_post($T2, [ev('tp.run', ['run' => ['id' => 'older', 'savedAt' => 500] + $runA])]);
check('an older copy from another device does not replace it', pull($T)['json']['tp']['run']['id'] === 'run1');
sync_post($T2, [ev('tp.run.clear', ['clearedAt' => 2000])]);
$g = pull($T)['json']['tp'];
check('clearing hides it and reports when', $g['run'] === null && $g['runClearedAt'] === 2000);
sync_post($T, [ev('tp.run', ['run' => ['id' => 'run2', 'savedAt' => 1500] + $runA])]);
check('a copy saved before the clear stays hidden', pull($T)['json']['tp']['run'] === null);
sync_post($T, [ev('tp.run', ['run' => ['id' => 'run3', 'savedAt' => 3000] + $runA])]);
check('a copy saved after the clear is back', pull($T)['json']['tp']['run']['id'] === 'run3');
$x = sync_post($T, [ev('tp.run', ['run' => ['id' => 'nosave']]), ev('tp.run.clear', ['clearedAt' => 0])]);
check('a run without savedAt and a clear without a time are rejected', array_column($x['json']['rejected'], 'code') === ['bad_run', 'bad_run']);

// ---- old test-prep records (v1) reach the v2 tables
$leg = fresh_user();
$rec = ['v' => 1, 'updatedAt' => 5000, 'q' => ['L1' => [5, 3, 1000, 1, 9000], 'L2' => [1, 0, 2000, 0, 500]], 'days' => ['cls9-bio' => ['2026-10-01' => [60000, 5, 3]]], 'run' => null, 'runClearedAt' => 0];
test_pdo()->prepare('INSERT INTO test_prep_records (user_id, record_json, updated_ms) VALUES (?, ?, 5000)')->execute([$leg['id'], json_encode($rec)]);
$g = pull($leg['token']);
check('first v2 contact imports the old record (once)', $g['json']['tp']['q']['L1'] === [5, 3, 1000, 1, 9000] && $g['json']['tp']['days']['cls9-bio']['2026-10-01'] === [60000, 5, 3] && $g['json']['tp']['days']['all']['2026-10-01'] === [60000, 5, 3], $g['body']);
sync_post($leg['token'], [ans('L1', true, 1000, 3000)]);
pull($leg['token']);
check('the import is not repeated on later pulls (L1 stays at 6 attempts)', pull($leg['token'])['json']['tp']['q']['L1'][0] === 6);
http('POST', 'auth.php?action=login', ['whatsapp' => $leg['num'], 'password' => 'secret123'], [], $leg['jar']);
$o = ['Origin: http://127.0.0.1:' . $port];
$rec2 = ['v' => 1, 'updatedAt' => 6000, 'q' => ['L1' => [2, 1, 500, 0, 100], 'L9' => [4, 4, 9000, 1, 700]], 'days' => [], 'run' => null, 'runClearedAt' => 0];
$x = http('POST', 'test_prep.php?action=save', ['record' => $rec2], $o, $leg['jar']);
$q = pull($leg['token'])['json']['tp']['q'];
check('an old client saving fewer attempts cannot reduce the totals; a new MCQ arrives', $x['code'] === 200 && $q['L1'][0] === 6 && $q['L9'] === [4, 4, 9000, 1, 700], json_encode($q));
$rec3 = ['v' => 1, 'updatedAt' => 7000, 'q' => ['L9' => [9, 8, 9500, 1, 900]], 'days' => [], 'run' => null, 'runClearedAt' => 0];
http('POST', 'test_prep.php?action=save', ['record' => $rec3], $o, $leg['jar']);
check('an old client with more attempts raises them (more attempts wins)', pull($leg['token'])['json']['tp']['q']['L9'] === [9, 8, 9500, 1, 900]);
$cl = pull($leg['token'])['json']['cursor'];
http('POST', 'test_prep.php?action=save', ['record' => $rec3], $o, $leg['jar']);
check('an old client re-sending an unchanged record adds no change-log rows', pull($leg['token'])['json']['cursor'] === $cl);
http('POST', 'test_prep.php?action=session', ['session' => ['id' => 'v1sess1', 'track' => 'cls9-bio', 'mode' => 'mock', 'ts' => 5, 'n' => 3, 'c' => 1, 'ms' => 10]], $o, $leg['jar']);
check('a session saved through v1 is pulled by v2', in_array('v1sess1', array_column(pull($leg['token'], $cl)['json']['tp']['sessions'], 'id'), true));

// ---- paging of the change log
$pg = fresh_user();
$evs = [];
for ($i = 0; $i < 1100; $i++) $evs[] = ans('pg' . $i, true, 10, 1000 + $i);
foreach (array_chunk($evs, 500) as $chunk) sync_post($pg['token'], $chunk);
$p1 = pull($pg['token'], 1);
check('a long change log is paged: first page has more = true', $p1['code'] === 200 && $p1['json']['more'] === true && $p1['json']['cursor'] > 1, $p1['code'] . ' ' . substr($p1['body'], 0, 120));
$p2 = pull($pg['token'], $p1['json']['cursor']);
$p3 = $p2['json']['more'] ? pull($pg['token'], $p2['json']['cursor']) : $p2;
$seen = count($p1['json']['tp']['q']) + count($p2['json']['tp']['q']) + ($p2['json']['more'] ? count($p3['json']['tp']['q']) : 0);
check('following the cursor reaches the end with every answered MCQ delivered (1,100)', $p3['json']['more'] === false && $seen >= 1099 && pull($pg['token'])['json']['cursor'] === $p3['json']['cursor'], "seen=$seen");

// cookie GET
$ck = fresh_user();
http('POST', 'auth.php?action=login', ['whatsapp' => $ck['num'], 'password' => 'secret123'], [], $ck['jar']);
sync_post($ck['token'], [stepEv(act_key('ckp'), 1, 0)]);
$x = pull(null, 0, $ck['jar']);
check('a cookie session can pull', $x['code'] === 200 && $x['json']['coins'] === 6, $x['body']);
check('a wrong bearer token cannot pull even with a cookie', pull(str_repeat('c', 64), 0, $ck['jar'])['code'] === 401);

// ============================================================ 6. account: profile, password, export, delete
echo "--- account ---\n";
function acct_login(array $acct, string $pw = 'secret123'): array
{
    $jar = tempnam(sys_get_temp_dir(), 'sbj');
    $r = http('POST', 'auth.php?action=login', ['whatsapp' => $acct['whatsapp'], 'password' => $pw, 'want_device' => true], [], $jar);
    $r['jar'] = $jar;
    return $r;
}
function new_acct(): array
{
    reset_limits();
    $r = reg(['want_device' => true]);
    return ['token' => $r['json']['device']['token'], 'devId' => $r['json']['device']['id'], 'id' => user_id_of($r['num']), 'jar' => $r['jar'], 'whatsapp' => $r['num']];
}
$ac = new_acct();
$x = http('POST', 'auth.php?action=update_profile', ['name' => 'Changed Name', 'father_name' => 'New Father'], [], $ac['jar']);
check('profile can be changed', $x['code'] === 200 && $x['json']['user']['name'] === 'Changed Name' && $x['json']['user']['father_name'] === 'New Father' && $x['json']['user']['whatsapp'] === $ac['whatsapp'], $x['body']);
$x = http('POST', 'auth.php?action=update_profile', ['name' => 'X'], [], $ac['jar']);
check('a one-letter name is refused', $x['code'] === 422);
$x = http('POST', 'auth.php?action=update_profile', ['name' => 'Evil Name'], ['Origin: http://evil.example'], $ac['jar']);
check('profile change from a foreign Origin is refused', $x['code'] === 403);
$x = http('POST', 'auth.php?action=update_profile', ['name' => 'Anonymous Name']);
check('profile change without a session is refused', $x['code'] === 401);

// data to export
sync_post($ac['token'], [stepEv(act_key('exp'), 1, 0), ans('exp1', true, 1000, 5), ev('plan.save', ['plan' => mk_plan('plan_exp01', 'Export plan', [task('t1', 1, 0)]), 'baseRev' => 0])]);
$x = http('GET', 'auth.php?action=export', null, [], $ac['jar']);
$ex = $x['json'];
check('export returns the account data as a download', $x['code'] === 200 && stripos($x['head'], 'Content-Disposition: attachment') !== false && $ex['schema'] === 'spacebook.export/1', substr($x['body'], 0, 120));
check('export holds rewards, plans, answers and devices of this student', count($ex['rewards']) === 1 && count($ex['study_plans']) === 1 && $ex['study_plans'][0]['plan']['name'] === 'Export plan' && $ex['tests_preps']['answers'][0]['mcq_id'] === 'exp1' && count($ex['devices']) >= 1 && $ex['account']['name'] === 'Changed Name');
check('export never contains the password hash or a device token', strpos($x['body'], 'password_hash') === false && strpos($x['body'], $ac['token']) === false && strpos($x['body'], hash('sha256', $ac['token'])) === false);
$other = new_acct();
$xo = http('GET', 'auth.php?action=export', null, [], $other['jar']);
check("another student's export does not contain this student's data", count($xo['json']['rewards']) === 0 && count($xo['json']['study_plans']) === 0 && strpos($xo['body'], 'Export plan') === false);
check('export needs a session', http('GET', 'auth.php?action=export')['code'] === 401);

// password change
$pc = new_acct();
$dev2 = sb_device_issue(test_pdo(), $pc['id'], 'second');
$x = http('POST', 'auth.php?action=change_password', ['current_password' => 'wrong', 'new_password' => 'newsecret1'], [], $pc['jar']);
check('changing the password needs the current one', $x['code'] === 403);
$x = http('POST', 'auth.php?action=change_password', ['current_password' => 'secret123', 'new_password' => '123'], [], $pc['jar']);
check('a too short new password is refused', $x['code'] === 422);
$x = http('POST', 'auth.php?action=change_password', ['current_password' => 'secret123', 'new_password' => 'secret123'], [], $pc['jar']);
check('the same password again is refused', $x['code'] === 422);
$x = http('POST', 'auth.php?action=change_password', ['current_password' => 'secret123', 'new_password' => 'newsecret1'], ['Authorization: Bearer ' . $pc['token']], $pc['jar']);
check('the password can be changed', $x['code'] === 200 && $x['json']['ok'] === true, $x['body']);
reset_limits();
check('the old password no longer works, the new one does', acct_login($pc)['code'] === 401 && acct_login($pc, 'newsecret1')['code'] === 200);
check('other devices are signed out, the device that changed the password stays', sync_post($dev2['token'], [])['code'] === 401 && sync_post($pc['token'], [])['code'] === 200);
$x = http('POST', 'auth.php?action=change_password', ['current_password' => 'newsecret1', 'new_password' => 'another1x'], ['Origin: http://evil.example'], $pc['jar']);
check('password change from a foreign Origin is refused', $x['code'] === 403);

// delete
$dl = new_acct();
sync_post($dl['token'], [stepEv(act_key('del'), 1, 0), ans('del1', true, 1000, 5)]);
$x = http('POST', 'auth.php?action=delete_account', ['password' => 'wrong'], [], $dl['jar']);
check('deleting the account needs the password', $x['code'] === 403 && (string)test_pdo()->query("SELECT status FROM users WHERE id = {$dl['id']}")->fetchColumn() === 'active');
$x = http('POST', 'auth.php?action=delete_account', ['password' => 'secret123'], ['Origin: http://evil.example'], $dl['jar']);
check('deleting from a foreign Origin is refused', $x['code'] === 403);
$x = http('POST', 'auth.php?action=delete_account', ['password' => 'secret123'], [], $dl['jar']);
check('the account is deleted', $x['code'] === 200 && (string)test_pdo()->query("SELECT status FROM users WHERE id = {$dl['id']}")->fetchColumn() === 'deleted');
reset_limits();
$lg = http('POST', 'auth.php?action=login', ['whatsapp' => $dl['whatsapp'], 'password' => 'secret123']);
check('a deleted account cannot sign in and the answer is the same as for a wrong password', $lg['code'] === 401 && strpos($lg['body'], 'Wrong WhatsApp number or password') !== false, $lg['body']);
check('its device token stops working', sync_post($dl['token'], [])['code'] === 401);
check('the session is gone (me answers no user)', http('GET', 'auth.php?action=me', null, [], $dl['jar'])['json']['user'] === null);
check('its data is still there for the grace period', (int)test_pdo()->query("SELECT COUNT(*) FROM activity_progress WHERE user_id = {$dl['id']}")->fetchColumn() === 1);
$t = test_pdo();
require_once $api . '/lib/account.php';
check('purge does not touch accounts deleted less than 30 days ago', sb_purge_deleted($t, 30) === 0 && (int)$t->query("SELECT COUNT(*) FROM users WHERE id = {$dl['id']}")->fetchColumn() === 1);
$t->exec("UPDATE users SET deleted_at = NOW() - INTERVAL 31 DAY WHERE id = {$dl['id']}");
$keep = $ac['id'];
check('purge removes an account deleted more than 30 days ago', sb_purge_deleted($t, 30) === 1);
$left = 0;
foreach (['users' => 'id', 'activity_progress' => 'user_id', 'tp_answers' => 'user_id', 'tp_days' => 'user_id', 'sync_events' => 'user_id', 'sync_changes' => 'user_id', 'devices' => 'user_id', 'audit_log' => 'user_id', 'study_plans' => 'user_id', 'user_sync_state' => 'user_id', 'user_items' => 'user_id'] as $tbl => $col) {
    $left += (int)$t->query("SELECT COUNT(*) FROM $tbl WHERE $col = {$dl['id']}")->fetchColumn();
}
check('and every record of that account is gone from every table', $left === 0, (string)$left);
check('other accounts are untouched by the purge', (int)$t->query("SELECT COUNT(*) FROM users WHERE id = $keep")->fetchColumn() === 1 && (int)$t->query("SELECT COUNT(*) FROM tp_answers WHERE user_id = $keep")->fetchColumn() === 1);

// ============================================================ 7. user items, then administration, backup and restore drill
require __DIR__ . '/items_tests.php';
require __DIR__ . '/admin_tests.php';
require __DIR__ . '/feed_tests.php';

echo "--- backup / restore drill ---\n";
function run_php(array $args, array $env = []): array
{
    $cmd = escapeshellarg(PHP_BINARY);
    foreach ($args as $a) $cmd .= ' ' . escapeshellarg($a);
    $p = proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes, null, array_merge(getenv(), $env));
    $o = stream_get_contents($pipes[1]); $e = stream_get_contents($pipes[2]);
    return ['code' => proc_close($p), 'out' => $o, 'err' => $e];
}
$bkDir = sys_get_temp_dir() . '/sb_backup_test_' . getmypid();
@mkdir($bkDir, 0700, true);
$src = test_pdo();
$expectTables = $src->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
// awkward values must survive: quotes, backslashes, newlines, semicolons at a line end, emoji, Urdu, NULL
$src->exec("INSERT INTO audit_log (user_id, action, detail) VALUES (NULL, 'drill', " . $src->quote("it's \\ a \"test\";\nsecond line;\n🙂 اردو متن") . ")");
$dump = run_php([$root . '/tools/backup/dump.php', '--out', $bkDir, '--keep', '2'], ['SB_CONFIG' => $cfg]);
$files = glob($bkDir . '/spacebook-*.sql.gz') ?: [];
check('a backup file is written', $dump['code'] === 0 && count($files) === 1 && filesize($files[0]) > 1000, $dump['out'] . $dump['err']);
check('the dump reports every table', preg_match('/(\d+) tables/', $dump['out'], $m) === 1 && (int)$m[1] === count($expectTables), $dump['out']);

$rname = 'spacebook_test_restore';
server_pdo()->exec("DROP DATABASE IF EXISTS `$rname`");
server_pdo()->exec("CREATE DATABASE `$rname` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
$rcfg = sys_get_temp_dir() . '/spacebook_restore_config_' . getmypid() . '.php';
file_put_contents($rcfg, '<?php return ' . var_export(['db_host' => $host, 'db_name' => $rname, 'db_user' => $user, 'db_pass' => $pass, 'db_port' => 3306], true) . ';');
$rs = run_php([$root . '/tools/backup/restore.php', '--file', $files[0], '--config', $rcfg]);
check('the dump restores into an empty database', $rs['code'] === 0, $rs['out'] . $rs['err']);
$dst = new PDO("mysql:host=$host;dbname=$rname;charset=utf8mb4", $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
$mismatch = [];
foreach ($expectTables as $t) {
    $a = (int)$src->query("SELECT COUNT(*) FROM `$t`")->fetchColumn();
    $b = (int)$dst->query("SELECT COUNT(*) FROM `$t`")->fetchColumn();
    $ca = $src->query("CHECKSUM TABLE `$t`")->fetch(PDO::FETCH_NUM)[1];
    $cb = $dst->query("CHECKSUM TABLE `$t`")->fetch(PDO::FETCH_NUM)[1];
    if ($a !== $b || $ca !== $cb) $mismatch[] = "$t rows $a/$b checksum $ca/$cb";
}
check('every table has the same rows and checksum after the restore (' . count($expectTables) . ' tables)', !$mismatch, json_encode($mismatch));
$d1 = $src->query("SELECT detail FROM audit_log WHERE action = 'drill'")->fetchColumn();
$d2 = $dst->query("SELECT detail FROM audit_log WHERE action = 'drill'")->fetchColumn();
check('quotes, backslashes, newlines, semicolons, emoji and Urdu survive byte for byte', $d1 === $d2 && strpos($d2, "\n🙂 اردو متن") !== false, json_encode([$d1, $d2], JSON_UNESCAPED_UNICODE));
check('the schema version and a user can be read from the restored copy', (int)$dst->query('SELECT MAX(version) FROM schema_version')->fetchColumn() === (int)$src->query('SELECT MAX(version) FROM schema_version')->fetchColumn() && (int)$dst->query('SELECT COUNT(*) FROM users')->fetchColumn() > 0);
$again = run_php([$root . '/tools/backup/restore.php', '--file', $files[0], '--config', $rcfg]);
check('a restore into a database that already has tables is refused without --force', $again['code'] === 3 && strpos($again['err'], '--force') !== false, $again['err']);
$forced = run_php([$root . '/tools/backup/restore.php', '--file', $files[0], '--config', $rcfg, '--force']);
check('and works with --force', $forced['code'] === 0);
$cut = $bkDir . '/cut.sql.gz';
$gzr = gzopen($cut, 'wb'); gzwrite($gzr, "DROP TABLE IF EXISTS `x`;\nCREATE TABLE `x` (a int);\nINSERT INTO `x` VALUES\n(1),\n(2"); gzclose($gzr);
server_pdo()->exec("DROP DATABASE IF EXISTS `$rname`"); server_pdo()->exec("CREATE DATABASE `$rname` CHARACTER SET utf8mb4");
$bad = run_php([$root . '/tools/backup/restore.php', '--file', $cut, '--config', $rcfg]);
check('a truncated dump is reported, not silently accepted', $bad['code'] === 1 && strpos($bad['err'], 'cut short') !== false, json_encode($bad));
$inside = run_php([$root . '/tools/backup/dump.php', '--out', '/home/x/public_html/backups'], ['SB_CONFIG' => $cfg]);
check('backups are refused inside public_html', $inside['code'] === 2 && strpos($inside['err'], 'public_html') !== false);
// rotation: keep the newest 2
foreach (['20200101-000000', '20200102-000000', '20200103-000000'] as $stamp) file_put_contents($bkDir . "/spacebook-$stamp.sql.gz", 'old');
$rot = run_php([$root . '/tools/backup/dump.php', '--out', $bkDir, '--keep', '2'], ['SB_CONFIG' => $cfg]);
$left = array_map('basename', glob($bkDir . '/spacebook-*.sql.gz') ?: []);
check('rotation keeps only the newest dumps (--keep 2)', $rot['code'] === 0 && count($left) === 2 && !in_array('spacebook-20200101-000000.sql.gz', $left, true), json_encode($left));
server_pdo()->exec("DROP DATABASE IF EXISTS `$rname`");
@unlink($rcfg);
foreach (glob($bkDir . '/*') ?: [] as $f) @unlink($f);
@rmdir($bkDir);

// ============================================================ done
if (is_resource($proc)) { proc_terminate($proc); proc_close($proc); }
@unlink($cfg);
test_pdo()->exec('SELECT 1');
server_pdo()->exec("DROP DATABASE IF EXISTS `$name`");
echo "---\nphp tests: $pass_n passed, $fail_n failed\n";
exit($fail_n ? 1 : 0);
