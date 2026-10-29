'use strict';
/* Shared helpers for the browser baseline: a static file server for the app folder and a Chromium launcher.
 * Locally the installed Chrome is used (no browser download); in CI set PW_CHANNEL= (empty) after
 * `npx playwright install chromium`. Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.webp': 'image/webp', '.gif': 'image/gif', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.mp4': 'video/mp4',
  '.mp3': 'audio/mpeg', '.ico': 'image/x-icon', '.pdf': 'application/pdf' };

function serve(port = 0) {
  const cache = new Map(); // scripts and styles are read from disk once per run
  return new Promise(resolve => {
    const server = http.createServer((req, res) => {
      let p = decodeURIComponent(req.url.split('?')[0]);
      if (p.endsWith('/')) p += 'index.html';
      const f = path.join(ROOT, p);
      if (!f.startsWith(ROOT) || /[\\/]api[\\/]config\.php$/i.test(f)) { res.writeHead(403); return res.end(); }
      const cached = cache.get(f);
      if (cached) { res.writeHead(200, { 'Content-Type': TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream' }); return res.end(cached); }
      fs.readFile(f, (err, buf) => {
        if (err) { res.writeHead(404); return res.end(); }
        if (/\.(js|css|html)$/i.test(f)) cache.set(f, buf);
        res.writeHead(200, { 'Content-Type': TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream' });
        res.end(buf);
      });
    });
    server.listen(port, '127.0.0.1', () => resolve({ server, url: 'http://127.0.0.1:' + server.address().port + '/' }));
  });
}

// Every context gets the access of a person with every plan (js/sb_access.js keeps its answer in localStorage), so the pages show every chapter.
// launch({ anonymous: true }) leaves the visitor's view alone (tests/access/*).
async function launch(opts = {}) {
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  if (!opts.anonymous) {
    const state = require('../../tools/lib/test_access_state')();
    const init = s => { try { localStorage.setItem('sb_access_v1', s); } catch (e) { /* no storage */ } };
    const newContext = browser.newContext.bind(browser), newPage = browser.newPage.bind(browser);
    browser.newContext = async o => { const c = await newContext(o); await c.addInitScript(init, state); return c; };
    browser.newPage = async o => { const p = await newPage(o); await p.context().addInitScript(init, state); return p; };
  }
  return browser;
}

module.exports = { ROOT, serve, launch };
