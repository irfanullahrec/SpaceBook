'use strict';
/* js/core/offline_queue.js: what a signed-in student does with no connection is kept and sent later, in order, and never under another student.
 *     node tests/sync/offline_queue.js */
const { create } = require('../../js/core/offline_queue.js');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail) : '')); } };

function world() {
  const mem = {}; const storage = { getItem: k => (k in mem ? mem[k] : null), setItem: (k, v) => { mem[k] = String(v); } };
  const w = { online: true, status: 200, user: '7', calls: [], clock: 1000 };
  const fetchFn = async (url, o) => {
    if (!w.online) throw new TypeError('Failed to fetch');
    w.calls.push({ url, body: JSON.parse(o.body) });
    return { status: w.status, json: async () => (w.status >= 400 && w.status < 500 ? { ok: false, error: 'rejected' } : { ok: true, n: w.calls.length }) };
  };
  w.q = create({ storage, fetch: fetchFn, user: () => w.user, now: () => ++w.clock });
  return w;
}

(async () => {
  let w = world();
  let r = await w.q.send('api/progress.php?action=step', { key: 'a', step: 0 });
  check('online: the server answers and nothing is queued', r.ok === true && w.q.pending() === 0);

  w = world(); w.online = false;
  r = await w.q.send('api/progress.php?action=step', { key: 'a', step: 1 });
  check('offline: the call is kept and answered {queued}', r.ok === false && r.queued === true && w.q.pending() === 1, r);
  await w.q.send('api/progress.php?action=step', { key: 'a', step: 2 });
  let f = await w.q.flush();
  check('still offline: a flush sends nothing and keeps everything', f.sent === 0 && f.left === 2 && w.q.pending() === 2, f);
  w.online = true;
  f = await w.q.flush();
  check('back online: everything is sent, oldest first', f.sent === 2 && f.left === 0 && w.calls.map(c => c.body.step).join() === '1,2', { f, order: w.calls.map(c => c.body.step) });

  w = world(); w.online = false;
  await w.q.send('api/study_plans.php?action=save', { plan: { id: 'p1', v: 1 } }, { dedupe: 'plan:p1' });
  await w.q.send('api/study_plans.php?action=save', { plan: { id: 'p1', v: 2 } }, { dedupe: 'plan:p1' });
  await w.q.send('api/study_plans.php?action=save', { plan: { id: 'p2', v: 1 } }, { dedupe: 'plan:p2' });
  check('a plan saved twice offline waits once (the newest)', w.q.pending() === 2 && w.q._load().find(x => x.dedupe === 'plan:p1').body.plan.v === 2);

  w = world(); w.online = false;
  await w.q.send('u', { a: 1 }); w.user = '8'; await w.q.send('u', { a: 2 });
  w.online = true; w.user = '8'; f = await w.q.flush();
  check('student 8 sends only their own work; student 7\'s waits', f.sent === 1 && w.calls[0].body.a === 2 && w.q._load().length === 1 && w.q._load()[0].uid === '7', { f, calls: w.calls });
  w.user = '7'; f = await w.q.flush();
  check('and it goes out when student 7 is back', f.sent === 1 && w.calls[1].body.a === 1 && w.q._load().length === 0);

  w = world(); w.online = false; w.user = '';
  r = await w.q.send('u', { a: 1 });
  check('nobody signed in: nothing is kept for an account that does not exist', r.ok === false && !r.queued && w.q._load().length === 0);

  w = world(); w.online = false; await w.q.send('u', { a: 1 }); w.online = true; w.status = 503;
  f = await w.q.flush();
  check('a busy server (503) keeps the call for later', f.sent === 0 && f.left === 1);
  w.status = 429; f = await w.q.flush();
  check('too many requests (429) keeps it too', f.sent === 0 && f.left === 1);
  w.status = 422; f = await w.q.flush();
  check('a refusal (422) is the server\'s decision: the call leaves the queue', f.sent === 1 && f.left === 0);

  w = world(); w.status = 500; r = await w.q.send('u', { a: 1 });
  check('a 500 answer on the first try is queued, not lost', r.queued === true && w.q.pending() === 1);

  w = world(); w.online = false; for (let i = 0; i < 450; i++) await w.q.send('u', { i });
  check('the queue is bounded (400), newest kept', w.q._load().length === 400 && w.q._load()[399].body.i === 449);

  console.log(`\n${pass} passed, ${fail} failed.`);
  process.exit(fail ? 1 : 0);
})();
