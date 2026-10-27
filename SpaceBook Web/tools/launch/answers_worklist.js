'use strict';
/* The questions of a book that have no answer, ready to be answered, and the step that puts the answers into the book's page files.
 *
 *   node --max-old-space-size=6144 tools/launch/answers_worklist.js list <book> [--dir <folder>]
 *        <book> is a registry id such as cls11:chem (see docs/launch/EXERCISE_COVERAGE.md). Writes <folder>/<book>.work.txt: one block per chapter, one numbered
 *        line per unanswered question with its printed page, exercise, number and words, then the lesson text of the chapter to answer from, and
 *        <folder>/<book>.map.json: for each number the page file and the line of its question. Default folder: .launch-answers/ (git-ignored).
 *   node tools/launch/answers_worklist.js apply <book> <answers.tsv> [--dir <folder>] [--dry]
 *        answers.tsv: lines   <number><TAB><answer> ## <reason>    (a line that starts with # is a comment). Each answer is inserted as a  sol  line right after
 *        its question in the page file, in the language of the question (the page syntax: docs/source-verification/class-6/tools/build_math6.py). Nothing
 *        else in a page file changes. Then rebuild the book (python -X utf8 tools/build_book11.py KEY from docs/source-verification/class-12; wire_book11.py).
 *   node tools/launch/answers_worklist.js check <answers.tsv>   every answer line has a number and a non-empty answer, no tab or || inside, numbers are unique.
 * Why page files: they are the source of the books (the generated js is rebuilt from them), so an answer written here survives every rebuild, is reviewed in a
 * diff, and reaches the Android app with the next sync. An answer inserted this way is shown by the app as "SpaceBook answer, not printed in the textbook".
 * Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const cmd = args[0], book = args[1];
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const DIR = path.resolve(ROOT, opt('--dir', '.launch-answers'));
const SV = path.join(ROOT, 'docs', 'source-verification');

// which folder holds the page files of a registry id
function pagesDir(id) {
  const m = /^cls(\d+):(.+)$/.exec(id); if (!m) throw new Error('book id like cls11:chem');
  const alias = { islc: 'isl', islopt: m[1] === '11' ? 'ikhtiari' : 'islopt', quran: m[1] === '11' ? 'mq' : 'quran', islhist: m[1] === '11' ? 'ishist' : 'islhist', comp: m[1] === '11' ? 'cs' : 'comp', phys: 'phys' };
  for (const d of [alias[m[2]], m[2]].filter(Boolean)) { const p = path.join(SV, 'class-' + m[1], d, 'pages'); if (fs.existsSync(p)) return p; }
  throw new Error('no page files for ' + id);
}
const pageFiles = dir => fs.readdirSync(dir).filter(f => /^p\d+\.txt$/.test(f)).sort();
const QLINE = /^qp?[ \t]/;                       // q = a question, qp = a part of a question (the page syntax of the Class 6-12 books)
const eng = line => line.replace(/^qp?\s*[^|]*\|\s?/, '').split(' || ')[0].trim();
const qNo = line => { const m = /^q\s*([^|]*)\|/.exec(line); return m ? m[1].trim() : null; };
const norm = s => String(s || '').replace(/\s+/g, ' ').trim();

if (cmd === 'check') {
  const f = args[1]; let bad = 0; const seen = new Set();
  fs.readFileSync(f, 'utf8').split(/\r?\n/).forEach((l, i) => {
    if (!l.trim() || l.startsWith('#')) return;
    const t = l.indexOf('\t');
    const id = t > 0 ? l.slice(0, t) : '', a = t > 0 ? l.slice(t + 1) : '';
    const why = !/^\d+$/.test(id) ? 'no number' : seen.has(id) ? 'number used twice' : !a.trim() ? 'empty answer' : /\t/.test(a) ? 'a tab inside' : /\|\|/.test(a) ? 'a || inside (that is the language separator of a page line)' : '';
    seen.add(id);
    if (why) { bad++; console.error(`line ${i + 1}: ${why}`); }
  });
  console.log(bad ? bad + ' problems' : 'answers file ok (' + seen.size + ' answers)'); process.exit(bad ? 1 : 0);
}

if (cmd === 'list') {
  // 1. the unanswered questions, from the audit (the reader's own answer lookup)
  const tmp = path.join(require('os').tmpdir(), 'sb_wl_audit_' + process.pid + '.json');
  cp.execFileSync(process.execPath, ['--max-old-space-size=6144', path.join(ROOT, 'tools', 'audit', 'answers_audit.js'), '--json', tmp], { stdio: 'ignore', maxBuffer: 1 << 28 });
  const audit = JSON.parse(fs.readFileSync(tmp, 'utf8')); fs.unlinkSync(tmp);
  // 2. the lesson text of each chapter (to answer from)
  const { load } = require('../lib/app_sandbox');
  const extract = require('../tests/extract_leaves');
  const app = load({ page: 'lazy.html', quiet: true });
  const raw = JSON.parse(app.run('JSON.stringify((' + extract.toString() + ')())', 900000));
  for (const book of args[1].split(',')) {            // several books at once: cls11:civics,cls11:stat
  const rec = audit.find(b => b.id === book);
  if (!rec) { console.error('no such book in the audit: ' + book); continue; }
  const miss = rec.missing.filter(m => m.why === 'none');
  const bk = raw.books.find(b => b.id === book);
  // 3. the page files: every q line, by printed page
  const dir = pagesDir(book), files = pageFiles(dir), byPrinted = new Map();
  files.forEach(f => {
    const lines = fs.readFileSync(path.join(dir, f), 'utf8').split(/\r?\n/);
    const m = /^@printed\s+(\S+)/m.exec(lines.join('\n')); const pr = m ? m[1] : '';
    if (!byPrinted.has(pr)) byPrinted.set(pr, []);
    byPrinted.get(pr).push({ f, lines });
  });
  const map = {}, out = [];
  let n = 0, unmatched = 0;
  const units = new Map();
  for (const m of miss) {
    const u = /unit (\S+)/.exec(m.loc); const key = u ? u[1] : '?';
    if (!units.has(key)) units.set(key, []);
    units.get(key).push(m);
  }
  for (const [u, list] of units) {
    const bu = bk && bk.units.find(x => String(x.n) === u);
    out.push(`\n########## UNIT ${u}  ${bu ? bu.title : ''}  (${list.length} unanswered)`);
    for (const m of list) {
      const want = norm(m.node && m.node.en);
      let hit = null;
      const cands = [];
      for (const pr of [String(m.pg), String(+m.pg + 1), String(+m.pg - 1)]) for (const pf of byPrinted.get(pr) || []) cands.push(pf);
      for (const pf of cands) { for (let i = 0; i < pf.lines.length && !hit; i++) { const l = pf.lines[i]; if (QLINE.test(l) && norm(eng(l)) === want) hit = { f: pf.f, i }; } if (hit) break; }
      if (!hit) { unmatched++; for (const pf of cands) for (let i = 0; i < pf.lines.length && !hit; i++) if (QLINE.test(pf.lines[i]) && want && norm(eng(pf.lines[i])).startsWith(want.slice(0, 30))) hit = { f: pf.f, i }; }
      if (!hit && want) {                          // the printed page the audit gives can be off by more than one: take the one page file that holds exactly this question
        const all = [];
        for (const arr of byPrinted.values()) for (const pf of arr) for (let i = 0; i < pf.lines.length; i++) if (QLINE.test(pf.lines[i]) && norm(eng(pf.lines[i])) === want) all.push({ f: pf.f, i });
        if (all.length === 1) hit = all[0];
      }
      n++;
      map[n] = hit ? { file: path.relative(ROOT, path.join(dir, hit.f)).replace(/\\/g, '/'), line: hit.i + 1, text: want.slice(0, 60) } : null;
      out.push(`[${n}] p${m.pg == null ? '?' : m.pg} ${m.loc.replace(/^unit \S+ ?/, '')}${hit ? '' : '  (NOT FOUND IN PAGE FILES)'} | ${want}`);
    }
    if (bu) {
      const txt = bu.secs.filter(s => !s.ex).map(s => `${s.t ? '## ' + s.t + '\n' : ''}${s.text}`).join('\n').replace(/\s+/g, ' ').slice(0, +opt('--chars', 6000));
      out.push(`--- lesson text of unit ${u} (first ${txt.length} characters) ---\n${txt}`);
    }
  }
  fs.mkdirSync(DIR, { recursive: true });
  const base = path.join(DIR, book.replace(':', '_'));
  fs.writeFileSync(base + '.work.txt', out.join('\n') + '\n');
  fs.writeFileSync(base + '.map.json', JSON.stringify(map, null, 0));
  console.log(`${book}: ${n} unanswered questions in ${units.size} chapters (${unmatched} not found in page files) -> ${path.relative(ROOT, base)}.work.txt`);
  }
  process.exit(0);
}

if (cmd === 'apply') {
  const tsv = args[2], dry = args.includes('--dry');
  const map = JSON.parse(fs.readFileSync(path.join(DIR, book.replace(':', '_') + '.map.json'), 'utf8'));
  const answers = [];
  fs.readFileSync(tsv, 'utf8').split(/\r?\n/).forEach(l => { if (!l.trim() || l.startsWith('#')) return; const t = l.indexOf('\t'); answers.push([l.slice(0, t), l.slice(t + 1).trim()]); });
  const byFile = new Map(); let missing = 0;
  for (const [id, a] of answers) {
    const m = map[id]; if (!m) { console.error('no place for answer ' + id); missing++; continue; }
    if (!byFile.has(m.file)) byFile.set(m.file, []);
    byFile.get(m.file).push({ line: m.line, text: m.text, a });
  }
  let done = 0;
  for (const [f, list] of byFile) {
    const p = path.join(ROOT, f), raw = fs.readFileSync(p, 'utf8'), nl = raw.includes('\r\n') ? '\r\n' : '\n', lines = raw.split(/\r?\n/);
    list.sort((x, y) => y.line - x.line);          // from the bottom up, so the lines above keep their numbers
    for (const e of list) {
      const l = lines[e.line - 1];
      if (!QLINE.test(l) || !norm(eng(l)).startsWith(e.text.slice(0, 30))) { console.error(`${f}:${e.line} is not the question any more ("${e.text}")`); missing++; continue; }
      if (/^sol /.test(lines[e.line] || '')) { console.error(`${f}:${e.line} already has an answer line`); missing++; continue; }
      lines.splice(e.line, 0, 'sol ' + e.a);
      done++;
    }
    if (!dry) fs.writeFileSync(p, lines.join(nl));
  }
  console.log(`${dry ? '(dry run) ' : ''}${done} answers inserted in ${byFile.size} page files, ${missing} problems`);
  process.exit(missing ? 1 : 0);
}
console.error('usage: answers_worklist.js list <book> | apply <book> <answers.tsv> | check <answers.tsv>'); process.exit(2);
