'use strict';
/* The coverage manifest:  Class -> Subject -> Book folder -> Chapter -> printed page / PDF page -> content location -> verification status.
 *   node tools/launch/coverage_manifest.js            writes docs/launch/COVERAGE_MANIFEST.json, COVERAGE_MANIFEST.md, coverage_chapters.csv
 *   node tools/launch/coverage_manifest.js --check    fails when a committed file is stale, or when a book that was accounted for is no longer
 * Reads only generated or committed files (no scans, no browser):
 *   docs/launch/books_inventory.json   what is in D:\SpaceBook\Books (tools/launch/books_inventory.js)
 *   content/app_catalog.json           the classes, subjects and chapters of the app
 *   content/lazy_manifest.json         which script file holds which book
 *   docs/source-verification/class-N/<book>/ledger.json   one row per scanned page: PDF page, scan file, printed page, status, notes, unit
 *   docs/launch/EXERCISE_COVERAGE.json (tools/launch/exercise_coverage.js)   questions and answers per chapter
 * A scan is "accounted for" when the book has a page ledger with as many rows as the scans (each row: front matter, lesson, answers, back matter,
 * blank or duplicate). Books without a ledger are older data: listed as "legacy (no page ledger)": the manifest does not claim they were page-verified.
 * "Verified" in this file means: the page-by-page work of the class pipeline recorded the page. It is not an expert sign-off (docs/launch/VERIFICATION_REPORT.md).
 * Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const L = path.join(ROOT, 'docs', 'launch');
const CHECK = process.argv.includes('--check');
const rd = f => JSON.parse(fs.readFileSync(f, 'utf8'));

const inv = rd(path.join(L, 'books_inventory.json'));
const catalog = rd(path.join(ROOT, 'content', 'app_catalog.json'));
const lazy = rd(path.join(ROOT, 'content', 'lazy_manifest.json'));
const ex = fs.existsSync(path.join(L, 'EXERCISE_COVERAGE.json')) ? rd(path.join(L, 'EXERCISE_COVERAGE.json')) : { chapters: [], books: [] };

// subject id -> the book folder(s) of the inventory
const folderOf = {};
for (const c of inv.classes) for (const b of c.books) if (b.subject) (folderOf[b.subject] = folderOf[b.subject] || []).push({ cls: c.cls, ...b });

// subject id -> registry key and ledger directory (class-N/<dir>)
const SV = path.join(ROOT, 'docs', 'source-verification');
const ALIASES = {      // subject suffix -> directory names tried in docs/source-verification/class-N/
  phy: ['phys', 'physics', 'phy'], pakstudy: ['pakstudy', 'pak'], pak: ['pakstudy', 'pak'], ishist: ['ishist', 'islhist'], islhist: ['islhist', 'ishist'],
  ikhtiari: ['ikhtiari', 'islopt'], islopt: ['islopt', 'ikhtiari'], mq: ['mq', 'quran'], quran: ['quran', 'mq'], cs: ['cs', 'comp'], comp: ['comp', 'cs'],
  isl: ['isl', 'islc'], eng: ['eng'], sci: ['sci'], bio: ['bio', 'biology'], chem: ['chem'],
};
function ledgerFor(sid) {
  const m = /^cls(\d+)-(.+)$/.exec(sid); if (!m) return null;
  for (const d of (ALIASES[m[2]] || [m[2]])) {
    const f = path.join(SV, 'class-' + m[1], d, 'ledger.json');
    if (fs.existsSync(f)) return { dir: 'docs/source-verification/class-' + m[1] + '/' + d, rows: rd(f) };
  }
  return null;
}
// which script file holds the book: CLSn_BOOKS key, or a legacy global
const fileOfBook = {};
for (const f of lazy.files) {
  for (const [g, keys] of Object.entries(f.keys || {})) { const mm = /^CLS(\d+)_BOOKS$/.exec(g); if (mm) for (const k of keys) fileOfBook['cls' + mm[1] + ':' + k] = f.src; }
}
const regKey = sid => { const m = /^cls(\d+)-(.+)$/.exec(sid); const k = m[2]; const map = { ishist: 'islhist', ikhtiari: 'islopt', mq: 'quran', cs: 'comp', isl: m[1] === '11' ? 'islc' : 'isl', phy: 'phys', pak: 'pakstudy' }; return 'cls' + m[1] + ':' + ((m[1] === '11' || m[1] === '12') && map[k] ? map[k] : k); };
const exBook = new Map(ex.books.map(b => [b.subject, b]));
const exChap = new Map(ex.chapters.map(r => [r.subject + '#' + r.n, r]));

const books = [], chapters = [], discrepancies = [];
const counts = (rows, f) => rows.reduce((o, r) => { const k = f(r); o[k] = (o[k] || 0) + 1; return o; }, {});
for (const c of catalog.classes) for (const s of c.subjects) {
  const cls = +c.id.replace('cls', '');
  const folders = folderOf[s.id] || [];
  const led = ledgerFor(s.id);
  const key = regKey(s.id);
  const scans = folders.reduce((n, f) => n + f.scans, 0);
  const row = { cls, subject: s.id, name: s.name, folders: folders.map(f => f.folder), scans, pdfFiles: folders.reduce((n, f) => n + f.pdfs, 0), docx: folders.reduce((n, f) => n + f.docx, 0),
    content: fileOfBook[key] || (exBook.get(s.id) ? '(registry)' : '(legacy data file)'), ledger: led ? led.dir : null, ledgerRows: led ? led.rows.length : 0, statuses: led ? counts(led.rows, r => r.status) : {},
    printed: null, flaggedPages: 0, chapters: s.chapters.length, status: '', notes: [] };
  if (led) {
    const nums = led.rows.filter(r => typeof r.printedPage === 'number').map(r => r.printedPage);
    row.printed = nums.length ? [Math.min(...nums), Math.max(...nums)] : null;
    row.flaggedPages = led.rows.filter(r => (r.issues || []).length).length;
    const have = new Set(nums), gaps = [];
    if (nums.length) for (let p = Math.min(...nums); p <= Math.max(...nums); p++) if (!have.has(p)) gaps.push(p);
    row.printedGaps = gaps.length > 40 ? gaps.slice(0, 40).concat(['...']) : gaps;
  }
  if (!folders.length && s.id === 'cls10-isl') { row.status = 'shared book (see notes)'; row.notes.push('the KPK Islamiat (compulsory) book is one book for Classes 9 and 10; Class 10 opens the Class 9 book'); }
  else if (!folders.length) { row.status = 'NO SOURCE SUPPLIED'; row.notes.push('no folder in Books maps to this subject'); }
  else if (folders.every(f => f.empty)) { row.status = 'NO SOURCE SUPPLIED'; row.notes.push('the book folder exists but is empty'); }
  else if (!led) { row.status = 'legacy (no page ledger)'; row.notes.push('older data: not page-ledgered; its scans are not individually accounted for'); }
  else {
    const n = led.rows.length;
    const d = n - scans;
    if (scans === n) row.status = 'accounted (every scan has a ledger row)';
    else if (scans && Math.abs(scans - 2 * n) <= 4) row.status = 'accounted (two scan sets of each page)';
    else if (scans && Math.abs(n - 2 * scans) <= 4) row.status = 'accounted (each scan is a two-page spread: two rows)';
    else if (scans && Math.abs(d) <= Math.max(6, Math.ceil(scans * 0.03))) { row.status = 'accounted within ' + Math.abs(d) + ' (rows split or merged, not reconciled one by one)'; row.notes.push(scans + ' scan files, ' + n + ' ledger rows'); }
    else if (!scans && row.pdfFiles) row.status = 'accounted (PDF only)';
    else { row.status = 'ledger differs from the scans'; row.notes.push(`${scans} scan files, ${n} ledger rows`); }
  }
  if (row.printedGaps && row.printedGaps.length) row.notes.push('printed pages with no ledger row: ' + row.printedGaps.join(','));
  if (row.flaggedPages) row.notes.push(row.flaggedPages + ' pages carry notes (see ledger "issues")');
  const eb = exBook.get(s.id);
  if (eb) { row.questions = eb.q; row.unanswered = eb.none; }
  if (/NO SOURCE|differs/.test(row.status)) discrepancies.push({ subject: s.id, name: s.name, what: row.status, notes: row.notes });
  books.push(row);

  // chapters
  const byUnit = new Map();
  if (led) for (const r of led.rows) { const u = r.unit == null ? '' : String(r.unit); if (!byUnit.has(u)) byUnit.set(u, []); byUnit.get(u).push(r); }
  s.chapters.forEach((ch, i) => {
    const e = exChap.get(s.id + '#' + i);
    const unitNo = e && e.number != null ? String(e.number) : null;
    const rows = unitNo && byUnit.has(unitNo) ? byUnit.get(unitNo) : [];
    const pp = rows.filter(r => typeof r.printedPage === 'number').map(r => r.printedPage);
    const pdfp = rows.map(r => r.pdfPage).filter(Number.isFinite);
    const flagged = rows.filter(r => (r.issues || []).length).length;
    let v;
    if (row.status === 'NO SOURCE SUPPLIED') v = 'no source';
    else if (!led) v = 'legacy data, not page-ledgered';
    else if (!rows.length) v = 'no ledger rows for this chapter (matched by unit number)';
    else v = flagged ? `recorded page by page, ${flagged} page note(s)` : 'recorded page by page';
    chapters.push({ cls, subject: s.id, n: i, title: ch.t, printed: e && e.printed ? e.printed : (pp.length ? [Math.min(...pp), Math.max(...pp)] : null), pdfPages: pdfp.length ? [Math.min(...pdfp), Math.max(...pdfp)] : null,
      content: row.content, questions: e ? e.q : null, unanswered: e ? e.none : null, exerciseState: e ? e.state : (eb ? '' : 'not counted (legacy data)'), verification: v });
  });
}

const totals = { classes: catalog.classes.length, subjects: books.length, chapters: chapters.length, scans: books.reduce((n, b) => n + b.scans, 0), ledgerRows: books.reduce((n, b) => n + b.ledgerRows, 0),
  byStatus: counts(books, b => b.status.replace(/within [0-9]+/, 'within a few pages')), flaggedPages: books.reduce((n, b) => n + b.flaggedPages, 0) };
const unmappedFolders = [];
for (const c of inv.classes) for (const b of c.books) if (!b.subject) unmappedFolders.push({ cls: c.cls, folder: b.folder, scans: b.scans });
// books in the Books folder that the app does not list (duplicates of another folder, or a book nobody built)
const listed = new Set(books.map(b => b.subject));
const unlistedFolders = [];
for (const c of inv.classes) for (const b of c.books) if (b.subject && !listed.has(b.subject)) unlistedFolders.push({ cls: c.cls, folder: b.folder, subject: b.subject, scans: b.scans });
const SHARED = { 'cls10-isl': 'the KPK Islamiat (compulsory) book is one book for Classes 9 and 10 (js/cls6_book_reader.js opens the Class 9 book)' };
for (const u of unmappedFolders.filter(u => !(u.cls === 4 && u.folder === '4th'))) discrepancies.push({ subject: '-', name: `Books/${u.cls}th/${u.folder}`, what: 'folder maps to no subject of the app', notes: [u.scans + ' scans'] });
for (const u of unlistedFolders) discrepancies.push({ subject: u.subject, name: `Books/${u.folder}`, what: 'folder has no subject in the app catalog', notes: [u.scans + ' scans'] });

const result = { schema: 'spacebook.coverage-manifest/1', totals, books, chapters, unmappedFolders, unlistedFolders, discrepancies };
const json = JSON.stringify(result) + '\n';

const q = s => '"' + String(s == null ? '' : s).replace(/"/g, '""') + '"';
const csv = ['class,subject,chapter_index,chapter,printed_from,printed_to,pdf_from,pdf_to,content_file,questions,unanswered,exercise_state,verification'];
for (const r of chapters) csv.push([r.cls, r.subject, r.n + 1, q(r.title), r.printed ? r.printed[0] : '', r.printed ? r.printed[1] : '', r.pdfPages ? r.pdfPages[0] : '', r.pdfPages ? r.pdfPages[1] : '', q(r.content), r.questions == null ? '' : r.questions, r.unanswered == null ? '' : r.unanswered, q(r.exerciseState), q(r.verification)].join(','));

const md = [];
md.push('# Textbook coverage manifest');
md.push('');
md.push('Generated by `tools/launch/coverage_manifest.js`. **Do not edit by hand.** Every chapter row (class, subject, chapter, printed page range, PDF page range, content file, questions, unanswered, verification) is in `coverage_chapters.csv`; this page is the book-level view and the discrepancies.');
md.push('');
md.push('"Recorded page by page" means the class pipeline wrote a ledger row for the page (PDF page, scan file, printed page, status, notes). It is the project\'s own record, **not** an expert sign-off, and a ledger row does not prove that every word of the page was compared with the scan (see `VERIFICATION_REPORT.md` for what was sampled by eye in this review).');
md.push('');
md.push('## Totals');
md.push('');
md.push(`Classes ${totals.classes}, subjects ${totals.subjects}, chapters ${totals.chapters}; ${totals.scans} scan files in \`Books\`; ${totals.ledgerRows} pages recorded in ledgers; ${totals.flaggedPages} pages carry a note.`);
md.push('');
md.push('| Status | Subjects |');
md.push('|---|---|');
for (const [k, v] of Object.entries(totals.byStatus).sort()) md.push(`| ${k} | ${v} |`);
md.push('');
md.push('## Discrepancies to resolve');
md.push('');
if (!discrepancies.length) md.push('None.');
else {
  md.push('| Subject | Item | Finding | Notes |');
  md.push('|---|---|---|---|');
  for (const d of discrepancies) md.push(`| \`${d.subject}\` | ${d.name} | ${d.what} | ${d.notes.join('; ')} |`);
}
md.push('');
md.push('## By book');
md.push('');
md.push('| Class | Subject | Book folder(s) | Scans | Ledger rows | Printed pages | Content file | Questions / unanswered | Status |');
md.push('|---|---|---|---|---|---|---|---|---|');
for (const b of books) {
  md.push(`| ${b.cls} | ${b.name} (\`${b.subject}\`) | ${b.folders.join(', ') || '-'} | ${b.scans || '-'} | ${b.ledgerRows || '-'} | ${b.printed ? b.printed[0] + '-' + b.printed[1] : '-'} | \`${b.content}\` | ${b.questions == null ? '-' : b.questions + ' / ' + b.unanswered} | ${b.status}${b.notes.length ? ' (' + b.notes.join('; ').replace(/\|/g, '/') + ')' : ''} |`);
}
md.push('');
const mdText = md.join('\n');
const csvText = csv.join('\n') + '\n';

if (CHECK) {
  const bad = [];
  const want = { 'COVERAGE_MANIFEST.json': json, 'COVERAGE_MANIFEST.md': mdText, 'coverage_chapters.csv': csvText };
  for (const [f, t] of Object.entries(want)) { const p = path.join(L, f); if (!fs.existsSync(p) || fs.readFileSync(p, 'utf8').replace(/\r\n/g, '\n') !== t.replace(/\r\n/g, '\n')) bad.push(f); }
  if (bad.length) { console.error('stale: ' + bad.join(', ') + ' (node tools/launch/coverage_manifest.js)'); process.exit(1); }
  console.log('coverage manifest is fresh (' + totals.subjects + ' subjects, ' + totals.chapters + ' chapters)');
  process.exit(0);
}
fs.writeFileSync(path.join(L, 'COVERAGE_MANIFEST.json'), json);
fs.writeFileSync(path.join(L, 'COVERAGE_MANIFEST.md'), mdText);
fs.writeFileSync(path.join(L, 'coverage_chapters.csv'), csvText);
console.log(`coverage manifest: ${totals.subjects} subjects, ${totals.chapters} chapters; ` + Object.entries(totals.byStatus).map(([k, v]) => v + ' ' + k).join(', ') + `; ${discrepancies.length} discrepancies`);
