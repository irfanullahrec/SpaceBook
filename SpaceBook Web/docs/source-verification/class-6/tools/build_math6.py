"""Build js/math_6_data.js from the page-by-page Class 6 Mathematics source transcriptions.

Source of truth: D:\\SpaceBook\\Books\\6th\\Math\\JPG\\NNN.jpg (single-page scans).
Each reviewed page is transcribed in docs/source-verification/class-6/math/pages/pNNN.txt
(NNN = JPG index; PDF page = NNN + 1; printed page = NNN - 2 for lesson pages).

Line syntax (one block per line; translated text is `English || Urdu || Pashto`):
  @printed N               printed page number on this scan (omit for unnumbered pages)
  @status STATUS           front-matter | lesson | answers | back-matter | blank
  @deco TEXT               decorative artwork on this page (recorded, not reproduced)
  @issue TEXT              unresolved/source problem on this page (recorded in ledger)
  @unit N | EN || UR || PS start unit N
  @sec ID | EN || UR || PS start a lesson section inside the current unit
  # EN || UR || PS         heading            ## ...  sub-heading
  p EN || UR || PS         paragraph (inline LaTeX with $...$)
  m TEXT                   math / numeric line, not translated ($...$ allowed)
  eq LATEX                 display equation
  - EN || UR || PS         bullet             -- ... nested bullet
  box KIND | EN || UR || PS  ... endbox      callout (KIND: note, check, prior, teach, info)
  example N | EN || UR || PS ... endexample worked example
  exercise ID ... endexercise                textbook exercise
  q NO | EN || UR || PS     exercise question   qp NO | TEXT [|| UR || PS]  sub-part
  svg EN || UR || PS  then raw <svg> lines, endsvg
  table EN || UR || PS then  th | a | b  /  tr | a | b  rows, endtable
  ans EXID | QNO | TEXT     textbook answer key entry
  slo EN || UR || PS        student learning outcome (also rendered as a bullet)
"""
from pathlib import Path
import json, re, sys, datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import figs
import solve

HERE = Path(__file__).resolve().parents[1]
APP = HERE.parents[2]
PAGES = HERE / 'math' / 'pages'
OUT = APP / 'js' / 'math_6_data.js'
LEDGER = HERE / 'math' / 'ledger.json'
VOCAB = HERE / 'math' / 'vocab.tsv'
SOURCE_JPG = r'D:\SpaceBook\Books\6th\Math\JPG'
TOTAL_PAGES = 263

UNIT_TITLES = {
    1: ('Multiples and Factors', 'اضعاف اور اجزائے ضربی', 'ضربونه او ضربي اجزا'),
    2: ('Integers', 'صحیح اعداد', 'تام عددونه'),
    3: ('Laws of Integers and Order of Operations', 'صحیح اعداد کے قوانین اور عملیات کی ترتیب', 'د تامو عددونو قوانین او د عملیو ترتیب'),
    4: ('Rate, Ratio and Percentage', 'شرح، نسبت اور فیصد', 'نرخ، نسبت او سلنه'),
    5: ('Sets', 'سیٹ', 'سېټونه'),
    6: ('Patterns and Algebraic Expressions', 'نمونے اور الجبری عبارتیں', 'بېلګې او الجبري افادې'),
    7: ('Linear Expressions and Equations', 'خطی عبارتیں اور مساواتیں', 'خطي افادې او معادلې'),
    8: ('Surface Area and Volume', 'سطحی رقبہ اور حجم', 'سطحي مساحت او حجم'),
    9: ('Lines, Angles and Symmetry', 'خطوط، زاویے اور تشاکل', 'کرښې، زاويې او تناظر'),
    10: ('Geometrical Constructions', 'جیومیٹریائی اشکال کی تعمیر', 'هندسي جوړونې'),
    11: ('Data Management', 'ڈیٹا کا انتظام', 'د معلوماتو مدیریت'),
}
UNIT_START_PRINTED = {1: 1, 2: 24, 3: 38, 4: 70, 5: 93, 6: 106, 7: 125, 8: 139, 9: 170, 10: 189, 11: 204}


def tri(raw):
    parts = [x.strip() for x in raw.split('||')]
    if len(parts) == 1:
        return {'en': parts[0]}
    if len(parts) != 3:
        raise ValueError(f'expected EN || UR || PS, got {len(parts)} parts: {raw[:80]}')
    return {'en': parts[0], 'ur': parts[1], 'ps': parts[2]}


