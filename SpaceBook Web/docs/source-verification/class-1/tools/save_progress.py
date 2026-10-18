"""Write docs/source-verification/class-1/progress.json from the per-book ledgers.

Usage: python save_progress.py [--next "exact next action"]
Ledgers are written by build_book1.py; timing samples come from <subj>/timing.log (ISO time, reviewed pages).
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_book1 import SUBJECTS, SOURCES, JPG_ROOT

ORDER = ['math', 'eng', 'isl', 'nazira', 'pashto', 'drawing']
MISSING = [
    {'subject': 'Urdu (اردو)', 'status': 'MISSING SOURCE', 'note': r'No Class 1 Urdu textbook in D:\SpaceBook\Books\1st; legacy cls1-urdu entry left unchanged.'},
    {'subject': 'General Knowledge (واقفیتِ عامہ)', 'status': 'MISSING SOURCE', 'note': r'No Class 1 General Knowledge textbook in D:\SpaceBook\Books\1st; legacy cls1-gk entry left unchanged.'},
]


def speed(code):
    tl = HERE / code / 'timing.log'
    if not tl.exists():
        return None
    rows = [l.split('\t') for l in tl.read_text(encoding='utf-8').splitlines() if l]
    if len(rows) < 2:
        return None
    t0, t1 = datetime.datetime.fromisoformat(rows[0][0]), datetime.datetime.fromisoformat(rows[-1][0])
    h = (t1 - t0).total_seconds() / 3600
    return round((int(rows[-1][1]) - int(rows[0][1])) / h, 1) if h > 0 else None


def book(code):
    name, out, glob_, title = SUBJECTS[code]
    total = len(list((JPG_ROOT / code).glob('[0-9][0-9][0-9].jpg')))
    lf = HERE / code / 'ledger.json'
    rec = {'subject': name, 'code': code, 'title': title, 'source': SOURCES[code], 'scanFolder': str(JPG_ROOT / code),
           'appFile': 'js/' + out, 'totalSourcePages': total or None, 'classVerified': None}
    if not lf.exists():
        rec['status'] = 'not started'
        return rec
    ledger = json.loads(lf.read_text(encoding='utf-8'))
    done = [m['pdfPage'] for m in ledger]
    printed = [m['printedPage'] for m in ledger if m['printedPage'] is not None]
    rec.update({
        'classVerified': 'Class 1 (cover/title page checked)',
        'status': 'complete' if total and len(done) >= total else 'in progress',
        'reviewedPages': len(done),
        'implementedPages': len([m for m in ledger if m['status'] not in ('blank', 'duplicate')]),
        'correctedPages': len([m for m in ledger if m['status'] not in ('blank', 'duplicate')]),
        'verifiedUnchangedPages': 0,
        'printedPagesCovered': f'{min(printed)}-{max(printed)}' if printed else None,
        'excludedNonInstructional': [m['pdfPage'] for m in ledger if m['status'] == 'blank'],
        'duplicatePages': [m['pdfPage'] for m in ledger if m['status'] == 'duplicate'],
        'figures': sum(m['svg'] for m in ledger),
        'lastSavedPdfPage': max(done) if done else None,
        'nextPdfPage': (max(done) + 1) if done and total and len(done) < total else None,
        'currentUnit': ledger[-1]['unit'] if ledger else None, 'currentSection': ledger[-1]['section'] if ledger else None,
        'unresolved': [{'pdfPage': m['pdfPage'], 'printedPage': m['printedPage'], 'issues': m['issues']} for m in ledger if m['issues']],
        'untranslatedBlocks': [{'pdfPage': m['pdfPage'], 'text': m['untranslated']} for m in ledger if m['untranslated']],
        'pagesPerHour': speed(code),
        'ledger': f'docs/source-verification/class-1/{code}/ledger.json',
        'transcriptions': f'docs/source-verification/class-1/{code}/pages/pNNN.txt (NNN = scan index = PDF page - 1)',
    })
    return rec


def main():
    args = sys.argv[1:]
    nxt = args[args.index('--next') + 1] if '--next' in args else None
    f = HERE / 'progress.json'
    old = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {}
    data = {
        'class': 1,
        'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'sourceDirectory': r'D:\SpaceBook\Books\1st',
        'pipeline': ('Page DSL (docs/source-verification/class-1/<subj>/pages/pNNN.txt) -> tools/build_book1.py -> '
                     'js/<name>_1_book.js (window.CLS1_BOOKS) -> js/cls1_book_reader.js (shared MATH6_READER renderer). '
                     'Figures: tools/figs1.py (counting icons drawn in exact quantities). index.html wiring: tools/wire_index.py (shared lock).'),
        'note': ('Legacy Class 1 files (js/*_1_data.js) are untouched and backed up in legacy-backup/; the reader switches a subject '
                 'to the rebuilt book only when its js/<name>_1_book.js is loaded. Exercise item numbers are SpaceBook labels where the book '
                 'prints none; all answers are SpaceBook answers (the book has no answer key) and are labelled as not printed in the textbook.'),
        'order': ['Mathematics', 'English', 'Urdu', 'General Knowledge', 'Islamyat', 'Nazira-Quran', 'Pashto', 'Drawing'],
        'missingSources': MISSING,
        'books': [book(c) for c in ORDER],
        'browserTesting': 'Not performed by the agent (user instruction); data-load checks via tools/check1.js.',
        'nextAction': nxt or old.get('nextAction'),
    }
    tmp = f.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    json.loads(tmp.read_text(encoding='utf-8'))
    tmp.replace(f)
    print('saved', f, [(b['code'], b.get('reviewedPages', 0)) for b in data['books']])


if __name__ == '__main__':
    main()
