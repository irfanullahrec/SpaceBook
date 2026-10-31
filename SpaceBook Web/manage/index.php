<?php
// SpaceBook management page: payment verification, users and subscriptions, free extensions, statistics, audit trail.
// Its own administrators (table admins), its own session cookie, no JavaScript at all (so a strict content-security policy can forbid it).
// Everything is decided on the server: every request re-reads the administrator from the database, every change is a POST with a
// per-session token and a same-site check, and every change writes the audit trail in the same transaction. Compatible with PHP 7.4.

// Opened as /manage (no trailing slash): relative links such as manage.css would miss, so go to /manage/ first.
$mp = (string) parse_url((string) ($_SERVER['REQUEST_URI'] ?? ''), PHP_URL_PATH);
if ($mp !== '' && substr($mp, -1) !== '/' && substr($mp, -4) !== '.php' && basename($mp) === 'manage') { header('Location: ' . $mp . '/' . (isset($_SERVER['QUERY_STRING']) && $_SERVER['QUERY_STRING'] !== '' ? '?' . $_SERVER['QUERY_STRING'] : '')); exit; }
require __DIR__ . '/../api/db.php';
require __DIR__ . '/../api/lib/manage.php';

header('Cache-Control: no-store');
header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: no-referrer');
header('X-Robots-Tag: noindex, nofollow, noarchive');
header("Content-Security-Policy: default-src 'none'; style-src 'self'; img-src 'self' data:; form-action 'self'; base-uri 'none'; frame-ancestors 'none'");

function m_stop(int $code, string $text): void
{
    http_response_code($code);
    header('Content-Type: text/plain; charset=utf-8');
    echo $text . "\n";
    exit;
}

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook manage DB: ' . $e->getMessage());
    m_stop(500, 'Database connection failed');
}
sb_m_session();

$h = 'sb_m_h';
$admin = sb_m_current($pdo);
$method = $_SERVER['REQUEST_METHOD'];
$v = isset($_GET['v']) ? preg_replace('/[^a-z_]/', '', (string)$_GET['v']) : 'dash';

function m_back(): string
{
    $b = isset($_POST['back']) ? (string)$_POST['back'] : '';
    return preg_match('/^\?v=[a-z_]+(&[a-z_]+=[A-Za-z0-9_.%\-]*)*$/', $b) ? $b : '?v=dash';
}
function m_go(string $to, string $flash = ''): void
{
    if ($flash !== '') $_SESSION['m_flash'] = $flash;
    header('Location: ' . $to, true, 303);
    exit;
}
function m_get(string $k, string $d = ''): string
{
    return isset($_GET[$k]) && is_string($_GET[$k]) ? trim($_GET[$k]) : $d;
}
function m_post(string $k, string $d = ''): string
{
    return isset($_POST[$k]) && is_string($_POST[$k]) ? trim($_POST[$k]) : $d;
}
function m_url(array $p): string
{
    return '?' . http_build_query(array_filter($p, function ($x) { return $x !== '' && $x !== null; }));
}

// ---------------------------------------------------------------- not signed in: the login form and nothing else
if (!$admin) {
    $err = '';
    if ($method === 'POST') {
        if (!sb_request_is_same_site()) m_stop(403, 'Request not allowed');
        if (m_post('do') !== 'login' || !sb_m_csrf_ok(m_post('csrf'))) { $err = 'The form expired. Reload and try again'; }
        else {
            $r = sb_m_login($pdo, m_post('username'), isset($_POST['password']) && is_string($_POST['password']) ? $_POST['password'] : '');
            if ($r['ok']) m_go($r['must_change'] ? '?v=password' : '?v=dash');
            if (!empty($r['retry'])) header('Retry-After: ' . (int)$r['retry']);
            http_response_code($r['code']);
            $err = $r['error'];
        }
    }
    header('Content-Type: text/html; charset=utf-8');
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Sign in · SpaceBook management</title><link rel="stylesheet" href="manage.css"></head><body class="login"><main class="card">',
         '<h1>SpaceBook management</h1><p class="muted">Administrators only.</p>';
    if ($err !== '') echo '<p class="flash bad" role="alert">', $h($err), '</p>';
    echo '<form method="post" autocomplete="off"><input type="hidden" name="do" value="login"><input type="hidden" name="csrf" value="', $h(sb_m_csrf()), '">',
         '<label>Username<input name="username" maxlength="40" autocomplete="username" required autofocus></label>',
         '<label>Password<input name="password" type="password" autocomplete="current-password" required></label>',
         '<button class="primary">Sign in</button></form></main></body></html>';
    exit;
}

$csrf = sb_m_csrf();

