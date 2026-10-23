'use strict';
/* Where a page is, the same on both platforms:
 *   1. the website's tab text and bookmark keys are the golden ones (tests/parity/locator_golden.json), which the app's unit test also checks;
 *   2. the pages of a chapter: the website's locator (js/sb_library.js collect) and the app's bridge (assets/reader_bridge.js) find the same
 *      units, in the same order, in the same markup (printed pages, topic cards, one block, scripts and empty blocks left out).
 *     node tests/parity/locator.js [--app "<folder of the app repo>"]
 * jsdom has no layout: offsetParent is faked (visible unless display:none). Where the app folder is absent the bridge half is skipped. Dev-only. */
const fs = require('fs'), path = require('path');
const { JSDOM } = require('jsdom');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const BRIDGE = path.join(APP, 'app', 'src', 'main', 'assets', 'reader_bridge.js');

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 500) : '')); } };

function page(html, withBridge) {
  const dom = new JSDOM('<!doctype html><html><body><div id="dashboard-body">' + html + '</div></body></html>', { runScripts: 'outside-only', pretendToBeVisual: true, url: 'http://localhost/' });
  const w = dom.window;
  Object.defineProperty(w.HTMLElement.prototype, 'offsetParent', { get() { return this.style && this.style.display === 'none' ? null : this.parentElement; } });
  w.fetch = () => Promise.reject(new Error('no network'));
  w.scrollTo = () => {};                                             // jsdom does not implement it
  w.eval(fs.readFileSync(path.join(ROOT, 'js', 'sb_library.js'), 'utf8'));
  if (withBridge) w.eval(fs.readFileSync(BRIDGE, 'utf8'));
  return w;
}

const cases = {
  'printed pages in a subject tab': '<div id="subjTabContent"><div class="bk-page">one</div><div class="bk-page">two</div><div class="bk-page">three</div></div>',
  'topic cards in a math tab': '<div id="mathTabContent"><div class="math-topic-card">a</div><div class="math-topic-card">b</div><div class="math-topic-card">c</div><div class="math-topic-card">d</div></div>',
  'a single block is not a set of pages': '<div id="subjTabContent"><div>just one block</div></div>',
  'printed pages win over cards': '<div id="subjTabContent"><div class="math-topic-card">card</div><div class="math-topic-card">card</div></div><div id="page-content"><div class="bk-page">p1</div><div class="bk-page">p2</div></div>',
  'scripts, styles and empty blocks are not pages': '<div id="subjTabContent"><script>1</script><style>.x{}</style><div></div><div class="c">a</div><div class="c">b</div><div class="c">   </div></div>',
  'a hidden card is not a page, a card the app hid is': '<div id="subjTabContent"><div class="c">a</div><div class="c" style="display:none">hidden</div><div class="c">c</div></div>',
};

(async () => {
  console.log('--- tabs and keys ---');
  const g = JSON.parse(fs.readFileSync(path.join(__dirname, 'locator_golden.json'), 'utf8'));
  const w0 = page('', false);
  const L = w0.SBLibrary;
  const badTabs = g.tabs.filter(([raw, want]) => L.cleanTab(raw) !== want).map(([raw, want]) => [raw, want, L.cleanTab(raw)]);
  check(`the website writes ${g.tabs.length} tab texts as the golden file says (the app's LibraryRepositoryTest checks the same file)`, badTabs.length === 0, badTabs);
  const badKeys = g.bookmarkKeys.filter(([s, ch, tb, p, want]) => L.bmKey({ s, ch, tb: L.cleanTab(tb), p }) !== want).map(k => k[4]);
  check(`and ${g.bookmarkKeys.length} bookmark keys`, badKeys.length === 0, badKeys);

  console.log('--- the pages of a chapter ---');
  if (!fs.existsSync(BRIDGE)) { console.log('SKIP  the app folder is not here (' + BRIDGE + '): the bridge was not compared'); }
  for (const [name, html] of Object.entries(cases)) {
    const w = page(html, fs.existsSync(BRIDGE));
    const web = w.SBLibrary.collect();
    if (!fs.existsSync(BRIDGE)) { check('website: ' + name + ' → ' + web.units.length + ' page(s)', true); continue; }
    w.SBApp.setMode({ paginate: true });
    await new Promise(r => setTimeout(r, 300));                       // the bridge refreshes after 160 ms
    const st = w.SBApp.state();
    const appPages = st.mode === '' || st.mode === 'flow' ? 0 : st.pages;
    let same = web.units.length === appPages;
    if (same) for (let i = 0; i < web.units.length; i++) { w.SBApp.go(i); same = same && w.document.querySelector('.sbapp-page-on') === web.units[i]; }
    check(`${name}: website ${web.units.length} unit(s) (${web.mode || 'none'}), app ${appPages} (${st.mode}), the same elements in the same order`, same, { web: web.units.length, app: appPages, mode: st.mode });
  }
  console.log(`---\nlocator parity: ${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
