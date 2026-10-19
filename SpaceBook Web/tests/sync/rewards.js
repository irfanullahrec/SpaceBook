'use strict';
/* Integration: the real js/sb_rewards.js (inside the app sandbox, all scripts loaded) with the real js/core/*
 * against the real PHP API on a scratch database.   node tests/sync/rewards.js */
const harness = require('./harness');

const KEY = s => 'cls2|math|u0|trace|' + s + '|0';
const storageOf = t => { const o = {}, ls = t.sb.localStorage; for (let i = 0; i < ls.length; i++) { const k = ls.key(i); o[k] = ls.getItem(k); } return o; };

(async () => {
  const h = await harness.start();
  const { check, sleep } = h;
  console.log('--- sb_rewards.js with sync v2 ---');

  // 1. offline steps are kept, shown immediately, and delivered later
  {
    const a = await h.account(); const t = h.newApp({ flag: true, me: a.user });
    await t.signIn(a);
    check('signed in with the flag on: rewards use the account', t.sb.SBRewards.signedIn === true && t.sb.SBRewards.coins === 0);
    t.offline();
    const r1 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 0);
    const r2 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 1);
    const r3 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 2);
    check('offline steps still earn at once (1 + 1 + 1 + 5 shown locally) and the student stays signed in', r1.ok && r1.earned === 1 && r2.earned === 1 && r3.earned === 6 && r3.completed === true && t.sb.SBRewards.coins === 8 && t.sb.SBRewards.signedIn === true, [r1, r2, r3]);
    check('the steps wait in the outbox, nothing was demoted to guest data', (await t.sb.SBSync.pending()) === 3 && (await t.sb.SBSync.pendingGuest()) === 0 && !t.sb.localStorage.getItem('sb_rewards_guest_v1'));
    check('the activity state shows the finished steps', JSON.stringify(t.sb.SBRewards.get(KEY('a1')).done) === '[0,1,2]' && t.sb.SBRewards.get(KEY('a1')).times === 1);
    t.online();
    const s = await t.sb.SBSync.sync(); await sleep(150);
    check('back online the events are delivered and the server agrees (8 coins)', s.flush.accepted === 3 && t.sb.SBRewards.coins === 8 && (await t.sb.SBSync.pending()) === 0, { s: s.flush, coins: t.sb.SBRewards.coins });
    const t2 = h.newApp({ flag: true, me: a.user }); await t2.signIn(a, await h.secondDevice(a)); await t2.sb.SBSync.sync(); await sleep(150);
    check('a second device (fresh page, same account) sees the same coins and steps', t2.sb.SBRewards.coins === 8 && JSON.stringify(t2.sb.SBRewards.get(KEY('a1')).done) === '[0,1,2]', t2.sb.SBRewards.coins);
  }

  // 2. a request that fails never changes who the student is
  {
    const a = await h.account(); const t = h.newApp({ flag: true, me: a.user });
    await t.signIn(a);
    t.net.down = true;                                          // online, but the server does not answer
    await t.sb.SBRewards.step(KEY('b1'), 'Figure', 2, 0);
    const fl = await t.sb.SBSync.flush();
    const st = await t.sb.SBSync.status();
    check('a server that does not answer only starts a back-off; the student stays signed in with the step safe', fl.status === 'network-error' && st.failures === 1 && st.signedIn && st.pending === 1 && t.sb.SBRewards.signedIn === true, [fl, st]);
  }

  // 3. progress made as a guest joins the account at sign-in, after the student agrees
  {
    const a = await h.account(); const G = h.newApp({ flag: true });
    await G.sb.SBRewards.step(KEY('g1'), 'Figure', 2, 0);       // nobody signed in yet
    await G.sb.SBRewards.step(KEY('g1'), 'Figure', 2, 1);
    check('as a guest the coins are kept on this device (1 + 1 + 5)', G.sb.SBRewards.coins === 7 && !!G.sb.localStorage.getItem('sb_rewards_guest_v1'));
    const t = h.newApp({ flag: true, me: a.user, storage: storageOf(G) });
    await t.signIn(a);
    check('the student is asked once and says yes: the local guest copy is removed and the coins are unchanged (7)', t.net.prompts.length === 1 && !t.sb.localStorage.getItem('sb_rewards_guest_v1') && t.sb.SBRewards.coins === 7, [t.net.prompts.length, t.sb.SBRewards.coins]);
    await t.sb.SBSync.sync(); await sleep(150);
    const t3 = h.newApp({ flag: true, me: a.user }); await t3.signIn(a, await h.secondDevice(a)); await t3.sb.SBSync.sync(); await sleep(150);
    check('the account (seen from a fresh page) holds the guest steps: 7 coins, 2 steps', t3.sb.SBRewards.coins === 7 && JSON.stringify(t3.sb.SBRewards.get(KEY('g1')).done) === '[0,1]');
  }

  // 3b. ... and when the student says no, the guest progress stays on the device
  {
    const a = await h.account(); const G = h.newApp({ flag: true });
    await G.sb.SBRewards.step(KEY('n1'), 'Figure', 2, 0);
    const t = h.newApp({ flag: true, me: a.user, storage: storageOf(G), consent: false });
    await t.signIn(a);
    check('Cancel: nothing is added to the account, the guest copy stays on this device, the account shows 0', t.net.prompts.length === 1 && !!t.sb.localStorage.getItem('sb_rewards_guest_v1') && t.sb.SBRewards.coins === 0 && (await t.sb.SBSync.pending()) === 0, [t.net.prompts.length, t.sb.SBRewards.coins]);
    const t2 = h.newApp({ flag: true, me: a.user, storage: storageOf(t), consent: false });
    await t2.signIn(a);
    check('and the question is not asked again on the next page load', t2.net.prompts.length === 0 && !!t2.sb.localStorage.getItem('sb_rewards_guest_v1'));
  }

  // 4. repeating a finished activity
  {
    const a = await h.account(); const t = h.newApp({ flag: true, me: a.user });
    await t.signIn(a);
    await t.sb.SBRewards.step(KEY('r1'), 'Figure', 1, 0);
    const again = await t.sb.SBRewards.again(KEY('r1'));
    check('doing a finished activity again on the same day earns nothing but is recorded', again.ok === true && again.earned === 0 && again.times === 2, again);
    const never = await t.sb.SBRewards.again(KEY('nope'));
    check('repeating an activity that was never finished is refused', never.ok === false);
    await t.sb.SBSync.sync();
    check('the server accepted both', (await t.sb.SBSync.pending()) === 0);
  }

  // 5. the flag off: the old behaviour, untouched
  {
    const a = await h.account(); const t = h.newApp({ flag: false, me: a.user });
    await t.signIn(a);
    await t.sb.SBRewards.step(KEY('l1'), 'Figure', 2, 0);
    check('flag off: rewards still talk to api/progress.php (v1) and never to v2', t.net.log.some(l => l.url.includes('progress.php')) && !t.net.log.some(l => l.url.includes('v2/sync.php')) && (await t.sb.SBSync.pending()) === 0, t.net.log.map(l => l.url));
  }

  h.finish('rewards integration tests');
})().catch(e => { console.error(e); process.exit(2); });
