/* SpaceBook service worker (Phase 4): the app and the books the student downloaded keep working with no network.
 *
 * Three caches, never mixed:
 *   sb-shell-<version>  the page and everything it needs before the first screen (content/sw_version.js lists it). A new version is a new
 *                       cache; the old one is deleted when the new worker takes over. Files are fetched with cache:'reload' so a version
 *                       never mixes old and new files.
 *   sb-content-v1       lazy book files and their patches, requested as name?v=<12 hex of the content hash>: the URL IS the content, so an
 *                       entry never goes stale and this cache is never wiped on an update. "Download for offline" fills it too.
 *   sb-assets-v1        images and other static files without a hash: answered from the cache, refreshed in the background.
 * Not cached on purpose: /api/ (personal data, and the sync outbox in js/core/sync.js already deals with being offline), anything
 * from another origin (the app makes no third-party request on its own), and anything that is not a GET.
 * The outbox lives in IndexedDB, which a service worker update never touches.
 *
 * Update flow: a new worker installs in the background and waits; the page shows "Update available" (js/core/offline.js) and, when the
 * student agrees, posts {type:'SKIP_WAITING'}. The very first install takes over at once.
 * Tests: tests/offline/sw.js runs this file against a fake worker environment. */
'use strict';
importScripts('content/sw_version.js');

const CFG = self.SB_SW;                      // { version, entry, offlinePage, shell: [url...] } (generated)
const SHELL = 'sb-shell-' + CFG.version;
const CONTENT = 'sb-content-v1';
const ASSETS = 'sb-assets-v1';
const scope = new URL('./', self.registration ? self.registration.scope : self.location.href);
const abs = u => new URL(u, scope).href;
const apiPath = new URL('api/', scope).pathname;
const HASHED = /^[0-9a-f]{12}$/;
const shellUrls = new Set(CFG.shell.map(abs));
const STATIC = /\.(?:png|jpe?g|gif|webp|svg|ico|woff2?|ttf|css|js|json|webmanifest)$/i;

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const hadShell = (await caches.keys()).some(k => k.startsWith('sb-shell-') && k !== SHELL);
    const cache = await caches.open(SHELL);
    try {
      // A file requested as name?v=<12 hex of its content> IS its content, so the browser's own copy (the page has just loaded it) is as good as a new
      // download and the install does not fetch it twice; everything else is fetched with cache:'reload' so a version never mixes old and new files.
      // Six at a time: one after the other, 100 files cost 100 round trips (15 s on a 150 ms connection) while the first screen is being drawn.
      const one = async u => {
        const hashed = /[?&]v=[0-9a-f]{12}(?:&|$)/.test(u);
        const res = await fetch(new Request(abs(u), hashed ? {} : { cache: 'reload' }));
        if (!res.ok) throw new Error('shell file unavailable: ' + u + ' (' + res.status + ')');
        await cache.put(abs(u), res);
      };
      for (let i = 0; i < CFG.shell.length; i += 6) await Promise.all(CFG.shell.slice(i, i + 6).map(one));
    } catch (e) {
      await caches.delete(SHELL);                              // the install fails as a whole: no half-cached shell is left to be mistaken for an old version
      throw e;
    }
    if (!hadShell) await self.skipWaiting();                   // first install: take over now; updates wait for the student (SKIP_WAITING)
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith('sb-shell-') && k !== SHELL) await caches.delete(k);   // only old shells go
    await self.clients.claim();
  })());
});

self.addEventListener('message', event => {
  const m = event.data || {};
  if (m.type === 'SKIP_WAITING') self.skipWaiting();
  else if (m.type === 'GET_VERSION' && event.source) event.source.postMessage({ type: 'VERSION', version: CFG.version, entry: CFG.entry });
});

async function put(name, req, res) {
  try { await (await caches.open(name)).put(req, res); } catch (e) { /* quota full or opaque: the answer is still served, only not kept */ }
}

async function fromShell(req) {
  const hit = await (await caches.open(SHELL)).match(req);
  return hit || fetch(req);                                     // not there (should not happen after a good install): ask the network
}

async function cacheFirst(req, name) {
  const hit = await caches.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok) await put(name, req, res.clone());
  return res;
}

async function staleWhileRevalidate(req, name) {
  const cache = await caches.open(name);
  const hit = await cache.match(req);
  const fresh = fetch(req).then(res => { if (res.ok) return put(name, req, res.clone()).then(() => res); return res; });
  if (hit) { fresh.catch(() => { }); return hit; }              // the background refresh may fail offline: that is fine
  return fresh;
}

async function navigate(req) {
  try {
    const timeout = new Promise((_, rej) => setTimeout(() => rej(new Error('slow')), 4000));
    return await Promise.race([fetch(req), timeout]);           // online (or fast enough): always the real page
  } catch (e) {
    const exact = await caches.match(req, { ignoreSearch: true });
    return exact || (await caches.match(abs(CFG.entry), { ignoreSearch: true })) || (await caches.match(abs(CFG.offlinePage))) ||
      new Response('Offline', { status: 503, headers: { 'Content-Type': 'text/plain' } });
  }
}

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== scope.origin) return;
  if (url.pathname.startsWith(apiPath)) return;
  if (req.mode === 'navigate') { event.respondWith(navigate(req)); return; }
  if (shellUrls.has(url.href)) { event.respondWith(fromShell(req)); return; }
  if (HASHED.test(url.searchParams.get('v') || '')) { event.respondWith(cacheFirst(req, CONTENT)); return; }
  if (STATIC.test(url.pathname)) { event.respondWith(staleWhileRevalidate(req, ASSETS)); return; }
});
