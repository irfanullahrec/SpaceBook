<?php
// Administration pages (Phase 9). Server-rendered, no JavaScript, one file.
//   GET  api/admin.php                     overview: people, devices, sync, what is deployed
//   GET  api/admin.php?v=users&q=&status=&page=   people (numbers masked)
//   GET  api/admin.php?v=user&id=N         one person (full number; opening it is written to the audit log) with the block / unblock form
//   GET  api/admin.php?v=sync              rejected sync events by code, and the latest ones
//   GET  api/admin.php?v=audit&action=&uid=       the audit log
//   GET  api/admin.php?v=feed             reported and hidden News Feed posts and comments, with Restore / Remove
//   GET  api/admin.php?v=feedback[&status=&kind=&page=]   suggestions, bug reports and mistakes students sent; ?v=feedback&id=N one report with its picture
//   GET  api/admin.php?v=feedback_image&id=N              the picture of one report (administrators only; served as an image, never as a page)
//   POST api/admin.php  action=set_status  id, to=blocked|active, reason, csrf
//   POST api/admin.php  action=feed_set    type=p|c, id, to=visible|removed, csrf
//   POST api/admin.php  action=feedback_set id, to=new|seen|fixed|wontfix|duplicate, note, csrf
// Only a signed-in, ACTIVE user whose users.role is 'admin' gets a page (role set from the command line: php api/migrate.php make-admin <number>);
// anyone else gets the same plain 404 a missing file would. Role and status are read from the database on every request.
// Compatible with PHP 7.4.

require __DIR__ . '/db.php';
require __DIR__ . '/session.php';
require __DIR__ . '/lib/security.php';
require __DIR__ . '/lib/admin.php';
require __DIR__ . '/lib/feed.php';
require __DIR__ . '/lib/feedback.php';

header('Cache-Control: no-store');
header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');          // not no-referrer: that makes a browser send "Origin: null" on the page's own forms
header('X-Robots-Tag: noindex, nofollow');
header("Content-Security-Policy: default-src 'none'; style-src 'self'; img-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'");

function admin_stop(int $code, string $text): void
{
    http_response_code($code);
    header('Content-Type: text/plain; charset=utf-8');
    echo $text . "\n";
    exit;
}

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook admin DB: ' . $e->getMessage());
    admin_stop(500, 'Database connection failed');
}

$me = sb_admin_user($pdo);
if (!$me) admin_stop(404, 'Not found');
$rl = sb_rate_hit($pdo, 'admin:u:' . $me['id'], 600, 3600);
if (!$rl['ok']) { header('Retry-After: ' . $rl['retry']); admin_stop(429, 'Too many requests'); }

$h = 'sb_admin_h';
$flash = null;

// ---------------------------------------------------------------- the one action
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!sb_request_is_same_site()) admin_stop(403, 'Request not allowed');
    if (!sb_admin_csrf_ok(isset($_POST['csrf']) ? $_POST['csrf'] : '')) admin_stop(403, 'The form expired: go back, reload and try again');
    $act = isset($_POST['action']) ? (string)$_POST['action'] : '';
    if ($act === 'feed_set') {
        $r = sb_feed_admin_set($pdo, $me, (string)(isset($_POST['type']) ? $_POST['type'] : 'p'), (int)(isset($_POST['id']) ? $_POST['id'] : 0), (string)(isset($_POST['to']) ? $_POST['to'] : ''));
        $_SESSION['admin_flash'] = $r['ok'] ? (!empty($r['unchanged']) ? 'Nothing to change.' : 'Done.') : 'Not done: ' . $r['error'];
        header('Location: admin.php?v=feed', true, 303);
        exit;
    }
    if ($act === 'feedback_set') {
        $fid = (int)(isset($_POST['id']) ? $_POST['id'] : 0);
        $r = sb_fb_admin_set($pdo, $me, $fid, (string)(isset($_POST['to']) ? $_POST['to'] : ''), (string)(isset($_POST['note']) ? $_POST['note'] : ''));
        $_SESSION['admin_flash'] = $r['ok'] ? (!empty($r['unchanged']) ? 'Nothing to change.' : 'Done.') : 'Not done: ' . $r['error'];
        header('Location: admin.php?v=feedback&id=' . $fid, true, 303);
        exit;
    }
    if ($act !== 'set_status') admin_stop(400, 'Unknown action');
    $id = (int)(isset($_POST['id']) ? $_POST['id'] : 0);
    $r = sb_admin_set_status($pdo, $me, $id, (string)(isset($_POST['to']) ? $_POST['to'] : ''), (string)(isset($_POST['reason']) ? $_POST['reason'] : ''));
    $_SESSION['admin_flash'] = $r['ok'] ? (!empty($r['unchanged']) ? 'Nothing to change.' : 'Done.') : 'Not done: ' . $r['error'];
    header('Location: admin.php?v=user&id=' . $id, true, 303);
    exit;
}
if (!empty($_SESSION['admin_flash'])) { $flash = (string)$_SESSION['admin_flash']; unset($_SESSION['admin_flash']); }

