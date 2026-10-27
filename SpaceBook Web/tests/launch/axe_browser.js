'use strict';
/* axe-core in a REAL browser (the jsdom run of tests/a11y/axe.js has no layout, so it cannot judge colour contrast, target size or visibility), plus copy and paste.
 *   node --max-old-space-size=3072 tests/launch/axe_browser.js [--json docs/launch/AXE_BROWSER.json]        PW_CHANNEL=msedge runs it in Edge
 * Views: Home, the subjects of Class 5, a subject, a chapter, its Exercise tab, the Offline books dialog and the suggestion dialog; at a desktop width (1280) and a
 * phone width (375). Rules: WCAG 2.0 / 2.1 / 2.2 A and AA and best practice. The test fails on a serious or critical violation that is not in tests/baseline/axe_browser.json
 * (what was found the first time and is listed in docs/launch/FINDINGS_REGISTER.md). Copy and paste: a sentence of an Urdu lesson is selected and copied; the clipboard
 * holds the same letters. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const { serve, launch } = require('../baseline/lib');
const ROOT = path.resolve(__dirname, '..', '..');
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 700) : '')); } };
const args = process.argv.slice(2);
const OUT = args.includes('--json') ? path.resolve(args[args.indexOf('--json') + 1]) : null;
const BASE = path.join(ROOT, 'tests', 'baseline', 'axe_browser.json');
const base = fs.existsSync(BASE) ? JSON.parse(fs.readFileSync(BASE, 'utf8')) : { known: {} };
const AXE = fs.readFileSync(path.join(ROOT, 'node_modules', 'axe-core', 'axe.min.js'), 'utf8');

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const found = {};
  async function open(viewport, extra = {}) {
    const ctx = await browser.newContext(Object.assign({ viewport }, extra));
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 140)));
    await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 120000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 120000 });
    await sleep(2500);
    await page.addScriptTag({ content: AXE });
    return { ctx, page, errors };
  }
  const views = [
    ['home', async p => { await p.evaluate(() => renderClasses()); }],
    ['class 5 subjects', async p => { await p.evaluate(() => goToSubjects('cls5')); }],
    ['subject', async p => { await p.evaluate(() => openSubject('cls5', 'cls5-eng')); }],
    ['chapter', async p => { await p.evaluate(() => selectSubjectChapter('eng', 1, 'cls5')); }],
    ['exercise tab', async p => { await p.evaluate(() => { const b = [...document.querySelectorAll('.math-nav-tabs button, .topic-sub-tabs-bar button')].find(x => /exercise/i.test(x.textContent || '')); if (b) b.click(); }); }],
    ['offline books dialog', async p => { await p.evaluate(() => SBOffline.openPanel()); await p.waitForSelector('.sb-off-box', { state: 'attached', timeout: 20000 }); }],
    ['suggestion dialog', async p => { await p.evaluate(() => { const b = document.getElementById('sbFeedbackBtn'); if (b) b.click(); }); await p.waitForSelector('.sbfb-box, .sbfb-dialog, [role=dialog]', { state: 'attached', timeout: 20000 }).catch(() => {}); }],
  ];
  for (const [wname, vp, extra] of [['desktop 1280', { width: 1280, height: 860 }, {}], ['phone 375', { width: 375, height: 812 }, { isMobile: true, hasTouch: true, deviceScaleFactor: 2 }]]) {
    const { ctx, page, errors } = await open(vp, extra);
    for (const [vname, go] of views) {
      try { await go(page); await sleep(1500); } catch (e) { check(`${wname}: ${vname} opens`, false, String(e.message).slice(0, 140)); continue; }
      const res = await page.evaluate(async () => {
        const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] }, resultTypes: ['violations'] });
        return r.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help, sample: v.nodes.slice(0, 2).map(n => n.target.join(' ').slice(0, 90)), detail: v.nodes.slice(0, 4).map(n => ({ t: n.target.join(' ').slice(0, 110), d: ((n.any || [])[0] && (n.any || [])[0].data ? JSON.stringify((n.any || [])[0].data).slice(0, 240) : '') })) }));
      });
      const bad = res.filter(v => v.impact === 'serious' || v.impact === 'critical');
      const fresh = bad.filter(v => { const k = `${v.id}`; const known = base.known[k]; return !known || v.nodes > known.nodes * 1.2 + 2; });
      for (const v of res) { const k = v.id; (found[k] = found[k] || { impact: v.impact, nodes: 0, help: v.help, views: [], sample: v.sample }).nodes = Math.max(found[k].nodes, v.nodes); found[k].views.push(`${wname}: ${vname}`); }
      if (process.env.DETAIL) for (const v of res) console.log('   DETAIL ' + wname + ' / ' + vname + ' / ' + v.id + ' ' + JSON.stringify(v.detail));
      console.log(`INFO  ${wname}: ${vname}: ${res.length} violations (${bad.length} serious or critical)` + (res.length ? ' ' + res.map(v => `${v.id}[${v.impact}]x${v.nodes}`).join(', ') : ''));
      check(`${wname}: ${vname}: no new serious or critical violation`, fresh.length === 0, fresh);
    }
    check(`${wname}: no script error`, errors.length === 0, errors.slice(0, 3));
    await ctx.close();
  }
  // copy and paste of an Urdu sentence from a lesson
  {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 860 }, permissions: ['clipboard-read', 'clipboard-write'] });
    const page = await ctx.newPage();
    await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 120000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 120000 });
    await sleep(2000);
    const call = await page.evaluate(async () => { const c = await (await fetch('content/app_catalog.json')).json(); const s = c.classes.find(x => x.id === 'cls7').subjects.find(x => x.id === 'cls7-urdu'); return (s.chapters.find(ch => ch.o) || {}).o; });
    await page.evaluate(() => openSubject('cls7', 'cls7-urdu')); await sleep(1500);
    await page.evaluate(c => (0, eval)(c), call); await sleep(3500);
    const sel = await page.evaluate(() => {
      const w = document.createTreeWalker(document.querySelector('#page-content'), NodeFilter.SHOW_TEXT);
      let n;
      while ((n = w.nextNode())) {
        const t = n.nodeValue.trim(), el = n.parentElement;
        if (t.length > 12 && /[؀-ۿ]{3,}/.test(t) && el && el.offsetParent && !el.closest('button, select, textarea, script, style')) {
          const r = document.createRange(); r.selectNodeContents(n); const s = getSelection(); s.removeAllRanges(); s.addRange(r);
          return s.toString().trim();
        }
      }
      return null;
    });
    check('an Urdu sentence of a lesson can be selected', !!sel && /[؀-ۿ]/.test(sel), sel);
    await page.keyboard.press('Control+C');
    await sleep(500);
    const clip = ((await page.evaluate(() => navigator.clipboard.readText().catch(e => 'ERR ' + e.message))) || '').trim();
    check('copy puts the same Urdu letters on the clipboard (no boxes, no reversed or broken text)', !!sel && clip.replace(/\s+/g, ' ') === sel.replace(/\s+/g, ' '), { sel: (sel || '').slice(0, 60), clip: clip.slice(0, 60) });
    const mixed = await page.evaluate(() => { const t = document.querySelector('#page-content').innerText; return /[A-Za-z]/.test(t) && /[؀-ۿ]/.test(t); });
    check('the lesson page mixes Urdu and Latin text and both are in the page text', mixed);
    await ctx.close();
  }
  if (OUT) fs.writeFileSync(OUT, JSON.stringify(found, null, 1) + '\n');
  if (args.includes('--update')) { fs.writeFileSync(BASE, JSON.stringify({ known: Object.fromEntries(Object.entries(found).filter(([, v]) => v.impact === 'serious' || v.impact === 'critical').map(([k, v]) => [k, { nodes: v.nodes, help: v.help }])) }, null, 1) + '\n'); console.log('baseline written'); }
  await browser.close(); server.close();
  console.log(`axe in a real browser: ${pass} passed, ${fail} failed; rules hit: ${Object.keys(found).length}`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
