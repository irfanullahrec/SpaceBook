'use strict';
/* Inventory of the supplied textbooks in D:\SpaceBook\Books (override with SB_BOOKS_DIR).
 *   node tools/launch/books_inventory.js            writes docs/launch/books_inventory.json
 *   node tools/launch/books_inventory.js --check    fails when the committed file differs from the folder
 *
 * Per class folder, per subject folder: the number of scan images (one per page of the book), the PDFs (and the pages their page tree
 * declares), the Word files, whether the scan numbering has gaps, and the subject id of the app it maps to (SUBJECT_MAP below).
 * A folder that maps to no subject, or a subject that no folder maps to, is a finding, not an error here: the manifest reports it.
 * Reads file names and the first and last 3 MB of each PDF only; changes nothing in Books. Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const BOOKS = process.env.SB_BOOKS_DIR || 'D:/SpaceBook/Books';
const OUT = path.join(ROOT, 'docs', 'launch', 'books_inventory.json');
const CHECK = process.argv.includes('--check');

const CLASS_DIRS = { '1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5, '6th': 6, '7th': 7, '8th': 8, '9th': 9, '10th': 10, '11th': 11, '12th': 12 };

/* folder name (lower case, spaces squeezed) -> subject id suffix, per class; the app ids are cls<N>-<suffix> (see content/app_catalog.json) */
const RULES = [
  [/drawing/, 'drawing'], [/hpe|health/, 'hpe'], [/general science|^science/, 'sci'], [/geography/, 'geo'],
  [/arabi/, 'arabic'], [/nazer|nazir/, 'nazira'], [/pashto/, 'pashto'], [/^(\d+(st|nd|rd|th) )?gk|\bgk\b|general knowledge/, 'gk'],
  [/english/, 'eng'], [/urdu/, 'urdu'], [/maths?\b|mtha/, 'math'], [/social study um/, 'sstum'], [/social study/, 'sst'],
  [/m[ -]?q\b|mutalia|mutalaa/, 'quran'], [/comput|\bcs\b/, 'comp'], [/physics/, 'phy'], [/chemi/, 'chem'], [/bio/, 'bio'],
  [/stat/, 'stat'], [/civic/, 'civics'], [/econom/, 'econ'], [/pak ?stud/, 'pakstudy'], [/islamic history/, 'ishist'],
  [/ikhtiari|ekhtyri|ismaiat ikhtiari/, 'islopt'], [/islam|ismaiat|slamyat/, 'isl'], [/history/, 'hist'],
];
/* exceptions where the app's id differs from the rule's suffix */
const CLASS_FIX = {
  9: { comp: 'comp', quran: 'quran', pakstudy: 'pakstudy', islopt: 'islopt' },
  10: { pakstudy: 'pakstudy' },
  11: { islopt: 'ikhtiari', quran: 'mq', ishist: 'ishist', comp: 'cs' },
  12: { pakstudy: 'pak', islopt: 'islopt', ishist: 'islhist', quran: 'quran', comp: 'comp' },
};
function subjectOf(cls, folder) {
  const f = folder.toLowerCase().replace(/\s+/g, ' ').trim();
  if (cls === 11 && /ekhtyri|ikhtiari/.test(f)) return 'cls11-ikhtiari';
  if (cls === 11 && /lazimi|lazmi/.test(f)) return 'cls11-isl';
  for (const [re, id] of RULES) {
    if (re.test(f)) return 'cls' + cls + '-' + ((CLASS_FIX[cls] && CLASS_FIX[cls][id]) || id);
  }
  return null;
}

function pdfPages(file) {
  let fd;
  try {
    fd = fs.openSync(file, 'r');
    const size = fs.fstatSync(fd).size, n = Math.min(size, 3000000);
    const re = /\/Type\s*\/Pages[^>]*?\/Count\s+(\d+)|\/Count\s+(\d+)[^>]*?\/Type\s*\/Pages/g;
    let max = 0;
    for (const off of [0, Math.max(0, size - n)]) {
      const b = Buffer.alloc(n); fs.readSync(fd, b, 0, n, off);
      const s = b.toString('latin1'); let m; re.lastIndex = 0;
      while ((m = re.exec(s))) max = Math.max(max, +(m[1] || m[2]));
      if (size <= n) break;
    }
    return max || null;
  } catch (e) { return null; } finally { if (fd !== undefined) try { fs.closeSync(fd); } catch (e) {} }
}

function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out); else out.push(p);
  }
  return out;
}

