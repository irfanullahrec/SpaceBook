'use strict';
/* The plans flow in a real browser (the installed Chrome through Playwright) against the real PHP API on a throwaway database:
 *     node --max-old-space-size=8192 tests/access/browser.js [--out <folder for screenshots>]
 * Anonymous reader meets a locked chapter -> sees the plans -> picks the Student plan and a class -> creates an account (no user type) ->
 * the payment window opens with the Easypaisa details -> Trx ID is required -> one submission (double tap) -> Pending Verification, nothing opens ->
 * an administrator approves (api/lib/billing.php) -> the chapter opens without reloading. Also the free limits of Test Preparation and papers,
 * the Teacher plan's 10-subject cap and the phone-width layout. Needs PHP and MySQL (XAMPP); dev-only, never shipped. */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path'), net = require('net');
const { launch, ROOT } = require('../baseline/lib');

const args = process.argv.slice(2);
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_access_shots'));
fs.mkdirSync(OUT, { recursive: true });
const PHP = process.env.PHP || (fs.existsSync('C:/xampp/php/php.exe') ? 'C:/xampp/php/php.exe' : 'php');
const CFG = path.join(os.tmpdir(), 'sb_access_cfg_' + process.pid + '.php');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const dbq = (...a) => spawnSync(PHP, [path.join(ROOT, 'tests/access/db.php'), ...a], { encoding: 'utf8' });
const rows = sql => JSON.parse(dbq('json', CFG, sql).stdout || '[]');
const freePort = () => new Promise(res => { const s = net.createServer(); s.listen(0, '127.0.0.1', () => { const p = s.address().port; s.close(() => res(p)); }); });

