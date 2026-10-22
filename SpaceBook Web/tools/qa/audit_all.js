'use strict';
/* QA audit for every class that has CLSn_BOOKS page books (Classes 1-10, 12 Maths/Stat) — dev only.
 *   node --max-old-space-size=8192 tools/qa/audit_c9_c10.js [--dump <dir>] [--json out.json]
 * Loads index.html in the sandbox, dumps books + answer store, then checks per book: answers coverage (q -> solId -> solution),
 * MCQs without a key, text anomalies (replacement chars, stray control chars, unbalanced $, KaTeX failures, empty text),
 * page order (printed number gaps/duplicates), unclosed/empty structures. */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('../lib/app_sandbox');
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
let katex = null; try { katex = require(path.join(ROOT, 'assets', 'vendor', 'katex', 'katex.min.js')); } catch (e) { /* optional */ }

const cache = opt('--cache');
let data;
if (cache && fs.existsSync(cache)) data = JSON.parse(fs.readFileSync(cache, 'utf8'));
else {
  const app = load({ page: 'index.html', quiet: true });
  data = JSON.parse(app.run(`(function(){var r={sols:{}};for(var n=1;n<=12;n++){try{Object.assign(r.sols,window['CLS'+n+'_SOLUTIONS']||{});}catch(e){}try{r['c'+n]=eval('CLS'+n+'_BOOKS');}catch(e){}}return JSON.stringify(r);})()`, 600000));
  if (cache) fs.writeFileSync(cache, JSON.stringify(data));
}
const sols = data.sols;
const report = { books: {} };
const MCQ_RE = /\(\s*a\s*\)[\s\S]*\(\s*b\s*\)[\s\S]*\(\s*c\s*\)|(?:^|\s)a[.)]\s[\s\S]*\sb[.)]\s[\s\S]*\sc[.)]\s/i;
const texFail = new Map();
function checkTeX(src, where, b) {
  if (!katex) return;
  const key = src;
  if (texFail.has(key) && texFail.get(key) === true) return;
  try { katex.renderToString(src, { throwOnError: true, strict: 'ignore', trust: true, macros: {} }); texFail.set(key, true); }
  catch (e) { b.texErrors.push({ where, tex: src.slice(0, 120), err: String(e.message).slice(0, 100) }); }
}

