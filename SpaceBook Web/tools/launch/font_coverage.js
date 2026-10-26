'use strict';
/* Does every Arabic-script character the books and the interface use have a glyph in the bundled font that is meant to draw it?
 *   node tools/launch/font_coverage.js [--check] [--write]
 * Characters are collected from: the typed pages of every book (docs/source-verification/**\/pages/*.txt), the generated lexicon (js/lexicon_data.js),
 * the search index (content/search/), the interface (index.html, js/app.js, js/sb_*.js, js/core/*.js). The fonts are read with fontkit
 * (assets/fonts/*.woff2). A character missing from the Nastaliq font is drawn by the next family of the stack (a system font, which a phone may not have);
 * one missing from all three is drawn as a box everywhere. --check fails on the second kind (and when css/sb_fonts.css is not what this tool makes),
 * --write writes docs/launch/FONT_COVERAGE.md, --css writes css/sb_fonts.css: each family is declared under the names the stylesheets use, and the characters
 * a family lacks are declared again from a font that has them (a second @font-face of the same name with a narrow unicode-range), so a Quranic mark inside
 * Urdu text still comes from a bundled font. Dev-only. */
const fs = require('fs'), path = require('path');
const fontkit = require('fontkit');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const FONTS = { nastaliq: 'NotoNastaliqUrdu-400.woff2', naskh: 'NotoNaskhArabic-400.woff2', amiri: 'Amiri-400.woff2' };
const cmap = {};
for (const [k, f] of Object.entries(FONTS)) {
  const font = fontkit.openSync(path.join(ROOT, 'assets', 'fonts', f));
  cmap[k] = new Set(font.characterSet);
}
// Arabic script blocks (the same list as unicode-range in css/sb_fonts.css, without the joiners and direction marks that need no glyph)
const inScript = c => (c >= 0x0600 && c <= 0x06FF) || (c >= 0x0750 && c <= 0x077F) || (c >= 0x0870 && c <= 0x08FF) || (c >= 0xFB50 && c <= 0xFDFF) || (c >= 0xFE70 && c <= 0xFEFC);
const NEEDS_NO_GLYPH = c => c === 0x200C || c === 0x200D || c === 0x200E || c === 0x200F || (c >= 0x0600 && c <= 0x0605 && false);
const count = new Map(), where = new Map();
function scan(text, label) {
  for (const ch of text) {
    const c = ch.codePointAt(0);
    if (!inScript(c)) continue;
    count.set(c, (count.get(c) || 0) + 1);
    if (!where.has(c)) where.set(c, label);
  }
}
const walk = (dir, rx, out = []) => { for (const e of fs.existsSync(dir) ? fs.readdirSync(dir, { withFileTypes: true }) : []) { const p = path.join(dir, e.name); if (e.isDirectory()) { if (!/node_modules|legacy-backup|_render|\.git/.test(e.name)) walk(p, rx, out); } else if (rx.test(e.name)) out.push(p); } return out; };
const sources = [];
for (const f of walk(path.join(ROOT, 'docs', 'source-verification'), /^p\d+\.txt$/)) sources.push(f);
sources.push(path.join(ROOT, 'js', 'lexicon_data.js'), path.join(ROOT, 'index.html'), path.join(ROOT, 'js', 'app.js'));
for (const f of walk(path.join(ROOT, 'js'), /^sb_.*\.js$/)) sources.push(f);
for (const f of walk(path.join(ROOT, 'js', 'core'), /\.js$/)) sources.push(f);
for (const f of walk(path.join(ROOT, 'content', 'search'), /\.json$/)) sources.push(f);
let files = 0;
for (const f of new Set(sources)) { if (!fs.existsSync(f)) continue; scan(fs.readFileSync(f, 'utf8'), path.relative(ROOT, f)); files++; }

