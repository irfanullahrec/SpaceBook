const fs = require('fs');
const vm = require('vm');

const path = require('path');
const DIR = path.resolve(__dirname, '../../../../js') + path.sep;
const files = ['data.js', 'drawing_1_data.js', 'drawing_2_data.js', 'drawing_3_data.js', 'data_chem.js', 'data_phys.js', 'data_eng.js', 'data_bio.js', 'data_comp.js', 'dictionary_data.js', 'urdu_data.js', 'urdu_10_data.js', 'english_data.js', 'english_10_data.js', 'english_1_data.js', 'math_data.js', 'pakstudy_data.js', 'general_science_9_data.js', 'hpe_9_data.js', 'drawing_9_data.js', 'islamiat_ikhtiari_9_data.js', 'mutalia_quran_9_data.js', 'pakstudy_10_data.js', 'bio_data.js', 'islamyat_data.js', 'islamyat_10_data.js', 'islamyat_1_data.js', 'nazira_1_data.js', 'pashto_1_data.js', 'math_10_data.js', 'computer_10_data.js', 'general_science_10_data.js', 'hpe_10_data.js', 'drawing_10_data.js', 'islamiat_ikhtiari_10_data.js', 'mutalia_quran_10_data.js', 'math_1_data.js', 'math_2_data.js', 'math_3_book_text.js', 'math_3_data.js', 'math_primary_visuals.js', 'english_2_data.js', 'urdu_2_data.js', 'islamyat_2_data.js', 'nazira_2_data.js', 'gk_2_data.js', 'pashto_2_data.js', 'islamyat_3_data.js', 'nazira_3_data.js', 'english_3_data.js', 'gk_3_data.js', 'pashto_3_data.js', 'math_12_data.js', 'phys_12_data.js', 'chem_12_data.js', 'stat_12_data.js', 'english_12_data.js', 'pakstudy_12_data.js', 'urdu_12_data.js', 'biology_12_data.js', 'computer_12_data.js', 'civics_12_data.js', 'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js', 'islamic_history_12_data.js', 'quran_12_data.js', 'math_5_data.js', 'general_science_5_data.js', 'english_5_data.js', 'urdu_5_data.js', 'islamiat_5_data.js', 'social_studies_5_data.js', 'social_studies_um_5_data.js', 'pashto_5_data.js', 'math_6_data.js', 'general_science_6_data.js', 'english_6_data.js', 'urdu_6_data.js', 'islamiat_6_data.js', 'computer_6_data.js', 'geography_6_data.js', 'history_6_data.js', 'hpe_6_data.js', 'drawing_6_data.js', 'arabic_6_data.js', 'mutalia_quran_6_data.js', 'pashto_6_data.js', 'data_phys.js', 'physics_10_source_data.js', 'physics_10_book_data.js', 'data_chem.js', 'chemistry_10_source_data.js'].concat(require('fs').existsSync(path.resolve(__dirname, '../../../../js/chemistry_10_book_data.js')) ? ['chemistry_10_book_data.js'] : []);

function makeEl(id) {
  const style = {};
  const el = {
    _id: id, innerHTML: '', textContent: '', value: '', className: '', title: '', src: '', href: '',
    style: new Proxy(style, { get: (t, k) => (k in t ? t[k] : ''), set: (t, k, v) => { t[k] = v; return true; } }),
    classList: { add() { }, remove() { }, toggle() { }, contains() { return false; } },
    dataset: {}, children: [], scrollHeight: 100, scrollTop: 0, offsetHeight: 100, checked: false, disabled: false,
    addEventListener() { }, removeEventListener() { }, appendChild() { }, insertBefore() { }, removeChild() { }, remove() { },
    setAttribute() { }, getAttribute() { return null; }, removeAttribute() { }, focus() { }, click() { }, blur() { },
    querySelector() { return makeEl(); }, querySelectorAll() { return []; }, closest() { return null; },
    getBoundingClientRect() { return { top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0 }; },
    contains() { return false; }, cloneNode() { return makeEl(); }, matches() { return false; }
  };
  return el;
}
const registry = {};
const NodeFilter = {
  SHOW_TEXT: 4,
  FILTER_ACCEPT: 1,
  FILTER_REJECT: 2,
  FILTER_SKIP: 3
};
const documentStub = {
  getElementById(id) { if (!registry[id]) registry[id] = makeEl(id); return registry[id]; },
  querySelector() { return makeEl(); },
  querySelectorAll() { return []; },
  createElement() { return makeEl(); },
  createTreeWalker() { return { nextNode: () => null }; },
  addEventListener() { }, removeEventListener() { },
  body: makeEl('body'), documentElement: makeEl('html'), head: makeEl('head'),
  location: { href: 'http://localhost/', search: '', hash: '' }
};
const windowStub = {
  document: documentStub, location: documentStub.location,
  localStorage: { getItem: () => null, setItem() { }, removeItem() { } },
  sessionStorage: { getItem: () => null, setItem() { } },
  open() { }, addEventListener() { }, removeEventListener() { },
  requestAnimationFrame() { return 0; }, matchMedia: () => ({ matches: false, addEventListener() { } }),
  navigator: { userAgent: 'smoke' }, innerWidth: 1400, innerHeight: 900,
  NodeFilter
};
windowStub.window = windowStub;

