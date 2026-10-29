'use strict';
/* Rights audit of the book text the website and the app serve (Classes 1-12): finds the markings of the textbook boards and the people who made the books,
 * so that a person can decide what, if anything, may be removed. It changes NOTHING. It lists every match (file, class, page when the data says it, a short
 * snippet) and a decision for each category.
 *     node tools/rights/audit_markings.js [--write]      --write: docs/launch/content_rights_findings.csv and docs/launch/CONTENT_RIGHTS_AUDIT.md
 * Categories:
 *   not-for-sale     "Not for sale" and the like
 *   free-distribution  "free distribution by / from Government", "distributed free", "free of cost"
 *   rights-notice    "All rights reserved", "Copyright", the (c) sign
 *   credit           authors, writers, editors, reviewers, translators, illustrators, designers ("written by", "reviewed by", "Authors", "Reviewers" ...)
 *   board            the Textbook Board, the Government, the Directorate (who published the book)
 * Decision rule (docs/launch/CONTENT_RIGHTS.md): nothing is removed unless a written permission of the rights holder is on file in docs/permissions/ AND the
 * removal is legally permitted; credits and rights notices are attribution and stay in any case. Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const WRITE = process.argv.includes('--write');

const RULES = [
  ['not-for-sale', /not\s+for\s+sale/gi],
  ['free-distribution', /free\s+(?:distribution\s+)?(?:from|by)\s+(?:the\s+)?govern\w*|distributed\s+free|free\s+of\s+(?:cost|charge)|free\s+textbook/gi],
  ['rights-notice', /all\s+rights\s+reserved|copyright|©/gi],
  ['credit', /(?:written|compiled|edited|reviewed|translated|illustrated|designed|prepared|composed|authored)\s+by|\b(?:authors?|co-?authors?|reviewers?|contributors?|illustrators?|writers?|editors?|translators?|panel\s+of\s+(?:authors|experts))\s*[:\-–]|مصنف|مؤلف|مرتب|نظر\s*ثانی|مترجم/gi],
  ['board', /textbook\s+board|government\s+of\s+(?:khyber|k\.?\s?p|pakistan)|directorate\s+of\s+curriculum|ministry\s+of\s+education/gi],
];

// the served data files: every js file that is not application code (the books, their data, the solutions)
const SKIP = /^(app|auth|sb_|core\/|universal_|word_stats\.js|test_prep\.js|search|class12_study|math\d+_reader|biology_10_reader|english_10_reader|tts|offline)/;
const files = fs.readdirSync(path.join(ROOT, 'js')).filter(f => f.endsWith('.js') && !SKIP.test(f));
const SUBJ = { eng: 'English', english: 'English', math: 'Mathematics', maths: 'Mathematics', urdu: 'Urdu', sci: 'Science', phys: 'Physics', phy: 'Physics', chem: 'Chemistry', bio: 'Biology', stat: 'Statistics', isl: 'Islamiat', islamiat: 'Islamiat', pashto: 'Pashto', quran: 'Quran', arabic: 'Arabic', comp: 'Computer', cs: 'Computer Science', civics: 'Civics', econ: 'Economics', hpe: 'HPE', pak: 'Pakistan Studies', pakstudy: 'Pakistan Studies', hist: 'History', geo: 'Geography', gk: 'General Knowledge', drawing: 'Drawing', sst: 'Social Studies' };
function guess(f) {
  const cls = (/_(\d{1,2})(?:_|\.)/.exec(f) || /(\d{1,2})/.exec(f) || [])[1] || '';
  const word = (/^(?:cls\d+_)?([a-z]+)/i.exec(f.replace(/^data_/, '')) || [])[1] || '';
  return { cls: cls && +cls >= 1 && +cls <= 12 ? cls : '', subject: SUBJ[word.toLowerCase()] || word };
}

const rows = [];
for (const f of files) {
  const text = fs.readFileSync(path.join(ROOT, 'js', f), 'utf8');
  const g = guess(f);
  for (const [cat, re] of RULES) {
    re.lastIndex = 0;
    let m;
    while ((m = re.exec(text))) {
      const a = Math.max(0, m.index - 50), b = Math.min(text.length, m.index + m[0].length + 90);
      const snippet = text.slice(a, b).replace(/\\n|\\r|\\t/g, ' ').replace(/\s+/g, ' ').replace(/[<>]/g, '').trim();
      const before = text.slice(Math.max(0, m.index - 4000), m.index);
      const pg = /"(?:printed|pdf)"\s*:\s*(\d+)(?![\s\S]*"(?:printed|pdf)"\s*:)/.exec(before);
      const kind = /_book\.js$/.test(f) ? 'page book' : /(_data|^data_)/.test(f) ? 'data file' : 'other';
      const ours = /printed (?:at|in)|is printed|watermark|diamond|the scan/i.test(snippet);          // a transcription note written for this project, not the book's own text
      rows.push({ file: 'js/' + f, cls: g.cls, subject: g.subject, category: cat, kind, ours, page: pg ? pg[1] : '', matched: m[0].replace(/\s+/g, ' '), snippet });
      if (m.index === re.lastIndex) re.lastIndex++;
    }
  }
}

const DECISION = {
  'not-for-sale': 'FLAG - not removed: removal needs the rights holder\'s written permission (none on file, S-06) and legal advice',
  'free-distribution': 'FLAG - not removed: same as above; a free-distribution mark on a book we show under a subscription is the most sensitive case',
  'rights-notice': 'KEEP - a copyright / rights notice is attribution and stays in any case',
  'credit': 'KEEP - names of authors, reviewers, editors, illustrators are attribution; removal also needs each person\'s consent and legal advice',
  'board': 'KEEP - the publisher\'s name; shows who made the book and must not suggest that SpaceBook is the publisher',
};
const byCat = {}, byBook = {};
for (const r of rows) {
  byCat[r.category] = (byCat[r.category] || 0) + 1;
  const k = (r.cls ? 'Class ' + r.cls : 'class not in the file name') + ' | ' + (r.subject || '?') + ' | ' + r.file;
  (byBook[k] = byBook[k] || {})[r.category] = ((byBook[k] || {})[r.category] || 0) + 1;
}
console.log(`rights audit: ${files.length} served data files scanned, ${rows.length} matches`);
for (const c of Object.keys(DECISION)) console.log(`  ${c.padEnd(18)} ${String(byCat[c] || 0).padStart(6)}   ${DECISION[c]}`);
const needsReview = Object.entries(byBook).filter(([, v]) => v['not-for-sale'] || v['free-distribution']).length;
const kinds = {};
for (const r of rows) { const k = r.kind + ' / ' + r.category; kinds[k] = (kinds[k] || 0) + 1; }
console.log('  by kind (page book = the reviewed books the reader draws; data file = older data and search sources):');
for (const k of Object.keys(kinds).filter(k => /not-for-sale|free-distribution/.test(k)).sort()) console.log('    ' + k.padEnd(36) + kinds[k]);
console.log(`  of the not-for-sale matches, ${rows.filter(r => r.category === 'not-for-sale' && r.ours).length} are transcription notes written for this project; the rest is the watermark or title-page text inside the typed pages`);
console.log(`  files with a not-for-sale or free-distribution mark: ${needsReview}; files with a credit line: ${Object.entries(byBook).filter(([, v]) => v.credit).length}`);

if (WRITE) {
  const esc = s => '"' + String(s).replace(/"/g, '""') + '"';
  // detail rows only where a person has to decide (the marks and the notices), and not the thousands of watermark fragments of the older data files and the credit lines:
  // those are counted per file in content_rights_by_file.csv
  const detail = rows.filter(r => r.category === 'free-distribution' || r.category === 'rights-notice' || (r.category === 'not-for-sale' && r.kind !== 'data file'));
  fs.writeFileSync(path.join(ROOT, 'docs', 'launch', 'content_rights_findings.csv'), 'file,class,subject,category,kind,our_transcription_note,page,matched,snippet,decision\n' +
    detail.map(r => [r.file, r.cls, r.subject, r.category, r.kind, r.ours ? 'yes' : '', r.page, esc(r.matched), esc(r.snippet.slice(0, 150)), esc(DECISION[r.category])].join(',')).join('\n') + '\n');
  fs.writeFileSync(path.join(ROOT, 'docs', 'launch', 'content_rights_by_file.csv'), 'file,class,subject,kind,not_for_sale,free_distribution,rights_notice,credit,board\n' +
    Object.entries(byBook).map(([k, v]) => { const [, , f] = k.split(' | '); const r0 = rows.find(r => r.file === f); return [f, r0.cls, r0.subject, r0.kind, v['not-for-sale'] || 0, v['free-distribution'] || 0, v['rights-notice'] || 0, v.credit || 0, v.board || 0].join(','); }).sort().join('\n') + '\n');
  const lines = ['# Content rights audit', '',
    'Made by `node tools/rights/audit_markings.js --write` (it changes nothing). Scope: the typed book text and data the website and the app serve (`js/*.js` data files), Classes 1 to 12. **Not scanned:** pictures (covers, figures, `assets/`): their text cannot be searched here and they must be looked at by a person (the covers carry the Textbook Board\'s mark).', '',
    '## Decision', '',
    '**Nothing was removed.** No written permission of a rights holder is on file (`FINDINGS_REGISTER.md` S-06, `docs/permissions/` is empty), so the rule of `CONTENT_RIGHTS.md` leaves every marking in place. Credits and rights notices are attribution and stay even with a permission. The "Not for sale" and free-distribution marks are listed for a decision by the owner with a lawyer.', '',
    '| Category | Matches | Decision |', '|---|---:|---|'];
  for (const c of Object.keys(DECISION)) lines.push(`| ${c} | ${byCat[c] || 0} | ${DECISION[c]} |`);
  lines.push('', '### What the matches are', '',
    'Most "Not for sale" matches are **the scan\'s watermark text that ended up inside the typed pages** (for example in the Class 12 Physics and Chemistry data: a page footer in the middle of a paragraph), not a deliberate notice. Some are our own transcription notes ("Not For Sale is printed at the lower right"). The title-page lines ("Free From Government - NOT FOR SALE - Khyber Pakhtunkhwa Textbook Board Peshawar") are the book\'s own legend. Removing the stray watermark text would also remove the legend, so it waits for the same permission.', '',
    '| Kind | Category | Matches |', '|---|---|---:|');
  for (const k of Object.keys(kinds).sort()) { const [kd, cg] = k.split(' / '); lines.push(`| ${kd} | ${cg} | ${kinds[k]} |`); }
  lines.push('', `${files.length} files scanned, ${rows.length} matches in total; the full list (file, class, subject, page when the data gives it, a short snippet) is \`content_rights_findings.csv\`.`, '',
    '## Files with a "Not for sale" or free-distribution mark (for review)', '', '| Class | Subject | File | Not for sale | Free distribution | Credit lines |', '|---|---|---|---:|---:|---:|');
  for (const [k, v] of Object.entries(byBook).filter(([, v]) => v['not-for-sale'] || v['free-distribution']).sort()) {
    const [c, s, f] = k.split(' | ');
    lines.push(`| ${c} | ${s} | \`${f}\` | ${v['not-for-sale'] || 0} | ${v['free-distribution'] || 0} | ${v.credit || 0} |`);
  }
  fs.writeFileSync(path.join(ROOT, 'docs', 'launch', 'CONTENT_RIGHTS_AUDIT.md'), lines.join('\n') + '\n');
  console.log('wrote docs/launch/content_rights_findings.csv and docs/launch/CONTENT_RIGHTS_AUDIT.md');
}
