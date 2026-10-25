'use strict';
/* "Create Test" in a real browser:  node --max-old-space-size=6144 tests/createtest/browser.js
 * Opens the page, picks a class, a subject, a chapter and a topic, asks for questions, creates the test, takes it (right answers for the MCQs), checks the
 * score and the review, builds the printed paper with its answer key, saves the test and reopens it. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  page.on('dialog', d => d.accept());
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
  }
  await page.evaluate(() => { document.querySelector('.nav-link[data-page="create-test"]').click(); });
  await page.waitForSelector('.sbct-pill', { timeout: 20000 });
  check('the Create Test tab opens', await page.evaluate(() => document.querySelector('.nav-tab[data-page="create-test"]').classList.contains('active')));
  await page.click('.sbct-pill[data-n="11"]');                      // Class 11 now has its page books' questions (it had no question file before): its subjects are listed
  await page.waitForSelector('.sbct-subj', { timeout: 30000 });
  check('class 11 lists its subjects (its books carry questions now)', await page.evaluate(() => document.querySelectorAll('input[data-act="subj"]').length >= 8 && !document.querySelector('.sbct-msg[role="alert"]')));
  await page.click('.sbct-pill[data-n="9"]');
  await page.waitForSelector('.sbct-subj', { timeout: 30000 });
  const subjects = await page.$$eval('input[data-act="subj"]', els => els.map(e => e.dataset.s));
  check('class 9 lists at least 8 subjects', subjects.length >= 8 && subjects.includes('cls9-chem') && subjects.includes('cls9-math'), subjects);
  await page.click('button[data-act="all"]');
  const allOn = await page.$$eval('input[data-act="subj"]', els => els.every(e => e.checked));
  check('"Whole class" ticks every subject', allOn);
  const wholeCls = await page.$$eval('.sbct-krow input[data-act="count"]', els => els.map(e => +e.max));
  await page.click('button[data-act="all"]');                       // clear
  await page.click('input[data-act="subj"][data-s="cls9-chem"]');
  await page.click('.sbct-subj:has(input[data-s="cls9-chem"]) > summary');
  await page.click('input[data-act="ch"][data-s="cls9-chem"][data-u="0"]');
  const topics = await page.$$eval('.sbct-tps label', els => els.length);
  check('one chapter ticked shows its topics', topics >= 5, topics);
  const chapMax = await page.$$eval('.sbct-krow input[data-act="count"]', els => els.map(e => +e.max));
  check('a chapter has fewer questions than the whole class', chapMax.reduce((a, b) => a + b, 0) > 0 && chapMax.reduce((a, b) => a + b, 0) < wholeCls.reduce((a, b) => a + b, 0), [chapMax, wholeCls]);
  await page.click('.sbct-tps label:nth-of-type(7) input');         // one topic
  const topicMax = await page.$$eval('.sbct-krow input[data-act="count"]', els => els.map(e => +e.max));
  check('one topic narrows it further (or keeps it)', topicMax.reduce((a, b) => a + b, 0) <= chapMax.reduce((a, b) => a + b, 0), [topicMax, chapMax]);
  await page.click('.sbct-tps label:nth-of-type(7) input');         // back to the whole chapter
  await page.click('button[data-act="preset"][data-i="1"]');        // Class test: 10 MCQs, 5 short, 2 long
  const counts = await page.$$eval('.sbct-krow input[data-act="count"]', els => Object.fromEntries(els.map(e => [e.dataset.k, +e.value])));
  check('the preset asks for MCQs, short and long questions up to what exists', counts.mcq > 0 && counts.short > 0 && counts.mcq <= 10 && counts.short <= 5 && counts.long <= 2, counts);
  await page.fill('input[data-act="title"]', 'Chapter 1 test');
  await page.fill('input[data-act="minutes"]', '20');
  await page.click('button[data-act="create"]');
  await page.waitForSelector('.sbct-item');
  const made = await page.evaluate(() => { const T = SBCreateTest.state.test; return {n: T.items.length, scope: T.scope, allChem: T.items.every(it => it.s === 'cls9-chem' && it.u === 0)}; });
  check('the test has the questions asked for, all from that chapter', made.n === Object.values(counts).reduce((a, b) => a + b, 0) && made.allChem, made);
  check('the paper says what it is made from', /Chemistry/.test(made.scope), made.scope);
  // swap and remove
  const before = await page.evaluate(() => SBCreateTest.state.test.items.map(i => i.i).join());
  await page.click('button[data-act="swap"] >> nth=0');
  const afterSwap = await page.evaluate(() => SBCreateTest.state.test.items.map(i => i.i).join());
  check('Swap replaces one question', before !== afterSwap || (await page.$('.sbct-msg')) !== null);
  const n0 = await page.$$eval('.sbct-item', e => e.length);
  await page.click('button[data-act="drop"] >> nth=0');
  check('Remove takes one out', (await page.$$eval('.sbct-item', e => e.length)) === n0 - 1);
  await page.check('input[data-act="showkey"]');
  check('Show the answers adds an answer to every question', (await page.$$eval('.sbct-ans', e => e.length)) === (await page.$$eval('.sbct-item', e => e.length)));
  // take the test with the right MCQ answers
  await page.click('button[data-act="take"]');
  await page.waitForSelector('.sbct-timer');
  const right = await page.evaluate(() => SBCreateTest.state.test.items.map((it, i) => it.y === 'mcq' ? [i, it.a] : null).filter(Boolean));
  for (const [i, a] of right) await page.check('input[data-act="pick"][data-i="' + i + '"][data-v="' + a + '"]');
  await page.click('button[data-act="finish"] >> nth=0');
  await page.waitForSelector('.sbct-score');
  const res = await page.evaluate(() => { const sc = SBCreateTest.score(); const T = SBCreateTest.state.test; return {got: sc.got, mcqMarks: T.items.filter(i => i.y === 'mcq').reduce((a, i) => a + T.marks.mcq, 0), text: document.querySelector('.sbct-score').textContent}; });
  check('right answers to all MCQs score the marks of the MCQs', res.got === res.mcqMarks, res);
  check('the result shows by subject and chapter', (await page.$$eval('.sbct-table tr', e => e.length)) >= 2);
  // print layout
  await page.click('button[data-act="back2"]');
  await page.evaluate(() => { window.print = () => { window.__printed = true; }; });
  await page.click('button[data-act="printkey"]');
  const pr = await page.evaluate(() => { const b = document.getElementById('sbct-print'); return {printed: !!window.__printed, cls: document.body.classList.contains('sbct-printing'), title: !!b.querySelector('h1'), sections: b.querySelectorAll('.sbct-sec').length, key: b.querySelectorAll('.sbct-keyrow').length, qs: b.querySelectorAll('.sbct-q').length}; });
  check('Print builds the paper with an answer key and asks the browser to print', pr.printed && pr.cls && pr.title && pr.sections >= 3 && pr.key === pr.qs && pr.qs > 5, pr);
  await page.emulateMedia({ media: 'print' });
  const vis = await page.evaluate(() => { const b = document.getElementById('sbct-print'); const cs = getComputedStyle(b); return {v: cs.visibility, d: cs.display, h: b.getBoundingClientRect().height, side: getComputedStyle(document.getElementById('sidebar')).display}; });
  check('in print the paper is visible and the rest of the page is hidden', vis.v === 'visible' && vis.d === 'block' && vis.h > 300 && vis.side === 'none', vis);
  await page.emulateMedia({ media: 'screen' });
  await page.evaluate(() => { document.body.classList.remove('sbct-printing'); });
  // save and reopen
  await page.click('button[data-act="save"]');
  await page.click('button[data-act="back"]');
  check('a saved test is listed on the first page', (await page.$$('button[data-act="open"]')).length >= 1);
  await page.click('button[data-act="open"] >> nth=0');
  await page.waitForSelector('.sbct-item');
  check('opening a saved test shows its questions again', (await page.$$eval('.sbct-item', e => e.length)) === n0 - 1);
  // the tutor's "make a test on it" opens this page with the chapter ticked
  await page.evaluate(() => { SBCreateTest.openWith({cls: 9, s: 'cls9-bio', u: 3}); });
  await page.waitForSelector('input[data-act="ch"][data-s="cls9-bio"][data-u="3"]:checked', { timeout: 20000, state: 'attached' });
  check('its subject is opened so the ticked chapter can be seen', await page.evaluate(() => !!document.querySelector('details.sbct-subj[open] input[data-act="ch"][data-s="cls9-bio"][data-u="3"]')));
  check('"Make a test on it" opens the chapter ticked, with a short test ready', await page.evaluate(() => Object.values(SBCreateTest.state.counts).some(n => n > 0)));
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('Create Test tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
