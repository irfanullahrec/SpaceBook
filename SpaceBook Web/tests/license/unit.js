'use strict';
/* The free-trial lock core (js/sb_license.js) and the code tool (tools/license/make_code.js), no browser:
 *   node tests/license/unit.js
 * A throw-away key pair is made here; the real private key is never read. The real PUBLIC key is checked only for being a valid key.
 * Dev-only, never shipped. */
const crypto = require('crypto'), fs = require('fs'), os = require('os'), path = require('path'), { spawnSync } = require('child_process');
const L = require('../../js/sb_license.js');

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };

const b64u = b => Buffer.from(b).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const kp = () => { const k = crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' }); return { priv: k.privateKey, spki: k.publicKey.export({ type: 'spki', format: 'der' }).toString('base64') }; };
const sign = (priv, payload) => 'SB1-' + b64u(Buffer.from(payload)) + '.' + b64u(crypto.sign('sha256', Buffer.from(payload), { key: priv, dsaEncoding: 'ieee-p1363' }));
const DAY = L.DAY, NOW = Date.UTC(2026, 9, 28, 12, 0, 0);

(async () => {
  const A = kp(), B = kp();
  const DEV = 'ABCD-2345';

  // ---- codes
  let r = await L.verifyCode(sign(A.priv, 'SB1|' + DEV + '|0'), DEV, NOW, A.spki);
  check('a code for this device with no end date is accepted', r.ok === true, r);
  r = await L.verifyCode(sign(A.priv, 'SB1|' + DEV + '|0'), 'WXYZ-9876', NOW, A.spki);
  check('the same code on another device is refused (reason: device)', !r.ok && r.reason === 'device', r);
  r = await L.verifyCode(sign(A.priv, 'SB1|*|0'), 'WXYZ-9876', NOW, A.spki);
  check('a code for every device ("*") works on any device', r.ok === true, r);
  r = await L.verifyCode(sign(A.priv, 'SB1|' + DEV + '|0'), DEV, NOW, B.spki);
  check('a code signed with a different key is refused (reason: signature)', !r.ok && r.reason === 'signature', r);
  const good = sign(A.priv, 'SB1|' + DEV + '|0');
  const tampered = 'SB1-' + b64u(Buffer.from('SB1|WXYZ-9876|0')) + '.' + good.split('.')[1];
  r = await L.verifyCode(tampered, 'WXYZ-9876', NOW, A.spki);
  check('changing the device inside a code breaks the signature', !r.ok && r.reason === 'signature', r);
  const lastMs = Date.UTC(2026, 9, 28, 23, 59, 59, 999);
  r = await L.verifyCode(sign(A.priv, 'SB1|' + DEV + '|20261028'), DEV, lastMs, A.spki);
  check('a code with an end date works until the last millisecond of that day (UTC)', r.ok === true, r);
  r = await L.verifyCode(sign(A.priv, 'SB1|' + DEV + '|20261028'), DEV, lastMs + 1, A.spki);
  check('...and is refused one millisecond later (reason: expired)', !r.ok && r.reason === 'expired', r);
  for (const [name, code] of [['empty', ''], ['plain text', 'hello'], ['wrong prefix', 'SB2-' + good.slice(4)], ['no signature', good.split('.')[0]], ['short signature', good.split('.')[0] + '.AAAA'], ['bad device text', sign(A.priv, 'SB1|abcd|0')]]) {
    r = await L.verifyCode(code, DEV, NOW, A.spki);
    check('not a code: ' + name, !r.ok && r.reason === 'format', r);
  }
  r = await L.verifyCode('  ' + good.slice(0, 20) + '\r\n  ' + good.slice(20) + ' ‎', DEV, NOW, A.spki);
  check('spaces, line breaks and invisible marks from WhatsApp are ignored', r.ok === true, r);

  // ---- the trial clock
  const rec = { start: NOW };
  const st = (days, ms = 0) => L.decide(rec, NOW + days * DAY + ms, false, 30);
  check('day 0: trial, 30 days left', st(0).kind === 'trial' && st(0).daysLeft === 30, st(0));
  check('day 29: trial, 1 day left', st(29).kind === 'trial' && st(29).daysLeft === 1, st(29));
  check('day 29 and 23 hours: still trial, 1 day left', st(29, 23 * 3600000).kind === 'trial' && st(29, 23 * 3600000).daysLeft === 1, st(29, 23 * 3600000));
  check('day 30 exactly: locked', st(30).kind === 'locked', st(30));
  check('day 400: locked', st(400).kind === 'locked', st(400));
  check('a valid code keeps it open after the trial', L.decide(rec, NOW + 400 * DAY, true, 30).kind === 'open');
  check('trialDays = 0 switches the lock off', L.decide(rec, NOW + 400 * DAY, false, 0).kind === 'open');

  // ---- the default unlock code (a salted hash; typing it opens the lock for 30 days from that moment)
  const salt = crypto.randomBytes(16);
  const spec = { salt: salt.toString('base64'), iterations: 100000, hash: crypto.pbkdf2Sync(Buffer.from('Test@Default-1', 'utf8'), salt, 100000, 32, 'sha256').toString('base64') };
  check('default code: the right text matches its hash', await L.checkDefault('Test@Default-1', spec) === true);
  check('default code: a wrong text, a different case and an empty text do not', !(await L.checkDefault('Test@Default-2', spec)) && !(await L.checkDefault('test@default-1', spec)) && !(await L.checkDefault('', spec)));
  check('default code: trimCode drops the spaces and invisible marks around it, and only those', L.trimCode(' \r\n Test@Default-1 ‎') === 'Test@Default-1' && L.trimCode('a b') === 'a b');
  const rec2 = { start: NOW, extendUntil: NOW + 60 * DAY };
  check('default code: the end moves to the day it opened (day 45: 15 days left)', L.decide(rec2, NOW + 45 * DAY, false, 30).daysLeft === 15, L.decide(rec2, NOW + 45 * DAY, false, 30));
  check('default code: ...and the lock is back when that month is over (day 60)', L.decide(rec2, NOW + 60 * DAY, false, 30).kind === 'locked');
  const real = L.CFG.defaultCode;
  check('default code: the one in js/sb_license.js is a 16-byte salt, a 32-byte hash and at least 100000 rounds (the code itself is not in the file)',
    real && Buffer.from(real.salt, 'base64').length === 16 && Buffer.from(real.hash, 'base64').length === 32 && real.iterations >= 100000 && L.CFG.grantDays === 30, real);

  // ---- device IDs
  const ids = new Set();
  for (let i = 0; i < 500; i++) ids.add(L.newDeviceId());
  check('500 device IDs: all in the ABCD-EFGH shape, no 0 O 1 I, no repeats', [...ids].every(x => /^[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$/.test(x)) && ids.size === 500);
  check('normalizeDevice: "abcd 2345" -> ABCD-2345', L.normalizeDevice('abcd 2345') === 'ABCD-2345' && L.normalizeDevice('abc') === '');

  // ---- the contact details
  check('the contact is 0343 0155606 on WhatsApp 923430155606', L.CFG.contactLocal === '0343 0155606' && L.CFG.contactWa === '923430155606', L.CFG);
  check('the trial is 30 days', L.CFG.trialDays === 30, L.CFG.trialDays);

  // ---- the real public key is a usable key; the tool and the page agree
  try {
    const k = await crypto.webcrypto.subtle.importKey('spki', Buffer.from(L.CFG.publicKey, 'base64'), { name: 'ECDSA', namedCurve: 'P-256' }, false, ['verify']);
    check('the public key in js/sb_license.js is a valid ECDSA P-256 key', !!k);
  } catch (e) { check('the public key in js/sb_license.js is a valid ECDSA P-256 key', false, String(e)); }

  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sblic-')), keyFile = path.join(tmp, 'k.pem');
  const tool = (...a) => spawnSync(process.execPath, [path.join(__dirname, '..', '..', 'tools', 'license', 'make_code.js'), ...a, '--key', keyFile], { encoding: 'utf8' });
  const init = tool('--init');
  check('make_code.js --init writes a key file', init.status === 0 && fs.existsSync(keyFile), init.stderr);
  const pub = tool('--public').stdout.trim();
  const made = tool('abcd-2345', '--days', '10').stdout.trim();
  r = await L.verifyCode(made, DEV, Date.now(), pub);
  check('a code made by tools/license/make_code.js is accepted by js/sb_license.js', r.ok === true, { made: made.slice(0, 30), r });
  r = await L.verifyCode(made, DEV, Date.now() + 11 * DAY, pub);
  check('...and its --days 10 end date is respected (11 days later: expired)', !r.ok && r.reason === 'expired', r);
  const dtool = spawnSync(process.execPath, [path.join(__dirname, '..', '..', 'tools', 'license', 'make_default.js'), 'Other@Code-77'], { encoding: 'utf8' });
  const dm = /salt: '([^']+)', iterations: (\d+), hash: '([^']+)'/.exec(dtool.stdout);
  check('tools/license/make_default.js prints a salt, iterations and hash that js/sb_license.js accepts for that code only',
    !!dm && await L.checkDefault('Other@Code-77', { salt: dm[1], iterations: +dm[2], hash: dm[3] }) && !(await L.checkDefault('Other@Code-78', { salt: dm[1], iterations: +dm[2], hash: dm[3] })), dtool.stdout.slice(0, 200));
  const any = tool('--any').stdout.trim();
  r = await L.verifyCode(any, 'QQQQ-2222', Date.now(), pub);
  check('make_code.js --any makes a code for every device', r.ok === true, r);
  check('make_code.js --verify reads a code back', /valid signature: device ABCD-2345/.test(tool('--verify', made).stdout), tool('--verify', made).stdout);
  check('make_code.js refuses a device ID that is not 8 letters/digits', tool('abc').status !== 0);
  check('make_code.js --init does not overwrite an existing key', /already exists/.test(tool('--init').stdout));
  fs.rmSync(tmp, { recursive: true, force: true });

  console.log('---\ntrial lock unit test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