$view = isset($_GET['v']) ? (string)$_GET['v'] : 'home';
$csrf = sb_admin_csrf();

function admin_head(string $title, string $view, array $me, ?string $flash): void
{
    $nav = ['home' => 'Overview', 'users' => 'People', 'sync' => 'Sync', 'feed' => 'News Feed', 'feedback' => 'Feedback', 'audit' => 'Audit log'];
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">';
    echo '<title>', sb_admin_h($title), ' · Administration</title><link rel="stylesheet" href="admin.css"></head><body><header><strong>SpaceBook administration</strong><nav aria-label="Administration">';
    foreach ($nav as $k => $label) echo '<a href="admin.php', $k === 'home' ? '' : '?v=' . $k, '"', $k === $view || ($view === 'user' && $k === 'users') ? ' aria-current="page"' : '', '>', $label, '</a>';
    echo '</nav><span>', sb_admin_h($me['name']), ' · <a href="../">the app</a></span></header><main><h1>', sb_admin_h($title), '</h1>';
    if ($flash) echo '<p class="flash" role="status">', sb_admin_h($flash), '</p>';
}
function admin_foot(): void { echo '</main></body></html>'; }
function admin_table(array $head, array $rows): void
{
    echo '<table><thead><tr>';
    foreach ($head as $c) echo '<th scope="col">', sb_admin_h($c), '</th>';
    echo '</tr></thead><tbody>';
    foreach ($rows as $r) { echo '<tr>'; foreach ($r as $c) echo '<td>', $c, '</td>'; echo '</tr>'; }    // cells are already escaped by the caller
    if (!$rows) echo '<tr><td colspan="', count($head), '">Nothing to show.</td></tr>';
    echo '</tbody></table>';
}

// the picture of a report: an image and nothing else (no page, no script; the sandbox header makes even a mislabelled file inert)
if ($view === 'feedback_image') {
    $img = sb_fb_image($pdo, (int)(isset($_GET['id']) ? $_GET['id'] : 0));
    if (!$img) admin_stop(404, 'Not found');
    header('Content-Type: ' . $img['mime']);
    header("Content-Security-Policy: default-src 'none'; sandbox");
    header('Content-Disposition: inline; filename="report-' . (int)$_GET['id'] . '.jpg"');
    header('Content-Length: ' . strlen($img['data']));
    echo $img['data'];
    exit;
}

header('Content-Type: text/html; charset=utf-8');

