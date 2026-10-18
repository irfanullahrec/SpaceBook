const fs = require('fs');
const path = require('path');
const target = path.resolve(__dirname, '../js/phys_12_data.js');
let source = fs.readFileSync(target, 'utf8');
const prefix = 'PHYS_12_DATA[0].sections.unshift(...';
const start = source.indexOf(prefix);
if (start < 0) throw new Error('Physics12 source sections missing');
const jsonStart = start + prefix.length;
let depth = 0, quoted = false, escaped = false, end = -1;
for (let i = jsonStart; i < source.length; i++) {
  const ch = source[i];
  if (quoted) {
    if (escaped) escaped = false;
    else if (ch === '\\') escaped = true;
    else if (ch === '"') quoted = false;
  } else if (ch === '"') quoted = true;
  else if (ch === '[') depth++;
  else if (ch === ']') { if (--depth === 0) { end = i + 1; break; } }
}
if (end < 0) throw new Error('Physics12 sections JSON is malformed');
const sections = JSON.parse(source.slice(jsonStart, end));
const section = sections.find(item => item.id === 'phys12-front-dielectric37');
if (!section) throw new Error('PDF23 dielectric section missing');
section.sourceLayout = section.sourceLayout.filter(block => !(block.indices || []).some(index => index >= section.paras.length));
source = source.slice(0, jsonStart) + JSON.stringify(sections, null, 2) + source.slice(end);
fs.writeFileSync(target, source);
