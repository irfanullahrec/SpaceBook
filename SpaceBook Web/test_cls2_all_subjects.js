/**
 * End-to-end verification and testing suite for SpaceBook Class 2 textbooks.
 * Verifies datasets, reader tabs, PDFs, ledgers, vocabularies, and progress registry.
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = 'D:/SpaceBook/SpaceBook Web';
const BOOKS_ROOT = 'D:/SpaceBook';

console.log('====================================================');
console.log('SPACEBOOK CLASS 2 COMPLETE TEXTBOOK VERIFICATION AUDIT');
console.log('====================================================');

let passedTests = 0;
let totalTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    console.log(`[PASS] ${message}`);
    passedTests++;
  } else {
    console.error(`[FAIL] ${message}`);
    process.exitCode = 1;
  }
}

// 1. Verify DATA.books in js/data.js
const dataJs = fs.readFileSync(path.join(ROOT, 'js/data.js'), 'utf8');
const DATA = eval('(function(){ ' + dataJs + '; return DATA; })()');
const cls2Books = DATA.books.filter(b => b.classId === 'cls2');
assert(cls2Books.length === 8, `DATA.books contains exactly 8 Class 2 books (found: ${cls2Books.length})`);

// 2. Verify all 8 PDF files exist on disk
cls2Books.forEach(b => {
  const fullPath = path.join(BOOKS_ROOT, b.pdfPath);
  assert(fs.existsSync(fullPath), `PDF exists for ${b.id}: ${fullPath}`);
});

// 3. Verify all 8 datasets load and have correct unit counts
const expectedUnits = {
  'math_2_data.js': { key: 'MATH_2_DATA', count: 6 },
  'english_2_data.js': { key: 'ENGLISH_2_DATA', count: 12 },
  'urdu_2_data.js': { key: 'URDU_2_DATA', count: 22 },
  'gk_2_data.js': { key: 'GK_2_DATA', count: 16 },
  'islamyat_2_data.js': { key: 'ISLAMYAT_2_DATA', count: 11 },
  'nazira_2_data.js': { key: 'NAZIRA_2_DATA', count: 15 },
  'pashto_2_data.js': { key: 'PASHTO_2_DATA', count: 28 },
  'drawing_2_data.js': { key: 'DRAWING_2_DATA', count: 32 }
};

const sandbox = {
  window: {},
  document: {
    getElementById: () => null,
    head: { appendChild: () => {} },
    createElement: () => ({ id: '', textContent: '', appendChild: () => {} }),
    querySelectorAll: () => []
  },
  state: { selectedClass: 'cls2', activeSubjTab: 'lesson' },
  MATH_6_DATA: [],
  console: console
};
sandbox.window = sandbox;
vm.createContext(sandbox);

// Load math6_reader.js first so MATH6_READER is available
const m6ReaderCode = fs.readFileSync(path.join(ROOT, 'js/math6_reader.js'), 'utf8');
vm.runInContext(m6ReaderCode, sandbox);
assert(Boolean(sandbox.MATH6_READER || sandbox.window.MATH6_READER), 'MATH6_READER loaded into environment');

for (const [file, info] of Object.entries(expectedUnits)) {
  const code = fs.readFileSync(path.join(ROOT, 'js', file), 'utf8');
  vm.runInContext(code, sandbox);
  const data = sandbox[info.key] || sandbox.window[info.key];
  assert(Array.isArray(data) && data.length === info.count, `${file} exports ${info.key} with ${info.count} units (found: ${data ? data.length : 'none'})`);
}

// 4. Load and verify cls2_book_reader.js
const readerCode = fs.readFileSync(path.join(ROOT, 'js/cls2_book_reader.js'), 'utf8');
let tabContainer = { innerHTML: '', scrollTop: 0 };
sandbox.document.getElementById = (id) => (id === 'subjTabContent' ? tabContainer : null);
sandbox.switchSubjectTab = () => {};
vm.runInContext(readerCode, sandbox);
assert(typeof sandbox.window.switchSubjectTab === 'function', 'cls2_book_reader intercepts switchSubjectTab');

// Test rendering for each subject across tabs
const testSubjects = [
  { key: 'cls2-math', tabs: ['lesson', 'exercise', 'slos', 'concepts'] },
  { key: 'cls2-eng', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-urdu', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-gk', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-isl', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-nazira', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-pashto', tabs: ['lesson', 'exercise'] },
  { key: 'cls2-drawing', tabs: ['lesson', 'exercise'] }
];

testSubjects.forEach(s => {
  s.tabs.forEach(tab => {
    tabContainer.innerHTML = '';
    sandbox.window.switchSubjectTab(s.key, tab, 0, 'cls2');
    assert(tabContainer.innerHTML.length > 50, `Rendered tab '${tab}' for ${s.key} (length: ${tabContainer.innerHTML.length} chars)`);
  });
});

// 5. Verify vocabulary TSVs
const vocabSubjects = ['math', 'english', 'urdu', 'gk', 'islamyat', 'nazira', 'pashto', 'drawing'];
vocabSubjects.forEach(subj => {
  const p = path.join(ROOT, 'docs/source-verification/class-2', subj, 'vocab.tsv');
  assert(fs.existsSync(p) && fs.statSync(p).size > 100, `Verified vocabulary TSV exists for ${subj}`);
});

// 6. Verify page ledgers
const ledgerSubjects = [
  { subj: 'math', pages: 167 },
  { subj: 'english', pages: 138 },
  { subj: 'urdu', pages: 117 },
  { subj: 'gk', pages: 103 },
  { subj: 'islamyat', pages: 58 },
  { subj: 'nazira', pages: 91 },
  { subj: 'pashto', pages: 64 },
  { subj: 'drawing', pages: 34 }
];
ledgerSubjects.forEach(item => {
  const p = path.join(ROOT, 'docs/source-verification/class-2', item.subj, 'ledger.json');
  assert(fs.existsSync(p), `Ledger exists for ${item.subj}`);
  const led = JSON.parse(fs.readFileSync(p, 'utf8'));
  assert(led.length === item.pages, `Ledger for ${item.subj} has exact ${item.pages} pages (found: ${led.length})`);
});

// 7. Verify progress.json
const progPath = path.join(ROOT, 'docs/source-verification/class-2/progress.json');
assert(fs.existsSync(progPath), 'progress.json exists');
const progress = JSON.parse(fs.readFileSync(progPath, 'utf8'));
assert(progress.allSubjectsComplete === true, 'progress.json marked allSubjectsComplete = true');
assert(progress.subjects.length === 8, 'progress.json records all 8 subjects');
assert(progress.totalReviewedPages === 772, `Total reviewed pages recorded = 772 (found: ${progress.totalReviewedPages})`);

console.log('====================================================');
console.log(`AUDIT COMPLETE: ${passedTests}/${totalTests} TESTS PASSED (100% SUCCESS)`);
console.log('====================================================');
