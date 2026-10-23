'use strict';
/* Plays every arcade game in a real Chrome, frame by frame (a clock we control, no waiting):
 *   a perfect player (env.auto = 'right') must win every game in the time a student has;
 *   a careless player (env.auto = 'wrong') must lose every game, never crash it, and never win.
 * It also checks the overlay (hub, how-to-play, pause, close) and takes a picture of each game at phone size.
 *     node tests/arcade/play.js [--only subway,snake] [--out <folder for pictures>] [--width 390 --height 780]
 * Local only (needs the installed Chrome); never shipped. */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const only = opt('--only', '') ? opt('--only', '').split(',') : null;
const OUT = path.resolve(opt('--out', path.join(os.tmpdir(), 'sb_arcade_shots')));
const WIDTH = +opt('--width', 390), HEIGHT = +opt('--height', 780);
fs.mkdirSync(OUT, { recursive: true });
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: WIDTH, height: HEIGHT }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|Failed to load resource/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.goto(url + 'tests/arcade/harness.html', { waitUntil: 'load' });
  await page.waitForFunction(() => window.SBArcade && SBArcade.games.length > 0);
  const ids = await page.evaluate(() => SBArcade.games.map(g => g.id));
  check('fifteen games are registered', ids.length === 15, ids);
  const wanted = ids.filter(id => !only || only.includes(id));

  // ---- the questions of a page ----
  const ex = await page.evaluate(() => { const r = SBArcade.extract(SAMPLE_EN); return { n: r.items.length, usable: r.usable, kinds: [...new Set(r.items.map(i => i.kind))], bad: r.items.filter(i => i.d.length < 2 || i.d.includes(i.a) || !/_____/.test(i.q)).length, sample: r.items.slice(0, 3).map(i => i.q + ' => ' + i.a + ' | ' + i.d.slice(0, 3).join(',')) }; });
  check('a lesson page makes questions (' + ex.n + ')', ex.usable && ex.n >= 8 && ex.bad === 0, ex);
  const urx = await page.evaluate(() => { const r = SBArcade.extract(SAMPLE_UR); return { n: r.items.length, usable: r.usable }; });
  check('an Urdu page makes questions too (' + urx.n + ')', urx.usable, urx);
  const none = await page.evaluate(() => SBArcade.extract('Contents. Page 3. Unit 1.').usable);
  check('a page with almost no text makes none', none === false);
  const sums = await page.evaluate(() => SBArcade.extract(SAMPLE_EN).items.filter(i => i.kind === 'eq').map(i => i.q + ' ' + i.a));
  check('printed sums become "12 + 7 = ?" questions', sums.some(s => /12 \+ 7 = _____ 19/.test(s)) && sums.some(s => /3 x 4 = _____ 12/.test(s)), sums);

  // ---- no content: the message, not a blank screen ----
  await page.evaluate(() => SBArcade.open('Contents. Page 3.', { manual: true }));
  const msg = await page.evaluate(() => document.querySelector('.sba-msg h2') && document.querySelector('.sba-msg h2').textContent);
  check('a page with nothing to play says so', /no games/i.test(msg || ''), msg);
  await page.screenshot({ path: path.join(OUT, '00-no-content.png') });
  await page.evaluate(() => SBArcade.close());

  // ---- the hub ----
  await page.evaluate(() => SBArcade.open(SAMPLE_EN, { manual: true, seed: 3 }));
  const cards = await page.evaluate(() => document.querySelectorAll('.sba-card').length);
  check('the hub shows every game', cards === 15, cards);
  await page.screenshot({ path: path.join(OUT, '01-hub.png') });
  await page.evaluate(() => SBArcade.close());
  check('closing leaves nothing behind', await page.evaluate(() => !document.querySelector('.sba') && !document.documentElement.classList.contains('sba-lock')));

  // ---- every game, both players ----
  async function run(id, auto, seed, seconds) {
    return page.evaluate(({ id, auto, seed, seconds }) => {
      const a = SBArcade.open(SAMPLE_EN, { manual: true, seed, auto, game: id });
      const E = a.E; let frames = 0, errs = 0, shot = null;
      const max = Math.round(seconds * 60);
      const old = console.error; console.error = (...x) => { errs++; old.apply(console, x); };
      while ((E.state === 'play' || E.state === 'ending') && frames < max) { a.step(1 / 60); frames++; }
      console.error = old;
      const out = { state: E.state, right: E.right, goal: E.goal, lives: E.lives, score: E.score, seconds: +(frames / 60).toFixed(1), errs, wrongs: E.wrongs };
      a.close();
      return out;
    }, { id, auto, seed, seconds });
  }
  for (const id of wanted) {
    const res = await run(id, 'right', 11, 240);
    check(id + ': a perfect player wins (' + res.right + '/' + res.goal + ' in ' + res.seconds + ' s, score ' + res.score + ')', res.state === 'won' && res.lives === 3 && res.errs === 0, res);
    const bad = await run(id, 'wrong', 5, 240);
    check(id + ': a careless player loses (' + bad.wrongs + ' mistakes in ' + bad.seconds + ' s)', bad.state === 'lost' && bad.right === 0 && bad.errs === 0, bad);
  }

  // ---- the coin keys are the shape api/lib/rewards.php accepts ----
  const RX = /^[A-Za-z0-9_.:-]{1,40}\|[A-Za-z0-9_.:-]{1,60}\|u[A-Za-z0-9]{0,8}\|(trace|count)\|[a-z0-9]{1,10}\|[0-9]{1,3}$/;
  const keys = await page.evaluate(() => SBArcade.games.map(g => { const a = SBArcade.open(SAMPLE_EN, { manual: true, game: g.id }); const k = a.E.key; a.close(); return [g.id, k]; }));
  check('the coin key of every game has the shape the server accepts', keys.every(([, k]) => RX.test(k)), keys.filter(([, k]) => !RX.test(k)));
  check('and each game has a key of its own', new Set(keys.map(([, k]) => k)).size === keys.length);

  // ---- a picture of each game mid-play (phone width) ----
  for (const id of wanted) {
    await page.evaluate(({ id }) => { window.__a = SBArcade.open(SAMPLE_EN, { manual: true, seed: 21, auto: 'right', game: id }); for (let i = 0; i < 150; i++) window.__a.step(1 / 60); }, { id });
    await page.screenshot({ path: path.join(OUT, id + '.png') });
    await page.evaluate(() => { window.__a.close(); });
  }

  // ---- pause and Escape ----
  await page.evaluate(() => { window.__a = SBArcade.open(SAMPLE_EN, { manual: true, seed: 2, game: 'snake' }); });
  await page.click('[data-a="pause"]');
  check('pause stops the game', await page.evaluate(() => window.__a.E.state === 'paused' && !!document.querySelector('[data-a="resume"]')));
  await page.click('[data-a="resume"]');
  check('resume carries on', await page.evaluate(() => window.__a.E.state === 'play'));
  await page.click('[data-a="back"]');
  check('the back button returns to the hub, a second one closes', await page.evaluate(() => window.__a.E.state === 'hub' && !!document.querySelector('.sba-card')));
  await page.click('[data-a="back"]');
  check('closed', await page.evaluate(() => !document.querySelector('.sba')));

  check('no script errors', errors.length === 0, errors);
  console.log(`\n${pass} passed, ${fail} failed.  Pictures: ${OUT}`);
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
