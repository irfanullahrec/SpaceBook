"""Small shared edits under the cross-class exclusive filesystem lock."""
import os
from pathlib import Path

ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
lock = ROOT/'tmp'/'class-content-shared.lock'
lock.parent.mkdir(exist_ok=True)
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
try:
    os.write(fd, f'class-10 pid={os.getpid()}\n'.encode())
    index = ROOT/'index.html'
    text = index.read_text(encoding='utf-8')
    anchor = '  <script src="js/data_phys.js?v=20261003_7"></script>'
    addition = '\n  <script src="js/physics_10_source_data.js?v=20261009_1"></script>'
    if 'src="js/physics_10_source_data.js' not in text:
        assert text.count(anchor) == 1
        index.write_text(text.replace(anchor, anchor+addition, 1), encoding='utf-8', newline='\n')
    app = ROOT/'js'/'app.js'
    text = app.read_text(encoding='utf-8')
    anchor = 'function renderScienceLessonSubContent(subjKey, ch, subTab) {'
    helper = '''function renderClass10PhysicsFrontMatter(ch) {
  if (state.selectedClass !== 'cls10' || !ch.sourceFrontMatter) return '';
  return `<details class="physics10-front-matter" style="margin-bottom:1rem;"><summary>Textbook front matter / کتاب کا ابتدائی حصہ / د کتاب لومړنۍ برخه</summary>${ch.sourceFrontMatter.map(page => {
    const paras = page.paras || [];
    return `<article style="padding:1rem;border-bottom:1px solid #e2e8f0;"><h4>${sanitize(page.title)}</h4><small>${sanitize(page.source.pdf)} · PDF page ${page.source.pdfPage}</small>
      ${paras.map((p, i) => `<p>${renderInteractiveParagraphHtml(p.text, p.urdu, p.pashto, `${page.id}-${i}`, true)}</p>`).join('')}
      <details dir="rtl" lang="ur"><summary>${sanitize(page.titleUrdu)}</summary>${paras.map(p => `<p>${sanitize(p.urdu)}</p>`).join('')}</details>
      <details dir="rtl" lang="ps"><summary>${sanitize(page.titlePashto)}</summary>${paras.map(p => `<p>${sanitize(p.pashto)}</p>`).join('')}</details>
    </article>`;
  }).join('')}</details>`;
}

'''
    if 'function renderClass10PhysicsFrontMatter(' not in text:
        assert text.count(anchor) == 1
        text = text.replace(anchor, helper+anchor, 1)
        start = text.index(anchor)
        before, tail = text[:start], text[start:]
        insertion = '        <div class="science-lesson-cards-list">'
        assert insertion in tail
        tail = tail.replace(insertion, "        ${subjKey === 'phys' ? renderClass10PhysicsFrontMatter(ch) : ''}\n"+insertion, 1)
        app.write_text(before+tail, encoding='utf-8', newline='\n')
finally:
    os.close(fd)
    lock.unlink()
print('Class 10 front matter wired; shared lock released.')
