<?php
// News feed (migration 008): the rules behind api/feed.php. Compatible with PHP 7.4. Nothing here is reachable over HTTP by itself.
//
// What a student can post: a plain post or a question (text), or one of three cards that the clients build from the student's own records:
// a My Stats snapshot, the day's study progress, a study plan. A card is stored as a small JSON object that this file REBUILDS from a whitelist
// of fields (numbers clamped, texts cut), so nothing the client sends is kept as it came. A share is a post of kind 'share' that points at the
// original post (a share of a share points at the original).
//
// Safety rules (the readers are school students):
//  * Only the display name is ever sent: first name and the first letter of the last word ("Ahmad K."); a school account shows its own name.
//    No number, no father name, no account id and no e-mail reaches another student. The avatar is the initial on a colour made from the id.
//  * Text is limited (post 1500 characters, comment 500), cleaned of control and direction-override characters, and refused when it holds an
//    e-mail address, a phone number or a link (sb_feed_screen_text). Clients escape the text when they draw it; the administrator page too.
//  * Every write is rate-limited per student (api/feed.php). The same text twice within two minutes is refused.
//  * A post or comment that SB_FEED_HIDE_AT different students report leaves the feed at once (status 'hidden') until an administrator
//    restores or removes it (api/admin.php?v=feed). The author can delete their own post or comment at any time (status 'removed').
//  * Posts of a blocked or deleted account are not shown.

const SB_FEED_POST_MAX    = 1500;
const SB_FEED_COMMENT_MAX = 500;
const SB_FEED_SHARE_MAX   = 500;
const SB_FEED_PAGE        = 20;
const SB_FEED_HIDE_AT     = 3;                     // different students who report a post or comment before it hides itself
const SB_FEED_KINDS       = ['text', 'question', 'stats', 'progress', 'plan', 'share'];
const SB_FEED_REASONS     = ['spam', 'unkind', 'personal', 'wrong', 'other'];

// ---------------------------------------------------------------- people

// "Ahmad Khan" -> "Ahmad K.", "Ahmad" -> "Ahmad", a school -> its own name.
function sb_feed_display_name(string $name, string $type): string
{
    $name = trim(preg_replace('/\s+/u', ' ', $name));
    if ($name === '') return 'Student';
    if ($type === 'school') return mb_substr($name, 0, 40);
    $parts = explode(' ', $name);
    $first = mb_substr($parts[0], 0, 24);
    if (count($parts) === 1) return $first;
    return $first . ' ' . mb_strtoupper(mb_substr($parts[count($parts) - 1], 0, 1)) . '.';
}

// What another student may know about the author.
function sb_feed_author(int $userId, string $name, string $type): array
{
    $display = sb_feed_display_name($name, $type);
    return [
        'name'    => $display,
        'type'    => in_array($type, ['school', 'teacher', 'student'], true) ? $type : 'student',
        'initial' => mb_strtoupper(mb_substr($display, 0, 1)),
        'hue'     => crc32('sbfeed' . $userId) % 360,
    ];
}

// ---------------------------------------------------------------- text

// Cleans typed text: valid UTF-8, \n for line ends, no control characters, no direction overrides (they can make a link or a name read backwards),
// at most one empty line in a row, cut to $max characters ($max 0 = not cut: the caller refuses a text that is too long). Returns null when the text is not valid UTF-8.
function sb_feed_clean_text($v, int $max, bool $multiline = true): ?string
{
    $s = is_string($v) ? $v : (is_scalar($v) ? (string)$v : '');
    if (!mb_check_encoding($s, 'UTF-8')) return null;
    $s = str_replace(["\r\n", "\r"], "\n", $s);
    $s = preg_replace('/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\x{202a}-\x{202e}\x{2066}-\x{2069}\x{feff}]/u', '', $s);
    if ($s === null) return null;
    if (!$multiline) $s = preg_replace('/\s+/u', ' ', $s);
    else $s = preg_replace(['/[ \t]+\n/u', '/\n{3,}/u'], ["\n", "\n\n"], $s);
    $s = trim($s);
    return $max > 0 ? mb_substr($s, 0, $max) : $s;
}

