'use strict';
/* "Learn it, then prove it" in a real browser:   node --max-old-space-size=6144 tests/mastery/browser.js
 * A plan with real tasks (Class 9 Chemistry, and a subject with no questions in the books) opened on its page. Ticking a task opens a check of the
 * book's own questions; one is answered wrongly on purpose, and only that one comes back, round after round, until it is right. Then the task is done
 * and the record (rounds, mistakes put right) is on the task, in the plan's storage, on the row and in the learning record. Also: written questions are
 * marked by the student against the book's answer; a task with no question in the books is marked by the student and says so; closing a check marks
 * nothing; un-ticking removes the record; "Go" then "I've finished - test me"; the sheet fits a phone. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  page.on('dialog', d => d.accept());
  await page.goto(url + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  for (let k = 0; k < 4; k++) {
    try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && window.SBStudyPlan && window.SBMastery, null, { timeout: 120000 }); await sleep(2500); if (await page.evaluate(() => typeof window.SBMastery === 'object')) break; } catch (e) { /* reloaded: wait again */ }
  }
  check('the page has the check module and the Study Plan', await page.evaluate(() => !!(window.SBMastery && window.SBMastery.checkTask && window.SBStudyPlan)));

  // a plan with one session today and five tasks
  await page.evaluate(() => {
    localStorage.removeItem('sb_study_plans_v1');
    const d = new Date(), pad = n => String(n).padStart(2, '0'), ymd = d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
    const t = (id, s, ch, cat, a, b) => ({ id, s, ch, cat, a, b, n: b - a + 1, done: 0 });
    window.__plan = { id: 'plan_mast1', name: 'Mastery test plan', classId: 'cls9', scope: [{ subj: 'cls9-chem', ch: [0] }], cats: ['read', 'mcq', 'sq'], start: ymd, end: ymd, weekdays: [0, 1, 2, 3, 4, 5, 6], skip: [], extra: [], alt: false,
      slots: [{ from: '00:00', to: '23:59' }], revision: false, createdAt: Date.now(), updatedAt: Date.now(),
      sessions: [{ id: 's_m1', date: ymd, slot: 0, from: '00:00', to: '23:59', len: 1439, tasks: [
        t('k_read', 'cls9-chem', 0, 'read', 1, 2), t('k_mcq', 'cls9-chem', 0, 'mcq', 1, 6), t('k_sq', 'cls9-chem', 0, 'sq', 1, 2),
        t('k_none', 'cls9-islopt', 0, 'read', 1, 1), t('k_x', 'cls9-chem', 0, 'read', 3, 4)] }] };
    SBStudyPlan.add(window.__plan);
    document.querySelector('.nav-link[data-page="study-plan"]').click();
    setTimeout(() => SBStudyPlan.open('plan_mast1'), 300);
  });
  await page.waitForSelector('.spx-dc-today', { timeout: 20000 });                                // the days of the plan are cards; today's holds the tasks
  await page.click('.spx-dc-today');
  await page.waitForSelector('.spx-task', { timeout: 20000 });
  const row = id => '.spx-task[data-task="' + id + '"]';
  const taskState = id => page.evaluate(i => { const p = SBStudyPlan.plans().find(x => x.id === 'plan_mast1'); const k = p.sessions[0].tasks.find(x => x.id === i); return { done: k.done, n: k.n, learn: k.learn || null }; }, id);
  check('every task has a "Test me" button and a Go button', await page.$$eval('.spx-task', els => els.length >= 5 && els.every(e => e.querySelector('[data-act="check"]') && e.querySelector('[data-act="go"]'))));

  // answer the question on screen: right or wrong. MCQ / true-false by clicking an option, written ones by "show the answer" and the self-mark.
  const answer = async right => {
    const kind = await page.evaluate(() => { const it = SBMastery.state.run.current(); return { y: it.y, a: it.a, n: it.o ? it.o.length : 2, id: it.id }; });
    if (kind.y === 'mcq' || kind.y === 'tf') {
      await page.click('.sbm-opt[data-v="' + (right ? kind.a : (kind.a + 1) % kind.n) + '"]');
      const okShown = await page.$eval('.sbm-fb', e => e.classList.contains('ok'));
      if (okShown !== right) check('the feedback matches the answer given', false, kind);
      await page.click('[data-a="next"]');
    } else {
      await page.click('[data-a="reveal"]');
      await page.click(right ? '[data-a="self-right"]' : '[data-a="self-wrong"]');
    }
    return kind.id;
  };

  // ---- 1. a lesson task: tick it, miss one question on purpose, only that one comes back
  await page.click(row('k_read') + ' input[data-act="tick"]');
  await page.waitForSelector('#sbm .sbm-body [data-a="start"]', { timeout: 30000 });
  check('ticking opens the check, and the task is not done yet', (await taskState('k_read')).done === 0 && await page.evaluate(() => !!document.getElementById('sbm')));
  const intro = await page.evaluate(() => ({ title: document.querySelector('#sbm-t').textContent, text: document.querySelector('.sbm-body').textContent, n: SBMastery.state.picked.items.length, scope: SBMastery.state.picked.scope }));
  check('the intro says how many questions, from the book, about this subject', intro.n >= 3 && new RegExp(intro.n + ' question').test(intro.text) && /Chemistry/.test(intro.title), intro);
  await page.click('[data-a="start"]');
  let total = await page.evaluate(() => SBMastery.state.run.total);
  const askedIds = []; let missed = null;
  for (let i = 0; i < total; i++) { const right = i !== 0; const id = await answer(right); askedIds.push(id); if (!right) missed = id; }
  await page.waitForSelector('#sbm .sbm-body [data-a="retry"]', { timeout: 10000 });
  const re = await page.evaluate(() => ({ phase: SBMastery.state.run.phase, mistakes: SBMastery.state.run.mistakes().map(x => x.id), text: document.querySelector('.sbm-body').textContent }));
  check('round 1 asked every question once', new Set(askedIds).size === total && total >= 3, askedIds);
  check('the round end says how many were right and lists exactly the missed one', re.phase === 'roundEnd' && re.mistakes.length === 1 && re.mistakes[0] === missed && new RegExp((total - 1) + ' of ' + total + ' right').test(re.text), re);
  check('still not done: the proof is not there yet', (await taskState('k_read')).done === 0);
  await page.click('[data-a="retry"]');
  const r2 = await page.evaluate(() => ({ round: SBMastery.state.run.round, total: SBMastery.state.run.total, id: SBMastery.state.run.current().id, prog: document.querySelector('.sbm-prog').textContent }));
  check('round 2 asks only the missed question', r2.round === 2 && r2.total === 1 && r2.id === missed && /Round 2/.test(r2.prog) && /only what you missed/.test(r2.prog), r2);
  await answer(false);                                           // wrong again
  await page.waitForSelector('#sbm .sbm-body [data-a="retry"]', { timeout: 10000 });
  await page.click('[data-a="retry"]');
  const r3 = await page.evaluate(() => ({ round: SBMastery.state.run.round, total: SBMastery.state.run.total, id: SBMastery.state.run.current().id }));
  check('round 3: the same single question again', r3.round === 3 && r3.total === 1 && r3.id === missed, r3);
  await answer(true);
  await page.waitForSelector('#sbm .sbm-body .sbm-stats', { timeout: 10000 });
  const win = await page.$eval('.sbm-body', e => e.textContent);
  check('the end says it is learnt, with the numbers', /You have learnt it/.test(win) && /after 3 rounds/.test(win) && new RegExp(total + 'questions').test(win.replace(/\s+/g, '')), win);
  const k1 = await taskState('k_read');
  check('the task is done and carries the record: 3 rounds, every question, 1 put right, the missed one named',
    k1.done === k1.n && k1.learn && k1.learn.mode === 'check' && k1.learn.rounds === 3 && k1.learn.asked === total && k1.learn.first === total - 1 && k1.learn.fixed === 1 && k1.learn.wrong === 2 && k1.learn.missed.length === 1 && k1.learn.missed[0] === missed, k1);
  const saved = await page.evaluate(() => { const p = JSON.parse(localStorage.getItem('sb_study_plans_v1')).find(x => x.id === 'plan_mast1'); return p.sessions[0].tasks.find(x => x.id === 'k_read').learn; });
  check('and it is saved in the plan\'s storage', saved && saved.mode === 'check' && saved.rounds === 3, saved);
  await page.click('#sbm [data-a="close"]');
  await page.waitForFunction(() => !document.getElementById('sbm'));
  check('closing the finished check leaves the task done', (await taskState('k_read')).done === k1.n);
  check('the row shows it: ticked, with the "learnt · 3 rounds" badge', await page.$eval(row('k_read'), e => e.classList.contains('spx-done') && e.querySelector('input[data-act="tick"]').checked && /learnt · 3 rounds/.test(e.querySelector('.spx-learnt').textContent)));
  check('the plan counts it: "Learnt and checked 1/5 tasks"', await page.$eval('.spx-chips-lg', e => /Learnt and checked\s*1\/5/.test(e.textContent)));
  await page.click('.spx-record summary');
  check('the learning record lists it with its numbers', await page.$eval('.spx-record', e => /Learning record \(1\)/.test(e.textContent) && /3 rounds/.test(e.textContent) && /1 mistake put right/.test(e.textContent)));
  check('a done task has no "Test me" button any more', await page.$eval(row('k_read'), e => !e.querySelector('[data-act="check"]')));

  // ---- 2. an MCQ task, all right in round 1
  await page.click(row('k_mcq') + ' [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  await page.click('[data-a="start"]');
  total = await page.evaluate(() => SBMastery.state.run.total);
  for (let i = 0; i < total; i++) await answer(true);
  await page.waitForSelector('#sbm .sbm-stats');
  const k2 = await taskState('k_mcq');
  check('all right first time: passed in one round, nothing to put right', k2.done === k2.n && k2.learn.rounds === 1 && k2.learn.fixed === 0 && k2.learn.first === total && /at the first try/.test(await page.$eval('.sbm-body', e => e.textContent)), k2);
  await page.click('#sbm [data-a="close"]');

  // ---- 3. written questions: the book's answer is shown, the student marks themselves
  await page.click(row('k_sq') + ' [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  const sqIntro = await page.evaluate(() => ({ kinds: [...new Set(SBMastery.state.picked.items.map(i => i.y))], text: document.querySelector('.sbm-body').textContent }));
  check('short questions are written: the intro says you compare with the book\'s answer', sqIntro.kinds.every(k => k === 'short') && /written/.test(sqIntro.text), sqIntro);
  await page.click('[data-a="start"]');
  check('the answer is hidden until asked for', await page.evaluate(() => !!document.querySelector('.sbm-ta') && !document.querySelector('.sbm-ans')));
  await page.click('[data-a="reveal"]');
  check('then the book\'s answer appears with "did you have it right?"', await page.evaluate(() => /The book's answer/.test(document.querySelector('.sbm-ans').textContent) && /had it right/.test(document.querySelector('.sbm-body').textContent)));
  await page.click('[data-a="self-wrong"]');
  const sqTotal = await page.evaluate(() => SBMastery.state.run.total);
  for (let i = 1; i < sqTotal; i++) await answer(true);
  await page.waitForSelector('#sbm [data-a="retry"]');
  check('"Not yet" brings that written question back in the next round', await page.evaluate(() => SBMastery.state.run.mistakes().length === 1));
  await page.click('[data-a="retry"]');
  await answer(true);
  await page.waitForSelector('#sbm .sbm-stats');
  const k3 = await taskState('k_sq');
  check('the record says 2 rounds and that all its questions were self-marked', k3.done === k3.n && k3.learn.mode === 'check' && k3.learn.rounds === 2 && k3.learn.self === sqTotal && k3.learn.auto === 0, k3);
  await page.click('#sbm [data-a="close"]');

  // ---- 4. no question in the books: the student marks it, and it says so
  await page.click(row('k_none') + ' [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="self"]');
  check('a task with no question in the books says so', await page.evaluate(() => /No test questions for this part yet/.test(document.querySelector('.sbm-body').textContent)));
  await page.click('#sbm [data-a="self"]');
  await page.waitForFunction(() => !document.getElementById('sbm'));
  const k4 = await taskState('k_none');
  check('the student\'s own word marks it, recorded as "self"', k4.done === k4.n && k4.learn && k4.learn.mode === 'self', k4);
  check('its row says "marked by you", not "learnt"', await page.$eval(row('k_none'), e => /marked by you/.test(e.querySelector('.spx-learnt').textContent)));
  check('the count of checked tasks stays 3 of 5: the self-marked one is not counted as checked', await page.$eval('.spx-chips-lg', e => /Learnt and checked\s*3\/5/.test(e.textContent)));

  // ---- 5. closing a check marks nothing; un-ticking removes the proof
  await page.click(row('k_x') + ' input[data-act="tick"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  await page.keyboard.press('Escape');
  await page.waitForFunction(() => !document.getElementById('sbm'));
  check('leaving a check (Escape) marks nothing', (await taskState('k_x')).done === 0 && await page.$eval(row('k_x') + ' input[data-act="tick"]', e => !e.checked));
  await page.click(row('k_read') + ' input[data-act="tick"]');       // un-tick a learnt task
  const k5 = await taskState('k_read');
  check('un-ticking a learnt task clears it and its record', k5.done === 0 && k5.learn === null, k5);

  // ---- 6. keyboard: the number of an option picks it, Enter goes on
  await page.click(row('k_mcq') + ' input[data-act="tick"]');          // the MCQ task was done in step 2: un-tick it to check it again
  check('un-ticking the MCQ task cleared it too', (await taskState('k_mcq')).learn === null);
  await page.click(row('k_mcq') + ' [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  await page.click('[data-a="start"]');
  const want = await page.evaluate(() => SBMastery.state.run.current().a);
  await page.keyboard.press(String(want + 1));
  check('pressing the number of the right option answers it', await page.$eval('.sbm-opt.right', e => e.disabled === true) && await page.$eval('.sbm-fb', e => e.classList.contains('ok')));
  await page.keyboard.press('Enter');
  check('Enter goes to the next question', await page.evaluate(() => SBMastery.state.run.position === 1 || SBMastery.state.run.phase !== 'ask'));
  await page.keyboard.press('Escape');
  await page.waitForFunction(() => !document.getElementById('sbm'));

  // ---- 7. the study bar: Go, then "I've finished - test me"
  await page.evaluate(() => { const p = SBStudyPlan.plans().find(x => x.id === 'plan_mast1'); SBStudyPlan.go(p, p.sessions[0].tasks.find(x => x.id === 'k_x')); });
  await page.waitForSelector('#spx-studybar [data-act="check"]', { timeout: 20000 });
  check('after Go the study bar offers "I\'ve finished — test me" (no bare "Done" any more)', await page.$eval('#spx-studybar', e => /test me/.test(e.textContent) && !e.querySelector('[data-act="done"]')));
  await page.click('#spx-studybar [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  check('it opens the check of that task', await page.evaluate(() => /Chemistry/.test(document.querySelector('#sbm-t').textContent)));
  await page.keyboard.press('Escape');
  await page.waitForFunction(() => !document.getElementById('sbm'));

  // ---- 8. on a phone
  await page.setViewportSize({ width: 390, height: 780 });
  await page.evaluate(() => { SBStudyPlan.open('plan_mast1'); });
  await page.waitForSelector(row('k_mcq'));
  await page.click(row('k_mcq') + ' [data-act="check"]');
  await page.waitForSelector('#sbm [data-a="start"]');
  await page.click('[data-a="start"]');
  const fit = await page.evaluate(() => { const c = document.querySelector('.sbm-card').getBoundingClientRect(), o = [...document.querySelectorAll('.sbm-opt')].map(b => b.getBoundingClientRect()); return { card: Math.round(c.width), left: Math.round(c.left), right: Math.round(c.right), minTap: Math.round(Math.min(...o.map(r => r.height))), over: document.querySelector('.sbm-body').scrollWidth > document.querySelector('.sbm-body').clientWidth }; });
  check('on a 390 px phone the sheet fits, options are big enough to tap, nothing scrolls sideways', fit.card <= 390 && fit.left >= 0 && fit.right <= 390 && fit.minTap >= 44 && !fit.over, fit);
  await page.keyboard.press('Escape');
  await page.waitForFunction(() => !document.getElementById('sbm'));

  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('---\nmastery browser: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
