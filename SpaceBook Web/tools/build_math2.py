# -*- coding: utf-8 -*-
"""Build js/math_2_data.js from page-by-page Class 2 Mathematics source transcriptions.
KPTBB Single National Curriculum (SNC 2020) Class 2 Mathematics.
"""
from pathlib import Path
import json, re, sys, datetime

HERE = Path(__file__).resolve().parent
APP = HERE.parent
VERIF = APP / 'docs' / 'source-verification' / 'class-2'
PAGES = VERIF / 'math' / 'pages'
OUT = APP / 'js' / 'math_2_data.js'
LEDGER = VERIF / 'math' / 'ledger.json'
VOCAB = VERIF / 'math' / 'vocab.tsv'
SOURCE_JPG = r'D:\SpaceBook\Books\2nd\2nd Maths\JPG'
TOTAL_PAGES = 167

UNIT_TITLES = {
    1: ('Whole Numbers', 'کامل اعداد', 'بشپړ عددونه'),
    2: ('Number Operations', 'اعداد کے عمل', 'د عددونو عملیې'),
    3: ('Fractions', 'کسور', 'کسرونه'),
    4: ('Measurement: Length, Mass and Capacity', 'پیمائش: لمبائی، کمیت اور گنجائش', 'اندازه: اوږدوالی، کتله او ظرفیت'),
    5: ('Time', 'وقت', 'وخت'),
    6: ('Geometry', 'جیومیٹری', 'هندسه'),
}

UNIT_START_PRINTED = {1: 1, 2: 29, 3: 94, 4: 108, 5: 128, 6: 141}

def tri(raw):
    parts = [x.strip() for x in raw.split('||')]
    if len(parts) == 1:
        return {'en': parts[0]}
    if len(parts) == 2:
        return {'en': parts[0], 'ur': parts[1], 'ps': parts[1]}
    return {'en': parts[0], 'ur': parts[1], 'ps': parts[2]}

def split_no(raw):
    no, _, rest = raw.partition('|')
    return no.strip(), rest.strip()

