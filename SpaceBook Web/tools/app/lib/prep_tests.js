'use strict';
/* The competitive tests a student can prepare for (PST, CT, SST ...), as the Android app lists them (assets/prep_tests.json):
 *   [{id, title, fullName, scale, emoji, color}, ...]  taken from COMPETITIVE_TESTS_DATA in js/app.js.
 * Moved here from the app's own tools/ (2026-10-23): the app's data is generated from the website by tools/app/sync_app.js. Dev-only. */
const fs = require('fs');
const vm = require('vm');

function build(appJsPath) {
  const text = fs.readFileSync(appJsPath, 'utf8');
  const start = text.indexOf('const COMPETITIVE_TESTS_DATA = [');
  if (start < 0) throw new Error('COMPETITIVE_TESTS_DATA not found in ' + appJsPath);
  const end = text.indexOf('\n];', start);
  const data = vm.runInNewContext('(' + text.slice(start + 'const COMPETITIVE_TESTS_DATA ='.length, end + 2) + ')', {});
  const tests = data.map(t => ({ id: t.id, title: t.title, fullName: t.fullName || '', scale: t.scale || '', emoji: t.emoji || '📝', color: t.color || '#5b4bff' }));
  return { text: JSON.stringify(tests), tests };
}

module.exports = { build };
