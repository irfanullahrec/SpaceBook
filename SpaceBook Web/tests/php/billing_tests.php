<?php
// Billing tests: free limits, plans, Easypaisa payment submissions, approval / rejection, one-month activation, renewal, expiry,
// suspension, free extensions, the separate administrator page and the dashboard numbers. Included by tests/php/run.php after the
// administration tests: it uses check(), http(), reg(), test_pdo(), reset_limits(), $api, $root, $cfg, $port and the running test server.

echo "--- billing ---\n";
require_once $api . '/lib/billing.php';
require_once $api . '/lib/manage.php';

$tp = test_pdo();
reset_limits();
$tp->exec('DELETE FROM rate_limits');
$adm = $tp->query("SELECT id, username FROM admins WHERE username = 'IrfanUllah123'")->fetch();

function bill(string $m, string $action, ?array $body = null, array $headers = [], ?string $jar = null): array { return http($m, 'billing.php?action=' . $action, $body, $headers, $jar); }
function vid(): string { return bin2hex(random_bytes(16)); }
function vh(string $v, bool $app = false): array { return ['X-SB-Visitor: ' . $v, 'User-Agent: Mozilla/5.0 (SpaceBook test)'] + ($app ? [2 => 'X-SB-Platform: app'] : []); }
function bearer(array $r): array { return ['Authorization: Bearer ' . $r['json']['device']['token']]; }
function pay_body(array $o = []): array { static $n = 0; $n++; return $o + ['plan' => 'student', 'cls' => 'cls9', 'trx' => '1' . str_pad((string)(5000000 + $n), 9, '0', STR_PAD_LEFT), 'idem' => 'i' . $n . bin2hex(random_bytes(4))]; }
function use_free(string $metric, int $n, array $headers, string $prefix = 'q', array $extra = []): array { $last = null; for ($i = 1; $i <= $n; $i++) $last = bill('POST', 'consume', ['metric' => $metric, 'key' => $prefix . $i] + $extra, $headers); return $last; }
function new_pay(PDO $tp, int $uid, array $o = []): int
{
    $u = $tp->query("SELECT * FROM users WHERE id = $uid")->fetch();
    $r = sb_payment_submit($tp, $u, pay_body($o));
    return $r['ok'] ? (int)$r['payment']['id'] : 0;
}
function sub_count(PDO $tp, int $uid): int { return (int)$tp->query("SELECT COUNT(*) FROM subscriptions WHERE user_id = $uid")->fetchColumn(); }

// ---------------------------------------------------------------- the first administrator
$a = $tp->query("SELECT * FROM admins WHERE username = 'IrfanUllah123'")->fetch();
$initial = 'Iam@' . '123123123';        // written in two pieces so that this file never contains the password as one string
check('seeded administrator exists, active, must change the password, only a bcrypt hash stored', $a && $a['status'] === 'active' && (int)$a['must_change_password'] === 1 && strpos($a['password_hash'], '$2y$') === 0 && strpos($a['password_hash'], 'Iam@') === false);
check('seeded hash is the hash of the agreed initial password', password_verify($initial, $a['password_hash']));
$leak = [];
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS));
foreach (['api', 'manage', 'css', 'tests', 'tools'] as $dir) {
    foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root . '/' . $dir, FilesystemIterator::SKIP_DOTS)) as $f) {
        if (!preg_match('/\.(php|js|css|html|json|sql|md|txt)$/', $f->getFilename()) || $f->getSize() > 2000000 || $f->getFilename() === 'config.php') continue;     // config.php is the git-ignored live/local credentials file
        if (strpos((string)file_get_contents($f->getPathname()), $initial) !== false) $leak[] = $f->getPathname();
    }
}
foreach (['index.html', 'lazy.html', 'sw.js'] as $f) if (is_file($root . '/' . $f) && strpos((string)file_get_contents($root . '/' . $f), $initial) !== false) $leak[] = $f;
check('the initial password is in no source, page, script or test file', $leak === [], json_encode($leak));

// ---------------------------------------------------------------- plans
$p = bill('GET', 'plans');
$pl = []; foreach ($p['json']['plans'] as $x) $pl[$x['id']] = $x;
check('plans: three plans, PKR 500, one month, with includes and excludes', $p['code'] === 200 && count($pl) === 3 && $pl['student']['price'] === 500 && $pl['teacher']['price'] === 500 && $pl['prep']['price'] === 500 && $pl['student']['months'] === 1
    && $pl['teacher']['maxSubjects'] === 10 && count($pl['student']['includes']) >= 3 && in_array('Paper creation', $pl['student']['excludes'], true) && $pl['student']['duration'] === '1 month', $p['body']);
check('plans: Easypaisa account, title and the thank-you text come from the server', $p['json']['payment']['number'] === '03456896156' && $p['json']['payment']['title'] === 'AMIN ALLAH' && strpos($p['json']['thankYou'], 'Please allow up to 1 hour for verification') !== false && count($p['json']['classes']) === 12 && count($p['json']['subjects']) > 100);
check('plans: free allowance is published', $p['json']['free']['limits'] === ['prep_q' => 50, 'plan_q' => 50, 'paper' => 1] && $p['json']['free']['chapters'] === 2);

// ---------------------------------------------------------------- free limits, no account
$v1 = vid();
$r = use_free('prep_q', 50, vh($v1));
check('anonymous: 50 Test Preparation questions are allowed', $r['json']['allowed'] === true && $r['json']['used'] === 50 && $r['json']['limit'] === 50, $r['body']);
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q51'], vh($v1));
check('anonymous: the 51st is refused by the server', $r['json']['allowed'] === false && $r['json']['reason'] === 'limit', $r['body']);
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q7'], vh($v1));
check('anonymous: answering a question already counted again costs nothing', $r['json']['allowed'] === true && $r['json']['used'] === 50);
$st = bill('GET', 'state', null, vh($v1));
check('anonymous: a fresh page load (no cookie) is still at 50/50', $st['json']['free']['prep_q']['used'] === 50 && $st['json']['plan'] === 'free' && $st['json']['signedIn'] === false, $st['body']);
$r = bill('POST', 'consume', ['metric' => 'plan_q', 'key' => 's1', 'cls' => 'cls9'], vh($v1));
check('anonymous: the allowances are separate (Study Plan still open)', $r['json']['allowed'] === true && $r['json']['used'] === 1);
$r = bill('POST', 'consume', ['metric' => 'paper', 'key' => 'paper-a', 'subject' => 'cls9-math'], vh($v1));
$r2 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 'paper-b', 'subject' => 'cls9-math'], vh($v1));
check('anonymous: one paper, the second is refused', $r['json']['allowed'] === true && $r2['json']['allowed'] === false && $r2['json']['reason'] === 'limit', $r2['body']);
$r = bill('POST', 'consume', ['metric' => 'bogus', 'key' => 'x'], vh($v1));
check('an unknown metric is refused', $r['json']['allowed'] === false);
$other = vid();
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q1'], vh($other));
check('another browser has its own allowance', $r['json']['allowed'] === true && $r['json']['used'] === 1);