// A reason to refuse the text, or null. Students are not to leave contact details or links where strangers read them.
function sb_feed_screen_text(string $s): ?string
{
    if (preg_match('/[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}/i', $s)) return 'Please do not put an e-mail address in a post.';
    if (preg_match('~(https?://|www\.)~i', $s) || preg_match('/\b[a-z0-9\-]{2,}\.(com|net|org|pk|info|xyz|me|io|ly|gl|app|tv|cc|biz)\b/i', $s)) {
        return 'Please do not put links in a post.';
    }
    if (preg_match_all('/\+?\d[\d \t\-.()]{8,}\d/', $s, $m)) {
        foreach ($m[0] as $run) {
            if (strlen(preg_replace('/\D/', '', $run)) < 10) continue;
            $short = false;
            foreach (preg_split('/\D+/', $run, -1, PREG_SPLIT_NO_EMPTY) as $g) if (strlen($g) < 2) $short = true;     // "1 2 3 4 5 6 7 8 9 10" is a list, not a number
            if (!$short) return 'Please do not put a phone number in a post.';
        }
    }
    return null;
}

// ---------------------------------------------------------------- attachments (cards)

function sb_feed_int($v, int $min, int $max): int
{
    return is_numeric($v) ? (int)max($min, min($max, round((float)$v))) : $min;
}

function sb_feed_short($v, int $max): string
{
    $s = sb_feed_clean_text($v, $max, false);
    return $s === null ? '' : $s;
}

// The card for $kind, rebuilt from a whitelist; [card or null, error or null]. A kind with no card gives [null, null].
function sb_feed_attach_clean(string $kind, $a): array
{
    if ($kind === 'text' || $kind === 'share') return [null, $a === null || $a === [] ? null : 'This kind of post has no card'];
    $a = is_array($a) ? $a : [];
    if ($kind === 'question') {
        $c = ['v' => 1, 'subject' => sb_feed_short(isset($a['subject']) ? $a['subject'] : '', 60), 'cls' => sb_feed_short(isset($a['cls']) ? $a['cls'] : '', 40), 'chapter' => sb_feed_short(isset($a['chapter']) ? $a['chapter'] : '', 80)];
        return [($c['subject'] === '' && $c['cls'] === '' && $c['chapter'] === '') ? null : $c, null];
    }
    if ($kind === 'stats') {
        $tests = [];
        foreach (array_slice(isset($a['tests']) && is_array($a['tests']) ? $a['tests'] : [], 0, 6) as $t) {
            if (!is_array($t)) continue;
            $title = sb_feed_short(isset($t['title']) ? $t['title'] : '', 30);
            if ($title === '') continue;
            $tests[] = ['title' => $title, 'mcqs' => sb_feed_int(isset($t['mcqs']) ? $t['mcqs'] : 0, 0, 10000000), 'acc' => sb_feed_int(isset($t['acc']) ? $t['acc'] : 0, 0, 100)];
        }
        $c = [
            'v' => 1,
            'questions' => sb_feed_int(isset($a['questions']) ? $a['questions'] : 0, 0, 10000000),
            'accuracy'  => sb_feed_int(isset($a['accuracy']) ? $a['accuracy'] : 0, 0, 100),
            'minutes'   => sb_feed_int(isset($a['minutes']) ? $a['minutes'] : 0, 0, 1000000),
            'streak'    => sb_feed_int(isset($a['streak']) ? $a['streak'] : 0, 0, 3650),
            'sessions'  => sb_feed_int(isset($a['sessions']) ? $a['sessions'] : 0, 0, 10000000),
            'words'     => sb_feed_int(isset($a['words']) ? $a['words'] : 0, 0, 10000000),
            'plans'     => sb_feed_int(isset($a['plans']) ? $a['plans'] : 0, 0, 1000),
            'tests'     => $tests,
        ];
        if ($c['questions'] === 0 && $c['minutes'] === 0 && $c['words'] === 0 && !$tests && $c['plans'] === 0) return [null, 'There is nothing to show yet: practise first, then share your stats'];
        return [$c, null];
    }
    if ($kind === 'progress') {
        $date = isset($a['date']) && is_string($a['date']) && preg_match('/^\d{4}-\d{2}-\d{2}$/', $a['date']) && checkdate((int)substr($a['date'], 5, 2), (int)substr($a['date'], 8, 2), (int)substr($a['date'], 0, 4)) ? $a['date'] : gmdate('Y-m-d');
        $c = [
            'v' => 1,
            'date'      => $date,
            'questions' => sb_feed_int(isset($a['questions']) ? $a['questions'] : 0, 0, 100000),
            'correct'   => sb_feed_int(isset($a['correct']) ? $a['correct'] : 0, 0, 100000),
            'minutes'   => sb_feed_int(isset($a['minutes']) ? $a['minutes'] : 0, 0, 1440),
            'goal'      => sb_feed_int(isset($a['goal']) ? $a['goal'] : 0, 0, 100000),
            'coins'     => sb_feed_int(isset($a['coins']) ? $a['coins'] : 0, 0, 10000000),
            'streak'    => sb_feed_int(isset($a['streak']) ? $a['streak'] : 0, 0, 3650),
            'tasksDone' => sb_feed_int(isset($a['tasksDone']) ? $a['tasksDone'] : 0, 0, 10000),
            'tasksTotal' => sb_feed_int(isset($a['tasksTotal']) ? $a['tasksTotal'] : 0, 0, 10000),
        ];
        if ($c['correct'] > $c['questions']) $c['correct'] = $c['questions'];
        if ($c['tasksDone'] > $c['tasksTotal']) $c['tasksDone'] = $c['tasksTotal'];
        if ($c['questions'] === 0 && $c['minutes'] === 0 && $c['tasksTotal'] === 0) return [null, 'There is no study today yet: practise first, then share your progress'];
        return [$c, null];
    }
    if ($kind === 'plan') {
        $subjects = [];
        foreach (array_slice(isset($a['subjects']) && is_array($a['subjects']) ? $a['subjects'] : [], 0, 8) as $s) {
            $t = sb_feed_short($s, 40);
            if ($t !== '') $subjects[] = $t;
        }
        $name = sb_feed_short(isset($a['name']) ? $a['name'] : '', 60);
        $tasks = sb_feed_int(isset($a['tasks']) ? $a['tasks'] : 0, 0, 100000);
        $done = min($tasks, sb_feed_int(isset($a['done']) ? $a['done'] : 0, 0, 100000));
        if ($name === '') return [null, 'The plan needs a name'];
        return [[
            'v' => 1, 'name' => $name, 'label' => sb_feed_short(isset($a['label']) ? $a['label'] : '', 80), 'subjects' => $subjects,
            'days' => sb_feed_int(isset($a['days']) ? $a['days'] : 0, 0, 3650), 'tasks' => $tasks, 'done' => $done,
            'pct' => $tasks > 0 ? (int)round($done * 100 / $tasks) : 0,
        ], null];
    }
    return [null, 'Unknown kind of post'];
}