// ---------------------------------------------------------------- the changes (POST only)
if ($method === 'POST') {
    if (!sb_request_is_same_site()) m_stop(403, 'Request not allowed');
    if (!sb_m_csrf_ok(m_post('csrf'))) m_go(m_back(), 'The form expired: nothing was changed. Try again.');
    $do = m_post('do');
    $rl = sb_rate_hit($pdo, 'mact:a:' . $admin['id'], 600, 3600);
    if (!$rl['ok']) m_stop(429, 'Too many requests');

    if ($do === 'logout') { sb_m_logout(); m_go('?v=dash'); }

    if ($admin['must_change'] && $do !== 'password') m_go('?v=password', 'Choose a new password first.');

    if ($do === 'password') {
        $r = sb_m_change_password($pdo, $admin, isset($_POST['current']) ? (string)$_POST['current'] : '', isset($_POST['new']) ? (string)$_POST['new'] : '', isset($_POST['again']) ? (string)$_POST['again'] : '');
        m_go($r['ok'] ? '?v=dash' : '?v=password', $r['ok'] ? 'Password changed.' : 'Not changed: ' . $r['error']);
    }
    if ($do === 'review') {
        $r = sb_payment_review($pdo, $admin, (int)m_post('id'), m_post('decision'), m_post('note'));
        $msg = !$r['ok'] ? 'Not done: ' . $r['error'] : (!empty($r['already']) ? 'Already ' . $r['status'] . ': nothing changed.' : ($r['status'] === 'approved' ? 'Approved. The plan is active until ' . sb_nice_date(str_replace(['T', 'Z'], [' ', ''], $r['expiresAt'])) . '.' : 'Rejected. The student was told.'));
        m_go('?v=payment&id=' . (int)m_post('id'), $msg);
    }
    if ($do === 'sub_suspend' || $do === 'sub_restore') {
        $r = $do === 'sub_suspend' ? sb_sub_suspend($pdo, $admin, (int)m_post('id'), m_post('reason')) : sb_sub_restore($pdo, $admin, (int)m_post('id'), m_post('reason'));
        m_go(m_back(), $r['ok'] ? (!empty($r['already']) ? 'Nothing to change.' : 'Done.') : 'Not done: ' . $r['error']);
    }
    if ($do === 'user_status') {
        $r = sb_account_set_status($pdo, $admin, (int)m_post('id'), m_post('to') === 'active' ? 'active' : 'blocked', m_post('reason'));
        m_go(m_back(), $r['ok'] ? (!empty($r['already']) ? 'Nothing to change.' : 'Done.') : 'Not done: ' . $r['error']);
    }
    if ($do === 'grant') {
        $subjects = isset($_POST['subjects']) && is_array($_POST['subjects']) ? array_values(array_filter($_POST['subjects'], 'is_string')) : [];
        $r = sb_sub_grant($pdo, $admin, (int)m_post('id'), m_post('plan'), m_post('cls'), $subjects, (int)m_post('days'), m_post('reason'));
        m_go(m_back(), $r['ok'] ? 'Free access given.' : 'Not done: ' . $r['error']);
    }
    if ($do === 'ext_apply') {
        $f = json_decode(m_post('filter'), true);
        $r = is_array($f) ? sb_ext_apply($pdo, $admin, $f, m_post('mode'), m_post('value'), m_post('hash'), m_post('reason')) : ['ok' => false, 'error' => 'Bad request'];
        m_go('?v=extend', $r['ok'] ? 'Extended ' . $r['count'] . ' subscription' . ($r['count'] === 1 ? '' : 's') . ' of ' . $r['users'] . ' people.' : 'Not done: ' . $r['error']);
    }
    if ($do !== 'ext_preview') m_stop(400, 'Unknown action');
    // ext_preview falls through to the page below
}

$flash = '';
if (!empty($_SESSION['m_flash'])) { $flash = (string)$_SESSION['m_flash']; unset($_SESSION['m_flash']); }

// ---------------------------------------------------------------- page frame
$cat = sb_catalog();
function m_name_of(string $kind, string $key): string
{
    global $cat;
    if ($kind === 'class') return isset($cat['classes'][$key]) ? $cat['classes'][$key] : $key;
    if ($kind === 'subject') return isset($cat['subjects'][$key]) ? ($cat['classes'][$cat['subjects'][$key]['class']] ?? '') . ' ' . $cat['subjects'][$key]['name'] : $key;
    return $key;
}
function m_head(string $title, string $view): void
{
    global $admin, $flash, $h, $csrf;
    $nav = ['dash' => 'Dashboard', 'payments' => 'Payments', 'users' => 'Users', 'subs' => 'Subscriptions', 'extend' => 'Free extension', 'audit' => 'Audit trail', 'password' => 'Password'];
    header('Content-Type: text/html; charset=utf-8');
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>', $h($title), ' · SpaceBook management</title><link rel="stylesheet" href="manage.css"></head><body>';
    echo '<header><strong>SpaceBook management</strong><nav aria-label="Sections">';
    if (!$admin['must_change']) foreach ($nav as $k => $label) echo '<a href="?v=', $k, '"', $k === $view || ($view === 'payment' && $k === 'payments') || ($view === 'user' && $k === 'users') ? ' aria-current="page"' : '', '>', $label, '</a>';
    echo '</nav><form method="post" class="inline"><input type="hidden" name="do" value="logout"><input type="hidden" name="csrf" value="', $h($csrf), '"><span>', $h($admin['username']), '</span> <button>Sign out</button></form></header><main><h1>', $h($title), '</h1>';
    if ($flash !== '') echo '<p class="flash', strpos($flash, 'Not ') === 0 ? ' bad' : ' good', '" role="status">', $h($flash), '</p>';
}
function m_foot(): void { echo '</main></body></html>'; }
function m_table(array $head, array $rows, string $empty = 'Nothing to show.'): void
{
    echo '<div class="scroll"><table><thead><tr>';
    foreach ($head as $c) echo '<th scope="col">', $c, '</th>';
    echo '</tr></thead><tbody>';
    foreach ($rows as $r) { echo '<tr>'; foreach ($r as $c) echo '<td>', $c, '</td>'; echo '</tr>'; }
    if (!$rows) echo '<tr><td colspan="', count($head), '" class="muted">', $empty, '</td></tr>';
    echo '</tbody></table></div>';
}
function m_money($n): string { return 'PKR ' . number_format((float)$n); }
function m_time($t): string { return $t ? substr((string)$t, 0, 16) . ' UTC' : '—'; }
function m_badge(string $s): string { return '<span class="b b-' . sb_m_h($s) . '">' . sb_m_h($s) . '</span>'; }
function m_card(string $label, $value, string $note = ''): string
{
    return '<div class="stat"><div class="n">' . sb_m_h((string)$value) . '</div><div class="l">' . sb_m_h($label) . '</div>' . ($note !== '' ? '<div class="note">' . sb_m_h($note) . '</div>' : '') . '</div>';
}
// a bar chart as inline SVG (no script needed)
function m_bars(array $labels, array $values, string $title, string $unit = ''): string
{
    $n = count($values);
    if ($n === 0) return '';
    $max = max(1, max($values));
    $w = 640; $hgt = 150; $pad = 22; $bw = max(2, ($w - $pad * 2) / $n);
    $o = '<figure class="chart"><figcaption>' . sb_m_h($title) . ' <span class="muted">(highest ' . sb_m_h(number_format($max) . $unit) . ')</span></figcaption><svg viewBox="0 0 ' . $w . ' ' . ($hgt + 24) . '" role="img" aria-label="' . sb_m_h($title) . '">';
    $o .= '<line class="axis" x1="' . $pad . '" y1="' . $hgt . '" x2="' . ($w - $pad) . '" y2="' . $hgt . '"/>';
    foreach ($values as $i => $val) {
        $bh = $val > 0 ? max(1, round(($hgt - 10) * $val / $max, 1)) : 0;
        $o .= '<rect class="bar" x="' . round($pad + $i * $bw + 0.5, 1) . '" y="' . round($hgt - $bh, 1) . '" width="' . round(max(1, $bw - 1.5), 1) . '" height="' . $bh . '"><title>' . sb_m_h($labels[$i] . ': ' . number_format($val) . $unit) . '</title></rect>';
    }
    $step = max(1, (int)ceil($n / 8));
    for ($i = 0; $i < $n; $i += $step) $o .= '<text class="tick" x="' . round($pad + $i * $bw, 1) . '" y="' . ($hgt + 16) . '">' . sb_m_h(substr($labels[$i], 5)) . '</text>';
    return $o . '</svg></figure>';
}
function m_pager(array $res, string $base): void
{
    echo '<p class="pages">', (int)$res['total'], ' found · page ', (int)$res['page'], ' of ', (int)$res['pages'], ' ',
         $res['page'] > 1 ? '<a href="' . sb_m_h($base . '&page=' . ($res['page'] - 1)) . '">← previous</a> ' : '',
         $res['page'] < $res['pages'] ? '<a href="' . sb_m_h($base . '&page=' . ($res['page'] + 1)) . '">next →</a>' : '', '</p>';
}
function m_reason_form(string $do, int $id, string $button, string $back, array $extra = [], string $placeholder = 'Reason (kept in the audit trail)'): string
{
    global $csrf;
    $o = '<form method="post" class="inline"><input type="hidden" name="do" value="' . $do . '"><input type="hidden" name="csrf" value="' . sb_m_h($csrf) . '"><input type="hidden" name="id" value="' . $id . '"><input type="hidden" name="back" value="' . sb_m_h($back) . '">';
    foreach ($extra as $k => $val) $o .= '<input type="hidden" name="' . sb_m_h($k) . '" value="' . sb_m_h($val) . '">';
    return $o . '<input name="reason" maxlength="300" placeholder="' . sb_m_h($placeholder) . '" required> <button>' . sb_m_h($button) . '</button></form>';
}
function m_class_select(string $name, string $sel = ''): string
{
    global $cat;
    $o = '<select name="' . $name . '">';
    foreach ($cat['classes'] as $id => $nm) $o .= '<option value="' . sb_m_h($id) . '"' . ($id === $sel ? ' selected' : '') . '>' . sb_m_h($nm) . '</option>';
    return $o . '</select>';
}
function m_plan_label_row(array $p): string
{
    $subjects = $p['subjects_json'] ? (json_decode($p['subjects_json'], true) ?: []) : [];
    return sb_m_h(sb_plan_label($p['plan_type'], $p['class_id'], $subjects));
}

