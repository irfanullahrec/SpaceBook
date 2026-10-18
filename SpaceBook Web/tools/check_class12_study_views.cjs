const { chromium }=require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),assert=require('assert/strict'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const report={checkedUtc:new Date().toISOString(),scope:'Class12 shared routing, question cards, answer reveal and preserved Class9 behavior; not full source verification.',subjects:[],pageErrors:[]};
 try{
  const page=await browser.newPage({viewport:{width:1280,height:900}});page.setDefaultNavigationTimeout(60000);page.setDefaultTimeout(10000);
  page.on('pageerror',error=>report.pageErrors.push(error.message));
  await page.route('**/*',route=>route.request().url().startsWith('file:')?route.continue():route.abort());
  await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'domcontentloaded'});
  const subjects=[['phys','phy'],['chem','chem'],['stat','stat'],['eng','eng'],['urdu','urdu'],['bio','bio'],['pakstudy','pak'],['comp','comp'],['civics','civics'],['econ','econ'],['hpe','hpe'],['islopt','islopt'],['islhist','islhist'],['quran','quran']];
  for(const [key,id] of subjects){
   const data=await page.evaluate(({key,id})=>{
    openSubject('cls12','cls12-'+id);
    const chapters=getSubjectChapterList(key,'cls12'),index=chapters.findIndex(c=>Number(c.number??c.num)>0);
    selectSubjectChapter(key,index<0?0:index,'cls12');
    const chapter=chapters[index<0?0:index];
    return {subject:key,chapters:chapters.length,chapter:chapter.number??chapter.num,index:index<0?0:index,title:chapter.title||chapter.name,
     inventory:chapters.map(c=>({chapter:c.number??c.num,...Object.fromEntries(Object.entries(getClass12QuestionBank(c,'study')).map(([kind,items])=>[kind,{count:items.length,missingAnswer:items.filter(q=>!(q.sol||q.solution||q.answer!==undefined||q.ans!==undefined||q.explanation||q.exp||q.steps?.length||q.correct!==undefined||q.desc)).length}]))}))};
   },{key,id});
   assert(data.chapters>0,key+' has chapters');
   assert.equal(await page.locator('#subjectTopicArea [data-tab="booktext"]').count(),0);
   assert((await page.locator('.math-sidebar-sub').innerText()).includes('textbook units'));
   for(const kind of ['exercise','slos']){
    await page.evaluate(({key,kind,index})=>switchSubjectTab(key,kind,index,'cls12'),{key,kind,index:data.index});
    const tabs=await page.locator('#subjTabContent [data-category]').evaluateAll(nodes=>nodes.map(n=>n.dataset.category));
    for(const category of tabs){
     await page.evaluate(({key,kind,category})=>class12SwitchQuestionCategory(key,kind==='exercise'?'exercise':'study',category),{key,kind,category});
     const cards=page.locator('#subjTabContent .class12-question');
     assert(await cards.count()>0,key+' '+category+' cards');
     const card=cards.first();assert((await card.locator('.class12-question-text').innerText()).trim().length);
     report.currentStep={subject:key,kind,category};
     try{await card.locator('.class12-answer > summary').click();}
     catch(error){
      report.failureGeometry=await card.evaluate(e=>({card:e.outerHTML.slice(0,1800),parents:[e,...(function*(n){while(n.parentElement){yield n=n.parentElement;}})(e)].map(n=>({tag:n.tagName,class:n.className,display:getComputedStyle(n).display,visibility:getComputedStyle(n).visibility,rect:{width:n.getBoundingClientRect().width,height:n.getBoundingClientRect().height}}))}));
      await page.screenshot({path:path.join(root,'tmp/class12-study-failure.png')});throw error;
     }
     assert(await card.locator('.class12-answer').evaluate(e=>e.open));
     if(await card.locator('button[data-option]').count()){
      await card.locator('button[data-option]').first().click();
      assert.equal(await card.locator('.class12-correct').count(),1);
      assert((await card.locator('[role="status"]').innerText()).length>5);
     }
    }
   }
   await page.evaluate(({key,id,number})=>openGenericChapterDetails('cls12','cls12-'+id,key,number),{key,id,number:data.chapter});
   assert(await page.locator('[data-class12-subject="'+key+'"]').count(),key+' source search route');
   await page.evaluate(({key,last})=>selectSubjectChapter(key,last,'cls12'),{key,last:data.chapters-1});
   report.subjects.push(data);
  }
  for(const width of [1280,390]){
   await page.setViewportSize({width,height:900});
   await page.evaluate(()=>{openSubject('cls12','cls12-bio');selectSubjectChapter('bio',0,'cls12');switchSubjectTab('bio','exercise',0,'cls12');class12SwitchQuestionCategory('bio','exercise','mcqs');});
   const first=page.locator('.class12-question').first();
   await first.locator('[data-option="2"]').click();
   assert((await first.locator('[role="status"]').innerText()).startsWith('Correct.'));
   assert.equal(await first.locator('[data-option="2"].class12-correct').count(),1,'ans index is respected');
   const bounds=await page.locator('#subjectTopicArea').evaluate(e=>({right:e.getBoundingClientRect().right,width:innerWidth}));
   assert(bounds.right<=bounds.width+2,'Class12 content overflow at '+width);
   await page.screenshot({path:path.join(root,'tmp/class12-study-biology-'+width+'.png')});
  }
  await page.evaluate(()=>openSubject('cls9','cls9-bio'));
  assert.equal(await page.locator('[data-class12-subject]').count(),0);
  assert.equal(report.pageErrors.length,0,report.pageErrors.join('\n'));
  report.passed=true;
 }finally{fs.writeFileSync(path.join(root,'docs/source-verification/class-12/shared-view-check.json'),JSON.stringify(report,null,2)+'\n');await browser.close();}
 console.log(JSON.stringify({passed:report.passed,subjects:report.subjects.length,pageErrors:report.pageErrors}));
})().catch(error=>{console.error(error);process.exitCode=1;});
