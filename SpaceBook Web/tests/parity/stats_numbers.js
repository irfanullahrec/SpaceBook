'use strict';
/* The same numbers for the same student: what the app's native Home shows (assets/prep_summary.js reads the browser storage of the page)
 * against what the website's own code computes from the same stored records.
 *     node --max-old-space-size=6144 tests/parity/stats_numbers.js [--app "<folder of the app repo>"]
 * Words and the minutes per kind of work are always compared. The website's Home functions (SBTestPrep.summary, SBStudyPlan.stats) are compared
 * when they are in this build; if they are not, the lines say SKIP. Without the app folder the test says so and compares nothing. Dev-only. */
const fs = require('fs'), path = require('path');
const { JSDOM } = require('jsdom');
const { load } = require('../../tools/lib/app_sandbox');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const SUMMARY = path.join(APP, 'app', 'src', 'main', 'assets', 'prep_summary.js');
if (!fs.existsSync(SUMMARY)) { console.log('SKIP  the app folder is not here (' + SUMMARY + ')'); process.exit(0); }

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 500) : '')); } };
const skip = l => console.log('SKIP  ' + l);

const DAY = 86400000, now = Date.now();
const pad = n => String(n).padStart(2, '0');
const ymd = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
const dayKey = back => ymd(new Date(now - back * DAY));

// the student's records, as the website writes them
const words = { v: 1, words: {
  'en:cell': { s: 'l', t: now - 3600e3 }, 'en:atom': { s: 'l', t: now - 3 * DAY }, 'en:force': { s: 'l', t: now - 20 * DAY }, 'en:mass': { s: 'k', t: now - 1 * DAY },
  'ur:کتاب': { s: 'l', t: now - 100 }, 'ps:کور': { s: 'k', t: now - 5 * DAY }, 'ar:علم': { s: 'l', t: now - 2 * DAY },
} };
const tp = { v: 1, q: {}, resets: {}, rid: {}, updatedAt: now, run: { id: 'r1', track: 'ct', mode: 'practice', ids: [], answers: [], i: 0, savedAt: now - 5000 }, runClearedAt: 0,
  sessions: [
    { id: 's1', track: 'pst', mode: 'practice', n: 10, c: 7, ms: 600000, ts: now - 2 * DAY },
    { id: 's2', track: 'pst', mode: 'mock', n: 20, c: 15, ms: 1200000, ts: now - 1 * DAY },
    { id: 's3', track: 'sst-bio', mode: 'mock', n: 10, c: 4, ms: 300000, ts: now - 3600e3 },
  ],
  days: { pst: { [dayKey(2)]: [600000, 10, 7], [dayKey(1)]: [1200000, 20, 15] }, 'sst-bio': { [dayKey(0)]: [300000, 10, 4] }, ct: { [dayKey(0)]: [60000, 3, 2] },
    all: { [dayKey(2)]: [600000, 10, 7], [dayKey(1)]: [1200000, 20, 15], [dayKey(0)]: [360000, 13, 6] } } };
const task = (id, cat, n, done, ch, learn) => Object.assign({ id, cat, s: 'cls5-math', ch: ch || 0, n, done, a: 1, b: n }, learn ? { learn } : {});
const LEARN = { at: now - 2 * DAY, mode: 'check', rounds: 2, asked: 6, first: 4, fixed: 2, wrong: 2, auto: 6, self: 0, missed: [], secs: 90 };
const plan = { id: 'plan_stat1', name: 'Numbers plan', classId: 'cls5', scope: [{ subj: 'cls5-math', ch: [0, 1] }], cats: ['read', 'mcq'], start: dayKey(3), end: ymd(new Date(now + 5 * DAY)), weekdays: [0, 1, 2, 3, 4, 5, 6], skip: [], extra: [], alt: false,
  slots: [{ from: '16:00', to: '17:00' }], revision: false, createdAt: 1, updatedAt: now - 1000,
  sessions: [
    { id: 'a', date: dayKey(2), slot: 0, from: '16:00', to: '17:00', len: 60, tasks: [task('t1', 'read', 4, 4, 0, LEARN), task('t2', 'mcq', 10, 6, 0, LEARN)] },       // t1 passed the check; t2 keeps a record but is not done (un-ticked): it does not count
    { id: 'b', date: dayKey(1), slot: 0, from: '16:00', to: '17:00', len: 60, tasks: [task('t3', 'read', 3, 3, 1, { at: now - DAY, mode: 'self' }), task('t4', 'sq', 5, 0, 1)] },
    { id: 'c', date: ymd(new Date(now + DAY)), slot: 0, from: '16:00', to: '17:00', len: 60, tasks: [task('t5', 'lq', 2, 0, 1)] },
  ] };

const app = load({ quiet: true, before(sb) {
  sb.localStorage.setItem('sbWS:progress:guest', JSON.stringify(words));
  sb.localStorage.setItem('sbTP:v1:guest', JSON.stringify(tp));
  sb.localStorage.setItem('sb_study_plans_v1', JSON.stringify([plan]));
} });
const sb = app.sb;