// ---------------------------------------------------------------- the password must be changed before anything else
if ($admin['must_change'] || $v === 'password') {
    m_head('Change your password', 'password');
    if ($admin['must_change']) echo '<p class="flash bad">This is your first sign-in (or the password was reset). Choose a new password before you continue.</p>';
    echo '<form method="post" class="card narrow"><input type="hidden" name="do" value="password"><input type="hidden" name="csrf" value="', $h($csrf), '">',
         '<label>Current password<input name="current" type="password" autocomplete="current-password" required></label>',
         '<label>New password (12 or more characters, letters and numbers)<input name="new" type="password" autocomplete="new-password" minlength="12" required></label>',
         '<label>New password again<input name="again" type="password" autocomplete="new-password" minlength="12" required></label><button class="primary">Change password</button></form>';
    m_foot();
    exit;
}

// ---------------------------------------------------------------- downloads
if ($v === 'export') {
    [$from, $to] = sb_m_range(m_get('from'), m_get('to'));
    $x = sb_m_export($pdo, m_get('kind'), $from, $to);
    if (!$x) m_stop(400, 'Unknown export');
    sb_admin_audit_write($pdo, $admin, 'export', $x[0], '', '', ['from' => $from, 'to' => $to]);
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="spacebook-' . $x[0] . '-' . $from . '_' . $to . '.csv"');
    echo $x[1];
    exit;
}

