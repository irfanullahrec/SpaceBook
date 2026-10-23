'use strict';
/* One screenshot per book family, as the app's reader shows a page (phone width). Local only.
 *   node tests/app/gallery.js [outdir] [--only cls5-math,cls9-phy] [--page N] [--tab Exercises] [--width 360]
 * Prints, per book, the reader state and how far the page starts from the top of the screen (the first pixel of content). */
const fs = require('fs'), path = require('path');
const { open, sleep, APP_ASSETS } = require('./phone');

const BOOKS = [
  ['cls1', 'cls1-math', 1], ['cls2', 'cls2-eng', 1], ['cls3', 'cls3-math', 1], ['cls5', 'cls5-math', 2], ['cls6', 'cls6-sci', 1],
  ['cls7', 'cls7-urdu', 1], ['cls8', 'cls8-eng', 1], ['cls9', 'cls9-math', 1], ['cls9', 'cls9-phy', 1], ['cls10', 'cls10-eng', 1],
  ['cls11', 'cls11-phy', 1], ['cls12', 'cls12-math', 1],
];

(async () => {
  const args = process.argv.slice(2);
  const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
  const out = path.resolve(args[0] && !args[0].startsWith('--') ? args[0] : 'C:/tmp/gallery');
  const only = opt('--only', '') ? opt('--only', '').split(',') : null;
  const page = +opt('--page', 1), tab = opt('--tab', ''), width = +opt('--width', 390);
  const cat = JSON.parse(fs.readFileSync(path.join(APP_ASSETS, 'app_catalog.json'), 'utf8'));
  const t = await open({ out, width, height: 780 });
  try {
    for (const [cls, sid, ch] of BOOKS) {
      if (only && !only.includes(sid)) continue;
      const c = cat.classes.find(x => x.id === cls), s = c && c.subjects.find(x => x.id === sid);
      const chap = s && s.chapters[ch];
      if (!chap) { console.log(sid, 'no chapter', ch); continue; }
      try {
        await t.chapter(cls, sid, chap.o, 0, tab);
        await t.settle();
        await t.page.evaluate(n => window.SBApp.go(n), page);
        await sleep(700);
        const st = await t.state();
        const geo = await t.page.evaluate(() => {
          const el = document.querySelector('.sbapp-page-on') || document.querySelector('#subjTabContent') || document.body;
          const r = el.getBoundingClientRect();
          return { firstTop: Math.round(r.top), left: Math.round(r.left), right: Math.round(innerWidth - r.right), scrollW: document.documentElement.scrollWidth };
        });
        const f = await t.shot(sid + '-c' + ch);
        console.log(sid.padEnd(14), JSON.stringify({ pages: st.pages, mode: st.mode, tab: st.tab, ...geo }), path.basename(f));
      } catch (e) { console.log(sid, 'ERROR', String(e.message).slice(0, 160)); }
    }
  } finally { await t.close(); }
  if (t.errors.length) console.log('page errors:\n' + t.errors.slice(0, 8).join('\n'));
})().catch(e => { console.error(e); process.exit(1); });
