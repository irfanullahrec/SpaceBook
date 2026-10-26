'use strict';
/* The days of a Study Plan as cards, in a real Chrome:   node --max-old-space-size=6144 tests/plan/day_cards.js [--shots <dir>]
 * A plan of 61 days: the days are cards, six in a row; at a desktop size (1920 x 1080 screen, page at 100 %) at least four rows of them are in view at once, at phone size
 * the six still fit. A closed card shows the percentage of its day and, when every task of the day is done, a tick; a click opens the day under its row (its tasks, the
 * Skip this day button), a second click (or Close) closes it; the open days stay open when a task is ticked and the page is drawn again; the page does not jump to
 * today on that redraw. Local only (CI has no browser). Dev-only, never shipped. */
const path = require('path');
const { serve, launch } = require('../baseline/lib');
const args = process.argv.slice(2), shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null;
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };

async function openPlan(page, url) {
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && window.SBStudyPlan && window.SBMastery, null, { timeout: 120000 }); await sleep(2500); break; } catch (e) { /* retry */ }
  }
  await page.evaluate(() => {
    localStorage.removeItem('sb_study_plans_v1');
    const d = new Date(), pad = n => String(n).padStart(2, '0'), ymd = x => x.getFullYear() + '-' + pad(x.getMonth() + 1) + '-' + pad(x.getDate());
    const end = new Date(d); end.setDate(end.getDate() + 60);
    const plan = SBStudyPlan.createPlan({ name: 'Class 7 Maths', classId: 'cls7', scope: [{ subj: 'cls7-math', ch: [0, 1, 2] }], cats: ['read', 'mcq', 'num', 'ex'], start: ymd(d), end: ymd(end), weekdays: [0, 1, 2, 3, 4, 5, 6], slots: [{ from: '16:00', to: '18:00' }], revision: true });
    SBStudyPlan.add(plan);
    const dates = [...new Set(plan.sessions.map(s => s.date))].sort();
    plan.sessions.filter(s => s.date === dates[0]).forEach(s => s.tasks.forEach(k => { k.done = k.n; }));                       // the first day is all done
    plan.sessions.filter(s => s.date === dates[1]).forEach(s => s.tasks.forEach((k, i) => { if (i === 0) k.done = Math.ceil(k.n / 2); }));   // the second is partly done
    SBStudyPlan.persist(plan);
    window.__plan = plan;
    document.querySelector('.nav-link[data-page="study-plan"]').click();
    setTimeout(() => SBStudyPlan.open(plan.id), 300);
  });
  await page.waitForSelector('.spx-dc', { timeout: 20000 });
  await sleep(900);
}

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  // ---- desktop: a 1920 x 1080 screen with the browser's bars leaves about 1900 x 880 for the page
  {
    const ctx = await browser.newContext({ viewport: { width: 1900, height: 880 } });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    page.on('dialog', d => d.accept());
    await openPlan(page, url);
    const geo = await page.evaluate(() => {
      const cards = [...document.querySelectorAll('.spx-dc')], rows = [...document.querySelectorAll('.spx-dayrow')];
      const r0 = rows[0].getBoundingClientRect();
      return { n: cards.length, perRow: rows.map(r => r.children.length), cols: getComputedStyle(rows[0]).gridTemplateColumns.split(' ').length, cardH: Math.round(cards[0].getBoundingClientRect().height), rowW: Math.round(r0.width) };
    });
    check('the 61 days are cards, six in a row (the last row holds what is left)', geo.n === 61 && geo.perRow.slice(0, -1).every(n => n === 6) && geo.cols === 6, geo);
    // scroll so that the first card row is at the top of the view, as the page does for today
    const view = await page.evaluate(() => {
      const first = document.querySelector('.spx-dayrow'); window.scrollTo(0, window.scrollY + first.getBoundingClientRect().top - 12);
      const rows = [...document.querySelectorAll('.spx-dayrow')];
      const full = rows.filter(r => { const b = r.getBoundingClientRect(); return b.top >= 0 && b.bottom <= window.innerHeight; });
      return { fullRows: full.length, vh: window.innerHeight };
    });
    check('at 100 % on a desktop screen at least four rows of day cards are in view at once', view.fullRows >= 4, view);
    const c0 = await page.$eval('.spx-dc:nth-child(1)', e => ({ cls: e.className, txt: e.innerText.replace(/\s+/g, ' ').trim(), tick: e.querySelector('.spx-dc-t').textContent, exp: e.getAttribute('aria-expanded') }));
    const c1 = await page.$eval('.spx-dc:nth-child(2)', e => ({ cls: e.className, txt: e.innerText.replace(/\s+/g, ' ').trim(), tick: e.querySelector('.spx-dc-t').textContent }));
    const c2 = await page.$eval('.spx-dc:nth-child(3)', e => ({ txt: e.innerText.replace(/\s+/g, ' ').trim(), tick: e.querySelector('.spx-dc-t').textContent }));
    check('a day with every task done shows 100 % and a tick, today is marked', /spx-dc-ok/.test(c0.cls) && /spx-dc-today/.test(c0.cls) && c0.tick === '✓' && /100/.test(c0.txt) && c0.exp === 'false', c0);
    check('a day that is partly done shows its percentage and no tick', /spx-dc-part/.test(c1.cls) && c1.tick === '' && /\d+\s*%/.test(c1.txt) && !/^.*\b100\s*%/.test(c1.txt), c1);
    check('a day not started shows 0 % and no tick', /\b0\s*%/.test(c2.txt) && c2.tick === '', c2);
    if (shots) await page.screenshot({ path: path.join(shots, 'days_desktop.png') });
    // open the third day: its tasks appear under its row, the card says so
    await page.click('.spx-dc[data-d]:nth-child(3)');
    await page.waitForSelector('.spx-daydetails .spx-day', { timeout: 5000 });
    const o1 = await page.evaluate(() => { const d = document.querySelector('.spx-daydetails .spx-day'), card = document.querySelector('.spx-dc-open'); return { tasks: d.querySelectorAll('.spx-task').length, hasSkip: !!d.querySelector('.spx-skipday'), exp: card && card.getAttribute('aria-expanded'), sameRow: card && card.closest('.spx-dayrow').nextElementSibling.contains(d) }; });
    check('a click opens the day under its row, with its tasks and the Skip button', o1.tasks > 0 && o1.hasSkip && o1.exp === 'true' && o1.sameRow, o1);
    if (shots) await page.screenshot({ path: path.join(shots, 'days_open.png') });
    // open a second day of another row; tick a task in the first: the page is drawn again and both stay open, and it stays where it was
    await page.click('.spx-dc[data-d]:nth-child(5)');
    const y0 = await page.evaluate(() => { window.scrollTo(0, window.scrollY + 120); return window.scrollY; });
    const before = await page.evaluate(() => document.querySelectorAll('.spx-daydetails .spx-day').length);
    await page.click('.spx-daydetails .spx-day .spx-task:nth-of-type(1) input[data-act="part"]').catch(() => null);
    await page.evaluate(() => { const k = window.__plan; });
    const ticked = await page.evaluate(() => { const row = document.querySelector('.spx-daydetails .spx-task'); if (!row) return false; const p = SBStudyPlan.plans()[0]; const s = p.sessions.find(x => x.id === row.dataset.sess); const k = s.tasks.find(x => x.id === row.dataset.task); k.done = Math.max(1, Math.floor(k.n / 2)); SBStudyPlan.persist(p); SBStudyPlan.render(); return true; });
    await sleep(400);
    const after = await page.evaluate(() => ({ open: document.querySelectorAll('.spx-daydetails .spx-day').length, y: window.scrollY }));
    check('open days stay open when the page is drawn again (a task changed), and the page stays where it was', ticked && after.open === before && Math.abs(after.y - y0) < 40, { before, after, y0 });
    // close both: click the card again, and the Close button
    await page.click('.spx-dc-open');
    const left = await page.evaluate(() => document.querySelectorAll('.spx-daydetails .spx-day').length);
    await page.click('.spx-closeday');
    const none = await page.evaluate(() => ({ open: document.querySelectorAll('.spx-daydetails .spx-day').length, cardsOpen: document.querySelectorAll('.spx-dc-open').length }));
    check('a second click on the card, or Close, closes the day, and the card shows its percentage again', left === 1 && none.open === 0 && none.cardsOpen === 0, { left, none });
    // Jump to today opens today's day
    await page.click('[data-act="today"]');
    await page.waitForSelector('#spx-d-' + new Date().toISOString().slice(0, 4), { timeout: 100 }).catch(() => null);
    await sleep(500);
    check('"Jump to today" opens today\'s day', await page.evaluate(() => { const c = document.querySelector('.spx-dc-today'); return !!c && c.getAttribute('aria-expanded') === 'true' && !!document.querySelector('.spx-daydetails .spx-isToday'); }));
    check('no page errors (desktop)', errors.length === 0, errors.slice(0, 3));
    await ctx.close();
  }
  // ---- a phone: six cards still fit in a row, and a card can be opened
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await openPlan(page, url);
    const g = await page.evaluate(() => {
      const rows = [...document.querySelectorAll('.spx-dayrow')], r = rows[0], cards = [...r.children].map(c => c.getBoundingClientRect());
      return { n: cards.length, minW: Math.round(Math.min(...cards.map(c => c.width))), h: Math.round(cards[0].height), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1, right: Math.round(Math.max(...cards.map(c => c.right))), vw: window.innerWidth };
    });
    check('on a phone six cards fit in a row without sideways scrolling', g.n === 6 && g.right <= g.vw && !g.overflowX && g.minW >= 44, g);
    await page.evaluate(() => { const f = document.querySelector('.spx-dayrow'); window.scrollTo(0, window.scrollY + f.getBoundingClientRect().top - 70); });
    if (shots) await page.screenshot({ path: path.join(shots, 'days_phone.png') });
    await page.tap('.spx-dc[data-d]:nth-child(2)');
    await page.waitForSelector('.spx-daydetails .spx-day', { timeout: 5000 });
    check('a tap opens the day on a phone', await page.evaluate(() => !!document.querySelector('.spx-daydetails .spx-day .spx-task')));
    if (shots) await page.screenshot({ path: path.join(shots, 'days_phone_open.png') });
    check('no page errors (phone)', errors.length === 0, errors.slice(0, 3));
    await ctx.close();
  }
  console.log('---\nday cards: ' + pass + ' passed, ' + fail + ' failed');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e && e.stack || e); process.exit(2); });