// ---------------------------------------------------------------- dashboard
if ($v === 'dash') {
    [$from, $to] = sb_m_range(m_get('from'), m_get('to'));
    $d = sb_m_dashboard($pdo, $from, $to);
    m_head('Dashboard', 'dash');
    echo '<form method="get" class="bar"><input type="hidden" name="v" value="dash"><label>From <input type="date" name="from" value="', $h($from), '"></label> <label>To <input type="date" name="to" value="', $h($to), '"></label> <button>Show</button> ',
         '<span class="muted">All times are UTC.</span></form>';
    if ($d['pendingNow'] > 0) echo '<p class="flash bad"><a href="?v=payments&amp;status=pending">', (int)$d['pendingNow'], ' payment', $d['pendingNow'] === 1 ? '' : 's', ' waiting to be checked →</a></p>';
    $paidAcc = $d['convBase'] > 0 ? round(100 * $d['convPaid'] / $d['convBase'], 1) . '%' : '—';
    echo '<section class="stats">',
         m_card('Registered accounts', number_format($d['accounts']), number_format($d['suspendedAccounts']) . ' suspended'),
         m_card('New in these dates', number_format($d['newAccounts'])),
         m_card('Active subscriptions', number_format($d['subActive'])), m_card('Expired subscriptions', number_format($d['subExpired'])), m_card('Suspended subscriptions', number_format($d['subSuspended'])),
         m_card('Pending payments (these dates)', $d['payStatus']['pending']), m_card('Approved', $d['payStatus']['approved']), m_card('Rejected', $d['payStatus']['rejected']),
         m_card('Verified revenue', m_money($d['revenue']), 'approved payments, by day of approval'),
         m_card('Active people today / 7 days / 30 days', $d['dau'] . ' / ' . $d['wau'] . ' / ' . $d['mau'], 'registered, ending ' . $to),
         m_card('Anonymous visitors (estimate)', number_format($d['anonVisitors']), 'browsers/phones that never signed in'),
         m_card('Sign-up to purchase', $paidAcc, $d['convPaid'] . ' of ' . $d['convBase'] . ' new accounts paid; ' . $d['convSubmitted'] . ' submitted a payment'),
         m_card('Expiring in 7 days', $d['expiringSoonCount']), m_card('Renewals in these dates', $d['renewals']),
         '</section>';
    echo m_bars($d['days'], $d['newByDay'], 'New registrations per day');
    echo m_bars($d['days'], $d['revenueByDay'], 'Verified revenue per day', ' PKR');
    echo m_bars($d['days'], $d['dauSeries'], 'Active registered people per day');
    echo m_bars($d['days'], $d['anonSeries'], 'Anonymous visitors per day (estimate)');

    echo '<div class="cols"><section><h2>Verified revenue</h2>';
    m_table(['Month', 'PKR'], array_map(function ($r) use ($h) { return [$h($r[0]), number_format((float)$r[1])]; }, $d['revenueByMonth']), 'No approved payments in these dates.');
    m_table(['Plan', 'PKR'], array_map(function ($r) use ($h) { return [$h($r[0]), number_format((float)$r[1])]; }, $d['revenueByPlan']), 'No approved payments in these dates.');
    echo '</section><section><h2>Website and app</h2>';
    $plat = ['web' => [0, 0, 0], 'app' => [0, 0, 0]];
    foreach ($d['signupPlatform'] as $r) $plat[$r[0]][0] = (int)$r[1];
    foreach ($d['activeByPlatform'] as $r) $plat[$r[0]][1] = (int)$r[1];
    foreach ($d['anonByPlatform'] as $r) $plat[$r[0]][2] = (int)$r[1];
    m_table(['Platform', 'New accounts', 'Active registered people', 'Anonymous visitors (est.)'], array_map(function ($k) use ($plat) { return [$k === 'web' ? 'Website' : 'Android app', $plat[$k][0], $plat[$k][1], $plat[$k][2]]; }, ['web', 'app']));
    echo '<h2>Active subscriptions by plan</h2>';
    m_table(['Plan', 'Active'], array_map(function ($r) use ($h) { return [$h($r[0]), (int)$r[1]]; }, $d['subByPlan']), 'None yet.');
    echo '</section></div>';

    echo '<div class="cols"><section><h2>Most active people</h2><p class="muted">Activity = tracked actions (hits) in these dates.</p>';
    m_table(['Person', 'Hits', 'Days active'], array_map(function ($r) use ($h) { return ['<a href="?v=user&amp;id=' . (int)$r[0] . '">' . $h($r[1]) . '</a>', (int)$r[2], (int)$r[3]]; }, $d['topUsers']), 'No activity yet.');
    echo '</section><section><h2>Plans ending in 7 days</h2>';
    m_table(['Person', 'Plan', 'Ends'], array_map(function ($r) use ($h) { return [$h($r[1]), $h($r[2]), $h(m_time($r[3]))]; }, $d['expiringSoon']), 'None.');
    echo '</section></div>';

    echo '<div class="cols three"><section><h2>Popular classes</h2>';
    m_table(['Class', 'Hits'], array_map(function ($r) use ($h) { return [$h(m_name_of('class', $r[0])), (int)$r[1]]; }, $d['top_class']));
    echo '</section><section><h2>Popular subjects</h2>';
    m_table(['Subject', 'Hits'], array_map(function ($r) use ($h) { return [$h(m_name_of('subject', $r[0])), (int)$r[1]]; }, $d['top_subject']));
    echo '</section><section><h2>Popular modules</h2>';
    m_table(['Module', 'Hits'], array_map(function ($r) use ($h) { return [$h($r[0]), (int)$r[1]]; }, $d['top_module']));
    echo '</section></div>';

    $lim = []; foreach ($d['limitHits'] as $r) $lim[$r[0]] = (int)$r[1];
    $pr = []; foreach ($d['prompts'] as $r) $pr[$r[0]] = (int)$r[1];
    $co = []; foreach ($d['checkout'] as $r) $co[$r[0]] = (int)$r[1];
    echo '<h2>Free limits and purchase prompts</h2><p class="muted">“Limit reached” counts requests the server refused because the free allowance was used up. “Prompts shown” counts times the purchase window opened because of it. “People at the limit” counts those who used the whole allowance in these dates.</p>';
    $labels = ['prep_q' => 'Test Preparation questions (50)', 'plan_q' => 'Study Plan questions (50)', 'paper' => 'Paper (1)', 'chapter' => 'Chapter 2 and later'];
    $rows = [];
    foreach ($labels as $k => $label) $rows[] = [$h($label), $k === 'chapter' ? '—' : number_format($d['atLimit'][$k]), number_format(isset($lim[$k]) ? $lim[$k] : 0), number_format(isset($pr[$k]) ? $pr[$k] : 0)];
    m_table(['Limit', 'People at the limit', 'Limit reached (requests)', 'Prompts shown'], $rows);
    echo '<p class="muted">Purchase window opened ', (int)($co['open'] ?? 0), ' times · payments submitted ', (int)($co['submitted'] ?? 0), ' times.</p>';

    echo '<h2>Exports</h2><form method="get" class="bar"><input type="hidden" name="v" value="export"><label>Records <select name="kind"><option value="users">Users</option><option value="payments">Payments</option><option value="subscriptions">Subscriptions</option></select></label> ',
         '<label>From <input type="date" name="from" value="', $h($from), '"></label> <label>To <input type="date" name="to" value="', $h($to), '"></label> <button>Download CSV</button></form>';
    echo '<details><summary>How each number is defined</summary><ul class="defs">',
         '<li><b>Registered account</b>: a person with an account that is not deleted. Administrators are not counted.</li>',
         '<li><b>Active / expired / suspended subscription</b>: active = not suspended and not past its end; expired = not suspended and past its end; suspended = stopped by an administrator.</li>',
         '<li><b>Verified revenue</b>: the amount of payments an administrator approved, on the day they were approved. A payment waiting for approval is not revenue.</li>',
         '<li><b>Hit</b>: one tracked action sent by the website or the app (a question answered in a limited module, a chapter or tool opened). Administrators and known bots are not counted.</li>',
         '<li><b>Active people (day / 7 days / 30 days)</b>: distinct registered people with at least one hit on the last chosen day / in the 7 / 30 days ending on it.</li>',
         '<li><b>Anonymous visitors</b>: distinct browsers or phones with hits that never signed in. An estimate: clearing browser data, or using two devices, counts one person twice.</li>',
         '<li><b>Sign-up to purchase</b>: of the accounts created in the chosen dates, how many have at least one approved payment.</li>',
         '<li><b>Popular</b>: hits per class, subject or module.</li></ul></details>';
    m_foot();
    exit;
}

