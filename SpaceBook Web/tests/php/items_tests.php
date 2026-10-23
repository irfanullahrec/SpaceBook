<?php
// User items tests (migration 007, api/lib/items.php, item.put / item.del in api/v2/sync.php, the `items` of the pull, export and purge).
// Included by tests/php/run.php after the account tests: it uses that file's check(), http(), sync_post(), pull(), ev(), fresh_user(),
// test_pdo() and the running test server.

echo "--- user items (bookmarks, notes, positions ...) ---\n";

function put(string $kind, string $key, array $value, ?int $at = null): array
{
    $p = ['kind' => $kind, 'key' => $key, 'value' => $value];
    if ($at !== null) $p['at'] = $at;
    return ev('item.put', $p);
}
function del(string $kind, string $key, ?int $at = null): array
{
    $p = ['kind' => $kind, 'key' => $key];
    if ($at !== null) $p['at'] = $at;
    return ev('item.del', $p);
}
function bm_value(string $s = 'cls5-math', int $ch = 2, int $p = 3, string $tb = '', string $t = 'Fractions'): array
{
    return ['c' => 'cls5', 's' => $s, 'ch' => $ch, 'p' => $p, 'tb' => $tb, 't' => $t];
}
function bm_key(string $s = 'cls5-math', int $ch = 2, int $p = 3, string $tb = ''): string { return "$s|$ch|$tb|$p"; }
function items_of(array $pullJson, string $kind): array
{
    $out = [];
    foreach ($pullJson['items'] as $it) if ($it['kind'] === $kind) $out[$it['key']] = $it;
    return $out;
}
function rejected_codes(array $resp): array
{
    $c = [];
    foreach ($resp['json']['rejected'] as $r) $c[] = $r['code'];
    return $c;
}

$a = fresh_user();
$now = (int)round(microtime(true) * 1000);