// ---------------------------------------------------------------- views
if ($view === 'users') {
    $q = isset($_GET['q']) ? (string)$_GET['q'] : '';
    $status = isset($_GET['status']) ? (string)$_GET['status'] : '';
    $page = (int)(isset($_GET['page']) ? $_GET['page'] : 1);
    $res = sb_admin_users($pdo, $q, $status, $page);
    admin_head('People', 'users', $me, $flash);
    echo '<form method="get" action="admin.php" class="bar"><input type="hidden" name="v" value="users"><label>Name or number <input name="q" value="', $h($q), '" maxlength="60"></label> ',
         '<label>Status <select name="status"><option value="">all</option><option value="active"', $status === 'active' ? ' selected' : '', '>active</option><option value="blocked"', $status === 'blocked' ? ' selected' : '', '>blocked</option></select></label> <button>Search</button></form>';
    echo '<p>', (int)$res['total'], ' people · page ', (int)$res['page'], ' of ', (int)$res['pages'], '</p>';
    $rows = [];
    foreach ($res['rows'] as $u) {
        $rows[] = ['<a href="admin.php?v=user&amp;id=' . (int)$u['id'] . '">' . $h($u['name']) . '</a>', $h($u['father_name']), $h($u['user_type']) . ($u['role'] === 'admin' ? ' · admin' : ''),
                   $h(sb_admin_mask($u['whatsapp'])), '<span class="st-' . $h($u['status']) . '">' . $h($u['status']) . '</span>', $h($u['created_at']), $h($u['last_login_at'] ?: '—')];
    }
    admin_table(['Name', 'Father', 'Type', 'Number', 'Status', 'Joined', 'Last sign-in'], $rows);
    $base = 'admin.php?v=users&amp;q=' . urlencode($q) . '&amp;status=' . urlencode($status) . '&amp;page=';
    echo '<p class="pages">', $res['page'] > 1 ? '<a href="' . $base . ($res['page'] - 1) . '">← previous</a> ' : '', $res['page'] < $res['pages'] ? '<a href="' . $base . ($res['page'] + 1) . '">next →</a>' : '', '</p>';
    admin_foot();
    exit;
}

if ($view === 'user') {
    $id = (int)(isset($_GET['id']) ? $_GET['id'] : 0);
    $u = sb_admin_user_detail($pdo, $id);
    if (!$u) { admin_head('No such person', 'users', $me, $flash); echo '<p>This account does not exist or was deleted.</p>'; admin_foot(); exit; }
    sb_audit($pdo, $id, 'admin_view', 'by:' . (int)$me['id']);
    admin_head($u['name'], 'user', $me, $flash);
    echo '<dl><dt>Father</dt><dd>', $h($u['father_name']), '</dd><dt>Type</dt><dd>', $h($u['user_type']), $u['role'] === 'admin' ? ' · administrator' : '', '</dd><dt>WhatsApp</dt><dd>', $h($u['whatsapp']),
         '</dd><dt>Status</dt><dd><span class="st-', $h($u['status']), '">', $h($u['status']), '</span></dd><dt>Joined</dt><dd>', $h($u['created_at']), '</dd><dt>Last sign-in</dt><dd>', $h($u['last_login_at'] ?: '—'),
         '</dd><dt>Coins</dt><dd>', (int)$u['coins'], '</dd></dl>';
    if ($u['role'] !== 'admin' && (int)$u['id'] !== (int)$me['id']) {
        $to = $u['status'] === 'blocked' ? 'active' : 'blocked';
        echo '<form method="post" action="admin.php" class="action"><input type="hidden" name="action" value="set_status"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="id" value="', (int)$u['id'], '"><input type="hidden" name="to" value="', $to, '">',
             '<label>Reason (kept in the audit log) <input name="reason" maxlength="100"></label> <button>', $to === 'blocked' ? 'Block this account and sign out its devices' : 'Unblock this account', '</button></form>';
    } else {
        echo '<p>An administrator, or you, is changed from the command line, not here.</p>';
    }
    echo '<h2>Devices</h2>';
    $rows = [];
    foreach ($u['devices'] as $d) $rows[] = [$h($d['name'] ?: '—'), $h($d['created_at']), $h($d['last_seen'] ?: '—'), $d['revoked'] ? 'signed out' : 'active'];
    admin_table(['Device', 'Added', 'Last seen', 'State'], $rows);
    echo '<h2>Latest sync problems</h2>';
    $rows = [];
    foreach ($u['sync_errors'] as $e) $rows[] = [$h($e['code']), $h($e['event_id']), $h($e['created_at'])];
    admin_table(['Code', 'Event', 'When'], $rows);
    echo '<h2>Latest audit rows</h2>';
    $rows = [];
    foreach ($u['audit'] as $a) $rows[] = [$h($a['action']), $h($a['detail']), $h($a['ip']), $h($a['created_at'])];
    admin_table(['Action', 'Detail', 'Address', 'When'], $rows);
    admin_foot();
    exit;
}

