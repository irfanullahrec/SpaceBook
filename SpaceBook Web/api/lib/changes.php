<?php
// Change log behind GET api/v2/sync.php?since=<seq>. Every write a device could want to pull (progress, plans,
// test-prep answers/days/sessions/unfinished run) adds one row; the pull returns the CURRENT state of the
// objects named after a cursor, so replays and out-of-order delivery are harmless. Compatible with PHP 7.4.

function sb_change_log(PDO $pdo, int $uid, string $kind, string $ref): void
{
    $pdo->prepare('INSERT INTO sync_changes (user_id, kind, ref) VALUES (?, ?, ?)')->execute([$uid, substr($kind, 0, 8), substr($ref, 0, 190)]);
}

function sb_change_cursor(PDO $pdo, int $uid): int
{
    $st = $pdo->prepare('SELECT COALESCE(MAX(seq), 0) FROM sync_changes WHERE user_id = ?');
    $st->execute([$uid]);
    return (int)$st->fetchColumn();
}
