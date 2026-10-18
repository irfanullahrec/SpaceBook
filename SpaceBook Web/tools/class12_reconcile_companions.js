const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const companionPath = path.join(root, 'docs/source-verification/class-12/physics-companions.json');
const sourcePath = path.join(root, 'js/phys_12_data.js');
const companions = JSON.parse(fs.readFileSync(companionPath, 'utf8'));
const continuation = companions.trimSections.find(item => item.id === '11.13');
continuation.startsAt = 'PARALLEL COMBINATION OF CAPACITORS';
continuation.title = 'Capacitor combinations (source review continues at PDF page 24)';
continuation.clearSciNote = true;
companions.trimSections = companions.trimSections.filter(item => !['11.14','11.15'].includes(item.id));
fs.writeFileSync(companionPath, JSON.stringify(companions, null, 2) + '\n');
let source = fs.readFileSync(sourcePath, 'utf8');
const marker = '// BEGIN CLASS12 FRESH AUDIT COMPANION UPSERTS';
const markerStart = source.indexOf(marker);
if (markerStart < 0) throw new Error('Physics12 companion marker missing');
const auditStart = source.indexOf('const audit = ', markerStart);
if (auditStart < 0) throw new Error('Physics12 audit data missing');
const jsonStart = auditStart + 'const audit = '.length;
const end = source.indexOf(';\r\nfor (const entry of audit.formulas)', jsonStart) >= 0
  ? source.indexOf(';\r\nfor (const entry of audit.formulas)', jsonStart)
  : source.indexOf(';\nfor (const entry of audit.formulas)', jsonStart);
if (end < 0) throw new Error('Physics12 companion tail missing');
source = source.slice(0, jsonStart) + JSON.stringify(companions, null, 2) + source.slice(end);
fs.writeFileSync(sourcePath, source);
