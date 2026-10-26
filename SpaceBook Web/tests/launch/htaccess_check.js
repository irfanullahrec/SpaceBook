'use strict';
/* The site's .htaccess on a real Apache 2.4 (XAMPP's, started on a spare port with this folder as the document root and AllowOverride All):
 *   the file parses (Apache answers instead of 500), the security headers are sent, hashed files are cached for a year, pages are always revalidated,
 *   images and fonts for a week, a backup / sql / log file is refused, no directory listing, the default page is lazy.html.
 *     node tests/launch/htaccess_check.js        (SKIPs when XAMPP's Apache is not installed: C:\xampp\apache\bin\httpd.exe, or HTTPD=<path>)
 * LiteSpeed (the live host) reads the same directives; this proves the syntax and the headers, not the host. Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path'), http = require('http');
const { spawn } = require('child_process');
const ROOT = path.resolve(__dirname, '..', '..');
const HTTPD = [process.env.HTTPD, 'C:/xampp/apache/bin/httpd.exe'].filter(Boolean).find(p => fs.existsSync(p));
if (!HTTPD) { console.log('SKIP  no Apache found (set HTTPD=<path to httpd.exe>)'); process.exit(0); }
const SR = path.resolve(path.dirname(HTTPD), '..').replace(/\\/g, '/');
const PORT = 8792;
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sb_htaccess_'));
const conf = path.join(tmp, 'httpd.conf');
const docroot = ROOT.replace(/\\/g, '/');
const mods = ['authz_core', 'dir', 'mime', 'log_config', 'alias', 'headers', 'rewrite', 'access_compat', 'authz_host', 'setenvif', 'env'];
fs.writeFileSync(conf, `ServerRoot "${SR}"
Listen 127.0.0.1:${PORT}
ServerName localhost
${mods.map(m => `LoadModule ${m}_module modules/mod_${m}.so`).join('\n')}
PidFile "${tmp.replace(/\\/g, '/')}/httpd.pid"
ErrorLog "${tmp.replace(/\\/g, '/')}/error.log"
LogLevel warn
TypesConfig "${SR}/conf/mime.types"
DocumentRoot "${docroot}"
<Directory "${docroot}">
  AllowOverride All
  Require all granted
</Directory>
`);
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const get = p => new Promise(res => http.get({ host: '127.0.0.1', port: PORT, path: p }, r => { r.resume(); r.on('end', () => res({ status: r.statusCode, h: r.headers })); }).on('error', e => res({ status: 0, h: {}, err: String(e) })));
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const srv = spawn(HTTPD, ['-f', conf, '-X'], { stdio: 'ignore' });
  let up = false;
  for (let i = 0; i < 60 && !up; i++) { await sleep(250); up = (await get('/')).status !== 0; }
  if (!up) { console.log('FAIL  Apache did not start: ' + (fs.existsSync(path.join(tmp, 'error.log')) ? fs.readFileSync(path.join(tmp, 'error.log'), 'utf8').slice(-500) : '')); process.exit(1); }
  const home = await get('/');
  check('the folder answers (the .htaccess parses: no 500)', home.status === 200 && /text\/html/.test(home.h['content-type'] || ''), home.status);
  check('the default page is lazy.html (the request for / is the lazy page, not a file list)', home.status === 200 && Number(home.h['content-length']) === fs.statSync(path.join(ROOT, 'lazy.html')).size, home.h['content-length']);
  check('X-Content-Type-Options: nosniff', home.h['x-content-type-options'] === 'nosniff');
  check('Referrer-Policy keeps the page and query to ourselves', home.h['referrer-policy'] === 'strict-origin-when-cross-origin');
  check('X-Frame-Options stops the site being framed by another page', /^(SAMEORIGIN|DENY)$/.test(home.h['x-frame-options'] || ''));
  check('Permissions-Policy switches off camera, microphone, location, payment', /camera=\(\)/.test(home.h['permissions-policy'] || '') && /microphone=\(\)/.test(home.h['permissions-policy'] || '') && /geolocation=\(\)/.test(home.h['permissions-policy'] || ''));
  check('Cross-Origin-Opener-Policy: same-origin', home.h['cross-origin-opener-policy'] === 'same-origin');
  check('the page itself is always revalidated (no-cache)', /no-cache/.test(home.h['cache-control'] || ''), home.h['cache-control']);
  const hashed = await get('/js/app.js?v=0123456789ab');
  check('a file requested with its content hash is cached for a year and immutable', /max-age=31536000/.test(hashed.h['cache-control'] || '') && /immutable/.test(hashed.h['cache-control'] || ''), hashed.h['cache-control']);
  const plain = await get('/js/app.js');
  check('the same file without the hash is revalidated every time', /no-cache/.test(plain.h['cache-control'] || '') && !/immutable/.test(plain.h['cache-control'] || ''), plain.h['cache-control']);
  const bad = await get('/js/app.js?v=notahash');
  check('a query that is not a content hash does not get the one-year rule', !/immutable/.test(bad.h['cache-control'] || ''), bad.h['cache-control']);
  const img = await get('/covers/Classes%20Cards/Another-Look/1.webp');
  check('images and fonts are kept for a week', /max-age=604800/.test(img.h['cache-control'] || '') && img.status === 200, img.h['cache-control']);
  const font = await get('/assets/fonts/NotoNastaliqUrdu-400.woff2');
  check('the bundled fonts are served and kept for a week', font.status === 200 && /max-age=604800/.test(font.h['cache-control'] || ''), font.h['cache-control']);
  // a stray backup must not be readable
  const strays = ['stray_test.sql', 'stray_test.bak', 'stray_test.log', 'stray_test~'];
  for (const f of strays) fs.writeFileSync(path.join(ROOT, f), 'secret');
  const refused = await Promise.all(strays.map(f => get('/' + encodeURIComponent(f))));
  for (const f of strays) fs.unlinkSync(path.join(ROOT, f));
  check('a .sql, .bak, .log or ~ file is refused (403)', refused.every(r => r.status === 403), refused.map(r => r.status));
  const dir = await get('/css/');
  check('a folder without an index shows no file list', dir.status === 403 || dir.status === 404, dir.status);
  const api = await get('/api/lib/feedback.php');
  check('the api/lib folder stays closed (its own .htaccess)', api.status === 403 || api.status === 404, api.status);
  srv.kill();
  await sleep(500);
  try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) { /* locked until Apache is gone */ }
  console.log('---\nhtaccess test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
