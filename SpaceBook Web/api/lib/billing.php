<?php
// Billing core, shared by the public endpoints (api/billing.php, api/v2/entitlements.php, api/auth.php) and the management page
// (manage/index.php). The website and the Android app both ask the same functions through the same endpoints, so a payment approved
// once opens the same access on both platforms. Compatible with PHP 7.4. Nothing here is reachable over HTTP by itself (api/lib is denied).
//
// What is free (no account):   Chapters 1 and 2 of every subject of every class, 50 Test Preparation questions, 50 Study Plan questions, 1 paper.
// What is sold (PKR 500, one calendar month each, paid by Easypaisa and approved by hand in the management page):
//   student  all subjects of ONE class, Study Plan for that class                       (no paper creation, no Test Preparation)
//   teacher  up to 10 chosen subjects (any classes), paper creation for those subjects (no Study Plan, no Test Preparation)
//   prep     the complete Test Preparation module (every class and subject)             (no chapters, no Study Plan, no papers)
// Submitting a payment never opens access; only an administrator's approval does, and approving twice grants once.
// All times are UTC strings 'Y-m-d H:i:s' in the database and ISO 8601 ('...Z') in answers.

require_once __DIR__ . '/security.php';

const SB_EASYPAISA_NUMBER = '03456896156';
const SB_EASYPAISA_TITLE  = 'AMIN ALLAH';
const SB_PLAN_PRICE_PKR   = 500;
const SB_FREE_CHAPTERS    = 2;                               // chapters 1 and 2 (index 0 and 1) of every subject
const SB_FREE_LIMITS      = ['prep_q' => 50, 'plan_q' => 50, 'paper' => 1];
const SB_MAX_TEACHER_SUBJECTS = 10;
const SB_THANK_YOU = 'Thank you for choosing SpaceBook! Your payment details have been submitted successfully. Please allow up to 1 hour for verification. Your plan will become active once your payment is approved. Happy learning!';

// ---------------------------------------------------------------- clock

// UTC now as 'Y-m-d H:i:s'. Tests may set $GLOBALS['SB_NOW'] to pin it.
function sb_now(): string
{
    return isset($GLOBALS['SB_NOW']) ? (string)$GLOBALS['SB_NOW'] : gmdate('Y-m-d H:i:s');
}

// $dt plus whole calendar months; a 31st becomes the last day of a shorter month (31 Jan + 1 month = 28/29 Feb), time of day kept.
function sb_add_months(string $dt, int $months): string
{
    $d = new DateTimeImmutable($dt, new DateTimeZone('UTC'));
    $day = (int)$d->format('j');
    $first = $d->modify('first day of this month')->modify('+' . $months . ' month');
    return $first->setDate((int)$first->format('Y'), (int)$first->format('n'), min($day, (int)$first->format('t')))->format('Y-m-d H:i:s');
}

function sb_add_days(string $dt, int $days): string
{
    return (new DateTimeImmutable($dt, new DateTimeZone('UTC')))->modify('+' . $days . ' day')->format('Y-m-d H:i:s');
}

function sb_iso($dt): ?string
{
    if ($dt === null || $dt === '' || $dt === '0000-00-00 00:00:00') return null;
    return str_replace(' ', 'T', (string)$dt) . 'Z';
}

function sb_nice_date($dt): string
{
    return (new DateTimeImmutable((string)$dt, new DateTimeZone('UTC')))->format('j M Y');
}

// ---------------------------------------------------------------- plans and catalog

// The one definition of what is sold; api/billing.php?action=plans publishes it, so both platforms show the same words and price.
function sb_plans(): array
{
    return [
        'student' => [
            'id' => 'student', 'title' => 'Student plan', 'price' => SB_PLAN_PRICE_PKR, 'months' => 1, 'duration' => '1 month',
            'pick' => 'class', 'maxSubjects' => 0,
            'tagline' => 'Everything in one class',
            'includes' => ['All subjects of the one class you choose', 'Every chapter, exercise and answer', 'Study Plan for that class'],
            'excludes' => ['Paper creation', 'Test Preparation (buy it separately for PKR 500)'],
        ],
        'teacher' => [
            'id' => 'teacher', 'title' => 'Teacher plan', 'price' => SB_PLAN_PRICE_PKR, 'months' => 1, 'duration' => '1 month',
            'pick' => 'subjects', 'maxSubjects' => SB_MAX_TEACHER_SUBJECTS,
            'tagline' => 'Up to 10 subjects of your choice',
            'includes' => ['Up to 10 subjects, from one class or from different classes', 'Every chapter, exercise and answer of those subjects', 'Paper creation for those subjects'],
            'excludes' => ['Study Plan', 'Test Preparation (buy it separately for PKR 500)'],
        ],
        'prep' => [
            'id' => 'prep', 'title' => 'Test Preparation module', 'price' => SB_PLAN_PRICE_PKR, 'months' => 1, 'duration' => '1 month',
            'pick' => 'none', 'maxSubjects' => 0,
            'tagline' => 'The complete Test Preparation',
            'includes' => ['The complete Test Preparation module: all classes and subjects', 'Unlimited practice and mock tests'],
            'excludes' => ['Textbook chapters', 'Study Plan', 'Paper creation'],
        ],
    ];
}

function sb_free_text(): array
{
    return [
        'Read and use Chapters 1 and 2 of every subject in every class',
        'Practise up to ' . SB_FREE_LIMITS['prep_q'] . ' questions in Test Preparation',
        'Create ' . SB_FREE_LIMITS['paper'] . ' paper',
        'Practise up to ' . SB_FREE_LIMITS['plan_q'] . ' questions in Study Plan',
    ];
}

// The classes and subjects of the app catalog (content/app_catalog.json, generated from the same registry the site uses).
function sb_catalog(): array
{
    static $cache = null;
    if ($cache !== null) return $cache;
    $file = getenv('SB_CATALOG_FILE');
    if ($file === false || $file === '') $file = __DIR__ . '/../../content/app_catalog.json';
    $out = ['classes' => [], 'subjects' => []];
    $j = is_file($file) ? json_decode((string)file_get_contents($file), true) : null;
    if (is_array($j) && isset($j['classes']) && is_array($j['classes'])) {
        foreach ($j['classes'] as $c) {
            if (!isset($c['id'])) continue;
            $out['classes'][(string)$c['id']] = isset($c['name']) ? (string)$c['name'] : (string)$c['id'];
            foreach ((isset($c['subjects']) && is_array($c['subjects']) ? $c['subjects'] : []) as $s) {
                if (isset($s['id'])) $out['subjects'][(string)$s['id']] = ['class' => (string)$c['id'], 'name' => isset($s['name']) ? (string)$s['name'] : (string)$s['id']];
            }
        }
    }
    return $cache = $out;
}

function sb_scope_key(string $type, ?string $cls, array $subjects): string
{
    if ($type === 'student') return sha1('student|' . $cls);
    if ($type === 'teacher') { sort($subjects); return sha1('teacher|' . implode(',', $subjects)); }
    return sha1('prep');
}

