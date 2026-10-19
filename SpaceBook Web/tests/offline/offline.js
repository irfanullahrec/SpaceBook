'use strict';
/* js/core/offline.js against a fake browser (jsdom + fake Cache Storage, scripted network, fake Storage API).
 *   node tests/offline/offline.js        exits 1 on any failure */
const { JSDOM } = require('jsdom');
const fs = require('fs'), path = require('path');
const { makeCaches, makeServer, sha256 } = require('./fakes');
const factory = require('../../js/core/offline.js');
const BASE = 'https://app.test/spacebook/';
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };
const tick = (ms = 5) => new Promise(r => setTimeout(r, ms));

const BIO = 'const BIO = [1, 2, 3];\n', CHEM = 'const CHEM = ["a"];\n', SHARED = 'window.SHARED = 1;\n', PIC = 'PNGDATA';
const entry = (text, v) => ({ v: sha256(text).slice(0, 12), bytes: Buffer.byteLength(text), sha256: sha256(text) });
const MAP = {
  schema: 'spacebook.offline/1',
  files: { 'js/bio.js': entry(BIO), 'js/chem.js': entry(CHEM), 'js/shared.js': entry(SHARED) },
  assets: { 'img/a.png': { bytes: PIC.length } },
  subjects: {
    'cls9-bio': { classId: 'cls9', name: 'Biology', files: ['js/bio.js'], assets: [], bytes: Buffer.byteLength(BIO) },
    'cls9-chem': { classId: 'cls9', name: 'Chemistry', files: ['js/chem.js', 'js/shared.js'], assets: ['img/a.png'], bytes: Buffer.byteLength(CHEM) + Buffer.byteLength(SHARED) + PIC.length },
    'cls10-chem': { classId: 'cls10', name: 'Chemistry', files: ['js/chem.js', 'js/shared.js'], assets: [], bytes: Buffer.byteLength(CHEM) + Buffer.byteLength(SHARED) },
    'cls-nur-eng': { classId: 'cls-nur', name: 'English', files: [], assets: [], bytes: 0 },
  },
};
const siteFiles = () => ({ 'content/offline_map.json': JSON.stringify(MAP), 'js/bio.js': BIO, 'js/chem.js': CHEM, 'js/shared.js': SHARED, 'img/a.png': PIC });

function setup({ files = siteFiles(), storage = { usage: 1000, quota: 1e9 }, controller = true } = {}) {
  const server = makeServer(files, BASE), caches = makeCaches({ base: BASE });
  const dom = new JSDOM('<!doctype html><body><div class="header-right-group"><div class="header-user-avatar"></div></div></body>', { url: BASE + 'lazy.html', pretendToBeVisual: true });
  const win = dom.window;
  win.caches = caches.api;
  win.fetch = (u, o) => server.fetch(u, o);
  Object.defineProperty(win, 'crypto', { value: require('crypto').webcrypto, configurable: true });
  win.TextEncoder = TextEncoder; win.TextDecoder = TextDecoder;
  const posted = [];
  const sw = { controller: controller ? {} : null, listeners: {}, addEventListener(t, fn) { this.listeners[t] = fn; }, register: async () => reg };
  const reg = { waiting: null, installing: null, listeners: {}, addEventListener(t, fn) { this.listeners[t] = fn; } };
  Object.defineProperty(win.navigator, 'serviceWorker', { value: sw, configurable: true });
  const st = { ...storage, persistCalls: 0 };
  Object.defineProperty(win.navigator, 'storage', { value: { estimate: async () => ({ usage: st.usage, quota: st.quota }), persist: async () => { st.persistCalls++; return true; }, persisted: async () => st.persistCalls > 0 }, configurable: true });
  Object.defineProperty(win.navigator, 'onLine', { value: true, configurable: true });
  win.SBLazy = {};
  win.DATA = { classes: [{ id: 'cls9', name: 'Class 9' }, { id: 'cls10', name: 'Class 10' }, { id: 'cls-nur', name: 'Nursery' }] };
  const O = factory(win);
  return { O, win, server, caches, st, sw, reg, posted };
}

