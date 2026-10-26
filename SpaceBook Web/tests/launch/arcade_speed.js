'use strict';
/* The page arcade's gentle start, in a real Chrome with the real animation loop:
 *   - a how-to-play screen (what to do, with the controls) comes before a game the first time it is chosen;
 *   - the games run at Easy speed by default (three quarters of the old speed), Slow is slower, Normal is the old speed; the choice is kept;
 *   - Pause stops the game clock and the timers for real (the game clock and the lives do not move while paused), Resume carries on;
 *   - the speed buttons are at least 44 px and the group is named for screen readers.
 *     node tests/launch/arcade_speed.js
 * Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const page = await (await browser.newContext({ viewport: { width: 390, height: 780 }, hasTouch: true, isMobile: true })).newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(url + 'tests/arcade/harness.html', { waitUntil: 'load' });
  await page.waitForFunction(() => window.SBArcade && SBArcade.games.length > 0);
  await page.evaluate(() => localStorage.clear());
  await page.evaluate(() => { window.__a = SBArcade.open(SAMPLE_EN, { seed: 5 }); });
  await page.waitForSelector('.sba-hub');

  // ---- speed choice on the hub
  const grp = page.locator('.sba-speed');
  check('the hub has a speed group named for screen readers, with Slow, Easy and Normal', (await grp.getAttribute('role')) === 'radiogroup' && (await grp.getAttribute('aria-label')) === 'Game speed' && (await grp.locator('button').count()) === 3);
  check('Easy is chosen by default and runs at three quarters of the old speed', (await grp.locator('button.on').innerText()) === 'Easy' && await page.evaluate(() => __a.E.speed === 0.75));
  check('every speed button is at least 44 px', await page.evaluate(() => [...document.querySelectorAll('.sba-speed button')].every(b => { const r = b.getBoundingClientRect(); return r.width >= 44 && r.height >= 44; })));
  await grp.locator('button', { hasText: 'Slow' }).click();
  check('Slow is slower and the choice is kept', await page.evaluate(() => __a.E.speed === 0.55 && JSON.parse(localStorage.getItem('sb_arcade_speed')) === 'slow'));
  await grp.locator('button', { hasText: 'Normal' }).click();
  check('Normal is the old speed', await page.evaluate(() => __a.E.speed === 1 && JSON.parse(localStorage.getItem('sb_arcade_speed')) === 'normal'));

  // ---- how to play, the first time
  await page.locator('.sba-card[data-g="snake"]').click();
  await page.waitForSelector('.sba-msg [data-a="go"]');
  const how = await page.locator('.sba-msg').innerText();
  check('the first time, a how-to-play screen says what to do, before the game starts', /Snake/.test(how) && how.length > 120 && /Play/.test(how) && (await page.evaluate(() => __a.E.state)) !== 'play', how.slice(0, 200));
  check('the speed can be changed on that screen too', (await page.locator('.sba-msg .sba-speed').count()) === 1);

  // ---- the speed is real: the game clock advances at the chosen rate
  const rate = async speed => {
    await page.locator('.sba-speed button[data-sp="' + speed + '"]').click();
    const a = await page.evaluate(() => __a.E.t); await sleep(1500); const b = await page.evaluate(() => __a.E.t);
    return (b - a) / 1.5;
  };
  await page.locator('[data-a="go"]').click();
  await page.waitForFunction(() => __a.E.state === 'play');
  // the speed buttons are on the hub and the how-to screen only: set the speed through the same pref the buttons write, as a student would between games
  await page.evaluate(() => { __a.E.speed = 1; });
  const a1 = await page.evaluate(() => __a.E.t); await sleep(1500); const b1 = await page.evaluate(() => __a.E.t);
  const normalRate = (b1 - a1) / 1.5;
  await page.evaluate(() => { __a.E.speed = 0.55; });
  const a2 = await page.evaluate(() => __a.E.t); await sleep(1500); const b2 = await page.evaluate(() => __a.E.t);
  const slowRate = (b2 - a2) / 1.5;
  check('at Normal the game clock runs about one second per second; at Slow about half as fast', normalRate > 0.8 && normalRate < 1.2 && slowRate > 0.35 && slowRate < 0.75 && slowRate < normalRate * 0.75, { normalRate, slowRate });

  // ---- pause stops it
  const lives0 = await page.evaluate(() => __a.E.lives);
  await page.locator('.sba-top [data-a="pause"]').click();
  const t1 = await page.evaluate(() => __a.E.t);
  await sleep(2500);
  const t2 = await page.evaluate(() => __a.E.t);
  check('paused: the game clock does not move for 2.5 seconds and no life is lost', t1 === t2 && (await page.evaluate(() => __a.E.paused === true && __a.E.lives)) === lives0, { t1, t2 });
  check('paused: a Paused message with a Resume button is shown', /Paused/.test(await page.locator('.sba-msg').innerText()) && (await page.locator('.sba-msg [data-a="resume"]').count()) === 1);
  await page.locator('[data-a="resume"]').click();
  await sleep(800);
  const t3 = await page.evaluate(() => __a.E.t);
  check('Resume carries on from where it stopped', t3 > t2 && t3 < t2 + 1.5, { t2, t3 });
  check('no script error', errors.length === 0, errors);
  await browser.close(); server.close();
  console.log('---\narcade speed test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
