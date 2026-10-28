'use strict';
/* The DEFAULT unlock code of the free-trial lock (docs/TRIAL_LOCK.md): one code that the owner types on a device and that opens the lock for 30 days
 * from that moment (then the lock comes back and the code is typed again).
 *   node tools/license/make_default.js "THE CODE"            prints the salt, iterations and hash to paste into js/sb_license.js (CFG.defaultCode)
 *                                                             and the App's expiry/DefaultCode.kt (SALT, ITERATIONS, HASH)
 *   node tools/license/make_default.js --check "THE CODE"     does this code match the hash that is in both files now?
 * Only a salted PBKDF2-HMAC-SHA256 hash is stored in the repositories, never the code. Because the repositories are public, anyone can try to guess the
 * code offline against that hash: use a long, unusual code and do not use it anywhere else.
 * Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');

const ITERATIONS = 100000;
const args = process.argv.slice(2);
const check = args.includes('--check');
const code = args.filter(a => a !== '--check')[0];
if (!code) { console.error('Usage: node tools/license/make_default.js [--check] "THE CODE"'); process.exit(1); }
const derive = (c, salt, it) => crypto.pbkdf2Sync(Buffer.from(c, 'utf8'), salt, it, 32, 'sha256');

if (!check) {
  const salt = crypto.randomBytes(16);
  const hash = derive(code, salt, ITERATIONS);
  console.log('CFG.defaultCode in js/sb_license.js:\n  defaultCode: { salt: \'' + salt.toString('base64') + '\', iterations: ' + ITERATIONS + ', hash: \'' + hash.toString('base64') + '\' }');
  console.log('\nDefaultCode.kt (SALT, ITERATIONS, HASH):\n  SALT = "' + salt.toString('base64') + '"\n  ITERATIONS = ' + ITERATIONS + '\n  HASH = "' + hash.toString('base64') + '"');
  process.exit(0);
}

const ROOT = path.resolve(__dirname, '..', '..');
const js = fs.readFileSync(path.join(ROOT, 'js', 'sb_license.js'), 'utf8');
const m = /defaultCode:\s*\{\s*salt:\s*'([^']+)',\s*iterations:\s*(\d+),\s*hash:\s*'([^']+)'/.exec(js);
let ok = true;
if (!m) { console.log('js/sb_license.js: no defaultCode found'); ok = false; }
else { const good = derive(code, Buffer.from(m[1], 'base64'), +m[2]).equals(Buffer.from(m[3], 'base64')); console.log('js/sb_license.js      : ' + (good ? 'this code matches' : 'this code does NOT match')); ok = ok && good; }
const ktFile = path.resolve(ROOT, '..', 'SpaceBook App', 'app', 'src', 'main', 'java', 'pk', 'wantuch', 'spacebook', 'expiry', 'DefaultCode.kt');
if (fs.existsSync(ktFile)) {
  const kt = fs.readFileSync(ktFile, 'utf8');
  const s = /SALT = "([^"]+)"/.exec(kt), i = /ITERATIONS = (\d+)/.exec(kt), h = /HASH = "([^"]+)"/.exec(kt);
  if (!s || !i || !h) { console.log('DefaultCode.kt: SALT/ITERATIONS/HASH not found'); ok = false; }
  else { const good = derive(code, Buffer.from(s[1], 'base64'), +i[1]).equals(Buffer.from(h[1], 'base64')); console.log('DefaultCode.kt (app)  : ' + (good ? 'this code matches' : 'this code does NOT match')); ok = ok && good; }
} else console.log('DefaultCode.kt: the app folder is not next to this one, not checked');
process.exit(ok ? 0 : 1);
