'use strict';
/* Data parity: everything the website shows is available, and the same, in the Android app, online and offline.
 *     node --max-old-space-size=8192 tools/parity/data_parity.js [--app "<folder of the app repo>"] [--no-app]
 * Fails (exit 1) when
 *   1. a class or subject of the website's registry (DATA, CLSn_BOOKS) is missing from content/app_catalog.json or content/offline_map.json
 *      and is not named in docs/parity.json "catalogExemptions" (with the reason), or an exemption is no longer needed;
 *   2. a chapter of the search index (the chapters the website lists) is missing from, or differs in the catalog, or has no open-call;
 *   3. a file listed in content/offline_map.json is missing, has the wrong size or the wrong SHA-256 (what "Download books" verifies on the phone);
 *   4. a script lazy.html names can be neither found in the shell (what the app bundles) nor downloaded on demand (offline map / lazy manifest);
 *   5. the app's bundled shell, catalog, question bank, test list or covers are not what tools/app/sync_app.js would produce now (stale);
 *   6. the app's MCQ bank is not the one derived from js/test_prep_bank.js (part of 5), or the page's units differ between the website's
 *      locator (js/sb_library.js) and the app's bridge (assets/reader_bridge.js).
 * The app folder defaults to ../SpaceBook App; where it is absent (CI checks out this repository only) the checks of the app's own files are skipped
 * and say so. Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const bundle = require('../app/lib/bundle');
const ROOT = bundle.ROOT;
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets');
const HAVE_APP = !args.includes('--no-app') && fs.existsSync(ASSETS);

let pass = 0, fail = 0;
const check = (label, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + (typeof detail === 'string' ? detail : JSON.stringify(detail)).slice(0, 700) : '')); } };
const json = f => JSON.parse(fs.readFileSync(path.join(ROOT, f), 'utf8'));
const parity = fs.existsSync(path.join(ROOT, 'docs', 'parity.json')) ? json('docs/parity.json') : { catalogExemptions: [] };
const exempt = new Map();
(parity.catalogExemptions || []).forEach(e => (e.subjects || []).forEach(s => exempt.set(s, e.reason)));

(async () => {
  // ---- 1 + 2: the registry and the chapters
  console.log('--- registry, catalog, offline map ---');
  const { load } = require('../lib/app_sandbox');
  const app = load({ quiet: true, page: 'index.html' });
  const D = app.run('DATA');
  const catalog = json('content/app_catalog.json');
  const offline = json('content/offline_map.json');
  const search = json('content/search/index.json');
  const catSubjects = new Map();
  catalog.classes.forEach(c => c.subjects.forEach(s => catSubjects.set(s.id, { cls: c.id, subj: s })));

  const registry = [];
  D.classes.forEach(c => (D.subjects[c.id] || []).forEach(s => registry.push({ cls: c.id, id: s.id })));
  check(`the registry has ${D.classes.length} classes and ${registry.length} subjects`, registry.length > 100, registry.length);

  const notInCatalog = registry.filter(r => !catSubjects.has(r.id) && !exempt.has(r.id)).map(r => r.id);
  check('every subject of the registry is in the app catalog (or exempted with a reason in docs/parity.json)', notInCatalog.length === 0, notInCatalog);
  const needless = [...exempt.keys()].filter(id => catSubjects.has(id));
  check('no exemption names a subject the catalog already has', needless.length === 0, needless);
  const notInRegistry = [...catSubjects.keys()].filter(id => !registry.some(r => r.id === id));
  check('the catalog lists nothing the registry does not have', notInRegistry.length === 0, notInRegistry);
  const classesInCatalog = new Set(catalog.classes.map(c => c.id));
  const classesMissing = D.classes.map(c => c.id).filter(id => !classesInCatalog.has(id) && !registry.filter(r => r.cls === id).every(r => exempt.has(r.id)));
  check('every class of the registry is in the catalog unless all its subjects are exempted', classesMissing.length === 0, classesMissing);
  const notOffline = registry.filter(r => !offline.subjects[r.id]).map(r => r.id);
  check('every subject of the registry is in the offline map (Books on this phone can download it)', notOffline.length === 0, notOffline);

  // the books: every CLSn_BOOKS entry is reachable through a chapter call of the catalog
  const calls = new Set();
  catalog.classes.forEach(c => c.subjects.forEach(s => s.chapters.forEach(ch => { const m = /^selectSubjectChapter\('([^']+)', \d+, '([^']+)'\)$/.exec(ch.o); if (m) calls.add(m[2] + ':' + m[1]); })));
  const bookKeys = [];
  Object.keys(app.sb).filter(k => /^CLS\d+_BOOKS$/.test(k)).forEach(g => Object.keys(app.sb[g]).forEach(k => bookKeys.push('cls' + g.replace(/\D/g, '') + ':' + k)));
  const reachableBook = b => { const [c, k] = b.split(':'); const s = catSubjects.get(c + '-' + k); return calls.has(b) || !!(s && s.subj.chapters.length); };
  const bookExempt = (parity.bookExemptions || []).map(e => e.book);
  const unexplained = bookKeys.filter(b => !reachableBook(b) && !bookExempt.includes(b) && !exempt.has(b.replace(':', '-')));
  check(`every one of the ${bookKeys.length} rebuilt books (CLSn_BOOKS) has chapters in the catalog (or an exemption)`, unexplained.length === 0, unexplained);

  // chapters: the catalog lists what the search index lists, in the same order, each with the call that opens it
  let chapterTotal = 0;
  const diffs = [];
  Object.keys(search.subjects).forEach(id => {
    const s = search.subjects[id], c = catSubjects.get(id);
    if (!c) { if (!exempt.has(id)) diffs.push(id + ': not in the catalog'); return; }
    const a = c.subj.chapters.map(x => x.t), b = (s.c || []).map(x => x.t);
    chapterTotal += a.length;
    if (a.length !== b.length || a.some((t, i) => t !== b[i])) diffs.push(`${id}: ${a.length} chapters in the catalog, ${b.length} in the search index`);
    c.subj.chapters.forEach((x, i) => { if (!x.o) diffs.push(`${id} chapter ${i + 1} has no open-call`); });
  });
  check(`the ${chapterTotal} chapters of the catalog are the chapters the website lists (same titles, same order, each with an open-call)`, diffs.length === 0, diffs.slice(0, 8));

  // ---- 3: the offline map is true
  console.log('--- offline map files ---');
  const crypto = require('crypto');
  const bad = [];
  let n = 0, bytes = 0;
  for (const [rel, f] of Object.entries(offline.files)) {
    const p = path.join(ROOT, rel);
    n++;
    if (!fs.existsSync(p)) { bad.push(rel + ': missing'); continue; }
    const buf = bundle.readServed(p);
    bytes += buf.length;
    if (buf.length !== f.bytes) bad.push(`${rel}: ${buf.length} bytes, the map says ${f.bytes}`);
    else if (crypto.createHash('sha256').update(buf).digest('hex') !== f.sha256) bad.push(rel + ': wrong SHA-256');
  }
  Object.entries(offline.assets || {}).forEach(([rel, f]) => {
    n++;
    const p = path.join(ROOT, rel);
    if (!fs.existsSync(p)) bad.push(rel + ': missing'); else if (f.bytes != null && bundle.readServed(p).length !== f.bytes) bad.push(`${rel}: wrong size`);
  });
  check(`all ${n} files of the offline map exist with the right size and SHA-256 (${(bytes / 1e6).toFixed(0)} MB hashed)`, bad.length === 0, bad.slice(0, 6));
  const unknownRefs = [];
  Object.entries(offline.subjects).forEach(([id, s]) => {
    (s.files || []).forEach(f => { if (!offline.files[f]) unknownRefs.push(id + ' -> ' + f); });
    (s.assets || []).forEach(f => { if (!offline.files[f] && !(offline.assets || {})[f]) unknownRefs.push(id + ' -> ' + f); });
  });
  check('every file a subject needs is described in the map', unknownRefs.length === 0, unknownRefs.slice(0, 6));

  // ---- 4: lazy.html
  console.log('--- the start page ---');
  const lazyHtml = fs.readFileSync(path.join(ROOT, 'lazy.html'), 'utf8');
  const scripts = [...lazyHtml.matchAll(/<script[^>]*\ssrc="([^"]+)"/g)].map(m => m[1].split('?')[0]);
  const shell = new Set(bundle.plan().files.keys());
  const lazyManifest = json('content/lazy_manifest.json');
  const reachable = rel => shell.has('site/' + rel) || !!offline.files[rel] || !!(offline.assets || {})[rel] || !!(lazyManifest.files || {})[rel];
  const lost = scripts.filter(s => !reachable(s));
  check(`every one of the ${scripts.length} scripts lazy.html names is in the app's shell or downloadable`, lost.length === 0, lost);

  // ---- 5: the app holds what the website would produce now
  console.log('--- the app\'s bundled files ---');
  if (!HAVE_APP) {
    console.log('SKIP  the app folder is not here (' + ASSETS + '): the bundled shell, catalog, question bank and covers were not compared. Run this on the PC that has SpaceBook App.');
  } else {
    const planned = bundle.plan();
    check('the shell is consistent with the website (every ?v= hash is the file\'s own)', planned.problems.length === 0, planned.problems);
    const d = bundle.diff(planned, ASSETS, path.join(APP, 'app', 'src', 'test', 'resources'));
    check(`the app's shell (${[...planned.files.keys()].filter(k => k.startsWith('site/')).length} files), catalog, question bank (${planned.mcq.kept} questions), test list and manifest and the golden test files (events contract, locator) are what the website produces now`,
      d.missing.length + d.changed.length + d.extra.length === 0, { missing: d.missing.slice(0, 6), changed: d.changed.slice(0, 6), leftover: d.extra.slice(0, 6) });
    const mcqApp = fs.existsSync(path.join(ASSETS, 'mcq_bank.json')) ? JSON.parse(fs.readFileSync(path.join(ASSETS, 'mcq_bank.json'), 'utf8')) : null;
    const mcqWeb = JSON.parse(planned.mcq.text);
    check(`the app's offline question bank is the Web's (${mcqWeb.q.length} questions, ${mcqWeb.sub.length} subjects)`, !!mcqApp && mcqApp.q.length === mcqWeb.q.length && JSON.stringify(mcqApp.sub) === JSON.stringify(mcqWeb.sub), mcqApp ? { app: mcqApp.q.length, web: mcqWeb.q.length } : 'missing');
    // covers by name
    const src = fs.readFileSync(path.join(ROOT, 'js', 'app.js'), 'utf8');
    const cm = /const coverPageMap = \{([\s\S]*?)\n  \};/.exec(src);
    const want = new Set();
    if (cm) for (const x of cm[1].matchAll(/"([^"]+)"\s*:\s*"([^"]+)"/g)) if (fs.existsSync(path.join(ROOT, 'covers', x[2]))) want.add(x[1] + '.webp');
    for (let k = 1; k <= 12; k++) if (fs.existsSync(path.join(ROOT, 'covers', 'Classes Cards', 'Another-Look', k + '.png'))) want.add('class-cls' + k + '.webp');
    const have = new Set(fs.existsSync(path.join(ASSETS, 'covers')) ? fs.readdirSync(path.join(ASSETS, 'covers')) : []);
    const miss = [...want].filter(x => !have.has(x)), extra = [...have].filter(x => !want.has(x));
    check(`the app carries the ${want.size} covers the website shows (by name)`, miss.length === 0 && extra.length === 0, { missing: miss.slice(0, 6), extra: extra.slice(0, 6) });
  }

  console.log(`---\ndata parity: ${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
