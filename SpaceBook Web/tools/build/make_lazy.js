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

const files = [], containers = new Set(), skipped = [];
for (const m of tags) {
  const src = m[1];
  if (!/^js\//.test(src) || /^js\/core\//.test(src) || eager.has(src.replace(/^js\//, '')) || overlaySet.has(src)) continue;
  const code = fs.readFileSync(path.join(ROOT, src), 'utf8');
  if (/^function\s+[A-Za-z_$]/m.test(code)) continue;                    // has behaviour: stays eager
  const ctx = vm.createContext({ console: { log() {}, warn() {}, error() {} }, setTimeout() {}, clearTimeout() {} });
  vm.runInContext('globalThis.window = globalThis; globalThis.self = globalThis;', ctx);
  const before = new Set(Object.keys(ctx));
  const names = [];
  const tx = code.replace(/^(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/gm, (all, n) => { names.push(n); return 'globalThis.' + n + ' ='; });
  try { vm.runInContext(tx, ctx, { timeout: 60000, filename: src }); } catch (e) { skipped.push([src, 'needs other scripts: ' + String(e.message).slice(0, 60)]); continue; }
  const defined = Object.keys(ctx).filter(k => !before.has(k));
  const keys = {}, stubs = [];
  let behaviour = null;
  for (const k of defined) {
    if (/^CLS\d+_(BOOKS|SOLUTIONS)$/.test(k)) {
      containers.add(k);
      if (/_BOOKS$/.test(k)) keys[k] = Object.keys(ctx[k]);
      continue;
    }
    const kd = kind(ctx[k]);
    if (kd === 'array' || kd === 'object') { if (holdsFunction(ctx[k])) behaviour = k + ' (holds functions)'; stubs.push({ name: k, kind: kd }); }
    else if (kd === 'function' && !privateHelpers.has(k)) { behaviour = k; }    // a public function: other scripts may call it before the file loads
    // other small values (numbers, flags) and the private helpers load with the file; nothing waits for them
  }
  if (behaviour) { skipped.push([src, 'defines ' + behaviour + ' (behaviour, stays eager)']); continue; }
  if (!stubs.length && !Object.keys(keys).length) { skipped.push([src, 'defines no array/object global and fills no book container']); continue; }
  files.push({ src, bytes: Buffer.byteLength(code), sha256: crypto.createHash('sha256').update(code).digest('hex'), stubs, keys });
}
// a name defined by two lazy files (other than the shared containers) would be ambiguous: keep both eager
const seen = {}; const clash = new Set();
files.forEach(f => f.stubs.forEach(s => { (seen[s.name] = seen[s.name] || []).push(f.src); }));
Object.keys(seen).filter(n => seen[n].length > 1).forEach(n => seen[n].forEach(s => clash.add(s)));
const lazy = files.filter(f => !clash.has(f.src));
// overlays follow their parent; an overlay whose parent is not lazy stays in the page
const attached = new Set();
for (const f of lazy) {
  f.after = (overlayCfg[f.src] || []).map(o => {
    const code = fs.readFileSync(path.join(ROOT, o), 'utf8');
    attached.add(o);
    return { src: o, bytes: Buffer.byteLength(code), sha256: crypto.createHash('sha256').update(code).digest('hex') };
  });
}
const orphan = [...overlaySet].filter(o => !attached.has(o));
clash.forEach(s => skipped.push([s, 'a global name is defined by more than one file']));

const manifest = { schema: 'spacebook.lazy/1', generated: new Date().toISOString().slice(0, 10), containers: [...containers].sort(), files: lazy };
const CHECK = args.includes('--check');                               // --check: write nothing, exit 1 if the committed files are stale
const stale = [];
function write(file, text) {
  if (CHECK) { if (!fs.existsSync(file) || fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n') !== text.replace(/\r\n/g, '\n')) stale.push(path.relative(ROOT, file)); return; }
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, text);
}
write(path.join(ROOT, 'content', 'lazy_manifest.json'), JSON.stringify(manifest, null, 1) + '\n');

const drop = new Set(lazy.map(f => f.src).concat([...attached]));
let out = html.replace(/<script\b[^>]*\bsrc="([^"?]+)(\?[^"]*)?"[^>]*><\/script>[ \t]*\r?\n?/g, (all, src) => (drop.has(src) ? '' : all));
const first = out.search(/<script\b[^>]*\bsrc=/);
const inject = '  <script>window.SB_LAZY_MANIFEST = ' + JSON.stringify({ containers: manifest.containers, files: lazy.map(f => ({ src: f.src, bytes: f.bytes, stubs: f.stubs, keys: f.keys, after: f.after.map(a => a.src) })) }) + ';</script>\n  <script src="js/core/lazy.js"></script>\n';
out = out.slice(0, first) + inject + out.slice(first);
out = out.replace('<title>', '<title>[lazy] ').replace(/<head>/, '<head>\n  <!-- GENERATED by tools/build/make_lazy.js from index.html: do not edit -->');
write(OUT, out);

const total = lazy.reduce((n, f) => n + f.bytes, 0);
console.log('lazy files:', lazy.length, '(' + (total / 1e6).toFixed(1) + ' MB not loaded at start); containers:', manifest.containers.length);
console.log('overlays run after their parent:', attached.size + (orphan.length ? ' (not attached, stay in the page: ' + orphan.join(', ') + ')' : ''));
console.log('stays eager:', skipped.length, 'data-like files');
skipped.slice(0, 12).forEach(s => console.log('  ' + s[0] + ' - ' + s[1]));
if (CHECK) {
  if (stale.length) { console.log('STALE: ' + stale.join(', ') + ' - run: node tools/build/make_lazy.js'); process.exit(1); }
  console.log('lazy.html and content/lazy_manifest.json are up to date');
} else console.log('wrote ' + path.relative(ROOT, OUT) + ' (' + (Buffer.byteLength(out) / 1024).toFixed(0) + ' KB), content/lazy_manifest.json');
