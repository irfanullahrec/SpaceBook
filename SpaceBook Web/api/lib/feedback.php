<?php
// Feedback: suggestions, bug reports, textbook mistakes and wrong answers / meanings / translations, with an optional picture.
// The rules live here so that api/feedback.php, api/admin.php, the export and the tests share them. Compatible with PHP 7.4.
//
//  * A report may come from a student who is not signed in. Nothing but what the form shows is stored: the kind, the words the student wrote,
//    a short "where was I" context (class, subject, book, chapter, page, screen, versions: a whitelist of short strings, see sb_fb_clean_context),
//    and the account id when the student is signed in. No address, no device name, no user agent beyond a short platform word.
//  * A picture is a JPEG, PNG or WebP of at most 1.5 MB. When PHP has the GD extension the server decodes it and stores a new JPEG of at most
//    1600 pixels (this drops location data and anything hidden after the image); without GD the bytes are kept only after the header, the size and a
//    scan for script text have passed. It is stored in the database, never as a file, and is served only to administrators.
//  * client_id (a UUID made on the device) makes a retry harmless: the second send answers with the first report.
//  * Reports of closed items are not kept forever (sb_fb_prune: pictures 90 days after the report was closed, closed reports after a year).

const SB_FB_KINDS    = ['suggestion', 'bug', 'content', 'translation', 'answer'];
const SB_FB_STATUSES = ['new', 'seen', 'fixed', 'wontfix', 'duplicate'];
const SB_FB_MIN_MESSAGE = 5;
const SB_FB_MAX_MESSAGE = 2000;
const SB_FB_MAX_IMAGE   = 1572864;        // bytes as received

function sb_fb_uuid_ok($s): bool
{
    return is_string($s) && preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i', $s) === 1;
}

// One line of plain text: valid UTF-8, no control characters, cut to $max characters.
function sb_fb_line($v, int $max): string
{
    if (is_int($v) || is_float($v)) $v = (string)$v;
    if (!is_string($v) || !mb_check_encoding($v, 'UTF-8')) return '';
    $v = preg_replace('/[\x00-\x1F\x7F]+/', ' ', $v);
    return mb_substr(trim((string)$v), 0, $max);
}

// The "where was I" context: only these keys, only short strings; a screen name loses anything after ? or #.
function sb_fb_clean_context($c): array
{
    if (is_string($c)) $c = json_decode($c, true);
    if (!is_array($c)) return [];
    $keys = ['cls' => 12, 'subject' => 40, 'subjectName' => 60, 'book' => 80, 'edition' => 60, 'chapter' => 20, 'chapterTitle' => 100, 'page' => 20, 'screen' => 60,
             'tab' => 40, 'question' => 40, 'version' => 40, 'app' => 20, 'platform' => 8, 'lang' => 8];
    $out = [];
    foreach ($keys as $k => $max) {
        if (!isset($c[$k])) continue;
        $v = sb_fb_line($c[$k], $max + 20);
        if ($k === 'screen') $v = preg_split('/[?]/', $v)[0];
        $v = mb_substr($v, 0, $max);
        if ($v !== '') $out[$k] = $v;
    }
    if (isset($c['online'])) $out['online'] = (bool)$c['online'];
    if (isset($out['platform']) && !in_array($out['platform'], ['web', 'app'], true)) unset($out['platform']);
    return $out;
}

// The words a student wrote: valid UTF-8, line breaks kept, other control characters dropped.
function sb_fb_message($m): string
{
    if (!is_string($m) || !mb_check_encoding($m, 'UTF-8')) return '';
    $m = str_replace(["\r\n", "\r"], "\n", $m);
    $m = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]+/', '', $m);
    $m = preg_replace("/\n{3,}/", "\n\n", (string)$m);
    return trim((string)$m);
}

