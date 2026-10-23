'use strict';
/* "Ask SpaceBook" (the offline tutor) in a real browser:  node --max-old-space-size=6144 tests/tutor/browser.js
 * Asks questions with known answers in the books and checks the answer, where it comes from and the links; asks in Urdu; asks in Class 11 (chapter pointers);
 * asks nonsense (it must say it found nothing); goes offline after the files are loaded and asks again (no network request is made). Dev-only, never shipped. */
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
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
  }
  await page.evaluate(() => { document.querySelector('.nav-link[data-page="assistant"]').click(); });
  await page.waitForSelector('.sbtu textarea', { timeout: 30000 });
  check('the Ask tab opens', await page.evaluate(() => state.page === 'assistant' && !!document.querySelector('.nav-tab[data-page="assistant"].active')));
  const ask = async (q, scope, wait = 120000) => {
    if (scope !== undefined) await page.selectOption('select[data-act="cls"]', String(scope));
    const n = await page.$$eval('.sbtu-a', e => e.length);
    const t0 = Date.now();
    await page.fill('.sbtu textarea', q); await page.click('button[data-act="ask"]');
    await page.waitForFunction(k => document.querySelectorAll('.sbtu-a').length > k && !document.querySelector('.sbtu-a:last-of-type .sbtu-prog'), n, { timeout: wait });
    return { text: await page.$eval('.sbtu-a:last-of-type', e => e.innerText.replace(/\s+/g, ' ')), html: await page.$eval('.sbtu-a:last-of-type', e => e.innerHTML), ms: Date.now() - t0 };
  };
  let a = await ask('What is a covalent bond?', 9);
  check('a definition question gets the defining sentence of the book', /A covalent bond is formed when two atoms are joined together by sharing of electrons/.test(a.text) && /Chemistry/.test(a.text), a.text.slice(0, 200));
  check('the answer says where it comes from and offers the chapter', /Class 9 · Chemistry · 4 Structure of Molecules/.test(a.text) && /data-act="open"/.test(a.html));
  check('a one-class question is answered quickly', a.ms < 20000, a.ms);
  a = await ask('meaning of abundant', 9);
  check('a word gets its meaning in Urdu, Pashto and Arabic from the lexicon', /وافر/.test(a.text) && /ډېر|ډیر/.test(a.text) && /وفير/.test(a.text), a.text.slice(0, 200));
  a = await ask('Which gas do plants take in for photosynthesis?', 9);
  check('a question the books also ask gets passages or an answer from the book', /Class 9/.test(a.text) && (/ANSWER|FROM THE BOOKS/i.test(a.text)), a.text.slice(0, 200));
  a = await ask('qzxvw plorbtq nonsense', 9);
  check('a question with no match says it found nothing', /could not find that in the books/.test(a.text), a.text.slice(0, 200));
  a = await ask('Newton second law of motion', 11);
  check('Class 11 gives chapter pointers from the search index', /Class 11 · Physics/.test(a.text) && /Open the chapter/.test(a.text), a.text.slice(0, 200));
  a = await ask('نمک کیا ہے؟', 0, 240000);
  check('an Urdu question finds Urdu passages and the word meaning', /نمک/.test(a.text) && /Salt|salt/.test(a.text) || /FROM THE BOOKS/i.test(a.text), a.text.slice(0, 200));
  check('searching all classes finishes in a reasonable time', a.ms < 120000, a.ms);
  // make a test from an answer
  await page.selectOption('select[data-act="cls"]', '9');
  a = await ask('What is a covalent bond?');
  const btn = await page.$('.sbtu-a:last-of-type button[data-act="test"]');
  check('the answer offers "Make a test on it"', !!btn);
  if (btn) { await btn.click(); await page.waitForSelector('.sbct-pill', { timeout: 20000 }); await page.waitForSelector('input[data-act="ch"]:checked', { timeout: 20000, state: 'attached' });
    check('"Make a test on it" opens Create Test with that chapter ticked', await page.evaluate(() => state.page === 'create-test' && Object.keys(SBCreateTest.state.chapters).length === 1)); }
  // offline: the files of class 9 are loaded, a new question needs no network
  await page.evaluate(() => { document.querySelector('.nav-link[data-page="assistant"]').click(); });
  await page.waitForSelector('.sbtu textarea');
  await page.selectOption('select[data-act="cls"]', '9');
  const requests = [];
  page.on('request', r => { if (/content\/(assistant|testbank|search)\//.test(r.url())) requests.push(r.url()); });
  await ctx.setOffline(true);
  a = await ask('What is a covalent bond?');
  check('offline, with the files already loaded, it still answers', /sharing of electrons/.test(a.text), a.text.slice(0, 160));
  check('and it made no request for them again', requests.length === 0, requests);
  await ctx.setOffline(false);
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('tutor tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
