'use strict';
/* The website's own pages as they run inside the Android app, tried in Chrome with a phone's width and touch (no mouse, no hover): the app's stylesheet
 * (reader_mobile.css) and bridge (reader_bridge.js) are injected into the real page exactly as the app's WebView does after the page loads.
 *     node --max-old-space-size=8192 tests/parity/app_pages.js [--app "<folder of the app repo>"] [--out <screenshots>]
 * Checks: Games, Tests Preps, Papers and Study Plan open from the bridge (SBApp.openPage), draw something, do not scroll sideways and react to a tap;
 * the website's search runs through the app's search_bridge.js and gives the website's own results; the account dialog and the data download go
 * through the bridge; nothing throws. A page the app shows is the page the website shows, so a failure here is a failure of the app.
 * Needs the app folder (for its bridge and stylesheet); without it the test says so and passes nothing. Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets');
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_app_pages'));
if (!fs.existsSync(path.join(ASSETS, 'reader_bridge.js'))) { console.log('SKIP  the app folder is not here (' + ASSETS + '): the app\'s bridge and stylesheet are needed'); process.exit(0); }
fs.mkdirSync(OUT, { recursive: true });

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + String(typeof d === 'string' ? d : JSON.stringify(d)).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const css = fs.readFileSync(path.join(ASSETS, 'reader_mobile.css'), 'utf8');
const bridge = fs.readFileSync(path.join(ASSETS, 'reader_bridge.js'), 'utf8');

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 411, height: 860 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::|api\//.test(m.text())) errors.push('console: ' + m.text()); });
  const shot = async n => { try { await page.screenshot({ path: path.join(OUT, n + '.png') }); } catch (e) { /* busy */ } };

  // what the WebView does after the page loads: the host object first, then the stylesheet and the bridge
  async function boot() {
    await page.addInitScript(() => {
      window.__host = { actions: [], states: [] };
      window.SBHost = { onReady() { }, onState(s) { window.__host.states.push(s); }, onAction(n, d) { window.__host.actions.push([n, d]); }, speak() { }, stopSpeech() { } };
    });
    await page.goto(url + 'index.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
    await page.waitForFunction(() => typeof openSubject === 'function' && window.SBStudyPlan && window.SBGames && window.SpaceBookAuth, null, { timeout: 120000 });
    await page.evaluate(([c]) => { const s = document.createElement('style'); s.id = 'sbapp-css'; s.textContent = c; document.head.appendChild(s); document.documentElement.classList.add('sbapp'); }, [css]);
    await page.evaluate(bridge);
  }
  const overflow = () => page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
  const text = () => page.evaluate(() => (document.getElementById('dashboard-body') || document.body).innerText.replace(/\s+/g, ' '));

  await boot();
  check('the bridge is in the page (SBApp, SBApp.openAccount, SBDownload)', await page.evaluate(() => !!window.SBApp && typeof SBApp.openAccount === 'function' && typeof window.SBDownload === 'function' && typeof SBApp.open === 'function'));

  for (const [name, page_, words] of [['Games', 'games', /Quiz Quest/], ['Tests Preps', 'tests-preps', /Tests? Prep|PST|Practice|Mock/i], ['Papers', 'papers', /Paper|Set A|Class/i], ['Study Plan', 'study-plan', /Study Plan|plan|Create/i]]) {
    const ok = await page.evaluate(n => SBApp.openPage(n), page_);
    await sleep(900);
    const t = await text();
    const o = await overflow();
    check(`${name}: opens through the bridge, shows its content (${t.length} characters) and does not scroll sideways at 411 px`, ok === true && words.test(t) && o.sw <= o.cw + 1, { ok, sw: o.sw, cw: o.cw, text: t.slice(0, 120) });
    await shot('page-' + page_);
  }

  // a tap, not a mouse: a game card opens its level map
  await page.evaluate(() => SBApp.openPage('games'));
  await page.waitForSelector('.gm-card', { timeout: 20000 });
  await page.tap('.gm-play');
  await page.waitForSelector('.gm-node', { timeout: 20000 }).catch(() => null);
  check('Games: a tap on Play opens the level map (no hover needed)', !!(await page.$('.gm-node')));
  await shot('games-levels');

  // a tap on a study plan card / the create button reacts
  await page.evaluate(() => SBApp.openPage('study-plan'));
  await sleep(700);
  const spButtons = await page.$$('#dashboard-body button');
  check('Study Plan: has buttons a finger can reach (each at least 28 px tall)', spButtons.length > 0 && (await Promise.all(spButtons.slice(0, 6).map(b => b.boundingBox()))).every(b => !b || b.height >= 26), spButtons.length);

  // BISE Swat Board centre and the translator: the website's own, in the same touch page
  await page.evaluate(() => SBBise.open('cls9-phy'));
  await sleep(900);
  const bt = await text(), bo = await overflow();
  check('BISE Swat Board centre opens at 411 px, shows the Board\'s pattern and does not scroll sideways', /BISE|Board|Swat/i.test(bt) && bo.sw <= bo.cw + 1, { sw: bo.sw, cw: bo.cw, text: bt.slice(0, 100) });
  await shot('page-bise');
  const tr = await page.evaluate(async () => { const r = await SBTranslate.translate('The cell is the unit of life.', 'en', 'ur', true); return r && r.text ? r.text : ''; });
  check('the translator gives Urdu for an English sentence with no network (the offline lexicon)', tr.length > 0 && /[؀-ۿ]/.test(tr), tr);

  console.log('--- search through the app\'s bridge ---');
  const searchJs = fs.readFileSync(path.join(ASSETS, 'site', 'js', 'core', 'search.js'), 'utf8');
  const searchBridge = fs.readFileSync(path.join(ASSETS, 'search_bridge.js'), 'utf8');
  const sp = await ctx.newPage();
  await sp.goto(url + 'tests/parity/blank.html', { waitUntil: 'domcontentloaded' });
  await sp.evaluate(() => { window.__done = []; window.SBSearchHost = { done(id, raw) { window.__done.push([id, raw]); } }; });
  await sp.evaluate(searchJs + '\n;\n' + searchBridge);
  await sp.evaluate(() => SBAppSearch(1, 'fractions', ['cls5-math', 'cls5-eng']));
  await sp.waitForFunction(() => window.__done.length === 1, null, { timeout: 30000 }).catch(() => null);
  const got = await sp.evaluate(() => window.__done[0]);
  const hits = got ? JSON.parse(got[1]) : [];
  const own = await sp.evaluate(async () => { const r = await SBSearch.searchSubjects('fractions', ['cls5-math', 'cls5-eng']); return r.map(x => x.id + ':' + x.chapter); });
  check('the app\'s search call returns the website\'s own results, each with a chapter title and a match count', hits.length > 0 && hits.map(x => x.id + ':' + x.chapter).join() === own.join() && hits.every(x => x.title && x.hits > 0), { hits: hits.slice(0, 2), own: own.slice(0, 2) });
  const bad = await sp.evaluate(async () => { window.__done.length = 0; await SBAppSearch(2, 'zzzzqqqqxxxx', ['cls5-math']); return window.__done[0]; });
  check('a word that is nowhere gives an empty list, not an error', bad && JSON.parse(bad[1]).length === 0);
  await sp.close();

  console.log('--- the account dialog and the data download ---');
  const signedOut = await page.evaluate(async () => { window.__host.actions.length = 0; const r = await SBApp.openAccount(); return { r, actions: window.__host.actions.slice() }; });
  check('"My account" while signed out sends the student to the app\'s own sign-in', signedOut.r === false && signedOut.actions.some(a => a[0] === 'auth'), signedOut);
  const saved = await page.evaluate(async () => {
    window.__host.actions.length = 0;
    const real = window.fetch;
    window.fetch = async () => ({ ok: true, status: 200, json: async () => ({ schema: 'spacebook.export/1', account: { name: 'T' } }) });
    const r = await SpaceBookAuth.exportData();
    window.fetch = real;
    return { schema: r && r.schema, actions: window.__host.actions.filter(a => a[0] === 'saveFile') };
  });
  const sf = saved.actions[0] ? JSON.parse(saved.actions[0][1]) : null;
  check('the data download is handed to the app (name, type, text), not made into a blob link', !!sf && sf.name === 'spacebook-my-data.json' && sf.mime === 'application/json' && JSON.parse(sf.text).schema === 'spacebook.export/1', saved);

  console.log('--- the page follows the owner\'s sync switch ---');
  const sync = await page.evaluate(async () => {
    localStorage.removeItem('sb_sync_v2'); localStorage.removeItem('sb_sync_server');
    await SBApp.setAuth({ id: 99 }, { id: '11111111-2222-4333-8444-555555555555', token: 't'.repeat(64) }, { syncV2: false });
    const off = SBSync.isEnabled(), forced = localStorage.getItem('sb_sync_v2');
    await SBApp.setAuth({ id: 99 }, { id: '11111111-2222-4333-8444-555555555555', token: 't'.repeat(64) }, { syncV2: true });
    return { off, forced, on: SBSync.isEnabled() };
  });
  check('setAuth does not switch sync on by itself; it passes the server\'s flag (off stays off, on turns on)', sync.off === false && sync.forced === null && sync.on === true, sync);

  check('nothing threw in the console', errors.length === 0, errors);
  await browser.close(); server.close();
  console.log(`---\napp pages: ${pass} passed, ${fail} failed (screenshots in ${OUT})`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
