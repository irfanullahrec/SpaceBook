<?php
// User items: what a student keeps on one device and expects on the other. Compatible with PHP 7.4.
//
// One table (user_items) and one small rule set per kind. The events are
//   item.put {kind, key, value, at}      item.del {kind, key, at}
// and the rows come back in the pull (`items`, `itemsDeleted`, see api/lib/pull.php).
//
//   kind   what                               key                                value (only these fields are kept)
//   bm     a bookmarked page                  <subject>|<chapter>|<tab>|<page>   {c, s, ch, p, tb, t}
//   note   a note or a highlight on a page    <uuid>                             {c, s, ch, p, tb, t, x, q, k}   x = text, q = the quoted words, k = note | hl
//   pos    where the student stopped          <subject>                          {c, ch, p, tb, n, t}            n = pages in the tab
//   word   a word marked learnt / known       <lang>:<word>                      {s}                             s = l | k
//   gbest  best run of a game level (0..1)    <level reward key>                 {b}
//   pref   a setting that follows the student class | games                       {id} | {cls, scope, streak}
//   slo    a ticked Board SLO                 <subject>|<chapter>|<n>            {}
//   drill  a finished Section A drill         <subject>|<ts>                     {n, c, ms}
//
// Merge rule: the change with the later `at` wins (the device's time, clamped to the server's own clock, so a fast clock cannot win);
// at the same time the one that arrives later wins. A delete is a tombstone with its `at`, so an older save arriving late is ignored.
// gbest is the exception: it only ever goes up and cannot be deleted. Every kind has a cap per student (`max`) and the table a total cap.
// Nothing is decided by the client except what it is: coins stay with api/lib/rewards.php.

const SB_ITEM_TOTAL_MAX = 30000;
const SB_ITEM_VALUE_MAX = 4096;

function sb_item_now_ms(): int { return (int)round(microtime(true) * 1000); }

// A device time: never in the future of the server (5 s of clock difference tolerated), 0 or missing = now.
function sb_item_at($v): int
{
    $now = sb_item_now_ms();
    $t = is_numeric($v) ? (int)$v : 0;
    return $t <= 0 ? $now : min($t, $now + 5000);
}

function sb_item_text($v, int $max): string
{
    $s = is_string($v) ? $v : (is_scalar($v) ? (string)$v : '');
    $s = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', ' ', $s);
    if ($s === null) return '';
    if (function_exists('mb_substr')) return mb_substr($s, 0, $max, 'UTF-8');
    return substr($s, 0, $max);
}

function sb_item_len(string $s): int
{
    return function_exists('mb_strlen') ? mb_strlen($s, 'UTF-8') : strlen($s);
}

function sb_item_int($v, int $min, int $max): ?int
{
    if (!is_numeric($v) || (float)$v != floor((float)$v)) return null;
    $i = (int)$v;
    return $i < $min || $i > $max ? null : $i;
}

function sb_item_id($v, string $rx): ?string
{
    return is_string($v) && preg_match($rx, $v) ? $v : null;
}

const SB_ITEM_CLASS   = '/^[a-z0-9_-]{1,24}$/';
const SB_ITEM_SUBJECT = '/^[a-z0-9_-]{1,40}$/';
const SB_ITEM_TAB     = '/^[A-Za-z0-9 _\-]{0,30}$/';

// Common locator fields of bm / note / pos.
function sb_item_loc(array $v, bool $withTab = true): ?array
{
    $c = sb_item_id(isset($v['c']) ? $v['c'] : null, SB_ITEM_CLASS);
    $ch = sb_item_int(isset($v['ch']) ? $v['ch'] : null, 0, 9999);
    $p = sb_item_int(isset($v['p']) ? $v['p'] : null, 0, 9999);
    if ($c === null || $ch === null || $p === null) return null;
    $out = ['c' => $c, 'ch' => $ch, 'p' => $p];
    if ($withTab) $out['tb'] = trim(sb_item_text(isset($v['tb']) ? $v['tb'] : '', 30));
    return $out;
}

