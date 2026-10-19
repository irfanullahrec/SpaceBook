'use strict';
/* Builds what the offline layer needs (Phase 4):
 *   content/offline_map.json  for every subject: the lazy book files it loads (each with its content-hash URL, size, sha256) and the image
 *                             files its chapters reference. Found by opening the subject in a fresh app sandbox and rendering every
 *                             chapter and tab, so it is what the page really asks for. Drives "Download for offline" (js/core/offline.js).
 *   content/sw_version.js     the service worker's version, its shell (lazy.html + every script, stylesheet, font and icon the page needs
 *                             at start) and the entry page. sw.js imports it, so the browser installs a new worker whenever the shell changes.
 *   node --max-old-space-size=8192 tools/build/make_offline.js [--check] [--page lazy.html]
 * --check exits 1 when the committed files are stale. Run through tools/build/all.js (after the lazy page it describes). Dev-only. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { load, ROOT } = require('../lib/app_sandbox');
const args = process.argv.slice(2);
const CHECK = args.includes('--check');
const PAGE = args.includes('--page') ? args[args.indexOf('--page') + 1] : 'lazy.html';
const sha256 = buf => crypto.createHash('sha256').update(buf).digest('hex');
const lf = file => fs.readFileSync(path.join(ROOT, file), 'utf8').replace(/\r\n/g, '\n');

// ---- the files lazy.js can ask for, with the hash URL it uses (content/lazy_manifest.json, built from the same sources)
const lazyManifest = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'lazy_manifest.json'), 'utf8'));
const files = {};
const addFile = (src, sha, bytes) => { files[src] = { v: sha.slice(0, 12), bytes, sha256: sha }; };
const group = {};      // parent src -> [src of parent, also, after...]: everything one load of the parent fetches
for (const f of lazyManifest.files) {
  addFile(f.src, f.sha256, Buffer.byteLength(lf(f.src)));
  group[f.src] = [f.src];
  for (const a of (f.also || []).concat(f.after || [])) { addFile(a.src, a.sha256, a.bytes); group[f.src].push(a.src); }
}

// ---- per subject: open it in a fresh page, render everything, note which lazy files loaded and which images the HTML names
const VIEWS = {
  generic: { area: 'subjectTopicArea', content: 'subjTabContent', chapter: 'select\\w*(?:Chapter|Unit|Lesson|Page)', tab: 'switchSubjectTab', reset: 'state.activeSubjTab = null; ' },
  math: { area: 'mathTopicArea', content: 'mathTabContent', chapter: 'selectMathChapter', tab: 'switchMathTab', reset: '' },
};
const unesc = oc => oc.replace(/&#39;|&quot;/g, "'");
const IMG = /(?:src|href|data-src|poster)="((?:assets|covers)\/[^"?#]+|[^"?#:]+\.(?:png|jpe?g|gif|webp|svg))"|url\(['"]?((?:assets|covers)\/[^'")?#]+)/gi;
const assetSizes = {};
function assetsIn(html, into) {
  for (const m of html.matchAll(IMG)) {
    const p = (m[1] || m[2] || '').replace(/&amp;/g, '&');
    if (!p || /^(https?:|data:|blob:|\/\/)/.test(p) || p.startsWith('/')) continue;
    if (!(p in assetSizes)) { const full = path.join(ROOT, p); assetSizes[p] = fs.existsSync(full) && fs.statSync(full).isFile() ? fs.statSync(full).size : -1; }
    if (assetSizes[p] >= 0) into.add(p);
  }
}

const probe = load({ page: PAGE, quiet: true });
const subjects = probe.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))');
const map = { schema: 'spacebook.offline/1', files: {}, assets: {}, subjects: {} };
const t0 = Date.now();
for (const s of subjects) {
  const app = load({ page: PAGE, quiet: true });
  const step = code => { try { return app.run(code, 120000); } catch (e) { return null; } };
  const imgs = new Set();
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const body = step(`document.getElementById('dashboard-body').innerHTML`) || '';
  assetsIn(body, imgs);
  const V = body.includes('id="mathTopicArea"') ? VIEWS.math : VIEWS.generic;
  const chs = [...new Set([...body.matchAll(new RegExp('onclick="(' + V.chapter + '\\([^"]*)"', 'g'))].map(m => m[1]))];
  for (const oc of chs) {
    step(`${V.reset}${unesc(oc)}`);
    const area = step(`document.getElementById('${V.area}').innerHTML`) || '';
    assetsIn(area, imgs);
    for (const t of [...new Set([...area.matchAll(new RegExp('onclick="(' + V.tab + '\\([^"]*)"', 'g'))].map(m => m[1]))]) {
      step(`document.getElementById('${V.content}').innerHTML = ''`);
      step(unesc(t));
      assetsIn(step(`document.getElementById('${V.content}').innerHTML`) || '', imgs);
    }
  }
  const loaded = app.sb.SBLazy ? app.sb.SBLazy.stats().log.map(l => l.src) : [];
  const list = [...new Set([].concat(...loaded.map(src => group[src] || [src])))];
  const assets = [...imgs].sort();
  list.forEach(src => { map.files[src] = files[src]; });
  assets.forEach(a => { map.assets[a] = { bytes: assetSizes[a] }; });
  map.subjects[s.id] = { classId: s.classId, name: s.name, files: list, assets, bytes: list.reduce((n, src) => n + files[src].bytes, 0) + assets.reduce((n, a) => n + assetSizes[a], 0) };
}
map.files = Object.fromEntries(Object.keys(map.files).sort().map(k => [k, map.files[k]]));
map.assets = Object.fromEntries(Object.keys(map.assets).sort().map(k => [k, map.assets[k]]));

// ---- the service worker's shell: the page and everything it needs before the first screen
const html = lf(PAGE);
const shell = new Set([PAGE, 'offline.html', 'manifest.webmanifest', 'content/offline_map.json', 'logo_tuitionhub_trans.png']);
for (const m of html.matchAll(/<script\b[^>]*\bsrc="([^"]+)"/g)) if (!/^(https?:)?\/\//.test(m[1])) shell.add(m[1]);
for (const m of html.matchAll(/<link\b[^>]*\bhref="([^"]+)"/g)) if (!/^(https?:)?\/\//.test(m[1]) && !/rel="(preconnect|dns-prefetch)"/.test(m[0])) shell.add(m[1]);
for (const css of [...shell].filter(u => /\.css(\?|$)/.test(u))) {            // fonts and images a stylesheet names
  const file = css.split('?')[0], dir = path.posix.dirname(file);
  if (!fs.existsSync(path.join(ROOT, file))) continue;
  for (const m of lf(file).matchAll(/url\(['"]?([^'")]+)['"]?\)/g)) {
    const u = m[1].split(/[?#]/)[0];
    if (/^(data:|https?:|\/\/|\/)/.test(u) || !/\.woff2$/.test(u)) continue;     // one font format is enough: every browser that can install a PWA reads woff2
    shell.add(path.posix.normalize(path.posix.join(dir, u)));
  }
}
if (fs.existsSync(path.join(ROOT, 'icons'))) for (const f of fs.readdirSync(path.join(ROOT, 'icons')).sort()) shell.add('icons/' + f);
if (fs.existsSync(path.join(ROOT, 'fonts'))) for (const f of fs.readdirSync(path.join(ROOT, 'fonts')).sort()) if (/\.woff2$/.test(f)) shell.add('fonts/' + f);
const shellList = [...shell].filter(u => fs.existsSync(path.join(ROOT, u.split('?')[0]))).sort();
const versionOf = u => { const full = path.join(ROOT, u.split('?')[0]); return u + ':' + sha256(fs.readFileSync(full)).slice(0, 12); };
const swVersion = sha256(shellList.map(versionOf).join('\n')).slice(0, 12);
const swFile = '/* GENERATED by tools/build/make_offline.js: do not edit. sw.js imports this; a new version installs a new worker. */\n' +
  'self.SB_SW = ' + JSON.stringify({ version: swVersion, entry: PAGE, offlinePage: 'offline.html', shell: shellList }, null, 1) + ';\n';

