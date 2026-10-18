const {chromium}=require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url'),fs=require('fs'),path=require('path'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const report={checkedUtc:new Date().toISOString(),queries:[],routes:[],pageErrors:[]};try{
 const page=await browser.newPage({viewport:{width:1280,height:900}});page.setDefaultNavigationTimeout(60000);page.setDefaultTimeout(10000);page.on('pageerror',e=>report.pageErrors.push(e.message));
 await page.route('**/*',r=>r.request().url().startsWith('file:')?r.continue():r.abort());await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'domcontentloaded'});
 for(const query of ['integration','biology','chemistry','physics','english','class 12','conics','electrostatics','nothingmatches012345']){
  const data=await page.evaluate(query=>{handleGlobalSearch(query);return {query,text:document.querySelector('#searchResultsDropdown').innerText,actions:window.spaceBookSearchActions.length};},query);
  assert(!data.text.includes('[object Object]'));assert(data.actions<=15);report.queries.push({query,actions:data.actions});
 }
 for(const item of [
  {query:'integration',text:'MATH · Ch 6:',selector:'#math-topic-sec-6-1',route:'Class12 Mathematics Unit6'},
  {query:'conics',text:'MATH · Ch 9:',selector:'#math-topic-sec-9-1',route:'Class12 Mathematics Unit9'},
  {query:'electrostatics',text:'PHY · Ch 11:',selector:'[data-class12-subject="phys"]',route:'Class12 Physics Unit11'},
  {query:'biodiversity',text:'Class 9 Biology',selector:'#subjectTopicArea, #bioTopicArea',route:'Class9 Biology'}
 ]){
  await page.evaluate(query=>handleGlobalSearch(query),item.query);
  const result=page.locator('.search-result-item').filter({hasText:item.text}).first();assert.equal(await result.count(),1,item.route+' result');await result.click();
  assert(await page.locator(item.selector).count(),item.route+' opened');
  if(item.route.startsWith('Class12 Mathematics'))assert.equal(await page.locator('#genericChapterModal.open').count(),0);
  assert.equal(await page.locator('#searchResultsDropdown').evaluate(e=>e.style.display),'none');report.routes.push(item.route);
 }
 await page.evaluate(()=>handleGlobalSearch('a'));assert.equal(await page.evaluate(()=>window.spaceBookSearchActions.length),0);
 assert.deepEqual(report.pageErrors,[]);report.passed=true;
}finally{fs.writeFileSync(path.join(root,'docs/source-verification/class-12/search-check.json'),JSON.stringify(report,null,2)+'\n');await browser.close();}console.log(JSON.stringify(report));})().catch(e=>{console.error(e);process.exitCode=1;});