// ['ok' => true, 'cls' => ?string, 'subjects' => [ids]] or ['ok' => false, 'error' => text]
function sb_validate_selection(string $type, $cls, $subjects): array
{
    $plans = sb_plans();
    if (!isset($plans[$type])) return ['ok' => false, 'error' => 'Choose a plan'];
    $cat = sb_catalog();
    if ($type === 'student') {
        $cls = is_string($cls) ? $cls : '';
        if (!isset($cat['classes'][$cls])) return ['ok' => false, 'error' => 'Choose your class'];
        return ['ok' => true, 'cls' => $cls, 'subjects' => []];
    }
    if ($type === 'teacher') {
        $list = [];
        foreach ((is_array($subjects) ? $subjects : []) as $s) {
            if (!is_string($s) || !isset($cat['subjects'][$s])) return ['ok' => false, 'error' => 'One of the chosen subjects does not exist'];
            $list[$s] = true;
        }
        $list = array_keys($list);
        if (count($list) < 1) return ['ok' => false, 'error' => 'Choose at least one subject'];
        if (count($list) > SB_MAX_TEACHER_SUBJECTS) return ['ok' => false, 'error' => 'The Teacher plan has up to ' . SB_MAX_TEACHER_SUBJECTS . ' subjects'];
        sort($list);
        return ['ok' => true, 'cls' => null, 'subjects' => $list];
    }
    return ['ok' => true, 'cls' => null, 'subjects' => []];
}

// "Student plan · Class 9", "Teacher plan · 4 subjects", "Test Preparation module"
function sb_plan_label(string $type, ?string $cls, array $subjects): string
{
    $plans = sb_plans();
    $title = isset($plans[$type]) ? $plans[$type]['title'] : $type;
    $cat = sb_catalog();
    if ($type === 'student') return $title . ' · ' . (isset($cat['classes'][$cls]) ? $cat['classes'][$cls] : (string)$cls);
    if ($type === 'teacher') return $title . ' · ' . count($subjects) . ' subject' . (count($subjects) === 1 ? '' : 's');
    return $title;
}

function sb_subject_names(array $ids): array
{
    $cat = sb_catalog();
    $out = [];
    foreach ($ids as $id) {
        $s = isset($cat['subjects'][$id]) ? $cat['subjects'][$id] : null;
        $out[] = ['id' => $id, 'class' => $s ? $s['class'] : '', 'name' => $s ? ((isset($cat['classes'][$s['class']]) ? $cat['classes'][$s['class']] . ' ' : '') . $s['name']) : $id];
    }
    return $out;
}

function sb_plans_public(): array
{
    $cat = sb_catalog();
    $classes = [];
    foreach ($cat['classes'] as $id => $name) $classes[] = ['id' => $id, 'name' => $name];
    $subjects = [];
    foreach ($cat['subjects'] as $id => $s) $subjects[] = ['id' => $id, 'class' => $s['class'], 'name' => $s['name']];
    return [
        'currency' => 'PKR',
        'plans' => array_values(sb_plans()),
        'free' => ['title' => 'Free, no account needed', 'items' => sb_free_text(), 'limits' => SB_FREE_LIMITS, 'chapters' => SB_FREE_CHAPTERS],
        'classes' => $classes, 'subjects' => $subjects,
        'payment' => [
            'method' => 'Easypaisa', 'number' => SB_EASYPAISA_NUMBER, 'title' => SB_EASYPAISA_TITLE,
            'instructions' => 'Send the amount shown to the Easypaisa account above, then paste the Transaction ID (TID) from your Easypaisa receipt.',
            'verifyNote' => 'Payments are checked by hand against the real Easypaisa record, usually within 1 hour. Your plan starts only after approval.',
        ],
        'thankYou' => SB_THANK_YOU,
    ];
}

// ---------------------------------------------------------------- who is calling: platform, bots, visitor

function sb_platform(): string
{
    $ua = isset($_SERVER['HTTP_USER_AGENT']) ? (string)$_SERVER['HTTP_USER_AGENT'] : '';
    $h = isset($_SERVER['HTTP_X_SB_PLATFORM']) ? strtolower((string)$_SERVER['HTTP_X_SB_PLATFORM']) : '';
    return ($h === 'app' || strpos($ua, 'SpaceBookApp/') !== false) ? 'app' : 'web';
}

function sb_is_bot(string $ua): bool
{
    if ($ua === '') return true;
    return (bool)preg_match('/bot|crawl|spider|slurp|headless|lighthouse|pingdom|uptime|monitor|curl\/|wget|python-requests|httpclient|facebookexternalhit|preview/i', $ua);
}

function sb_visitor_valid($id): bool
{
    return is_string($id) && (bool)preg_match('/^[0-9a-f]{32}$/', $id);
}

function sb_visitor_from_request(): string
{
    $h = isset($_SERVER['HTTP_X_SB_VISITOR']) ? strtolower(trim((string)$_SERVER['HTTP_X_SB_VISITOR'])) : '';
    if (sb_visitor_valid($h)) return $h;
    $c = isset($_COOKIE['sb_vid']) ? strtolower((string)$_COOKIE['sb_vid']) : '';
    return sb_visitor_valid($c) ? $c : '';
}

// Makes sure the visitor row exists and is fresh; links it to $uid when someone is signed in. Returns the id to use, or '' when the
// caller made too many new ids (a script minting visitors): metered use is then refused.
function sb_visitor_touch(PDO $pdo, string $vid, int $uid, bool $mayCreate = true): string
{
    $ua = isset($_SERVER['HTTP_USER_AGENT']) ? (string)$_SERVER['HTTP_USER_AGENT'] : '';
    $platform = sb_platform();
    if ($vid !== '') {
        $st = $pdo->prepare('UPDATE visitors SET last_seen = NOW(), platform = ?, user_id = IF(? > 0, ?, user_id) WHERE id = ?');
        $st->execute([$platform, $uid, $uid, $vid]);
        if ($st->rowCount() > 0) return $vid;
        $st = $pdo->prepare('SELECT 1 FROM visitors WHERE id = ?');
        $st->execute([$vid]);
        if ($st->fetchColumn()) return $vid;               // unchanged row (same second)
    }
    if (!$mayCreate) return '';
    $rl = sb_rate_hit($pdo, 'vnew:ip:' . sb_client_ip(), 120, 3600);
    if (!$rl['ok']) return '';
    if ($vid === '') $vid = bin2hex(random_bytes(16));
    $pdo->prepare('INSERT IGNORE INTO visitors (id, platform, user_id, is_bot, ip_hash) VALUES (?, ?, ?, ?, ?)')
        ->execute([$vid, $platform, $uid > 0 ? $uid : null, sb_is_bot($ua) ? 1 : 0, substr(sha1(sb_client_ip()), 0, 16)]);
    return $vid;
}

// The signed-in user of this request (device token first, then the cookie session), or 0.
function sb_actor_uid(PDO $pdo): int
{
    $dev = sb_device_from_request($pdo);
    if ($dev) return (int)$dev['user_id'];
    if (sb_bearer_token() === '' && isset($_COOKIE['spacebook_sid'])) {
        if (session_status() !== PHP_SESSION_ACTIVE) require __DIR__ . '/../session.php';
        if (!empty($_SESSION['uid'])) {
            $st = $pdo->prepare("SELECT id FROM users WHERE id = ? AND status = 'active'");
            $st->execute([(int)$_SESSION['uid']]);
            $id = $st->fetchColumn();
            return $id ? (int)$id : 0;
        }
    }
    return 0;
}

// ---------------------------------------------------------------- subscriptions and access

function sb_sub_status(array $row, ?string $now = null): string
{
    if ($row['status'] === 'suspended') return 'suspended';
    return strtotime($row['expires_at'] . ' UTC') > strtotime(($now === null ? sb_now() : $now) . ' UTC') ? 'active' : 'expired';
}

