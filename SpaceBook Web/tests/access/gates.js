'use strict';
/* "Chapters 1 and 2 of every subject of every class are free, the rest needs a plan", on the real pages of every class (they use different readers).
 *     node --max-old-space-size=8192 tests/access/gates.js [--all] [--out <folder for screenshots>]
 * For subjects of the app catalog (content/app_catalog.json: the same call the app uses to open each chapter): open the subject, open chapters 1 and 2 (index 0 and 1)
 * with the catalog's own call and require that no lock shows and the page has content; then chapter 3 (index 2) and require the locked panel.
 * Default: 3 subjects per class (the first, the middle, the last); --all: every subject (about 130, several minutes).
 * Then the same with a Student plan for the class (a visitor with an approved payment): chapter 3 opens. Needs PHP and MySQL; dev-only, never shipped. */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path'), net = require('net');
const { launch, ROOT } = require('../baseline/lib');

const args = process.argv.slice(2);
const ALL = args.includes('--all') || args.includes('--from') || args.includes('--only');
const ONLY = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',') : null;      // --only cls10-islopt,cls9-eng
const FROM = args.includes('--from') ? args[args.indexOf('--from') + 1] : '';      // --from cls10-chem: the subjects from that one on (with --all)
const PHP = process.env.PHP || (fs.existsSync('C:/xampp/php/php.exe') ? 'C:/xampp/php/php.exe' : 'php');
const CFG = path.join(os.tmpdir(), 'sb_gates_cfg_' + process.pid + '.php');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const dbq = (...a) => spawnSync(PHP, [path.join(ROOT, 'tests/access/db.php'), ...a], { encoding: 'utf8' });
const freePort = () => new Promise(res => { const s = net.createServer(); s.listen(0, '127.0.0.1', () => { const p = s.address().port; s.close(() => res(p)); }); });