// ---------------------------------------------------------------- payments
if ($v === 'payments') {
    $f = ['q' => m_get('q'), 'status' => m_get('status'), 'plan' => m_get('plan'), 'from' => m_get('from'), 'to' => m_get('to')];
    $res = sb_m_payments($pdo, $f, (int)m_get('page', '1'));
    m_head('Payments', 'payments');
    echo '<form method="get" class="bar"><input type="hidden" name="v" value="payments"><label>Search <input name="q" value="', $h($f['q']), '" maxlength="60" placeholder="Transaction ID, reference, name, number"></label> ',
         '<label>Status <select name="status"><option value="">all</option>';
    foreach (['pending', 'approved', 'rejected'] as $s) echo '<option', $f['status'] === $s ? ' selected' : '', '>', $s, '</option>';
    echo '</select></label> <label>Plan <select name="plan"><option value="">all</option>';
    foreach (['student', 'teacher', 'prep'] as $s) echo '<option', $f['plan'] === $s ? ' selected' : '', '>', $s, '</option>';
    echo '</select></label> <label>From <input type="date" name="from" value="', $h($f['from']), '"></label> <label>To <input type="date" name="to" value="', $h($f['to']), '"></label> <button>Search</button></form>';
    m_pager($res, m_url(['v' => 'payments'] + $f));
    $rows = [];
    foreach ($res['rows'] as $p) {
        $rows[] = ['<a href="?v=payment&amp;id=' . (int)$p['id'] . '">' . $h($p['ref']) . '</a>', $h(m_time($p['submitted_at'])), '<a href="?v=user&amp;id=' . (int)$p['user_id'] . '">' . $h($p['contact_name']) . '</a>', m_plan_label_row($p), m_money($p['amount_pkr']),
                   '<code>' . $h($p['trx_id']) . '</code>', m_badge($p['status']), $h($p['reviewed_by_name'] ?: '—')];
    }
    m_table(['Reference', 'Submitted', 'Person', 'Plan', 'Amount', 'Transaction ID', 'Status', 'Reviewed by'], $rows);
    m_foot();
    exit;
}

if ($v === 'payment') {
    $st = $pdo->prepare('SELECT * FROM payment_requests WHERE id = ?');
    $st->execute([(int)m_get('id')]);
    $p = $st->fetch();
    if (!$p) { m_head('No such payment', 'payments'); echo '<p><a href="?v=payments">Back to payments</a></p>'; m_foot(); exit; }
    sb_admin_audit_write($pdo, $admin, 'payment_view', 'payment', $p['id'], '', []);
    $subjects = $p['subjects_json'] ? (json_decode($p['subjects_json'], true) ?: []) : [];
    $u = sb_m_user_detail($pdo, (int)$p['user_id']);
    m_head('Payment ' . $p['ref'], 'payment');
    echo '<p>', m_badge($p['status']), ' ', $p['status'] === 'pending' ? '<strong>Pending Verification</strong>' : '', '</p>';
    echo '<dl class="grid"><dt>Person</dt><dd>', $u ? '<a href="?v=user&amp;id=' . (int)$p['user_id'] . '">' . $h($p['contact_name']) . '</a>' : $h($p['contact_name']), ' · ', $h($p['contact_whatsapp']), '</dd>',
         '<dt>Plan</dt><dd>', m_plan_label_row($p), '</dd>';
    if ($p['class_id']) echo '<dt>Class</dt><dd>', $h(m_name_of('class', $p['class_id'])), '</dd>';
    if ($subjects) { echo '<dt>Subjects</dt><dd>'; foreach ($subjects as $s) echo $h(m_name_of('subject', $s)), '<br>'; echo '</dd>'; }
    echo '<dt>Expected amount</dt><dd><strong>', m_money($p['amount_pkr']), '</strong> for ', (int)$p['duration_months'], ' month</dd>',
         '<dt>Method</dt><dd>', $h($p['method']), ' to ', $h(SB_EASYPAISA_NUMBER), ' (', $h(SB_EASYPAISA_TITLE), ')</dd>',
         '<dt>Transaction ID</dt><dd><code class="big">', $h($p['trx_id']), '</code></dd>',
         '<dt>Payment date (said by the student)</dt><dd>', $h($p['paid_on'] ?: 'not given'), '</dd>',
         '<dt>Submitted</dt><dd>', $h(m_time($p['submitted_at'])), ' from the ', $h($p['platform'] === 'app' ? 'Android app' : 'website'), '</dd>';
    if ($p['status'] !== 'pending') echo '<dt>Reviewed</dt><dd>', $h($p['reviewed_by_name']), ' · ', $h(m_time($p['reviewed_at'])), $p['review_note'] !== '' ? ' · ' . $h($p['review_note']) : '', '</dd>';
    if ($p['status'] === 'approved') echo '<dt>Plan period</dt><dd>', $h(m_time($p['activated_at'])), ' → ', $h(m_time($p['expires_at'])), ' (subscription <a href="?v=subs&amp;q=', (int)$p['user_id'], '">#', (int)$p['subscription_id'], '</a>)</dd>';
    echo '</dl>';
    $st = $pdo->prepare('SELECT id, ref, user_id, status, submitted_at FROM payment_requests WHERE trx_norm = ? AND id <> ? ORDER BY id');
    $st->execute([$p['trx_norm'], $p['id']]);
    $same = $st->fetchAll();
    if ($same) {
        echo '<p class="flash bad">The same Transaction ID appears on other submissions:</p>';
        m_table(['Reference', 'Person', 'Status', 'Submitted'], array_map(function ($s) use ($h) { return ['<a href="?v=payment&amp;id=' . (int)$s['id'] . '">' . $h($s['ref']) . '</a>', '<a href="?v=user&amp;id=' . (int)$s['user_id'] . '">#' . (int)$s['user_id'] . '</a>', m_badge($s['status']), $h(m_time($s['submitted_at']))]; }, $same));
    }
    if ($p['status'] === 'pending') {
        echo '<div class="warn"><strong>Before you approve:</strong> a Transaction ID alone is not proof of payment. Open the Easypaisa account records and check that this exact ID exists, was received in <b>', $h(SB_EASYPAISA_TITLE), ' (', $h(SB_EASYPAISA_NUMBER), ')</b>, for <b>', m_money($p['amount_pkr']), '</b> or more, on the date above, and has not been used for another student.</div>';
        echo '<div class="cols"><form method="post" class="card"><h2>Approve</h2><input type="hidden" name="do" value="review"><input type="hidden" name="decision" value="approve"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="id" value="', (int)$p['id'], '">',
             '<p class="muted">The plan starts now and lasts one calendar month. If the student already has the same plan running, the month is added after its end date. Pressing twice grants once.</p>',
             '<label>Note (optional)<input name="note" maxlength="300"></label><button class="primary">I checked the Easypaisa record: approve</button></form>',
             '<form method="post" class="card"><h2>Reject</h2><input type="hidden" name="do" value="review"><input type="hidden" name="decision" value="reject"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="id" value="', (int)$p['id'], '">',
             '<p class="muted">The student is told the reason below and can submit again.</p>',
             '<label>Reason (shown to the student)<input name="note" maxlength="300" required placeholder="e.g. Transaction ID not found in Easypaisa"></label><button class="danger">Reject</button></form></div>';
    }
    if ($u && count($u['payments']) > 1) {
        echo '<h2>Other payments by this person</h2>';
        m_table(['Reference', 'Plan', 'Transaction ID', 'Status', 'Submitted'], array_map(function ($x) use ($h) { return ['<a href="?v=payment&amp;id=' . (int)$x['id'] . '">' . $h($x['ref']) . '</a>', m_plan_label_row($x), '<code>' . $h($x['trx_id']) . '</code>', m_badge($x['status']), $h(m_time($x['submitted_at']))]; }, array_filter($u['payments'], function ($x) use ($p) { return (int)$x['id'] !== (int)$p['id']; })));
    }
    m_foot();
    exit;
}

