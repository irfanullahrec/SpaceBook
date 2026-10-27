'use strict';
/* The Ans buttons of the Mathematics chapters of Classes 5, 6, 7, 8 and 11 in a real browser (finding M-01 of docs/launch/FINDINGS_REGISTER.md).
 * On a wide screen the Exercises tab is the open book of js/sb_book_spread.js, drawn with the Class 6 reader; the SpaceBook solution ids ("s814") repeat from
 * class to class, so every Ans button and multiple-choice widget of another class must carry its class and read that class's own solutions file.
 * Real clicks (class card, subject card, chapter button, Exercises tab) at 1280 px; per class:
 *   1. every Ans button that is not a printed-key record names its class (Class 5: m6SolOpen(this,'s814','5'); Class 6 names none), and every multiple-choice
 *      widget has the source of its class ('m6c5', 'm6c7', ...; Class 6: 'm6');
 *   2. pressing Ans on one named question shows the answer that exists only in that class's solutions file.
 *   SB_PAGE=lazy.html node --max-old-space-size=3072 tests/launch/maths_answers_browser.js
 * Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };

// class number, chapter (1-based as in the book), the question to press (the text of its button's line), the text its panel must show
const TARGETS = [
  [5, 7, '^a\\)\\s*3\\.4 cm\\W*Ans', 'Square of side 3.4 cm'],
  [6, 1, 'The number is greater than 10\\.', 'Numbers 11 to 100 remain'],
  [7, 11, '^Square\\W*Ans', 'Draw AB = 4 cm'],
  [8, 5, 'How many students like only pizza\\?', 'Only pizza is the region of the pizza circle'],
  [11, 1, null, null],
];

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  for (const [n, chNo, rx, expect] of TARGETS) {
    const cls = 'cls' + n, sid = cls + '-math';
    const page = await (await browser.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 150)));
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'load', timeout: 180000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 180000 });
    await sleep(3000);
    await page.evaluate(c => { [...document.querySelectorAll('[onclick]')].find(e => e.getAttribute('onclick') === `goToSubjects('${c}')`).click(); }, cls);
    await sleep(1500);
    await page.evaluate(([c, s]) => { [...document.querySelectorAll('[onclick]')].find(e => e.getAttribute('onclick').replace(/\s/g, '') === `openSubject('${c}','${s}')`).click(); }, [cls, sid]);
    await sleep(2500);
    await page.evaluate(i => { document.querySelectorAll('.math-ch-btn')[i].click(); }, chNo - 1);
    await sleep(2500);
    const r = await page.evaluate(async ([n, rx, expect]) => {
      const tab = [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].find(b => /exercise/i.test(b.textContent));
      tab.click(); await new Promise(r => setTimeout(r, 2000));
      const norm = t => (t || '').replace(/\s+/g, ' ').trim();
      const ans = [...document.querySelectorAll('button.sb-ans')];
      const out = { buttons: ans.length, wrong: [], mcq: [] };
      ans.forEach(a => {
        const m = /m6SolOpen\(this,'([^']+)'(?:,'(\d+)')?\)/.exec(a.getAttribute('onclick') || '');
        if (!m) { out.wrong.push('no m6SolOpen: ' + (a.getAttribute('onclick') || '').slice(0, 60)); return; }
        const own = /^k\d+$/.test(m[1]) || m[1].includes('-');          // a printed-key record or a book with inline answers: no class needed
        if (!own && String(m[2] || '6') !== String(n)) out.wrong.push(m[1] + ' -> class ' + (m[2] || '6'));
      });
      out.mcq = [...new Set([...document.querySelectorAll('[data-src]')].map(e => e.dataset.src))];
      if (rx) {
        const re = new RegExp(rx);
        const btn = ans.find(a => re.test(norm(a.parentElement.textContent)));
        out.found = !!btn;
        if (btn) {
          btn.scrollIntoView({ block: 'center' });
          btn.click();
          for (let k = 0; k < 60; k++) {
            await new Promise(r => setTimeout(r, 200));
            const p = [...document.querySelectorAll('.sb-solve')].find(x => !x.hidden && norm(x.textContent).length > 5 && !/^Loading the solution/.test(norm(x.textContent)));   // the solutions file loads on the first press
            if (p) { out.panel = norm(p.textContent).slice(0, 220); break; }
          }
          out.shown = !!out.panel && out.panel.includes(expect);
        }
      }
      return out;
    }, [n, rx, expect]);
    check(`Class ${n} chapter ${chNo}: ${r.buttons} Ans buttons, every one names class ${n}`, r.buttons > 0 && r.wrong.length === 0, r.wrong.slice(0, 3));
    const want = n === 6 ? ['m6'] : ['m6c' + n];
    check(`Class ${n} chapter ${chNo}: the multiple-choice widgets read class ${n}'s solutions (${r.mcq.join(', ') || 'none'})`, r.mcq.every(s => want.includes(s)), r.mcq);
    if (rx) check(`Class ${n} chapter ${chNo}: Ans on the named question shows the class's own answer`, r.found && r.shown === true, r.panel || r.found);
    if (n === 11) {
      // a multiple-choice question answers from Class 11's own key: the option the key names is marked right, a wrong pick is marked wrong
      const q = await page.evaluate(async () => {
        const g = [...document.querySelectorAll('[data-src="m6c11"]')].find(x => x.querySelectorAll('input[type=radio]').length);
        if (!g) return { found: false };
        g.scrollIntoView({ block: 'center' });
        g.querySelectorAll('input[type=radio]')[0].click();
        await new Promise(r => setTimeout(r, 2000));
        const rec = (window.MATH_11_SOLUTIONS || {})[g.dataset.sol];
        const key = rec && /^\(?([a-d])\)?/i.exec(String(rec.answer || ''));
        const opts = [...g.querySelectorAll('label')];
        const right = opts.findIndex(l => l.classList.contains('is-correct'));
        return { found: true, answered: g.classList.contains('is-answered'), key: key && key[1].toLowerCase(), right: right >= 0 ? 'abcd'[right] : null };
      });
      check('Class 11: a multiple-choice question marks the option of Class 11\'s own key', q.found && q.answered && !!q.key && q.key === q.right, q);
    }
    check(`Class ${n}: no script error`, errors.length === 0, errors.slice(0, 3));
    await page.context().close();
  }
  // a phone-width screen has no open book: each class draws its own chapter with its own reader and handler (mNSolOpen)
  for (const [n, chNo] of [[5, 7], [7, 11], [8, 5], [11, 1]]) {
    const cls = 'cls' + n, sid = cls + '-math';
    const page = await (await browser.newContext({ viewport: { width: 390, height: 844 } })).newPage();
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'load', timeout: 180000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 180000 });
    await sleep(3000);
    await page.evaluate(c => { [...document.querySelectorAll('[onclick]')].find(e => e.getAttribute('onclick') === `goToSubjects('${c}')`).click(); }, cls);
    await sleep(1500);
    await page.evaluate(([c, s]) => { [...document.querySelectorAll('[onclick]')].find(e => e.getAttribute('onclick').replace(/\s/g, '') === `openSubject('${c}','${s}')`).click(); }, [cls, sid]);
    await sleep(2500);
    await page.evaluate(i => { document.querySelectorAll('.math-ch-btn')[i].click(); }, chNo - 1);
    await sleep(2500);
    const r = await page.evaluate(async n => {
      const tab = [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].find(b => /exercise/i.test(b.textContent));
      tab.click(); await new Promise(r => setTimeout(r, 2000));
      const ans = [...document.querySelectorAll('button.sb-ans')];
      const own = ans.filter(a => new RegExp('m' + n + 'SolOpen\\(').test(a.getAttribute('onclick') || ''));
      return { buttons: ans.length, own: own.length, roots: [...new Set([...document.querySelectorAll('[class*="-root"]')].map(e => e.className.split(' ')[0]))] };
    }, n);
    check(`Class ${n} on a phone: ${r.buttons} Ans buttons, all of them use the Class ${n} handler (${r.roots.join(', ')})`, r.buttons > 0 && r.own === r.buttons, r);
    await page.context().close();
  }
  console.log('---\nmaths answers browser test: ' + pass + ' passed, ' + fail + ' failed');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