(async () => {
  const cat = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  let picks = [];
  for (const c of cat.classes) {
    const list = c.subjects.filter(s => s.chapters.length >= 3);
    const chosen = ALL ? list : [...new Set([list[0], list[Math.floor(list.length / 2)], list[list.length - 1]])].filter(Boolean);
    chosen.forEach(s => picks.push({ cls: c.id, id: s.id, name: s.name, ch0: s.chapters[0].o, ch1: s.chapters[1].o, ch2: s.chapters[2].o }));
  }
  if (ONLY) picks = picks.filter(p => ONLY.includes(p.id));
  if (FROM) { const k = picks.findIndex(p => p.id === FROM); if (k >= 0) picks = picks.slice(k); }
  if (!/ready/.test(dbq('init', CFG).stdout)) { console.log('FAIL  throwaway database'); process.exit(1); }
  const port = await freePort();
  const srv = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', ROOT], { env: Object.assign({}, process.env, { SB_CONFIG: CFG }), stdio: 'ignore' });
  for (let i = 0; i < 60; i++) { const ok = await new Promise(r => { const s = net.connect(port, '127.0.0.1', () => { s.destroy(); r(true); }); s.on('error', () => r(false)); }); if (ok) break; await sleep(150); }
  const url = 'http://127.0.0.1:' + port + '/';
  const browser = await launch({ anonymous: true });
  const errors = [];
  let ctx = null, page = null;
  async function fresh() {                                   // a new page: a very heavy subject can hang one
    if (ctx) { try { await ctx.close(); } catch (e) { /* gone */ } }
    ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
    page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(url + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
    await page.waitForFunction(() => window.SBAccess && window.SBBilling && typeof openSubject === 'function' && window.SBAccess.state().ok, null, { timeout: 120000 });
    await sleep(3000);
  }
  await fresh();
  const within = (ms, p) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('timeout ' + ms + ' ms')), ms))]);

  async function look(p, chapterCall) {
    await page.evaluate(([cls, id]) => { openSubject(cls, id); }, [p.cls, p.id]);
    await sleep(900);
    await page.evaluate(call => { (0, eval)(call); }, chapterCall);
    await sleep(900);
    return page.evaluate(() => {
      const lock = !!document.querySelector('.sbx-lock');
      const body = document.getElementById('page-content') || document.body;
      return { lock, len: (body.innerText || '').length };
    });
  }
  const rows = [];
  for (const p of picks) {
    let a, a2, b;
    try { a = await within(90000, look(p, p.ch0)); a2 = await within(90000, look(p, p.ch1)); b = await within(90000, look(p, p.ch2)); } catch (e) { a = { err: String(e.message).slice(0, 120) }; a2 = a; b = a; try { await fresh(); } catch (e2) { /* the next subject reports it */ } }
    rows.push({ p, a, a2, b });
    check(p.id + ' (' + p.name + '): Chapters 1 and 2 open, Chapter 3 is locked', a.lock === false && a.len > 200 && a2.lock === false && a2.len > 200 && b.lock === true, { a, a2, b });
  }

  // the same subjects with a Student plan for their class: Chapter 2 opens (a visitor account with an approved payment, signed in through the page)
  const sample = picks.filter((p, i, all) => all.findIndex(x => x.cls === p.cls) === i).slice(0, ALL ? 12 : 4);
  for (const p of sample) {
    const num = '9230099' + String(Math.floor(Math.random() * 1e5)).padStart(5, '0');
    const reg = await page.evaluate(async ([n]) => {
      const r = await fetch('api/auth.php?action=register', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name: 'Gate Tester', father_name: 'Father', whatsapp: n, password: 'secret123', want_device: true }) });
      const j = await r.json();
      if (j.ok && j.device && window.SBSync) await window.SBSync.setDevice(j.user.id, j.device);
      document.dispatchEvent(new CustomEvent('spacebook:auth', { detail: { user: j.user } }));
      return j.ok;
    }, [num]);
    const uid = JSON.parse(dbq('json', CFG, "SELECT id FROM users WHERE whatsapp = '" + '92' + num.slice(2) + "'").stdout || '[]');
    // a payment through the real API, approved as the administrator would
    const sub = await page.evaluate(async (cls) => {
      const r = await SBAccess.call('billing.php?action=submit_payment', { method: 'POST', headers: SBAccess.headers({ 'Content-Type': 'application/json' }), body: JSON.stringify({ plan: 'student', cls, trx: 'T' + String(Date.now()).slice(-9) + Math.floor(Math.random() * 99), idem: 'g' + Math.random() }) }, 10000);
      return r.json;
    }, p.cls);
    const pid = sub && sub.payment && sub.payment.id;
    if (pid) dbq('approve', CFG, String(pid));
    await page.evaluate(async () => { await SBAccess.load(); });
    const r2 = await look(p, p.ch2);
    check(p.id + ': with a Student plan for ' + p.cls + ' Chapter 3 opens', reg === true && !!pid && r2.lock === false && r2.len > 200, { reg, pid, r2 });
    await page.evaluate(async () => { await fetch('api/auth.php?action=logout', { method: 'POST', credentials: 'same-origin', headers: Object.assign({ 'Content-Type': 'application/json' }, SBSync.bearerHeaders()), body: '{}' }); try { await SBSync.clearDevice(SpaceBookAuth.user && SpaceBookAuth.user.id); } catch (e) { /* fine */ } document.dispatchEvent(new CustomEvent('spacebook:auth', { detail: { user: null } })); await SBAccess.load(); });
  }

  await browser.close();
  srv.kill();
  dbq('drop', CFG);
  try { fs.unlinkSync(CFG); } catch (e) { /* gone */ }
  check('no page errors', errors.length === 0, errors.slice(0, 4));
  console.log('---\ngates: ' + pass + ' passed, ' + fail + ' failed (' + picks.length + ' subjects' + (ALL ? ', all' : ', sample') + ')');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
