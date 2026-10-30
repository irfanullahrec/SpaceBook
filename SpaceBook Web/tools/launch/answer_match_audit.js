'use strict';
/* Does each Ans belong to its question? A wrong answer under a question (the owner met "Factors of 42" under a question about complex numbers, 2026-10-29) is worse
 * than a missing one. This reads what exercise_coverage.js reads (tools/tests/extract_leaves.js: every question and part of every CLSn_BOOKS book and of the Mathematics
 * books of Classes 5, 6, 7, 8 and 11, with the answer exactly as the Ans button shows it) and compares each QUESTION with its ANSWER by content:
 *   key-mismatch  the question has a written solution AND a line in the book's own printed answer key, and the two disagree: no number in common, or a different option
 *                 letter. This is the check that finds an answer that is wrong for its question, whatever the reason (a solution looked up for another question or class, a
 *                 misprint, a bad transcription). Only questions that have both can be judged: Mathematics books and the books with a printed key.
 *   shared        the same answer text (30 characters or more) stands under questions of two or more different books or classes and does not share a token with at least
 *                 one of them: the sign of an answer looked up in the wrong book (the "s7" of Class 6 under Class 11).
 * Information only, never a finding: a long answer that shares no word or number with its question (counted as "weak"); most are right, an answer need not repeat the
 * question ("Practise the dialogue ..." has a long answer of its own), and a sum is answered with numbers that are not in the question.
 * It cannot prove an answer is right; it finds answers that disagree with the book's own key or that stand under unrelated questions. Every finding is a line in
 * docs/launch/ANSWER_MATCH_AUDIT.md and answer_match_findings.csv for a person to look at, never a change.
 *   node --max-old-space-size=6144 tools/launch/answer_match_audit.js [--from leaves.json] [--save-leaves leaves.json] [--check] [--write-baseline]
 * --check fails when a book has more findings than in docs/launch/answer_match_baseline.json (the looked-at findings are listed there with the reason).
 * Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const OUT = path.join(ROOT, 'docs', 'launch');
const BASE = path.join(OUT, 'answer_match_baseline.json');

let raw;
if (opt('--from')) raw = JSON.parse(fs.readFileSync(opt('--from'), 'utf8'));
else {
  const { load } = require('../lib/app_sandbox');
  // The extractor itself is NOT edited (tools/tests/build_test_bank.js hashes its text as an input of the Create Test bank): this audit reads it, adds one line in memory so
  // that each question with a written solution also carries the book's printed key line (kt), and runs that copy.
  const extractFile = path.join(ROOT, 'tools', 'tests', 'extract_leaves.js');
  let extractSrc = fs.readFileSync(extractFile, 'utf8').replace(/\r\n/g, '\n');
  const patch = (a, b) => { if (extractSrc.split(a).length !== 2) { console.error('the extractor changed: patch point not found: ' + a.slice(0, 60)); process.exit(2); } extractSrc = extractSrc.replace(a, () => b); };
  patch("            emit({ ex: exId == null ? '' : String(exId), clash, fig: how.strict &&", "            const auditKey = own ? { kt: (() => { const k = keyRec(); return k && k.src === 'book' && k.answer ? T(k.answer) : ''; })() } : null;\n            emit(Object.assign({ ex: exId == null ? '' : String(exId), clash, fig: how.strict &&");
  patch("sid: node.solId || '', src: own ? 'sol' : rec ? (rec.src === 'book' ? 'key' : 'extra') : '' });", "sid: node.solId || '', src: own ? 'sol' : rec ? (rec.src === 'book' ? 'key' : 'extra') : '' }, auditKey));");
  const extractModule = new (require('module'))(extractFile); extractModule._compile(extractSrc, extractFile);
  const extract = extractModule.exports;
  const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true });
  for (const n of [5, 6, 7, 8, 11]) app.run(fs.readFileSync(path.join(ROOT, 'js/math_' + n + '_solutions.js'), 'utf8'));
  raw = JSON.parse(app.run('JSON.stringify((' + extract.toString() + ')())', 900000));
  if (opt('--save-leaves')) fs.writeFileSync(opt('--save-leaves'), JSON.stringify(raw));
}

const STOP = new Set(('about above after again also always another answer answers because before being below between both cannot could correct does doing done each either enough every example exercise find finds first following from given gives have having here however into itself just least less like made make many might more most much must next only other others over part parts please question questions result same shall should since some such than that their them then there these they this those through under until using value values very what when where whether which while whose will with within without would write your').split(' '));
const first = x => (Array.isArray(x) ? String(x[0] || '') : String(x == null ? '' : x));
const tokens = text => {
  const t = String(text || '').toLowerCase().replace(/\\[a-z]+/g, ' ').replace(/[{}$^_\\]/g, ' ');
  const out = new Set();
  (t.match(/\d+(?:\.\d+)?/g) || []).forEach(n => out.add(n.replace(/^0+(?=\d)/, '')));
  (t.match(/[a-z]{5,}/g) || []).forEach(w => { if (!STOP.has(w)) out.add(w.replace(/(ing|ed|es|s)$/, '')); });
  (t.match(/[؀-ۿ]{3,}/g) || []).forEach(w => out.add(w));
  return out;
};
const common = (a, b) => { let n = 0; for (const x of a) if (b.has(x)) n++; return n; };

const rows = [];                 // findings
const bySig = new Map();         // answer text -> leaves that carry it
let looked = 0, compared = 0, keyed = 0, weak = 0, acknowledged = 0;
// the numeric values an answer states: whole numbers, decimals, fractions (a/b, \frac{a}{b}, \dfrac) and mixed numbers (7\frac{9}{10}); signs are ignored (the printed keys
// often lose a minus sign) and a rounded value agrees with the exact one (104 and 104.40, 0.9 and 9/10, 38.85 and 38.86)
const values = s => {
  const digits = x => x.replace(/[^\d.]/g, '');
  let t = String(s || '').replace(/(\d),(?=\d{3})/g, '$1').replace(/\\[dt]?frac\s*(\{[^{}]*\}|\d)\s*(\{[^{}]*\}|\d)/g, (m, n, d) => (digits(n) && digits(d) ? ' ' + digits(n) + '/' + digits(d) + ' ' : ' ')).replace(/[-−–]\s*(?=\d)/g, ' ');
  const out = [];
  t = t.replace(/(\d+)\s+(\d+)\/(\d+)/g, (m, w, n, d) => { if (+d) out.push(+w + +n / +d); return ' '; });
  t = t.replace(/(\d+(?:\.\d+)?)\s*\/\s*(\d+(?:\.\d+)?)/g, (m, n, d) => { if (+d) out.push(+n / +d); return ' '; });
  (t.match(/\d+(?:\.\d+)?/g) || []).forEach(x => out.push(parseFloat(x)));
  return out;
};
const agree = (A, K) => A.some(a => K.some(k => Math.abs(a - k) <= 0.012 * Math.max(a, k) + 0.011));
const letter = s => { const m = /^\s*\(?([a-e])\)?(?:[\s.:)]|$)/i.exec(String(s || '')); return m ? m[1].toLowerCase() : ''; };
for (const L of raw.leaves) {
  const ans = String(L.a || '') + ' ' + String(L.st || '');
  if (!ans.trim()) continue;
  looked++;
  const q = tokens(first(L.q) + ' ' + String(L.stem || ''));
  const a = tokens(ans);
  const sig = String(L.a || '').trim() + '|' + String(L.st || '').trim();
  if (sig.length >= 30 && L.src === 'sol') { if (!bySig.has(sig)) bySig.set(sig, []); bySig.get(sig).push({ L, q, a }); }
  if (L.src !== 'sol' && L.src !== 'extra') continue;               // a printed key is a bare line: nothing to compare
  // (1) the written solution against the book's own printed key line for the same question: the numbers (or the option letter) must agree
  if (L.kt) {
    keyed++;
    const nA = values(L.a), nK = values(L.kt), lA = letter(L.a), lK = letter(L.kt);
    const numbersDisagree = nA.length > 0 && nK.length > 0 && !agree(nA, nK);
    const lettersDisagree = lA && lK && lA !== lK;
    // a solution that says itself that the printed key is wrong ("the printed key shows 57, which does not match the data") is a known, explained difference
    const explained = /printed key|answer key|key (?:shows|gives|says)|teacher'?s note/i.test(String(L.st || '') + ' ' + String(L.a || ''));
    if ((numbersDisagree || lettersDisagree) && explained) acknowledged++;
    else if (numbersDisagree || lettersDisagree) rows.push({ kind: 'key-mismatch', L, shared: 0 });
  }
  // (2) information only: a long answer that shares no word or number with its question (most are right: an answer need not repeat the question)
  if (q.size >= 3 && a.size >= 10 && ans.trim().length >= 150) { compared++; if (common(q, a) === 0) weak++; }
}
for (const [, list] of bySig) {
  const books = new Set(list.map(x => x.L.b));
  const qs = new Set(list.map(x => first(x.L.q).replace(/\s+/g, ' ').trim()));
  if (books.size < 2 || qs.size < 2) continue;
  for (const x of list) {
    if (x.q.size >= 2 && common(x.q, x.a) === 0 && !rows.some(r => r.L === x.L)) rows.push({ kind: 'shared', L: x.L, shared: books.size });
  }
}
rows.sort((x, y) => (x.kind === y.kind ? String(x.L.b).localeCompare(String(y.L.b)) || x.L.u - y.L.u : x.kind === 'shared' ? -1 : 1));

const perBook = {};
rows.forEach(r => { perBook[r.L.b] = (perBook[r.L.b] || 0) + 1; });
const cut = (s, n) => String(s || '').replace(/\s+/g, ' ').trim().slice(0, n);
const csv = ['book,unit,question_no,part,kind,question,answer_shown,printed_key'].concat(rows.map(r => [r.L.b, r.L.u + 1, r.L.no, r.L.pn, r.kind, cut(first(r.L.q), 160), cut(String(r.L.a || '') + ' ' + String(r.L.st || ''), 200), cut(r.L.kt, 160)].map(v => '"' + String(v).replace(/"/g, '""') + '"').join(',')));
fs.writeFileSync(path.join(OUT, 'answer_match_findings.csv'), csv.join('\n') + '\n');

const md = ['# Answer and question match audit', '', 'Generated by `node --max-old-space-size=6144 tools/launch/answer_match_audit.js` (do not edit by hand). It compares each question with its answer by content; **it cannot prove an answer right, it lists answers that disagree with the printed key of their book or stand under unrelated questions.** Method and limits: the header of `tools/launch/answer_match_audit.js`.', '',
  '* Questions and parts with an answer: ' + looked + '; of them with a written solution AND a printed key line to compare: ' + keyed + '; long answers sharing nothing with the question (information only): ' + weak + ' of ' + compared + '; known and explained differences (the solution itself says the printed key is wrong): ' + acknowledged + '; **findings: ' + rows.length + '** (`key-mismatch` ' + rows.filter(r => r.kind === 'key-mismatch').length + ', `shared` ' + rows.filter(r => r.kind === 'shared').length + ').', '',
  '## Findings per book', '', '| Book | Findings |', '|---|---:|'].concat(Object.entries(perBook).sort((x, y) => y[1] - x[1]).map(([b, n]) => '| ' + b + ' | ' + n + ' |'));
md.push('', '## The first 150 findings (the full list is `answer_match_findings.csv`)', '', '| Book | Unit | No. | Kind | Question | Answer shown | Printed key |', '|---|---:|---|---|---|---|---|');
rows.slice(0, 150).forEach(r => md.push('| ' + r.L.b + ' | ' + (r.L.u + 1) + ' | ' + String(r.L.no || '') + String(r.L.pn || '') + ' | ' + r.kind + ' | ' + cut(first(r.L.q), 80).replace(/\|/g, '/') + ' | ' + cut(r.L.a, 70).replace(/\|/g, '/') + ' | ' + cut(r.L.kt, 70).replace(/\|/g, '/') + ' |'));
fs.writeFileSync(path.join(OUT, 'ANSWER_MATCH_AUDIT.md'), md.join('\n') + '\n');

console.log('answer match audit: ' + looked + ' answered questions, ' + keyed + ' with a written solution and a printed key to compare, ' + rows.length + ' findings (key-mismatch ' + rows.filter(r => r.kind === 'key-mismatch').length + ', shared ' + rows.filter(r => r.kind === 'shared').length + '); explained by the solution itself: ' + acknowledged + '; weak overlap, information only: ' + weak + ' of ' + compared);
Object.entries(perBook).sort((x, y) => y[1] - x[1]).slice(0, 12).forEach(([b, n]) => console.log('  ' + b + ': ' + n));
if (args.includes('--write-baseline')) { fs.writeFileSync(BASE, JSON.stringify({ perBook }, null, 1) + '\n'); console.log('baseline written'); }
if (args.includes('--check')) {
  const base = fs.existsSync(BASE) ? JSON.parse(fs.readFileSync(BASE, 'utf8')).perBook : {};
  const worse = Object.entries(perBook).filter(([b, n]) => n > (base[b] || 0));
  if (worse.length) { console.log('FAIL  more findings than the baseline: ' + worse.map(([b, n]) => b + ' ' + (base[b] || 0) + ' -> ' + n).join(', ')); process.exit(1); }
  console.log('PASS  no book has more findings than its baseline');
}
