'use strict';
/* The arcade the way the Android app opens it: the website's page in a phone-sized Chrome with the app's reader bridge, a book page on screen,
 * then SBApp.openGames() (the footer's Games button) and the 🎮 tab of the page bar.   node tests/app/games_in_app.js [--out <folder>]
 * The arcade scripts are added by hand when lazy.html has not been regenerated yet. Local only; never shipped. */
const fs = require('fs'), path = require('path');
const { open, sleep, APP_ASSETS } = require('./phone');
const args = process.argv.slice(2);
const out = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : 'C:/tmp/games_in_app');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };

(async () => {
  const web = path.resolve(__dirname, '..', '..');
  const extra = ['sb_arcade.js', 'sb_arcade_runners.js', 'sb_arcade_shoot.js', 'sb_arcade_puzzle.js', 'sb_arcade_build.js'].map(f => path.join(web, 'js', f));
  const cat = JSON.parse(fs.readFileSync(path.join(APP_ASSETS, 'app_catalog.json'), 'utf8'));
  const t = await open({ out, extra: [] });
  try {
    const have = await t.page.evaluate(() => !!window.SBArcade);
    if (!have) for (const f of extra) await t.page.addScriptTag({ path: f });
    // the page bar must carry the Games tab as well (sb_page_tabs.js is part of the page, no need to add it)
    await t.page.evaluate(() => { window.__host = []; window.SBHost = { onAction(n, d) { window.__host.push(n); }, onState() {}, onReady() {}, speak() {}, stopSpeech() {} }; });
    const ch = cat.classes.find(c => c.id === 'cls5').subjects.find(s => s.id === 'cls5-math').chapters[2];
    await t.chapter('cls5', 'cls5-math', ch.o); await t.settle();
    await t.page.evaluate(() => window.SBApp.go(2)); await sleep(800);
    check('the page bar has a Games tab', await t.page.evaluate(() => !!document.querySelector('.sbapp-page-on .sb-pt-game')));

    // the footer's Games button
    const ok = await t.page.evaluate(() => window.SBApp.openGames());
    await sleep(500);
    const hub = await t.page.evaluate(() => ({ open: !!document.querySelector('.sba'), cards: document.querySelectorAll('.sba-card').length, q: SBArcade.current && SBArcade.current.pack.items.length }));
    check('SBApp.openGames() opens the arcade over the page (' + hub.cards + ' games, ' + hub.q + ' questions from this page)', ok && hub.open && hub.cards === 15 && hub.q >= 3, hub);
    await t.shot('hub');
    // a page swipe must not turn the page under the game
    const before = (await t.state()).page;
    await t.page.touchscreen.tap(195, 400);   // harmless tap on the hub
    check('the page does not move under the game', (await t.state()).page === before);
    // play one game for a few seconds, perfectly
    await t.page.evaluate(() => { SBArcade.current.start('subway'); SBArcade.current.E.auto = 'right'; });
    await sleep(6000);
    const play = await t.page.evaluate(() => ({ right: SBArcade.current.E.right, lives: SBArcade.current.E.lives, state: SBArcade.current.E.state }));
    check('a game runs in real time inside the page (' + play.right + ' right answers so far)', play.right >= 1 && play.lives === 3, play);
    await t.shot('playing');
    // back: game -> hub -> closed, and the app is told
    await t.page.evaluate(() => window.SBApp.gamesBack());
    check('back from a game goes to the hub', await t.page.evaluate(() => SBArcade.current && SBArcade.current.E.state === 'hub'));
    await t.page.evaluate(() => window.SBApp.gamesBack());
    check('back from the hub closes the arcade and tells the app', await t.page.evaluate(() => !document.querySelector('.sba') && window.__host.includes('gamesClosed')));
    check('the reader is where it was', (await t.state()).page === before);

    // the 🎮 tab of the page bar
    await t.page.evaluate(() => document.querySelector('.sbapp-page-on .sb-pt-game').click()); await sleep(400);
    check('the Games tab of the page bar opens it too', await t.page.evaluate(() => !!document.querySelector('.sba .sba-card')));
    await t.page.evaluate(() => window.SBApp.closeGames());
    check('closeGames() leaves nothing behind', await t.page.evaluate(() => !document.querySelector('.sba') && !document.documentElement.classList.contains('sba-lock')));
    check('no script errors', t.errors.length === 0, t.errors);
  } finally { await t.close(); }
  console.log(`\n${pass} passed, ${fail} failed.  Pictures: ${out}`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
