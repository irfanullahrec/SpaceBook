<?php
// News feed tests (migration 008, api/feed.php, api/lib/feed.php, the News Feed page of api/admin.php, export and purge).
// Included by tests/php/run.php after the user-items tests: it uses that file's check(), http(), reg(), fresh_user(), user_id_of(),
// reset_limits(), test_pdo(), $api, $port and the running test server. admin_tests.php (included after this file) defines http_form(), cli()
// and csrf_of(); this file is therefore included after admin_tests.php.

echo "--- news feed ---\n";

function fd_get(?string $token, string $query, ?string $jar = null): array
{
    return http('GET', 'feed.php?' . $query, null, $token ? ['Authorization: Bearer ' . $token] : [], $jar);
}
function fd_post(?string $token, string $action, array $body, array $extra = [], ?string $jar = null): array
{
    return http('POST', 'feed.php?action=' . $action, $body, array_merge($token ? ['Authorization: Bearer ' . $token] : [], $extra), $jar);
}
// a student with a chosen name: ['token','id','jar','num']
function fd_user(string $name = 'Test User', string $type = 'student'): array
{
    reset_limits();
    $r = reg(['name' => $name, 'father_name' => 'Secretfather', 'user_type' => $type, 'want_device' => true]);
    return ['token' => $r['json']['device']['token'], 'id' => user_id_of($r['num']), 'jar' => $r['jar'], 'num' => $r['num']];
}
function fd_post_text(array $u, string $body, string $kind = 'text', $card = null): array
{
    global $fd_keep_limits;
    if (empty($fd_keep_limits)) reset_limits();       // most checks are about the text, not about the hourly limit
    return fd_post($u['token'], 'create', ['kind' => $kind, 'body' => $body, 'card' => $card]);
}
function fd_ids(array $json): array { return array_map(function ($p) { return $p['id']; }, $json['posts']); }

$ali = fd_user('Ali Khan');
$sara = fd_user('Sara Bibi Yousafzai');
$tea = fd_user('Mrs Nasreen', 'teacher');
$sch = fd_user('Government High School Mingora', 'school');

// ---- who may read and write
$x = fd_get(null, 'action=list');
check('a guest cannot read the feed', $x['code'] === 401 && $x['json']['ok'] === false, $x['body']);
check('a made-up device token cannot read it either', fd_get(str_repeat('0', 64), 'action=list')['code'] === 401);
$x = fd_post(null, 'create', ['kind' => 'text', 'body' => 'hello there']);
check('a guest cannot post', $x['code'] === 401);
$x = fd_get($ali['token'], 'action=list');
check('a signed-in student reads an empty feed', $x['code'] === 200 && $x['json']['ok'] === true && $x['json']['posts'] === [] && $x['json']['next'] === 0, $x['body']);
check('a write by GET is refused', fd_get($ali['token'], 'action=create')['code'] === 405);
check('an unknown action is refused', fd_get($ali['token'], 'action=nope')['code'] === 400);

// ---- a plain post, and what other people may learn about its author
$x = fd_post_text($ali, "My first post\n\nwith two lines");
check('a text post is created', $x['code'] === 201 && $x['json']['ok'] === true && $x['json']['post']['kind'] === 'text' && $x['json']['post']['body'] === "My first post\n\nwith two lines" && $x['json']['post']['mine'] === true && $x['json']['post']['likes'] === 0, $x['body']);
$p1 = $x['json']['post']['id'];
$x = fd_get($sara['token'], 'action=list');
check('another student sees it, not as hers', $x['code'] === 200 && fd_ids($x['json']) === [$p1] && $x['json']['posts'][0]['mine'] === false && $x['json']['posts'][0]['liked'] === false, $x['body']);
$a = $x['json']['posts'][0]['author'];
check('the author is shown as first name and the initial of the last name only', $a['name'] === 'Ali K.' && $a['initial'] === 'A' && $a['type'] === 'student' && is_int($a['hue']) && count($a) === 4, json_encode($a));
check('no number, father name, account id or e-mail is in what another student receives', strpos($x['body'], $ali['num']) === false && stripos($x['body'], 'Secretfather') === false && strpos($x['body'], 'whatsapp') === false && strpos($x['body'], 'user_id') === false && strpos($x['body'], 'Khan') === false, $x['body']);
$x = fd_post_text($sara, 'Sara writes');
check('a three-word name is shown as first name and last initial', fd_get($ali['token'], 'action=post&id=' . $x['json']['post']['id'])['json']['post']['author']['name'] === 'Sara Y.');
check('a teacher is marked as a teacher, a school shows its own name', fd_post_text($tea, 'A tip from the teacher')['json']['post']['author']['type'] === 'teacher' && fd_post_text($sch, 'Exam dates are out soon')['json']['post']['author']['name'] === 'Government High School Mingora');

