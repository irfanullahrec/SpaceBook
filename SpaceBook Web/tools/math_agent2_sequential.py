"""Save only the current independently inspected Class 12 PDF page.

Reuses sourcePages; never regenerates other agents' content or old reports.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'js/math_12_data.js'
PROGRESS = ROOT / 'docs/source-verification/math-agent2-sequential.json'
PDF = 'Books/12th/12th Maths/PDF/Math Book for 12 class KPTBB.pdf'

def source_records(files):
    text = DATA.read_text(encoding='utf-8')
    marker = 'MATH_12_DATA[0].sourcePages = '
    start = text.index(marker) + len(marker)
    pages, _ = json.JSONDecoder().raw_decode(text[start:])
    return [next(item for item in pages if item['file'] == file).copy() for file in files]

def save_page(pdf_page, records, printed_pages, note=None):
    progress = json.loads(PROGRESS.read_text(encoding='utf-8')) if PROGRESS.exists() else {
        'agent': 'Mathematics Content Agent 2', 'classOrder': [12, 11],
        'freshPass': True, 'previousClaimsTrusted': False, 'currentClass': 12,
        'sourcePdf': PDF, 'sourcePdfPageCount': 180, 'completedPages': [],
        'unresolvedExtractionIssues': [], 'class11Status': 'not_started',
        'browserTesting': False,
    }
    assert pdf_page == len(progress['completedPages']) + 1, 'Must save consecutive PDF pages'
    text = DATA.read_text(encoding='utf-8')
    marker = 'MATH_12_DATA[0].sourcePages = '
    start = text.index(marker) + len(marker)
    pages, size = json.JSONDecoder().raw_decode(text[start:])
    refs = []
    for record in records:
        existing = next((item for item in pages if item.get('file') == record['file']), None)
        if existing is None:
            existing = record.copy()
            pages.append(existing)
        else:
            existing.update(record)
        existing['agent2Verification'] = {
            'sourcePdf': PDF, 'pdfPage': pdf_page,
            'printedPage': existing['page'], 'status': 'independently_inspected_and_saved',
        }
        refs.append(existing['file'])
    DATA.write_text(text[:start] + json.dumps(pages, ensure_ascii=False, indent=2) + text[start+size:], encoding='utf-8')
    progress['completedPages'].append({'pdfPage': pdf_page, 'printedPages': printed_pages, 'sourceRecords': refs, 'note': note})
    progress.update(currentChapter='Front matter' if pdf_page < 5 else 'Unit 1: Introduction to Symbolic Package, Maple', currentPdfPage=pdf_page,
                    lastFullyImplementedPdfPage=pdf_page, printedTextbookPageReference=printed_pages,
                    nextPage=pdf_page+1, status='in_progress')
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS.write_text(json.dumps(progress, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

if __name__ == '__main__':
    save_page(1, [{
        'file': '001_page_1.jpg', 'page': 'cover', 'title': 'A Textbook of Mathematics',
        'paragraphs': ['For Grade XII', 'Free From Government', 'NOT FOR SALE',
                       'Khyber Pakhtunkhwa Textbook Board, Peshawar.'],
        'visualStatus': 'Decorative cover artwork; no instructional diagram',
    }], ['cover'])
    save_page(2, [], [], 'Inserted distributor advertisement; inspected, contains no textbook educational content. Excluded from lessons and question banks.')
