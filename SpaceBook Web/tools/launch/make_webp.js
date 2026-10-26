'use strict';
/* Makes a WebP next to each PNG of a folder (default covers/Classes Cards/Another-Look), using the installed Chrome's own encoder (no image library needed).
 *   node tools/launch/make_webp.js [--dir "covers/Classes Cards/Another-Look"] [--quality 0.82] [--check]
 * The website shows the WebP (about a sixth of the PNG's bytes); the PNG stays because tools/app/sync_app.js derives the app's covers from it.
 * --check fails when a PNG has no WebP or the WebP is older than the PNG. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const DIR = path.join(ROOT, opt('--dir', 'covers/Classes Cards/Another-Look'));
const Q = +opt('--quality', 0.82);
const pngs = fs.readdirSync(DIR).filter(f => /\.png$/i.test(f));
if (args.includes('--check')) {
  const bad = pngs.filter(f => { const w = path.join(DIR, f.replace(/\.png$/i, '.webp')); return !fs.existsSync(w) || fs.statSync(w).mtimeMs + 2000 < fs.statSync(path.join(DIR, f)).mtimeMs; });
  if (bad.length) { console.error('no current WebP for: ' + bad.join(', ') + ' (node tools/launch/make_webp.js)'); process.exit(1); }
  console.log('every PNG in ' + path.relative(ROOT, DIR) + ' has a current WebP (' + pngs.length + ')');
  process.exit(0);
}
(async () => {
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  const page = await browser.newPage();
  await page.goto('about:blank');
  let before = 0, after = 0;
  for (const f of pngs) {
    const buf = fs.readFileSync(path.join(DIR, f));
    const b64 = await page.evaluate(async ({ data, q }) => {
      const blob = new Blob([Uint8Array.from(atob(data), c => c.charCodeAt(0))], { type: 'image/png' });
      const bmp = await createImageBitmap(blob);
      const c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height;
      c.getContext('2d').drawImage(bmp, 0, 0);
      const out = await new Promise(r => c.toBlob(r, 'image/webp', q));
      const ab = new Uint8Array(await out.arrayBuffer());
      let s = ''; for (let i = 0; i < ab.length; i += 8192) s += String.fromCharCode.apply(null, ab.subarray(i, i + 8192));
      return btoa(s);
    }, { data: buf.toString('base64'), q: Q });
    const out = Buffer.from(b64, 'base64');
    fs.writeFileSync(path.join(DIR, f.replace(/\.png$/i, '.webp')), out);
    before += buf.length; after += out.length;
  }
  await browser.close();
  console.log(`${pngs.length} images: ${Math.round(before / 1024)} KB of PNG -> ${Math.round(after / 1024)} KB of WebP`);
})().catch(e => { console.error(e); process.exit(1); });
