'use strict';
/* The app in a real DOM (jsdom), for the things the plain sandbox cannot show: what MutationObserver-driven scripts do to a page after it
 * is drawn. Timers and animation frames are queued and run by settle(), so a test decides when "later" happens.
 *   const { loadDom } = require('./lib/app_dom');
 *   const app = await loadDom({ page: 'lazy.html' });
 *   app.run("openSubject('cls9', 'cls9-bio')"); await app.settle();
 *   app.html('dashboard-body')
 * Dev-only; never shipped. Needs the dev dependency jsdom. */
const fs = require('fs'), vm = require('vm'), path = require('path');
const { ROOT } = require('./app_sandbox');

async function loadDom(opts = {}) {
  const { JSDOM } = require('jsdom');
  const page = opts.page || 'lazy.html';
  const html = fs.readFileSync(path.join(ROOT, page), 'utf8');
  const items = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)].map(m => {
    const src = (m[1].match(/\bsrc="([^"]+)"/) || [])[1];
    if (src) return { src: src.split('?')[0] };
    return /^\s*(?:window\.SB_LAZY_MANIFEST\s*=|SBLazy\.attachData\()/.test(m[2]) ? { inline: m[2] } : null;
  }).filter(Boolean);
  const bare = html.replace(/<script\b[\s\S]*?<\/script>/g, '');          // scripts are run below, in order, by this loader
  // 'dangerously' so that onclick="..." attributes run like in a browser (the page's own scripts are stripped and run below, in order)
  const dom = new JSDOM(bare, { url: 'http://localhost/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window, ctx = dom.getInternalVMContext();
  const timers = new Map(); let nextId = 1;
  win.setTimeout = (fn, ms, ...a) => { const id = nextId++; timers.set(id, { fn: () => fn(...a), ms: ms || 0 }); return id; };
  win.clearTimeout = id => { timers.delete(id); };
  win.setInterval = () => 0; win.clearInterval = () => { };
  win.requestAnimationFrame = fn => win.setTimeout(() => fn(Date.now()), 16);
  win.cancelAnimationFrame = id => win.clearTimeout(id);
  win.requestIdleCallback = fn => win.setTimeout(() => fn({ timeRemaining: () => 10 }), 0);
  win.matchMedia = win.matchMedia || (() => ({ matches: false, addEventListener() { }, addListener() { } }));
  win.scrollTo = () => { }; win.alert = () => { }; win.open = () => null;
  win.HTMLElement.prototype.scrollIntoView = function () { };
  win.fetch = () => Promise.reject(new Error('offline in the DOM test'));
  win.speechSynthesis = { getVoices: () => [], speak() { }, cancel() { }, pause() { }, resume() { }, addEventListener() { } };
  win.SB_LAZY_FETCH = url => fs.readFileSync(path.join(ROOT, url.split('?')[0]), 'utf8');
  if (opts.beforeScripts) opts.beforeScripts(win);
  const fails = [];
  for (const it of items) {
    const code = it.inline || fs.readFileSync(path.join(ROOT, it.src), 'utf8');
    win.__sbCurrentSrc = it.src || 'inline';
    try { new vm.Script(code, { filename: it.src || 'inline' }).runInContext(ctx, { timeout: 60000 }); }
    catch (e) { fails.push((it.src || 'inline') + ': ' + (e && e.message)); }
  }
  const run = code => vm.runInContext(code, ctx, { timeout: opts.timeout || 120000 });
  if (!opts.anonymous) { try { run(require('./test_access')); } catch (e) { /* no access module */ } }      // every chapter open, as for a person with every plan (opts.anonymous: as a visitor)
  // Let "later" happen: deliver mutation records (microtasks), run queued timers by their delay, repeat until nothing is waiting.
  async function settle(max = 40) {
    for (let i = 0; i < max; i++) {
      await new Promise(r => setImmediate(r));
      await Promise.resolve();
      if (!timers.size) { await new Promise(r => setImmediate(r)); if (!timers.size) return i; }
      const due = [...timers.entries()].sort((a, b) => a[1].ms - b[1].ms);
      timers.clear();
      for (const [, t] of due) { try { t.fn(); } catch (e) { /* a script's own timer error */ } }
    }
    return max;
  }
  const html_ = id => { const el = win.document.getElementById(id); return el ? el.innerHTML : ''; };
  return { dom, win, ctx, run, settle, html: html_, fails, pending: () => timers.size };
}

module.exports = { loadDom };
