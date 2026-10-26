<?php
// Feedback tests (migration 009, api/feedback.php, api/lib/feedback.php, the Feedback pages of api/admin.php, export, prune).
// Included by tests/php/run.php after the news feed tests: it uses that file's check(), http(), reg(), user_id_of(), reset_limits(), test_pdo(), $api,
// $port and the running test server, and admin_tests.php's http_form(), csrf_of(), admin_page() and the administrator $ad.

echo "--- feedback ---\n";

function fb_uuid(): string { return sb_uuid4(); }
$fb_keep_limits = false;      // most checks are about the words and the picture, not about the hourly limit: the limit is reset before each send unless this is true
// a valid PNG made without GD: 32x32 noise, a few KB
function fb_png(int $w = 32, int $h = 32, int $seed = 7, string $text = ''): string
{
    mt_srand($seed);
    $raw = '';
    for ($y = 0; $y < $h; $y++) { $raw .= "\0"; for ($x = 0; $x < $w; $x++) $raw .= chr(mt_rand(0, 255)) . chr(mt_rand(0, 255)) . chr(mt_rand(0, 255)); }
    $chunk = function ($type, $data) { return pack('N', strlen($data)) . $type . $data . pack('N', crc32($type . $data)); };
    return "\x89PNG\r\n\x1a\n" . $chunk('IHDR', pack('NNCCCCC', $w, $h, 8, 2, 0, 0, 0)) . ($text !== '' ? $chunk('tEXt', "Comment\0" . $text) : '') . $chunk('IDAT', gzcompress($raw, 9)) . $chunk('IEND', '');
}
// multipart: fields plus an optional picture
function fb_multipart(array $fields, ?string $bytes = null, array $headers = [], ?string $jar = null, string $name = 'picture.png', string $mime = 'image/png'): array
{
    global $port, $fb_keep_limits;
    if (!$fb_keep_limits) reset_limits();
    $ch = curl_init("http://127.0.0.1:$port/feedback.php?action=submit");
    $post = $fields; $tmp = null;
    if ($bytes !== null) { $tmp = tempnam(sys_get_temp_dir(), 'sbfb'); file_put_contents($tmp, $bytes); $post['image'] = new CURLFile($tmp, $mime, $name); }
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_HEADER => true, CURLOPT_POST => true, CURLOPT_POSTFIELDS => $post, CURLOPT_TIMEOUT => 30, CURLOPT_HTTPHEADER => $headers]);
    if ($jar) { curl_setopt($ch, CURLOPT_COOKIEJAR, $jar); curl_setopt($ch, CURLOPT_COOKIEFILE, $jar); }
    $raw = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $hs = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    curl_close($ch);
    if ($tmp) @unlink($tmp);
    return ['code' => $code, 'head' => substr((string)$raw, 0, $hs), 'json' => json_decode(substr((string)$raw, $hs), true), 'body' => substr((string)$raw, $hs)];
}
function fb_fields(array $over = []): array
{
    return $over + ['client_id' => fb_uuid(), 'kind' => 'content', 'message' => 'Page 14 of the Class 7 Maths book: the answer to Q3 (b) is printed as 12 but it should be 21.',
                    'context' => json_encode(['cls' => '7', 'subject' => 'cls7-math', 'subjectName' => 'Mathematics', 'chapter' => '3', 'page' => '14', 'screen' => '#subject/cls7/math', 'version' => 'abc123def456', 'platform' => 'web', 'online' => true])];
}
function fb_row(string $cid): ?array
{
    $st = test_pdo()->prepare('SELECT * FROM feedback_reports WHERE client_id = ?'); $st->execute([$cid]);
    $r = $st->fetch();
    return $r ? $r : null;
}

reset_limits();
$gd = function_exists('imagecreatefromstring') && function_exists('imagejpeg') && !getenv('SB_TEST_NO_GD');

