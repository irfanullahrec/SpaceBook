<?php
// Study plans: server-side merge. Compatible with PHP 7.4.
//
// The server numbers every accepted change of a plan (`rev`); a device says which revision its edit was based on
// (`baseRev`). Ordering never uses a device clock.
//   - baseRev >= rev (the device had seen the latest), or the same device wrote last: its plan replaces the stored one.
//   - baseRev <  rev and another device wrote last (someone else changed it meanwhile): the incoming plan wins field by field, but a task that
//     exists on both sides keeps the larger `done`, so ticked work is never lost to a concurrent edit.
//     Tasks that exist only on the server and not in the incoming plan are treated as removed by the device.
//   - a deleted plan stays as a tombstone: later saves of it are ignored, so an offline edit cannot resurrect it.
// The plan JSON is stored untouched (including its own `updatedAt`, which the page shows); `rev` is the order.

const SB_MAX_PLANS      = 50;
const SB_PLAN_ID        = '/^[A-Za-z0-9_-]{4,40}$/';

function sb_plan_task_done(array $plan): array
{
    $out = [];
    foreach ((isset($plan['sessions']) && is_array($plan['sessions']) ? $plan['sessions'] : []) as $s) {
        foreach ((isset($s['tasks']) && is_array($s['tasks']) ? $s['tasks'] : []) as $t) {
            if (is_array($t) && isset($t['id'])) $out[(string)$t['id']] = isset($t['done']) ? (float)$t['done'] : 0;
        }
    }
    return $out;
}

// The learning record of each task ({mode: 'check'|'self', at, rounds, asked, ...}): the proof that the student passed the check of that task.
function sb_plan_task_learn(array $plan): array
{
    $out = [];
    foreach ((isset($plan['sessions']) && is_array($plan['sessions']) ? $plan['sessions'] : []) as $s) {
        foreach ((isset($s['tasks']) && is_array($s['tasks']) ? $s['tasks'] : []) as $t) {
            if (is_array($t) && isset($t['id']) && isset($t['learn']) && is_array($t['learn'])) $out[(string)$t['id']] = $t['learn'];
        }
    }
    return $out;
}

// Of two records of one task keep the better: a passed check beats the student's own word, then the later one.
function sb_learn_pick(?array $a, ?array $b): ?array
{
    if ($a === null) return $b;
    if ($b === null) return $a;
    $ra = (isset($a['mode']) && $a['mode'] === 'check') ? 1 : 0;
    $rb = (isset($b['mode']) && $b['mode'] === 'check') ? 1 : 0;
    if ($ra !== $rb) return $ra > $rb ? $a : $b;
    return ((isset($b['at']) ? (float)$b['at'] : 0) > (isset($a['at']) ? (float)$a['at'] : 0)) ? $b : $a;
}

function sb_plan_merge(array $incoming, array $stored): array
{
    $srv = sb_plan_task_done($stored);
    $srvLearn = sb_plan_task_learn($stored);
    if (!$srv || !isset($incoming['sessions']) || !is_array($incoming['sessions'])) return $incoming;
    foreach ($incoming['sessions'] as $si => $s) {
        if (!is_array($s) || !isset($s['tasks']) || !is_array($s['tasks'])) continue;
        foreach ($s['tasks'] as $ti => $t) {
            if (!is_array($t) || !isset($t['id']) || !isset($srv[(string)$t['id']])) continue;
            $id = (string)$t['id'];
            $mine = isset($t['done']) ? (float)$t['done'] : 0;
            if ($srv[$id] > $mine) $incoming['sessions'][$si]['tasks'][$ti]['done'] = $srv[$id];
            // the proof travels with the ticked work: a record one device holds is not lost because the other one never saw it
            if (isset($srvLearn[$id])) {
                $kept = sb_learn_pick(isset($t['learn']) && is_array($t['learn']) ? $t['learn'] : null, $srvLearn[$id]);
                if ($kept !== null) $incoming['sessions'][$si]['tasks'][$ti]['learn'] = $kept;
            }
        }
    }
    return $incoming;
}

function sb_plan_now_ms(): int { return (int)round(microtime(true) * 1000); }

// Returns null when handled (applied or deliberately ignored), else a rejection code.
// $deviceId: a save from the device that wrote the plan last is a fast-forward whatever its baseRev (it already contains
// that device's earlier edits, so an un-tick must stick); only another device's stale save is merged.
function sb_plan_save(PDO $pdo, int $uid, array $plan, int $baseRev, string $deviceId = ''): ?string
{
    $id = isset($plan['id']) ? (string)$plan['id'] : '';
    if (!preg_match(SB_PLAN_ID, $id)) return 'bad_plan_id';
    $json = json_encode($plan, JSON_UNESCAPED_UNICODE);
    $st = $pdo->prepare('SELECT plan_json, deleted, rev, last_device FROM study_plans WHERE user_id = ? AND plan_id = ? FOR UPDATE');
    $st->execute([$uid, $id]);
    $row = $st->fetch();
    if (!$row) {
        $st = $pdo->prepare('SELECT COUNT(*) FROM study_plans WHERE user_id = ? AND deleted = 0');
        $st->execute([$uid]);
        if ((int)$st->fetchColumn() >= SB_MAX_PLANS) return 'plan_limit';
        $pdo->prepare('INSERT INTO study_plans (user_id, plan_id, plan_json, updated_ms, deleted, rev, last_device) VALUES (?, ?, ?, ?, 0, 1, ?)')
            ->execute([$uid, $id, $json, sb_plan_now_ms(), $deviceId]);
    } else {
        if ((int)$row['deleted'] === 1) return null;                       // tombstone wins
        $rev = (int)$row['rev'];
        if ($baseRev < $rev && $row['last_device'] !== $deviceId) {
            $stored = json_decode($row['plan_json'], true);
            if (is_array($stored)) $json = json_encode(sb_plan_merge($plan, $stored), JSON_UNESCAPED_UNICODE);
        }
        $pdo->prepare('UPDATE study_plans SET plan_json = ?, updated_ms = ?, rev = rev + 1, last_device = ? WHERE user_id = ? AND plan_id = ?')
            ->execute([$json, sb_plan_now_ms(), $deviceId, $uid, $id]);
    }
    sb_change_log($pdo, $uid, 'plan', $id);
    return null;
}

function sb_plan_delete(PDO $pdo, int $uid, string $id): ?string
{
    if (!preg_match(SB_PLAN_ID, $id)) return 'bad_plan_id';
    // a tombstone is written even when the plan never reached the server, so a late save of it is ignored
    $pdo->prepare('INSERT INTO study_plans (user_id, plan_id, plan_json, updated_ms, deleted, rev) VALUES (?, ?, \'{}\', ?, 1, 1)
                   ON DUPLICATE KEY UPDATE plan_json = \'{}\', deleted = 1, last_device = \'\', updated_ms = VALUES(updated_ms), rev = rev + 1')
        ->execute([$uid, $id, sb_plan_now_ms()]);
    sb_change_log($pdo, $uid, 'plan', $id);
    return null;
}
