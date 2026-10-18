const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'../../..');
const shared=fs.readFileSync(path.join(root,'js/data_phys.js'),'utf8');
const start=shared.indexOf('"phys10Chapters": [');
const end=shared.indexOf('\n});',start);
assert(start>0 && end>start);
const DATA=JSON.parse('{'+shared.slice(start,end)+'}');
const untouched=JSON.stringify(DATA.phys10Chapters.filter(c=>![10,11,12,13,14,15,16,17,18].includes(c.num)));
const context={DATA,state:{selectedClass:'cls10'},katex:require(path.join(root,'assets/vendor/katex/katex.min.js'))};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root,'js/physics_10_source_data.js'),'utf8'),context);
const ch=DATA.phys10Chapters[0];
assert(!ch.sections,'Active Class 10 science reader uses topics');
assert.equal(JSON.stringify(DATA.phys10Chapters.filter(c=>![10,11,12,13,14,15,16,17,18].includes(c.num))),untouched);
assert.equal(ch.definitions.length,24);
assert.equal(ch.slos.length,13);
assert.equal(ch.numericals.length,7,'Keep separate unreviewed exercise problems');
assert.equal(ch.workedExamples.length,6);
const snapshot=JSON.stringify(DATA);
vm.runInContext(fs.readFileSync(path.join(root,'js/physics_10_source_data.js'),'utf8'),context);
assert.equal(JSON.stringify(DATA),snapshot);
context.sanitize=s=>String(s).replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;').replaceAll('>','&gt;');
context.renderInteractiveParagraphHtml=(t,u,p,id)=>`<span data-en="${context.sanitize(t)}" data-ur="${context.sanitize(u)}" data-ps="${context.sanitize(p)}">${context.sanitize(t)}</span>`;
const html=['text','urdu','pashto'].map(field=>context.renderPhysics10SourceSection(ch.topics[0],field==='text'?'en':field==='urdu'?'ur':'ps',0)+context.renderPhysics10SourcePage(ch.sourceOpening)).join('');
assert(html.includes('class="katex"'));
assert(!html.includes('katex-error'));
assert(!/<img\b|<image\b|data:image|<iframe\b/.test(html));
const visibleMath=html.replace(/<annotation\b[^>]*>[\s\S]*?<\/annotation>/g,'');
assert(!/\\frac|\\sqrt/.test(visibleMath),'TeX may appear only inside KaTeX accessibility annotations');
assert(context.physics10SourceSearchText(ch).includes('frequency of oscillation'));
assert(context.physics10SourceSearchText(ch).includes('دورانیہ'));
assert(context.physics10SourceSearchText(ch).includes('فریکونسي'));
assert.equal(ch.topics.filter(t=>t.num==='10.2').length,1);
assert.equal(ch.topics.find(t=>t.num==='10.6').legacyTopicNum,'10.2');
const shm=context.renderPhysics10SourceSection(ch.topics.find(t=>t.num==='10.2'),'en',1);
assert(shm.includes('(10.2)') && shm.includes('(10.3)'));
assert(shm.includes('TIP: Harmonic Motion'));
assert(shm.includes('Editorial clarification'));
assert(shm.includes('phys10-ecg-title'));
assert(!shm.includes('katex-error'));
assert(context.physics10SourceSearchText(ch).includes('restoring force'));
const spring=context.renderPhysics10SourceSection(ch.topics.find(t=>t.num==='10.3'),'en',2);
assert(spring.includes('EXAMPLE 10.2: SPRING RESTORING FORCE'));
assert(spring.includes('26.4'));
assert(spring.includes('TIP: Angular Frequency'));
assert(spring.includes('class="katex"') && !spring.includes('katex-error'));
assert(spring.indexOf('EXAMPLE 10.2') < spring.indexOf('10.3.1 Time period'));
assert(spring.indexOf('Consider a block of mass') < spring.indexOf('EXAMPLE 10.2'));
assert(spring.includes('(10.4)'));
assert(spring.includes('Figure 10.3 - Mass Spring System'));
assert(!spring.includes('(undefined)'));
assert.equal(ch.topics.find(t=>t.num==='10.3').prefixReview.pdfPage,11);
assert(spring.includes('(10.5)') && spring.includes('(10.6)'));
assert(spring.includes('EXAMPLE 10.3: MASS OF OSCILLATING MASS SPRING SYSTEM'));
assert(spring.indexOf('(10.6)') < spring.indexOf('EXAMPLE 10.3'));
for (const lang of ['ur','ps']) assert(!context.renderPhysics10SourceSection(ch.topics.find(t=>t.num==='10.3'),lang,2).includes('katex-error'));
assert.equal(ch.workedExamples[2].source.pdfPage,12);
assert.equal(ch.sourceAssignments.length,6);
assert.equal(ch.sourceAssignments[2].question.text.includes('4 N/m'),true);
assert(!Object.hasOwn(ch.sourceAssignments[2],'answer'));
for(const lang of ['en','ur','ps']){
 const pendulum=context.renderPhysics10SourceSection(ch.topics.find(t=>t.num==='10.4'),lang,3);
 assert(pendulum.includes('<ul>') && pendulum.includes('phys10-pendulum-title'));
 assert(!pendulum.includes('katex-error') && !pendulum.includes('(undefined)'));
 assert(pendulum.includes('(10.7)'));
 assert(pendulum.includes('(10.8)'));
 assert(pendulum.includes('(10.9)'));
}
const props=ch.topics.find(t=>t.num==='10.7');
for(const lang of ['en','ur','ps']){
 const rendered=context.renderPhysics10SourceSection(props,lang,6);
 assert(rendered.includes('phys10-ripple-title') && rendered.includes('phys10-wavefront-title') && rendered.includes('phys10-refraction-title') && rendered.includes('phys10-diffraction-title') && !rendered.includes('undefined'));
 if(lang==='en') assert(rendered.includes('GROUP B') && rendered.includes('A transverse wave on a string'));
}
for(const field of ['text','urdu','pashto']){
 const worked=context.renderPhysics10WorkedExample(ch.workedExamples[4],field);
 assert(worked.includes('3.73') && !worked.includes('katex-error'));
 assert(!/\\frac|\\sqrt/.test(worked.replace(/<annotation\b[^>]*>[\s\S]*?<\/annotation>/g,'')));
}
assert(ch.sourceAssignments[4].question.text.includes('8954.0 m'));
const damping=ch.topics.find(t=>t.num==='10.5');
assert.equal(damping.sourceFigure.geometry.positivePeakCoordinates.length,3);
for(const lang of ['en','ur','ps']){
 const rendered=context.renderPhysics10SourceSection(damping,lang,4);
 assert(rendered.includes('phys10-damping-title'));
 assert(!rendered.includes('undefined') && !/<img\b|<image\b|data:image/.test(rendered));
 assert(rendered.includes('phys10-shock-cutaway-title') && rendered.includes('phys10-damping-types-title'));
}
const wave=ch.topics.find(t=>t.num==='10.6');
assert.equal(wave.sourceActivityFigures[1].geometry.phases.length,5);
for(const lang of ['en','ur','ps']){
 const rendered=context.renderPhysics10SourceSection(wave,lang,5);
 assert(rendered.includes('<ol>') && rendered.includes('phys10-water-cork-title'));
 assert(rendered.includes('phys10-rope-wave-title') && rendered.includes('phys10-em-wave-title'));
 assert(rendered.includes('phys10-transverse-slinky-title') && rendered.includes('class="katex"'));
 assert(!rendered.includes('katex-error'));
 assert(!rendered.includes('undefined') && !/<img\b|<image\b|data:image/.test(rendered));
}
for(const lang of ['en','ur','ps']){
 const rendered=context.renderPhysics10SourceSection(wave,lang,5);
 assert(rendered.includes('phys10-frequency-title') && rendered.includes('phys10-earthquake-title'));
 assert(rendered.includes('(10.10)') && rendered.includes('(10.11)'));
 assert(!rendered.includes('katex-error') && !rendered.includes('undefined'));
}
assert.equal(ch.workedExamples[3].continuationExpected,false);
assert(ch.workedExamples[3].sourceParagraphs.at(-1).text.includes('0.167 N'));
const soundCh=DATA.phys10Chapters.find(c=>c.num===11);
assert.equal(soundCh.sourceReview.sourcePdf,'10thphysics2.pdf');
assert.equal(soundCh.sourceReview.lastFullyVerifiedPdfPage,16);
assert.equal(soundCh.sourceReview.nextPdfPage,17);
assert(soundCh.sourceFrontMatter?.[0].paras.some(p=>p.text==='UNIT 11 SOUND'));
for(const [topicNum,idx,needles] of [['11.1',0,['phys10-sound-fork-title','phys10-bell-title','phys10-sound-prop-title']],['11.2',1,['phys10-ear-title','phys10-bicycle-title','phys10-ruler-title']],['11.3',2,['phys10-intensity-title','phys10-meter-title','<table','β = 10 log']]]){
  for(const lang of ['en','ur','ps']){
    const rendered=context.renderPhysics10SourceSection(soundCh.topics.find(t=>t.num===topicNum),lang,idx);
    assert(needles.every(needle=>rendered.includes(needle)));
    assert(!rendered.includes('undefined') && !rendered.includes('katex-error'));
  }
}
for(const lang of ['en','ur','ps']){
  const rendered=context.renderPhysics10SourceSection(soundCh.topics.find(t=>t.num==='11.4'),lang,3);
  if(lang==='en') assert(rendered.includes('11.4 SPEED OF SOUND WAVES'));
  if(lang==='en') assert(rendered.includes('EXAMPLE 11.2') && rendered.includes('Table 11.3'));
  assert(!rendered.includes('undefined'));
}
assert(context.renderPhysics10SourceSection(soundCh.topics.find(t=>t.num==='11.3'),'en',2).includes('phys10-music-noise-title'));
const opticsCh=DATA.phys10Chapters.find(c=>c.num===12);
assert.equal(opticsCh.sourceReview.lastFullyVerifiedPdfPage,28);
assert.equal(opticsCh.sourceFrontMatter[0].title,'UNIT 12 GEOMETRICAL OPTICS');
for(const lang of ['en','ur','ps']){
  const rendered=context.renderPhysics10SourceSection(opticsCh.topics.find(t=>t.num==='12.1'),lang,12);
  assert(rendered.includes('phys10-reflection-laws'));
  assert(rendered.includes('θᵢ = θᵣ'));
  for(const id of ['phys10-concave-focal','phys10-convex-focal','phys10-principal-focus','phys10-concave-ray-tracing']) assert(rendered.includes(id));
  for(const id of ['phys10-fig128','phys10-solar-mirror','phys10-headlight','phys10-mirror-equation','phys10-mirror-compare']) assert(rendered.includes(id));
  assert(rendered.includes('phys10-example121-rays') && rendered.includes('phys10-example122-rays'));
  assert(rendered.includes('Table 12.1 Single-Mirror System Properties') || lang!=='en');
  assert(!rendered.includes('undefined') && !rendered.includes('katex-error'));
  const refraction=context.renderPhysics10SourceSection(opticsCh.topics.find(t=>t.num==='12.2'),lang,13);
  for(const id of ['phys10-refraction-visual','phys10-refraction-boundary','phys10-glass-slab','phys10-snell-law']) assert(refraction.includes(id));
  for(const id of ['phys10-total-internal-reflection','phys10-tir-tank']) assert(refraction.includes(id));
  assert(refraction.includes('Table 12.2 Indices of Refraction for Some Common Materials') || lang!=='en');
  assert(!refraction.includes('undefined') && !refraction.includes('katex-error'));
}
const figures=html.match(/<svg\b[\s\S]*?<\/svg>/g)||[];
assert(figures.length>=6);
fs.writeFileSync(path.join(root,'tmp/class-10-physics/coded-figure-checks.json'),JSON.stringify(figures));
console.log(`Actual Class 10 data passed through PDF ${ch.sourceReview.lastFullyVerifiedPdfPage}: ${ch.definitions.length} source definitions, 13 outcomes, ${ch.workedExamples.length} source examples and assignments, unchanged other chapters/exercise bank, idempotent upserts, real KaTeX in three languages, source search, no raster embeds.`);