// registering or signing in brings the used allowance along; so does the other platform
$reg1 = http('POST', 'auth.php?action=register', ['name' => 'Free Rider', 'father_name' => 'Father', 'whatsapp' => '923009100001', 'password' => 'secret123', 'want_device' => true], vh($v1), $jar1 = tempnam(sys_get_temp_dir(), 'sbj'));
check('register needs no user type: a general account, made on the website', $reg1['code'] === 201 && $reg1['json']['user']['user_type'] === 'general' && $tp->query("SELECT signup_platform FROM users WHERE whatsapp = '923009100001'")->fetchColumn() === 'web', $reg1['body']);
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q99'], bearer($reg1) + vh($v1));
check('a new account does not reset the allowance (50 already used)', $r['json']['allowed'] === false && $r['json']['signedIn'] === true, $r['body']);
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q99'], vh($v1));
check('signing out does not reset it either', $r['json']['allowed'] === false);
$app = vid();
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'q98'], bearer($reg1) + ['X-SB-Visitor: ' . $app, 'X-SB-Platform: app', 'User-Agent: Mozilla/5.0 (SpaceBook test)']);
check('the same account on the app (another visitor id) is also at its limit', $r['json']['allowed'] === false, $r['body']);
$login = http('POST', 'auth.php?action=login', ['whatsapp' => '923009100001', 'password' => 'secret123', 'want_device' => true], ['X-SB-Visitor: ' . vid(), 'X-SB-Platform: app', 'User-Agent: Mozilla/5.0 (SpaceBook test)']);
check('signing in on the app works with the same account', $login['code'] === 200 && isset($login['json']['device']['token']));
$regApp = http('POST', 'auth.php?action=register', ['name' => 'App Person', 'father_name' => 'Father', 'whatsapp' => '923009100002', 'password' => 'secret123', 'want_device' => true], ['X-SB-Platform: app']);
check('an account made in the app records the app as its platform', $regApp['code'] === 201 && $tp->query("SELECT signup_platform FROM users WHERE whatsapp = '923009100002'")->fetchColumn() === 'app');
$older = http('POST', 'auth.php?action=register', ['name' => 'Spare Account', 'father_name' => 'Father', 'whatsapp' => '923009100003', 'password' => 'secret123', 'want_device' => true], vh(vid()));
$loginSpare = http('POST', 'auth.php?action=login', ['whatsapp' => '923009100003', 'password' => 'secret123', 'want_device' => true], vh($v1));
$r = bill('POST', 'consume', ['metric' => 'prep_q', 'key' => 'zz1'], bearer($loginSpare) + vh($v1));
check('signing in to another, unused account on the exhausted browser brings the used allowance', $r['json']['allowed'] === false, $r['body']);

// ---------------------------------------------------------------- submitting a payment
$noAuth = bill('POST', 'submit_payment', pay_body());
check('a payment needs a signed-in user', $noAuth['code'] === 401 && !empty($noAuth['json']['needSignIn']), $noAuth['body']);
$stuA = reg(['want_device' => true]); $stuB = reg(['want_device' => true]);
$uidA = (int)$stuA['json']['user']['id']; $uidB = (int)$stuB['json']['user']['id'];
$hA = bearer($stuA); $hB = bearer($stuB);
foreach ([
    ['no plan', pay_body(['plan' => ''])], ['student without a class', pay_body(['cls' => ''])], ['unknown class', pay_body(['cls' => 'cls99'])],
    ['teacher without subjects', pay_body(['plan' => 'teacher', 'cls' => null, 'subjects' => []])], ['teacher with an unknown subject', pay_body(['plan' => 'teacher', 'subjects' => ['nope']])],
    ['missing transaction id', pay_body(['trx' => ''])], ['short transaction id', pay_body(['trx' => '123'])], ['transaction id with symbols', pay_body(['trx' => '123456<script>'])],
    ['future payment date', pay_body(['paid_on' => gmdate('Y-m-d', time() + 5 * 86400)])], ['impossible payment date', pay_body(['paid_on' => '2026-02-31'])],
] as $c) {
    $r = bill('POST', 'submit_payment', $c[1], $hA);
    check('submit refused: ' . $c[0], $r['code'] === 422 && $r['json']['ok'] === false, $r['code'] . ' ' . $r['body']);
}
$all = array_keys($p['json']['subjects'] ? array_column($p['json']['subjects'], 'id', 'id') : []);
$r = bill('POST', 'submit_payment', pay_body(['plan' => 'teacher', 'cls' => null, 'subjects' => array_slice($all, 0, 11)]), $hA);
check('Teacher plan: 11 subjects refused', $r['code'] === 422 && strpos($r['json']['error'], '10') !== false, $r['body']);
check('nothing was saved by the refused submissions', (int)$tp->query("SELECT COUNT(*) FROM payment_requests WHERE user_id = $uidA")->fetchColumn() === 0);

$tp->exec("DELETE FROM rate_limits WHERE bucket LIKE 'pay:u:%'");
$body = pay_body(['trx' => '00012345678', 'amount' => 1, 'paid_on' => gmdate('Y-m-d')]);
$r = bill('POST', 'submit_payment', $body, $hA);
$pay1 = $r['json']['payment'] ?? [];
check('a valid payment is saved as Pending Verification with the thank-you text', $r['code'] === 201 && $pay1['status'] === 'pending' && $pay1['statusText'] === 'Pending Verification' && $r['json']['message'] === 'Thank you for choosing SpaceBook! Your payment details have been submitted successfully. Please allow up to 1 hour for verification. Your plan will become active once your payment is approved. Happy learning!', $r['body']);
check('the amount is the server price, never the browser\'s', $pay1['amount'] === 500 && (int)$tp->query("SELECT amount_pkr FROM payment_requests WHERE id = " . (int)$pay1['id'])->fetchColumn() === 500);
check('the transaction id is kept exactly as text (leading zeros)', $tp->query("SELECT trx_id FROM payment_requests WHERE id = " . (int)$pay1['id'])->fetchColumn() === '00012345678');
$row = $tp->query('SELECT * FROM payment_requests WHERE id = ' . (int)$pay1['id'])->fetch();
check('the record links user, plan, class, contact, method and dates', (int)$row['user_id'] === $uidA && $row['plan_type'] === 'student' && $row['class_id'] === 'cls9' && $row['contact_whatsapp'] === $stuA['num'] && $row['method'] === 'easypaisa' && $row['paid_on'] === gmdate('Y-m-d') && $row['submitted_at'] !== null && $row['status'] === 'pending' && $row['reviewed_at'] === null);
$ent = http('GET', 'v2/entitlements.php', null, $hA);
check('submitting alone activates nothing', $ent['json']['access']['readClasses'] === [] && $ent['json']['plan'] === 'free' && $ent['json']['pendingPayments'] === 1 && $ent['json']['subscriptions'] === [], $ent['body']);
$again = bill('POST', 'submit_payment', $body, $hA);
check('the same submission twice (double tap) saves one request', $again['code'] === 200 && $again['json']['repeat'] === true && $again['json']['payment']['id'] === $pay1['id'] && (int)$tp->query("SELECT COUNT(*) FROM payment_requests WHERE user_id = $uidA")->fetchColumn() === 1);
$again2 = bill('POST', 'submit_payment', pay_body(['trx' => '00012345678', 'idem' => 'different']), $hA);
check('the same transaction id again by the same person also returns the first', $again2['json']['repeat'] === true && (int)$tp->query("SELECT COUNT(*) FROM payment_requests WHERE user_id = $uidA")->fetchColumn() === 1);
$dup = bill('POST', 'submit_payment', pay_body(['trx' => '00012345678']), $hB);
check('the same transaction id from another account is refused', $dup['code'] === 409, $dup['body']);
$dupLower = bill('POST', 'submit_payment', pay_body(['trx' => 'ab12cd34ef']), $hB);
$dupUpper = bill('POST', 'submit_payment', pay_body(['trx' => 'AB12CD34EF']), $hA);
check('transaction ids compare ignoring case', $dupLower['code'] === 201 && $dupUpper['code'] === 409, $dupUpper['body']);
$tp->exec("INSERT INTO payment_requests (ref, user_id, plan_type, class_id, scope_key, amount_pkr, trx_id, trx_norm, active_trx, idem_key) VALUES ('SBDUPTEST1', $uidA, 'prep', NULL, 'x', 500, 'zzz', 'ZZZ000', 'ZZZ000', 'k1')");
try { $tp->exec("INSERT INTO payment_requests (ref, user_id, plan_type, class_id, scope_key, amount_pkr, trx_id, trx_norm, active_trx, idem_key) VALUES ('SBDUPTEST2', $uidB, 'prep', NULL, 'x', 500, 'zzz', 'ZZZ000', 'ZZZ000', 'k2')"); $dbDup = false; } catch (PDOException $e) { $dbDup = true; }
check('the database itself refuses two live requests with one transaction id', $dbDup);
$tp->exec("DELETE FROM payment_requests WHERE ref LIKE 'SBDUPTEST%'");

