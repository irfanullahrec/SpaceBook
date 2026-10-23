'use strict';
/* One account, two platforms, one database. Against the real PHP API and MySQL (tests/sync/harness.js):
 *   - the "app" is a raw client with its own device token that sends exactly the events of tests/parity/events_contract.json (the file the app's
 *     EventContractTest checks the app's own events against) and reads the server with GET api/v2/sync.php?since=, as the app does;
 *   - the "website" is the real page (every script of index.html in the app sandbox) with the real client code: SBSync, SBItems, SBRewards, SBStudyPlan.
 * What one does shows up on the other: coins and steps, a study plan and its deletion, Tests Preps answers, bookmarks, notes, highlights, reading
 * position, my class, marked words, game runs; both read the same plan answer from api/v2/entitlements.php.
 *     node tests/sync/parity_e2e.js */
const fs = require('fs'), path = require('path');
const harness = require('./harness');
const C = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'parity', 'events_contract.json'), 'utf8'));

const uuid = (() => { let n = 0; return () => '00000000-0000-4000-8000-' + (++n).toString(16).padStart(12, '0'); })();
const ev = (type, payload) => ({ eventId: uuid(), type, payload, clientTs: Date.now(), schema: 1 });
const itemPayloads = C.events['item.put'].payloads;

(async () => {
  const h = await harness.start();
  const { check, sleep } = h;
  console.log('--- the app writes, the website reads ---');

  const acct = await h.account();
  const W = h.newApp({ flag: true });
  await W.signIn(acct);
  const dev = await h.secondDevice(acct);                       // the app's own device token
  const auth = { Authorization: 'Bearer ' + dev.token };
  const post = events => h.api('v2/sync.php', { events }, auth);
  const pull = since => h.api('v2/sync.php?since=' + since, undefined, auth);

  // everything the contract names, as the app would send it
  const events = [
    ev('step', C.events.step.payload),
    ...Object.values(itemPayloads).map(p => ev('item.put', p)),
    ev('plan.save', C.events['plan.save'].payload),
    ev('tp.answer', C.events['tp.answer'].payload),
    ev('tp.session', C.events['tp.session'].payload),
  ];
  const r = await post(events);
  check('the server accepts every event of the contract, none rejected', r.status === 200 && r.json.ok && r.json.accepted.length === events.length && r.json.rejected.length === 0, r.json);
  check('one step is one coin, decided by the server', r.json.coins === 1, r.json.coins);

  await W.sb.SBSync.sync(); await W.sb.SBItems.syncNow(); await sleep(250);
  const snap = await W.sb.SBSync.snapshot();
  const bm = C.events['item.put'].payloads.bm;
  check('the website sees the app\'s bookmark (same place, same title)', JSON.stringify(W.sb.SBItems.get('bm', bm.key)) === JSON.stringify(bm.value), W.sb.SBItems.get('bm', bm.key));
  const note = itemPayloads.note;
  check('its note and highlight words', (W.sb.SBItems.get('note', note.key) || {}).x === note.value.x && W.sb.SBItems.get('note', note.key).q === note.value.q);
  check('where the app stopped reading, and its chosen class', (W.sb.SBItems.get('pos', 'cls5-math') || {}).p === 4 && (W.sb.SBItems.get('pref', 'class') || {}).id === 'cls5');
  check('a marked word, a best game run, a ticked SLO and a drill', (W.sb.SBItems.get('word', 'en:fraction') || {}).s === 'l' && (W.sb.SBItems.get('gbest', itemPayloads.gbest.key) || {}).b === 0.8 && W.sb.SBItems.get('slo', 'cls9-phy|1|0') !== null && (W.sb.SBItems.get('drill', itemPayloads.drill.key) || {}).c === 7);
  check('the step and the coin', snap.coins === 1 && snap.progress[C.events.step.payload.key] && snap.progress[C.events.step.payload.key].done.includes(0), { coins: snap.coins });
  check('the study plan', !!(snap.plans.plan_contract1 && snap.plans.plan_contract1.name === 'Contract plan' && snap.plans.plan_contract1.rev === 1), snap.plans);
  check('and the Tests Preps answer', snap.tp.q.g1 && snap.tp.q.g1[0] === 1 && snap.tp.q.g1[1] === 1 && snap.tp.sessions.sess_contract1, snap.tp.q);

  console.log('--- the website writes, the app reads ---');
  const first = await pull(0);
  const cursor = first.json.cursor;
  const sb = W.sb;
  await sb.SBItems.put('bm', 'cls9-phy|3|Exercises|1', { c: 'cls9', s: 'cls9-phy', ch: 3, p: 1, tb: 'Exercises', t: '4 Forces' });
  await sb.SBItems.put('note', '22222222-2222-4333-8444-555555555555', { c: 'cls9', s: 'cls9-phy', ch: 3, p: 1, tb: 'Exercises', t: '4 Forces', x: '', q: 'net force', k: 'hl' });
  await sb.SBItems.del('bm', bm.key);
  await sb.SBItems.put('pref', 'class', { id: 'cls9' });
  await sb.SBSync.emit('step', { key: 'cls9|g-quiz|u3|count|def456|5', title: 'Quiz Quest: Forces', total: 5, step: 2 });
  sb.SBStudyPlan.add({ id: 'plan_webmade1', name: 'Made on the website', classId: 'cls9', scope: [], cats: [], start: '2026-10-24', end: '2026-10-30', weekdays: [1, 2], skip: [], extra: [], alt: false, slots: [], revision: false, createdAt: 1, updatedAt: 1,
    sessions: [{ id: 's1', date: '2026-10-25', slot: 0, from: '16:00', to: '17:00', len: 60, tasks: [{ id: 't1', cat: 'rd', n: 2, done: 0 }] }] });
  await sb.SBSync.sync(); await sb.SBItems.syncNow(); await sleep(300);
  const second = await pull(cursor);
  const j = second.json;
  check('the app\'s pull has every field the app reads (' + C.pull.requiredByTheApp.join(', ') + ')', C.pull.requiredByTheApp.every(k => k in j), Object.keys(j));
  const kinds = Object.fromEntries(j.items.map(i => [i.kind + ':' + i.key, i]));
  check('it carries the website\'s new bookmark, highlight and class, each with kind, key, value and at', kinds['bm:cls9-phy|3|Exercises|1'] && kinds['note:22222222-2222-4333-8444-555555555555'].value.k === 'hl' && kinds['pref:class'].value.id === 'cls9'
    && j.items.every(i => C.pull.item.every(k => k in i)), Object.keys(kinds));
  check('and the delete of the bookmark the app had made (itemsDeleted with kind, key, at)', j.itemsDeleted.some(d => d.kind === 'bm' && d.key === bm.key) && j.itemsDeleted.every(d => C.pull.itemDeleted.every(k => k in d)), j.itemsDeleted);
  const full = (await pull(0)).json;
  check('the website\'s step is in the app\'s progress and the coins add up', full.progress['cls9|g-quiz|u3|count|def456|5'] && full.coins === 2, { coins: full.coins });
  check('the plan made on the website is there for the app', full.plans.some(p => p.id === 'plan_webmade1'), full.plans.map(p => p.id));
  check('the app\'s first bookmark is gone from a full pull (a deleted item is not carried)', !full.items.some(i => i.kind === 'bm' && i.key === bm.key));

  console.log('--- deleting a plan, from either side ---');
  const del = await post([ev('plan.delete', C.events['plan.delete'].payload)]);
  await sb.SBSync.sync(); await sleep(150);
  const snap2 = await sb.SBSync.snapshot();
  check('a plan deleted by the app disappears on the website', del.json.accepted.length === 1 && !snap2.plans.plan_contract1 && snap2.plansDeleted.plan_contract1 === true, snap2.plansDeleted);
  sb.SBStudyPlan.removePlan(sb.SBStudyPlan.plans().find(p => p.id === 'plan_webmade1'));
  await sb.SBSync.sync(); await sleep(150);
  check('and one deleted by the website is a deletion for the app', (await pull(0)).json.plansDeleted.includes('plan_webmade1'));

  console.log('--- one place for the plan ---');
  const wEnt = await sb.SBEntitlements.load();
  const aEnt = (await h.api('v2/entitlements.php', undefined, auth)).json;
  check('the website and the app read the same plan answer (plan, features, flags, signed in)', wEnt.plan === aEnt.plan && JSON.stringify(wEnt.features) === JSON.stringify(aEnt.features) && JSON.stringify(wEnt.flags) === JSON.stringify(aEnt.flags) && aEnt.signedIn === true && wEnt.signedIn === true, { web: wEnt, app: aEnt });
  check('it also carries the owner\'s sync switch, off', aEnt.flags && aEnt.flags.syncV2 === false);
  const me = (await h.api('auth.php?action=me', undefined, auth)).json;
  check('and so does "me", for the page the app shows', me.flags && me.flags.syncV2 === false && me.user && me.user.id === acct.user.id);

  h.finish('parity e2e (website client and app request shapes, one server)');
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
