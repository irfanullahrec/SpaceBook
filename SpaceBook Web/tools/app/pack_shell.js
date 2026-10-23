'use strict';
/* Superseded by tools/app/sync_app.js, which packs the shell together with everything else the Android app bundles and can check that
 * the app is still in step with the website (node tools/app/sync_app.js --check). Kept so an old command line keeps working:
 *     node tools/app/pack_shell.js [<assets dir>]    ==    node tools/app/sync_app.js [--app <app repo folder>]
 * The shell's file list and hashes are made by tools/app/lib/bundle.js. Dev-only (not deployed). */
const path = require('path');
const { spawnSync } = require('child_process');
const arg = process.argv[2];
const extra = [];
if (arg) {
  // <repo>/app/src/main/assets  ->  <repo>
  const repo = path.resolve(arg, '..', '..', '..', '..');
  extra.push('--app', repo);
}
console.log('tools/app/pack_shell.js now runs tools/app/sync_app.js');
const r = spawnSync(process.execPath, [path.join(__dirname, 'sync_app.js')].concat(extra, process.argv.slice(3)), { stdio: 'inherit' });
process.exit(r.status === null ? 1 : r.status);
