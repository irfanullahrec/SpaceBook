<?php
// Tests Preps statistics and track record of the signed-in student.
// Only progress is stored here — the MCQs themselves stay in js/test_prep_bank.js.
//   GET  api/test_prep.php?action=load                       → {ok, record:{q,days,run,runClearedAt,updatedAt}|null, sessions:[…]}
//   POST api/test_prep.php?action=save    {record:{…}}       newer copy (updatedAt) wins
//   POST api/test_prep.php?action=session {session:{id,track,mode,ts,n,c,ms,items,secs,lv}}  one finished session, kept once
// The browser keeps its own copy too, so practice works offline and for guests.

require __DIR__ . '/db.php';
require __DIR__ . '/session.php';
require __DIR__ . '/lib/security.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const MAX_RECORD_BYTES  = 4000000;
const MAX_SESSION_BYTES = 200000;
const MAX_SESSIONS_SENT = 300;

function reply(int $code, array $body): void
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function fail(int $code, string $msg): void
{
    reply($code, ['ok' => false, 'error' => $msg]);
}

function input(): array
{
    $data = json_decode(file_get_contents('php://input') ?: '', true);
    return is_array($data) ? $data : [];
}

if (empty($_SESSION['uid'])) fail(401, 'Log in to keep your test progress on every device');
$uid = (int)$_SESSION['uid'];

try {
    $pdo = db();
} catch (Throwable $e) {
    error_log('SpaceBook DB: ' . $e->getMessage());
    fail(500, 'Database connection failed');
}

$action = $_GET['action'] ?? '';
if ($action !== 'load' && $_SERVER['REQUEST_METHOD'] !== 'POST') fail(405, 'POST required');
if ($action !== 'get' && $action !== 'load' && $action !== 'list' && !sb_request_is_same_site()) fail(403, 'Request not allowed');

try {
    switch ($action) {

    case 'load':
        $st = $pdo->prepare('SELECT record_json FROM test_prep_records WHERE user_id = ?');
        $st->execute([$uid]);
        $json = $st->fetchColumn();
        $record = $json ? json_decode($json, true) : null;
        $st = $pdo->prepare('SELECT session_json FROM test_prep_sessions WHERE user_id = ? ORDER BY started_ms DESC LIMIT ' . MAX_SESSIONS_SENT);
        $st->execute([$uid]);
        $sessions = [];
        foreach ($st as $r) {
            $s = json_decode($r['session_json'], true);
            if (is_array($s)) $sessions[] = $s;
        }
        reply(200, ['ok' => true, 'record' => is_array($record) ? $record : null, 'sessions' => array_reverse($sessions)]);

    case 'save':
        $rec = input()['record'] ?? null;
        if (!is_array($rec)) fail(422, 'Bad record');
        $json = json_encode($rec, JSON_UNESCAPED_UNICODE);
        if (strlen($json) > MAX_RECORD_BYTES) fail(413, 'Record is too large');
        $ms = max(0, (int)($rec['updatedAt'] ?? 0));
        // keep the newer copy when two devices practise at the same time
        $pdo->prepare('INSERT INTO test_prep_records (user_id, record_json, updated_ms) VALUES (?, ?, ?)
                       ON DUPLICATE KEY UPDATE
                         record_json = IF(VALUES(updated_ms) >= updated_ms, VALUES(record_json), record_json),
                         updated_ms  = GREATEST(updated_ms, VALUES(updated_ms))')
            ->execute([$uid, $json, $ms]);
        reply(200, ['ok' => true]);

    case 'session':
        $s = input()['session'] ?? null;
        if (!is_array($s)) fail(422, 'Bad session');
        $id = (string)($s['id'] ?? '');
        $track = (string)($s['track'] ?? '');
        $mode = (string)($s['mode'] ?? '');
        if (!preg_match('/^[A-Za-z0-9_-]{3,40}$/', $id) || !preg_match('/^[a-z0-9-]{1,40}$/', $track) || !in_array($mode, ['practice', 'mock'], true)) fail(422, 'Bad session');
        $json = json_encode($s, JSON_UNESCAPED_UNICODE);
        if (strlen($json) > MAX_SESSION_BYTES) fail(413, 'Session is too large');
        $n = max(0, (int)($s['n'] ?? 0));
        $c = max(0, min($n, (int)($s['c'] ?? 0)));
        $pdo->prepare('INSERT IGNORE INTO test_prep_sessions (user_id, session_id, track, mode, questions, correct, duration_ms, started_ms, session_json)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)')
            ->execute([$uid, $id, $track, $mode, $n, $c, max(0, (int)($s['ms'] ?? 0)), max(0, (int)($s['ts'] ?? 0)), $json]);
        reply(200, ['ok' => true]);

    default:
        fail(400, 'Unknown action');
    }
} catch (Throwable $e) {
    error_log('SpaceBook test prep: ' . $e->getMessage());
    fail(500, 'Could not save your test progress');
}
