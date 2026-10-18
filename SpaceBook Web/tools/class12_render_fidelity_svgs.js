// Local coded-SVG inspection only: no browser, network or application navigation.
const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root = path.resolve(__dirname,'..');
const sections = JSON.parse(fs.readFileSync(path.join(root,'docs/source-verification/class-12/physics-sections-unit20.json'),'utf8'));
const wanted = new Set(process.argv.slice(2).map(Number));
const out = path.join(root,'tmp/class12-review');
(async()=>{
  const jobs=[];
  for(const section of sections) {
    if(!section.sourceClass12Physics || !section.sourceReferences.some(ref=>wanted.has(ref.pdfPage))) continue;
    for(const block of section.sourceBlocks) for(const [lang,key] of [['en','svg'],['ur','svgUrdu'],['ps','svgPashto']]) {
      const target=path.join(out,block.id+'-'+lang+'.png');
      jobs.push(sharp(Buffer.from(block[key])).png().toFile(target));
    }
  }
  await Promise.all(jobs);
  console.log(`Rendered ${jobs.length} local coded-figure previews.`);
})().catch(error=>{console.error(error);process.exitCode=1;});
