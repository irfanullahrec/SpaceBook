"""Build js/math_11_data.js from the page-by-page Class 11 Mathematics transcriptions.

    python -X utf8 tools/build_math11.py

Source of truth: D:/SpaceBook/Books/11th/11th Maths/JPG/NNN_page_H.jpg — 216 photographed
spreads, two portrait pages each (H = 1, 2). Scan index i = 2*(NNN-1) + (H-1), 0..431.
Each reviewed scan is transcribed in class-11/math/pages/pIII.txt (III = scan index).

Same page syntax, parser and reader as Class 8 Mathematics (class-8/tools/build_math8.py,
js/math8_reader.js -> js/math11_reader.js): `English || Urdu || Pashto` lines, $LaTeX$,
@unit / @sec / example / exercise / q / qp / svg / table / ans directives.
Upside-down scans are transcribed in reading order and noted with @issue.
"""
from pathlib import Path
import json, sys, datetime

HERE = Path(__file__).resolve().parents[1]          # docs/source-verification/class-11
APP = HERE.parents[2]                                # SpaceBook Web
sys.path.insert(0, str(HERE.parent / 'class-8' / 'tools'))
import build_math8 as bm  # noqa: E402  (parser, vocab loader)

PAGES = HERE / 'math' / 'pages'
OUT = APP / 'js' / 'math_11_data.js'
SOLS = APP / 'js' / 'math_11_solutions.js'
LEDGER = HERE / 'math' / 'ledger.json'
SOURCE_JPG = r'D:\SpaceBook\Books\11th\11th Maths\JPG'
TOTAL_PAGES = 432

UNIT_TITLES = {
    1: ('Complex Numbers', 'مختلط اعداد', 'مختلط عددونه'),
    2: ('Matrices and Determinants', 'قالب اور مقطع', 'میټریکسونه او ډیټرمینانټونه'),
    3: ('Vectors', 'سمتیے', 'وېکټورونه'),
    4: ('Sequences and Series', 'ترتیب اور سلسلے', 'ترتیبونه او لړۍ'),
    5: ('Miscellaneous Series', 'متفرق سلسلے', 'بېلابېلې لړۍ'),
    6: ('Permutation, Combination and Probability', 'ترتیب، جوڑ اور احتمال', 'ترتیب، ترکیب او احتمال'),
    7: ('Mathematical Induction and Binomial Theorem', 'ریاضیاتی استقرا اور مسئلہ دو رقمی', 'ریاضیاتي استقرا او د دوه حدي قضیه'),
    8: ('Functions and Graphs', 'تفاعل اور گراف', 'تابعګانې او ګرافونه'),
    9: ('Linear Programming', 'خطی پروگرامنگ', 'خطي پروګرام جوړونه'),
    10: ('Trigonometric Identities of Sum and Difference of Angles', 'زاویوں کے مجموعے اور فرق کی مثلثیاتی مماثلتیں', 'د زاویو د مجموعې او توپیر مثلثاتي مطابقتونه'),
    11: ('Application of Trigonometry', 'مثلثیات کا اطلاق', 'د مثلثاتو کارونه'),
    12: ('Graphs of Trigonometric and Inverse Trigonometric Functions and Solutions of Trigonometric Equations',
         'مثلثیاتی اور معکوس مثلثیاتی تفاعلات کے گراف اور مثلثیاتی مساواتوں کا حل',
         'د مثلثاتي او معکوس مثلثاتي تابعګانو ګرافونه او د مثلثاتي معادلو حل'),
}

# the Class 8 parser reads these module globals
bm.UNIT_TITLES = UNIT_TITLES
bm.UNIT_START_PRINTED = {n: None for n in UNIT_TITLES}
bm.VOCAB = HERE / 'math' / 'vocab.tsv'
bm.HERE = HERE  # ocr_recall() looks for class-11/math/ocr (absent -> skipped)


def _tri(raw):
    # languages are separated by ' || ' (with spaces) so LaTeX such as |a||b| stays intact
    parts = [x.strip() for x in raw.split(' || ')]
    if len(parts) == 1:
        return {'en': parts[0]}
    if len(parts) != 3:
        raise ValueError(f'expected EN || UR || PS, got {len(parts)} parts: {raw[:80]}')
    return {'en': parts[0], 'ur': parts[1], 'ps': parts[2]}


bm.tri = _tri


def jpg_name(i):
    return f'{i // 2 + 1:03}_page_{i % 2 + 1}.jpg'


