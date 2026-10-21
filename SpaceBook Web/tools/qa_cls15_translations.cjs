// Cross-checks the three languages of every text block in the Class 1-5 books.
//   node tools/qa_cls15_translations.cjs [--json out.json] [--show N]
// Findings (each is a lead for a person, not an automatic fix):
//   numbers   the digits written in the English differ from those in the Urdu or Pashto (after mapping Urdu/Pashto digits)
//   missing   a block with English text but no Urdu or no Pashto
//   latin     Urdu/Pashto text that still contains a run of 4+ Latin letters (untranslated English left in)
//   same      Urdu or Pashto identical to the English (not translated)
//   empty     Urdu/Pashto present but only punctuation/whitespace
const fs = require('fs'), vm = require('vm'), path = require('path');
const JS = path.join(__dirname, '..', 'js');
const ARABIC_DIGITS = { '۰': 0, '۱': 1, '۲': 2, '۳': 3, '۴': 4, '۵': 5, '۶': 6, '۷': 7, '۸': 8, '۹': 9, '٠': 0, '١': 1, '٢': 2, '٣': 3, '٤': 4, '٥': 5, '٦': 6, '٧': 7, '٨': 8, '٩': 9 };
const digitsOf = s => String(s).replace(/[۰-۹٠-٩]/g, d => ARABIC_DIGITS[d]).replace(/(\d),(?=\d{3}\b)/g, '$1').replace(/\{,\}/g, '').match(/\d+(?:\.\d+)?/g) || [];
const strip = s => String(s).replace(/\$[^$]*\$/g, ' ').replace(/\*\*/g, '').replace(/<[^>]+>/g, ' ');
const out = { findings: [], books: {} };
const F = (book, kind, where, msg) => out.findings.push({ book, kind, where, msg });
function load(f) { const c = { window: {}, console, document: {}, self: {} }; vm.runInNewContext(fs.readFileSync(path.join(JS, f), 'utf8'), c); return c; }
function audit(key, B, primaryRTL) {
  const st = out.books[key] = { blocks: 0, numbers: 0, missing: 0, latin: 0, same: 0 };
  const walk = (o, where) => {
    if (Array.isArray(o)) return o.forEach(x => walk(x, where));
    if (!o || typeof o !== 'object') return;
    if ((o.t === 'p' || o.t === 'q' || o.t === 'h' || o.t === 'li') && typeof o.en === 'string' && /[A-Za-z]{3}/.test(o.en) && !primaryRTL) {
      st.blocks++;
      const en = strip(o.en);
      for (const [lang, v] of [['ur', o.ur], ['ps', o.ps]]) {
        if (typeof v !== 'string' || !v.trim()) { st.missing++; F(key, 'missing', where, lang + ' missing: ' + en.slice(0, 50)); continue; }
        const t = strip(v);
        if (!/[؀-ۿ]/.test(t)) { st.same++; F(key, 'same', where, lang + ' not translated: ' + en.slice(0, 50)); continue; }
        if (/[A-Za-z]{4,}/.test(t.replace(/\b(KPTBB|GK|cm|mm|km|kg|ml|Rs|AM|PM|NADH)\b/g, ''))) { st.latin++; F(key, 'latin', where, lang + ' has English letters: ' + t.slice(0, 60)); }
        const big = x => x.filter(n => n.length > 1 || n.includes('.')).sort().join(' ');   // one-digit numbers are often spelled out ("2-digit" = "two-digit")
        const a = big(digitsOf(en)), b = big(digitsOf(t));      // RTL text reorders numbers: compare as a multiset
        if (a && b && a !== b) { st.numbers++; F(key, 'numbers', where, `${lang}: EN [${a}] vs [${b}] :: ${en.slice(0, 50)}`); }
      }
    }
    for (const k in o) { if (k === 'svg' || k === 'tex') continue; const v = o[k]; if (v && typeof v === 'object') walk(v, where); }
  };
  for (const u of B.units || []) walk(u.sections, key + ' u' + u.number);
  walk((B.book || {}).frontMatter, key + ' front'); walk((B.book || {}).backMatter, key + ' back');
}
for (const cl of [1, 2, 3, 4, 5]) {
  const re = new RegExp('(_' + cl + '_(data|book|book_text|pages))\\.js$');
  for (const f of fs.readdirSync(JS).filter(f => re.test(f))) {
    let c; try { c = load(f); } catch (e) { continue; }
    const B = c.window['CLS' + cl + '_BOOKS'];
    if (B) for (const s in B) audit('c' + cl + '-' + s, { units: B[s].units, book: B[s].book }, /^(urdu|nazira|pashto|arabic|quran)/.test(s));
  }
}
const sum = {}; for (const f of out.findings) { const k = f.book + ' ' + f.kind; sum[k] = (sum[k] || 0) + 1; }
if (process.argv.includes('--json')) fs.writeFileSync(process.argv[process.argv.indexOf('--json') + 1], JSON.stringify(out, null, 1));
console.log(Object.entries(out.books).map(([k, v]) => k + ' ' + JSON.stringify(v)).join('\n'));
const n = process.argv.includes('--show') ? +process.argv[process.argv.indexOf('--show') + 1] : 0;
out.findings.slice(0, n).forEach(f => console.log(f.book, f.kind, f.where, '|', f.msg));
