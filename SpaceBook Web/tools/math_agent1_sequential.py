"""Save reviewed Class 9 pages in order; no inferred/OCR completion."""
import json
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'Books/9th/9th MTHA/PDF/9th maaths.pdf'
LEDGER = ROOT / 'docs/source-verification/math9-agent1.json'
PROGRESS = ROOT / 'docs/math-agent1-progress.json'

def save(page):
    entries = json.loads(LEDGER.read_text(encoding='utf-8')) if LEDGER.exists() else []
    assert page['pdfPage'] == len(entries) + 1, 'Pages must be saved sequentially'
    entries.append(page)
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(entries, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    data = ROOT / 'js/math_data.js'
    text = data.read_text(encoding='utf-8')
    marker = '// Agent 1 fresh sequential source review\n'
    text = text.split(marker)[0]
    text += marker + 'MATH_DATA[0].sourcePages = ' + json.dumps(entries, ensure_ascii=False, indent=2) + ';\n'
    text += '''(function () {
  const chapter = MATH_DATA[0];
  chapter.title = 'Matrices';
  chapter.badge = 'Source review in progress';
  chapter.sourceReviewStatus = {reviewedPdfPages: chapter.sourcePages.length, nextPdfPage: chapter.sourcePages.length + 1, totalPdfPages: 336, complete: false};
  chapter.description = 'Original textbook content is being reviewed in PDF page order. Source-reviewed pages have separate PDF and printed page references; later content awaits review.';
  const reviewedSections = new Map();
  for (const page of chapter.sourcePages) {
    for (const exercise of page.exercises || []) {
      const existing = chapter.exercises.find(item => item.exercise === exercise.exercise);
      if (existing) {
        for (const key of Object.keys(existing)) delete existing[key];
        Object.assign(existing, exercise);
      } else chapter.exercises.push(exercise);
    }
    for (const example of page.workedExamples || []) {
      const existing = chapter.workedExamples.find(item => item.id === example.id);
      if (existing) {
        for (const key of Object.keys(existing)) delete existing[key];
        Object.assign(existing, example);
      } else chapter.workedExamples.push(example);
    }
    for (const fragment of page.sections || []) {
      if (!reviewedSections.has(fragment.id)) reviewedSections.set(fragment.id, {id: fragment.id, title: fragment.title, sourceBlocks: [], sourcePages: [], sourcePdfPages: []});
      const section = reviewedSections.get(fragment.id);
      section.sourceBlocks.push(...fragment.blocks);
      section.sourcePages.push(page.printedPage);
      section.sourcePdfPages.push(page.pdfPage);
    }
  }
  for (const section of reviewedSections.values()) {
    const existing = chapter.sections.find(item => item.id === section.id);
    section.theory = section.sourceBlocks.map(block => block.text || ((block.matrices || []).map(matrix => JSON.stringify(matrix)).join(' ') + (block.suffix || ''))).filter(Boolean).join('\n\n');
    section.rules = [];
    if (existing) Object.assign(existing, section);
    else chapter.sections.unshift(section);
  }
})();
'''
    data.write_text(text, encoding='utf-8')
    PROGRESS.write_text(json.dumps(dict(agent=1, textbook='Class 9 Mathematics', source=str(SOURCE),
        totalPdfPages=336, currentChapter=page.get('chapter','Front matter'), lastFullyCompletedPdfPage=page['pdfPage'],
        printedPage=page['printedPage'], pagesCompleted=len(entries), unresolvedIssues=[], nextPdfPage=len(entries)+1,
        class10Status='Not started; Class 9 must finish first'), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def render(number):
    folder = ROOT / 'tmp/math-agent1'
    folder.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as doc:
        doc[number-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(folder / f'page{number:03}.png')

def crop(number, name, bounds):
    folder = ROOT / 'assets/math9-agent1'
    folder.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as doc:
        page = doc[number-1]
        w, h = page.rect.width, page.rect.height
        rect = pymupdf.Rect(bounds[0]*w,bounds[1]*h,bounds[2]*w,bounds[3]*h)
        page.get_pixmap(matrix=pymupdf.Matrix(2,2),clip=rect).save(folder / name)
    return 'assets/math9-agent1/'+name

if __name__ == '__main__':
    import sys
    render(int(sys.argv[1]))
