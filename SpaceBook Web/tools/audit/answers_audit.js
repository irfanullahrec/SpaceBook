'use strict';
/* Which questions of the books have an answer?   node --max-old-space-size=6144 tools/audit/answers_audit.js [--list cls9:math] [--json out.json] [--check] [--write-baseline]
 *
 * A leaf is what a student can ask the answer of: a question without parts, or one part of a question (a part of a "parts" block too). The a) b) c) d)
 * lines that follow a roman-numbered part are that part's options, not leaves.
 *   ans    the leaf has its own Ans record (solId) and the record exists
 *   viaQ   no record of its own, but its question has one (one Ans button for the whole question)
 *   key    no record, the book's printed answer key has a line for exactly this part (js/math6_reader.js shows it behind an Ans button)
 *   extra  an answer written for it (js/answers_extra.js)
 *   whole  only the printed line of the whole question exists (a list of the parts that qualify, prose): the Ans button shows that line
 *   none   nothing: no record, no printed line, no written answer
 *   head   a group heading ("Short Questions", "B. Write short answers ...", "Activities"): a question without parts that is followed by a question numbered
 *          1 / i / a, which is its first sub-question. No Ans button is shown for a heading; every sub-question has its own.
 * dangling = a solId whose record does not exist. Books: every CLSn_BOOKS entry.
 * --check fails when a book has more "whole", "none" or dangling leaves than tools/audit/answers_baseline.json (--write-baseline after an intended change).
 * Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const { load } = require('../lib/app_sandbox');

const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const BASE = path.join(__dirname, 'answers_baseline.json');

const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true });
const data = JSON.parse(app.run(`JSON.stringify((() => {
  const stores = ['CLS5_SOLUTIONS', 'CLS6_SOLUTIONS'].map(k => window[k]).filter(Boolean);
  const hasRec = id => stores.some(s => s[id] !== undefined);
  const R = window.MATH6_READER;
  const books = [];
  for (let n = 1; n <= 12; n++) {
    const L = window['CLS' + n + '_BOOKS']; if (!L) continue;
    Object.keys(L).forEach(k => {
      const B = L[k]; if (!B || !B.units) return;
      const rec = { id: 'cls' + n + ':' + k, cls: n, subject: k, leaves: 0, ans: 0, viaQ: 0, key: 0, extra: 0, whole: 0, none: 0, head: 0, dangling: 0, missing: [] };
      R.withBook(B.words, B.book, () => {
        const leaf = (loc, label, own, qSol, kindOf) => {
          rec.leaves++;
          if (own) { if (hasRec(own)) rec.ans++; else { rec.dangling++; rec.missing.push({ loc, label, why: 'dangling' }); } return; }
          if (qSol) { rec.viaQ++; return; }
          const a = kindOf();
          if (a.kind === 'part') rec.key++;
          else if (a.kind === 'extra') rec.extra++;
          else { rec[a.kind]++; rec.missing.push({ loc, label, why: a.kind }); }
        };
        const text = x => String((x && x.en) || '').replace(/\\s+/g, ' ').slice(0, 90);
        const lab = no => String(no == null ? '' : no).split('(').join('').split(')').join('').split('.').join('').trim().toLowerCase();
        const FIRST = ['1', 'i', 'a', '۱', 'الف'];   // 1 i a, the Urdu digit one and the Urdu letter alif-lam-fe (the first label of lettered parts)
        const markHeads = arr => { (arr || []).forEach((b, i) => {
          // the last part of a question whose own sub-questions (a, b, c ...) follow in the next parts block is a heading too
          if (b && (b.t === 'q' || b.t === 'parts') && (b.parts || []).length) {
            const last = b.parts[b.parts.length - 1];
            let k = i + 1; while (arr[k] && ['page', 'svg', 'm', 'table', 'box'].includes(arr[k].t)) k++;
            const nb = arr[k];
            if (last && !last.solId && nb && nb.t === 'parts' && (nb.parts || []).length && FIRST.includes(lab(nb.parts[0].no)) && !FIRST.includes(lab(last.no))) b.__tail = true;
          }
          if (!b || b.t !== 'q' || (b.parts || []).length || b.solId) return;
          // a question followed (after a word box, an info box or an intro line) by its first sub-question 1 / i / a, or by a block of parts
          let j = i + 1; while (arr[j] && ['m', 'table', 'svg', 'box', 'page', 'p'].includes(arr[j].t)) j++;
          const nx = arr[j];
          if (nx && nx.t === 'q' && FIRST.includes(lab(nx.no)) && !FIRST.includes(lab(b.no))) b.__head = true;
          if (nx && nx.t === 'parts' && j > i + 1) b.__head = true;
        }); };
        B.units.forEach(u => (u.sections || []).forEach(s => {
          let lastQ = null;
          const walk = (b, exId) => {
            if (!b || typeof b !== 'object') return;
            if (b.t === 'exercise') exId = String(b.id);
            if (b.t === 'q') {
              lastQ = b;
              const loc = 'unit ' + u.number + (exId ? ' ex ' + exId : '') + ' Q' + b.no;
              const ps = b.parts || [];
              if (ps.length) {
                const labs = R.partLabels(ps);
                const opt = ps.map((p, i) => /^[a-e]$/.test(labs[i]) && labs.slice(0, i).some(x => R.isRoman(x)));
                ps.forEach((p, i) => { if (b.__tail && i === ps.length - 1 && !p.solId && !b.solId) { rec.leaves++; rec.head++; } else if (!opt[i]) leaf(loc + ' ' + p.no, text(p) || text(b), p.solId, b.solId, () => R.answerOf(exId, b, labs[i])); });
              } else if (b.__head) { rec.leaves++; rec.head++; }
              else leaf(loc, text(b), b.solId, null, () => R.answerOf(exId, b, null));
            }
            if (b.t === 'parts') { const labs = R.partLabels(b.parts || []); (b.parts || []).forEach((p, i) => { if (b.__tail && i === b.parts.length - 1 && !p.solId) { rec.leaves++; rec.head++; } else leaf('unit ' + u.number + (exId ? ' ex ' + exId : '') + ' parts ' + p.no, text(p), p.solId, null, () => lastQ ? R.answerOf(exId, lastQ, labs[i]) : ({ kind: 'none' })); }); }
            markHeads(b.blocks);
            (b.blocks || []).forEach(x => walk(x, exId));
          };
          markHeads(s.blocks);
          (s.blocks || []).forEach(b => walk(b, null));
        }));
      });
      if (rec.leaves) books.push(rec);
    });
  }
  return books;
})())`));

const sum = k => data.reduce((n, b) => n + b[k], 0);
const pad = (s, n) => String(s).padEnd(n), num = (v, n) => String(v).padStart(n);
const cols = ['leaves', 'ans', 'viaQ', 'key', 'extra', 'whole', 'none', 'head', 'dangling'];
console.log(pad('book', 14) + cols.map(c => num(c, c === 'dangling' ? 9 : 7)).join(''));
data.forEach(b => console.log(pad(b.id, 14) + cols.map(c => num(b[c], c === 'dangling' ? 9 : 7)).join('')));
console.log(pad('TOTAL', 14) + cols.map(c => num(sum(c), c === 'dangling' ? 9 : 7)).join(''));

const want = opt('--list');
if (want) {
  const b = data.find(x => x.id === want);
  if (!b) { console.error('no such book: ' + want); process.exit(2); }
  b.missing.forEach(m => console.log(m.why.padEnd(9) + ' | ' + m.loc + ' | ' + m.label));
}
if (opt('--json')) fs.writeFileSync(opt('--json'), JSON.stringify(data));
const weak = b => ({ whole: b.whole, none: b.none, dangling: b.dangling });
if (args.includes('--write-baseline')) {
  fs.writeFileSync(BASE, JSON.stringify(Object.fromEntries(data.map(b => [b.id, weak(b)])), null, 1) + '\n');
  console.log('wrote ' + path.relative(ROOT, BASE));
}
if (args.includes('--check')) {
  const base = JSON.parse(fs.readFileSync(BASE, 'utf8'));
  const worse = data.filter(b => { const o = base[b.id] || { whole: 0, none: 0, dangling: 0 }; return b.whole > o.whole || b.none > o.none || b.dangling > o.dangling; });
  if (worse.length) { console.log('FAIL  more questions without a full answer than the baseline in: ' + worse.map(b => b.id).join(', ')); process.exit(1); }
  console.log('answers audit: no book has more questions without a full answer than the baseline');
}
