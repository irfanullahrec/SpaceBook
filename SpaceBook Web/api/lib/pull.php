<?php
// GET api/v2/sync.php?since=<seq>: the current state of everything that changed after the cursor.
// since=0 (first sync on a device) returns the full state. Compatible with PHP 7.4.
//
//   {ok, cursor, more, coins,
//    progress: {activityKey: {done:[..], total, times, first, last}},
//    plans: [plan...], plansDeleted: [id...],
//    tp: {q: {mcqId: [attempts, correct, lastTs, lastCorrect, ms]}, days: {track: {day: [ms, answered, correct]}},
//         sessions: [session...], run: {...}|null, runClearedAt}      (run and runClearedAt only when they changed, or on a full pull)
//    items: [{kind, key, value, at}...], itemsDeleted: [{kind, key, at}...]}      (bookmarks, notes, positions ...: api/lib/items.php)
//
// Objects are absolute (not deltas), so applying a pull twice, or in any order, gives the same result.
// `cursor` is the highest change number covered; call again with it. `more` = there is a next page.

const SB_PULL_PAGE = 2000;

function sb_pull(PDO $pdo, int $uid, int $since): array
{
    $refs = ['act' => [], 'plan' => [], 'tpq' => [], 'tpd' => [], 'tps' => [], 'tpr' => [], 'item' => []];
    $full = $since <= 0;
    $more = false;
    if ($full) {
        $cursor = sb_change_cursor($pdo, $uid);              // read first: a change during the read is delivered again next time
    } else {
        $st = $pdo->prepare('SELECT seq, kind, ref FROM sync_changes WHERE user_id = ? AND seq > ? ORDER BY seq LIMIT ' . (SB_PULL_PAGE + 1));
        $st->execute([$uid, $since]);
        $rows = $st->fetchAll();
        if (count($rows) > SB_PULL_PAGE) { $more = true; array_pop($rows); }
        $cursor = $since;
        foreach ($rows as $r) {
            $cursor = (int)$r['seq'];
            if (isset($refs[$r['kind']])) $refs[$r['kind']][$r['ref']] = true;
        }
    }
    $want = function (string $kind, string $ref) use ($full, $refs): bool { return $full || isset($refs[$kind][$ref]); };

    $out = ['ok' => true, 'cursor' => $cursor, 'more' => $more, 'coins' => sb_total_coins($pdo, $uid),
            'progress' => [], 'plans' => [], 'plansDeleted' => [], 'tp' => ['q' => [], 'days' => [], 'sessions' => []]];     // run / runClearedAt only when the unfinished test changed (or on a full pull)

    $st = $pdo->prepare('SELECT activity_key, steps_total, steps_done, times_completed, first_completed_at, last_completed_at FROM activity_progress WHERE user_id = ?');
    $st->execute([$uid]);
    foreach ($st as $r) {
        if (!$want('act', $r['activity_key'])) continue;
        $out['progress'][$r['activity_key']] = ['done' => sb_parse_done($r['steps_done']), 'total' => (int)$r['steps_total'],
            'times' => (int)$r['times_completed'], 'first' => $r['first_completed_at'], 'last' => $r['last_completed_at']];
    }

    $st = $pdo->prepare('SELECT plan_id, plan_json, deleted, rev FROM study_plans WHERE user_id = ?');
    $st->execute([$uid]);
    foreach ($st as $r) {
        if (!$want('plan', $r['plan_id'])) continue;
        if ((int)$r['deleted'] === 1) { $out['plansDeleted'][] = $r['plan_id']; continue; }
        $p = json_decode($r['plan_json'], true);
        if (is_array($p)) { $p['rev'] = (int)$r['rev']; $out['plans'][] = $p; }
    }

    $st = $pdo->prepare('SELECT mcq_id, attempts, correct, last_ts, last_correct, total_ms FROM tp_answers WHERE user_id = ?');
    $st->execute([$uid]);
    foreach ($st as $r) {
        if ($want('tpq', $r['mcq_id'])) $out['tp']['q'][$r['mcq_id']] = [(int)$r['attempts'], (int)$r['correct'], (int)$r['last_ts'], (int)$r['last_correct'], (int)$r['total_ms']];
    }

    $st = $pdo->prepare('SELECT track, day, ms, answered, correct FROM tp_days WHERE user_id = ?');
    $st->execute([$uid]);
    $all = [];
    foreach ($st as $r) {
        $v = [(int)$r['ms'], (int)$r['answered'], (int)$r['correct']];
        $a = isset($all[$r['day']]) ? $all[$r['day']] : [0, 0, 0];
        $all[$r['day']] = [$a[0] + $v[0], $a[1] + $v[1], $a[2] + $v[2]];
        if ($want('tpd', $r['track'] . '|' . $r['day'])) $out['tp']['days'][$r['track']][$r['day']] = $v;
    }
    // the page keeps a track called 'all' (the sum of the tracks) for the daily minutes; send it for the days that changed
    foreach ($out['tp']['days'] as $track => $days) {
        foreach ($days as $day => $_) $out['tp']['days']['all'][$day] = $all[$day];
    }

    $st = $pdo->prepare('SELECT session_id, session_json FROM test_prep_sessions WHERE user_id = ? ORDER BY started_ms DESC LIMIT 300');
    $st->execute([$uid]);
    foreach ($st as $r) {
        if (!$want('tps', $r['session_id'])) continue;
        $s = json_decode($r['session_json'], true);
        if (is_array($s)) $out['tp']['sessions'][] = $s;
    }
    $out['tp']['sessions'] = array_reverse($out['tp']['sessions']);

    $out = array_merge($out, sb_item_rows($pdo, $uid, $full ? null : $refs['item']));

    if ($want('tpr', 'run')) {
        $out['tp']['run'] = null;
        $out['tp']['runClearedAt'] = 0;
        $st = $pdo->prepare('SELECT run_json, saved_ms, cleared_ms FROM tp_runs WHERE user_id = ?');
        $st->execute([$uid]);
        $r = $st->fetch();
        if ($r) {
            $run = json_decode($r['run_json'], true);
            $out['tp']['runClearedAt'] = (int)$r['cleared_ms'];
            $out['tp']['run'] = (is_array($run) && $run && (int)$r['saved_ms'] > (int)$r['cleared_ms']) ? $run : null;
        }
    }
    return $out;
}
