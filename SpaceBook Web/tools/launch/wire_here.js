'use strict';
/* Copies rebuilt page books into THIS checkout's js/ and bumps their ?v= in this checkout's index.html.
 *   node tools/launch/wire_here.js <version> <class> KEY [KEY ...]       e.g.  node tools/launch/wire_here.js 20261027_ans1 11 isl hpe cs
 * The files come from docs/source-verification/class-<class>/KEY/build/<KEY>_<class>_book.js (written by tools/build_book11.py / build_book12.py).
 * Why this exists: docs/source-verification/class-12/tools/wire_book11.py has the path D:\SpaceBook\SpaceBook Web written into it (biology_tools.ROOT), so run from
 * another checkout or worktree it changes the MAIN checkout instead. This one only ever touches the checkout it lives in. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const [ver, cls, ...keys] = process.argv.slice(2);
if (!ver || !cls || !keys.length) { console.error('usage: wire_here.js <version> <class 11|12> KEY...'); process.exit(2); }
let html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
for (const k of keys) {
  const name = `${k}_${cls}_book.js`;
  const src = path.join(ROOT, 'docs', 'source-verification', 'class-' + cls, k, 'build', name);
  if (!fs.existsSync(src)) { console.error('missing ' + src); process.exit(1); }
  fs.copyFileSync(src, path.join(ROOT, 'js', name));
  const rx = new RegExp('(js/' + name.replace(/[.]/g, '\\.') + '\\?v=)[0-9A-Za-z_]+');
  if (!rx.test(html)) { console.error('index.html has no script tag for ' + name); process.exit(1); }
  html = html.replace(rx, '$1' + ver);
  console.log('wired ' + name);
}
fs.writeFileSync(path.join(ROOT, 'index.html'), html);