// ---- text rules
$bad = [
    'empty'             => ['', 'Write something'],
    'one letter'        => ['a', 'Write something'],
    'e-mail address'    => ['write to me at someone@example.com please', 'e-mail'],
    'phone number'      => ['call me on 0300-1234567 tonight', 'phone'],
    'phone with +92'    => ['my number is +92 300 1234567', 'phone'],
    'phone in one run'  => ['03001234567', 'phone'],
    'https link'        => ['see https://example.org/page for this', 'links'],
    'www link'          => ['go to www.example.org now', 'links'],
    'bare domain'       => ['visit freemoney.com today', 'links'],
    'too long'          => [str_repeat('a', 1501), '1500'],
];
foreach ($bad as $label => $b) {
    $x = fd_post_text($ali, $b[0]);
    check("a post is refused: $label", $x['code'] === 422 && $x['json']['ok'] === false && stripos($x['json']['error'], $b[1]) !== false, $x['body']);
}
$x = fd_post_text($ali, "What comes next: 1 2 3 4 5 6 7 8 9 10 11 12?");
check('a list of single digits is not taken for a phone number', $x['code'] === 201, $x['body']);
$x = fd_post_text($ali, 'The answer is 1500 and the page is 33 of chapter 7.');
check('ordinary numbers are fine', $x['code'] === 201, $x['body']);
$x = fd_post_text($ali, 'یہ ایک سوال ہے: پانی کا کیمیائی فارمولا کیا ہے؟ 🙂');
check('Urdu text and an emoji are kept as they are', $x['code'] === 201 && $x['json']['post']['body'] === 'یہ ایک سوال ہے: پانی کا کیمیائی فارمولا کیا ہے؟ 🙂', $x['body']);
$x = fd_post_text($ali, "tricky \u{202e}txt.exe\u{202c} and\x01 control\x00 chars");
check('direction overrides and control characters are removed', $x['code'] === 201 && $x['json']['post']['body'] === 'tricky txt.exe and control chars', json_encode($x['json']['post']['body'] ?? null));
$x = fd_post_text($ali, '<script>alert(1)</script> & "quotes" <b>bold</b>');
check('markup is stored as plain text (the clients escape it when they draw it)', $x['code'] === 201 && $x['json']['post']['body'] === '<script>alert(1)</script> & "quotes" <b>bold</b>', $x['body']);
$x = http('POST', 'feed.php?action=create', null, ['Authorization: Bearer ' . $ali['token'], 'Content-Type: application/json']);
check('a request with no body is a clear error', $x['code'] === 422, $x['body']);
$x = fd_post_text($ali, 'The same words once only');
$y = fd_post_text($ali, 'The same words once only');
check('the same text twice in two minutes is refused (a double tap)', $x['code'] === 201 && $y['code'] === 409, $y['body']);
check('unknown kinds and a card on a text post are refused', fd_post_text($ali, 'hello world', 'video')['code'] === 422 && fd_post_text($ali, 'hello world again', 'text', ['v' => 1, 'questions' => 5])['code'] === 422);

// ---- the cards
$stats = ['questions' => 120, 'accuracy' => 87, 'minutes' => 340, 'streak' => 6, 'sessions' => 9, 'words' => 55, 'plans' => 2,
          'tests' => [['title' => 'PST', 'mcqs' => 80, 'acc' => 90], ['title' => '', 'mcqs' => 5, 'acc' => 5]], 'evil' => '<img src=x onerror=alert(1)>', 'whatsapp' => '923001234567'];
