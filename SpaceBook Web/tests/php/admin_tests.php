<?php
// Administration tests (api/admin.php, api/lib/admin.php, migrate.php make-admin). Included by tests/php/run.php after the account tests:
// it uses that file's check(), http(), reg(), fresh_user(), test_pdo(), $api, $port and the running test server.

echo "--- administration ---\n";

function http_form(string $path, array $fields, array $headers = [], ?string $jar = null): array
{
    global $port;
    $ch = curl_init("http://127.0.0.1:$port/$path");
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_HEADER => true, CURLOPT_POST => true, CURLOPT_POSTFIELDS => http_build_query($fields), CURLOPT_TIMEOUT => 30]);
    if ($jar) { curl_setopt($ch, CURLOPT_COOKIEJAR, $jar); curl_setopt($ch, CURLOPT_COOKIEFILE, $jar); }
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $raw = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $hs = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    curl_close($ch);
    return ['code' => $code, 'head' => substr((string)$raw, 0, $hs), 'body' => substr((string)$raw, $hs)];
}
function cli(string $args): array
{
    global $api;
    $out = [];
    exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($api . '/migrate.php') . ' ' . $args . ' 2>&1', $out, $rc);
    return ['rc' => $rc, 'out' => implode("\n", $out)];
}
function csrf_of(string $html): string { return preg_match('/name="csrf" value="([0-9a-f]{32})"/', $html, $m) ? $m[1] : ''; }
function admin_page(string $query, string $jar): array { return http('GET', 'admin.php' . $query, null, [], $jar); }

reset_limits();
$ad = reg(['name' => 'Chief Admin']);                    // the future administrator
$stu = reg(['name' => 'Ordinary Student', 'want_device' => true]);
$xss = reg(['name' => '<script>alert(1)</script>']);
$adId = user_id_of($ad['num']); $stuId = user_id_of($stu['num']); $xssId = user_id_of($xss['num']);

// ---- nobody gets in without the role
$x = http('GET', 'admin.php');
check('anonymous: the same plain 404 a missing file gives', $x['code'] === 404 && strpos($x['body'], 'Not found') !== false && strpos($x['body'], 'Administration') === false, $x['code'] . ' ' . substr($x['body'], 0, 60));
$x = admin_page('', $stu['jar']);
check('an ordinary signed-in user gets 404 too, on every view', $x['code'] === 404 && admin_page('?v=users', $stu['jar'])['code'] === 404 && admin_page('?v=user&id=' . $adId, $stu['jar'])['code'] === 404 && admin_page('?v=sync', $stu['jar'])['code'] === 404 && admin_page('?v=audit', $stu['jar'])['code'] === 404);
$x = http_form('admin.php', ['action' => 'set_status', 'id' => $xssId, 'to' => 'blocked', 'csrf' => str_repeat('a', 32)], [], $stu['jar']);
check('an ordinary user cannot block anyone, even with a made-up form', $x['code'] === 404 && (string)test_pdo()->query("SELECT status FROM users WHERE id = $xssId")->fetchColumn() === 'active');