(async () => {
  // ---- estimate / download
  {
    const t = setup();
    const e0 = await t.O.estimate(['cls9-chem', 'cls10-chem']);
    check('estimate counts each shared file once', e0.files === 2 && e0.assets === 1 && e0.bytes === Buffer.byteLength(CHEM) + Buffer.byteLength(SHARED) + PIC.length, JSON.stringify(e0));
    const progress = [];
    const r = await t.O.download(['cls9-bio'], { onProgress: p => progress.push(p) });
    check('download resolves ok with the byte count', r.ok && r.bytes === Buffer.byteLength(BIO) && r.files === 1);
    const u = t.caches.urls('sb-content-v1');
    check('the file is stored under its hash URL (the one lazy.js asks for)', u.length === 1 && u[0] === BASE + 'js/bio.js?v=' + MAP.files['js/bio.js'].v, u.join(','));
    check('progress reports start and end', progress.length >= 2 && progress[0].doneBytes === 0 && progress[progress.length - 1].doneBytes === progress[progress.length - 1].totalBytes);
    check('persistent storage was requested', t.st.persistCalls === 1);
    const have = await t.O.downloaded();
    check('the subject is remembered as downloaded', !!have['cls9-bio'] && have['cls9-bio'].bytes === Buffer.byteLength(BIO));
    const e1 = await t.O.estimate(['cls9-bio']);
    check('nothing is left to fetch for a downloaded subject', e1.files === 0 && e1.bytes === 0);
    t.server.hits.length = 0;
    await t.O.download(['cls9-bio']);
    check('downloading it again fetches nothing', t.server.hits.filter(h => h.startsWith('js/')).length === 0, t.server.hits.join(','));
    const rc = await t.O.download(['cls9-chem']);
    check('files and images are stored in their caches', t.caches.urls('sb-content-v1').length === 3 && t.caches.urls('sb-assets-v1').some(x => x.endsWith('img/a.png')) && rc.files === 3);
  }

  // ---- integrity
  {
    const files = siteFiles(); files['js/chem.js'] = 'const CHEM = ["tampered"];\n';
    const t = setup({ files });
    let code = null;
    try { await t.O.download(['cls9-chem']); } catch (e) { code = e.code; }
    check('a file that does not match its hash is refused', code === 'integrity', code);
    check('and is not stored', !t.caches.urls('sb-content-v1').some(u => u.includes('chem.js')));
    const files2 = siteFiles(); files2['js/chem.js'] = CHEM.replace(/\n/g, '\r\n');
    const t2 = setup({ files: files2 });
    let ok = true;
    try { await t2.O.download(['cls9-chem']); } catch (e) { ok = false; }
    check('a host that serves CRLF still verifies (the hash is of the LF form)', ok);
  }

  // ---- quota
  {
    const t = setup({ storage: { usage: 1e9 - 10, quota: 1e9 } });
    t.server.hits.length = 0;
    let code = null;
    try { await t.O.download(['cls9-chem']); } catch (e) { code = e.code; }
    check('not enough space is reported before anything is fetched', code === 'quota' && t.server.hits.filter(h => h.startsWith('js/')).length === 0, code + ' ' + t.server.hits.join(','));
    const t2 = setup();
    await t2.O.download(['cls9-bio']);
    t2.caches.quota.full = true;
    let code2 = null;
    try { await t2.O.download(['cls9-chem']); } catch (e) { code2 = e.code; }
    check('a storage that fills up mid-download is reported as quota', code2 === 'quota', code2);
    check('what was stored before stays', t2.caches.urls('sb-content-v1').some(u => u.includes('bio.js')));
    const have = await t2.O.downloaded();
    check('a failed download is not recorded as done', !have['cls9-chem'] && !!have['cls9-bio']);
  }

  // ---- network and abort
  {
    const t = setup();
    await t.O.loadMap();
    t.server.online = false;
    let code = null;
    try { await t.O.download(['cls9-bio']); } catch (e) { code = e.code; }
    check('no network is reported as network', code === 'network', code);
    t.server.online = true;
    const ctl = new t.win.AbortController(); ctl.abort();
    let code2 = null;
    try { await t.O.download(['cls9-chem'], { signal: ctl.signal }); } catch (e) { code2 = e.code; }
    check('an aborted download stops', code2 === 'aborted', code2);
  }

  // ---- remove keeps what other subjects still need
  {
    const t = setup();
    await t.O.download(['cls9-chem', 'cls10-chem', 'cls9-bio']);
    const r = await t.O.remove(['cls9-chem']);
    check('removing a subject keeps files another downloaded subject shares', t.caches.urls('sb-content-v1').some(u => u.includes('chem.js')) && t.caches.urls('sb-content-v1').some(u => u.includes('shared.js')));
    check('but deletes its own image', !t.caches.urls('sb-assets-v1').some(u => u.endsWith('img/a.png')) && r.freed === PIC.length, String(r.freed));
    await t.O.remove(['cls10-chem']);
    check('removing the last user of a file deletes it', !t.caches.urls('sb-content-v1').some(u => u.includes('chem.js')) && t.caches.urls('sb-content-v1').some(u => u.includes('bio.js')));
    const have = await t.O.downloaded();
    check('the list of downloaded subjects follows', Object.keys(have).join() === 'cls9-bio');
  }

  // ---- dialog
  {
    const t = setup();
    t.O.init();
    check('the header button appears on the lazy page', !!t.win.document.getElementById('sbOffBtn'));
    check('and sits before the avatar', t.win.document.getElementById('sbOffBtn').nextElementSibling === t.win.document.querySelector('.header-user-avatar'));
    t.win.document.getElementById('sbOffBtn').click();
    await tick(40);
    const dlg = t.win.document.querySelector('.sb-off-overlay');
    check('the dialog opens as a modal dialog with a label', !!dlg && dlg.getAttribute('role') === 'dialog' && dlg.getAttribute('aria-modal') === 'true' && !!t.win.document.getElementById('sbOffTitle'));
    check('it lists classes with their subjects', dlg.querySelectorAll('details').length === 3 && dlg.querySelectorAll('input[data-id]').length === 4);
    check('a subject with nothing to download is not selectable', dlg.querySelector('input[data-id="cls-nur-eng"]').disabled === true);
    const box = dlg.querySelector('input[data-id="cls9-bio"]');
    box.checked = true; dlg.dispatchEvent(new t.win.Event('change', { bubbles: true }));
    await tick(40);
    const dl = dlg.querySelector('[data-act="download"]');
    check('selecting a subject shows its size on the button', !dl.disabled && /Download \(/.test(dl.textContent), dl.textContent);
    dl.click();
    await tick(120);
    check('download finishes with a message', /Done: 1 subject/.test(dlg.querySelector('.sb-off-msg').textContent), dlg.querySelector('.sb-off-msg').textContent);
    check('the file is on the device', t.caches.urls('sb-content-v1').some(u => u.includes('bio.js')));
    const rm = dlg.querySelector('[data-act="remove"]');
    check('remove is enabled for a downloaded subject', !rm.disabled);
    rm.click();
    await tick(80);
    check('remove frees the space and says so', /Removed\./.test(dlg.querySelector('.sb-off-msg').textContent) && !t.caches.urls('sb-content-v1').some(u => u.includes('bio.js')));
    t.win.document.dispatchEvent(new t.win.KeyboardEvent('keydown', { key: 'Escape' }));
    check('Escape closes the dialog', !t.win.document.querySelector('.sb-off-overlay'));
  }

  // ---- no feature off the lazy page
  {
    const t = setup();
    delete t.win.SBLazy;
    t.O.init();
    check('the button does not appear on the normal page', !t.win.document.getElementById('sbOffBtn'));
    t.win.localStorage.setItem('sb_offline', 'on');
    t.O.init();
    check('unless switched on with localStorage sb_offline=on', !!t.win.document.getElementById('sbOffBtn'));
  }

  // ---- update offer
  {
    const t = setup();
    const worker = { postMessage: m => t.posted.push(m), addEventListener() { } };
    t.reg.waiting = worker;
    await t.O.register();
    const banner = t.win.document.getElementById('sbOffUpdate');
    check('a waiting worker with an active one shows "update" (never switches by itself)', !!banner && t.posted.length === 0);
    banner.querySelector('[data-act="update"]').click();
    check('"Update now" tells the new worker to take over', t.posted.length === 1 && t.posted[0].type === 'SKIP_WAITING');
    const t2 = setup({ controller: false });
    t2.reg.waiting = { postMessage() { }, addEventListener() { } };
    await t2.O.register();
    check('the very first install shows no update banner', !t2.win.document.getElementById('sbOffUpdate'));
  }

  // ---- offline badge
  {
    const t = setup();
    t.O.init();
    const b = () => t.win.document.getElementById('sbOffBadge');
    check('the badge is hidden while online', b().hidden === true);
    Object.defineProperty(t.win.navigator, 'onLine', { value: false, configurable: true });
    t.win.dispatchEvent(new t.win.Event('offline'));
    check('the badge shows while offline', b().hidden === false && b().getAttribute('role') === 'status');
    t.win.dispatchEvent(new t.win.CustomEvent('sb:lazy-error', { detail: { src: 'js/x.js' } }));
    check('a book that cannot be fetched explains why', /not on the device/.test(b().textContent));
  }

  console.log(`offline module tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
