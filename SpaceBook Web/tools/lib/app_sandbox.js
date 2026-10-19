'use strict';
/* Loads the app the way the browser does: every <script src> of index.html, in order, into one vm context
 * where window === globalThis, with a minimal DOM stub (innerHTML strings, no layout). Used by tools/smoke.js
 * and the tracer. Timers never fire, fetch rejects (offline), storage is in memory. Dev-only: never shipped.
 *   const { load } = require('./lib/app_sandbox'); const app = load(); app.run("openSubject('cls9','cls9-bio')");
 */
const fs = require('fs'), vm = require('vm'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');

function makeEl(id) {
  const style = {};
  return {
    _id: id, innerHTML: '', textContent: '', innerText: '', value: '', className: '', title: '', src: '', href: '',
    style: new Proxy(style, {
      get: (t, k) => (k in t ? t[k]
        : k === 'setProperty' ? (p, v) => { t[p] = v; }
        : k === 'removeProperty' ? p => { delete t[p]; }
        : k === 'getPropertyValue' ? p => t[p] || '' : ''),
      set: (t, k, v) => { t[k] = v; return true; }
    }),
    classList: { add() { }, remove() { }, toggle() { }, contains() { return false; } },
    dataset: {}, children: [], childNodes: [], scrollHeight: 100, scrollTop: 0, offsetHeight: 100, checked: false, disabled: false,
    addEventListener() { }, removeEventListener() { }, appendChild(x) { return x; }, append() { }, prepend() { },
    insertBefore(x) { return x; }, insertAdjacentHTML() { }, insertAdjacentElement() { }, removeChild() { }, remove() { },
    setAttribute() { }, getAttribute() { return null; }, hasAttribute() { return false; }, removeAttribute() { },
    focus() { }, click() { }, blur() { }, scrollIntoView() { }, scrollTo() { },
    querySelector() { return null; }, querySelectorAll() { return []; }, closest() { return null; },
    getElementsByTagName() { return []; }, getElementsByClassName() { return []; },
    getBoundingClientRect() { return { top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0 }; },
    contains() { return false; }, cloneNode() { return makeEl(); }, matches() { return false; }, dispatchEvent() { return true; }
  };
}

function memoryStorage() {
  const m = {};
  return { getItem: k => (k in m ? m[k] : null), setItem: (k, v) => { m[k] = String(v); }, removeItem: k => { delete m[k]; },
    key: i => Object.keys(m)[i] || null, get length() { return Object.keys(m).length; }, clear() { for (const k in m) delete m[k]; } };
}

function load(opts = {}) {
  const page = opts.page || 'index.html';
  const html = fs.readFileSync(path.join(ROOT, page), 'utf8');
  // scripts in page order; the only inline scripts run are the lazy-loading manifest and the attachData call of lazy.html (tools/build/make_lazy.js)
  const items = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)].map(m => {
    const src = (m[1].match(/\bsrc="([^"]+)"/) || [])[1];
    if (src) return { src: src.split('?')[0] };
    return /^\s*(?:window\.SB_LAZY_MANIFEST\s*=|SBLazy\.attachData\()/.test(m[2]) ? { inline: m[2] } : null;
  }).filter(Boolean);
  const srcs = items.filter(i => i.src).map(i => i.src);
  const registry = {};
  const document = {
    getElementById(id) { if (!registry[id]) registry[id] = makeEl(id); return registry[id]; },
    querySelector() { return null; }, querySelectorAll() { return []; }, getElementsByTagName() { return []; }, getElementsByClassName() { return []; },
    createElement() { return makeEl(); }, createElementNS() { return makeEl(); }, createTextNode() { return makeEl(); },
    createDocumentFragment() { return makeEl(); }, createTreeWalker() { return { nextNode: () => null }; },
    // a working event bus (tests dispatch 'spacebook:auth' and similar); nothing in the app dispatches on its own here
    _l: {}, addEventListener(t, fn) { (this._l[t] = this._l[t] || []).push(fn); }, removeEventListener(t, fn) { this._l[t] = (this._l[t] || []).filter(x => x !== fn); },
    dispatchEvent(e) { (this._l[e.type] || []).slice().forEach(fn => { try { fn(e); } catch (err) { /* like a browser, a listener error does not stop the others */ } }); return true; },
    body: makeEl('body'), documentElement: makeEl('html'), head: makeEl('head'), readyState: 'complete',
    fonts: { ready: Promise.resolve() }, location: { href: 'http://localhost/', search: '', hash: '', pathname: '/' }, cookie: ''
  };
  const g = {
    console: opts.console || console, document, location: document.location, localStorage: memoryStorage(), sessionStorage: memoryStorage(),
    navigator: { userAgent: 'smoke', onLine: false, language: 'en' }, innerWidth: 1400, innerHeight: 900,
    setTimeout: () => 0, clearTimeout() { }, setInterval: () => 0, clearInterval() { },
    requestAnimationFrame: () => 0, cancelAnimationFrame() { }, requestIdleCallback: () => 0,
    matchMedia: () => ({ matches: false, addEventListener() { }, addListener() { } }),
    getComputedStyle: () => ({ getPropertyValue: () => '' }),
    addEventListener() { }, removeEventListener() { }, dispatchEvent() { return true; }, open() { }, scrollTo() { }, alert() { }, confirm: () => false,
    MutationObserver: class { observe() { } disconnect() { } takeRecords() { return []; } },
    IntersectionObserver: class { observe() { } unobserve() { } disconnect() { } },
    ResizeObserver: class { observe() { } unobserve() { } disconnect() { } },
    CustomEvent: class { constructor(t, o) { this.type = t; this.detail = o && o.detail; } },
    Event: class { constructor(t) { this.type = t; } },
    NodeFilter: { SHOW_TEXT: 4, SHOW_ELEMENT: 1, FILTER_ACCEPT: 1, FILTER_REJECT: 2, FILTER_SKIP: 3 },
    Node: { TEXT_NODE: 3, ELEMENT_NODE: 1 }, HTMLElement: class { }, Element: class { },
    fetch: () => Promise.reject(new Error('offline in sandbox')),
    speechSynthesis: { getVoices: () => [], speak() { }, cancel() { } },
    history: { pushState() { }, replaceState() { }, back() { } },
    performance: { now: () => Date.now(), mark() { }, measure() { } },
    URL, URLSearchParams, TextEncoder, TextDecoder, structuredClone, queueMicrotask,
  };
  const sb = vm.createContext(g);
  vm.runInContext('globalThis.window = globalThis; globalThis.self = globalThis;', sb);
  if (opts.before) opts.before(sb);
  if (opts.lazy !== false && items.some(i => i.inline)) sb.SB_LAZY_FETCH = url => fs.readFileSync(path.join(ROOT, url), 'utf8');   // lazy.js loads files synchronously
  const t0 = Date.now(), loadFails = [];
  for (const it of items) {
    if (it.inline) { try { vm.runInContext(it.inline, sb, { filename: 'inline-manifest' }); } catch (e) { loadFails.push('inline manifest: ' + e.message); } continue; }
    const s = it.src;
    let code = fs.readFileSync(path.join(ROOT, s), 'utf8');
    // tracing: top-level data constants become configurable globals so they can later be swapped for logging getters
    if (opts.trace) code = code.replace(/^(?:const|let|var)\s+([A-Z][A-Z0-9_]{2,})\s*=/gm, 'globalThis.$1 =');
    sb.__sbCurrentSrc = s;                                            // lets js/core/lazy.js say which script caused a load
    try { vm.runInContext(code, sb, { filename: s, timeout: 60000 }); }
    catch (e) { loadFails.push(s + ': ' + (e && e.message)); }
  }
  const ms = Date.now() - t0;
  if (!opts.quiet) {
    console.log('loaded ' + srcs.length + ' scripts in ' + ms + ' ms; load failures: ' + loadFails.length);
    loadFails.forEach(x => console.log('  LOADFAIL ' + x.slice(0, 200)));
  }
  // opts.trace: every global named like DATA / ENGLISH_9_DATA / CLS2_BOOKS now logs its reads into reads (a Set)
  const reads = new Set();
  if (opts.trace) {
    const names = vm.runInContext('Object.keys(globalThis).filter(k => /^[A-Z][A-Z0-9_]{2,}$/.test(k))', sb);
    for (const n of names) {
      const d = Object.getOwnPropertyDescriptor(sb, n);
      if (!d || !d.configurable || !('value' in d) || typeof d.value === 'function' || d.value == null) continue;
      let v = d.value;
      Object.defineProperty(sb, n, { configurable: true, enumerable: d.enumerable, get() { reads.add(n); return v; }, set(x) { v = x; } });
    }
  }
  return { sb, registry, srcs, loadFails, ms, reads, run: (code, t) => vm.runInContext(code, sb, { timeout: t || 30000 }) };
}

module.exports = { load, ROOT };