function sb_sub_subjects(PDO $pdo, int $subId): array
{
    $st = $pdo->prepare('SELECT subject_id FROM subscription_subjects WHERE subscription_id = ? ORDER BY subject_id');
    $st->execute([$subId]);
    return $st->fetchAll(PDO::FETCH_COLUMN);
}

function sb_sub_public(PDO $pdo, array $r, bool $withEvents = false): array
{
    $subjects = $r['plan_type'] === 'teacher' ? sb_sub_subjects($pdo, (int)$r['id']) : [];
    $status = sb_sub_status($r);
    $secs = strtotime($r['expires_at'] . ' UTC') - strtotime(sb_now() . ' UTC');
    $o = [
        'id' => (int)$r['id'], 'planType' => $r['plan_type'], 'classId' => $r['class_id'],
        'label' => sb_plan_label($r['plan_type'], $r['class_id'], $subjects),
        'subjects' => sb_subject_names($subjects),
        'status' => $status, 'startsAt' => sb_iso($r['starts_at']), 'expiresAt' => sb_iso($r['expires_at']),
        'daysLeft' => $status === 'expired' ? 0 : max(0, (int)ceil($secs / 86400)),
        'source' => $r['source'], 'suspendReason' => $status === 'suspended' ? $r['suspend_reason'] : '',
    ];
    if ($withEvents) {
        $st = $pdo->prepare('SELECT event, old_expires_at, new_expires_at, reason, created_at FROM subscription_events WHERE subscription_id = ? ORDER BY id DESC LIMIT 20');
        $st->execute([(int)$r['id']]);
        $o['history'] = array_map(function ($e) {
            return ['event' => $e['event'], 'from' => sb_iso($e['old_expires_at']), 'to' => sb_iso($e['new_expires_at']), 'reason' => $e['reason'], 'at' => sb_iso($e['created_at'])];
        }, $st->fetchAll());
    }
    return $o;
}

function sb_user_subscriptions(PDO $pdo, int $uid): array
{
    $st = $pdo->prepare('SELECT * FROM subscriptions WHERE user_id = ? ORDER BY expires_at DESC, id DESC LIMIT 100');
    $st->execute([$uid]);
    return $st->fetchAll();
}

