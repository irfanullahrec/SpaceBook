'use strict';
/* Runs tools/study_plan/extract_in_page.js without a browser: in the app sandbox (tools/lib/app_sandbox.js), with the sidebar read
 * from the HTML the app renders (parsed with jsdom, a dev dependency) instead of from a live page. The extractor itself is not copied:
 * its source is taken as it is and only the three browser-only parts are swapped (timers, the sidebar query, the result element).
 *   const { extract } = require('./node_backend'); const data = extract({ page: 'lazy.html' });
 * Dev-only. */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('../lib/app_sandbox');

function candidateNames() {
  const JS = path.join(ROOT, 'js'), names = new Set();
  for (const f of fs.readdirSync(JS).filter(f => f.endsWith('.js'))) {
    const src = fs.readFileSync(path.join(JS, f), 'utf8');
    for (const m of src.matchAll(/^(?:const|let|var)\s+([A-Z][A-Za-z0-9_$]*)/gm)) names.add(m[1]);
    for (const m of src.matchAll(/window\.([A-Z][A-Z0-9_]+)\s*=/g)) names.add(m[1]);
  }
  names.add('DATA');
  return [...names];
}

function swap(code, from, to) {
  if (!code.includes(from)) throw new Error('study index extractor changed: cannot find ' + from.slice(0, 50));
  return code.replace(from, () => to);
}

function extract(opts = {}) {
  const { JSDOM } = require('jsdom');
  const app = load({ page: opts.page || 'lazy.html', quiet: true });
  const SIDEBAR = '.math-ch-list [onclick*="Chapter("], .math-ch-list button, .drawing-page-list button';
  // what the extractor read from the live page: the visible sidebar entries of the subject just opened
  app.sb.__sidebar = () => {
    const html = app.run("document.getElementById('dashboard-body').innerHTML");
    const doc = new JSDOM('<body>' + html + '</body>').window.document;
    const hidden = el => { for (let e = el; e && e.nodeType === 1; e = e.parentElement) { if (e.hasAttribute('hidden') || /display\s*:\s*none/i.test(e.getAttribute('style') || '')) return true; } return false; };
    return [...doc.querySelectorAll(SIDEBAR)].filter(e => !hidden(e)).map(e => e.textContent);
  };
  let code = fs.readFileSync(path.join(__dirname, 'extract_in_page.js'), 'utf8');
  code = swap(code, "const visible = () => [...document.querySelectorAll(SIDEBAR)].filter(e => e.offsetParent !== null);", "const visible = () => __sidebar().map(t => ({ textContent: t }));");
  code = code.replace(/await wait\(\d+\);?/g, '');                         // nothing is asynchronous here: openSubject renders synchronously
  code = swap(code, "(async () => {", "(() => {");
  code = swap(code, "const pre = document.createElement('pre'); pre.id = 'sp-out'; pre.textContent = JSON.stringify(out); document.body.appendChild(pre);", "window.__SP_RESULT = JSON.stringify(out);");
  app.sb.__SP_NAMES = candidateNames();
  code = code.replace(/window\.__SP_NAMES/g, '__SP_NAMES');
  app.run(code, 3600000);
  const result = app.sb.__SP_RESULT;
  if (!result) throw new Error('study index extraction produced no result');
  return JSON.parse(result);
}

module.exports = { extract };
