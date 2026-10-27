'use strict';
/* Offline in a real Chrome (the real service worker, the real Cache Storage), step by step:
 *   0. a first visit with no connection at all cannot load anything (the one unavoidable download: documented, not a bug);
 *   1. a first visit online: the page does not reload itself, the service worker installs after the first screen and caches the whole start-up shell;
 *   2. after that, the shell opens with the network off (reload offline), and a subject that was NOT downloaded says so instead of showing a blank screen;
 *   3. "Download for offline" of one subject: the size is announced first, progress is reported, every file is checked (sha256) and stored;
 *   4. with the network off, that subject opens, a chapter opens, its exercise tab opens and an Ans button answers; no request fails;
 *   5. an interrupted download (the network drops half way) is reported as a failure and leaves the subject marked as NOT downloaded; the retry completes it;
 *   6. removing the subject frees its files and marks it not downloaded; the Offline books dialog shows the sizes.
 *     node --max-old-space-size=3072 tests/launch/offline_browser.js
 * The cache and the service worker are per browser context: each part starts from the state it describes. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();

  // ---- 0. no connection, never visited
  {
    const ctx = await browser.newContext(); await ctx.setOffline(true);
    const page = await ctx.newPage();
    let failed = false;
    try { await page.goto(url + 'lazy.html', { timeout: 15000 }); } catch (e) { failed = /ERR_INTERNET_DISCONNECTED|net::/.test(String(e.message)); }
    check('a first visit with no connection cannot load the app (the first download needs a connection: said in docs/launch/OFFLINE_REPORT.md)', failed);
    await ctx.close();
  }

  const ctx = await browser.newContext({ viewport: { width: 1280, height: 860 } });
  const page = await ctx.newPage();
  const errors = [], failedReqs = [];
  let navs = 0;
  page.on('framenavigated', f => { if (f === page.mainFrame()) navs++; });
  page.on('pageerror', e => errors.push(String(e.message).slice(0, 160)));
  // the word-meanings table (js/lexicon_data.js) is optional: js/universal_translate.js asks for it when the page is idle and handles the failure; it is kept for offline use only if it was fetched online first
  page.on('requestfailed', r => { const u = r.url(); if (u.startsWith(url) && !/\/api\//.test(u) && !/favicon/.test(u) && !/lexicon_data\.js/.test(u)) failedReqs.push(u.replace(url, '') + ' ' + (r.failure() && r.failure().errorText)); });
  const ready = () => page.waitForFunction(() => window.SBOffline && window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 120000 });

  // ---- 1. first visit
  await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 120000 });
  await ready();
  await page.waitForFunction(async () => { const r = await navigator.serviceWorker.getRegistration(); return !!(r && r.active); }, null, { timeout: 90000 });
  await sleep(2500);
  // the shell (about 180 files) is stored after the first screen: on a slow PC that takes longer than 2.5 s, so wait for it (up to 40 s) instead of a fixed pause
  const wantShell = await page.evaluate(async () => { const t = await (await fetch('content/sw_version.js')).text(); return JSON.parse(t.slice(t.indexOf('{'), t.lastIndexOf('}') + 1)).shell.length; });
  for (let t = 0; t < 120; t++) {           // (waitForFunction does not wait for a promise, so poll by hand)
    const n = await page.evaluate(async () => { const ks = (await caches.keys()).filter(k => k.startsWith('sb-shell-')); return ks.length ? (await (await caches.open(ks[0])).keys()).length : 0; });
    if (n >= wantShell) break;
    await sleep(500);
  }
  check('the first visit does not reload itself when the worker takes over', navs === 1, navs);
  const shell = await page.evaluate(async () => { const ks = (await caches.keys()).filter(k => k.startsWith('sb-shell-')); if (!ks.length) return { n: 0 }; const c = await caches.open(ks[0]); return { n: (await c.keys()).length, name: ks[0] }; });
  const want = await page.evaluate(async () => { const t = await (await fetch('content/sw_version.js')).text(); return JSON.parse(t.slice(t.indexOf('{'), t.lastIndexOf('}') + 1)).shell.length; });
  check('the service worker has cached the whole start-up shell (' + want + ' files)', shell.n === want && want > 90, { shell, want });
  check('the page is now controlled by the worker (it serves from the cache)', await page.evaluate(() => !!navigator.serviceWorker.controller));

  // ---- 2. the shell offline; a book that is not on the device
  await ctx.setOffline(true);
  await page.reload({ waitUntil: 'load' });
  await ready();
  // the Home page is the class cards, pictures with the class name only in the alt text: drawn means the 15 covers really loaded from the cache
  const covers = await page.evaluate(async () => { const imgs = [...document.querySelectorAll('.class-jewel-card img')]; imgs.forEach(i => { i.loading = 'eager'; }); await new Promise(r => setTimeout(r, 2000)); return { n: imgs.length, loaded: imgs.filter(i => i.complete && i.naturalWidth > 0).length }; });
  check('offline, the app opens from the cache (the Home page is drawn: all 15 class covers load)', covers.n >= 15 && covers.loaded === covers.n, covers);
  await page.evaluate(() => { try { openSubject('cls1', 'cls1-eng'); } catch (e) { window.__openErr = String(e); } });
  await sleep(1500);
  const badge = await page.evaluate(() => { const b = document.getElementById('sbOffBadge'); return b && !b.hidden ? b.textContent : ''; });
  check('a subject that was not downloaded says so (no blank screen)', /not on the device/i.test(badge), badge);
  await ctx.setOffline(false);
  await page.reload({ waitUntil: 'load' }); await ready(); await sleep(3000);

  // ---- 3. download one subject
  const est = await page.evaluate(() => SBOffline.estimate(['cls1-eng']));
  check('the size is known before anything is downloaded', est && est.bytes > 100000 && est.files > 0, est);
  const prog = await page.evaluate(async () => { const ticks = []; const r = await SBOffline.download(['cls1-eng'], { onProgress: p => ticks.push(p) }); return { r, n: ticks.length, last: ticks[ticks.length - 1] }; });
  check('Download for offline reports progress and finishes', prog.r && prog.r.ok && prog.n > 1, prog);
  const state = await page.evaluate(async () => ({ got: await SBOffline.downloaded(), left: await SBOffline.estimate(['cls1-eng']) }));
  check('the subject is marked downloaded and nothing is left to fetch', !!state.got['cls1-eng'] && state.left.bytes === 0 && state.left.files === 0, state);
  // a stored file is the file: its hash is the one in the map (the module checked it; this is a second look from outside)
  const hashOk = await page.evaluate(async () => {
    const map = await SBOffline.loadMap(); const s = map.subjects['cls1-eng']; const c = await caches.open('sb-content-v1'); let bad = 0, n = 0;
    for (const src of s.files.slice(0, 4)) { const r = await c.match(src + '?v=' + map.files[src].v); if (!r) { bad++; continue; } const b = await r.arrayBuffer(); const h = [...new Uint8Array(await crypto.subtle.digest('SHA-256', b))].map(x => x.toString(16).padStart(2, '0')).join(''); n++; if (h !== map.files[src].sha256) bad++; }
    return { bad, n };
  });
  check('the stored book files have the hash the map promises', hashOk.bad === 0 && hashOk.n > 0, hashOk);

  // ---- 4. offline use of that subject
  await ctx.setOffline(true);
  await page.reload({ waitUntil: 'load' }); await ready(); await sleep(1500);
  await page.evaluate(() => SBOffline.warmed());           // the books on the device are read ahead (a service worker cannot answer the synchronous request that loads a book)
  failedReqs.length = 0;
  await page.evaluate(() => openSubject('cls1', 'cls1-eng'));
  await sleep(1500);
  await page.evaluate(() => selectSubjectChapter('eng', 1, 'cls1'));
  await page.waitForFunction(() => window.SBLibrary && SBLibrary.collect().units.length > 0, null, { timeout: 60000 });
  check('offline: the downloaded subject opens and a chapter is drawn', (await page.evaluate(() => document.querySelector('#page-content').innerText.length)) > 300);
  const tab = await page.evaluate(() => { const b = [...document.querySelectorAll('.math-nav-tabs button, .topic-sub-tabs-bar button')].find(x => /exercise/i.test(x.textContent || '')); if (b) { b.click(); return (b.textContent || '').trim(); } return ''; });
  await sleep(1500);
  check('offline: its Exercise tab opens (' + tab + ')', !!tab && (await page.evaluate(() => document.querySelector('#page-content').innerText.length)) > 200, tab);
  const ans = await page.evaluate(async () => { const b = document.querySelector('.sb-ans'); if (!b) return { found: false }; b.click(); await new Promise(r => setTimeout(r, 600)); return { found: true, open: b.getAttribute('aria-expanded') === 'true' }; });
  check('offline: an Ans button answers', ans.found && ans.open, ans);
  check('offline: not one request of the site failed', failedReqs.length === 0, failedReqs.slice(0, 6));
  await ctx.setOffline(false);
  await page.reload({ waitUntil: 'load' }); await ready(); await sleep(2500);

  // ---- 5. an interrupted download
  const ID = 'cls9-chem';            // 13 MB: big enough that the download is still running 350 ms after it starts, even from the local server
  // the network drops after the first book file: every later request for a hashed file fails the way fetch fails offline
  // (not a route or setOffline: with the service worker in charge a 13 MB download from the local server is over before either takes effect)
  await page.evaluate(id => {
    const orig = window.fetch; let n = 0; window.__origFetch = orig;
    window.fetch = function (u) { if (/\?v=/.test(String(u && u.url || u)) && ++n > 1) return Promise.reject(new TypeError('Failed to fetch')); return orig.apply(this, arguments); };
    window.__dl = SBOffline.download([id], {}).then(r => ({ ok: true, r }), e => ({ ok: false, code: e && e.code, message: e && e.message }));
  }, ID);
  const cut = await page.evaluate(async () => await window.__dl);
  await page.evaluate(() => { window.fetch = window.__origFetch; });
  await sleep(1500);
  const after = await page.evaluate(async id => ({ got: await SBOffline.downloaded(), left: await SBOffline.estimate([id]) }), ID);
  check('a download the network cut is reported as a failure (code network), not as done', cut.ok === false && cut.code === 'network', cut);
  check('and the subject is not marked as downloaded (no half book is offered offline)', !after.got[ID] && after.left.bytes > 0, after);
  const retry = await page.evaluate(async id => { try { const r = await SBOffline.download([id], {}); return { ok: r.ok }; } catch (e) { return { ok: false, code: e.code }; } }, ID);
  const fin = await page.evaluate(async id => ({ got: await SBOffline.downloaded(), left: await SBOffline.estimate([id]) }), ID);
  check('the retry completes it (nothing left to fetch, marked downloaded)', retry.ok && !!fin.got[ID] && fin.left.files === 0, { retry, fin });

  // ---- 6. the dialog, and removing
  await page.evaluate(() => SBOffline.openPanel());
  await page.waitForSelector('.sb-off-row', { state: 'attached', timeout: 20000 });
  const panel = await page.locator('.sb-off-box').innerText();
  check('the Offline books dialog shows each subject with its size in MB and what is on the device', /MB/.test(panel) && /Offline books/.test(panel), panel.slice(0, 300));
  const syncLine = await page.locator('.sb-off-sync').innerText().catch(() => '');
  check('the dialog says what happens to progress (saved on this device, signed out)', /saved on this device/i.test(syncLine) && /Sign in/i.test(syncLine), syncLine);
  await page.evaluate(() => document.querySelector('.sb-off-close').click());
  const before = await page.evaluate(async () => (await SBOffline.usage()).usage);
  const rm = await page.evaluate(async id => { const r = await SBOffline.remove([id]); return { r, got: await SBOffline.downloaded() }; }, ID);
  check('removing a subject marks it not downloaded and frees its files', rm.r && rm.r.ok && !rm.got[ID] && !!rm.got['cls1-eng'] && rm.r.freed > 0, rm);
  check('no script error during the whole run', errors.length === 0, errors.slice(0, 5));
  await browser.close(); server.close();
  console.log('---\noffline browser test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
