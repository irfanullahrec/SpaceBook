"""Write docs/source-verification/class-6/progress.json: Class 6 source inventory and verification status.

Usage: save_progress.py [--next "exact next action"]
Timing samples are appended by build runs to math/timing.log (ISO time, reviewed pages).
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
BOOKS = Path(r'D:\SpaceBook\Books\6th')
ORDER = ['Math', 'English', 'General science', 'Urdu', 'Computer', 'Geography', 'History', 'Islamiat', 'M-Q',
         'Arabic', 'Drawing', 'Hpe', 'Pashto']
NAMES = {'Math': 'Mathematics', 'General science': 'General Science', 'Computer': 'Computer Science', 'M-Q': 'Mutalia-e-Quran',
         'Hpe': 'Health & Physical Education'}
APP_FILES = {'Math': 'js/math_6_data.js', 'English': 'js/english_6_data.js', 'General science': 'js/general_science_6_data.js',
             'Urdu': 'js/urdu_6_data.js', 'Computer': 'js/computer_6_data.js', 'Geography': 'js/geography_6_data.js',
             'History': 'js/history_6_data.js', 'Islamiat': 'js/islamiat_6_data.js', 'M-Q': 'js/mutalia_quran_6_data.js',
             'Arabic': 'js/arabic_6_data.js', 'Drawing': 'js/drawing_6_data.js', 'Hpe': 'js/hpe_6_data.js', 'Pashto': 'js/pashto_6_data.js'}


SUBJ = {'English': 'eng', 'General science': 'sci', 'Urdu': 'urdu', 'Computer': 'comp', 'Geography': 'geo', 'History': 'hist',
        'Islamiat': 'isl', 'M-Q': 'quran', 'Arabic': 'arabic', 'Drawing': 'drawing', 'Hpe': 'hpe', 'Pashto': 'pashto'}


def book_status(key, n):
    code = SUBJ[key]
    lf = HERE / code / 'ledger.json'
    if not lf.exists():
        return {}
    ledger = json.loads(lf.read_text(encoding='utf-8'))
    total = len(list(Path('D:/SpaceBook/_cls6_jpg', code).glob('[0-9][0-9][0-9].jpg'))) or n
    done = [m['pdfPage'] for m in ledger]
    speed = None
    tl = HERE / code / 'timing.log'
    if tl.exists():
        rows = [l.split('	') for l in tl.read_text(encoding='utf-8').splitlines() if l]
        if len(rows) >= 2:
            t0, t1 = datetime.datetime.fromisoformat(rows[0][0]), datetime.datetime.fromisoformat(rows[-1][0])
            h = (t1 - t0).total_seconds() / 3600
            speed = round((int(rows[-1][1]) - int(rows[0][1])) / h, 1) if h > 0 else None
    return {'status': 'complete' if len(done) >= total else 'in progress', 'totalPages': total,
            'reviewedPages': len(done), 'correctedPages': len([m for m in ledger if m['status'] != 'blank']),
            'lastCompletedPdfPage': max(done) if done else None,
            'nextPdfPage': (max(done) + 1) if done and len(done) < total else None,
            'currentUnit': ledger[-1]['unit'] if ledger else None,
            'unresolvedPages': [{'pdfPage': m['pdfPage'], 'issues': m['issues']} for m in ledger if m['issues']],
            'lowOcrAgreementPages': [{'pdfPage': m['pdfPage'], 'ocrWordRecall': m['ocrWordRecall']} for m in ledger
                                     if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85],
            'pagesPerHour': speed,
            'ledger': f'docs/source-verification/class-6/{code}/ledger.json',
            'transcriptions': f'docs/source-verification/class-6/{code}/pages/pNNN.txt (NNN = scan index = PDF page - 1)',
            'note': 'Rebuilt page by page from the scans by tools/build_book6.py; the old generic dataset was replaced.'}


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
        rec = {'subject': NAMES.get(key, key), 'sourceFolder': str(BOOKS / key), 'pageImages': jpg, 'pdfFiles': pdfs,
               'totalPages': n, 'appFile': APP_FILES[key], 'status': 'not started (waits for Mathematics to finish)',
               'reviewedPages': 0, 'correctedPages': 0, 'unresolvedPages': []}
        if key == 'Math':
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
                'ledger': 'docs/source-verification/class-6/math/ledger.json',
                'transcriptions': 'docs/source-verification/class-6/math/pages/pNNN.txt (NNN = JPG index = PDF page - 1)',
                'note': 'Previous js/math_6_data.js held generic placeholder text and invented Q&A; it is being replaced page by page from the scans.'})
        if key in SUBJ:
            rec.update(book_status(key, n))
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
        'class': 6, 'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'order': 'Mathematics first; then English, General Science, Urdu, Computer Science, Geography, History, Islamiat, Mutalia-e-Quran, Arabic, Drawing, HPE, Pashto',
        'note': 'No separate Social Studies textbook exists in the Class 6 source folder (Geography and History are separate books).',
        'subjects': subjects,
        'speed': {'pagesPerHourOverall': speed, 'samples': len(timing),
                  'benchmarkFirst10Pages': old.get('speed', {}).get('benchmarkFirst10Pages')},
        'nextAction': nxt or old.get('nextAction'),
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for m in subjects:
        if m['reviewedPages']:
            print(f"{m['subject']} {m['reviewedPages']}/{m['totalPages']} pages ({m['status']})")


if __name__ == '__main__':
    main()