const sb = vm.createContext({
  console, window: windowStub, document: documentStub, NodeFilter,
  localStorage: windowStub.localStorage, sessionStorage: windowStub.sessionStorage,
  navigator: windowStub.navigator, location: documentStub.location,
  setTimeout, clearTimeout, setInterval, clearInterval,
  requestAnimationFrame: windowStub.requestAnimationFrame,
  getComputedStyle: () => ({ getPropertyValue: () => '' }),
  module: undefined, exports: undefined
});
const declared = new Set();
for (const f of files) {
  const code = fs.readFileSync(DIR + f, 'utf8');
  const re = /^\s*(?:const|var|let)\s+([A-Za-z_$][\w$]*)/gm;
  let d; while ((d = re.exec(code))) declared.add(d[1]);
  vm.runInContext(code, sb, { filename: f, timeout: 60000 });
}
vm.runInContext('for (const n of ' + JSON.stringify([...declared]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);
// app.js declares functions / let state -> hoist those too
{
  const code = fs.readFileSync(DIR + 'app.js', 'utf8');
  const names = new Set();
  const re = /^\s*(?:function\s+([A-Za-z_$][\w$]*)|(?:const|let|var)\s+([A-Za-z_$][\w$]*))/gm;
  let m; while ((m = re.exec(code))) names.add(m[1] || m[2]);
  vm.runInContext(code, sb, { filename: 'app.js', timeout: 60000 });
  vm.runInContext('for (const n of ' + JSON.stringify([...names]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);
}


vm.runInContext('for (const k of Object.getOwnPropertyNames(globalThis)) { if (typeof globalThis[k] === "function" && !(k in window)) window[k] = globalThis[k]; }', sb);
for (const f of ['math6_reader.js']) vm.runInContext(fs.readFileSync(DIR + f, 'utf8'), sb, { filename: f });
vm.runInContext(fs.readFileSync(DIR + 'cls6_book_reader.js', 'utf8'), sb, { filename: 'cls6_book_reader.js' });
let fails = 0;
function chk(label, src) {
  try { vm.runInContext(src, sb, { timeout: 20000 }); console.log('PASS  ' + label); }
  catch (e) { fails++; console.log('FAIL  ' + label + ' -> ' + (e && e.message)); }
}
const subj = process.argv[2] || 'phys';
const B = sb.window.CLS10_BOOKS && sb.window.CLS10_BOOKS[subj];
if (!B) { console.log('no book', subj); process.exit(1); }
const list = vm.runInContext(`getSubjectChapterList('${subj}', 'cls10')`, sb);
list.forEach((c, i) => {
  const u = B.units.find(x => String(x.number) === String(c.num || c.number));
  if (!u || !u.sections.length) { console.log('skip  unit', c.num, '(not in book yet)'); return; }
  for (const tab of ['lesson', 'exercise', 'slos']) {
    chk(`${subj} unit ${c.num} tab ${tab}`, `state.selectedClass='cls10'; document.getElementById('subjTabContent').innerHTML=''; window.switchSubjectTab('${subj}', '${tab}', ${i}, 'cls10'); if (document.getElementById('subjTabContent').innerHTML.length < 200) throw new Error('empty');`);
  }
});
console.log(fails ? fails + ' FAIL' : 'all ok');
if (process.argv[3]) { vm.runInContext(`state.selectedClass='cls10'; window.switchSubjectTab('${subj}', '${process.argv[3]}', ${process.argv[4]||3}, 'cls10');`, sb); console.log(sb.document.getElementById('subjTabContent').innerHTML.slice(0, 1500)); }
