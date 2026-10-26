<?php
// News feed: posts students write for each other, with likes, comments, shares and reports. Compatible with PHP 7.4.
// The rules (what may be posted, what is shown of a person, when a post hides itself) are in api/lib/feed.php.
//
//   GET  api/feed.php?action=list[&before=<post id>][&limit=20][&mine=1][&kind=question]   -> {ok, posts:[...], next}      next = the id to pass as `before`, 0 = no more
//   GET  api/feed.php?action=post&id=N                                      -> {ok, post}
//   GET  api/feed.php?action=comments&post=N[&before=<comment id>]          -> {ok, comments:[{..., replies:[...]}], next}
//   POST api/feed.php?action=create   {kind, body, card}                    kind: text | question | stats | progress | plan     -> {ok, post}
//   POST api/feed.php?action=share    {id, body}                            share a post into the feed                          -> {ok, post, shares}
//   POST api/feed.php?action=like     {type:'post'|'comment', id, on:bool}  -> {ok, likes, liked}
//   POST api/feed.php?action=comment  {post, body, parent}                  -> {ok, comment, count}
//   POST api/feed.php?action=delete   {id}                                  delete your own post
//   POST api/feed.php?action=comment_delete {id}                            delete your own comment                             -> {ok, count}
//   POST api/feed.php?action=report   {type:'post'|'comment', id, reason, note}                                                  -> {ok, hidden}
//
// Everything needs a signed-in student: 'Authorization: Bearer <device token>' (the Android app) or the session cookie (then a write must be
// same-site). Reading is for signed-in students only. Errors are {ok:false, error:"text for the student"}.

require __DIR__ . '/db.php';
require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/feed.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const FEED_RATE_READ    = 240;       // reads per minute
const FEED_RATE_POST    = 12;        // posts and shares per hour
const FEED_RATE_COMMENT = 60;        // comments per hour
const FEED_RATE_LIKE    = 300;       // likes per hour
const FEED_RATE_REPORT  = 30;        // reports per hour
const FEED_RATE_DELETE  = 60;        // deletions per hour

function feed_reply(int $code, array $body, int $retryAfter = 0): void
{
    if ($retryAfter > 0) header('Retry-After: ' . $retryAfter);
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_PARTIAL_OUTPUT_ON_ERROR);
    exit;
}

function feed_fail(int $code, string $msg, int $retryAfter = 0): void
{
    feed_reply($code, ['ok' => false, 'error' => $msg], $retryAfter);
}

function feed_input(): array
{
    $raw = (string)file_get_contents('php://input', false, null, 0, 70000);
    $data = json_decode($raw, true);
    return is_array($data) ? $data : [];
}

function feed_limit(PDO $pdo, string $bucket, int $limit, int $window, string $message): void
{
    $rl = sb_rate_hit($pdo, $bucket, $limit, $window);
    if (!$rl['ok']) feed_fail(429, $message, $rl['retry']);
}

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    feed_fail(500, 'Database connection failed');
}

$method = $_SERVER['REQUEST_METHOD'];
$action = isset($_GET['action']) ? (string)$_GET['action'] : '';
if ($method !== 'GET' && $method !== 'POST') feed_fail(405, 'GET or POST required');

// ---- who is calling
$uid = 0;
$dev = sb_device_from_request($pdo);
if ($dev) {
    $uid = $dev['user_id'];
} elseif (sb_bearer_token() === '' && isset($_COOKIE['spacebook_sid'])) {
    require __DIR__ . '/session.php';
    if (!empty($_SESSION['uid'])) {
        if ($method === 'POST' && !sb_request_is_same_site()) feed_fail(403, 'Request not allowed');
        $st = $pdo->prepare("SELECT id FROM users WHERE id = ? AND status = 'active'");
        $st->execute([(int)$_SESSION['uid']]);
        if ($st->fetch()) $uid = (int)$_SESSION['uid'];
    }
}
if ($uid <= 0) feed_fail(401, 'Sign in to see the News Feed');

$writes = ['create', 'share', 'like', 'comment', 'delete', 'comment_delete', 'report'];
if (in_array($action, $writes, true) && $method !== 'POST') feed_fail(405, 'POST required');
if (!in_array($action, $writes, true)) feed_limit($pdo, 'fread:u:' . $uid, FEED_RATE_READ, 60, 'Slow down a little, then pull to refresh');

function feed_kind_of(string $t): string
{
    return $t === 'comment' || $t === 'c' ? 'c' : 'p';
}

