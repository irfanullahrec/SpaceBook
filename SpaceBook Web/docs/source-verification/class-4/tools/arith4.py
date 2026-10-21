"""Insert SpaceBook answers (`solution` + `ss`/`sm` steps) after plain arithmetic questions of a Class 4 page.

    python arith4.py [SUBJ=math] [--write]       (dry run counts; --write edits the page files)

Only unambiguous items are handled: a column array (A + B / A - B), `A + B`, `A - B`, `A x B`, `A ÷ B`, and the
`D ) N` long-division picture. Every value is computed here, never typed. Items that already carry an answer
(sol / solution / qsol) are left alone; everything else (word problems, patterns, fractions) is NOT touched.
"""
import re, sys
from pathlib import Path

import os
HERE = Path(__file__).resolve().parents[1]
if os.environ.get('CLS'):          # CLS=2 runs the same pass over docs/source-verification/class-2
    HERE = HERE.parent / ('class-' + os.environ['CLS'])
SYM = {'+': '+', '-': '-', 'x': r'\times', '/': r'\div'}
STEP = {
    '+': ('Add the numbers column by column from the ones, carrying when a column sum is 10 or more.',
          'اکائی سے شروع کر کے کالم وار جمع کریں؛ جب کسی کالم کا مجموعہ 10 یا زیادہ ہو تو حاصل آگے لے جائیں۔',
          'له یوونو څخه پیل کړئ او ستون په ستون جمع کړئ؛ کله چې د ستون مجموعه 10 یا ډېره وي، انتقال یې مخ ته یوسئ.'),
    '-': ('Subtract column by column from the ones, borrowing when the top digit is smaller.',
          'اکائی سے شروع کر کے کالم وار تفریق کریں؛ جب اوپر کا ہندسہ چھوٹا ہو تو ادھار لیں۔',
          'له یوونو څخه پیل کړئ او ستون په ستون تفریق کړئ؛ کله چې پورته رقم کوچنی وي، پور واخلئ.'),
    'x': ('Multiply by each digit of the second number, shift each partial product one place left, then add.',
          'دوسرے عدد کے ہر ہندسے سے ضرب دیں، ہر جزوی حاصلِ ضرب کو ایک مقام بائیں کھسکائیں، پھر جمع کریں۔',
          'د دوهم عدد په هر رقم کې ضرب کړئ، هر جزوي حاصل ضرب یو ځای کیڼ لوري ته وښوروئ، بیا یې جمع کړئ.'),
    '/': ('Divide step by step: how many times does the divisor go into each part of the number? Write the quotient digit, multiply back, subtract and bring down the next digit.',
          'قدم بہ قدم تقسیم کریں: مقسوم علیہ عدد کے ہر حصے میں کتنی بار آتا ہے؟ خارجِ قسمت کا ہندسہ لکھیں، ضرب دے کر تفریق کریں اور اگلا ہندسہ نیچے لائیں۔',
          'ګام په ګام ووېشئ: وېشونکی د شمېرې په هره برخه کې څو ځله راځي؟ د خارج قسمت رقم ولیکئ، ضرب کړئ، تفریق کړئ او بل رقم ښکته راوړئ.'),
}
SMALL = {   # child-level wording when both numbers are below 100 (Classes 1-3)
    '+': ('Add the ones first, then add the tens.',
          'پہلے اکائیاں جمع کریں، پھر دہائیاں جمع کریں۔',
          'لومړی یوونه سره جمع کړئ، بیا لسیزې سره جمع کړئ.'),
    '-': ('Take away the ones first, then take away the tens.',
          'پہلے اکائیاں منفی کریں، پھر دہائیاں منفی کریں۔',
          'لومړی یوونه تفریق کړئ، بیا لسیزې تفریق کړئ.'),
    'x': ('Use the multiplication table: count equal groups.',
          'پہاڑے کی مدد لیں: برابر گروہ گنیں۔',
          'د جدول مرسته واخلئ: مساوي ډلې وشمېرئ.'),
    '/': ('Share equally: how many groups of the divisor fit in the number? Use the multiplication table backwards.',
          'برابر بانٹیں: عدد میں مقسوم علیہ کے کتنے گروہ آتے ہیں؟ پہاڑے کو الٹ کر دیکھیں۔',
          'مساوي ووېشئ: په شمېره کې د وېشونکي څو ډلې راځي؟ جدول بېرته وکاروئ.'),
}
WRITE = ('Write the question', 'سوال لکھیں', 'پوښتنه ولیکئ')
RESULT = ('So the answer is', 'لہٰذا جواب ہے', 'نو ځواب دی')
CHECK = ('Check by multiplying back: the divisor times the quotient (plus the remainder) gives the number.',
         'تصدیق کے لیے واپس ضرب دیں: مقسوم علیہ ضرب خارجِ قسمت (جمع باقی) عدد کے برابر آتا ہے۔',
         'د تایید لپاره بېرته ضرب کړئ: وېشونکی ضرب خارج قسمت (او پاتې) شمېره ورکوي.')


def t(n):
    return f'{n:,}'.replace(',', '{,}')


