'use strict';
/* The activity cards of Classes 1 and 2 start folded and a pill opens each one (js/sb_card_fold.js), in a real browser:
 *     node --max-old-space-size=6144 tests/reader/cards.js
 * Opens the Exercise tab of Class 2 English and Class 1 Maths and the Urdu Exercise tab of Class 2. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];

  async function openBook(classId, subjectId, key, tabText) {
    const ctx = await browser.newContext({ viewport: { width: 1366, height: 768 } });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {
      try {
        await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 });
        await sleep(3000);
        if (await page.evaluate(() => typeof openSubject === 'function')) break;
      } catch (e) { /* reloaded */ }
    }
    await page.evaluate(c => { goToSubjects(c); }, classId); await sleep(500);
    await page.evaluate(([c, s]) => { openSubject(c, s); }, [classId, subjectId]); await sleep(1000);
    await page.evaluate(([k, c]) => { selectSubjectChapter(k, 0, c); }, [key, classId]); await sleep(3000);
    const tabs = await page.$$('xpath=//div[contains(@class,"math-nav-tabs")]//button');
    const names = await Promise.all(tabs.map(t => t.textContent()));
    const t = tabs[names.findIndex(n => n.includes(tabText))];
    if (t) { await t.click(); await sleep(3000); }
    await page.evaluate(() => { document.querySelectorAll('.math-accordion-card:not(.open) .math-acc-header').forEach(h => { try { h.click(); } catch (e) { /* ignore */ } }); });
    await sleep(2500);
    return { ctx, page };
  }
  const facts = page => page.evaluate(() => {
    const cards = [...document.querySelectorAll('.c1a-card')];
    return {
      cards: cards.length, shown: cards.filter(c => c.getBoundingClientRect().height > 0).length,
      pills: document.querySelectorAll('.sb-fold-pill').length,
      linked: [...document.querySelectorAll('.sb-fold-pill')].filter(p => document.getElementById(p.getAttribute('aria-controls'))).length,
      oldPills: document.querySelectorAll('.c1a-doit').length
    };
  });

  for (const [name, args] of [['Class 2 English', ['cls2', 'cls2-eng', 'eng', 'Exercise']], ['Class 1 Maths', ['cls1', 'cls1-math', 'math', 'Exercises']], ['Class 2 Urdu', ['cls2', 'cls2-urdu', 'urdu', 'مشق']]]) {
    const { ctx, page } = await openBook(...args);
    const f = await facts(page);
    check(name + ': the book has activity cards', f.cards >= 5, f);
    check(name + ': every card starts folded', f.shown === 0, f);
    check(name + ': every card has a pill, and the old Let\'s do it button is gone', f.pills >= f.cards && f.linked === f.pills && f.oldPills === 0, f);
    const pill = await page.$('.sb-fold-pill');
    await pill.scrollIntoViewIfNeeded(); await pill.click(); await sleep(500);
    const open = await page.evaluate(() => { const p = document.querySelector('.sb-fold-pill'); const c = document.getElementById(p.getAttribute('aria-controls')); return { exp: p.getAttribute('aria-expanded'), h: Math.round(c.getBoundingClientRect().height), same: c.querySelector('.c1a-h') ? p.textContent === c.querySelector('.c1a-h').textContent.replace(/\s+/g, ' ').trim() : true }; });
    check(name + ': pressing the pill opens its card (the pill carries the card\'s title)', open.exp === 'true' && open.h > 20 && open.same, open);
    await (await page.$('.sb-fold-pill')).click(); await sleep(300);
    check(name + ': pressing it again folds the card', await page.evaluate(() => { const p = document.querySelector('.sb-fold-pill'); return document.getElementById(p.getAttribute('aria-controls')).getBoundingClientRect().height === 0 && p.getAttribute('aria-expanded') === 'false'; }));
    await ctx.close();
  }
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('activity card tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
