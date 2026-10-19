'use strict';
/* Integration: the real js/sb_rewards.js (inside the app sandbox, all 250 scripts loaded) with the real js/core/*
 * against the real PHP API on a scratch database.   node tests/sync/rewards.js */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
const { load } = require('../../tools/lib/app_sandbox');

const ROOT = path.resolve(__dirname, '..', '..');
const PHP = [process.env.PHP, 'php', 'C:/xampp/php/php.exe'].filter(Boolean).find(p => spawnSync(p, ['-v']).status === 0);
if (!PHP) { console.log('SKIP  no PHP found'); process.exit(0); }
let pass = 0, fail = 0;
const check = (label, cond, detail) => { if (cond) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

const cfg = path.join(os.tmpdir(), 'sb_rw_config_' + process.pid + '.php');
const mk = spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'create', cfg], { encoding: 'utf8' });
if (mk.status !== 0) { console.log('FAIL  cannot create the scratch database: ' + (mk.stderr || mk.stdout)); process.exit(1); }
const port = 19800 + (process.pid % 150);
const base = 'http://127.0.0.1:' + port + '/';
const server = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', path.join(ROOT, 'api')], { env: Object.assign({}, process.env, { SB_CONFIG: cfg }), stdio: 'ignore' });

async function api(p, body) {
  const res = await fetch(base + p, { method: body === undefined ? 'GET' : 'POST', headers: { 'Content-Type': 'application/json' }, body: body === undefined ? undefined : JSON.stringify(body) });
  return { status: res.status, json: await res.json().catch(() => null) };
}
let n = 0;
async function account() {
  n++;
  const r = await api('auth.php?action=register', { name: 'RW User', father_name: 'Father', user_type: 'student', whatsapp: '92300' + String(4000000 + n * 11 + process.pid % 7), password: 'secret123', want_device: true, device_name: 'node' });
  if (!r.json || !r.json.ok) throw new Error('register failed ' + JSON.stringify(r));
  return r.json;
}
const KEY = s => 'cls2|math|u0|trace|' + s + '|0';

// a fresh app: all scripts loaded; fetch goes to the real server (relative URLs resolved against it) or fails when `net.down`
function newApp(flagOn) {
  const net = { down: false, log: [], meUser: null };   // meUser: what auth.php?action=me answers (a real browser would hold the session cookie)
  const app = load({
    quiet: true,
    before(sb) {
      if (flagOn) sb.localStorage.setItem('sb_sync_v2', 'on');
      sb.navigator.onLine = true;
      sb.fetch = async (url, o) => {
        net.log.push({ url: String(url), method: (o && o.method) || 'GET' });
        if (net.down) throw new Error('network down');
        if (String(url).includes('auth.php?action=me')) return new Response(JSON.stringify({ ok: true, user: net.meUser }), { headers: { 'Content-Type': 'application/json' } });
        return fetch(String(url).startsWith('http') ? url : base + String(url).replace(/^\.?\/?(api\/)?/, ''), o);
      };
    },
  });
  const sb = app.sb;
  const signIn = async acct => {
    await sb.SBSync.ready;
    net.meUser = acct.user;
    await sb.SBSync.setDevice(acct.user.id, acct.device);
    sb.document.dispatchEvent(new sb.CustomEvent('spacebook:auth', { detail: { user: acct.user } }));
    await sb.SBRewards.ready;
    await sleep(300);                                   // the sign-in sync running in the background settles
  };
  return { app, sb, net, signIn };
}

