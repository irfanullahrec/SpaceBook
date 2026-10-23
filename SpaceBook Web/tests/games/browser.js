'use strict';
/* Games in a real browser (the installed Chrome through Playwright, like tests/baseline):
 *     node --max-old-space-size=8192 tests/games/browser.js [--out <folder for screenshots>]
 * Opens the Games page (a light test page; `--full` = the whole app on #games) and plays real levels of every kind of game (the right answer is read from the game's own state).
 * Checks: the page draws, levels unlock in order, steps become coins through SBRewards (guest mode, localStorage), lives end a
 * run, a hint costs the coin, progress survives a reload, no sideways scrolling on a phone, nothing throws in the console.
 * Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const args = process.argv.slice(2);
const FULL = args.includes('--full');   // the whole app (needs ~1 GB of free memory); default: tests/games/harness.html
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_games_shots'));
fs.mkdirSync(OUT, { recursive: true });

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) pass++; else { fail++; console.log('FAIL ' + name + (detail !== undefined ? ' :: ' + String(detail).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 860 } });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::/.test(m.text())) errors.push('console: ' + m.text()); });
  const shot = async name => { try { await page.screenshot({ path: path.join(OUT, name + '.png') }); } catch (e) { /* page busy */ } };
  const coins = () => page.evaluate(() => window.SBRewards.coins);
  const toHub = async () => { if (await page.$('.gm-back')) { await page.click('.gm-back'); } await page.waitForSelector('.gm-card'); };
  const openLevel = async level => { await page.click('.gm-node[data-level="' + level + '"]'); await page.waitForSelector('.gm-intro'); await page.click('[data-go]'); };
  const pickClass = async n => { await page.click('.gm-pill[data-cls="' + n + '"]'); await sleep(250); };
  const openGame = async g => { await page.waitForSelector('.gm-play[data-game="' + g + '"]', { timeout: 30000 }); await page.click('.gm-play[data-game="' + g + '"]'); await page.waitForSelector('.gm-path'); };

  // play a "choice" level; pick(a, n) says which option to click given the right index and the option count
  async function playChoice(pick) {
    for (let guard = 0; guard < 60; guard++) {
      if (await page.$('.gm-res')) return;
      const st = await page.evaluate(() => { const r = window.SBGames.state.run; return r && r.q && r.q.it ? { a: r.q.it.a, n: r.q.it.c.length, locked: r.q.locked } : null; });
      if (st && !st.locked) await page.click('.gm-opt[data-i="' + pick(st.a, st.n) + '"]').catch(() => null);
      await sleep(150);
      const nb = await page.$('[data-next]');
      if (nb) await nb.click().catch(() => null);
      await sleep(850);
    }
  }
  const right = a => a, wrong = (a, n) => (a + 1) % n;

  await page.goto(url + (FULL ? 'index.html#games' : 'tests/games/harness.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  await page.waitForSelector('.gm-root', { timeout: 90000 });
  await sleep(500);
  if (FULL) check('Games tab is in the header and active', await page.evaluate(() => { const t = document.querySelector('.nav-tab[data-page="games"]'); return !!t && t.classList.contains('active'); }));
  check('hub shows six game cards', (await page.$$('.gm-card')).length === 6);
  await shot('01-hub-desktop');

  // ----- class 9, Quiz Quest -----
  await pickClass(9);
  await page.waitForFunction(() => document.querySelectorAll('.gm-play').length >= 4, null, { timeout: 40000 });
  await shot('02-hub-class9');
  const c0 = await coins();
  await openGame('quiz');
  check('level map has 10 levels, only level 1 open', await page.evaluate(() => { const n = [...document.querySelectorAll('.gm-node')]; return n.length === 10 && !n[0].disabled && n.slice(1).every(x => x.disabled); }));
  await shot('03-map');
  await page.click('.gm-node[data-level="1"]'); await page.waitForSelector('.gm-intro'); await shot('04-intro');
  await page.click('[data-go]'); await page.waitForSelector('.gm-opt'); await shot('05-question');
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 20000 });
  await shot('06-results');
  check('a perfect level is cleared with 3 stars', (await page.textContent('.gm-res-stars')).includes('★★★'), await page.textContent('.gm-res'));
  check('level 1 paid 5 steps + 5 bonus = 10 coins', (await coins()) - c0 === 10, (await coins()) - c0);
  check('the run chip shows +10', /\+10/.test(await page.textContent('.gm-run')), await page.textContent('.gm-run'));
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');
  check('level 2 is open after clearing level 1', await page.evaluate(() => !document.querySelector('.gm-node[data-level="2"]').disabled));
  check('level 1 shows as complete', await page.evaluate(() => document.querySelector('.gm-node[data-level="1"]').classList.contains('is-complete')));
  await shot('07-map-after');

  // the same level again on the same day: nothing more to earn
  await openLevel(1); await page.waitForSelector('.gm-opt');
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 20000 });
  check('playing a finished level again the same day pays nothing more', (await coins()) - c0 === 10, (await coins()) - c0);
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');

  // level 2, every answer wrong: three lives end the run, level 3 stays locked
  await openLevel(2); await page.waitForSelector('.gm-opt');
  const c2 = await coins();
  await playChoice(wrong);
  await page.waitForSelector('.gm-res', { timeout: 20000 });
  const failText = await page.textContent('.gm-res');
  check('three wrong answers end the run: not cleared', /try again|Out of lives|So close/i.test(failText), failText);
  check('a failed run pays no coins', (await coins()) === c2);
  check('no star after a failed run', (await page.textContent('.gm-res-stars')).startsWith('☆☆☆'));
  check('the results list the questions that were missed, with answers', (await page.$$('.gm-review .gm-rv')).length >= 3 && (await page.$$('.gm-rv-a')).length >= 1);
  await shot('08-failed');
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');
  check('level 3 stays locked after a failed level 2', await page.evaluate(() => document.querySelector('.gm-node[data-level="3"]').disabled));

  // ----- Math Sprint, class 5 -----
  await toHub(); await pickClass(5); await openGame('math');
  await openLevel(1); await page.waitForSelector('.gm-opt');
  check('math sprint has a clock', !!(await page.$('.gm-clock')));
  await shot('09-math');
  const m0 = await coins();
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 30000 });
  check('math level paid 6 steps + 5 = 11 coins', (await coins()) - m0 === 11, (await coins()) - m0);
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');

  // ----- Word Builder with pictures, class 2: first word with a hint (no coin), the rest clean -----
  await toHub(); await pickClass(2); await openGame('spell');
  await openLevel(1); await page.waitForSelector('.gm-tile');
  await shot('10-spell');
  const s0 = await coins();
  for (let g = 0; g < 8; g++) {
    if (await page.$('.gm-res')) break;
    const ans = await page.evaluate(() => window.SBGames.state.run.q.it.ans);
    if (g === 0) await page.click('[data-hint]');
    await page.keyboard.type(ans, { delay: 25 });
    const nb = await page.waitForSelector('[data-next]', { timeout: 5000 }).catch(() => null);
    if (nb) await nb.click();
    await sleep(350);
  }
  await page.waitForSelector('.gm-res', { timeout: 15000 });
  check('word builder: 3 clean words = 3 coins, the hinted word 0, no bonus', (await coins()) - s0 === 3, (await coins()) - s0);
  await shot('11-spell-results');
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');

  // ----- Memory Match, class 8 -----
  await toHub(); await pickClass(8); await openGame('memory');
  await page.click('.gm-node[data-level="1"]'); await page.waitForSelector('.gm-intro'); await page.click('[data-go]');
  await page.waitForSelector('[data-hide]'); await shot('12-memory-peek');
  await page.click('[data-hide]'); await sleep(200);
  const mem0 = await coins();
  const deck = await page.evaluate(() => window.SBGames.state.run.q.deck.map(c => c.pair));
  const done = new Set();
  for (let i = 0; i < deck.length; i++) {
    if (done.has(i)) continue;
    const j = deck.findIndex((p, k) => k !== i && p === deck[i] && !done.has(k));
    done.add(i); done.add(j);
    await page.click('.gm-card2[data-c="' + i + '"]'); await page.click('.gm-card2[data-c="' + j + '"]'); await sleep(250);
  }
  await page.waitForSelector('.gm-res', { timeout: 15000 });
  await shot('13-memory-done');
  check('memory match: 3 pairs + 5 bonus = 8 coins', (await coins()) - mem0 === 8, (await coins()) - mem0);
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');

  // ----- Little Learners (class 1) and True or False (class 4) -----
  await toHub(); await pickClass(1); await openGame('learn');
  await openLevel(1); await page.waitForSelector('.gm-opt'); await shot('14-learner');
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 30000 });
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');
  await toHub(); await pickClass(4); await openGame('tf');
  await openLevel(1); await page.waitForSelector('.gm-opt'); await shot('15-truefalse');
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 30000 });
  await page.click('[data-map]'); await page.waitForSelector('.gm-path');

  // progress survives a reload (guest data in localStorage)
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForSelector('.gm-root', { timeout: 90000 });
  await pickClass(9);
  await page.waitForFunction(() => [...document.querySelectorAll('.gm-card')].some(c => /Quiz Quest/.test(c.textContent) && /levels/.test(c.textContent)), null, { timeout: 40000 });
  const quiz = await page.evaluate(() => [...document.querySelectorAll('.gm-card')].find(x => /Quiz Quest/.test(x.textContent)).textContent);
  check('after a reload the hub still shows the cleared level', /1 \/ \d+ levels/.test(quiz), quiz);
  await shot('16-hub-after-reload');

  // a finished level played again on a LATER day pays +2 (back-date the saved progress by reloading with older dates)
  await page.evaluate(() => { const g = JSON.parse(localStorage.getItem('sb_rewards_guest_v1')); Object.values(g.activities).forEach(a => { a.last = '2026-01-01 10:00:00'; }); localStorage.setItem('sb_rewards_guest_v1', JSON.stringify(g)); });
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForSelector('.gm-root', { timeout: 90000 });
  await pickClass(9); await openGame('quiz');
  const p0 = await coins();
  await openLevel(1); await page.waitForSelector('.gm-opt');
  await playChoice(right);
  await page.waitForSelector('.gm-res', { timeout: 20000 });
  check('replaying a finished level on a later day pays +2', (await coins()) - p0 === 2, (await coins()) - p0);
  check('and the results say so', /practice/.test(await page.textContent('.gm-res-coins')), await page.textContent('.gm-res-coins'));
  await page.click('[data-map]'); await page.waitForSelector('.gm-path'); await toHub();

  // ----- phone width -----
  await page.setViewportSize({ width: 375, height: 812 }); await sleep(300);
  await shot('17-hub-phone');
  check('no sideways scrolling on a phone', !(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 2)));
  await openGame('quiz'); await shot('18-map-phone');
  await page.click('.gm-node[data-level="2"]'); await page.waitForSelector('.gm-intro'); await page.click('[data-go]'); await page.waitForSelector('.gm-opt'); await shot('19-question-phone');
  check('no sideways scrolling in a game on a phone', !(await page.evaluate(() => { const o = document.querySelector('.gm-ov'); return o.scrollWidth > o.clientWidth + 2; })));
  await page.keyboard.press('Escape'); await sleep(200);
  check('leaving a started level asks first', !!(await page.$('.gm-ask')) || !(await page.$('.gm-ov')));

  check('no errors in the console', errors.length === 0, errors.slice(0, 3).join(' | '));
  console.log('games browser: ' + pass + ' ok, ' + fail + ' failed; screenshots in ' + OUT);
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
