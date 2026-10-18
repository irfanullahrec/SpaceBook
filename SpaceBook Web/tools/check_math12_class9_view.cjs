const { chromium } = require('C:/Users/Shehroz Khan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url'),assert=require('assert');
const root=path.resolve(__dirname,'..'),output=path.join(root,'docs/source-verification/class-12/math12-view-check.json');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const report={scope:'Class12 mathematics and unchanged Class9 comparison',checks:[],pageErrors:[]};
 try {
  const page=await browser.newPage({viewport:{width:1280,height:900}});page.setDefaultTimeout(10000);page.setDefaultNavigationTimeout(60000);
  page.on('pageerror',e=>report.pageErrors.push(e.message));
  await page.route('**/*',r=>r.request().url().startsWith('file:')?r.continue():r.abort());
  await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'domcontentloaded'});
  await page.evaluate(()=>openSubject('cls9','cls9-math'));
  const tabsSelector='.math-nav-tabs .math-top-tab[data-tab="lesson"], .math-nav-tabs .math-top-tab[data-tab="examples"], .math-nav-tabs .math-top-tab[data-tab="exercises"], .math-nav-tabs .math-top-tab[data-tab="slos"], .math-nav-tabs .math-top-tab[data-tab="formulas"]';
  const class9Tabs=await page.locator(tabsSelector).allTextContents();
  assert.equal(class9Tabs.length,5);
  await page.evaluate(()=>openSubject('cls12','cls12-math'));
  const class12Tabs=await page.locator(tabsSelector).allTextContents();
  console.log(JSON.stringify({class9Tabs,class12Tabs}));
  assert.equal(class12Tabs.length,5);
  assert.equal(await page.locator('.math-ch-list .math-ch-btn').count(),12);
  assert.equal(await page.locator('#math-topic-sec-1-1 .topic-sub-tab-btn').count(),6);
  for(let chapter=0;chapter<12;chapter++) {
   const data=await page.evaluate(chapter=>{
    selectMathChapter(chapter);switchMathTab('slos');
    const ch=MATH_12_DATA[chapter],bank=getMath12StudyBank(ch);
    return {number:ch.number,mcqs:bank.mcqs.length,short:bank.shortQuestions.length,long:bank.longQuestions.length};
   },chapter);
   assert(data.mcqs+data.short+data.long>0,'Empty question bank for '+data.number);
   for(const category of ['mcqs','sqs','lqs']) {
    await page.evaluate(category=>switchMathSloCategory(category),category);
    const text=await page.locator('#mathSloContentArea').innerText();
    assert(!text.includes('[object Object]'),'Unrendered object in unit '+data.number);
    const cards=page.locator('#mathSloContentArea .math12-study-question');
    if(await cards.count()) {
     const first=cards.first();assert((await first.locator('.math12-question-text').innerText()).trim().length>0);await first.locator('.math12-worked-answer > summary').click();
     assert((await first.locator('.math12-worked-answer').innerText()).trim().length>35,'Missing worked answer');
    }
   }
   report.checks.push({...data,categoriesRendered:true});
  }
  for(const width of [1280,390]) {
   await page.setViewportSize({width,height:900});
   await page.evaluate(()=>{selectMathChapter(1);switchMathTab('lesson');});
   const topic=page.locator('#math-topic-sec-2-1');await topic.locator('.math-acc-header').click();
   await topic.locator('[data-subtab="exercise"]').click();
   assert(await topic.locator('.math12-study-question').count()>0,'Topic exercise is not linked');
   await topic.locator('.math12-study-question summary').first().click();
   await topic.locator('[data-subtab="slos"]').click();
   await topic.locator('[data-study-category="lqs"]').click();
   await page.evaluate(()=>{selectMathChapter(0);switchMathTab('lesson');});
   const intro=page.locator('#math-topic-sec-1-1');await intro.locator('.math-acc-header').click();
   for(const lang of ['urdu','pashto']) {
    await intro.locator('[data-subtab="'+lang+'"]').click();
    assert(await intro.locator('[lang="'+(lang==='urdu'?'ur':'ps')+'"]').count()>0,'Missing paired translation');
   }
   await page.screenshot({path:path.join(root,`tmp/math12-class9-language-${width}.png`)});
   await page.evaluate(()=>{selectMathChapter(1);switchMathTab('slos');switchMathSloCategory('mcqs');});
   const mcq=page.locator('.math12-study-question').first();
   const buttons=mcq.locator('[data-option]');assert(await buttons.count()>1);
   await buttons.first().click();
   assert(await mcq.locator('.math12-worked-answer').evaluate(e=>e.open));
   assert((await mcq.locator('[role="status"]').innerText()).length>10);
   assert.equal(await mcq.locator('.math12-option-correct').count(),1);
   const overflow=await page.locator('#mathTopicArea').evaluate(e=>e.getBoundingClientRect().right>innerWidth+2);
   assert(!overflow,'Study area overflows at '+width);
   await page.screenshot({path:path.join(root,`tmp/math12-class9-mcqs-${width}.png`)});
   report.checks.push({viewport:width,topicExercise:true,translations:true,mcqFeedback:true,answerReveal:true});
  }
  await page.evaluate(()=>openSubject('cls9','cls9-math'));
  assert.equal(await page.locator(tabsSelector).count(),class9Tabs.length);
  report.class9Preserved=true;report.passed=true;
 } finally {report.checkedUtc=new Date().toISOString();fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');await browser.close();}
 console.log(JSON.stringify(report));
})().catch(e=>{console.error(e);process.exitCode=1;});