if ($view === 'sync') {
    $s = sb_admin_sync($pdo, 100);
    admin_head('Sync', 'sync', $me, $flash);
    echo '<p>', (int)$s['devices'], ' devices are signed in; ', (int)$s['idle'], ' of them have not been seen for 30 days. A rejected event is one the server will never accept (the device drops it): the code says why. Payloads are never kept.</p>';
    echo '<h2>Rejected events by code</h2>';
    $rows = [];
    foreach ($s['codes'] as $c) $rows[] = [$h($c['code']), (int)$c['day'], (int)$c['week']];
    admin_table(['Code', 'Last 24 hours', 'Last 7 days'], $rows);
    echo '<h2>Latest 100</h2>';
    $rows = [];
    foreach ($s['rows'] as $e) $rows[] = ['<a href="admin.php?v=user&amp;id=' . (int)$e['user_id'] . '">' . $h($e['name'] ?: ('#' . $e['user_id'])) . '</a>', $h($e['code']), $h($e['event_id']), $h(substr((string)$e['device_id'], 0, 8)), $h($e['created_at'])];
    admin_table(['Person', 'Code', 'Event', 'Device', 'When'], $rows);
    admin_foot();
    exit;
}

if ($view === 'feed') {
    admin_head('News Feed: reported posts', 'feed', $me, $flash);
    echo '<p>A post or comment that ', (int)SB_FEED_HIDE_AT, ' different students report hides itself from the feed. Restore puts it back (its reports are cleared), Remove deletes it for good. Names are the full account names here.</p>';
    $rows = [];
    foreach (sb_feed_admin_rows($pdo, 100) as $r) {
        $form = function (string $to, string $label) use ($r, $csrf, $h) {
            return '<form method="post" action="admin.php" class="action"><input type="hidden" name="action" value="feed_set"><input type="hidden" name="csrf" value="' . $h($csrf) . '"><input type="hidden" name="type" value="' . $r['type'] . '"><input type="hidden" name="id" value="' . (int)$r['id'] . '"><input type="hidden" name="to" value="' . $to . '"><button>' . $label . '</button></form>';
        };
        $rows[] = [$r['type'] === 'c' ? 'comment' : 'post', (int)$r['id'], '<a href="admin.php?v=user&amp;id=' . (int)$r['user_id'] . '">' . $h($r['author']) . '</a>', '<span class="st-' . $h($r['status'] === 'visible' ? 'active' : 'blocked') . '">' . $h($r['status']) . '</span>',
                   (int)$r['reports'] . ' · ' . $h($r['reasons']), $h(mb_substr($r['body'], 0, 300)), $h($r['created_at']),
                   ($r['status'] === 'visible' ? '' : $form('visible', 'Restore')) . ($r['status'] === 'removed' ? '' : $form('removed', 'Remove'))];
    }
    admin_table(['What', 'No.', 'Author', 'State', 'Reports · reasons', 'Text', 'Written', ''], $rows);
    admin_foot();
    exit;
}

