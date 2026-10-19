'use strict';
/* Service worker tests: sw.js runs in a vm context that stands in for a ServiceWorkerGlobalScope (fake Cache Storage, scripted network).
 *   node tests/offline/sw.js            exits 1 on any failure */
const fs = require('fs'), path = require('path'), vm = require('vm');
const { makeCaches, makeServer } = require('./fakes');
const SRC = fs.readFileSync(path.join(__dirname, '..', '..', 'sw.js'), 'utf8');
const BASE = 'https://app.test/spacebook/';
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

const HASH = 'abcdef012345';
const SITE = {
  'lazy.html': '<html>app</html>', 'offline.html': '<html>offline</html>', 'css/style.css?v=1': 'body{}',
  'js/app.js': 'app()', 'js/data_a.js': 'const A=1;', 'img/pic.png': 'PNG', 'api/progress.php': '{"coins":1}',
};
const siteFiles = () => ({ 'lazy.html': SITE['lazy.html'], 'offline.html': SITE['offline.html'], 'js/app.js': SITE['js/app.js'], 'js/data_a.js': SITE['js/data_a.js'], 'img/pic.png': 'PNG', 'api/progress.php': '{"coins":1}', 'api/export.json': '{}', 'css/style.css': 'body{}', 'icons/icon-192.png': 'ICON' });
const SHELL = ['lazy.html', 'offline.html', 'js/app.js?v=' + HASH, 'css/style.css?v=111111111111', 'icons/icon-192.png'];

function worker({ version = 'v1', shell = SHELL, server, caches, swFiles }) {
  const handlers = {};
  const ctx = {
    console, URL, Request, Response, Promise, setTimeout, clearTimeout, Headers,
    caches: caches.api, fetch: (input, init) => server.fetch(input, init),
    skipped: false, claimed: false, handlers,
    addEventListener(type, fn) { handlers[type] = fn; },
    registration: { scope: BASE }, location: new URL(BASE + 'sw.js'),
    clients: { claim: async () => { ctx.claimed = true; } },
    skipWaiting: async () => { ctx.skipped = true; },
    importScripts() { ctx.SB_SW = { version, entry: 'lazy.html', offlinePage: 'offline.html', shell }; },
  };
  ctx.self = ctx;
  vm.createContext(ctx);
  vm.runInContext(SRC, ctx, { filename: 'sw.js' });
  const waitUntilEvent = () => { const ev = { p: Promise.resolve(), waitUntil(p) { this.p = p; } }; return ev; };
  return {
    ctx,
    async install() { const ev = waitUntilEvent(); handlers.install(ev); await ev.p; },
    async activate() { const ev = waitUntilEvent(); handlers.activate(ev); await ev.p; },
    async message(data) { const sent = []; handlers.message({ data, source: { postMessage: m => sent.push(m) } }); return sent; },
    async fetch(url, { method = 'GET', mode = 'cors' } = {}) {
      const request = new Request(new URL(url, BASE), { method });
      Object.defineProperty(request, 'mode', { value: mode });
      let answer = null;
      handlers.fetch({ request, respondWith(p) { answer = p; } });
      if (!answer) return { handled: false };
      try { return { handled: true, res: await answer }; } catch (error) { return { handled: true, error }; }
    },
  };
}