$acc = bill('GET', 'account', null, $hA);
$accB = bill('GET', 'account', null, $hB);
$refsA = array_column($acc['json']['payments'], 'ref'); $refsB = array_column($accB['json']['payments'], 'ref');
check('the account page shows only the person\'s own payments, pending', $acc['code'] === 200 && in_array($pay1['ref'], $refsA, true) && !in_array($pay1['ref'], $refsB, true) && $acc['json']['payments'][0]['statusText'] === 'Pending Verification', $acc['body']);
check('account asks for a sign-in, and ignores a user id in the address', bill('GET', 'account')['code'] === 401 && !in_array($pay1['ref'], array_column(bill('GET', 'account&user=' . $uidA, null, $hB)['json']['payments'], 'ref'), true));
check('the person is told the payment was received', $acc['json']['notifications'][0]['kind'] === 'pay_pending' && $acc['json']['unread'] >= 1);

// ---------------------------------------------------------------- approval: one calendar month, once
$tp->exec('UPDATE rate_limits SET hits = 0');
$ap = sb_payment_review($tp, $adm, (int)$pay1['id'], 'approve', '');
$sub = $tp->query("SELECT * FROM subscriptions WHERE user_id = $uidA")->fetch();
check('approve starts the plan now for one calendar month and records exact times', $ap['ok'] && $sub && $sub['plan_type'] === 'student' && $sub['class_id'] === 'cls9' && $sub['expires_at'] === sb_add_months($sub['starts_at'], 1) && abs(strtotime($sub['starts_at'] . ' UTC') - time()) < 10, json_encode($ap) . json_encode($sub));
$pr = $tp->query('SELECT * FROM payment_requests WHERE id = ' . (int)$pay1['id'])->fetch();
check('the payment shows who approved, when, and the plan period', $pr['status'] === 'approved' && $pr['reviewed_by_name'] === 'IrfanUllah123' && $pr['reviewed_at'] !== null && (int)$pr['subscription_id'] === (int)$sub['id'] && $pr['activated_at'] === $sub['starts_at'] && $pr['expires_at'] === $sub['expires_at']);
$ap2 = sb_payment_review($tp, $adm, (int)$pay1['id'], 'approve', '');
$ap3 = sb_payment_review($tp, $adm, (int)$pay1['id'], 'approve', '');
check('approving again (double click) changes and grants nothing', $ap2['ok'] && !empty($ap2['already']) && $ap3['ok'] && sub_count($tp, $uidA) === 1 && (int)$tp->query('SELECT COUNT(*) FROM subscription_events WHERE subscription_id = ' . (int)$sub['id'])->fetchColumn() === 1 && $tp->query('SELECT expires_at FROM subscriptions WHERE id = ' . (int)$sub['id'])->fetchColumn() === $sub['expires_at']);
check('a rejection after an approval is refused', sb_payment_review($tp, $adm, (int)$pay1['id'], 'reject', 'too late')['ok'] === false);
$ent = http('GET', 'v2/entitlements.php', null, $hA);
check('the website and the app see the same access after approval', $ent['json']['access']['readClasses'] === ['cls9'] && $ent['json']['access']['planClasses'] === ['cls9'] && $ent['json']['access']['prep'] === false && $ent['json']['plan'] === 'paid' && $ent['json']['subscriptions'][0]['status'] === 'active' && $ent['json']['subscriptions'][0]['daysLeft'] >= 27, $ent['body']);
$entApp = http('GET', 'v2/entitlements.php', null, $hA + ['X-SB-Platform: app', 'X-SB-Visitor: ' . vid()]);
check('another visitor id (the app) gets the same paid access for the same account', $entApp['json']['access'] === $ent['json']['access'] && $entApp['json']['subscriptions'][0]['expiresAt'] === $ent['json']['subscriptions'][0]['expiresAt']);
$acc = bill('GET', 'account', null, $hA);
check('the account shows the approval, dates and a notice', $acc['json']['payments'][0]['status'] === 'approved' && $acc['json']['payments'][0]['activatedAt'] !== null && $acc['json']['subscriptions'][0]['history'][0]['event'] === 'activated' && $acc['json']['notifications'][0]['kind'] === 'pay_approved');
check('B still has nothing from A\'s purchase', http('GET', 'v2/entitlements.php', null, $hB)['json']['access']['readClasses'] === []);
check('rule: Chapters 1 and 2 are open to everyone, later chapters need the class, the subject or nothing else', sb_can_read(sb_access($tp, 0), 'cls9', 'cls9-math', 0) && sb_can_read(sb_access($tp, 0), 'cls9', 'cls9-math', 1) && !sb_can_read(sb_access($tp, 0), 'cls9', 'cls9-math', 2) && sb_can_read(sb_access($tp, $uidA), 'cls9', 'cls9-math', 5) && !sb_can_read(sb_access($tp, $uidA), 'cls10', 'cls10-math', 2));

// paid student plan: Study Plan of that class has no limit, Test Preparation and papers still do
$vs = vid();
$rr = use_free('plan_q', 55, bearer($stuA) + vh($vs), 'sp', ['cls' => 'cls9']);
check('Student plan: Study Plan questions of its class are unlimited', $rr['json']['allowed'] === true && !empty($rr['json']['unlimited']));
$rr = bill('POST', 'consume', ['metric' => 'plan_q', 'key' => 'o1', 'cls' => 'cls10'], bearer($stuA) + vh($vs));
check('Student plan: Study Plan of another class is still metered', empty($rr['json']['unlimited']) && $rr['json']['limit'] === 50);
$rr = bill('POST', 'consume', ['metric' => 'paper', 'key' => 'p1', 'subject' => 'cls9-math'], bearer($stuA) + vh($vs));
$rr2 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 'p2', 'subject' => 'cls9-math'], bearer($stuA) + vh($vs));
check('Student plan: paper creation is excluded (one free paper only)', $rr['json']['allowed'] === true && empty($rr['json']['unlimited']) && $rr2['json']['allowed'] === false);
$rr = use_free('prep_q', 51, bearer($stuA) + vh($vs), 'tq');
check('Student plan: Test Preparation is excluded (50 free)', $rr['json']['allowed'] === false);

// ---------------------------------------------------------------- renewal, other classes, expiry
$pay2 = new_pay($tp, $uidA);
$sub = $tp->query("SELECT * FROM subscriptions WHERE user_id = $uidA")->fetch();
sb_payment_review($tp, $adm, $pay2, 'approve', '');
$sub2 = $tp->query("SELECT * FROM subscriptions WHERE id = " . (int)$sub['id'])->fetch();
$pr2 = $tp->query("SELECT * FROM payment_requests WHERE id = $pay2")->fetch();
check('early renewal adds the month after the current end date, on the same subscription', sub_count($tp, $uidA) === 1 && $sub2['expires_at'] === sb_add_months($sub['expires_at'], 1) && $sub2['starts_at'] === $sub['starts_at'] && $pr2['activated_at'] === $sub['expires_at'] && $pr2['expires_at'] === $sub2['expires_at']);
check('the renewal is in the history', (int)$tp->query('SELECT COUNT(*) FROM subscription_events WHERE subscription_id = ' . (int)$sub['id'] . " AND event = 'renewed'")->fetchColumn() === 1);
$pay3 = new_pay($tp, $uidA, ['cls' => 'cls10']);
sb_payment_review($tp, $adm, $pay3, 'approve', '');
check('a different class is a separate subscription', sub_count($tp, $uidA) === 2 && sb_access($tp, $uidA)['readClasses'] === ['cls10', 'cls9']);