function numberGaps(names) {
  /* scan files are numbered ("000.jpg", "Name 12.jpg", "..._123.jpg"): the last number of each name; gaps and repeats in that run */
  const nums = [];
  for (const n of names) { const m = n.replace(/\.[^.]+$/, '').match(/(\d+)\D*$/); if (m) nums.push(+m[1]); }
  nums.sort((a, b) => a - b);
  const gaps = [], dups = [];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) dups.push(nums[i]);
    else if (nums[i] > nums[i - 1] + 1) gaps.push([nums[i - 1] + 1, nums[i] - 1]);
  }
  return { first: nums[0] == null ? null : nums[0], last: nums.length ? nums[nums.length - 1] : null, numbered: nums.length, gaps: gaps.slice(0, 20), repeats: dups.slice(0, 20) };
}

const inv = { schema: 'spacebook.books-inventory/1', root: 'Books', classes: [] };
for (const dirName of Object.keys(CLASS_DIRS).sort((a, b) => CLASS_DIRS[a] - CLASS_DIRS[b])) {
  const cls = CLASS_DIRS[dirName];
  const cdir = path.join(BOOKS, dirName);
  if (!fs.existsSync(cdir)) { inv.classes.push({ cls, folder: dirName, missing: true, books: [] }); continue; }
  const entries = fs.readdirSync(cdir, { withFileTypes: true });
  const books = [];
  const loose = []; // Class 4 keeps its books as PDFs next to a folder
  for (const e of entries) {
    const p = path.join(cdir, e.name);
    if (e.isDirectory()) {
      const files = walk(p, []);
      const imgs = files.filter(f => /\.(jpe?g|jfif|png)$/i.test(f)).map(f => path.basename(f));
      const pdfs = files.filter(f => /\.pdf$/i.test(f));
      const docx = files.filter(f => /\.docx?$/i.test(f));
      const pdfInfo = pdfs.map(f => ({ name: path.basename(f), pages: pdfPages(f) }));
      const wholePdf = pdfInfo.filter(x => !/\d+\s*\.pdf$/i.test(x.name) && !/part_\d+/i.test(x.name));
      books.push({
        folder: e.name, subject: subjectOf(cls, e.name),
        scans: imgs.length, scanNumbers: numberGaps(imgs),
        pdfs: pdfInfo.length, pdfPages: pdfInfo.reduce((n, x) => n + (x.pages || 0), 0), pdfPagesUnknown: pdfInfo.filter(x => x.pages == null).length,
        pdfFiles: pdfInfo.map(x => x.name + (x.pages ? ' (' + x.pages + ')' : '')),
        docx: docx.length, empty: files.filter(f => !/Thumbs\.db$/i.test(f)).length === 0,
      });
    } else if (/\.pdf$/i.test(e.name)) loose.push({ name: e.name, pages: pdfPages(p) });
  }
  if (loose.length) {
    for (const f of loose) {
      const sub = (() => {
        const n = f.name.toLowerCase();
        if (/english/.test(n)) return 'cls4-eng'; if (/general science/.test(n)) return 'cls4-sci'; if (/islamiat/.test(n)) return 'cls4-isl';
        if (/math/.test(n)) return 'cls4-math'; if (/pashto/.test(n)) return 'cls4-pashto'; if (/urdu/.test(n)) return 'cls4-urdu';
        if (/social study.*em|social study book 4th em/.test(n)) return 'cls4-sst'; if (/social study/.test(n)) return 'cls4-sstum'; return null;
      })();
      books.push({ folder: f.name, subject: sub, scans: 0, scanNumbers: null, pdfs: 1, pdfPages: f.pages || 0, pdfPagesUnknown: f.pages ? 0 : 1, pdfFiles: [f.name + (f.pages ? ' (' + f.pages + ')' : '')], docx: 0, empty: false, looseInClassFolder: true });
    }
  }
  inv.classes.push({ cls, folder: dirName, books: books.sort((a, b) => a.folder.localeCompare(b.folder)) });
}

const json = JSON.stringify(inv, null, 1) + '\n';
if (CHECK) {
  const have = fs.existsSync(OUT) ? fs.readFileSync(OUT, 'utf8') : '';
  if (have !== json) { console.error('docs/launch/books_inventory.json differs from ' + BOOKS + ': run node tools/launch/books_inventory.js'); process.exit(1); }
  console.log('books_inventory.json matches the Books folder');
} else {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, json);
  let b = 0, s = 0, p = 0, un = 0;
  inv.classes.forEach(c => c.books.forEach(x => { b++; s += x.scans; p += x.pdfPages; if (!x.subject) un++; }));
  console.log('books_inventory.json: ' + inv.classes.length + ' classes, ' + b + ' book folders, ' + s + ' scan images, ' + p + ' PDF pages, ' + un + ' folders with no subject mapping');
}
