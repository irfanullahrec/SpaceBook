const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict'),path=require('path');
const root=path.resolve(__dirname,'../../..');
const c={DATA:{},sanitize:v=>String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')};
const calls=[];
c.renderInteractiveParagraphHtml=(text,ur,ps,id,aligned)=>{assert(text&&ur&&ps);assert.equal(aligned,true);calls.push({text,ur,ps,id});return `<span data-en="${c.sanitize(text)}">${c.sanitize(text)}</span>`;};
vm.createContext(c);
vm.runInContext(fs.readFileSync(path.join(root,'js/data_phys.js'),'utf8'),c);
const app=fs.readFileSync(path.join(root,'js/app.js'),'utf8');
const readerStart=app.indexOf('function getScienceSectionParagraphsWithTranslations('),readerEnd=app.indexOf('\nfunction switchScienceLessonSubTab(',readerStart);
vm.runInContext(app.slice(readerStart,readerEnd),c);
const layoutStart=app.indexOf('function renderScienceSourceLayout('),layoutEnd=app.indexOf('\nfunction renderClass9PhysicsFrontMatterBlocks(',layoutStart);
vm.runInContext(app.slice(layoutStart,layoutEnd),c);
const ch=c.DATA.physChapters[0];
const reviewedNumbers=fs.readdirSync(__dirname).filter(f=>/^physics-page-\d{3}\.json$/.test(f)).map(f=>Number(f.slice(13,16))).filter(n=>n>=6).sort((a,b)=>a-b);
for(const number of reviewedNumbers){
 const page=JSON.parse(fs.readFileSync(path.join(__dirname,`physics-page-${String(number).padStart(3,'0')}.json`),'utf8'));
 const actual=c.DATA.physChapters.find(ch=>ch.num===page.chapterNumber).sourcePages.find(p=>p.pdfPage===number);
 assert.deepEqual(JSON.parse(JSON.stringify(actual)),page);
 for(const fragment of actual.sections){
  const seen=fragment.sourceLayout.flatMap(b=>b.columns?b.columns.flat():(b.indices||[]));
  assert.equal(seen.length,fragment.paras.length);
  assert.equal(new Set(seen).size,seen.length);
  fragment.paras.forEach(p=>{assert(p.text&&p.urdu&&p.pashto);assert(!/<\/?[a-z][\w:-]*(?:\s[^<>]*)?\/?>/i.test(p.text)&&!p.text.includes('\uFFFD'));});
  (fragment.blocks||[]).forEach(b=>assert(!/<image\b|<img\b|data:image/.test(b.svg||'')));
 }
}
const section=ch.sections.find(s=>s.code==='1.1');
const paras=c.getScienceSectionParagraphsWithTranslations(section,ch,'phys');
const html=c.renderScienceSourceLayout(section,paras,'en',0);
for(const id of ['physics9-telescope-title','physics9-galaxy-title','physics9-pet-title','physics9-hologram-title','physics9-kindi-title'])assert.equal((html.match(new RegExp(`id="${id}"`,'g'))||[]).length,1,'Each visual occurs once');
assert(html.includes('Physics investigate')&&html.includes('by physics.'));
assert(html.includes('I equals Q divided by t'));
assert(html.includes('data-source-language="ar"')&&html.includes('data-source-language="ur"'));
assert(html.includes('data-en="The sun is not to overtake the moon'));
assert.equal((html.match(/<blockquote /g)||[]).length,3);
assert.equal((html.match(/<table class="diff-table">/g)||[]).length,1);
for(const lang of ['ur','ps']){const translated=c.renderScienceSourceLayout(section,paras,lang,0);assert(translated.includes('<table class="diff-table">'));assert(!translated.includes('Motion of objects and how'));}
assert.equal(ch.definitions.find(d=>d.term==='Physics').definition,JSON.parse(fs.readFileSync(path.join(__dirname,'physics-page-007.json'),'utf8')).sections[0].paras[5].text);
const opening=ch.sections.find(s=>s.code==='source-u1-opening');
assert(c.renderScienceSourceLayout(opening,opening.paras,'en',1).includes('Editorial source-review note'));
assert(c.renderScienceSourceLayout(opening,opening.paras,'en',1).includes('<ul'));
const car=c.DATA.physChapters[0].sections.find(s=>s.code==='1.1');
const urCar=c.renderScienceSourceLayout(car,c.getScienceSectionParagraphsWithTranslations(car,ch,'phys'),'ur',2);
assert(urCar.includes('physics9-car-title-urdu'));
const defs=ch.definitions;
for(const term of ['Measurement','Unit','Physical Quantity','Base Quantities','Derived Quantities'])assert.equal(defs.filter(d=>d.term===term).length,1);
for(const code of ['1.3','1.4']){
 const sec=ch.sections.find(s=>s.code===code),pairs=c.getScienceSectionParagraphsWithTranslations(sec,ch,'phys');
 const rendered=c.renderScienceSourceLayout(sec,pairs,'en',3);
 if(code==='1.3'){assert.equal((rendered.match(/colspan="2"/g)||[]).length,4);assert(rendered.includes('kg⁻¹m⁻²s⁴A²'));}
 else {assert(rendered.includes('exponent (n)'));assert(rendered.includes('physics9-earthmoon-title'));assert(rendered.includes('<ol'));}
}
assert.equal(ch.sourceReview.complete,false);
assert.equal(ch.sourceReview.lastPdfPage,33);
assert.deepEqual(Array.from(ch.sourceReview.unresolvedPdfPages),[6,20,25,26,27]);
const prefixes=ch.sections.find(s=>s.code==='1.5');
const prefHtml=c.renderScienceSourceLayout(prefixes,c.getScienceSectionParagraphsWithTranslations(prefixes,ch,'phys'),'en',5);
assert(prefHtml.includes('10¹⁸')&&prefHtml.includes('10⁻¹⁸'));
assert(prefHtml.includes('a) width of a book')&&prefHtml.includes('e) mass of cricket ball.'));
for(const num of ['1.1','1.2','1.3','1.4','1.5'])assert.equal(ch.numericals.filter(n=>n.num===num).length,1);
for(const id of ['physics9-example14-conversion','physics9-example15-conversion'])assert(prefHtml.includes(id.includes('14')?'Textbook femtogram':'Kilometre to megametre'));
const vernier=ch.sections.find(s=>s.code==='1.6.2');
assert(c.renderScienceSourceLayout(vernier,c.getScienceSectionParagraphsWithTranslations(vernier,ch,'phys'),'en',6).includes('tiny unit marks'));
assert.equal(c.DATA.physChapters[1].sourceReview.lastPdfPage,Math.max(...reviewedNumbers.filter(n=>{const page=JSON.parse(fs.readFileSync(path.join(__dirname,`physics-page-${String(n).padStart(3,'0')}.json`),'utf8'));return page.chapterNumber===2;})));
assert.equal(c.DATA.physChapters[1].sourceReview.complete,false);
const unit2=c.DATA.physChapters[1];
for(const sec of unit2.sections.filter(s=>s.sourceLayout)){
 const pairs=c.getScienceSectionParagraphsWithTranslations(sec,unit2,'phys');
 for(const lang of ['en','ur','ps']){
  const rendered=c.renderScienceSourceLayout(sec,pairs,lang,8);
  assert(!/<image\b|<img\b|data:image/.test(rendered));
  for(const b of sec.sourceBlocks.filter(b=>b.svg)){
   assert(b.sourceWidthRatio>0&&b.sourceWidthRatio<=1);
   assert(rendered.includes('max-width:'));
  }
 }
}
const velocity=unit2.sections.find(s=>s.code==='2.3.4');
if(velocity.sourcePdfPages.includes(44)){
 assert(velocity.paras.some(p=>p.text.includes('Things in motion often have variations in speed or direction. ‘The instantaneous velocity')));
 assert.equal(velocity.paras.filter(p=>p.text.startsWith('instantaneous velocity is')).length,0);
}
const motion=unit2.sections.find(s=>s.code==='2.1');
if(motion){const rendered=c.renderScienceSourceLayout(motion,motion.paras,'ur',9);assert(rendered.includes('colspan="3"'));}
console.log(`PASS: Physics pages 6–${reviewedNumbers.at(-1)} active records, aligned translations, exactly-once layout indices, coded/translated visuals, source-size caps, table column groups, source paragraph continuation, synced definitions/examples and honest review status.`);
