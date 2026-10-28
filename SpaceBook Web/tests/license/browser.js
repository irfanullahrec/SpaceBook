'use strict';
/* The free-trial lock (js/sb_license.js) in a real Chrome, on the real page (docs/TRIAL_LOCK.md):
 *   SB_PAGE=lazy.html node --max-old-space-size=3072 tests/license/browser.js
 * The page's public key is swapped for a throw-away one (the script is rewritten on its way to the browser) so a code can be made here;
 * the real private key is never read. The trial start is put into localStorage before the page loads, as if the first visit was N days ago.
 * Dev-only, never shipped. */
const crypto = require('crypto');
const { serve, launch } = require('../baseline/lib');
const L = require('../../js/sb_license.js');

const DAY = 86400000, KEY = 'sb.lic.v1', PAGE = process.env.SB_PAGE || 'lazy.html';
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };

const kp = crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' });
const TEST_SPKI = kp.publicKey.export({ type: 'spki', format: 'der' }).toString('base64');
const DEF_SALT = crypto.randomBytes(16), DEF_CODE = 'Test@Default-1';       // a throw-away default code: the real one is only a hash in the page
const TEST_DEF = { salt: DEF_SALT.toString('base64'), hash: crypto.pbkdf2Sync(Buffer.from(DEF_CODE, 'utf8'), DEF_SALT, L.CFG.defaultCode.iterations, 32, 'sha256').toString('base64') };
const b64u = b => Buffer.from(b).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const code = (dev, until = '0') => { const p = 'SB1|' + dev + '|' + until; return 'SB1-' + b64u(Buffer.from(p)) + '.' + b64u(crypto.sign('sha256', Buffer.from(p), { key: kp.privateKey, dsaEncoding: 'ieee-p1363' })); };
const ymd = ms => new Date(ms).toISOString().slice(0, 10).replace(/-/g, '');

