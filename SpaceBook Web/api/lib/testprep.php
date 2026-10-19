<?php
// Tests Preps state on the server. Compatible with PHP 7.4.
//
//   tp.answer  one answer: per-MCQ counters are ADDED (the event ledger makes each event count once, so two
//              devices answering the same MCQ both count; the old whole-record last-writer-wins lost one).
//   tp.session a finished session (kept once by id, like v1)
//   tp.run / tp.run.clear   the unfinished session: the copy saved last wins unless cleared later
// The legacy v1 record (test_prep_records blob) is merged in with "more attempts wins" per MCQ, once per user
// (sb_tp_import_legacy) and whenever an old client saves (sb_tp_merge_blob).

const SB_TP_MCQ_ID   = '/^[A-Za-z0-9_-]{1,40}$/';
const SB_TP_TRACK    = '/^[a-z0-9-]{1,40}$/';
const SB_TP_DAY      = '/^\d{4}-\d{2}-\d{2}$/';
const SB_TP_MAX_MS   = 3600000;          // one answer never counts more than an hour
const SB_TP_DAY_MS   = 300000;           // and at most 5 minutes towards the daily minutes (same cap as the page)

function sb_tp_clamp_ts($ts): int
{
    $ts = is_numeric($ts) ? (int)$ts : 0;
    return max(0, min($ts, (int)round(microtime(true) * 1000) + 86400000));   // not more than a day ahead
}

