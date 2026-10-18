const {chromium}=require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),assert=require('assert/strict'),{pathToFileURL}=require('url');const root=path.resolve(__dirname,'..');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const report={checkedUtc:new Date().toISOString(),scope:'Actual loaded reviewed Mathematics translations, language tabs, word meanings and original formulas; remaining sections stay pending.',pageErrors:[]};try{
 const page=await browser.newPage({viewport:{width:1280,height:900}});page.setDefaultNavigationTimeout(60000);page.setDefaultTimeout(10000);page.on('pageerror',e=>report.pageErrors.push(e.message));await page.route('**/*',r=>r.request().url().startsWith('file:')?r.continue():r.abort());await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'domcontentloaded'});
 report.sections=await page.evaluate(()=>{
  openSubject('cls12','cls12-math');const output=[];
  for(const unit of MATH_12_DATA){const r=Number(unit.number)===1?globalThis.MATH12_TRANSLATION_COMPLETIONS_REPORT:globalThis['MATH12_UNIT'+unit.number+'_TRANSLATION_REPORT'];if(!r)continue;
   const ids=r.completedSectionIds||r.sections.map(x=>x.id);
   for(const id of ids){const section=unit.sections.find(x=>x.id===id);for(const language of ['urdu','pashto']){const html=renderMath12TopicContent(section,unit,language);const doc=new DOMParser().parseFromString(html,'text/html');output.push({unit:unit.number,id,language,paragraphs:doc.querySelectorAll('[lang="'+(language==='urdu'?'ur':'ps')+'"]').length,pending:/Remaining passages are shown in English/.test(html),hasArabicScript:/[\u0600-\u06ff]/.test(html),unrendered:/\[object Object\]/.test(html)});}}
  }return output;
 });
 for(const r of report.sections){assert(r.paragraphs>0&&r.hasArabicScript,JSON.stringify(r));assert.equal(r.pending,false,JSON.stringify(r));assert.equal(r.unrendered,false,JSON.stringify(r));}
 report.interactions=[];
 for(const width of [1280,390]){await page.setViewportSize({width,height:900});await page.evaluate(()=>{selectMathChapter(4);switchMathTab('lesson');});const topic=page.locator('#math-topic-sec-5-1');await topic.locator('.math-acc-header').click();const word=topic.locator('[data-math12-word="vector"]').first();await word.click();assert(await page.locator('#math12-word-meaning').evaluate(e=>e.open));assert(/[\u0600-\u06ff]/.test(await page.locator('#math12-word-meaning [lang="ps"]').innerText()));await page.locator('[aria-label="Close word meaning"]').click();
  for(const language of ['urdu','pashto']){await topic.locator('[data-subtab="'+language+'"]').click();assert(!/Remaining passages are shown/.test(await topic.innerText()));assert(await topic.locator('[dir="rtl"]').count()>0);await page.screenshot({path:path.join(root,'tmp/math12-unit5-'+language+'-'+width+'.png')});}
  report.interactions.push({width,wordMeaning:true,urdu:true,pashto:true});
 }
 assert.deepEqual(report.pageErrors,[]);report.passed=true;
}finally{fs.writeFileSync(path.join(root,'docs/source-verification/class-12/translation-view-check.json'),JSON.stringify(report,null,2)+'\n');await browser.close();}console.log(JSON.stringify({passed:report.passed,renderedSectionLanguages:report.sections?.length,interactions:report.interactions,pageErrors:report.pageErrors}));})().catch(e=>{console.error(e);process.exitCode=1;});