(async () => {
  for (let i = 0; i < 60; i++) { try { await fetch(base + 'health.php'); break; } catch (e) { await sleep(100); } }
  console.log('--- sb_rewards.js with sync v2 ---');

  // 1. offline steps are kept, shown immediately, and delivered later
  {
    const a = await account(); const t = newApp(true);
    await t.signIn(a);
    check('signed in with the flag on: rewards use the account', t.sb.SBRewards.signedIn === true && t.sb.SBRewards.coins === 0);
    t.net.down = true; t.sb.navigator.onLine = false;
    const r1 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 0);
    const r2 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 1);
    const r3 = await t.sb.SBRewards.step(KEY('a1'), 'Figure', 3, 2);
    check('offline steps still earn at once (1 + 1 + 1 + 5 shown locally) and the student stays signed in', r1.ok && r1.earned === 1 && r2.earned === 1 && r3.earned === 6 && r3.completed === true && t.sb.SBRewards.coins === 8 && t.sb.SBRewards.signedIn === true, [r1, r2, r3]);
    check('the steps wait in the outbox, nothing was demoted to guest data', (await t.sb.SBSync.pending()) === 3 && (await t.sb.SBSync.pendingGuest()) === 0 && !t.sb.localStorage.getItem('sb_rewards_guest_v1'));
    check('the activity state shows the finished steps', JSON.stringify(t.sb.SBRewards.get(KEY('a1')).done) === '[0,1,2]' && t.sb.SBRewards.get(KEY('a1')).times === 1);
    t.net.down = false; t.sb.navigator.onLine = true;
    const s = await t.sb.SBSync.sync(); await sleep(150);     // the page re-derives its numbers after the pull
    check('back online the events are delivered and the server agrees (8 coins)', s.flush.accepted === 3 && t.sb.SBRewards.coins === 8 && (await t.sb.SBSync.pending()) === 0, { s: s.flush, coins: t.sb.SBRewards.coins });
    const server = await api('progress.php?action=get');       // no cookie: expect 401; the truth is read through a pull instead
    const t2 = newApp(true); await t2.signIn(a); await t2.sb.SBSync.sync(); await sleep(150);
    check('a second device (fresh page, same account) sees the same coins and steps', t2.sb.SBRewards.coins === 8 && JSON.stringify(t2.sb.SBRewards.get(KEY('a1')).done) === '[0,1,2]' && server.status === 401, t2.sb.SBRewards.coins);
  }

  // 2. a request that fails never changes who the student is
  {
    const a = await account(); const t = newApp(true);
    await t.signIn(a);
    t.net.down = true;
    await t.sb.SBRewards.step(KEY('b1'), 'Figure', 2, 0);
    const fl = await t.sb.SBSync.flush();
    check('a failed request leaves the student signed in with the step safe', fl.status === 'network-error' && t.sb.SBRewards.signedIn === true && (await t.sb.SBSync.pending()) === 1);
    t.net.down = false; t.sb.SBSync.flush;                       // (the back-off timer never fires in the sandbox: wait it out by hand)
    const st = await t.sb.SBSync.status();
    check('and the back-off is recorded', st.failures === 1 && st.signedIn);
  }

  // 3. progress made as a guest joins the account at sign-in
  {
    const a = await account(); const t = newApp(true);
    await t.sb.SBRewards.step(KEY('g1'), 'Figure', 2, 0);       // nobody is signed in yet
    await t.sb.SBRewards.step(KEY('g1'), 'Figure', 2, 1);
    check('as a guest the coins are kept on this device (1 + 1 + 5)', t.sb.SBRewards.coins === 7 && !!t.sb.localStorage.getItem('sb_rewards_guest_v1'));
    await t.signIn(a);
    check('on sign-in the local guest copy is removed and the coins are unchanged (7)', !t.sb.localStorage.getItem('sb_rewards_guest_v1') && t.sb.SBRewards.coins === 7, t.sb.SBRewards.coins);
    await t.sb.SBSync.sync(); await sleep(150);
    const t3 = newApp(true); await t3.signIn(a); await t3.sb.SBSync.sync(); await sleep(150);
    check('the account (seen from a fresh page) holds the guest steps: 7 coins, 2 steps', t3.sb.SBRewards.coins === 7 && JSON.stringify(t3.sb.SBRewards.get(KEY('g1')).done) === '[0,1]' && (await t.sb.SBSync.pending()) === 0, t3.sb.SBRewards.coins);
  }

  // 4. repeating a finished activity
  {
    const a = await account(); const t = newApp(true);
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
    const a = await account(); const t = newApp(false);
    await t.signIn(a);
    await t.sb.SBRewards.step(KEY('l1'), 'Figure', 2, 0);
    check('flag off: rewards still talk to api/progress.php (v1) and never to v2', t.net.log.some(l => l.url.includes('progress.php')) && !t.net.log.some(l => l.url.includes('v2/sync.php')) && (await t.sb.SBSync.pending()) === 0, t.net.log);
  }

  finish();
})().catch(e => { console.error(e); fail++; finish(); });

function finish() {
  try { server.kill(); } catch (e) { /* gone */ }
  spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'drop']);
  try { fs.unlinkSync(cfg); } catch (e) { /* gone */ }
  console.log('---\nrewards integration tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
}
