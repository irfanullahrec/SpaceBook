const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const root = 'D:/SpaceBook/SpaceBook Web/';
const app = fs.readFileSync(root + 'js/app.js', 'utf8');
const html = fs.readFileSync(root + 'index.html', 'utf8');
const context = vm.createContext({
  sanitize: value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c])),
  SpaceBookLessonMath: { renderMath: equation => `<span role="math">${equation.latex}</span>` }
});
vm.runInContext(fs.readFileSync(root + 'js/chem_11_data.js', 'utf8') + '\n;globalThis.data=CHEM_11_DATA;globalThis.render=renderChemistry11Tab;', context);
assert(app.includes("subjId === 'cls11-chem'"), 'Class 11 Chemistry subject route');
assert(app.includes("classId === 'cls11' && typeof CHEM_11_DATA !== 'undefined'"), 'Class 11 Chemistry dataset selection');
assert(app.includes("classId === 'cls11' && subjKey === 'chem'"), 'Class 11 Chemistry source reader selection');
assert(html.indexOf('js/chem_11_data.js') < html.indexOf('js/app.js'), 'Chemistry data loads before app');
const ids = new Set();
let paragraphs = 0;
for (const chapter of context.data) {
  assert(chapter.id && chapter.title, 'chapter identity');
  for (const section of chapter.sections) {
    assert(!ids.has(section.id), `duplicate section ${section.id}`); ids.add(section.id);
    assert(section.source.pdfPage >= 1 && section.source.pdfPage <= 419, `source page ${section.id}`);
    for (const paragraph of section.paras || []) {
      paragraphs++;
      assert(!ids.has(paragraph.id), `duplicate paragraph ${paragraph.id}`); ids.add(paragraph.id);
      assert(paragraph.original && paragraph.text === paragraph.original, `source language ${paragraph.id}`);
      assert(paragraph.urdu && paragraph.pashto, `translation pair ${paragraph.id}`);
    }
  }
}
const sourcePages = new Set(context.data.flatMap(ch => ch.sections.map(sec => sec.source.pdfPage)));
for (let page = 1; page <= Math.max(...sourcePages); page++) assert(context.data.some(ch => ch.sections.some(sec => sec.source.pdfPage === page)), `missing page ${page}`);
assert(context.data[0].sections.filter(sec => sec.table).reduce((n, sec) => n + sec.table.rows.length, 0) === 14, 'Table of Contents rows');
const rendered = context.data.map(ch => context.render(ch, 'lesson')).join('');
assert(!/<img|<iframe|<embed|<object|data:image/i.test(rendered), 'no raster textbook embeds');
assert(rendered.includes('chem11-p017-eq-1-4') || rendered.includes('Number of moles of gas'), 'equation rendering');
assert(!/rotate\(#[^)]*\)/.test(rendered), 'valid molecule rotations');
assert(rendered.includes('<details>'), 'interactive translations');
console.log(`Class 11 Chemistry reader checks passed: ${paragraphs} paired paragraphs, ${ids.size} unique IDs, ${sourcePages.size} represented source pages (verification tracked separately), route wiring, tables, equations, interactive translations, and no raster embeds.`);
