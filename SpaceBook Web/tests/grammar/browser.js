'use strict';
/* Grammar Stats in a real browser:  node --max-old-space-size=6144 tests/grammar/browser.js
 * The page from the sidebar, the four languages, a topic from easy to hard, its lessons and its practice (answers, MCQ feedback), the Urdu and Pashto lines,
 * "Open in the book", and the card on Project Stats. Dev-only, never shipped. */
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
  await page.evaluate(() => { document.querySelector('.nav-link[data-page="grammar-stats"]').click(); });
  await page.waitForSelector('.sbgr-topic', { timeout: 30000 });
  check('the Grammar Stats page opens from the sidebar', await page.evaluate(() => state.page === 'grammar-stats'));
  const tiles = await page.$$eval('.sbgr-tile b', e => e.map(x => x.textContent.replace(/,/g, '')));
  check('English shows 30+ topics and 200+ lessons', +tiles[0] >= 30 && +tiles[1] >= 200, tiles);
  const levels = await page.$$eval('.sbgr-lvl', e => e.map(x => +/Level (\d)/.exec(x.textContent)[1]));
  check('topics are listed level by level from easy to hard', levels.length >= 4 && levels.join() === levels.slice().sort().join(), levels);
  for (const [l, n] of [['ur', 10], ['ps', 8], ['ar', 1]]) {
    await page.click('.sbgr-tab[data-l="' + l + '"]'); await page.waitForSelector('.sbgr-tile');
    const c = await page.$$eval('.sbgr-topic', e => e.length);
    check(l + ': its own topics are listed (' + c + ')', c >= n, c);
  }
  check('Arabic says its books are reading lessons', await page.$eval('.sbgr-note', e => /reading lessons/.test(e.textContent)));
  await page.click('.sbgr-tab[data-l="ur"]'); await page.waitForSelector('.sbgr-topic');
  check('an Urdu topic name is shown right to left', await page.$eval('.sbgr-topic .t', e => e.getAttribute('dir') === 'auto' && /[؀-ۿ]/.test(e.textContent)));
  await page.click('.sbgr-tab[data-l="en"]'); await page.waitForSelector('.sbgr-topic');
  await page.click('.sbgr-topic[data-id="adjectives"]'); await page.waitForSelector('.sbgr-lesson');
  const lessons = await page.$$eval('.sbgr-lesson', e => e.length);
  check('a topic opens with the books\' own lessons', lessons >= 5, lessons);
  check('each lesson says where it comes from', await page.$$eval('.sbgr-src', e => e.every(x => /Class \d+/.test(x.textContent))));
  await page.click('.sbgr-tab[data-c="3"]'); await page.waitForSelector('.sbgr-lesson, .sbgr-note');
  check('a class tab shows only that class', await page.$$eval('.sbgr-src .sbgr-chip', e => e.every(x => x.textContent === 'Class 3')));
  await page.click('.sbgr-tab[data-c="0"]');
  await page.check('input[data-act="tr"]');
  check('the Urdu and Pashto lines appear under the lessons', (await page.$$eval('.sbgr-lesson .sbgr-alt', e => e.length)) > 0);
  await page.click('.sbgr-tab[data-t="practice"]'); await page.waitForSelector('.sbgr-q');
  check('practice has questions by class', (await page.$$eval('.sbgr-q', e => e.length)) >= 20);
  await page.click('button[data-act="show"] >> nth=0');
  check('Show the answer reveals the answer', (await page.$$eval('[data-ans] .sbgr-ans', e => e.length)) === 1);
  const mcq = await page.$('input[data-act="pick"]');
  if (mcq) { await mcq.check(); check('an MCQ shows right and wrong at once', (await page.$$eval('.sbgr-opt.ok', e => e.length)) >= 1); }
  else check('an MCQ shows right and wrong at once (no MCQ in this topic: skipped)', true);
  // opening a lesson in the book
  await page.click('.sbgr-tab[data-t="lessons"]'); await page.waitForSelector('button[data-act="open"]');
  await page.click('button[data-act="open"] >> nth=0');
  await sleep(2500);
  check('"Open in the book" goes to the book', await page.evaluate(() => state.page !== 'grammar-stats' || state.activeView !== 'grammar-stats'));
  // Project Stats card
  await page.evaluate(() => { document.querySelector('.nav-link[data-page="home"]').click(); });
  await sleep(1500);
  await page.evaluate(() => { switchHomeStatsTab('project'); });
  await page.waitForSelector('#homeGrammar .sbgr-card', { timeout: 20000 });
  check('Project Stats has a Grammar Stats card for each of the four languages', (await page.$$eval('#homeGrammar .sbgr-card', e => e.length)) === 4);
  await page.click('#homeGrammar .sbgr-card[data-lang="ps"]');
  await page.waitForSelector('.sbgr-topic');
  check('tapping a language opens its topics', await page.evaluate(() => SBGrammar.state.lang === 'ps' && state.page === 'grammar-stats'));
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('Grammar Stats tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