// The rules. 'key' checks the key, 'check' returns the normalised value or null, 'max' is the cap per student.
function sb_item_kinds(): array
{
    static $kinds = null;
    if ($kinds !== null) return $kinds;
    $kinds = [
        'bm' => ['max' => 1000, 'rule' => 'later', 'key' => '/^[a-z0-9_-]{1,40}\|[0-9]{1,4}\|[A-Za-z0-9 _-]{0,30}\|[0-9]{1,4}$/',
            'check' => function (array $v, string $key): ?array {
                $loc = sb_item_loc($v);
                $s = sb_item_id(isset($v['s']) ? $v['s'] : null, SB_ITEM_SUBJECT);
                if ($loc === null || $s === null) return null;
                if ($key !== $s . '|' . $loc['ch'] . '|' . $loc['tb'] . '|' . $loc['p']) return null;       // the key is the place
                return ['c' => $loc['c'], 's' => $s, 'ch' => $loc['ch'], 'p' => $loc['p'], 'tb' => $loc['tb'], 't' => trim(sb_item_text(isset($v['t']) ? $v['t'] : '', 160))];
            }],
        'note' => ['max' => 3000, 'rule' => 'later', 'key' => '/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/',
            'check' => function (array $v, string $key): ?array {
                $loc = sb_item_loc($v);
                $s = sb_item_id(isset($v['s']) ? $v['s'] : null, SB_ITEM_SUBJECT);
                if ($loc === null || $s === null) return null;
                $x = trim(sb_item_text(isset($v['x']) ? $v['x'] : '', 2000));
                $q = trim(sb_item_text(isset($v['q']) ? $v['q'] : '', 500));
                $k = isset($v['k']) && $v['k'] === 'hl' ? 'hl' : 'note';
                if ($x === '' && $q === '') return null;
                return ['c' => $loc['c'], 's' => $s, 'ch' => $loc['ch'], 'p' => $loc['p'], 'tb' => $loc['tb'], 't' => trim(sb_item_text(isset($v['t']) ? $v['t'] : '', 160)), 'x' => $x, 'q' => $q, 'k' => $k];
            }],
        'pos' => ['max' => 400, 'rule' => 'later', 'key' => '/^[a-z0-9_-]{1,40}$/',
            'check' => function (array $v, string $key): ?array {
                $loc = sb_item_loc($v);
                $n = sb_item_int(isset($v['n']) ? $v['n'] : 0, 0, 9999);
                if ($loc === null || $n === null) return null;
                return ['c' => $loc['c'], 'ch' => $loc['ch'], 'p' => $loc['p'], 'tb' => $loc['tb'], 'n' => $n, 't' => trim(sb_item_text(isset($v['t']) ? $v['t'] : '', 160))];
            }],
        'word' => ['max' => 6000, 'rule' => 'later', 'key' => '/^(en|ur|ps|ar):.{1,80}$/su',
            'check' => function (array $v, string $key): ?array {
                $s = isset($v['s']) ? $v['s'] : '';
                return $s === 'l' || $s === 'k' ? ['s' => $s] : null;
            }],
        'gbest' => ['max' => 4000, 'rule' => 'max', 'key' => null,
            'check' => function (array $v, string $key): ?array {
                if (sb_reward_key_kind($key) === null || !isset($v['b']) || !is_numeric($v['b'])) return null;
                return ['b' => round(max(0.0, min(1.0, (float)$v['b'])), 4)];
            }],
        'pref' => ['max' => 20, 'rule' => 'later', 'key' => '/^(class|games)$/',
            'check' => function (array $v, string $key): ?array {
                if ($key === 'class') {
                    $id = sb_item_id(isset($v['id']) ? $v['id'] : null, SB_ITEM_CLASS);
                    return $id === null ? null : ['id' => $id];
                }
                $out = [];
                if (isset($v['cls'])) { $c = sb_item_int($v['cls'], 1, 12); if ($c === null) return null; $out['cls'] = $c; }
                if (isset($v['scope'])) {
                    if (!is_array($v['scope']) || count($v['scope']) > 80) return null;
                    $out['scope'] = [];
                    foreach ($v['scope'] as $k => $s) {
                        if (!is_string($k) || !is_string($s) || strlen($k) > 40 || strlen($s) > 40) return null;
                        $out['scope'][$k] = $s;
                    }
                }
                if (isset($v['streak'])) {
                    $n = is_array($v['streak']) ? sb_item_int(isset($v['streak']['n']) ? $v['streak']['n'] : 0, 0, 99999) : null;
                    $last = is_array($v['streak']) && isset($v['streak']['last']) ? (string)$v['streak']['last'] : '';
                    if ($n === null || !($last === '' || preg_match('/^\d{4}-\d{2}-\d{2}$/', $last))) return null;
                    $out['streak'] = ['n' => $n, 'last' => $last];
                }
                return $out;
            }],
        'slo' => ['max' => 9000, 'rule' => 'later', 'key' => '/^[a-z0-9_-]{1,40}\|[A-Za-z0-9_.-]{1,12}\|[0-9]{1,3}$/',
            'check' => function (array $v, string $key): ?array { return []; }],
        'drill' => ['max' => 500, 'rule' => 'later', 'key' => '/^[a-z0-9_-]{1,40}\|[0-9]{10,14}$/',
            'check' => function (array $v, string $key): ?array {
                $n = sb_item_int(isset($v['n']) ? $v['n'] : null, 0, 500);
                $c = sb_item_int(isset($v['c']) ? $v['c'] : null, 0, 500);
                $ms = sb_item_int(isset($v['ms']) ? $v['ms'] : 0, 0, 86400000);
                return $n === null || $c === null || $ms === null || $c > $n ? null : ['n' => $n, 'c' => $c, 'ms' => $ms];
            }],
    ];
    return $kinds;
}