async function open(browser, url, { rec, viewport = { width: 1280, height: 900 }, init, errors } = {}) {
  const ctx = await browser.newContext({ viewport });
  await ctx.route('**/js/sb_license.js*', async route => {
    const r = await route.fetch();
    await route.fulfill({ response: r, body: (await r.text()).replace(L.CFG.publicKey, TEST_SPKI).replace(L.CFG.defaultCode.salt, TEST_DEF.salt).replace(L.CFG.defaultCode.hash, TEST_DEF.hash) });
  });
  const page = await ctx.newPage();
  if (errors) page.on('pageerror', e => errors.push(String(e.message).slice(0, 150)));
  if (rec) {                                                       // same origin as the page, but no scripts: put the record in before the page starts
    await page.goto(url + 'css/sb_license.css');
    await page.evaluate(([k, r]) => localStorage.setItem(k, JSON.stringify(r)), [KEY, rec]);
  }
  if (init) await page.addInitScript(init);
  await page.goto(url + PAGE, { waitUntil: 'domcontentloaded', timeout: 180000 });
  return page;
}
const submit2 = async (page, text) => { await page.fill('#sblicCode', text); await page.click('.sblic-go'); await page.waitForTimeout(500); return page.evaluate(() => document.getElementById('sblicMsg').textContent); };
const waitStatus = (page, fn, arg) => page.waitForFunction(fn, arg, { timeout: 60000 }).then(() => true, () => false);
const stored = page => page.evaluate(k => JSON.parse(localStorage.getItem(k) || 'null'), KEY);

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const now = Date.now();

  // 1. a first visit
  let page = await open(browser, url, { errors });
  check('first visit: the trial starts (30 days left)', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'trial' && window.SBLicense.status().daysLeft === 30));
  let rec = await stored(page);
  check('first visit: start, latest time seen and a device ID are remembered', rec && Math.abs(rec.start - now) < 120000 && rec.seen >= rec.start && /^[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$/.test(rec.device), rec);
  check('first visit: no lock screen and no notice', await page.evaluate(() => !document.getElementById('sbLicLock') && !document.querySelector('.sblic-note')));
  await page.reload({ waitUntil: 'domcontentloaded' });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'trial');
  const again = await stored(page);
  check('a reload keeps the same start and device ID', again.start === rec.start && again.device === rec.device, [rec.start, again.start]);
  await page.context().close();

  // 2. day 25: the notice, shown once a day
  page = await open(browser, url, { rec: { start: now - 25 * DAY, seen: now - 1000 }, errors });
  check('day 25: 5 days left', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'trial' && window.SBLicense.status().daysLeft === 5));
  const note = await page.evaluate(() => (document.querySelector('.sblic-note') || {}).textContent || '');
  check('day 25: a notice says 5 days left and gives the WhatsApp number', /5 days left/.test(note) && /0343 0155606/.test(note), note);
  await page.click('.sblic-note button');
  check('the notice goes away with OK', await page.evaluate(() => !document.querySelector('.sblic-note')));
  await page.reload({ waitUntil: 'domcontentloaded' });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'trial');
  await page.waitForTimeout(500);
  check('...and does not come back the same day', await page.evaluate(() => !document.querySelector('.sblic-note')));
  await page.context().close();

  // 3. day 31: the lock
  page = await open(browser, url, { rec: { start: now - 31 * DAY, seen: now - 1000 }, errors });
  check('day 31: locked', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked'));
  const dev = (await stored(page)).device;
  const lock = await page.evaluate(() => {
    const l = document.getElementById('sbLicLock'); if (!l) return null;
    const a = l.querySelector('a.sblic-wa'), r = l.getBoundingClientRect();
    const kids = [...document.body.children].filter(c => c !== l);
    const mid = document.elementFromPoint(innerWidth / 2, innerHeight / 2);
    return {
      title: l.querySelector('h1').textContent, ur: (l.querySelector('.sblic-ur') || {}).textContent || '', href: a ? a.getAttribute('href') : '', waText: a ? a.textContent : '',
      shown: (l.querySelector('#sblicDev') || {}).textContent, dialog: l.getAttribute('role') + '/' + l.getAttribute('aria-modal'),
      covers: r.width >= innerWidth - 1 && r.height >= innerHeight - 1 && l.contains(mid), kids: kids.length, inert: kids.filter(c => c.hasAttribute('inert')).length,
      rootClass: document.documentElement.classList.contains('sblic-on'),
    };
  });
  check('locked: a dialog covering the whole window, the background inert', lock && lock.dialog === 'dialog/true' && lock.covers && lock.kids > 0 && lock.inert === lock.kids && lock.rootClass, lock);
  check('locked: the title says the 1-month free trial has ended', lock && /1-month free trial has ended/.test(lock.title), lock && lock.title);
  check('locked: the Urdu line is there', lock && /مفت آزمائش/.test(lock.ur), lock && lock.ur);
  check('locked: the WhatsApp button shows 0343 0155606', lock && /0343 0155606/.test(lock.waText), lock && lock.waText);
  const href = lock && lock.href || '';
  check('locked: the WhatsApp link goes to 923430155606 with the device ID in the message', href.startsWith('https://wa.me/923430155606?text=') && decodeURIComponent(href).includes(dev) && /free trial has ended/.test(decodeURIComponent(href)), href);
  check('locked: the device ID shown is the one remembered', lock && lock.shown === dev, [lock && lock.shown, dev]);
  const focusOk = [];
  for (let i = 0; i < 14; i++) { await page.keyboard.press(i % 3 === 2 ? 'Shift+Tab' : 'Tab'); focusOk.push(await page.evaluate(() => !!document.activeElement && !!document.activeElement.closest('#sbLicLock'))); }
  check('keyboard: Tab never leaves the lock screen (14 presses)', focusOk.every(Boolean), focusOk);
  const links = await page.evaluate(() => [...document.querySelectorAll('#sbLicLock a, #sbLicLock button')].map(b => Math.round(b.getBoundingClientRect().height)));
  check('every button and link on the lock screen is at least 44 px high', links.length >= 3 && links.every(h => h >= 44), links);

  // 3b. wrong codes: 4 tries left, a code for another device, then blocked after 5
  const submit = async text => { await page.fill('#sblicCode', text); await page.click('.sblic-go'); await page.waitForTimeout(400); return page.evaluate(() => document.getElementById('sblicMsg').textContent); };
  let msg = await submit('SB1-garbage.garbage');
  check('a wrong code: "4 tries left"', /not right\. 4 tries left/.test(msg), msg);
  msg = await submit(code('WXYZ-9876'));
  check('a good code for another device: says it is for another device', /another device/.test(msg), msg);
  await submit('nope'); await submit('nope2');
  msg = await submit('nope3');
  check('five wrong tries: the box is blocked for a minute', /Too many wrong tries\. Please wait 60 seconds/.test(msg), msg);
  msg = await submit(code(dev));
  check('...and even the right code waits while blocked', /Too many wrong tries/.test(msg) && await page.evaluate(() => !!document.getElementById('sbLicLock')), msg);
  await page.context().close();

  // 4. unlocking with the right code
  page = await open(browser, url, { rec: { start: now - 40 * DAY, seen: now - 1000 }, errors });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked');
  const dev2 = (await stored(page)).device;
  const pasted = code(dev2);                                       // one code: a signature is random, two calls give two different codes
  await page.fill('#sblicCode', ' ' + pasted.slice(0, 30) + '\n ' + pasted.slice(30) + ' ');       // as pasted from WhatsApp, broken over two lines
  await page.click('.sblic-go');
  check('the right code unlocks it: the lock screen is gone, the page is usable again', await waitStatus(page, () => window.SBLicense.status().licensed === true && !document.getElementById('sbLicLock') && !document.documentElement.classList.contains('sblic-on') && !document.querySelector('[data-sblic]')));
  check('the code is remembered', !!(await stored(page)).code);
  await page.reload({ waitUntil: 'domcontentloaded' });
  check('after a reload it stays unlocked (no lock screen at all)', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().licensed === true) && await page.evaluate(() => !document.getElementById('sbLicLock')));
  await page.context().close();

  // 5. a code with an end date in the past
  page = await open(browser, url, { rec: { start: now - 40 * DAY, seen: now - 1000 }, errors });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked');
  const dev3 = (await stored(page)).device;
  await page.fill('#sblicCode', code(dev3, ymd(now - 2 * DAY)));
  await page.click('.sblic-go'); await page.waitForTimeout(500);
  msg = await page.evaluate(() => document.getElementById('sblicMsg').textContent);
  check('a code that ended yesterday is refused ("has ended")', /has ended/.test(msg), msg);
  await page.context().close();

  // 5b. the default unlock code: opens the lock for 30 days from the moment it is typed
  page = await open(browser, url, { rec: { start: now - 40 * DAY, seen: now - 1000 }, errors });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked');
  msg = await submit2(page, 'Test@Default-2');
  check('a wrong text that is not a signed code counts as a wrong try ("4 tries left")', /not right\. 4 tries left/.test(msg), msg);
  await page.fill('#sblicCode', '  ' + DEF_CODE + '  ');
  await page.click('.sblic-go');
  check('the default code (with spaces around it) opens the lock', await waitStatus(page, () => !document.getElementById('sbLicLock') && window.SBLicense.status().kind === 'trial'));
  const st = await page.evaluate(() => window.SBLicense.status());
  const r2 = await stored(page);
  check('...for 30 days from now: 30 days left, the end remembered', st.daysLeft === 30 && Math.abs(r2.extendUntil - (now + 30 * DAY)) < 180000 && r2.fails === 0, { st, ext: r2.extendUntil - now });
  await page.reload({ waitUntil: 'domcontentloaded' });
  check('after a reload it is still open (30 days left)', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'trial' && window.SBLicense.status().daysLeft === 30) && await page.evaluate(() => !document.getElementById('sbLicLock')));
  check('the default code is not kept: only the end date is', !JSON.stringify(await stored(page)).includes(DEF_CODE));
  await page.context().close();

  page = await open(browser, url, { rec: { start: now - 70 * DAY, extendUntil: now - 1000, seen: now - 500 }, errors });
  check('when that month is over the lock is back', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked'));
  await page.context().close();

  page = await open(browser, url, { rec: { start: now - 70 * DAY, extendUntil: now + 3 * DAY, seen: now - 500 }, errors });
  check('in the last days of that month: 3 days left and the notice says so', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().daysLeft === 3) && /SpaceBook access: 3 days left/.test(await page.evaluate(() => (document.querySelector('.sblic-note') || {}).textContent || '')));
  await page.context().close();

  // 6. the clock moved back
  page = await open(browser, url, { rec: { start: now - 29 * DAY, seen: now + 5 * DAY }, errors });
  check('a clock moved back does not reopen it (29 days since start, but time was seen 5 days ahead: locked)', await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked'));
  await page.context().close();

  // 7. the Android app's WebView has its own gate
  page = await open(browser, url, { rec: { start: now - 40 * DAY, seen: now - 1000 }, init: () => { window.SBHost = {}; }, errors });
  await page.waitForTimeout(2500);
  check('inside the app (SBHost) the page does not lock: the app has its own gate', await page.evaluate(() => !document.getElementById('sbLicLock') && window.SBLicense.status().kind === 'open'));
  await page.context().close();

  // 8. a phone-size screen
  page = await open(browser, url, { rec: { start: now - 31 * DAY, seen: now - 1000 }, viewport: { width: 390, height: 844 }, errors });
  await waitStatus(page, () => window.SBLicense && window.SBLicense.status().kind === 'locked');
  const ph = await page.evaluate(() => {
    const l = document.getElementById('sbLicLock'), c = l.querySelector('.sblic-card').getBoundingClientRect();
    return { noSideScroll: document.documentElement.scrollWidth <= innerWidth && l.scrollWidth <= l.clientWidth + 1, cardFits: c.left >= 0 && c.right <= innerWidth, btn: [...l.querySelectorAll('a, button')].every(b => b.getBoundingClientRect().height >= 44) };
  });
  check('390 px wide: no sideways scrolling, the card fits, every button is 44 px high', ph.noSideScroll && ph.cardFits && ph.btn, ph);
  await page.context().close();

  check('no script error on any of these pages', errors.length === 0, errors.slice(0, 3));
  console.log('---\ntrial lock browser test: ' + pass + ' passed, ' + fail + ' failed');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
