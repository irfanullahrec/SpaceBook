'use strict';
/* Issues and checks the unlock codes of the 1-month free-trial lock (docs/TRIAL_LOCK.md).
 *   node tools/license/make_code.js --init                          make the signing key pair once (the private key stays on this PC, never in git)
 *   node tools/license/make_code.js ABCD-EFGH                       code for the device whose lock screen shows ABCD-EFGH, for good
 *   node tools/license/make_code.js ABCD-EFGH --days 365            ... valid for 365 days from today (UTC)
 *   node tools/license/make_code.js ABCD-EFGH --until 2027-12-31    ... valid up to the end of that day (UTC)
 *   node tools/license/make_code.js --any [--days N]                a code for every device: whoever has it can use it, keep it private
 *   node tools/license/make_code.js --verify CODE [--device ABCD-EFGH]
 * Options: --key FILE   the private key (default: env SPACEBOOK_LICENSE_KEY, else ~/SpaceBook-License/private_key.pem)
 * Code = "SB1-" + base64url("SB1|<device or *>|<YYYYMMDD or 0>") + "." + base64url(ECDSA P-256 / SHA-256 signature, 64 bytes r||s).
 * The website (js/sb_license.js) and the app (expiry/LicenseCode.kt) hold only the PUBLIC key, so a code cannot be made without the private key.
 * Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path'), crypto = require('crypto');

const args = process.argv.slice(2);
const flag = n => args.includes(n);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const KEY_FILE = opt('--key') || process.env.SPACEBOOK_LICENSE_KEY || path.join(os.homedir(), 'SpaceBook-License', 'private_key.pem');
const ALPHABET = /^[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{8}$/;

const b64u = buf => Buffer.from(buf).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64u = s => Buffer.from(s.replace(/-/g, '+').replace(/_/g, '/'), 'base64');
const die = m => { console.error(m); process.exit(1); };

function device(s) {
  const d = String(s || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
  if (!ALPHABET.test(d)) die('The device ID must be 8 letters/digits as shown on the lock screen (for example ABCD-EFGH): "' + s + '"');
  return d.slice(0, 4) + '-' + d.slice(4);
}
const ymd = d => d.toISOString().slice(0, 10).replace(/-/g, '');
function until() {
  if (opt('--until')) { const m = /^(\d{4})-?(\d{2})-?(\d{2})$/.exec(opt('--until')); if (!m) die('--until needs YYYY-MM-DD'); return m[1] + m[2] + m[3]; }
  if (opt('--days')) { const n = parseInt(opt('--days'), 10); if (!(n > 0)) die('--days needs a number above 0'); return ymd(new Date(Date.now() + n * 86400000)); }
  return '0';
}
const privateKey = () => { if (!fs.existsSync(KEY_FILE)) die('No private key at ' + KEY_FILE + '\nMake one with:  node tools/license/make_code.js --init'); return crypto.createPrivateKey(fs.readFileSync(KEY_FILE)); };
const publicSpki = priv => crypto.createPublicKey(priv).export({ type: 'spki', format: 'der' }).toString('base64');

function make(dev, until_) {
  const payload = 'SB1|' + dev + '|' + until_;
  const sig = crypto.sign('sha256', Buffer.from(payload, 'utf8'), { key: privateKey(), dsaEncoding: 'ieee-p1363' });
  return 'SB1-' + b64u(Buffer.from(payload, 'utf8')) + '.' + b64u(sig);
}

function verify(code, dev) {
  const m = /^SB1-([A-Za-z0-9_-]+)\.([A-Za-z0-9_-]+)$/.exec(String(code).replace(/\s+/g, ''));
  if (!m) return 'not a SpaceBook code';
  const payload = unb64u(m[1]).toString('utf8'), sig = unb64u(m[2]);
  const ok = crypto.verify('sha256', Buffer.from(payload, 'utf8'), { key: crypto.createPublicKey(privateKey()), dsaEncoding: 'ieee-p1363' }, sig);
  if (!ok) return 'the signature is NOT valid (not made with this key)';
  const p = payload.split('|');
  const who = p[1] === '*' ? 'every device' : 'device ' + p[1];
  const end = p[2] === '0' ? 'no end date' : 'until the end of ' + p[2].replace(/(\d{4})(\d{2})(\d{2})/, '$1-$2-$3') + ' (UTC)';
  const wrong = dev && p[1] !== '*' && p[1] !== device(dev) ? '  <- this is NOT the device you asked about' : '';
  return 'valid signature: ' + who + ', ' + end + wrong;
}

if (flag('--init')) {
  if (fs.existsSync(KEY_FILE)) { console.log('A private key already exists at ' + KEY_FILE + ' (not touched).\nPublic key: ' + publicSpki(privateKey())); process.exit(0); }
  const { privateKey: priv } = crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' });
  fs.mkdirSync(path.dirname(KEY_FILE), { recursive: true });
  fs.writeFileSync(KEY_FILE, priv.export({ type: 'pkcs8', format: 'pem' }), { mode: 0o600 });
  console.log('Private key written to ' + KEY_FILE + '\nKeep it secret and back it up; without it no code can be made. It must never be committed or put in a zip you share.\nPublic key (paste into js/sb_license.js PUBLIC_KEY and the App\'s expiry/LicenseCode.kt PUBLIC_KEY):\n' + publicSpki(priv));
  process.exit(0);
}
if (flag('--verify')) { console.log(verify(opt('--verify'), opt('--device'))); process.exit(0); }
if (flag('--public')) { console.log(publicSpki(privateKey())); process.exit(0); }
const target = flag('--any') ? '*' : (args.find(a => !a.startsWith('--') && a !== opt('--days') && a !== opt('--until') && a !== opt('--key') && a !== opt('--device')) || '');
if (!target) die('Usage: node tools/license/make_code.js ABCD-EFGH [--days N | --until YYYY-MM-DD]   (see the top of this file)');
const code = make(target === '*' ? '*' : device(target), until());
console.log(code);
console.error('\n' + verify(code));