$x = fd_post_text($ali, 'My stats this week', 'stats', $stats);
$card = $x['json']['post']['card'] ?? [];
check('a My Stats card is stored from a whitelist of fields', $x['code'] === 201 && $card['questions'] === 120 && $card['accuracy'] === 87 && $card['streak'] === 6 && count($card['tests']) === 1 && $card['tests'][0]['title'] === 'PST' && !isset($card['evil']) && !isset($card['whatsapp']) && strpos($x['body'], '923001234567') === false, $x['body']);
$x = fd_post_text($ali, 'Over the top', 'stats', ['questions' => 99999999999, 'accuracy' => 400, 'minutes' => -5, 'streak' => 'many']);
check('numbers on a card are clamped into a sane range', $x['code'] === 201 && $x['json']['post']['card']['questions'] === 10000000 && $x['json']['post']['card']['accuracy'] === 100 && $x['json']['post']['card']['minutes'] === 0 && $x['json']['post']['card']['streak'] === 0, $x['body']);
check('a My Stats card with nothing in it is refused', fd_post_text($ali, '', 'stats', ['questions' => 0])['code'] === 422 && fd_post_text($ali, '', 'stats', null)['code'] === 422);
$x = fd_post_text($ali, '', 'progress', ['date' => '2026-10-24', 'questions' => 30, 'correct' => 40, 'minutes' => 25, 'goal' => 20, 'coins' => 12, 'streak' => 3, 'tasksDone' => 5, 'tasksTotal' => 3]);
$card = $x['json']['post']['card'] ?? [];
check('a daily progress card may have no caption; correct and done never pass the totals', $x['code'] === 201 && $x['json']['post']['body'] === '' && $card['date'] === '2026-10-24' && $card['correct'] === 30 && $card['tasksDone'] === 3 && $card['goal'] === 20, $x['body']);
check('a progress card with a made-up date gets today, with nothing studied it is refused', fd_post_text($ali, 'x1', 'progress', ['date' => '2026-13-45', 'questions' => 1])['json']['post']['card']['date'] === gmdate('Y-m-d') && fd_post_text($ali, 'nothing', 'progress', ['questions' => 0, 'minutes' => 0, 'tasksTotal' => 0])['code'] === 422);
$x = fd_post_text($ali, 'My plan for the exams', 'plan', ['name' => 'Class 9 Science', 'label' => 'Class 9 · all subjects', 'subjects' => ['Physics', 'Chemistry', 'Biology'], 'days' => 30, 'tasks' => 90, 'done' => 45, 'pct' => 99]);
$card = $x['json']['post']['card'] ?? [];
check('a plan card computes the percentage itself', $x['code'] === 201 && $card['name'] === 'Class 9 Science' && $card['pct'] === 50 && $card['subjects'] === ['Physics', 'Chemistry', 'Biology'] && $card['done'] === 45, $x['body']);
check('a plan card needs a name', fd_post_text($ali, 'plan', 'plan', ['tasks' => 4])['code'] === 422);
$x = fd_post_text($sara, 'What is the formula of water?', 'question', ['subject' => 'Chemistry', 'cls' => 'Class 9', 'chapter' => 'Unit 1']);
check('a question post may carry subject, class and chapter', $x['code'] === 201 && $x['json']['post']['card']['subject'] === 'Chemistry' && $x['json']['post']['card']['cls'] === 'Class 9', $x['body']);
$qid = $x['json']['post']['id'];
$x = fd_post_text($sara, 'A question with no tags at all?', 'question');
check('and may carry nothing', $x['code'] === 201 && $x['json']['post']['card'] === null, $x['body']);
check('a question needs text', fd_post_text($sara, '', 'question')['code'] === 422);

// ---- the list: newest first, pages, own posts
$x = fd_get($sara['token'], 'action=list&limit=5');
$first = $x['json'];
check('the newest post comes first and a full page says where the next starts', $x['code'] === 200 && count($first['posts']) === 5 && $first['next'] === $first['posts'][4]['id'] && $first['posts'][0]['id'] > $first['posts'][1]['id'], $x['body']);
$seen = fd_ids($first);
$next = $first['next'];
for ($i = 0; $i < 30 && $next > 0; $i++) {
    $pg = fd_get($sara['token'], 'action=list&limit=5&before=' . $next)['json'];
    $seen = array_merge($seen, fd_ids($pg));
    $next = $pg['next'];
}
$total = (int)test_pdo()->query("SELECT COUNT(*) FROM feed_posts WHERE status = 'visible'")->fetchColumn();
check('paging by `before` reaches every visible post once, newest first, and ends with next = 0', count($seen) === $total && count(array_unique($seen)) === $total && $next === 0 && $seen[count($seen) - 1] === $p1, count($seen) . ' of ' . $total);
$sorted = $seen; rsort($sorted);
check('the pages are in descending order', $sorted === $seen);
$mine = fd_get($ali['token'], 'action=list&mine=1&limit=50')['json']['posts'];
check('mine=1 lists only the student\'s own posts', count($mine) > 3 && count(array_filter($mine, function ($p) { return !$p['mine']; })) === 0);
check('the page size is limited to 50', count(fd_get($sara['token'], 'action=list&limit=500')['json']['posts']) <= 50);
check('a single post can be fetched, a missing one is a 404', fd_get($sara['token'], 'action=post&id=' . $p1)['json']['post']['id'] === $p1 && fd_get($sara['token'], 'action=post&id=999999')['code'] === 404);

