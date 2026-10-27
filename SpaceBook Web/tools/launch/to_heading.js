'use strict';
/* Turns instruction lines that were counted as unanswered questions ("Fill in the blanks.", "Mark the correct answer.") into headings, in the page files of a book.
 *
 *   node tools/launch/to_heading.js <book> <number,number,...> [--dir <folder>] [--dry]
 *        <book> is a registry id such as cls11:islhist; the numbers are those of <folder>/<book>.work.txt (default folder .launch-answers/, see answers_worklist.js list).
 *        A line   q <label> | text   or   qp <label> | text   becomes   ## <label>. text   (the page syntax of the Class 10-12 books). Nothing else changes, no line is added or
 *        removed, so run this BEFORE answers_worklist.js apply (apply adds lines and makes the line numbers of <book>.map.json stale).
 * Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const book = args[0], list = args[1];
if (!book || !list) { console.error('usage: to_heading.js <book> <n,n,...> [--dir d] [--dry]'); process.exit(2); }
const DIR = path.resolve(ROOT, opt('--dir', '.launch-answers'));
const map = JSON.parse(fs.readFileSync(path.join(DIR, book.replace(':', '_') + '.map.json'), 'utf8'));
const nums = list.split(',').map(s => s.trim()).filter(Boolean).flatMap(s => { const m = /^(\d+)-(\d+)$/.exec(s); if (!m) return [s]; const o = []; for (let i = +m[1]; i <= +m[2]; i++) o.push(String(i)); return o; });
const dry = args.includes('--dry');
const byFile = {};
let bad = 0;
for (const n of nums) {
  const e = map[n];
  if (!e) { console.error('no entry for ' + n); bad++; continue; }
  (byFile[e.file] = byFile[e.file] || []).push({ n, line: e.line, text: e.text });
}
let changed = 0;
for (const [f, items] of Object.entries(byFile)) {
  const file = path.resolve(ROOT, f);
  const raw = fs.readFileSync(file, 'utf8');
  const eol = raw.includes('\r\n') ? '\r\n' : '\n';
  const lines = raw.split(/\r?\n/);
  for (const it of items) {
    const l = lines[it.line - 1];
    const m = /^qp?[ \t]+([^|]*?)[ \t]*\|[ \t]?(.*)$/.exec(l || '');
    if (!m) { console.error(`${f}:${it.line} (#${it.n}) is not a question line: ${String(l).slice(0, 60)}`); bad++; continue; }
    const label = m[1].trim();
    const rest = m[2];
    if (it.text && !rest.replace(/\s+/g, ' ').startsWith(it.text.replace(/\s+/g, ' ').slice(0, 20))) { console.error(`${f}:${it.line} (#${it.n}) text differs from the work list`); bad++; continue; }
    const label2 = /^\d+$/.test(label) && /^\d+[\s.)]/.test(rest) ? '' : label;                 // "q 3 | 16 The following ..." : the label is the exercise, the question carries its own number
    lines[it.line - 1] = '## ' + (label2 ? label2 + (/[.۔]$/.test(label2) ? ' ' : '۔ ') : '') + rest;
    changed++;
  }
  if (!dry) fs.writeFileSync(file, lines.join(eol));
}
console.log(`${dry ? '(dry run) ' : ''}${changed} lines turned into headings, ${bad} problems`);
process.exit(bad ? 1 : 0);
