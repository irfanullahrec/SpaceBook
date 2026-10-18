"""Build a Class 6 (non-Mathematics) textbook from its page-by-page transcriptions.

    python tools/build_book6.py SUBJ        (SUBJ: eng, sci, urdu, comp, geo, hist, isl, quran, arabic, drawing, hpe, pashto)

Pages:   docs/source-verification/class-6/<SUBJ>/pages/pNNN.txt  (NNN = 0-based scan index; PDF page = NNN + 1)
Scans:   D:/SpaceBook/_cls6_jpg/<SUBJ>/NNN.jpg  (hard links to the original Books/6th/<Subject>/JPG files)
Units:   <SUBJ>/units.tsv  (number, EN, UR, PS, first printed page) taken from the book's contents page,
         so the chapter list is complete even before every unit is reviewed.
Output:  js/<legacy>_6_data.js  — rewrites the existing Class 6 dataset (same global name, legacy fields kept
         for search) and registers window.CLS6_BOOKS[SUBJ] for js/cls6_book_reader.js.

The page syntax is the one documented in build_math6.py, plus:
  @tab NAME        the current section also appears in subject tab NAME (grammar, writing, vocabulary, ...)
  sol ANSWER ## EN || UR || PS     answer for the last question/part (shown behind a button)
"""
from pathlib import Path
import json, re, sys, datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_math6 as bm

HERE = bm.HERE
APP = bm.APP
SUBJECTS = {
    'eng': ('English', 'english_6_data.js', 'ENGLISH_6_DATA', 'English 6 (KPTBB, NC 2022, Test Edition)'),
    'sci': ('General Science', 'general_science_6_data.js', 'GENERAL_SCIENCE_6_DATA', 'General Science 6 (KPTBB, NC 2022)'),
    'urdu': ('Urdu', 'urdu_6_data.js', 'URDU_6_DATA', 'Urdu 6 (KPTBB, NC 2022)'),
    'comp': ('Computer Science', 'computer_6_data.js', 'COMPUTER_6_DATA', 'Computer Science 6 (KPTBB, NC 2022)'),
    'geo': ('Geography', 'geography_6_data.js', 'GEOGRAPHY_6_DATA', 'Geography 6 (KPTBB, NC 2022)'),
    'hist': ('History', 'history_6_data.js', 'HISTORY_6_DATA', 'History 6 (KPTBB, NC 2022)'),
    'isl': ('Islamiat', 'islamiat_6_data.js', 'ISLAMIAT_6_DATA', 'Islamiat 6 (KPTBB, NC 2022)'),
    'quran': ('Mutalia-e-Quran', 'mutalia_quran_6_data.js', 'MUTALIA_QURAN_6_DATA', 'Mutalia-e-Quran 6 (KPTBB, NC 2022)'),
    'arabic': ('Arabic', 'arabic_6_data.js', 'ARABIC_6_DATA', 'Arabic 6 (KPTBB, NC 2022)'),
    'drawing': ('Drawing', 'drawing_6_data.js', 'DRAWING_6_DATA', 'Drawing 6 (KPTBB, NC 2022)'),
    'hpe': ('Health & Physical Education', 'hpe_6_data.js', 'HPE_6_DATA', 'Health & Physical Education 6 (KPTBB, NC 2022)'),
    'pashto': ('Pashto', 'pashto_6_data.js', 'PASHTO_6_DATA', 'Pashto 6 (KPTBB, NC 2022)'),
}
JPG_ROOT = Path('D:/SpaceBook/_cls6_jpg')
# Order of the three slots in "original || translation || translation" for books not printed in English.
LANGS = {'urdu': ['ur', 'en', 'ps'], 'isl': ['ur', 'en', 'ps'], 'quran': ['ur', 'en', 'ps'], 'arabic': ['ur', 'en', 'ps'], 'hpe': ['ur', 'en', 'ps'], 'pashto': ['ps', 'en', 'ur']}


class BookBuilder(bm.Builder):
    def page(self, idx, text):
        # @tab is the only directive the math builder does not know; strip it here and record it on the section.
        keep = []
        for line in text.splitlines():
            s = line.strip()
            if s.startswith('@tab '):
                keep.append('// TAB ' + s[5:].strip())
            else:
                keep.append(line)
        tabs = [l[7:] for l in keep if l.startswith('// TAB ')]
        super().page(idx, '\n'.join(keep))
        if tabs and self.section is not None:
            for t in tabs:
                self.section.setdefault('tabs', [])
                if t not in self.section['tabs']:
                    self.section['tabs'].append(t)


