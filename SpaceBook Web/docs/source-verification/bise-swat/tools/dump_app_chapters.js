'use strict';
/* Writes data/app_chapters.json: for every Class 9-12 subject, the chapter list the app itself shows.
 *   node --max-old-space-size=8192 docs/source-verification/bise-swat/tools/dump_app_chapters.js <out.json>
 * Uses the same sandbox as tools/arch02_matrix.js. build_bise.py reads the file to match Board chapters to the app's. */
const path = require('path');
const { load } = require(path.resolve(__dirname, '../../../../tools/lib/app_sandbox'));
const app = load({ page: 'index.html', quiet: true });
const out = app.run(`(() => {
  const res = {}, orig = getSubjectChapterList; let cur = null;
  getSubjectChapterList = function (key, classId) { const r = orig.apply(this, arguments); if (cur && classId === cur.c && !cur.k) cur.k = key; return r; };
  for (const c of DATA.classes) { if (!['cls9','cls10','cls11','cls12'].includes(c.id)) continue;
    for (const s of (DATA.subjects[c.id] || [])) {
      cur = { c: c.id, k: null }; try { openSubject(c.id, s.id); } catch (e) {}
      let ch = []; if (cur.k) { try { ch = orig(cur.k, c.id).map((x, i) => [x.number || x.num || x.id || (i+1), String(x.title || x.name || '').slice(0, 70)]); } catch (e) {} }
      res[s.id] = { key: cur.k, name: s.name, n: s.chapters, ch };
    } }
  getSubjectChapterList = orig; return res; })()`);
require('fs').writeFileSync(process.argv[2], JSON.stringify(out));
console.log(Object.keys(out).length + ' subjects');
