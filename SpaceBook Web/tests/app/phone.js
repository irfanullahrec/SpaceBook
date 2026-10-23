'use strict';
/* The website as the Android app shows it: lazy.html in a phone-sized Chrome with the app's own reader_mobile.css and reader_bridge.js
 * injected the way SbWebView does. Local only (needs the installed Chrome and the sibling "SpaceBook App" folder); never shipped.
 *
 *   const { open } = require('./phone');
 *   const t = await open({ width: 390, height: 780 });      // t.page, t.shot(name), t.close()
 *   await t.chapter('cls5', 'cls5-math', "selectSubjectChapter('math', 2, 'cls5')");
 *
 * As a command: node tests/app/phone.js <classId> <subjectId> "<chapter call>" [tab] [outdir] */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const APP_ASSETS = path.resolve(__dirname, '..', '..', '..', 'SpaceBook App', 'app', 'src', 'main', 'assets');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function open(opts = {}) {
  const width = opts.width || 390, height = opts.height || 780;
  const out = path.resolve(opts.out || path.join(os.tmpdir(), 'sb_phone_shots'));
  fs.mkdirSync(out, { recursive: true });
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: opts.scale || 1, isMobile: true, hasTouch: true,
    userAgent: 'Mozilla/5.0 (Linux; Android 14; SM-A146P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36 SpaceBookApp/test' });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::|api\//.test(m.text())) errors.push('console: ' + m.text()); });
  const css = fs.readFileSync(path.join(APP_ASSETS, 'reader_mobile.css'), 'utf8');
  const bridge = fs.readFileSync(path.join(APP_ASSETS, 'reader_bridge.js'), 'utf8');
  // what the app injects after the page loads
  await page.goto(url + (opts.entry || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  await page.waitForFunction(() => typeof window.openSubject === 'function' && window.SBSolve, null, { timeout: 120000 });
  await page.evaluate(c => { const s = document.createElement('style'); s.id = 'sbapp-css'; s.textContent = c; document.head.appendChild(s); document.documentElement.classList.add('sbapp'); }, css);
  await page.evaluate(bridge);
  for (const f of opts.extra || []) await page.addScriptTag({ path: f });
  // when did the page last change? (a big chapter keeps drawing for a few seconds)
  await page.evaluate(() => { window.__lastMut = Date.now(); new MutationObserver(ms => { if (ms.some(m => m.type === 'childList')) window.__lastMut = Date.now(); }).observe(document.body, { childList: true, subtree: true }); });
  const t = {
    page, errors, url, out, server, browser,
    shot: async (name, o) => { const f = path.join(out, name + '.png'); await page.screenshot({ path: f, ...(o || {}) }); return f; },
    chapter: (cls, subj, call, start, tab) => page.evaluate(([a, b, c, d, e]) => window.SBApp.open(a, b, c, d == null ? 0 : d, e || ''), [cls, subj, call, start, tab]),
    state: () => page.evaluate(() => window.SBApp.state()),
    // wait until the page count has not changed for a moment (the chapter renders in two steps)
    settle: async (ms = 700, max = 15000) => {
      let last = '', since = Date.now(); const end = Date.now() + max;
      while (Date.now() < end) {
        const s = JSON.stringify(await page.evaluate(() => { const a = window.SBApp.state(); return [a.pages, a.tab, a.page, document.querySelectorAll('.sbapp-hide').length]; }));
        const quiet = await page.evaluate(() => Date.now() - window.__lastMut);
        if (s !== last) { last = s; since = Date.now(); } else if (Date.now() - since >= ms && quiet >= ms + 300) return JSON.parse(s);
        await sleep(120);
      }
      return JSON.parse(last);
    },
    close: async () => { await browser.close(); server.close(); },
  };
  return t;
}

module.exports = { open, sleep, APP_ASSETS };

if (require.main === module) {
  (async () => {
    const [cls, subj, call, tab, outdir] = process.argv.slice(2);
    const t = await open({ out: outdir });
    try {
      await t.chapter(cls, subj, call, 0, tab);
      await sleep(1200);
      console.log(JSON.stringify(await t.state()));
      console.log(await t.shot('reader'));
      if (t.errors.length) console.log(t.errors.join('\n'));
    } finally { await t.close(); }
  })().catch(e => { console.error(e); process.exit(1); });
}