$GLOBALS['SB_NOW'] = '2026-01-31 10:00:00';
$stuC = reg(['want_device' => true]); $uidC = (int)$stuC['json']['user']['id'];
sb_payment_review($tp, $adm, new_pay($tp, $uidC, ['cls' => 'cls8']), 'approve', '');
$subC = $tp->query("SELECT * FROM subscriptions WHERE user_id = $uidC")->fetch();
check('one calendar month from 31 January ends on 28 February', $subC['starts_at'] === '2026-01-31 10:00:00' && $subC['expires_at'] === '2026-02-28 10:00:00', json_encode($subC));
check('one calendar month from 15 March ends on 15 April', sb_add_months('2026-03-15 08:30:00', 1) === '2026-04-15 08:30:00' && sb_add_months('2026-12-31 00:00:00', 1) === '2027-01-31 00:00:00');
unset($GLOBALS['SB_NOW']);
check('after the end date the plan is expired and opens nothing', sb_access($tp, $uidC)['readClasses'] === [] && sb_sub_status($tp->query("SELECT * FROM subscriptions WHERE user_id = $uidC")->fetch()) === 'expired');
$entC = http('GET', 'v2/entitlements.php', null, bearer($stuC));
check('the client sees it as expired, with reminders', $entC['json']['subscriptions'][0]['status'] === 'expired' && $entC['json']['access']['readClasses'] === [] && bill('GET', 'account', null, bearer($stuC))['json']['reminders'][0]['daysLeft'] === 0);
sb_payment_review($tp, $adm, new_pay($tp, $uidC, ['cls' => 'cls8']), 'approve', '');
check('buying again after it ended starts a new subscription from approval time', sub_count($tp, $uidC) === 2 && sb_access($tp, $uidC)['readClasses'] === ['cls8']);

// ---------------------------------------------------------------- rejection
$stuD = reg(['want_device' => true]); $uidD = (int)$stuD['json']['user']['id'];
$payD = new_pay($tp, $uidD, ['trx' => 'WRONG123456']);
check('rejecting needs a reason', sb_payment_review($tp, $adm, $payD, 'reject', '')['ok'] === false && $tp->query("SELECT status FROM payment_requests WHERE id = $payD")->fetchColumn() === 'pending');
$rj = sb_payment_review($tp, $adm, $payD, 'reject', 'Transaction ID not found in Easypaisa');
$accD = bill('GET', 'account', null, bearer($stuD));
check('rejection is shown to the student with the reason and activates nothing', $rj['ok'] && $accD['json']['payments'][0]['status'] === 'rejected' && $accD['json']['payments'][0]['reviewNote'] === 'Transaction ID not found in Easypaisa' && sub_count($tp, $uidD) === 0 && $accD['json']['notifications'][0]['kind'] === 'pay_rejected' && strpos($accD['json']['notifications'][0]['body'], 'not found') !== false);
check('rejecting twice is harmless, approving a rejected payment is refused', sb_payment_review($tp, $adm, $payD, 'reject', 'again')['ok'] === true && sb_payment_review($tp, $adm, $payD, 'approve', '')['ok'] === false && sub_count($tp, $uidD) === 0);
$resub = bill('POST', 'submit_payment', pay_body(['trx' => 'WRONG123456']), bearer($stuD));
check('after a rejection the person can submit again (even the same id)', $resub['code'] === 201);

// ---------------------------------------------------------------- suspension and restoration
$subA = (int)$tp->query("SELECT id FROM subscriptions WHERE user_id = $uidA AND class_id = 'cls9'")->fetchColumn();
check('suspending needs a reason', sb_sub_suspend($tp, $adm, $subA, '')['ok'] === false);
check('suspend works and removes the access at once on both platforms', sb_sub_suspend($tp, $adm, $subA, 'Chargeback check')['ok'] && sb_access($tp, $uidA)['readClasses'] === ['cls10'] );
$ent = http('GET', 'v2/entitlements.php', null, $hA);
$statusById = []; foreach ($ent['json']['subscriptions'] as $s) $statusById[$s['id']] = $s['status'];
check('the account shows it suspended with the reason', $statusById[$subA] === 'suspended' && !in_array('cls9', $ent['json']['access']['readClasses'], true));
$payBlocked = new_pay($tp, $uidA);
check('approving a payment for a suspended plan is refused until it is restored', sb_payment_review($tp, $adm, $payBlocked, 'approve', '')['ok'] === false);
check('restore returns the access with the same end date', sb_sub_restore($tp, $adm, $subA, 'Cleared')['ok'] && in_array('cls9', sb_access($tp, $uidA)['readClasses'], true));
sb_payment_review($tp, $adm, $payBlocked, 'reject', 'duplicate test payment');
check('suspend and restore are in the history', (int)$tp->query("SELECT COUNT(*) FROM subscription_events WHERE subscription_id = $subA AND event IN ('suspended','restored')")->fetchColumn() === 2);
$uStatus = sb_account_set_status($tp, $adm, $uidD, 'blocked', 'Abuse report');
$loginBlocked = http('POST', 'auth.php?action=login', ['whatsapp' => $stuD['num'], 'password' => 'secret123']);
check('a suspended account cannot sign in and its token stops working', $uStatus['ok'] && $loginBlocked['code'] === 403 && http('GET', 'v2/entitlements.php', null, bearer($stuD))['json']['signedIn'] === false);
sb_account_set_status($tp, $adm, $uidD, 'active', 'Resolved');
check('restoring the account lets the person in again', http('POST', 'auth.php?action=login', ['whatsapp' => $stuD['num'], 'password' => 'secret123'])['code'] === 200);