// ---- the role can only be given on the command line
$r = http('POST', 'auth.php?action=update_profile', ['name' => 'Ordinary Student', 'father_name' => 'Father', 'role' => 'admin'], [], $stu['jar']);
check('no request can set a role (profile update ignores role)', (string)test_pdo()->query("SELECT role FROM users WHERE id = $stuId")->fetchColumn() === 'user');
check('the role is not part of what the app learns about a user', strpos(json_encode($r['json']), 'role') === false && strpos(json_encode(http('GET', 'auth.php?action=me', null, [], $stu['jar'])['json']), 'role') === false);
$c = cli('make-admin ' . substr($ad['num'], 0, 2) . '000');
check('make-admin for an unknown number fails', $c['rc'] === 1 && strpos($c['out'], 'no active account') !== false, json_encode($c));
$c = cli('make-admin 0' . substr($ad['num'], 2));
check('make-admin takes the 03... form and says who', $c['rc'] === 0 && strpos($c['out'], "user #$adId is now an administrator") !== false, json_encode($c));
check('and writes admin_grant to the audit log', (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE user_id = $adId AND action = 'admin_grant' AND detail = 'cli'")->fetchColumn() === 1);

// ---- the administrator's pages
$x = admin_page('', $ad['jar']);
check('the overview opens for the administrator', $x['code'] === 200 && strpos($x['body'], 'Overview') !== false && strpos($x['body'], 'What is deployed') !== false, $x['code'] . ' ' . substr($x['body'], 0, 80));
check('and carries the security headers (no framing, no caching, no indexing, a strict policy)', stripos($x['head'], 'X-Frame-Options: DENY') !== false && stripos($x['head'], 'Cache-Control: no-store') !== false && stripos($x['head'], 'X-Robots-Tag: noindex') !== false && stripos($x['head'], "Content-Security-Policy: default-src 'none'") !== false && stripos($x['head'], 'Content-Type: text/html') !== false);
check('no inline script or inline style in any admin page', strpos($x['body'], '<script') === false && strpos($x['body'], 'style="') === false && strpos($x['body'], ' onclick') === false);
check('the deployed content is shown (service worker version from content/sw_version.js)', preg_match('/Service worker version<\/dt><dd>[0-9a-f]{12}</', $x['body']) === 1 && strpos($x['body'], 'Database schema') !== false && strpos($x['body'], 'version 8 of 8') !== false, substr(strip_tags($x['body']), -400));

$x = admin_page('?v=users', $ad['jar']);
check('people: numbers are masked in the list', strpos($x['body'], $stu['num']) === false && strpos($x['body'], substr($stu['num'], 0, 5) . str_repeat('*', strlen($stu['num']) - 7) . substr($stu['num'], -2)) !== false);
check('people: a name from the app that holds markup is shown as text, never as markup', strpos($x['body'], '<script>alert(1)</script>') === false && strpos($x['body'], '&lt;script&gt;alert(1)&lt;/script&gt;') !== false);
$x = admin_page('?v=users&q=' . urlencode('Ordinary'), $ad['jar']);
check('people: search by part of a name', strpos($x['body'], 'Ordinary Student</a>') !== false && strpos($x['body'], 'Chief Admin</a>') === false, $x['code'] . ' ' . substr(strip_tags($x['body']), 0, 500));
$x = admin_page('?v=users&q=' . urlencode($stu['num']), $ad['jar']);
check('people: search by the whole number', strpos($x['body'], 'Ordinary Student</a>') !== false && strpos($x['body'], 'Chief Admin</a>') === false, $x['code'] . ' ' . substr(strip_tags($x['body']), 0, 500));
$x = admin_page('?v=users&q=' . urlencode('0' . substr($stu['num'], 2)), $ad['jar']);
check('people: search by the 03... form', strpos($x['body'], 'Ordinary Student</a>') !== false && strpos($x['body'], 'Chief Admin</a>') === false, $x['code'] . ' ' . substr(strip_tags($x['body']), 0, 500));
$x = admin_page('?v=users&q=' . urlencode("100%"), $ad['jar']);
check('people: a % in the search is a plain character, not a wildcard', $x['code'] === 200 && strpos($x['body'], 'Ordinary Student') === false);
check('people: deleted accounts are not listed', (function () use ($ad) {
    $d = reg(['name' => 'Gone Person']); test_pdo()->exec("UPDATE users SET status = 'deleted' WHERE whatsapp = '" . $d['num'] . "'");
    return strpos(admin_page('?v=users&q=Gone', $ad['jar'])['body'], 'Gone Person') === false;
})());

$x = admin_page('?v=user&id=' . $stuId, $ad['jar']);
check('one person: the whole number, the type, the device', strpos($x['body'], $stu['num']) !== false && strpos($x['body'], 'student') !== false && strpos($x['body'], 'Block this account') !== false);
check('opening a person is written to the audit log with who looked', (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE user_id = $stuId AND action = 'admin_view' AND detail = 'by:$adId'")->fetchColumn() === 1);

// ---- blocking
$csrf = csrf_of($x['body']);
check('the form carries a token', strlen($csrf) === 32);
$y = http_form('admin.php', ['action' => 'set_status', 'id' => $stuId, 'to' => 'blocked', 'reason' => 'x'], [], $ad['jar']);
check('block without the token is refused and changes nothing', $y['code'] === 403 && (string)test_pdo()->query("SELECT status FROM users WHERE id = $stuId")->fetchColumn() === 'active');
$y = http_form('admin.php', ['action' => 'set_status', 'id' => $stuId, 'to' => 'blocked', 'csrf' => str_repeat('0', 32)], [], $ad['jar']);
check('a wrong token is refused', $y['code'] === 403 && (string)test_pdo()->query("SELECT status FROM users WHERE id = $stuId")->fetchColumn() === 'active');
$y = http_form('admin.php', ['action' => 'set_status', 'id' => $stuId, 'to' => 'blocked', 'csrf' => $csrf], ['Origin: http://evil.example'], $ad['jar']);
check('a form from another site is refused even with the right token', $y['code'] === 403 && (string)test_pdo()->query("SELECT status FROM users WHERE id = $stuId")->fetchColumn() === 'active');
$y = http_form('admin.php', ['action' => 'set_status', 'id' => $stuId, 'to' => 'blocked', 'csrf' => $csrf, 'reason' => "spam\nsecond line"], ['Origin: http://127.0.0.1:' . $port], $ad['jar']);
check('block with the token: redirected back to the person', $y['code'] === 303 && stripos($y['head'], 'Location: admin.php?v=user&id=' . $stuId) !== false, $y['code'] . ' ' . $y['head']);
check('the account is blocked and every device signed out', (string)test_pdo()->query("SELECT status FROM users WHERE id = $stuId")->fetchColumn() === 'blocked' && (int)test_pdo()->query("SELECT COUNT(*) FROM devices WHERE user_id = $stuId AND revoked = 0")->fetchColumn() === 0);
$row = test_pdo()->query("SELECT detail FROM audit_log WHERE user_id = $stuId AND action = 'admin_block' ORDER BY id DESC LIMIT 1")->fetchColumn();
check('the audit log says who, why, and holds no line break', $row === "by:$adId spam second line", (string)$row);
$x = admin_page('?v=user&id=' . $stuId, $ad['jar']);
check('the page shows the result and offers to unblock', strpos($x['body'], 'Done.') !== false && strpos($x['body'], 'Unblock this account') !== false);
$l = http('POST', 'auth.php?action=login', ['whatsapp' => $stu['num'], 'password' => 'secret123']);
check('a blocked person cannot sign in', $l['code'] === 403 && strpos(json_encode($l['json']), 'blocked') !== false);
check('and their old session and device token stop working', http('GET', 'auth.php?action=me', null, [], $stu['jar'])['json']['user'] === null && sync_post($stu['json']['device']['token'], [])['code'] === 401);
$csrf = csrf_of($x['body']);
$y = http_form('admin.php', ['action' => 'set_status', 'id' => $stuId, 'to' => 'active', 'csrf' => $csrf], [], $ad['jar']);
check('unblock works and is logged', $y['code'] === 303 && (string)test_pdo()->query("SELECT status FROM users WHERE id = $stuId")->fetchColumn() === 'active' && (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE user_id = $stuId AND action = 'admin_unblock'")->fetchColumn() === 1);
reset_limits();
check('the unblocked person can sign in again', http('POST', 'auth.php?action=login', ['whatsapp' => $stu['num'], 'password' => 'secret123'])['code'] === 200);

// ---- what an administrator may not do
$self = http_form('admin.php', ['action' => 'set_status', 'id' => $adId, 'to' => 'blocked', 'csrf' => $csrf], [], $ad['jar']);
check('an administrator cannot block themselves', (string)test_pdo()->query("SELECT status FROM users WHERE id = $adId")->fetchColumn() === 'active' && strpos(admin_page('?v=user&id=' . $adId, $ad['jar'])['body'], 'cannot block yourself') !== false);
$ad2 = reg(['name' => 'Second Admin']); $ad2Id = user_id_of($ad2['num']);
cli('make-admin ' . $ad2['num']);
http_form('admin.php', ['action' => 'set_status', 'id' => $ad2Id, 'to' => 'blocked', 'csrf' => $csrf], [], $ad['jar']);
check('nor another administrator (that is the owner\'s job on the command line)', (string)test_pdo()->query("SELECT status FROM users WHERE id = $ad2Id")->fetchColumn() === 'active');
http_form('admin.php', ['action' => 'set_status', 'id' => 999999, 'to' => 'blocked', 'csrf' => $csrf], [], $ad['jar']);
http_form('admin.php', ['action' => 'set_status', 'id' => $xssId, 'to' => 'deleted', 'csrf' => $csrf], [], $ad['jar']);
http_form('admin.php', ['action' => 'make_admin', 'id' => $xssId, 'csrf' => $csrf], [], $ad['jar']);
check('no such account, a status that is not block / unblock, and an action that does not exist do nothing', (string)test_pdo()->query("SELECT status FROM users WHERE id = $xssId")->fetchColumn() === 'active' && (string)test_pdo()->query("SELECT role FROM users WHERE id = $xssId")->fetchColumn() === 'user');

// ---- sync problems are visible
$bad = [];
for ($i = 0; $i < 30; $i++) $bad[] = ['eventId' => 'not-a-uuid-' . $i, 'type' => 'step', 'payload' => ['x' => 1], 'schema' => 1];
$u = fresh_user();
sync_post($u['token'], $bad);
check('rejected events are recorded: code and id only, at most 20 per request', (int)test_pdo()->query("SELECT COUNT(*) FROM sync_errors WHERE user_id = " . $u['id'] . " AND code = 'bad_event_id'")->fetchColumn() === 20);
sync_post($u['token'], [['eventId' => sb_uuid4(), 'type' => 'no.such.type', 'payload' => ['a' => 1], 'schema' => 1]]);
check('an unsupported type is recorded with its code', (int)test_pdo()->query("SELECT COUNT(*) FROM sync_errors WHERE user_id = " . $u['id'] . " AND code = 'unsupported_type'")->fetchColumn() === 1);
check('and no payload is kept anywhere in that table', (int)test_pdo()->query("SELECT COUNT(*) FROM information_schema.columns WHERE table_schema = DATABASE() AND table_name = 'sync_errors' AND data_type IN ('text','mediumtext','longtext','blob','json')")->fetchColumn() === 0);
$x = admin_page('?v=sync', $ad['jar']);
$nBad = (int)test_pdo()->query("SELECT COUNT(*) FROM sync_errors WHERE code = 'bad_event_id'")->fetchColumn();
check('the sync view counts them by code (the 24-hour and 7-day columns match the table) and lists the latest', strpos($x['body'], 'unsupported_type') !== false && preg_match('/bad_event_id<\/td><td>' . $nBad . '<\/td><td>' . $nBad . '</', $x['body']) === 1, $nBad . ' ' . substr(strip_tags($x['body']), 0, 300));
$x = admin_page('?v=user&id=' . $u['id'], $ad['jar']);
check('and the person\'s page lists their problems', strpos($x['body'], 'Latest sync problems') !== false && strpos($x['body'], 'bad_event_id') !== false);

// ---- the audit log
$x = admin_page('?v=audit&action=admin_block', $ad['jar']);
check('the audit view filters by action', strpos($x['body'], '<td>admin_block</td>') !== false && strpos($x['body'], 'by:' . $adId) !== false && strpos($x['body'], '<td>admin_unblock</td>') === false && strpos($x['body'], '<td>login</td>') === false);
$x = admin_page('?v=audit&uid=' . $stuId, $ad['jar']);
check('and by person', strpos($x['body'], '<td>admin_view</td>') !== false && strpos($x['body'], '<td>admin_block</td>') !== false && strpos($x['body'], '<td>register</td>') !== false && strpos($x['body'], 'Chief Admin</a>') === false);

// ---- the role is checked in the database on every request
cli('remove-admin ' . $ad2['num']);
check('remove-admin ends access at the next request', admin_page('', $ad2['jar'])['code'] === 404 && (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE user_id = $ad2Id AND action = 'admin_revoke'")->fetchColumn() === 1);
test_pdo()->exec("UPDATE users SET status = 'blocked' WHERE id = $adId");
check('a blocked administrator is turned away although the session is still there', admin_page('', $ad['jar'])['code'] === 404);
test_pdo()->exec("UPDATE users SET status = 'active' WHERE id = $adId");
check('and is let in again when active', admin_page('', $ad['jar'])['code'] === 200);
check('migrate.php prune also clears old sync errors', (function () use ($u) {
    test_pdo()->exec("UPDATE sync_errors SET created_at = NOW() - INTERVAL 100 DAY WHERE user_id = " . $u['id'] . " AND code = 'bad_event_id'");
    $c = cli('prune');
    return strpos($c['out'], 'sync_errors=20') !== false && (int)test_pdo()->query("SELECT COUNT(*) FROM sync_errors WHERE user_id = " . $u['id'])->fetchColumn() === 1;
})());
check('deleting an account takes its sync error rows with it', (function () use ($u) {
    test_pdo()->exec("DELETE FROM users WHERE id = " . $u['id']);
    return (int)test_pdo()->query("SELECT COUNT(*) FROM sync_errors WHERE user_id = " . $u['id'])->fetchColumn() === 0;
})());
