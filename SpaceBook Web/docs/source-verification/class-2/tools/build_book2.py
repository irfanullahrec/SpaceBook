"""Build a Class 2 textbook (any subject, Mathematics included) from its page-by-page transcriptions.

    python docs/source-verification/class-2/tools/build_book2.py SUBJ   (SUBJ: math, eng, sci, sst, sstum, isl, pashto, urdu)

Pages:   docs/source-verification/class-2/<SUBJ>/pages/pNNN.txt  (NNN = 0-based scan index; PDF page = NNN + 1)
Scans:   D:/SpaceBook/_cls2_jpg/<SUBJ>/NNN.jpg  (hard links to Books/2nd JPGs in part order; map.tsv lists each index's source file)
Units:   <SUBJ>/units.tsv  (number, EN, UR, PS, first printed page, optional label) from the book's contents page.
Output:  js/<name>_2_data.js — keeps the legacy global (e.g. MATH_4_DATA) and registers window.CLS2_BOOKS[SUBJ]
         for js/cls2_page_reader.js. Answers/solutions go to window.CLS6_SOLUTIONS under 'c3<subj>-sN' ids
         (the shared math6_reader looks answers up there).

Page syntax: as documented in build_math6.py (copied here unchanged), plus
  @tab NAME        the current section also appears in subject tab NAME (grammar, vocabulary, ...)
  sol ANSWER ## EN || UR || PS     SpaceBook answer for the last question/part (shown behind a button)
"""
from pathlib import Path
import json, re, sys, datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_math6 as bm

HERE = bm.HERE          # docs/source-verification/class-2
APP = bm.APP            # SpaceBook Web
SUBJECTS = {
    'math': ('Mathematics', 'math_2_data.js', 'MATH_2_DATA', 'Mathematics 2 (KPTBB, Curriculum 2020)'),
    'eng': ('English', 'english_2_data.js', 'ENGLISH_2_DATA', 'English 2 (KPTBB)'),
    'urdu': ('Urdu', 'urdu_2_data.js', 'URDU_2_DATA', 'Urdu 2 (KPTBB)'),
    'gk': ('General Knowledge', 'gk_2_data.js', 'GK_2_DATA', 'General Knowledge 2 (KPTBB)'),
    'isl': ('Islamiat', 'islamyat_2_data.js', 'ISLAMYAT_2_DATA', 'Islamiat 2 (KPTBB)'),
    'nazira': ('Nazira Quran', 'nazira_2_data.js', 'NAZIRA_2_DATA', 'Nazira Quran 2 (KPTBB)'),
    'pashto': ('Pashto', 'pashto_2_data.js', 'PASHTO_2_DATA', 'Pashto 2 (KPTBB)'),
    'drawing': ('Drawing', 'drawing_2_data.js', 'DRAWING_2_DATA', 'Drawing 2 (KPTBB)'),
}
SOURCES = {
    'math': 'D:/SpaceBook/Books/2nd/2nd Maths/JPG (168 scans in two parts; PDF "Math Book for 2 class KPTBB.pdf" has 167 pages)',
    'eng': 'D:/SpaceBook/Books/2nd/2nd English/JPG (138 scans in two parts)',
    'urdu': 'D:/SpaceBook/Books/2nd/2nd Urdu/JPG (117 scans in two parts)',
    'gk': 'D:/SpaceBook/Books/2nd/2nd GK/JPG (103 scans in two parts)',
    'isl': 'D:/SpaceBook/Books/2nd/2nd Islamyat/JPG (58 scans)',
    'nazira': 'D:/SpaceBook/Books/2nd/2nd Nazira/JPG (91 scans in two parts)',
    'pashto': 'D:/SpaceBook/Books/2nd/2nd Pashto/JPG (64 scans)',
    'drawing': 'D:/SpaceBook/Books/2nd/2nd Drawing/JPG (34 scans)',
}
JPG_ROOT = Path('D:/SpaceBook/_cls2_jpg')
# Slot order of "original || translation || translation" for books not printed in English.
LANGS = {'urdu': ['ur', 'en', 'ps'], 'isl': ['ur', 'en', 'ps'], 'nazira': ['ur', 'en', 'ps'], 'pashto': ['ps', 'ur', 'en']}
IGNORE = {'not', 'for', 'sale', 'downloaded', 'from', 'awazeinqilab', 'com', 'download', 'millions', 'mcqs', 'books',
          'notes', 'any', 'subject', 'website', 'awaz', 'inqilab', 'free', 'government'}