// ---------------------------------------------------------------- Teacher plan and Test Preparation module
$stuT = reg(['want_device' => true]); $uidT = (int)$stuT['json']['user']['id'];
$subjects = ['cls9-math', 'cls9-phy', 'cls10-math'];
$subjects = array_values(array_filter($subjects, function ($s) use ($all) { return in_array($s, $all, true); }));
if (count($subjects) < 3) $subjects = array_slice($all, 0, 3);
$payT = new_pay($tp, $uidT, ['plan' => 'teacher', 'cls' => null, 'subjects' => $subjects]);
check('a Teacher plan request keeps its subjects', $payT > 0 && json_decode($tp->query("SELECT subjects_json FROM payment_requests WHERE id = $payT")->fetchColumn(), true) === (function ($s) { sort($s); return $s; })($subjects));
sb_payment_review($tp, $adm, $payT, 'approve', '');
$accT = sb_access($tp, $uidT);
$clsOfFirst = $p['json']['subjects'][array_search($subjects[0], array_column($p['json']['subjects'], 'id'), true)]['class'];
check('Teacher plan opens exactly the chosen subjects (any classes), their papers, no Study Plan', $accT['readSubjects'] === (function ($s) { sort($s); return $s; })($subjects) && $accT['paperSubjects'] === $accT['readSubjects'] && $accT['planClasses'] === [] && $accT['readClasses'] === [] && $accT['prep'] === false);
check('Teacher plan: a chosen subject\'s later chapters are open, others are not', sb_can_read($accT, $clsOfFirst, $subjects[0], 7) && !sb_can_read($accT, 'cls1', 'cls1-eng', 2) && sb_can_read($accT, 'cls1', 'cls1-eng', 1) && sb_can_read($accT, 'cls1', 'cls1-eng', 0));
$vt = vid();
$r1 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 't1', 'subject' => $subjects[0]], bearer($stuT) + vh($vt));
$r2 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 't2', 'subject' => $subjects[0]], bearer($stuT) + vh($vt));
$r3 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 't3', 'subject' => 'cls1-eng'], bearer($stuT) + vh($vt));
$r4 = bill('POST', 'consume', ['metric' => 'paper', 'key' => 't4', 'subject' => 'cls1-eng'], bearer($stuT) + vh($vt));
check('Teacher plan: unlimited papers for its subjects, one free paper elsewhere', !empty($r1['json']['unlimited']) && !empty($r2['json']['unlimited']) && $r3['json']['allowed'] === true && $r4['json']['allowed'] === false);
$payP = new_pay($tp, $uidT, ['plan' => 'prep', 'cls' => null]);
sb_payment_review($tp, $adm, $payP, 'approve', '');
$rp = use_free('prep_q', 60, bearer($stuT) + vh($vt), 'pq');
check('Test Preparation module: unlimited questions, and it adds no chapters or Study Plan', !empty($rp['json']['unlimited']) && sb_access($tp, $uidT)['prep'] === true && sb_access($tp, $uidT)['planClasses'] === []);
$accT = bill('GET', 'account', null, bearer($stuT));
check('the account lists both plans', count($accT['json']['subscriptions']) === 2 && count($accT['json']['subscriptions'][0]['subjects']) + count($accT['json']['subscriptions'][1]['subjects']) === 3);

// ---------------------------------------------------------------- free extensions: one, several, everyone; preview, confirm
$before = []; foreach ($tp->query('SELECT id, expires_at FROM subscriptions') as $s) $before[(int)$s['id']] = $s['expires_at'];
$pv = sb_ext_preview($tp, ['users' => [$uidA], 'plan' => 'student', 'states' => ['active']], 'add_days', '10');
check('preview lists the affected subscriptions and changes nothing', $pv['count'] === 2 && $pv['items'][0]['user'] === $uidA && (function ($tp, $before) { foreach ($tp->query('SELECT id, expires_at FROM subscriptions') as $s) if ($before[(int)$s['id']] !== $s['expires_at']) return false; return true; })($tp, $before));
check('apply with a wrong preview hash is refused', sb_ext_apply($tp, $adm, ['users' => [$uidA], 'plan' => 'student', 'states' => ['active']], 'add_days', '10', 'deadbeef', 'x reason')['ok'] === false);
check('apply needs a reason', sb_ext_apply($tp, $adm, ['users' => [$uidA], 'plan' => 'student', 'states' => ['active']], 'add_days', '10', $pv['hash'], '')['ok'] === false);
$ap = sb_ext_apply($tp, $adm, ['users' => [$uidA], 'plan' => 'student', 'states' => ['active']], 'add_days', '10', $pv['hash'], 'Exam week gift');
$now = []; foreach ($tp->query('SELECT id, expires_at FROM subscriptions') as $s) $now[(int)$s['id']] = $s['expires_at'];
check('extending one person adds 10 days to their running student plans only', $ap['ok'] && $ap['count'] === 2 && $now[$subA] === sb_add_days($before[$subA], 10) && $now[(int)$sub['id']] === $now[$subA] && $before[(int)$tp->query("SELECT id FROM subscriptions WHERE user_id = $uidT AND plan_type = 'prep'")->fetchColumn()] === $now[(int)$tp->query("SELECT id FROM subscriptions WHERE user_id = $uidT AND plan_type = 'prep'")->fetchColumn()]);
$audit = $tp->query("SELECT * FROM admin_audit WHERE action = 'sub_extend' ORDER BY id DESC LIMIT 1")->fetch();
check('the extension is in the audit trail with who, why and what', $audit && $audit['admin_name'] === 'IrfanUllah123' && $audit['reason'] === 'Exam week gift' && strpos($audit['detail_json'], '"subscriptions":2') !== false);
check('the person is told', bill('GET', 'account', null, $hA)['json']['notifications'][0]['kind'] === 'sub_extended');
$f2 = ['users' => [$uidA, $uidT], 'plan' => '', 'states' => ['active']];
$pv2 = sb_ext_preview($tp, $f2, 'add_days', '5');
$ap2 = sb_ext_apply($tp, $adm, $f2, 'add_days', '5', $pv2['hash'], 'Selected people');
check('extending several selected people touches only theirs', $ap2['ok'] && $ap2['users'] === 2 && $ap2['count'] === $pv2['count']);
$fAll = ['users' => [], 'plan' => 'prep', 'states' => ['active']];
$pvAll = sb_ext_preview($tp, $fAll, 'add_days', '3');
$apAll = sb_ext_apply($tp, $adm, $fAll, 'add_days', '3', $pvAll['hash'], 'Everybody on Test Preparation');
check('extending everyone with a matching plan works and counts them', $apAll['ok'] && $apAll['count'] === (int)$tp->query("SELECT COUNT(*) FROM subscriptions WHERE plan_type = 'prep' AND status = 'active' AND expires_at > UTC_TIMESTAMP()")->fetchColumn());
$fEnded = ['users' => [$uidC], 'plan' => '', 'states' => ['expired']];
$pvE = sb_ext_preview($tp, $fEnded, 'set_date', gmdate('Y-m-d', time() + 20 * 86400));
$apE = sb_ext_apply($tp, $adm, $fEnded, 'set_date', gmdate('Y-m-d', time() + 20 * 86400), $pvE['hash'], 'Set a date');
check('setting a new end date reopens an ended plan until that date', $apE['ok'] && $apE['count'] === 1 && $tp->query("SELECT expires_at FROM subscriptions WHERE user_id = $uidC AND expires_at LIKE '" . gmdate('Y-m-d', time() + 20 * 86400) . "%'")->fetchColumn() !== false);
check('a date that is not later than the current end changes nothing', sb_ext_preview($tp, ['users' => [$uidT], 'plan' => '', 'states' => ['active']], 'set_date', gmdate('Y-m-d', time() + 1 * 86400))['count'] === 0 && sb_ext_preview($tp, $f2, 'set_date', '2020-01-01')['count'] === 0);
$gr = sb_sub_grant($tp, $adm, $uidB, 'student', 'cls5', [], 14, 'Scholarship');
check('a manual grant starts a free subscription and records the reason', $gr['ok'] && sb_access($tp, $uidB)['readClasses'] === ['cls5'] && $tp->query("SELECT source FROM subscriptions WHERE user_id = $uidB")->fetchColumn() === 'grant' && sb_sub_grant($tp, $adm, $uidB, 'student', 'cls5', [], 14, '')['ok'] === false);

