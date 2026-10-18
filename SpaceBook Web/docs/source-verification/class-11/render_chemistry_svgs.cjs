// librsvg renders SVG gradients and markers that the PDF fallback omits.
const fs=require('fs');
const path=require('path');
const sharp=require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../../..');
(async()=>{
 for(const n of process.argv.slice(2).map(Number)){
  const page=JSON.parse(fs.readFileSync(path.join(__dirname,`chemistry-page-${n}.json`),'utf8'));
  for(const [i,figure] of (page.figures||[]).entries()){
   const output=path.join(root,`tmp/class-11/chemistry-p${n}-fig${i+1}-qa.png`);
   await sharp(Buffer.from(figure.svg),{density:144}).flatten({background:'#ffffff'}).png().toFile(output);
   console.log(output);
  }
 }
})().catch(error=>{console.error(error);process.exitCode=1;});