function sb_tp_answer(PDO $pdo, int $uid, array $p): ?string
{
    $id = isset($p['mcqId']) ? (string)$p['mcqId'] : '';
    $track = isset($p['track']) ? (string)$p['track'] : '';
    $day = isset($p['day']) ? (string)$p['day'] : '';
    if (!preg_match(SB_TP_MCQ_ID, $id)) return 'bad_mcq';
    if (!preg_match(SB_TP_TRACK, $track) || $track === 'all') return 'bad_track';
    if (!preg_match(SB_TP_DAY, $day)) return 'bad_day';
    $correct = !empty($p['correct']) ? 1 : 0;
    $ms = isset($p['ms']) && is_numeric($p['ms']) ? max(0, min((int)$p['ms'], SB_TP_MAX_MS)) : 0;
    $ts = sb_tp_clamp_ts(isset($p['ts']) ? $p['ts'] : 0);
    // last_correct is assigned before last_ts so it compares against the previous last_ts
    $pdo->prepare('INSERT INTO tp_answers (user_id, mcq_id, attempts, correct, last_ts, last_correct, total_ms) VALUES (?, ?, 1, ?, ?, ?, ?)
                   ON DUPLICATE KEY UPDATE
                     last_correct = IF(VALUES(last_ts) >= last_ts, VALUES(last_correct), last_correct),
                     attempts     = attempts + 1,
                     correct      = correct + VALUES(correct),
                     total_ms     = total_ms + VALUES(total_ms),
                     last_ts      = GREATEST(last_ts, VALUES(last_ts))')
        ->execute([$uid, $id, $correct, $ts, $correct, $ms]);
    $pdo->prepare('INSERT INTO tp_days (user_id, track, day, ms, answered, correct) VALUES (?, ?, ?, ?, 1, ?)
                   ON DUPLICATE KEY UPDATE ms = ms + VALUES(ms), answered = answered + 1, correct = correct + VALUES(correct)')
        ->execute([$uid, $track, $day, min($ms, SB_TP_DAY_MS), $correct]);
    sb_change_log($pdo, $uid, 'tpq', $id);
    sb_change_log($pdo, $uid, 'tpd', $track . '|' . $day);
    return null;
}

function sb_tp_session(PDO $pdo, int $uid, array $s): ?string
{
    $id = isset($s['id']) ? (string)$s['id'] : '';
    $track = isset($s['track']) ? (string)$s['track'] : '';
    $mode = isset($s['mode']) ? (string)$s['mode'] : '';
    if (!preg_match('/^[A-Za-z0-9_-]{3,40}$/', $id) || !preg_match('/^[a-z0-9-]{1,40}$/', $track) || !in_array($mode, ['practice', 'mock'], true)) return 'bad_session';
    $n = max(0, (int)(isset($s['n']) ? $s['n'] : 0));
    $c = max(0, min($n, (int)(isset($s['c']) ? $s['c'] : 0)));
    $st = $pdo->prepare('INSERT IGNORE INTO test_prep_sessions (user_id, session_id, track, mode, questions, correct, duration_ms, started_ms, session_json)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)');
    $st->execute([$uid, $id, $track, $mode, $n, $c, max(0, (int)(isset($s['ms']) ? $s['ms'] : 0)), sb_tp_clamp_ts(isset($s['ts']) ? $s['ts'] : 0), json_encode($s, JSON_UNESCAPED_UNICODE)]);
    if ($st->rowCount() > 0) sb_change_log($pdo, $uid, 'tps', $id);
    return null;
}

function sb_tp_run_save(PDO $pdo, int $uid, array $run): ?string
{
    $saved = sb_tp_clamp_ts(isset($run['savedAt']) ? $run['savedAt'] : 0);
    if ($saved <= 0) return 'bad_run';
    $st = $pdo->prepare('INSERT INTO tp_runs (user_id, run_json, saved_ms, cleared_ms) VALUES (?, ?, ?, 0)
                   ON DUPLICATE KEY UPDATE
                     run_json = IF(VALUES(saved_ms) >= saved_ms, VALUES(run_json), run_json),
                     saved_ms = GREATEST(saved_ms, VALUES(saved_ms))');
    $st->execute([$uid, json_encode($run, JSON_UNESCAPED_UNICODE), $saved]);
    if ($st->rowCount() > 0) sb_change_log($pdo, $uid, 'tpr', 'run');
    return null;
}

function sb_tp_run_clear(PDO $pdo, int $uid, array $p): ?string
{
    $at = sb_tp_clamp_ts(isset($p['clearedAt']) ? $p['clearedAt'] : 0);
    if ($at <= 0) return 'bad_run';
    $st = $pdo->prepare('INSERT INTO tp_runs (user_id, run_json, saved_ms, cleared_ms) VALUES (?, \'{}\', 0, ?)
                   ON DUPLICATE KEY UPDATE cleared_ms = GREATEST(cleared_ms, VALUES(cleared_ms))');
    $st->execute([$uid, $at]);
    if ($st->rowCount() > 0) sb_change_log($pdo, $uid, 'tpr', 'run');
    return null;
}

// Old-format record {q:{id:[attempts, correct, lastTs, lastCorrect, ms]}, days:{track:{day:[ms, n, c]}}, run, runClearedAt}:
// the copy with more attempts wins per MCQ, the larger number per day. Skips 'all' (the sum is computed on read).
function sb_tp_merge_blob(PDO $pdo, int $uid, array $rec): void
{
    $q = $pdo->prepare('INSERT INTO tp_answers (user_id, mcq_id, attempts, correct, last_ts, last_correct, total_ms) VALUES (?, ?, ?, ?, ?, ?, ?)
                        ON DUPLICATE KEY UPDATE
                          correct      = IF(VALUES(attempts) > attempts OR (VALUES(attempts) = attempts AND VALUES(last_ts) > last_ts), VALUES(correct), correct),
                          total_ms     = IF(VALUES(attempts) > attempts OR (VALUES(attempts) = attempts AND VALUES(last_ts) > last_ts), VALUES(total_ms), total_ms),
                          last_correct = IF(VALUES(attempts) > attempts OR (VALUES(attempts) = attempts AND VALUES(last_ts) > last_ts), VALUES(last_correct), last_correct),
                          last_ts      = IF(VALUES(attempts) > attempts OR (VALUES(attempts) = attempts AND VALUES(last_ts) > last_ts), VALUES(last_ts), last_ts),
                          attempts     = GREATEST(attempts, VALUES(attempts))');
    $n = 0;
    foreach ((isset($rec['q']) && is_array($rec['q']) ? $rec['q'] : []) as $id => $v) {
        if (!preg_match(SB_TP_MCQ_ID, (string)$id) || !is_array($v) || count($v) < 4 || $n >= 20000) continue;
        $n++;
        $q->execute([$uid, (string)$id, max(0, (int)$v[0]), max(0, (int)$v[1]), max(0, (int)$v[2]), empty($v[3]) ? 0 : 1, max(0, (int)(isset($v[4]) ? $v[4] : 0))]);
        if ($q->rowCount() > 0) sb_change_log($pdo, $uid, 'tpq', (string)$id);      // only rows that really changed
    }
    $d = $pdo->prepare('INSERT INTO tp_days (user_id, track, day, ms, answered, correct) VALUES (?, ?, ?, ?, ?, ?)
                        ON DUPLICATE KEY UPDATE ms = GREATEST(ms, VALUES(ms)), answered = GREATEST(answered, VALUES(answered)), correct = GREATEST(correct, VALUES(correct))');
    foreach ((isset($rec['days']) && is_array($rec['days']) ? $rec['days'] : []) as $track => $days) {
        if (!preg_match(SB_TP_TRACK, (string)$track) || $track === 'all' || !is_array($days)) continue;
        foreach ($days as $day => $v) {
            if (!preg_match(SB_TP_DAY, (string)$day) || !is_array($v) || count($v) < 3) continue;
            $d->execute([$uid, (string)$track, (string)$day, max(0, (int)$v[0]), max(0, (int)$v[1]), max(0, (int)$v[2])]);
            if ($d->rowCount() > 0) sb_change_log($pdo, $uid, 'tpd', $track . '|' . $day);
        }
    }
    if (isset($rec['run']) && is_array($rec['run'])) sb_tp_run_save($pdo, $uid, $rec['run']);
    if (!empty($rec['runClearedAt'])) sb_tp_run_clear($pdo, $uid, ['clearedAt' => $rec['runClearedAt']]);
}

// Once per user: bring the v1 blob into the tables.
function sb_tp_import_legacy(PDO $pdo, int $uid): void
{
    $pdo->prepare('INSERT IGNORE INTO user_sync_state (user_id, legacy_imported) VALUES (?, 0)')->execute([$uid]);
    $st = $pdo->prepare('SELECT legacy_imported FROM user_sync_state WHERE user_id = ? FOR UPDATE');
    $st->execute([$uid]);
    if ((int)$st->fetchColumn() === 1) return;
    $st = $pdo->prepare('SELECT record_json FROM test_prep_records WHERE user_id = ?');
    $st->execute([$uid]);
    $json = $st->fetchColumn();
    $rec = $json ? json_decode($json, true) : null;
    if (is_array($rec)) sb_tp_merge_blob($pdo, $uid, $rec);
    $pdo->prepare('UPDATE user_sync_state SET legacy_imported = 1 WHERE user_id = ?')->execute([$uid]);
}
