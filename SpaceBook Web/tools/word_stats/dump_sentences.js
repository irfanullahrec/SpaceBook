'use strict';
/* Dumps every English (Latin-script) sentence of the book data with the classes that use it, for the offline translation store.
 *   node --max-old-space-size=8192 tools/word_stats/dump_sentences.js <out.json>   */
const fs = require('fs'), path = require('path');
const W = require('./build_word_stats.js');
const { JS, subjectForFile, evaluate, SKIP_FILES, DATA_KEY_FILES } = W;
const SKIP_KEY = /^(id|ids|.*Id|.*Ids|uid|key|keys|ref|refs|slug|type|kind|status|layout|align|dir|lang|style|styles|css|class|cls|className|color|colour|colors|bg|background|icon|img|image|images|src|href|url|path|file|files|svg|figure|figures|fig|figs|latex|tex|formula|katex)$/i;
const PLACEHOLDER = /^(اردو ترجمہ دستیاب ہے۔|د پښتو ژباړه شتون لري\.)$/;
const arabicText = x => typeof x === 'string' && (x.match(/[؀-ۿ]/g) || []).length >= 3 && !PLACEHOLDER.test(x.trim());
// translated: true while the strings being read sit in an object that also carries a real Urdu and a real Pashto text
function walk(v, on, seen, translated) {
  if (v == null) return;
  if (typeof v === 'string') return on(v, !!translated);
  if (typeof v !== 'object' || seen.has(v)) return;
  seen.add(v);
  if (Array.isArray(v)) { v.forEach(x => walk(x, on, seen, translated)); return; }
  const ks = Object.keys(v);
  const val = k => { try { return v[k]; } catch (e) { return undefined; } };
  const here = ks.some(k => /^(ur|urdu)$/i.test(k) && arabicText(val(k))) && ks.some(k => /^(ps|pashto)$/i.test(k) && arabicText(val(k)));
  for (const k of ks) { if (SKIP_KEY.test(k)) continue; walk(val(k), on, seen, here || (translated && typeof val(k) === 'string')); }
}
const D = W.loadCatalogue();
const out = new Map();   // sentence -> {n, cls:Set, subj:Set}
function addText(txt, sid, tr) {
  let t = txt.replace(/<(script|style|svg|math)\b[\s\S]*?<\/\1>/gi, ' ').replace(/<[^>]*>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&[a-z]+;|&#\d+;/gi, ' ');
  t = t.replace(/\$\$[\s\S]*?\$\$/g, ' ').replace(/\$[^$\n]{0,400}\$/g, ' ').replace(/\s+/g, ' ').trim();
  if (!/[A-Za-z]{2}/.test(t)) return;
  const parts = t.split(/(?<=[.!?])\s+(?=[A-Z"'(\[])/);
  for (const p0 of parts) {
    const p = p0.trim();
    if ((p.match(/[A-Za-z]+/g) || []).length < 1) continue;
    const lat = (p.match(/[A-Za-z]/g) || []).length, ara = (p.match(/[\u0600-\u06FF]/g) || []).length;
    if (ara > 0) continue;               // mixed or non-English: not a source sentence
    if (lat < 3) continue;
    let r = out.get(p); if (!r) out.set(p, r = { n: 0, t: 0, c: new Set() });
    r.n++; if (tr) r.t++; r.c.add(sid.split('-')[0]);
  }
}
const files = fs.readdirSync(JS).filter(f => f.endsWith('.js') && !SKIP_FILES.has(f) && !/reader\.js$/.test(f)).sort();
for (const file of files) {
  const sid = subjectForFile(file, D.subjects), keyed = DATA_KEY_FILES[file];
  if (!sid && !keyed) continue;
  let ev; try { ev = evaluate(file); } catch (e) { console.error('FAIL', file); continue; }
  if (keyed) { for (const [k, v] of Object.entries(ev.data)) walk(v, (t, tr) => addText(t, (/10/.test(k) ? 'cls10' : 'cls9') + '-' + keyed, tr), new Set()); continue; }
  walk([...Object.values(ev.globals), ev.data], (t, tr) => addText(t, sid, tr), new Set());
}
const rows = [...out.entries()].map(([s, r]) => ({ s, n: r.n, t: r.t, c: [...r.c].sort() }));
fs.writeFileSync(process.argv[2], JSON.stringify(rows));
console.log('unique sentences', rows.length, 'total chars', rows.reduce((a, r) => a + r.s.length, 0));