// Checks (and when GD is there, re-encodes) a picture. Returns ['ok' => true, 'mime', 'data', 'reencoded'] or ['ok' => false, 'error'].
function sb_fb_image_clean(string $raw): array
{
    $len = strlen($raw);
    if ($len < 100) return ['ok' => false, 'error' => 'The picture is empty or damaged.'];
    if ($len > SB_FB_MAX_IMAGE) return ['ok' => false, 'error' => 'The picture is too big: 1.5 MB at most.'];
    $info = @getimagesizefromstring($raw);
    $types = [IMAGETYPE_JPEG, IMAGETYPE_PNG];
    if (defined('IMAGETYPE_WEBP')) $types[] = IMAGETYPE_WEBP;
    if (!$info || !in_array($info[2], $types, true)) return ['ok' => false, 'error' => 'Only JPEG, PNG or WebP pictures can be sent.'];
    $w = (int)$info[0]; $h = (int)$info[1];
    if ($w < 1 || $h < 1 || $w > 6000 || $h > 6000 || $w * $h > 16000000) return ['ok' => false, 'error' => 'The picture is too large in pixels.'];
    // a file that is a picture and also a script or a web page (text after the image data) is refused outright. Only long markers are looked for: a photo is
    // random-looking data, and a 3-byte marker such as the short PHP tag appears by chance in about one photo in ten of 1.5 MB.
    if (preg_match('/<\?php|<script|<html/i', $raw)) return ['ok' => false, 'error' => 'This file is not a plain picture.'];
    if (function_exists('imagecreatefromstring') && function_exists('imagejpeg')) {
        $im = @imagecreatefromstring($raw);
        if (!$im) return ['ok' => false, 'error' => 'The picture could not be read.'];
        $scale = min(1.0, 1600 / max($w, $h));
        $nw = max(1, (int)round($w * $scale)); $nh = max(1, (int)round($h * $scale));
        $out = imagecreatetruecolor($nw, $nh);
        imagefill($out, 0, 0, imagecolorallocate($out, 255, 255, 255));            // a transparent PNG gets a white page
        imagecopyresampled($out, $im, 0, 0, 0, 0, $nw, $nh, $w, $h);
        ob_start();
        imagejpeg($out, null, 82);
        $jpg = (string)ob_get_clean();
        imagedestroy($im); imagedestroy($out);
        if ($jpg === '') return ['ok' => false, 'error' => 'The picture could not be processed.'];
        return ['ok' => true, 'mime' => 'image/jpeg', 'data' => $jpg, 'reencoded' => true];
    }
    return ['ok' => true, 'mime' => image_type_to_mime_type($info[2]), 'data' => $raw, 'reencoded' => false];
}