const missingAll = [], missingNastaliq = [];
for (const [c, n] of [...count].sort((a, b) => b[1] - a[1])) {
  if (NEEDS_NO_GLYPH(c)) continue;
  const has = k => cmap[k].has(c);
  if (!has('nastaliq') && !has('naskh') && !has('amiri')) missingAll.push([c, n]);
  else if (!has('nastaliq')) missingNastaliq.push([c, n, has('naskh') ? 'Naskh' : 'Amiri']);
}
// ---- the stylesheet
const toRanges = list => { const cs = list.slice().sort((a, b) => a - b), out = []; for (let i = 0; i < cs.length;) { let j = i; while (j + 1 < cs.length && cs[j + 1] === cs[j] + 1) j++; out.push(i === j ? 'U+' + cs[i].toString(16).toUpperCase() : 'U+' + cs[i].toString(16).toUpperCase() + '-' + cs[j].toString(16).toUpperCase()); i = j + 1; } return out.join(','); };
const RANGE = 'U+0600-06FF,U+0750-077F,U+0870-08FF,U+200C-200F,U+FB50-FDFF,U+FE70-FEFC';
const FAMILIES = [
  { key: 'nastaliq', file: 'NotoNastaliqUrdu', weights: [400, 700], names: ['Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', 'Jameel Noor Nastaleeq', 'Urdu Typesetting', 'Nafees Nastaleeq'] },
  { key: 'naskh', file: 'NotoNaskhArabic', weights: [400, 700], names: ['Noto Naskh Arabic', 'Pashto Koodak'] },
  { key: 'amiri', file: 'Amiri', weights: [400], names: ['Amiri', 'Scheherazade New', 'Traditional Arabic', 'KFGQPC Uthman Taha Naskh', 'Lateef'] },
];
const FILEOF = { nastaliq: 'NotoNastaliqUrdu', naskh: 'NotoNaskhArabic', amiri: 'Amiri' };
const used = [...count.keys()].filter(c => !NEEDS_NO_GLYPH(c));
let css = `/* sb_fonts.css: Urdu, Pashto and Arabic fonts that travel with the site (SIL Open Font Licence 1.1, see assets/fonts/README.md).
 *
 * Before this file the stylesheets named fonts the device may or may not have ('Jameel Noori Nastaleeq', 'Noto Nastaliq Urdu', 'Amiri' ...): a phone without
 * them drew Urdu in whatever the system chose, sometimes boxes. Each name the stylesheets already use is declared here, so every existing font stack
 * resolves to a bundled file without touching them:
 *   Nastaliq  (Urdu)                      Noto Nastaliq Urdu   400 and 700   also answers to: Jameel Noori Nastaleeq, Jameel Noor Nastaleeq, Urdu Typesetting, Nafees Nastaleeq
 *   Naskh     (Pashto, Arabic, Urdu UI)   Noto Naskh Arabic    400 and 700   also answers to: Pashto Koodak
 *   Quranic Arabic                        Amiri                400           also answers to: Scheherazade New, Traditional Arabic, KFGQPC Uthman Taha Naskh, Lateef
 * A second @font-face of the same name, with a narrow unicode-range, hands the characters a family lacks (the small Quranic marks inside Urdu text, a few
 * letters) to a bundled font that has them. unicode-range keeps each file to Arabic-script characters, and a browser fetches a font only when a character of
 * that range is drawn: pages without Urdu, Pashto or Arabic download none. font-display:swap shows the text at once in the fallback and switches when the file
 * arrives. The files are in the service worker's shell (tools/build/make_offline.js reads the url() lines), so they are there offline too.
 * MADE BY tools/launch/font_coverage.js --css from the characters the books use: do not edit by hand (the check fails when this file differs). */

`;
const face = (name, file, w, range) => `@font-face{font-family:'${name}';font-style:normal;font-weight:${w};font-display:swap;src:url('../assets/fonts/${file}-${w}.woff2') format('woff2');unicode-range:${range}}\n`;
for (const fam of FAMILIES) {
  const lacking = used.filter(c => !cmap[fam.key].has(c));
  const donor = {};
  for (const c of lacking) { const d = ['naskh', 'nastaliq', 'amiri'].find(k => k !== fam.key && cmap[k].has(c)); if (d) (donor[d] = donor[d] || []).push(c); }
  for (const name of fam.names) {
    for (const w of fam.weights) css += face(name, fam.file, w, RANGE);
    for (const [d, list] of Object.entries(donor)) for (const w of (d === 'amiri' ? [400] : [400, 700])) css += face(name, FILEOF[d], w, toRanges(list));
  }
}
css += '\n/* Kerning and the joining ligatures on for right-to-left text (Nastaliq needs them) */\n.sb-rtl-text,[dir="rtl"]{font-kerning:normal;font-variant-ligatures:common-ligatures contextual}\n';
const hex = c => 'U+' + c.toString(16).toUpperCase().padStart(4, '0');
const total = [...count.values()].reduce((a, b) => a + b, 0);
const lines = [];
lines.push('# Font coverage of the Arabic-script characters in use');
lines.push('');
lines.push(`Generated by \`tools/launch/font_coverage.js\` from ${files} files (typed book pages, the lexicon, the search index, the interface). ${count.size} different Arabic-script characters, ${total.toLocaleString('en-US')} occurrences.`);
lines.push('');
lines.push(`* **Not in any bundled font (drawn as a box on a device that lacks the character): ${missingAll.length}**${missingAll.length ? ' — ' + missingAll.map(([c, n]) => `${hex(c)} \`${String.fromCodePoint(c)}\` (${n}, first in ${where.get(c)})`).join('; ') : ''}`);
lines.push(`* Not in Noto Nastaliq Urdu but in another bundled font: ${missingNastaliq.length}${missingNastaliq.length ? ' — ' + missingNastaliq.slice(0, 40).map(([c, n, f]) => `${hex(c)} \`${String.fromCodePoint(c)}\` (${n}, ${f})`).join('; ') : ''}`);
lines.push('');
lines.push('A character in the second list is drawn by the next family of the font stack where the stack has one; the stacks in `css/style.css` end in Segoe UI / Tahoma / serif, so on a phone the system chooses.');
const md = lines.join('\n') + '\n';
if (args.includes('--write')) fs.writeFileSync(path.join(ROOT, 'docs', 'launch', 'FONT_COVERAGE.md'), md);
console.log(md);
const cssFile = path.join(ROOT, 'css', 'sb_fonts.css');
if (args.includes('--css')) { fs.writeFileSync(cssFile, css); console.log('wrote css/sb_fonts.css'); }
if (args.includes('--check')) {
  let bad = 0;
  if (missingAll.length) { console.error('FAIL: ' + missingAll.length + ' characters have no glyph in any bundled font'); bad++; }
  const have = fs.existsSync(cssFile) ? fs.readFileSync(cssFile, 'utf8').replace(/\r\n/g, '\n') : '';
  if (have !== css) { console.error('FAIL: css/sb_fonts.css is not what tools/launch/font_coverage.js --css makes'); bad++; }
  if (bad) process.exit(1);
  console.log('fonts: every character has a glyph, css/sb_fonts.css is current');
}
