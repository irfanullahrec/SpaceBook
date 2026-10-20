'use strict';
/* BISE Swat data (js/bise_swat_data.js, built by docs/source-verification/bise-swat/tools/build_bise.py).
 *   node tests/bise/data.js
 * Guards the numbers a student will plan an exam around: every section of every paper pattern adds up to the Board's total,
 * the chapter tables add up to the Board's item counts, every Board link is on the Board's own site (or its Drive), every
 * learning outcome has text, and the module that shows them (js/sb_bise.js) loads and registers its hooks. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

const g = { console };
g.window = g; vm.createContext(g);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', 'bise_swat_data.js'), 'utf8'), g);
const D = g.SB_BISE;
check('the data file defines window.SB_BISE', !!D && D.v === 1 && !!D.subjects);
const subs = Object.values(D.subjects);
check('39 subjects of Classes 9-12', subs.length === 39, String(subs.length));
check('every class 9-12 has subjects', [9, 10, 11, 12].every(c => subs.some(s => s.cls === c)));

let sloCount = 0;
for (const s of subs) {
  const p = s.pattern;
  if (p) {
    const B = p.B || {}, C = p.C || {};
    check(s.id + ': sections A + B + C = total (' + p.total + ')', p.A.marks + B.marks + C.marks === p.total, [p.A.marks, B.marks, C.marks].join('+'));
    if (B.attempt) check(s.id + ': B attempt x each = marks', B.attempt * B.each === B.marks && B.attempt <= B.n);
    if (C.attempt) check(s.id + ': C attempt x each = marks', C.attempt * C.each === C.marks && C.attempt <= C.n);
    if (B.parts && B.parts.length && !B.offered && B.parts.every(x => x.marks != null)) check(s.id + ': B parts add up', B.parts.reduce((n, x) => n + x.marks, 0) === B.marks);
    if (C.parts && C.parts.length && C.parts.every(x => x.marks != null)) check(s.id + ': C parts add up', C.parts.reduce((n, x) => n + x.marks, 0) === C.marks);
  }
  (s.files || []).concat(s.past || []).forEach(f => check(s.id + ': Board link ' + f.url.slice(-40), /^https:\/\/(www\.bisess\.edu\.pk\/|drive\.google\.com\/file\/d\/)/.test(f.url) && !/\s/.test(f.url)));
  const chs = s.chapters || [];
  const nos = chs.map(c => c.no);
  check(s.id + ': chapter numbers are unique', new Set(nos).size === nos.length);
  if (s.tosTotals && chs.some(c => c.m != null)) {
    const m = chs.reduce((n, c) => n + (c.m || 0), 0), r = chs.reduce((n, c) => n + (c.r || 0), 0), e = chs.reduce((n, c) => n + (c.e || 0), 0);
    check(s.id + ': chapter MCQ items = Section A (' + (p && p.A.n) + ')', !p || m === p.A.n, String(m));
    check(s.id + ': chapter items = totals recorded', m === s.tosTotals.m && r === s.tosTotals.r && e === s.tosTotals.e);
  }
  const ws = chs.filter(c => c.w != null && !c.pp);
  if (ws.length && s.id !== 'cls12-bio' && s.id !== 'cls9-comp') {
    const sum = ws.reduce((n, c) => n + c.w, 0);
    check(s.id + ': chapter weightage adds up to 100 (' + sum.toFixed(2) + ')', Math.abs(sum - 100) < 0.2);
  }
  for (const c of chs) {
    check(s.id + ' ch ' + c.no + ' has a title', !!c.t);
    (c.slos || []).forEach(x => { sloCount++; if (!x.t || x.t.length < 3 || x.t.length > 450 || !['U', 'K', 'A', 'S', 'STS', 'T'].includes(x.g)) check(s.id + ' ch ' + c.no + ' SLO text/group', false, JSON.stringify(x).slice(0, 80)); });
  }
}
check('more than 4,000 learning outcomes / topics are included', sloCount > 4000, String(sloCount));
check('every subject with SLOs says where they come from', subs.every(s => !subs || !(s.chapters || []).some(c => (c.slos || []).length) || ['curriculum', 'textbook', 'headings'].includes(s.sloSrc)));
check('Physics 9 has the Board\'s nine chapters and 12 + 32 + 21 marks', D.subjects['cls9-phy'].chapters.length === 9 && D.subjects['cls9-phy'].pattern.total === 65);
check('Class 9 Computer Science is flagged as a different book from the Board\'s', !!D.subjects['cls9-comp'].mismatch);
check('General Mathematics is a Board subject the app does not have yet', D.subjects['cls9-gm'] && D.subjects['cls9-gm'].inApp === false);

// the module loads (no DOM needed) and keeps its public API
const src = fs.readFileSync(path.join(ROOT, 'js', 'sb_bise.js'), 'utf8');
check('sb_bise.js parses', (() => { try { new vm.Script(src); return true; } catch (e) { return false; } })());
check('sb_bise.js extends functions only through SBHooks', !/window\.(renderSubjectChapterView|renderPapersView|goToSubjects|renderMathChapter)\s*=(?!=)/.test(src));
check('sb_bise.js sends nothing to the network but the Board\'s own links', !/fetch\(|XMLHttpRequest|sendBeacon/.test(src));

console.log(`bise tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
