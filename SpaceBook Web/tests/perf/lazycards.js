'use strict';
/* SBLazyCards (js/core/lazycards.js): with the owner flag on, the closed cards of a Maths tab are empty until opened, and then they are exactly what they
 * would have been. Runs the real page twice (flag off / flag on) in a simulated DOM, opens every card, and compares the result.
 *   node --max-old-space-size=8192 tests/perf/lazycards.js */
const { loadDom } = require('../../tools/lib/app_dom');
const LC = require('../../js/core/lazycards.js');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

// ---- the string transform alone
{
  const big = 'x'.repeat(5000);
  const body = n => `<div class="math-accordion-body" style="display:none;margin:0"><div>${big}${n}</div><div><p>inner</p></div></div>`;
  const card = n => `<div class="math-topic-card math-accordion-card"><div class="math-acc-header" onclick="toggleMathAccordion(this)">H${n}</div>${body(n)}</div>`;
  const open = `<div class="math-topic-card math-accordion-card open"><div class="math-acc-header">O</div><div class="math-accordion-body" style="display:block"><div>${big}</div></div></div>`;
  const small = `<div class="math-accordion-card"><div class="math-accordion-body" style="display:none"><div>small</div></div></div>`;
  const pad = '<p>' + 'y'.repeat(200000) + '</p>';
  const html = pad + card(1) + open + small + card(2);
  const keep = new Map();
  const out = LC.defer(html, keep);
  check('the two big closed bodies are kept, the open one and the small one stay', keep.size === 2 && (out.match(/data-sb-lazy="/g) || []).length === 2 && out.includes(big + '</div>') && out.includes('<div>small</div>'));
  check('what is kept is exactly the inside of the body (nested divs and all)', [...keep.values()].every(v => v.startsWith('<div>' + big) && v.endsWith('<p>inner</p></div>')));
  check('the page shrinks by the kept bodies', html.length - out.length > 2 * 5000 && out.length < html.length / 1.02 + 200);
  check('putting the kept bodies back gives the original page (after removing the marker)', (() => { let r = out; keep.forEach((v, id) => { r = r.replace(new RegExp('(<div data-sb-lazy="' + id + '" class="math-accordion-body"[^>]*>)</div>'), '$1' + v + '</div>'); }); return r.replace(/ data-sb-lazy="\d+"/g, '') === html; })());
  check('a small page is returned as it is', LC.defer(card(1), new Map()) === card(1));
  check('an unbalanced body is left alone', (() => { const k = new Map(); const bad = pad + `<div class="math-accordion-body" style="display:none"><div>${big}</div>`; return LC.defer(bad, k) === bad && k.size === 0; })());
}

// ids with a random part differ between two runs of the same page (sb_mcq ids, ids inside Maths diagrams); rename them in order of first appearance
const normIds = html => {
  const m = new Map();
  for (const x of html.matchAll(/\bid="(m[a-z]*\d*-[^"]+)"/g)) if (!m.has(x[1])) m.set(x[1], 'fig' + m.size);
  return (m.size ? html.replace(/m[a-z]*\d*-[A-Za-z0-9-]+/g, t => m.get(t) || t) : html).replace(/sbq\d+_[a-z0-9]{4}/g, 'sbqN_ID');
};
(async () => {
  const ALL = [['cls5', 'cls5-math', 7, 0.3], ['cls8', 'cls8-math', 4, 0]].concat(process.env.SB_LC_FULL ? [['cls11', 'cls11-math', 4, 0.1], ['cls12', 'cls12-math', 1, 0.9]] : []);   // [class, subject, chapter, least share of the elements that must go]; SB_LC_FULL=1 adds the big ones (minutes each in the simulated DOM)
const SUBJECTS = process.env.SB_LC_ONLY ? ALL.filter(x => process.env.SB_LC_ONLY.split(',').includes(x[1])) : ALL;
  async function session(lazy) {
    const app = await loadDom({ page: 'index.html', timeout: 1800000 });
    const w = app.win, d = w.document;
    if (lazy) w.SB_FLAGS = { lazyCards: true };
    const out = [];
    for (const [cls, sid, ch] of SUBJECTS) {
      app.run(`openSubject('${cls}', '${sid}')`); await app.settle();
      const calls = [...d.querySelectorAll('[onclick*="Chapter("]')].map(e => e.getAttribute('onclick'));
      app.run(calls[ch]); await app.settle();
      const lessonTab = [...d.querySelectorAll('.math-nav-tabs [onclick], .math-tab-btn[onclick]')].find(b => /'lesson'/.test(b.getAttribute('onclick')));
      if (lessonTab) { lessonTab.click(); await app.settle(); }
      const c = d.getElementById('mathTabContent') || d.getElementById('subjTabContent');
      const rec = { sid, elements: c.querySelectorAll('*').length, htmlKB: Math.round(c.innerHTML.length / 1024), lazy: c.querySelectorAll('[data-sb-lazy]').length, cards: c.querySelectorAll('.math-accordion-card').length };
      // open every card the way a reader does: click its header
      c.querySelectorAll('.math-accordion-card .math-acc-header').forEach(h => h.click());
      await app.settle();
      rec.lazyAfter = c.querySelectorAll('[data-sb-lazy]').length;
      rec.html = normIds(c.innerHTML.replace(/ data-sb-lazy="\d+"/g, '').replace(/\s+/g, ' '));
      rec.open = c.querySelectorAll('.math-accordion-card.open').length;
      out.push(rec);
      // the same renderer called from anywhere else returns the whole page
      if (lazy) rec.outside = (() => {      // assigned at any other time than while a tab is switched: kept whole
        const big = 'x'.repeat(5000); c.innerHTML = '<p>' + 'y'.repeat(200000) + '</p><div class="math-accordion-card"><div class="math-accordion-body" style="display:none"><div>' + big + '</div></div></div>'; return c.querySelectorAll('[data-sb-lazy]').length === 0 && c.querySelector('.math-accordion-body').innerHTML.length > 5000; })();
    }
    return out;
  }
  const off = await session(false), on = await session(true);
  for (let i = 0; i < SUBJECTS.length; i++) {
    const a = off[i], b = on[i];
    check(`${a.sid}: flag off, nothing is deferred`, a.lazy === 0 && a.cards > 3, JSON.stringify({ lazy: a.lazy, cards: a.cards }));
    const least = SUBJECTS[i][3];
    check(`${a.sid}: flag on, the tab is smaller by at least ${Math.round(least * 100)} % (${a.elements} -> ${b.elements} elements, ${a.htmlKB} -> ${b.htmlKB} KB, ${b.lazy} bodies kept back)`, b.elements <= a.elements && b.elements <= a.elements * (1 - least) && (least === 0 || b.lazy >= 1));
    check(`${a.sid}: opening every card fills every body`, b.lazyAfter === 0 && b.open === a.open);
    { let k = 0; while (k < a.html.length && a.html[k] === b.html[k]) k++;
      check(`${a.sid}: once every card is open the page is identical to the eager one`, a.html === b.html, a.html.length + ' vs ' + b.html.length + ' first difference at ' + k + ': eager ...' + a.html.slice(Math.max(0, k - 60), k + 100) + ' | lazy ...' + b.html.slice(Math.max(0, k - 60), k + 100)); }
  }
  check('what is assigned to the tab container outside a tab switch (printing, comparing tabs) is kept whole', on.every(r => r.outside === true));
  console.log(`lazy cards tests: ${passed} passed, ${failed} failed`);
  console.log(JSON.stringify(off.map((a, i) => ({ sid: a.sid, off: a.elements, on: on[i].elements, kbOff: a.htmlKB, kbOn: on[i].htmlKB }))));
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