def load_units(subj):
    f = HERE / subj / 'units.tsv'
    titles, starts, labels = {}, {}, {}
    if f.exists():
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            n, en, ur, ps, start, label = (line.split('\t') + [''] * 6)[:6]
            titles[int(n)] = (en.strip(), ur.strip(), ps.strip())
            if label.strip():
                labels[int(n)] = label.strip()
            starts[int(n)] = int(start) if start.strip().isdigit() else None
    return titles, starts, labels


def load_vocab(subj):
    words = {}
    for f in (HERE / subj / 'vocab.tsv', HERE / 'shared_vocab.tsv'):
        if not f.exists():
            continue
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 3:
                raise SystemExit(f'bad vocab line in {f.name}: {line}')
            words.setdefault(parts[0].strip().lower(), [parts[1].strip(), parts[2].strip()])
    return words


def ocr_recall(subj, idx, english):
    f = HERE / subj / 'ocr' / f'{idx:03}.json'
    if not f.exists():
        return None
    ocr = ' '.join(l['text'] for l in json.loads(f.read_text(encoding='utf-8'))['lines'] if l['conf'] > 0.8)
    if subj in LANGS:
        return None  # the cached OCR is English-only; Arabic-script pages are checked against the scan by eye
    src = [w for w in re.findall(r'[a-z]{3,}', ocr.lower()) if w not in IGNORE]
    if len(src) < 8:
        return None
    stream = re.sub(r'[^a-z]', '', ' '.join(english).lower())
    return round(sum(1 for w in src if w in stream) / len(src), 3)


IGNORE = {'not', 'for', 'sale', 'downloaded', 'from', 'awazeinqilab', 'com', 'download', 'millions', 'mcqs', 'books',
          'notes', 'any', 'subject', 'website', 'awaz', 'inqilab', 'free', 'government'}


def main():
    subj = sys.argv[1]
    name, legacy_file, global_name, title = SUBJECTS[subj]
    total = len(list((JPG_ROOT / subj).glob('[0-9][0-9][0-9].jpg')))
    titles, starts, labels = load_units(subj)
    b = BookBuilder(titles, starts)
    files = sorted((HERE / subj / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        b.page(expected, f.read_text(encoding='utf-8'))
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'{subj}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        for s_ in u['sections']:
            extract(s_['blocks'])
    words = load_vocab(subj)
    for m in b.ledger:
        m['ocrWordRecall'] = None if m['status'] in ('duplicate', 'blank', 'answers') else ocr_recall(subj, m['pdfPage'] - 1, m['english'])
        m.pop('english')
    for u in units:
        if u['number'] in labels:
            u['order'], u['number'] = u['number'], labels[u['number']]
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        for s in u['sections']:
            paras = [x.get('en', '') for x in s['blocks'] if x['t'] in ('h', 'p')]
            s['heading'] = s['title']
            s['headingUrdu'] = s['titleUrdu']
            s['paras'] = paras
            s['text'] = '\n\n'.join(paras)[:6000]
    reviewed = len(b.ledger)
    book = {'subject': subj, 'name': name, 'title': title, 'source': str(JPG_ROOT / subj), 'totalPdfPages': total,
            'reviewedPdfPages': reviewed, 'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers,
            'answerPdfPages': b.answer_pages, 'complete': reviewed >= total}
    if subj in LANGS:
        book['langs'] = LANGS[subj]
    js = [f'// Class 6 {name} (KPTBB) — generated by docs/source-verification/class-6/tools/build_book6.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + json.dumps(units, ensure_ascii=False) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS6_BOOKS = window.CLS6_BOOKS || {};',
          f'  window.CLS6_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + json.dumps(book, ensure_ascii=False) + ', words: ' + json.dumps(words, ensure_ascii=False) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + json.dumps(solutions, ensure_ascii=False) + ');',
          '}', '']
    out = APP / 'js' / legacy_file
    out.write_text('\n'.join(js), encoding='utf-8')
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    low = [(m['pdfPage'] - 1, m['ocrWordRecall']) for m in b.ledger if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85]
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if low:
        print('LOW OCR RECALL (scan idx, recall):', low)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
