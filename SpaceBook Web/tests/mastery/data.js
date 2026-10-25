'use strict';
/* js/sb_mastery.js against the real data: every chapter of the Study Plan index, every kind of work, the real Create Test question files.
 *     node tests/mastery/data.js [--report]
 * Checks that what a check would ask is always valid (a key that exists, an answer for every written question, only this chapter's questions, no
 * question twice, never more than MAX_Q), that neighbouring tasks of a chapter never share a question, and counts how much of the plan can be checked. */
const fs = require('fs'), path = require('path');
const M = require('../../js/sb_mastery.js');
const ROOT = path.resolve(__dirname, '..', '..');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };

global.window = {};
new Function('window', fs.readFileSync(path.join(ROOT, 'js', 'study_plan_index.js'), 'utf8'))(global.window);
const IX = global.window.SB_STUDY_INDEX;
const CATS = ['read', 'slo', 'mcq', 'tf', 'blank', 'match', 'sq', 'lq', 'num', 'ex'];

const bad = [], overlaps = [], gaps = [], tooMany = [], wrongChapter = [];
const cover = {}, fb = {}, none = {};
let tasks = 0, chapters = 0, subjectsNoBank = [];
for (const C of IX.classes) {
  const n = +C.id.replace('cls', '');
  let shard; try { shard = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'testbank', 'cls' + n + '.json'), 'utf8')); } catch (e) { continue; }
  for (const S of C.subjects) {
    if (!shard.subjects[S.id]) { subjectsNoBank.push(S.id); continue; }
    S.chapters.forEach((chp, ch) => {
      chapters++;
      const counts = chp.c || {};
      for (const cat of CATS) {
        const total = counts[cat] || 0; if (!total) continue;
        // as the planner would cut it: tasks of about 5 items (3 lesson parts), numbered from 1
        const step = cat === 'read' ? 3 : 5, seen = new Set(), picks = [];
        for (let a = 1; a <= total; a += step) {
          const b = Math.min(total, a + step - 1);
          const r = M.pick(shard, counts, { s: S.id, ch, cat, a, b, n: b - a + 1 });
          tasks++; picks.push(r);
          const key = cat;
          cover[key] = cover[key] || { tasks: 0, withCheck: 0 }; cover[key].tasks++;
          if (r.items.length >= M.config.MIN_Q) cover[key].withCheck++; else none[key] = (none[key] || 0) + 1;
          if (r.items.length >= M.config.MIN_Q && r.fallback) fb[key] = (fb[key] || 0) + 1;
          if (r.items.length > M.config.MAX_Q) tooMany.push([S.id, ch, cat, r.items.length]);
          const ids = new Set();
          r.items.forEach(it => {
            if (!M.engine.usable(it)) bad.push([S.id, ch, cat, it.i]);
            if (it.s !== S.id || it.u !== ch) wrongChapter.push([S.id, ch, cat, it.i]);
            if (ids.has(it.id)) bad.push(['duplicate', S.id, ch, cat, it.i]); ids.add(it.id);
          });
        }
        if (cat !== 'read') {
          const kinds = M.config.KINDS[cat];
          const L = shard.items.filter(it => it.s === S.id && it.u === ch && M.engine.usable(it) && kinds.indexOf(it.y) >= 0);
          const all = picks.filter(r => !r.fallback).flatMap(r => r.items.map(it => it.id));
          // where the book holds at least as many questions of the kind as the plan counted, neighbouring tasks share none
          if (L.length >= total && new Set(all).size !== all.length) overlaps.push([S.id, ch, cat, all.length - new Set(all).size]);
          // and wherever it holds fewer, every question it does hold is asked by some task
          if (L.length && L.length <= M.config.MAX_Q * picks.length && !picks.some(r => r.fallback)) {
            const asked = new Set(all), left = L.filter(it => !asked.has(it.s + ':' + it.i));
            if (left.length && L.length <= total) gaps.push([S.id, ch, cat, left.length]);
          }
        }
      }
    });
  }
}
check('every question a check would ask is valid (key exists, written ones have the book\'s answer, no repeats)', bad.length === 0, bad.slice(0, 5));
check('a check only ever asks questions of its own chapter', wrongChapter.length === 0, wrongChapter.slice(0, 5));
check('no check is longer than ' + M.config.MAX_Q + ' questions', tooMany.length === 0, tooMany.slice(0, 5));
check('neighbouring tasks of one kind in a chapter share no question (where the book holds enough)', overlaps.length === 0, overlaps.slice(0, 8));
check('and no question of the book is left out when the plan counted at least as many', gaps.length === 0, gaps.slice(0, 8));
const pct = (a, b) => b ? Math.round(100 * a / b) : 0;
const allT = Object.values(cover).reduce((a, v) => a + v.tasks, 0), allC = Object.values(cover).reduce((a, v) => a + v.withCheck, 0);
check('most plan tasks in the covered subjects can be checked with the book\'s own questions (' + pct(allC, allT) + '%)', pct(allC, allT) >= 55, { tasks: allT, withCheck: allC });
check('lesson-part tasks, the main case, can be checked in most chapters (' + pct(cover.read.withCheck, cover.read.tasks) + '%)', pct(cover.read.withCheck, cover.read.tasks) >= 60, cover.read);
if (process.argv.includes('--report') || fail) {
  console.log('\ncoverage by kind of work (tasks that can be checked / all; of those how many ask about the chapter instead of the exact part):');
  CATS.forEach(c => { if (cover[c]) console.log('  ' + c.padEnd(6), String(cover[c].withCheck).padStart(5) + ' / ' + String(cover[c].tasks).padEnd(5), pct(cover[c].withCheck, cover[c].tasks) + '%', '  chapter-level: ' + (fb[c] || 0)); });
  console.log('subjects with no questions in the bank (their tasks are marked by the student): ' + subjectsNoBank.join(' '));
}
console.log('---\nmastery data: ' + pass + ' passed, ' + fail + ' failed  (' + chapters + ' chapters, ' + tasks + ' tasks tried)');
process.exit(fail ? 1 : 0);