try {
    switch ($action) {

    case 'list':
        $r = sb_feed_list($pdo, $uid, max(0, (int)(isset($_GET['before']) ? $_GET['before'] : 0)), (int)(isset($_GET['limit']) ? $_GET['limit'] : SB_FEED_PAGE), !empty($_GET['mine']), isset($_GET['kind']) ? (string)$_GET['kind'] : '');
        feed_reply(200, ['ok' => true, 'posts' => $r['posts'], 'next' => $r['next'], 'now' => (int)round(microtime(true) * 1000)]);

    case 'post':
        $p = sb_feed_get($pdo, $uid, (int)(isset($_GET['id']) ? $_GET['id'] : 0));
        if (!$p) feed_fail(404, 'That post is no longer there');
        feed_reply(200, ['ok' => true, 'post' => $p]);

    case 'comments':
        $r = sb_feed_comments($pdo, $uid, (int)(isset($_GET['post']) ? $_GET['post'] : 0), max(0, (int)(isset($_GET['before']) ? $_GET['before'] : 0)));
        if ($r === null) feed_fail(404, 'That post is no longer there');
        feed_reply(200, ['ok' => true, 'comments' => $r['comments'], 'next' => $r['next']]);

    case 'create':
    case 'share':
        feed_limit($pdo, 'fpost:u:' . $uid, FEED_RATE_POST, 3600, 'You have posted a lot in the last hour. Try again a little later');
        $in = feed_input();
        if ($action === 'share') $res = sb_feed_create($pdo, $uid, 'share', isset($in['body']) ? $in['body'] : '', null, (int)(isset($in['id']) ? $in['id'] : 0));
        else $res = sb_feed_create($pdo, $uid, isset($in['kind']) && is_string($in['kind']) ? $in['kind'] : 'text', isset($in['body']) ? $in['body'] : '', isset($in['card']) ? $in['card'] : null);
        if (!$res['ok']) feed_fail($res['code'], $res['error']);
        sb_audit($pdo, $uid, $action === 'share' ? 'feed_share' : 'feed_post', 'post ' . $res['id']);
        $post = sb_feed_get($pdo, $uid, $res['id']);
        $out = ['ok' => true, 'post' => $post];
        if ($action === 'share' && $post && !empty($post['shared'])) {
            $st = $pdo->prepare('SELECT share_count FROM feed_posts WHERE id = ?');
            $st->execute([$post['shared']['id']]);
            $out['shares'] = (int)$st->fetchColumn();
        }
        feed_reply(201, $out);

    case 'like':
        feed_limit($pdo, 'flike:u:' . $uid, FEED_RATE_LIKE, 3600, 'Too many likes for now. Try again a little later');
        $in = feed_input();
        $type = feed_kind_of(isset($in['type']) ? (string)$in['type'] : 'post');
        $on = !array_key_exists('on', $in) || !empty($in['on']);
        $n = sb_feed_like($pdo, $uid, $type, (int)(isset($in['id']) ? $in['id'] : 0), $on);
        if ($n === null) feed_fail(404, 'That is no longer there');
        feed_reply(200, ['ok' => true, 'likes' => $n, 'liked' => $on]);

    case 'comment':
        feed_limit($pdo, 'fcom:u:' . $uid, FEED_RATE_COMMENT, 3600, 'You have commented a lot in the last hour. Try again a little later');
        $in = feed_input();
        $res = sb_feed_add_comment($pdo, $uid, (int)(isset($in['post']) ? $in['post'] : 0), isset($in['body']) ? $in['body'] : '', (int)(isset($in['parent']) ? $in['parent'] : 0));
        if (!$res['ok']) feed_fail($res['code'], $res['error']);
        feed_reply(201, ['ok' => true, 'comment' => $res['comment'], 'count' => $res['count']]);

    case 'delete':
        feed_limit($pdo, 'fdel:u:' . $uid, FEED_RATE_DELETE, 3600, 'Too many deletions for now');
        $in = feed_input();
        if (!sb_feed_delete_post($pdo, $uid, (int)(isset($in['id']) ? $in['id'] : 0))) feed_fail(404, 'That post is not yours or is already gone');
        feed_reply(200, ['ok' => true]);

    case 'comment_delete':
        feed_limit($pdo, 'fdel:u:' . $uid, FEED_RATE_DELETE, 3600, 'Too many deletions for now');
        $in = feed_input();
        $n = sb_feed_delete_comment($pdo, $uid, (int)(isset($in['id']) ? $in['id'] : 0));
        if ($n === null) feed_fail(404, 'That comment is not yours or is already gone');
        feed_reply(200, ['ok' => true, 'count' => $n]);

    case 'report':
        feed_limit($pdo, 'frep:u:' . $uid, FEED_RATE_REPORT, 3600, 'Too many reports for now. Thank you, we will look at them');
        $in = feed_input();
        $res = sb_feed_report($pdo, $uid, feed_kind_of(isset($in['type']) ? (string)$in['type'] : 'post'), (int)(isset($in['id']) ? $in['id'] : 0), isset($in['reason']) ? (string)$in['reason'] : '', isset($in['note']) ? $in['note'] : '');
        if (!$res['ok']) feed_fail($res['code'], $res['error']);
        sb_audit($pdo, $uid, 'feed_report', (isset($in['type']) && $in['type'] === 'comment' ? 'comment ' : 'post ') . (int)$in['id']);
        feed_reply(200, ['ok' => true, 'hidden' => $res['hidden']]);

    default:
        feed_fail(400, 'Unknown action');
    }
} catch (Throwable $e) {
    error_log('SpaceBook feed: ' . $e->getMessage());
    feed_fail(500, 'Could not do that, try again');
}
