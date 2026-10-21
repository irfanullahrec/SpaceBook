'use strict';
/* Replace text in a data file and log the correction for the QA report.
 *   node tools/qa/fix_text.js <js file> <book> <pdf page> <old> <new> [--expect N]
 * Replaces every occurrence of <old> (plain text, as it appears in the file: JSON escapes included) by <new>, refuses when the
 * number of occurrences differs from --expect (default: at least 1), appends a line to docs/qa/proofreading_fixes.tsv. */
const fs = require('fs'), path = require('path');
const [file, book, page, oldT, newT] = process.argv.slice(2, 7);
const ei = process.argv.indexOf('--expect'); const expect = ei > 0 ? +process.argv[ei + 1] : null;
const f = path.resolve(__dirname, '..', '..', file);
let s = fs.readFileSync(f, 'utf8');
const n = s.split(oldT).length - 1;
if (!n || (expect !== null && n !== expect)) { console.error('occurrences:', n, 'expected', expect === null ? '>=1' : expect); process.exit(1); }
s = s.split(oldT).join(newT);
for (let i = 0; i < 6; i++) { try { fs.writeFileSync(f, s); break; } catch (e) { if (i === 5) throw e; Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 3000); } }
const log = path.resolve(__dirname, '..', '..', 'docs', 'qa', 'proofreading_fixes.tsv');
fs.mkdirSync(path.dirname(log), { recursive: true });
if (!fs.existsSync(log)) fs.writeFileSync(log, 'book\tpdf page\tfile\told\tnew\toccurrences\n');
fs.appendFileSync(log, [book, page, file, oldT.replace(/\t|\n/g, ' '), newT.replace(/\t|\n/g, ' '), n].join('\t') + '\n');
console.log('fixed', n, 'occurrence(s) in', file);
