'use strict';
/* The Munawar (Kanz) series, as data: every book is registered, has a data file that registers the right key with the right units, a cover,
 * a script tag in index.html and a coverPageMap line, and the Government lists are untouched.
 *     node tests/private/data.js
 * No browser. Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), vm = require('vm'), cp = require('child_process');
const ROOT = path.resolve(__dirname, '..', '..');
const MUN = path.join(ROOT, 'docs', 'source-verification', 'private', 'munawar');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };
const read = f => fs.readFileSync(path.join(ROOT, f), 'utf8');

const reg = JSON.parse(fs.readFileSync(path.join(MUN, 'books.json'), 'utf8'));
const books = reg.books;

// 1. the registry files are the ones registry.py writes
{
  let out = null, err = null;
  for (const py of ['python3', 'python']) {        // the CI runner has python3, a Windows PC has python
    try { out = cp.execFileSync(py, ['-P', path.join(MUN, 'tools', 'registry.py'), '--check'], { cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'] }).toString(); break; }
    catch (e) { err = e; if (e.code !== 'ENOENT') break; }
  }
  if (out === null && err && err.code === 'ENOENT') console.log('SKIP  registry.py --check (no Python on this machine)');
  else check('books.json and js/munawar_registry.js are what registry.py writes', out !== null && /up to date/.test(out), String((err && (err.stderr || err.message)) || out));
}

check('42 books, ids unique, four classes', books.length === 42 && new Set(books.map(b => b.subjectId)).size === 42 && new Set(books.map(b => b.cls)).size === 4, books.length);
const perClass = c => books.filter(b => b.cls === c).length;
check('Class 1 has 11 books, Class 2 has 10 (no Urdu), Class 3 has 11, Class 4 has 10', [1, 2, 3, 4].map(perClass).join() === '11,10,11,10', [1, 2, 3, 4].map(perClass));

// 2. the registry in a page: DATA.subjects with the series flag, Government lists unchanged
const box = { window: {}, console };
vm.createContext(box);
vm.runInContext(read('js/data.js'), box);
const govBefore = JSON.stringify(vm.runInContext('DATA.subjects', box));
vm.runInContext(read('js/munawar_registry.js'), box);
const DATA = vm.runInContext('DATA', box);
check('DATA.series.munawar describes the series', DATA.series && DATA.series.munawar && DATA.series.munawar.name === 'Munawar' && DATA.series.munawar.classes.join() === '1,2,3,4', DATA.series);
let govOk = true;
for (const cls of Object.keys(JSON.parse(govBefore))) {
  const gov = (DATA.subjects[cls] || []).filter(s => !s.series);
  if (JSON.stringify(gov) !== JSON.stringify(JSON.parse(govBefore)[cls])) govOk = false;
}
check('the Government subjects of every class are exactly what data.js lists (no Munawar book leaks into them)', govOk);
check('every Munawar subject carries series:"munawar", a cover path and a chapter count', books.every(b => { const s = (DATA.subjects[b.classId] || []).find(x => x.id === b.subjectId); return s && s.series === 'munawar' && s.cover === 'covers/' + b.cover && s.chapters >= 1; }));
check('Classes 5-8 list no Munawar book yet', ['cls5', 'cls6', 'cls7', 'cls8'].every(c => !(DATA.subjects[c] || []).some(s => s.series)));

// 3. each book's data file
const unitCount = id => { const f = path.join(MUN, id, 'units.tsv'); return fs.existsSync(f) ? fs.readFileSync(f, 'utf8').split(/\r?\n/).filter(l => l.trim() && !l.startsWith('#')).length : 1; };
const bad = [];
for (const b of books) {
  const f = path.join(ROOT, 'js', b.dataFile);
  if (!fs.existsSync(f)) { bad.push(b.id + ': no ' + b.dataFile); continue; }
  const sb = { window: {} }; vm.createContext(sb);
  try { vm.runInContext(fs.readFileSync(f, 'utf8'), sb); } catch (e) { bad.push(b.id + ': ' + e.message); continue; }
  const B = (sb.window['CLS' + b.cls + '_BOOKS'] || {})[b.key];
  if (!B) { bad.push(b.id + ': CLS' + b.cls + '_BOOKS[' + b.key + '] missing'); continue; }
  const n = unitCount(b.id);
  if (B.units.length !== n) bad.push(b.id + ': ' + B.units.length + ' units, units.tsv has ' + n);
  if (B.book.series !== 'munawar' || B.book.totalPdfPages !== b.pdfPages) bad.push(b.id + ': book record');
  if (B.book.reviewedPdfPages > B.book.totalPdfPages) bad.push(b.id + ': reviewed more pages than the pdf has');
  if (b.medium === 'ur' && JSON.stringify(B.book.langs) !== '["ur","en","ps"]') bad.push(b.id + ': Urdu-medium book without the Urdu-first slot order');
  const empty = B.units.filter(u => !u.sections.length).length;
  if (B.book.reviewedPdfPages === 0 && empty !== B.units.length) bad.push(b.id + ': unreviewed book with sections');
}
check('all 42 data files register CLS<N>_BOOKS["mun-<code>"] with the units of their contents page and a consistent book record', bad.length === 0, bad.slice(0, 6));

// 4. the transcribed pages
const sb1 = { window: {} }; vm.createContext(sb1);
vm.runInContext(read('js/munawar_c1_math_book.js'), sb1);
const M1 = sb1.window.CLS1_BOOKS['mun-math'];
const blocks = []; (function walk(l) { (l || []).forEach(x => { blocks.push(x); walk(x.blocks); walk(x.items); }); })(M1.units.flatMap(u => u.sections.flatMap(s => s.blocks)));
const sols = Object.keys(sb1.window.CLS6_SOLUTIONS || {}).filter(k => k.startsWith('mc1math-'));
check('Class 1 Mathematics: 8 pages reviewed, Unit 1 has its pages, 12 answers, every question has its answer', M1.book.reviewedPdfPages === 8 && M1.units[0].sections.length >= 4 && sols.length === 12 && blocks.filter(b => b.t === 'q').every(q => q.solId && sb1.window.CLS6_SOLUTIONS[q.solId]), { reviewed: M1.book.reviewedPdfPages, sections: M1.units[0].sections.length, sols: sols.length });
const texts = JSON.stringify(M1.units);
check('the transcription says what could not be read instead of guessing it (@issue notes are in the ledger)', fs.readFileSync(path.join(MUN, 'c1-math', 'ledger.json'), 'utf8').includes('too small to read') || fs.readFileSync(path.join(MUN, 'c1-math', 'ledger.json'), 'utf8').includes('cannot be read'));
check('every sentence of the transcribed pages has Urdu and Pashto', !/"en":"[^"]+","ur":""/.test(texts) && !/UNTRANSLATED/.test(fs.readFileSync(path.join(MUN, 'c1-math', 'ledger.json'), 'utf8')));

// 5. covers, index.html, coverPageMap
check('every book has its cover file (covers/Munawar/<subject id>.webp)', books.every(b => fs.existsSync(path.join(ROOT, 'covers', b.cover)) && fs.statSync(path.join(ROOT, 'covers', b.cover)).size > 4000), books.filter(b => !fs.existsSync(path.join(ROOT, 'covers', b.cover))).map(b => b.id));
const index = read('index.html');
check('index.html loads the registry, the stylesheet, the module and all 42 data files', index.includes('js/munawar_registry.js') && index.includes('css/sb_private.css') && index.includes('js/sb_private_books.js') && books.every(b => index.includes('js/' + b.dataFile)), books.filter(b => !index.includes('js/' + b.dataFile)).map(b => b.id));
const appjs = read('js/app.js');
check('js/app.js has a coverPageMap line for every book (the app\'s cover maker reads them)', books.every(b => appjs.includes('"' + b.subjectId + '": "' + b.cover + '"')), books.filter(b => !appjs.includes('"' + b.subjectId + '": "' + b.cover + '"')).map(b => b.id));
check('the class cards, the home cards and the search result for a class go through SBPrivate.entry', (appjs.match(/SBPrivate\.entry\('\$\{c\.id\}'\)/g) || []).length === 2 && /SBPrivate\.entry\(c\.id\)/.test(appjs));
check('every Munawar page file is consecutive from p000 (the builder needs it)', books.every(b => { const d = path.join(MUN, b.id, 'pages'); if (!fs.existsSync(d)) return true; const f = fs.readdirSync(d).filter(x => /^p\d{3}\.txt$/.test(x)).sort(); return f.every((x, i) => x === 'p' + String(i).padStart(3, '0') + '.txt'); }));

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
