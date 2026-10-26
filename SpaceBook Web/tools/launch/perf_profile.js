'use strict';
/* Where the time goes when a book, a chapter or a tab is opened: a Chrome CPU profile around one action, summarised by script file and by function.
 *   node --max-old-space-size=3072 tools/launch/perf_profile.js --subject cls5-math [--chapter 3] [--tab Exercise] [--cpu 1] [--top 25] [--root <site folder>]
 * It opens the start page, waits until the app has started, then profiles (a) openSubject, (b) the chapter, (c) the tab, one after the other, and prints for each:
 * wall time, and the heaviest scripts and functions by SELF time (time inside the function itself), plus the share spent in layout / style / parse / GC reported by the
 * profile's own idle / program / garbage-collector nodes. Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT0 = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const ROOT = path.resolve(opt('--root', ROOT0));
const SUBJECT = opt('--subject', 'cls5-math'), CHAPTER = +opt('--chapter', 3), TAB = opt('--tab', 'Exercise'), CPU = +opt('--cpu', 1), TOP = +opt('--top', 25);
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json' };
const sleep = ms => new Promise(r => setTimeout(r, ms));

function serve() {
  return new Promise(resolve => {
    const cache = new Map();
    const s = http.createServer((req, res) => {
      const u = new URL(req.url, 'http://x');
      let f = path.join(ROOT, decodeURIComponent(u.pathname)); if (u.pathname.endsWith('/')) f += 'lazy.html';
      if (!f.startsWith(ROOT) || /[\\/]api[\\/]/.test(f) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
      let e = cache.get(f); if (!e) { const b = fs.readFileSync(f); e = { b, gz: /\.(html|js|css|json|svg)$/.test(f) ? zlib.gzipSync(b) : null }; cache.set(f, e); }
      const gz = e.gz && /gzip/.test(req.headers['accept-encoding'] || '');
      res.writeHead(200, Object.assign({ 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }, gz ? { 'Content-Encoding': 'gzip' } : {})); res.end(gz ? e.gz : e.b);
    });
    s.listen(0, '127.0.0.1', () => resolve({ s, url: 'http://127.0.0.1:' + s.address().port + '/' }));
  });
}

function summarise(profile, label, wallMs) {
  const nodes = new Map(profile.nodes.map(n => [n.id, n]));
  const dt = profile.timeDeltas, self = new Map();
  profile.samples.forEach((id, i) => self.set(id, (self.get(id) || 0) + (dt[i] || 0)));
  const byFn = new Map(), byFile = new Map(); let total = 0, idle = 0, gc = 0, program = 0;
  for (const [id, us] of self) {
    const n = nodes.get(id), cf = n.callFrame, name = cf.functionName || '(anonymous)';
    total += us;
    if (name === '(idle)') { idle += us; continue; }
    if (name === '(garbage collector)') { gc += us; continue; }
    if (name === '(program)') { program += us; continue; }
    const file = (cf.url || '(native)').replace(/^https?:\/\/[^/]+\//, '').replace(/\?.*$/, '');
    const k = name + ' ' + file + ':' + cf.lineNumber;
    byFn.set(k, (byFn.get(k) || 0) + us);
    byFile.set(file, (byFile.get(file) || 0) + us);
  }
  const ms = us => Math.round(us / 100) / 10;
  console.log(`\n== ${label}: ${wallMs} ms wall, ${ms(total - idle)} ms busy (JS ${ms(total - idle - gc - program)}, garbage collection ${ms(gc)}, browser work outside JS: style, layout, paint, parsing ${ms(program)}), idle ${ms(idle)}`);
  console.log('   by script file (self time, ms):');
  [...byFile].sort((a, b) => b[1] - a[1]).slice(0, 10).forEach(([k, v]) => console.log('     ' + String(ms(v)).padStart(8) + '  ' + k));
  console.log('   by function:');
  [...byFn].sort((a, b) => b[1] - a[1]).slice(0, TOP).forEach(([k, v]) => console.log('     ' + String(ms(v)).padStart(8) + '  ' + k));
}

(async () => {
  const { chromium } = require('playwright');
  const { s, url } = await serve();
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}), args: args.includes('--noinline') ? ['--js-flags=--max-inlined-bytecode-size=0 --no-turbo-inlining'] : [] });
  const page = await (await browser.newContext({ viewport: { width: +opt('--width', 1280), height: 800 } })).newPage();
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Profiler.enable');
  await cdp.send('Profiler.setSamplingInterval', { interval: 200 });
  if (CPU > 1) await cdp.send('Emulation.setCPUThrottlingRate', { rate: CPU });
  await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 240000 });
  await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 240000 });
  await sleep(5000);
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  let cls = null, subj = null;
  for (const c of catalog.classes) for (const x of c.subjects) if (x.id === SUBJECT) { cls = c.id; subj = x; }
  const call = subj.chapters[CHAPTER - 1].o;
  const step = async (label, fn, arg) => {
    await cdp.send('Profiler.start');
    const t0 = Date.now();
    await page.evaluate(fn, arg);
    const wall = Date.now() - t0;
    const { profile } = await cdp.send('Profiler.stop');
    summarise(profile, label, wall);
  };
  await step('openSubject ' + SUBJECT, async a => {
    openSubject(a.cls, a.sid);
    const end = performance.now() + 120000;
    while (performance.now() < end) { if (state.activeView === 'subject-detail' && document.querySelector('#page-content').innerHTML.length > 2500) break; await new Promise(r => setTimeout(r, 16)); }
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, { cls, sid: SUBJECT });
  await sleep(800);
  await step('chapter ' + CHAPTER + ' (' + call + ')', async c => {
    const before = document.querySelector('#page-content').innerHTML.length;
    (0, eval)(c);
    const end = performance.now() + 120000;
    while (performance.now() < end) { const l = document.querySelector('#page-content').innerHTML.length; if (l !== before && l > 800 && SBLibrary.collect().units.length > 0) break; await new Promise(r => setTimeout(r, 16)); }
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, call);
  await sleep(800);
  await step('tab ' + TAB, async t => {
    const b = [...document.querySelectorAll('.math-nav-tabs button, .topic-sub-tabs-bar button')].find(x => new RegExp(t, 'i').test(x.textContent || ''));
    if (!b) return;
    const before = document.querySelector('#page-content').innerHTML.length;
    b.click();
    const end = performance.now() + 120000;
    while (performance.now() < end) { if (document.querySelector('#page-content').innerHTML.length !== before) break; await new Promise(r => setTimeout(r, 16)); }
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, TAB);
  console.log('\nnodes in the page now: ' + await page.evaluate(() => document.getElementsByTagName('*').length));
  await browser.close(); s.close();
})().catch(e => { console.error(e); process.exit(1); });