// What this person may use because of paid plans, as plain lists the clients test:
//   readClasses   classes whose every chapter is open          readSubjects  single subjects whose every chapter is open
//   planClasses   classes whose Study Plan has no limit        paperSubjects subjects whose papers have no limit
//   prep          Test Preparation has no limit
function sb_access(PDO $pdo, int $uid): array
{
    $acc = ['readClasses' => [], 'readSubjects' => [], 'planClasses' => [], 'paperSubjects' => [], 'prep' => false];
    if ($uid <= 0) return $acc;
    $st = $pdo->prepare("SELECT s.* FROM subscriptions s JOIN users u ON u.id = s.user_id
                         WHERE s.user_id = ? AND s.status = 'active' AND s.expires_at > ? AND u.status = 'active'");
    $st->execute([$uid, sb_now()]);
    foreach ($st->fetchAll() as $s) {
        if ($s['plan_type'] === 'student' && $s['class_id'] !== null) {
            $acc['readClasses'][] = $s['class_id'];
            $acc['planClasses'][] = $s['class_id'];
        } elseif ($s['plan_type'] === 'teacher') {
            foreach (sb_sub_subjects($pdo, (int)$s['id']) as $sid) { $acc['readSubjects'][] = $sid; $acc['paperSubjects'][] = $sid; }
        } elseif ($s['plan_type'] === 'prep') {
            $acc['prep'] = true;
        }
    }
    foreach (['readClasses', 'readSubjects', 'planClasses', 'paperSubjects'] as $k) { $acc[$k] = array_values(array_unique($acc[$k])); sort($acc[$k]); }
    return $acc;
}

// The single rule both platforms apply to a chapter (index 0 is Chapter 1). tests/access/contract.json holds cases for it.
function sb_can_read(array $acc, string $cls, string $subject, int $chapterIdx): bool
{
    return $chapterIdx < SB_FREE_CHAPTERS || in_array($cls, $acc['readClasses'], true) || in_array($subject, $acc['readSubjects'], true);
}

// Whether a metric has no limit for this context ($ctx: cls, subject)
function sb_metric_unlimited(array $acc, string $metric, array $ctx): bool
{
    if ($metric === 'prep_q') return $acc['prep'];
    if ($metric === 'plan_q') return isset($ctx['cls']) && in_array($ctx['cls'], $acc['planClasses'], true);
    if ($metric === 'paper')  return isset($ctx['subject']) && in_array($ctx['subject'], $acc['paperSubjects'], true);
    return false;
}

// ---------------------------------------------------------------- the free allowance

function sb_free_used(PDO $pdo, int $uid, string $vid, string $metric): int
{
    $key = $uid > 0 ? 'u:' . $uid : ($vid !== '' ? 'v:' . $vid : '');
    if ($key === '') return 0;
    $st = $pdo->prepare('SELECT COUNT(*) FROM free_usage WHERE owner_key = ? AND metric = ?');
    $st->execute([$key, $metric]);
    return (int)$st->fetchColumn();
}

// A person who signs in (or registers) brings what this browser or phone already used, so a fresh or older account is not a fresh allowance.
function sb_free_merge(PDO $pdo, int $uid, string $vid): void
{
    if ($uid <= 0 || $vid === '') return;
    $pdo->prepare("INSERT IGNORE INTO free_usage (owner_key, metric, item_key) SELECT ?, metric, item_key FROM free_usage WHERE owner_key = ?")
        ->execute(['u:' . $uid, 'v:' . $vid]);
}

function sb_free_state(PDO $pdo, int $uid, string $vid): array
{
    $out = [];
    foreach (SB_FREE_LIMITS as $m => $limit) $out[$m] = ['limit' => $limit, 'used' => min($limit, sb_free_used($pdo, $uid, $vid, $m))];
    return $out;
}

function sb_stat(PDO $pdo, string $kind, string $skey, int $n = 1): void
{
    $skey = substr($skey, 0, 60);
    if ($skey === '') return;
    try {
        $pdo->prepare('INSERT INTO usage_stats (day, kind, skey, hits) VALUES (UTC_DATE(), ?, ?, ?) ON DUPLICATE KEY UPDATE hits = hits + VALUES(hits)')->execute([substr($kind, 0, 12), $skey, $n]);
    } catch (Throwable $e) {
        error_log('SpaceBook stat: ' . $e->getMessage());
    }
}

function sb_activity(PDO $pdo, int $uid, string $vid): void
{
    $key = $uid > 0 ? 'u:' . $uid : ($vid !== '' ? 'v:' . $vid : '');
    if ($key === '') return;
    $ua = isset($_SERVER['HTTP_USER_AGENT']) ? (string)$_SERVER['HTTP_USER_AGENT'] : '';
    if (sb_is_bot($ua)) return;
    try {
        $pdo->prepare('INSERT INTO activity_days (day, owner_key, platform, hits) VALUES (UTC_DATE(), ?, ?, 1) ON DUPLICATE KEY UPDATE hits = hits + 1')->execute([$key, sb_platform()]);
    } catch (Throwable $e) {
        error_log('SpaceBook activity: ' . $e->getMessage());
    }
}

// Spend one question (or the paper) of the allowance. $key makes it idempotent: the same question again costs nothing.
//   ['allowed' => bool, 'unlimited' => bool, 'used' => n, 'limit' => n, 'reason' => 'limit'|'busy'|'']
function sb_consume(PDO $pdo, int $uid, string $vid, string $metric, string $key, array $ctx): array
{
    if (!isset(SB_FREE_LIMITS[$metric])) return ['allowed' => false, 'unlimited' => false, 'used' => 0, 'limit' => 0, 'reason' => 'unknown'];
    $limit = SB_FREE_LIMITS[$metric];
    $acc = sb_access($pdo, $uid);
    if (sb_metric_unlimited($acc, $metric, $ctx)) return ['allowed' => true, 'unlimited' => true, 'used' => 0, 'limit' => 0, 'reason' => ''];
    $owner = $uid > 0 ? 'u:' . $uid : ($vid !== '' ? 'v:' . $vid : '');
    if ($owner === '') return ['allowed' => false, 'unlimited' => false, 'used' => $limit, 'limit' => $limit, 'reason' => 'busy'];
    $key = substr($key, 0, 80);
    if ($key === '') $key = bin2hex(random_bytes(8));
    $lock = 'sbfree_' . substr(sha1($owner), 0, 24);
    $got = (int)$pdo->query("SELECT GET_LOCK('" . $lock . "', 5)")->fetchColumn();
    if ($got !== 1) return ['allowed' => false, 'unlimited' => false, 'used' => 0, 'limit' => $limit, 'reason' => 'busy'];
    try {
        $st = $pdo->prepare('SELECT 1 FROM free_usage WHERE owner_key = ? AND metric = ? AND item_key = ?');
        $st->execute([$owner, $metric, $key]);
        $used = sb_free_used($pdo, $uid, $vid, $metric);
        if ($st->fetchColumn()) return ['allowed' => true, 'unlimited' => false, 'used' => min($limit, $used), 'limit' => $limit, 'reason' => ''];
        if ($used >= $limit) {
            sb_stat($pdo, 'limit', $metric);
            return ['allowed' => false, 'unlimited' => false, 'used' => $limit, 'limit' => $limit, 'reason' => 'limit'];
        }
        $ins = $pdo->prepare('INSERT IGNORE INTO free_usage (owner_key, metric, item_key) VALUES (?, ?, ?)');
        $ins->execute([$owner, $metric, $key]);
        if ($uid > 0 && $vid !== '') $ins->execute(['v:' . $vid, $metric, $key]);        // signing out keeps what was used
        return ['allowed' => true, 'unlimited' => false, 'used' => $used + 1, 'limit' => $limit, 'reason' => ''];
    } finally {
        $pdo->query("SELECT RELEASE_LOCK('" . $lock . "')");
    }
}

// ---------------------------------------------------------------- the answer both platforms read

function sb_notify(PDO $pdo, int $uid, string $kind, string $title, string $body = '', ?int $paymentId = null, ?int $subId = null): void
{
    $pdo->prepare('INSERT INTO notifications (user_id, kind, title, body, payment_id, subscription_id) VALUES (?, ?, ?, ?, ?, ?)')
        ->execute([$uid, substr($kind, 0, 20), mb_substr($title, 0, 120), mb_substr($body, 0, 400), $paymentId, $subId]);
}

function sb_payment_public(PDO $pdo, array $p): array
{
    $subjects = $p['subjects_json'] ? (json_decode($p['subjects_json'], true) ?: []) : [];
    return [
        'ref' => $p['ref'], 'id' => (int)$p['id'], 'planType' => $p['plan_type'], 'classId' => $p['class_id'],
        'label' => sb_plan_label($p['plan_type'], $p['class_id'], $subjects), 'subjects' => sb_subject_names($subjects),
        'amount' => (int)$p['amount_pkr'], 'months' => (int)$p['duration_months'], 'method' => $p['method'], 'trxId' => $p['trx_id'],
        'paidOn' => $p['paid_on'], 'submittedAt' => sb_iso($p['submitted_at']),
        'status' => $p['status'], 'statusText' => $p['status'] === 'pending' ? 'Pending Verification' : ucfirst($p['status']),
        'reviewNote' => $p['status'] === 'rejected' ? $p['review_note'] : '',
        'reviewedAt' => sb_iso($p['reviewed_at']), 'activatedAt' => sb_iso($p['activated_at']), 'expiresAt' => sb_iso($p['expires_at']),
    ];
}

function sb_user_payments(PDO $pdo, int $uid, int $limit = 50): array
{
    $st = $pdo->prepare('SELECT * FROM payment_requests WHERE user_id = ? ORDER BY id DESC LIMIT ' . (int)$limit);
    $st->execute([$uid]);
    return array_map(function ($p) use ($pdo) { return sb_payment_public($pdo, $p); }, $st->fetchAll());
}

// What the clients read (api/v2/entitlements.php, api/billing.php?action=state). Backward compatible with version 1 (plan, unlocked, classes, features).
function sb_state(PDO $pdo, int $uid, string $vid): array
{
    $acc = sb_access($pdo, $uid);
    $anyPaid = $acc['prep'] || $acc['readClasses'] || $acc['readSubjects'];
    $subs = $uid > 0 ? array_map(function ($r) use ($pdo) { return sb_sub_public($pdo, $r); }, sb_user_subscriptions($pdo, $uid)) : [];
    $pending = 0;
    if ($uid > 0) {
        $st = $pdo->prepare("SELECT COUNT(*) FROM payment_requests WHERE user_id = ? AND status = 'pending'");
        $st->execute([$uid]);
        $pending = (int)$st->fetchColumn();
    }
    return [
        'plan' => $anyPaid ? 'paid' : 'free',
        'unlocked' => false,
        'classes' => $acc['readClasses'],
        'features' => [
            'books' => true, 'meanings' => true, 'solutions' => true, 'games' => true, 'offlineBooks' => true, 'sync' => $uid > 0,
            'testPrep' => true, 'papers' => true, 'studyPlan' => true,           // available, each with its own free limit (see access and free)
        ],
        'limits' => new stdClass(),
        'access' => $acc,
        'free' => ['chapters' => SB_FREE_CHAPTERS] + sb_free_state($pdo, $uid, $vid),
        'subscriptions' => $subs,
        'pendingPayments' => $pending,
        'serverTime' => sb_iso(sb_now()),
        'visitor' => $vid,
    ];
}

// The account page: plans, payments, notices and expiry reminders. Only this user's own records.
function sb_account(PDO $pdo, int $uid): array
{
    $subs = array_map(function ($r) use ($pdo) { return sb_sub_public($pdo, $r, true); }, sb_user_subscriptions($pdo, $uid));
    $st = $pdo->prepare('SELECT id, kind, title, body, payment_id, read_at, created_at FROM notifications WHERE user_id = ? ORDER BY id DESC LIMIT 30');
    $st->execute([$uid]);
    $notes = array_map(function ($n) {
        return ['id' => (int)$n['id'], 'kind' => $n['kind'], 'title' => $n['title'], 'body' => $n['body'], 'paymentId' => $n['payment_id'] === null ? null : (int)$n['payment_id'], 'read' => $n['read_at'] !== null, 'at' => sb_iso($n['created_at'])];
    }, $st->fetchAll());
    $reminders = [];
    foreach ($subs as $s) {
        if ($s['status'] === 'active' && $s['daysLeft'] <= 7) $reminders[] = ['subscriptionId' => $s['id'], 'label' => $s['label'], 'daysLeft' => $s['daysLeft'], 'expiresAt' => $s['expiresAt'], 'text' => $s['label'] . ' ends in ' . $s['daysLeft'] . ' day' . ($s['daysLeft'] === 1 ? '' : 's') . '. Renew early and the new month is added after the end date.'];
        elseif ($s['status'] === 'expired') $reminders[] = ['subscriptionId' => $s['id'], 'label' => $s['label'], 'daysLeft' => 0, 'expiresAt' => $s['expiresAt'], 'text' => $s['label'] . ' has ended. Renew to open it again.'];
    }
    return ['subscriptions' => $subs, 'payments' => sb_user_payments($pdo, $uid), 'notifications' => $notes, 'reminders' => $reminders,
            'unread' => count(array_filter($notes, function ($n) { return !$n['read']; }))];
}

// ---------------------------------------------------------------- payment submission

function sb_trx_clean($raw): string
{
    return trim((string)$raw);
}

function sb_trx_valid(string $t): bool
{
    return (bool)preg_match('/^[A-Za-z0-9]{6,30}$/', $t);
}

function sb_payment_ref(PDO $pdo): string
{
    $alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    for ($i = 0; $i < 8; $i++) {
        $r = 'SB';
        for ($j = 0; $j < 8; $j++) $r .= $alphabet[random_int(0, strlen($alphabet) - 1)];
        $st = $pdo->prepare('SELECT 1 FROM payment_requests WHERE ref = ?');
        $st->execute([$r]);
        if (!$st->fetchColumn()) return $r;
    }
    throw new RuntimeException('Could not make a payment reference');
}

// $user: the signed-in users row. $in: plan, cls, subjects[], trx, paid_on, idem.
// ['ok' => true, 'payment' => public, 'repeat' => bool] or ['ok' => false, 'code' => http, 'error' => text]
function sb_payment_submit(PDO $pdo, array $user, array $in): array
{
    $fail = function (int $code, string $msg) { return ['ok' => false, 'code' => $code, 'error' => $msg]; };
    $uid = (int)$user['id'];
    $rl = sb_rate_hit($pdo, 'pay:u:' . $uid, 12, 3600);
    if (!$rl['ok']) return $fail(429, 'Too many payment submissions. Try again later');

    $type = strtolower(trim((string)(isset($in['plan']) ? $in['plan'] : '')));
    $sel = sb_validate_selection($type, isset($in['cls']) ? $in['cls'] : null, isset($in['subjects']) ? $in['subjects'] : []);
    if (!$sel['ok']) return $fail(422, $sel['error']);

    $trx = sb_trx_clean(isset($in['trx']) ? $in['trx'] : '');
    if ($trx === '') return $fail(422, 'Enter the Transaction ID (TID) from your Easypaisa receipt');
    if (!sb_trx_valid($trx)) return $fail(422, 'The Transaction ID must be 6 to 30 letters and numbers, exactly as Easypaisa shows it');
    $norm = strtoupper($trx);

    $paidOn = null;
    $po = isset($in['paid_on']) ? trim((string)$in['paid_on']) : '';
    if ($po !== '') {
        $d = DateTimeImmutable::createFromFormat('!Y-m-d', $po, new DateTimeZone('UTC'));
        if (!$d || $d->format('Y-m-d') !== $po) return $fail(422, 'The payment date is not a date');
        $today = new DateTimeImmutable(substr(sb_now(), 0, 10), new DateTimeZone('UTC'));
        if ($d > $today->modify('+1 day')) return $fail(422, 'The payment date cannot be in the future');
        if ($d < $today->modify('-60 day')) return $fail(422, 'The payment date is too old. Contact us on WhatsApp');
        $paidOn = $po;
    }

    $idemRaw = isset($in['idem']) ? (string)$in['idem'] : '';
    $idem = $idemRaw !== '' ? md5($uid . '|' . $idemRaw) : md5($uid . '|' . $norm . '|' . $type . '|' . sb_scope_key($type, $sel['cls'], $sel['subjects']));

    // the same submission again (a double tap, a retry after a lost answer) returns the one already saved
    $st = $pdo->prepare('SELECT * FROM payment_requests WHERE user_id = ? AND (idem_key = ? OR (trx_norm = ? AND status IN (\'pending\',\'approved\')))');
    $st->execute([$uid, $idem, $norm]);
    $same = $st->fetch();
    if ($same) return ['ok' => true, 'repeat' => true, 'payment' => sb_payment_public($pdo, $same), 'message' => SB_THANK_YOU];

    $st = $pdo->prepare("SELECT COUNT(*) FROM payment_requests WHERE user_id = ? AND status = 'pending'");
    $st->execute([$uid]);
    if ((int)$st->fetchColumn() >= 5) return $fail(429, 'You already have 5 payments waiting for verification. Please wait for them to be checked');

    $st = $pdo->prepare("SELECT user_id FROM payment_requests WHERE active_trx = ?");
    $st->execute([$norm]);
    if ($st->fetch()) return $fail(409, 'This Transaction ID has already been submitted. Check the number, or contact us on WhatsApp if you made this payment');

    $scope = sb_scope_key($type, $sel['cls'], $sel['subjects']);
    try {
        $ref = sb_payment_ref($pdo);
        $pdo->prepare('INSERT INTO payment_requests (ref, user_id, contact_name, contact_whatsapp, plan_type, class_id, subjects_json, scope_key, amount_pkr, duration_months,
                           method, trx_id, trx_norm, active_trx, paid_on, idem_key, platform) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, \'easypaisa\', ?, ?, ?, ?, ?, ?)')
            ->execute([$ref, $uid, mb_substr((string)$user['name'], 0, 100), (string)$user['whatsapp'], $type, $sel['cls'],
                $sel['subjects'] ? json_encode($sel['subjects']) : null, $scope, SB_PLAN_PRICE_PKR, $trx, $norm, $norm, $paidOn, $idem, sb_platform()]);
    } catch (PDOException $e) {
        if ($e->getCode() === '23000') {                                  // two taps at once, or the same TID from another account at the same moment
            $st = $pdo->prepare('SELECT * FROM payment_requests WHERE user_id = ? AND idem_key = ?');
            $st->execute([$uid, $idem]);
            $row = $st->fetch();
            if ($row) return ['ok' => true, 'repeat' => true, 'payment' => sb_payment_public($pdo, $row), 'message' => SB_THANK_YOU];
            return $fail(409, 'This Transaction ID has already been submitted. Check the number, or contact us on WhatsApp if you made this payment');
        }
        throw $e;
    }
    $id = (int)$pdo->lastInsertId();
    $st = $pdo->prepare('SELECT * FROM payment_requests WHERE id = ?');
    $st->execute([$id]);
    $row = $st->fetch();
    $label = sb_plan_label($type, $sel['cls'], $sel['subjects']);
    sb_notify($pdo, $uid, 'pay_pending', 'Payment received: Pending Verification', $label . ' · PKR ' . SB_PLAN_PRICE_PKR . ' · TID ' . $trx . '. Allow up to 1 hour. Your plan starts after approval.', $id);
    sb_audit($pdo, $uid, 'payment_submit', 'ref:' . $row['ref'] . ' plan:' . $type);
    return ['ok' => true, 'repeat' => false, 'payment' => sb_payment_public($pdo, $row), 'message' => SB_THANK_YOU];
}

