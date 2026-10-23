'use strict';
/* "Fill the table" and "Show the work" in a real browser:  node --max-old-space-size=6144 tests/fills/browser.js
 * Every table and project box of the books that has a fill (js/fills_data.js) is drawn by the reader into a bare page and its button pressed: a table ends with
 * no empty cell (jagged rows get their missing cells) and goes back to its first look; a project shows its panel with its drawings. A table or box that has
 * no fill has no button. The same buttons are found in a real chapter. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 1000, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
  }
  const fills = await page.evaluate(() => { const F = window.SB_FILLS || {}; return {n: Object.keys(F).length, tables: Object.values(F).filter(f => f.t === 'table').length, work: Object.values(F).filter(f => f.t === 'work').length}; });
  check('the fills are loaded: tables and project work', fills.tables >= 5 && fills.work >= 15, fills);
  // draw every unit of every book that has a fill, press every button
  const report = await page.evaluate(() => {
    const R = window.MATH6_READER, out = {tables: 0, filledOk: 0, emptiedOk: 0, jagged: 0, works: 0, worksOk: 0, svgs: 0, noFillButtons: 0, nodes: []};
    for (let n = 1; n <= 12; n++) {
      const L = window['CLS' + n + '_BOOKS']; if (!L) continue;
      Object.keys(L).forEach(k => {
        const B = L[k]; if (!B || !B.units) return;
        B.units.forEach(u => {
          const picked = [];
          (function walk(list) { (list || []).forEach(b => { if (!b || typeof b !== 'object') return; if (b.t === 'table' || b.t === 'box') picked.push(b); if (b.t !== 'box') walk(b.blocks); }); })((u.sections || []).flatMap(s => s.blocks));
          if (!picked.length) return;
          const host = document.createElement('div');
          host.innerHTML = R.withBook(B.words, B.book, () => '<div class="probe-root">' + R.blocks(picked, {}) + '</div>');
          if (!host.querySelector('.sb-fill-btn')) return;
          document.body.appendChild(host);
          host.querySelectorAll('.m6-table[data-fkey]').forEach(t => {
            out.tables++;
            const emptyBefore = [...t.querySelectorAll('tbody td')].filter(td => !td.textContent.trim() && !td.children.length).length;
            const cellsBefore = t.querySelectorAll('tbody td').length;
            t.querySelector('.sb-fill-btn').click();
            const emptyAfter = [...t.querySelectorAll('tbody td')].filter(td => !td.textContent.trim() && !td.children.length).length;
            if (emptyAfter === 0 && emptyBefore > 0) out.filledOk++; else out.nodes.push('table of ' + k + ' unit ' + u.number + ': ' + emptyAfter + ' cells still empty');
            if (t.querySelectorAll('tbody td').length > cellsBefore) out.jagged++;
            t.querySelector('.sb-fill-btn').click();
            const back = [...t.querySelectorAll('tbody td')].filter(td => !td.textContent.trim() && !td.children.length).length;
            if (back === emptyBefore && t.querySelectorAll('tbody td').length === cellsBefore) out.emptiedOk++; else out.nodes.push('table of ' + k + ' unit ' + u.number + ' did not return to its first look');
          });
          host.querySelectorAll('.m6-box[data-fkey]').forEach(bx => {
            out.works++;
            bx.querySelector('.sb-fill-btn').click();
            const panel = bx.querySelector(':scope > .sb-work');
            if (panel && !panel.hidden && panel.textContent.trim().length > 80) out.worksOk++; else out.nodes.push('work of ' + k + ' unit ' + u.number + ' did not open');
            out.svgs += panel ? panel.querySelectorAll('svg').length : 0;
            bx.querySelector('.sb-fill-btn').click();
            if (!bx.querySelector(':scope > .sb-work').hidden) out.nodes.push('work of ' + k + ' unit ' + u.number + ' did not close');
          });
          // a table with empty cells and no fill gets no button
          host.querySelectorAll('.m6-table:not([data-fkey])').forEach(t => { if (t.querySelector('.sb-fill-btn')) out.noFillButtons++; });
          host.remove();
        });
      });
    }
    return out;
  });
  check('every table with a fill ends with no empty cell', report.tables > 0 && report.filledOk === report.tables, report);
  check('pressing the button again puts the table back as the book printed it', report.emptiedOk === report.tables, report.nodes.slice(0, 3));
  check('cells a printed row was missing are added (jagged rows)', report.jagged >= 1, report.jagged);
  check('every project with a fill shows its work, and closes again', report.works > 0 && report.worksOk === report.works, report.nodes.slice(0, 3));
  check('the work of a model project has drawings', report.svgs >= 5, report.svgs);
  check('a table without a fill has no button', report.noFillButtons === 0, report.noFillButtons);
  // in a real chapter the buttons are there (Class 9 Chemistry, unit 4)
  await page.evaluate(() => { goToSubjects('cls9'); openSubject('cls9', 'cls9-chem'); selectSubjectChapter('chem', 3, 'cls9'); });
  await sleep(4000);
  const real = await page.evaluate(() => document.querySelectorAll('.sb-fill-btn').length);
  check('a real chapter shows fill buttons', real >= 1, real);
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('fill tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
