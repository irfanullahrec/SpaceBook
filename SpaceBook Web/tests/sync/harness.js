'use strict';
/* Shared scaffolding for the integration tests (tests/sync/rewards.js, planner.js, ...):
 *   const h = await harness.start();            scratch MySQL database + PHP built-in server on api/
 *   const acct = await h.account();             registered student with a device token
 *   const t = h.newApp({flag: true});           the whole app loaded in the sandbox; fetch goes to the real server
 *   await t.signIn(acct);                       dispatches spacebook:auth like auth.js does
 *   h.check(label, cond, detail); h.finish();   */
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
const { load } = require('../../tools/lib/app_sandbox');

const ROOT = path.resolve(__dirname, '..', '..');
const PHP = [process.env.PHP, 'php', 'C:/xampp/php/php.exe'].filter(Boolean).find(p => spawnSync(p, ['-v']).status === 0);
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function start() {
  if (!PHP) { console.log('SKIP  no PHP found'); process.exit(0); }
  const cfg = path.join(os.tmpdir(), 'sb_h_config_' + process.pid + '.php');
  const mk = spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'create', cfg], { encoding: 'utf8' });
  if (mk.status !== 0) { console.log('FAIL  cannot create the scratch database: ' + (mk.stderr || mk.stdout)); process.exit(1); }
  const port = 19200 + (process.pid % 600);
  const base = 'http://127.0.0.1:' + port + '/';
  const server = spawn(PHP, ['-S', '127.0.0.1:' + port, '-t', path.join(ROOT, 'api')], { env: Object.assign({}, process.env, { SB_CONFIG: cfg }), stdio: 'ignore' });
  for (let i = 0; i < 60; i++) { try { await fetch(base + 'health.php'); break; } catch (e) { await sleep(100); } }

  let pass = 0, fail = 0, n = 0;
  const h = {
    base, sleep,
    check(label, cond, detail) { if (cond) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } },
    async api(p, body, headers) {
      const res = await fetch(base + p, { method: body === undefined ? 'GET' : 'POST', headers: Object.assign({ 'Content-Type': 'application/json' }, headers || {}), body: body === undefined ? undefined : JSON.stringify(body) });
      return { status: res.status, json: await res.json().catch(() => null) };
    },
    async account() {
      n++;
      const r = await h.api('auth.php?action=register', { name: 'H User', father_name: 'Father', user_type: 'student', whatsapp: '92300' + String(5000000 + n * 13 + process.pid % 11), password: 'secret123', want_device: true, device_name: 'node' });
      if (!r.json || !r.json.ok) throw new Error('register failed ' + JSON.stringify(r));
      return r.json;
    },
    async secondDevice(acct) {
      const r = await h.api('auth.php?action=login', { whatsapp: acct.user.whatsapp, password: 'secret123', want_device: true, device_name: 'second' });
      return r.json.device;
    },
    // a fresh page: all scripts loaded; `flag` turns sync v2 on; the network can be switched off with net.down
    newApp(opts) {
      opts = opts || {};
      const net = { down: false, log: [], meUser: opts.me || null };   // opts.me: the user auth.php?action=me reports from the start (a signed-in page after a reload)   // meUser: what auth.php?action=me answers (a real browser holds the session cookie)
      const app = load({
        quiet: true,
        before(sb) {
          if (opts.flag) sb.localStorage.setItem('sb_sync_v2', 'on');
          if (opts.storage) Object.keys(opts.storage).forEach(k => sb.localStorage.setItem(k, opts.storage[k]));
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
      if (opts.bank) app.run(fs.readFileSync(path.join(ROOT, 'js', 'test_prep_bank.js'), 'utf8'), 60000);   // the page loads it lazily with a script tag
      return {
        app, sb, net,
        async signIn(acct, dev) {
          await sb.SBSync.ready;
          net.meUser = acct.user;
          await sb.SBSync.setDevice(acct.user.id, dev || acct.device);
          sb.document.dispatchEvent(new sb.CustomEvent('spacebook:auth', { detail: { user: acct.user } }));
          await sleep(400);                                 // background sync started by the modules settles
          if (opts.flag) { await sb.SBSync.sync(); await sleep(250); }   // stands in for the retry timer, which never fires in the sandbox
        },
        offline() { net.down = true; sb.navigator.onLine = false; },
        online() { net.down = false; sb.navigator.onLine = true; },
      };
    },
    finish(name) {
      try { server.kill(); } catch (e) { /* gone */ }
      spawnSync(PHP, [path.join(ROOT, 'tests', 'sync', 'db.php'), 'drop']);
      try { fs.unlinkSync(cfg); } catch (e) { /* gone */ }
      console.log('---\n' + name + ': ' + pass + ' passed, ' + fail + ' failed');
      process.exit(fail ? 1 : 0);
    },
  };
  return h;
}

module.exports = { start, sleep, ROOT };
