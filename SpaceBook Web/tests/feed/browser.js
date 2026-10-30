'use strict';
/* The News Feed on the Home page in a real browser (the installed Chrome through Playwright) against the real PHP API and a scratch MySQL database:
 *     node --max-old-space-size=4096 tests/feed/browser.js [--out <folder for screenshots>]
 * A student signs in (session cookie), opens Home, finds the News Feed first and open, reads posts of other students (shown as "Ali K." and nothing
 * else), likes, comments and replies, shares, posts a question and a My Stats card made from this browser's own records, reports (three reports hide
 * a post), deletes, scrolls for more, filters, goes offline and signed out, and the page fits a phone. Local only (CI has no browser). Dev-only. */
const fs = require('fs'), os = require('os'), path = require('path');
const { spawn, spawnSync } = require('child_process');
const { launch } = require('../baseline/lib');

const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_feed_shots'));
fs.mkdirSync(OUT, { recursive: true });
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const PHP = [process.env.PHP, 'php', 'C:/xampp/php/php.exe'].filter(Boolean).find(p => spawnSync(p, ['-v']).status === 0);

(async () => {
  if (!PHP) { console.log('SKIP  no PHP found'); return; }
  const cfg = path.join(os.tmpdir(), 'sb_feed_browser_config_' + process.pid + '.php');
  const mk = spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'create', cfg], { encoding: 'utf8' });
  if (mk.status !== 0) { console.log('FAIL  cannot create the scratch database: ' + (mk.stderr || mk.stdout)); process.exit(1); }
  const port = 19800 + (process.pid % 150);
  const base = 'http://127.0.0.1:' + port + '/';
  const server = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', ROOT], { env: Object.assign({}, process.env, { SB_CONFIG: cfg }), stdio: 'ignore' });
  for (let i = 0; i < 80; i++) { try { await fetch(base + 'api/health.php'); break; } catch (e) { await sleep(100); } }

  const api = async (p, body, headers) => {
    const res = await fetch(base + p, { method: body === undefined ? 'GET' : 'POST', headers: Object.assign({ 'Content-Type': 'application/json' }, headers || {}), body: body === undefined ? undefined : JSON.stringify(body) });
    const sc = (res.headers.getSetCookie ? res.headers.getSetCookie() : []).map(c => c.split(';')[0]).find(c => c.startsWith('spacebook_sid='));
    return { status: res.status, json: await res.json().catch(() => null), cookie: sc || null };
  };
  let n = 0;
  const account = async (name, type) => {
    n++;
    const r = await api('api/auth.php?action=register', { name, father_name: 'Secretfather', user_type: type || 'student', whatsapp: '92300' + String(7000000 + n * 17 + process.pid % 13), password: 'secret123', want_device: true, device_name: 'node' });
    if (!r.json || !r.json.ok) throw new Error('register failed ' + JSON.stringify(r));
    // sign-up makes one general account (the plan is chosen when buying) and ignores user_type: a teacher is made by setting the type in the scratch database
    if (type && type !== 'student' && r.json.user.user_type !== type) {
      const set = spawnSync(PHP, ['-r', '$p = new PDO("mysql:host=" . (getenv("SB_TEST_DB_HOST") ?: "127.0.0.1") . ";dbname=spacebook_test_e2e;charset=utf8mb4", getenv("SB_TEST_DB_USER") ?: "root", getenv("SB_TEST_DB_PASS") !== false ? getenv("SB_TEST_DB_PASS") : ""); $p->prepare("UPDATE users SET user_type = ? WHERE id = ?")->execute([$argv[1], (int)$argv[2]]);', type, String(r.json.user.id)], { encoding: 'utf8' });
      if (set.status !== 0) throw new Error('cannot make a ' + type + ' account: ' + (set.stderr || set.stdout));
      r.json.user.user_type = type;
    }
    return { token: r.json.device.token, cookie: r.cookie, user: r.json.user, auth: { Authorization: 'Bearer ' + r.json.device.token } };
  };
  const post = (acct, action, body) => api('api/feed.php?action=' + action, body, acct.auth);

  const me = await account('Ayesha Khan');
  const ali = await account('Ali Khan');
  const sara = await account('Sara Bibi Yousafzai');
  const teacher = await account('Mrs Nasreen', 'teacher');
  const posts = {};
  // 40 older posts, from four other students (a student may post 12 an hour); the four below are the newest
  for (let k = 0; k < 4; k++) {
    const other = await account('Filler Student ' + k);
    for (let i = 1; i <= 10; i++) await post(other, 'create', { kind: 'text', body: 'Filler post ' + i + ' of student ' + k + ' in the long feed, with a few more words so it is not shown big.' });
  }

  posts.tip = (await post(teacher, 'create', { kind: 'text', body: 'Exam tip: read the question twice before you start writing. Good luck, everyone!' })).json.post.id;
  posts.q = (await post(sara, 'create', { kind: 'question', body: 'What is the chemical formula of water, and why is it polar?', card: { subject: 'Chemistry', cls: 'Class 9', chapter: 'Unit 4' } })).json.post.id;
  posts.xss = (await post(ali, 'create', { kind: 'text', body: '<img src=x onerror="window.__xss=1"> <script>window.__xss=2</script> five <b>bold</b>' })).json.post.id;
  posts.stats = (await post(ali, 'create', { kind: 'stats', body: 'My week', card: { questions: 340, accuracy: 82, minutes: 410, streak: 7, sessions: 18, words: 126, plans: 2, tests: [{ title: 'PST', mcqs: 220, acc: 85 }] } })).json.post.id;
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 }, serviceWorkers: 'block' });
  await ctx.addCookies([{ name: 'spacebook_sid', value: me.cookie.split('=')[1], url: base }]);
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::/.test(m.text())) errors.push('console: ' + m.text()); });
  page.on('dialog', d => d.accept());
  const shot = async name => { try { await page.screenshot({ path: path.join(OUT, name + '.png') }); } catch (e) { /* page busy */ } };
  const feedCall = (action, body) => page.evaluate(async ([a, b]) => (await fetch('api/feed.php?action=' + a, b ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(b), credentials: 'same-origin' } : { credentials: 'same-origin' })).json(), [action, body]);
  const art = id => page.locator('article[data-id="' + id + '"]');
  // the page draws its list again after every change, so a check must cope with the moment when there is nothing there
  const liked = (id, v) => page.waitForFunction(([i, want]) => { const b = document.querySelector('article[data-id="' + i + '"] [data-a="like"]'); return !!b && b.getAttribute('aria-pressed') === want; }, [id, v]);

  // ---- the page opens on the News Feed
  await page.goto(base + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.waitForFunction(() => window.SBFeed && window.SpaceBookAuth && typeof renderHome === 'function', null, { timeout: 60000 });
  await page.evaluate(() => { localStorage.removeItem('sbHomeStatsTab'); });
  await page.waitForFunction(() => window.SpaceBookAuth.user, null, { timeout: 15000 });
  await page.evaluate(() => document.querySelector('.nav-tab[data-page="home"]').click());
  await page.waitForSelector('#homeFeed:not([hidden]) article[data-id]', { timeout: 20000 });
  const tabs = await page.$$eval('.hcb-tab', els => els.map(e => ({ page: e.dataset.homeTab, on: e.classList.contains('active'), sel: e.getAttribute('aria-selected') })));
  check('Home has the News Feed as its first tab and it is open', tabs[0].page === 'feed' && tabs[0].on && tabs[0].sel === 'true' && tabs.slice(1).every(t => !t.on), tabs);
  check('the other tabs are still there (My Stats, Project Stats)', tabs.map(t => t.page).slice(1).join() === 'mine,project' || tabs.map(t => t.page).slice(1).join() === 'mine,project,account', tabs);
  check('the statistics panels are hidden behind it', await page.evaluate(() => document.getElementById('homeMyStats').hidden && document.getElementById('homeProjectStats').hidden));
  await shot('01-feed-open');

  // ---- what is shown
  const text = await page.evaluate(() => document.getElementById('homeFeed').innerText);
  check('the composer and the four quick buttons are there', /What's on your mind\?/.test(text) && /Question/.test(text) && /My Stats/.test(text) && /Today/.test(text) && /Study plan/.test(text));
  check('other students are shown as first name and initial only', /Ali K\./.test(text) && /Sara Y\./.test(text) && /Mrs N\./.test(text) && !/Khan|Yousafzai|Nasreen|Secretfather/.test(text), text.slice(0, 300));
  check('no phone number or father name anywhere on the page', !(await page.content()).includes(ali.user.whatsapp) && !(await page.content()).includes('Secretfather'));
  check('a teacher has the tick', await art(posts.tip).locator('.sbfd-tick').count() === 1);
  check('a question has its badge and its tags', await art(posts.q).locator('.sbfd-qb').count() === 1 && /Chemistry/.test(await art(posts.q).innerText()) && /Class 9/.test(await art(posts.q).innerText()));
  check('the stats card shows the numbers', /340/.test(await art(posts.stats).innerText()) && /82%/.test(await art(posts.stats).innerText()) && /PST/.test(await art(posts.stats).innerText()));
  check('markup in a post is shown as words and never runs', await page.evaluate(() => !window.__xss && !document.querySelector('#homeFeed img[src="x"]')) && /<img src=x/.test(await art(posts.xss).innerText()));
  check('the first page has 20 posts', (await page.locator('#homeFeed article[data-id]').count()) === 20);

  // ---- like
  await art(posts.q).locator('[data-a="like"]').click();
  await liked(posts.q, 'true');
  check('a like turns the button on and the server has it', (await feedCall('post&id=' + posts.q)).post.likes === 1 && (await feedCall('post&id=' + posts.q)).post.liked === true);
  await art(posts.q).locator('[data-a="like"]').click();
  await liked(posts.q, 'false');
  check('a second tap takes it back', (await feedCall('post&id=' + posts.q)).post.likes === 0);
  await art(posts.q).locator('[data-a="like"]').click();
  await liked(posts.q, 'true');

  // ---- comment and reply
  await art(posts.q).locator('[data-a="comments"]').first().click();
  await page.waitForSelector('article[data-id="' + posts.q + '"] .sbfd-in textarea');
  await art(posts.q).locator('.sbfd-in textarea').fill('I think it is H2O, because oxygen pulls the electrons.');
  await art(posts.q).locator('[data-a="csend"]').click();
  await page.waitForSelector('article[data-id="' + posts.q + '"] .sbfd-c');
  check('a comment appears under the post and the post counts it', /H2O/.test(await art(posts.q).locator('.sbfd-c').first().innerText()) && /1 comment/.test(await art(posts.q).locator('.sbfd-counts').innerText()));
  const cid = await art(posts.q).locator('.sbfd-c').first().getAttribute('data-cid');
  await post(teacher, 'comment', { post: posts.q, body: 'Well done!', parent: +cid });
  await art(posts.q).locator('.sbfd-c [data-a="creply"]').first().click();
  await art(posts.q).locator('.sbfd-in textarea').fill('Thank you madam');
  await art(posts.q).locator('[data-a="csend"]').click();
  await page.waitForFunction(id => document.querySelectorAll('article[data-id="' + id + '"] .sbfd-c.r').length >= 1, posts.q);
  const comments = await feedCall('comments&post=' + posts.q);
  check('a reply sits under its comment on the server too', comments.comments.length === 1 && comments.comments[0].replies.length >= 1 && comments.comments[0].replies.some(r => r.body === 'Thank you madam'), comments);
  await shot('02-comments');

  // ---- share
  await art(posts.tip).locator('[data-a="share"]').click();
  await page.waitForSelector('.sbfd-dlg textarea');
  await page.fill('.sbfd-dlg textarea', 'So true!');
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => /So true!/.test(((document.querySelector('#homeFeed article[data-id]') || {}).innerText || '')));
  const first = await page.locator('#homeFeed article[data-id]').first().innerText();
  check('a share goes on top with the original inside', /shared a post/.test(first) && /Exam tip/.test(first) && /So true!/.test(first), first.slice(0, 200));
  check('the original counts the share', /1 share/.test(await art(posts.tip).innerText()));

  // ---- the composer: a question, and a My Stats card made from this browser's own records
  await page.click('.sbfd-quick [data-k="question"]');
  await page.waitForSelector('.sbfd-dlg textarea');
  await page.fill('.sbfd-dlg textarea', 'How do I remember the parts of the brain?');
  await page.selectOption('.sbfd-dlg [data-cls]', { index: 1 }).catch(() => {});
  await page.fill('.sbfd-dlg [data-subj]', 'Biology');
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => /How do I remember the parts of the brain\?/.test(((document.querySelector('#homeFeed article[data-id]') || {}).innerText || '')));
  const qPost = (await feedCall('list&limit=5')).posts[0];
  check('a question is posted with its tag and shown first', qPost.kind === 'question' && qPost.card && qPost.card.subject === 'Biology' && qPost.mine === true, qPost);

  await page.click('.sbfd-quick [data-k="stats"]');
  await page.waitForSelector('.sbfd-dlg');
  check('with nothing studied yet the My Stats card cannot be sent', /nothing to show yet/.test(await page.innerText('.sbfd-dlg')) && await page.isDisabled('.sbfd-dlg [data-go]'));
  await page.click('.sbfd-dlg .sbfd-x');
  await page.evaluate(uid => {
    const d = n => { const t = new Date(Date.now() - n * 86400000); return t.getFullYear() + '-' + String(t.getMonth() + 1).padStart(2, '0') + '-' + String(t.getDate()).padStart(2, '0'); };
    localStorage.setItem('sbTP:v1:' + uid, JSON.stringify({ v: 1, updatedAt: Date.now(), sessions: [{ id: 'a', track: 'pst', mode: 'practice', ts: Date.now() - 3600000, n: 20, c: 15, ms: 600000 }], days: { pst: { [d(1)]: [1200000, 30, 25], [d(0)]: [900000, 20, 15] }, all: { [d(1)]: [1200000, 30, 25], [d(0)]: [900000, 20, 15] } } }));
  }, me.user.id);
  await page.click('.sbfd-quick [data-k="stats"]');
  await page.waitForSelector('.sbfd-dlg .sbfd-attach');
  check('with records the My Stats card is previewed with the real numbers', /50/.test(await page.innerText('.sbfd-dlg .sbfd-attach')) && /80%/.test(await page.innerText('.sbfd-dlg .sbfd-attach')));
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => document.querySelector('#homeFeed article[data-id] .sbfd-attach'));
  const sPost = (await feedCall('list&limit=5')).posts[0];
  check('the stats post is stored with the card', sPost.kind === 'stats' && sPost.card.questions === 50 && sPost.card.accuracy === 80 && sPost.card.tests[0].title === 'PST', sPost);
  await page.click('.sbfd-quick [data-k="progress"]');
  await page.waitForSelector('.sbfd-dlg .sbfd-ring');
  check("today's card shows the day's 20 questions", /20\/20/.test(await page.innerText('.sbfd-dlg .sbfd-attach')));
  await page.click('.sbfd-dlg .sbfd-x');

  await page.click('.sbfd-pill');
  await page.waitForSelector('.sbfd-dlg textarea');
  await page.fill('.sbfd-dlg textarea', 'mail me at bob@example.com');
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => /e-mail/.test((document.querySelector('.sbfd-dlg [data-e]') || {}).textContent || ''));
  check('an e-mail address is refused with the reason and the dialog stays open', await page.locator('.sbfd-dlg').count() === 1);
  await shot('03-composer-error');
  await page.click('.sbfd-dlg .sbfd-x');

  // ---- report (three students hide a post), delete
  await art(posts.xss).locator('[data-a="menu"]').click();
  await art(posts.xss).locator('[data-m="rep"]').click();
  await page.waitForSelector('.sbfd-dlg input[name="sbfd-reason"]');
  await page.check('.sbfd-dlg input[value="spam"]');
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => /Thank you/.test((document.querySelector('.sbfd-toast') || {}).textContent || ''));
  check('a report is thanked and one report does not hide', (await feedCall('post&id=' + posts.xss)).ok === true);
  await post(sara, 'report', { type: 'post', id: posts.xss, reason: 'spam' });
  const hid = await post(teacher, 'report', { type: 'post', id: posts.xss, reason: 'unkind' });
  check('three students hide the post', hid.json.hidden === true && (await feedCall('post&id=' + posts.xss)).ok === false);

  const mine = (await feedCall('list&mine=1&limit=3')).posts[0].id;
  await art(mine).locator('[data-a="menu"]').click();
  await art(mine).locator('[data-m="del"]').click();
  await page.waitForFunction(id => !document.querySelector('article[data-id="' + id + '"]'), mine);
  check('deleting my post removes it for everyone', (await feedCall('post&id=' + mine)).ok === false);

  // ---- more posts as the page is scrolled, and the filter
  await page.evaluate(() => document.querySelector('[data-sentinel]').scrollIntoView());
  await page.waitForFunction(() => document.querySelectorAll('#homeFeed article[data-id]').length > 20, null, { timeout: 15000 });
  const count1 = await page.locator('#homeFeed article[data-id]').count();
  check('scrolling to the end loads the next page', count1 > 20 && count1 <= 40, count1);
  for (let i = 0; i < 4; i++) { await page.evaluate(() => { const s = document.querySelector('[data-sentinel]'); if (s) s.scrollIntoView(); }); await sleep(600); }
  const ids = await page.$$eval('#homeFeed article[data-id]', els => els.map(e => +e.dataset.id));
  check('every post once, newest first, and the end is announced', new Set(ids).size === ids.length && ids.every((v, i) => i === 0 || ids[i - 1] > v) && /caught up/.test(await page.innerText('#homeFeed')), ids.length);
  await page.click('[data-f="question"]');
  await page.waitForFunction(() => [...document.querySelectorAll('#homeFeed article[data-id]')].every(a => a.querySelector('.sbfd-qb')) && document.querySelectorAll('#homeFeed article[data-id]').length >= 1);
  check('the Questions filter shows only questions', (await page.locator('#homeFeed article[data-id]').count()) >= 2);
  await page.click('[data-f="all"]');
  await page.waitForFunction(() => document.querySelectorAll('#homeFeed article[data-id]').length >= 10);

  // ---- tabs, offline, signed out
  await page.evaluate(() => switchHomeStatsTab('project'));
  check('another tab hides the feed', await page.evaluate(() => document.getElementById('homeFeed').hidden));
  await page.evaluate(() => switchHomeStatsTab('feed'));
  check('and the feed comes back', await page.evaluate(() => !document.getElementById('homeFeed').hidden && document.querySelectorAll('#homeFeed article[data-id]').length > 0));
  await ctx.setOffline(true);
  await page.click('[data-a="refresh"]');
  await page.waitForSelector('.sbfd-off');
  check('offline: the posts stay and a note says they are saved', (await page.locator('#homeFeed article[data-id]').count()) > 0 && /offline/.test(await page.innerText('.sbfd-off')));
  await page.click('.sbfd-pill'); await page.waitForSelector('.sbfd-dlg textarea');
  await page.fill('.sbfd-dlg textarea', 'posting while offline');
  await page.click('.sbfd-dlg [data-go]');
  await page.waitForFunction(() => /offline/.test((document.querySelector('.sbfd-dlg [data-e]') || {}).textContent || ''));
  check('offline: a post is refused with a clear reason and the dialog stays', /offline/.test(await page.innerText('.sbfd-dlg [data-e]')) && await page.locator('.sbfd-dlg').count() === 1);
  await page.click('.sbfd-dlg .sbfd-x');
  await ctx.setOffline(false);
  await page.click('[data-a="refresh"]');
  await page.waitForFunction(() => !document.querySelector('.sbfd-off'));

  await page.setViewportSize({ width: 390, height: 844 });
  await sleep(300);
  const fit = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth }));
  check('on a phone the page fits the width', fit.sw <= fit.iw + 1, fit);
  await shot('04-phone');
  await page.setViewportSize({ width: 1100, height: 900 });

  await ctx.clearCookies();
  await page.evaluate(() => { document.dispatchEvent(new CustomEvent('spacebook:auth', { detail: { user: null } })); });
  await page.waitForSelector('#homeFeed [data-a="login"]');
  check('signed out: the feed asks to sign in, shows no posts and keeps nothing of the account', (await page.locator('#homeFeed article[data-id]').count()) === 0 && await page.evaluate(() => !Object.keys(localStorage).some(k => k.indexOf('sbFeedCache:') === 0)));
  await shot('05-signed-out');

  check('no script errors on the page', errors.length === 0, errors);

  await browser.close();
  try { server.kill(); } catch (e) { /* gone */ }
  spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'drop']);
  try { fs.unlinkSync(cfg); } catch (e) { /* gone */ }
  console.log('---\nfeed browser: ' + pass + ' passed, ' + fail + ' failed  (screenshots in ' + OUT + ')');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
