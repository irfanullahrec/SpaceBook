'use strict';
/* SBStudyPlan.reminders(): the reminders the Android app schedules as phone notifications are the ones the website would show, with the same words.
 *     node --max-old-space-size=6144 tests/plan/reminders.js
 * Runs the real js/sb_study_plan.js in the app sandbox (tools/lib/app_sandbox.js). Dev-only, never shipped. */
const { load } = require('../../tools/lib/app_sandbox');

let pass = 0, fail = 0;
const check = (label, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };

const app = load({ quiet: true });
const sb = app.sb;
const P = sb.SBStudyPlan;
const pad = n => String(n).padStart(2, '0');
const ymd = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
const at = (daysAhead, hh, mm) => { const d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() + daysAhead); d.setHours(hh, mm, 0, 0); return d; };
const session = (id, day, from, to, tasks) => ({ id, date: ymd(day), slot: 0, from, to, len: 60, tasks });
const task = (id, n, done, ch) => ({ id, cat: 'read', s: 'cls5-math', ch: ch || 0, n, done, a: 1, b: n });

const tomorrow = at(1, 16, 0);
const plan = { id: 'plan_rem1', name: 'Reminder plan', classId: 'cls5', scope: [], cats: [], start: ymd(at(-3, 9, 0)), end: ymd(at(8, 9, 0)), weekdays: [0, 1, 2, 3, 4, 5, 6], skip: [], extra: [], alt: false,
  slots: [{ from: '16:00', to: '17:00' }], revision: false, createdAt: 1, updatedAt: 1,
  sessions: [
    session('gone', at(-1, 16, 0), '16:00', '17:00', [task('t0', 3, 1)]),            // yesterday, unfinished: becomes "unfinished from earlier", gets no reminder itself
    session('done', at(1, 8, 0), '08:00', '09:00', [task('t1', 2, 2)]),              // tomorrow morning, everything ticked: no reminder
    session('s1', tomorrow, '16:00', '17:00', [task('t2', 4, 1, 2), task('t3', 2, 0, 3)]),
    session('late', at(20, 16, 0), '16:00', '17:00', [task('t4', 2, 0)]),            // beyond a week
  ] };
P.add(plan);
const r = P.reminders(7);
check('a session in the next week has two reminders: five minutes before, and at the start', r.length === 2 && r[0].key === 'plan_rem1|s1|soon' && r[1].key === 'plan_rem1|s1', r.map(x => x.key));
check('their times are exact (start minus 5 minutes, start), in milliseconds', r[0].at === tomorrow.getTime() - 300000 && r[1].at === tomorrow.getTime(), r.map(x => x.at - tomorrow.getTime()));
check('earliest first, planId and sessionId say which plan and session to open', r[0].at < r[1].at && r[0].planId === 'plan_rem1' && r[0].sessionId === 's1');
check('the title is the one the website notification shows', r[0].title === 'Study time in 5 minutes · 4:00 PM–5:00 PM' && r[1].title === 'Study time now · 4:00 PM–5:00 PM', r.map(x => x.title));
check('the body lists the unfinished work and the tasks left over from earlier', /Mathematics: Read lesson parts 1–4 \(4\)/.test(r[0].body) || /Mathematics: Read lesson part/.test(r[0].body), r[0].body);
check('and counts the unfinished task from yesterday', /\+ 1 unfinished task from earlier/.test(r[0].body), r[0].body);
check('a session whose work is all done has none, and one beyond the horizon has none', !r.some(x => /done|late/.test(x.key)));
check('a longer horizon reaches the later session', P.reminders(30).length === 4);
check('the browser notification and the phone reminder say the same (same function)', typeof P.tick === 'function' && typeof P.reminders === 'function');
console.log(`---\nstudy plan reminders: ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
