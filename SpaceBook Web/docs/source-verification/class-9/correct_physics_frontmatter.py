"""Precisely upsert one reviewed page under the shared filesystem lock."""
import json
import os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
LOCK = ROOT/'tmp/class-content-shared.lock'
PAGE = {'id':'cls9-physics-front-001','pdfPage':1,'printedPage':None,'status':'corrected-fresh-review','kind':'cover','title':'A Textbook of PHYSICS','headingUrdu':'طبیعیات کی درسی کتاب','headingPashto':'د فزیک درسي کتاب','sourcePdf':r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf','paragraphs':['for Grade IX','Khyber Pakhtunkhwa Textbook Board, Peshawar'],'pairedParagraphs':[{'text':'for Grade IX','urdu':'جماعت نہم کے لیے','pashto':'د نهم ټولګي لپاره'},{'text':'Khyber Pakhtunkhwa Textbook Board, Peshawar','urdu':'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','pashto':'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'}],'comparison':'Freshly inspected local 1.5x render. Title, grade and publisher preserved; decorative globe and publisher emblem excluded as noninstructional cover decoration. Added aligned translations and accessible front-matter display.'}
fd = os.open(LOCK, os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 physics front matter\n')
    target=ROOT/'js/data_phys.js'
    text=target.read_text(encoding='utf-8')
    marker='// Agent 1 sequential Class 9 Physics source review\n'
    start=text.index('const pages = ',text.index(marker))+len('const pages = ')
    pages,end=json.JSONDecoder().raw_decode(text[start:])
    pages[0]=PAGE
    text=text[:start]+json.dumps(pages,ensure_ascii=False,indent=2)+text[start+end:]
    target.write_text(text,encoding='utf-8')
    app=ROOT/'js/app.js'
    text=app.read_text(encoding='utf-8')
    needle="function renderScienceLessonSubContent(subjKey, ch, subTab) {"
    helper='''function renderClass9PhysicsFrontMatter(ch) {
  if (state.selectedClass !== 'cls9') return '';
  return (ch.sourceFrontMatter || []).filter(page => page.pairedParagraphs).map(page => `
    <details class="physics-front-matter" data-source-pdf-page="${page.pdfPage}" style="margin-bottom:1rem;padding:1rem;border:1px solid #e2e8f0;border-radius:8px;">
      <summary><strong>${sanitize(page.title)}</strong> · PDF page ${page.pdfPage}</summary>
      <h4>${sanitize(page.headingUrdu || '')} / ${sanitize(page.headingPashto || '')}</h4>
      ${page.pairedParagraphs.map((para, index) => renderInteractiveParagraphHtml(para.text, para.urdu, para.pashto, `${page.id}-${index}`, true)).join('<div style="height:.75rem"></div>')}
    </details>`).join('');
}

'''
    if 'function renderClass9PhysicsFrontMatter(' not in text:
        text=text.replace(needle,helper+needle,1)
        anchor="function renderScienceLessonSubContent(subjKey, ch, subTab) {\n  if (subTab === 'translations') {\n    const sections = ch.sections || ch.topics || [];\n    return `\n      <div>"
        assert anchor in text
        text=text.replace(anchor,anchor+"\n        ${subjKey === 'phys' ? renderClass9PhysicsFrontMatter(ch) : ''}",1)
        app.write_text(text,encoding='utf-8')
finally:
    os.close(fd)
    LOCK.unlink()
(Path(__file__).resolve().parent/'physics-page-001.json').write_text(json.dumps(PAGE,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved Physics cover correction in existing source record and scoped renderer.')
