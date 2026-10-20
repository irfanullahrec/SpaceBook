'use strict';
/* Colour contrast of text against its own background (WCAG 2 AA), found without a browser.
 *   node tools/a11y_contrast.js                 report: worst pairs and a count per file
 *   node tools/a11y_contrast.js --check         CI gate: no file may have more failing pairs than tests/baseline/contrast.json
 *   node tools/a11y_contrast.js --update        write the baseline (after an intended change)
 *   node tools/a11y_contrast.js --list [n]      print the n worst (default 40)
 *
 * What it sees: a declaration block (a CSS rule, or the style="" attribute written in the JavaScript that draws the page) that sets BOTH a text
 * colour and a background colour as plain colours (#rgb, #rrggbb, rgb(), a few names). Ratios: 4.5 for normal text, 3 for large text (font-size
 * >= 24px, or >= 18.66px and bold). What it cannot see: text whose background comes from a parent, a gradient, an image, a var(), opacity, or a
 * colour chosen at run time. So "0 failing" here is necessary, not sufficient: axe-core in a real browser is the final judge. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const args = process.argv.slice(2);
const BASE = path.join(ROOT, 'tests', 'baseline', 'contrast.json');

const NAMED = { white: '#ffffff', black: '#000000', red: '#ff0000', blue: '#0000ff', green: '#008000', gray: '#808080', grey: '#808080', silver: '#c0c0c0', yellow: '#ffff00', orange: '#ffa500', navy: '#000080', maroon: '#800000', purple: '#800080', teal: '#008080' };
function parseColor(v) {
  v = String(v || '').trim().toLowerCase().replace(/\s*!important\s*$/, '');
  if (NAMED[v]) v = NAMED[v];
  let m = /^#([0-9a-f]{3})$/.exec(v);
  if (m) return m[1].split('').map(c => parseInt(c + c, 16));
  m = /^#([0-9a-f]{6})$/.exec(v);
  if (m) return [0, 2, 4].map(i => parseInt(m[1].slice(i, i + 2), 16));
  m = /^rgba?\(\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)\s*(?:[,/]\s*([\d.]+%?)\s*)?\)$/.exec(v);
  if (m) { const a = m[4] === undefined ? 1 : (m[4].endsWith('%') ? parseFloat(m[4]) / 100 : parseFloat(m[4])); return a >= 1 ? [+m[1], +m[2], +m[3]] : null; }
  return null;
}
const lum = ([r, g, b]) => { const f = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
function ratio(a, b) { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
function fontPx(v) {
  if (!v) return null;
  const m = /^([\d.]+)(px|rem|em|pt)?/.exec(String(v).trim());
  if (!m) return null;
  const n = parseFloat(m[1]);
  return m[2] === 'px' ? n : m[2] === 'pt' ? n * 4 / 3 : (m[2] === 'rem' || m[2] === 'em') ? n * 16 : null;
}

// one declaration block -> a finding or null
function judge(decls) {
  const d = {};
  decls.split(';').forEach(x => { const i = x.indexOf(':'); if (i > 0) d[x.slice(0, i).trim().toLowerCase()] = x.slice(i + 1).trim(); });
  const fgRaw = d.color;
  let bgRaw = d['background-color'];
  if (!bgRaw && d.background && !/gradient|url\(/i.test(d.background)) bgRaw = d.background.split(/\s+/).find(t => parseColor(t)) || null;
  if (!fgRaw || !bgRaw || /var\(|\$\{|inherit|currentcolor|transparent/i.test(fgRaw + bgRaw)) return null;
  const fg = parseColor(fgRaw), bg = parseColor(bgRaw);
  if (!fg || !bg) return null;
  const px = fontPx(d['font-size']);
  const bold = /^(bold|[6-9]00)$/.test(String(d['font-weight'] || ''));
  const large = px !== null && (px >= 24 || (px >= 18.66 && bold));
  const need = large ? 3 : 4.5;
  const r = ratio(fg, bg);
  return r + 0.005 < need ? { fg: fgRaw, bg: bgRaw, fgRgb: fg, bgRgb: bg, decl: decls, ratio: Math.round(r * 100) / 100, need } : null;
}

// ---- --fix: the smallest darkening (same hue) that reaches the ratio; a dry run unless --write is given
function toHsl([r, g, b]) {
  r /= 255; g /= 255; b /= 255;
  const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let h = 0, s = 0; const l = (mx + mn) / 2;
  if (mx !== mn) { const d = mx - mn; s = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; }
  return [h, s, l];
}
function fromHsl([h, s, l]) {
  const f = (p, q, t) => { if (t < 0) t += 1; if (t > 1) t -= 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < 1 / 2 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; };
  if (s === 0) { const v = Math.round(l * 255); return [v, v, v]; }
  const q = l < 0.5 ? l * (1 + s) : l + s - l * s, p = 2 * l - q;
  return [f(p, q, h + 1 / 3), f(p, q, h), f(p, q, h - 1 / 3)].map(x => Math.round(x * 255));
}
const hex = rgb => '#' + rgb.map(x => Math.max(0, Math.min(255, x)).toString(16).padStart(2, '0')).join('');
function darken(rgb, against, need) {
  const [h, s] = toHsl(rgb); let l = toHsl(rgb)[2];
  for (let i = 0; i < 200 && l > 0; i++) { l = Math.max(0, l - 0.005); const c = fromHsl([h, s, l]); if (ratio(c, against) >= need + 0.02) return c; }
  return [0, 0, 0];
}
const reEsc = x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
// the declaration text with one colour darkened, and what changed
function fixDecl(f) {
  const fgLighter = lum(f.fgRgb) > lum(f.bgRgb);
  let target, newRgb;
  if (fgLighter && (lum(f.bgRgb) < 0.3 || lum(f.fgRgb) > 0.8)) { target = 'bg'; newRgb = darken(f.bgRgb, f.fgRgb, f.need); }   // white or light text on a coloured pill: darken the pill
  else { target = 'fg'; newRgb = darken(f.fgRgb, f.bgRgb, f.need); }                                          // otherwise darken the text
  if (target === 'fg' && ratio(newRgb, f.bgRgb) < f.need) newRgb = darken([0, 0, 0], f.bgRgb, f.need);
  let decl = f.decl, ok = false;
  const keep = raw => { const m = /\s*!important\s*$/i.exec(raw); return m ? m[0] : ''; };          // the colour is replaced, "!important" stays
  if (target === 'fg') decl = decl.replace(new RegExp('(^|;)(\\s*color\\s*:\\s*)' + reEsc(f.fg), 'i'), (m, a, b) => { ok = true; return a + b + hex(newRgb) + keep(f.fg); });
  else decl = decl.replace(new RegExp('((?:^|;)\\s*background(?:-color)?\\s*:[^;]*?)' + reEsc(f.bg), 'i'), (m, a) => { ok = true; return a + hex(newRgb) + keep(f.bg); });
  return ok ? { decl, target, from: target === 'fg' ? f.fg : f.bg, to: hex(newRgb) } : null;
}
if (require.main !== module) { module.exports = { parseColor, ratio, judge, fixDecl, hex }; return; }     // the tests use the functions

const findings = [];
const lineOf = (text, idx) => text.slice(0, idx).split('\n').length;
function scanCss(file) {
  const text = fs.readFileSync(file, 'utf8');
  const re = /([^{}]+)\{([^{}]*)\}/g;
  let m;
  while ((m = re.exec(text))) {
    const f = judge(m[2]);
    if (f) findings.push(Object.assign({ file: path.relative(ROOT, file).replace(/\\/g, '/'), abs: file, start: m.index + m[1].length + 1, decl: m[2], line: lineOf(text, m.index + m[1].length - (m[1].length - m[1].trimStart().length)), where: m[1].trim().split(',')[0].slice(0, 60) }, f));
  }
}
function scanJs(file) {
  const text = fs.readFileSync(file, 'utf8');
  const re = /style\s*=\s*(["'])((?:(?!\1)[^\n])*)\1/g;
  let m;
  while ((m = re.exec(text))) {
    const f = judge(m[2]);
    if (f) findings.push(Object.assign({ file: path.relative(ROOT, file).replace(/\\/g, '/'), abs: file, start: m.index + m[0].indexOf(m[2], 1), decl: m[2], line: lineOf(text, m.index), where: 'style=""' }, f));
  }
}

const cssDir = path.join(ROOT, 'css');
fs.readdirSync(cssDir).filter(f => f.endsWith('.css')).forEach(f => scanCss(path.join(cssDir, f)));
const jsDir = path.join(ROOT, 'js');
const jsFiles = [];
(function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith('.js') && fs.statSync(p).size < 2 * 1024 * 1024 && !/_data|_book_data|lexicon|dictionary|chapters_data|bank_data/i.test(e.name)) jsFiles.push(p);
  }
})(jsDir);
jsFiles.forEach(scanJs);
scanJs(path.join(ROOT, 'index.html'));

if (args.includes('--fix')) {
  const write = args.includes('--write');
  const byFile = {};
  findings.forEach(f => { const x = fixDecl(f); if (x) (byFile[f.abs] = byFile[f.abs] || []).push({ f, x }); else console.log('no automatic fix for', f.file + ':' + f.line, f.where, f.fg, 'on', f.bg); });
  let n = 0;
  Object.entries(byFile).forEach(([file, list]) => {
    let text = fs.readFileSync(file, 'utf8');
    list.sort((a, b) => b.f.start - a.f.start);                 // from the end, so earlier offsets stay valid
    list.forEach(({ f, x }) => {
      if (text.slice(f.start, f.start + f.decl.length) !== f.decl) { console.log('offset moved, skipped', f.file + ':' + f.line); return; }
      text = text.slice(0, f.start) + x.decl + text.slice(f.start + f.decl.length); n++;
      console.log(`${f.file}:${f.line} ${f.where}  ${x.target === 'fg' ? 'text' : 'background'} ${x.from} -> ${x.to}  (${f.ratio}:1, needs ${f.need}:1)`);
    });
    if (write) fs.writeFileSync(file, text);
  });
  console.log((write ? 'fixed ' : 'would fix ') + n + ' of ' + findings.length + ' pairs');
  process.exit(0);
}

const perFile = {};
findings.forEach(f => { perFile[f.file] = (perFile[f.file] || 0) + 1; });

if (args.includes('--update')) {
  fs.writeFileSync(BASE, JSON.stringify({ note: 'Failing text/background pairs per file (tools/a11y_contrast.js). A file may not get worse; lower the number when you fix some (--update).', total: findings.length, files: perFile }, null, 1) + '\n');
  console.log('contrast baseline written:', findings.length, 'failing pairs in', Object.keys(perFile).length, 'files');
  process.exit(0);
}
if (args.includes('--check')) {
  const base = JSON.parse(fs.readFileSync(BASE, 'utf8'));
  const worse = Object.keys(perFile).filter(f => perFile[f] > (base.files[f] || 0));
  if (worse.length) {
    console.log('FAIL  more low-contrast pairs than the baseline in: ' + worse.map(f => `${f} (${perFile[f]} > ${base.files[f] || 0})`).join(', '));
    findings.filter(f => worse.includes(f.file)).slice(-8).forEach(f => console.log(`  ${f.file}:${f.line} ${f.where}  ${f.fg} on ${f.bg} = ${f.ratio}:1 (needs ${f.need}:1)`));
    process.exit(1);
  }
  console.log(`contrast: ${findings.length} failing pairs (baseline ${base.total}), none worse than the baseline`);
  process.exit(0);
}
const li = args.indexOf('--list');
const n = li >= 0 ? (parseInt(args[li + 1], 10) || 40) : 25;
console.log(`${findings.length} text/background pairs below AA in ${Object.keys(perFile).length} files (of ${jsFiles.length} scripts, ${fs.readdirSync(cssDir).length} stylesheets scanned)`);
console.log('worst ratios:');
findings.slice().sort((a, b) => a.ratio - b.ratio).slice(0, n).forEach(f => console.log(`  ${f.ratio}:1 (needs ${f.need})  ${f.fg} on ${f.bg}   ${f.file}:${f.line} ${f.where}`));
console.log('per file (top 15):');
Object.entries(perFile).sort((a, b) => b[1] - a[1]).slice(0, 15).forEach(([f, c]) => console.log(`  ${String(c).padStart(5)}  ${f}`));
