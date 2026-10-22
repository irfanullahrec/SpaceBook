'use strict';
/* Copies the website's start-up files (the "shell") into the Android app, so the app opens and shows its pages with no network.
 *   node tools/app/pack_shell.js "<repo>/SpaceBook App/app/src/main/assets"
 * Writes <out>/site/:
 *   lazy.html and every file listed in content/sw_version.js `shell` (scripts, stylesheets, KaTeX fonts, icons), at the same relative path
 *   content/offline_map.json, content/lazy_manifest.json, content/search/index.json   (what "Download books" and the search need)
 *   site-index.json   {"schema": "spacebook.app-shell/1", "files": {"js/app.js": "5e4a1a6cdbf0", "lazy.html": "", ...}}
 *                     the ?v= hash each bundled file belongs to ("" = none): the app serves a bundled file only for that hash
 * The book data (about 390 MB) is NOT copied: the app downloads it per class (offline_map.json lists every file with its hash).
 * Run after tools/build/all.js, from a clean checkout of what is being released. Dev-only (not deployed). */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..');
const OUT = process.argv[2] ? path.join(path.resolve(process.argv[2]), 'site') : null;
if (!OUT) { console.error('usage: node tools/app/pack_shell.js <assets dir>'); process.exit(2); }

const ctx = { self: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'content', 'sw_version.js'), 'utf8'), ctx);
const sw = ctx.self.SB_SW;
if (!sw || !Array.isArray(sw.shell)) throw new Error('content/sw_version.js has no shell list');

fs.rmSync(OUT, { recursive: true, force: true });
const index = { schema: 'spacebook.app-shell/1', files: {} };
let bytes = 0, count = 0;

function put(entry) {
  const [rel, query] = entry.split('?');
  const v = /^v=([0-9a-f]+)$/.exec(query || '') ? RegExp.$1 : '';
  const from = path.join(ROOT, rel), to = path.join(OUT, rel);
  if (!fs.existsSync(from)) throw new Error('shell file missing: ' + rel);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(from, to);
  index.files[rel] = v;
  bytes += fs.statSync(from).size; count++;
}

// the lazy page (its own script tags carry the ?v= hashes) and the logo it shows at start
['lazy.html', 'logo_tuitionhub_trans.png'].forEach(put);
sw.shell.forEach(put);
['content/offline_map.json', 'content/lazy_manifest.json', 'content/search/index.json'].forEach(put);

fs.writeFileSync(path.join(OUT, 'site-index.json'), JSON.stringify(index));
console.log(`shell: ${count} files, ${(bytes / 1e6).toFixed(1)} MB -> ${OUT}`);
