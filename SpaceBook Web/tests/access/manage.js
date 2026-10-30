'use strict';
/* The management page in a REAL browser (the installed Chrome through Playwright), against the real PHP on a throwaway database:
 *     node --max-old-space-size=4096 tests/access/manage.js
 * Why it exists: the curl-based PHP tests send no Origin header, so they passed while every browser form post of the page was refused with
 * "Request not allowed" (the page was sent with Referrer-Policy: no-referrer, which makes a browser send "Origin: null"). Here a person signs in, is shown
 * the dashboard, opens the other pages and signs out, through the page's own forms. Needs PHP and MySQL (XAMPP); dev-only, never shipped. */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path'), net = require('net');
const { launch, ROOT } = require('../baseline/lib');

const PHP = process.env.PHP || (fs.existsSync('C:/xampp/php/php.exe') ? 'C:/xampp/php/php.exe' : 'php');
const CFG = path.join(os.tmpdir(), 'sb_manage_cfg_' + process.pid + '.php');
const PASSWORD = 'Test-' + Math.random().toString(36).slice(2, 10) + '-Pw9x';       // a throwaway database: never the real administrator's password
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const dbq = (...a) => spawnSync(PHP, [path.join(ROOT, 'tests/access/db.php'), ...a], { encoding: 'utf8' });
const freePort = () => new Promise(res => { const s = net.createServer(); s.listen(0, '127.0.0.1', () => { const p = s.address().port; s.close(() => res(p)); }); });
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  if (!/ready/.test(dbq('init', CFG).stdout)) { console.log('FAIL  throwaway database'); process.exit(1); }
  dbq('adminpw', CFG, PASSWORD);
  const port = await freePort();
  const srv = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', ROOT], { env: Object.assign({}, process.env, { SB_CONFIG: CFG }), stdio: 'ignore' });
  for (let i = 0; i < 60; i++) { const ok = await new Promise(r => { const s = net.connect(port, '127.0.0.1', () => { s.destroy(); r(true); }); s.on('error', () => r(false)); }); if (ok) break; await sleep(150); }
  const base = 'http://127.0.0.1:' + port + '/manage/';
  const browser = await launch({ anonymous: true });
  const page = await (await browser.newContext({ viewport: { width: 1100, height: 800 } })).newPage();
  const text = () => page.evaluate(() => document.body.innerText);
  try {
    await page.goto(base, { waitUntil: 'domcontentloaded' });
    check('the sign-in form is shown to a visitor', await page.locator('input[name=password]').count() === 1);

    await page.fill('input[name=username]', 'IrfanUllah123');
    await page.fill('input[name=password]', 'a-wrong-password-1');
    await page.click('button.primary');
    await page.waitForLoadState('domcontentloaded');
    let t = await text();
    check('a wrong password gives the plain wrong-password message, not "Request not allowed"', /Wrong username or password/.test(t) && !/Request not allowed/.test(t), t.slice(0, 120));

    await page.fill('input[name=username]', 'IrfanUllah123');
    await page.fill('input[name=password]', PASSWORD);
    await page.click('button.primary');
    await page.waitForSelector('h1', { timeout: 20000 });
    t = await text();
    check('the right password opens the dashboard', /Dashboard/.test(t) && /Verified revenue/.test(t) && !/Request not allowed/.test(t), t.slice(0, 160));

    for (const [v, word] of [['payments', 'Payments'], ['users', 'Users'], ['subs', 'Subscriptions'], ['extend', 'Free extension'], ['audit', 'Audit trail']]) {
      await page.goto(base + '?v=' + v, { waitUntil: 'domcontentloaded' });
      check('the ' + word + ' page opens', new RegExp(word).test(await text()));
    }

    // a form on a page: the free-extension preview is posted by the page itself
    await page.goto(base + '?v=extend', { waitUntil: 'domcontentloaded' });
    await page.fill('input[name=who]', '1');
    await page.click('button.primary');
    await page.waitForLoadState('domcontentloaded');
    t = await text();
    check('a form of the page (the extension preview) is accepted, not refused', !/Request not allowed/.test(t) && /Free extension/.test(t), t.slice(0, 120));

    await page.goto(base, { waitUntil: 'domcontentloaded' });
    await page.click('header form button');
    await page.waitForLoadState('domcontentloaded');
    check('signing out returns to the sign-in form', await page.locator('input[name=password]').count() === 1);
  } catch (e) {
    check('the page flow completes', false, String(e && e.message));
  }
  await browser.close();
  srv.kill();
  dbq('drop', CFG);
  try { fs.unlinkSync(CFG); } catch (e) { /* gone */ }
  console.log('---\nmanage page in Chrome: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
