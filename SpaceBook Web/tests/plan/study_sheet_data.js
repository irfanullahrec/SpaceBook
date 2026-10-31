'use strict';
/* The lesson sheet of the Study Plan ("Go" on lesson parts, js/sb_study_sheet.js) against the real book data:   node --max-old-space-size=8192 tests/plan/study_sheet_data.js [--report]
 * For every chapter of every subject of the plan index (js/study_plan_index.js): where the book is in the form the sheet reads, the number of lesson parts it finds is
 * the number the plan counted ("read"), so "Read lesson parts 3-5" is the third to fifth lesson section of that chapter; every part gives a title, and the first
 * part of every chapter renders to non-empty text without an error. The subjects the sheet cannot read (the book is not in that form) are listed: "Go" takes the
 * student to the chapter page there, as it always did. Dev-only, never shipped. */
const { load } = require('../../tools/lib/app_sandbox');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 500) : '')); } };

const app = load({ page: 'index.html', quiet: true });
const res = JSON.parse(app.run(`(function () {
  const SS = window.SBStudySheet, IX = window.SB_STUDY_INDEX;
  const out = {has: !!SS, tooMany: SS.partsFor('cls7', 'cls7-math', 0, 1, 99, 99), subjects: 0, covered: [], uncovered: [], chapters: 0, same: 0, shared: [], fewer: [], bad: [], noTitle: [], emptyFirst: [], threw: [], parts: 0};
  for (const C of IX.classes) for (const S of C.subjects) {
    out.subjects++;
    let bk = null; try { bk = SS.bookOf(C.id, S.id); } catch (e) { out.threw.push([S.id, 'bookOf', String(e.message).slice(0, 80)]); }
    if (!bk || bk.units.length !== S.chapters.length) { out.uncovered.push(S.id + (bk ? ' (' + bk.units.length + ' units, ' + S.chapters.length + ' chapters)' : '')); continue; }
    out.covered.push(S.id);
    S.chapters.forEach((ch, i) => {
      out.chapters++;
      let L = null, parts = null;
      try { L = SS.lessonCount(C.id, S.id, i); parts = SS.partsFor(C.id, S.id, i, 1, ch.c.read, ch.c.read); } catch (e) { out.threw.push([S.id, i, String(e.message).slice(0, 80)]); return; }
      if (!parts) { out.fewer.push([S.id, i, L, ch.c.read]); return; }                       // the book has fewer parts than the plan counted: the chapter page
      if (L === ch.c.read) out.same++; else out.shared.push([S.id, i, L, ch.c.read]);
      const all = [].concat(...parts.map(p => p.sections));
      if (parts.length !== ch.c.read || all.length !== L || all.some((x, k) => x !== k + 1)) out.bad.push([S.id, i, L, ch.c.read, parts.length]);
      out.parts += parts.length;
      if (parts.some(p => !p.title)) out.noTitle.push([S.id, i]);
      try { const h = parts[0].html(); if (!h || h.length < 20) out.emptyFirst.push([S.id, i, parts[0].title.slice(0, 30)]); } catch (e) { out.threw.push([S.id, i, 'html: ' + String(e.message).slice(0, 80)]); }
    });
  }
  return JSON.stringify(out);
})()`, 600000));

check('the sheet module is loaded with the page, and asking for more parts than the chapter has gives null', res.has && res.tooMany === null, res.tooMany);
check('no subject or chapter made the sheet throw', res.threw.length === 0, res.threw.slice(0, 5));
check('in every chapter it can read, the parts are the plan\'s count and together they are every lesson section of the chapter once, in order (' + res.same + ' of ' + res.chapters + ' chapters: part n is section n; ' + res.shared.length + ' where the book has more sections than the plan counted: they are shared out)', res.bad.length === 0, res.bad.slice(0, 8));
const fewer = res.fewer.filter(x => x[2] > 0);
// 11 on the Government books; the 6 chapters of the Munawar Class 4 Social Studies book (cls4-mun-sst) keep each lesson in one section while the plan counted 2 to 10 topic headings, so Go opens their chapter page
check('the chapters that fall back to the chapter page are those with no lesson section at all (' + (res.fewer.length - fewer.length) + ': reviews, drawing pages) and a handful where the book has fewer parts than the plan counted (' + fewer.length + ')', fewer.length <= 25, fewer.slice(0, 25));
check('every part has a title', res.noTitle.length === 0, res.noTitle.slice(0, 5));
check('the first part of the chapters renders to text (all but ' + res.emptyFirst.length + ': a part that holds only an exercise says so)', res.emptyFirst.length <= 3, res.emptyFirst.slice(0, 8));
const pct = Math.round(100 * res.covered.length / res.subjects);
check('the sheet reads most subjects of the plan (' + res.covered.length + ' of ' + res.subjects + ', ' + pct + ' %)', pct >= 75, res.uncovered);
if (process.argv.includes('--report') || fail) {
  console.log('\nsubjects the sheet cannot read (Go takes the student to the chapter page): ' + res.uncovered.join(', '));
  console.log(res.chapters + ' chapters, ' + res.parts + ' parts checked');
}
console.log('---\nstudy sheet data: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
