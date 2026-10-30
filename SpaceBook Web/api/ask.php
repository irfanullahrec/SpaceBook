<?php
// "Ask SpaceBook" AI answers.
//   POST api/ask.php  {q, history:[{q,a}], sources:[{t, w}]}  → {ok, answer}
// The browser first searches the books on the device (sb_tutor.js) and sends the best passages and the books' own
// written answers as `sources`; the model may use only those. The Groq key lives in api/config.php (gitignored,
// 'groq_key') and never reaches the browser. Without a key, or offline, Ask still answers from the books alone.

require __DIR__ . '/db.php';
require __DIR__ . '/lib/security.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const ASK_MODEL       = 'openai/gpt-oss-120b';
const ASK_MAX_SOURCES = 8;
const ASK_MAX_SRC_LEN = 1400;

function ask_reply(int $code, array $body): void
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function ask_clip($s, int $n): string
{
    $s = trim((string)$s);
    return function_exists('mb_substr') ? mb_substr($s, 0, $n, 'UTF-8') : substr($s, 0, $n);
}

if (($_GET['action'] ?? '') === 'ping') {
    $c = [];
    try { $c = db_config(); } catch (Throwable $e) { /* no config */ }
    ask_reply(200, ['ok' => true, 'ai' => (string)(getenv('GROQ_API_KEY') ?: ($c['groq_key'] ?? '')) !== '']);
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') ask_reply(405, ['ok' => false, 'error' => 'POST required']);
if (!sb_request_is_same_site()) ask_reply(403, ['ok' => false, 'error' => 'Request not allowed']);

$cfg = [];
try { $cfg = db_config(); } catch (Throwable $e) { /* no config: handled below */ }
$key = (string)(getenv('GROQ_API_KEY') ?: ($cfg['groq_key'] ?? ''));
if ($key === '') ask_reply(503, ['ok' => false, 'error' => 'AI is not set up on this server']);

$in = json_decode(file_get_contents('php://input') ?: '', true);
if (!is_array($in)) ask_reply(400, ['ok' => false, 'error' => 'Bad request']);
$q = ask_clip($in['q'] ?? '', 600);
if ($q === '') ask_reply(400, ['ok' => false, 'error' => 'Ask a question']);

// a fair limit per visitor, so one person cannot spend the whole key
try {
    $hit = sb_rate_hit(db(), 'ask:' . sb_client_ip(), 80, 600);
    if (!$hit['ok']) ask_reply(429, ['ok' => false, 'error' => 'Too many questions: try again in ' . $hit['retry'] . ' seconds', 'retry' => $hit['retry']]);
} catch (Throwable $e) {
    error_log('SpaceBook ask limit: ' . $e->getMessage());
}

function ask_groq(string $key, array $payload): ?array
{
    $ch = curl_init('https://api.groq.com/openai/v1/chat/completions');
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
        CURLOPT_HTTPHEADER => ['Content-Type: application/json', 'Authorization: Bearer ' . $key],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 6,
        CURLOPT_TIMEOUT => 25,
    ]);
    $raw = curl_exec($ch);
    $code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $err = curl_error($ch);
    curl_close($ch);
    if ($raw === false || $code !== 200) {
        error_log('SpaceBook ask: Groq HTTP ' . $code . ' ' . $err . ' ' . substr((string)$raw, 0, 200));
        return null;
    }
    $j = json_decode($raw, true);
    return is_array($j) ? $j : null;
}

