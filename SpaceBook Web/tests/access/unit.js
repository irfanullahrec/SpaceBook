'use strict';
/* js/sb_access.js in Node: the rules shared with the server and the app (tests/parity/access_contract.json), the free allowance with a fake server,
 * the offline fallback, and that a paid answer never outlives its end date.   node tests/access/unit.js */
const fs = require('fs'), path = require('path');
const { create } = require('../../js/sb_access.js');
const contract = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'parity', 'access_contract.json'), 'utf8'));
let pass = 0, fail = 0;
const check = (n, ok, d) => { if (ok) { pass++; console.log('PASS  ' + n); } else { fail++; console.log('FAIL  ' + n + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 300) : '')); } };
const store = () => { const m = {}; return { getItem: k => (k in m ? m[k] : null), setItem: (k, v) => { m[k] = String(v); }, removeItem: k => { delete m[k]; } }; };
const same = (a, b) => JSON.stringify([].concat(a).sort()) === JSON.stringify([].concat(b).sort());
const NOW = Date.parse(contract.now);

(async () => {
  // ---- the contract: server answer (fresh) and the offline recomputation must both agree with every scenario
  for (const sc of contract.scenarios) {
    for (const mode of ['fresh', 'offline']) {
      const a = create({ fetch: async () => { throw new Error('offline'); }, storage: store(), noAutoload: true, now: () => NOW, visitorId: 'a'.repeat(32) });
      a._setState({ access: sc.access, subscriptions: sc.subscriptions.map(s => Object.assign({ subjects: [] }, s)) }, mode === 'fresh');
      const acc = a.access();
      const accOk = ['readClasses', 'readSubjects', 'planClasses', 'paperSubjects'].every(k => same(acc[k], sc.access[k])) && acc.prep === sc.access.prep;
      const readOk = sc.read.every(c => a.canRead(c.cls, c.subject, c.chapter) === c.expect);
      const unlOk = sc.unlimited.every(c => a.unlimited(c.metric, { cls: c.cls, subject: c.subject }) === c.expect);
      check(sc.name + ' [' + mode + ']', accOk && readOk && unlOk, { acc, accOk, readOk, unlOk });
    }
  }

  // ---- a paid answer cached on the phone stops working at its end date even with no network
  let t = NOW;
  const exp = create({ fetch: async () => { throw new Error('offline'); }, storage: store(), noAutoload: true, now: () => t, visitorId: 'b'.repeat(32) });
  exp._setState({ access: { readClasses: ['cls9'], readSubjects: [], planClasses: ['cls9'], paperSubjects: [], prep: false },
    subscriptions: [{ planType: 'student', classId: 'cls9', status: 'active', expiresAt: '2026-10-30T00:00:00Z', subjects: [] }] }, false);
  check('offline, before the end date: the plan still opens its class', exp.canRead('cls9', 'cls9-eng', 3) === true);
  t = Date.parse('2026-10-30T00:00:01Z');
  check('offline, after the end date: it no longer does', exp.canRead('cls9', 'cls9-eng', 3) === false && exp.canRead('cls9', 'cls9-eng', 0) === true);

  // ---- the free allowance is spent on the server
  const server = { used: 0, calls: [] };
  const fetchOk = async (url, o) => {
    if (/entitlements/.test(url)) return { status: 200, json: async () => ({ ok: true, signedIn: false, plan: 'free', access: { readClasses: [], readSubjects: [], planClasses: [], paperSubjects: [], prep: false }, free: { chapters: 1, prep_q: { limit: 50, used: server.used }, plan_q: { limit: 50, used: 0 }, paper: { limit: 1, used: 0 } }, subscriptions: [] }) };
    const b = JSON.parse(o.body); server.calls.push(b);
    if (server.used >= 50) return { status: 200, json: async () => ({ ok: true, allowed: false, reason: 'limit', used: 50, limit: 50 }) };
    server.used++;
    return { status: 200, json: async () => ({ ok: true, allowed: true, used: server.used, limit: 50 }) };
  };
  const s = create({ fetch: fetchOk, storage: store(), noAutoload: true, now: () => NOW, visitorId: 'c'.repeat(32) });
  await s.load();
  let r = await s.useQuestion('prep_q', 'q1', {});
  check('a question goes to the server and is allowed', r.allowed && server.calls.length === 1 && server.calls[0].metric === 'prep_q' && s.free('prep_q').used === 1, r);
  server.used = 50;
  r = await s.useQuestion('prep_q', 'q51', {});
  check('the server refusing the 51st is final', r.allowed === false && r.reason === 'limit' && s.free('prep_q').used === 50, r);

  // ---- offline: counted here, sent later, never past the limit
  const down = create({ fetch: async () => { throw new Error('offline'); }, storage: store(), noAutoload: true, now: () => NOW, visitorId: 'd'.repeat(32) });
  let ok = 0; for (let i = 0; i < 52; i++) { const x = await down.useQuestion('prep_q', 'k' + i, {}); if (x.allowed) ok++; }
  check('offline: 50 are allowed on this phone and the 51st is not', ok === 50 && Object.keys(down.pending().prep_q).length === 50, ok);
  const x2 = await down.useQuestion('prep_q', 'k3', {});
  check('offline: the same question again is free', x2.allowed === true);
  const up = create({ fetch: fetchOk, storage: store(), noAutoload: true, now: () => NOW, visitorId: 'e'.repeat(32) });
  server.used = 0; server.calls = [];
  up._setState({ free: { chapters: 1, prep_q: { limit: 50, used: 0 }, plan_q: { limit: 50, used: 0 }, paper: { limit: 1, used: 0 } } }, true);
  await up.useQuestion('prep_q', 'z', {});
  const never = create({ fetch: async () => { throw new Error('should not be called'); }, storage: store(), noAutoload: true, now: () => NOW, visitorId: 'f'.repeat(32) });
  never._setState({ access: { readClasses: [], readSubjects: [], planClasses: [], paperSubjects: [], prep: true }, subscriptions: [] }, true);
  const nv = await never.useQuestion('prep_q', 'q', {});
  check('an unlimited plan never calls the server for a question', nv.allowed === true && nv.unlimited === true);

  // ---- visitor id: made once, 32 hex, kept
  const st = store();
  const v1 = create({ fetch: fetchOk, storage: st, noAutoload: true }); const id1 = v1.visitorId();
  const v2 = create({ fetch: fetchOk, storage: st, noAutoload: true });
  check('the visitor id is 32 hex characters and stays the same', /^[0-9a-f]{32}$/.test(id1) && v2.visitorId() === id1);
  check('requests carry the visitor id (and the device token when there is one)', (() => { const h = create({ fetch: fetchOk, storage: st, noAutoload: true, headers: () => ({ Authorization: 'Bearer x' }) }).headers(); return h['X-SB-Visitor'] === id1 && h.Authorization === 'Bearer x'; })());

  console.log('---\naccess unit: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})();