def split_no(raw):
    no, _, rest = raw.partition('|')
    return no.strip(), rest.strip()



def _nums(t):
    """Numbers in an answer string, normalising fractions and thousands separators."""
    from fractions import Fraction
    t = t.replace(',', '').replace('−', '-').replace('–', '-')
    out = set()
    for m in re.finditer(r'(-)?\\frac\{(\d+)\}\{(\d+)\}', t):
        out.add(round(float(Fraction(int(m.group(2)), int(m.group(3)))) * (-1 if m.group(1) else 1), 4))
    t2 = re.sub(r'-?\\frac\{\d+\}\{\d+\}', ' ', t)
    for m in re.finditer(r'-?\d+(?:\.\d+)?', t2):
        out.add(round(float(m.group()), 4))
    return out


ANSWER_WARNINGS = []


def check_answer(sol, where):
    """Warn when a typed answer shares no number with the answer of the last generated working."""
    gens = sol.pop('_gen', None) if sol else None
    if not gens:
        return
    typed = _nums(sol['answer'])
    gen = _nums(gens[-1])
    if typed and gen and not (typed & gen):
        ANSWER_WARNINGS.append(f'{where}: typed "{sol["answer"]}" vs generated "{gens[-1]}"')


class Builder:
    def __init__(self, unit_titles=None, unit_start=None):
        unit_titles = UNIT_TITLES if unit_titles is None else unit_titles
        unit_start = UNIT_START_PRINTED if unit_start is None else unit_start
        self.units = {n: self.new_unit(n, t, unit_start.get(n)) for n, t in unit_titles.items()}
        self.front = []          # front-matter blocks
        self.back = []           # back-matter blocks (glossary, formulas, links, index, symbols)
        self.back_mode = False
        self.answers = {}        # exercise id -> {qno: text}
        self.answer_pages = []
        self.unit = None
        self.section = None
        self.stack = []          # open containers (box/example/exercise/svg/table)
        self.ledger = []
        self.issues = []
        self.cur_sol = None

    @staticmethod
    def new_unit(n, t, start=None):
        return {'number': n, 'id': f'unit-{n}', 'title': t[0], 'titleUrdu': t[1], 'titlePashto': t[2],
                'type': 'chapter', 'pageStart': start, 'sections': [], 'workedExamples': [],
                'exercises': [], 'slos': [], 'sourcePdfPages': []}

    def target(self):
        if self.stack:
            return self.stack[-1]['blocks']
        if self.back_mode:
            return self.back
        if self.section is not None:
            return self.section['blocks']
        return self.front

    def add(self, block):
        self.target().append(block)
        return block

    def page(self, idx, text):
        pdf = idx + 1
        meta = {'pdfPage': pdf, 'jpg': f'{idx:03}.jpg', 'printedPage': None, 'status': 'lesson', 'decorative': [], 'issues': [],
                'blocks': 0, 'svg': 0, 'tables': 0, 'translated': 0, 'untranslated': [], 'english': []}
        lines = text.splitlines()
        # page marker goes in once the page's structural directives are known
        marker_done = False
        svg_buf = None
        for n, line in enumerate(lines, 1):
            raw = line.rstrip('\n')
            if svg_buf is not None:
                if raw.strip() == 'endsvg':
                    svg_buf['svg'] = '\n'.join(svg_buf.pop('_lines'))
                    svg_buf = None
                else:
                    svg_buf['_lines'].append(raw)
                continue
            s = raw.strip()
            if not s or s.startswith('//'):
                continue
            try:
                if s.startswith('@'):
                    key, _, val = s[1:].partition(' ')
                    val = val.strip()
                    if key == 'printed':
                        meta['printedPage'] = int(val)
                    elif key == 'pdf':   # scan bound out of order: file sits in reading order, this is its real PDF page
                        meta['pdfPage'] = int(val)
                        meta['jpg'] = f'{int(val) - 1:03}.jpg'
                    elif key == 'status':
                        meta['status'] = val
                        if val == 'back-matter':
                            self.back_mode = True
                    elif key == 'deco':
                        meta['decorative'].append(val)
                    elif key == 'issue':
                        meta['issues'].append(val)
                    elif key == 'unit':
                        no, rest = split_no(val)
                        if int(no) not in self.units:
                            t_ = tri(rest)
                            self.units[int(no)] = self.new_unit(int(no), (t_['en'], t_.get('ur', ''), t_.get('ps', '')), meta['printedPage'])
                        self.unit = self.units[int(no)]
                        self.section = None
                    elif key == 'sec':
                        sid, rest = split_no(val)
                        title = tri(rest)
                        existing = next((x for x in self.unit['sections'] if x['id'] == sid), None)
                        if existing:
                            self.section = existing
                        else:
                            self.section = {'id': sid, 'title': title['en'], 'titleUrdu': title.get('ur', ''),
                                            'titlePashto': title.get('ps', ''), 'blocks': [], 'sourcePdfPages': [], 'sourcePrintedPages': []}
                            self.unit['sections'].append(self.section)
                        if marker_done and pdf not in self.section['sourcePdfPages']:
                            self.section['sourcePdfPages'].append(pdf)
                            self.section['sourcePrintedPages'].append(meta['printedPage'])
                            self.section['blocks'].append({'t': 'page', 'pdf': pdf, 'printed': meta['printedPage']})
                    else:
                        raise ValueError('unknown directive ' + key)
                    continue
                if not marker_done:
                    marker_done = True
                    if self.unit is not None and pdf not in self.unit['sourcePdfPages']:
                        self.unit['sourcePdfPages'].append(pdf)
                    if self.section is not None:
                        self.section['sourcePdfPages'].append(pdf)
                        self.section['sourcePrintedPages'].append(meta['printedPage'])
                    if meta['status'] != 'answers':
                        self.add({'t': 'page', 'pdf': pdf, 'printed': meta['printedPage']})
                op, _, rest = s.partition(' ')
                rest = rest.strip()
                if op in ('#', '##', '###'):
                    b = self.add({'t': 'h', 'l': len(op) + 2, **tri(rest)})
                elif op == 'p':
                    b = self.add({'t': 'p', **tri(rest)})
                elif op == 'm':
                    b = self.add({'t': 'm', 'en': rest})
                elif op == 'eq':
                    tex, _, tr = rest.partition('||')
                    b = self.add({'t': 'eq', 'tex': tex.strip()})
                    if tr.strip():
                        u, _, ps_ = tr.partition('||')
                        b.update({'ur': u.strip(), 'ps': ps_.strip(), 'en': tex.strip()})
                elif op in ('-', '--', '---'):
                    tgt = self.target()
                    item = {'lv': len(op), **tri(rest)}
                    if tgt and tgt[-1]['t'] == 'ul':
                        tgt[-1]['items'].append(item)
                    else:
                        tgt.append({'t': 'ul', 'items': [item]})
                    b = item
                elif op == 'slo':
                    item = {'lv': 1, **tri(rest)}
                    self.unit['slos'].append(item)
                    tgt = self.target()
                    if tgt and tgt[-1]['t'] == 'ul' and tgt[-1].get('slo'):
                        tgt[-1]['items'].append(item)
                    else:
                        tgt.append({'t': 'ul', 'slo': True, 'items': [item]})
                    b = item
                elif op == 'box':
                    kind, rest2 = split_no(rest)
                    blk = self.add({'t': 'box', 'kind': kind, 'title': tri(rest2) if rest2 else None, 'blocks': []})
                    self.stack.append(blk)
                    b = blk['title'] or {}
                elif op == 'example':
                    no, rest2 = split_no(rest)
                    blk = self.add({'t': 'example', 'no': no, 'id': f"u{self.unit['number']}-ex{no}-{len(self.unit['workedExamples'])+1}",
                                    'title': tri(rest2) if rest2 else None, 'blocks': [], 'pdf': pdf, 'printed': meta['printedPage'],
                                    'section': self.section['id'] if self.section else None})
                    self.unit['workedExamples'].append(blk)
                    self.stack.append(blk)
                    b = blk['title'] or {}
                elif op == 'exercise':
                    blk = self.add({'t': 'exercise', 'id': rest, 'blocks': [], 'pdf': pdf, 'printed': meta['printedPage'],
                                    'section': self.section['id'] if self.section else None})
                    self.unit['exercises'].append(blk)
                    self.stack.append(blk)
                    b = {}
                elif op in ('endbox', 'endexample', 'endexercise'):
                    want = {'endbox': 'box', 'endexample': 'example', 'endexercise': 'exercise'}[op]
                    if not self.stack or self.stack[-1]['t'] != want:
                        raise ValueError(f'{op} without open {want}')
                    self.stack.pop()
                    continue
                elif op == 'q':
                    no, rest2 = split_no(rest)
                    b = self.add({'t': 'q', 'no': no, 'parts': [], **tri(rest2)})
                elif op == 'qp':
                    no, rest2 = split_no(rest)
                    tgt = self.target()
                    b = {'no': no, **tri(rest2)}
                    last = next((x for x in reversed(tgt) if x['t'] != 'page'), None)
                    if last is not None and last['t'] in ('q', 'parts'):
                        last['parts'].append(b)
                    else:
                        tgt.append({'t': 'parts', 'parts': [b]})
                elif op == 'qsolve':
                    q = next((x for x in reversed(self.target()) if x['t'] == 'q'), None)
                    kind, _, arg = rest.partition(' ')
                    q['solveParts'] = [kind] + ([arg.strip()] if arg.strip() else [])
                    continue
                elif op == 'qsol':
                    q = next((x for x in reversed(self.target()) if x['t'] == 'q'), None)
                    kind, _, arg = rest.partition(' ')
                    q['sol'] = solve.generate(kind, arg.strip())
                    continue
                elif op in ('solution', 'qsolution'):
                    tgt = self.target()
                    q = next((x for x in reversed(tgt) if x['t'] in ('q', 'parts')), None)
                    owner = q['parts'][-1] if q.get('parts') and op == 'solution' else q
                    owner['sol'] = {'steps': [], 'answer': rest}
                    self.cur_sol = owner['sol']
                    continue
                elif op == 'sol':
                    ans, _, why = rest.partition('##')
                    tgt = self.target()
                    q = next((x for x in reversed(tgt) if x['t'] in ('q', 'parts')), None)
                    owner = q['parts'][-1] if q.get('parts') else q
                    owner['sol'] = {'steps': [tri(why.strip())], 'answer': ans.strip()}
                    continue
                elif op == 'ss':
                    self.cur_sol['steps'].append(tri(rest))
                    continue
                elif op == 'suse':
                    kind, _, arg = rest.partition(' ')
                    parts_ = [arg.strip()] if kind in ('share', 'urate', 'evalx', 'pieq') else [x.strip() for x in arg.split('|')]
                    g_ = solve.generate(kind, *parts_)
                    self.cur_sol['steps'].extend(g_['steps'])
                    self.cur_sol.setdefault('_gen', []).append(g_['answer'])
                    continue
                elif op == 'stable':
                    self.sol_table = []
                    continue
                elif op in ('tr', 'endtable') and getattr(self, 'sol_table', None) is not None:
                    if op == 'tr':
                        self.sol_table.append([c.strip() for c in rest.strip().strip('|').split('|')])
                    else:
                        rows = self.sol_table
                        n = max(len(r) for r in rows)
                        body = r' \\ \hline '.join(' & '.join(r'\text{' + c + '}' for c in r + [''] * (n - len(r))) for r in rows)
                        arr = r'\begin{array}{|' + '|'.join('c' * n) + r'|} \hline ' + body + r' \\ \hline \end{array}'
                        self.cur_sol['steps'].append({'m': arr})
                        self.sol_table = None
                    continue
                elif op == 'sfig':
                    kind, _, spec = rest.partition(' ')
                    svg_ = getattr(figs, kind)(spec.strip())
                    if self.cur_sol['steps'] and 'svg' not in self.cur_sol['steps'][-1]:
                        self.cur_sol['steps'][-1]['svg'] = svg_
                    else:
                        self.cur_sol['steps'].append({'svg': svg_})
                    continue
                elif op == 'sm':
                    if self.cur_sol['steps'] and 'm' not in self.cur_sol['steps'][-1]:
                        self.cur_sol['steps'][-1]['m'] = rest
                    else:
                        self.cur_sol['steps'].append({'m': rest})
                    continue
                elif op == 'endsolution':
                    check_answer(self.cur_sol, f'p{idx:03}.txt line {n}')
                    self.cur_sol = None
                    continue
                elif op == 'svg':
                    svg_buf = self.add({'t': 'svg', 'cap': tri(rest) if rest else None, '_lines': []})
                    meta['svg'] += 1
                    b = svg_buf['cap'] or {}
                elif op in ('longdiv', 'ladder', 'ftree', 'stair', 'nline', 'beads', 'grid', 'bar', 'icons', 'cross', 'venn', 'balance', 'tiles', 'rect', 'path', 'shape', 'solid', 'reflect', 'transv', 'bisect', 'perpon', 'perpoff', 'angcon', 'bisangle', 'chart', 'pie', 'spinner', 'ptree'):
                    spec, _, cap = rest.partition('||')
                    b = self.add({'t': 'svg', 'cap': tri(cap) if cap.strip() else None, 'svg': getattr(figs, op)(spec.strip()), 'gen': op})
                    meta['svg'] += 1
                    b = b['cap'] or {}
                elif op == 'table':
                    blk = self.add({'t': 'table', 'cap': tri(rest) if rest else None, 'rows': [], 'head': 0})
                    self.stack.append(blk)
                    meta['tables'] += 1
                    b = blk['cap'] or {}
                elif op in ('th', 'tr'):
                    tbl = self.stack[-1] if self.stack and self.stack[-1]['t'] == 'table' else None
                    if tbl is None:
                        raise ValueError('row outside table')
                    cells = [c.strip() for c in re.split(r'(?<!\|)\|(?!\|)', rest.strip().strip('|'))]
                    tbl['rows'].append(cells)
                    if op == 'th':
                        tbl['head'] += 1
                    meta['english'].extend(cells)
                    continue
                elif op == 'endtable':
                    if not self.stack or self.stack[-1]['t'] != 'table':
                        raise ValueError('endtable without table')
                    self.stack.pop()
                    continue
                elif op == 'ans':
                    ex, rest2 = split_no(rest)
                    qno, txt = split_no(rest2)
                    self.answers.setdefault(ex, []).append({'q': qno, 'a': txt, 'pdf': pdf, 'printed': meta['printedPage']})
                    meta['english'].append(txt)
                    continue
                else:
                    raise ValueError('unknown op ' + op)
                meta['blocks'] += 1
                if isinstance(b, dict) and b.get('en'):
                    meta['english'].append(b['en'])
                    if 'ur' in b:
                        meta['translated'] += 1
                    elif op not in ('m', 'eq', 'qp') and re.search(r'[A-Za-z]{3,}', re.sub(r'\$[^$]*\$', '', b['en'])):
                        meta['untranslated'].append(b['en'][:60])
                if op == 'eq':
                    meta['english'].append(rest)
            except Exception as e:
                raise SystemExit(f'p{idx:03}.txt line {n}: {e}\n  {raw}')
        if svg_buf is not None:
            raise SystemExit(f'p{idx:03}.txt: unterminated svg')
        if meta['status'] == 'answers':
            self.answer_pages.append(pdf)
        meta['unit'] = self.unit['number'] if self.unit else None
        meta['section'] = self.section['id'] if self.section else None
        self.ledger.append(meta)