// ---------------------------------------------------------------- administrator actions (called from manage/index.php and tests)

function sb_admin_audit_write(PDO $pdo, array $admin, string $action, string $targetType, $targetId, string $reason, array $detail): void
{
    $pdo->prepare('INSERT INTO admin_audit (admin_id, admin_name, action, target_type, target_id, reason, detail_json, ip) VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$admin['id'] === null ? null : (int)$admin['id'], substr((string)$admin['username'], 0, 40), substr($action, 0, 40), substr($targetType, 0, 20), substr((string)$targetId, 0, 40),
                   mb_substr($reason, 0, 300), json_encode($detail, JSON_UNESCAPED_UNICODE), sb_client_ip()]);
}

function sb_reason_ok(string $reason): bool
{
    return mb_strlen(trim($reason)) >= 3;
}

function sb_clean_reason(string $reason): string
{
    return mb_substr(trim(preg_replace('/[\x00-\x1f\x7f]+/u', ' ', $reason)), 0, 300);
}

function sb_sub_event(PDO $pdo, int $subId, string $event, ?int $paymentId, array $admin, ?string $old, ?string $new, string $reason): void
{
    $pdo->prepare('INSERT INTO subscription_events (subscription_id, event, payment_id, admin_id, admin_name, old_expires_at, new_expires_at, reason) VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$subId, $event, $paymentId, $admin['id'] === null ? null : (int)$admin['id'], substr((string)$admin['username'], 0, 40), $old, $new, $reason]);
}

function sb_in_tx(PDO $pdo, callable $fn)
{
    $pdo->beginTransaction();
    try {
        $r = $fn();
        $pdo->commit();
        return $r;
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
}

// Approve or reject a pending payment. Idempotent: a second approval (a double click, two administrators) changes nothing and grants nothing.
// ['ok' => bool, 'error' => text, 'already' => bool, 'status' => 'approved'|'rejected', 'subscription' => id, 'startsAt','expiresAt']
function sb_payment_review(PDO $pdo, array $admin, int $paymentId, string $decision, string $note): array
{
    if ($decision !== 'approve' && $decision !== 'reject') return ['ok' => false, 'error' => 'Unknown decision'];
    $note = sb_clean_reason($note);
    if ($decision === 'reject' && !sb_reason_ok($note)) return ['ok' => false, 'error' => 'Please give a short reason for rejecting (the student sees it)'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $paymentId, $decision, $note) {
        $st = $pdo->prepare('SELECT * FROM payment_requests WHERE id = ? FOR UPDATE');
        $st->execute([$paymentId]);
        $p = $st->fetch();
        if (!$p) return ['ok' => false, 'error' => 'No such payment'];
        if ($p['status'] !== 'pending') {
            $same = ($decision === 'approve' && $p['status'] === 'approved') || ($decision === 'reject' && $p['status'] === 'rejected');
            if ($same) return ['ok' => true, 'already' => true, 'status' => $p['status'], 'subscription' => $p['subscription_id'] === null ? null : (int)$p['subscription_id'], 'expiresAt' => sb_iso($p['expires_at'])];
            return ['ok' => false, 'error' => 'This payment was already ' . $p['status'] . '. Ask the student to submit it again if it was a mistake'];
        }
        $uid = (int)$p['user_id'];
        $label = sb_plan_label($p['plan_type'], $p['class_id'], $p['subjects_json'] ? (json_decode($p['subjects_json'], true) ?: []) : []);
        $now = sb_now();
        if ($decision === 'reject') {
            $pdo->prepare("UPDATE payment_requests SET status = 'rejected', active_trx = NULL, reviewed_by = ?, reviewed_by_name = ?, reviewed_at = ?, review_note = ? WHERE id = ? AND status = 'pending'")
                ->execute([$admin['id'], substr((string)$admin['username'], 0, 40), $now, $note, $paymentId]);
            if ($uid > 0 && sb_user_exists($pdo, $uid)) sb_notify($pdo, $uid, 'pay_rejected', 'Payment not approved', $label . ' · TID ' . $p['trx_id'] . '. Reason: ' . $note, $paymentId);
            sb_admin_audit_write($pdo, $admin, 'payment_reject', 'payment', $paymentId, $note, ['ref' => $p['ref'], 'user' => $uid, 'trx' => $p['trx_id'], 'plan' => $label]);
            return ['ok' => true, 'status' => 'rejected'];
        }

        // approve: a matching subscription that is still running gets the month added after its end; otherwise a new one starts now
        $subjects = $p['subjects_json'] ? (json_decode($p['subjects_json'], true) ?: []) : [];
        $months = (int)$p['duration_months'];
        $st = $pdo->prepare('SELECT * FROM subscriptions WHERE user_id = ? AND scope_key = ? AND plan_type = ? ORDER BY expires_at DESC, id DESC LIMIT 1 FOR UPDATE');
        $st->execute([$uid, $p['scope_key'], $p['plan_type']]);
        $m = $st->fetch();
        $subId = 0; $startsAt = $now; $expires = null; $event = 'activated';
        if ($m && $m['status'] === 'suspended' && strtotime($m['expires_at'] . ' UTC') > strtotime($now . ' UTC')) {
            return ['ok' => false, 'error' => 'This student has a suspended subscription for the same plan. Restore or end it first (Subscriptions), then approve'];
        }
        if ($m && $m['status'] === 'active' && strtotime($m['expires_at'] . ' UTC') > strtotime($now . ' UTC')) {
            $subId = (int)$m['id'];
            $startsAt = $m['expires_at'];                                  // the added month starts where the running one ends
            $expires = sb_add_months($m['expires_at'], $months);
            $pdo->prepare('UPDATE subscriptions SET expires_at = ? WHERE id = ?')->execute([$expires, $subId]);
            sb_sub_event($pdo, $subId, 'renewed', $paymentId, $admin, $m['expires_at'], $expires, 'Payment ' . $p['ref']);
        } else {
            $expires = sb_add_months($now, $months);
            $pdo->prepare("INSERT INTO subscriptions (user_id, plan_type, class_id, scope_key, status, starts_at, expires_at, source) VALUES (?, ?, ?, ?, 'active', ?, ?, 'payment')")
                ->execute([$uid, $p['plan_type'], $p['class_id'], $p['scope_key'], $now, $expires]);
            $subId = (int)$pdo->lastInsertId();
            if ($p['plan_type'] === 'teacher') {
                $cat = sb_catalog();
                $ins = $pdo->prepare('INSERT INTO subscription_subjects (subscription_id, class_id, subject_id) VALUES (?, ?, ?)');
                foreach ($subjects as $sid) $ins->execute([$subId, isset($cat['subjects'][$sid]) ? $cat['subjects'][$sid]['class'] : '', $sid]);
            }
            sb_sub_event($pdo, $subId, 'activated', $paymentId, $admin, null, $expires, 'Payment ' . $p['ref']);
        }
        $pdo->prepare("UPDATE payment_requests SET status = 'approved', reviewed_by = ?, reviewed_by_name = ?, reviewed_at = ?, review_note = ?, subscription_id = ?, activated_at = ?, expires_at = ? WHERE id = ? AND status = 'pending'")
            ->execute([$admin['id'], substr((string)$admin['username'], 0, 40), $now, $note, $subId, $startsAt, $expires, $paymentId]);
        if (sb_user_exists($pdo, $uid)) sb_notify($pdo, $uid, 'pay_approved', 'Payment approved. Your plan is active!', $label . ' is active until ' . sb_nice_date($expires) . '.', $paymentId, $subId);
        sb_admin_audit_write($pdo, $admin, 'payment_approve', 'payment', $paymentId, $note, ['ref' => $p['ref'], 'user' => $uid, 'trx' => $p['trx_id'], 'plan' => $label, 'subscription' => $subId, 'startsAt' => $startsAt, 'expiresAt' => $expires, 'renewal' => $event !== 'activated' || ($m && $startsAt === $m['expires_at'])]);
        return ['ok' => true, 'status' => 'approved', 'subscription' => $subId, 'startsAt' => sb_iso($startsAt), 'expiresAt' => sb_iso($expires)];
    });
}

function sb_user_exists(PDO $pdo, int $uid): bool
{
    $st = $pdo->prepare('SELECT 1 FROM users WHERE id = ?');
    $st->execute([$uid]);
    return (bool)$st->fetchColumn();
}

function sb_sub_row(PDO $pdo, int $id, bool $lock = false): ?array
{
    $st = $pdo->prepare('SELECT * FROM subscriptions WHERE id = ?' . ($lock ? ' FOR UPDATE' : ''));
    $st->execute([$id]);
    $r = $st->fetch();
    return $r ? $r : null;
}

function sb_sub_suspend(PDO $pdo, array $admin, int $subId, string $reason): array
{
    $reason = sb_clean_reason($reason);
    if (!sb_reason_ok($reason)) return ['ok' => false, 'error' => 'A reason is required'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $subId, $reason) {
        $s = sb_sub_row($pdo, $subId, true);
        if (!$s) return ['ok' => false, 'error' => 'No such subscription'];
        if ($s['status'] === 'suspended') return ['ok' => true, 'already' => true];
        $pdo->prepare("UPDATE subscriptions SET status = 'suspended', suspended_at = ?, suspend_reason = ? WHERE id = ?")->execute([sb_now(), $reason, $subId]);
        sb_sub_event($pdo, $subId, 'suspended', null, $admin, $s['expires_at'], $s['expires_at'], $reason);
        sb_notify($pdo, (int)$s['user_id'], 'sub_suspended', 'A plan was suspended', sb_plan_label($s['plan_type'], $s['class_id'], sb_sub_subjects($pdo, $subId)) . '. ' . $reason . ' Contact us on WhatsApp if this is a mistake.', null, $subId);
        sb_admin_audit_write($pdo, $admin, 'sub_suspend', 'subscription', $subId, $reason, ['user' => (int)$s['user_id'], 'expiresAt' => $s['expires_at']]);
        return ['ok' => true];
    });
}