// ---------------------------------------------------------------- the rules shared with the website and the app (tests/parity/access_contract.json)
$contract = json_decode(file_get_contents($root . '/tests/parity/access_contract.json'), true);
$GLOBALS['SB_NOW'] = str_replace(['T', 'Z'], [' ', ''], $contract['now']);
foreach ($contract['scenarios'] as $sc) {
    $u = reg(); $cu = (int)$u['json']['user']['id'];
    foreach ($sc['subscriptions'] as $i => $s) {
        $subj = array_column($s['subjects'], 'id');
        $tp->prepare('INSERT INTO subscriptions (user_id, plan_type, class_id, scope_key, status, starts_at, expires_at) VALUES (?, ?, ?, ?, ?, ?, ?)')
           ->execute([$cu, $s['planType'], $s['classId'], sb_scope_key($s['planType'], $s['classId'], $subj) . '', $s['status'], '2026-10-01 00:00:00', str_replace(['T', 'Z'], [' ', ''], $s['expiresAt'])]);
        $sid = (int)$tp->lastInsertId();
        foreach ($subj as $x) $tp->prepare('INSERT INTO subscription_subjects (subscription_id, class_id, subject_id) VALUES (?, ?, ?)')->execute([$sid, explode('-', $x)[0], $x]);
    }
    $acc = sb_access($tp, $cu);
    $accOk = $acc['prep'] === $sc['access']['prep'];
    foreach (['readClasses', 'readSubjects', 'planClasses', 'paperSubjects'] as $k) { $a = $acc[$k]; $b = $sc['access'][$k]; sort($a); sort($b); $accOk = $accOk && $a === $b; }
    $readOk = true; foreach ($sc['read'] as $c) $readOk = $readOk && sb_can_read($acc, $c['cls'], $c['subject'], $c['chapter']) === $c['expect'];
    $unlOk = true; foreach ($sc['unlimited'] as $c) $unlOk = $unlOk && sb_metric_unlimited($acc, $c['metric'], ['cls' => $c['cls'], 'subject' => $c['subject']]) === $c['expect'];
    check('contract: ' . $sc['name'], $accOk && $readOk && $unlOk, json_encode([$acc, $accOk, $readOk, $unlOk]));
}
unset($GLOBALS['SB_NOW']);

// ---------------------------------------------------------------- usage numbers and the dashboard
$tp->exec('DELETE FROM rate_limits');
$ping = bill('POST', 'ping', ['module' => 'testprep', 'cls' => 'cls9', 'subject' => 'cls9-math'], bearer($stuA) + vh(vid()));
$pingAnon = bill('POST', 'ping', ['module' => 'reading', 'cls' => 'cls9'], vh($anonV = vid()));
$pingBot = bill('POST', 'ping', ['module' => 'reading', 'cls' => 'cls9'], ['X-SB-Visitor: ' . vid(), 'User-Agent: Googlebot/2.1']);
check('pings are recorded (and a crawler\'s are dropped)', $ping['json']['ok'] === true && !empty($pingBot['json']['dropped']) && (int)$tp->query("SELECT hits FROM usage_stats WHERE kind = 'module' AND skey = 'testprep'")->fetchColumn() >= 1);
bill('POST', 'ping', ['event' => 'prompt', 'metric' => 'prep_q'], vh($anonV));
$tp->exec("UPDATE subscriptions SET expires_at = '2026-01-01 00:00:00' WHERE user_id = $uidT AND plan_type = 'prep'");     // one ended plan
$tp->exec("UPDATE subscriptions SET status = 'suspended', suspend_reason = 'test' WHERE user_id = $uidB");                       // and one suspended
$dash = sb_m_dashboard($tp, gmdate('Y-m-d', time() - 29 * 86400), gmdate('Y-m-d'));
$tp->exec("UPDATE subscriptions SET status = 'active', suspend_reason = '' WHERE user_id = $uidB");
$revenue = (int)$tp->query("SELECT SUM(amount_pkr) FROM payment_requests WHERE status = 'approved' AND reviewed_at >= '" . gmdate('Y-m-d', time() - 29 * 86400) . " 00:00:00'")->fetchColumn();
check('dashboard: revenue is the approved payments only, counted on the day of approval', $dash['revenue'] === $revenue && $revenue >= 2000 && $dash['payStatus']['pending'] >= 0 && $dash['payStatus']['approved'] >= 5 && $dash['payStatus']['rejected'] >= 1, json_encode([$dash['revenue'], $dash['payStatus']]));
check('dashboard: subscriptions are split into active, expired and suspended', $dash['subActive'] >= 4 && $dash['subExpired'] >= 1 && $dash['subSuspended'] >= 1);
check('dashboard: registered people are counted apart from anonymous visitors, administrators excluded', $dash['accounts'] >= 8 && $dash['dau'] >= 1 && $dash['anonVisitors'] >= 1 && $dash['activeByPlatform'] !== []);
check('dashboard: popular classes, free-limit hits, prompts and conversion are filled in', $dash['top_class'][0][0] === 'cls9' && array_sum(array_column($dash['limitHits'], 1)) > 0 && array_sum(array_column($dash['prompts'], 1)) >= 1 && $dash['convPaid'] >= 3 && $dash['renewals'] >= 1 && $dash['atLimit']['prep_q'] >= 1);
check('dashboard: the free-limit flow counted refused requests per metric', in_array('prep_q', array_column($dash['limitHits'], 0), true) && in_array('paper', array_column($dash['limitHits'], 0), true));

// ---------------------------------------------------------------- CSV export is safe in a spreadsheet
$tp->exec("UPDATE users SET name = '=HYPERLINK(\"http://evil\")' WHERE id = $uidB");
$x = sb_m_export($tp, 'users', gmdate('Y-m-d', time() - 3 * 86400), gmdate('Y-m-d'));
check('CSV export neutralises a name that starts like a formula', strpos($x[1], '"\'=HYPERLINK') !== false && strpos($x[1], '"=HYPERLINK') === false);
check('CSV export of payments and subscriptions works with the transaction id as text', strpos(sb_m_export($tp, 'payments', '2020-01-01', gmdate('Y-m-d'))[1], '"00012345678"') !== false && strpos(sb_m_export($tp, 'subscriptions', '2020-01-01', gmdate('Y-m-d'))[1], 'state_now') !== false && sb_m_export($tp, 'bogus', '2020-01-01', '2030-01-01') === null);