// ---- an anonymous report
$f = fb_fields();
$x = fb_multipart($f);
check('an anonymous report is stored', $x['code'] === 201 && $x['json']['ok'] === true && $x['json']['duplicate'] === false && $x['json']['id'] > 0, $x['body']);
$row = fb_row($f['client_id']);
check('with its kind and words, no account, state new', $row && $row['kind'] === 'content' && strpos($row['message'], 'Q3 (b)') !== false && $row['user_id'] === null && $row['status'] === 'new' && (int)$row['has_image'] === 0, json_encode($row));
$ctx = json_decode((string)$row['context_json'], true);
check('the context is kept: class, subject, chapter, page, screen, version, platform', $ctx['cls'] === '7' && $ctx['subject'] === 'cls7-math' && $ctx['chapter'] === '3' && $ctx['page'] === '14' && $ctx['screen'] === '#subject/cls7/math' && $ctx['version'] === 'abc123def456' && $ctx['platform'] === 'web' && $ctx['online'] === true, json_encode($ctx));
$x2 = fb_multipart($f);
check('sending the same client_id again answers with the first report, it never makes a second', $x2['code'] === 200 && $x2['json']['duplicate'] === true && $x2['json']['id'] === $x['json']['id'] && (int)test_pdo()->query("SELECT COUNT(*) FROM feedback_reports WHERE client_id = '" . $f['client_id'] . "'")->fetchColumn() === 1, $x2['body']);

// ---- only a whitelist of short strings is kept
$f = fb_fields(['context' => json_encode(['cls' => '9', 'email' => 'kid@example.com', 'password' => 'hunter2', 'phone' => '03001234567', 'screen' => '#home?token=SECRET&x=1#frag', 'book' => str_repeat('B', 500), 'platform' => 'banana', 'chapterTitle' => "Line\nbreak\x01 here"])]);
$x = fb_multipart($f);
$ctx = json_decode((string)fb_row($f['client_id'])['context_json'], true);
check('unknown context keys (e-mail, password, phone) are dropped, long strings are cut, a query string never leaves the device, a bad platform word is ignored', $x['code'] === 201 && !isset($ctx['email']) && !isset($ctx['password']) && !isset($ctx['phone']) && $ctx['screen'] === '#home' && mb_strlen($ctx['book']) === 80 && $ctx['platform'] === 'web' && strpos($ctx['chapterTitle'], "\n") === false && strpos($ctx['chapterTitle'], "\x01") === false, json_encode($ctx));
$x = fb_multipart(fb_fields(['context' => '{not json']));
check('a context that is not JSON is ignored, the report is still taken', $x['code'] === 201);
$x = fb_multipart(fb_fields(['context' => json_encode(['platform' => 'app', 'app' => '1.4.2'])]));
check('a report from the app is marked as such', $x['code'] === 201 && (string)test_pdo()->query('SELECT platform FROM feedback_reports WHERE id = ' . (int)$x['json']['id'])->fetchColumn() === 'app');

// ---- validation
$bad = function (array $over, string $label) { $x = fb_multipart(fb_fields($over)); check($label, $x['code'] === 400 && $x['json']['ok'] === false && is_string($x['json']['error']) && $x['json']['error'] !== '', $x['code'] . ' ' . $x['body']); };
$bad(['kind' => 'rant'], 'an unknown kind is refused');
$bad(['kind' => ''], 'no kind is refused');
$bad(['message' => 'ab'], 'a message of two characters is refused');
$bad(['message' => ''], 'an empty message is refused');
$bad(['message' => str_repeat('x', 2001)], 'a message over 2000 characters is refused');
$bad(['client_id' => 'not-a-uuid'], 'a client_id that is not a UUID is refused');
$bad(['client_id' => ''], 'no client_id is refused');
$x = fb_multipart(fb_fields(['message' => str_repeat('ا', 2000)]));
check('2000 Urdu / Arabic characters are accepted (counted as characters, not bytes)', $x['code'] === 201, $x['body']);
$x = fb_multipart(fb_fields(['message' => "  Hello\r\n\r\n\r\n\r\nworld \x07 ok  "]));
check('line breaks are kept (at most one blank line), control characters and padding are dropped', $x['code'] === 201 && (string)test_pdo()->query('SELECT message FROM feedback_reports WHERE id = ' . (int)$x['json']['id'])->fetchColumn() === "Hello\n\nworld  ok", $x['body']);
reset_limits();
$x = http('POST', 'feedback.php?action=submit', ['client_id' => fb_uuid(), 'kind' => 'suggestion', 'message' => 'Please add a night mode to the reader.', 'context' => ['cls' => '5']]);
check('a JSON report (no picture) is accepted too', $x['code'] === 201 && $x['json']['ok'] === true, $x['body']);
check('GET cannot submit and POST cannot read the state', http('GET', 'feedback.php?action=submit')['code'] === 400 && http('POST', 'feedback.php?action=status', [])['code'] === 400 && http('PUT', 'feedback.php?action=submit', [])['code'] === 405 && http('GET', 'feedback.php?action=nope')['code'] === 400);

