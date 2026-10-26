'use strict';
/* The timed level games (Math Sprint, True or False) in a real Chrome: the learner is not punished for reading slowly.
 *   - the intro explains the controls and offers the clock: Take my time (no clock) / Relaxed (twice as long, the default) / Normal;
 *   - a Pause button (and the P key) stops the clock for real: the bar does not move, the time left is the same after a long pause, nothing can be answered
 *     while paused, Resume carries on from where the clock stopped; a hidden page pauses by itself;
 *   - with no clock there is no bar and no pause button and a question never times out;
 *   - a question that runs out of a Relaxed clock does not cost a life (only the Normal clock does);
 *   - the choice is kept.
 *     node --max-old-space-size=3072 tests/launch/games_pause.js
 * Uses tests/games/harness.html (the Games page without the rest of the app). Dev-only, never shipped. */
const path = require('path');
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const page = await (await browser.newContext({ viewport: { width: 1000, height: 860 } })).newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(url + 'tests/games/harness.html', { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.waitForSelector('.gm-root', { timeout: 90000 });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForSelector('.gm-root');
  await sleep(500);
  await page.click('.gm-pill[data-cls="7"]'); await sleep(400);
  await page.waitForSelector('.gm-play[data-game="math"]', { timeout: 40000 });
  await page.click('.gm-play[data-game="math"]');
  await page.waitForSelector('.gm-node[data-level="1"]');
  await page.click('.gm-node[data-level="1"]');
  await page.waitForSelector('.gm-intro');

  // ---- the intro
  const intro = await page.locator('.gm-intro').innerText();
  check('the intro says how to answer (tap, 1-4, A-D) and that the clock can be paused or switched off', /press\s*1.*4|1\s*–\s*4/.test(intro) && /pause/i.test(intro) && /switch it off|no clock/i.test(intro), intro.slice(0, 300));
  check('the clock choice is there, and Relaxed is the default', (await page.locator('input[name="gm-timing"]').count()) === 3 && (await page.locator('input[name="gm-timing"]:checked').getAttribute('value')) === 'relaxed');
  check('each choice is at least 44 px high', await page.evaluate(() => [...document.querySelectorAll('.gm-timing label')].every(l => l.getBoundingClientRect().height >= 43)));

  // ---- the clock runs, and is twice the old length
  await page.click('[data-go]');
  await page.waitForSelector('.gm-clock i');
  const secs = await page.evaluate(() => SBGames.state.run.built.secs);
  const clockOf = () => page.evaluate(() => SBGames.state.run.q.clock.left);
  const c1 = await clockOf(); await sleep(1200); const c2 = await clockOf();
  check('Relaxed: the clock starts at twice the level\'s seconds and runs', c1 > secs * 1000 * 1.8 && c1 <= secs * 2000 && c2 < c1 - 900, { secs, c1, c2 });

  // ---- pause stops it
  const pauseBtn = page.locator('[data-pause]');
  check('a Pause button is in the game bar, named for screen readers', (await pauseBtn.count()) === 1 && /Pause/.test(await pauseBtn.getAttribute('aria-label')) && (await pauseBtn.getAttribute('aria-pressed')) === 'false');
  await pauseBtn.click();
  const p1 = await clockOf();
  const w1 = await page.evaluate(() => document.querySelector('.gm-clock i').style.width);
  await sleep(3500);
  const p2 = await clockOf();
  const w2 = await page.evaluate(() => document.querySelector('.gm-clock i').style.width);
  check('paused: the clock does not move for 3.5 seconds (the bar and the time left are the same)', p1 === p2 && w1 === w2, { p1, p2, w1, w2 });
  check('paused: the button says Resume, a "Paused" layer covers the question', (await pauseBtn.getAttribute('aria-pressed')) === 'true' && (await page.locator('.gm-paused').isVisible()) && /Paused/.test(await page.locator('.gm-paused').innerText()));
  const before = await page.evaluate(() => ({ idx: SBGames.state.run.idx, locked: SBGames.state.run.q.locked }));
  await page.keyboard.press('1'); await page.keyboard.press('a');
  const after = await page.evaluate(() => ({ idx: SBGames.state.run.idx, locked: SBGames.state.run.q.locked }));
  check('paused: answering by keyboard does nothing', before.locked === false && after.locked === false && after.idx === before.idx, { before, after });
  await page.locator('[data-resume]').click();
  await sleep(1200);
  const r2 = await clockOf();
  check('Resume carries on from where it stopped (not from the full time, not from zero)', r2 < p2 && r2 > p2 - 1800, { p2, r2 });
  check('the Paused layer is gone and the answers can be clicked again', !(await page.locator('.gm-paused').count()) && (await page.locator('.gm-opt:not([disabled])').count()) >= 2);

  // ---- the P key, and a hidden page
  await page.keyboard.press('p');
  check('the P key pauses', await page.evaluate(() => SBGames.state.run.paused === true));
  await page.keyboard.press('p');
  check('and resumes', await page.evaluate(() => SBGames.state.run.paused === false));
  await page.evaluate(() => { Object.defineProperty(document, 'hidden', { configurable: true, get: () => true }); document.dispatchEvent(new Event('visibilitychange')); });
  check('a hidden page (a phone call, another tab) pauses by itself', await page.evaluate(() => SBGames.state.run.paused === true));
  await page.evaluate(() => { Object.defineProperty(document, 'hidden', { configurable: true, get: () => false }); });
  await page.locator('[data-resume]').click();

  // ---- running out of a Relaxed clock costs no life
  await page.evaluate(() => { const r = SBGames.state.run; r.q.clock.left = 150; });
  await page.waitForFunction(() => SBGames.state.run.q.locked, null, { timeout: 5000 });
  const lost = await page.evaluate(() => ({ lives: SBGames.state.run.lives, fb: document.querySelector('.gm-fb').innerText }));
  check('time up on a Relaxed clock: the right answer is shown and no life is lost', lost.lives === 3 && /Time is up/.test(lost.fb), lost);

  // ---- no clock
  await page.click('[data-leave]').catch(() => {});
  await sleep(300);
  if (await page.locator('[data-quit]').count()) await page.locator('[data-quit]').click();
  await page.waitForSelector('.gm-node[data-level="1"]');
  await page.click('.gm-node[data-level="1"]');
  await page.waitForSelector('.gm-intro');
  await page.locator('input[name="gm-timing"][value="off"]').check();
  await page.click('[data-go]');
  await page.waitForSelector('.gm-opt');
  check('no clock: no bar and no Pause button', (await page.locator('.gm-clock').count()) === 0 && (await page.locator('[data-pause]').count()) === 0);
  await sleep(2500);
  check('no clock: a question never times out', await page.evaluate(() => !SBGames.state.run.q.locked));
  check('the choice was saved', await page.evaluate(() => Object.keys(localStorage).some(k => /sb_games_v1/.test(k) && JSON.parse(localStorage.getItem(k)).timing === 'off')));

  // ---- Normal costs a life (as before)
  await page.click('[data-leave]').catch(() => {}); await sleep(300);
  if (await page.locator('[data-quit]').count()) await page.locator('[data-quit]').click();
  await page.waitForSelector('.gm-node[data-level="1"]');
  await page.click('.gm-node[data-level="1"]'); await page.waitForSelector('.gm-intro');
  await page.locator('input[name="gm-timing"][value="normal"]').check();
  await page.click('[data-go]'); await page.waitForSelector('.gm-clock i');
  const n1 = await page.evaluate(() => SBGames.state.run.q.clock.left), secsN = await page.evaluate(() => SBGames.state.run.built.secs);
  check('Normal: the clock is the level\'s own length', n1 <= secsN * 1000 && n1 > secsN * 1000 - 1500, { n1, secsN });
  await page.evaluate(() => { SBGames.state.run.q.clock.left = 150; });
  await page.waitForFunction(() => SBGames.state.run.q.locked, null, { timeout: 5000 });
  check('Normal: time up costs a life', await page.evaluate(() => SBGames.state.run.lives === 2));
  check('no script error', errors.length === 0, errors);
  await browser.close(); server.close();
  console.log('---\ngames pause test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