// Stores a report. $in: client_id, kind, message, context (array or JSON text), platform. $image: the raw picture bytes or null.
// Returns ['ok' => true, 'id' => N, 'duplicate' => bool] or ['ok' => false, 'error' => 'text for the student', 'code' => 400].
function sb_fb_create(PDO $pdo, ?int $uid, array $in, ?string $image): array
{
    $cid = isset($in['client_id']) ? strtolower((string)$in['client_id']) : '';
    if (!sb_fb_uuid_ok($cid)) return ['ok' => false, 'error' => 'This report has no valid identifier. Update the app or reload the page and try again.', 'code' => 400];
    $st = $pdo->prepare('SELECT id FROM feedback_reports WHERE client_id = ?');
    $st->execute([$cid]);
    $have = $st->fetchColumn();
    if ($have) return ['ok' => true, 'id' => (int)$have, 'duplicate' => true];

    $kind = isset($in['kind']) ? (string)$in['kind'] : '';
    if (!in_array($kind, SB_FB_KINDS, true)) return ['ok' => false, 'error' => 'Choose what you want to tell us about.', 'code' => 400];
    $msg = sb_fb_message(isset($in['message']) ? $in['message'] : '');
    $n = mb_strlen($msg);
    if ($n < SB_FB_MIN_MESSAGE) return ['ok' => false, 'error' => 'Please write a few words about it.', 'code' => 400];
    if ($n > SB_FB_MAX_MESSAGE) return ['ok' => false, 'error' => 'Please keep it under ' . SB_FB_MAX_MESSAGE . ' characters.', 'code' => 400];
    $ctx = sb_fb_clean_context(isset($in['context']) ? $in['context'] : []);
    $platform = isset($in['platform']) && $in['platform'] === 'app' ? 'app' : (isset($ctx['platform']) && $ctx['platform'] === 'app' ? 'app' : 'web');
    $ctx['platform'] = $platform;
    $img = null;
    if ($image !== null && $image !== '') {
        $img = sb_fb_image_clean($image);
        if (!$img['ok']) return ['ok' => false, 'error' => $img['error'], 'code' => 400];
    }
    try {
        $pdo->beginTransaction();
        $pdo->prepare('INSERT INTO feedback_reports (client_id, user_id, platform, kind, message, context_json, has_image) VALUES (?, ?, ?, ?, ?, ?, ?)')
            ->execute([$cid, $uid ?: null, $platform, $kind, $msg, $ctx ? json_encode($ctx, JSON_UNESCAPED_UNICODE) : null, $img ? 1 : 0]);
        $id = (int)$pdo->lastInsertId();
        if ($img) {
            $pdo->prepare('INSERT INTO feedback_images (report_id, mime, bytes, sha256, data) VALUES (?, ?, ?, ?, ?)')
                ->execute([$id, $img['mime'], strlen($img['data']), hash('sha256', $img['data']), $img['data']]);
        }
        $pdo->commit();
    } catch (PDOException $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        if ($e->getCode() === '23000') {            // the same client_id arrived twice at once: answer with the first
            $st->execute([$cid]);
            $have = $st->fetchColumn();
            if ($have) return ['ok' => true, 'id' => (int)$have, 'duplicate' => true];
        }
        throw $e;
    }
    return ['ok' => true, 'id' => $id, 'duplicate' => false];
}

// What the sender may learn about reports it made: only a word for the state, never text. ids are client_ids.
function sb_fb_status(PDO $pdo, array $clientIds): array
{
    $ids = [];
    foreach ($clientIds as $c) { $c = strtolower((string)$c); if (sb_fb_uuid_ok($c)) $ids[$c] = true; if (count($ids) >= 30) break; }
    if (!$ids) return [];
    $keys = array_keys($ids);
    $st = $pdo->prepare('SELECT client_id, status FROM feedback_reports WHERE client_id IN (' . implode(',', array_fill(0, count($keys), '?')) . ')');
    $st->execute($keys);
    $out = [];
    foreach ($st->fetchAll() as $r) $out[$r['client_id']] = $r['status'] === 'new' ? 'received' : $r['status'];
    return $out;
}

// ---- administration
function sb_fb_admin_counts(PDO $pdo): array
{
    $r = $pdo->query("SELECT COUNT(*) AS total, SUM(status = 'new') AS fresh, SUM(has_image = 1) AS pics FROM feedback_reports")->fetch();
    return ['total' => (int)$r['total'], 'new' => (int)$r['fresh'], 'pictures' => (int)$r['pics']];
}

