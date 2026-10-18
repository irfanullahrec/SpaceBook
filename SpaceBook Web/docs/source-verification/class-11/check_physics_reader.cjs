const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const root = 'D:/SpaceBook/SpaceBook Web/';
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(root + 'js/phys_11_data.js', 'utf8'), context);
const app = fs.readFileSync(root + 'js/app.js', 'utf8');
function functionSource(name) {
  const start = app.indexOf('function ' + name + '(');
  assert(start >= 0, name);
  const end = app.indexOf('\nfunction ', start + 1);
  return app.slice(start, end < 0 ? undefined : end);
}
context.sanitize = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;');
vm.runInContext(functionSource('renderInteractiveParagraphHtml'), context);
vm.runInContext(functionSource('getScienceSectionParagraphsWithTranslations'), context);
vm.runInContext(functionSource('getSubjectChapterList'), context);
vm.runInContext(fs.readFileSync(root + 'assets/vendor/katex/katex.min.js', 'utf8'), context);
vm.runInContext(fs.readFileSync(root + 'js/lesson_math_reader.js', 'utf8'), context);
vm.runInContext(`
  const list = getSubjectChapterList('phys', 'cls11');
  if (list !== PHYS_11_DATA) throw Error('Wrong class dataset');
  for (const ch of PHYS_11_DATA) {
  const allParas = ch.sections.flatMap(s => [...s.paras, ...(s.continuation ? [s.continuation.transition,s.continuation.extension] : []), ...(s.branches||[]).flatMap(b=>b.paras)]);
  const ids = [...ch.sections.map(s => s.id), ...allParas.map(p => p.id)];
  if (new Set(ids).size !== ids.length) throw Error('Duplicate IDs');
  for (const sec of ch.sections) {
    const paras = getScienceSectionParagraphsWithTranslations(sec, ch, 'phys');
    if (paras.length !== sec.paras.length) throw Error('Pair count');
    for (const p of sec.paras) {
      if (!p.original || !p.text || !p.urdu || !p.pashto) throw Error('Missing language');
      if (sec.sourceLanguage === 'ur' && p.original !== p.urdu) throw Error('Urdu original mismatch');
      if (sec.sourceLanguage === 'en' && p.original !== p.text) throw Error('English original mismatch');
    }
  }
  const html = renderPhysics11Source(ch);
  if (html.includes('katex-error')) throw Error('Malformed equation');
  if (/<img|<iframe|<embed|<object|data:image|<image/i.test(html)) throw Error('Scan embed');
  if ((html.match(/class="lesson-sentence"/g) || []).length !== allParas.length) throw Error('Paragraph alignment');
  }
`, context);
assert(fs.readFileSync(root + 'index.html', 'utf8').includes('js/phys_11_data.js'));
assert(app.includes("subjId === 'cls11-phy'"));
assert(app.includes('renderPhysics11Tab(ch, tabId)'));
console.log('Class 11 Physics: routing, paragraph pairs, unique IDs, source language, and no-raster reader checks passed.');