// ---------------------------------------------------------------- users
if ($v === 'users') {
    $f = ['q' => m_get('q'), 'status' => m_get('status'), 'platform' => m_get('platform'), 'sub' => m_get('sub'), 'from' => m_get('from'), 'to' => m_get('to')];
    $res = sb_m_users($pdo, $f, (int)m_get('page', '1'));
    m_head('Users', 'users');
    echo '<form method="get" class="bar"><input type="hidden" name="v" value="users"><label>Search <input name="q" value="', $h($f['q']), '" maxlength="60" placeholder="Name, number or id"></label> ',
         '<label>Account <select name="status"><option value="">all</option><option value="active"', $f['status'] === 'active' ? ' selected' : '', '>active</option><option value="blocked"', $f['status'] === 'blocked' ? ' selected' : '', '>suspended</option></select></label> ',
         '<label>Subscription <select name="sub"><option value="">any</option>';
    foreach (['active' => 'has an active plan', 'expired' => 'only expired', 'suspended' => 'has a suspended plan', 'none' => 'never had one'] as $k => $l) echo '<option value="', $k, '"', $f['sub'] === $k ? ' selected' : '', '>', $l, '</option>';
    echo '</select></label> <label>Joined from <input type="date" name="from" value="', $h($f['from']), '"></label> <label>to <input type="date" name="to" value="', $h($f['to']), '"></label> <button>Search</button></form>';
    m_pager($res, m_url(['v' => 'users'] + $f));
    echo '<form method="post" action="?v=extend"><input type="hidden" name="do" value="ext_preview"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="back" value="?v=users">';
    $rows = [];
    foreach ($res['rows'] as $u) {
        $rows[] = ['<input type="checkbox" name="users[]" value="' . (int)$u['id'] . '" aria-label="Select ' . $h($u['name']) . '">', (int)$u['id'], '<a href="?v=user&amp;id=' . (int)$u['id'] . '">' . $h($u['name']) . '</a>', $h($u['whatsapp']), $u['status'] === 'blocked' ? m_badge('suspended') : m_badge('active'),
                   $h($u['signup_platform']), (int)$u['subs_active'] . ' of ' . (int)$u['subs_all'], $h(m_time($u['created_at'])), $h(m_time($u['last_login_at']))];
    }
    m_table(['', 'Id', 'Name', 'WhatsApp', 'Account', 'Joined on', 'Active plans', 'Created', 'Last sign-in'], $rows);
    echo '<p><button>Preview a free extension for the selected people →</button></p></form>';
    m_foot();
    exit;
}