if ($view === 'feedback') {
    $fid = (int)(isset($_GET['id']) ? $_GET['id'] : 0);
    $kindNames = ['suggestion' => 'Suggestion', 'bug' => 'Bug', 'content' => 'Textbook mistake', 'translation' => 'Meaning / translation', 'answer' => 'Wrong answer'];
    if ($fid) {
        $r = sb_fb_admin_get($pdo, $fid);
        if (!$r) { admin_head('No such report', 'feedback', $me, $flash); echo '<p>This report does not exist or was removed.</p>'; admin_foot(); exit; }
        if ($r['status'] === 'new') { $pdo->prepare("UPDATE feedback_reports SET status = 'seen', handled_by = ? WHERE id = ? AND status = 'new'")->execute([(int)$me['id'], $fid]); $r['status'] = 'seen'; }
        admin_head('Report #' . $fid, 'feedback', $me, $flash);
        $ctx = $r['context_json'] ? json_decode($r['context_json'], true) : [];
        echo '<dl><dt>Kind</dt><dd>', $h($kindNames[$r['kind']] ?? $r['kind']), '</dd><dt>From</dt><dd>', $r['user_id'] ? '<a href="admin.php?v=user&amp;id=' . (int)$r['user_id'] . '">' . $h($r['user_name'] ?: ('#' . $r['user_id'])) . '</a>' : 'not signed in', ' · ', $h($r['platform']),
             '</dd><dt>Sent</dt><dd>', $h($r['created_at']), '</dd><dt>State</dt><dd>', $h($r['status']), '</dd></dl>';
        echo '<h2>What was written</h2><p class="feedback-text">', nl2br($h($r['message'])), '</p>';
        echo '<h2>Where it was</h2><dl>';
        if (is_array($ctx)) foreach ($ctx as $k => $v) echo '<dt>', $h($k), '</dt><dd>', $h(is_bool($v) ? ($v ? 'yes' : 'no') : $v), '</dd>';
        echo '</dl>';
        if ($r['has_image']) echo '<h2>Picture</h2><p><img src="admin.php?v=feedback_image&amp;id=', $fid, '" alt="Picture sent with report ', $fid, '" style="max-width:100%;max-height:480px;border:1px solid #cbd5e1"></p>';
        echo '<h2>Handle it</h2><form method="post" action="admin.php" class="action"><input type="hidden" name="action" value="feedback_set"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="id" value="', $fid, '">',
             '<label>State <select name="to">';
        foreach (SB_FB_STATUSES as $s) echo '<option value="', $s, '"', $s === $r['status'] ? ' selected' : '', '>', $s === 'wontfix' ? "won't fix" : $s, '</option>';
        echo '</select></label> <label>Note (what was done, 500 characters) <input name="note" value="', $h($r['admin_note']), '" maxlength="500" size="50"></label> <button>Save</button></form>';
        echo '<p><a href="admin.php?v=feedback">← all reports</a></p>';
        admin_foot();
        exit;
    }
    $status = isset($_GET['status']) ? (string)$_GET['status'] : '';
    $kind = isset($_GET['kind']) ? (string)$_GET['kind'] : '';
    $page = (int)(isset($_GET['page']) ? $_GET['page'] : 1);
    $res = sb_fb_admin_list($pdo, $status, $kind, $page);
    admin_head('Feedback', 'feedback', $me, $flash);
    echo '<form method="get" action="admin.php" class="bar"><input type="hidden" name="v" value="feedback"><label>State <select name="status"><option value="">all</option>';
    foreach (SB_FB_STATUSES as $s) echo '<option value="', $s, '"', $s === $status ? ' selected' : '', '>', $s === 'wontfix' ? "won't fix" : $s, '</option>';
    echo '</select></label> <label>Kind <select name="kind"><option value="">all</option>';
    foreach ($kindNames as $k => $label) echo '<option value="', $k, '"', $k === $kind ? ' selected' : '', '>', $h($label), '</option>';
    echo '</select></label> <button>Filter</button></form>';
    echo '<p>', (int)$res['total'], ' reports · page ', (int)$res['page'], ' of ', (int)$res['pages'], '. Opening a new report marks it seen. Reports may be anonymous: there is no way to reply, so the state and the note are all the sender can see (as a word) in the app.</p>';
    $rows = [];
    foreach ($res['rows'] as $x) {
        $c = $x['context_json'] ? json_decode($x['context_json'], true) : [];
        $where = is_array($c) ? trim(implode(' · ', array_filter([isset($c['cls']) ? 'Class ' . $c['cls'] : '', isset($c['subjectName']) ? $c['subjectName'] : (isset($c['subject']) ? $c['subject'] : ''), isset($c['chapter']) ? 'ch. ' . $c['chapter'] : '', isset($c['page']) ? 'p. ' . $c['page'] : '']))) : '';
        $rows[] = ['<a href="admin.php?v=feedback&amp;id=' . (int)$x['id'] . '">#' . (int)$x['id'] . '</a>', $h($kindNames[$x['kind']] ?? $x['kind']), '<span class="st-' . $h($x['status'] === 'new' ? 'blocked' : 'active') . '">' . $h($x['status']) . '</span>',
                   $h($where), $h($x['snippet']), $x['has_image'] ? 'picture' : '', $h($x['platform']), $h($x['created_at'])];
    }
    admin_table(['No.', 'Kind', 'State', 'Where', 'Text', '', 'From', 'Sent'], $rows);
    $base = 'admin.php?v=feedback&amp;status=' . urlencode($status) . '&amp;kind=' . urlencode($kind) . '&amp;page=';
    echo '<p class="pages">', $res['page'] > 1 ? '<a href="' . $base . ($res['page'] - 1) . '">← previous</a> ' : '', $res['page'] < $res['pages'] ? '<a href="' . $base . ($res['page'] + 1) . '">next →</a>' : '', '</p>';
    admin_foot();
    exit;
}