function sb_fb_admin_list(PDO $pdo, string $status, string $kind, int $page = 1, int $per = 50): array
{
    $where = []; $args = [];
    if (in_array($status, SB_FB_STATUSES, true)) { $where[] = 'r.status = ?'; $args[] = $status; }
    if (in_array($kind, SB_FB_KINDS, true)) { $where[] = 'r.kind = ?'; $args[] = $kind; }
    $w = $where ? ' WHERE ' . implode(' AND ', $where) : '';
    $st = $pdo->prepare('SELECT COUNT(*) FROM feedback_reports r' . $w);
    $st->execute($args);
    $total = (int)$st->fetchColumn();
    $pages = max(1, (int)ceil($total / $per));
    $page = max(1, min($pages, $page));
    $st = $pdo->prepare('SELECT r.id, r.kind, r.platform, r.status, r.has_image, r.created_at, r.user_id, LEFT(r.message, 160) AS snippet, r.context_json
                         FROM feedback_reports r' . $w . ' ORDER BY r.id DESC LIMIT ' . (int)$per . ' OFFSET ' . (int)(($page - 1) * $per));
    $st->execute($args);
    return ['total' => $total, 'page' => $page, 'pages' => $pages, 'rows' => $st->fetchAll()];
}

function sb_fb_admin_get(PDO $pdo, int $id): ?array
{
    $st = $pdo->prepare('SELECT r.*, u.name AS user_name, i.mime AS image_mime, i.bytes AS image_bytes
                         FROM feedback_reports r LEFT JOIN users u ON u.id = r.user_id LEFT JOIN feedback_images i ON i.report_id = r.id WHERE r.id = ?');
    $st->execute([$id]);
    $r = $st->fetch();
    return $r ? $r : null;
}

function sb_fb_image(PDO $pdo, int $id): ?array
{
    $st = $pdo->prepare('SELECT mime, data FROM feedback_images WHERE report_id = ?');
    $st->execute([$id]);
    $r = $st->fetch();
    return $r ? $r : null;
}

// An administrator sets the state (and a note). Opening a new report for the first time is not an action; changing its state is, and is logged.
function sb_fb_admin_set(PDO $pdo, array $me, int $id, string $to, string $note): array
{
    if (!in_array($to, SB_FB_STATUSES, true)) return ['ok' => false, 'error' => 'Unknown state'];
    $r = sb_fb_admin_get($pdo, $id);
    if (!$r) return ['ok' => false, 'error' => 'No such report'];
    $note = sb_fb_line($note, 500);
    if ($r['status'] === $to && (string)$r['admin_note'] === $note) return ['ok' => true, 'unchanged' => true];
    $pdo->prepare('UPDATE feedback_reports SET status = ?, admin_note = ?, handled_by = ? WHERE id = ?')->execute([$to, $note === '' ? null : $note, (int)$me['id'], $id]);
    sb_audit($pdo, (int)$me['id'], 'admin_feedback_set', 'report:' . $id . ' ' . $r['status'] . '>' . $to);
    return ['ok' => true];
}

// Housekeeping (php api/migrate.php prune): pictures go 90 days after a report was closed, closed reports after a year.
function sb_fb_prune(PDO $pdo): array
{
    $pics = $pdo->exec("DELETE i FROM feedback_images i JOIN feedback_reports r ON r.id = i.report_id
                        WHERE r.status IN ('fixed','wontfix','duplicate') AND r.updated_at < NOW() - INTERVAL 90 DAY");
    $pdo->exec("UPDATE feedback_reports r LEFT JOIN feedback_images i ON i.report_id = r.id SET r.has_image = 0 WHERE r.has_image = 1 AND i.report_id IS NULL");
    $rows = $pdo->exec("DELETE FROM feedback_reports WHERE status IN ('fixed','wontfix','duplicate') AND updated_at < NOW() - INTERVAL 365 DAY");
    return ['images' => (int)$pics, 'reports' => (int)$rows];
}

// The student's own reports for the data export (no pictures: they are not returned to anyone but an administrator).
function sb_fb_export(PDO $pdo, int $uid): array
{
    $st = $pdo->prepare('SELECT id, kind, platform, message, context_json, has_image, status, created_at FROM feedback_reports WHERE user_id = ? ORDER BY id');
    $st->execute([$uid]);
    $out = [];
    foreach ($st->fetchAll() as $r) {
        $out[] = ['id' => (int)$r['id'], 'kind' => $r['kind'], 'platform' => $r['platform'], 'message' => $r['message'], 'context' => $r['context_json'] ? json_decode($r['context_json'], true) : null,
                  'had_picture' => (bool)$r['has_image'], 'status' => $r['status'], 'sent_at' => $r['created_at']];
    }
    return $out;
}
