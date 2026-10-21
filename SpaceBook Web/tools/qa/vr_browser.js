'use strict';
/* Real-browser check of the animated solutions: loads lazy.html, walks MATH_12_DATA, and counts the items for which SBVR.autoHtml
 * returns an animation host, then mounts one of the new calculus packs and reports the board steps.
 *   node tools/qa/vr_browser.js */
const path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const { serve, launch } = require(path.join(ROOT, 'tests', 'baseline', 'lib'));
(async () => {
  const { server, url } = await serve(); const browser = await launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const errors = []; page.on('pageerror', e => errors.push(e.message.slice(0, 200)));
  await page.goto(url + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 600000 });
  await page.waitForTimeout(5000);
  await page.waitForFunction(() => typeof openSubject === 'function' && typeof DATA !== 'undefined', null, { timeout: 600000 });
  const res = await page.evaluate(() => {
    const out = { packs: SBVR.sol.all().length, tot: 0, host: 0, calc: [] };
    const seen = new Set();
    const walk = (o, d) => {
      if (!o || typeof o !== 'object' || seen.has(o) || d > 14) return; seen.add(o);
      if (!Array.isArray(o) && typeof o.question === 'string' && (Array.isArray(o.steps) || typeof o.solution === 'string')) {
        out.tot++; let h = ''; try { h = SBVR.autoHtml(o) || ''; } catch (e) { h = ''; }
        if (h) out.host++;
        if (/integration by parts|dx\)|Find fₓ and fᵧ|coth x|production function/.test(o.question) && h) out.calc.push(o.question.slice(0, 50));
      }
      for (const k of Object.keys(o)) walk(o[k], d + 1);
    };
    walk(window.MATH_12_DATA, 0);
    return out;
  });
  console.log(JSON.stringify(res, null, 1), 'page errors', errors.length, errors.slice(0, 3));
  await browser.close(); server.close();
})().catch(e => { console.error(e); process.exit(2); });
