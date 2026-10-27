'use strict';
/* Suggests the missing word of a fill-in-the-blank question from the lesson text of the same book.
 *   node tools/launch/blank_finder.js <book> [--dir .launch-answers]       e.g.  node tools/launch/blank_finder.js cls11:civics
 * Reads <dir>/<book>.work.txt (made by answers_worklist.js list), and for every question that has a run of underscores (or dots) looks in the page files of the
 * book for a sentence that is the same with one phrase in the place of the blank. Prints   [number] suggestion(s) | the question.
 * A suggestion is only a pointer into the book's own text: it has to be read and confirmed by whoever writes the answer. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2), book = args[0];
const DIR = path.resolve(ROOT, args.includes('--dir') ? args[args.indexOf('--dir') + 1] : '.launch-answers');
const m = /^cls(\d+):(.+)$/.exec(book || ''); if (!m) { console.error('usage: blank_finder.js cls11:civics'); process.exit(2); }
const alias = { islc: 'isl', islopt: m[1] === '11' ? 'ikhtiari' : 'islopt', quran: m[1] === '11' ? 'mq' : 'quran', islhist: m[1] === '11' ? 'ishist' : 'islhist', comp: m[1] === '11' ? 'cs' : 'comp' };
const dir = ['pages'].map(() => [alias[m[2]], m[2]].filter(Boolean).map(d => path.join(ROOT, 'docs', 'source-verification', 'class-' + m[1], d, 'pages')).find(p => fs.existsSync(p)))[0];
if (!dir) { console.error('no page files'); process.exit(2); }
// Arabic and Urdu letter variants, diacritics and punctuation are ignored in the comparison
const norm = s => String(s).replace(/[ً-ٰٟۖ-ۭ‌-‏]/g, '').replace(/[يىئ]/g, 'ی').replace(/ك/g, 'ک').replace(/[ۂۃہة]/g, 'ہ').replace(/[ےۓ]/g, 'ے').replace(/[أإآٱ]/g, 'ا').replace(/[۔،؛؟!:"“”‘’'()\[\]{}.,\-–—]/g, ' ').replace(/\s+/g, ' ').trim();
const text = [];
for (const f of fs.readdirSync(dir).filter(x => /^p\d+\.txt$/.test(x)).sort()) {
  for (const l of fs.readFileSync(path.join(dir, f), 'utf8').split(/\r?\n/)) {
    if (/^(p|li|ss|##) /.test(l) || /^p\s/.test(l)) text.push(norm(l.replace(/^\S+\s/, '').split(' || ')[0]));
  }
}
const blob = text.join(' | ');
const work = fs.readFileSync(path.join(DIR, book.replace(':', '_') + '.work.txt'), 'utf8').split(/\r?\n/);
let found = 0, total = 0;
for (const line of work) {
  const mm = /^\[(\d+)\] .*? \| (.*)$/.exec(line); if (!mm) continue;
  const q = mm[2];
  if (!/(_{3,}|\.{4,}|…{2,})/.test(q)) continue;
  total++;
  const parts = q.replace(/\((?:[^()]*[،,][^()]*)\)\s*$/, '').split(/_{3,}|\.{4,}|…{2,}/).map(norm).filter(p => p.length >= 3);
  if (!parts.length) continue;
  // before and after the blank (the longest two pieces next to it)
  const pre = parts[0], post = parts.length > 1 ? parts[1] : '';
  const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const tail = (s, n) => s.split(' ').slice(-n).join(' '), head = (s, n) => s.split(' ').slice(0, n).join(' ');
  const rx = new RegExp((q.trim().startsWith('_') ? '' : esc(tail(pre, 4)) + ' ') + '([^|]{1,40}?)' + (post ? ' ' + esc(head(post, 3)) : ''), 'g');
  const hits = new Set(); let h;
  while ((h = rx.exec(blob)) && hits.size < 4) hits.add(h[1].trim());
  if (hits.size) found++;
  console.log(`[${mm[1]}] ${hits.size ? [...hits].join(' / ') : '-'}  |  ${q.slice(0, 110)}`);
}
console.error(`${found} of ${total} fill-in-the-blank questions have a candidate in the lesson text`);