// ---- likes
$x = fd_post($sara['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => true]);
check('a like counts', $x['code'] === 200 && $x['json']['likes'] === 1 && $x['json']['liked'] === true, $x['body']);
$x = fd_post($sara['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => true]);
check('liking twice counts once', $x['json']['likes'] === 1);
$x = fd_post($ali['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => true]);
check('a second student makes it two, and the post shows who liked it for each viewer', $x['json']['likes'] === 2 && fd_get($sara['token'], 'action=post&id=' . $p1)['json']['post']['liked'] === true && fd_get($tea['token'], 'action=post&id=' . $p1)['json']['post']['liked'] === false);
$x = fd_post($sara['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => false]);
check('an unlike takes it back, twice is harmless', $x['json']['likes'] === 1 && $x['json']['liked'] === false && fd_post($sara['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => false])['json']['likes'] === 1);
check('liking a post that is not there is a 404', fd_post($sara['token'], 'like', ['type' => 'post', 'id' => 999999, 'on' => true])['code'] === 404);
check('the like count on the row matches the likes table', (int)test_pdo()->query("SELECT like_count FROM feed_posts WHERE id = $p1")->fetchColumn() === (int)test_pdo()->query("SELECT COUNT(*) FROM feed_post_likes WHERE post_id = $p1")->fetchColumn());

// ---- comments and replies
$x = fd_post($sara['token'], 'comment', ['post' => $qid, 'body' => 'I think it is H2O']);
check('a comment is created and counted', $x['code'] === 201 && $x['json']['comment']['body'] === 'I think it is H2O' && $x['json']['comment']['mine'] === true && $x['json']['count'] === 1 && $x['json']['comment']['parent'] === 0, $x['body']);
$c1 = $x['json']['comment']['id'];
$x = fd_post($ali['token'], 'comment', ['post' => $qid, 'body' => 'Yes, two hydrogen and one oxygen', 'parent' => $c1]);
$r1 = $x['json']['comment']['id'];
check('a reply sits under its comment', $x['code'] === 201 && $x['json']['comment']['parent'] === $c1 && $x['json']['count'] === 2, $x['body']);
$x = fd_post($tea['token'], 'comment', ['post' => $qid, 'body' => 'Well done both', 'parent' => $r1]);
check('a reply to a reply goes under the same comment', $x['code'] === 201 && $x['json']['comment']['parent'] === $c1 && $x['json']['count'] === 3, $x['body']);
$x = fd_post($tea['token'], 'comment', ['post' => $qid, 'body' => 'A second top comment']);
$c2 = $x['json']['comment']['id'];
$x = fd_get($ali['token'], 'action=comments&post=' . $qid);
$cm = $x['json']['comments'] ?? [];
check('comments come newest first, each with its replies oldest first', $x['code'] === 200 && count($cm) === 2 && $cm[0]['id'] === $c2 && $cm[1]['id'] === $c1 && count($cm[1]['replies']) === 2 && $cm[1]['replies'][0]['id'] === $r1 && $cm[0]['replies'] === [] && $x['json']['next'] === 0, $x['body']);
check('the comment authors are shown by display name only', $cm[1]['author']['name'] === 'Sara Y.' && strpos($x['body'], $sara['num']) === false);
check('the post shows the comment count', fd_get($ali['token'], 'action=post&id=' . $qid)['json']['post']['comments'] === 4);
$x = fd_post($ali['token'], 'like', ['type' => 'comment', 'id' => $c1, 'on' => true]);
check('a comment can be liked', $x['code'] === 200 && $x['json']['likes'] === 1 && fd_get($ali['token'], 'action=comments&post=' . $qid)['json']['comments'][1]['liked'] === true);
check('a comment is screened like a post', fd_post($ali['token'], 'comment', ['post' => $qid, 'body' => 'mail me bob@example.com'])['code'] === 422 && fd_post($ali['token'], 'comment', ['post' => $qid, 'body' => ''])['code'] === 422 && fd_post($ali['token'], 'comment', ['post' => $qid, 'body' => str_repeat('b', 501)])['code'] === 422);
check('a comment on a post that is not there, or a reply to a comment of another post, is refused', fd_post($ali['token'], 'comment', ['post' => 999999, 'body' => 'hello'])['code'] === 404 && fd_post($ali['token'], 'comment', ['post' => $p1, 'body' => 'hello again', 'parent' => $c1])['code'] === 404);
check('the same comment twice in two minutes is refused', fd_post($ali['token'], 'comment', ['post' => $qid, 'body' => 'Yes, two hydrogen and one oxygen'])['code'] === 409);
for ($i = 0; $i < 22; $i++) { reset_limits(); fd_post($tea['token'], 'comment', ['post' => $p1, 'body' => "page filler number $i"]); }
$pg1 = fd_get($ali['token'], 'action=comments&post=' . $p1)['json'];
$pg2 = fd_get($ali['token'], 'action=comments&post=' . $p1 . '&before=' . $pg1['next'])['json'];
check('comments are paged: 20 and then the rest', count($pg1['comments']) === 20 && $pg1['next'] > 0 && count($pg2['comments']) === 2 && $pg2['next'] === 0);
// delete
check('another student cannot delete a comment', fd_post($ali['token'], 'comment_delete', ['id' => $c2])['code'] === 404);
$x = fd_post($sara['token'], 'comment_delete', ['id' => $c1]);
check('deleting a comment removes its replies and lowers the count by all of them', $x['code'] === 200 && $x['json']['count'] === 1 && count(fd_get($ali['token'], 'action=comments&post=' . $qid)['json']['comments']) === 1 && fd_get($ali['token'], 'action=post&id=' . $qid)['json']['post']['comments'] === 1);
check('a deleted comment cannot be deleted again', fd_post($sara['token'], 'comment_delete', ['id' => $c1])['code'] === 404);

// ---- counts stay right with ten or more comments (a text comparison would get 13 - 3 wrong)
$cnp = fd_user('Count Poster'); $cnc = fd_user('Count Commenter');
$cnpost = fd_post_text($cnp, 'A post with many comments')['json']['post']['id'];
$cnfirst = 0;
for ($i = 1; $i <= 11; $i++) { $r = fd_post($cnc['token'], 'comment', ['post' => $cnpost, 'body' => "many comments $i"]); if ($i === 1) $cnfirst = $r['json']['comment']['id']; }
fd_post($cnc['token'], 'comment', ['post' => $cnpost, 'body' => 'reply one', 'parent' => $cnfirst]);
fd_post($cnc['token'], 'comment', ['post' => $cnpost, 'body' => 'reply two', 'parent' => $cnfirst]);
check('13 comments are counted as 13', fd_get($cnp['token'], 'action=post&id=' . $cnpost)['json']['post']['comments'] === 13);
$x = fd_post($cnc['token'], 'comment_delete', ['id' => $cnfirst]);
check('deleting a comment with two replies lowers a two-digit count by exactly three', $x['code'] === 200 && $x['json']['count'] === 10 && fd_get($cnp['token'], 'action=post&id=' . $cnpost)['json']['post']['comments'] === 10, $x['body']);

// ---- shares
$x = fd_post($sara['token'], 'share', ['id' => $p1, 'body' => 'Good one!']);
$s1 = $x['json']['post']['id'] ?? 0;
check('a share is a post that carries the original and counts on it', $x['code'] === 201 && $x['json']['post']['kind'] === 'share' && $x['json']['post']['body'] === 'Good one!' && $x['json']['post']['shared']['id'] === $p1 && $x['json']['post']['shared']['author']['name'] === 'Ali K.' && $x['json']['shares'] === 1, $x['body']);
$x = fd_post($tea['token'], 'share', ['id' => $s1]);
check('a share of a share points at the original', $x['code'] === 201 && $x['json']['post']['shared']['id'] === $p1 && $x['json']['shares'] === 2, $x['body']);
$s2 = $x['json']['post']['id'];
check('the original shows its share count, and a share has none of its own', fd_get($ali['token'], 'action=post&id=' . $p1)['json']['post']['shares'] === 2 && fd_get($ali['token'], 'action=post&id=' . $s1)['json']['post']['shares'] === 0);
check('a share may have no text; a link in its text is refused; a post that is not there cannot be shared', fd_post($sch['token'], 'share', ['id' => $p1])['code'] === 201 && fd_post($sch['token'], 'share', ['id' => $p1, 'body' => 'see www.example.org'])['code'] === 422 && fd_post($sch['token'], 'share', ['id' => 999999])['code'] === 404);
$x = fd_post($tea['token'], 'delete', ['id' => $s2]);
check('deleting a share lowers the count on the original', $x['code'] === 200 && fd_get($ali['token'], 'action=post&id=' . $p1)['json']['post']['shares'] === 2);   // 3 shares made, 1 deleted
// delete
check('another student cannot delete a post', fd_post($sara['token'], 'delete', ['id' => $p1])['code'] === 404 && fd_get($ali['token'], 'action=post&id=' . $p1)['code'] === 200);
$x = fd_post($ali['token'], 'delete', ['id' => $p1]);
check('the author deletes their post', $x['code'] === 200 && fd_get($sara['token'], 'action=post&id=' . $p1)['code'] === 404 && !in_array($p1, fd_ids(fd_get($sara['token'], 'action=list&limit=50')['json']), true));
$l = fd_get($sara['token'], 'action=list&limit=50')['json']['posts'];
$sharePost = null; foreach ($l as $p) if ($p['id'] === $s1) $sharePost = $p;
check('a share of a deleted post stays and says the original is gone', $sharePost !== null && $sharePost['shared'] === null, json_encode($sharePost));
check('a deleted post cannot be shared, liked or commented on', fd_post($tea['token'], 'share', ['id' => $p1])['code'] === 404 && fd_post($tea['token'], 'like', ['type' => 'post', 'id' => $p1, 'on' => true])['code'] === 404 && fd_post($tea['token'], 'comment', ['post' => $p1, 'body' => 'late reply'])['code'] === 404 && fd_get($tea['token'], 'action=comments&post=' . $p1)['code'] === 404);
check('a post cannot be deleted twice', fd_post($ali['token'], 'delete', ['id' => $p1])['code'] === 404);

// ---- reports and hiding
$rp = fd_user('Bad Poster');
$r1u = fd_user('Reporter One'); $r2u = fd_user('Reporter Two'); $r3u = fd_user('Reporter Three');
$x = fd_post_text($rp, 'This post will be reported by three students');
$rid = $x['json']['post']['id'];
check('a reason from the list is needed', fd_post($r1u['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'because'])['code'] === 422 && fd_post($r1u['token'], 'report', ['type' => 'post', 'id' => $rid])['code'] === 422);
check('your own post cannot be reported', fd_post($rp['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'spam'])['code'] === 422);
check('a post that is not there cannot be reported', fd_post($r1u['token'], 'report', ['type' => 'post', 'id' => 999999, 'reason' => 'spam'])['code'] === 404);
$x = fd_post($r1u['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'unkind', 'note' => 'it was mean']);
check('a report is taken, one report does not hide', $x['code'] === 200 && $x['json']['hidden'] === false && fd_get($ali['token'], 'action=post&id=' . $rid)['code'] === 200, $x['body']);
$x = fd_post($r1u['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'spam']);
check('the same student reporting again changes nothing', $x['code'] === 200 && $x['json']['hidden'] === false && (int)test_pdo()->query("SELECT report_count FROM feed_posts WHERE id = $rid")->fetchColumn() === 1 && (int)test_pdo()->query("SELECT COUNT(*) FROM feed_reports WHERE target_id = $rid")->fetchColumn() === 1);
fd_post($r2u['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'personal']);
$x = fd_post($r3u['token'], 'report', ['type' => 'post', 'id' => $rid, 'reason' => 'spam']);
check('three different students hide the post at once', $x['code'] === 200 && $x['json']['hidden'] === true && fd_get($ali['token'], 'action=post&id=' . $rid)['code'] === 404 && !in_array($rid, fd_ids(fd_get($ali['token'], 'action=list&limit=50')['json']), true) && (string)test_pdo()->query("SELECT status FROM feed_posts WHERE id = $rid")->fetchColumn() === 'hidden');
$cp = fd_post_text($ali, 'A post with a comment that gets reported');
$cpid = $cp['json']['post']['id'];
$cc = fd_post($rp['token'], 'comment', ['post' => $cpid, 'body' => 'a rude comment'])['json']['comment']['id'];
foreach ([$r1u, $r2u, $r3u] as $r) fd_post($r['token'], 'report', ['type' => 'comment', 'id' => $cc, 'reason' => 'unkind']);
check('three reports hide a comment too', count(fd_get($ali['token'], 'action=comments&post=' . $cpid)['json']['comments']) === 0 && (string)test_pdo()->query("SELECT status FROM feed_comments WHERE id = $cc")->fetchColumn() === 'hidden');

// ---- the administrator's page
reset_limits();
$adm = reg(['name' => 'Feed Admin']);
$admId = user_id_of($adm['num']);
$c = cli('make-admin 0' . substr($adm['num'], 2));
check('an administrator is made on the command line', $c['rc'] === 0, json_encode($c));
check('an ordinary student gets the plain 404 on the feed page', admin_page('?v=feed', $r1u['jar'])['code'] === 404);
$x = admin_page('?v=feed', $adm['jar']);
check('the administrator sees the reported post and comment, with the reasons', $x['code'] === 200 && strpos($x['body'], 'This post will be reported by three students') !== false && strpos($x['body'], 'a rude comment') !== false && strpos($x['body'], 'unkind') !== false && strpos($x['body'], 'Restore') !== false, substr(strip_tags($x['body']), 0, 500));
check('the page has no inline script', strpos($x['body'], '<script') === false);
$tok = csrf_of($x['body']);
$y = http_form('admin.php', ['action' => 'feed_set', 'type' => 'p', 'id' => $rid, 'to' => 'visible', 'csrf' => 'wrong'], [], $adm['jar']);
check('a restore with a wrong csrf token is refused', $y['code'] === 403 && (string)test_pdo()->query("SELECT status FROM feed_posts WHERE id = $rid")->fetchColumn() === 'hidden');
$y = http_form('admin.php', ['action' => 'feed_set', 'type' => 'p', 'id' => $rid, 'to' => 'visible', 'csrf' => $tok], [], $adm['jar']);
check('restoring a post puts it back and clears its reports', $y['code'] === 303 && fd_get($ali['token'], 'action=post&id=' . $rid)['code'] === 200 && (int)test_pdo()->query("SELECT report_count FROM feed_posts WHERE id = $rid")->fetchColumn() === 0 && (int)test_pdo()->query("SELECT COUNT(*) FROM feed_reports WHERE target_id = $rid AND target_type = 'p'")->fetchColumn() === 0);
check('the restore is in the audit log', (int)test_pdo()->query("SELECT COUNT(*) FROM audit_log WHERE action = 'feed_restore' AND detail LIKE 'by:$admId post $rid'")->fetchColumn() === 1);
$y = http_form('admin.php', ['action' => 'feed_set', 'type' => 'c', 'id' => $cc, 'to' => 'removed', 'csrf' => $tok], [], $adm['jar']);
check('removing a comment keeps it hidden for good', $y['code'] === 303 && (string)test_pdo()->query("SELECT status FROM feed_comments WHERE id = $cc")->fetchColumn() === 'removed');
check('a student cannot use the admin form', http_form('admin.php', ['action' => 'feed_set', 'type' => 'p', 'id' => $rid, 'to' => 'removed', 'csrf' => $tok], [], $r1u['jar'])['code'] === 404 && (string)test_pdo()->query("SELECT status FROM feed_posts WHERE id = $rid")->fetchColumn() === 'visible');
$xp = fd_user('Mallory Script');
$xx = fd_post_text($xp, '<img src=x onerror=alert(1)> <script>alert(2)</script>');
foreach ([$r1u, $r2u, $r3u] as $r) fd_post($r['token'], 'report', ['type' => 'post', 'id' => $xx['json']['post']['id'], 'reason' => 'spam']);
$x = admin_page('?v=feed', $adm['jar']);
check('the administrator page escapes what students wrote', strpos($x['body'], '<img src=x') === false && strpos($x['body'], '&lt;img src=x') !== false && strpos($x['body'], '<script>alert(2)') === false);

// ---- blocked accounts, the browser session, limits
$bp = fd_user('Blocked Person');
$bpost = fd_post_text($bp, 'Posted before the account was blocked')['json']['post']['id'];
test_pdo()->exec("UPDATE users SET status = 'blocked' WHERE id = {$bp['id']}");
check('the posts of a blocked account leave the feed', fd_get($ali['token'], 'action=post&id=' . $bpost)['code'] === 404 && !in_array($bpost, fd_ids(fd_get($ali['token'], 'action=list&limit=50')['json']), true));
check('and a blocked account can neither read nor post', fd_get($bp['token'], 'action=list')['code'] === 401 && fd_post_text($bp, 'still here?')['code'] === 401 && fd_get(null, 'action=list', $bp['jar'])['code'] === 401);
test_pdo()->exec("UPDATE users SET status = 'active' WHERE id = {$bp['id']}");

$w = fd_user('Web Browser');
$x = fd_get(null, 'action=list', $w['jar']);
check('the website reads with its session cookie', $x['code'] === 200 && $x['json']['ok'] === true, $x['body']);
$x = fd_post(null, 'create', ['kind' => 'text', 'body' => 'Posted from the browser'], [], $w['jar']);
check('and posts with it', $x['code'] === 201 && $x['json']['post']['mine'] === true, $x['body']);
$x = fd_post(null, 'create', ['kind' => 'text', 'body' => 'Posted from another site'], ['Origin: http://evil.example'], $w['jar']);
check('a post from a foreign Origin is refused (the session cookie alone is not enough)', $x['code'] === 403, $x['body']);
$x = fd_post(null, 'like', ['type' => 'post', 'id' => $rid, 'on' => true], ['Sec-Fetch-Site: cross-site'], $w['jar']);
check('so is a like from a cross-site page', $x['code'] === 403);

$lim = fd_user('Busy Poster');
$fd_keep_limits = true;
$codes = [];
for ($i = 1; $i <= 14; $i++) $codes[] = fd_post_text($lim, "Post number $i of the rate limit test")['code'];
check('12 posts an hour, then 429 with Retry-After', array_slice($codes, 0, 12) === array_fill(0, 12, 201) && $codes[12] === 429 && $codes[13] === 429, json_encode($codes));
$x = fd_post_text($lim, 'One more');
$fd_keep_limits = false;
check('the limit message tells the student what to do', $x['code'] === 429 && strpos($x['json']['error'], 'Try again') !== false && stripos($x['head'], 'Retry-After:') !== false, $x['head'] . $x['body']);
check('reading is not blocked by the posting limit', fd_get($lim['token'], 'action=list')['code'] === 200);
$lim2 = fd_user('Many Likes');
$codes = [];
for ($i = 0; $i < 3; $i++) $codes[] = fd_post($lim2['token'], 'like', ['type' => 'post', 'id' => $rid, 'on' => $i % 2 === 0])['code'];
check('likes toggle freely under the hourly limit', $codes === [200, 200, 200]);
$cl = fd_user('Many Comments');
$codes = [];
for ($i = 1; $i <= 62; $i++) $codes[] = fd_post($cl['token'], 'comment', ['post' => $rid, 'body' => "comment $i for the limit"])['code'];
check('60 comments an hour, then 429', array_slice($codes, 0, 60) === array_fill(0, 60, 201) && $codes[60] === 429, json_encode(array_count_values($codes)));

// ---- export and purge
$ex = http('GET', 'auth.php?action=export', null, [], $w['jar']);
check('the account export holds the student\'s own posts and not other people\'s', $ex['code'] === 200 && count($ex['json']['feed']['posts']) === 1 && $ex['json']['feed']['posts'][0]['body'] === 'Posted from the browser' && strpos($ex['body'], 'Reporter One') === false, substr($ex['body'], 0, 200));
$pu = fd_user('Purge Me');
$pp = fd_post_text($pu, 'This will be purged with its owner')['json']['post']['id'];
fd_post($ali['token'], 'comment', ['post' => $pp, 'body' => 'A comment from someone else on the purged post']);
fd_post($ali['token'], 'like', ['type' => 'post', 'id' => $pp, 'on' => true]);
fd_post($pu['token'], 'comment', ['post' => $rid, 'body' => 'A comment by the account to be purged']);
fd_post($sara['token'], 'share', ['id' => $pp, 'body' => 'sharing the soon gone post']);
require_once $api . '/lib/account.php';
sb_purge_user(test_pdo(), $pu['id']);
$t = test_pdo();
check('purging an account removes its posts, comments and likes', (int)$t->query("SELECT COUNT(*) FROM feed_posts WHERE user_id = {$pu['id']}")->fetchColumn() === 0 && (int)$t->query("SELECT COUNT(*) FROM feed_comments WHERE user_id = {$pu['id']} OR post_id = $pp")->fetchColumn() === 0 && (int)$t->query("SELECT COUNT(*) FROM feed_post_likes WHERE post_id = $pp")->fetchColumn() === 0);
$l = fd_get($ali['token'], 'action=list&limit=50')['json']['posts'];
$orphan = null; foreach ($l as $p) if ($p['kind'] === 'share' && $p['body'] === 'sharing the soon gone post') $orphan = $p;
check('a share of a purged post survives and says the original is gone', $orphan !== null && $orphan['shared'] === null);
check('the feed still works after the purge', fd_get($ali['token'], 'action=list')['code'] === 200);

// ---- the golden file both platforms read (tests/parity/feed_contract.json): the real answers have exactly these fields
$contract = json_decode(file_get_contents($root . '/tests/parity/feed_contract.json'), true);
function ks($a) { $k = array_keys($a); sort($k); return $k; }
$cu = fd_user('Contract Person');
$cv = fd_user('Contract Viewer');
$k1 = fd_post_text($cu, 'A post for the contract check')['json']['post'];
$ks_stats = fd_post_text($cu, 'stats', 'stats', $contract['cards']['stats'])['json']['post'];
$ks_prog = fd_post_text($cu, 'prog', 'progress', $contract['cards']['progress'])['json']['post'];
$ks_plan = fd_post_text($cu, 'plan', 'plan', $contract['cards']['plan'])['json']['post'];
$ks_q = fd_post_text($cu, 'A question for the contract check?', 'question', $contract['cards']['question'])['json']['post'];
$sh = fd_post($cv['token'], 'share', array_merge($contract['requests']['share'], ['id' => $k1['id']]));
$cm = fd_post($cv['token'], 'comment', ['post' => $k1['id'], 'body' => 'top comment for the contract']);
$rp = fd_post($cu['token'], 'comment', ['post' => $k1['id'], 'body' => 'reply for the contract', 'parent' => $cm['json']['comment']['id']]);
$lst = fd_get($cv['token'], 'action=list&limit=50');
$cl = fd_get($cv['token'], 'action=comments&post=' . $k1['id']);
$lk = fd_post($cv['token'], 'like', array_merge($contract['requests']['like'], ['id' => $k1['id']]));
check('contract: a post has the fields of the golden post', ks($k1) === ks($contract['post']) && ks($k1['author']) === ks($contract['author']), json_encode(ks($k1)));
check('contract: a share also carries the original with the golden fields', ks($sh['json']['post']) === ks($contract['share']) && ks($sh['json']['post']['shared']) === ks($contract['share']['shared']), json_encode(ks($sh['json']['post'])));
check('contract: the four cards have the golden fields', ks($ks_stats['card']) === ks($contract['cards']['stats']) && ks($ks_prog['card']) === ks($contract['cards']['progress']) && ks($ks_plan['card']) === ks($contract['cards']['plan']) && ks($ks_q['card']) === ks($contract['cards']['question']) && ks($ks_stats['card']['tests'][0]) === ks($contract['cards']['stats']['tests'][0]), json_encode([ks($ks_stats['card']), ks($ks_plan['card'])]));
check('contract: comments and replies have the golden fields', ks($cl['json']['comments'][0]) === ks($contract['comment']) && ks($cl['json']['comments'][0]['replies'][0]) === ks($contract['comment']['replies'][0]), json_encode(ks($cl['json']['comments'][0])));
check('contract: the answers of every action have the golden fields', ks($lst['json']) === ks($contract['answers']['list'] + ['posts' => 1]) && ks($cl['json']) === ks($contract['answers']['comments'] + ['comments' => 1]) && ks($lk['json']) === ks($contract['answers']['like'])
    && ks($cm['json']) === ks($contract['answers']['comment'] + ['comment' => 1]) && ks($sh['json']) === ks($contract['answers']['share'] + ['post' => 1]) && ks(fd_post($cu['token'], 'create', ['kind' => 'text', 'body' => 'one more post for the contract'])['json']) === ks($contract['answers']['create'] + ['post' => 1])
    && ks(fd_post($cu['token'], 'comment_delete', ['id' => $rp['json']['comment']['id']])['json']) === ks($contract['answers']['commentDelete']) && ks(fd_post($cu['token'], 'delete', ['id' => $k1['id']])['json']) === ks($contract['answers']['delete'])
    && ks(fd_post($cv['token'], 'report', array_merge($contract['requests']['report'], ['type' => 'post', 'id' => $ks_q['id']]))['json']) === ks($contract['answers']['report']) && ks(fd_post_text($cu, 'see https://x.org')['json']) === ks($contract['answers']['error']));
check('contract: reasons and limits are the ones the server uses', $contract['reasons'] === SB_FEED_REASONS && $contract['limits'] === ['post' => SB_FEED_POST_MAX, 'comment' => SB_FEED_COMMENT_MAX, 'share' => SB_FEED_SHARE_MAX, 'page' => SB_FEED_PAGE, 'hideAfterReports' => SB_FEED_HIDE_AT]);
$qs = fd_get($cv['token'], 'action=list&kind=question&limit=50')['json']['posts'];
check('the Questions filter lists only questions', count($qs) >= 2 && count(array_filter($qs, function ($p) { return $p['kind'] !== 'question'; })) === 0);
