'use strict';
/* In the Android app's reader, a tap on "Ans" / "جواب" opens the answer, and a tap on the sentence text still asks for its meaning.
 * "Ans" sits inside the element of the sentence it answers; the app's tap handler once took its tap for a tap on that sentence (a meaning
 * pop-up, the answer never opened). Local only, like the other tests/app files (needs the installed Chrome and the sibling "SpaceBook App" folder):
 *     node tests/app/ans_tap.js [subjectId,subjectId ...] */
const fs = require('fs'), path = require('path');
const { open, sleep, APP_ASSETS } = require('./phone');

const catalog = JSON.parse(fs.readFileSync(path.join(APP_ASSETS, 'app_catalog.json'), 'utf8'));
// one book whose Ans buttons are inside the sentence (English 8, Pakistan Studies 12) and one whose are not (Maths 5)
const subjects = (process.argv[2] || 'cls8-eng,cls12-pak,cls5-math').split(',');
const SENT = '.lesson-sentence,.sb-tri-target,[class*="-s"][onclick]';

(async () => {
  const t = await open({ width: 411, height: 900 });
  let fails = 0;
  const ok = (cond, msg) => { console.log((cond ? 'ok    ' : 'FAIL  ') + msg); if (!cond) fails++; };
  try {
    await t.page.evaluate(() => { window.__acts = []; window.SBHost = { onReady() { }, onState() { }, onAction(n) { window.__acts.push(n); } }; });
    for (const sid of subjects) {
      const cl = catalog.classes.find(c => c.subjects.some(s => s.id === sid)); if (!cl) { ok(false, sid + ' is not in the catalog'); continue; }
      const subj = cl.subjects.find(s => s.id === sid);
      let found = false;
      for (let ci = 1; ci < Math.min(subj.chapters.length, 6) && !found; ci++) {
        await t.chapter(cl.id, sid, subj.chapters[ci].o, 0, 'Lessons');
        await t.settle();
        await t.page.evaluate(() => { const b = document.querySelector('.math-nav-tabs [data-tab="exercise"], .math-top-tab[data-tab="exercise"], .math-tab-btn[data-tab="exercise"]'); if (b && !b.classList.contains('active')) b.click(); });
        await t.settle();
        const pages = (await t.state()).pages || 1;
        for (let n = 0; n < pages && !found; n++) {
          await t.page.evaluate(i => { if (window.SBApp.state().pages) window.SBApp.go(i); }, n);
          await sleep(500);
          // bring the first visible Ans into view and say where it is, and where the text of its sentence is
          const spot = await t.page.evaluate(sel => {
            const root = document.querySelector('.sbapp-page-on') || document.body;
            const b = [...root.querySelectorAll('.sb-ans')].find(x => x.getBoundingClientRect().width > 0); if (!b) return null;
            b.scrollIntoView({ block: 'center' });
            const se = b.closest(sel);
            let text = null;
            if (se) {
              const w = document.createTreeWalker(se, NodeFilter.SHOW_TEXT); let nd;
              while ((nd = w.nextNode())) {
                if (nd.parentElement.closest('button,.sb-ans,.sb-solve')) continue;
                const m = /\p{L}{3,}/u.exec(nd.data); if (!m) continue;
                const r = document.createRange(); r.setStart(nd, m.index); r.setEnd(nd, m.index + m[0].length);
                if (r.getBoundingClientRect().width > 0) { nd.parentElement.scrollIntoView({ block: 'center' }); text = true; break; }
              }
            }
            return { inSentence: !!se, hasText: !!text };
          }, SENT);
          if (!spot) continue;
          found = true;
          await sleep(300);
          const at = await t.page.evaluate(() => { const root = document.querySelector('.sbapp-page-on') || document.body; const b = [...root.querySelectorAll('.sb-ans')].find(x => x.getBoundingClientRect().width > 0); const r = b.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2, label: b.textContent.trim() }; });
          await t.page.evaluate(() => { window.__acts = []; });
          await t.page.touchscreen.tap(at.x, at.y);
          await sleep(1200);
          const r = await t.page.evaluate(() => ({ acts: window.__acts.slice(), open: [...document.querySelectorAll('.sb-ans')].filter(b => b.getAttribute('aria-expanded') === 'true').length }));
          ok(r.open === 1 && !r.acts.includes('meaning'), `${sid} ch${ci}: tap on "${at.label}"${spot.inSentence ? ' (inside its sentence)' : ''} opens the answer, no meaning pop-up (opened ${r.open}, host got [${r.acts}])`);
          if (spot.inSentence && spot.hasText) {
            const tx = await t.page.evaluate(sel => {
              const root = document.querySelector('.sbapp-page-on') || document.body;
              const b = [...root.querySelectorAll('.sb-ans')].find(x => x.getBoundingClientRect().width > 0); const se = b && b.closest(sel); if (!se) return null;
              const w = document.createTreeWalker(se, NodeFilter.SHOW_TEXT); let nd;
              while ((nd = w.nextNode())) {
                if (nd.parentElement.closest('button,.sb-ans,.sb-solve')) continue;
                const m = /\p{L}{3,}/u.exec(nd.data); if (!m) continue;
                const rg = document.createRange(); rg.setStart(nd, m.index); rg.setEnd(nd, m.index + m[0].length);
                const q = rg.getBoundingClientRect(); if (q.width > 0) return { x: q.x + q.width / 2, y: q.y + q.height / 2 };
              }
              return null;
            }, SENT);
            if (tx) {
              await t.page.evaluate(() => { window.__acts = []; });
              await t.page.touchscreen.tap(tx.x, tx.y);
              await sleep(1200);
              const acts = await t.page.evaluate(() => window.__acts.slice());
              ok(acts.includes('meaning'), `${sid}: a tap on the sentence text still asks for its meaning (host got [${acts}])`);
            }
          }
        }
      }
      if (!found) ok(false, sid + ': no Ans button found in the first chapters');
    }
    if (t.errors.length) { console.log(t.errors.join('\n')); fails++; }
  } finally { await t.close(); }
  console.log(fails ? `\n${fails} FAILED` : '\nall passed');
  process.exit(fails ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
