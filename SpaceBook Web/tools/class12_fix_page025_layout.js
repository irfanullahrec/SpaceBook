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
const section = sections.find(item => item.id === 'phys12-front-example11740');
if (!section) throw new Error('PDF25 Example 11.7 section missing');
const missingIndex = 12;
if (section.sourceLayout.some(block => (block.indices || []).includes(missingIndex))) {
  throw new Error('Expected paragraph is already covered; refusing duplicate layout');
}
const lastEquation = section.sourceLayout.findLast(block => block.type === 'equation');
if (!lastEquation || !lastEquation.indices.includes(11)) throw new Error('Unexpected Example 11.7 ending layout');
section.sourceLayout.push({ type: 'equation', indices: [missingIndex] });
source = source.slice(0, jsonStart) + JSON.stringify(sections, null, 2) + source.slice(end);
fs.writeFileSync(target, source);
