<?php
// What the caller may use: the one server-side source for payment-plan gates, shared by the website and the
// Android app. Compatible with PHP 7.4.
//
//   GET api/v2/entitlements.php      (guest, or 'Authorization: Bearer <device token>', or the session cookie; X-SB-Visitor for a guest)
//     -> {ok, plan, signedIn, unlocked:false, classes, features{...}, access{...}, free{...}, subscriptions[...], version, flags{syncV2}}
//
// Version 2 (billing): Chapter 1 of every subject, 50 Test Preparation questions, 50 Study Plan questions and 1 paper are free; the rest
// opens with an approved payment (api/lib/billing.php holds every rule). `access` lists what the paid plans open, `free` how much of the
// free allowance is used. Both clients read this answer, so a change here needs no app update. A client that cannot reach this endpoint
// keeps the last answer it saw (never a paid answer past its expiry), and on a first run treats everything as free-tier.

require __DIR__ . '/../db.php';
require_once __DIR__ . '/../lib/security.php';
require_once __DIR__ . '/../lib/flags.php';
require_once __DIR__ . '/../lib/billing.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const SB_ENTITLEMENTS_VERSION = 2;

$uid = 0; $state = null;
try {
    $pdo = db();
    $uid = sb_actor_uid($pdo);
    $given = sb_visitor_from_request();
    $vid = sb_visitor_touch($pdo, $given, $uid, true);
    if ($vid !== '' && $vid !== $given && PHP_SAPI !== 'cli') {
        setcookie('sb_vid', $vid, ['expires' => time() + 86400 * 365, 'path' => '/', 'httponly' => true, 'samesite' => 'Lax', 'secure' => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off']);
    }
    $state = sb_state($pdo, $uid, $vid);
} catch (Throwable $e) {
    error_log('SpaceBook entitlements: ' . $e->getMessage());
}

if ($state === null) {        // the database could not be asked: say so, clients keep their last answer
    http_response_code(503);
    echo json_encode(['ok' => false, 'error' => 'Temporarily unavailable', 'version' => SB_ENTITLEMENTS_VERSION, 'flags' => sb_flags()]);
    exit;
}
echo json_encode(['ok' => true, 'signedIn' => $uid > 0, 'version' => SB_ENTITLEMENTS_VERSION, 'flags' => sb_flags()] + $state, JSON_UNESCAPED_UNICODE);
