'use strict';
/* End-to-end: the real client core (js/core) against the real PHP API (api/v2/sync.php) on a scratch MySQL database.
 *   node tests/sync/e2e.js          needs PHP (env PHP, `php`, or C:/xampp/php/php.exe) and MySQL as for tests/php/run.php */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
const { IDBFactory } = require('fake-indexeddb');
const Store = require('../../js/core/store.js');
const Sync = require('../../js/core/sync.js');

const ROOT = path.resolve(__dirname, '..', '..');
const PHP = [process.env.PHP, 'php', 'C:/xampp/php/php.exe'].filter(Boolean).find(p => spawnSync(p, ['-v']).status === 0);
if (!PHP) { console.log('SKIP  no PHP found'); process.exit(0); }
let pass = 0, fail = 0;
const check = (label, cond, detail) => { if (cond) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

const cfg = path.join(os.tmpdir(), 'sb_e2e_config_' + process.pid + '.php');
const mk = spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'create', cfg], { encoding: 'utf8' });
if (mk.status !== 0) { console.log('FAIL  cannot create the scratch database: ' + (mk.stderr || mk.stdout)); process.exit(1); }
const port = 19100 + (process.pid % 700);
const base = 'http://127.0.0.1:' + port + '/';
const server = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', path.join(ROOT, 'api')], { env: Object.assign({}, process.env, { SB_CONFIG: cfg }), stdio: 'ignore' });

// a fake clock so retries never fire on their own; tests call flush()/pull() themselves
function clock() { let t = Date.now(); return { now: () => t, advance: ms => { t += ms; }, timers: { setTimeout: () => 0, clearTimeout: () => {}, setInterval: () => 0 } }; }

function client(opts) {
  opts = opts || {};
  const store = Store.create({ indexedDB: opts.idb || new IDBFactory() });
  const clk = opts.clock || clock();
  let online = true, lose = 0, lost = 0;
  const log = [];
  const fetch2 = async (url, o) => {
    if (opts.token) { /* the token is added by SBSync from setDevice */ }
    const res = await fetch(url, o);
    log.push({ url, method: o.method, status: res.status, events: o.body ? JSON.parse(o.body).events.map(e => e.eventId) : null });
    if (lose > 0 && o.method === 'POST') { lose--; lost++; await res.text(); throw new Error('response lost'); }   // the server did the work, the answer never arrived
    return res;
  };
  const sync = Sync.create({ store, enabled: () => true, endpoint: base + 'v2/sync.php', fetch: fetch2, now: clk.now, timers: clk.timers, random: () => 0.5, isOnline: () => online });
  return { sync, store, clk, log, setOnline: v => { online = v; }, loseNextResponses: n => { lose = n; }, get lost() { return lost; } };
}
async function api(pathAndQuery, body, headers) {
  const res = await fetch(base + pathAndQuery, { method: body === undefined ? 'GET' : 'POST', headers: Object.assign({ 'Content-Type': 'application/json' }, headers || {}), body: body === undefined ? undefined : JSON.stringify(body) });
  return { status: res.status, json: await res.json().catch(() => null) };
}
let n = 0;
async function account() {
  n++;
  const r = await api('auth.php?action=register', { name: 'E2E User', father_name: 'Father', user_type: 'student', whatsapp: '92300' + String(3000000 + n * 7 + process.pid % 5), password: 'secret123', want_device: true, device_name: 'node' });
  if (!r.json || !r.json.ok) throw new Error('register failed: ' + JSON.stringify(r));
  return { user: r.json.user, device: r.json.device, whatsapp: r.json.user.whatsapp };
}
async function secondDevice(acct) {
  const r = await api('auth.php?action=login', { whatsapp: acct.whatsapp, password: 'secret123', want_device: true, device_name: 'second' });
  return r.json.device;
}
const key = s => 'cls2|math|u0|trace|' + s + '|0';
const plan = (id, name, tasks) => ({ id, name, updatedAt: 1, sessions: [{ id: 's1', date: '2026-10-20', tasks }] });
const sign = async (c, acct, dev) => { await c.sync.setUser({ id: acct.user.id }); await c.sync.setDevice(acct.user.id, dev || acct.device); };

