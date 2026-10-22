<?php
// What the caller may use: the one server-side source for payment-plan gates, shared by the website and the
// Android app. Compatible with PHP 7.4.
//
//   GET api/v2/entitlements.php      (guest, or 'Authorization: Bearer <device token>', or the session cookie)
//     -> {ok, plan, signedIn, unlocked, classes, features{...}, limits{...}, version}
//
// Today everything is unlocked ("free for everyone"). To start limiting later, change sb_entitlements() below
// (for example read a `plan` column or a payments table for $uid); both clients read this answer, so no app
// update is needed. A client that cannot reach this endpoint keeps the last answer it saw and, on a first run,
// treats everything as unlocked.

require __DIR__ . '/../db.php';
require_once __DIR__ . '/../lib/security.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const SB_ENTITLEMENTS_VERSION = 1;

// $uid is 0 for a guest. Return the plan name and what it allows.
function sb_entitlements(int $uid): array
{
    $features = [
        'books'         => true,   // read the textbooks
        'meanings'      => true,   // word and sentence meanings
        'solutions'     => true,   // step-by-step and animated solutions
        'testPrep'      => true,
        'papers'        => true,
        'studyPlan'     => true,
        'games'         => true,
        'offlineBooks'  => true,
        'sync'          => $uid > 0,
    ];
    return [
        'plan'     => 'free',
        'unlocked' => true,
        'classes'  => 'all',       // or a list such as ['cls1','cls2']
        'features' => $features,
        'limits'   => new stdClass(), // e.g. {"testsPerDay": 5} when a plan needs it
    ];
}

$uid = 0;
try {
    $pdo = db();
    $dev = sb_device_from_request($pdo);
    if ($dev) {
        $uid = $dev['user_id'];
    } elseif (sb_bearer_token() === '' && isset($_COOKIE['spacebook_sid'])) {
        require __DIR__ . '/../session.php';
        if (!empty($_SESSION['uid'])) $uid = (int)$_SESSION['uid'];
    }
} catch (Throwable $e) {
    error_log('SpaceBook entitlements: ' . $e->getMessage());   // a database problem must not lock students out
}

echo json_encode(['ok' => true, 'signedIn' => $uid > 0, 'version' => SB_ENTITLEMENTS_VERSION] + sb_entitlements($uid), JSON_UNESCAPED_UNICODE);