// ---------------------------------------------------------------- reading

function sb_feed_post_json(array $r, int $viewer, ?array $shared): array
{
    $attach = $r['attach_json'] !== null && $r['attach_json'] !== '' ? json_decode($r['attach_json'], true) : null;
    $out = [
        'id'       => (int)$r['id'],
        'kind'     => $r['kind'],
        'author'   => sb_feed_author((int)$r['user_id'], (string)$r['author_name'], (string)$r['author_type']),
        'mine'     => (int)$r['user_id'] === $viewer,
        'body'     => $r['body'],
        'card'     => is_array($attach) ? $attach : null,
        'likes'    => (int)$r['like_count'],
        'comments' => (int)$r['comment_count'],
        'shares'   => (int)$r['share_count'],
        'liked'    => !empty($r['liked']),
        'at'       => (int)$r['at_ms'],
    ];
    if ($r['kind'] === 'share') $out['shared'] = $shared;      // null: the original is gone
    return $out;
}

// Columns every post query needs.
function sb_feed_post_select(): string
{
    return 'p.id, p.user_id, p.kind, p.body, p.attach_json, p.shared_id, p.like_count, p.comment_count, p.share_count, p.status, UNIX_TIMESTAMP(p.created_at) * 1000 AS at_ms, u.name AS author_name, u.user_type AS author_type';
}