def main():
    b = bm.Builder()
    files = sorted(PAGES.glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        txt = f.read_text(encoding='utf-8')
        if '@status front-matter' in txt and b.unit is not None:
            # front matter photographed between lesson pages (e.g. Contents after printed page 1):
            # keep it in the book's front matter, then resume the open unit/section
            unit, section = b.unit, b.section
            b.unit = b.section = None
            b.page(expected, txt)
            b.unit, b.section = unit, section
        else:
            b.page(expected, txt)
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])

    # Authored solutions are deliberately separate from transcribed source pages.
    # Exact question matching prevents an answer silently attaching to revised text.
    authored_path = HERE / 'math' / 'authored-solutions.json'
    authored = json.loads(authored_path.read_text(encoding='utf-8')) if authored_path.exists() else {}
    attached = set()
    for unit in b.units.values():
        for exercise in unit['exercises']:
            def attach(blocks):
                for record in blocks:
                    if record.get('t') == 'q':
                        owners = [(record, '')] + [(part, part['no']) for part in record.get('parts', [])]
                        for owner, part_no in owners:
                            key = f"{exercise['id']}|{record['no']}|{part_no}"
                            solution = authored.get(key)
                            if solution:
                                assert owner['en'] == solution['question'], f'Changed question: {key}'
                                assert record['en'] == solution['prompt'], f'Changed prompt: {key}'
                                owner['sol'] = {k: solution[k] for k in ('answer', 'steps')}
                                for language in ('answerUr', 'answerPs'):
                                    if solution.get(language): owner['sol'][language] = solution[language]
                                owner['authoredAnswer'] = {
                                    'en': solution['answer'],
                                    'ur': solution.get('answerUr', solution['answer']),
                                    'ps': solution.get('answerPs', solution['answer'])
                                }
                                owner['answerSource'] = 'SpaceBook authored solution'
                                owner['answerKey'] = key
                                if solution.get('category'): owner['questionCategory'] = solution['category']
                                attached.add(key)
                    if record.get('blocks'): attach(record['blocks'])
            attach(exercise['blocks'])
    assert attached == set(authored), f'Unmatched authored solutions: {set(authored)-attached}'

    def resolve(list_):
        for x in list_:
            if x.get('t') == 'q' and x.get('solveParts'):
                kind, *args = x.pop('solveParts')
                for part in x['parts']:
                    if 'sol' not in part:
                        part['sol'] = bm.solve.generate(kind, part['en'], *args)
            if x.get('blocks'):
                resolve(x['blocks'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f's{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    for u in b.units.values():
        for s_ in u['sections']:
            resolve(s_['blocks'])
            extract(s_['blocks'])
    SOLS.write_text('// Class 11 Mathematics: SpaceBook step-by-step solutions (not printed in the textbook). Generated by build_math11.py.\n'
                    'window.MATH_11_SOLUTIONS = ' + json.dumps(solutions, ensure_ascii=False) + ';\n', encoding='utf-8')

    words = bm.load_vocab()
    # Reviewed, subject-specific additions; the shared dictionary contains
    # untranslated placeholders and is intentionally not used as a fallback.
    for extra_vocab in sorted((HERE / 'math').glob('vocab-*.tsv')):
        for line in extra_vocab.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            key, ur, ps = line.split('\t')
            assert key not in words, f'Duplicate Mathematics vocabulary: {key}'
            words[key] = [ur, ps]
    for m in b.ledger:
        m.pop('english', None)
        m['jpg'] = jpg_name(m['pdfPage'] - 1)
    # only units that have reviewed pages are published; the rest are added as their pages are reviewed
    units = [b.units[n] for n in sorted(b.units) if b.units[n]['sourcePdfPages']]
    for u in units:
        printed = [m['printedPage'] for m in b.ledger if m.get('unit') == u['number'] and m['printedPage']]
        u['pageStart'] = min(printed) if printed else None
        u['pageRange'] = f"Pages {min(printed)}–{max(printed)}" if printed else ''
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        for s in u['sections']:
            s['theory'] = '\n\n'.join(x.get('en', '') for x in s['blocks'] if x['t'] in ('h', 'p'))[:4000]
            s['heading'] = s['title']
            s['headingUrdu'] = s['titleUrdu']
    reviewed = len(b.ledger)
    book = {
        'title': 'A Textbook of Mathematics for Grade XI (KPTBB, 2021-22)',
        'source': SOURCE_JPG, 'totalPdfPages': TOTAL_PAGES, 'reviewedPdfPages': reviewed,
        'frontMatter': b.front, 'answers': b.answers, 'answerPdfPages': b.answer_pages,
        'complete': reviewed >= TOTAL_PAGES,
    }
    js = ['// Class 11 Mathematics (KPTBB) — generated by docs/source-verification/class-11/tools/build_math11.py',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          'const MATH_11_DATA = ' + json.dumps(units, ensure_ascii=False) + ';',
          'const MATH_11_BOOK = ' + json.dumps(book, ensure_ascii=False) + ';',
          'const MATH_11_WORDS = ' + json.dumps(words, ensure_ascii=False) + ';',
          "if (typeof window !== 'undefined') { window.MATH_11_DATA = MATH_11_DATA; window.MATH_11_BOOK = MATH_11_BOOK; window.MATH_11_WORDS = MATH_11_WORDS; }", '']
    OUT.write_text('\n'.join(js), encoding='utf-8')
    LEDGER.write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / 'math' / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    untr = [(m['pdfPage'] - 1, m['untranslated']) for m in b.ledger if m['untranslated']]
    print(f'reviewed {reviewed}/{TOTAL_PAGES} scans; units {len(units)}; vocab {len(words)}; output {OUT.stat().st_size} bytes')
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