// the app's side: its script in a page that holds the same storage
const dom = new JSDOM('<!doctype html><body></body>', { runScripts: 'outside-only', url: 'http://localhost/' });
dom.window.localStorage.setItem('sbWS:progress:guest', JSON.stringify(words));
dom.window.localStorage.setItem('sbTP:v1:guest', JSON.stringify(tp));
dom.window.localStorage.setItem('sb_study_plans_v1', JSON.stringify([plan]));
dom.window.eval(fs.readFileSync(SUMMARY, 'utf8'));
const meta = [{ id: 'pst', title: 'PST' }, { id: 'sst-bio', title: 'SST Bio/Chem' }, { id: 'ct', title: 'CT' }];
const appSum = JSON.parse(dom.window.SBPrepSummary(['guest'], meta, now));
const appTests = appSum.tests.tests;

console.log('--- words ---');
const w = sb.SBWordStats.progressSummary();
check('learnt, already knew, today, this week and the total are the same', w.learnt === appSum.words.learnt && w.knew === appSum.words.knew && w.today === appSum.words.today && w.week === appSum.words.week && w.total === appSum.words.total,
  { web: [w.learnt, w.knew, w.today, w.week, w.total], app: [appSum.words.learnt, appSum.words.knew, appSum.words.today, appSum.words.week, appSum.words.total] });
check('and per language', ['en', 'ur', 'ps', 'ar'].every(l => w.byLang[l].learnt === appSum.words.byLang[l].learnt && w.byLang[l].knew === appSum.words.byLang[l].knew), { web: w.byLang, app: appSum.words.byLang });

console.log('--- minutes per kind of work (the app copies them) ---');
const planSrc = fs.readFileSync(path.join(ROOT, 'js', 'sb_study_plan.js'), 'utf8');
const webMin = {};
for (const m of planSrc.slice(planSrc.indexOf('const CATS = ['), planSrc.indexOf('const CAT = ')).matchAll(/\['([a-z]+)', '[^']*', '[^']*', ([0-9.]+), /g)) webMin[m[1]] = +m[2];
const appSrc = fs.readFileSync(SUMMARY, 'utf8');
const appMin = {};
for (const m of /var CAT_MIN = \{([^}]*)\}/.exec(appSrc)[1].matchAll(/([a-z]+): ([0-9.]+)/g)) appMin[m[1]] = +m[2];
check('prep_summary.js CAT_MIN is CATS of js/sb_study_plan.js', JSON.stringify(webMin) === JSON.stringify(appMin), { web: webMin, app: appMin });

console.log('--- study plans ---');
const P = sb.SBStudyPlan;
if (typeof P.stats !== 'function') skip('this build of the website has no SBStudyPlan.stats (the Home twin is not committed): plan percentages were not compared');
else {
  const ws = P.stats(P.plans().find(p => p.id === 'plan_stat1'));
  const ap = appSum.plans.find(p => p.id === 'plan_stat1');
  check(`the plan percentage is the same (${ws.pct} %)`, !!ap && ap.pct === ws.pct, { web: ws.pct, app: ap && ap.pct });
  check('and the count of items done in each kind of work', !!ap && Object.keys(ws.byCat).every(k => ap.byCat[k] && ap.byCat[k].n === ws.byCat[k].n && ap.byCat[k].done === ws.byCat[k].done), { web: ws.byCat, app: ap && ap.byCat });
  if (ws.tasks === undefined) skip('this build of the website has no learnt-and-checked count in SBStudyPlan.stats');
  else check(`the tasks learnt by passing the check, and those ticked by hand, are the same (${ws.checked} of ${ws.tasks}, ${ws.selfMarked})`, !!ap && ap.tasks === ws.tasks && ap.checked === ws.checked && ap.selfMarked === ws.selfMarked && ws.checked === 1 && ws.selfMarked === 1,
    { web: [ws.tasks, ws.checked, ws.selfMarked], app: ap && [ap.tasks, ap.checked, ap.selfMarked] });
}

console.log('--- Tests Preps ---');
const T = sb.SBTestPrep;
if (!T || typeof T.summary !== 'function') skip('this build of the website has no SBTestPrep.summary (the Home twin is not committed): test numbers were not compared');
else {
  const web = T.summary();
  const bad = [];
  web.forEach(t => {
    const a = appTests.find(x => x.id === t.track);
    if (!a) { bad.push(t.track + ': missing in the app'); return; }
    const pairs = [['mcqs', 'questions'], ['correct', 'correct'], ['sessions', 'sessions'], ['mocks', 'mock'], ['minutes', 'minutes']];
    pairs.forEach(([wk, ak]) => { if (t[wk] !== a[ak]) bad.push(`${t.track}.${wk}: web ${t[wk]}, app ${a[ak]}`); });
    if (t.bestMock !== Math.max(0, a.bestMock)) bad.push(`${t.track}.bestMock: web ${t.bestMock}, app ${a.bestMock}`);
    if (t.paused !== a.running) bad.push(`${t.track}.paused/running`);
  });
  appTests.forEach(a => { if (!web.some(t => t.track === a.id)) bad.push(a.id + ': only in the app'); });
  check(`the ${web.length} tests the student started have the same questions, correct answers, sessions, mocks, minutes and best mock`, bad.length === 0, bad);
}

console.log(`---\nstats numbers: ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