const normT = t => String(t || '').toLowerCase().replace(/\$|\\[a-z]+|[{}^_\\]/g, '').replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
function mcqOptions(text) {
  const t = String(text), re = /(?:\(\s*([a-dA-D])\s*\)|(?:^|\s)([A-D])[.)](?=\s))/g, hits = [];
  let m; while ((m = re.exec(t))) hits.push({ k: (m[1] || m[2]).toLowerCase(), at: m.index, end: re.lastIndex });
  const order = 'abcd'; const seq = []; let want = 0;
  for (const h of hits) if (h.k === order[want]) { seq.push(h); want++; if (want === 4) break; }
  if (seq.length < 3) return null;
  const o = {}; seq.forEach((h, i) => { o[h.k] = t.slice(h.end, i + 1 < seq.length ? seq[i + 1].at : t.length).trim(); });
  return o;
}
function answerLetter(a) {
  const m = String(a || '').match(/^\s*\(?\s*([a-dA-D])\s*[).]/); if (m) return { k: m[1].toLowerCase(), rest: String(a).slice(m[0].length).trim() };
  const u = String(a || '').match(/^\s*\(?\s*(الف|ب|ج|د)\s*\)?/); if (u) return { k: 'abcd'['الف ب ج د'.split(' ').indexOf(u[1])], rest: String(a).slice(u[0].length).trim() };
  return null;
}
function strs(o, f, p) {
  if (typeof o === 'string') return f(o, p);
  if (Array.isArray(o)) return o.forEach((x, i) => strs(x, f, p + '[' + i + ']'));
  if (o && typeof o === 'object') for (const k in o) strs(o[k], f, p + '.' + k);
}
for (const cls of Object.keys(data).filter(k => /^c\d+$/.test(k))) for (const sub in data[cls]) {
  const bk = data[cls][sub];
  const b = report.books[cls + '/' + sub] = {
    pages: 0, printedGaps: [], printedDups: [], emptyPages: [], leaves: 0, withSol: 0, solMissing: [], solEmpty: [], mcq: 0, mcqNoKey: [], units: bk.units.length,
    anomalies: [], mcqMismatch: [], texErrors: [], unclosedExamples: 0, noText: []
  };
  const pages = [];
  let curPage = null;
  const visit = (blk, ctx) => {
    if (!blk) return;
    if (Array.isArray(blk)) return blk.forEach(x => visit(x, ctx));
    if (typeof blk !== 'object') return;
    if (blk.t === 'page') { curPage = { pdf: blk.pdf, printed: blk.printed, n: 0 }; pages.push(curPage); return; }
    if (curPage) curPage.n++;
    const where = `${cls}/${sub} pdf${curPage ? curPage.pdf : '?'}`;
    // text checks
    for (const k of ['en', 'ur', 'ps', 'ar', 'text']) if (typeof blk[k] === 'string') {
      const s = blk[k];
      if (/\uFFFD|[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(s)) b.anomalies.push({ where, why: 'bad-char', s: s.slice(0, 80) });
      if (blk.t !== 'm' && blk.t !== 'eq' && / {2,}/.test(s.replace(/\$[^$]*\$/g, ''))) b.anomalies.push({ where, why: 'double-space', s: s.slice(0, 80) });
      const d = (s.replace(/\\$/g, '').match(/\$/g) || []).length;
      if (d % 2) b.anomalies.push({ where, why: 'odd-$', s: s.slice(0, 100) });
      if (/\?\?|\[\?\]|\bTODO\b|lorem|ï¿½|Ã©|â€/i.test(s)) b.anomalies.push({ where, why: 'junk', s: s.slice(0, 80) });
      if (/([A-Za-z\u0600-\u06FF])\1{4,}/.test(s)) b.anomalies.push({ where, why: 'repeat', s: s.slice(0, 80) });
      const m = s.match(/\$([^$]+)\$/g); if (m) m.forEach(x => checkTeX(x.slice(1, -1), where, b));
    }
    if (blk.t === 'm' && typeof blk.en === 'string' && !/\$/.test(blk.en)) checkTeX(blk.en, where, b);
    if (blk.t === 'eq' && typeof blk.tex === 'string') checkTeX(blk.tex, where, b);
    if (blk.t === 'q') {
      const leaves = blk.parts && blk.parts.length ? blk.parts : [blk];
      for (const lf of leaves) {
        if (lf === blk && blk.parts && blk.parts.length) continue;
        const text = lf.en || lf.ur || lf.ps || '';
        if (lf === blk && !text) continue;
        // a heading-only "q" (e.g. "Short Questions") has no solId and no parts: skip
        if (!lf.solId && lf === blk && /^(Short|Long|Multiple|Comprehension|Choose|Fill|True|Match|Write)/i.test(text) && text.length < 60) continue;
        b.leaves++;
        const isMcq = MCQ_RE.test(String(text));
        if (isMcq) b.mcq++;
        if (lf.solId) {
          b.withSol++;
          const so = sols[lf.solId];
          if (!so) b.solMissing.push(lf.solId);
          else {
            const has = (so.steps && so.steps.length && so.steps.some(x => (typeof x === 'string' ? x : (x.en || x.ur || x.ps || x.text || '')).trim())) || (so.answer && String(so.answer).trim());
            if (!has) b.solEmpty.push(lf.solId);
            { const blob = JSON.stringify(so); if (/not verified/i.test(blob)) b.notVerified = (b.notVerified||0)+1; else if (/derived/i.test(blob)) b.derived = (b.derived||0)+1; }
            if (isMcq && !(so.answer && String(so.answer).trim())) b.mcqNoKey.push({ id: lf.solId, q: String(text).slice(0, 80) });
            if (isMcq && so.answer) {
              const opts = mcqOptions(text), al = answerLetter(so.answer);
              if (opts && al) {
                const o = opts[al.k];
                if (o === undefined) b.mcqMismatch.push({ id: lf.solId, why: 'letter-not-in-options', ans: String(so.answer).slice(0, 60) });
                else if (al.rest && normT(o) && !(normT(o).includes(normT(al.rest)) || normT(al.rest).includes(normT(o)))) b.mcqMismatch.push({ id: lf.solId, why: 'text-differs', ans: String(so.answer).slice(0, 60), opt: o.slice(0, 60) });
              } else if (opts && !al) b.mcqMismatch.push({ id: lf.solId, why: 'answer-not-a-letter', ans: String(so.answer).slice(0, 60) });
            }
          }
        } else if (isMcq) b.mcqNoKey.push({ id: null, q: String(text).slice(0, 80), where });
      }
    }
    if (blk.t === 'example' && (!blk.blocks || !blk.blocks.length)) b.unclosedExamples++;
    for (const k of ['blocks', 'parts', 'items', 'rows']) if (blk[k] && typeof blk[k] === 'object') visit(blk[k], ctx);
  };
  const doUnits = u => { (u.sections || []).forEach(sec => visit(sec.blocks, sec)); };
  visit(bk.book.frontMatter); bk.units.forEach(doUnits); visit(bk.book.backMatter);
  b.pages = pages.length;
  let last = null;
  pages.forEach(p => {
    if (p.n === 0) b.emptyPages.push(p.pdf);
    if (typeof p.printed === 'number') {
      if (last !== null && p.printed === last) b.printedDups.push(p.printed);
      else if (last !== null && p.printed > last + 1 && p.printed - last < 40) b.printedGaps.push(last + '→' + p.printed);
      last = p.printed;
    }
  });
}
const out = opt('--json');
if (out) fs.writeFileSync(out, JSON.stringify(report, null, 1));
const pad = (s, n) => String(s).padEnd(n);
console.log(pad('book', 16), pad('pages', 6), pad('leaves', 7), pad('withSol', 8), pad('solMiss', 8), pad('solEmpty', 9), pad('mcq', 5), pad('mcqNoKey', 9), pad('anom', 6), pad('tex', 5), pad('mism', 5), pad('empty', 6), pad('gaps', 5), 'dups');
for (const k in report.books) { const b = report.books[k]; console.log(pad(k, 16), pad(b.pages, 6), pad(b.leaves, 7), pad(b.withSol, 8), pad(b.solMissing.length, 8), pad(b.solEmpty.length, 9), pad(b.mcq, 5), pad(b.mcqNoKey.length, 9), pad(b.anomalies.length, 6), pad(b.texErrors.length, 5), pad(b.mcqMismatch.length, 5), pad(b.emptyPages.length, 6), pad(b.printedGaps.length, 5), b.printedDups.length); }