if ($view === 'audit') {
    $action = isset($_GET['action']) ? (string)$_GET['action'] : '';
    $uid = (int)(isset($_GET['uid']) ? $_GET['uid'] : 0);
    $rows = sb_admin_audit_rows($pdo, $action, $uid, 200);
    admin_head('Audit log', 'audit', $me, $flash);
    echo '<form method="get" action="admin.php" class="bar"><input type="hidden" name="v" value="audit"><label>Action <select name="action"><option value="">all</option>';
    foreach (sb_admin_audit_actions($pdo) as $a) echo '<option value="', $h($a['action']), '"', $a['action'] === $action ? ' selected' : '', '>', $h($a['action']), ' (', (int)$a['n'], ')</option>';
    echo '</select></label> <label>Person number <input name="uid" value="', $uid ?: '', '" size="6" inputmode="numeric"></label> <button>Filter</button></form>';
    $out = [];
    foreach ($rows as $a) $out[] = [$h($a['created_at']), $h($a['action']), $a['user_id'] ? '<a href="admin.php?v=user&amp;id=' . (int)$a['user_id'] . '">' . $h($a['name'] ?: ('#' . $a['user_id'])) . '</a>' : '—', $h($a['detail']), $h($a['ip'])];
    admin_table(['When', 'Action', 'Person', 'Detail', 'Address'], $out);
    admin_foot();
    exit;
}

// overview
$c = sb_admin_counts($pdo);
$content = sb_admin_content_status($pdo, dirname(__DIR__));
admin_head('Overview', 'home', $me, $flash);
echo '<h2>People</h2><ul><li><strong>', (int)$c['users'], '</strong> accounts (', (int)$c['blocked'], ' blocked, ', (int)$c['admins'], ' administrators); ', (int)$c['deleted'], ' deleted and waiting to be purged</li>',
     '<li>', (int)$c['new_7d'], ' joined in the last 7 days; ', (int)$c['login_24h'], ' signed in in the last 24 hours</li><li>By type: ';
$t = [];
foreach ($c['types'] as $k => $n) $t[] = $h($k) . ' ' . (int)$n;
echo implode(', ', $t) ?: '—', '</li></ul>';
echo '<h2>Sync</h2><ul><li>', (int)$c['devices_7d'], ' devices seen in the last 7 days</li><li>', (int)$c['sync_24h'], ' events applied in the last 24 hours</li><li><a href="admin.php?v=sync">', (int)$c['sync_err_24h'], ' rejected in the last 24 hours, ', (int)$c['sync_err_7d'], ' in 7 days</a></li></ul>';
$fb = sb_fb_admin_counts($pdo);
echo '<h2>Feedback</h2><ul><li><a href="admin.php?v=feedback&amp;status=new"><strong>', (int)$fb['new'], '</strong> new reports</a> of ', (int)$fb['total'], ' (', (int)$fb['pictures'], ' with a picture)</li></ul>';
echo '<h2>What is deployed</h2><dl><dt>Service worker version</dt><dd>', $h($content['version'] ?: 'not found'), '</dd><dt>Content built</dt><dd>', $h($content['built'] ?: 'not found'),
     '</dd><dt>Book files</dt><dd>', $h($content['lazy_files'] === null ? 'not found' : $content['lazy_files']), '</dd><dt>Offline packages</dt><dd>', $h($content['offline_subjects'] === null ? 'not found' : $content['offline_subjects']),
     '</dd><dt>Search index</dt><dd>', $h($content['search_subjects'] === null ? 'not found' : $content['search_subjects'] . ' subjects · source ' . $content['search_source']),
     '</dd><dt>Database schema</dt><dd>version ', (int)$content['schema']['current'], ' of ', (int)$content['schema']['latest'], $content['schema']['pending'] ? ' · pending: ' . $h(implode(', ', $content['schema']['pending'])) : ' · up to date', '</dd></dl>';
admin_foot();
