/* Focused non-browser check for the Class 10 Biology source overlays and reader.
 * Loads data.js + data_bio.js + biology overlays + app.js + reader inside the smoke DOM stub,
 * renders each owned unit through the real science lesson route, and asserts there is no
 * raw markup leakage, every paragraph has non-English Urdu/Pashto text, figures are inline SVG,
 * and no raster images are embedded. Run: node docs/source-verification/class-10/biology_check.cjs */
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const ROOT = path.resolve(__dirname, '../../..');
const JS = path.join(ROOT, 'js') + path.sep;

function makeEl(id) {
  const style = {};
  return {
    _id: id, innerHTML: '', textContent: '', value: '', className: '', title: '', src: '', href: '',
    style: new Proxy(style, { get: (t, k) => (k in t ? t[k] : ''), set: (t, k, v) => { t[k] = v; return true; } }),
    classList: { add() {}, remove() {}, toggle() {}, contains() { return false; } },
    dataset: {}, children: [], scrollHeight: 100, scrollTop: 0, offsetHeight: 100, checked: false, disabled: false,
    addEventListener() {}, removeEventListener() {}, appendChild() {}, insertBefore() {}, removeChild() {}, remove() {},
    setAttribute() {}, getAttribute() { return null; }, removeAttribute() {}, focus() {}, click() {}, blur() {},
    querySelector() { return makeEl(); }, querySelectorAll() { return []; }, closest() { return null; },
    getBoundingClientRect() { return { top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0 }; },
    contains() { return false; }, cloneNode() { return makeEl(); }, matches() { return false; }
  };
}
const registry = {};
const documentStub = {
  getElementById(id) { if (!registry[id]) registry[id] = makeEl(id); return registry[id]; },
  querySelector() { return makeEl(); }, querySelectorAll() { return []; }, createElement() { return makeEl(); },
  createTreeWalker() { return { nextNode: () => null }; }, addEventListener() {}, removeEventListener() {},
  body: makeEl('body'), documentElement: makeEl('html'), head: makeEl('head'),
  location: { href: 'http://localhost/', search: '', hash: '' }
};
const windowStub = {
  document: documentStub, location: documentStub.location,
  localStorage: { getItem: () => null, setItem() {}, removeItem() {} }, sessionStorage: { getItem: () => null, setItem() {} },
  open() {}, addEventListener() {}, removeEventListener() {}, requestAnimationFrame() { return 0; },
  matchMedia: () => ({ matches: false, addEventListener() {} }), navigator: { userAgent: 'smoke' }, innerWidth: 1400, innerHeight: 900,
  NodeFilter: { SHOW_TEXT: 4, FILTER_ACCEPT: 1, FILTER_REJECT: 2, FILTER_SKIP: 3 }
};
windowStub.window = windowStub;
const sb = vm.createContext({
  console, window: windowStub, document: documentStub, NodeFilter: windowStub.NodeFilter,
  localStorage: windowStub.localStorage, sessionStorage: windowStub.sessionStorage, navigator: windowStub.navigator,
  location: documentStub.location, setTimeout, clearTimeout, setInterval, clearInterval,
  requestAnimationFrame: windowStub.requestAnimationFrame, getComputedStyle: () => ({ getPropertyValue: () => '' }),
  module: undefined, exports: undefined
});
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const srcs = [...html.matchAll(/<script\s+src="([^"]+)"/g)].map(m => m[1].split('?')[0]);
const wanted = srcs.filter(s => /js\/(data\.js|data_bio\.js|biology_10_.*\.js|app\.js|dictionary_data\.js|data_chem\.js|data_phys\.js|data_eng\.js|bio_data\.js)$/.test(s));
let failures = 0;
const check = (name, ok, detail) => { console.log((ok ? 'PASS ' : 'FAIL ') + name + (ok || !detail ? '' : ' — ' + detail)); if (!ok) failures++; };
const declared = new Set();
for (const s of wanted) {
  const code = fs.readFileSync(path.join(ROOT, s), 'utf8');
  const re = /^\s*(?:function\s+([A-Za-z_$][\w$]*)|(?:const|let|var)\s+([A-Za-z_$][\w$]*))/gm;
  let m; while ((m = re.exec(code))) declared.add(m[1] || m[2]);
  try { vm.runInContext(code, sb, { filename: s, timeout: 60000 }); } catch (e) { check('load ' + s, false, e.message); }
}
vm.runInContext('for (const n of ' + JSON.stringify([...declared]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);
check('reader installed', typeof sb.Biology10SourceReader === 'object');
check('bio10 scripts wired in order', wanted.indexOf('js/biology_10_front_source.js') > wanted.indexOf('js/data_bio.js') && wanted.indexOf('js/biology_10_reader.js') > wanted.indexOf('js/app.js'));
vm.runInContext("state.selectedClass='cls10'; state.activeSubject='bio';", sb);
const chapters = sb.DATA.bio10Chapters.filter(ch => ch.__bio10Source);
check('at least one owned chapter', chapters.length > 0);
const isRtl = s => /[؀-ۿ]/.test(s || '');
const noLatinOnly = s => isRtl(s) && !/^[A-Za-z0-9 .,;:()'"%-]+$/.test(s || '');
for (const ch of chapters) {
  const out = vm.runInContext(`renderScienceLessonSubContent('bio', DATA.bio10Chapters.find(c=>c.num===${ch.num}), 'translations')`, sb);
  check(`unit ${ch.num} translations render`, typeof out === 'string' && out.length > 2000, String(out).slice(0, 100));
  check(`unit ${ch.num} no raster images`, !/<img\b|data:image|\.jpg|\.png|\.webp/i.test(out));
  check(`unit ${ch.num} no leaked markup text`, !/&lt;(p|b|svg|div)\b|\\\(|\\\[/.test(out));
  check(`unit ${ch.num} undefined/NaN free`, !/undefined|NaN|\[object Object\]/.test(out));
  const ex = vm.runInContext(`renderScienceLessonSubContent('bio', DATA.bio10Chapters.find(c=>c.num===${ch.num}), 'exercise')`, sb);
  check(`unit ${ch.num} exercise renders`, typeof ex === 'string' && ex.length > 200);
  const slo = vm.runInContext(`renderScienceLessonSubContent('bio', DATA.bio10Chapters.find(c=>c.num===${ch.num}), 'slos')`, sb);
  check(`unit ${ch.num} SLOs render`, typeof slo === 'string' && slo.length > 200);
  const ids = new Set();
  let dup = [];
  for (const t of ch.topics) {
    if (t.id) { if (ids.has(t.id)) dup.push(t.id); ids.add(t.id); }
    if (!t.paras) continue;
    t.paras.forEach((p, i) => {
      if (!noLatinOnly(p.urdu) || !noLatinOnly(p.pashto)) check(`unit ${ch.num} ${t.num} para ${i} has Urdu+Pashto`, false, (p.text || '').slice(0, 60));
      if (/<[a-z]+\b[^>]*>/i.test(p.text)) check(`unit ${ch.num} ${t.num} para ${i} plain text`, false, p.text.slice(0, 60));
    });
    const used = new Set();
    const walk = b => { if (typeof b === 'number') used.add(b); else if (b && typeof b === 'object') { if ('i' in b) used.add(b.i); (b.items || []).forEach(walk); (b.paras || []).forEach(walk); (b.blocks || []).forEach(walk); (b.main || []).forEach(walk); (b.side || []).forEach(walk); if ('title' in b) used.add(b.title); if ('headingIndex' in b) used.add(b.headingIndex); } };
    (t.layout || []).forEach(walk);
    const unused = t.paras.map((_, i) => i).filter(i => !used.has(i));
    check(`unit ${ch.num} ${t.num} every paragraph placed in layout`, unused.length === 0, 'unused indices ' + unused.join(','));
    const bad = [...used].filter(i => !t.paras[i]);
    check(`unit ${ch.num} ${t.num} layout indices exist`, bad.length === 0, 'missing ' + bad.join(','));
    for (const [id, fig] of Object.entries(t.figures || {})) {
      check(`unit ${ch.num} ${t.num} figure ${id} is inline svg`, /^\s*<svg[\s\S]*<\/svg>\s*$/.test(fig.svg));
      for (const l of fig.labels || []) check(`unit ${ch.num} figure ${id} label "${l.text}" present in svg`, fig.svg.includes('>' + l.text + '<'));
    }
  }
  check(`unit ${ch.num} topic ids unique`, dup.length === 0, dup.join(','));
  check(`unit ${ch.num} search fields intact`, typeof ch.name === 'string' && ch.topics.every(t => typeof t.title === 'string') && Array.isArray(ch.textbookExercise?.mcqs));
}
console.log(failures ? `\n${failures} check(s) failed` : '\nAll Biology checks passed');
process.exit(failures ? 1 : 0);
