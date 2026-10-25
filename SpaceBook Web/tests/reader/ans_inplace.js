'use strict';
/* "Ans" / "جواب" shows its answer IN PLACE (js/sb_solve.js, IN_PLACE): in the dash of a fill-in-the-blank question, otherwise in a small box
 * right under the question, on the same page; no answer window opens and no word meaning pops up. Maths solutions (worked steps with equations) open the answer
 * window instead, on a wide screen and on a phone. Opens Class 12 Pakistan Studies, Class 8 English and Class 8 Maths in the installed Chrome:
 *     node --max-old-space-size=4096 tests/reader/ans_inplace.js
 * Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  async function open(width, height, cls, subj, call) {
    const ctx = await browser.newContext({ viewport: { width, height } });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {
      try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
    }
    if (width < 700) await page.evaluate(() => document.documentElement.classList.add('sbapp'));
    await page.evaluate(([c, s]) => openSubject(c, s), [cls, subj]); await sleep(2500);
    await page.evaluate(c => (0, eval)(c), call); await sleep(3500);
    await page.evaluate(() => { const b = document.querySelector('.math-nav-tabs [data-tab="exercise"], .math-top-tab[data-tab="exercise"], .math-tab-btn[data-tab="exercise"]'); if (b && !b.classList.contains('active')) b.click(); });
    await sleep(3000);
    return { ctx, page };
  }
  // the first Ans (in the open tab) whose question has a dash / has none; clicking is done by the page's own button
  const pick = (page, wantBlank) => page.evaluate(wantBlank => {
    const BL = /_{3,}|\.{4,}|…+|-{3,}|[—–]{2,}/;
    const root = document.getElementById('subjTabContent') || document.body;
    for (const b of root.querySelectorAll('.sb-ans')) {
      const se = b.closest('[class~="m6-s"]') || b.parentElement;
      const c = se.cloneNode(true); c.querySelectorAll('button,.sb-solve,[class*="-tr"]').forEach(n => n.remove());
      if (BL.test(c.textContent) === wantBlank) { b.setAttribute('data-test-ans', '1'); b.scrollIntoView({ block: 'center' }); return true; }
    }
    return false;
  }, wantBlank);

  for (const [w, h, label] of [[1360, 900, 'desktop'], [411, 900, 'phone']]) {
    const { ctx, page } = await open(w, h, 'cls12', 'cls12-pak', "selectSubjectChapter('pakstudy', 1, 'cls12')");
    await sleep(500);
    // 1. a fill-in-the-blank question: the answer goes into the dash
    check(`${label}: Pakistan Studies has a question with a dash`, await pick(page, true));
    const before = await page.evaluate(() => { const b = document.querySelector('[data-test-ans]'); const se = b.closest('[class~="m6-s"]') || b.parentElement; const tr = se.nextElementSibling; return { text: se.textContent, en: tr && tr.querySelector('p[lang="en"]') ? tr.querySelector('p[lang="en"]').textContent : '' }; });
    await page.click('[data-test-ans]'); await sleep(900);
    const filled = await page.evaluate(() => {
      const b = document.querySelector('[data-test-ans]'); const se = b.closest('[class~="m6-s"]') || b.parentElement; const tr = se.nextElementSibling;
      return { fills: [...document.querySelectorAll('.sbs-fill')].map(x => x.textContent), inSentence: !!se.querySelector('.sbs-fill'), enFill: tr ? [...tr.querySelectorAll('p[lang="en"] .sbs-fill')].map(x => x.textContent) : [], modal: !!document.querySelector('.bk-modal'), full: !!document.querySelector('.sbs-fs'), expanded: b.getAttribute('aria-expanded') };
    });
    check(`${label}: the answer is written in the dash of the question`, filled.inSentence && filled.fills[0] === 'غدر', filled);
    check(`${label}: the English line of the same question gets its English answer`, filled.enFill[0] === 'Mutiny', filled.enFill);
    check(`${label}: no answer window opens`, !filled.modal && !filled.full && filled.expanded === 'true', filled);
    await page.click('[data-test-ans]'); await sleep(600);
    const back = await page.evaluate(() => { const b = document.querySelector('[data-test-ans]'); const se = b.closest('[class~="m6-s"]') || b.parentElement; return { fills: document.querySelectorAll('.sbs-fill').length, text: se.textContent.replace(/\s+/g, ' ').trim(), expanded: b.getAttribute('aria-expanded') }; });
    check(`${label}: a second tap puts the dash back`, back.fills === 0 && back.expanded === 'false' && back.text.replace(/جواب|🔊/g, '').replace(/\s+/g, ' ').trim() === before.text.replace(/جواب|🔊/g, '').replace(/\s+/g, ' ').trim(), { back, before: before.text.slice(0, 80) });
    await page.evaluate(() => document.querySelector('[data-test-ans]').removeAttribute('data-test-ans'));

    // 2. a question without a dash: the answer box is right under the question, on the same page, not in a window
    check(`${label}: Pakistan Studies has a question without a dash`, await pick(page, false));
    await page.click('[data-test-ans]'); await sleep(900);
    const box = await page.evaluate(() => {
      const b = document.querySelector('[data-test-ans]'); const q = b.closest('.m6-part, .m6-q') || b.parentElement; const p = [...q.querySelectorAll('.sb-solve')].find(x => !x.hidden);
      const bb = b.getBoundingClientRect(), pb = p ? p.getBoundingClientRect() : null;
      return { open: !!p, inPlace: !!(p && p.classList.contains('sbs-inline')), answer: p ? (p.querySelector('.sbs-final') || {}).textContent : '', below: pb ? pb.top >= bb.bottom - 2 : false, sameQuestion: !!(p && q.contains(p)), modal: !!document.querySelector('.bk-modal'), toolbar: !!(p && p.querySelector('.sbs-top')) };
    });
    check(`${label}: the answer shows just below its question`, box.open && box.inPlace && box.below && box.sameQuestion && box.answer && box.answer.trim().length > 4, box);
    check(`${label}: no answer window and no tool bar over a plain answer`, !box.modal && !box.toolbar, box);
    await ctx.close();
  }

  // 3. the Ans button is a button: resting the mouse on it does not open a word meaning
  {
    const { ctx, page } = await open(1360, 900, 'cls12', 'cls12-pak', "selectSubjectChapter('pakstudy', 1, 'cls12')");
    check('desktop: an Ans button is on screen', await pick(page, false));
    const at = await page.evaluate(() => { const r = document.querySelector('[data-test-ans]').getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; });
    await page.mouse.move(at.x - 40, at.y); await page.mouse.move(at.x, at.y, { steps: 4 }); await sleep(1100);
    const card = await page.evaluate(() => { const c = document.querySelector('.ut-card.ut-show, .ut-root .ut-show'); return !!c; });
    check('desktop: resting the mouse on Ans / جواب shows no meaning card', !card);
    // control: the same mouse rest on an ordinary word of the question does open the card (so the check above can fail)
    const word = await page.evaluate(() => {
      const b = document.querySelector('[data-test-ans]'), se = b.closest('[class~="m6-s"]') || b.parentElement;
      const w = document.createTreeWalker(se, NodeFilter.SHOW_TEXT);
      for (let n; (n = w.nextNode());) {
        if (n.parentElement.closest('button')) continue;
        const m = /[\p{L}]{3,}/u.exec(n.data); if (!m) continue;
        const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        const q = r.getBoundingClientRect(); if (q.width > 0) return { x: q.x + q.width / 2, y: q.y + q.height / 2 };
      }
      return null;
    });
    if (word) {
      await page.mouse.move(word.x + 30, word.y + 60); await page.mouse.move(word.x, word.y, { steps: 4 }); await sleep(1200);
      check('desktop: (control) resting the mouse on an ordinary word opens its meaning card', await page.evaluate(() => !!document.querySelector('.ut-card.ut-show, .ut-root .ut-show')));
    }
    await ctx.close();
  }

  // 4. every book answers in place: Class 8 English (no tool bar, no window) ...
  {
    const { ctx, page } = await open(1360, 900, 'cls8', 'cls8-eng', "selectSubjectChapter('eng', 1, 'cls8')");
    const has = await page.evaluate(() => { const b = document.querySelector('#subjTabContent .sb-ans'); if (!b) return false; b.scrollIntoView({ block: 'center' }); b.setAttribute('data-test-ans', '1'); return true; });
    check('Class 8 English: an Ans button is on screen', has);
    if (has) {
      await page.click('[data-test-ans]'); await sleep(1000);
      const r = await page.evaluate(() => ({ inPlace: !!document.querySelector('.sb-solve.sbs-inline:not([hidden])'), bar: !!document.querySelector('.sb-solve .sbs-top'), modal: !!document.querySelector('.bk-modal') }));
      check('Class 8 English: the answer shows in place (no tool bar, no window)', r.inPlace && !r.bar && !r.modal, r);
    }
    await ctx.close();
  }

  // 5. ... and a maths solution (worked steps) opens the answer window, on a wide screen and on a phone, and the window closes again
  for (const [w, h, label] of [[1360, 900, 'desktop'], [411, 900, 'phone']]) {
    const { ctx, page } = await open(w, h, 'cls8', 'cls8-math', "selectSubjectChapter('math', 1, 'cls8')");
    const n = await page.evaluate(() => document.querySelectorAll('#subjTabContent .sb-ans, #mathTabContent .sb-ans').length);
    check(`${label}: Class 8 Maths has Ans buttons`, n > 0, n);
    let seen = null;
    for (let k = 0; k < Math.min(n, 10) && !seen; k++) {
      await page.evaluate(k => { const b = [...document.querySelectorAll('#subjTabContent .sb-ans, #mathTabContent .sb-ans')][k]; b.setAttribute('data-test-ans', '1'); b.scrollIntoView({ block: 'center' }); }, k);
      await page.evaluate(() => document.querySelector('[data-test-ans]').click()); await sleep(1200);   // the button itself (a page's bookmark icons can sit over the first Ans of a page)
      const r = await page.evaluate(() => { const m = document.querySelector('.bk-modal'); return { modal: !!m, bar: !!(m && m.querySelector('.sbs-top')), steps: m ? m.querySelectorAll('.sbs-step').length : 0, fits: m ? (() => { const c = m.querySelector('.bk-modal-card').getBoundingClientRect(); return c.left >= -1 && c.right <= innerWidth + 1 && c.bottom <= innerHeight + 1; })() : false }; });
      if (r.modal) seen = r;
      else { await page.evaluate(() => { document.querySelector('[data-test-ans]').click(); document.querySelector('[data-test-ans]').removeAttribute('data-test-ans'); }); await sleep(300); continue; }
    }
    check(`${label}: a maths solution opens the answer window with its tool bar and steps`, !!seen && seen.bar && seen.steps > 0, seen);
    check(`${label}: the answer window fits the screen`, !!seen && seen.fits, seen);
    if (seen) {
      await page.click('.bk-modal-x'); await sleep(500);
      const back = await page.evaluate(() => ({ modal: !!document.querySelector('.bk-modal'), expanded: document.querySelector('[data-test-ans]').getAttribute('aria-expanded') }));
      check(`${label}: Close takes the answer window away`, !back.modal && back.expanded === 'false', back);
    }
    await ctx.close();
  }

  check('no page errors', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
