// Non-browser checks for the reported HTML/translation reader regression.
const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const path = require('path');
const root = path.resolve(__dirname, '..');
const context = {
  document: {createElement() {
    return {
      set innerHTML(value) {this.textContent = String(value).replace(/<[^>]*>/g, '')
        .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
        .replace(/&quot;/g, '"').replace(/&#(?:39|x27);/gi, "'");},
      textContent: '',
    };
  }},
  sanitize: value => String(value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;'),
};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root,'js/phys_12_data.js'),'utf8')+';globalThis.physics = PHYS_12_DATA;', context);
const app = fs.readFileSync(path.join(root,'js/app.js'),'utf8');
for (const name of ['splitSentenceText','renderInteractiveParagraphHtml','getScienceSectionParagraphsWithTranslations','renderScienceSourceLayout','renderScienceLessonSubContent']) {
  const source = app.match(new RegExp('function '+name+'\\([^]*?\\n\\}'));
  assert(source, 'Reader function must exist: '+name);
  vm.runInContext(source[0],context);
}
const chapter = context.physics[0];
const reviewed = chapter.sections.filter(section => section.id.startsWith('phys12-front-'));
const savedRecords=JSON.parse(fs.readFileSync(path.join(root,'docs/source-verification/physics-agent2-pages.json'),'utf8'));
assert.equal(reviewed.length,savedRecords.length);
let count=0;
for (const section of reviewed) {
  assert(section.headingUrdu && section.headingPashto);
  const paragraphs = context.getScienceSectionParagraphsWithTranslations(section,chapter,'phys');
  const indices = section.sourceLayout.flatMap(block=>block.indices||[]).sort((a,b)=>a-b);
  assert.equal(JSON.stringify(indices),JSON.stringify(paragraphs.map((_,index)=>index)),section.id+' layout must retain every source block exactly once');
  assert(paragraphs.length > 0, 'Every section, including contents, needs reading text');
  for (const paragraph of paragraphs) {
    assert(!/<\/?(?:p|b|strong|figure|svg)\b/.test(paragraph.text),section.id+' contains HTML in prose');
    assert(paragraph.urdu && paragraph.pashto,section.id+' lacks a translation');
    if (/[A-Za-z]{3}/.test(paragraph.text) && !/^\\\(/.test(paragraph.text)) {
      assert(/[\u0600-\u06ff]/.test(paragraph.urdu),section.id+' Urdu repeats English');
      assert(/[\u0600-\u06ff]/.test(paragraph.pashto),section.id+' Pashto repeats English');
    }
    const result = context.renderInteractiveParagraphHtml(paragraph.text,paragraph.urdu,paragraph.pashto,'check',true);
    assert(!/&lt;\/?(?:p|b|strong|figure|svg)\b/.test(result),'Markup must not become visible reader text');
    assert(result.includes('data-ur="'+context.sanitize(paragraph.urdu)+'"'));
    assert(result.includes('data-ps="'+context.sanitize(paragraph.pashto)+'"'));
    count++;
  }
}
assert.deepEqual(chapter.sections.map(s=>s.id),chapter.topics.map(s=>s.id),'Lessons and topic lists must agree');
const fixture = context.getScienceSectionParagraphsWithTranslations({content:'<p>Alpha <b>beta</b></p><p>Gamma</p>'},chapter,'phys');
assert.equal(fixture.length,2);
assert.equal(fixture[0].text,'Alpha beta');
assert.equal(fixture[1].text,'Gamma');
assert(fixture[0].urdu.includes('مکمل نہیں'),'Unfinished translations must be disclosed');
const encoded = context.getScienceSectionParagraphsWithTranslations({content:'&lt;p&gt;Alpha &lt;b&gt;beta&lt;/b&gt;&lt;/p&gt;'},chapter,'phys');
assert.equal(encoded[0].text,'Alpha beta');
const rendered = context.renderScienceLessonSubContent('phys',chapter,'translations');
assert(!/&lt;\/?(?:p|b|strong|figure|svg)\b/.test(rendered),'No escaped HTML tags in the complete Physics reader');
assert(rendered.includes('فروخت کے لیے نہیں'));
assert(rendered.includes('د پلور لپاره نه دی'));
assert(rendered.includes('<svg'));
const contents = reviewed.find(section=>section.id==='phys12-front-contents');
const contentsOutput=context.renderScienceSourceLayout(contents,contents.paras,'en',0);
assert(contentsOutput.includes('<table') && contentsOutput.includes('<th scope="col"'));
assert(!contentsOutput.includes('lesson-sentence'),'Table cells must not become stacked reading paragraphs');
const outcomes=reviewed.find(section=>section.id==='phys12-front-outcomes1');
assert(context.renderScienceSourceLayout(outcomes,outcomes.paras,'en',0).includes('<ul'));
const intro=reviewed.find(section=>section.id==='phys12-front-coulomb-introduction');
const introOutput=context.renderScienceSourceLayout(intro,intro.paras,'en',0);
assert(introOutput.includes('circuits is capacitance'),'Continuous book prose must not split into scan lines');
console.log('PASS: '+reviewed.length+' corrected sections, '+count+' aligned paragraph translations; actual reader output, legacy markup cleanup and topic synchronization checked without a browser.');