// ---- who is the sender
reset_limits();
$stu = reg(['name' => 'Feedback Student', 'want_device' => true]);
$stuId = user_id_of($stu['num']);
$f = fb_fields();
$x = fb_multipart($f, null, ['Authorization: Bearer ' . $stu['json']['device']['token']]);
check('with a device token (the app) the report is linked to the account', $x['code'] === 201 && (int)fb_row($f['client_id'])['user_id'] === $stuId, $x['body']);
$f = fb_fields();
$x = fb_multipart($f, null, ['Authorization: Bearer ' . str_repeat('0', 64)]);
check('an unknown token does not reject the report: it is taken as anonymous', $x['code'] === 201 && fb_row($f['client_id'])['user_id'] === null, $x['body']);
$f = fb_fields();
$x = fb_multipart($f, null, [], $stu['jar']);
check('with the session cookie (the website) the report is linked to the account', $x['code'] === 201 && (int)fb_row($f['client_id'])['user_id'] === $stuId, $x['body']);
$f = fb_fields();
$x = fb_multipart($f, null, ['Sec-Fetch-Site: cross-site'], $stu['jar']);
check('a cross-site request with the cookie is NOT linked to the account (no forged report in a student\'s name)', $x['code'] === 201 && fb_row($f['client_id'])['user_id'] === null, $x['body']);

// ---- pictures
reset_limits();
$f = fb_fields();
$png = fb_png();
$x = fb_multipart($f, $png);
$row = fb_row($f['client_id']);
check('a PNG is accepted', $x['code'] === 201 && (int)$row['has_image'] === 1, $x['body']);
$img = test_pdo()->query('SELECT * FROM feedback_images WHERE report_id = ' . (int)$x['json']['id'])->fetch();
check('it is stored in the database with its size and hash' . ($gd ? ' (re-encoded as a JPEG: no location data survives)' : ' (GD is not installed here: the bytes are kept after the checks)'),
    $img && (int)$img['bytes'] === strlen($img['data']) && $img['sha256'] === hash('sha256', $img['data']) && ($gd ? ($img['mime'] === 'image/jpeg' && substr($img['data'], 0, 3) === "\xFF\xD8\xFF") : ($img['mime'] === 'image/png' && $img['data'] === $png)), $img ? $img['mime'] : 'no row');
$picId = (int)$x['json']['id'];
$refuse = function (string $label, ?string $bytes, string $name = 'x.png', string $mime = 'image/png') {
    $f = fb_fields();
    $x = fb_multipart($f, $bytes, [], null, $name, $mime);
    check($label, $x['code'] === 400 && $x['json']['ok'] === false && fb_row($f['client_id']) === null, $x['code'] . ' ' . $x['body']);
};
$f2 = fb_fields();
$x2 = fb_multipart($f2, fb_png(32, 32, 9, 'a<?=b<svg c <? d'), [], null, 'ok.png');
check('a real picture that happens to contain short markers such as <?= and <svg in its data is accepted (photos are random-looking: only long markers like <?php and <script show a hidden script)', $x2['code'] === 201, $x2['body']);
$refuse('a GIF is refused', "GIF89a" . str_repeat("\x01", 400), 'a.gif', 'image/gif');
$refuse('a PHP file called .png is refused', "<?php echo 'hello'; ?>" . str_repeat('x', 400), 'shell.png');
$refuse('text called .jpg with an image content type is refused', str_repeat('hello world ', 50), 'a.jpg', 'image/jpeg');
$refuse('a real PNG with a script hidden after the image data is refused', $png . '<?php system($_GET["c"]); ?>');
$refuse('a real PNG with an HTML page hidden after the image data is refused', $png . '<html><script>alert(1)</script></html>');
$refuse('a picture over 1.5 MB is refused', $png . str_repeat("\0", 1600000));
$refuse('a few bytes are not a picture', "\x89PNG");
$refuse('an SVG (script-capable) is refused', '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)">' . str_repeat(' ', 300) . '</svg>', 'a.svg', 'image/svg+xml');
check('a report that failed on its picture leaves nothing behind', (int)test_pdo()->query('SELECT COUNT(*) FROM feedback_images')->fetchColumn() === 2);

