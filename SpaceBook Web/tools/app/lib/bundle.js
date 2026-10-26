'use strict';
/* What the Android app bundles from the website, as a pure function of the website's files: plan() says, for every file under the app's
 * assets folder that is generated, where it comes from (a file of this folder, or bytes made here). tools/app/sync_app.js writes the plan
 * into the app; tools/parity/data_parity.js compares the app's assets with it ("stale" = the app holds something the website would not
 * produce now). Nothing here is edited by hand in the app afterwards.
 *
 *   site/**                the shell: lazy.html and every file content/sw_version.js lists, the three content/ indexes the app needs, site-index.json
 *   app_catalog.json       classes, subjects, chapters (content/app_catalog.json, made by tools/build/make_app_catalog.js)
 *   mcq_bank.json          the offline question bank (lib/mcq.js)
 *   prep_tests.json        the competitive tests (lib/prep_tests.js)
 *   sync_manifest.json     what the above are made of (hashes, the service worker version), no dates, so it only changes with the content
 * Test resources (tests/parity/*.json -> the app's src/test/resources/parity/): the golden files both platforms are checked against, so the
 * app's unit tests hold the website's contract, not a copy somebody typed.
 * The covers (assets/covers/*.webp) are made by tools/app/make_app_covers.py and checked by name only (image encoders differ between machines).
 * Not generated, owned by the app: reader_bridge.js, reader_mobile.css, prep_summary.js. Dev-only, never deployed. */
const fs = require('fs'), path = require('path'), vm = require('vm'), crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..', '..', '..');
const sha256 = buf => crypto.createHash('sha256').update(buf).digest('hex');

// What the site serves is what git stores: LF line ends. A working folder on Windows may hold CRLF copies of text files (a Python script
// wrote them, or the checkout was made with autocrlf), which must not change a hash or a size, so text files are read with LF.
const TEXT = /\.(js|css|html|json|txt|svg|webmanifest|csv|md)$/i;
function readServed(file) {
  const buf = fs.readFileSync(file);
  if (!TEXT.test(file) || buf.indexOf(13) < 0) return buf;
  return Buffer.from(buf.toString('latin1').replace(/\r\n/g, '\n'), 'latin1');
}

function swVersion() {
  const ctx = { self: {} };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(ROOT, 'content', 'sw_version.js'), 'utf8'), ctx);
  const sw = ctx.self.SB_SW;
  if (!sw || !Array.isArray(sw.shell)) throw new Error('content/sw_version.js has no shell list');
  return sw;
}

// Shell entries are "path" or "path?v=<12 hex of the file's own sha256>": the app serves a bundled file only for that hash.
function shellEntries() {
  const sw = swVersion();
  const entries = ['lazy.html', 'logo_tuitionhub_trans.png'].concat(sw.shell, ['content/offline_map.json', 'content/lazy_manifest.json', 'content/search/index.json']);
  return { sw, entries };
}

// The golden files of tests/parity that the app's unit tests read. The app's copy is generated; nothing in it is edited by hand.
const TEST_RESOURCES = ['events_contract.json', 'locator_golden.json', 'feed_contract.json'];