function sb_sub_restore(PDO $pdo, array $admin, int $subId, string $reason): array
{
    $reason = sb_clean_reason($reason);
    if (!sb_reason_ok($reason)) return ['ok' => false, 'error' => 'A reason is required'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $subId, $reason) {
        $s = sb_sub_row($pdo, $subId, true);
        if (!$s) return ['ok' => false, 'error' => 'No such subscription'];
        if ($s['status'] !== 'suspended') return ['ok' => true, 'already' => true];
        $pdo->prepare("UPDATE subscriptions SET status = 'active', suspended_at = NULL, suspend_reason = '' WHERE id = ?")->execute([$subId]);
        sb_sub_event($pdo, $subId, 'restored', null, $admin, $s['expires_at'], $s['expires_at'], $reason);
        sb_notify($pdo, (int)$s['user_id'], 'sub_restored', 'Your plan is active again', sb_plan_label($s['plan_type'], $s['class_id'], sb_sub_subjects($pdo, $subId)) . ' is active until ' . sb_nice_date($s['expires_at']) . '.', null, $subId);
        sb_admin_audit_write($pdo, $admin, 'sub_restore', 'subscription', $subId, $reason, ['user' => (int)$s['user_id'], 'expiresAt' => $s['expires_at']]);
        return ['ok' => true];
    });
}

