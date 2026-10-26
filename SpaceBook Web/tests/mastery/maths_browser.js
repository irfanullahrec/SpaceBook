'use strict';
/* The Study Plan check on the Mathematics books of Classes 5, 6, 7, 8 and 11, in a real phone-size Chrome:   node --max-old-space-size=6144 tests/mastery/maths_browser.js [--shots <dir>]
 * These books are not CLSn_BOOKS; their questions come from MATH_n_DATA through tools/tests/extract_leaves.js into content/testbank. For each class a plan with a lesson task,
 * a numericals task and an MCQ task of chapter 2 is opened on its page; ticking a task opens the check, the book's right option of every MCQ is marked right, every written
 * question shows the book's answer, and answering everything right ends the check as learnt. Local only (CI has no browser). Dev-only, never shipped. */
const path = require('path');
const { serve, launch } = require('../baseline/lib');
const args = process.argv.slice(2), shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null;
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 1 });
  for (const [cls, subj] of [['cls5', 'cls5-math'], ['cls6', 'cls6-math'], ['cls7', 'cls7-math'], ['cls8', 'cls8-math'], ['cls11', 'cls11-math']]) {
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    page.on('dialog', d => d.accept());
    await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {
      try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && window.SBStudyPlan && window.SBMastery, null, { timeout: 120000 }); await sleep(2500); break; } catch (e) { /* retry */ }
    }
    await page.evaluate(([cls, subj]) => {
      localStorage.removeItem('sb_study_plans_v1');
      const d = new Date(), pad = n => String(n).padStart(2, '0'), ymd = d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
      const t = (id, ch, cat, a, b) => ({ id, s: subj, ch, cat, a, b, n: b - a + 1, done: 0 });
      SBStudyPlan.add({ id: 'plan_m_' + cls, name: 'Maths check', classId: cls, scope: [{ subj, ch: [1] }], cats: ['read', 'mcq', 'num'], start: ymd, end: ymd, weekdays: [0, 1, 2, 3, 4, 5, 6],
        slots: [{ from: '00:00', to: '23:59' }], revision: false, createdAt: Date.now(), updatedAt: Date.now(),
        sessions: [{ id: 's_m1', date: ymd, slot: 0, from: '00:00', to: '23:59', len: 1439, tasks: [t('k_read', 1, 'read', 1, 2), t('k_num', 1, 'num', 1, 5), t('k_mcq', 1, 'mcq', 1, 5)] }] });
      document.querySelector('.nav-link[data-page="study-plan"]').click();
      setTimeout(() => SBStudyPlan.open('plan_m_' + cls), 300);
    }, [cls, subj]);
    await page.waitForSelector('.spx-dc-today', { timeout: 20000 });                              // the days of the plan are cards; today's holds the tasks
    await page.evaluate(() => document.querySelector('.spx-dc-today').click());                   // the reminder banner may sit over it
    await page.waitForSelector('.spx-task', { timeout: 20000 });
    for (const id of ['k_read', 'k_num', 'k_mcq']) {
      await page.click('.spx-task[data-task="' + id + '"] input[data-act="tick"]');
      await page.waitForSelector('#sbm .sbm-body [data-a="start"]', { timeout: 30000 });
      const intro = await page.evaluate(() => ({ n: SBMastery.state.picked.items.length, scope: SBMastery.state.picked.scope, kinds: SBMastery.state.picked.items.map(i => i.y).join(',') }));
      check(cls + ' ' + id + ': the check asks questions of the book (' + intro.n + ', ' + intro.scope + ')', intro.n >= 2, intro);
      await page.click('[data-a="start"]');
      const total = await page.evaluate(() => SBMastery.state.run.total);
      let shotMcq = false, shotWritten = false;
      for (let i = 0; i < total; i++) {
        const kind = await page.evaluate(() => { const it = SBMastery.state.run.current(); return { y: it.y, a: it.a, n: it.o ? it.o.length : 2, q: it.q.slice(0, 60) }; });
        if (kind.y === 'mcq' || kind.y === 'tf') {
          if (shots && !shotMcq) { await page.screenshot({ path: path.join(shots, cls + '_mcq.png') }); shotMcq = true; }
          await page.click('.sbm-opt[data-v="' + kind.a + '"]');
          check(cls + ' ' + id + ': the book\'s right option is marked right (' + kind.q + ')', await page.$eval('.sbm-fb', e => e.classList.contains('ok')), kind);
          await page.click('[data-a="next"]');
        } else {
          await page.click('[data-a="reveal"]');
          if (shots && !shotWritten) { await page.screenshot({ path: path.join(shots, cls + '_written.png') }); shotWritten = true; }
          check(cls + ' ' + id + ': a written question shows the book\'s answer (' + kind.q + ')', await page.$eval('.sbm-ans', e => e.textContent.replace(/\s+/g, '').length > 12), kind);
          await page.click('[data-a="self-right"]');
        }
      }
      await page.waitForSelector('#sbm .sbm-body .sbm-stats', { timeout: 10000 });
      check(cls + ' ' + id + ': every question right ends the check as learnt', await page.$eval('.sbm-body', e => /You have learnt it/.test(e.textContent)));
      await page.click('#sbm [data-a="close"]');
      await page.waitForFunction(() => !document.getElementById('sbm'));
    }
    await page.close();
  }
  check('no page errors', errors.length === 0, errors.slice(0, 3));
  console.log('---\nmaths check in the browser: ' + pass + ' passed, ' + fail + ' failed');
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e && e.stack || e); process.exit(2); });
