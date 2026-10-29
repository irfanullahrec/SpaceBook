'use strict';
/* Flags PHP 8-only syntax/functions in api/ and manage/ (the live host ran PHP 7.4.33 on 2026-10-19) and runs `php -l` if available.
 * Heuristic, regex based: comments and string literals are stripped first.   node tools/php74_lint.js */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const API = path.resolve(__dirname, '..', 'api');
const NS = '[A-Za-z_\\\\]+';          // a type name, optionally namespaced
const RULES = [
  [/\bmatch\s*\(/, 'match expression (PHP 8.0)'],
  [/\b(str_contains|str_starts_with|str_ends_with|array_is_list|fdiv|get_debug_type|get_resource_id)\s*\(/, 'PHP 8 function'],
  [/\?->/, 'nullsafe operator (PHP 8.0)'],
  [/#\[/, 'attribute (PHP 8.0)'],
  [/\bfunction\s+__construct\s*\([^)]*\b(public|private|protected|readonly)\s/, 'constructor promotion (PHP 8.0)'],
  [new RegExp('\\)\\s*:\\s*(mixed|static|never|\\??' + NS + '\\s*\\|\\s*' + NS + ')'), 'mixed/static/never/union return type (PHP 8)'],
  [new RegExp('\\bfunction\\s+\\w+\\s*\\([^)]*\\b' + NS + '\\s*\\|\\s*' + NS + '\\s+\\$'), 'union parameter type (PHP 8.0)'],
  [/\benum\s+\w+/, 'enum (PHP 8.1)'],
  [/\breadonly\b/, 'readonly (PHP 8.1)'],
  [/[(,]\s*[a-z_]\w*\s*:\s*[^:\s]/, 'possible named argument (PHP 8.0)'],
];
function strip(src) {
  return src.replace(/\/\*[\s\S]*?\*\//g, m => m.replace(/[^\n]/g, ' '))
    .replace(/'(?:[^'\\\n]|\\.)*'/g, "''").replace(/"(?:[^"\\\n]|\\.)*"/g, '""')
    .replace(/\/\/.*$/gm, '').replace(/^\s*#(?!\[).*$/gm, '');
}
function walk(d) { return fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(d, e.name)) : e.name.endsWith('.php') ? [path.join(d, e.name)] : []); }
let bad = 0;
const files = walk(API).concat(walk(path.resolve(__dirname, '..', 'manage')));
for (const f of files) {
  strip(fs.readFileSync(f, 'utf8')).split('\n').forEach((line, i) => {
    if (/\?\s.*:\s/.test(line) && !/^\s*(case|default)\b/.test(line) && RULES[RULES.length - 1][0].test(line) && /\?[^?]*\b\w+\s*:/.test(line)) return; // ternary, not a named argument
    for (const [re, why] of RULES) if (re.test(line)) { bad++; console.log(`${path.relative(path.resolve(__dirname, '..'), f)}:${i + 1}: ${why}`); }
  });
}
let syntax = 'php not found, skipped';
for (const exe of [process.env.PHP, 'php', 'C:/xampp/php/php.exe'].filter(Boolean)) {
  const r = cp.spawnSync(exe, ['-v']); if (r.status !== 0) continue;
  syntax = 'php -l (' + String(r.stdout).split('\n')[0] + ')';
  for (const f of files) { const l = cp.spawnSync(exe, ['-l', f]); if (l.status !== 0) { bad++; console.log(String(l.stdout) + String(l.stderr)); } }
  break;
}
console.log(`php74_lint: ${files.length} files, ${bad} problems; syntax check: ${syntax}`);
process.exit(bad ? 1 : 0);
