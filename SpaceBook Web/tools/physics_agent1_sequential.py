"""Strict, source-reviewed Class 9 Physics ingestion using existing data models."""
import json
import subprocess
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'Books/9th/9th physics/pdf/9thphysics.pdf'
DATAFILE = ROOT / 'js/data_phys.js'
LEDGER = ROOT / 'docs/source-verification/physics9-agent1.json'
PROGRESS = ROOT / 'docs/physics-agent1-progress.json'
TRANSLATIONS = ROOT / 'tools/physics9-agent1-translations.json'
MARKER = '// Agent 1 sequential Class 9 Physics source review\n'

def existing_chapter(index=0):
    code = "const fs=require('fs'),vm=require('vm');let c={DATA:{}};vm.createContext(c);vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),c);console.log(JSON.stringify(c.DATA.physChapters[Number(process.argv[2])]));"
    return json.loads(subprocess.check_output(['node','-e',code,str(DATAFILE),str(index)],text=True,encoding='utf-8'))

def save(page):
    entries = json.loads(LEDGER.read_text(encoding='utf-8')) if LEDGER.exists() else []
    assert page['pdfPage'] == len(entries)+1, 'Save the immediately following source page only'
    entries.append(page)
    write_review(entries)

def write_review(entries):
    page = entries[-1]
    translations = json.loads(TRANSLATIONS.read_text(encoding='utf-8')) if TRANSLATIONS.exists() else {}
    # Raster source illustrations are inspection aids only, never lesson assets.
    people = {'YAQUB KINDI', 'IBNAL HAITHAM', 'AL BERUNI', 'Ishfaq Ahmad', 'Abdul Qadeer Khan'}
    for entry in entries:
        for section in entry.get('sections', []):
            pairs = translations.get(str(entry['pdfPage']), {}).get(section['code'])
            if pairs is not None:
                assert len(pairs) == len(section['paras']), f"Translation count differs on PDF page {entry['pdfPage']}"
                section['paras'] = [dict(text=para if isinstance(para,str) else para['text'], urdu=pair[0], pashto=pair[1], translationOrigin='SpaceBook translation; original Arabic/Urdu quotations retained from source') for para,pair in zip(section['paras'],pairs)]
            assert all(isinstance(para,dict) and para.get('urdu') and para.get('pashto') for para in section['paras']), f"Explicit translations required on PDF page {entry['pdfPage']}"
            figures = section.pop('figures', [])
            names = [figure['caption'] for figure in figures if figure.get('caption') in people]
            if names:
                section['personNames'] = names
            for block in section.get('blocks', []):
                if block.get('type') == 'formula' and block.get('latex') == r'I=\frac{Q}{t}':
                    block['svg'] = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 100" width="260" height="100" role="img" aria-label="I equals Q divided by t"><g fill="currentColor" font-family="serif" font-size="28" font-style="italic"><text x="30" y="58">I</text><text x="124" y="30">Q</text><text x="128" y="84">t</text></g><text x="72" y="58" fill="currentColor" font-size="28">=</text><path d="M113 46H155" stroke="currentColor" stroke-width="2"/></svg>'
    content = DATAFILE.read_text(encoding='utf-8').split(MARKER)[0]
    content += MARKER + '(function () {\nconst pages = '+json.dumps(entries,ensure_ascii=False,indent=2)+''';
for (const chapter of DATA.physChapters) {
  const reviewed = pages.filter(page => page.chapterNumber === chapter.num);
  if (!reviewed.length) continue;
  chapter.sourcePages = reviewed;
  chapter.sourceReview = {complete: reviewed.some(page => page.chapterEnd), lastPdfPage: reviewed.at(-1).pdfPage};
  if (chapter.sourceReview.complete) chapter.pageRange = `Pages ${reviewed[0].printedPage} – ${reviewed.at(-1).printedPage}`;
  const sections = new Map();
  for (const page of reviewed) {
    for (const example of page.numericals || []) {
      const existing = (chapter.numericals || []).find(item => item.num === example.num);
      if (existing) Object.assign(existing, example);
      else { chapter.numericals ||= []; chapter.numericals.push(example); }
    }
    for (const activity of page.activities || []) {
      const existing = (chapter.activities || []).find(item => item.num === activity.num);
      if (existing) Object.assign(existing, activity);
      else { chapter.activities ||= []; chapter.activities.push(activity); }
    }
    for (const table of page.tables || []) {
      const existing = (chapter.tables || []).find(item => item.id === table.id || item.title.startsWith(table.sourceNumber));
      if (existing) Object.assign(existing, table);
      else { chapter.tables ||= []; chapter.tables.push(table); }
    }
    if (page.objectives) { chapter.sourceObjectives = page.objectives; chapter.slos = page.objectives; }
    if (page.textbookExercise) {
      chapter.textbookExercise ||= {mcqs: [], sq: [], lq: []};
      for (const [kind, questions] of Object.entries(page.textbookExercise)) {
        chapter.textbookExercise[kind] = questions;
      }
    }
    for (const fragment of page.sections || []) {
      if (!sections.has(fragment.code)) sections.set(fragment.code, {code: fragment.code, heading: fragment.heading, headingEn: fragment.heading, paras: [], sourceBlocks: [], sourcePdfPages: [], sourcePrintedPages: [], personNames: []});
      const section = sections.get(fragment.code);
      section.paras.push(...fragment.paras);
      section.sourceBlocks.push(...(fragment.blocks || []));
      section.personNames.push(...(fragment.personNames || []));
      section.sourcePdfPages.push(page.pdfPage);
      section.sourcePrintedPages.push(page.printedPage);
    }
  }
  for (const section of sections.values()) {
    const existing = chapter.sections.find(item => item.code === section.code);
    section.text = section.paras.map(para => typeof para === 'string' ? para : para.text).join('\\n\\n');
    section.urdu = section.paras.map(para => para.urdu || '').join('\\n\\n');
    section.pashto = section.paras.map(para => para.pashto || '').join('\\n\\n');
    section.translationStatus = 'authored_aligned_paragraphs';
    section.diagramSvg = section.sourceBlocks.filter(block => block.svg).map(block => block.svg).join('');
    section.diagramSvg += section.sourceBlocks.filter(block => block.type === 'dataTable').map(table => `<div style="overflow-x:auto"><table class="diff-table"><caption>${table.title}</caption><thead><tr>${table.headers.map(header => `<th>${header}</th>`).join('')}</tr></thead><tbody>${table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`).join('');
    section.diagramSvg += section.sourceBlocks.filter(block => block.type === 'dataTable').flatMap(table => (table.translations || []).map(translation => `<details dir="rtl"><summary>${translation.language}</summary><div style="overflow-x:auto"><table class="diff-table"><thead><tr>${translation.headers.map(header => `<th>${header}</th>`).join('')}</tr></thead><tbody>${translation.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}</tbody></table></div></details>`)).join('');
    if (existing) Object.assign(existing, section);
    else chapter.sections.unshift(section);
  }
  const sourceOrder = [...sections.keys()];
  chapter.sections.sort((a,b) => {
    const ai = sourceOrder.indexOf(a.code), bi = sourceOrder.indexOf(b.code);
    return (ai < 0 ? sourceOrder.length : ai) - (bi < 0 ? sourceOrder.length : bi);
  });
}
DATA.physChapters[0].sourceFrontMatter = pages.filter(page => !page.chapterNumber);
})();
'''
    DATAFILE.write_text(content,encoding='utf-8')
    subprocess.run(['node','--check',str(DATAFILE)],check=True,capture_output=True)
    LEDGER.parent.mkdir(parents=True,exist_ok=True)
    LEDGER.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    progress=json.loads(PROGRESS.read_text(encoding='utf-8'))
    progress.update(currentChapter=page.get('chapter','Front matter'),lastFullyCompletedPdfPage=page['pdfPage'],
        lastInspectedPdfPage=page['pdfPage'],printedPage=page['printedPage'],pagesCompleted=len(entries),nextPageToVerify=len(entries)+1,
        verificationMode='Original PDF compared with coded project content; browser not required by latest user instruction',
        unresolvedIssues=[issue for entry in entries for issue in entry.get('issues',[])])
    progress.pop('page1',None)
    progress['translationCorrection'] = f"Explicit Urdu/Pashto paragraph pairs saved through PDF page {page['pdfPage']}; raster topic images removed."
    PROGRESS.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def render(number):
    folder=ROOT/'tmp/physics-agent1'
    folder.mkdir(parents=True,exist_ok=True)
    with pymupdf.open(SOURCE) as doc:
        doc[number-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(folder/f'page{number:03}.png')

def crop(number,name,bounds):
    # Compatibility with earlier authoring scripts; save() strips figure entries.
    return ''

if __name__=='__main__':
    import sys
    render(int(sys.argv[1]))
