'use strict';
/* Copies rebuilt page books into THIS checkout's js/ and bumps their ?v= in this checkout's index.html.
 *   node tools/launch/wire_here.js <version> <class> KEY [KEY ...]       e.g.  node tools/launch/wire_here.js 20261027_ans1 11 isl hpe cs
 * The file is the only *_book.js in docs/source-verification/class-<class>/KEY/build/ (written by tools/build_book11.py / build_book12.py; Class 12 names differ from the key,
 * e.g. islopt -> islamiat_ikhtiari_12_book.js).
 * Why this exists: docs/source-verification/class-12/tools/wire_book11.py has the path D:\SpaceBook\SpaceBook Web written into it (biology_tools.ROOT), so run from
 * another checkout or worktree it changes the MAIN checkout instead. This one only ever touches the checkout it lives in. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const [ver, cls, ...keys] = process.argv.slice(2);
if (!ver || !cls || !keys.length) { console.error('usage: wire_here.js <version> <class 11|12> KEY...'); process.exit(2); }
let html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
for (const k of keys) {
  const bdir = path.join(ROOT, 'docs', 'source-verification', 'class-' + cls, k, 'build');
  const found = fs.existsSync(bdir) ? fs.readdirSync(bdir).filter(f => /_book\.js$/.test(f)) : [];
  if (found.length !== 1) { console.error('expected one *_book.js in ' + bdir + ', found ' + found.length); process.exit(1); }
  const name = found[0];
  const src = path.join(bdir, name);
  fs.copyFileSync(src, path.join(ROOT, 'js', name));
  const rx = new RegExp('(js/' + name.replace(/[.]/g, '\\.') + '\\?v=)[0-9A-Za-z_]+');
  if (!rx.test(html)) { console.error('index.html has no script tag for ' + name); process.exit(1); }
  html = html.replace(rx, '$1' + ver);
  console.log('wired ' + name);
}
fs.writeFileSync(path.join(ROOT, 'index.html'), html);
