const {chromium}=require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url');const path=require('path');const assert=require('assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});try{
 const p=await b.newPage();await p.route('**/*',r=>r.request().url().startsWith('file:')?r.continue():r.abort());await p.goto(pathToFileURL(path.resolve(__dirname,'../index.html')).href);
 const stats=await p.evaluate(()=>{for(const [text,pairs] of Object.entries(MATH12_SENTENCE_TRANSLATIONS)){if(pairs.map(p=>p.en).join(' ')!==text||pairs.some(p=>!p.ur||!p.ps))throw Error('Broken sentence alignment');}return {passages:Object.keys(MATH12_SENTENCE_TRANSLATIONS).length,sentences:Object.values(MATH12_SENTENCE_TRANSLATIONS).flat().length};});
 for(const width of [1280,390]){
  await p.setViewportSize({width,height:844});await p.evaluate(()=>{openSubject('cls12','cls12-math');selectMathChapter(0);switchMathTab('lesson')});
  const id=await p.evaluate(()=>MATH_12_DATA[0].sections[0].id);await p.locator('#math-topic-'+id+' .math-acc-header').evaluate(e=>e.click());
  const passages=p.locator('.math12-translated-passage');assert(await passages.count()>0);const first=passages.locator('details').first();
  await first.locator('summary').focus();await p.keyboard.press('Enter');assert(await first.locator('p[lang="ur"]').isVisible());assert(await first.locator('p[lang="ps"]').isVisible());
  // A controlled empty device voice list must produce an honest status.
  await p.evaluate(()=>{window.__math12Voices=speechSynthesis.getVoices;speechSynthesis.getVoices=()=>[];});
  await first.getByRole('button',{name:'Listen in Pashto',exact:true}).click();assert((await first.innerText()).includes('No Pashto voice is available'));
  await p.evaluate(()=>{speechSynthesis.getVoices=window.__math12Voices;});
  await first.locator('[data-math12-word="science"]').click();const dialog=p.locator('#math12-word-meaning');assert(await dialog.isVisible());assert((await dialog.locator('p[lang="ps"]').innerText()).includes('ساینس'));
  await dialog.getByRole('button',{name:'Close word meaning'}).click();assert(!await dialog.isVisible());
  for(const c of await passages.all())assert(!await c.evaluate(e=>e.scrollWidth>e.clientWidth+2),'Translation overflow');
  await first.scrollIntoViewIfNeeded();await p.screenshot({path:path.join(__dirname,'source-review/math12-translation-'+width+'.png')});
 }
 console.log(JSON.stringify({...stats,result:'Sentence alignment, RTL reading, word dialog, device voice handling and desktop/mobile layout passed'}));
}finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1)});
