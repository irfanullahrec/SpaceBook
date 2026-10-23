<?php
// Account lifecycle: a student's own data export and the purge of deleted accounts. Compatible with PHP 7.4.

function sb_json_or_null($s)
{
    $v = json_decode((string)$s, true);
    return $v === null ? null : $v;
}

// Everything the system holds about one user, except secrets (password hash, device tokens).
function sb_account_export(PDO $pdo, int $uid): array
{
    $one = function (string $sql, array $args = []) use ($pdo) {
        $st = $pdo->prepare($sql);
        $st->execute($args);
        return $st->fetchAll();
    };
    $user = $one('SELECT id, name, father_name, user_type, whatsapp, status, created_at, last_login_at FROM users WHERE id = ?', [$uid]);
    $plans = [];
    foreach ($one('SELECT plan_id, plan_json, rev, updated_ms FROM study_plans WHERE user_id = ? AND deleted = 0', [$uid]) as $r) {
        $plans[] = ['id' => $r['plan_id'], 'rev' => (int)$r['rev'], 'plan' => sb_json_or_null($r['plan_json'])];
    }
    $sessions = [];
    foreach ($one('SELECT session_json FROM test_prep_sessions WHERE user_id = ? ORDER BY started_ms', [$uid]) as $r) {
        $sessions[] = sb_json_or_null($r['session_json']);
    }
    $legacy = $one('SELECT record_json FROM test_prep_records WHERE user_id = ?', [$uid]);
    $run = $one('SELECT run_json, saved_ms, cleared_ms FROM tp_runs WHERE user_id = ?', [$uid]);
    $items = [];
    foreach ($one('SELECT kind, item_key, value_json, at_ms FROM user_items WHERE user_id = ? AND deleted = 0 ORDER BY kind, item_key', [$uid]) as $r) {
        $items[] = ['kind' => $r['kind'], 'key' => $r['item_key'], 'value' => sb_json_or_null($r['value_json']), 'at' => (int)$r['at_ms']];
    }
    return [
        'schema'      => 'spacebook.export/1',
        'exported_at' => gmdate('c'),
        'account'     => $user ? $user[0] : null,
        'rewards'     => $one('SELECT activity_key, title, steps_total, steps_done, coins_earned, times_completed, first_completed_at, last_completed_at FROM activity_progress WHERE user_id = ?', [$uid]),
        'study_plans' => $plans,
        'tests_preps' => [
            'answers'          => $one('SELECT mcq_id, attempts, correct, last_ts, last_correct, total_ms FROM tp_answers WHERE user_id = ?', [$uid]),
            'days'             => $one('SELECT track, day, ms, answered, correct FROM tp_days WHERE user_id = ?', [$uid]),
            'sessions'         => $sessions,
            'unfinished_test'  => $run ? ['run' => sb_json_or_null($run[0]['run_json']), 'saved_ms' => (int)$run[0]['saved_ms'], 'cleared_ms' => (int)$run[0]['cleared_ms']] : null,
            'older_record'     => $legacy ? sb_json_or_null($legacy[0]['record_json']) : null,
        ],
        'saved_items' => $items,       // bookmarks, notes and highlights, reading positions, marked words, best game runs, settings, ticked SLOs
        'devices'     => $one('SELECT id, name, created_at, last_seen, revoked FROM devices WHERE user_id = ?', [$uid]),
        'activity_log' => $one('SELECT action, ip, created_at FROM audit_log WHERE user_id = ? ORDER BY id DESC LIMIT 200', [$uid]),
    ];
}

// Removes one user and everything attached to them (tables with a foreign key cascade; the others are cleared here).
function sb_purge_user(PDO $pdo, int $uid): void
{
    foreach (['sync_events', 'sync_changes', 'tp_answers', 'tp_days', 'tp_runs', 'user_sync_state', 'audit_log'] as $t) {
        $pdo->prepare("DELETE FROM $t WHERE user_id = ?")->execute([$uid]);
    }
    foreach (['coins:u:', 'acts:u:', 'sync:u:', 'pw:u:'] as $prefix) {
        $pdo->prepare('DELETE FROM rate_limits WHERE bucket = ?')->execute([$prefix . $uid]);
    }
    $pdo->prepare('DELETE FROM users WHERE id = ?')->execute([$uid]);       // devices, progress, plans, test-prep rows go by cascade
}

// Accounts deleted more than $days days ago. Returns the number purged.
function sb_purge_deleted(PDO $pdo, int $days = 30): int
{
    $st = $pdo->prepare("SELECT id FROM users WHERE status = 'deleted' AND deleted_at IS NOT NULL AND deleted_at < NOW() - INTERVAL " . (int)$days . ' DAY');
    $st->execute();
    $ids = $st->fetchAll(PDO::FETCH_COLUMN);
    foreach ($ids as $id) sb_purge_user($pdo, (int)$id);
    return count($ids);
}