def num(s):
    return int(re.sub(r'[,\s]|\{,\}', '', s))


def parse(text):
    """-> (a, op, b) or None"""
    s = text.strip()
    if r'\begin{array}' in s:
        body = re.search(r'\\begin\{array\}\{[^}]*\}(.*)\\end\{array\}', s, re.S)
        if not body:
            return None
        rows = [r.replace(r'\hline', '').strip() for r in body.group(1).split(r'\\')]
        digs = []
        for r in rows:
            cells = [c.strip() for c in r.split('&')]
            if not any(cells) or any(c.startswith('\\text') for c in cells):
                continue
            digs.append(cells)
        if len(digs) < 2:
            return None
        if any(c and not c.isdigit() for c in digs[0]):
            return None
        top = ''.join(digs[0])
        sec = digs[1]
        sign = next((c for c in sec if c in ('+', '-', '−', r'\times')), None)
        bot = ''.join(c for c in sec if c.isdigit())
        if not top or not bot or sign is None or any(c and not (c.isdigit() or c == sign) for c in sec):
            return None
        op = {'+': '+', '-': '-', '−': '-', r'\times': 'x'}[sign]
        return int(top), op, int(bot)
    m = re.match(r'^\$?\s*(\d[\d,{}]*)\s*(?:\\,)?\s*\\overline\{\)\s*(?:\\,)?\s*(\d[\d,{}]*)\}\s*\$?$', s)
    if m:
        return num(m.group(2)), '/', num(m.group(1))
    m = re.match(r'^\$?\s*(\d[\d,{}]*)\s*(\+|−|-|×|x|÷|/|\\times|\\div)\s*(\d[\d,{}]*)\s*(?:=\s*\??)?\s*\$?$', s)
    if m:
        op = {'+': '+', '−': '-', '-': '-', '×': 'x', 'x': 'x', r'\times': 'x', '÷': '/', '/': '/', r'\div': '/'}[m.group(2)]
        return num(m.group(1)), op, num(m.group(3))
    return None


def build(a, op, b):
    if op == '/':
        if b == 0:
            return None
        q, r = divmod(a, b)
        ans = f'{q:,}' + (f' r {r}' if r else '')
        res = f'{t(a)} \\div {t(b)} = {t(q)}' + (f'\\text{{ remainder }}{r}' if r else '')
        chk = f'{t(b)} \\times {t(q)}' + (f' + {r}' if r else '') + f' = {t(a)}'
    else:
        v = a + b if op == '+' else a - b if op == '-' else a * b
        if v < 0:
            return None
        ans = f'{v:,}'
        res = f'{t(a)} {SYM[op]} {t(b)} = {t(v)}'
        chk = None
    st = SMALL[op] if max(a, b) < 100 else STEP[op]
    lines = [f'solution {ans}',
             f'ss {WRITE[0]}. || {WRITE[1]}۔ || {WRITE[2]}.',
             f'sm {t(a)} {SYM[op]} {t(b)}',
             f'ss {st[0]} || {st[1]} || {st[2]}',
             f'sm {res}']
    if chk:
        lines += [f'ss {CHECK[0]} || {CHECK[1]} || {CHECK[2]}', f'sm {chk}']
    lines += [f'ss {RESULT[0]} {ans}. || {RESULT[1]} {ans}۔ || {RESULT[2]} {ans}.']
    return lines


def process(path, write):
    src = path.read_text(encoding='utf8').split('\n')
    out, n = [], 0
    parent_solved = False
    for i, line in enumerate(src):
        out.append(line)
        m = re.match(r'^(q|qp)\s+(\S+)\s*\|\s*(.*)$', line)
        if not m:
            continue
        nxt = src[i + 1] if i + 1 < len(src) else ''
        first = m.group(3).split(' || ')[0]
        if m.group(1) == 'q':             # qsolve / qsol on the parent question answers all its parts
            parent_solved = False
            for x in src[i + 1:]:
                if re.match(r'^(q|exercise|endexercise|h|page|unit)\b', x):
                    break
                if re.match(r'^(qsolve|qsol)\b', x):
                    parent_solved = True
        if m.group(1) == 'qp' and parent_solved:
            continue
        if m.group(1) == 'q' and nxt.startswith('qp '):
            continue
        # an answer may follow after eq/fig lines: look ahead to the next question line
        ahead = []
        for x in src[i + 1:]:
            if re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', x):
                break
            ahead.append(x)
        if any(re.match(r'^(sol|solution|qsol|qsolution|qsolve)\b', x) for x in ahead):
            continue
        p = parse(first)
        lines = build(*p) if p else None
        if lines:
            if '--list' in sys.argv:
                print(path.name, line[:100])
            out.extend(lines)
            n += 1
    if write and n:
        with open(path, 'w', encoding='utf8', newline='\n') as f:
            f.write('\n'.join(out))
    return n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    subj = args[0] if args else 'math'
    total = sum(process(p, '--write' in sys.argv) for p in sorted((HERE / subj / 'pages').glob('p*.txt')))
    print(f'{subj}: {total} answers {"written" if "--write" in sys.argv else "found (dry run)"}')


if __name__ == '__main__':
    main()

