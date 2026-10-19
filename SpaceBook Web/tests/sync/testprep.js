'use strict';
/* Integration: the real js/test_prep.js (app sandbox, real MCQ bank) + js/core/* against the real PHP API.
 *   node tests/sync/testprep.js */
const harness = require('./harness');

const storageOf = t => { const o = {}, ls = t.sb.localStorage; for (let i = 0; i < ls.length; i++) { const k = ls.key(i); o[k] = ls.getItem(k); } return o; };
const recOf = (t, uid) => JSON.parse(t.sb.localStorage.getItem('sbTP:v1:' + uid) || 'null');
const tupleSum = rec => Object.values(rec.q).reduce((n, v) => n + v[0], 0);

(async () => {
  const h = await harness.start();
  const { check, sleep } = h;
  console.log('--- test_prep.js with sync v2 ---');

  // practise `n` questions of track 'pst' through the real module (open -> start -> answer -> next -> finish)
  async function practise(t, n, finish) {
    await t.sb.SBTestPrep.open('pst'); await sleep(250);
    t.sb.SBTestPrep.startPractice();
    for (let i = 0; i < n; i++) { t.sb.SBTestPrep.answer(0); if (i < n - 1) t.sb.SBTestPrep.next(); }
    if (finish) t.sb.SBTestPrep.finish();
  }
  const types = async t => (await t.sb.SBSync.pendingEvents()).map(e => e.type).sort().join(',');

  // 1. practice offline, then sync; a second device sees the same statistics
  {
    const a = await h.account(); const uid = a.user.id;
    const A = h.newApp({ flag: true, bank: true, me: a.user }); await A.signIn(a);
    A.offline();
    await practise(A, 3, true);
    const ev = await types(A);
    check('offline practice: 3 answers + the finished session + run changes wait in the outbox, student stays signed in', /(tp\.answer,){2}tp\.answer/.test(ev) && ev.includes('tp.session') && (await A.sb.SBSync.status()).signedIn, ev);
    check('the page shows the new numbers at once (3 attempts, 1 session)', tupleSum(recOf(A, uid)) === 3 && recOf(A, uid).sessions.length === 1, recOf(A, uid));
    A.online(); await A.sb.SBSync.sync(); await sleep(200);
    check('after the sync nothing waits any more', (await A.sb.SBSync.pending()) === 0);
    const B = h.newApp({ flag: true, bank: true, me: a.user }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBTestPrep.open('pst'); await sleep(900);
    const rb = recOf(B, uid);
    check('a second device sees the same attempts, the session and the daily numbers', rb && tupleSum(rb) === 3 && rb.sessions.length === 1 && rb.days.pst && rb.days.all && Object.values(rb.days.all)[0][1] === 3, rb && { att: tupleSum(rb), s: rb.sessions.length, d: rb.days });
  }

  // 2. two devices answer the same MCQ: both count
  {
    const a = await h.account(); const uid = a.user.id;
    const A = h.newApp({ flag: true, bank: true, me: a.user }); await A.signIn(a);
    await practise(A, 2, true);
    await A.sb.SBSync.sync(); await sleep(150);
    const ra = recOf(A, uid), id = Object.keys(ra.q)[0];
    const dev2 = await h.secondDevice(a);
    const B = h.newApp({ flag: true, bank: true, me: a.user }); await B.signIn(a, dev2);
    await B.sb.SBSync.emit('tp.answer', { mcqId: id, track: 'pst', day: '2026-10-20', correct: true, ms: 1000, ts: Date.now() });
    await B.sb.SBSync.sync(); await sleep(150);
    await A.sb.SBSync.sync(); await sleep(150);
    check("the other device's answer to the same MCQ adds to it on this device (attempts 1 -> 2)", recOf(A, uid).q[id][0] === ra.q[id][0] + 1, [ra.q[id], recOf(A, uid).q[id]]);
  }

  // 3. practice as a guest, then sign in: the guest record joins the account once
  {
    const a = await h.account(); const uid = a.user.id;
    const G = h.newApp({ flag: true, bank: true });
    await practise(G, 2, true);                                             // nobody signed in
    check('as a guest the record is kept on this device only (nothing queued)', !!G.sb.localStorage.getItem('sbTP:v1:guest') && (await G.sb.SBSync.pendingGuest()) === 0);
    const A = h.newApp({ flag: true, bank: true, storage: storageOf(G), me: a.user });   // the student signs in: a page that holds the session
    await A.signIn(a);
    await A.sb.SBTestPrep.open('pst'); await sleep(900);
    check('at sign-in the guest copy is removed and the numbers are the same (2 attempts, 1 session)', !A.sb.localStorage.getItem('sbTP:v1:guest') && tupleSum(recOf(A, uid)) === 2 && recOf(A, uid).sessions.length === 1, recOf(A, uid));
    await A.sb.SBSync.sync(); await sleep(150);
    const B = h.newApp({ flag: true, bank: true, me: a.user }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBTestPrep.open('pst'); await sleep(900);
    check('the account holds the guest practice (seen from a fresh page)', recOf(B, uid) && tupleSum(recOf(B, uid)) === 2 && recOf(B, uid).sessions.length === 1);
    const a2 = await h.account();
    const A2 = h.newApp({ flag: true, bank: true, storage: storageOf(A), me: a2.user });  // same browser, a different student
    await A2.signIn(a2); await A2.sb.SBTestPrep.open('pst'); await sleep(900);
    check("another student on the same browser does not receive the first student's practice", !recOf(A2, a2.user.id) || tupleSum(recOf(A2, a2.user.id)) === 0, recOf(A2, a2.user.id));
  }

  // 4. the record the old version kept on this device is imported once
  {
    const a = await h.account(); const uid = a.user.id;
    const old = { v: 1, q: { oldq1: [5, 3, 1000, 1, 9000], oldq2: [1, 0, 2000, 0, 500] }, sessions: [{ id: 'oldsess1', track: 'pst', mode: 'practice', ts: 1700000000000, n: 6, c: 3, ms: 9500, items: [], secs: {}, lv: {} }], days: { pst: { '2026-10-01': [60000, 6, 3] } }, run: null, runClearedAt: 0, updatedAt: 5, pushed: [] };
    const A = h.newApp({ flag: true, bank: true, storage: { ['sbTP:v1:' + uid]: JSON.stringify(old) }, me: a.user }); await A.signIn(a);
    await A.sb.SBTestPrep.open('pst'); await sleep(900);
    await A.sb.SBSync.sync(); await sleep(150);
    const B = h.newApp({ flag: true, bank: true, me: a.user }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBTestPrep.open('pst'); await sleep(900);
    const rb = recOf(B, uid);
    check('numbers made before the update reach the account and a second device (oldq1 5 attempts, the old session, the day)', rb && rb.q.oldq1 && rb.q.oldq1[0] === 5 && rb.sessions.some(s => s.id === 'oldsess1') && rb.days.pst['2026-10-01'][1] === 6, rb);
  }

  // 5. the unfinished test follows the student to another device and disappears when it is finished
  {
    const a = await h.account(); const uid = a.user.id;
    const A = h.newApp({ flag: true, bank: true, me: a.user }); await A.signIn(a);
    await practise(A, 2, false);                                            // stopped half way: the run is saved
    await A.sb.SBSync.sync(); await sleep(150);
    check('the unfinished test waits for the student in the account (one run event, not one per answer)', !!recOf(A, uid).run);
    const B = h.newApp({ flag: true, bank: true, me: a.user }); await B.signIn(a, await h.secondDevice(a)); await B.sb.SBTestPrep.open('pst'); await sleep(900);
    check('another device offers to continue it', recOf(B, uid) && recOf(B, uid).run && recOf(B, uid).run.id === recOf(A, uid).run.id, recOf(B, uid) && recOf(B, uid).run);
    A.sb.SBTestPrep.finish(); await A.sb.SBSync.sync(); await sleep(150);
    await B.sb.SBSync.sync(); await sleep(200);
    check('after it is finished on the first device the second no longer offers it', recOf(B, uid).run === null, recOf(B, uid).run && recOf(B, uid).run.id);
  }

  // 6. the outbox does not fill with copies of the unfinished test
  {
    const a = await h.account();
    const A = h.newApp({ flag: true, bank: true, me: a.user }); await A.signIn(a); A.offline();
    await practise(A, 5, false); await sleep(200);
    const ev = (await A.sb.SBSync.pendingEvents()).map(e => e.type);
    check('5 answers leave 5 answer events but a single run event', ev.filter(t => t === 'tp.answer').length === 5 && ev.filter(t => t === 'tp.run').length === 1, ev);
  }

  // 7. flag off: the old behaviour
  {
    const a = await h.account();
    const A = h.newApp({ flag: false, bank: true, me: a.user }); await A.signIn(a);
    await practise(A, 2, true); await sleep(100);
    check('flag off: nothing goes to the outbox and no v2 request is made', (await A.sb.SBSync.pending()) === 0 && !A.net.log.some(l => l.url.includes('v2/sync.php')), A.net.log.map(l => l.url));
  }

  h.finish('test prep integration tests');
})().catch(e => { console.error(e); process.exit(2); });
