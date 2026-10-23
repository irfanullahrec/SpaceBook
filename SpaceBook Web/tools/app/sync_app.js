'use strict';
/* One command that brings everything the Android app bundles up to date with this website, so the two cannot drift apart:
 *     node tools/app/sync_app.js [--app "<folder of the app repo>"] [--check] [--covers] [--allow-dirty]
 *   (no flags)   rewrite the app's generated assets: the shell (site/), the catalog, the offline question bank, the list of tests,
 *                sync_manifest.json; with --covers also the book covers (needs Python and Pillow)
 *   --check      change nothing; exit 1 and list what is stale (what the app holds is not what the website would produce now)
 *   --allow-dirty  write even when a shell file differs from the last commit (never for a release: the app must match what is deployed)
 * Default app folder: ../SpaceBook App next to this website's folder. Run it after tools/build/all.js, from a clean checkout of the commit
 * that is being released. Files under the app's assets that are generated are never edited by hand; see tools/app/lib/bundle.js for the list.
 * Dev-only, never deployed. */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const bundle = require('./lib/bundle');

const ROOT = bundle.ROOT;
const args = process.argv.slice(2);
const flag = n => args.includes(n);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const APP = path.resolve(opt('--app') || path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets');
const TEST_RES = path.join(APP, 'app', 'src', 'test', 'resources');
const CHECK = flag('--check');

function fail(msg) { console.error(msg); process.exit(1); }
if (!fs.existsSync(ASSETS)) { console.error('no app assets folder at ' + ASSETS + ' (use --app "<folder of the app repo>")'); process.exit(2); }

// 1. the website's own generated files must be fresh, or the app would copy a stale shell
const run = (script, extra) => cp.spawnSync(process.execPath, ['--max-old-space-size=6144', path.join(ROOT, script)].concat(extra || []), { cwd: ROOT, encoding: 'utf8' });
const cat = run('tools/build/make_app_catalog.js', ['--check']);
if (cat.status !== 0) fail('content/app_catalog.json is stale: run node tools/build/make_app_catalog.js (after tools/build/all.js)\n' + (cat.stderr || cat.stdout));
const lazy = run('tools/build/make_lazy.js', ['--check']);
if (lazy.status !== 0) fail('lazy.html / content/lazy_manifest.json are stale against index.html: run node tools/build/all.js from a clean checkout\n' + (lazy.stderr || lazy.stdout).slice(0, 600));

const planned = bundle.plan();
if (planned.problems.length) fail('the shell is not consistent with the website:\n  ' + planned.problems.join('\n  '));

// 2. the app must carry what is committed, not what happens to lie in a working folder
if (!flag('--allow-dirty') && !CHECK) {
  const touched = [...planned.files.values()].filter(f => f.from).map(f => path.relative(ROOT, f.from).replace(/\\/g, '/'));
  const st = cp.spawnSync('git', ['status', '--porcelain', '--'].concat(touched), { cwd: ROOT, encoding: 'utf8' });
  const dirty = (st.stdout || '').split('\n').filter(Boolean);
  if (dirty.length) fail('these shell files differ from the last commit, so the app would not match what is deployed (commit them, or use --allow-dirty to try):\n  ' + dirty.slice(0, 15).join('\n  '));
}

// 3. compare / write
const d = bundle.diff(planned, ASSETS, TEST_RES);
const stale = d.missing.length + d.changed.length + d.extra.length;
const report = () => {
  console.log(`app assets: ${d.missing.length} missing, ${d.changed.length} changed, ${d.extra.length} leftover`);
  d.missing.slice(0, 12).forEach(x => console.log('  missing   ' + x));
  d.changed.slice(0, 12).forEach(x => console.log('  changed   ' + x));
  d.extra.slice(0, 12).forEach(x => console.log('  leftover  ' + x));
};

if (CHECK) {
  report();
  if (flag('--covers')) { const c = coversStatus(); if (c) { console.log(c); process.exitCode = 1; } }
  if (stale) { console.error('the app is stale: run node tools/app/sync_app.js'); process.exit(1); }
  console.log('the app matches the website (' + planned.files.size + ' generated files, service worker ' + planned.sw.version + ')');
  process.exit(process.exitCode || 0);
}

fs.rmSync(path.join(ASSETS, 'site'), { recursive: true, force: true });
let bytes = 0;
for (const [rel, f] of planned.files) {
  const to = path.join(ASSETS, rel);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  const buf = bundle.bytesOf(f);
  fs.writeFileSync(to, buf);
  bytes += buf.length;
}
for (const [rel, f] of planned.tests) {
  const to = path.join(TEST_RES, rel);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.writeFileSync(to, f.bytes);
}
console.log(`wrote ${planned.files.size} files (${(bytes / 1e6).toFixed(1)} MB) into ${ASSETS}; ${stale} of them were stale`);
console.log(`  question bank: ${planned.mcq.kept} of ${planned.mcq.total} questions   tests: ${planned.prep.tests.length}   service worker ${planned.sw.version}`);

if (flag('--covers')) {
  const py = cp.spawnSync(process.env.PYTHON || 'python', [path.join(ROOT, 'tools', 'app', 'make_app_covers.py'), ASSETS], { encoding: 'utf8' });
  if (py.status !== 0) fail('make_app_covers.py failed: ' + (py.stderr || py.stdout));
  console.log(py.stdout.trim());
}

// covers are compared by name only: the image encoder differs between machines
function coversStatus() {
  const src = fs.readFileSync(path.join(ROOT, 'js', 'app.js'), 'utf8');
  const m = /const coverPageMap = \{([\s\S]*?)\n  \};/.exec(src);
  if (!m) return 'coverPageMap not found in js/app.js';
  const want = new Set();
  for (const x of m[1].matchAll(/"([^"]+)"\s*:\s*"([^"]+)"/g)) if (fs.existsSync(path.join(ROOT, 'covers', x[2]))) want.add(x[1] + '.webp');
  for (let n = 1; n <= 12; n++) if (fs.existsSync(path.join(ROOT, 'covers', 'Classes Cards', 'Another-Look', n + '.png'))) want.add('class-cls' + n + '.webp');
  const dir = path.join(ASSETS, 'covers');
  const have = new Set(fs.existsSync(dir) ? fs.readdirSync(dir) : []);
  const missing = [...want].filter(x => !have.has(x)), extra = [...have].filter(x => !want.has(x));
  return missing.length || extra.length ? `covers: ${missing.length} missing (${missing.slice(0, 5).join(', ')}), ${extra.length} not in the website's coverPageMap (${extra.slice(0, 5).join(', ')})` : null;
}