// ---- put, pull, replay
$e1 = put('bm', bm_key(), bm_value(), $now - 5000);
$x = sync_post($a['token'], [$e1]);
check('a bookmark is accepted', $x['code'] === 200 && $x['json']['accepted'] === [$e1['eventId']] && $x['json']['rejected'] === [], $x['body']);
$g = pull($a['token']);
$bms = items_of($g['json'], 'bm');
check('and comes back in the pull with its value and time', isset($bms[bm_key()]) && $bms[bm_key()]['value'] === bm_value() && $bms[bm_key()]['at'] === $now - 5000 && $g['json']['itemsDeleted'] === [], $g['body']);
$cur1 = $g['json']['cursor'];
$x = sync_post($a['token'], [$e1]);
check('the same event again is accepted and changes nothing', $x['json']['accepted'] === [$e1['eventId']] && (int)test_pdo()->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']}")->fetchColumn() === 1 && pull($a['token'], $cur1)['json']['items'] === []);
$x = sync_post($a['token'], [put('bm', bm_key(), bm_value(), $now - 4000)]);
check('the same bookmark saved again (a new event, same value) is no new change for the other devices', pull($a['token'], $cur1)['json']['items'] === [], $x['body']);

// ---- validation
$bad = [
    put('nope', 'k', ['a' => 1]),                                           // unknown kind
    put('bm', 'cls5-math|2||3|x', bm_value()),                              // key shape
    put('bm', bm_key('cls5-math', 2, 4), bm_value('cls5-math', 2, 3)),      // the key must be the place (page 4 vs 3)
    put('bm', bm_key(), ['c' => 'cls5', 's' => 'cls5-math', 'ch' => 2]),    // no page
    put('bm', bm_key(), ['c' => 'CLS 5!', 's' => 'cls5-math', 'ch' => 2, 'p' => 3, 'tb' => '', 't' => 'x']),
    put('note', sb_uuid4(), ['c' => 'cls5', 's' => 'cls5-math', 'ch' => 1, 'p' => 0, 'tb' => '', 't' => 'T', 'x' => '', 'q' => '']),   // neither text nor quote
    put('note', 'not-a-uuid', ['c' => 'cls5', 's' => 'cls5-math', 'ch' => 1, 'p' => 0, 'x' => 'hello']),
    put('pos', 'cls5-math', ['c' => 'cls5', 'ch' => 1, 'p' => 0, 'n' => 100000]),
    put('word', 'xx:hello', ['s' => 'l']),                                  // language
    put('word', 'en:hello', ['s' => 'z']),                                  // mark
    put('gbest', 'not a reward key', ['b' => 0.5]),
    put('pref', 'theme', ['id' => 'dark']),
    put('pref', 'class', ['id' => 'Class Five']),
    put('slo', 'cls9-phy|1|abc', []),
    put('drill', 'cls9-phy|1700000000000', ['n' => 5, 'c' => 9, 'ms' => 1]),   // more correct than asked
    ev('item.put', ['kind' => 'bm', 'key' => bm_key()]),                    // no value
    ev('item.del', ['kind' => 'bm', 'key' => '']),
];
$x = sync_post($a['token'], $bad);
check('malformed items are rejected with a reason and nothing is stored', $x['code'] === 200 && $x['json']['accepted'] === [] && count($x['json']['rejected']) === count($bad)
    && rejected_codes($x) === ['bad_kind', 'bad_key', 'bad_value', 'bad_value', 'bad_value', 'bad_value', 'bad_key', 'bad_value', 'bad_key', 'bad_value', 'bad_value', 'bad_key', 'bad_value', 'bad_key', 'bad_value', 'bad_value', 'bad_key']
    && (int)test_pdo()->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']}")->fetchColumn() === 1, $x['body']);

// ---- the value is whitelisted and trimmed: nothing the client invents is kept
$nid = sb_uuid4();
$long = str_repeat('é', 3000);
$x = sync_post($a['token'], [put('note', $nid, ['c' => 'cls5', 's' => 'cls5-math', 'ch' => 1, 'p' => 0, 'tb' => 'Lessons', 't' => 'T', 'x' => $long, 'q' => 'a quote', 'k' => 'hl', 'evil' => '<script>', 'html' => '<b>'], $now - 3000)]);
$notes = items_of(pull($a['token'])['json'], 'note');
check('a note keeps only its own fields, its text cut at 2000 characters, a highlight stays a highlight', $x['json']['accepted'] !== [] && isset($notes[$nid]) && !isset($notes[$nid]['value']['evil']) && !isset($notes[$nid]['value']['html'])
    && mb_strlen($notes[$nid]['value']['x'], 'UTF-8') === 2000 && $notes[$nid]['value']['k'] === 'hl' && $notes[$nid]['value']['q'] === 'a quote', json_encode(array_keys($notes[$nid]['value'] ?? [])));

// ---- later time wins; a delete is a tombstone that an older save cannot undo
$k = bm_key('cls5-math', 7, 1);
sync_post($a['token'], [put('bm', $k, bm_value('cls5-math', 7, 1, '', 'First'), $now - 2000)]);
sync_post($a['token'], [put('bm', $k, bm_value('cls5-math', 7, 1, '', 'Older'), $now - 3000)]);
check('an older save arriving later is ignored', items_of(pull($a['token'])['json'], 'bm')[$k]['value']['t'] === 'First');
sync_post($a['token'], [put('bm', $k, bm_value('cls5-math', 7, 1, '', 'Newer'), $now - 1000)]);
check('a newer save wins', items_of(pull($a['token'])['json'], 'bm')[$k]['value']['t'] === 'Newer');
$cur = pull($a['token'])['json']['cursor'];
sync_post($a['token'], [del('bm', $k, $now - 500)]);
$g = pull($a['token'], $cur);
check('a delete shows in the next pull as itemsDeleted', $g['json']['items'] === [] && count($g['json']['itemsDeleted']) === 1 && $g['json']['itemsDeleted'][0]['key'] === $k && $g['json']['itemsDeleted'][0]['kind'] === 'bm', $g['body']);
check('and a first sync does not carry the tombstone', !isset(items_of(pull($a['token'])['json'], 'bm')[$k]) && pull($a['token'])['json']['itemsDeleted'] === []);
sync_post($a['token'], [put('bm', $k, bm_value('cls5-math', 7, 1, '', 'Late'), $now - 800)]);
check('a save older than the delete cannot bring it back', !isset(items_of(pull($a['token'])['json'], 'bm')[$k]));
sync_post($a['token'], [put('bm', $k, bm_value('cls5-math', 7, 1, '', 'Again'), $now - 100)]);
check('a save after the delete does', items_of(pull($a['token'])['json'], 'bm')[$k]['value']['t'] === 'Again');
$x = sync_post($a['token'], [del('bm', 'cls5-math|9||9', $now - 100), put('bm', 'cls5-math|9||9', bm_value('cls5-math', 9, 9), $now - 900)]);
check('deleting what never reached the server leaves a tombstone, so a late older save of it is ignored', $x['json']['rejected'] === [] && !isset(items_of(pull($a['token'])['json'], 'bm')['cls5-math|9||9']));
$future = sync_post($a['token'], [put('bm', 'cls5-math|8||8', bm_value('cls5-math', 8, 8), $now + 90 * 86400000)]);
$st = test_pdo()->prepare("SELECT at_ms FROM user_items WHERE user_id = ? AND item_key = 'cls5-math|8||8'");
$st->execute([$a['id']]);
check('a time far in the future is cut to the server clock, so a fast clock cannot win for ever', (int)$st->fetchColumn() <= (int)round(microtime(true) * 1000) + 6000);

// ---- reading position: the later stop wins
sync_post($a['token'], [put('pos', 'cls5-math', ['c' => 'cls5', 'ch' => 4, 'p' => 2, 'tb' => '', 'n' => 9, 't' => 'Decimals'], $now - 2000), put('pos', 'cls5-math', ['c' => 'cls5', 'ch' => 1, 'p' => 0, 'tb' => '', 'n' => 3, 't' => 'Earlier'], $now - 4000)]);
$pos = items_of(pull($a['token'])['json'], 'pos');
check('the position keeps the later stop whatever the order of arrival', $pos['cls5-math']['value']['ch'] === 4 && $pos['cls5-math']['value']['p'] === 2);

// ---- best game run only goes up and cannot be deleted
$gk = 'cls5|g-quiz|u0|count|abc123|10';
sync_post($a['token'], [put('gbest', $gk, ['b' => 0.6]), put('gbest', $gk, ['b' => 0.4]), put('gbest', $gk, ['b' => 1.7])]);
check('a best run only rises (0.6, then 0.4 ignored, 1.7 cut to 1)', items_of(pull($a['token'])['json'], 'gbest')[$gk]['value']['b'] === 1);
$x = sync_post($a['token'], [del('gbest', $gk)]);
check('and cannot be deleted', rejected_codes($x) === ['not_deletable']);

// ---- words: case and accents are different words (binary key), the mark is one of two
sync_post($a['token'], [put('word', 'ur:علم', ['s' => 'l'], $now - 10), put('word', 'ur:عِلم', ['s' => 'k'], $now - 10), put('word', 'en:Apple', ['s' => 'l'], $now - 10), put('word', 'en:apple', ['s' => 'k'], $now - 10)]);
$w = items_of(pull($a['token'])['json'], 'word');
check('words that differ only by case or by a vowel mark are different rows', count($w) === 4 && $w['ur:علم']['value']['s'] === 'l' && $w['ur:عِلم']['value']['s'] === 'k' && $w['en:Apple']['value']['s'] === 'l' && $w['en:apple']['value']['s'] === 'k', json_encode(array_keys($w), JSON_UNESCAPED_UNICODE));

// ---- settings, SLOs, drills
sync_post($a['token'], [put('pref', 'class', ['id' => 'cls7'], $now - 50), put('pref', 'games', ['cls' => 7, 'scope' => ['7|quiz' => 'all'], 'streak' => ['n' => 3, 'last' => '2026-10-22']], $now - 50),
    put('slo', 'cls9-phy|1|0', [], $now - 50), put('drill', 'cls9-phy|1700000000000', ['n' => 10, 'c' => 7, 'ms' => 45000], $now - 50)]);
$g = pull($a['token'])['json'];
$pref = items_of($g, 'pref');
check('class, game settings, a ticked SLO and a drill are kept', $pref['class']['value'] === ['id' => 'cls7'] && $pref['games']['value']['streak']['n'] === 3 && $pref['games']['value']['scope'] === ['7|quiz' => 'all']
    && isset(items_of($g, 'slo')['cls9-phy|1|0']) && items_of($g, 'drill')['cls9-phy|1700000000000']['value'] === ['n' => 10, 'c' => 7, 'ms' => 45000], json_encode($g['items'], JSON_UNESCAPED_UNICODE));
check('an empty value is an object (a ticked SLO reads back as {}, not [])', strpos(http('GET', 'v2/sync.php?since=0', null, ['Authorization: Bearer ' . $a['token']])['body'], '"key":"cls9-phy|1|0","value":{}') !== false);

// ---- caps
$many = [];
for ($i = 0; $i < 400; $i++) $many[] = put('pos', 'sub' . str_pad((string)$i, 4, '0', STR_PAD_LEFT), ['c' => 'cls5', 'ch' => 0, 'p' => 0, 'tb' => '', 'n' => 1, 't' => ''], $now - 20);
$x = sync_post($a['token'], $many);
check('at most 400 reading positions: the 400th new one is refused, the rest are kept', count($x['json']['accepted']) === 399 && rejected_codes($x) === ['item_limit'] && (int)test_pdo()->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']} AND kind = 'pos'")->fetchColumn() === 400, $x['body']);
$x = sync_post($a['token'], [put('pos', 'cls5-math', ['c' => 'cls5', 'ch' => 5, 'p' => 5, 'tb' => '', 'n' => 9, 't' => 'again'], $now)]);
check('an existing position can still be updated at the cap', $x['json']['rejected'] === [] && items_of(pull($a['token'])['json'], 'pos')['cls5-math']['value']['ch'] === 5);

// ---- incremental pull names only what changed
$cur = pull($a['token'])['json']['cursor'];
sync_post($a['token'], [put('word', 'en:river', ['s' => 'l'], $now + 1)]);
$g = pull($a['token'], $cur)['json'];
check('an incremental pull returns only the item that changed', count($g['items']) === 1 && $g['items'][0]['key'] === 'en:river' && $g['itemsDeleted'] === []);

// ---- two devices of one account, and another account
$b = fresh_user();
$login = http('POST', 'auth.php?action=login', ['whatsapp' => $a['num'], 'password' => 'secret123', 'want_device' => true, 'device_name' => 'Second phone']);
$tok2 = $login['json']['device']['token'] ?? '';
check('a second device signs in to the same account', strlen($tok2) === 64 && $tok2 !== $a['token'], $login['body']);
$cursor2 = pull($tok2)['json']['cursor'];
sync_post($a['token'], [put('note', $nid, ['c' => 'cls5', 's' => 'cls5-math', 'ch' => 1, 'p' => 0, 'tb' => 'Lessons', 't' => 'T', 'x' => 'edited on the first phone', 'q' => '', 'k' => 'note'], $now + 5)]);
$seen = items_of(pull($tok2, $cursor2)['json'], 'note');
check('what one device saves, the other pulls', isset($seen[$nid]) && $seen[$nid]['value']['x'] === 'edited on the first phone');
sync_post($tok2, [del('note', $nid, $now + 10)]);
$gd = pull($a['token'], pull($a['token'])['json']['cursor'] - 1)['json'];
check('and a delete on the second reaches the first', array_filter($gd['itemsDeleted'], function ($d) use ($nid) { return $d['key'] === $nid; }) !== []);
check('another account sees none of it', pull($b['token'])['json']['items'] === []);
$x = sync_post($b['token'], [put('bm', bm_key(), bm_value('cls5-math', 2, 3, '', 'Mine'), $now)]);
check('and the same key in another account is its own row', items_of(pull($b['token'])['json'], 'bm')[bm_key()]['value']['t'] === 'Mine' && items_of(pull($a['token'])['json'], 'bm')[bm_key()]['value']['t'] === 'Fractions');

// ---- housekeeping: old tombstones go, recent ones and live items stay
$tt = test_pdo();
$tt->exec("INSERT INTO user_items (user_id, kind, item_key, value_json, at_ms, deleted, rev, updated_ms) VALUES ({$a['id']}, 'bm', 'old|1||1', '{}', 5, 1, 1, " . ((time() - 200 * 86400) * 1000) . "), ({$a['id']}, 'bm', 'new|1||1', '{}', 5, 1, 1, " . ((time() - 10 * 86400) * 1000) . ")");
$before = (int)$tt->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']} AND deleted = 0")->fetchColumn();
$pr = run_php([$api . '/migrate.php', 'prune'], ['SB_CONFIG' => $cfg]);
check('prune removes tombstones older than 180 days only', $pr['code'] === 0 && strpos($pr['out'], 'user_items_deleted=1') !== false
    && (int)$tt->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']} AND item_key = 'old|1||1'")->fetchColumn() === 0
    && (int)$tt->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']} AND item_key = 'new|1||1'")->fetchColumn() === 1
    && (int)$tt->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$a['id']} AND deleted = 0")->fetchColumn() === $before, $pr['out'] . $pr['err']);

// ---- export and the 30-day purge
$ex = http('GET', 'auth.php?action=export', null, [], $a['jar']);
$exItems = isset($ex['json']['saved_items']) ? $ex['json']['saved_items'] : [];
check('the account export lists the saved items', $ex['code'] === 200 && count($exItems) > 400 && in_array('bm', array_column($exItems, 'kind'), true), substr($ex['body'], 0, 200));
check('and not the deleted ones', !array_filter($exItems, function ($i) use ($nid) { return $i['key'] === $nid; }));
$t = test_pdo();
check('rows of a purged account go with it (cascade)', (int)$t->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$b['id']}")->fetchColumn() === 1 && ($t->exec("DELETE FROM users WHERE id = {$b['id']}") >= 0) && (int)$t->query("SELECT COUNT(*) FROM user_items WHERE user_id = {$b['id']}")->fetchColumn() === 0);

// ---- old clients: a pull answer still has everything an old client reads
$g = pull($a['token'])['json'];
check('the pull keeps its old fields (progress, plans, plansDeleted, tp, coins) next to the new ones', isset($g['progress'], $g['plans'], $g['plansDeleted'], $g['tp'], $g['coins'], $g['items'], $g['itemsDeleted']));

// ---- owner flags: the website and the app read the same switch from the server
echo "--- owner flags (api/lib/flags.php) ---\n";
require_once $api . '/lib/flags.php';
$m = http('GET', 'auth.php?action=me');
check('me publishes the flags to a guest: client sync is off by default', $m['code'] === 200 && $m['json']['flags'] === ['syncV2' => false], $m['body']);
check('and to a signed-in student', http('GET', 'auth.php?action=me', null, ['Authorization: Bearer ' . $a['token']])['json']['flags'] === ['syncV2' => false]);
$en = http('GET', 'v2/entitlements.php');
check('entitlements carry the same flags', $en['json']['flags'] === ['syncV2' => false], $en['body']);
$ff = sys_get_temp_dir() . '/sb_flags_' . getmypid() . '.php';
file_put_contents($ff, '<?php return ["syncV2" => true, "somethingElse" => true];');
putenv('SB_FLAGS_FILE=' . $ff);
check('a flags file switches it on and unknown names are ignored', sb_flags() === ['syncV2' => true]);
file_put_contents($ff, '<?php return "not an array";');
check('a broken flags file leaves the default (off)', sb_flags() === ['syncV2' => false]);
file_put_contents($ff, '<?php return ["syncV2" => true];');
$port2 = $port + 1;
$proc2 = proc_open([PHP_BINARY, '-S', "127.0.0.1:$port2", '-t', $api], [0 => ['pipe', 'r'], 1 => ['file', sys_get_temp_dir() . '/sb_php_server2.log', 'w'], 2 => ['file', sys_get_temp_dir() . '/sb_php_server2.log', 'a']], $pipes2, $api, array_merge(getenv(), ['SB_CONFIG' => $cfg, 'SB_FLAGS_FILE' => $ff]));
$up2 = false;
for ($i = 0; $i < 50 && !$up2; $i++) { $s2 = @fsockopen('127.0.0.1', $port2, $en2, $es2, 0.2); if ($s2) { fclose($s2); $up2 = true; } else usleep(100000); }
$ch = curl_init("http://127.0.0.1:$port2/v2/entitlements.php");
curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30]);
$body2 = json_decode((string)curl_exec($ch), true);
curl_close($ch);
check('a server with the flag on tells every client so', $up2 && isset($body2['flags']) && $body2['flags'] === ['syncV2' => true], json_encode($body2));
if (is_resource($proc2)) { proc_terminate($proc2); proc_close($proc2); }
putenv('SB_FLAGS_FILE');
@unlink($ff);
check('with no file the switch is off again', sb_flags() === ['syncV2' => false]);