(async () => {
  for (let i = 0; i < 60; i++) { try { await fetch(base + 'health.php'); break; } catch (e) { await sleep(100); } }

  // ---- 1. the plain path
  console.log('--- e2e ---');
  {
    const a = await account(); const c = client(); await sign(c, a);
    for (let i = 0; i < 3; i++) await c.sync.emit('step', { key: key('e1'), title: 'T', total: 3, step: i });
    const r = await c.sync.sync();
    const snap = await c.sync.snapshot();
    check('events written locally are delivered and the pulled snapshot has them (8 coins)', r.flush.accepted === 3 && snap.coins === 8 && snap.progress[key('e1')].done.length === 3, { r, snap: snap.coins });
    check('the outbox is empty afterwards', (await c.sync.pending()) === 0);
  }

  // ---- 2. the answer is lost: the client resends the SAME events, the server applies them once
  {
    const a = await account(); const c = client(); await sign(c, a);
    await c.sync.emit('step', { key: key('lost'), title: 'T', total: 2, step: 0 });
    await c.sync.emit('step', { key: key('lost'), title: 'T', total: 2, step: 1 });
    c.loseNextResponses(1);
    const r1 = await c.sync.flush();
    check('the lost answer looks like a network error and the events stay in the outbox', r1.status === 'network-error' && (await c.sync.pending()) === 2 && c.lost === 1, r1);
    c.clk.advance(60000);
    const r2 = await c.sync.flush();
    const posts = c.log.filter(l => l.method === 'POST');
    check('the resend carries the same event ids and the server accepts them', r2.accepted === 2 && JSON.stringify(posts[0].events) === JSON.stringify(posts[1].events), { r2 });
    await c.sync.pull();
    check('the work was done once: 1 + 1 + 5 = 7 coins, not doubled', (await c.sync.snapshot()).coins === 7, (await c.sync.snapshot()).coins);
    // and a repeat event whose answer is lost is not counted twice (this is the case a "set" cannot protect)
    const db = spawnSync(PHP, ['-r', `$c = require '${cfg.replace(/\\/g, '/')}'; $p = new PDO("mysql:host={$c['db_host']};dbname={$c['db_name']}", $c['db_user'], $c['db_pass']); $p->exec("UPDATE activity_progress SET last_completed_at = NOW() - INTERVAL 3 DAY WHERE user_id = ${a.user.id}");`]);
    await c.sync.emit('again', { key: key('lost') });
    c.loseNextResponses(1); await c.sync.flush(); c.clk.advance(60000); await c.sync.flush();
    await c.sync.pull();
    const times = (await c.sync.snapshot()).progress[key('lost')].times;
    check('a repeat whose answer was lost is counted once (times = 2, 9 coins)', db.status === 0 && times === 2 && (await c.sync.snapshot()).coins === 9, { times, coins: (await c.sync.snapshot()).coins });
  }

  // ---- 3. offline, reload, online
  {
    const a = await account(); const idb = new IDBFactory();
    const c1 = client({ idb }); await sign(c1, a); c1.setOnline(false);
    await c1.sync.emit('step', { key: key('off'), title: 'T', total: 2, step: 0 });
    await c1.sync.emit('step', { key: key('off'), title: 'T', total: 2, step: 1 });
    check('offline: nothing is sent', (await c1.sync.flush()).status === 'offline' && c1.log.length === 0);
    const c2 = client({ idb }); await c2.sync.setUser({ id: a.user.id });         // the page was reloaded: new objects, same IndexedDB
    check('after the reload the events and the device token are still there', (await c2.sync.pending()) === 2 && (await c2.sync.status()).hasDeviceToken);
    const r = await c2.sync.sync();
    check('back online they are delivered exactly once', r.flush.accepted === 2 && (await c2.sync.snapshot()).coins === 7);
  }

  // ---- 4. two devices, concurrent plan edits
  {
    const a = await account(); const dev2 = await secondDevice(a);
    const A = client(), B = client(); await sign(A, a); await sign(B, a, dev2);
    await A.sync.emit('plan.save', { plan: plan('plan_e2e1', 'Start', [{ id: 't1', n: 3, done: 0 }, { id: 't2', n: 2, done: 0 }]), baseRev: 0 });
    await A.sync.sync(); await B.sync.sync();
    check('the second device receives the plan with its revision', (await B.sync.snapshot()).plans.plan_e2e1.rev === 1);
    A.setOnline(false); B.setOnline(false);
    await A.sync.emit('plan.save', { plan: plan('plan_e2e1', 'Start', [{ id: 't1', n: 3, done: 3 }, { id: 't2', n: 2, done: 0 }]), baseRev: 1 });
    await B.sync.emit('plan.save', { plan: plan('plan_e2e1', 'Renamed on B', [{ id: 't1', n: 3, done: 1 }]), baseRev: 1 });
    A.setOnline(true); B.setOnline(true);
    await A.sync.sync(); await B.sync.sync(); await A.sync.sync();
    const pa = (await A.sync.snapshot()).plans.plan_e2e1, pb = (await B.sync.snapshot()).plans.plan_e2e1;
    check('both devices end with the same plan: B\'s name, A\'s ticked work kept (done 3), B\'s removal kept', JSON.stringify(pa) === JSON.stringify(pb) && pa.name === 'Renamed on B' && pa.sessions[0].tasks.length === 1 && pa.sessions[0].tasks[0].done === 3, { pa, pb });
    await A.sync.emit('plan.delete', { id: 'plan_e2e1' });
    await A.sync.sync(); await B.sync.sync();
    check('a delete reaches the other device', !(await B.sync.snapshot()).plans.plan_e2e1 && (await B.sync.snapshot()).plansDeleted.plan_e2e1 === true);
  }

  // ---- 5. guest first, account later
  {
    const c = client();
    await c.sync.emit('step', { key: key('guest'), title: 'T', total: 1, step: 0 });
    await c.sync.emit('tp.answer', { mcqId: 'g1', track: 'cls9-bio', day: '2026-10-20', correct: true, ms: 1000, ts: 5 });
    const a = await account(); const offered = []; c.sync.on('guestevents', k => offered.push(k));
    await sign(c, a);
    await c.sync.sync();
    check('guest events are offered, not sent, until the student agrees', offered[0] === 2 && c.log.filter(l => l.method === 'POST').length === 0 && (await c.sync.pendingGuest()) === 2);
    await c.sync.adoptGuest(); await c.sync.sync();
    const snap = await c.sync.snapshot();
    check('after agreeing they reach the account (6 coins for the finished activity, 1 answer)', snap.coins === 6 && snap.tp.q.g1[0] === 1, { coins: snap.coins, q: snap.tp.q });
  }

  // ---- 6. the device is revoked on the server
  {
    const a = await account(); const c = client(); await sign(c, a);
    await api('auth.php?action=logout', {}, { Authorization: 'Bearer ' + a.device.token });
    await c.sync.emit('step', { key: key('rev'), title: 'T', total: 1, step: 0 });
    const r = await c.sync.flush();
    const st = await c.sync.status();
    check('a revoked token ends in auth-lost; the student stays signed in and the event is kept', r.status === 'auth-lost' && st.signedIn && st.pending === 1 && st.pendingGuest === 0, st);
    const fresh = await secondDevice(a);
    await c.sync.setDevice(a.user.id, fresh);
    check('with a new token the waiting event is delivered', (await c.sync.flush()).accepted === 1);
  }

  // ---- 7. a bad event does not block the good ones
  {
    const a = await account(); const c = client(); await sign(c, a);
    await c.sync.emit('step', { key: 'not a valid key', title: 'T', total: 1, step: 0 });
    await c.sync.emit('step', { key: key('good'), title: 'T', total: 1, step: 0 });
    const r = await c.sync.flush();
    const rej = await c.sync.rejected();
    check('a rejected event is dropped with its reason and the good one is accepted', r.accepted === 1 && r.rejected === 1 && rej[0].code === 'bad_key' && (await c.sync.pending()) === 0);
  }
  finish();
})().catch(e => { console.error(e); fail++; finish(); });

function finish() {
  try { server.kill(); } catch (e) { /* gone */ }
  spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'drop']);
  try { fs.unlinkSync(cfg); } catch (e) { /* gone */ }
  console.log('---\nsync e2e tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
}
