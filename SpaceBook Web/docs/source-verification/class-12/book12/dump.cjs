'use strict';
/* Dumps a Class 11/12 book's reviewed scan data and exercise bank to JSON for engine.py.
 *   node dump.cjs <data file in js/> <GLOBAL name> <bank files, comma separated or ->  <bank subject key or -> <out.json>
 * e.g. node dump.cjs pakstudy_12_data.js PAKSTUDY_12_DATA pakstudy12_exercise_banks.js pakstudy pakstudy/dump.json */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const [dataFile, glob, banks, , out] = process.argv.slice(2);
global.window = global;
global.document = {addEventListener() {}, querySelector() { return null; }};
vm.runInThisContext(fs.readFileSync(path.join(ROOT, 'js', dataFile), 'utf8') + `\n;globalThis[${JSON.stringify(glob)}] = ${glob};`);
const DATA = globalThis[glob];
if (banks && banks !== '-') {
  const run = f => vm.runInThisContext(fs.readFileSync(path.join(ROOT, 'js', f), 'utf8') + '\n;globalThis.__x=1;', {filename: f});
  run('class12_exercise_banks.js');
  for (const f of banks.split(',')) run(f);
}
const res = DATA.map(ch => ({
  number: ch.number, title: ch.title, titleUrdu: ch.titleUrdu, titlePashto: ch.titlePashto, titleEn: ch.titleEn, author: ch.author || null,
  bank: ch.class12Exercise || null,
  sections: (ch.sections || []).map(s => ({
    id: s.id, title: s.title, titleEn: s.titleEn, headingUrdu: s.headingUrdu, headingPashto: s.headingPashto,
    label: s.sourcePageLabel, refs: s.sourceReferences, note: s.sourceNote || null,
    paras: (s.paras || []).map(p => typeof p === 'string' ? {urdu: p} : p), blocks: s.sourceBlocks || [], layout: s.sourceLayout || null, cover: s.sourceCoverIllustrationReview || null
  }))
}));
fs.mkdirSync(path.dirname(path.resolve(out)), {recursive: true});
fs.writeFileSync(out, JSON.stringify(res));
console.log('chapters', res.length, 'sections', res.reduce((n, c) => n + c.sections.length, 0), 'bank units', res.filter(c => c.bank).length);