function sb_item_json(array $value): string
{
    // an empty value is `{}`, not `[]`, so it reads back as an object
    return $value ? json_encode($value, JSON_UNESCAPED_UNICODE) : '{}';
}

function sb_item_count(PDO $pdo, int $uid, ?string $kind): int
{
    if ($kind === null) {
        $st = $pdo->prepare('SELECT COUNT(*) FROM user_items WHERE user_id = ?');
        $st->execute([$uid]);
    } else {
        $st = $pdo->prepare('SELECT COUNT(*) FROM user_items WHERE user_id = ? AND kind = ? AND deleted = 0');
        $st->execute([$uid, $kind]);
    }
    return (int)$st->fetchColumn();
}

// item.put. Returns null when handled (applied or deliberately ignored), else a rejection code.
function sb_item_put(PDO $pdo, int $uid, array $p): ?string
{
    $kind = isset($p['kind']) && is_string($p['kind']) ? $p['kind'] : '';
    $kinds = sb_item_kinds();
    if (!isset($kinds[$kind])) return 'bad_kind';
    $spec = $kinds[$kind];
    $key = isset($p['key']) && is_string($p['key']) ? $p['key'] : '';
    if ($spec['key'] !== null && !preg_match($spec['key'], $key)) return 'bad_key';
    if ($key === '' || sb_item_len($key) > 160) return 'bad_key';
    if (!isset($p['value']) || !is_array($p['value'])) return 'bad_value';
    $value = $spec['check']($p['value'], $key);
    if ($value === null) return 'bad_value';
    $json = sb_item_json($value);
    if (strlen($json) > SB_ITEM_VALUE_MAX) return 'too_large';
    $at = sb_item_at(isset($p['at']) ? $p['at'] : 0);
    $now = sb_item_now_ms();

    $st = $pdo->prepare('SELECT value_json, at_ms, deleted FROM user_items WHERE user_id = ? AND kind = ? AND item_key = ? FOR UPDATE');
    $st->execute([$uid, $kind, $key]);
    $row = $st->fetch();
    if (!$row) {
        if (sb_item_count($pdo, $uid, $kind) >= $spec['max'] || sb_item_count($pdo, $uid, null) >= SB_ITEM_TOTAL_MAX) return 'item_limit';
        $pdo->prepare('INSERT INTO user_items (user_id, kind, item_key, value_json, at_ms, deleted, rev, updated_ms) VALUES (?, ?, ?, ?, ?, 0, 1, ?)')
            ->execute([$uid, $kind, $key, $json, $at, $now]);
    } else {
        $alive = (int)$row['deleted'] === 0;
        if ($spec['rule'] === 'max') {
            $old = json_decode($row['value_json'], true);
            if ($alive && is_array($old) && isset($old['b']) && (float)$old['b'] >= (float)$value['b']) return null;     // only ever goes up
        } elseif ($at < (int)$row['at_ms']) {
            return null;                                                              // older than what the server has: ignored
        } elseif ($alive && $row['value_json'] === $json) {
            $pdo->prepare('UPDATE user_items SET at_ms = ? WHERE user_id = ? AND kind = ? AND item_key = ?')->execute([$at, $uid, $kind, $key]);
            return null;                                                              // nothing changed: no new change for the other devices
        }
        if (!$alive && sb_item_count($pdo, $uid, $kind) >= $spec['max']) return 'item_limit';
        $pdo->prepare('UPDATE user_items SET value_json = ?, at_ms = ?, deleted = 0, rev = rev + 1, updated_ms = ? WHERE user_id = ? AND kind = ? AND item_key = ?')
            ->execute([$json, max($at, (int)$row['at_ms']), $now, $uid, $kind, $key]);
    }
    sb_change_log($pdo, $uid, 'item', $kind . '|' . $key);
    return null;
}

