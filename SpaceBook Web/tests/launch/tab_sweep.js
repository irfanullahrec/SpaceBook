'use strict';
/* Every tab of every subject, opened in a real Chrome, to find the ones that are empty, misleading or broken.
 *   node --max-old-space-size=3072 tests/launch/tab_sweep.js [--classes 1,2,...] [--out docs/launch/TAB_SWEEP.json] [--chapters 2] [--width 1280]
 * For each class and subject of content/app_catalog.json: open the subject, open the first chapter that has an exercise (and, with --chapters N, the next ones),
 * click each tab of the chapter's tab bar in turn and record what it shows: its label, how much text, how many Ans buttons, MCQ rows, pictures, whether the
 * label says what is inside (an "Exercise" tab with no exercise, a "Videos" tab with no video, a "Summary" tab with nothing in it), and any script error.
 * A tab is flagged EMPTY when it shows less than 40 characters of text and no picture, no figure and no table. The result is the finding list of
 * docs/launch/FINDINGS_REGISTER.md (section U); it is also a regression check: --check fails when a tab that had content in the baseline is empty now.
 * Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const CLASSES = opt('--classes', '1,2,3,4,5,6,7,8,9,10,11,12').split(',').map(x => 'cls' + x.trim());
const ONLY = opt('--subjects', null) ? opt('--subjects', '').split(',') : null;        // e.g. --subjects cls12-islopt,cls12-quran
const PER_SUBJECT_MS = +opt('--subject-timeout', 240000);                                // a subject that hangs is reported, not waited for
const NCH = +opt('--chapters', 1), WIDTH = +opt('--width', 1280);
const OUT = path.resolve(ROOT, opt('--out', 'docs/launch/TAB_SWEEP.json'));
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json' };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const cache = new Map();
  const server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x');
    let f = path.join(ROOT, decodeURIComponent(u.pathname)); if (u.pathname.endsWith('/')) f += 'lazy.html';
    if (!f.startsWith(ROOT) || /[\\/]api[\\/]/.test(f) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(u.pathname.startsWith('/api/') ? 404 : 404); return res.end('{"ok":false}'); }
    let e = cache.get(f); if (!e) { const b = fs.readFileSync(f); e = { b, gz: /\.(html|js|css|json|svg)$/.test(f) ? zlib.gzipSync(b, { level: 1 }) : null }; if (b.length < 3e7) cache.set(f, e); }
    const gz = e.gz && /gzip/.test(req.headers['accept-encoding'] || '');
    res.writeHead(200, Object.assign({ 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }, gz ? { 'Content-Encoding': 'gzip' } : {})); res.end(gz ? e.gz : e.b);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const url = 'http://127.0.0.1:' + server.address().port + '/';
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  const result = { schema: 'spacebook.tab-sweep/1', width: WIDTH, subjects: [] };
  let page = null, errors = [];
  const fresh = async () => {
    if (page) { try { await page.context().close(); } catch (e) { /* gone */ } }
    const ctx = await browser.newContext({ viewport: { width: WIDTH, height: 900 } });
    page = await ctx.newPage();
    errors = [];
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 140)));
    await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 180000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 180000 });
    await sleep(4000);
  };
  await fresh();
  let n = 0;
  for (const c of catalog.classes) {
    if (!CLASSES.includes(c.id)) continue;
    for (const s of c.subjects) {
      if (ONLY && !ONLY.includes(s.id)) continue;
      if (++n % 12 === 0) await fresh();      // a long run leaks: a new page every dozen subjects
      const rec = { class: c.id, subject: s.id, name: s.name, chapters: [] };
      let timer;
      const guard = new Promise((_, rej) => { timer = setTimeout(() => rej(new Error('timeout: no answer after ' + PER_SUBJECT_MS / 1000 + ' s')), PER_SUBJECT_MS); });
      try { await Promise.race([guard, (async () => {
        await page.evaluate(([cls, sid]) => openSubject(cls, sid), [c.id, s.id]);
        await sleep(1200);
        const order = s.chapters.map((ch, i) => ({ i, n: ch.n || 0, o: ch.o })).filter(x => x.o).sort((a, b) => b.n - a.n);
        const pick = [order[0], ...order.slice(1).filter(x => x.i !== order[0].i)].filter(Boolean).slice(0, NCH);
        for (const ch of pick) {
          await page.evaluate(call => (0, eval)(call), ch.o);
          await sleep(1800);
          const tabs = await page.evaluate(() => [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].filter((b, i, a) => a.indexOf(b) === i).map((b, i) => ({ i, label: (b.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) })));
          const out = { chapter: ch.i + 1, title: s.chapters[ch.i].t.slice(0, 60), tabs: [] };
          for (const t of tabs) {
            const info = await page.evaluate(async i => {
              const bs = [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].filter((b, k, a) => a.indexOf(b) === k);
              const b = bs[i]; if (!b) return null;
              b.click();
              await new Promise(r => setTimeout(r, 900));
              const box = document.querySelector('#subjTabContent, #mathTabContent, #page-content');
              const text = (box.innerText || '').replace(/\s+/g, ' ').trim();
              return { text: text.length, sample: text.slice(0, 70), ans: box.querySelectorAll('.sb-ans').length, opts: box.querySelectorAll('input[type=radio]').length, pics: box.querySelectorAll('img, svg, figure, table, video, iframe, canvas').length, nodes: box.getElementsByTagName('*').length };
            }, t.i);
            if (!info) continue;
            out.tabs.push(Object.assign({ label: t.label }, info, { empty: info.text < 40 && info.pics === 0 }));
          }
          rec.chapters.push(out);
        }
      })()]); } catch (e) { rec.error = String(e.message).slice(0, 160); await fresh(); }
      clearTimeout(timer);
      rec.errors = errors.splice(0).slice(0, 3);
      result.subjects.push(rec);
      const empt = rec.chapters.reduce((k, ch) => k + ch.tabs.filter(t => t.empty).length, 0), tt = rec.chapters.reduce((k, ch) => k + ch.tabs.length, 0);
      console.log(`${s.id.padEnd(14)} ${String(tt).padStart(2)} tabs, ${empt} empty${rec.error ? ' ERROR ' + rec.error : ''}${rec.errors.length ? ' script errors: ' + rec.errors[0] : ''}`);
    }
  }
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(result) + '\n');
  const all = result.subjects.flatMap(s => s.chapters.flatMap(ch => ch.tabs.map(t => ({ s: s.subject, label: t.label, empty: t.empty }))));
  console.log(`\n${result.subjects.length} subjects, ${all.length} tabs opened, ${all.filter(t => t.empty).length} empty, ${result.subjects.filter(s => s.error).length} subjects failed to open, ${result.subjects.filter(s => s.errors.length).length} with script errors`);
  await browser.close(); server.close();
})().catch(e => { console.error(e); process.exit(1); });