// ---- limits
reset_limits();
$fb_keep_limits = true;
$last = null;
for ($i = 0; $i < 9; $i++) $last = fb_multipart(fb_fields());
check('an address that is not signed in may send 8 reports an hour; the 9th waits (429 with Retry-After)', $last['code'] === 429 && stripos($last['head'], 'Retry-After:') !== false && $last['json']['ok'] === false, $last['code']);
$retry = fb_fields();
reset_limits();
$fb_keep_limits = true;
$first = fb_multipart($retry);
for ($i = 0; $i < 8; $i++) fb_multipart(fb_fields());
$again = fb_multipart($retry);
$fb_keep_limits = false;
check('a retry of a report that is already stored is answered even when the address is over its limit', $first['code'] === 201 && $again['code'] === 200 && $again['json']['duplicate'] === true, $again['code'] . ' ' . $again['body']);
reset_limits();
$lim = reg(['name' => 'Many Reports', 'want_device' => true]);
$fb_keep_limits = true;
$last = null;
for ($i = 0; $i < 21; $i++) $last = fb_multipart(fb_fields(), null, ['Authorization: Bearer ' . $lim['json']['device']['token']]);
check('a signed-in student may send 20 an hour; the 21st waits', $last['code'] === 429, $last['code']);
$fb_keep_limits = false;
reset_limits();

// ---- what the sender may learn: a word for the state, never text
$f = fb_fields();
$x = fb_multipart($f);
$s = http('GET', 'feedback.php?action=status&ids=' . $f['client_id'] . ',' . fb_uuid() . ',not-an-id,' . strtoupper($f['client_id']));
check('the sender can ask for the state of its reports by client_id: received', $s['code'] === 200 && $s['json']['status'][$f['client_id']] === 'received' && count($s['json']['status']) === 1, $s['body']);
check('the answer carries no text, no id, no context', strpos($s['body'], 'Q3') === false && strpos($s['body'], 'message') === false && strpos($s['body'], 'context') === false, $s['body']);
check('an empty or unknown list answers an empty object', http('GET', 'feedback.php?action=status&ids=')['body'] === '{"ok":true,"status":{}}' && http('GET', 'feedback.php?action=status')['json']['status'] === []);
$many = [];
for ($i = 0; $i < 40; $i++) $many[] = fb_uuid();
check('at most 30 ids are looked up', http('GET', 'feedback.php?action=status&ids=' . implode(',', $many))['code'] === 200);

