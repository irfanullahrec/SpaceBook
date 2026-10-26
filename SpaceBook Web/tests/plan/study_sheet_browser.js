'use strict';
/* "Go" on lesson parts of a Study Plan task, in a real Chrome (phone size, then desktop):   node --max-old-space-size=6144 tests/plan/study_sheet_browser.js [--shots <dir>]
 * Go opens a sheet over the plan with the first lesson part of the task as the book prints it; "Read & next" counts the part as read on the task (done 1 / 4) and shows
 * the next; the last part offers "I've finished - test me", which opens the check of questions (the sheet stays underneath until the task is passed); Back goes back;
 * Escape closes; opening it again starts at the first part not read yet. Tried on a Maths book (MATH_n_DATA) and on an English book (CLSn_BOOKS). Local only
 * (CI has no browser). Dev-only, never shipped. */
const path = require('path');
const { serve, launch } = require('../baseline/lib');
const args = process.argv.slice(2), shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null;
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };

async function plan(page, url, cls, subj, ch, n) {
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && window.SBStudyPlan && window.SBMastery && window.SBStudySheet, null, { timeout: 120000 }); await sleep(2500); break; } catch (e) { /* retry */ }
  }
  await page.evaluate(([cls, subj, ch, n]) => {
    localStorage.removeItem('sb_study_plans_v1');
    const d = new Date(), pad = x => String(x).padStart(2, '0'), ymd = d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
    window.__plan = { id: 'plan_sheet', name: 'Sheet test', classId: cls, scope: [{ subj, ch: [ch] }], cats: ['read'], start: ymd, end: ymd, weekdays: [0, 1, 2, 3, 4, 5, 6],
      slots: [{ from: '00:00', to: '23:59' }], revision: false, createdAt: Date.now(), updatedAt: Date.now(),
      sessions: [{ id: 's_1', date: ymd, slot: 0, from: '00:00', to: '23:59', len: 1439, tasks: [{ id: 'k_read', s: subj, ch, cat: 'read', a: 1, b: n, n, done: 0 }] }] };
    SBStudyPlan.add(window.__plan);
    document.querySelector('.nav-link[data-page="study-plan"]').click();
    setTimeout(() => SBStudyPlan.open('plan_sheet'), 300);
  }, [cls, subj, ch, n]);
  await page.waitForSelector('.spx-dc-today', { timeout: 20000 });
  await page.evaluate(() => document.querySelector('.spx-dc-today').click());
  await page.waitForSelector('.spx-task[data-task="k_read"]', { timeout: 10000 });
}
const done = page => page.evaluate(() => SBStudyPlan.plans().find(p => p.id === 'plan_sheet').sessions[0].tasks[0].done);
const clickGo = page => page.evaluate(() => document.querySelector('.spx-task[data-task="k_read"] [data-act="go"]').click());

async function run(browser, url, label, cls, subj, ch, n, vp, shotName) {
  const ctx = await browser.newContext(vp);
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('dialog', d => d.accept());
  await plan(page, url, cls, subj, ch, n);
  await clickGo(page);
  await page.waitForSelector('#sbss .sbss-body', { timeout: 20000 });
  const first = await page.evaluate(() => ({ prog: document.querySelector('.sbss-prog').textContent.replace(/\s+/g, ' '), len: document.querySelector('.sbss-body').innerText.replace(/\s+/g, ' ').length, btn: document.querySelector('.sbss-foot .main').textContent.trim(), back: !!document.querySelector('[data-a="back"]'), title: document.querySelector('#sbss-t').textContent }));
  check(label + ': Go opens the sheet with part 1 of ' + n + ' (the book\'s own text)', first.prog.indexOf('Part 1 of ' + n) >= 0 && first.len > 150 && /Read & next/.test(first.btn) && !first.back, first);
  if (shots) await page.screenshot({ path: path.join(shots, shotName + '_part1.png') });
  check(label + ': the plan stayed where it was (the sheet is over it)', await page.evaluate(() => !!document.querySelector('.spx-task[data-task="k_read"]') && state.page === 'study-plan'));
  // read and next through the parts
  for (let i = 1; i < n; i++) {
    await page.click('[data-a="next"]');
    const st = await page.evaluate(() => ({ prog: document.querySelector('.sbss-prog small span').textContent, scroll: document.querySelector('.sbss-body').scrollTop }));
    const d = await done(page);
    check(label + ': "Read & next" shows part ' + (i + 1) + ' and counts ' + i + ' read on the task (done ' + d + ' / ' + n + ')', st.prog === 'Part ' + (i + 1) + ' of ' + n && d === i && st.scroll === 0, { st, d });
  }
  const last = await page.evaluate(() => ({ btn: document.querySelector('.sbss-foot .main').textContent.trim(), back: !!document.querySelector('[data-a="back"]') }));
  check(label + ': the last part offers "I\'ve finished — test me" and Back', /finished/.test(last.btn) && last.back, last);
  if (shots) await page.screenshot({ path: path.join(shots, shotName + '_last.png') });
  await page.click('[data-a="back"]');
  check(label + ': Back shows the part before', await page.$eval('.sbss-prog small span', e => e.textContent) === 'Part ' + (n - 1) + ' of ' + n);
  await page.click('[data-a="next"]');
  // the test opens over the sheet, and cancelling it leaves the sheet and the task as they were
  await page.click('[data-a="finish"]');
  await page.waitForSelector('#sbm .sbm-body', { timeout: 20000 });
  check(label + ': "I\'ve finished — test me" opens the check, the sheet stays under it', await page.evaluate(() => !!document.getElementById('sbss') && !!document.getElementById('sbm')));
  await page.evaluate(() => document.querySelector('#sbm [data-a="close"], #sbm .sbm-x').click());
  await page.waitForFunction(() => !document.getElementById('sbm'), null, { timeout: 5000 });
  check(label + ': leaving the check keeps the sheet and the task not done', await page.evaluate(() => !!document.getElementById('sbss')) && (await done(page)) === n - 1);
  // Escape closes; opening again starts at the first part not read yet
  await page.keyboard.press('Escape');
  await page.waitForFunction(() => !document.getElementById('sbss'), null, { timeout: 5000 });
  await clickGo(page);
  await page.waitForSelector('#sbss .sbss-body');
  check(label + ': Escape closes the sheet; Go again starts at the first part not read (part ' + n + ')', await page.$eval('.sbss-prog small span', e => e.textContent) === 'Part ' + n + ' of ' + n);
  check(label + ': no page errors', errors.length === 0, errors.slice(0, 3));
  await ctx.close();
}

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  await run(browser, url, 'Maths 7, phone', 'cls7', 'cls7-math', 1, 4, { viewport: { width: 390, height: 780 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true }, 'math7_phone');
  await run(browser, url, 'Maths 7, desktop', 'cls7', 'cls7-math', 1, 3, { viewport: { width: 1500, height: 880 } }, 'math7_desktop');
  await run(browser, url, 'English 8, phone', 'cls8', 'cls8-eng', 0, 3, { viewport: { width: 390, height: 780 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true }, 'eng8_phone');
  console.log('---\nstudy sheet in the browser: ' + pass + ' passed, ' + fail + ' failed');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e && e.stack || e); process.exit(2); });