def load_vocab():
    words = {}
    if VOCAB.exists():
        for line in VOCAB.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 3:
                raise SystemExit('bad vocab line: ' + line)
            words[parts[0].strip().lower()] = [parts[1].strip(), parts[2].strip()]
    return words


def ocr_recall(idx, english, numeric=False):
    f = HERE / 'math' / 'ocr' / f'{idx:03}.json'
    if not f.exists():
        return None
    ocr = ' '.join(l['text'] for l in json.loads(f.read_text(encoding='utf-8'))['lines'] if l['conf'] > 0.8)
    if numeric:
        # Answer-key pages are mostly numbers: check that every 3+ digit number OCR read is in the transcription.
        nums = [n for n in re.findall(r'\d{3,}', ocr.replace(',', '')) if n not in ('238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250')]
        mine_n = set(re.findall(r'\d+', ' '.join(english).replace(',', '')))
        nums = [n for n in nums if len(n) <= 6]   # longer digit runs are OCR merging several numbers
        if len(nums) < 5:
            return None
        return round(sum(1 for n in nums if n in mine_n) / len(nums), 3)
    norm = lambda t: re.findall(r'[a-z]{3,}', t.lower())
    src = norm(ocr)
    stream = re.sub(r'[^a-z]', '', ' '.join(english).lower())
    mine = type('S', (), {'__contains__': lambda self, w: w in stream})()
    ignore = {'not', 'for', 'sale', 'downloaded', 'from', 'awazeinqilab', 'com', 'download', 'millions', 'mcqs', 'books', 'notes', 'any', 'subject', 'website', 'awaz', 'inqilab'}
    src = [w for w in src if w not in ignore]
    if not src:
        return None
    hit = sum(1 for w in src if w in mine)
    return round(hit / len(src), 3)


