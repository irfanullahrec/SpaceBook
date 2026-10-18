"""Build a Class 10 (non-Mathematics) textbook from its page-by-page transcriptions.

    python tools/build_book10.py SUBJ   (SUBJ: urdu, pak, comp, gensci, drawing, hpe, islx, quran, ...)

Same page syntax, builder and reader as the Class 6/8 books (class-6/tools/build_book6.py); registry window.CLS10_BOOKS,
rendered by js/cls6_book_reader.js for classId 'cls10'. Pages: class-10/<SUBJ>/pages/pNNN.txt, one file per PDF page in
source order (SOURCES below). Page totals come from the source PDFs; renders for reading live outside the repo.
"""
from pathlib import Path
import json, sys, datetime

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / 'class-6' / 'tools'))
import build_math6 as bm
import build_book6 as b6

APP = HERE.parents[2]
b6.HERE = HERE                     # load_units / load_vocab / ocr_recall read class-8/<subj>/...
SOURCES = {'urdu': [f'D:/SpaceBook/Books/10th/10 urdu/pdf/10th urdu{i}.pdf' for i in (1, 2, 3, 4)],
           'pakstudy': [f'D:/SpaceBook/Books/10th/10th pakstudy/pdf/{n}.pdf'
                        for n in ('10th pakstudy1', '10th pakstudy2', '10th pakstudy3', '10thpakstudy4')],
           'comp': ['D:/SpaceBook/Books/10th/10th CS/PDF/Computer-Science Book for 10 class KPTBB.pdf'],
           'sci': ['D:/SpaceBook/Books/10th/10th General Science/PDF/General Science 10th book EM.pdf'],
           'drawing': ['D:/SpaceBook/Books/10th/10th  Drawing/PDF/Drawing book 10th EM KPK.pdf'],
           'hpe': ['D:/SpaceBook/Books/10th/10th HPE/PDF/HPE book UM 10th class KPK.pdf'],
           'islopt': ['D:/SpaceBook/Books/10th/10th Ismaiat Ikhtiari/PDF/Islamiat Elective book 10th kpk.pdf'],
           'quran': ['D:/SpaceBook/Books/10th/10th M Q/PDF/Mutlia_e_Quran_Book_KPK_10.pdf'],
           # Physics Units 10-12 stay in data_phys.js + physics_10_source_data.js; this book starts at Unit 13 (10thphysics3.pdf p30).
           # "path#N" = start at PDF page N of that file.
           'phys': ['D:/SpaceBook/Books/10th/10th physics/pdf/10thphysics3.pdf#30'] +
                   [f'D:/SpaceBook/Books/10th/10th physics/pdf/10thphysics{i}.pdf' for i in (4, 5, 6, 7)],
           'chem': [f'D:/SpaceBook/Books/10th/10th Chemistry/PDF/{n}.pdf' for n in ('Doc1', '2', '3', '4', '5', '6', '7', '8')]}
SUBJECTS = {
    'urdu': ('Urdu', 'urdu_10_data.js', 'URDU_10_DATA', 'Urdu 10 (KPTBB)'),
    'pakstudy': ('Pakistan Studies', 'pakstudy_10_data.js', 'PAKSTUDY_10_DATA', 'Pakistan Studies 10 (KPTBB)'),
    'comp': ('Computer Science', 'computer_10_data.js', 'COMPUTER_10_DATA', 'Computer Science 10 (KPTBB)'),
    'sci': ('General Science', 'general_science_10_data.js', 'GENERAL_SCIENCE_10_DATA', 'General Science 10 (KPTBB)'),
    'drawing': ('Drawing', 'drawing_10_data.js', 'DRAWING_10_DATA', 'Art & Model Drawing 10 (KPTBB)'),
    'hpe': ('Health & Physical Education', 'hpe_10_data.js', 'HPE_10_DATA', 'Health & Physical Education 10 (KPTBB)'),
    'islopt': ('Islamiat (Elective)', 'islamiat_ikhtiari_10_data.js', 'ISLAMIAT_IKHTIARI_10_DATA', 'Islamiat Elective 10 (KPTBB)'),
    'quran': ('Mutalia-e-Quran', 'mutalia_quran_10_data.js', 'MUTALIA_QURAN_10_DATA', 'Mutalia-e-Quran 10 (KPTBB)'),
    'phys': ('Physics', 'physics_10_book_data.js', 'PHYSICS_10_BOOK_DATA', 'Physics 10 (KPTBB), Units 13-18'),
    'chem': ('Chemistry', 'chemistry_10_book_data.js', 'CHEMISTRY_10_BOOK_DATA', 'Chemistry 10 (KPTBB)'),
}


def source_pages(subj):
    """[(pdf path, 1-based page)] for every scan of the book, in pNNN order."""
    import pymupdf
    out = []
    for spec in SOURCES[subj]:
        path, _, first = spec.partition('#')
        n = pymupdf.open(path).page_count
        out += [(path, k) for k in range(int(first or 1), n + 1)]
    return out
# Urdu-medium books: slot order of "original || translation || translation" (see math6_reader.js LANGS)
LANGS = {'pakstudy': ['ur', 'en', 'ps'], 'comp': ['ur', 'en', 'ps'], 'hpe': ['ur', 'en', 'ps'], 'islopt': ['ur', 'en', 'ps'], 'quran': ['ur', 'en', 'ps']}


def main():
    subj = sys.argv[1]
    name, legacy_file, global_name, title = SUBJECTS[subj]
    total = len(source_pages(subj))
    titles, starts, labels = b6.load_units(subj)
    b = b6.BookBuilder(titles, starts)
    files = sorted((HERE / subj / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        txt = f.read_text(encoding='utf-8')
        if '@status lesson' in txt:
            b.back_mode = False   # a stray back-matter page (e.g. a back cover) mid-book must not swallow later lessons
        b.page(expected, txt)
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c10{subj}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        for s_ in u['sections']:
            extract(s_['blocks'])
    words = b6.load_vocab(subj)
    for m in b.ledger:
        m['ocrWordRecall'] = None if m['status'] in ('duplicate', 'blank', 'answers') else b6.ocr_recall(subj, m['pdfPage'] - 1, m['english'])
        m.pop('english')
    for u in units:
        if u['number'] in labels:
            u['order'], u['number'] = u['number'], labels[u['number']]
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        # legacy URDU_10_DATA consumers (tools/validate.js) look for a truthy `exercise`; the reader uses `exercises`
        u.setdefault('exercise', {'source': 'exercises', 'count': len(u.get('exercises') or [])})
        u.setdefault('sloBank', {'source': 'slos'})
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
    if subj in ('phys', 'chem'):
        book['byNumber'] = True   # chapter list stays DATA.phys10Chapters/chem10Chapters; reader matches units by number
    # "||" and "|" are DSL separators; pages write the C OR operator as {{OR}} and a literal bar as {{BAR}}.
    J = lambda o: json.dumps(o, ensure_ascii=False).replace('{{OR}}', '||').replace('{{BAR}}', '|')
    js = [f'// Class 10 {name} (KPTBB) — generated by docs/source-verification/class-10/tools/build_book10.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + J(units) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS10_BOOKS = window.CLS10_BOOKS || {};',
          f'  window.CLS10_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + J(book) + ', words: ' + J(words) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + J(solutions) + ');',
          '}', '']
    import os
    out = Path(os.environ['BOOK10_OUT']) if os.environ.get('BOOK10_OUT') else (HERE / subj / 'build' / legacy_file)
    out.parent.mkdir(parents=True, exist_ok=True)
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
