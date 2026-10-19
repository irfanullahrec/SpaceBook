'use strict';
/* Unit tests for js/core/store.js and js/core/sync.js: fake IndexedDB, fake clock/timers, stub server.
 *   node tests/sync/unit.js */
const { IDBFactory } = require('fake-indexeddb');
const Store = require('../../js/core/store.js');
const Sync = require('../../js/core/sync.js');

let pass = 0, fail = 0;
function check(label, cond, detail) {
  if (cond) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail) : '')); }
}

function clock() {
  let t = 1700000000000, id = 0, timers = [];
  return {
    now: () => t, advance(ms) { t += ms; const due = timers.filter(x => x.at <= t); timers = timers.filter(x => x.at > t); due.forEach(x => x.fn()); },
    timers: { setTimeout: (fn, ms) => { const h = ++id; timers.push({ id: h, at: t + ms, fn }); return h; }, clearTimeout: h => { timers = timers.filter(x => x.id !== h); }, setInterval: () => 0 },
    armed: () => timers.length, nextDue: () => (timers.length ? Math.min(...timers.map(x => x.at)) - t : null),
  };
}
const settle = () => new Promise(r => setTimeout(r, 60));   // lets pending IndexedDB work finish
let uidN = 0;
const uuid = () => { const h = (++uidN).toString(16).padStart(12, '0'); return '00000000-0000-4000-8000-' + h; };

// a stub of api/v2/sync.php: `handler(events, req)` returns {status, body, headers}
function stubServer(handler) {
  const calls = [];
  const fetch = async (url, o) => {
    const body = o.body ? JSON.parse(o.body) : null;
    const call = { url, method: o.method, headers: o.headers, events: body ? body.events : null };
    calls.push(call);
    const r = await handler(call);
    if (r instanceof Error) throw r;
    return { status: r.status, headers: { get: k => (r.headers || {})[k] || null }, json: async () => r.body };
  };
  return { fetch, calls };
}
const emptyPull = { ok: true, cursor: 1, more: false, coins: 7, progress: {}, plans: [], plansDeleted: [], tp: { q: {}, days: {}, sessions: [], run: null, runClearedAt: 0 } };
const okAll = call => (call.events ? { status: 200, body: { ok: true, accepted: call.events.map(e => e.eventId), rejected: [], cursor: 1, coins: 7 } } : { status: 200, body: emptyPull });

function make(opts) {
  opts = opts || {};
  const idb = opts.idb || new IDBFactory();
  const store = Store.create({ indexedDB: idb });
  const clk = opts.clock || clock();
  const srv = opts.server || stubServer(okAll);
  const sync = Sync.create({ store, enabled: opts.enabled || (() => true), fetch: srv.fetch, now: clk.now, timers: clk.timers, uuid, random: () => 0.5, isOnline: opts.isOnline || (() => true) });
  return { idb, store, clk, srv, sync };
}

