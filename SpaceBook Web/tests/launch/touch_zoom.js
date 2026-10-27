'use strict';
/* What jsdom cannot judge (acceptance criterion AC-A2), in a real Chrome: touch-target size on a phone, no sideways scrolling on a phone and at 200 % zoom,
 * and reduced motion.
 *   node --max-old-space-size=3072 tests/launch/touch_zoom.js [--json docs/launch/TOUCH_ZOOM.json]
 * Views: Home (class cards), the subjects of Class 5, a subject, a chapter and its Exercise tab. Phone = 375 x 812 with touch; 200 % zoom = a 640 px wide window
 * (a 1280 px window zoomed to 200 %). A target is a visible button, link, input, select, textarea or role=button/tab/checkbox/radio; it is reported when its
 * box is smaller than 44 x 44 CSS px (links inside running text are not counted: the WCAG "inline" exception). Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const { serve, launch } = require('../baseline/lib');
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 500) : '')); } };
const args = process.argv.slice(2);
const OUT = args.includes('--json') ? path.resolve(args[args.indexOf('--json') + 1]) : null;

const measure = () => {
  const sel = 'button, a[href], input:not([type=hidden]), select, textarea, [role=button], [role=tab], [role=checkbox], [role=radio], [onclick]';
  const seen = new Set(), small = [], all = [];
  for (const el of document.querySelectorAll(sel)) {
    if (seen.has(el)) continue; seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || el.closest('[hidden],[aria-hidden=true],[inert]')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (el.tagName === 'A' && !el.matches('.btn, [class*=btn], [role=button]') && el.closest('p, li, td, span.sentence, .sentence') && cs.display === 'inline') continue;   // a link inside running text
    if (el.tagName === 'INPUT' && /^(radio|checkbox)$/.test(el.type) && el.closest('label')) continue;                                                              // the label is the target
    all.push(1);
    if (r.width < 44 || r.height < 44) small.push({ tag: el.tagName.toLowerCase(), cls: String(el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className || '').slice(0, 60), text: (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0, 24), w: Math.round(r.width), h: Math.round(r.height) });
  }
  return { targets: all.length, small };
};

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const result = { views: {} };
  async function openPage(ctxOpts) {
    const ctx = await browser.newContext(ctxOpts);
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 140)));
    await page.goto(url + 'lazy.html', { waitUntil: 'load', timeout: 120000 });
    await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function' && document.querySelector('#page-content') && document.querySelector('#page-content').innerHTML.length > 1500, null, { timeout: 120000 });
    await sleep(2500);
    return { ctx, page, errors };
  }
  const views = [
    ['home', async p => { await p.evaluate(() => renderClasses()); }],
    ['class 5 subjects', async p => { await p.evaluate(() => goToSubjects('cls5')); }],
    ['subject (Class 5 English)', async p => { await p.evaluate(() => openSubject('cls5', 'cls5-eng')); }],
    ['chapter', async p => { await p.evaluate(() => selectSubjectChapter('eng', 1, 'cls5')); }],
    ['exercise tab', async p => { await p.evaluate(() => { const b = [...document.querySelectorAll('.math-nav-tabs button, .topic-sub-tabs-bar button')].find(x => /exercise/i.test(x.textContent || '')); if (b) b.click(); }); }],
  ];
  const profiles = [
    ['phone 375 px', { viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }],
    ['200 % zoom (640 px window)', { viewport: { width: 640, height: 900 } }],
  ];
  for (const [pname, opts] of profiles) {
    const { ctx, page, errors } = await openPage(opts);
    for (const [vname, go] of views) {
      try { await go(page); await sleep(1800); } catch (e) { check(pname + ': ' + vname + ' opens', false, String(e.message).slice(0, 120)); continue; }
      const o = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth, body: document.body.scrollWidth }));
      const over = Math.max(o.sw, o.body) - o.iw;
      check(`${pname}: ${vname}: no sideways scrolling`, over <= 1, o);
      if (pname.startsWith('phone')) {
        const m = await page.evaluate(measure);
        const groups = {}; for (const x of m.small) { const k = x.tag + '.' + (x.cls.split(' ')[0] || '-'); (groups[k] = groups[k] || { n: 0, w: x.w, h: x.h, text: x.text }).n++; }
        result.views[vname] = { targets: m.targets, small: m.small.length, groups: Object.entries(groups).sort((a, b) => b[1].n - a[1].n).slice(0, 14).map(([k, v]) => `${k} x${v.n} ${v.w}x${v.h} "${v.text}"`) };
        console.log(`INFO  ${vname}: ${m.targets} touch targets, ${m.small.length} smaller than 44 x 44 px` + (m.small.length ? ' e.g. ' + m.small.slice(0, 4).map(s => `${s.tag}.${s.cls}"${s.text}" ${s.w}x${s.h}`).join('; ') : ''));
      }
    }
    check(pname + ': no script error', errors.length === 0, errors.slice(0, 3));
    await ctx.close();
  }
  // the header must fit the phone: the account button, the coins and the offline button are on screen (they were pushed off the right edge)
  for (const w of [360, 375, 412]) {
    const { ctx, page } = await openPage({ viewport: { width: w, height: 800 }, isMobile: true, hasTouch: true });
    const r = await page.evaluate(() => ['.hamburger-btn', '.header-search-box input', '.sb-off-btn', '.sbr-chip', '.header-user-avatar'].map(s => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return { s, ok: b.left >= 0 && b.right <= innerWidth + 0.5, x: Math.round(b.left) + '..' + Math.round(b.right) }; }).filter(x => x && !x.ok));
    check(`header at ${w} px: every control is on screen`, r.length === 0, r);
    await ctx.close();
  }
  // reduced motion: no animation or transition keeps running on the main views
  {
    const { ctx, page } = await openPage({ viewport: { width: 1280, height: 860 }, reducedMotion: 'reduce' });
    for (const [vname, go] of views.slice(0, 4)) {
      await go(page); await sleep(1500);
      const anim = await page.evaluate(() => document.getAnimations().filter(a => a.playState === 'running').map(a => (a.animationName || a.transitionProperty || 'animation') + ' ' + (a.effect && a.effect.target ? (a.effect.target.className || a.effect.target.tagName) : '')).slice(0, 6));
      check(`reduced motion: ${vname}: no animation keeps running`, anim.length === 0, anim);
    }
    await ctx.close();
  }
  const totalSmall = Object.values(result.views).reduce((n, v) => n + v.small, 0), totalT = Object.values(result.views).reduce((n, v) => n + v.targets, 0);
  console.log(`---\ntouch targets on the five phone views: ${totalT}, ${totalSmall} below 44 x 44 px (${totalT ? Math.round(100 * totalSmall / totalT) : 0} %)`);
  if (OUT) fs.writeFileSync(OUT, JSON.stringify(result, null, 1) + '\n');
  await browser.close(); server.close();
  console.log(`touch / zoom / motion test: ${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