// Posts for the feed, newest first. $before: only posts with a smaller id (0 = from the newest). $mineOnly: only this student's own posts.
// $kind: only posts of that kind ('question' for the Questions filter), '' = all.
// Returns ['posts' => [...], 'next' => id to ask for the next page, 0 when there are no more].
function sb_feed_list(PDO $pdo, int $viewer, int $before = 0, int $limit = SB_FEED_PAGE, bool $mineOnly = false, string $kind = ''): array
{
    $limit = max(1, min(50, $limit));
    $where = "p.status = 'visible'";
    $args = [$viewer];
    if ($before > 0) { $where .= ' AND p.id < ?'; $args[] = $before; }
    if ($mineOnly) { $where .= ' AND p.user_id = ?'; $args[] = $viewer; }
    if ($kind !== '' && in_array($kind, SB_FEED_KINDS, true)) { $where .= ' AND p.kind = ?'; $args[] = $kind; }
    $st = $pdo->prepare('SELECT ' . sb_feed_post_select() . ', (l.user_id IS NOT NULL) AS liked
                         FROM feed_posts p JOIN users u ON u.id = p.user_id AND u.status = \'active\'
                         LEFT JOIN feed_post_likes l ON l.post_id = p.id AND l.user_id = ?
                         WHERE ' . $where . ' ORDER BY p.id DESC LIMIT ' . ($limit + 1));
    $st->execute($args);
    $rows = $st->fetchAll();
    $more = count($rows) > $limit;
    $rows = array_slice($rows, 0, $limit);
    $shared = sb_feed_shared_map($pdo, $rows, $viewer);
    $posts = [];
    foreach ($rows as $r) $posts[] = sb_feed_post_json($r, $viewer, $r['shared_id'] !== null && isset($shared[(int)$r['shared_id']]) ? $shared[(int)$r['shared_id']] : null);
    return ['posts' => $posts, 'next' => $more && $rows ? (int)$rows[count($rows) - 1]['id'] : 0];
}

// The originals of the shares in $rows, as a small post each: id => json.
function sb_feed_shared_map(PDO $pdo, array $rows, int $viewer): array
{
    $ids = [];
    foreach ($rows as $r) if ($r['kind'] === 'share' && $r['shared_id'] !== null) $ids[(int)$r['shared_id']] = true;
    if (!$ids) return [];
    $in = implode(',', array_map('intval', array_keys($ids)));
    $out = [];
    foreach ($pdo->query('SELECT ' . sb_feed_post_select() . " FROM feed_posts p JOIN users u ON u.id = p.user_id AND u.status = 'active' WHERE p.status = 'visible' AND p.id IN ($in)") as $r) {
        $r['liked'] = false;
        $j = sb_feed_post_json($r, $viewer, null);
        $out[(int)$r['id']] = ['id' => $j['id'], 'kind' => $j['kind'], 'author' => $j['author'], 'body' => $j['body'], 'card' => $j['card'], 'at' => $j['at']];
    }
    return $out;
}

// One visible post for this viewer, or null.
function sb_feed_get(PDO $pdo, int $viewer, int $id): ?array
{
    $st = $pdo->prepare('SELECT ' . sb_feed_post_select() . ', (l.user_id IS NOT NULL) AS liked
                         FROM feed_posts p JOIN users u ON u.id = p.user_id AND u.status = \'active\'
                         LEFT JOIN feed_post_likes l ON l.post_id = p.id AND l.user_id = ?
                         WHERE p.id = ? AND p.status = \'visible\'');
    $st->execute([$viewer, $id]);
    $r = $st->fetch();
    if (!$r) return null;
    $shared = sb_feed_shared_map($pdo, [$r], $viewer);
    return sb_feed_post_json($r, $viewer, $r['shared_id'] !== null && isset($shared[(int)$r['shared_id']]) ? $shared[(int)$r['shared_id']] : null);
}

// ---------------------------------------------------------------- posting

// The same text by the same student within two minutes is a double tap or a flood.
function sb_feed_is_repeat(PDO $pdo, string $table, int $uid, string $body): bool
{
    if ($body === '') return false;
    $st = $pdo->prepare("SELECT COUNT(*) FROM $table WHERE user_id = ? AND body = ? AND created_at > NOW() - INTERVAL 2 MINUTE AND status <> 'removed'");
    $st->execute([$uid, $body]);
    return (int)$st->fetchColumn() > 0;
}

// Creates a post. $attach is the card as the client sent it (rebuilt here). For 'share', $sharedId is the post being shared.
// Returns ['ok' => true, 'id' => n] or ['ok' => false, 'code' => http status, 'error' => text].
function sb_feed_create(PDO $pdo, int $uid, string $kind, $body, $attach, int $sharedId = 0): array
{
    if (!in_array($kind, SB_FEED_KINDS, true)) return ['ok' => false, 'code' => 422, 'error' => 'Unknown kind of post'];
    $max = $kind === 'share' ? SB_FEED_SHARE_MAX : SB_FEED_POST_MAX;
    $text = sb_feed_clean_text($body, 0);
    if ($text === null) return ['ok' => false, 'code' => 422, 'error' => 'That text could not be read'];
    if (mb_strlen($text) > $max) return ['ok' => false, 'code' => 422, 'error' => 'Please keep it under ' . $max . ' characters'];
    if (($kind === 'text' || $kind === 'question') && mb_strlen($text) < 2) return ['ok' => false, 'code' => 422, 'error' => $kind === 'question' ? 'Write your question' : 'Write something to post'];
    if ($text !== '' && ($why = sb_feed_screen_text($text)) !== null) return ['ok' => false, 'code' => 422, 'error' => $why];
    list($card, $err) = sb_feed_attach_clean($kind, $attach);
    if ($err !== null) return ['ok' => false, 'code' => 422, 'error' => $err];
    if (($kind === 'stats' || $kind === 'progress' || $kind === 'plan') && $card === null) return ['ok' => false, 'code' => 422, 'error' => 'There is nothing to share'];
    if (sb_feed_is_repeat($pdo, 'feed_posts', $uid, $text)) return ['ok' => false, 'code' => 409, 'error' => 'You already posted this'];

    $root = null;
    if ($kind === 'share') {
        $st = $pdo->prepare("SELECT id, kind, shared_id FROM feed_posts WHERE id = ? AND status = 'visible'");
        $st->execute([$sharedId]);
        $orig = $st->fetch();
        if (!$orig) return ['ok' => false, 'code' => 404, 'error' => 'That post is no longer there'];
        $root = (int)($orig['kind'] === 'share' && $orig['shared_id'] !== null ? $orig['shared_id'] : $orig['id']);     // a share of a share points at the original
        $st = $pdo->prepare("SELECT COUNT(*) FROM feed_posts WHERE id = ? AND status = 'visible'");
        $st->execute([$root]);
        if ((int)$st->fetchColumn() === 0) return ['ok' => false, 'code' => 404, 'error' => 'That post is no longer there'];
    }
    $pdo->beginTransaction();
    try {
        $pdo->prepare('INSERT INTO feed_posts (user_id, kind, body, attach_json, shared_id) VALUES (?, ?, ?, ?, ?)')
            ->execute([$uid, $kind, $text, $card === null ? null : json_encode($card, JSON_UNESCAPED_UNICODE), $root]);
        $id = (int)$pdo->lastInsertId();
        if ($root !== null) $pdo->prepare('UPDATE feed_posts SET share_count = share_count + 1 WHERE id = ?')->execute([$root]);
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    return ['ok' => true, 'id' => $id];
}

// The author removes their own post (it keeps its row, status 'removed', so the shares of it read "no longer there").
function sb_feed_delete_post(PDO $pdo, int $uid, int $id): bool
{
    $st = $pdo->prepare("SELECT id, kind, shared_id FROM feed_posts WHERE id = ? AND user_id = ? AND status <> 'removed'");
    $st->execute([$id, $uid]);
    $p = $st->fetch();
    if (!$p) return false;
    $pdo->beginTransaction();
    try {
        $pdo->prepare("UPDATE feed_posts SET status = 'removed' WHERE id = ?")->execute([$id]);
        if ($p['kind'] === 'share' && $p['shared_id'] !== null) {
            $pdo->prepare('UPDATE feed_posts SET share_count = GREATEST(share_count, 1) - 1 WHERE id = ?')->execute([(int)$p['shared_id']]);
        }
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    return true;
}

// ---------------------------------------------------------------- likes

// Sets the like to $on (idempotent: two taps never count twice). $type 'p' post or 'c' comment. Returns the new count, or null when the target is not visible.
function sb_feed_like(PDO $pdo, int $uid, string $type, int $id, bool $on): ?int
{
    $table = $type === 'c' ? 'feed_comments' : 'feed_posts';
    $likes = $type === 'c' ? 'feed_comment_likes' : 'feed_post_likes';
    $col   = $type === 'c' ? 'comment_id' : 'post_id';
    $st = $pdo->prepare("SELECT id FROM $table WHERE id = ? AND status = 'visible'");
    $st->execute([$id]);
    if (!$st->fetch()) return null;
    $pdo->beginTransaction();
    try {
        if ($on) {
            $ins = $pdo->prepare("INSERT IGNORE INTO $likes ($col, user_id) VALUES (?, ?)");
            $ins->execute([$id, $uid]);
            if ($ins->rowCount() > 0) $pdo->prepare("UPDATE $table SET like_count = like_count + 1 WHERE id = ?")->execute([$id]);
        } else {
            $del = $pdo->prepare("DELETE FROM $likes WHERE $col = ? AND user_id = ?");
            $del->execute([$id, $uid]);
            if ($del->rowCount() > 0) $pdo->prepare("UPDATE $table SET like_count = GREATEST(like_count, 1) - 1 WHERE id = ?")->execute([$id]);
        }
        $n = $pdo->prepare("SELECT like_count FROM $table WHERE id = ?");
        $n->execute([$id]);
        $count = (int)$n->fetchColumn();
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    return $count;
}

// ---------------------------------------------------------------- comments

function sb_feed_comment_json(array $r, int $viewer): array
{
    return [
        'id'      => (int)$r['id'],
        'post'    => (int)$r['post_id'],
        'parent'  => $r['parent_id'] === null ? 0 : (int)$r['parent_id'],
        'author'  => sb_feed_author((int)$r['user_id'], (string)$r['author_name'], (string)$r['author_type']),
        'mine'    => (int)$r['user_id'] === $viewer,
        'body'    => $r['body'],
        'likes'   => (int)$r['like_count'],
        'liked'   => !empty($r['liked']),
        'at'      => (int)$r['at_ms'],
        'replies' => [],
    ];
}

// The comments of a post: a page of top-level comments (newest first, $before = smaller ids only) each with its replies (oldest first).
function sb_feed_comments(PDO $pdo, int $viewer, int $postId, int $before = 0, int $limit = SB_FEED_PAGE): ?array
{
    $st = $pdo->prepare("SELECT id FROM feed_posts WHERE id = ? AND status = 'visible'");
    $st->execute([$postId]);
    if (!$st->fetch()) return null;
    $limit = max(1, min(50, $limit));
    $cols = 'c.id, c.post_id, c.user_id, c.parent_id, c.body, c.like_count, UNIX_TIMESTAMP(c.created_at) * 1000 AS at_ms, u.name AS author_name, u.user_type AS author_type, (l.user_id IS NOT NULL) AS liked';
    $join = "JOIN users u ON u.id = c.user_id AND u.status = 'active' LEFT JOIN feed_comment_likes l ON l.comment_id = c.id AND l.user_id = ?";
    $args = [$viewer, $postId];
    $where = "c.post_id = ? AND c.status = 'visible' AND c.parent_id IS NULL";
    if ($before > 0) { $where .= ' AND c.id < ?'; $args[] = $before; }
    $st = $pdo->prepare("SELECT $cols FROM feed_comments c $join WHERE $where ORDER BY c.id DESC LIMIT " . ($limit + 1));
    $st->execute($args);
    $rows = $st->fetchAll();
    $more = count($rows) > $limit;
    $rows = array_slice($rows, 0, $limit);
    $out = [];
    foreach ($rows as $r) $out[(int)$r['id']] = sb_feed_comment_json($r, $viewer);
    if ($out) {
        $in = implode(',', array_map('intval', array_keys($out)));
        $st = $pdo->prepare("SELECT $cols FROM feed_comments c $join WHERE c.status = 'visible' AND c.parent_id IN ($in) ORDER BY c.id ASC LIMIT 500");
        $st->execute([$viewer]);
        foreach ($st as $r) if (isset($out[(int)$r['parent_id']])) $out[(int)$r['parent_id']]['replies'][] = sb_feed_comment_json($r, $viewer);
    }
    return ['comments' => array_values($out), 'next' => $more && $rows ? (int)$rows[count($rows) - 1]['id'] : 0];
}

// Adds a comment (or a reply when $parent is a comment of the same post). Returns ['ok' => true, 'comment' => json, 'count' => the post's comment count] or an error.
function sb_feed_add_comment(PDO $pdo, int $uid, int $postId, $body, int $parent = 0): array
{
    $text = sb_feed_clean_text($body, 0);
    if ($text === null) return ['ok' => false, 'code' => 422, 'error' => 'That text could not be read'];
    if (mb_strlen($text) > SB_FEED_COMMENT_MAX) return ['ok' => false, 'code' => 422, 'error' => 'Please keep a comment under ' . SB_FEED_COMMENT_MAX . ' characters'];
    if (mb_strlen($text) < 1) return ['ok' => false, 'code' => 422, 'error' => 'Write a comment'];
    if (($why = sb_feed_screen_text($text)) !== null) return ['ok' => false, 'code' => 422, 'error' => $why];
    $st = $pdo->prepare("SELECT id FROM feed_posts WHERE id = ? AND status = 'visible'");
    $st->execute([$postId]);
    if (!$st->fetch()) return ['ok' => false, 'code' => 404, 'error' => 'That post is no longer there'];
    $parentId = null;
    if ($parent > 0) {
        $st = $pdo->prepare("SELECT id, parent_id FROM feed_comments WHERE id = ? AND post_id = ? AND status = 'visible'");
        $st->execute([$parent, $postId]);
        $pc = $st->fetch();
        if (!$pc) return ['ok' => false, 'code' => 404, 'error' => 'That comment is no longer there'];
        $parentId = (int)($pc['parent_id'] !== null ? $pc['parent_id'] : $pc['id']);          // a reply to a reply sits under the same comment
    }
    if (sb_feed_is_repeat($pdo, 'feed_comments', $uid, $text)) return ['ok' => false, 'code' => 409, 'error' => 'You already wrote this'];
    $pdo->beginTransaction();
    try {
        $pdo->prepare('INSERT INTO feed_comments (post_id, user_id, parent_id, body) VALUES (?, ?, ?, ?)')->execute([$postId, $uid, $parentId, $text]);
        $id = (int)$pdo->lastInsertId();
        $pdo->prepare('UPDATE feed_posts SET comment_count = comment_count + 1 WHERE id = ?')->execute([$postId]);
        $count = $pdo->prepare('SELECT comment_count FROM feed_posts WHERE id = ?');
        $count->execute([$postId]);
        $n = (int)$count->fetchColumn();
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    $st = $pdo->prepare('SELECT c.id, c.post_id, c.user_id, c.parent_id, c.body, c.like_count, UNIX_TIMESTAMP(c.created_at) * 1000 AS at_ms, u.name AS author_name, u.user_type AS author_type, 0 AS liked
                         FROM feed_comments c JOIN users u ON u.id = c.user_id WHERE c.id = ?');
    $st->execute([$id]);
    return ['ok' => true, 'comment' => sb_feed_comment_json($st->fetch(), $uid), 'count' => $n];
}

// The author removes their comment; its replies go with it. Returns the post's new comment count, or null when it is not theirs.
function sb_feed_delete_comment(PDO $pdo, int $uid, int $id): ?int
{
    $st = $pdo->prepare("SELECT id, post_id, parent_id FROM feed_comments WHERE id = ? AND user_id = ? AND status <> 'removed'");
    $st->execute([$id, $uid]);
    $c = $st->fetch();
    if (!$c) return null;
    $pdo->beginTransaction();
    try {
        $gone = $pdo->prepare("UPDATE feed_comments SET status = 'removed' WHERE (id = ? OR parent_id = ?) AND status <> 'removed'");
        $gone->execute([$id, $id]);
        $removed = (int)$gone->rowCount();          // inside the SQL as numbers: bound values arrive as strings and GREATEST would compare them as text
        $pdo->prepare('UPDATE feed_posts SET comment_count = GREATEST(comment_count, ' . $removed . ') - ' . $removed . ' WHERE id = ?')->execute([(int)$c['post_id']]);
        $n = $pdo->prepare('SELECT comment_count FROM feed_posts WHERE id = ?');
        $n->execute([(int)$c['post_id']]);
        $count = (int)$n->fetchColumn();
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    return $count;
}

// ---------------------------------------------------------------- reports

// One report per student per post or comment. SB_FEED_HIDE_AT different students hide it. Returns ['ok' => true, 'hidden' => bool] or an error.
function sb_feed_report(PDO $pdo, int $uid, string $type, int $id, string $reason, $note): array
{
    $table = $type === 'c' ? 'feed_comments' : 'feed_posts';
    if (!in_array($reason, SB_FEED_REASONS, true)) return ['ok' => false, 'code' => 422, 'error' => 'Choose a reason'];
    $st = $pdo->prepare("SELECT id, user_id FROM $table WHERE id = ? AND status = 'visible'");
    $st->execute([$id]);
    $t = $st->fetch();
    if (!$t) return ['ok' => false, 'code' => 404, 'error' => 'That is no longer there'];
    if ((int)$t['user_id'] === $uid) return ['ok' => false, 'code' => 422, 'error' => 'This is your own post: you can delete it'];
    $note = sb_feed_clean_text($note, 200, false);
    $hidden = false;
    $pdo->beginTransaction();
    try {
        $ins = $pdo->prepare('INSERT IGNORE INTO feed_reports (target_type, target_id, user_id, reason, note) VALUES (?, ?, ?, ?, ?)');
        $ins->execute([$type === 'c' ? 'c' : 'p', $id, $uid, $reason, $note === null ? '' : $note]);
        if ($ins->rowCount() > 0) {
            $pdo->prepare("UPDATE $table SET report_count = report_count + 1 WHERE id = ?")->execute([$id]);
            $n = $pdo->prepare("SELECT report_count FROM $table WHERE id = ?");
            $n->execute([$id]);
            if ((int)$n->fetchColumn() >= SB_FEED_HIDE_AT) {
                $pdo->prepare("UPDATE $table SET status = 'hidden' WHERE id = ? AND status = 'visible'")->execute([$id]);
                $hidden = true;
            }
        }
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
    return ['ok' => true, 'hidden' => $hidden];
}

// ---------------------------------------------------------------- administration (api/admin.php?v=feed)

// Reported or hidden posts and comments, newest report first. Names are the display names, text is escaped by the page.
function sb_feed_admin_rows(PDO $pdo, int $limit = 100): array
{
    $rows = [];
    foreach ([['p', 'feed_posts', 'body'], ['c', 'feed_comments', 'body']] as $t) {
        $st = $pdo->prepare("SELECT x.id, x.user_id, x.$t[2] AS body, x.status, x.report_count, x.created_at, u.name, u.user_type,
                                    (SELECT GROUP_CONCAT(DISTINCT r.reason) FROM feed_reports r WHERE r.target_type = '$t[0]' AND r.target_id = x.id) AS reasons
                             FROM $t[1] x JOIN users u ON u.id = x.user_id
                             WHERE x.report_count > 0 OR x.status = 'hidden' ORDER BY x.id DESC LIMIT " . (int)$limit);
        $st->execute();
        foreach ($st as $r) $rows[] = ['type' => $t[0], 'id' => (int)$r['id'], 'user_id' => (int)$r['user_id'], 'author' => $r['name'], 'body' => $r['body'], 'status' => $r['status'], 'reports' => (int)$r['report_count'], 'reasons' => (string)$r['reasons'], 'created_at' => $r['created_at']];
    }
    usort($rows, function ($a, $b) { return strcmp($b['created_at'], $a['created_at']) ?: $b['id'] - $a['id']; });
    return array_slice($rows, 0, $limit);
}

// An administrator restores ('visible') or removes ('removed') a reported post or comment. Writes the audit row.
function sb_feed_admin_set(PDO $pdo, array $admin, string $type, int $id, string $to): array
{
    if ($to !== 'visible' && $to !== 'removed') return ['ok' => false, 'error' => 'Unknown status'];
    $table = $type === 'c' ? 'feed_comments' : 'feed_posts';
    $st = $pdo->prepare("SELECT id, user_id, status FROM $table WHERE id = ?");
    $st->execute([$id]);
    $t = $st->fetch();
    if (!$t) return ['ok' => false, 'error' => 'No such post or comment'];
    if ($t['status'] === $to) return ['ok' => true, 'unchanged' => true];
    // a restored item starts again with no reports, so a single new report does not hide it at once
    $pdo->prepare("UPDATE $table SET status = ?" . ($to === 'visible' ? ', report_count = 0' : '') . ' WHERE id = ?')->execute([$to, $id]);
    if ($to === 'visible') $pdo->prepare("DELETE FROM feed_reports WHERE target_type = ? AND target_id = ?")->execute([$type === 'c' ? 'c' : 'p', $id]);
    require_once __DIR__ . '/security.php';
    sb_audit($pdo, (int)$t['user_id'], $to === 'visible' ? 'feed_restore' : 'feed_remove', 'by:' . (int)$admin['id'] . ' ' . ($type === 'c' ? 'comment ' : 'post ') . $id);
    return ['ok' => true];
}

// What a student's export holds from the feed (their own posts and comments).
function sb_feed_export(PDO $pdo, int $uid): array
{
    $one = function (string $sql) use ($pdo, $uid) { $st = $pdo->prepare($sql); $st->execute([$uid]); return $st->fetchAll(); };
    return [
        'posts'    => $one("SELECT id, kind, body, attach_json, shared_id, like_count, comment_count, share_count, status, created_at FROM feed_posts WHERE user_id = ? AND status <> 'removed' ORDER BY id"),
        'comments' => $one("SELECT id, post_id, parent_id, body, like_count, status, created_at FROM feed_comments WHERE user_id = ? AND status <> 'removed' ORDER BY id"),
    ];
}
