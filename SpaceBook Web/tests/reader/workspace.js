'use strict';
/* The reader workspace of the website in a real browser (the installed Chrome through Playwright):
 *     node --max-old-space-size=6144 tests/reader/workspace.js
 * Wide screens show a chapter the way full screen does: thin chapter rail that opens to the names, tight header and tabs, the open book
 * (facing pages with the Board SLOs / Exercise bar on every lesson page). Full screen covers the whole page so word cards stay visible.
 * Narrow screens and the Android app (html.sbapp) keep their own layout. Opens Class 5 Maths "Fractions" (js/sb_book_spread.js, js/sb_global_ui.js).
 * Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];

  // a fresh page at one screen size; asApp = the Android app's bridge has marked the page
  async function open(width, height, asApp) {
    const ctx = await browser.newContext({ viewport: { width, height } });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {       // the first load may reload itself once (service worker)
      try {
        await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 });
        await sleep(3000);
        if (await page.evaluate(() => typeof openSubject === 'function')) break;
      } catch (e) { /* reloaded: wait again */ }
    }
    if (asApp) await page.evaluate(() => document.documentElement.classList.add('sbapp'));
    await page.evaluate(() => { goToSubjects('cls5'); }); await sleep(500);
    await page.evaluate(() => { openSubject('cls5', 'cls5-math'); }); await sleep(1000);
    await page.evaluate(() => { selectSubjectChapter('math', 2, 'cls5'); }); await sleep(2500);
    // a slow machine (the CI runner) may still be drawing the chapter: wait until the page is quiet before anything is measured. A page that redraws
    // itself for ever never gets quiet; after 45 s the measuring goes ahead and the "no endless redrawing" check below fails as it should.
    await page.evaluate(() => new Promise(res => {
      const t0 = Date.now();
      const look = () => {
        let c = 0; const mo = new MutationObserver(m => { c += m.length; });
        mo.observe(document.body, { childList: true, subtree: true, attributes: true, characterData: true });
        setTimeout(() => { mo.disconnect(); if (c < 40 || Date.now() - t0 > 45000) res(); else look(); }, 1200);
      };
      look();
    }));
    return { ctx, page };
  }
  const facts = page => page.evaluate(() => {
    const q = s => document.querySelector(s), box = e => { if (!e) return null; const b = e.getBoundingClientRect(); return { l: Math.round(b.left), t: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height) }; };
    const vis = e => !!e && e.getBoundingClientRect().width > 0 && getComputedStyle(e).display !== 'none';
    const head = q('.bk-head');
    return {
      host: box(q('.math-unified-view')), rail: box(q('.math-ch-sidebar')), header: box(q('.math-compact-header-bar')), tabs: box(q('.math-nav-tabs')),
      headGap: head && q('.math-nav-tabs') ? Math.round(head.getBoundingClientRect().top - q('.math-nav-tabs').getBoundingClientRect().bottom) : null,
      spreads: document.querySelectorAll('.bk-spread').length, cards: document.querySelectorAll('.sb-pgcard').length,
      bars: [...document.querySelectorAll('.bk-page .sb-pt')].filter(vis).length,
      names: [...document.querySelectorAll('.math-ch-sidebar .mcb-name')].filter(vis).length,
      railBtn: vis(q('.sb-rail-btn')), fs: !!document.fullscreenElement, fallback: !!q('.sb-fs-fallback')
    };
  });

  // ---------- a wide screen, the website ----------
  let { ctx, page } = await open(1366, 768, false);
  let f = await facts(page);
  check('wide: the chapter rail is thin (numbers only)', f.rail && f.rail.w <= 80 && f.names === 0, f.rail);
  check('wide: the chapter is the open book (facing pages), not page cards', f.spreads > 3 && f.cards === 0, { spreads: f.spreads, cards: f.cards });
  check('wide: header and tabs are tight (header under 50 px, page head within 20 px of the tabs)', f.header && f.header.h <= 50 && f.tabs.h <= 40 && f.headGap !== null && f.headGap <= 20, { header: f.header, tabs: f.tabs, gap: f.headGap });
  check('wide: the workspace almost touches the screen sides', f.host && f.host.l <= 6 && f.host.w >= 1366 - 12, f.host);
  check('wide: the Board SLOs / Exercise bar is on the lesson pages', f.bars >= 3, f.bars);
  check('wide: the rail has an expand button', f.railBtn === true);
  // nobody touches the page: it must not keep redrawing itself (formula glyphs were marked and unmarked on every scan, the page counter was rewritten every 300 ms)
  const idle = await page.evaluate(() => new Promise(res => { let c = 0; const mo = new MutationObserver(m => { c += m.length; }); mo.observe(document.body, { childList: true, subtree: true, attributes: true, characterData: true }); setTimeout(() => { mo.disconnect(); res(c); }, 2500); }));
  check('wide: the open workspace is quiet while nobody touches it (no endless redrawing)', idle < 40, idle);

  await page.click('.sb-rail-btn'); await sleep(600);
  f = await facts(page);
  check('the rail opens to the right and shows the chapter names', f.rail.w >= 270 && f.rail.w <= 320 && f.names >= 9, { rail: f.rail, names: f.names });
  check('the choice is kept', await page.evaluate(() => localStorage.getItem('sbRailOpen')) === '1');
  await page.click('.math-ch-btn >> nth=3'); await sleep(2200);
  f = await facts(page);
  check('the rail stays open when another chapter is chosen', f.rail.w >= 270 && f.spreads > 3, { rail: f.rail, spreads: f.spreads });
  await page.click('.sb-rail-btn'); await sleep(500);
  f = await facts(page);
  check('the rail closes again', f.rail.w <= 80 && f.names === 0, f.rail);

  // a sentence opens its translations
  const sent = await page.evaluate(() => { const e = [...document.querySelectorAll('.bk-page .m6-s')].find(x => { const b = x.getBoundingClientRect(); return b.width > 80 && b.top > 150 && b.bottom < 600; }); if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.left + 30, y: b.top + b.height / 2 }; });
  await page.mouse.click(sent.x, sent.y); await sleep(900);
  check('wide: clicking a sentence opens its translation', await page.evaluate(() => [...document.querySelectorAll('.m6-tr')].some(e => !e.hidden && e.getBoundingClientRect().height > 8)));

  // an Ans button opens a window the size of its answer: a short answer is a small window, a long one a big window that scrolls
  // the chapter opens at its first page (it no longer jumps to the exercise spread): bring the first Ans button of the lesson pages to the middle of the screen
  // some answers are short and show in the page (a fill-in-the-blank, a symbol, a number): those are not windows. Go through the Ans buttons of the page until one opens its window.
  const nAns = await page.evaluate(() => [...document.querySelectorAll('.bk-page .sb-ans')].filter(x => x.getBoundingClientRect().width > 10).length);
  check('wide: an Ans button is on the page', nAns > 0);
  let m = null;
  for (let k = 0; k < Math.min(nAns, 30) && !m; k++) {
    const ans = await page.evaluate(k => { const b = [...document.querySelectorAll('.bk-page .sb-ans')].filter(x => x.getBoundingClientRect().width > 10)[k]; if (!b) return null; b.scrollIntoView({block: 'center'}); return true; }, k);
    if (!ans) break;
    await sleep(300);
    const pos = await page.evaluate(k => { const b = [...document.querySelectorAll('.bk-page .sb-ans')].filter(x => x.getBoundingClientRect().width > 10)[k]; const r = b.getBoundingClientRect(); return { x: r.left + r.width / 2, y: r.top + r.height / 2 }; }, k);
    await page.mouse.click(pos.x, pos.y); await sleep(1500);
    m = await page.evaluate(() => {
      const c = document.querySelector('.bk-modal-card'); if (!c) return null;
      const r = c.getBoundingClientRect(), bar = c.querySelector('.bk-modal-bar').getBoundingClientRect(), body = c.querySelector('.bk-modal-body');
      return { w: Math.round(r.width), h: Math.round(r.height), content: Math.round(bar.height + body.scrollHeight), screen: innerHeight };
    });
    if (!m) await page.mouse.click(pos.x, pos.y);               // close the answer shown in the page and try the next button
  }
  check('wide: the Ans window opens', !!m, m);
  check('wide: the Ans window is as big as its answer (no empty space below it), and never taller than the screen', !!m && (m.h <= m.content + 3 || m.h >= m.screen * 0.9) && m.h <= m.screen, m);
  await page.keyboard.press('Escape'); await sleep(500);
  check('Esc closes the Ans window', await page.evaluate(() => !document.querySelector('.bk-modal')));

  // full screen: the whole page, so the word card is on screen
  await page.click('.sb-fs-btn'); await sleep(2500);
  f = await facts(page);
  check('full screen: the workspace covers the screen with the same thin rail', f.fallback && f.host.w === 1366 && f.host.h === 768 && f.rail.w <= 80, f);
  check('full screen: the browser is in full screen (or the covering layout is the full screen view)', f.fs || f.fallback);
  let shown = null;
  for (const dx of [20, 45, 70, 95]) {
    const w = await page.evaluate(d => { const e = [...document.querySelectorAll('.bk-page .m6-s')].find(x => { const b = x.getBoundingClientRect(); return b.width > 140 && b.top > 150 && b.bottom < 600; }); if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.left + d, y: b.top + b.height / 2 }; }, dx);
    if (!w) break;
    await page.mouse.move(w.x - 30, w.y - 30); await page.mouse.move(w.x, w.y, { steps: 5 }); await sleep(1100);
    shown = await page.evaluate(() => { const c = document.querySelector('.ut-root.ut-card.ut-show'); if (!c) return null; const b = c.getBoundingClientRect(); const top = document.elementFromPoint(b.left + b.width / 2, b.top + b.height / 2); return { onTop: !!(top && top.closest('.ut-root')), rect: [Math.round(b.left), Math.round(b.top), Math.round(b.width), Math.round(b.height)] }; });
    if (shown) break;
  }
  check('full screen: resting the mouse on a word shows its meaning card on top of the page', !!shown && shown.onTop, shown);
  await page.keyboard.press('Escape'); await sleep(900);
  f = await facts(page);
  check('Esc leaves full screen and the workspace goes back into the page', !f.fallback && !f.fs && f.host.l <= 6 && f.host.w < 1366, f);
  await ctx.close();

  // ---------- a narrow screen keeps the page cards ----------
  ({ ctx, page } = await open(600, 900, false));
  f = await facts(page);
  check('narrow: page cards, no open book, no thin rail', f.cards > 3 && f.spreads === 0 && f.rail.w > 400 && f.railBtn === false, { cards: f.cards, spreads: f.spreads, rail: f.rail, btn: f.railBtn });
  await ctx.close();

  // ---------- the Android app's page keeps its own layout ----------
  ({ ctx, page } = await open(1366, 768, true));
  f = await facts(page);
  check('app page (html.sbapp): no open book, normal rail, no expand button', f.cards > 3 && f.spreads === 0 && f.rail.w > 250 && f.railBtn === false, { cards: f.cards, spreads: f.spreads, rail: f.rail, btn: f.railBtn });
  await ctx.close();

  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('reader workspace tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
