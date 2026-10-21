'use strict';
/* Prints the scan path and the data text of one or more pages for visual proofreading.
 *   node tools/qa/qa_page.js <book> <page> [page ...]        (pages are PDF page numbers; JPG = N-th file in sorted order)
 * book = hpe12 | pak12 | isl12 | ihist12 | quran12 | econ12 | urdu12 ... (see BOOKS).  Urdu-source books print the Urdu strings only (Pashto
 * translations are dropped by script: they contain letters that Urdu does not use); English books print the English strings. */
const fs = require('fs'), path = require('path');
const BOOKS = {
  hpe12: ['12th/12th HPE', 'hpe12_ur', 1], pak12: ['12th/12th Pak Studies', 'pakstudy_12_data', 1], isl12: ['12th/12th Islamiat Ikhtiari', 'islamiat_ikhtiari_12_data', 1],
  ihist12: ['12th/12th Islamic History', 'islamic_history_12_data', 1], quran12: ['12th/12th Mutalia e Quran', 'quran_12_data', 1], econ12: ['12th/12th Economics', 'economics_12_data', 1],
  urdu12: ['12th/12th Urdu', 'urdu_12_data', 1]
};
const ROOT = 'D:/SpaceBook/Books/';
const PS = /[\u0689\u0681\u0685\u069A\u0696\u0693\u06CD\u06D0\u06BC\u06AB]/;   // ډ ځ څ ښ ږ ړ ۍ ې ڼ ګ : Pashto-only letters
const [bk, ...pgs] = process.argv.slice(2);
const B = BOOKS[bk]; if (!B) { console.log('unknown book', bk, Object.keys(BOOKS).join(' ')); process.exit(1); }
const pagesFile = 'D:/SpaceBook/_qa/pages/' + B[1] + (B[1].endsWith('_ur') ? '' : '_ur') + '.json';
const pages = JSON.parse(fs.readFileSync(pagesFile, 'utf8'));
const dir = ROOT + B[0] + '/JPG';
const files = fs.readdirSync(dir).filter(f => /\.jpg$/i.test(f)).sort();
for (const p of pgs) {
  const seen = new Set(); const out = [];
  for (const s of pages[p] || []) { if (PS.test(s) || seen.has(s)) continue; seen.add(s); out.push(s); }
  const outF = out.filter(x => !out.some(y => y !== x && y.includes(x) && y.length > x.length));
  console.log('=== ' + bk + ' pdf ' + p + ' -> ' + (files[p - 1] || '?') + '\nSCAN: ' + dir + '/' + (files[p - 1] || '') + '\n' + outF.join('\n¶ '));
}
