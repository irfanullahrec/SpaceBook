'use strict';
/* Builds js/fills_data.js: the answers for the tables the student has to fill in and the work for the projects / activities of the books.
 *     node --max-old-space-size=6144 tools/fills/build_fills.js [--check] [--list cls9:chem] [--report]
 * Sources: tools/fills/src/*.json, one file per book:
 *   {cls: 9, key: "chem",
 *    tables: [{unit, n, head, rows}],   n = the table's place among the tables with empty cells of that unit (--list shows it), head = text the table's header must contain,
 *                                       rows = every body row in full; a cell is text, or {lewis: {...}} / {bohr: {...}} for a drawing (tools/fills/svg.js)
 *    work:   [{unit, n, starts, blocks}]}  n = the place among the project / activity boxes of that unit, starts = text the box must contain,
 *                                          blocks = reader blocks (p, h, ul, table, svg) plus {t: "bohr"|"lewis", ..., cap}
 * Every given cell of the book must equal the fill's cell at the same place, and every empty cell must be filled, or the build fails: a fill that
 * does not line up with the table is never written. The reader (js/math6_reader.js) shows the button only where a fill exists (key = hash of the book
 * title and the table / box text), js/sb_fill.js does the filling. --check fails when the file is stale. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const { load } = require('../lib/app_sandbox');
const svg = require('./svg');

const SRC = path.join(__dirname, 'src');
const OUT = path.join(ROOT, 'js', 'fills_data.js');
const args = process.argv.slice(2);
const sources = fs.readdirSync(SRC).filter(f => f.endsWith('.json')).sort().map(f => Object.assign(JSON.parse(fs.readFileSync(path.join(SRC, f), 'utf8')), { file: f }));
const listArg = args.includes('--list') ? args[args.indexOf('--list') + 1] : null;
const wanted = listArg ? [listArg] : sources.map(s => 'cls' + s.cls + ':' + s.key);

const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true });
const found = JSON.parse(app.run(`JSON.stringify((() => {
  const R = window.MATH6_READER, out = {};
  ${JSON.stringify(wanted)}.forEach(id => {
    const [c, k] = id.split(':'), B = window['CLS' + c.replace('cls', '') + '_BOOKS'] && window['CLS' + c.replace('cls', '') + '_BOOKS'][k];
    if (!B) return;
    const res = out[id] = {title: (B.book && B.book.title) || '', tables: [], boxes: []};
    R.withBook(B.words, B.book, () => B.units.forEach(u => {
      let tn = 0, bn = 0;
      const walk = list => (list || []).forEach(b => {
        if (!b || typeof b !== 'object') return;
        if (b.t === 'table' && b.rows) {
          const body = b.rows.slice(b.head || 0);
          if (body.some(r => r.some(x => !R.cellText(x)))) res.tables.push({unit: u.number, n: tn++, key: R.fillKeyOfTable(b), head: b.rows.slice(0, b.head || 0).map(r => r.map(R.cellText).join(' | ')).join(' / '), cap: b.cap ? R.cellText(b.cap) : '',
            width: Math.max(...b.rows.map(r => r.length)), rows: body.map(r => r.map(R.cellText))});
        }
        if (b.t === 'box') {
          const title = R.cellText(b.title), text = (b.blocks || []).map(x => R.cellText(x.en) || (x.items || []).map(i => R.cellText(i)).join(' ')).join(' ');
          if (/project|activity/i.test(title) || /^\\s*(project|activity)/i.test(text)) res.boxes.push({unit: u.number, n: bn++, key: R.fillKeyOfBox(b), title, text});
        }
        walk(b.blocks);
      });
      (u.sections || []).forEach(s => walk(s.blocks));
    }));
  });
  return out;
})())`));

if (listArg) {
  const f = found[listArg];
  if (!f) { console.log('no such book ' + listArg); process.exit(1); }
  const have = new Set(); sources.forEach(s => { if ('cls' + s.cls + ':' + s.key === listArg) { (s.tables || []).forEach(t => have.add('T' + t.unit + '.' + t.n)); (s.work || []).forEach(t => have.add('W' + t.unit + '.' + t.n)); } });
  console.log(f.title);
  f.tables.forEach(t => console.log((have.has('T' + t.unit + '.' + t.n) ? 'done ' : 'TODO ') + 'table unit ' + t.unit + ' n ' + t.n + '  ' + t.rows.length + ' rows, ' + t.rows.reduce((a, r) => a + r.filter(x => !x).length, 0) + ' empty  | ' + t.head.slice(0, 110) + (t.cap ? '  [' + t.cap.slice(0, 50) + ']' : '')));
  f.boxes.forEach(b => console.log((have.has('W' + b.unit + '.' + b.n) ? 'done ' : 'TODO ') + 'work  unit ' + b.unit + ' n ' + b.n + '  ' + b.title.slice(0, 40) + ' | ' + b.text.slice(0, 110)));
  process.exit(0);
}

const problems = [], out = {}, stat = {};
const norm = s => String(s).split('||')[0].replace(/\s+/g, ' ').trim();
const cell = v => (v && typeof v === 'object') ? (v.lewis ? svg.lewis(v.lewis) : v.bohr ? svg.bohr(v.bohr) : String(v)) : String(v);
const expandBlock = b => {
  if (b.t === 'bohr') return { t: 'svg', svg: svg.bohr(b), cap: { en: b.cap || '' } };
  if (b.t === 'lewis') return { t: 'svg', svg: svg.lewis(b), cap: { en: b.cap || '' } };
  return b;
};
sources.forEach(src => {
  const id = 'cls' + src.cls + ':' + src.key, f = found[id], tag = src.file + ': ';
  if (!f) { problems.push(tag + 'book ' + id + ' not found'); return; }
  stat[id] = stat[id] || { tables: f.tables.length, boxes: f.boxes.length, tFilled: 0, bFilled: 0, cells: 0 };
  (src.tables || []).forEach(e => {
    const t = f.tables.find(x => String(x.unit) === String(e.unit) && x.n === e.n), where = tag + 'table unit ' + e.unit + ' n ' + e.n;
    if (!t) { problems.push(where + ': no such table with empty cells'); return; }
    if (e.head && !t.head.toLowerCase().includes(String(e.head).toLowerCase())) { problems.push(where + ': header does not contain "' + e.head + '" (it is "' + t.head.slice(0, 80) + '")'); return; }
    if (e.rows.length !== t.rows.length) { problems.push(where + ': ' + e.rows.length + ' rows given, the table has ' + t.rows.length); return; }
    let bad = false;
    e.rows.forEach((row, i) => {
      if (row.length < t.width) { problems.push(where + ' row ' + i + ': ' + row.length + ' cells given, the table is ' + t.width + ' wide'); bad = true; }
      t.rows[i].forEach((have, j) => {
        if (have && norm(have) !== norm(row[j])) { problems.push(where + ' row ' + i + ' cell ' + j + ': the book has "' + norm(have) + '" but the fill has "' + norm(row[j]) + '"'); bad = true; }
        if (!have && (row[j] == null || row[j] === '')) { problems.push(where + ' row ' + i + ' cell ' + j + ': empty in the book and in the fill'); bad = true; }
      });
    });
    if (bad) return;
    if (out[t.key]) { problems.push(where + ': two fills for one table'); return; }
    out[t.key] = { t: 'table', rows: e.rows.map(r => r.map(cell)) };
    stat[id].tFilled++; stat[id].cells += t.rows.reduce((a, r) => a + r.filter(x => !x).length, 0);
  });
  (src.work || []).forEach(e => {
    const b = f.boxes.find(x => String(x.unit) === String(e.unit) && x.n === e.n), where = tag + 'work unit ' + e.unit + ' n ' + e.n;
    if (!b) { problems.push(where + ': no such project / activity box'); return; }
    if (e.starts && !(b.title + ' ' + b.text).toLowerCase().includes(String(e.starts).toLowerCase())) { problems.push(where + ': box does not contain "' + e.starts + '" (it is "' + (b.title + ' ' + b.text).slice(0, 80) + '")'); return; }
    if (out[b.key]) { problems.push(where + ': two fills for one box'); return; }
    out[b.key] = { t: 'work', blocks: e.blocks.map(expandBlock) };
    stat[id].bFilled++;
  });
});

if (problems.length) { console.log('FAIL  ' + problems.length + ' fills do not line up with the book data:\n  ' + problems.join('\n  ')); process.exit(1); }
const sorted = Object.fromEntries(Object.keys(out).sort().map(k => [k, out[k]]));
const text = '// Answers for the tables the student fills in and the work for the projects and activities of the books. Generated by tools/fills/build_fills.js from tools/fills/src/*.json: do not edit.\n'
  + 'window.SB_FILLS = ' + JSON.stringify(sorted) + ';\n';
const n = Object.keys(sorted).length;
if (args.includes('--report')) {
  console.log('book            tables filled/with-empty-cells   boxes filled/project-or-activity');
  Object.entries(stat).forEach(([id, s]) => console.log(id.padEnd(15), String(s.tFilled + '/' + s.tables).padStart(8), String(s.bFilled + '/' + s.boxes).padStart(28)));
}
if (args.includes('--check')) {
  const have = fs.existsSync(OUT) ? fs.readFileSync(OUT, 'utf8').replace(/\r\n/g, '\n') : '';
  if (have !== text) { console.log('STALE  js/fills_data.js (node tools/fills/build_fills.js)'); process.exit(1); }
  console.log('fresh  fills_data  (' + n + ' fills)');
} else {
  fs.writeFileSync(OUT, text);
  console.log('wrote js/fills_data.js: ' + n + ' fills (' + Object.values(stat).reduce((a, s) => a + s.cells, 0) + ' table cells), ' + (text.length / 1024).toFixed(1) + ' KB');
}