(async () => {
  const init = dbq('init', CFG);
  if (!/ready/.test(init.stdout)) { console.log('FAIL  throwaway database\n' + init.stdout + init.stderr); process.exit(1); }
  const port = await freePort();
  const srv = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', ROOT], { env: Object.assign({}, process.env, { SB_CONFIG: CFG }), stdio: 'ignore' });
  for (let i = 0; i < 60; i++) { const ok = await new Promise(r => { const s = net.connect(port, '127.0.0.1', () => { s.destroy(); r(true); }); s.on('error', () => r(false)); }); if (ok) break; await sleep(150); }
  const url = 'http://127.0.0.1:' + port + '/';
  const browser = await launch();
  const errors = [];
  async function newPage(vp) {
    const ctx = await browser.newContext({ viewport: vp || { width: 1100, height: 900 }, permissions: ['clipboard-read', 'clipboard-write'] });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::|404|403|401|409|422/.test(m.text())) errors.push('console: ' + m.text()); });
    return { ctx, page };
  }
  async function boot(page) {
    await page.goto(url + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
    await page.waitForFunction(() => window.SBAccess && window.SBBilling && window.SpaceBookAuth && typeof openSubject === 'function' && typeof selectSubjectChapter === 'function' && window.SBAccess.state().ok, null, { timeout: 120000 });
    await page.waitForFunction(() => window.SBAccess.state().free && window.SBAccess.visitorId(), null, { timeout: 20000 });
    await sleep(500);
  }
  const shot = async (page, name) => { try { await page.screenshot({ path: path.join(OUT, name + '.png') }); } catch (e) { /* page busy */ } };
  async function step(name, fn) { try { await fn(); } catch (e) { fail++; console.log('FAIL  ' + name + '  -> ' + String(e && e.message).slice(0, 300)); } }

  // ================================================================ 1. an anonymous reader
  const A = await newPage(); const page = A.page;
  await step('boot', async () => { await boot(page); check('the page loads with the access module, the billing window and the account module', true); });
  await step('free chapter / locked chapter', async () => {
    for (let i = 0; i < 4; i++) {                       // the first call can land before the start page has finished drawing
      await page.evaluate(() => { openSubject('cls9', 'cls9-eng'); });
      await sleep(i ? 6000 : 3000);
      if (await page.evaluate(() => !!document.getElementById('subjectTopicArea'))) break;
    }
    await page.waitForSelector('#subjectTopicArea', { state: 'attached', timeout: 60000 });
    await page.evaluate(() => { selectSubjectChapter('eng', 0, 'cls9'); });
    await sleep(1500);
    const ch1 = await page.evaluate(() => ({ lock: !!document.querySelector('.sbx-lock'), len: (document.getElementById('subjectTopicArea') || {}).textContent.length }));
    check('Chapter 1 of an English book opens with no lock', !ch1.lock && ch1.len > 300, ch1);
    const tags = await page.evaluate(() => document.querySelectorAll('.math-ch-btn.sbx-locked').length);
    const total = await page.evaluate(() => document.querySelectorAll('.math-ch-list .math-ch-btn').length);
    check('every later chapter button carries a lock', tags === total - 1 && total > 3, { tags, total });
    await page.evaluate(() => { selectSubjectChapter('eng', 1, 'cls9'); });
    await sleep(700);
    const ch2 = await page.evaluate(() => { const l = document.querySelector('#subjectTopicArea .sbx-lock'); return { lock: !!l, text: l ? l.textContent : '' }; });
    check('Chapter 2 shows the locked panel with a way to buy', ch2.lock && /needs a plan/.test(ch2.text) && /See plans/.test(ch2.text), ch2);
    await shot(page, '01_locked_chapter');
  });
  await step('math chapters', async () => {
    await page.evaluate(() => { openSubject('cls9', 'cls9-math'); });
    await page.waitForSelector('#mathTopicArea', { timeout: 30000 });
    await page.evaluate(() => { selectMathChapter(0); });
    await sleep(700);
    const a = await page.evaluate(() => ({ lock: !!document.querySelector('#mathTopicArea .sbx-lock'), len: document.getElementById('mathTopicArea').textContent.length }));
    await page.evaluate(() => { selectMathChapter(2); });
    await sleep(500);
    const b = await page.evaluate(() => !!document.querySelector('#mathTopicArea .sbx-lock'));
    check('Maths: Chapter 1 opens, Chapter 3 is locked', !a.lock && a.len > 300 && b, { a, b });
  });

  // ================================================================ 2. the plans window
  await step('plans window', async () => {
    await page.evaluate(() => { openSubject('cls9', 'cls9-eng'); });
    await sleep(600);
    await page.evaluate(() => { selectSubjectChapter('eng', 1, 'cls9'); });
    await page.waitForSelector('#subjectTopicArea .sbx-lock [data-sbx="plans"]');
    await page.click('#subjectTopicArea .sbx-lock [data-sbx="plans"]');
    await page.waitForSelector('#sbbModal.sbb-show .sbb-plan', { timeout: 20000 });
    const t = await page.evaluate(() => document.querySelector('#sbbModal').innerText);
    check('three plans, each PKR 500 for 1 month, with includes and restrictions', (t.match(/PKR 500/g) || []).length >= 3 && /Student plan/.test(t) && /Teacher plan/.test(t) && /Test Preparation module/.test(t) && /Paper creation/.test(t) && /up to 10 subjects/i.test(t) && /for 1 month/.test(t), t.slice(0, 500));
    check('the free allowance is listed', /Chapter 1 of every subject/.test(t) && /50 questions in Test Preparation/.test(t) && /Create 1 paper/.test(t) && /50 questions in Study Plan/.test(t));
    await shot(page, '02_plans');
    await page.click('[data-act="choose"][data-plan="student"]');
    await page.waitForSelector('#sbbModal input[name="cls"]');
    const pre = await page.evaluate(() => ({ checked: (document.querySelector('input[name="cls"]:checked') || {}).value, count: document.querySelectorAll('input[name="cls"]').length, cont: document.querySelector('[data-act="continue"]').disabled }));
    check('the Student plan asks for one class, the class being read is already chosen', pre.checked === 'cls9' && pre.count === 12 && pre.cont === false, pre);
    await page.click('[data-act="continue"]');
    await page.waitForSelector('#authModal:not([hidden])', { timeout: 10000 });
    const reg = await page.evaluate(() => { document.querySelector('#authModal [data-tab="register"]').click(); const f = document.querySelector('#authModal form[data-form="register"]'); return { names: Array.from(f.elements).map(e => e.name).filter(Boolean), bill: document.querySelector('#sbbModal').hidden }; });
    check('payment needs an account first; registration has no School / Student / Teacher field', reg.names.join() === 'name,father_name,whatsapp,password' && reg.bill === true, reg);
    await shot(page, '03_register');
  });

  // ================================================================ 3. register, then the payment window with the choice kept
  await step('register and pay', async () => {
    await page.fill('#authModal form[data-form="register"] [name="name"]', 'Browser Tester');
    await page.fill('#authModal form[data-form="register"] [name="father_name"]', 'Father');
    await page.fill('#authModal form[data-form="register"] [name="whatsapp"]', '03001230099');
    await page.fill('#authModal form[data-form="register"] [name="password"]', 'secret123');
    await page.click('#authModal form[data-form="register"] .auth-submit');
    await page.waitForSelector('#sbbModal.sbb-show .sbb-form', { timeout: 30000 });
    const u = rows("SELECT user_type, signup_platform FROM users WHERE whatsapp = '923001230099'");
    check('a general account was made on the website', u.length === 1 && u[0].user_type === 'general' && u[0].signup_platform === 'web', u);
    const t = await page.evaluate(() => document.querySelector('#sbbModal').innerText);
    check('the payment window shows the plan, class, amount, duration and the Easypaisa account', /Student plan/.test(t) && /Class 9/.test(t) && /PKR 500/.test(t) && /1 month/.test(t) && /Easypaisa/.test(t) && /03456896156/.test(t) && /AMIN ALLAH/.test(t) && /Trx ID \(Transaction ID\)/.test(t) && /Submit Payment for Verification/.test(t), t.slice(0, 700));
    check('instructions say to send the amount to that account', /send .*PKR 500.* to the account above/i.test(t));
    await page.evaluate(() => { window.__w = []; });
    const copied = await page.evaluate(async () => { const b = document.querySelectorAll('.sbb-copy'); b[0].click(); await new Promise(r => setTimeout(r, 400)); const first = b[0].textContent; b[1].click(); await new Promise(r => setTimeout(r, 400)); return { n: b.length, first, second: b[1].textContent }; });
    check('both copy buttons work', copied.n === 2 && /Copied/.test(copied.first) && /Copied/.test(copied.second), copied);
    await shot(page, '04_payment');
    await page.click('.sbb-submit');
    await sleep(300);
    const err = await page.evaluate(() => document.querySelector('.sbb-err').textContent);
    check('submitting without a Transaction ID is refused in the window', /Transaction ID/.test(err) && rows('SELECT COUNT(*) c FROM payment_requests')[0].c == 0, err);
    await page.fill('.sbb-form [name="trx"]', 'abc');
    await page.click('.sbb-submit');
    check('a too-short Transaction ID is refused too', /6 to 30/.test(await page.evaluate(() => document.querySelector('.sbb-err').textContent)));
    await page.fill('.sbb-form [name="trx"]', '12345678901');
    await page.evaluate(() => { const b = document.querySelector('.sbb-submit'); b.click(); b.click(); });     // a double tap
    await page.waitForSelector('.sbb-done', { timeout: 30000 });
    const done = await page.evaluate(() => document.querySelector('.sbb-done').innerText);
    check('the thank-you message is shown word for word, as Pending Verification', done.includes('Thank you for choosing SpaceBook! Your payment details have been submitted successfully. Please allow up to 1 hour for verification. Your plan will become active once your payment is approved. Happy learning!') && /Pending Verification/.test(done), done);
    const pay = rows('SELECT * FROM payment_requests');
    check('exactly one request was saved (double tap), pending, with the exact text id and the server price', pay.length === 1 && pay[0].status === 'pending' && pay[0].trx_id === '12345678901' && pay[0].amount_pkr == 500 && pay[0].plan_type === 'student' && pay[0].class_id === 'cls9' && pay[0].platform === 'web', pay);
    check('nothing is subscribed yet', rows('SELECT COUNT(*) c FROM subscriptions')[0].c == 0);
    await shot(page, '05_thanks');
  });
  await step('still locked while pending', async () => {
    await page.click('[data-act="close"]');
    await page.evaluate(async () => { await SBAccess.load(); });
    const s = await page.evaluate(() => ({ pend: SBAccess.state().pendingPayments, read: SBAccess.canRead('cls9', 'cls9-eng', 1) }));
    check('the account shows one pending payment and Chapter 2 is still locked', s.pend === 1 && s.read === false, s);
    await page.evaluate(() => { SBBilling.openAccount(); });
    await page.waitForSelector('#sbbModal .sbb-pay', { timeout: 20000 });
    const t = await page.evaluate(() => document.querySelector('#sbbModal').innerText);
    check('My plans lists the request as Pending Verification with its Transaction ID', /Pending Verification/.test(t) && /12345678901/.test(t) && /up to 1 hour/.test(t), t.slice(0, 400));
    await shot(page, '06_account_pending');
    await page.click('#sbbModal [data-act="close"]');
    await page.reload({ waitUntil: 'domcontentloaded' });
    await boot(page);
    await page.evaluate(() => { openSubject('cls9', 'cls9-eng'); });
    await sleep(500);
    await page.evaluate(() => { selectSubjectChapter('eng', 1, 'cls9'); });
    await sleep(700);
    check('after a reload it is still locked (nothing was unlocked by the browser)', await page.evaluate(() => !!document.querySelector('#subjectTopicArea .sbx-lock')));
  });

  // ================================================================ 4. the administrator approves; the chapter opens
  await step('approval', async () => {
    const id = rows('SELECT id FROM payment_requests')[0].id;
    const r = JSON.parse(dbq('approve', CFG, String(id)).stdout);
    check('the administrator approves the payment', r.ok === true && r.status === 'approved', r);
    await page.evaluate(async () => { await SBAccess.load(); });
    await sleep(300);
    await page.evaluate(() => { selectSubjectChapter('eng', 1, 'cls9'); });
    await sleep(900);
    const o = await page.evaluate(() => ({ lock: !!document.querySelector('#subjectTopicArea .sbx-lock'), len: document.getElementById('subjectTopicArea').textContent.length, tags: document.querySelectorAll('.math-ch-btn.sbx-locked').length }));
    check('Chapter 2 now opens, with no locks left on the buttons', !o.lock && o.len > 300 && o.tags === 0, o);
    await page.evaluate(() => { SBBilling.openAccount(); });
    await page.waitForSelector('#sbbModal .sbb-sub-card', { timeout: 20000 });
    const t = await page.evaluate(() => document.querySelector('#sbbModal').innerText);
    check('My plans shows it Active with the class, start and end dates, days left and a renew button', /Active/.test(t) && /Class 9/.test(t) && /Started/.test(t) && /Ends/.test(t) && /Days left/.test(t) && /Renew early/.test(t) && /Payment approved/.test(t), t.slice(0, 600));
    await shot(page, '07_account_active');
    await page.click('#sbbModal [data-act="close"]');
    const m = rows('SELECT status FROM payment_requests')[0];
    check('the payment record is Approved', m.status === 'approved');
    // a suspension reaches the open page at its next check
    const sid = rows('SELECT id FROM subscriptions')[0].id;
    dbq('suspend', CFG, String(sid));
    await page.evaluate(async () => { await SBAccess.load(); });
    check('a suspension closes the chapters again', await page.evaluate(() => !SBAccess.canRead('cls9', 'cls9-eng', 1)));
    dbq('restore', CFG, String(sid));
    await page.evaluate(async () => { await SBAccess.load(); });
    check('and the restoration opens them again', await page.evaluate(() => SBAccess.canRead('cls9', 'cls9-eng', 1)));
  });

  // ================================================================ 5. free limits for a new visitor
  const B = await newPage(); const p2 = B.page;
  await step('free limits', async () => {
    await boot(p2);
    await sleep(2500);                                  // the service worker may reload the page once after its first install
    await p2.waitForFunction(() => window.SBTestPrep && window.SBAccess && document.readyState === 'complete', null, { timeout: 60000 });
    await p2.evaluate(() => { SBTestPrep.open('pst'); });
    await p2.waitForSelector('.tp-root', { timeout: 60000 });
    await sleep(800);
    await p2.evaluate(() => { SBTestPrep.startPractice(); });
    await p2.waitForSelector('button.tp-opt', { state: 'attached', timeout: 90000 });
    await p2.evaluate(() => { SBTestPrep.answer(0); });
    await sleep(1200);
    const used1 = rows("SELECT COUNT(*) c FROM free_usage WHERE metric = 'prep_q'")[0].c;
    check('the first Test Preparation answer is counted on the server', used1 == 1, used1);
    const vid = await p2.evaluate(() => SBAccess.visitorId());
    const ins = []; for (let i = 0; i < 49; i++) ins.push("('v:" + vid + "','prep_q','fill" + i + "')");
    // top the allowance up to 50 with a direct insert through the helper's own connection
    const php = "putenv('SB_CONFIG=" + CFG.replace(/\\/g, '/') + "'); require '" + ROOT.replace(/\\/g, '/') + "/api/db.php'; db()->exec(\"INSERT IGNORE INTO free_usage (owner_key, metric, item_key) VALUES " + ins.join(',') + "\");";
    const ph = spawnSync(PHP, ['-r', php], { encoding: 'utf8' });
    check('the allowance was topped up to 50 for this visitor', rows("SELECT COUNT(*) c FROM free_usage WHERE metric = 'prep_q' AND owner_key = 'v:" + vid + "'")[0].c == 50, ph.stderr + ph.stdout);
    await p2.evaluate(async () => { SBTestPrep.next(); await new Promise(r => setTimeout(r, 400)); SBTestPrep.answer(0); });
    await p2.waitForSelector('#sbbModal.sbb-show', { timeout: 15000 });
    await p2.waitForSelector('#sbbModal .sbb-plan', { timeout: 30000 });        // the window opens at once, the plans arrive a moment later
    const t = await p2.evaluate(() => document.querySelector('#sbbModal').innerText);
    check('the 51st Test Preparation question opens the purchase window', /used your 50 free Test Preparation questions/.test(t) && /Student plan/.test(t), t.slice(0, 200));
    check('and the answer was not counted past the limit', rows("SELECT COUNT(*) c FROM free_usage WHERE metric = 'prep_q' AND owner_key = 'v:" + vid + "'")[0].c == 50);
    await shot(p2, '08_prep_limit');
    await p2.click('#sbbModal .sbb-x');
    // papers: the first is free, the second is not
    const paper = await p2.evaluate(async () => {
      const a = await SBAccess.useQuestion('paper', 'cls9|cls9-math|annual', { cls: 'cls9', subject: 'cls9-math' });
      paperCreationState.classId = 'cls9'; paperCreationState.subjectId = 'cls9-eng'; paperCreationState.paperType = 'annual';
      jumpToReviewStage();
      await new Promise(r => setTimeout(r, 1500));
      return { first: a.allowed, modal: document.querySelector('#sbbModal').classList.contains('sbb-show'), text: document.querySelector('#sbbModal').innerText.slice(0, 160) };
    });
    check('one paper is free; the second opens the purchase window', paper.first === true && paper.modal === true && /Paper creation|Your free paper/.test(paper.text), paper);
  });

  // ================================================================ 6. the Teacher plan picker, on a phone
  const C = await newPage({ width: 390, height: 780 }); const p3 = C.page;
  await step('teacher plan on a phone', async () => {
    await boot(p3);
    await p3.evaluate(() => { SBBilling.open({}); });
    await p3.waitForSelector('#sbbModal .sbb-plan');
    await p3.click('[data-act="choose"][data-plan="teacher"]');
    await p3.waitForSelector('input[name="subjects"]', { state: 'attached' });
    const r = await p3.evaluate(async () => {
      const boxes = Array.from(document.querySelectorAll('input[name="subjects"]'));
      const out = { total: boxes.length, cont0: document.querySelector('[data-act="continue"]').disabled };
      document.querySelectorAll('.sbb-cls').forEach(d => { d.open = true; });
      let n = 0;
      for (const b of Array.from(document.querySelectorAll('input[name="subjects"]'))) { if (n >= 12) break; if (!b.disabled) { b.checked = true; b.dispatchEvent(new Event('input', { bubbles: true })); n++; } }
      out.checked = document.querySelectorAll('input[name="subjects"]:checked').length;
      out.count = document.querySelector('.sbb-count').textContent;
      out.cont1 = document.querySelector('[data-act="continue"]').disabled;
      const card = document.querySelector('.sbb-card');
      out.overflowX = card.scrollWidth > card.clientWidth + 1 || document.documentElement.scrollWidth > window.innerWidth + 1;
      return out;
    });
    check('Teacher plan: no subject chosen disables Continue; at most 10 can be chosen', r.cont0 === true && r.checked === 10 && /10 of 10/.test(r.count) && r.cont1 === false && r.total > 100, r);
    check('the plans windows fit a phone screen with no sideways scrolling', r.overflowX === false, r);
    await shot(p3, '09_teacher_phone');
  });

  await browser.close();
  srv.kill();
  dbq('drop', CFG);
  try { fs.unlinkSync(CFG); } catch (e) { /* gone */ }
  check('no page errors', errors.length === 0, errors.slice(0, 5));
  console.log('---\nbrowser tests: ' + pass + ' passed, ' + fail + ' failed  (screenshots: ' + OUT + ')');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