if ($v === 'user') {
    $u = sb_m_user_detail($pdo, (int)m_get('id'));
    if (!$u) { m_head('No such person', 'users'); echo '<p><a href="?v=users">Back to users</a></p>'; m_foot(); exit; }
    sb_admin_audit_write($pdo, $admin, 'user_view', 'user', $u['id'], '', []);
    $back = '?v=user&id=' . (int)$u['id'];
    m_head($u['name'], 'user');
    echo '<dl class="grid"><dt>Id</dt><dd>', (int)$u['id'], '</dd><dt>Father name</dt><dd>', $h($u['father_name']), '</dd><dt>WhatsApp</dt><dd>', $h($u['whatsapp']), '</dd><dt>Account</dt><dd>', $u['status'] === 'blocked' ? m_badge('suspended') : m_badge('active'), '</dd>',
         '<dt>Created</dt><dd>', $h(m_time($u['created_at'])), ' on the ', $u['signup_platform'] === 'app' ? 'Android app' : 'website', '</dd><dt>Last sign-in</dt><dd>', $h(m_time($u['last_login_at'])), '</dd>',
         '<dt>Free allowance used</dt><dd>Test Preparation ', (int)$u['free']['prep_q']['used'], '/', (int)$u['free']['prep_q']['limit'], ' · Study Plan ', (int)$u['free']['plan_q']['used'], '/', (int)$u['free']['plan_q']['limit'], ' · Papers ', (int)$u['free']['paper']['used'], '/', (int)$u['free']['paper']['limit'], '</dd></dl>';
    echo '<h2>Account</h2>', m_reason_form('user_status', (int)$u['id'], $u['status'] === 'blocked' ? 'Restore this account' : 'Suspend this account (signs out its devices)', $back, ['to' => $u['status'] === 'blocked' ? 'active' : 'blocked']);
    echo '<h2>Subscriptions</h2>';
    $rows = [];
    foreach ($u['subs'] as $s) {
        $detail = $s['subjects'] ? '<br><span class="muted">' . $h(implode(', ', array_map(function ($x) { return $x['name']; }, $s['subjects']))) . '</span>' : '';
        $hist = '';
        foreach ($s['history'] as $e) $hist .= '<li>' . $h(substr(str_replace('T', ' ', (string)$e['at']), 0, 16)) . ' ' . $h($e['event']) . ($e['to'] ? ' → ' . $h(substr(str_replace('T', ' ', (string)$e['to']), 0, 10)) : '') . ($e['reason'] !== '' ? ' (' . $h($e['reason']) . ')' : '') . '</li>';
        $act = $s['status'] === 'suspended' ? m_reason_form('sub_restore', $s['id'], 'Restore', $back) : m_reason_form('sub_suspend', $s['id'], 'Suspend', $back);
        $rows[] = ['#' . $s['id'], $h($s['label']) . $detail, m_badge($s['status']), $h(substr(str_replace('T', ' ', (string)$s['startsAt']), 0, 16)), $h(substr(str_replace('T', ' ', (string)$s['expiresAt']), 0, 16)), $h($s['source']), '<ul class="hist">' . $hist . '</ul>', $act];
    }
    m_table(['Id', 'Plan', 'State', 'Started', 'Ends', 'Source', 'History', 'Action'], $rows, 'No subscriptions.');
    echo '<h2>Give free access</h2><form method="post" class="card"><input type="hidden" name="do" value="grant"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="id" value="', (int)$u['id'], '"><input type="hidden" name="back" value="', $h($back), '">',
         '<label>Plan <select name="plan"><option value="student">Student plan (one class)</option><option value="teacher">Teacher plan (chosen subjects)</option><option value="prep">Test Preparation module</option></select></label>',
         '<label>Class (Student plan) ', m_class_select('cls'), '</label><label>Subjects (Teacher plan, up to 10; hold Ctrl to pick several)<select name="subjects[]" multiple size="8">';
    foreach ($cat['subjects'] as $sid => $s) echo '<option value="', $h($sid), '">', $h(m_name_of('subject', $sid)), '</option>';
    echo '</select></label><label>Days <input name="days" type="number" min="1" max="731" value="30" required></label><label>Reason<input name="reason" maxlength="300" required></label><button class="primary">Give access</button></form>';
    echo '<h2>Payments</h2>';
    m_table(['Reference', 'Plan', 'Transaction ID', 'Status', 'Submitted', 'Plan period'], array_map(function ($x) use ($h) { return ['<a href="?v=payment&amp;id=' . (int)$x['id'] . '">' . $h($x['ref']) . '</a>', m_plan_label_row($x), '<code>' . $h($x['trx_id']) . '</code>', m_badge($x['status']), $h(m_time($x['submitted_at'])), $x['status'] === 'approved' ? $h(substr((string)$x['activated_at'], 0, 10) . ' → ' . substr((string)$x['expires_at'], 0, 10)) : ($x['review_note'] !== '' ? $h($x['review_note']) : '—')]; }, $u['payments']), 'No payments.');
    echo '<h2>What administrators did</h2>';
    m_table(['When', 'Who', 'Action', 'Reason'], array_map(function ($a) use ($h) { return [$h(m_time($a['created_at'])), $h($a['admin_name']), $h($a['action']), $h($a['reason'])]; }, $u['audit']), 'Nothing yet.');
    m_foot();
    exit;
}

// ---------------------------------------------------------------- subscriptions
if ($v === 'subs') {
    $f = ['q' => m_get('q'), 'status' => m_get('status'), 'plan' => m_get('plan'), 'from' => m_get('from'), 'to' => m_get('to')];
    $res = sb_m_subscriptions($pdo, $f, (int)m_get('page', '1'));
    m_head('Subscriptions', 'subs');
    echo '<form method="get" class="bar"><input type="hidden" name="v" value="subs"><label>Person <input name="q" value="', $h($f['q']), '" maxlength="60" placeholder="Name, number or id"></label> <label>State <select name="status"><option value="">all</option>';
    foreach (['active', 'expired', 'suspended'] as $s) echo '<option', $f['status'] === $s ? ' selected' : '', '>', $s, '</option>';
    echo '</select></label> <label>Plan <select name="plan"><option value="">all</option>';
    foreach (['student', 'teacher', 'prep'] as $s) echo '<option', $f['plan'] === $s ? ' selected' : '', '>', $s, '</option>';
    echo '</select></label> <label>Ends from <input type="date" name="from" value="', $h($f['from']), '"></label> <label>to <input type="date" name="to" value="', $h($f['to']), '"></label> <button>Search</button></form>';
    m_pager($res, m_url(['v' => 'subs'] + $f));
    $back = m_url(['v' => 'subs'] + $f);
    $rows = [];
    foreach ($res['rows'] as $s) {
        $pub = sb_sub_public($pdo, $s);
        $rows[] = ['#' . (int)$s['id'], '<a href="?v=user&amp;id=' . (int)$s['user_id'] . '">' . $h($s['user_name']) . '</a>', $h($pub['label']), m_badge($pub['status']), $h(m_time($s['starts_at'])), $h(m_time($s['expires_at'])), $h($s['source']),
                   $s['status'] === 'suspended' ? m_reason_form('sub_restore', (int)$s['id'], 'Restore', $back) : m_reason_form('sub_suspend', (int)$s['id'], 'Suspend', $back)];
    }
    m_table(['Id', 'Person', 'Plan', 'State', 'Started', 'Ends', 'Source', 'Action'], $rows);
    m_foot();
    exit;
}

