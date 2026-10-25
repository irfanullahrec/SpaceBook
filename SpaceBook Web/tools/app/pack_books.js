'use strict';
/* Puts every book of the website INTO the Android app, so the app reads with no internet from the first start and shows exactly the books of
 * this checkout (not whatever the live website happens to hold):
 *     node tools/app/pack_books.js [--app "<folder of the app repo>"] [--check]
 *   (no flags)  copies every file content/offline_map.json lists (the lazy book files with their hash names, the search files and the
 *               pictures the chapters use) into <app>/app/src/main/assets/books/<same path>, and writes books/books-index.json
 *               {builtAt, files: {path: ?v hash}, assets: [paths]}. The app's SiteStore answers the WebView from there.
 *   --check     change nothing; exit 1 when the app's copy is missing, partial or differs from what the website produces now.
 * Run it after tools/build/all.js and tools/app/sync_app.js, from a clean checkout of the commit that is being released, and before the
 * app is built. About 420 MB of files that the build packs (deflated) into the APK, about 100 MB. The folder is NOT committed to the app's git
 * repository (it is in its .gitignore): it is made on the machine that builds the APK. Dev-only, never deployed. */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const bundle = require('./lib/bundle');

const ROOT = bundle.ROOT;
const args = process.argv.slice(2);
const flag = n => args.includes(n);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const APP = path.resolve(opt('--app') || path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets');
const BOOKS = path.join(ASSETS, 'books');
const CHECK = flag('--check');
if (!fs.existsSync(ASSETS)) { console.error('no app assets folder at ' + ASSETS + ' (use --app "<folder of the app repo>")'); process.exit(2); }

const map = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'offline_map.json'), 'utf8'));
const files = new Map();      // path -> {v, sha256}
const assets = new Set();
for (const s of Object.values(map.subjects || {})) {
  for (const f of s.files || []) {
    const m = map.files[f];
    if (m) files.set(f, { v: m.v || '', sha256: m.sha256 || '' });
  }
  for (const a of s.assets || []) assets.add(a);
}

const problems = [];
const plan = [];              // {rel, abs, sha256}
for (const [rel, m] of files) {
  const abs = path.join(ROOT, rel);
  if (!fs.existsSync(abs)) { problems.push('missing in the website: ' + rel); continue; }
  const buf = bundle.readServed(abs);
  const h = bundle.sha256(buf);
  if (m.sha256 && h !== m.sha256) { problems.push(`${rel} differs from content/offline_map.json (run node tools/build/all.js from a clean checkout)`); continue; }
  plan.push({ rel, buf, sha256: h });
}
for (const rel of assets) {
  const abs = path.join(ROOT, rel);
  if (!fs.existsSync(abs)) { problems.push('missing picture in the website: ' + rel); continue; }
  const buf = fs.readFileSync(abs);
  plan.push({ rel, buf, sha256: bundle.sha256(buf) });
}
if (problems.length) { console.error('the books are not consistent with the website:\n  ' + problems.slice(0, 15).join('\n  ') + (problems.length > 15 ? `\n  ... ${problems.length - 15} more` : '')); process.exit(1); }

if (CHECK) {
  const idxFile = path.join(BOOKS, 'books-index.json');
  if (!fs.existsSync(idxFile)) { console.error('the app carries no books (run node tools/app/pack_books.js)'); process.exit(1); }
  let missing = 0, changed = 0;
  for (const p of plan) {
    const f = path.join(BOOKS, p.rel);
    if (!fs.existsSync(f)) { missing++; continue; }
    if (bundle.sha256(fs.readFileSync(f)) !== p.sha256) changed++;
  }
  console.log(`app books: ${plan.length} files expected, ${missing} missing, ${changed} changed`);
  if (missing || changed) { console.error('the app\'s books are stale: run node tools/app/pack_books.js'); process.exit(1); }
  console.log('the app carries the books of this website');
  process.exit(0);
}

fs.rmSync(BOOKS, { recursive: true, force: true });
let bytes = 0;
for (const p of plan) {
  const to = path.join(BOOKS, p.rel);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.writeFileSync(to, p.buf);
  bytes += p.buf.length;
}
let rev = '';
try { rev = cp.spawnSync('git', ['rev-parse', 'HEAD'], { cwd: ROOT, encoding: 'utf8' }).stdout.trim(); } catch (e) { /* not a git checkout */ }
const index = { schema: 'spacebook.app-books/1', builtAt: Date.now(), source: rev, files: {}, assets: [...assets].sort() };
for (const [rel, m] of [...files].sort((a, b) => a[0].localeCompare(b[0]))) index.files[rel] = m.v;
fs.writeFileSync(path.join(BOOKS, 'books-index.json'), JSON.stringify(index));
console.log(`wrote ${plan.length} files (${(bytes / 1e6).toFixed(0)} MB) into ${BOOKS}; builtAt ${new Date(index.builtAt).toISOString()}, website commit ${rev.slice(0, 8) || 'unknown'}`);
