const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname,'..');
const app = fs.readFileSync(path.join(root,'js/app.js'),'utf8');
const context = {state:{selectedClass:'cls9'},sanitize:value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))};
vm.createContext(context);
const splitStart = app.indexOf('function splitSentenceText(');
const splitEnd = app.indexOf('// ─── SECTION PARAGRAPH',splitStart);
vm.runInContext(app.slice(splitStart,splitEnd),context);
const readerStart = app.indexOf('function renderInteractiveParagraphHtml(');
const readerEnd = app.indexOf('\nfunction playParaTTSFromBtn(',readerStart);
vm.runInContext(app.slice(readerStart,readerEnd),context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/vendor/katex/katex.min.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(root,'js/lesson_math_reader.js'),'utf8'),context);
const examples = [
 String.raw`Force \(\vec F_{12}=k\frac{q_1q_2}{r^2}\hat r_{21}\) ... (11.3)`,
 String.raw`Since \(\hat r_{12}=-\hat r_{21}\). So from Eq. (11.2).`,
 String.raw`Charge \(q_1\) acts on \(q_2\).`,
 String.raw`Current \[I=\frac{Q}{t}\]`,
 String.raw`Current \(I=\frac{Q}{t}\), charge.`,
 'Energy '+String.fromCharCode(92)+'(E=mc^2'+String.fromCharCode(92)+')',
 'Energy $E=mc^2$'
];
for (const text of examples) {
 const html = context.renderInteractiveParagraphHtml(text,'درست اردو ترجمہ','سمه پښتو ژباړه','test',true);
 assert(html.includes('class="katex"'),'Equation failed to render');
 assert(!html.includes('katex-error'),'Equation parser error');
 assert(!html.includes('SPACEBOOKMATH'),'Equation placeholder leaked');
 const visible = html.replace(/<[^>]*>/g,'').replace(/<annotation[\s\S]*?<\/annotation>/g,'');
 // TeX source in the accessibility annotation is intentional; visible reader spans use KaTeX.
 assert(!/dict-clickable-word[^>]*>[^<]*\\/.test(html),'LaTeX was word-tokenized');
 assert(html.includes('data-ur="درست اردو ترجمہ"'));
 assert.equal((html.match(/class="lesson-sentence"/g)||[]).length,1,'Source paragraph was split');
}
console.log('Passed single/double escaped LaTeX, inline/display equations, punctuation, preserved paragraph and translation regression checks.');
