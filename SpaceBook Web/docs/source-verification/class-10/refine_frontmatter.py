import os
from pathlib import Path
ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
lock = ROOT/'tmp'/'class-content-shared.lock'
fd = os.open(lock, os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,f'class-10 pid={os.getpid()}\n'.encode())
    app = ROOT/'js'/'app.js'
    text = app.read_text(encoding='utf-8')
    start = text.index('function renderClass10PhysicsFrontMatter(')
    end = text.index('function renderScienceLessonSubContent(', start)
    helper = '''function renderClass10PhysicsFrontMatter(ch) {
  if (state.selectedClass !== 'cls10' || !ch.sourceFrontMatter) return '';
  const translated = (p, field) => p.type === 'heading'
    ? `<h5>${sanitize(p[field])}</h5>` : `<p>${sanitize(p[field])}</p>`;
  const table = (page, lang) => !page.table ? '' : `<div style="overflow-x:auto;"><table style="border-collapse:collapse;width:100%;"><caption>${sanitize(lang === 'ur' ? page.titleUrdu : lang === 'ps' ? page.titlePashto : page.title)}</caption><tbody>${page.table.rows.map((row, r) => `<tr>${row[lang].map((cell, c) => `<${c === 1 ? 'th scope="row"' : 'td'} style="padding:.5rem;border-bottom:1px solid #cbd5e1;text-align:start;">${lang === 'en' && cell && c < 2 ? renderInteractiveParagraphHtml(cell, row.ur[c], row.ps[c], `${page.id}-row-${r}-${c}`, true) : sanitize(cell)}</${c === 1 ? 'th' : 'td'}>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  return `<details class="physics10-front-matter" style="margin-bottom:1rem;"><summary>Textbook front matter / کتاب کا ابتدائی حصہ / د کتاب لومړنۍ برخه</summary>${ch.sourceFrontMatter.map(page => {
    const paras = page.paras || [];
    const urduOriginal = page.sourceLanguage === 'ur';
    const original = urduOriginal ? `<div dir="rtl" lang="ur" style="text-align:right;">${paras.map(p => p.sourceLines ? `<p>${p.sourceLines.map(line => sanitize(line)).join('<br>')}</p>` : translated(p, 'urdu')).join('')}</div>` : '';
    return `<article style="padding:1rem;border-bottom:1px solid #e2e8f0;"><h4>${sanitize(urduOriginal ? page.titleUrdu : page.title)}</h4><small>${sanitize(page.source.pdf)} · PDF page ${page.source.pdfPage}${page.source.printedPage ? ` · printed page ${sanitize(page.source.printedPage)}` : ''}</small>
      ${original}${urduOriginal ? '<h5>English translation</h5>' : ''}
      ${table(page, 'en')}
      ${paras.map((p, i) => {
        const tag = p.type === 'heading' ? 'h5' : 'p';
        return `<${tag}>${renderInteractiveParagraphHtml(p.text, p.urdu, p.pashto, `${page.id}-${i}`, true)}</${tag}>`;
      }).join('')}
      ${urduOriginal ? '' : `<details dir="rtl" lang="ur"><summary>${sanitize(page.titleUrdu)}</summary>${table(page, 'ur')}${paras.map(p => translated(p, 'urdu')).join('')}</details>`}
      <details dir="rtl" lang="ps"><summary>${sanitize(page.titlePashto)}</summary>${table(page, 'ps')}${paras.map(p => translated(p, 'pashto')).join('')}</details>
    </article>`;
  }).join('')}</details>`;
}

'''
    helper = '''function renderClass10PhysicsFrontMatter(ch) {
  if (state.selectedClass !== 'cls10' || !ch.sourceFrontMatter) return '';
  const front = `<details class="physics10-front-matter" style="margin-bottom:1rem;"><summary>Textbook front matter / کتاب کا ابتدائی حصہ / د کتاب لومړنۍ برخه</summary>${ch.sourceFrontMatter.map(renderPhysics10SourcePage).join('')}</details>`;
  return front + (ch.sourceOpening ? renderPhysics10SourcePage(ch.sourceOpening) : '') + (ch.sourceIntroduction ? renderPhysics10SourcePage(ch.sourceIntroduction) : '');
}

'''
    text = text[:start]+helper+text[end:]
    start = text.index('function renderScienceLessonSubContent(')
    before, tail = text[:start],text[start:]
    if 'sec.sourceClass10Physics ? renderPhysics10SourceSection' not in tail:
        replacements = {
            "const secUrdu = sec.sourceLayout ?": "const secUrdu = sec.sourceClass10Physics ? renderPhysics10SourceSection(sec, 'ur', idx) : sec.sourceLayout ?",
            "const secPashto = sec.sourceLayout ?": "const secPashto = sec.sourceClass10Physics ? renderPhysics10SourceSection(sec, 'ps', idx) : sec.sourceLayout ?",
            "${sec.sourceLayout ? renderScienceSourceLayout(sec, paras, 'en', idx)": "${sec.sourceClass10Physics ? renderPhysics10SourceSection(sec, 'en', idx) : sec.sourceLayout ? renderScienceSourceLayout(sec, paras, 'en', idx)"
        }
        for old,new in replacements.items():
            assert tail.count(old) == 1, old
            tail = tail.replace(old,new,1)
    text = before+tail
    old = "      if (catKey === 'num') return chunk;"
    if old in text:
        assert text.count(old) == 1
        text = text.replace(old,"      if (catKey === 'num') return res + chunk;",1)
    anchor = "  if (catKey === 'num' || catKey === 'all') {\n    const numericals = ch.numericals || ex.numericals || [];"
    if "res += renderClass10PhysicsWorkedExamples(ch)" not in text:
        assert text.count(anchor) == 1
        text = text.replace(anchor, "  if (catKey === 'num' || catKey === 'all') {\n    if (subjKey === 'phys' && state.selectedClass === 'cls10') res += renderClass10PhysicsWorkedExamples(ch);\n    const numericals = ch.numericals || ex.numericals || [];",1)
    start = text.index('  const definitions = ch.definitions || [];')
    before,tail = text[:start],text[start:]
    if "${subjKey === 'phys' ? renderClass10PhysicsWorkedExamples(ch) : ''}" not in tail:
        anchor = '  return `\n    <div>'
        assert anchor in tail
        tail = tail.replace(anchor, anchor+"\n      ${subjKey === 'phys' ? renderClass10PhysicsWorkedExamples(ch) : ''}",1)
    text = before+tail
    if '// Class 10 Physics: search visually reviewed source records.' not in text:
        anchor = '  // 6. Search Class 12 Chapters'
        addition = '''  // Class 10 Physics: search visually reviewed source records.
  (DATA.phys10Chapters || []).forEach((ch, idx) => {
    if (typeof physics10SourceSearchText !== 'function' || !physics10SourceSearchText(ch).toLowerCase().includes(q)) return;
    results.push({type: "Chapter", badge: "⚛️ Class 10 Physics", title: `Chapter ${ch.num}: ${ch.name}`,
      sub: "Textbook text, worked examples and aligned translations",
      action: () => { clearGlobalSearch(); openSubject("cls10", "cls10-phy"); selectSubjectChapter('phys', idx, 'cls10'); }});
  });

'''
        assert text.count(anchor) == 1
        text = text.replace(anchor,addition+anchor,1)
    app.write_text(text,encoding='utf-8',newline='\n')
finally:
    os.close(fd)
    lock.unlink()
print('Front matter preserves credit headings and Urdu original line structure.')
