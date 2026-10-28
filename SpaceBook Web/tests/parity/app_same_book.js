'use strict';
/* The phone and the app show the SAME book as the website: the printed pages, one at a time, with the same exercises, the same Ans buttons that answer
 * in place, and the same tabs (the owner's rule: "the page must look as it does on the web, every tab that works on the web works in the app").
 * Class 11 English Unit 1 and Class 11 Statistics Unit 1 are read in a phone-size Chrome as the app's WebView shows them (html.sbapp + the app's own
 * stylesheet and bridge) and, for the numbers, on the wide website.
 *     SB_PAGE=lazy.html node --max-old-space-size=4096 tests/parity/app_same_book.js [--app "<folder of the app repo>"]
 * Without the app folder it says SKIP. Dev-only. */
const fs = require('fs'), path = require('path');
const { serve, launch } = require('../baseline/lib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets') + path.sep;
if (!fs.existsSync(ASSETS + 'reader_bridge.js')) { console.log('SKIP  the app folder is not here (' + ASSETS + ')'); process.exit(0); }

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 500) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const catalog = JSON.parse(fs.readFileSync(ASSETS + 'app_catalog.json', 'utf8'));
const call = (cls, subj, i) => catalog.classes.find(c => c.id === cls).subjects.find(s => s.id === subj).chapters[i].o;

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const phone = { viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' };
  const load = async (page, app) => {
    for (let attempt = 0; attempt < 3; attempt++) {
      await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
      try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 120000 }); } catch (e) { continue; }
      await sleep(2500);
      if (!app) return true;
      await page.evaluate(() => document.documentElement.classList.add('sbapp'));
      await page.addStyleTag({ content: fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8') });
      await page.addScriptTag({ content: fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8') });
      if (await page.waitForFunction(() => window.SBApp && typeof window.SBApp.open === 'function', null, { timeout: 20000 }).then(() => true, () => false)) return true;
    }
    return false;
  };

  // ---- the wide website: the numbers the phone must match
  const wctx = await browser.newContext({ viewport: { width: 1600, height: 1000 } });
  const wide = await wctx.newPage();
  wide.on('pageerror', e => errors.push(e.message.slice(0, 120)));
  await load(wide, false);
  await wide.evaluate(() => { openSubject('cls11', 'cls11-eng'); selectSubjectChapter('eng', 1, 'cls11'); }); await sleep(4500);
  await wide.evaluate(() => { const b = [...document.querySelectorAll('.math-nav-tabs button')].find(b => /Exercise/.test(b.textContent) && b.offsetParent); b.click(); }); await sleep(3500);
  const W = await wide.evaluate(() => {
    const box = document.querySelector('#subjTabContent');
    const tabs = [...document.querySelectorAll('.math-nav-tabs button')].filter(b => b.offsetParent).map(b => b.textContent.replace(/\s+/g, ' ').trim());
    return { ans: box.querySelectorAll('.sb-ans').length, tabs, qs: [...box.querySelectorAll('.m6-q .m6-qno')].length };
  });
  await wctx.close();
  check('the wide website: Class 11 English Unit 1 Exercise has Ans on its questions', W.ans >= 60, W);

  // ---- the app's reader
  const actx = await browser.newContext(Object.assign({ deviceScaleFactor: 1 }, phone));
  const page = await actx.newPage();
  page.on('pageerror', e => errors.push(e.message.slice(0, 120)));
  check('the app\'s bridge is running on the page', await load(page, true));
  // the app answers every file from the phone itself (SiteStore): a service worker would bypass it and show the website's older files (found on the phone, X-04)
  const swTry = await page.evaluate(async () => { try { await navigator.serviceWorker.register('sw.js', { scope: './' }); return 'registered'; } catch (e) { return 'refused'; } });
  check('the app\'s bridge refuses the website\'s service worker (it would bypass the phone\'s own copy of the site)', swTry === 'refused', swTry);
  await page.evaluate(([c, s, o]) => window.SBApp.open(c, s, o, 0, ''), ['cls11', 'cls11-eng', call('cls11', 'cls11-eng', 1)]); await sleep(5000);

  const tabs = await page.evaluate(() => window.SBApp.tabs());
  const words = a => JSON.stringify(a.map(t => t.replace(/^\S+\s/, '')));
  check('the app offers the tabs the website shows (Lesson, Exercise, Vocabulary, SLOs, Word Stats) and no tab that goes nowhere', words(tabs) === words(W.tabs), { app: tabs, web: W.tabs });
  let st = await page.evaluate(() => window.SBApp.state());
  check('Lesson: the printed pages of the unit, one at a time (book mode, 12 pages or more)', st.mode === 'book' && st.pages >= 12, st);
  const blank = await page.evaluate(() => [...document.querySelectorAll('.bk-page')].map((p, i) => ({ i, len: (p.textContent || '').trim().length })).filter(x => x.len < 40));
  check('no printed page of the unit is blank', blank.length === 0, blank);

  await page.evaluate(() => window.SBApp.clickTab('Exercise')); await sleep(3500);
  st = await page.evaluate(() => window.SBApp.state());
  check('Exercise: the same pages, opened at the first exercise page', st.mode === 'book' && /Exercise/.test(st.tab) && st.page >= 4, st);
  const A = await page.evaluate(() => ({ ans: document.querySelectorAll('.bk-page .sb-ans').length, qs: document.querySelectorAll('.bk-page .m6-q .m6-qno').length }));
  check('Exercise: as many Ans buttons and numbered questions as on the website', A.ans === W.ans && A.qs === W.qs, { app: A, web: W });

  // Ans in place: a plain question gets its answer in a box under it; a sentence with blanks gets the words in the blanks
  const plain = await page.evaluate(async () => {
    const q = [...document.querySelectorAll('.bk-page .m6-s')].find(e => /Why does the Quaid stress/.test(e.textContent));
    if (!q) return null;
    q.scrollIntoView({ block: 'center' });
    q.querySelector('.sb-ans').click(); await new Promise(r => setTimeout(r, 1200));
    const box = q.closest('.m6-q').querySelector('.sb-solve.sbs-inline');
    return box && !box.hidden ? (box.innerText || '').replace(/\s+/g, ' ').slice(0, 120) : null;
  });
  check('Ans on a question opens its answer under the question, in place (no window)', !!plain && /Model answer/.test(plain) && !(await page.evaluate(() => !!document.querySelector('.bk-modal'))), plain);
  const blanks = await page.evaluate(async () => {
    const s = [...document.querySelectorAll('.bk-page .m6-s')].find(e => /of locusts attacked/.test(e.textContent));
    if (!s) return null;
    s.scrollIntoView({ block: 'center' });
    s.querySelector('.sb-ans').click(); await new Promise(r => setTimeout(r, 1200));
    return { text: s.textContent.replace(/\s+/g, ' ').slice(0, 90), fills: s.querySelectorAll('.sbs-fill').length };
  });
  check('Ans on a sentence with blanks puts the words in the blanks ("A swarm of locusts attacked a herd of cattle.")', !!blanks && blanks.fills === 2 && /swarm.*herd/.test(blanks.text), blanks);

  // the question bank of the SLOs tab: every question answered, the matching ones with the same Ans button
  await page.evaluate(() => window.SBApp.clickTab('SLOs')); await sleep(3500);
  const B = await page.evaluate(() => {
    const box = document.querySelector('#subjTabContent');
    const cards = [...box.querySelectorAll('.class12-question')];
    return { cards: cards.length, pending: box.querySelectorAll('[data-answer-pending]').length, withAns: box.querySelectorAll('.class12-question .sb-ans').length };
  });
  check('SLOs: the Board SLO questions (70) show no "answer still needs to be completed", and most carry the Ans button', B.cards >= 60 && B.pending === 0 && B.withAns >= 40, B);

  // Class 11 Statistics: a printed-page book too, with its answers
  await page.evaluate(([c, s, o]) => window.SBApp.open(c, s, o, 0, ''), ['cls11', 'cls11-stat', call('cls11', 'cls11-stat', 1)]); await sleep(5000);
  await page.evaluate(() => window.SBApp.clickTab('Exercise')); await sleep(3500);
  st = await page.evaluate(() => window.SBApp.state());
  const S = await page.evaluate(() => ({ ans: document.querySelectorAll('.bk-page .sb-ans').length, hist: !![...document.querySelectorAll('.bk-page .m6-q')].find(q => /Histogram is suitable for the presentation of/.test(q.textContent) && q.querySelector('.sb-ans')) }));
  check('Statistics Unit 1: the printed pages, with Ans on the questions (including the Histogram question)', st.mode === 'book' && S.ans >= 30 && S.hist, { st, S });

  // the page books of Class 5 keep their answers in their own store (CLS5_SOLUTIONS): Ans must open the answer, not an empty window
  for (const [subj, i] of [['cls5-sci', 1], ['cls5-eng', 1]]) {
    await page.evaluate(([c, s, o]) => window.SBApp.open(c, s, o, 0, ''), ['cls5', subj, call('cls5', subj, i)]); await sleep(5000);
    await page.evaluate(() => window.SBApp.clickTab('Exercise')); await sleep(3500);
    const C5 = await page.evaluate(async () => {
      const b = [...document.querySelectorAll('.bk-page .sb-ans')][0];
      if (!b) return null;
      b.scrollIntoView({ block: 'center' }); b.click(); await new Promise(r => setTimeout(r, 1500));
      const box = [...document.querySelectorAll('.sb-solve')].find(x => !x.hidden);
      return box ? { inline: box.classList.contains('sbs-inline'), text: (box.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100), modal: !!document.querySelector('.bk-modal') } : null;
    });
    check(`${subj}: Ans opens its answer in place (it once opened an empty window)`, !!C5 && C5.inline && C5.text.length > 8 && !C5.modal, C5);
  }
  await actx.close();

  // ---- a narrow phone browser (not the app) shows the same pages one at a time
  const nctx = await browser.newContext(phone);
  const narrow = await nctx.newPage();
  narrow.on('pageerror', e => errors.push(e.message.slice(0, 120)));
  await load(narrow, false);
  await narrow.evaluate(() => { openSubject('cls11', 'cls11-eng'); selectSubjectChapter('eng', 1, 'cls11'); }); await sleep(4500);
  await narrow.evaluate(() => { const b = [...document.querySelectorAll('.math-nav-tabs button')].find(b => /Exercise/.test(b.textContent) && b.offsetParent); b.click(); }); await sleep(3500);
  const N = await narrow.evaluate(() => ({ singles: document.querySelectorAll('.bk-spread.bk-single').length, pairs: document.querySelectorAll('.bk-spread:not(.bk-single)').length, ans: document.querySelectorAll('.bk-page .sb-ans').length, side: document.documentElement.scrollWidth <= innerWidth + 1 }));
  check('a narrow phone browser: the same printed pages one at a time (no facing pairs), the same Ans buttons, no sideways scrolling', N.singles >= 12 && N.pairs === 0 && N.ans === W.ans && N.side, N);
  await nctx.close();

  check('no script error on any of these pages', errors.length === 0, errors.slice(0, 3));
  console.log('\n' + pass + ' passed, ' + fail + ' failed  (app same book)');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