function plan() {
  const files = new Map();
  const tests = new Map();
  for (const f of TEST_RESOURCES) {
    const from = path.join(ROOT, 'tests', 'parity', f);
    if (!fs.existsSync(from)) continue;
    const b = readServed(from);
    tests.set('parity/' + f, { bytes: b, sha256: sha256(b) });
  }
  const problems = [];
  const { sw, entries } = shellEntries();
  const index = { schema: 'spacebook.app-shell/1', files: {} };
  const siteLines = [];
  for (const entry of entries) {
    const [rel, query] = entry.split('?');
    const m = /^v=([0-9a-f]+)$/.exec(query || '');
    const v = m ? m[1] : '';
    const from = path.join(ROOT, rel);
    if (!fs.existsSync(from)) { problems.push('shell file missing: ' + rel); continue; }
    const buf = readServed(from);
    const h = sha256(buf);
    if (v && !h.startsWith(v)) problems.push(`shell file ${rel} does not match its ?v=${v} (its content hash is ${h.slice(0, 12)}): the generated files are stale, run node tools/build/all.js from a clean checkout`);
    index.files[rel] = v;
    files.set('site/' + rel, { bytes: buf, sha256: h, from });
    siteLines.push(rel + ':' + h);
  }
  // The files of Create Test, Ask SpaceBook and Grammar Stats (the question bank, the tutor's passages, the grammar), and the search files of the subjects the
  // tutor reads by chapter (Class 11 and the ones without passages): requested as name?v=<12 hex of their hash>, so the app serves them from its own copy and
  // the three features work offline from the first start. The index of each folder is asked for without a version.
  for (const dir of ['content/testbank', 'content/assistant', 'content/grammar']) {
    const abs = path.join(ROOT, dir);
    if (!fs.existsSync(abs)) { problems.push(dir + ' is missing: run node tools/build/all.js'); continue; }
    for (const f of fs.readdirSync(abs).sort()) {
      const rel = dir + '/' + f, from = path.join(abs, f), buf = readServed(from), h = sha256(buf);
      index.files[rel] = f === 'index.json' ? '' : h.slice(0, 12);
      files.set('site/' + rel, { bytes: buf, sha256: h, from });
      siteLines.push(rel + ':' + h);
    }
  }
  try {
    const sIdx = JSON.parse(readServed(path.join(ROOT, 'content', 'search', 'index.json')).toString('utf8'));
    const aIdx = JSON.parse(readServed(path.join(ROOT, 'content', 'assistant', 'index.json')).toString('utf8'));
    for (const id of Object.keys(sIdx.subjects).sort()) {
      const meta = sIdx.subjects[id];
      if (meta.classId !== 'cls11' && aIdx.subjects[id]) continue;
      const rel = 'content/search/' + id + '.json', from = path.join(ROOT, rel);
      if (!fs.existsSync(from)) { problems.push('search file missing: ' + rel); continue; }
      const buf = readServed(from), h = sha256(buf);
      index.files[rel] = h.slice(0, 12);
      files.set('site/' + rel, { bytes: buf, sha256: h, from });
      siteLines.push(rel + ':' + h);
    }
  } catch (e) { problems.push('the search or tutor index could not be read: ' + e.message); }
  files.set('site/site-index.json', { bytes: Buffer.from(JSON.stringify(index)) });

  const catalogFrom = path.join(ROOT, 'content', 'app_catalog.json');
  if (!fs.existsSync(catalogFrom)) problems.push('content/app_catalog.json is missing: run node tools/build/make_app_catalog.js');
  else { const b = readServed(catalogFrom); files.set('app_catalog.json', { bytes: b, sha256: sha256(b), from: catalogFrom }); }

  const mcq = require('./mcq').build(path.join(ROOT, 'js', 'test_prep_bank.js'));
  files.set('mcq_bank.json', { bytes: Buffer.from(mcq.text) });
  const prep = require('./prep_tests').build(path.join(ROOT, 'js', 'app.js'));
  files.set('prep_tests.json', { bytes: Buffer.from(prep.text) });

  const manifest = {
    schema: 'spacebook.app-sync/1',
    serviceWorker: sw.version,
    site: { files: siteLines.length, sha256: sha256(Buffer.from(siteLines.sort().join('\n'))) },
    generated: {},
  };
  for (const name of ['app_catalog.json', 'mcq_bank.json', 'prep_tests.json']) {
    const f = files.get(name);
    if (f) manifest.generated[name] = f.sha256 || sha256(f.bytes);
  }
  files.set('sync_manifest.json', { bytes: Buffer.from(JSON.stringify(manifest, null, 1) + '\n') });
  for (const f of files.values()) if (!f.sha256) f.sha256 = sha256(f.bytes);
  return { files, tests, problems, mcq, prep, sw };
}

const bytesOf = f => (f.bytes ? f.bytes : readServed(f.from));

// Compares a plan with the app's assets folder. Returns {missing, changed, extra} (relative paths under assets/).
function diff(planned, assetsDir, testResDir) {
  const missing = [], changed = [], extra = [];
  if (testResDir) {
    for (const [rel, f] of planned.tests) {
      const p = path.join(testResDir, rel);
      if (!fs.existsSync(p)) { missing.push('test resource ' + rel); continue; }
      if (sha256(fs.readFileSync(p)) !== f.sha256) changed.push('test resource ' + rel);
    }
  }
  for (const [rel, f] of planned.files) {
    const p = path.join(assetsDir, rel);
    if (!fs.existsSync(p)) { missing.push(rel); continue; }
    const have = fs.readFileSync(p);
    if (have.length !== bytesOf(f).length || sha256(have) !== f.sha256) changed.push(rel);
  }
  const siteDir = path.join(assetsDir, 'site');
  (function walk(dir, rel) {
    if (!fs.existsSync(dir)) return;
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const r = rel ? rel + '/' + e.name : e.name;
      if (e.isDirectory()) walk(path.join(dir, e.name), r);
      else if (!planned.files.has('site/' + r)) extra.push('site/' + r);
    }
  })(siteDir, '');
  return { missing, changed, extra };
}

module.exports = { ROOT, plan, diff, bytesOf, sha256, swVersion, readServed };