// item.del: a tombstone, written even when the item never reached the server (a late save of it is then ignored).
function sb_item_del(PDO $pdo, int $uid, array $p): ?string
{
    $kind = isset($p['kind']) && is_string($p['kind']) ? $p['kind'] : '';
    $kinds = sb_item_kinds();
    if (!isset($kinds[$kind])) return 'bad_kind';
    if ($kinds[$kind]['rule'] === 'max') return 'not_deletable';
    $key = isset($p['key']) && is_string($p['key']) ? $p['key'] : '';
    if ($key === '' || sb_item_len($key) > 160 || ($kinds[$kind]['key'] !== null && !preg_match($kinds[$kind]['key'], $key))) return 'bad_key';
    $at = sb_item_at(isset($p['at']) ? $p['at'] : 0);
    $now = sb_item_now_ms();

    $st = $pdo->prepare('SELECT at_ms, deleted FROM user_items WHERE user_id = ? AND kind = ? AND item_key = ? FOR UPDATE');
    $st->execute([$uid, $kind, $key]);
    $row = $st->fetch();
    if (!$row) {
        if (sb_item_count($pdo, $uid, null) >= SB_ITEM_TOTAL_MAX) return 'item_limit';
        $pdo->prepare('INSERT INTO user_items (user_id, kind, item_key, value_json, at_ms, deleted, rev, updated_ms) VALUES (?, ?, ?, \'{}\', ?, 1, 1, ?)')
            ->execute([$uid, $kind, $key, $at, $now]);
    } else {
        if ($at < (int)$row['at_ms'] || (int)$row['deleted'] === 1) return null;      // a newer save stays; already deleted
        $pdo->prepare('UPDATE user_items SET value_json = \'{}\', at_ms = ?, deleted = 1, rev = rev + 1, updated_ms = ? WHERE user_id = ? AND kind = ? AND item_key = ?')
            ->execute([$at, $now, $uid, $kind, $key]);
    }
    sb_change_log($pdo, $uid, 'item', $kind . '|' . $key);
    return null;
}

// The rows a pull returns. $refs: set of "kind|key" named by the change log, or null for everything (a first sync: tombstones are not sent).
function sb_item_rows(PDO $pdo, int $uid, ?array $refs): array
{
    $out = ['items' => [], 'itemsDeleted' => []];
    $rows = [];
    if ($refs === null) {
        $st = $pdo->prepare('SELECT kind, item_key, value_json, at_ms, deleted FROM user_items WHERE user_id = ? AND deleted = 0 ORDER BY kind, item_key');
        $st->execute([$uid]);
        $rows = $st->fetchAll();
    } else {
        $pairs = [];
        foreach (array_keys($refs) as $ref) {
            $i = strpos((string)$ref, '|');
            if ($i === false) continue;
            $pairs[] = [substr((string)$ref, 0, $i), substr((string)$ref, $i + 1)];
        }
        foreach (array_chunk($pairs, 50) as $chunk) {
            $where = implode(' OR ', array_fill(0, count($chunk), '(kind = ? AND item_key = ?)'));
            $args = [$uid];
            foreach ($chunk as $pr) { $args[] = $pr[0]; $args[] = $pr[1]; }
            $st = $pdo->prepare("SELECT kind, item_key, value_json, at_ms, deleted FROM user_items WHERE user_id = ? AND ($where)");
            $st->execute($args);
            foreach ($st->fetchAll() as $r) $rows[] = $r;
        }
    }
    foreach ($rows as $r) {
        if ((int)$r['deleted'] === 1) { $out['itemsDeleted'][] = ['kind' => $r['kind'], 'key' => $r['item_key'], 'at' => (int)$r['at_ms']]; continue; }
        $v = json_decode($r['value_json'], true);
        $out['items'][] = ['kind' => $r['kind'], 'key' => $r['item_key'], 'value' => is_array($v) && $v ? $v : new stdClass(), 'at' => (int)$r['at_ms']];
    }
    return $out;
}