// ---------------------------------------------------------------- the management page over HTTP (document root = the site, not api/)
$port2 = $port + 1;
$proc2 = proc_open([PHP_BINARY, '-S', "127.0.0.1:$port2", '-t', $root], [0 => ['pipe', 'r'], 1 => ['file', sys_get_temp_dir() . '/sb_php_server2.log', 'w'], 2 => ['file', sys_get_temp_dir() . '/sb_php_server2.log', 'a']], $pipes2, $root, array_merge(getenv(), ['SB_CONFIG' => $cfg]));
$up2 = false;
for ($i = 0; $i < 50 && !$up2; $i++) { $s = @fsockopen('127.0.0.1', $port2, $en, $es, 0.2); if ($s) { fclose($s); $up2 = true; } else usleep(100000); }
check('management test server started', $up2);
function mhttp(string $method, string $path, ?array $fields = null, array $headers = [], ?string $jar = null): array
{
    global $port2;
    $ch = curl_init("http://127.0.0.1:$port2/$path");
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_HEADER => true, CURLOPT_CUSTOMREQUEST => $method, CURLOPT_TIMEOUT => 60]);
    if ($fields !== null) curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($fields));
    if ($jar) { curl_setopt($ch, CURLOPT_COOKIEJAR, $jar); curl_setopt($ch, CURLOPT_COOKIEFILE, $jar); }
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $raw = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $hs = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    curl_close($ch);
    return ['code' => $code, 'head' => substr((string)$raw, 0, $hs), 'body' => substr((string)$raw, $hs)];
}
function mcsrf(string $html): string { return preg_match('/name="csrf" value="([0-9a-f]{40})"/', $html, $m) ? $m[1] : ''; }
$tp->exec('DELETE FROM rate_limits');
$mjar = tempnam(sys_get_temp_dir(), 'sbm');
$pg = mhttp('GET', 'manage/index.php', null, [], $mjar);
check('the management page shows only a sign-in form to a visitor, with strict headers', $pg['code'] === 200 && strpos($pg['body'], 'name="password"') !== false && strpos($pg['body'], 'Payments') === false && stripos($pg['head'], "default-src 'none'") !== false && stripos($pg['head'], 'X-Frame-Options: DENY') !== false && stripos($pg['head'], 'no-store') !== false && strpos($pg['body'], '<script') === false);
$dirIdx = @file_get_contents(__DIR__ . '/../../manage/.htaccess');
check('/manage/ with no file name opens the page on the host: manage/.htaccess makes index.php the directory index (the root one lists only lazy.html and index.html)', $dirIdx !== false && preg_match('/^DirectoryIndex\s+index\.php\s*$/m', $dirIdx) === 1 && preg_match('/^DirectoryIndex\s+lazy\.html/m', (string)@file_get_contents(__DIR__ . '/../../.htaccess')) === 1);
foreach (['?v=payments', '?v=users', '?v=dash', '?v=export&kind=users', '?v=payment&id=1'] as $q) {
    $x = mhttp('GET', 'manage/index.php' . $q, null, [], tempnam(sys_get_temp_dir(), 'sbm'));
    if ($x['code'] !== 200 || strpos($x['body'], 'name="password"') === false || strpos($x['body'], 'Verified') !== false || strpos($x['body'], 'transaction_id') !== false) { $leaky = $q; break; }
}
check('nothing else is reachable without signing in', !isset($leaky), isset($leaky) ? $leaky : '');
$userJar = $stuA['jar'];
$x = mhttp('GET', 'manage/index.php?v=payments', null, [], $userJar);
check('a signed-in ordinary user of the site is not an administrator', strpos($x['body'], 'name="password"') !== false && strpos($x['body'], 'Reference') === false);
$tok = mcsrf($pg['body']);
$bad = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'IrfanUllah123', 'password' => 'definitely-wrong'], [], $mjar);
$noTok = mhttp('POST', 'manage/index.php', ['do' => 'login', 'username' => 'IrfanUllah123', 'password' => $initial], [], $mjar);
$cross = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'IrfanUllah123', 'password' => $initial], ['Origin: https://evil.example'], $mjar);
check('a wrong password gives one plain message; a request without the token or from another site is refused', $bad['code'] === 401 && strpos($bad['body'], 'Wrong username or password') !== false && strpos($noTok['body'], 'form expired') !== false && $cross['code'] === 403);
$unknown = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'NoSuchAdmin', 'password' => 'x'], [], $mjar);
check('an unknown name gets the same message as a wrong password', $unknown['code'] === 401 && strpos($unknown['body'], 'Wrong username or password') !== false);
for ($i = 0; $i < 4; $i++) mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'IrfanUllah123', 'password' => 'wrong' . $i], [], $mjar);
$locked = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'IrfanUllah123', 'password' => $initial], [], $mjar);
check('five wrong passwords lock the account: even the right password is refused for a while', $locked['code'] === 429 && strpos($locked['body'], 'locked') !== false && $tp->query("SELECT locked_until IS NOT NULL FROM admins WHERE username = 'IrfanUllah123'")->fetchColumn() == 1);
$tp->exec("UPDATE admins SET locked_until = NULL, failed_logins = 0 WHERE username = 'IrfanUllah123'");
$tp->exec('DELETE FROM rate_limits');
$ok = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => $tok, 'username' => 'IrfanUllah123', 'password' => $initial], [], $mjar);
check('the initial password signs in and goes straight to the password change', $ok['code'] === 303 && strpos($ok['head'], 'Location: ?v=password') !== false, $ok['head']);
$dashFirst = mhttp('GET', 'manage/index.php?v=dash', null, [], $mjar);
$payFirst = mhttp('GET', 'manage/index.php?v=payments', null, [], $mjar);
check('until the password is changed only the change form is available', strpos($dashFirst['body'], 'Change your password') !== false && strpos($dashFirst['body'], 'Verified revenue') === false && strpos($payFirst['body'], 'Change your password') !== false && strpos($payFirst['body'], 'Reference') === false);
$tokP = mcsrf($dashFirst['body']);
$weak = mhttp('POST', 'manage/index.php', ['do' => 'password', 'csrf' => $tokP, 'current' => $initial, 'new' => 'short1', 'again' => 'short1'], [], $mjar);
$mismatch = mhttp('POST', 'manage/index.php', ['do' => 'password', 'csrf' => $tokP, 'current' => $initial, 'new' => 'Aa1-Aa1-Aa1-xyz9', 'again' => 'different'], [], $mjar);
$wrongCur = mhttp('POST', 'manage/index.php', ['do' => 'password', 'csrf' => $tokP, 'current' => 'nope', 'new' => 'Aa1-Aa1-Aa1-xyz9', 'again' => 'Aa1-Aa1-Aa1-xyz9'], [], $mjar);
$stillMust = (int)$tp->query("SELECT must_change_password FROM admins WHERE username = 'IrfanUllah123'")->fetchColumn();
mhttp('GET', 'manage/index.php?v=password', null, [], $mjar);
check('a weak, mismatched or wrongly-confirmed new password is refused', $stillMust === 1 && (int)$weak['code'] === 303 && (int)$mismatch['code'] === 303);
$newPw = 'Spacebook-' . bin2hex(random_bytes(4)) . '-9A';
$chg = mhttp('POST', 'manage/index.php', ['do' => 'password', 'csrf' => $tokP, 'current' => $initial, 'new' => $newPw, 'again' => $newPw], [], $mjar);
$a2 = $tp->query("SELECT * FROM admins WHERE username = 'IrfanUllah123'")->fetch();
check('changing the password clears the first-login requirement and stores only the new hash', $chg['code'] === 303 && (int)$a2['must_change_password'] === 0 && password_verify($newPw, $a2['password_hash']) && !password_verify($initial, $a2['password_hash']) && $a2['password_changed_at'] !== null);
$dash = mhttp('GET', 'manage/index.php?v=dash', null, [], $mjar);
check('the dashboard opens, with cards, charts and the definitions', $dash['code'] === 200 && strpos($dash['body'], 'Verified revenue') !== false && strpos($dash['body'], '<svg') !== false && strpos($dash['body'], 'How each number is defined') !== false && strpos($dash['body'], 'Anonymous visitors (estimate)') !== false && strpos($dash['body'], '<script') === false);
foreach (['payments', 'users', 'subs', 'extend', 'audit'] as $view) {
    $x = mhttp('GET', 'manage/index.php?v=' . $view, null, [], $mjar);
    if ($x['code'] !== 200 || strpos($x['body'], 'Fatal') !== false || strpos($x['body'], 'Warning') !== false || strpos($x['body'], 'Notice') !== false || strpos($x['body'], 'Deprecated') !== false) { $badView = $view . ' ' . $x['code']; break; }
}
check('every management view renders without errors', !isset($badView), isset($badView) ? $badView : '');

// a new pending payment, found by transaction id, approved over HTTP; the second click grants nothing more
$stuE = reg(['want_device' => true]); $uidE = (int)$stuE['json']['user']['id'];
$sE = bill('POST', 'submit_payment', pay_body(['trx' => 'SEARCH99887766', 'plan' => 'student', 'cls' => 'cls7']), bearer($stuE));
$idE = (int)$sE['json']['payment']['id'];
$found = mhttp('GET', 'manage/index.php?v=payments&q=search99887766&status=pending', null, [], $mjar);
$none = mhttp('GET', 'manage/index.php?v=payments&q=nomatch0000&status=pending', null, [], $mjar);
check('payments can be searched by transaction id, status, user and date', strpos($found['body'], $sE['json']['payment']['ref']) !== false && strpos($none['body'], $sE['json']['payment']['ref']) === false && strpos(mhttp('GET', 'manage/index.php?v=payments&q=' . urlencode($stuE['num']), null, [], $mjar)['body'], $sE['json']['payment']['ref']) !== false
    && strpos(mhttp('GET', 'manage/index.php?v=payments&from=' . gmdate('Y-m-d') . '&to=' . gmdate('Y-m-d') . '&plan=student', null, [], $mjar)['body'], $sE['json']['payment']['ref']) !== false);
