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

// Files that scripts load ON DEMAND, under a fixed ?v= that is not a content hash (sb_bise.js, sb_page_tabs.js, word_stats.js, test_prep.js ...) or under
// another file's hash (the Maths readers ask for their solutions with their own ?v=). They are in no offline map and no shell list, so a fresh install had to
// fetch them from the network the first time (Ans of Maths, Word Stats, Tests Preps, the Board SLO bar) and, with no network, the app covered the reader with
// "not on this phone yet" (found on a fresh install of the app, X-08). They are packed with an empty version: the app's SiteStore serves such an entry for
// whatever ?v= the page asks for.
const ON_DEMAND = ['js/word_stats_words.js', 'js/test_prep_bank.js', 'js/bise_swat_data.js',
  'js/math_5_solutions.js', 'js/math_6_solutions.js', 'js/math_7_solutions.js', 'js/math_8_solutions.js', 'js/math_11_solutions.js'];
for (const rel of ON_DEMAND) if (!files.has(rel)) files.set(rel, { v: '', sha256: '' });

const problems = [];
// a script or style that another script names but lazy.html does not, and that the app does not carry, would need the network on a fresh install: name it above
{
  const lazyHtml = fs.readFileSync(path.join(ROOT, 'lazy.html'), 'utf8');
  const shellPaths = new Set(bundle.swVersion().shell.map(e => e.split('?')[0]));
  const names = [];
  for (const d of ['js', 'js/core', 'css']) for (const f of fs.readdirSync(path.join(ROOT, d))) if (/\.(js|css)$/.test(f)) names.push(d + '/' + f);
  const sources = names.filter(n => n.endsWith('.js')).map(n => [n, fs.readFileSync(path.join(ROOT, n), 'utf8')]);
  for (const rel of names) {
    const base = path.basename(rel);
    if (files.has(rel) || shellPaths.has(rel) || lazyHtml.includes(base)) continue;
    const by = sources.find(([n, text]) => n !== rel && text.includes(base));
    if (by) problems.push(`${rel} is named by ${by[0]} but is in no shell list or offline map: add it to ON_DEMAND in tools/app/pack_books.js (or the app needs the network the first time it is used)`);
  }
}
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
