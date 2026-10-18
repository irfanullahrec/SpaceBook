"""Write docs/source-verification/class-7/progress.json: Class 7 source inventory and verification status.

Usage: save_progress.py [--next "exact next action"]
Timing samples are appended by build runs to math/timing.log (ISO time, reviewed pages).
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
BOOKS = Path('D:/SpaceBook/Books/7th')
ORDER = ['7th MAths', '7th English', '7th General Science', '7th Urdu', '7th CS', '7th Geography', '7th History',
         '7th Islamiat', '7th M Q', '7th Arabi', '7th Drawing', '7th HPE', '7th PAshto']
NAMES = {'7th MAths': 'Mathematics', '7th English': 'English', '7th General Science': 'General Science', '7th Urdu': 'Urdu',
         '7th CS': 'Computer Science', '7th Geography': 'Geography', '7th History': 'History', '7th Islamiat': 'Islamiat',
         '7th M Q': 'Mutalia-e-Quran', '7th Arabi': 'Arabic', '7th Drawing': 'Drawing', '7th HPE': 'Health & Physical Education',
         '7th PAshto': 'Pashto'}
APP_FILES = {'7th MAths': 'js/math_7_data.js', '7th English': 'js/english_7_data.js', '7th General Science': 'js/general_science_7_data.js',
             '7th Urdu': 'js/urdu_7_data.js', '7th CS': 'js/computer_7_data.js', '7th Geography': 'js/geography_7_data.js',
             '7th History': 'js/history_7_data.js', '7th Islamiat': 'js/islamiat_7_data.js', '7th M Q': 'js/mutalia_quran_7_data.js',
             '7th Arabi': 'js/arabic_7_data.js', '7th Drawing': 'js/drawing_7_data.js', '7th HPE': 'js/hpe_7_data.js', '7th PAshto': 'js/pashto_7_data.js'}

BOOK_DIRS = {'7th English': 'eng', '7th General Science': 'sci', '7th Urdu': 'urdu', '7th CS': 'comp', '7th Geography': 'geo',
             '7th History': 'hist', '7th Islamiat': 'isl', '7th M Q': 'quran', '7th Arabi': 'arabic', '7th Drawing': 'drawing',
             '7th HPE': 'hpe', '7th PAshto': 'pashto'}
VERIFIED = {'7th English': '2026-10-10', '7th General Science': '2026-10-11', '7th Urdu': '2026-10-11', '7th Computer': '2026-10-11', '7th Geography': '2026-10-11', '7th History': '2026-10-11', '7th Islamiat': '2026-10-11', '7th M Q': '2026-10-11', '7th Arabi': '2026-10-11', '7th Drawing': '2026-10-11', '7th HPE': '2026-10-12'}


def pages_of(folder):
    jpg = folder / 'JPG'
    numbered = sorted(p for p in jpg.glob('*.jpg') if p.stem.isdigit()) if jpg.exists() else []
    pdfs = sorted(str(p) for d in folder.iterdir() if d.is_dir() and d.name.lower().startswith('pdf') for p in d.glob('*.pdf'))
    return len(numbered), str(jpg), pdfs


def main():
    nxt = sys.argv[sys.argv.index('--next') + 1] if '--next' in sys.argv else None
    out_path = HERE / 'progress.json'
    old = json.loads(out_path.read_text(encoding='utf-8')) if out_path.exists() else {}
    subjects = []
    for key in ORDER:
        n, jpg, pdfs = pages_of(BOOKS / key)
        linked = Path('D:/SpaceBook/_cls7_jpg') / BOOK_DIRS.get(key, '-')
        if key != '7th MAths' and linked.exists():
            n = len(list(linked.glob('*.jpg')))
        rec = {'subject': NAMES.get(key, key), 'sourceFolder': str(BOOKS / key), 'pageImages': jpg, 'pdfFiles': pdfs,
               'totalPages': n, 'appFile': APP_FILES[key], 'status': 'not started (waits for Mathematics to finish)',
               'reviewedPages': 0, 'correctedPages': 0, 'unresolvedPages': []}
        if key == '7th MAths':
            ledger = json.loads((HERE / 'math' / 'ledger.json').read_text(encoding='utf-8'))
            done = [m['pdfPage'] for m in ledger]
            rec.update({
                'status': 'complete' if len(done) >= n else 'in progress',
                'reviewedPages': len(done), 'correctedPages': len([m for m in ledger if m['status'] != 'blank']),
                'lastCompletedPdfPage': max(done) if done else None,
                'lastCompletedPrintedPage': next((m['printedPage'] for m in reversed(ledger) if m['printedPage']), None),
                'nextPdfPage': (max(done) + 1) if done and len(done) < n else None,
                'currentUnit': ledger[-1]['unit'] if ledger else None, 'currentSection': ledger[-1]['section'] if ledger else None,
                'unresolvedPages': [{'pdfPage': m['pdfPage'], 'issues': m['issues']} for m in ledger if m['issues']],
                'lowOcrAgreementPages': [{'pdfPage': m['pdfPage'], 'ocrWordRecall': m['ocrWordRecall']} for m in ledger
                                         if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85 and m['status'] != 'blank'],
                'ledger': 'docs/source-verification/class-7/math/ledger.json',
                'transcriptions': 'docs/source-verification/class-7/math/pages/pNNN.txt (NNN = JPG index = PDF page - 1)',
                'note': 'Previous js/math_7_data.js was raw OCR text with recognition errors (e.g. "2" for the ≥ symbol, bullet glyphs, broken fractions) and no coded diagrams; it is being replaced page by page from the scans. Backup: docs/source-verification/class-7/math/legacy_math_7_data.js'})
        else:
            sub = BOOK_DIRS.get(key)
            lp = HERE / sub / 'ledger.json' if sub else None
            if lp and lp.exists():
                ledger = json.loads(lp.read_text(encoding='utf-8'))
                done = [m['pdfPage'] for m in ledger]
                verified = VERIFIED.get(key)
                rec.update({
                    'status': ('complete, browser verified ' + verified) if (verified and len(done) >= n) else
                              ('complete (awaiting browser check)' if len(done) >= n else 'in progress'),
                    'reviewedPages': len(done), 'correctedPages': len([m for m in ledger if m['status'] not in ('blank', 'duplicate')]),
                    'lastCompletedPdfPage': max(done) if done else None,
                    'nextPdfPage': (max(done) + 1) if done and len(done) < n else None,
                    'unresolvedPages': [{'pdfPage': m['pdfPage'], 'issues': m['issues']} for m in ledger if m['issues']],
                    'ledger': f'docs/source-verification/class-7/{sub}/ledger.json',
                    'transcriptions': f'docs/source-verification/class-7/{sub}/pages/pNNN.txt (NNN = JPG index)'})
            elif n == 0:
                rec['status'] = 'no source scans available'
            else:
                rec['status'] = 'not started'
        subjects.append(rec)
    timing = []
    tl = HERE / 'math' / 'timing.log'
    if tl.exists():
        for line in tl.read_text(encoding='utf-8').splitlines():
            t, n = line.split('\t')
            timing.append((datetime.datetime.fromisoformat(t), int(n)))
    speed = None
    if len(timing) >= 2:
        (t0, n0), (t1, n1) = timing[0], timing[-1]
        hours = (t1 - t0).total_seconds() / 3600
        speed = round((n1 - n0) / hours, 1) if hours > 0 else None
    data = {
        'class': 7, 'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'order': 'Mathematics first; then English, General Science, Urdu, Computer Science, Geography, History, Islamiat, Mutalia-e-Quran, Arabic, Drawing, HPE, Pashto',
        'note': 'No separate Social Studies textbook exists in the Class 7 source folder (Geography and History are separate books).',
        'subjects': subjects,
        'speed': {'pagesPerHourOverall': speed, 'samples': len(timing),
                  'benchmarkFirst10Pages': old.get('speed', {}).get('benchmarkFirst10Pages')},
        'nextAction': nxt or old.get('nextAction'),
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    m = subjects[0]
    print(f"Math {m['reviewedPages']}/{m['totalPages']} pages; speed {speed} pages/hour")


if __name__ == '__main__':
    main()
