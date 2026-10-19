'use strict';
/* Move files out of the working folder into the archive, never delete (Phase 10, docs/CLEANUP_LOG.md).
 *   node tools/cleanup/archive.js --plan tools/cleanup/plan_2026-10-20.json              dry run: what would move, sizes
 *   node tools/cleanup/archive.js --plan tools/cleanup/plan_2026-10-20.json --execute    do it
 * A plan lists paths relative to "SpaceBook Web" (a file or a folder). For every file: size and SHA-256 are written to
 * <archive>/ARCHIVE_LOG_<plan name>.csv BEFORE it moves; it is then moved (renamed, same drive) to <archive>/SpaceBook Web/<same relative path>;
 * the destination must exist with the same size, else the run stops. Nothing is overwritten (an existing destination aborts), nothing is
 * deleted; an emptied folder stays as it is. Restore = move the same relative path back. The archive is outside git (SpaceBook_Archive/
 * is in the root .gitignore). Tracked files are refused here: moves of tracked files are committed separately by hand. */
const fs = require('fs'), path = require('path'), crypto = require('crypto'), { spawnSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..', '..');                       // .../SpaceBook Web
const ARCHIVE = path.resolve(ROOT, '..', 'SpaceBook_Archive');
const args = process.argv.slice(2);
const planFile = args[args.indexOf('--plan') + 1];
const EXECUTE = args.includes('--execute');
if (!planFile || !fs.existsSync(planFile)) { console.log('usage: node tools/cleanup/archive.js --plan <plan.json> [--execute]'); process.exit(2); }
const plan = JSON.parse(fs.readFileSync(planFile, 'utf8'));
const planName = path.basename(planFile, '.json');

function* walk(p) {
  const st = fs.lstatSync(p);
  if (st.isDirectory()) { for (const n of fs.readdirSync(p)) yield* walk(path.join(p, n)); }
  else if (st.isFile()) yield p;
}
const sha = file => new Promise((res, rej) => { const h = crypto.createHash('sha256'); fs.createReadStream(file).on('data', d => h.update(d)).on('end', () => res(h.digest('hex'))).on('error', rej); });
const tracked = new Set(spawnSync('git', ['ls-files', '-z'], { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 28 }).stdout.split('\0').filter(Boolean).map(p => p.replace(/^SpaceBook Web\//, '')));

(async () => {
  const files = [];
  for (const rel of plan.paths) {
    const abs = path.join(ROOT, rel);
    if (!fs.existsSync(abs)) { console.log('missing (skipped): ' + rel); continue; }
    for (const f of walk(abs)) files.push(path.relative(ROOT, f).replace(/\\/g, '/'));
  }
  const refused = files.filter(f => tracked.has(f));
  if (refused.length) { console.log('REFUSED: ' + refused.length + ' tracked file(s), e.g. ' + refused[0] + ' (move tracked files by hand and commit separately)'); process.exit(1); }
  const total = files.reduce((n, f) => n + fs.statSync(path.join(ROOT, f)).size, 0);
  console.log(`${plan.paths.length} paths, ${files.length} files, ${(total / 1e6).toFixed(0)} MB -> ${path.join(ARCHIVE, 'SpaceBook Web')}`);
  if (!EXECUTE) { console.log('dry run: nothing moved (add --execute)'); return; }
  fs.mkdirSync(ARCHIVE, { recursive: true });
  const logFile = path.join(ARCHIVE, 'ARCHIVE_LOG_' + planName + '.csv');
  const log = fs.createWriteStream(logFile, { flags: 'a' });
  if (!fs.existsSync(logFile) || fs.statSync(logFile).size === 0) log.write('path,bytes,sha256,moved_at\n');
  let n = 0, moved = 0;
  for (const rel of files) {
    const src = path.join(ROOT, rel), dst = path.join(ARCHIVE, 'SpaceBook Web', rel);
    if (fs.existsSync(dst)) { console.log('STOP: destination exists ' + dst); process.exit(1); }
    const size = fs.statSync(src).size, hash = await sha(src);
    log.write(JSON.stringify(rel) + ',' + size + ',' + hash + ',' + new Date().toISOString() + '\n');
    fs.mkdirSync(path.dirname(dst), { recursive: true });
    fs.renameSync(src, dst);
    if (!fs.existsSync(dst) || fs.statSync(dst).size !== size) { console.log('STOP: ' + rel + ' did not arrive intact'); process.exit(1); }
    moved += size; n++;
    if (n % 1000 === 0) console.log(n + ' / ' + files.length + ' files, ' + (moved / 1e6).toFixed(0) + ' MB');
  }
  log.end();
  console.log(`moved ${n} files (${(moved / 1e6).toFixed(0)} MB); log: ${logFile}`);
})().catch(e => { console.log('CRASH', e.stack); process.exit(1); });
