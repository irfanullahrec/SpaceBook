<?php
// Reward coins: the rules live here, used by api/progress.php (v1) and api/v2/sync.php. Compatible with PHP 7.4.
//   +1 for each step the first time it is finished
//   +5 when the whole activity is first completed
//   +2 for doing a completed activity again (at most once per activity per day)
// Abuse limits (the browser can claim anything): an activity has at most SB_MAX_STEPS steps (the largest shipped
// figure has 126 countable items); per user and 24 hours at most SB_DAILY_COINS coins and SB_DAILY_NEW_ACTIVITIES
// new activities. Over the limit the progress is still recorded, but earns nothing (and past the new-activity
// limit nothing is created).
//
// Every function here expects to run inside a transaction (rows are locked with FOR UPDATE).

require_once __DIR__ . '/changes.php';

const SB_STEP_COIN            = 1;
const SB_COMPLETE_COIN        = 5;
const SB_PRACTICE_COIN        = 2;
const SB_MAX_STEPS            = 200;
const SB_DAILY_COINS          = 600;
const SB_DAILY_NEW_ACTIVITIES = 300;
const SB_BUDGET_WINDOW        = 86400;

function sb_parse_done(string $s): array
{
    return $s === '' ? [] : array_map('intval', explode(',', $s));
}

// Generic key check (the charset v1 always used).
function sb_reward_key($k): ?string
{
    $k = (string)$k;
    return preg_match('/^[A-Za-z0-9_.:|\-]{1,190}$/', $k) ? $k : null;
}

// Strict shape of the keys the app really produces: 'trace' / 'count' figures (js/sb_trace.js keyOf:
// class|subject|u<unit>|kind|<hash>|<n>) and study-plan sessions (js/sb_study_plan.js: plan|<planId>|<sessionId>).
// Returns 'trace', 'count', 'plan' or null.
function sb_reward_key_kind($k): ?string
{
    $k = (string)$k;
    if (strlen($k) > 190) return null;
    if (preg_match('/^[A-Za-z0-9_.:-]{1,40}\|[A-Za-z0-9_.:-]{1,60}\|u[A-Za-z0-9]{0,8}\|(trace|count)\|[a-z0-9]{1,10}\|[0-9]{1,3}$/', $k, $m)) return $m[1];
    if (preg_match('/^plan\|[A-Za-z0-9_.:-]{1,60}\|[A-Za-z0-9_.:-]{1,60}$/', $k)) return 'plan';
    return null;
}

// Takes up to $want from a fixed-window budget and returns how much was granted (0..$want).
function sb_budget_take(PDO $pdo, string $bucket, int $want, int $limit, int $windowSec): int
{
    if ($want <= 0) return 0;
    $pdo->prepare('INSERT IGNORE INTO rate_limits (bucket, window_start, hits) VALUES (?, NOW(), 0)')->execute([$bucket]);
    $st = $pdo->prepare('SELECT hits, window_start < NOW() - INTERVAL ? SECOND AS expired FROM rate_limits WHERE bucket = ? FOR UPDATE');
    $st->execute([$windowSec, $bucket]);
    $r = $st->fetch();
    $used = (int)$r['hits'];
    if ((int)$r['expired'] === 1) {
        $pdo->prepare('UPDATE rate_limits SET hits = 0, window_start = NOW() WHERE bucket = ?')->execute([$bucket]);
        $used = 0;
    }
    $granted = max(0, min($want, $limit - $used));
    if ($granted > 0) $pdo->prepare('UPDATE rate_limits SET hits = hits + ? WHERE bucket = ?')->execute([$granted, $bucket]);
    return $granted;
}

function sb_total_coins(PDO $pdo, int $uid): int
{
    $st = $pdo->prepare('SELECT COALESCE(SUM(coins_earned), 0) FROM activity_progress WHERE user_id = ?');
    $st->execute([$uid]);
    return (int)$st->fetchColumn();
}