(async () => {
  // ================= store
  console.log('--- store ---');
  {
    const idb = new IDBFactory();
    const s1 = Store.create({ indexedDB: idb });
    await s1.put('outbox', 'b', { n: 2 }); await s1.put('outbox', 'a', { n: 1 }); await s1.put('meta', 'k', 'v');
    check('IndexedDB backend is used and lists keys in order', (await s1.ready) === 'idb' && JSON.stringify((await s1.all('outbox')).map(r => r[0])) === '["a","b"]');
    const s2 = Store.create({ indexedDB: idb });          // "reload": a new store over the same database
    check('data survives a reload (new store, same database)', (await s2.get('outbox', 'a')).n === 1 && (await s2.count('outbox')) === 2 && (await s2.get('meta', 'k')) === 'v');
    await s2.delMany('outbox', ['a']);
    check('delMany removes only the named keys', (await s2.count('outbox')) === 1);
    const mem = {}; const ls = { getItem: k => (k in mem ? mem[k] : null), setItem: (k, v) => { mem[k] = String(v); }, removeItem: k => { delete mem[k]; }, key: i => Object.keys(mem)[i] || null, get length() { return Object.keys(mem).length; } };
    const s3 = Store.create({ indexedDB: null, localStorage: ls });
    await s3.put('state', 'x', { a: [1] });
    check('falls back to localStorage when IndexedDB is missing', (await s3.ready) === 'localStorage' && (await s3.get('state', 'x')).a[0] === 1 && Object.keys(mem)[0].indexOf('sbcore:state:') === 0);
    const s4 = Store.create({ indexedDB: { open() { throw new Error('blocked'); } }, localStorage: null });
    await s4.put('meta', 'z', 1);
    check('falls back to memory when IndexedDB throws and there is no localStorage', (await s4.ready) === 'memory' && (await s4.get('meta', 'z')) === 1);
  }

  // ================= emit / outbox / guest
  console.log('--- outbox ---');
  {
    const t = make({ server: stubServer(() => new Error('offline')) });
    await t.sync.setUser({ id: 7 });
    const ev = await t.sync.emit('step', { key: 'k', total: 3, step: 0 });
    check('emit writes the event to the outbox before any request', (await t.store.count('outbox')) === 1 && t.srv.calls.length === 0 && ev.schema === 1 && ev.eventId.length === 36);
    const e2 = await t.sync.emit('step', { key: 'k', total: 3, step: 1 });
    const keys = (await t.store.all('outbox')).map(r => r[0]);
    check('events are kept in the order they were made, even with the same millisecond', keys[0].endsWith(ev.eventId) && keys[1].endsWith(e2.eventId) && keys[0] < keys[1]);
  }
  {
    const t = make();
    const seen = []; t.sync.on('guestevents', n => seen.push(n));
    await t.sync.emit('step', { key: 'g', total: 1, step: 0 });
    await t.sync.emit('step', { key: 'g2', total: 1, step: 0 });
    check('events made while signed out belong to the guest and are not sent', (await t.sync.pendingGuest()) === 2 && t.srv.calls.length === 0);
    await t.sync.setUser({ id: 9 });
    check('signing in reports the waiting guest events', seen[0] === 2 && (await t.sync.pendingGuest()) === 2);
    await t.sync.flush();
    check('guest events stay on the device until the student agrees', t.srv.calls.length === 0 && (await t.sync.pendingGuest()) === 2);
    check('adoptGuest moves them to the account', (await t.sync.adoptGuest()) === 2 && (await t.sync.pending()) === 2 && (await t.sync.pendingGuest()) === 0);
    const r = await t.sync.flush();
    check('and then they are sent', r.accepted === 2 && t.srv.calls[0].events.length === 2 && (await t.store.count('outbox')) === 0);
  }
  {
    const t = make();
    await t.sync.setUser({ id: 1 });
    await t.sync.emit('step', { key: 'u1', total: 1, step: 0 });
    await t.sync.setUser(null);
    await t.sync.setUser({ id: 2 });
    const r = await t.sync.flush();
    check("one account's events are never sent as another's", r.sent === 0 && (await t.store.count('outbox')) === 1);
  }

  // ================= flush results
  console.log('--- flush ---');
  {
    const t = make({ server: stubServer(call => ({ status: 200, body: { ok: true, accepted: [call.events[0].eventId], rejected: [{ eventId: call.events[1].eventId, code: 'bad_key' }], cursor: 3, coins: 12 } })) });
    await t.sync.setUser({ id: 1 });
    const coins = []; t.sync.on('coins', c => coins.push(c));
    await t.sync.emit('step', {}); await t.sync.emit('step', {});
    const r = await t.sync.flush();
    check('accepted and rejected events leave the outbox, the coin total is announced', r.accepted === 1 && r.rejected === 1 && (await t.store.count('outbox')) === 0 && coins[0] === 12, r);
    const rej = await t.sync.rejected();
    check('rejected events are remembered with the reason', rej.length === 1 && rej[0].code === 'bad_key');
  }
  {
    let mode = 'drop';
    const t = make({ server: stubServer(call => (mode === 'drop' ? new Error('network down') : okAll(call))) });
    await t.sync.setUser({ id: 1 });
    await t.sync.emit('step', { n: 1 }); await t.sync.emit('step', { n: 2 });
    const r1 = await t.sync.flush();
    const ids1 = t.srv.calls[0].events.map(e => e.eventId);
    check('a network error keeps every event and starts a back-off of 1-2 s x2', r1.status === 'network-error' && (await t.store.count('outbox')) === 2 && r1.waitMs >= 2000 * 0.5 && r1.waitMs <= 2000, r1);
    const r2 = await t.sync.flush();
    check('flush during the back-off sends nothing and keeps the retry armed', r2.status === 'backoff' && t.srv.calls.length === 1 && t.clk.armed() === 1);
    t.clk.advance(r1.waitMs + 100);
    await settle();
    check('the retry fires by itself (still failing: second back-off is longer)', t.srv.calls.length === 2);
    const st = await t.sync.status();
    check('status shows the failure count and that the student is still signed in', st.failures === 2 && st.signedIn === true && st.lastError === 'network' && st.pending === 2);
    mode = 'ok';
    t.clk.advance(60000); await settle(); t.clk.advance(60000); await settle();
    const after = await t.sync.status();
    const posts = t.srv.calls.filter(c => c.events);
    const ids3 = posts[posts.length - 1].events.map(e => e.eventId);
    check('when the network returns everything is sent, with the same event ids as before', after.pending === 0 && after.failures === 0 && JSON.stringify(ids3) === JSON.stringify(ids1), { after, ids1, ids3 });
  }
  {
    // a new event during a back-off re-arms the debounce timer; the pending retry must survive that
    let mode = 'drop';
    const t = make({ server: stubServer(call => (mode === 'drop' ? new Error('down') : okAll(call))) });
    await t.sync.setUser({ id: 1 });
    await t.sync.emit('step', { n: 1 });
    await t.sync.flush();                                  // failure 1 -> wait ~1.5 s
    t.clk.advance(1700); await settle();                   // retry fires, fails again -> failure 2, wait ~3 s
    const callsBefore = t.srv.calls.length;
    await t.sync.emit('step', { n: 2 });                   // debounce timer (1.5 s) replaces the retry timer
    t.clk.advance(1600); await settle();                   // fires inside the back-off window: must not send, must re-arm
    check('an event made during a back-off does not send early', t.srv.calls.length === callsBefore);
    mode = 'ok';
    t.clk.advance(4000); await settle(); t.clk.advance(4000); await settle();
    check('and the retry still happens afterwards (nothing waits forever)', (await t.sync.pending()) === 0, await t.sync.status());
  }
  {
    // flag off: no automatic sending at all (the page behaves as before), explicit flush still works
    const t = make({ enabled: () => false });
    await t.sync.setUser({ id: 1 });
    await t.sync.emit('step', {});
    t.clk.advance(10000); await settle();
    check('with the flag off nothing is sent automatically and no timer is armed', t.srv.calls.length === 0 && t.clk.armed() === 0 && (await t.sync.pending()) === 1);
    const r = await t.sync.flush();
    check('with the flag off an explicit flush still works', r.accepted === 1);
  }
  {
    const t = make({ server: stubServer(() => ({ status: 429, headers: { 'Retry-After': '30' }, body: { ok: false } })) });
    await t.sync.setUser({ id: 1 }); await t.sync.emit('step', {});
    const r = await t.sync.flush();
    check('429 honours Retry-After (>= 30 s)', r.status === 'http-429' && r.waitMs >= 30000 && (await t.store.count('outbox')) === 1, r);
  }
  {
    const t = make({ server: stubServer(() => ({ status: 500, body: null })) });
    await t.sync.setUser({ id: 1 }); await t.sync.emit('step', {});
    const r = await t.sync.flush();
    check('a 500 with no JSON body keeps the event', r.status === 'http-500' && (await t.store.count('outbox')) === 1);
  }
  {
    let auth = false;
    const t = make({ server: stubServer(call => (auth ? okAll(call) : { status: 401, body: { ok: false } })) });
    await t.sync.setUser({ id: 5 });
    const lost = []; t.sync.on('authlost', () => lost.push(1));
    await t.sync.emit('step', {});
    const r = await t.sync.flush();
    const st = await t.sync.status();
    check('401 reports auth-lost, keeps the event and does NOT sign the student out or turn them into a guest', r.status === 'auth-lost' && lost.length === 1 && st.signedIn && st.user === '5' && st.pending === 1 && st.pendingGuest === 0);
    check('while auth is lost nothing more is sent', (await t.sync.flush()).status === 'auth-lost' && t.srv.calls.length === 1);
    auth = true;
    await t.sync.setDevice(5, { id: 'd', token: 'a'.repeat(64) });
    const r2 = await t.sync.flush();
    check('a new device token resumes sending, with the Authorization header', r2.accepted === 1 && t.srv.calls[1].headers.Authorization === 'Bearer ' + 'a'.repeat(64));
  }
  {
    // emitLatest: "the latest copy wins" state does not pile up, even when called many times at once
    const t = make({ server: stubServer(() => new Error('offline')) });
    await t.sync.setUser({ id: 1 });
    await Promise.all([1, 2, 3, 4, 5, 6].map(i => t.sync.emitLatest('tp.run', { run: { savedAt: i } })));
    await t.sync.emit('tp.answer', { n: 1 });
    await t.sync.emitLatest('tp.run', { run: { savedAt: 7 } });
    const evs = await t.sync.pendingEvents();
    const runs = evs.filter(e => e.type === 'tp.run');
    check('emitLatest keeps one waiting copy (the newest) however it is called, and leaves other events alone', runs.length === 1 && runs[0].payload.run.savedAt === 7 && evs.filter(e => e.type === 'tp.answer').length === 1, evs.map(e => e.type + ':' + (e.payload.run ? e.payload.run.savedAt : '')));
  }
  {
    // a 401 for a request that was sent before the device token arrived must not latch "auth lost"
    let t;
    t = make({ server: stubServer(async call => {
      if (!call.headers.Authorization) { await t.sync.setDevice(5, { id: 'd', token: 'c'.repeat(64) }); return { status: 401, body: { ok: false } }; }   // the token arrives while the first request is in flight
      return okAll(call);
    }) });
    await t.sync.setUser({ id: 5 });
    await t.sync.emit('step', {});
    const r1 = await t.sync.flush();
    check('a 401 that answers a request sent with old credentials is ignored (not auth-lost) and retried', r1.status === 'retry' && (await t.sync.status()).authLost === false && t.clk.armed() >= 1, r1);
    t.clk.advance(100); await settle();
    check('and the retry with the new token delivers the event', (await t.sync.pending()) === 0 && t.srv.calls.some(c => c.headers.Authorization === 'Bearer ' + 'c'.repeat(64)));
  }
  {
    // the server answers 413 for more than 3 events per batch, and 422 for a poison event
    const t = make({ server: stubServer(call => {
      if (call.events.some(e => e.payload.poison)) return call.events.length > 1 ? { status: 422, body: { ok: false } } : { status: 422, body: { ok: false } };
      if (call.events.length > 3) return { status: 413, body: { ok: false } };
      return okAll(call);
    }) });
    await t.sync.setUser({ id: 1 });
    for (let i = 0; i < 10; i++) await t.sync.emit('step', { i, poison: i === 6 });
    const r = await t.sync.flush();
    const rej = await t.sync.rejected();
    check('a too-large batch is halved until it fits; a poison event is dropped alone and recorded', (await t.store.count('outbox')) === 0 && r.accepted === 9 && rej.length === 1 && rej[0].code === 'server_422', { r, rej });
  }
  {
    // two flush() calls at once never overlap
    let inflight = 0, maxInflight = 0;
    const t = make({ server: stubServer(async call => { inflight++; maxInflight = Math.max(maxInflight, inflight); await new Promise(r => setTimeout(r, 20)); inflight--; return okAll(call); }) });
    await t.sync.setUser({ id: 1 });
    await t.sync.emit('step', {});
    await Promise.all([t.sync.flush(), t.sync.flush(), t.sync.flush()]);
    check('concurrent flush calls are single-flight', maxInflight === 1);
  }
  {
    const t = make({ isOnline: () => false });
    await t.sync.setUser({ id: 1 }); await t.sync.emit('step', {});
    check('offline: nothing is sent and nothing is lost', (await t.sync.flush()).status === 'offline' && t.srv.calls.length === 0 && (await t.sync.pending()) === 1);
  }

  // ================= survives a reload
  console.log('--- reload ---');
  {
    const idb = new IDBFactory();
    const a = make({ idb, server: stubServer(() => new Error('offline')) });
    await a.sync.setUser({ id: 3 });
    await a.sync.setDevice(3, { id: 'dev', token: 'b'.repeat(64) });
    await a.sync.emit('step', { n: 1 }); await a.sync.emit('step', { n: 2 }); await a.sync.emit('step', { n: 3 });
    const b = make({ idb });                       // the page was reloaded: new objects over the same IndexedDB
    await b.sync.setUser({ id: 3 });
    check('after a reload the events and the device token are still there', (await b.sync.pending()) === 3 && (await b.sync.status()).hasDeviceToken && b.sync.deviceId === a.sync.deviceId);
    const r = await b.sync.flush();
    check('and are sent after the reload', r.accepted === 3 && (await b.sync.pending()) === 0);
  }

  // ================= pull
  console.log('--- pull ---');
  {
    const snap = Sync.emptySnapshot();
    Sync.applyPull(snap, { coins: 5, progress: { a: { done: [0], total: 2 } }, plans: [{ id: 'p1', name: 'one', rev: 1 }, { id: 'p2', name: 'two', rev: 1 }], plansDeleted: [],
      tp: { q: { m1: [1, 1, 5, 1, 9] }, days: { t: { d1: [1, 1, 1] } }, sessions: [{ id: 's1' }], run: { id: 'r' }, runClearedAt: 0 } });
    Sync.applyPull(snap, { coins: 9, progress: { b: { done: [], total: 1 } }, plans: [{ id: 'p1', name: 'one v2', rev: 2 }], plansDeleted: ['p2'],
      tp: { q: { m2: [1, 0, 6, 0, 1] }, days: { t: { d2: [2, 2, 2] }, u: { d1: [3, 3, 3] } }, sessions: [{ id: 's2' }], run: null, runClearedAt: 77 } });
    check('applyPull merges objects, replaces plans, removes deleted plans, clears the run', Object.keys(snap.progress).length === 2 && snap.plans.p1.name === 'one v2' && !snap.plans.p2 && snap.plansDeleted.p2 === true
      && Object.keys(snap.tp.q).length === 2 && Object.keys(snap.tp.days.t).length === 2 && snap.tp.days.u.d1[0] === 3 && Object.keys(snap.tp.sessions).length === 2 && snap.tp.run === null && snap.tp.runClearedAt === 77 && snap.coins === 9, snap);
    const again = JSON.stringify(snap);
    Sync.applyPull(snap, { coins: 9, progress: { b: { done: [], total: 1 } }, plans: [{ id: 'p1', name: 'one v2', rev: 2 }], plansDeleted: ['p2'], tp: { q: { m2: [1, 0, 6, 0, 1] }, days: { t: { d2: [2, 2, 2] }, u: { d1: [3, 3, 3] } }, sessions: [{ id: 's2' }], run: null, runClearedAt: 77 } });
    check('applying the same pull twice changes nothing', JSON.stringify(snap) === again);
  }
  {
    const pages = [
      { ok: true, cursor: 10, more: true, coins: 1, progress: { a: { done: [0], total: 1 } }, plans: [], plansDeleted: [], tp: { q: {}, days: {}, sessions: [], run: null, runClearedAt: 0 } },
      { ok: true, cursor: 12, more: false, coins: 2, progress: { b: { done: [0], total: 1 } }, plans: [], plansDeleted: [], tp: { q: {}, days: {}, sessions: [], run: null, runClearedAt: 0 } },
    ];
    const t = make({ server: stubServer(call => ({ status: 200, body: pages.shift() })) });
    await t.sync.setUser({ id: 4 });
    const r = await t.sync.pull();
    const snap = await t.sync.snapshot();
    check('pull follows "more" to the end, merges both pages and stores the cursor', r.status === 'ok' && r.pages === 2 && r.cursor === 12 && Object.keys(snap.progress).length === 2 && snap.coins === 2 && t.srv.calls[0].url.endsWith('since=0') && t.srv.calls[1].url.endsWith('since=10'), { r, urls: t.srv.calls.map(c => c.url) });
    const t2 = make({ idb: t.idb, server: stubServer(call => ({ status: 200, body: { ok: true, cursor: 12, more: false, coins: 2, progress: {}, plans: [], plansDeleted: [], tp: {} } })) });
    await t2.sync.setUser({ id: 4 }); await t2.sync.pull();
    check('after a reload the next pull continues from the stored cursor', t2.srv.calls[0].url.endsWith('since=12'));
    const t3 = make({ server: stubServer(() => ({ status: 401, body: { ok: false } })) });
    await t3.sync.setUser({ id: 4 });
    check('a 401 while pulling is reported as auth-lost, not as sign-out', (await t3.sync.pull()).status === 'auth-lost' && (await t3.sync.status()).signedIn);
  }

  console.log('---\nsync unit tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
