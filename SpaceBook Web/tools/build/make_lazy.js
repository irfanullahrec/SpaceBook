'use strict';
/* Builds the lazy-loading page.   node tools/build/make_lazy.js [--src index.html] [--eager a.js,b.js] [--out lazy.html] [--check]
 *
 * Reads index.html, picks the big self-contained data files (they run alone in an empty context, see probe_files.js, and
 * define named arrays/objects or fill a CLSn_BOOKS container), drops their <script> tags, and puts js/core/lazy.js with an
 * inline manifest in front of the other scripts. Writes lazy.html and content/lazy_manifest.json.
 * Files listed in tools/build/lazy_eager.json (files that were found to be needed at page load anyway) stay eager. */
const fs = require('fs'), path = require('path'), vm = require('vm'), crypto = require('crypto');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : args[i + 1]; };
const OUT = path.join(ROOT, opt('out', 'lazy.html'));
const eagerFile = path.join(__dirname, 'lazy_eager.json');
const eager = new Set((fs.existsSync(eagerFile) ? JSON.parse(fs.readFileSync(eagerFile, 'utf8')).files : []).concat((opt('eager', '') || '').split(',').filter(Boolean)).map(f => f.replace(/^js\//, '')));

const privateHelpers = new Set((fs.existsSync(eagerFile) ? JSON.parse(fs.readFileSync(eagerFile, 'utf8')).privateHelpers : []) || []);
const overlayCfg = JSON.parse(fs.readFileSync(path.join(__dirname, 'lazy_overlays.json'), 'utf8')).after || {};
const overlaySet = new Set([].concat(...Object.values(overlayCfg)));
const html = fs.readFileSync(path.join(ROOT, opt('src', 'index.html')), 'utf8');      // --src: the eager page to derive the lazy one from
const tags = [...html.matchAll(/<script\b[^>]*\bsrc="([^"?]+)(\?[^"]*)?"[^>]*><\/script>[ \t]*\r?\n?/g)];
const kind = v => Array.isArray(v) ? 'array' : (v && typeof v === 'object') ? 'object' : typeof v;
// data contains no functions: a global that holds one (an API object, a reader's helpers) belongs to a script with behaviour
function holdsFunction(v, seen = new Set(), budget = { n: 0 }) {
  if (typeof v === 'function') return true;
  if (!v || typeof v !== 'object' || seen.has(v)) return false;
  seen.add(v);
  if (++budget.n > 5e6) return true;                                 // too big to check: treat as code
  for (const k of Object.keys(v)) { const d = Object.getOwnPropertyDescriptor(v, k); if (d.get || d.set) return true; if (holdsFunction(d.value, seen, budget)) return true; }
  return false;
}

// sizes and hashes describe the committed form (LF): a Windows working copy with CRLF line ends must give the same manifest as the CI checkout
const read = file => fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
const CONTAINER = /^(CLS\d+_(BOOKS|SOLUTIONS)|CLASS11_BOOKS)$/;
const files = [], containers = new Set(), skipped = [];
for (const m of tags) {
  const src = m[1];
  if (!/^js\//.test(src) || /^js\/core\//.test(src) || eager.has(src.replace(/^js\//, '')) || overlaySet.has(src)) continue;
  const code = read(path.join(ROOT, src));
  const ctx = vm.createContext({ console: { log() {}, warn() {}, error() {} }, setTimeout() {}, clearTimeout() {} });
  vm.runInContext('globalThis.window = globalThis; globalThis.self = globalThis; globalThis.DATA = {};', ctx);   // DATA: the registry the Class 9/10 data files extend (Object.assign(DATA, {...}))
  const before = new Set(Object.keys(ctx));
  const names = [];
  const tx = code.replace(/^(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/gm, (all, n) => { names.push(n); return 'globalThis.' + n + ' ='; });
  try { vm.runInContext(tx, ctx, { timeout: 60000, filename: src }); } catch (e) { skipped.push([src, 'needs other scripts: ' + String(e.message).slice(0, 60)]); continue; }
  const defined = Object.keys(ctx).filter(k => !before.has(k));
  const keys = {}, stubs = [], fns = [];
  const dataKeys = Object.keys(ctx.DATA);                                    // keys this file adds to DATA: accessors on DATA until it loads
  let behaviour = null;
  for (const k of defined) {
    if (CONTAINER.test(k)) {
      containers.add(k);
      if (/_BOOKS$/.test(k)) keys[k] = Object.keys(ctx[k]);
      continue;
    }
    if (privateHelpers.has(k)) continue;                                  // only its own file uses it: loads with the file
    const kd = kind(ctx[k]);
    if (kd === 'array' || kd === 'object') { if (!/_data\.js$/.test(src) && holdsFunction(ctx[k])) behaviour = (behaviour ? behaviour + ', ' : '') + k + ' (holds functions)'; stubs.push({ name: k, kind: kd }); }
    else if (kd === 'function') fns.push(k);          // a public function: other scripts may call it before the file loads, so it gets a forwarding stub
    // other small values (numbers, flags) and the private helpers load with the file; nothing waits for them
  }
  if (behaviour) { skipped.push([src, 'defines ' + behaviour + ' (behaviour, stays eager)']); continue; }
  if (!stubs.length && !Object.keys(keys).length && !dataKeys.length) { skipped.push([src, 'defines no array/object global and fills no book container']); continue; }
  files.push({ src, bytes: Buffer.byteLength(code), sha256: crypto.createHash('sha256').update(code).digest('hex'), stubs, keys, fns, dataKeys });
}
// Two files that set the same key of DATA (data_eng.js, then english_10_data.js overwrites eng10Chapters) form one unit: the later one runs
// right after the earlier one in the original order and the unit answers for the names of both, so the final value is the same as in the
// normal page. (They cannot be separate lazy files: whichever loaded first would decide the value.)
{
  const order = new Map(tags.map((m, i) => [m[1], i])), byKey = {};
  files.forEach(f => f.dataKeys.forEach(k => { (byKey[k] = byKey[k] || []).push(f); }));
  for (const group of Object.values(byKey).filter(g => g.length > 1)) {
    const [parent, ...rest] = [...new Set(group)].sort((a, b) => order.get(a.src) - order.get(b.src));
    for (const f of rest) {
      if (f.merged) continue;
      f.merged = true;
      parent.also = (parent.also || []).concat({ src: f.src, bytes: f.bytes, sha256: f.sha256 });
      parent.bytes += f.bytes;
      parent.stubs.push(...f.stubs); parent.fns.push(...f.fns);
      f.dataKeys.forEach(k => { if (!parent.dataKeys.includes(k)) parent.dataKeys.push(k); });
      Object.keys(f.keys).forEach(c => { parent.keys[c] = (parent.keys[c] || []).concat(f.keys[c]); });
    }
  }
  files.forEach(f => { f.also = f.also || []; });
  files.splice(0, files.length, ...files.filter(f => !f.merged));
}
// a name defined by two lazy files (other than the shared containers) would be ambiguous: keep both eager
const seen = {}; const clash = new Set();
files.forEach(f => f.stubs.map(s => s.name).concat(f.fns, f.dataKeys.map(k => 'DATA.' + k)).forEach(n => { (seen[n] = seen[n] || []).push(f.src); }));
Object.keys(seen).filter(n => seen[n].length > 1).forEach(n => { if (args.includes('--explain')) console.log('  clash: ' + n + ' defined by ' + seen[n].join(', ')); seen[n].forEach(s => clash.add(s)); });
let lazy = files.filter(f => !clash.has(f.src));
// A lazy file's functions are stood in for until it loads, and loading replaces whatever is in the global then. If another script
// reassigns one of them (wraps it), the wrapper would be lost: that file stays eager. Only scripts that are not themselves lazy and
// are smaller than 2 MB can hold behaviour; data files are skipped for speed.
const fnOwner = {}; lazy.forEach(f => {
  f.fns.forEach(n => { fnOwner[n] = f.src; });
  (overlayCfg[f.src] || []).forEach(o => { for (const m of read(path.join(ROOT, o)).matchAll(/^(?:async\s+)?function\s+([A-Za-z_$][\w$]*)/gm)) fnOwner[m[1]] = f.src; });
});
const fnNames = Object.keys(fnOwner), wrapped = new Map();
if (fnNames.length) {
  const re = new RegExp('(?:^|[^\\w$.])(?:window\\.|globalThis\\.)?(' + fnNames.map(n => n.replace(/[$]/g, '\\$&')).join('|') + ')\\s*=(?!=)', 'gm');
  const lazySrc = new Set(lazy.map(f => f.src).concat(...lazy.map(f => f.also.map(a => a.src))));
  for (const m of tags) {
    const src = m[1];
    if (lazySrc.has(src) || !/^js\//.test(src)) continue;
    const full = path.join(ROOT, src);
    if (!fs.existsSync(full) || fs.statSync(full).size > 2e6) continue;
    for (const x of read(full).matchAll(re)) if (fnOwner[x[1]] !== src && !(overlayCfg[fnOwner[x[1]]] || []).includes(src)) wrapped.set(fnOwner[x[1]], (wrapped.get(fnOwner[x[1]]) || []).concat(x[1] + ' in ' + src));
  }
}
wrapped.forEach((why, owner) => skipped.push([owner, 'a script reassigns its function(s): ' + [...new Set(why)].slice(0, 3).join('; ')]));
lazy = lazy.filter(f => !wrapped.has(f.src));
// overlays follow their parent; an overlay whose parent is not lazy stays in the page
const attached = new Set();
for (const f of lazy) {
  f.after = (overlayCfg[f.src] || []).map(o => {
    const code = read(path.join(ROOT, o));
    attached.add(o);
    // functions an overlay declares (physics_10_source_data.js: renderClass10PhysicsWorkedExamples...) get forwarding stubs that load the parent
    for (const m of code.matchAll(/^(?:async\s+)?function\s+([A-Za-z_$][\w$]*)/gm)) if (!f.fns.includes(m[1])) f.fns.push(m[1]);
    return { src: o, bytes: Buffer.byteLength(code), sha256: crypto.createHash('sha256').update(code).digest('hex') };
  });
}
const orphan = [...overlaySet].filter(o => !attached.has(o));
clash.forEach(s => skipped.push([s, 'a global name is defined by more than one file']));

const manifest = { schema: 'spacebook.lazy/1', containers: [...containers].sort(), files: lazy };
const CHECK = args.includes('--check');                               // --check: write nothing, exit 1 if the committed files are stale
const stale = [];
function write(file, text) {
  if (CHECK) { if (!fs.existsSync(file) || fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n') !== text.replace(/\r\n/g, '\n')) stale.push(path.relative(ROOT, file)); return; }
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, text);
}
write(path.join(ROOT, 'content', 'lazy_manifest.json'), JSON.stringify(manifest, null, 1) + '\n');

const drop = new Set(lazy.map(f => f.src).concat([...attached], ...lazy.map(f => f.also.map(a => a.src))));
let out = html.replace(/<script\b[^>]*\bsrc="([^"?]+)(\?[^"]*)?"[^>]*><\/script>[ \t]*\r?\n?/g, (all, src) => (drop.has(src) ? '' : all));
const first = out.search(/<script\b[^>]*\bsrc=/);
const inject = '  <script>window.SB_LAZY_MANIFEST = ' + JSON.stringify({ containers: manifest.containers, files: lazy.map(f => ({ src: f.src, bytes: f.bytes, v: f.sha256.slice(0, 12), also: f.also.map(a => ({ src: a.src, v: a.sha256.slice(0, 12) })), stubs: f.stubs, fns: f.fns, keys: f.keys, dataKeys: f.dataKeys, after: f.after.map(a => ({ src: a.src, v: a.sha256.slice(0, 12) })) })) }) + ';</script>\n  <script src="js/core/lazy.js"></script>\n';
out = out.slice(0, first) + inject + out.slice(first);
// DATA is a const of data.js, so lazy.js cannot reach it before that script has run: the keys that lazy files add to it become accessors right after
const dataTag = /(<script\b[^>]*\bsrc="js\/data\.js(?:\?[^"]*)?"[^>]*><\/script>[ \t]*\r?\n)/;
if (lazy.some(f => f.dataKeys.length)) out = out.replace(dataTag, '$1  <script>SBLazy.attachData(DATA);</script>\n');
// Every local script and stylesheet of the lazy page is requested as file?v=<12 hex of the sha256 of its LF form>: a changed file is a
// new URL, an unchanged one may be cached for a year (deploy/spacebook.htaccess), and this page is stale (--check) the moment one changes.
const contentVersion = file => { const full = path.join(ROOT, file); return fs.existsSync(full) ? crypto.createHash('sha256').update(read(full)).digest('hex').slice(0, 12) : null; };
const versionUrl = (all, head, file, tail) => { const v = /^(?:https?:)?\/\//.test(file) ? null : contentVersion(file); return v ? head + file + '?v=' + v + tail : all; };
out = out.replace(/(<script\b[^>]*\bsrc=")([^"?]+)(?:\?[^"]*)?(")/g, (all, h, f, t) => versionUrl(all, h, f, t));
out = out.replace(/(<link\b[^>]*\bhref=")([^"?]+\.css)(?:\?[^"]*)?(")/g, (all, h, f, t) => versionUrl(all, h, f, t));
out = out.replace('<title>', '<title>[lazy] ').replace(/<head>/, '<head>\n  <!-- GENERATED by tools/build/make_lazy.js from index.html: do not edit -->');
write(OUT, out);

const total = lazy.reduce((n, f) => n + f.bytes, 0);
console.log('lazy files:', lazy.length, '(' + (total / 1e6).toFixed(1) + ' MB not loaded at start); containers:', manifest.containers.length);
console.log('functions with a forwarding stub:', lazy.reduce((n, f) => n + f.fns.length, 0), '(none of them reassigned by another script)');
console.log('overlays run after their parent:', attached.size + (orphan.length ? ' (not attached, stay in the page: ' + orphan.join(', ') + ')' : ''));
console.log('stays eager:', skipped.length, 'data-like files');
skipped.slice(0, args.includes('--explain') ? skipped.length : 12).forEach(s => console.log('  ' + s[0] + ' - ' + s[1]));   // --explain: every file that stays eager, with the reason
if (CHECK) {
  if (stale.length) { console.log('STALE: ' + stale.join(', ') + ' - run: node tools/build/make_lazy.js'); process.exit(1); }
  console.log('lazy.html and content/lazy_manifest.json are up to date');
} else console.log('wrote ' + path.relative(ROOT, OUT) + ' (' + (Buffer.byteLength(out) / 1024).toFixed(0) + ' KB), content/lazy_manifest.json');