function sb_progress_row(PDO $pdo, int $uid, string $key): ?array
{
    $st = $pdo->prepare('SELECT * FROM activity_progress WHERE user_id = ? AND activity_key = ? FOR UPDATE');
    $st->execute([$uid, $key]);
    $row = $st->fetch();
    return $row ? $row : null;
}

// Adds finished steps to one activity. Returns ['earned' => coins granted, 'completed' => finished now?,
// 'times' => times completed, 'created' => false when the new-activity limit stopped it]. Steps are a set: sending
// the same step twice, or in any order from any device, never pays twice.
function sb_reward_add_steps(PDO $pdo, int $uid, string $key, string $title, int $total, array $steps): array
{
    $total = max(1, min(SB_MAX_STEPS, $total));
    $row = sb_progress_row($pdo, $uid, $key);
    if (!$row) {
        if (sb_budget_take($pdo, 'acts:u:' . $uid, 1, SB_DAILY_NEW_ACTIVITIES, SB_BUDGET_WINDOW) < 1) {
            return ['earned' => 0, 'completed' => false, 'times' => 0, 'created' => false];
        }
        $pdo->prepare('INSERT INTO activity_progress (user_id, activity_key, title, steps_total, steps_done) VALUES (?, ?, ?, ?, \'\')')
            ->execute([$uid, $key, mb_substr($title, 0, 190), $total]);
        $row = ['steps_total' => $total, 'steps_done' => '', 'times_completed' => 0];
    }
    $total = (int)$row['steps_total'];               // the first report fixes the size of the activity
    $done = sb_parse_done($row['steps_done']);
    $earned = 0;
    foreach ($steps as $s) {
        $s = (int)$s;
        if ($s < 0 || $s >= $total || in_array($s, $done, true)) continue;
        $done[] = $s;
        $earned += SB_STEP_COIN;
    }
    sort($done);
    $times = (int)$row['times_completed'];
    $completedNow = false;
    if ($times === 0 && count($done) >= $total) {
        $earned += SB_COMPLETE_COIN;
        $times = 1;
        $completedNow = true;
    }
    $earned = sb_budget_take($pdo, 'coins:u:' . $uid, $earned, SB_DAILY_COINS, SB_BUDGET_WINDOW);
    $pdo->prepare('UPDATE activity_progress SET steps_done = ?, coins_earned = coins_earned + ?, times_completed = ?,
                       first_completed_at = IF(? AND first_completed_at IS NULL, NOW(), first_completed_at),
                       last_completed_at  = IF(?, NOW(), last_completed_at)
                   WHERE user_id = ? AND activity_key = ?')
        ->execute([implode(',', $done), $earned, $times, $completedNow ? 1 : 0, $completedNow ? 1 : 0, $uid, $key]);
    sb_change_log($pdo, $uid, 'act', $key);
    return ['earned' => $earned, 'completed' => $completedNow, 'times' => $times, 'created' => true];
}

// A completed activity was done again. Returns null when it was never completed, else ['earned' => ..., 'times' => ...].
function sb_reward_again(PDO $pdo, int $uid, string $key): ?array
{
    $row = sb_progress_row($pdo, $uid, $key);
    if (!$row || (int)$row['times_completed'] === 0) return null;
    $st = $pdo->prepare('SELECT last_completed_at >= CURDATE() FROM activity_progress WHERE user_id = ? AND activity_key = ?');
    $st->execute([$uid, $key]);
    $doneToday = (int)$st->fetchColumn() === 1;
    $earned = $doneToday ? 0 : sb_budget_take($pdo, 'coins:u:' . $uid, SB_PRACTICE_COIN, SB_DAILY_COINS, SB_BUDGET_WINDOW);
    $pdo->prepare('UPDATE activity_progress SET times_completed = times_completed + 1, coins_earned = coins_earned + ?, last_completed_at = NOW()
                   WHERE user_id = ? AND activity_key = ?')->execute([$earned, $uid, $key]);
    sb_change_log($pdo, $uid, 'act', $key);
    return ['earned' => $earned, 'times' => (int)$row['times_completed'] + 1];
}
