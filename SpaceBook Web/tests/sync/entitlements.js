'use strict';
/* js/core/entitlements.js: the website reads the same plan answer as the Android app (api/v2/entitlements.php). No server needed.
 *     node tests/sync/entitlements.js */
const E = require('../../js/core/entitlements.js');
let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d) : '')); } };
const mem = () => { const m = {}; return { getItem: k => (k in m ? m[k] : null), setItem: (k, v) => { m[k] = String(v); }, m }; };
const answer = body => async () => ({ ok: true, status: 200, json: async () => body });

(async () => {
  const none = E.create({ storage: mem(), noAutoload: true, fetch: async () => { throw new Error('offline'); } });
  check('with no answer ever everything is allowed and the plan is free', none.allows('testPrep') && none.allows('anything') && none.plan() === 'free');
  await none.load();
  check('a failed request keeps it that way', none.allows('games') && none.get().unlocked === true);

  const st = mem(), seen = [];
  const e = E.create({ storage: st, noAutoload: true, fetch: answer({ ok: true, plan: 'free', signedIn: true, unlocked: false, classes: ['cls1'], features: { games: false, testPrep: true }, flags: { syncV2: false }, version: 1 }), headers: () => ({ Authorization: 'Bearer x' }) });
  e.on(v => seen.push(v.plan));
  await e.load();
  check('a locked plan allows what the server says true and blocks what it says false', e.allows('testPrep') && !e.allows('games') && e.allows('unmentioned') && !seen.length === false);
  check('and says which classes', JSON.stringify(e.get().classes) === '["cls1"]' && e.get().signedIn === true);
  check('the answer is kept for the next page load', JSON.parse(st.m.sb_entitlements).features.games === false);
  const later = E.create({ storage: st, noAutoload: true, fetch: async () => { throw new Error('offline'); } });
  check('a page with no network still knows the last plan', !later.allows('games') && later.allows('testPrep'));
  const open = E.create({ storage: mem(), noAutoload: true, fetch: answer({ ok: true, plan: 'free', unlocked: true, features: { games: false } }) });
  await open.load();
  check('unlocked wins over a feature flag, exactly as in the app (EntitlementsDto.allows)', open.allows('games'));
  const bad = E.create({ storage: mem(), noAutoload: true, fetch: async () => ({ ok: false, status: 500, json: async () => ({ ok: false }) }) });
  await bad.load();
  check('an error answer changes nothing', bad.allows('games') && bad.plan() === 'free');
  console.log(`---\nentitlements: ${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})();