(async () => {
  // ---- install: first time, everything in the shell is cached and the worker takes over at once
  {
    const caches = makeCaches(), server = makeServer(siteFiles());
    server.files['js/app.js'] = SITE['js/app.js']; server.files['css/style.css'] = 'body{}';
    const w = worker({ server, caches });
    await w.install();
    check('first install caches every shell file', caches.urls('sb-shell-v1').length === SHELL.length, caches.urls('sb-shell-v1').join(','));
    check('shell files keep their hash query in the cache key', caches.urls('sb-shell-v1').some(u => u.endsWith('js/app.js?v=' + HASH)));
    check('first install takes over at once', w.ctx.skipped === true);
    check('install asks the network, not the HTTP cache (cache: reload)', server.hits.length === SHELL.length);
    await w.activate();
    check('activate claims the open pages', w.ctx.claimed === true);
  }

  // ---- install fails as a whole when a shell file is missing; no half-filled cache remains
  {
    const caches = makeCaches(), server = makeServer({ 'lazy.html': 'x' });
    const w = worker({ server, caches, shell: ['lazy.html', 'missing.js'] });
    let threw = false;
    try { await w.install(); } catch (e) { threw = true; }
    check('install rejects when a shell file is unavailable', threw);
    check('a failed install leaves no shell cache behind', !(await caches.api.has('sb-shell-v1')));
    check('a failed install does not take over', w.ctx.skipped === false);
  }

  // ---- an update waits for the student; old shell is deleted only on activate; content and asset caches stay
  {
    const caches = makeCaches(), server = makeServer(siteFiles());
    const v1 = worker({ server, caches, version: 'v1' });
    await v1.install(); await v1.activate();
    await (await caches.api.open('sb-content-v1')).put(BASE + 'js/data_a.js?v=' + HASH, new Response('const A=1;'));
    await (await caches.api.open('sb-assets-v1')).put(BASE + 'img/pic.png', new Response('PNG'));
    const v2 = worker({ server, caches, version: 'v2', shell: ['lazy.html', 'offline.html'] });
    await v2.install();
    check('an update installs a second shell cache', (await caches.api.keys()).includes('sb-shell-v1') && (await caches.api.keys()).includes('sb-shell-v2'));
    check('an update does not take over by itself', v2.ctx.skipped === false);
    const sent = await v2.message({ type: 'GET_VERSION' });
    check('GET_VERSION answers with the version', sent[0] && sent[0].version === 'v2');
    await v2.message({ type: 'SKIP_WAITING' });
    check('SKIP_WAITING makes it take over', v2.ctx.skipped === true);
    await v2.activate();
    const keys = await caches.api.keys();
    check('activate deletes the old shell', !keys.includes('sb-shell-v1') && keys.includes('sb-shell-v2'), keys.join(','));
    check('activate keeps the content cache (hash-addressed, never stale)', keys.includes('sb-content-v1') && caches.urls('sb-content-v1').length === 1);
    check('activate keeps the assets cache', keys.includes('sb-assets-v1'));
  }

  // ---- fetch routing
  {
    const caches = makeCaches(), server = makeServer(siteFiles());
    server.files['js/app.js'] = SITE['js/app.js']; server.files['css/style.css'] = 'body{}';
    const w = worker({ server, caches });
    await w.install(); await w.activate();
    server.hits.length = 0;

    check('a POST is not handled', (await w.fetch('api/auth.php', { method: 'POST' })).handled === false);
    check('the API is not handled (no personal data in a cache)', (await w.fetch('api/progress.php')).handled === false);
    check('not even an API URL that looks like a static file or carries a hash', (await w.fetch('api/export.json')).handled === false && (await w.fetch('api/progress.php?v=abcdef012345')).handled === false);
    check('another origin is not handled (no third-party caching)', (await w.fetch('https://fonts.example/x.css')).handled === false);

    server.online = false;
    const shellRes = await w.fetch('js/app.js?v=' + HASH);
    check('a shell file is served from the shell cache with no network', shellRes.handled && (await shellRes.res.text()) === 'app()');
    const icon = await w.fetch('icons/icon-192.png');
    check('an unhashed shell file (icon) is served from the shell cache with no network', icon.handled && (await icon.res.text()) === 'ICON');
    const nav = await w.fetch('lazy.html', { mode: 'navigate' });
    check('offline navigation to the entry page gives the cached page', nav.handled && (await nav.res.text()) === '<html>app</html>');
    const navOther = await w.fetch('somewhere/else.html?x=1', { mode: 'navigate' });
    check('offline navigation to an unknown page falls back to the entry page', navOther.handled && (await navOther.res.text()) === '<html>app</html>');
    server.online = true;
    const live = await w.fetch('lazy.html', { mode: 'navigate' });
    check('online navigation asks the network', live.handled && server.hits.includes('lazy.html'));

    // hashed book file: first online, then offline
    server.files['js/data_a.js'] = 'const A=1;';
    const first = await w.fetch('js/data_a.js?v=' + HASH);
    check('a hashed file is fetched once and answered', first.handled && (await first.res.text()) === 'const A=1;');
    check('and stored in the content cache under its hash URL', caches.urls('sb-content-v1').some(u => u.endsWith('data_a.js?v=' + HASH)));
    server.hits.length = 0; server.online = false;
    const second = await w.fetch('js/data_a.js?v=' + HASH);
    check('a hashed file is served from the cache with no network', second.handled && (await second.res.text()) === 'const A=1;' && server.hits.length === 0);
    const other = await w.fetch('js/data_a.js?v=ffffffffffff');
    check('a hashed file never fetched and offline fails (not a wrong file)', other.handled && !!other.error);
    server.online = true;

    // unhashed static asset: stale-while-revalidate
    const pic1 = await w.fetch('img/pic.png');
    check('an unhashed image is fetched and stored in the assets cache', pic1.handled && caches.urls('sb-assets-v1').some(u => u.endsWith('img/pic.png')));
    server.files['img/pic.png'] = 'PNG2'; server.hits.length = 0;
    const pic2 = await w.fetch('img/pic.png');
    check('the cached image is answered at once', (await pic2.res.text()) === 'PNG');
    await new Promise(r => setTimeout(r, 20));
    check('and refreshed in the background', server.hits.includes('img/pic.png'));
    const pic3 = await w.fetch('img/pic.png');
    check('the refreshed copy is used next time', (await pic3.res.text()) === 'PNG2');

    // a full disk does not break answers
    caches.quota.full = true;
    server.files['js/data_b.js'] = 'const B=2;';
    const big = await w.fetch('js/data_b.js?v=123456789abc');
    check('a full storage still returns the response (just not kept)', big.handled && (await big.res.text()) === 'const B=2;');
  }

  console.log(`service worker tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
