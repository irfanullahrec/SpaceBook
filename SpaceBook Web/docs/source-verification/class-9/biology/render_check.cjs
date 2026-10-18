// Non-browser reader check: renders BIO_DATA sections through the real app.js
// source-layout renderer and reports malformed output. Usage: node render_check.cjs <unitNumber>
const fs = require('fs'), vm = require('vm'), path = require('path');
const web = path.resolve(__dirname, '../../../..');
const app = fs.readFileSync(path.join(web, 'js/app.js'), 'utf8');
function grab(name) {
  const i = app.indexOf('function ' + name + '(');
  if (i < 0) throw new Error('missing ' + name);
  let depth = 0;
  for (let k = app.indexOf('{', i); k < app.length; k++) {
    if (app[k] === '{') depth++;
    else if (app[k] === '}') { depth--; if (depth === 0) return app.slice(i, k + 1); }
  }
}
const lines = app.split(String.fromCharCode(10));
const sanLine = lines.find(l => l.startsWith('const sanitize =')).replace('const sanitize', 'var sanitize');
const ctx = { console, state: { selectedClass: 'cls9' }, document: { createElement: () => ({}) } };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(web, 'js/bio_data.js'), 'utf8'), ctx);
const fns = ['splitSentenceText', 'renderInteractiveParagraphHtml', 'getScienceSectionParagraphsWithTranslations', 'renderScienceSourceLayout'];
vm.runInContext(sanLine + String.fromCharCode(10) + fns.map(grab).join(String.fromCharCode(10)), ctx);
const unit = ctx.BIO_DATA.find(u => String(u.number) === String(process.argv[2] || 1));
let bad = 0, svgs = 0, tables = 0;
unit.sections.forEach((sec, idx) => {
  const paras = ctx.getScienceSectionParagraphsWithTranslations(sec, unit, 'bio');
  for (const lang of ['en', 'ur', 'ps']) {
    const html = sec.sourceLayout ? ctx.renderScienceSourceLayout(sec, paras, lang, idx) : '';
    const issues = [];
    if (!html) issues.push('empty');
    const prose = html.replace(/<svg[\s\S]*?<\/svg>/g, '');
    if (/\[object Object\]|undefined|NaN/.test(prose)) issues.push('object/undefined text');
    if (/&lt;(p|b|svg|div)\b/.test(prose)) issues.push('escaped markup');
    if (lang === 'en') { svgs += (html.match(/<svg\b/g) || []).length; tables += (html.match(/<table\b/g) || []).length; }
    if (lang !== 'en' && sec.sourceBlocks?.some(b => b.kind === 'table') && !/<table\b/.test(html)) issues.push('table missing in ' + lang);
    if (issues.length) { bad++; console.log(sec.id, lang, issues.join(',')); }
  }
});
console.log(`unit ${unit.number}: sections=${unit.sections.length} svg=${svgs} tables=${tables} problems=${bad}`);
process.exit(bad ? 1 : 0);