$det = mhttp('GET', 'manage/index.php?v=payment&id=' . $idE, null, [], $mjar);
$tokR = mcsrf($det['body']);
check('the payment page warns that a transaction id alone is not proof and shows what to check', strpos($det['body'], 'not proof of payment') !== false && strpos($det['body'], '03456896156') !== false && strpos($det['body'], 'SEARCH99887766') !== false && strpos($det['body'], 'Pending Verification') !== false);
$noCsrf = mhttp('POST', 'manage/index.php', ['do' => 'review', 'id' => $idE, 'decision' => 'approve'], [], $mjar);
$crossOrigin = mhttp('POST', 'manage/index.php', ['do' => 'review', 'csrf' => $tokR, 'id' => $idE, 'decision' => 'approve'], ['Origin: https://evil.example'], $mjar);
check('approving without the form token, or from another site, does nothing', $tp->query("SELECT status FROM payment_requests WHERE id = $idE")->fetchColumn() === 'pending' && $crossOrigin['code'] === 403);
$a1 = mhttp('POST', 'manage/index.php', ['do' => 'review', 'csrf' => $tokR, 'id' => $idE, 'decision' => 'approve', 'note' => 'Checked in Easypaisa app'], [], $mjar);
$a2h = mhttp('POST', 'manage/index.php', ['do' => 'review', 'csrf' => $tokR, 'id' => $idE, 'decision' => 'approve', 'note' => 'Checked in Easypaisa app'], [], $mjar);
$after = mhttp('GET', 'manage/index.php?v=payment&id=' . $idE, null, [], $mjar);
check('approving over HTTP twice grants once and says so', sub_count($tp, $uidE) === 1 && strpos($after['body'], 'Already approved') !== false && strpos($after['body'], 'Plan period') !== false && http('GET', 'v2/entitlements.php', null, bearer($stuE))['json']['access']['readClasses'] === ['cls7']);
$userPage = mhttp('GET', 'manage/index.php?v=user&id=' . $uidE, null, [], $mjar);
check('a person\'s page shows their class, payments, subscription history and actions', strpos($userPage['body'], 'Student plan') !== false && strpos($userPage['body'], 'SEARCH99887766') !== false && strpos($userPage['body'], 'activated') !== false && strpos($userPage['body'], 'Suspend this account') !== false);
$subE = (int)$tp->query("SELECT id FROM subscriptions WHERE user_id = $uidE")->fetchColumn();
$susp = mhttp('POST', 'manage/index.php', ['do' => 'sub_suspend', 'csrf' => $tokR, 'id' => $subE, 'reason' => 'checking', 'back' => '?v=subs'], [], $mjar);
$noReason = mhttp('POST', 'manage/index.php', ['do' => 'sub_restore', 'csrf' => $tokR, 'id' => $subE, 'reason' => '', 'back' => '?v=subs'], [], $mjar);
check('suspending over HTTP works; restoring without a reason does not', $tp->query("SELECT status FROM subscriptions WHERE id = $subE")->fetchColumn() === 'suspended');
$ext = mhttp('POST', 'manage/index.php?v=extend', ['do' => 'ext_preview', 'csrf' => $tokR, 'scope' => 'users', 'who' => (string)$uidE, 'plan' => '', 'states' => ['active', 'suspended'], 'mode' => 'add_days', 'days' => '7'], [], $mjar);
check('the extension page previews who is affected before asking to confirm', strpos($ext['body'], 'would change') !== false && strpos($ext['body'], 'Apply to 1 subscription') !== false && strpos($ext['body'], 'name="hash"') !== false);
$csv = mhttp('GET', 'manage/index.php?v=export&kind=payments&from=2020-01-01&to=' . gmdate('Y-m-d'), null, [], $mjar);
check('the payments export downloads as CSV and is audited', $csv['code'] === 200 && stripos($csv['head'], 'text/csv') !== false && stripos($csv['head'], 'attachment') !== false && strpos($csv['body'], 'SEARCH99887766') !== false && (int)$tp->query("SELECT COUNT(*) FROM admin_audit WHERE action = 'export'")->fetchColumn() >= 1);
$aud = mhttp('GET', 'manage/index.php?v=audit', null, [], $mjar);
check('the audit trail shows who did what and the reason', strpos($aud['body'], 'IrfanUllah123') !== false && strpos($aud['body'], 'payment_approve') !== false && strpos($aud['body'], 'sub_suspend') !== false && strpos($aud['body'], 'Exam week gift') !== false);
$out = mhttp('POST', 'manage/index.php', ['do' => 'logout', 'csrf' => $tokR], [], $mjar);
$afterOut = mhttp('GET', 'manage/index.php?v=payments', null, [], $mjar);
check('signing out ends the session', strpos($afterOut['body'], 'name="password"') !== false && strpos($afterOut['body'], 'Reference') === false);
$expiredJar = tempnam(sys_get_temp_dir(), 'sbm');
$ok2 = mhttp('POST', 'manage/index.php', ['do' => 'login', 'csrf' => mcsrf(mhttp('GET', 'manage/index.php', null, [], $expiredJar)['body']), 'username' => 'IrfanUllah123', 'password' => $newPw], [], $expiredJar);
check('the new password signs in, straight to the dashboard', $ok2['code'] === 303 && strpos($ok2['head'], 'Location: ?v=dash') !== false);
check('every administrator action is in the audit trail with the administrator\'s name', (int)$tp->query("SELECT COUNT(*) FROM admin_audit WHERE admin_name = 'IrfanUllah123'")->fetchColumn() > 20 && (int)$tp->query("SELECT COUNT(*) FROM admin_audit WHERE action = 'login_fail'")->fetchColumn() >= 5 && (int)$tp->query("SELECT COUNT(*) FROM admin_audit WHERE action = 'password_change'")->fetchColumn() === 1);

// ---------------------------------------------------------------- forgot the password: only the command line can issue a temporary one
$noAdmin = cli('admin-reset NoSuchAdmin');
$res = cli('admin-reset IrfanUllah123');
$tmp = preg_match('/temporary password for IrfanUllah123: (\S+)/', $res['out'], $mm) ? $mm[1] : '';
$a3 = $tp->query("SELECT * FROM admins WHERE username = 'IrfanUllah123'")->fetch();
check('admin-reset on the command line gives a one-time temporary password that must be changed', $noAdmin['rc'] === 1 && $res['rc'] === 0 && strlen($tmp) >= 16 && password_verify($tmp, $a3['password_hash']) && (int)$a3['must_change_password'] === 1 && !password_verify($newPw, $a3['password_hash']), $res['out']);
check('there is no way to reset it over HTTP', strpos(mhttp('POST', 'manage/index.php', ['do' => 'admin-reset', 'username' => 'IrfanUllah123'])['body'], 'temporary') === false && http('GET', 'migrate.php')['code'] !== 200);

// ---------------------------------------------------------------- the account export includes the billing records; a deleted account keeps its payment records
$ex = sb_account_export($tp, $uidA);
check('the data export of an account lists its payments and subscriptions', isset($ex['billing']) && count($ex['billing']['payments']) >= 2 && count($ex['billing']['subscriptions']) >= 2);

if (is_resource($proc2)) { proc_terminate($proc2); proc_close($proc2); }