const outputs = [['content/offline_map.json', JSON.stringify(map, null, 1) + '\n'], ['content/sw_version.js', swFile]];
let stale = 0;
for (const [file, text] of outputs) {
  const full = path.join(ROOT, file);
  if (CHECK) {
    const now = fs.existsSync(full) ? fs.readFileSync(full, 'utf8').replace(/\r\n/g, '\n') : null;
    if (now !== text) { console.log('STALE ' + file); stale++; }
  } else { fs.mkdirSync(path.dirname(full), { recursive: true }); fs.writeFileSync(full, text); }
}
const withFiles = Object.values(map.subjects).filter(s => s.files.length);
const bytes = Object.values(map.subjects).map(s => s.bytes);
console.log(`offline map: ${subjects.length} subjects (${withFiles.length} load book files, largest ${(Math.max(...bytes) / 1e6).toFixed(1)} MB, all together ${(Object.values(map.files).reduce((n, f) => n + f.bytes, 0) / 1e6).toFixed(0)} MB of book files + ${Object.keys(map.assets).length} images), ${((Date.now() - t0) / 60000).toFixed(1)} min`);
console.log(`service worker: version ${swVersion}, shell ${shellList.length} files (${(shellList.reduce((n, u) => n + fs.statSync(path.join(ROOT, u.split('?')[0])).size, 0) / 1e6).toFixed(1)} MB), entry ${PAGE}`);
if (CHECK) { if (stale) { console.log('run: node --max-old-space-size=8192 tools/build/make_offline.js'); process.exit(1); } console.log('offline map and service worker version are up to date'); }
