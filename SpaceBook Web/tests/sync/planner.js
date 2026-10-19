'use strict';
/* Integration: the real js/sb_study_plan.js (app sandbox) + js/core/* against the real PHP API.   node tests/sync/planner.js */
const harness = require('./harness');

const mkPlan = (id, name, tasks) => ({ id, name, classId: 'cls9', scope: {}, cats: [], start: '2026-10-20', end: '2026-10-25', weekdays: [1, 2, 3], skip: [], extra: [], alt: false,
  slots: [{ from: '16:00', to: '17:00' }], revision: false, createdAt: 1, updatedAt: 1, sessions: [{ id: 's1', date: '2026-10-21', slot: 0, from: '16:00', to: '17:00', len: 60, tasks }] });
const task = (id, n, done) => ({ id, cat: 'rd', n, done, a: 1, b: n, s: 'x', ch: 0 });
const storageOf = t => { const o = {}, ls = t.sb.localStorage; for (let i = 0; i < ls.length; i++) { const k = ls.key(i); o[k] = ls.getItem(k); } return o; };
const planOf = (t, pid) => t.sb.SBStudyPlan.plans().find(x => x.id === pid);
const doneOf = (t, pid, tid) => { const p = planOf(t, pid); return p ? p.sessions[0].tasks.find(x => x.id === tid).done : null; };

