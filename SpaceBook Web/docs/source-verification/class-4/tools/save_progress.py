"""Write docs/source-verification/class-4/progress.json from the per-book ledgers.

Usage: python save_progress.py [--next "exact next action"] [--browser "verification note"]
Ledgers are written by build_book4.py; timing samples come from <subj>/timing.log (ISO time, reviewed pages).
The previous (pre-rebuild) progress.json is kept in legacy-backup/progress.json.
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_book4 import SUBJECTS, SOURCES, JPG_ROOT

ORDER = ['math', 'eng', 'urdu', 'sci', 'sst', 'sstum', 'isl', 'pashto']
NOT_AVAILABLE = ['General Knowledge (no separate book; the General Science PDF set has "general knowledge" split files of the same book)',
                 'Computer Science', 'Mutalia-e-Quran', 'Geography', 'History', 'Arabic', 'Drawing / Art',
                 'Health and Physical Education']


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
           'appFile': 'js/' + out, 'totalSourcePages': total or None}
    if not lf.exists():
        rec['status'] = 'not started'
        return rec
    ledger = json.loads(lf.read_text(encoding='utf-8'))
    done = [m['pdfPage'] for m in ledger]
    printed = [m['printedPage'] for m in ledger if m['printedPage'] is not None]
    rec.update({
        'status': 'complete' if total and len(done) >= total else 'in progress',
        'reviewedPages': len(done), 'implementedPages': len([m for m in ledger if m['status'] not in ('blank', 'duplicate')]),
        'printedPagesCovered': f'{min(printed)}-{max(printed)}' if printed else None,
        'blankOrAdPages': [m['pdfPage'] for m in ledger if m['status'] == 'blank'],
        'duplicatePages': [m['pdfPage'] for m in ledger if m['status'] == 'duplicate'],
        'lastSavedPdfPage': max(done) if done else None,
        'nextPdfPage': (max(done) + 1) if done and total and len(done) < total else None,
        'currentUnit': ledger[-1]['unit'] if ledger else None, 'currentSection': ledger[-1]['section'] if ledger else None,
        'unresolved': [{'pdfPage': m['pdfPage'], 'printedPage': m['printedPage'], 'issues': m['issues']} for m in ledger if m['issues']],
        'untranslatedBlocks': [{'pdfPage': m['pdfPage'], 'text': m['untranslated']} for m in ledger if m['untranslated']],
        'pagesPerHour': speed(code),
        'ledger': f'docs/source-verification/class-4/{code}/ledger.json',
        'transcriptions': f'docs/source-verification/class-4/{code}/pages/pNNN.txt (NNN = scan index = PDF page - 1)',
    })
    return rec


def main():
    args = sys.argv[1:]
    nxt = args[args.index('--next') + 1] if '--next' in args else None
    browser = args[args.index('--browser') + 1] if '--browser' in args else None
    f = HERE / 'progress.json'
    old = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {}
    data = {
        'class': 4,
        'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'sourceDirectory': r'D:\SpaceBook\Books\4th\4th',
        'pipeline': 'Page DSL (docs/source-verification/class-4/<subj>/pages/pNNN.txt) -> tools/build_book4.py -> js/<name>_4_data.js -> js/cls4_book_reader.js (uses the shared Class 6 renderer MATH6_READER).',
        'note': ('Class 4 is being rebuilt page by page from the scans. The earlier Class 4 datasets (backed up in legacy-backup/) '
                 'were generated from Word OCR with placeholder answers and untranslated "translations"; their "verified" status was not supported by the content.'),
        'order': [SUBJECTS[c][0] for c in ORDER],
        'subjectsNotInSourceFolder': NOT_AVAILABLE,
        'books': [book(c) for c in ORDER],
        'lastBrowserVerification': browser or old.get('lastBrowserVerification'),
        'environmentBlockers': ['Machine RAM nearly exhausted (about 0.4 GB free, page file full on C:): RapidOCR batch OCR fails with allocation errors, so pages are transcribed by reading the scan images directly.'],
        'nextAction': nxt or old.get('nextAction'),
    }
    tmp = f.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    json.loads(tmp.read_text(encoding='utf-8'))
    tmp.replace(f)
    print('saved', f, [(b['code'], b.get('reviewedPages', 0)) for b in data['books']])


if __name__ == '__main__':
    main()