def main():
    b = Builder()
    files = sorted(PAGES.glob('p[0-9][0-9][0-9].txt'))
    expected = 0
    for f in files:
        idx = int(f.stem[1:])
        if idx != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        expected += 1
        b.page(idx, f.read_text(encoding='utf-8'))
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    def resolve(list_):
        for x in list_:
            if x.get('t') == 'q' and x.get('solveParts'):
                kind, *args = x.pop('solveParts')
                for part in x['parts']:
                    if 'sol' not in part:
                        part['sol'] = solve.generate(kind, part['en'], *args)
            if x.get('blocks'):
                resolve(x['blocks'])
    for u in b.units.values():
        for s_ in u['sections']:
            resolve(s_['blocks'])
    # Move solutions to a lazily loaded file; questions keep only a solution id.
    solutions = {}
    def extract(list_, path):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f"s{len(solutions) + 1}"
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'], path)
    for u in b.units.values():
        for s_ in u['sections']:
            extract(s_['blocks'], u['number'])
    (APP / 'js' / 'math_6_solutions.js').write_text(
        '// Class 6 Mathematics: SpaceBook step-by-step solutions (not printed in the textbook). Generated by build_math6.py.\n'
        'window.MATH_6_SOLUTIONS = ' + json.dumps(solutions, ensure_ascii=False) + ';\n', encoding='utf-8')
    words = load_vocab()
    for m in b.ledger:
        m['ocrWordRecall'] = None if m['status'] in ('duplicate', 'blank') else ocr_recall(m['pdfPage'] - 1, m['english'], m['status'] == 'answers')
        m.pop('english')
    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        for s in u['sections']:
            # plain-text theory for search / legacy consumers
            s['theory'] = '\n\n'.join(x.get('en', '') for x in s['blocks'] if x['t'] in ('h', 'p'))[:4000]
            s['heading'] = s['title']
            s['headingUrdu'] = s['titleUrdu']
    reviewed = len(b.ledger)
    book = {
        'title': 'Mathematics 6 (KPTBB, SNC 2022, Test Edition)',
        'source': SOURCE_JPG, 'totalPdfPages': TOTAL_PAGES, 'reviewedPdfPages': reviewed,
        'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers, 'answerPdfPages': b.answer_pages,
        'complete': reviewed >= TOTAL_PAGES,
    }
    js = ['// Class 6 Mathematics (KPTBB, SNC 2022) — generated by docs/source-verification/class-6/tools/build_math6.py',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          'const MATH_6_DATA = ' + json.dumps(units, ensure_ascii=False) + ';',
          'const MATH_6_BOOK = ' + json.dumps(book, ensure_ascii=False) + ';',
          'const MATH_6_WORDS = ' + json.dumps(words, ensure_ascii=False) + ';',
          "if (typeof window !== 'undefined') { window.MATH_6_DATA = MATH_6_DATA; window.MATH_6_BOOK = MATH_6_BOOK; window.MATH_6_WORDS = MATH_6_WORDS; }", '']
    OUT.write_text('\n'.join(js), encoding='utf-8')
    LEDGER.write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    low = [(m['pdfPage'], m['ocrWordRecall']) for m in b.ledger if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < (0.7 if m['status'] == 'answers' else 0.85) and m['status'] != 'blank']
    untr = [(m['pdfPage'], m['untranslated']) for m in b.ledger if m['untranslated']]
    with (HERE / 'math' / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + chr(9) + str(reviewed) + chr(10))
    for w_ in ANSWER_WARNINGS:
        print('ANSWER MISMATCH', w_)
    print(f'reviewed {reviewed}/{TOTAL_PAGES} pages; vocab {len(words)} words; output {OUT.stat().st_size} bytes')
    if low:
        print('LOW OCR RECALL (check):', low)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
