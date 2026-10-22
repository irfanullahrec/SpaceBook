'use strict';
/* Document-order stream of the Urdu text of an Urdu-source book, for reading it against the scans in order.
 *   node tools/qa/stream.js <js data file> <out.txt>
 * Urdu strings only (Pashto lines are dropped by their letters), nested duplicates removed, paragraph per line, "¶n" index in front. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const f = path.resolve(__dirname, '..', '..', 'js', process.argv[2].replace(/^js[\\/]/, ''));
const code = fs.readFileSync(f, 'utf8').replace(/^(const|let) /gm, 'var ');
const win = {}; const ctx = vm.createContext({ window: win, self: win, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {}, setTimeout() { }, addEventListener() { } });
try { vm.runInContext(code, ctx, { timeout: 120000 }); } catch (e) { }
const PS = /[ډځڅښږړۍېڼګۓ]/;
const SKIP = /^(id|sourcePdf|jpg|svg|tex|latex|code|path|d|html|content|theory|sciNote|urdu|pashto|titleUrdu|titlePashto|headingPashto|text_ps)$/;
const out = []; const seen = new Set(); const seenO = new Set();
function add(s) { s = s.trim(); if (s.length < 6 || PS.test(s) || seen.has(s)) return; if ((s.match(/[؀-ۿ]/g) || []).length < 6) return; seen.add(s); out.push(s); }
function walk(o, key, d) {
  if (d > 18) return;
  if (typeof o === 'string') { if (!/^(id|sourcePdf|jpg|svg|tex|latex|code|path|d|html|content|theory|sciNote)$/.test(key) && !/^</.test(o)) for (const p of o.split(/\n+/)) add(p); return; }
  if (!o || typeof o !== 'object' || seenO.has(o)) return; seenO.add(o);
  if (Array.isArray(o)) { for (const v of o) walk(v, key, d + 1); return; }
  // in-order: text-like keys first so a record reads naturally
  const ks = Object.keys(o); for (const k of ks) walk(o[k], k, d + 1);
}
for (const k of Object.keys(ctx)) walk(ctx[k], k, 0); for (const k of Object.keys(win)) walk(win[k], k, 0);
// drop strings that are contained in a longer string (section text repeats its paragraphs)
const big = out.join('\n'); const keep = out.filter((s, i) => !out.some((t, j) => j !== i && t.length > s.length + 20 && t.includes(s)));
fs.writeFileSync(process.argv[3], keep.map((s, i) => '¶' + (i + 1) + ' ' + s).join('\n'));
console.log(path.basename(f), 'paragraphs', keep.length, 'chars', keep.join('').length);