(async () => {
  const h = await harness.start();
  const { check, sleep } = h;
  console.log('--- sb_study_plan.js with sync v2 ---');

  // 1. a plan made and ticked offline reaches the account and a second device
  {
    const a = await h.account();
    const A = h.newApp({ flag: true }); await A.signIn(a);
    A.offline();
    const p = mkPlan('plan_it01', 'Offline plan', [task('t1', 3, 0)]);
    A.sb.SBStudyPlan.add(p);
    p.sessions[0].tasks[0].done = 2; A.sb.SBStudyPlan.persist(p);
    await sleep(50);
    check('offline: the plan and the tick wait in the outbox (2 events) and the student stays signed in', (await A.sb.SBSync.pending()) === 2 && (await A.sb.SBSync.status()).signedIn && A.sb.SBStudyPlan.plans().length === 1);
    A.online();
    await A.sb.SBSync.sync(); await sleep(100);
    check('back online the events are delivered', (await A.sb.SBSync.pending()) === 0);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBSync.sync(); await sleep(200);
    check('a second device receives the plan with the tick (done 2) and its revision', doneOf(B, 'plan_it01', 't1') === 2 && planOf(B, 'plan_it01').rev >= 1, B.sb.SBStudyPlan.plans());
  }

  // 2. un-ticking on the same device sticks
  {
    const a = await h.account(); const A = h.newApp({ flag: true }); await A.signIn(a);
    const p = mkPlan('plan_it02', 'Untick', [task('t1', 3, 0)]); A.sb.SBStudyPlan.add(p);
    p.sessions[0].tasks[0].done = 3; A.sb.SBStudyPlan.persist(p);
    p.sessions[0].tasks[0].done = 1; A.sb.SBStudyPlan.persist(p);            // un-tick before anything was confirmed
    await A.sb.SBSync.sync(); await sleep(100);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBSync.sync(); await sleep(200);
    check('a task un-ticked before the sync is un-ticked everywhere (done 1, not 3)', doneOf(B, 'plan_it02', 't1') === 1, doneOf(B, 'plan_it02', 't1'));
  }

  // 3. two devices edit while offline; both end with the same plan
  {
    const a = await h.account(); const A = h.newApp({ flag: true }); await A.signIn(a);
    A.sb.SBStudyPlan.add(mkPlan('plan_it03', 'Shared', [task('t1', 3, 0), task('t2', 2, 0)]));
    await A.sb.SBSync.sync(); await sleep(100);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBSync.sync(); await sleep(200);
    A.offline(); B.offline();
    const pa = planOf(A, 'plan_it03'); pa.sessions[0].tasks[0].done = 3; A.sb.SBStudyPlan.persist(pa);
    const pb = planOf(B, 'plan_it03'); pb.name = 'Renamed on B'; pb.sessions[0].tasks[0].done = 1; B.sb.SBStudyPlan.persist(pb);
    A.online(); B.online();
    await A.sb.SBSync.sync(); await B.sb.SBSync.sync(); await sleep(150); await A.sb.SBSync.sync(); await sleep(150);
    check("both devices converge: B's name, A's ticked work kept (done 3)", planOf(A, 'plan_it03').name === 'Renamed on B' && planOf(B, 'plan_it03').name === 'Renamed on B' && doneOf(A, 'plan_it03', 't1') === 3 && doneOf(B, 'plan_it03', 't1') === 3,
      [planOf(A, 'plan_it03').name, planOf(B, 'plan_it03').name, doneOf(A, 'plan_it03', 't1'), doneOf(B, 'plan_it03', 't1')]);
  }

  // 4. deleting offline: no resurrection, and the other device sees the deletion once synced
  {
    const a = await h.account(); const A = h.newApp({ flag: true }); await A.signIn(a);
    A.sb.SBStudyPlan.add(mkPlan('plan_it04', 'To delete', [task('t1', 2, 0)]));
    await A.sb.SBSync.sync(); await sleep(100);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBSync.sync(); await sleep(200);
    A.offline();
    A.sb.SBStudyPlan.removePlan(planOf(A, 'plan_it04'));
    await sleep(50);
    check('offline delete: gone locally, the deletion is queued', A.sb.SBStudyPlan.plans().length === 0 && (await A.sb.SBSync.pending()) === 1);
    A.online(); await A.sb.SBSync.pull(); await sleep(150);                       // a pull while the deletion is still waiting
    check('a pull while the deletion is waiting does not bring the plan back', A.sb.SBStudyPlan.plans().length === 0);
    await A.sb.SBSync.sync(); await sleep(150);
    await B.sb.SBSync.sync(); await sleep(150);
    check('after the sync the other device has dropped it too', B.sb.SBStudyPlan.plans().length === 0 && A.sb.SBStudyPlan.plans().length === 0);
  }

  // 5. plans made as a guest join the account at sign-in; nothing is queued while signed out
  {
    const a = await h.account(); const A = h.newApp({ flag: true });
    A.sb.SBStudyPlan.add(mkPlan('plan_it05', 'Guest plan', [task('t1', 2, 1)]));
    check('signed out: the plan is kept on this device and nothing is queued', (await A.sb.SBSync.pendingGuest()) === 0 && A.sb.SBStudyPlan.plans().length === 1);
    await A.signIn(a); await A.sb.SBSync.sync(); await sleep(150);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBSync.sync(); await sleep(200);
    check('at sign-in the plan joins the account (a second device sees it with its tick)', doneOf(B, 'plan_it05', 't1') === 1);
  }

  // 6. reload with waiting events: nothing lost
  {
    const a = await h.account(); const A = h.newApp({ flag: true }); await A.signIn(a); A.offline();
    const p = mkPlan('plan_it06', 'Reload', [task('t1', 2, 0)]); A.sb.SBStudyPlan.add(p); p.sessions[0].tasks[0].done = 1; A.sb.SBStudyPlan.persist(p);
    const B = h.newApp({ flag: true, storage: storageOf(A), me: a.user });      // the page is reloaded: same storage, the session cookie still valid
    await sleep(900);
    check('after a reload the plan and its waiting events are still there and are delivered', B.sb.SBStudyPlan.plans().length === 1 && (await B.sb.SBSync.pending()) === 0, await B.sb.SBSync.status());
    const C = h.newApp({ flag: true }); await C.signIn(a, await h.secondDevice(a)); await C.sb.SBSync.sync(); await sleep(200);
    check('and the account holds the ticked plan', doneOf(C, 'plan_it06', 't1') === 1);
  }

  // 7. flag off: the old v1 behaviour
  {
    const a = await h.account(); const A = h.newApp({ flag: false }); await A.signIn(a);
    A.sb.SBStudyPlan.add(mkPlan('plan_it07', 'Legacy', [task('t1', 2, 0)])); await sleep(200);
    check('flag off: plans are saved through api/study_plans.php (v1) and never through v2', A.net.log.some(l => l.url.includes('study_plans.php')) && !A.net.log.some(l => l.url.includes('v2/sync.php')), A.net.log.map(l => l.url));
  }

  h.finish('planner integration tests');
})().catch(e => { console.error(e); process.exit(2); });