// ---------------------------------------------------------------- free extension: choose, preview, confirm
if ($v === 'extend') {
    $preview = null; $filter = null; $mode = 'add_days'; $value = '30';
    if ($method === 'POST' && m_post('do') === 'ext_preview') {
        $users = isset($_POST['users']) && is_array($_POST['users']) ? array_map('intval', $_POST['users']) : [];
        $typed = preg_split('/[\s,;]+/', m_post('who'), -1, PREG_SPLIT_NO_EMPTY);
        foreach ($typed as $t) {
            $digits = sb_m_digits($t);
            if (strlen($digits) >= 10) { $id = $pdo->prepare('SELECT id FROM users WHERE whatsapp = ?'); $id->execute([$digits]); $x = $id->fetchColumn(); if ($x) $users[] = (int)$x; }
            elseif (ctype_digit($t)) $users[] = (int)$t;
        }
        $scope = m_post('scope', $users ? 'users' : 'all');
        $filter = ['users' => $scope === 'all' ? [] : array_values(array_unique($users)), 'plan' => m_post('plan'), 'states' => isset($_POST['states']) && is_array($_POST['states']) ? array_values(array_filter($_POST['states'], 'is_string')) : ['active']];
        $mode = m_post('mode', 'add_days') === 'set_date' ? 'set_date' : 'add_days';
        $value = $mode === 'set_date' ? m_post('date') : m_post('days', '30');
        if ($scope === 'users' && !$filter['users']) { $flash = 'Not done: no person matched. Type user ids or WhatsApp numbers, or tick people on the Users page.'; }
        else $preview = sb_ext_preview($pdo, $filter, $mode, $value);
    }
    m_head('Free extension', 'extend');
    echo '<p class="muted">Add days, or set a new end date, to subscriptions without a payment. You always see who is affected and confirm before anything changes. “Add days” adds to the later of the current end and now.</p>';
    $selUsers = $filter ? $filter['users'] : [];
    echo '<form method="post" class="card"><input type="hidden" name="do" value="ext_preview"><input type="hidden" name="csrf" value="', $h($csrf), '">',
         '<fieldset><legend>Who</legend><label class="row"><input type="radio" name="scope" value="users"', $selUsers || !$filter ? ' checked' : '', '> These people (user ids or WhatsApp numbers, separated by spaces or commas)</label>',
         '<input name="who" value="', $h(implode(' ', $selUsers)), '" maxlength="400" placeholder="12 15 923001234567">',
         '<label class="row"><input type="radio" name="scope" value="all"', $filter && !$selUsers ? ' checked' : '', '> Everybody with a matching subscription</label></fieldset>',
         '<fieldset><legend>Which subscriptions</legend><label>Plan <select name="plan"><option value="">all plans</option>';
    foreach (['student' => 'Student plan', 'teacher' => 'Teacher plan', 'prep' => 'Test Preparation'] as $k => $l) echo '<option value="', $k, '"', $filter && $filter['plan'] === $k ? ' selected' : '', '>', $l, '</option>';
    echo '</select></label><span>State:</span>';
    $sel = $filter ? $filter['states'] : ['active'];
    foreach (['active' => 'running', 'expired' => 'already ended', 'suspended' => 'suspended'] as $k => $l) echo '<label class="row"><input type="checkbox" name="states[]" value="', $k, '"', in_array($k, $sel, true) ? ' checked' : '', '> ', $l, '</label>';
    echo '</fieldset><fieldset><legend>Change</legend><label class="row"><input type="radio" name="mode" value="add_days"', $mode === 'add_days' ? ' checked' : '', '> Add <input name="days" type="number" min="1" max="731" value="', $h($mode === 'add_days' ? $value : '30'), '"> days</label>',
         '<label class="row"><input type="radio" name="mode" value="set_date"', $mode === 'set_date' ? ' checked' : '', '> Set the end date to <input name="date" type="date" value="', $h($mode === 'set_date' ? $value : ''), '"> (after the current end)</label></fieldset><button class="primary">Preview who is affected</button></form>';
    if ($preview) {
        echo '<h2>Preview</h2><p><strong>', (int)$preview['count'], '</strong> subscription', $preview['count'] === 1 ? '' : 's', ' would change', $preview['skipped'] ? '; ' . (int)$preview['skipped'] . ' skipped because the new date would not be later than their current end' : '', '.</p>';
        m_table(['Subscription', 'Person', 'Plan', 'State', 'Ends now', 'Would end'], array_map(function ($i) use ($h) { return ['#' . $i['id'], '<a href="?v=user&amp;id=' . (int)$i['user'] . '">' . $h($i['name']) . '</a>', $h($i['plan']), m_badge($i['state']), $h(m_time($i['from'])), '<strong>' . $h(m_time($i['to'])) . '</strong>']; }, array_slice($preview['items'], 0, 300)));
        if ($preview['count'] > 300) echo '<p class="muted">Showing the first 300 of ', (int)$preview['count'], '. All of them will change.</p>';
        if ($preview['count'] > 0) {
            echo '<form method="post" class="card"><h2>Confirm</h2><input type="hidden" name="do" value="ext_apply"><input type="hidden" name="csrf" value="', $h($csrf), '"><input type="hidden" name="filter" value="', $h(json_encode($filter)), '"><input type="hidden" name="mode" value="', $h($mode), '"><input type="hidden" name="value" value="', $h($value), '"><input type="hidden" name="hash" value="', $h($preview['hash']), '">',
                 '<label>Reason (kept in the audit trail and told to the students)<input name="reason" maxlength="300" required></label><button class="danger">Apply to ', (int)$preview['count'], ' subscription', $preview['count'] === 1 ? '' : 's', '</button></form>';
        }
    }
    m_foot();
    exit;
}

// ---------------------------------------------------------------- audit trail
if ($v === 'audit') {
    $f = ['action' => m_get('action'), 'admin' => m_get('admin'), 'target' => m_get('target'), 'from' => m_get('from'), 'to' => m_get('to')];
    $rows = sb_m_audit($pdo, $f, 300);
    m_head('Audit trail', 'audit');
    echo '<form method="get" class="bar"><input type="hidden" name="v" value="audit"><label>Action <select name="action"><option value="">all</option>';
    foreach ($pdo->query('SELECT action, COUNT(*) n FROM admin_audit GROUP BY action ORDER BY n DESC')->fetchAll() as $a) echo '<option value="', $h($a['action']), '"', $a['action'] === $f['action'] ? ' selected' : '', '>', $h($a['action']), ' (', (int)$a['n'], ')</option>';
    echo '</select></label> <label>Administrator <input name="admin" value="', $h($f['admin']), '" size="14"></label> <label>Target id <input name="target" value="', $h($f['target']), '" size="8"></label> <label>From <input type="date" name="from" value="', $h($f['from']), '"></label> <label>To <input type="date" name="to" value="', $h($f['to']), '"></label> <button>Filter</button></form>';
    m_table(['When', 'Who', 'Action', 'Target', 'Reason', 'What changed', 'Address'], array_map(function ($a) use ($h) {
        $d = $a['detail_json'] ? json_decode($a['detail_json'], true) : [];
        $bits = [];
        if (is_array($d)) foreach ($d as $k => $val) { if (is_scalar($val) || $val === null) $bits[] = $k . '=' . (string)$val; elseif ($k !== 'ids' && $k !== 'filter') $bits[] = $k . '=' . json_encode($val); }
        return [$h(m_time($a['created_at'])), $h($a['admin_name']), $h($a['action']), $h($a['target_type'] . ' ' . $a['target_id']), $h($a['reason']), $h(implode(' · ', $bits)), $h($a['ip'])];
    }, $rows));
    m_foot();
    exit;
}

m_go('?v=dash');