class Builder:
    def __init__(self):
        self.units = {n: self.new_unit(n, t, UNIT_START_PRINTED.get(n)) for n, t in UNIT_TITLES.items()}
        self.front = []
        self.back = []
        self.back_mode = False
        self.answers = {}
        self.answer_pages = []
        self.unit = None
        self.section = None
        self.stack = []
        self.ledger = []
        self.issues = []
        self.cur_sol = None

    @staticmethod
    def new_unit(n, t, start=None):
        return {
            'number': n,
            'id': f'unit-{n}',
            'title': t[0],
            'titleUrdu': t[1],
            'titlePashto': t[2],
            'type': 'chapter',
            'pageStart': start,
            'sections': [],
            'workedExamples': [],
            'exercises': [],
            'slos': [],
            'formulaSheet': [],
            'sourcePdfPages': []
        }

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
        meta = {
            'pdfPage': pdf,
            'jpg': f'page-{idx+1:04}.jpg',
            'printedPage': None,
            'status': 'lesson',
            'decorative': [],
            'issues': [],
            'blocks': 0,
            'svg': 0,
            'tables': 0,
            'translated': 0,
            'untranslated': [],
            'english': []
        }
        lines = text.splitlines()
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

            if s.startswith('@'):
                key, _, val = s[1:].partition(' ')
                val = val.strip()
                if key == 'printed':
                    meta['printedPage'] = int(val)
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
                    u_num = int(no)
                    if u_num not in self.units:
                        t_ = tri(rest)
                        self.units[u_num] = self.new_unit(u_num, (t_['en'], t_.get('ur', ''), t_.get('ps', '')), meta['printedPage'])
                    self.unit = self.units[u_num]
                    self.section = None
                elif key == 'sec':
                    sid, rest = split_no(val)
                    title = tri(rest)
                    existing = next((x for x in self.unit['sections'] if x['id'] == sid), None)
                    if existing:
                        self.section = existing
                    else:
                        self.section = {
                            'id': sid,
                            'title': title['en'],
                            'titleUrdu': title.get('ur', ''),
                            'titlePashto': title.get('ps', ''),
                            'blocks': [],
                            'sourcePdfPages': [],
                            'sourcePrintedPages': []
                        }
                        self.unit['sections'].append(self.section)
                    if marker_done and pdf not in self.section['sourcePdfPages']:
                        self.section['sourcePdfPages'].append(pdf)
                        self.section['sourcePrintedPages'].append(meta['printedPage'])
                        self.section['blocks'].append({'t': 'page', 'pdf': pdf, 'printed': meta['printedPage']})
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
                self.add({'t': 'h', 'l': len(op) + 2, **tri(rest)})
            elif op == 'p':
                self.add({'t': 'p', **tri(rest)})
            elif op == 'm':
                self.add({'t': 'm', 'en': rest})
            elif op == 'eq':
                tex, _, tr = rest.partition('||')
                b = self.add({'t': 'eq', 'tex': tex.strip()})
                if tr.strip():
                    u, _, ps_ = tr.partition('||')
                    b.update({'ur': u.strip(), 'ps': ps_.strip(), 'en': tex.strip()})
            elif op in ('-', '--', '---'):
                tgt = self.target()
                item = {'lv': len(op), **tri(rest)}
                if tgt and tgt[-1].get('t') == 'ul':
                    tgt[-1]['items'].append(item)
                else:
                    tgt.append({'t': 'ul', 'items': [item]})
            elif op == 'slo':
                item = {'lv': 1, **tri(rest)}
                self.unit['slos'].append(item)
                tgt = self.target()
                if tgt and tgt[-1].get('t') == 'ul' and tgt[-1].get('slo'):
                    tgt[-1]['items'].append(item)
                else:
                    tgt.append({'t': 'ul', 'slo': True, 'items': [item]})
            elif op == 'box':
                kind, rest2 = split_no(rest)
                blk = self.add({'t': 'box', 'kind': kind, 'title': tri(rest2) if rest2 else None, 'blocks': []})
                self.stack.append(blk)
            elif op == 'example':
                no, rest2 = split_no(rest)
                blk = self.add({
                    't': 'example',
                    'no': no,
                    'id': f"u{self.unit['number']}-ex{no}-{len(self.unit['workedExamples'])+1}",
                    'title': tri(rest2) if rest2 else None,
                    'blocks': [],
                    'pdf': pdf,
                    'printed': meta['printedPage'],
                    'section': self.section['id'] if self.section else None
                })
                self.unit['workedExamples'].append(blk)
                self.stack.append(blk)
            elif op == 'exercise':
                blk = self.add({
                    't': 'exercise',
                    'id': rest,
                    'blocks': [],
                    'pdf': pdf,
                    'printed': meta['printedPage'],
                    'section': self.section['id'] if self.section else None
                })
                self.unit['exercises'].append(blk)
                self.stack.append(blk)
            elif op in ('endbox', 'endexample', 'endexercise'):
                want = {'endbox': 'box', 'endexample': 'example', 'endexercise': 'exercise'}[op]
                if self.stack and self.stack[-1]['t'] == want:
                    self.stack.pop()
            elif op == 'q':
                no, rest2 = split_no(rest)
                self.add({'t': 'q', 'no': no, 'parts': [], **tri(rest2)})
            elif op == 'qp':
                no, rest2 = split_no(rest)
                tgt = self.target()
                b = {'no': no, **tri(rest2)}
                last = next((x for x in reversed(tgt) if x['t'] != 'page'), None)
                if last is not None and last['t'] in ('q', 'parts'):
                    last['parts'].append(b)
                else:
                    tgt.append({'t': 'parts', 'parts': [b]})
            elif op == 'sol':
                ans, _, why = rest.partition('##')
                tgt = self.target()
                q = next((x for x in reversed(tgt) if x['t'] in ('q', 'parts')), None)
                if q:
                    owner = q['parts'][-1] if q.get('parts') else q
                    owner['sol'] = {'steps': [tri(why.strip())] if why.strip() else [], 'answer': ans.strip()}
            elif op == 'svg':
                svg_buf = self.add({'t': 'svg', 'cap': tri(rest) if rest else None, '_lines': []})
                meta['svg'] += 1
            elif op == 'table':
                blk = self.add({'t': 'table', 'cap': tri(rest) if rest else None, 'head': [], 'rows': []})
                self.stack.append(blk)
            elif op == 'th':
                if self.stack and self.stack[-1]['t'] == 'table':
                    cells = [tri(c.strip()) for c in rest.split('|')]
                    self.stack[-1]['head'] = cells
            elif op == 'tr':
                if self.stack and self.stack[-1]['t'] == 'table':
                    cells = [tri(c.strip()) for c in rest.split('|')]
                    self.stack[-1]['rows'].append(cells)
            elif op == 'endtable':
                if self.stack and self.stack[-1]['t'] == 'table':
                    self.stack.pop()
            elif op == 'ans':
                exid, qno, txt = [x.strip() for x in rest.split('|', 2)]
                self.answers.setdefault(exid, {})[qno] = txt

        self.ledger.append(meta)

