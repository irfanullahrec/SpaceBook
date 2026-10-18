// Checks that every reviewed source record reaches both applicable reader views.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '../../..');
const katex = require(path.join(root,'assets/vendor/katex/katex.min.js'));
const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
const context = vm.createContext({sanitize: escape});
vm.runInContext(fs.readFileSync(path.join(root,'js/stat_11_data.js'),'utf8')+'\nglobalThis.book=STAT_11_DATA;globalThis.render=renderStatistics11Tab;',context);
for (const page of process.argv.slice(2).map(Number)) {
  const expected = JSON.parse(fs.readFileSync(path.join(__dirname,`stat-page-${page}.json`),'utf8'));
  const chapter = context.book.find(ch => ch.id === expected.chapter);
  const sections = chapter.sections.filter(sec => sec.source.pdfPage === page);
  assert.equal(sections.length,1,`Page ${page} represented exactly once`);
  const section = sections[0];
  assert.deepEqual(Array.from(section.paras,p=>p.id),expected.paras.map(p=>p.id));
  const lesson = context.render(chapter,'lesson');
  const exercise = context.render(chapter,'exercise');
  for (const [index,row] of expected.paras.entries()) {
    const actual = section.paras[index];
    assert.equal(actual.original,row.en,row.id+' English');
    assert.equal(actual.urdu,row.ur,row.id+' Urdu');
    assert.equal(actual.pashto,row.ps,row.id+' Pashto');
    const token = `data-source-id="${row.id}"`;
    assert.equal(lesson.split(token).length-1,1,row.id+' lesson visibility');
    if(row.exerciseId || row.exampleId || ['question','solution'].includes(row.role)) {
      assert.equal(exercise.split(token).length-1,1,row.id+' exercise visibility');
    }
    if (/[A-Za-z]{4}/.test(row.en.replace(/\[scan obscured\]/g,''))) {
      assert(/[\u0600-\u06ff]/.test(row.ur),row.id+' Urdu script');
      assert(/[\u0600-\u06ff]/.test(row.ps),row.id+' Pashto script');
    }
  }
  for (const [index,figure] of (expected.figures||[]).entries()) {
    assert.equal(section.figures[index].svg,figure.svg,`Page ${page} SVG ${index}`);
    assert(lesson.includes(figure.svg),`Page ${page} figure visibility`);
    if(figure.exampleId||figure.exerciseId)assert(exercise.includes(figure.svg),`Page ${page} example figure visible in exercise view`);
    assert(!/<image|data:image|<foreignObject/i.test(figure.svg),'Coded figure only');
  }
  const formulas=context.render(chapter,'formulas');
  if(expected.table){
    assert.deepEqual(JSON.parse(JSON.stringify(section.table)),expected.table,'Exact table record match');
    assert(lesson.includes(escape(expected.table.caption)),'Table caption visible');
    for(const row of expected.table.rows)for(const cell of row)for(const lang of ['en','ur','ps']) {
      assert(cell[lang],'Translated table cell '+lang);
      assert(lesson.includes(escape(cell[lang])),'Table cell visible '+cell[lang]);
    }
  }
  for(const [index,equation] of (expected.equations||[]).entries()) {
    assert.equal(section.equations[index].latex,equation.latex,'Source equation '+equation.id);
    assert(katex.renderToString(equation.latex,{throwOnError:true,displayMode:true}).includes('katex'),'Valid mathematical notation');
    assert(lesson.includes(`data-source-id="${equation.id}"`),'Equation in lesson');
    assert(formulas.includes(`data-source-id="${equation.id}"`),'Equation in formula view');
    for(const lang of ['en','ur','ps'])assert(equation.nativeLines?.[lang]?.length,'Offline equation fallback '+lang);
  }
  const vocabTerms=Object.keys(vm.runInContext('stat11WordVocabulary',context));
  if(expected.paras.some(p=>vocabTerms.some(term=>(' '+p.en.toLowerCase().replace(/[^a-z0-9]+/g,' ')+' ').includes(' '+term.toLowerCase()+' '))))assert(lesson.includes('popovertarget='),'Interactive vocabulary available');
  console.log(`Page ${page}: ${expected.paras.length} paired source records, exact data match and reader visibility passed; source review status: ${expected.auditStatus}`);
}
