const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '..');
const context = {DATA:{}};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root,'js/data_phys.js'),'utf8'),context);
const app = fs.readFileSync(path.join(root,'js/app.js'),'utf8');
const start = app.indexOf('function getScienceSectionParagraphsWithTranslations(');
const end = app.indexOf('\nfunction switchScienceLessonSubTab(',start);
assert(start >= 0 && end > start);
vm.runInContext(app.slice(start,end),context);
context.getScienceParagraphTranslation = () => { throw Error('Reviewed paragraph used fallback translation'); };
const chapter = context.DATA.physChapters[0];
let count = 0;
for (const section of chapter.sections.filter(item => item.sourcePdfPages)) {
  assert(!/<img\b|\.(?:png|jpe?g)\b/i.test(section.diagramSvg || ''),'Raster image found in reviewed topic');
  const paragraphs = context.getScienceSectionParagraphsWithTranslations(section,chapter,'phys');
  assert.equal(paragraphs.length,section.paras.length);
  for (const paragraph of paragraphs) {
    assert(paragraph.text.trim());
    if (/^https?:\/\//.test(paragraph.text)) {
      assert.equal(paragraph.urdu,paragraph.text);
      assert.equal(paragraph.pashto,paragraph.text);
      count++;
      continue;
    }
    if (!/[A-Za-z\u0600-\u06ff]/u.test(paragraph.text)) {
      assert(paragraph.urdu.trim() && paragraph.pashto.trim());
      count++;
      continue;
    }
    assert(/[\u0600-\u06ff]/u.test(paragraph.urdu),'Urdu translation missing');
    assert(/[\u0600-\u06ff]/u.test(paragraph.pashto),'Pashto translation missing');
    if (/[A-Za-z]{3}/.test(paragraph.text) && !/[\u0600-\u06ff]/u.test(paragraph.text)) {
      assert.notEqual(paragraph.urdu.trim(),paragraph.text.trim());
      assert.notEqual(paragraph.pashto.trim(),paragraph.text.trim());
    }
    count++;
  }
}
const ledger = JSON.parse(fs.readFileSync(path.join(root,'docs/source-verification/physics9-agent1.json'),'utf8'));
ledger.forEach((page,index) => assert.equal(page.pdfPage,index+1));
assert(!/\.png|\.jpg|<img\b/i.test(JSON.stringify(ledger)));
assert(chapter.sections.find(section => section.code==='1.1').diagramSvg.includes('<svg'));
assert.equal(new Set(chapter.sections.map(section => section.code)).size,chapter.sections.length);
console.log(`Verified ${count} paragraph translation pairs, sequential source pages, vector equation, and zero raster topic images.`);