// A free grant: a new subscription starting now for $days days, or (same user, same plan, still running) days added to it.
function sb_sub_grant(PDO $pdo, array $admin, int $uid, string $type, $cls, $subjects, int $days, string $reason): array
{
    $reason = sb_clean_reason($reason);
    if (!sb_reason_ok($reason)) return ['ok' => false, 'error' => 'A reason is required'];
    if ($days < 1 || $days > 731) return ['ok' => false, 'error' => 'Days must be between 1 and 731'];
    $sel = sb_validate_selection($type, $cls, $subjects);
    if (!$sel['ok']) return $sel;
    if (!sb_user_exists($pdo, $uid)) return ['ok' => false, 'error' => 'No such account'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $uid, $type, $sel, $days, $reason) {
        $scope = sb_scope_key($type, $sel['cls'], $sel['subjects']);
        $now = sb_now();
        $st = $pdo->prepare('SELECT * FROM subscriptions WHERE user_id = ? AND scope_key = ? AND plan_type = ? ORDER BY expires_at DESC, id DESC LIMIT 1 FOR UPDATE');
        $st->execute([$uid, $scope, $type]);
        $m = $st->fetch();
        if ($m && $m['status'] === 'active' && strtotime($m['expires_at'] . ' UTC') > strtotime($now . ' UTC')) {
            $new = sb_add_days($m['expires_at'], $days);
            $pdo->prepare('UPDATE subscriptions SET expires_at = ? WHERE id = ?')->execute([$new, $m['id']]);
            sb_sub_event($pdo, (int)$m['id'], 'granted', null, $admin, $m['expires_at'], $new, $reason);
            $subId = (int)$m['id']; $old = $m['expires_at'];
        } else {
            if ($m && $m['status'] === 'suspended' && strtotime($m['expires_at'] . ' UTC') > strtotime($now . ' UTC')) return ['ok' => false, 'error' => 'This account has a suspended subscription for the same plan: restore it first'];
            $new = sb_add_days($now, $days); $old = null;
            $pdo->prepare("INSERT INTO subscriptions (user_id, plan_type, class_id, scope_key, status, starts_at, expires_at, source) VALUES (?, ?, ?, ?, 'active', ?, ?, 'grant')")
                ->execute([$uid, $type, $sel['cls'], $scope, $now, $new]);
            $subId = (int)$pdo->lastInsertId();
            if ($type === 'teacher') {
                $cat = sb_catalog();
                $ins = $pdo->prepare('INSERT INTO subscription_subjects (subscription_id, class_id, subject_id) VALUES (?, ?, ?)');
                foreach ($sel['subjects'] as $sid) $ins->execute([$subId, $cat['subjects'][$sid]['class'], $sid]);
            }
            sb_sub_event($pdo, $subId, 'granted', null, $admin, null, $new, $reason);
        }
        $label = sb_plan_label($type, $sel['cls'], $sel['subjects']);
        sb_notify($pdo, $uid, 'sub_granted', 'You were given free access', $label . ' is active until ' . sb_nice_date($new) . '.', null, $subId);
        sb_admin_audit_write($pdo, $admin, 'sub_grant', 'subscription', $subId, $reason, ['user' => $uid, 'plan' => $label, 'days' => $days, 'from' => $old, 'to' => $new]);
        return ['ok' => true, 'subscription' => $subId, 'expiresAt' => sb_iso($new)];
    });
}

