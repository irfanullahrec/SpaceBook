'use strict';
/* Automatic proofreading scan of the Class 11/12 data files: strings with the typical marks of a bad transcription.
 *   node tools/qa/proof_scan.js [--json out.json] [--show N]
 * It cannot compare with the scans; it only lists suspicious strings (repeated words, glued words, OCR confusions, unbalanced brackets,
 * replacement characters). Each hit still has to be judged against the page image. Math, code and SVG strings are skipped. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const dir = path.resolve(__dirname, '..', '..', 'js');
const files = fs.readdirSync(dir).filter(f => /^(?!sent_data)(.*(_11_|_12_|math11|math12|class1[12]).*)\.js$/.test(f) && /_data\.js$|book_data\.js$/.test(f) && !/translat|study_views|recovery|answer_repairs|reader|^sb_|^vr_|lexicon/.test(f));
const SKIPKEY = /^(svg|svgUrdu|svgPashto|diagramSvg|tex|latex|m|code|formula|d|path|html|src|id|sourcePdf|jpg|stroke|fill)$/;
const OCR = /\b(tbe|tlie|thc|wliich|wbich|arid|ofthe|inthe|tha t|tbat|tbis|wben|wbat|witb|iu the|aud the|tlie)\b|\b[A-Za-z]*[a-z]I[a-z]+\b(?<!\bMcIntosh)|\bl[a-z]{2,}\b(?<=\b(?:lt|lf|ls)\b)/;
const KINDS = {
  repeat: s => { const m = /\b([A-Za-z]{3,})\s+\1\b/i.exec(s); return m && !/^(that|had|very|bye|tom|yo|no|so|well)$/i.test(m[1]) ? m[0] : null; },
  glued: s => { const m = /\b[a-z]{3,}(the|and|that|with|from)[a-z]{3,}\b/.exec(s); return null; },
  ocr: s => { const m = OCR.exec(s); return m ? m[0] : null; },
  brackets: s => { if (/[$\\]/.test(s) || s.length > 400) return null; let d = 0; for (const c of s) { if (c === '(') d++; else if (c === ')') d--; if (d < 0) return ')'; } return d !== 0 ? '(' : null; },
  repl: s => (/[�\u0000-\u0008]/.test(s) ? 'U+FFFD/control' : null),
  punct: s => { const m = /[,;:]{2,}|\s[,;](?=\s|$)|\.\.(?!\.)/.exec(s); return !/[$\\]/.test(s) && m ? m[0] : null; },
  lowerstart: s => (/^[a-z]{2,}\s/.test(s) && s.length > 60 && !/[$\\]/.test(s) ? s.slice(0, 20) : null)
};
const out = {}; const show = {};
for (const f of files) {
  const code = fs.readFileSync(path.join(dir, f), 'utf8').replace(/^(const|let) /gm, 'var ');
  const win = {}; const ctx = vm.createContext({ window: win, self: win, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {}, setTimeout() { }, addEventListener() { } });
  try { vm.runInContext(code, ctx, { timeout: 60000 }); } catch (e) { /* partial */ }
  const r = { strings: 0 }; for (const k of Object.keys(KINDS)) r[k] = 0; r.ex = [];
  const seen = new Set(), seenS = new Set();
  const walk = (o, key, d) => {
    if (d > 16) return;
    if (typeof o === 'string') {
      if (o.length < 25 || SKIPKEY.test(key) || /^</.test(o) || !/[A-Za-z]{3,} [A-Za-z]{3,}/.test(o) || /[؀-ۿ]/.test(o) || seenS.has(o)) return; seenS.add(o); r.strings++;
      for (const [k, fn] of Object.entries(KINDS)) { const hit = fn(o); if (hit) { r[k]++; if (r.ex.length < 400) r.ex.push([k, hit, o.slice(0, 140)]); } }
      return;
    }
    if (!o || typeof o !== 'object' || seen.has(o)) return; seen.add(o);
    for (const k of Object.keys(o)) walk(o[k], k, d + 1);
  };
  for (const k of Object.keys(ctx)) walk(ctx[k], k, 0); for (const k of Object.keys(win)) walk(win[k], k, 0);
  out[f] = r;
}
const N = +(process.argv[process.argv.indexOf('--show') + 1]) || 0;
console.log('file'.padEnd(36), 'strings', ...Object.keys(KINDS).map(k => k.padStart(8)));
for (const [f, r] of Object.entries(out)) console.log(f.padEnd(36), String(r.strings).padStart(7), ...Object.keys(KINDS).map(k => String(r[k]).padStart(8)));
if (N) for (const [f, r] of Object.entries(out)) r.ex.filter(e => e[0] !== 'lowerstart').slice(0, N).forEach(e => console.log(f.slice(0, 22), e[0], JSON.stringify(e[1]), '|', e[2]));
const ji = process.argv.indexOf('--json'); if (ji > 0) fs.writeFileSync(process.argv[ji + 1], JSON.stringify(out, null, 1));
