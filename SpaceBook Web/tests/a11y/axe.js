'use strict';
/* axe-core on sampled views of the real page (jsdom, no browser).
 *   node --max-old-space-size=8192 tests/a11y/axe.js [--all]      default: fail on any serious / critical issue; --all lists every issue
 *   node --max-old-space-size=8192 tests/a11y/axe.js --update     write the known-issue baseline (tests/baseline/axe.json) after an intended change
 *
 * What jsdom cannot judge (no layout engine): colour contrast (tools/a11y_contrast.js covers the colours written in the source),
 * visibility by stylesheet, target size, focus order on screen. So this is a floor, not the final audit: axe in a real browser
 * (Lighthouse / the axe extension) on the pages listed in docs/ACCESSIBILITY.md is still to be run by a person.
 * The baseline lists the issues that exist today per view and rule; a view may not get a rule it did not have. */
const fs = require('fs'), path = require('path');
const { loadDom } = require('../../tools/lib/app_dom');
const args = process.argv.slice(2);
const BASE = path.join(__dirname, '..', 'baseline', 'axe.json');
let axeSource;
try { axeSource = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8'); } catch (e) { console.log('axe-core is not installed (npm ci in SpaceBook Web); skipped'); process.exit(0); }

const VIEWS = [
  ['home', []],
  ['class 9 subjects', ["goToSubjects('cls9')"]],
  ['class 9 biology list', ["openSubject('cls9','cls9-bio')"]],
  ['class 9 biology lesson', ["openSubject('cls9','cls9-bio')", "selectSubjectChapter('bio', 0, 'cls9')", "(function(){var b=document.querySelector('.math-nav-tabs button[data-tab=\"lesson\"]'); if (b) b.click();})()"]],
  ['class 9 maths', ["openSubject('cls9','cls9-math')"]],
  ['class 5 maths', ["openSubject('cls5','cls5-math')"]],
  ['class 2 english', ["openSubject('cls2','cls2-eng')"]],
  ['class 10 physics', ["openSubject('cls10','cls10-phy')"]],
  ['class 12 chemistry', ["openSubject('cls12','cls12-chem')"]],
  ['class 4 urdu (right to left)', ["openSubject('cls4','cls4-urdu')"]],
  ['class 1 english', ["openSubject('cls1','cls1-eng')"]],
  ['class 12 urdu chapter', ["openSubject('cls12','cls12-urdu')", "selectSubjectChapter('urdu', 0, 'cls12')"]],
  ['tests preparation', ["renderTestsPreps()"]],
  ['sign-in dialog', ["SpaceBookAuth.open('login')"]],
  ['offline books dialog', ["SBOffline.openPanel()"]],
];

let finished = false;
process.on('exit', () => { if (!finished) { console.log('FAIL  the test ended before axe answered'); process.exitCode = 1; } });
(async () => {
  const app = await loadDom({ page: process.env.SB_PAGE || 'index.html' });          // the source page: always current (lazy.html is generated from it)
  const w = app.win;
  // the page's timers are queued by the loader (tools/lib/app_dom.js): axe waits on them, so run them until it has answered
  const pump = async p => { let done = false, out, err; p.then(v => { done = true; out = v; }, e => { done = true; err = e; }); for (let i = 0; i < 4000 && !done; i++) { await app.settle(3); await new Promise(r => setImmediate(r)); } if (err) throw err; if (!done) throw new Error('axe did not finish'); return out; };
  w.eval(axeSource);
  const found = {};
  let serious = 0;
  for (const [name, steps] of VIEWS) {
    for (const code of steps) { try { app.run(code); await app.settle(); } catch (e) { console.log('step failed in', name, ':', code.slice(0, 50), e.message.slice(0, 80)); } }
    // a keyboard user presses Tab first: that is when non-button controls get their roles (js/core/a11y.js)
    w.document.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true }));
    const res = await pump(w.axe.run(w.document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice'] }, rules: { 'color-contrast': { enabled: false }, 'color-contrast-enhanced': { enabled: false } }, resultTypes: ['violations'] }));
    found[name] = {};
    for (const v of res.violations) {
      found[name][v.id] = { impact: v.impact, nodes: v.nodes.length, help: v.help, sample: v.nodes.slice(0, 2).map(n => (n.target || []).join(' ').slice(0, 90)) };
      if (v.impact === 'serious' || v.impact === 'critical') serious += v.nodes.length;
    }
  }
  finished = true;
  const lines = [];
  for (const [view, rules] of Object.entries(found)) for (const [id, v] of Object.entries(rules)) lines.push(`${view.padEnd(24)} ${String(v.impact).padEnd(9)} ${id.padEnd(30)} x${String(v.nodes).padEnd(4)} ${v.help.slice(0, 60)}  e.g. ${v.sample[0] || ''}`);
  if (args.includes('--all') || args.includes('--update')) lines.forEach(l => console.log(l));

  if (args.includes('--update')) {
    const slim = {};
    for (const [view, rules] of Object.entries(found)) slim[view] = Object.fromEntries(Object.entries(rules).map(([id, v]) => [id, { impact: v.impact, nodes: v.nodes }]));
    fs.writeFileSync(BASE, JSON.stringify({ note: 'axe-core issues per sampled view in jsdom (tests/a11y/axe.js). A view may not get a rule it did not have, nor more nodes than listed.', views: slim }, null, 1) + '\n');
    console.log('axe baseline written:', Object.values(slim).reduce((n, r) => n + Object.keys(r).length, 0), 'view/rule pairs');
    return;
  }
  const base = fs.existsSync(BASE) ? JSON.parse(fs.readFileSync(BASE, 'utf8')).views : {};
  let worse = 0;
  for (const [view, rules] of Object.entries(found)) for (const [id, v] of Object.entries(rules)) {
    const was = base[view] && base[view][id];
    if (!was || v.nodes > was.nodes) { worse++; console.log(`FAIL  ${view}: ${id} (${v.impact}) ${was ? was.nodes + ' -> ' : 'new, '}${v.nodes} nodes  ${v.help}  e.g. ${v.sample.join(' | ')}`); }
  }
  const totalSerious = Object.values(found).reduce((n, r) => n + Object.values(r).filter(v => v.impact === 'serious' || v.impact === 'critical').reduce((m, v) => m + v.nodes, 0), 0);
  console.log(`axe: ${VIEWS.length} views, ${Object.values(found).reduce((n, r) => n + Object.keys(r).length, 0)} rule hits, ${totalSerious} serious/critical nodes, ${worse} worse than the baseline`);
  process.exit(worse ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