// action=understand: mend the spelling of the question and say which exercise / question of a book it points to
if (($_GET['action'] ?? '') === 'understand') {
    $sys = "You read a student's message to a school study assistant. Reply with JSON only: {\"kind\": one of \"chat\" (greetings, thanks, feelings, agreeing or disagreeing, praise, small talk, anything needing no book), \"followup\" (refers to the previous answer: why, explain more, next one, again, show steps) or \"study\" (a new school question), \"fixed\": the message with spelling mistakes mended (same language, same meaning, keep numbers and maths), \"cls\": class number 1-12 or 0, \"subject\": subject name in English or \"\", \"exercise\": exercise number like \"3.5\" or \"Review 3\" or \"\", \"q\": question number as text or \"\"}. Do not answer the message.";
    $j = ask_groq($key, ['model' => ASK_MODEL, 'messages' => [['role' => 'system', 'content' => $sys], ['role' => 'user', 'content' => $q]],
        'temperature' => 0, 'reasoning_effort' => 'low', 'max_completion_tokens' => 600, 'response_format' => ['type' => 'json_object']]);
    $u = $j ? json_decode((string)($j['choices'][0]['message']['content'] ?? ''), true) : null;
    if (!is_array($u)) ask_reply(502, ['ok' => false, 'error' => 'The AI could not read that']);
    $kind = in_array($u['kind'] ?? '', ['chat', 'followup', 'study'], true) ? $u['kind'] : 'study';
    ask_reply(200, ['ok' => true, 'kind' => $kind, 'fixed' => ask_clip($u['fixed'] ?? $q, 600), 'cls' => (int)($u['cls'] ?? 0), 'subject' => ask_clip($u['subject'] ?? '', 60),
        'exercise' => ask_clip($u['exercise'] ?? '', 20), 'q' => ask_clip($u['q'] ?? '', 6)]);
}

$ctx = '';
$n = 0;
foreach ((array)($in['sources'] ?? []) as $s) {
    if (!is_array($s) || $n >= ASK_MAX_SOURCES) continue;
    $t = ask_clip($s['t'] ?? '', ASK_MAX_SRC_LEN);
    if ($t === '') continue;
    $n++;
    $ctx .= '[' . $n . '] (' . ask_clip($s['w'] ?? '', 160) . ")\n" . $t . "\n\n";
}

$system = "You are SpaceBook AI, a warm, clever study friend for students of Classes 1 to 12 of the Khyber Pakhtunkhwa Textbook Board. Talk like a kind, patient human teacher chatting with the student, not like a search engine.\n"
    . "Personality: friendly, encouraging, natural; short replies for chat (one to three sentences), and use the earlier messages: remember what the student said, their name if they gave it, what you just explained. React to what they say (\"Great, glad it helped!\"), ask one small follow-up question or offer a next step (a similar question, a quick quiz, a simpler explanation). Use a few emojis sparingly.\n"
    . "Language: mirror the student's exact writing: English gets English; Roman Urdu (Urdu in Latin letters, e.g. 'mujhe samajh nahi aya') gets Roman Urdu in Latin letters, never Urdu script; Urdu script gets Urdu script; Pashto and Arabic likewise.\n"
    . "Chat and feelings: answer freely and kindly. If they say something is correct, wrong or confusing, respond to that and help.\n"
    . "Study content (facts, definitions, exercises, calculations): use ONLY the textbook SOURCES below or what you already explained in this chat. A source may hold the book's own question with its answer and steps: explain it clearly, show steps for a calculation, correct any slip. Mention the source numbers like [1]. If the sources do not contain the answer to a study question, say honestly, in a friendly way, that the books you have do not cover it, and suggest how to ask it (class, subject, chapter); do not guess or use outside knowledge for facts.\n"
    . "Format: short plain lines; write every formula inside single dollar signs like \$x^2+1\$ (never \[ \] or \( \)); no headings, no tables; **bold** is allowed.\n\n"
    . "SOURCES:\n" . ($ctx !== '' ? $ctx : "(none for this message)\n");

$messages = [['role' => 'system', 'content' => $system]];
foreach (array_slice((array)($in['history'] ?? []), -6) as $h) {
    if (!is_array($h)) continue;
    $hq = ask_clip($h['q'] ?? '', 300);
    $ha = ask_clip($h['a'] ?? '', 700);
    if ($hq !== '' && $ha !== '') { $messages[] = ['role' => 'user', 'content' => $hq]; $messages[] = ['role' => 'assistant', 'content' => $ha]; }
}
$messages[] = ['role' => 'user', 'content' => $q];

$j = ask_groq($key, ['model' => ASK_MODEL, 'messages' => $messages, 'temperature' => 0.5, 'reasoning_effort' => 'low', 'max_completion_tokens' => 2000]);
if ($j === null) ask_reply(502, ['ok' => false, 'error' => 'The AI could not answer now']);
$answer = trim((string)($j['choices'][0]['message']['content'] ?? ''));
if ($answer === '') ask_reply(502, ['ok' => false, 'error' => 'The AI gave no answer']);
ask_reply(200, ['ok' => true, 'answer' => $answer, 'sources' => $n]);
