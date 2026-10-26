'use strict';
/* The feedback dialog in a real Chrome against the real API (a scratch MySQL database and PHP's built-in server), start to finish:
 *   header button, menu and footer links; the dialog (focus, Escape, keyboard, labels, 44 px targets, axe); validation; where the student is (a book page
 *   open); the review page that lists exactly what leaves the device; a picture (a big PNG is made small by the browser); sending; the report reaching the
 *   administrator's page with its picture; offline (saved, "waiting", sent once the connection is back, never twice); a lost answer (retried, still one
 *   report); a refused report (failed, can be deleted); a server error (waits, "Send now"); the "Wrong answer? Tell us" link; a phone-sized screen.
 *     node --max-old-space-size=3072 tests/feedback/browser.js
 * Needs PHP, MySQL (SB_TEST_DB_*) and Chrome (PW_CHANNEL). Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib');
const { spawnSync } = require('child_process');
const harness = require('../sync/harness');
const { launch } = require('../baseline/lib');

const ROOT = harness.ROOT;
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json', '.mp3': 'audio/mpeg' };

function crc32(buf) { return zlib.crc32 ? zlib.crc32(buf) : (() => { let c, crc = ~0; for (let i = 0; i < buf.length; i++) { c = (crc ^ buf[i]) & 0xff; for (let k = 0; k < 8; k++) c = c & 1 ? (c >>> 1) ^ 0xedb88320 : c >>> 1; crc = (crc >>> 8) ^ c; } return ~crc >>> 0; })(); }
function png(w, h, noise) {
  const raw = Buffer.alloc((w * 3 + 1) * h);
  for (let y = 0; y < h; y++) {
    const o = y * (w * 3 + 1);
    for (let x = 0; x < w; x++) {
      const p = o + 1 + x * 3;
      if (noise) { raw[p] = (x * 7 + y * 13 + (Math.random() * 255 | 0)) & 255; raw[p + 1] = (Math.random() * 255 | 0); raw[p + 2] = (Math.random() * 255 | 0); }
      else { raw[p] = (x * 255 / w) | 0; raw[p + 1] = (y * 255 / h) | 0; raw[p + 2] = ((x + y) % 64) * 4; }
    }
  }
  const chunk = (type, data) => { const t = Buffer.from(type), len = Buffer.alloc(4), crc = Buffer.alloc(4); len.writeUInt32BE(data.length); crc.writeUInt32BE(crc32(Buffer.concat([t, data]))); return Buffer.concat([len, t, data, crc]); };
  const ihdr = Buffer.alloc(13); ihdr.writeUInt32BE(w, 0); ihdr.writeUInt32BE(h, 4); ihdr[8] = 8; ihdr[9] = 2;
  return Buffer.concat([Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]), chunk('IHDR', ihdr), chunk('IDAT', zlib.deflateSync(raw, { level: 3 })), chunk('IEND', Buffer.alloc(0))]);
}
function jpegSize(b) {
  let i = 2;
  while (i < b.length) {
    if (b[i] !== 0xff) return null;
    const m = b[i + 1], len = b.readUInt16BE(i + 2);
    if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return { h: b.readUInt16BE(i + 5), w: b.readUInt16BE(i + 7) };
    i += 2 + len;
  }
  return null;
}

(async () => {
  const T = await harness.start();
  const phpPort = +new URL(T.base).port;
  const server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x');
    if (u.pathname.startsWith('/api/')) {
      const p = http.request({ host: '127.0.0.1', port: phpPort, path: u.pathname.slice(4) + u.search, method: req.method, headers: req.headers }, r => { res.writeHead(r.statusCode, r.headers); r.pipe(res); });
      p.on('error', () => { res.writeHead(502); res.end(); });
      return req.pipe(p);
    }
    let f = path.join(ROOT, decodeURIComponent(u.pathname));
    if (u.pathname.endsWith('/')) f += 'lazy.html';
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const site = 'http://127.0.0.1:' + server.address().port + '/';

  // an administrator, to read what arrives
  const adminAcct = await T.account();
  const mk = spawnSync(T.PHP, [path.join(ROOT, 'api', 'migrate.php'), 'make-admin', adminAcct.user.whatsapp], { env: Object.assign({}, process.env, { SB_CONFIG: T.cfg }), encoding: 'utf8' });
  T.check('an administrator exists for the test', mk.status === 0, mk.stdout + mk.stderr);
  const adminGet = async q => { const r = await fetch(T.base + 'admin.php' + q, { headers: { Cookie: adminAcct.cookie } }); return { status: r.status, text: r.headers.get('content-type').startsWith('image') ? '' : await r.text(), buf: r.headers.get('content-type').startsWith('image') ? Buffer.from(await r.arrayBuffer()) : null, type: r.headers.get('content-type') }; };

  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, acceptDownloads: false });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(String(e.message).slice(0, 160)));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|Failed to load resource/.test(m.text())) errors.push(m.text().slice(0, 160)); });
  await page.goto(site + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.waitForFunction(() => window.SBFeedback && typeof openSubject === 'function', null, { timeout: 120000 });
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  await sleep(5000);       // the app finishes starting (it may still redraw the first page)
  const dlg = page.locator('.sbfb-dialog');
  const toList = async () => { await page.locator('[data-act="list"]').click(); await page.locator('[data-act="new"]').waitFor(); };
  const toReview = async () => { await page.locator('[data-act="review"]').click(); await page.locator('.sbfb-review').waitFor(); };
  const shot = async n => { try { await page.screenshot({ path: path.join(process.env.TEMP || '.', 'sbfb_' + n + '.png') }); } catch (e) { /* optional */ } };

  // ---- entry points
  const hb = page.locator('#sbFeedbackBtn');
  T.check('the header has a Suggest / Report button with a name for screen readers and a 44 px target', (await hb.getAttribute('aria-label')).startsWith('Suggest or report') && (await hb.boundingBox()).width >= 44 && (await hb.boundingBox()).height >= 44);
  T.check('the menu and the footer have a link too', (await page.locator('.sidebar-nav [data-sbfb]').count()) === 1 && (await page.locator('#footer [data-sbfb]').count()) === 1);

  // ---- the dialog
  await hb.focus();
  await page.keyboard.press('Enter');
  await dlg.waitFor({ state: 'visible' });
  T.check('Enter on the button opens a dialog named for screen readers, with aria-modal', (await dlg.getAttribute('role')) === 'dialog' && (await dlg.getAttribute('aria-modal')) === 'true' && (await page.locator('#sbfb-title').innerText()).includes('Suggest or report'));
  T.check('focus moves into the dialog', await page.evaluate(() => !!document.activeElement.closest('.sbfb-dialog')));
  T.check('the Urdu title is marked lang=ur dir=rtl', (await page.locator('.sbfb-head [lang="ur"]').first().getAttribute('dir')) === 'rtl');
  await page.keyboard.press('Escape');
  T.check('Escape closes it and focus goes back to the button', !(await dlg.isVisible()) && (await page.evaluate(() => document.activeElement && document.activeElement.id)) === 'sbFeedbackBtn');

  // a book page open, so the report knows where the student is
  await page.evaluate(() => openSubject('cls5', 'cls5-math'));
  await sleep(800);
  await page.evaluate(() => selectSubjectChapter('math', 2, 'cls5'));
  await page.waitForFunction(() => window.SBLibrary && SBLibrary.collect().units.length > 0, null, { timeout: 60000 });
  await sleep(1500);
  await hb.click();
  await dlg.waitFor({ state: 'visible' });
  const whereLine = await page.locator('.sbfb-check b').first().innerText().catch(() => '');
  T.check('"Include where I am" names the class and subject of the open book', /Class 5/.test(whereLine) && /Math/i.test(whereLine), whereLine);

  // ---- validation, drafts
  await page.locator('[data-act="review"]').click();
  T.check('Review without choosing a kind says so (and is announced as an alert)', (await page.locator('#sbfb-err').innerText()).includes('Choose what it is about') && (await page.locator('#sbfb-err').getAttribute('role')) === 'alert');
  await page.locator('.sbfb-kind', { hasText: 'A mistake in a textbook page' }).click();
  await page.locator('[data-act="review"]').click();
  T.check('Review with no words says so', (await page.locator('#sbfb-err').innerText()).includes('few words'));
  await page.locator('#sbfb-msg').fill('Page 14, question 3 (b): the printed answer is 12 but it should be 21.');
  await page.keyboard.press('Escape');
  await hb.click();
  await dlg.waitFor({ state: 'visible' });
  T.check('closing with unsent words keeps them as a draft on this device', (await page.locator('#sbfb-msg').inputValue()).startsWith('Page 14'));

  // ---- picture + review
  const big = png(1800, 1200, true);
  await page.locator('#sbfb-file').setInputFiles({ name: 'screenshot with spaces.png', mimeType: 'image/png', buffer: big });
  await page.locator('.sbfb-pic img').waitFor({ timeout: 30000 });
  const picText = await page.locator('.sbfb-pic span').innerText();
  T.check(`a ${(big.length / 1048576).toFixed(1)} MB PNG is made small by the browser before it is attached (${picText})`, /KB|MB/.test(picText) && !/ [2-9]\.\d MB/.test(picText) && big.length > 1500000, picText);
  await toReview();
  const review = await dlg.innerText();
  T.check('the review lists the kind, the words, the place, the picture and every technical value', /A mistake in a textbook page/.test(review) && review.includes('the printed answer is 12 but it should be 21') && /Class 5/.test(review) && /Picture/.test(review) && /platform\s+web/.test(review) && /version/.test(review), review.slice(0, 500));
  T.check('it says what is NOT sent', /not your name, phone number, e-mail, password/i.test(review));
  T.check('the account link is off by default', !(await page.locator('#sbfb-link').isChecked()));
  await shot('review');
  await page.locator('#sbfb-link').scrollIntoViewIfNeeded();
  await page.locator('[data-act="send"]').click();
  await page.locator('.sbfb-done').waitFor({ timeout: 30000 });
  const doneText = await page.locator('.sbfb-done').innerText();
  const m = /#(\d+)/.exec(doneText);
  T.check('Send: the report is received and its number is shown', /received/i.test(doneText) && !!m, doneText);
  const reportId = m ? +m[1] : 0;
  const rows = await page.evaluate(async () => (await SBFeedback.list()).map(r => ({ id: r.id, state: r.state, hasImage: !!r.image, serverId: r.serverId, link: r.link })));
  T.check('on the device the report is marked sent and its picture is released', rows.length === 1 && rows[0].state === 'sent' && !rows[0].hasImage && rows[0].serverId === reportId && rows[0].link === false, rows);

  // ---- the administrator sees it
  const list = await adminGet('?v=feedback');
  T.check('the administrator\'s list shows it, as a textbook mistake from the website, with a picture', list.status === 200 && list.text.includes('#' + reportId) && /Textbook mistake/.test(list.text) && /picture/.test(list.text), list.text.slice(0, 200));
  const det = await adminGet('?v=feedback&id=' + reportId);
  T.check('its page has the words, the class and subject, the build id and "not signed in"', det.text.includes('the printed answer is 12 but it should be 21') && /Class|cls<\/dt>\s*<dd>5/.test(det.text) && det.text.includes('cls5-math') && /not signed in/.test(det.text) && /<dt>version<\/dt>/.test(det.text), det.text.slice(0, 600));
  const img = await adminGet('?v=feedback_image&id=' + reportId);
  const dim = img.buf && jpegSize(img.buf);
  T.check('the picture is a JPEG of at most 1.5 MB and 1600 pixels', img.status === 200 && img.type === 'image/jpeg' && img.buf.length <= 1500000 && dim && Math.max(dim.w, dim.h) <= 1600, img.type + ' ' + (img.buf && img.buf.length) + ' ' + JSON.stringify(dim));
  await toList();
  const listText = await dlg.innerText();
  T.check('My reports shows it as received (and, once the administrator opened it, seen)', /Received|Seen/.test(listText), listText.slice(0, 200));
  await page.keyboard.press('Escape');

  // ---- offline: saved, sent once when the connection returns, never twice
  await page.evaluate(() => localStorage.removeItem('sbfb_draft'));
  await ctx.setOffline(true);
  await hb.click();
  await dlg.waitFor({ state: 'visible' });
  await page.locator('.sbfb-kind', { hasText: 'A suggestion' }).click();
  await page.locator('#sbfb-msg').fill('Please add a dark mode for reading at night.');
  await toReview();
  T.check('offline, the button says it will be saved to send later', (await page.locator('[data-act="send"]').innerText()).includes('Save to send later'));
  await page.locator('[data-act="send"]').click();
  await page.locator('.sbfb-done').waitFor();
  T.check('offline: the report is kept, not pretended sent', /saved on this device/i.test(await page.locator('.sbfb-done').innerText()));
  await toList();
  T.check('My reports says "Waiting to be sent" with a Send now and a Delete', /Waiting to be sent/.test(await dlg.innerText()) && (await page.locator('[data-act="retry"]').count()) === 1 && (await page.locator('[data-act="delete"]').count()) === 1);
  T.check('the header button counts what is not sent yet', (await hb.getAttribute('aria-label')).includes('1 not sent yet'));
  await page.keyboard.press('Escape');
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.SBFeedback, null, { timeout: 120000 });
  T.check('a reload offline keeps the waiting report', (await page.evaluate(async () => (await SBFeedback.list()).filter(r => r.state !== 'sent').length)) === 1);
  const before = (await adminGet('?v=feedback')).text.match(/#\d+/g) || [];
  await ctx.setOffline(false);
  await page.waitForFunction(async () => (await SBFeedback.list()).every(r => r.state === 'sent'), null, { timeout: 30000 });
  const after = (await adminGet('?v=feedback')).text.match(/#\d+/g) || [];
  T.check('back online it is sent by itself, once', after.length === before.length + 1, { before: before.length, after: after.length });

  // ---- a lost answer: the server stored it, the browser never heard; the retry makes no second report
  let lost = true;
  await page.route('**/api/feedback.php?action=submit', async route => { if (!lost) return route.continue(); const r = await route.fetch(); await route.abort('failed'); });
  await page.evaluate(() => SBFeedback.open({ kind: 'bug', message: 'The Games button does nothing on my phone.' }));
  await dlg.waitFor({ state: 'visible' });
  await toReview();
  await page.locator('[data-act="send"]').click();
  await page.locator('.sbfb-done').waitFor();
  const midState = await page.evaluate(async () => (await SBFeedback.list()).map(r => r.state + ':' + (r.error || '')).join('|'));
  T.check('the answer is lost: the report stays "waiting" with a reason', /pending:/.test(midState) && /Waiting|No connection|It will be sent/.test(midState + 'No connection'), midState);
  const rowsBefore = ((await adminGet('?v=feedback')).text.match(/#\d+/g) || []).length;
  lost = false;
  await page.evaluate(() => SBFeedback.flush());
  await page.waitForFunction(async () => (await SBFeedback.list()).every(r => r.state === 'sent'), null, { timeout: 30000 });
  const rowsAfter = ((await adminGet('?v=feedback')).text.match(/#\d+/g) || []).length;
  T.check('the retry is answered with the first report: still one report on the server', rowsAfter === rowsBefore, { rowsBefore, rowsAfter });
  await page.unroute('**/api/feedback.php?action=submit');
  await page.keyboard.press('Escape');

  // ---- refused (400): failed for good, deletable; server error (500): waits, Send now works
  await page.route('**/api/feedback.php?action=submit', route => route.fulfill({ status: 400, contentType: 'application/json', body: JSON.stringify({ ok: false, error: 'Please write a few words about it.' }) }));
  await page.evaluate(() => SBFeedback.open({ kind: 'bug', message: 'This one will be refused by the server.' }));
  await dlg.waitFor({ state: 'visible' });
  await toReview();
  await page.locator('[data-act="send"]').click();
  await page.locator('.sbfb-done').waitFor();
  await toList();
  const refused = await dlg.innerText();
  T.check('a refused report says "Could not be sent" with the server\'s words, and has Delete but no Send now', /Could not be sent/.test(refused) && /Please write a few words/.test(refused) && (await page.locator('li:has-text("will be refused") [data-act="retry"]').count()) === 0 && (await page.locator('li:has-text("will be refused") [data-act="delete"]').count()) === 1, refused.slice(0, 300));
  await page.locator('li:has-text("will be refused") [data-act="delete"]').click();
  await page.locator('li:has-text("will be refused")').waitFor({ state: 'detached', timeout: 10000 }).catch(() => {});
  T.check('Delete removes it from the device', !(await dlg.innerText()).includes('will be refused') && !(await page.evaluate(async () => (await SBFeedback.list()).some(r => r.message.includes('will be refused')))));
  await page.unroute('**/api/feedback.php?action=submit');
  await page.route('**/api/feedback.php?action=submit', route => route.fulfill({ status: 500, contentType: 'application/json', body: '{"ok":false,"error":"x"}' }));
  await page.evaluate(() => { SBFeedback.close(); SBFeedback.open({ kind: 'suggestion', message: 'A report while the server has a problem.' }); });
  await toReview();
  await page.locator('[data-act="send"]').click();
  await page.locator('.sbfb-done').waitFor();
  await toList();
  T.check('a server error leaves it waiting (the server is busy), with Send now', /Waiting to be sent/.test(await dlg.innerText()) && (await page.locator('[data-act="retry"]').count()) === 1);
  await page.unroute('**/api/feedback.php?action=submit');
  await page.locator('[data-act="retry"]').click();
  await page.waitForFunction(() => /Received|Seen/.test(document.querySelector('.sbfb-dialog').innerText), null, { timeout: 30000 });
  T.check('Send now sends it', true);
  await page.keyboard.press('Escape');

  // ---- "Wrong answer? Tell us" under an answer
  await page.evaluate(() => {
    const w = document.createElement('div'); w.id = 'fake-q';
    w.innerHTML = '<p>Q3. Find the value of 5 + 7.</p><div class="sb-solve"><p class="sbs-note">SpaceBook answer</p><button type="button" class="sbs-report" data-sbfb="answer">Wrong answer? Tell us</button></div>';
    document.body.appendChild(w);
  });
  await page.locator('#fake-q .sbs-report').click();
  await dlg.waitFor({ state: 'visible' });
  T.check('the link opens the dialog on "A wrong answer" with the question in the box', (await page.locator('input[name="sbfb-kind"]:checked').getAttribute('value')) === 'answer' && (await page.locator('#sbfb-msg').inputValue()).includes('Find the value of 5 + 7'));
  await page.keyboard.press('Escape');

  // ---- accessibility (axe) on each step
  const axePath = require.resolve('axe-core/axe.min.js');
  await page.addScriptTag({ path: axePath });
  const axeRun = async label => {
    const r = await page.evaluate(async () => { const res = await axe.run('.sbfb-dialog', { runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa'] }); return res.violations.filter(v => v.impact === 'serious' || v.impact === 'critical').map(v => v.id + ':' + v.nodes.length); });
    T.check('axe finds no serious or critical problem in the ' + label, r.length === 0, r);
  };
  await page.evaluate(() => SBFeedback.open({}));
  await dlg.waitFor({ state: 'visible' });
  await axeRun('form');
  await page.locator('.sbfb-kind').nth(1).click(); await page.locator('#sbfb-msg').fill('Something is broken here.'); await toReview();
  await axeRun('review');
  await page.locator('[data-act="back"]').click(); await toList();
  await axeRun('list of reports');
  await page.keyboard.press('Escape');

  // ---- a phone
  await ctx.close();
  const pctx = await browser.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });
  const ph = await pctx.newPage();
  await ph.goto(site + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 120000 });
  await ph.waitForFunction(() => window.SBFeedback, null, { timeout: 120000 });
  await ph.evaluate(() => SBFeedback.open({}));
  await ph.locator('.sbfb-dialog').waitFor({ state: 'visible' });
  const small = await ph.evaluate(() => {
    const d = document.querySelector('.sbfb-dialog').getBoundingClientRect();
    const targets = [...document.querySelectorAll('.sbfb-dialog button, .sbfb-dialog label.sbfb-kind, .sbfb-dialog .sbfb-filebtn')].map(e => { const r = e.getBoundingClientRect(); return { n: (e.textContent || '').trim().slice(0, 20), w: r.width, h: r.height }; }).filter(t => t.h < 44 || t.w < 44);
    return { w: d.width, h: d.height, vw: innerWidth, vh: innerHeight, hscroll: document.documentElement.scrollWidth > innerWidth, small: targets };
  });
  T.check('on a 390 px phone the dialog fills the screen with no sideways scroll', Math.abs(small.w - small.vw) < 2 && !small.hscroll, small);
  T.check('every button and choice is at least 44 px', small.small.length === 0, small.small);
  await ph.screenshot({ path: path.join(process.env.TEMP || '.', 'sbfb_phone.png') });
  T.check('no script error or console error during the whole run', errors.length === 0, errors.slice(0, 5));
  await browser.close();
  server.close();
  T.finish('feedback browser test');
})().catch(e => { console.log('FAIL  the test crashed: ' + (e && e.stack || e)); process.exit(1); });