// Subscriptions an extension would touch. $f: users[] (empty = everybody), plan ('', 'student', 'teacher', 'prep'), states[] of 'active','expired','suspended'.
function sb_ext_targets(PDO $pdo, array $f): array
{
    $where = []; $args = [];
    $users = array_values(array_filter(array_map('intval', isset($f['users']) && is_array($f['users']) ? $f['users'] : []), function ($x) { return $x > 0; }));
    if ($users) { $where[] = 's.user_id IN (' . implode(',', array_fill(0, count($users), '?')) . ')'; $args = array_merge($args, $users); }
    $plan = isset($f['plan']) ? (string)$f['plan'] : '';
    if (in_array($plan, ['student', 'teacher', 'prep'], true)) { $where[] = 's.plan_type = ?'; $args[] = $plan; }
    $states = array_values(array_intersect(isset($f['states']) && is_array($f['states']) ? $f['states'] : ['active'], ['active', 'expired', 'suspended']));
    if (!$states) $states = ['active'];
    $now = sb_now();
    $sq = [];
    if (in_array('active', $states, true))    { $sq[] = "(s.status = 'active' AND s.expires_at > ?)"; $args[] = $now; }
    if (in_array('expired', $states, true))   { $sq[] = "(s.status = 'active' AND s.expires_at <= ?)"; $args[] = $now; }
    if (in_array('suspended', $states, true)) { $sq[] = "(s.status = 'suspended')"; }
    $where[] = '(' . implode(' OR ', $sq) . ')';
    $sql = 'SELECT s.*, u.name AS user_name, u.whatsapp FROM subscriptions s JOIN users u ON u.id = s.user_id' . ($where ? ' WHERE ' . implode(' AND ', $where) : '') . ' ORDER BY s.id';
    $st = $pdo->prepare($sql);
    $st->execute($args);
    return $st->fetchAll();
}

// The new expiry for one subscription. mode 'add_days' adds to the later of its end and now; 'set_date' sets 23:59:59 UTC of a date after its current end.
function sb_ext_new_expiry(array $s, string $mode, string $value): ?string
{
    $now = sb_now();
    if ($mode === 'add_days') {
        $days = (int)$value;
        if ($days < 1 || $days > 731) return null;
        $base = strtotime($s['expires_at'] . ' UTC') > strtotime($now . ' UTC') ? $s['expires_at'] : $now;
        return sb_add_days($base, $days);
    }
    if ($mode === 'set_date') {
        $d = DateTimeImmutable::createFromFormat('!Y-m-d', $value, new DateTimeZone('UTC'));
        if (!$d || $d->format('Y-m-d') !== $value) return null;
        $new = $d->format('Y-m-d') . ' 23:59:59';
        if (strtotime($new . ' UTC') <= strtotime($now . ' UTC')) return null;
        if (strtotime($new . ' UTC') <= strtotime($s['expires_at'] . ' UTC')) return null;
        return $new;
    }
    return null;
}

// The preview: who is touched and what each new end date would be. 'hash' ties the confirmation to exactly this list.
function sb_ext_preview(PDO $pdo, array $f, string $mode, string $value): array
{
    $rows = sb_ext_targets($pdo, $f);
    $items = []; $skipped = 0; $ids = [];
    foreach ($rows as $s) {
        $new = sb_ext_new_expiry($s, $mode, $value);
        if ($new === null) { $skipped++; continue; }
        $ids[] = (int)$s['id'];
        $items[] = ['id' => (int)$s['id'], 'user' => (int)$s['user_id'], 'name' => $s['user_name'], 'plan' => $s['plan_type'], 'from' => $s['expires_at'], 'to' => $new, 'state' => sb_sub_status($s)];
    }
    return ['ok' => true, 'items' => $items, 'count' => count($items), 'skipped' => $skipped, 'hash' => sha1(implode(',', $ids) . '|' . $mode . '|' . $value)];
}

function sb_ext_apply(PDO $pdo, array $admin, array $f, string $mode, string $value, string $hash, string $reason): array
{
    $reason = sb_clean_reason($reason);
    if (!sb_reason_ok($reason)) return ['ok' => false, 'error' => 'A reason is required'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $f, $mode, $value, $hash, $reason) {
        $pv = sb_ext_preview($pdo, $f, $mode, $value);
        if (!hash_equals($pv['hash'], $hash)) return ['ok' => false, 'error' => 'The list changed since you previewed it. Preview again'];
        if ($pv['count'] === 0) return ['ok' => false, 'error' => 'No subscription would change'];
        $done = 0; $users = [];
        foreach ($pv['items'] as $it) {
            $s = sb_sub_row($pdo, $it['id'], true);
            if (!$s) continue;
            $new = sb_ext_new_expiry($s, $mode, $value);
            if ($new === null) continue;
            $pdo->prepare('UPDATE subscriptions SET expires_at = ? WHERE id = ?')->execute([$new, $s['id']]);
            sb_sub_event($pdo, (int)$s['id'], $mode === 'add_days' ? 'extended' : 'set_expiry', null, $admin, $s['expires_at'], $new, $reason);
            sb_notify($pdo, (int)$s['user_id'], 'sub_extended', 'Your plan was extended', sb_plan_label($s['plan_type'], $s['class_id'], sb_sub_subjects($pdo, (int)$s['id'])) . ' now ends on ' . sb_nice_date($new) . '.', null, (int)$s['id']);
            $done++; $users[(int)$s['user_id']] = true;
        }
        sb_admin_audit_write($pdo, $admin, 'sub_extend', 'bulk', $done, $reason, ['mode' => $mode, 'value' => $value, 'subscriptions' => $done, 'users' => count($users), 'filter' => $f, 'ids' => array_slice(array_column($pv['items'], 'id'), 0, 200)]);
        return ['ok' => true, 'count' => $done, 'users' => count($users)];
    });
}

// Suspend or restore a whole account (the existing 'blocked' status: sign-in and sync stop at once).
function sb_account_set_status(PDO $pdo, array $admin, int $uid, string $to, string $reason): array
{
    $reason = sb_clean_reason($reason);
    if (!sb_reason_ok($reason)) return ['ok' => false, 'error' => 'A reason is required'];
    if ($to !== 'blocked' && $to !== 'active') return ['ok' => false, 'error' => 'Unknown status'];
    return sb_in_tx($pdo, function () use ($pdo, $admin, $uid, $to, $reason) {
        $st = $pdo->prepare('SELECT id, role, status FROM users WHERE id = ? FOR UPDATE');
        $st->execute([$uid]);
        $u = $st->fetch();
        if (!$u || $u['status'] === 'deleted') return ['ok' => false, 'error' => 'No such account'];
        if ($u['status'] === $to) return ['ok' => true, 'already' => true];
        $pdo->prepare('UPDATE users SET status = ? WHERE id = ?')->execute([$to, $uid]);
        if ($to === 'blocked') sb_device_revoke_all($pdo, $uid);
        sb_audit($pdo, $uid, $to === 'blocked' ? 'admin_block' : 'admin_unblock', 'by:' . $admin['username']);
        sb_admin_audit_write($pdo, $admin, $to === 'blocked' ? 'user_suspend' : 'user_restore', 'user', $uid, $reason, ['from' => $u['status'], 'to' => $to]);
        return ['ok' => true];
    });
}