class BookBuilder(bm.Builder):
    def page(self, idx, text):
        keep = []
        for line in text.splitlines():
            s = line.strip()
            keep.append('// TAB ' + s[5:].strip() if s.startswith('@tab ') else line)
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
    f = HERE / subj / 'vocab.tsv'
    if f.exists():
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
    if not f.exists() or subj in LANGS:
        return None
    ocr = ' '.join(l['text'] for l in json.loads(f.read_text(encoding='utf-8'))['lines'] if l['conf'] > 0.8)
    src = [w for w in re.findall(r'[a-z]{3,}', ocr.lower()) if w not in IGNORE]
    if len(src) < 8:
        return None
    stream = re.sub(r'[^a-z]', '', ' '.join(english).lower())
    return round(sum(1 for w in src if w in stream) / len(src), 3)


def main():
    subj = sys.argv[1]
    name, out_file, global_name, title = SUBJECTS[subj]
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
    def resolve(list_):
        for x in list_:
            if x.get('t') == 'q' and x.get('solveParts'):
                kind, *args = x.pop('solveParts')
                for part in x['parts']:
                    if 'sol' not in part:
                        part['sol'] = bm.solve.generate(kind, part['en'], *args)
            if x.get('blocks'):
                resolve(x['blocks'])
    for u in b.units.values():
        for s_ in u['sections']:
            resolve(s_['blocks'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c2{subj}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    units = [b.units[n] for n in sorted(b.units)]
    # <SUBJ>/missing.tsv: n \t slot1 \t slot2 \t slot3 — notice shown for a unit whose pages are absent from every source
    mf = HERE / subj / 'missing.tsv'
    if mf.exists():
        for line in mf.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            n, a, c, d = (line.split('\t') + [''] * 4)[:4]
            u = b.units.get(int(n))
            if u is None or u['sections']:
                continue
            note = {'t': 'box', 'kind': 'note', 'title': {'en': a.split(' :: ')[0], 'ur': c.split(' :: ')[0], 'ps': d.split(' :: ')[0]},
                    'blocks': [{'t': 'p', 'en': a.split(' :: ')[-1], 'ur': c.split(' :: ')[-1], 'ps': d.split(' :: ')[-1]}]}
            u['sections'].append({'id': f'{u["id"]}-missing', 'title': u['title'], 'titleUrdu': u['titleUrdu'],
                                  'titlePashto': u['titlePashto'], 'blocks': [note], 'sourcePdfPages': [], 'sourcePrintedPages': []})
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
    book = {'subject': subj, 'name': name, 'title': title, 'source': SOURCES[subj], 'totalPdfPages': total,
            'reviewedPdfPages': reviewed, 'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers,
            'answerPdfPages': b.answer_pages, 'complete': reviewed >= total}
    if subj in LANGS:
        book['langs'] = LANGS[subj]
    js = [f'// Class 2 {name} (KPTBB) — generated by docs/source-verification/class-2/tools/build_book2.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + json.dumps(units, ensure_ascii=False) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS2_BOOKS = window.CLS2_BOOKS || {};',
          f'  window.CLS2_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + json.dumps(book, ensure_ascii=False) + ', words: ' + json.dumps(words, ensure_ascii=False) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + json.dumps(solutions, ensure_ascii=False) + ');',
          '}', '']
    out = APP / 'js' / out_file
    tmp = out.with_suffix('.js.tmp')
    tmp.write_text('\n'.join(js), encoding='utf-8')
    tmp.replace(out)
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    low = [(m['pdfPage'] - 1, m['ocrWordRecall']) for m in b.ledger if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85]
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if bm.ANSWER_WARNINGS:
        print('ANSWER WARNINGS:', bm.ANSWER_WARNINGS)
    if low:
        print('LOW OCR RECALL (scan idx, recall):', low)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
