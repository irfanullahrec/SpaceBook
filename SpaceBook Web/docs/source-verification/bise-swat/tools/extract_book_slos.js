'use strict';
/* Learning outcomes PRINTED IN THE APP'S OWN TEXTBOOKS (the "After studying this unit, students will be able to ..." /
 * "Student Learning Outcomes" blocks of the KPTBB books), for the subjects whose Board SLO list is not published.
 *   node --max-old-space-size=6144 docs/source-verification/bise-swat/tools/extract_book_slos.js <out.json> [subjectId,...]
 * Renders every chapter of the subject in the app sandbox (same loop as tools/snapshot_html.js), turns each tab's html into text and
 * keeps the text that follows an outcome heading. Writes {subjectId: [{ch, title, tab, text}]} for build_book_slos.py to split. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const { load } = require(path.join(ROOT, 'tools', 'lib', 'app_sandbox'));
const out = process.argv[2];
const only = process.argv[3] ? process.argv[3].split(',') : null;
const TARGET = ['cls9-isl', 'cls9-islopt', 'cls9-urdu', 'cls9-quran', 'cls10-isl', 'cls10-islopt', 'cls10-urdu', 'cls10-quran',
  'cls11-phy', 'cls11-chem', 'cls11-bio', 'cls11-urdu', 'cls11-isl', 'cls12-phy', 'cls12-chem', 'cls12-bio', 'cls12-pak', 'cls12-urdu'];
const app = load({ page: 'index.html', quiet: true });
const VIEWS = {
  generic: { area: 'subjectTopicArea', content: 'subjTabContent', chapter: 'select\\w*(?:Chapter|Unit|Lesson|Page)', tab: 'switchSubjectTab', reset: 'state.activeSubjTab = null; ' },
  math: { area: 'mathTopicArea', content: 'mathTabContent', chapter: 'selectMathChapter', tab: 'switchMathTab', reset: '' }
};
const unesc = oc => oc.replace(/&#39;|&quot;/g, "'");
const text = html => html.replace(/<(script|style)[\s\S]*?<\/\1>/g, ' ').replace(/<\/(p|li|h\d|div|tr|details|summary)>/g, '\n').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/[ \t]+/g, ' ');
const res = {};
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id })))').filter(s => (only || TARGET).includes(s.id));
for (const s of subjects) {
  const step = code => { try { return app.run(code, 120000); } catch (e) { return null; } };
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const body = step(`document.getElementById('dashboard-body').innerHTML`) || '';
  const V = body.includes('id="mathTopicArea"') ? VIEWS.math : VIEWS.generic;
  const chs = [...new Set([...body.matchAll(new RegExp('onclick="(' + V.chapter + '\\([^"]*)"', 'g'))].map(m => m[1]))];
  const rows = [], heads = [];
  chs.forEach((oc, i) => {
    step(`${V.reset}${unesc(oc)}`);
    const area = step(`document.getElementById('${V.area}').innerHTML`) || '';
    const title = text((area.match(/class="mch-title"[^>]*>([\s\S]*?)<\/span>/) || [])[1] || '').trim();
    const tabOcs = [...new Set([...area.matchAll(new RegExp('onclick="(' + V.tab + '\\([^"]*)"', 'g'))].map(m => m[1]))];
    let hseen = false;
    for (const t of tabOcs) {
      step(`document.getElementById('${V.content}').innerHTML = ''`);
      step(unesc(t));
      const rawHtml = step(`document.getElementById('${V.content}').innerHTML`) || '';
      const tx = text(rawHtml);
      if (!hseen && /lesson|text|sabaq|reading|سبق/i.test(t)) { hseen = true; heads.push({ i, title, tab: t.slice(0, 60), h: [...rawHtml.matchAll(/<h[2-5][^>]*>([\s\S]*?)<\/h[2-5]>/g)].map(m => text(m[1]).replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 80) }); }
      for (const m of tx.matchAll(/(students?\s+(?:will|should)\s+be\s+able\s+to|learning\s+outcomes?|student\s+learning\s+outcomes|طلبہ\s+(?:اس\s+قابل|کے\s+تعلیمی\s+نتائج)|سیکھنے\s+کے\s+نتائج|تعلیمی\s+نتائج)/gi)) {
        const hi = rawHtml.search(/(students?\s+(?:will|should)\s+be\s+able\s+to|learning\s+outcomes?|student\s+learning\s+outcomes|تعلیمی\s+نتائج|اس\s+قابل)/i);
        rows.push({ i, title, html: hi < 0 ? '' : rawHtml.slice(Math.max(0, hi - 200), hi + 60000), tab: (t.match(/'([^']+)'\s*,\s*(?:\d+|'[^']*')/) || [])[1] || t.slice(0, 40), at: m.index, text: tx.slice(Math.max(0, m.index - 60), m.index + 1600) });
        break;
      }
    }
  });
  res[s.id] = rows; res[s.id + '#heads'] = heads;
  console.log(s.id, chs.length, 'chapters,', rows.length, 'with an outcome block');
}
fs.writeFileSync(out, JSON.stringify(res));
