'use strict';
/* Loading speed in a real Chrome: cold load, repeat load, opening a book, a chapter and its exercise, with the bytes that crossed the wire.
 *   node --max-old-space-size=3072 tools/launch/perf_browser.js [--profile desktop|phone|slowphone] [--page lazy.html] [--runs 3] [--out file.json]
 *                                                               [--subjects cls1-eng,cls5-math,...] [--root <folder of the site>]
 * Profiles (Chrome DevTools throttling, applied with the DevTools protocol):
 *   desktop    no throttling
 *   phone      CPU 4x slower, "Fast 3G" (1.6 Mbit/s down, 750 kbit/s up, 150 ms round trip): a modest phone on a poor connection
 *   slowphone  CPU 6x slower, "Slow 3G" (400 kbit/s, 400 ms): the worst case worth designing for
 * The site is served by a small static server that behaves like the host: gzip, ETag / 304 for pages, immutable caching for ?v=<hash> files (deploy/spacebook.htaccess).
 * Every number is the median of --runs fresh browser contexts; the file says which Chrome ran it. Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib'), crypto = require('crypto'), os = require('os');
const ROOT0 = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const ROOT = path.resolve(opt('--root', ROOT0));
const PROFILE = opt('--profile', 'phone');
const PAGE = opt('--page', 'lazy.html');
const RUNS = +opt('--runs', 3);
const OUT = opt('--out', null);
const WIDTH = +opt('--width', 0);
const SUBJECTS = opt('--subjects', 'cls1-eng,cls5-math,cls8-eng,cls9-bio,cls10-urdu,cls11-math,cls12-stat').split(',');
const PROFILES = {
  desktop: { cpu: 1, net: null },
  phone: { cpu: 4, net: { latency: 150, downloadThroughput: 1.6 * 1024 * 1024 / 8, uploadThroughput: 750 * 1024 / 8 } },
  slowphone: { cpu: 6, net: { latency: 400, downloadThroughput: 400 * 1024 / 8, uploadThroughput: 400 * 1024 / 8 } },
};
if (!PROFILES[PROFILE]) { console.error('unknown profile ' + PROFILE); process.exit(2); }
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.webmanifest': 'application/manifest+json', '.mp3': 'audio/mpeg', '.ico': 'image/x-icon' };
const GZ = /\.(html|js|css|json|svg|webmanifest|ttf)$/i;

function startServer() {
  const cache = new Map();
  return new Promise(resolve => {
    const server = http.createServer((req, res) => {
      const u = new URL(req.url, 'http://x');
      let f = path.join(ROOT, decodeURIComponent(u.pathname));
      if (u.pathname.endsWith('/')) f += PAGE;
      if (!f.startsWith(ROOT) || /[\\/]api[\\/]/.test(f)) { res.writeHead(u.pathname.startsWith('/api/') ? 404 : 403); return res.end('{"ok":false}'); }
      let ent = cache.get(f);
      if (!ent) {
        if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
        const buf = fs.readFileSync(f), st = fs.statSync(f);
        ent = { buf, etag: '"' + crypto.createHash('md5').update(buf).digest('hex').slice(0, 16) + '"', mtime: st.mtime.toUTCString(), gz: GZ.test(f) ? zlib.gzipSync(buf, { level: 6 }) : null, type: TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream' };
        cache.set(f, ent);
      }
      const hashed = /(^|&)v=[0-9a-f]{12}(&|$)/.test(u.search.slice(1)) && /\.(js|css|json)$/.test(f);
      const hdr = { 'Content-Type': ent.type, ETag: ent.etag, 'Last-Modified': ent.mtime, 'Cache-Control': hashed ? 'public, max-age=31536000, immutable' : (/\.(woff2?|png|jpe?g|webp|svg|ico)$/i.test(f) ? 'public, max-age=604800' : 'no-cache'), Vary: 'Accept-Encoding' };
      if (req.headers['if-none-match'] === ent.etag) { res.writeHead(304, hdr); return res.end(); }
      const gz = ent.gz && /gzip/.test(req.headers['accept-encoding'] || '');
      if (gz) hdr['Content-Encoding'] = 'gzip';
      const body = gz ? ent.gz : ent.buf;
      hdr['Content-Length'] = body.length;
      res.writeHead(200, hdr); res.end(body);
    });
    server.listen(0, '127.0.0.1', () => resolve({ server, url: 'http://127.0.0.1:' + server.address().port + '/' }));
  });
}

const median = a => { const s = a.filter(x => x != null && !isNaN(x)).sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : null; };
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function run() {
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const { server, url } = await startServer();
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  const version = browser.version();
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  const findSubject = id => { for (const c of catalog.classes) for (const s of c.subjects) if (s.id === id) return { cls: c.id, subj: s }; return null; };
  const P = PROFILES[PROFILE];
  const runs = [];
  for (let r = 0; r < RUNS; r++) {
    const ctx = await browser.newContext({ viewport: WIDTH ? { width: WIDTH, height: 800 } : (PROFILE === 'desktop' ? { width: 1280, height: 800 } : { width: 390, height: 844 }), hasTouch: PROFILE !== 'desktop', isMobile: PROFILE !== 'desktop' });
    const page = await ctx.newPage();
    const cdp = await ctx.newCDPSession(page);
    await cdp.send('Network.enable');
    await cdp.send('Performance.enable');
    let bytes = 0, reqs = 0;
    cdp.on('Network.loadingFinished', e => { bytes += e.encodedDataLength || 0; reqs++; });
    const resetNet = () => { const o = { bytes, reqs }; bytes = 0; reqs = 0; return o; };
    if (P.cpu > 1) await cdp.send('Emulation.setCPUThrottlingRate', { rate: P.cpu });
    if (P.net) await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: P.net.latency, downloadThroughput: P.net.downloadThroughput, uploadThroughput: P.net.uploadThroughput });
    await page.addInitScript(() => {
      window.__perf = { fcp: null, lcp: null, longTasks: 0, longMs: 0 };
      try { new PerformanceObserver(l => { for (const e of l.getEntries()) if (e.name === 'first-contentful-paint') window.__perf.fcp = e.startTime; }).observe({ type: 'paint', buffered: true }); } catch (e) { /* older engine */ }
      try { new PerformanceObserver(l => { for (const e of l.getEntries()) window.__perf.lcp = e.startTime; }).observe({ type: 'largest-contentful-paint', buffered: true }); } catch (e) { /* older engine */ }
      try { new PerformanceObserver(l => { for (const e of l.getEntries()) { window.__perf.longTasks++; window.__perf.longMs += e.duration; } }).observe({ type: 'longtask', buffered: true }); } catch (e) { /* older engine */ }
    });
    const rec = { run: r, load: {}, subjects: {} };
    const ready = () => page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 240000 });
    for (const phase of ['cold', 'repeat', 'repeat2']) {
      resetNet();
      const t0 = Date.now();
      await page.goto(url + PAGE, { waitUntil: 'load', timeout: 240000 });
      const tLoad = Date.now() - t0;
      await ready();
      const tReady = Date.now() - t0;
      const m = await page.evaluate(() => { const n = performance.getEntriesByType('navigation')[0]; return { dcl: n.domContentLoadedEventEnd, loadEnd: n.loadEventEnd, fcp: window.__perf.fcp, lcp: window.__perf.lcp, longTasks: window.__perf.longTasks, longMs: Math.round(window.__perf.longMs), heap: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null, nodes: document.getElementsByTagName('*').length }; });
      const net = resetNet();
      rec.load[phase] = Object.assign({ loadMs: tLoad, readyMs: tReady, kb: Math.round(net.bytes / 1024), requests: net.reqs }, m);
      if (phase === 'cold') { await sleep(3000); await page.evaluate(() => navigator.serviceWorker && navigator.serviceWorker.ready).catch(() => {}); }   // the service worker installs after the first load
    }
    await sleep(4000);
    // books: each opened from the start page, first with nothing loaded (cold = the book's data file comes over the network), then another chapter (warm)
    for (const sid of SUBJECTS) {
      const f = findSubject(sid);
      if (!f) { rec.subjects[sid] = { error: 'not in the catalog' }; continue; }
      await page.goto(url + PAGE, { waitUntil: 'load' }); await ready(); await sleep(3500);
      const out = { name: f.subj.name, cls: f.cls, chapters: f.subj.chapters.length };
      resetNet();
      let t = await page.evaluate(async (a) => {
        const t0 = performance.now();
        try { openSubject(a.cls, a.sid); } catch (e) { return { error: String(e) }; }
        const end = performance.now() + 120000;
        while (performance.now() < end) {
          if (typeof state !== 'undefined' && state.activeView === 'subject-detail' && document.querySelector('#page-content').innerHTML.length > 2500) break;
          await new Promise(r => setTimeout(r, 16));
        }
        return { ms: Math.round(performance.now() - t0) };
      }, { cls: f.cls, sid });
      let n = resetNet();
      out.openBook = Object.assign({ kb: Math.round(n.bytes / 1024), requests: n.reqs }, t);
      // the first chapter that has an exercise is not known up front: open the chapter the catalog calls "n" biggest in exercises among the first six
      const cand = f.subj.chapters.map((c, i) => ({ i, n: c.n || 0, o: c.o })).filter(c => c.o).slice(0, 8).sort((a, b) => b.n - a.n)[0] || f.subj.chapters.map((c, i) => ({ i, o: c.o })).find(c => c.o);
      if (!cand) { rec.subjects[sid] = out; continue; }
      await sleep(500);
      t = await page.evaluate(async (call) => {
        const t0 = performance.now();
        const before = document.querySelector('#page-content').innerHTML.length;
        try { (0, eval)(call); } catch (e) { return { error: String(e) }; }
        const end = performance.now() + 120000;
        let last = -1, stable = 0;
        while (performance.now() < end) {
          const len = document.querySelector('#page-content').innerHTML.length;
          if (len !== before && len > 800 && window.SBLibrary && SBLibrary.collect().units.length > 0) break;
          await new Promise(r => setTimeout(r, 16));
        }
        const ms = Math.round(performance.now() - t0);
        await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
        return { ms, msPainted: Math.round(performance.now() - t0), nodes: document.getElementsByTagName('*').length, htmlKB: Math.round(document.querySelector('#page-content').innerHTML.length / 1024), heap: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null };
      }, cand.o);
      n = resetNet();
      out.openChapter = Object.assign({ chapter: cand.i + 1, kb: Math.round(n.bytes / 1024), requests: n.reqs }, t);
      // the exercise tab of that chapter
      await sleep(400);
      t = await page.evaluate(async () => {
        const tabs = [...document.querySelectorAll('.math-nav-tabs button, .topic-sub-tabs-bar button')];
        const b = tabs.find(x => /exercise/i.test(x.textContent || '')) || tabs.find(x => /question|مشق|تمرین|مشغول/i.test(x.textContent || ''));
        if (!b) return { error: 'no exercise tab', tabs: tabs.map(x => (x.textContent || '').trim().slice(0, 20)) };
        const before = document.querySelector('#page-content').innerHTML.length;
        const t0 = performance.now();
        b.click();
        const end = performance.now() + 120000;
        while (performance.now() < end) { if (document.querySelector('#page-content').innerHTML.length !== before) break; await new Promise(r => setTimeout(r, 16)); }
        const ms = Math.round(performance.now() - t0);
        await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
        return { ms, msPainted: Math.round(performance.now() - t0), tab: (b.textContent || '').trim().slice(0, 24), nodes: document.getElementsByTagName('*').length, htmlKB: Math.round(document.querySelector('#page-content').innerHTML.length / 1024) };
      });
      out.openExercise = t;
      rec.subjects[sid] = out;
    }
    runs.push(rec);
    await ctx.close();
    console.log('run ' + (r + 1) + '/' + RUNS + ' done');
  }
  await browser.close();
  server.close();

  // medians over the runs
  const res = { schema: 'spacebook.perf-browser/1', chrome: version, profile: PROFILE, cpuThrottle: P.cpu, network: P.net ? { latencyMs: P.net.latency, downKbit: Math.round(P.net.downloadThroughput * 8 / 1024), upKbit: Math.round(P.net.uploadThroughput * 8 / 1024) } : 'none',
    page: PAGE, runs: RUNS, machine: { cpus: os.cpus().length, cpu: os.cpus()[0].model.trim(), ramGB: Math.round(os.totalmem() / 1073741824) }, load: {}, subjects: {} };
  for (const ph of ['cold', 'repeat', 'repeat2']) {
    const keys = Object.keys(runs[0].load[ph]);
    res.load[ph] = Object.fromEntries(keys.map(k => [k, Math.round(median(runs.map(x => x.load[ph][k])) * 10) / 10]));
  }
  for (const sid of SUBJECTS) {
    const all = runs.map(x => x.subjects[sid]).filter(Boolean);
    if (!all.length || all[0].error) { res.subjects[sid] = all[0] || { error: 'missing' }; continue; }
    const o = { name: all[0].name, cls: all[0].cls, chapters: all[0].chapters };
    for (const st of ['openBook', 'openChapter', 'openExercise']) {
      if (!all[0][st]) continue;
      const keys = Object.keys(all[0][st]).filter(k => typeof all[0][st][k] === 'number');
      o[st] = Object.fromEntries(keys.map(k => [k, median(all.map(x => x[st] && x[st][k]))]));
      if (all[0][st].error) o[st].error = all[0][st].error;
      if (all[0][st].tab) o[st].tab = all[0][st].tab;
    }
    res.subjects[sid] = o;
  }
  if (OUT) { fs.mkdirSync(path.dirname(path.resolve(OUT)), { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(res, null, 1) + '\n'); }
  const f = x => (x == null ? '-' : x);
  console.log(`\n${PROFILE}: Chrome ${version}, ${RUNS} runs, median`);
  for (const ph of ['cold', 'repeat']) { const l = res.load[ph]; console.log(`${ph.padEnd(7)} load ${f(l.loadMs)} ms, ready ${f(l.readyMs)} ms, FCP ${f(l.fcp)}, LCP ${f(l.lcp)}, ${f(l.kb)} KB in ${f(l.requests)} requests, long tasks ${f(l.longTasks)} (${f(l.longMs)} ms), heap ${f(l.heap)} MB`); }
  for (const sid of SUBJECTS) {
    const s = res.subjects[sid]; if (!s || s.error) { console.log(sid, s && s.error); continue; }
    console.log(`${sid.padEnd(12)} book ${f(s.openBook && s.openBook.ms)} ms (${f(s.openBook && s.openBook.kb)} KB)  chapter ${f(s.openChapter && s.openChapter.ms)} ms (${f(s.openChapter && s.openChapter.kb)} KB, ${f(s.openChapter && s.openChapter.nodes)} nodes, ${f(s.openChapter && s.openChapter.htmlKB)} KB html)  exercise ${f(s.openExercise && s.openExercise.ms)} ms (${f(s.openExercise && s.openExercise.nodes)} nodes)${s.openExercise && s.openExercise.error ? ' ' + s.openExercise.error : ''}`);
  }
}
run().catch(e => { console.error(e); process.exit(1); });