def load_vocab():
    words = {}
    if VOCAB.exists():
        for line in VOCAB.read_text(encoding='utf-8').splitlines():
            s = line.strip()
            if not s or s.startswith('#'):
                continue
            parts = s.split('\t')
            if len(parts) >= 3:
                words[parts[0].lower()] = [parts[1], parts[2]]
    return words

def main():
    b = Builder()
    files = sorted(PAGES.glob('p[0-9][0-9][0-9].txt'))
    print(f"Building Class 2 Math from {len(files)} page files...")
    for f in files:
        idx = int(f.stem[1:])
        b.page(idx, f.read_text(encoding='utf-8'))

    vocab = load_vocab()
    units = [b.units[n] for n in sorted(b.units)]
    
    # Bridge to existing format for compatibility with existing readers
    for u in units:
        u['badge'] = 'Class 2 Textbook'
        u['description'] = f"KPTBB Class 2 Mathematics Unit {u['number']} ({u['title']})."
        u['pageRange'] = f"Pages {u.get('pageStart', 1)}–{u.get('pageStart', 1) + 20}"
        
        # Ensure theory field exists on sections
        for s in u['sections']:
            text_blocks = [x['en'] for x in s['blocks'] if x.get('t') in ('p', 'h') and 'en' in x]
            s['theory'] = '\n\n'.join(text_blocks[:10])
            ur_blocks = [x['ur'] for x in s['blocks'] if x.get('t') in ('p', 'h') and 'ur' in x]
            s['theoryUrdu'] = '\n\n'.join(ur_blocks[:10])
            s['rules'] = [x['en'] for x in s['blocks'] if x.get('t') == 'ul' for x in x.get('items', [])][:4]
            s['rulesUrdu'] = [x['ur'] for x in s['blocks'] if x.get('t') == 'ul' for x in x.get('items', []) if 'ur' in x][:4]

    book_meta = {
        'title': 'Mathematics 2 (KPTBB SNC 2020)',
        'source': SOURCE_JPG,
        'totalPdfPages': TOTAL_PAGES,
        'reviewedPdfPages': len(b.ledger),
        'frontMatter': b.front,
        'backMatter': b.back,
        'answers': b.answers,
        'complete': len(b.ledger) >= TOTAL_PAGES,
    }

    js_lines = [
        '// Khyber Pakhtunkhwa Textbook Board Mathematics 2 (Curriculum 2020)',
        '// Generated by build_math2.py from page-by-page verified source transcriptions.',
        'const MATH_2_DATA = ' + json.dumps(units, ensure_ascii=False, indent=2) + ';',
        'const MATH_2_BOOK = ' + json.dumps(book_meta, ensure_ascii=False, indent=2) + ';',
        'const MATH_2_WORDS = ' + json.dumps(vocab, ensure_ascii=False, indent=2) + ';',
        '',
        "if (typeof DATA !== 'undefined' && DATA) { DATA.math2Chapters = MATH_2_DATA; }",
        "if (typeof window !== 'undefined') {",
        "  window.MATH_2_DATA = MATH_2_DATA;",
        "  window.MATH_2_BOOK = MATH_2_BOOK;",
        "  window.MATH_2_WORDS = MATH_2_WORDS;",
        "}",
        ""
    ]

    OUT.write_text('\n'.join(js_lines), encoding='utf-8')
    LEDGER.write_text(json.dumps(b.ledger, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Successfully wrote {OUT} ({OUT.stat().st_size:,} bytes) and {LEDGER}")

if __name__ == '__main__':
    main()