// ---- the administrator's pages
$rid = (int)$x['json']['id'];
$a = admin_page('?v=feedback', $stu['jar']);
check('an ordinary student gets 404 on the feedback pages and the picture', $a['code'] === 404 && admin_page('?v=feedback&id=' . $rid, $stu['jar'])['code'] === 404 && admin_page('?v=feedback_image&id=' . $picId, $stu['jar'])['code'] === 404 && admin_page('?v=feedback_image&id=' . $picId, '')['code'] === 404);
check('a made-up form cannot change a report', http_form('admin.php', ['action' => 'feedback_set', 'id' => $rid, 'to' => 'fixed', 'csrf' => str_repeat('a', 32)], [], $stu['jar'])['code'] === 404 && (string)test_pdo()->query("SELECT status FROM feedback_reports WHERE id = $rid")->fetchColumn() === 'new');
check('the overview counts the new reports', strpos(admin_page('', $ad['jar'])['body'], 'new reports</a> of') !== false);
$xssId = fb_multipart(fb_fields(['message' => 'Look: <script>alert(1)</script> & <img src=x onerror=alert(2)>', 'kind' => 'bug', 'context' => json_encode(['chapterTitle' => '<b>bold</b>', 'cls' => '"><script>x</script>'])]));
$l = admin_page('?v=feedback', $ad['jar']);
check('the list shows reports to the administrator, with the headers of an admin page', $l['code'] === 200 && strpos($l['body'], '#' . $rid) !== false && stripos($l['head'], 'X-Frame-Options: DENY') !== false && stripos($l['head'], 'Cache-Control: no-store') !== false && stripos($l['head'], 'X-Robots-Tag: noindex') !== false, $l['code']);
check('markup in a message, a context value or a title is shown as text, never as markup', strpos($l['body'], '<script>alert(1)') === false && strpos($l['body'], '<img src=x') === false && strpos(admin_page('?v=feedback&id=' . (int)$xssId['json']['id'], $ad['jar'])['body'], '<script>alert(1)') === false && strpos(admin_page('?v=feedback&id=' . (int)$xssId['json']['id'], $ad['jar'])['body'], '<b>bold</b>') === false);
check('no inline script in the feedback pages', strpos($l['body'], '<script') === false && strpos($l['body'], ' onclick') === false);
$d = admin_page('?v=feedback&id=' . $rid, $ad['jar']);
check('a report opens with its words and where it was', $d['code'] === 200 && strpos($d['body'], 'Q3 (b)') !== false && strpos($d['body'], 'cls7-math') !== false && strpos($d['body'], 'Mathematics') !== false);
check('opening a new report marks it seen', (string)test_pdo()->query("SELECT status FROM feedback_reports WHERE id = $rid")->fetchColumn() === 'seen' && (string)http('GET', 'feedback.php?action=status&ids=' . $f['client_id'])['json']['status'][$f['client_id']] === 'seen');
$p = admin_page('?v=feedback&id=' . $picId, $ad['jar']);
check('a report with a picture shows it through the picture address', strpos($p['body'], 'v=feedback_image&amp;id=' . $picId) !== false);
$im = admin_page('?v=feedback_image&id=' . $picId, $ad['jar']);
check('the picture is served as an image, inert (sandboxed, no sniffing) and never cached', $im['code'] === 200 && preg_match('/Content-Type: image\/(jpeg|png)/i', $im['head']) === 1 && stripos($im['head'], 'sandbox') !== false && stripos($im['head'], 'X-Content-Type-Options: nosniff') !== false && stripos($im['head'], 'no-store') !== false && strlen($im['body']) > 100, substr($im['head'], 0, 300));
check('a report without a picture has no picture address', admin_page('?v=feedback_image&id=' . $rid, $ad['jar'])['code'] === 404);
$csrf = csrf_of($d['body']);
check('the page has a form with a one-use token', $csrf !== '' && strpos($d['body'], 'name="to"') !== false);
check('without the token the state cannot be changed', http_form('admin.php', ['action' => 'feedback_set', 'id' => $rid, 'to' => 'fixed', 'note' => 'x', 'csrf' => str_repeat('b', 32)], [], $ad['jar'])['code'] === 403);
check('a request from another site cannot change it either', http_form('admin.php', ['action' => 'feedback_set', 'id' => $rid, 'to' => 'fixed', 'note' => 'x', 'csrf' => $csrf], ['Sec-Fetch-Site: cross-site'], $ad['jar'])['code'] === 403 && (string)test_pdo()->query("SELECT status FROM feedback_reports WHERE id = $rid")->fetchColumn() === 'seen');
$r = http_form('admin.php', ['action' => 'feedback_set', 'id' => $rid, 'to' => 'fixed', 'note' => "Corrected in the data on 26 October.\nThanks", 'csrf' => $csrf], [], $ad['jar']);
$row = test_pdo()->query("SELECT * FROM feedback_reports WHERE id = $rid")->fetch();
check('the administrator sets the state and a note (one line, 500 characters at most)', $r['code'] === 303 && $row['status'] === 'fixed' && $row['admin_note'] === 'Corrected in the data on 26 October. Thanks' && (int)$row['handled_by'] === $adId, $r['code'] . ' ' . json_encode($row));
check('the change is written to the audit log with the old and the new state', (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE action = 'admin_feedback_set' AND detail = 'report:$rid seen>fixed'")->fetchColumn() === 1);
check('and the sender now sees the word fixed, nothing more', http('GET', 'feedback.php?action=status&ids=' . $f['client_id'])['json']['status'][$f['client_id']] === 'fixed');
$r = http_form('admin.php', ['action' => 'feedback_set', 'id' => $rid, 'to' => 'banana', 'note' => '', 'csrf' => $csrf], [], $ad['jar']);
check('an unknown state is refused and nothing changes', (string)test_pdo()->query("SELECT status FROM feedback_reports WHERE id = $rid")->fetchColumn() === 'fixed' && strpos(admin_page('?v=feedback&id=' . $rid, $ad['jar'])['body'], 'Not done') !== false);
$l = admin_page('?v=feedback&status=fixed&kind=content', $ad['jar']);
check('the list filters by state and by kind', strpos($l['body'], '#' . $rid) !== false && strpos(admin_page('?v=feedback&status=fixed&kind=bug', $ad['jar'])['body'], '#' . $rid) === false && strpos(admin_page('?v=feedback&status=new', $ad['jar'])['body'], '#' . $rid) === false);
check('an unknown filter value is ignored, not an error', admin_page('?v=feedback&status=zzz&kind=zzz&page=-4', $ad['jar'])['code'] === 200);

// ---- export, deleting an account, retention
require_once $api . '/lib/account.php';
$ex = sb_account_export(test_pdo(), $stuId);
check('the student\'s data export lists the reports sent while signed in (words, state; no picture bytes)', isset($ex['feedback']) && count($ex['feedback']) === 2 && $ex['feedback'][0]['kind'] === 'content' && strpos(json_encode($ex['feedback']), 'Q3') !== false && strpos(json_encode($ex['feedback']), 'PNG') === false, json_encode($ex['feedback']));
$cid = fb_uuid();
fb_multipart(fb_fields(['client_id' => $cid, 'message' => 'A report with a picture from a student who will leave']), fb_png(24, 24, 3), ['Authorization: Bearer ' . $stu['json']['device']['token']]);
$before = (int)test_pdo()->query('SELECT COUNT(*) FROM feedback_reports')->fetchColumn();
sb_purge_user(test_pdo(), $stuId);
check('deleting an account keeps the reports but no longer links them to anyone', (int)test_pdo()->query('SELECT COUNT(*) FROM feedback_reports')->fetchColumn() === $before && (int)test_pdo()->query("SELECT COUNT(*) FROM feedback_reports WHERE user_id = $stuId")->fetchColumn() === 0 && fb_row($cid) !== null && fb_row($cid)['user_id'] === null);
$t = test_pdo();
$old = fb_uuid();
fb_multipart(fb_fields(['client_id' => $old]), fb_png(20, 20, 5));
$oldRow = fb_row($old);
$t->exec("UPDATE feedback_reports SET status = 'fixed', updated_at = NOW() - INTERVAL 100 DAY WHERE id = " . (int)$oldRow['id']);
$open = fb_uuid();
fb_multipart(fb_fields(['client_id' => $open]), fb_png(20, 20, 6));
$t->exec("UPDATE feedback_reports SET updated_at = NOW() - INTERVAL 400 DAY WHERE client_id = '$open'");
$c = cli('prune');
check('prune removes the picture of a report closed over 90 days ago, keeps its words, and keeps everything of a report that is still open', $c['rc'] === 0 && strpos($c['out'], 'feedback_images=1') !== false
    && (int)$t->query('SELECT COUNT(*) FROM feedback_images WHERE report_id = ' . (int)$oldRow['id'])->fetchColumn() === 0 && (int)fb_row($old)['has_image'] === 0 && fb_row($old)['message'] !== ''
    && (int)fb_row($open)['has_image'] === 1, $c['out']);
$t->exec("UPDATE feedback_reports SET updated_at = NOW() - INTERVAL 400 DAY WHERE id = " . (int)$oldRow['id']);
$c = cli('prune');
check('and a report closed over a year ago goes with the next prune', $c['rc'] === 0 && fb_row($old) === null && fb_row($open) !== null, $c['out']);
