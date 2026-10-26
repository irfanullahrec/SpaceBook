'use strict';
/* A speed fix must not change what the student sees. This opens the same chapters and tabs in two copies of the website (a "before" folder and this one) in a
 * real Chrome and compares the text and the structure of what is drawn.
 *   node --max-old-space-size=3072 tests/launch/render_equivalence.js --before "D:/SpaceBook_perf_before/SpaceBook Web" [--classes 1,5,11] [--width 1280] [--per 1]
 *        [--only cls5-math,cls5-isl] [--context 50] [--show 12]
 * For each subject: the first chapter that has an exercise (--per N: the first N), every tab. Compared: the visible text, the number of .sb-ans buttons, the
 * number of elements of each class name that matters (cards, pages, questions), with random ids and generated numbers removed. A difference is printed with
 * the first place where the text differs (--context: how many characters after it). Each tab is read when its text has stopped changing, and the small buttons
 * that other scripts add some time after a page is drawn (colouring, tracing, speaker) are left out: their moment differs between two runs, the content does not.
 * Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const BEFORE = path.resolve(opt('--before', ''));
const CLASSES = opt('--classes', '1,2,3,4,5,6,7,8,9,10,11,12').split(',').map(x => 'cls' + x.trim());
const WIDTH = +opt('--width', 1280), PER = +opt('--per', 1), ONLY = opt('--only', '') ? opt('--only', '').split(',') : null, CTX = +opt('--context', 50);
if (!fs.existsSync(path.join(BEFORE, 'lazy.html'))) { console.error('--before must be a folder with lazy.html'); process.exit(2); }
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json' };
const sleep = ms => new Promise(r => setTimeout(r, ms));
function serve(root) {
  const cache = new Map();
  return new Promise(res => {
    const s = http.createServer((req, rs) => {
      const u = new URL(req.url, 'http://x'); let f = path.join(root, decodeURIComponent(u.pathname)); if (u.pathname.endsWith('/')) f += 'lazy.html';
      if (!f.startsWith(root) || /[\\/]api[\\/]/.test(f) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rs.writeHead(404); return rs.end(); }
      let e = cache.get(f); if (!e) { const b = fs.readFileSync(f); e = { b, gz: /\.(html|js|css|json|svg)$/.test(f) ? zlib.gzipSync(b, { level: 1 }) : null }; if (b.length < 3e7) cache.set(f, e); }
      const gz = e.gz && /gzip/.test(req.headers['accept-encoding'] || '');
      rs.writeHead(200, Object.assign({ 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }, gz ? { 'Content-Encoding': 'gzip' } : {})); rs.end(gz ? e.gz : e.b);
    });
    s.listen(0, '127.0.0.1', () => res({ s, url: 'http://127.0.0.1:' + s.address().port + '/' }));
  });
}
const snapshot = async page => page.evaluate(() => {
  const box = document.querySelector('#subjTabContent, #mathTabContent, #page-content');
  // textContent, not innerText: content-visibility skips off-screen spreads for innerText (and only for it); the content is all there
  const clone = box.cloneNode(true); clone.querySelectorAll('.bk-nav, .sbl-tools, .sbl-flash, script, style, template').forEach(x => x.remove());
  // buttons that other scripts add some time after a page is drawn (colouring, tracing, speaker): their moment, not the content, differs between two runs
  clone.querySelectorAll('button').forEach(b => { if (/^(\u270F\uFE0F? ?Draw \/ Colour|\u21BA ?Trace again|\uD83D\uDD0A+)$/.test((b.textContent || '').trim())) b.remove(); });
  const text = (clone.textContent || '').replace(/\s+/g, ' ').replace(/\d{6,}/g, '#').trim();
  const count = sel => box.querySelectorAll(sel).length;
  return { text, ans: count('.sb-ans'), pages: count('.bk-page'), spreads: count('.bk-wrap'), cards: count('[class*="card"]'), q: count('[class*="-q"], .m6-qno'), tables: count('table'), imgs: count('img, svg') };
});

(async () => {
  const a = await serve(BEFORE), b = await serve(ROOT);
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  const open = async url => {
    const ctx = await browser.newContext({ viewport: { width: WIDTH, height: 900 } }); const page = await ctx.newPage();
    await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 180000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 180000 });
    await sleep(4000);
    return page;
  };
  let pa = await open(a.url), pb = await open(b.url);
  let n = 0, tabs = 0, diffs = [];
  for (const c of catalog.classes) {
    if (!CLASSES.includes(c.id)) continue;
    for (const s of c.subjects) {
      if (ONLY && !ONLY.includes(s.id)) continue;
      if (++n % 15 === 0) { await pa.context().close(); await pb.context().close(); pa = await open(a.url); pb = await open(b.url); }
      const order = s.chapters.map((ch, i) => ({ i, n: ch.n || 0, o: ch.o })).filter(x => x.o).sort((x, y) => y.n - x.n).slice(0, PER);
      for (const ch of order) {
        for (const p of [pa, pb]) { await p.evaluate(([cls, sid, call]) => { openSubject(cls, sid); }, [c.id, s.id, ch.o]); }
        await sleep(1200);
        for (const p of [pa, pb]) { await p.evaluate(call => (0, eval)(call), ch.o); }
        await sleep(2200);
        const labels = await pa.evaluate(() => [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].filter((x, i, arr) => arr.indexOf(x) === i).length);
        for (let t = 0; t < labels; t++) {
          const snap = [];
          for (const p of [pa, pb]) {
            // click the tab, then wait until the text has stopped changing (three equal readings, 400 ms apart, at most about 10 s)
            await p.evaluate(async i => {
              const bs = [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].filter((x, k, arr) => arr.indexOf(x) === k); if (bs[i]) bs[i].click();
              const box = document.querySelector('#subjTabContent, #mathTabContent, #page-content'); let last = -1, same = 0;
              for (let k = 0; k < 24 && same < 3; k++) { await new Promise(r => setTimeout(r, 400)); const len = box.textContent.length; same = len === last ? same + 1 : 0; last = len; }
            }, t);
            snap.push(await snapshot(p));
          }
          tabs++;
          const [x, y] = snap;
          const same = x.text === y.text && x.ans === y.ans && x.pages === y.pages && x.spreads === y.spreads && x.tables === y.tables && x.imgs === y.imgs && x.q === y.q;
          if (!same) {
            let k = 0; while (k < x.text.length && x.text[k] === y.text[k]) k++;
            diffs.push({ subject: s.id, chapter: ch.i + 1, tab: t, counts: [x.ans, y.ans, x.pages, y.pages, x.spreads, y.spreads, x.q, y.q], at: k, before: x.text.slice(Math.max(0, k - 30), k + CTX), after: y.text.slice(Math.max(0, k - 30), k + CTX) });
          }
        }
      }
      process.stdout.write('.');
    }
  }
  console.log(`\n${n} subjects, ${tabs} tabs compared, ${diffs.length} differ`);
  diffs.slice(0, +opt('--show', 12)).forEach(d => console.log(JSON.stringify(d)));
  await browser.close(); a.s.close(); b.s.close();
  process.exit(diffs.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
