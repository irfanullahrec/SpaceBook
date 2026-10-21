"""Worked-equation chains for Class 4 Maths fraction and decimal exercises, using the instruction line to know the operation.

    python upgrade_ctx4.py [--write]

Handles the parts `X, Y` under "Add / Subtract / Multiply / Divide ..." and the parts `X op Y` (fractions, mixed numbers,
whole numbers, decimals). The existing one-line answer (copied from the printed key) is kept as step 1 and the value
computed here must equal the key's value, otherwise the item is NOT changed and is listed. Nothing is typed by hand.
"""
import re, sys
from fractions import Fraction
from decimal import Decimal
from pathlib import Path

PAGES = Path(__file__).resolve().parents[1] / 'math' / 'pages'
NUM = r'(?:\d+\\frac\{\d+\}\{\d+\}|\\frac\{\d+\}\{\d+\}|\d[\d,]*(?:\.\d+)?)'


def val(tok):
    tok = tok.replace(',', '')
    m = re.fullmatch(r'(\d+)\\frac\{(\d+)\}\{(\d+)\}', tok)
    if m:
        return Fraction(int(m.group(1))) + Fraction(int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(r'\\frac\{(\d+)\}\{(\d+)\}', tok)
    if m:
        return Fraction(int(m.group(1)), int(m.group(2)))
    return Fraction(Decimal(tok))


def tex(fr, keep=None):
    """Fraction -> TeX; whole numbers plain, improper fractions as n/d"""
    if fr.denominator == 1:
        return f'{fr.numerator:,}'.replace(',', '{,}')
    return f'\\frac{{{fr.numerator}}}{{{fr.denominator}}}'


def mixed(fr):
    if fr.denominator == 1 or fr < 1:
        return None
    w, r = divmod(fr.numerator, fr.denominator)
    return f'{w}\\frac{{{r}}}{{{fr.denominator}}}' if r else None


def tok_tex(tok):
    return tok.replace(',', '{,}')


def key_value(text):
    s = text.split('##')[0].strip()
    s = s.replace('$', '')
    m = re.search(r'(\d+\\frac\{\d+\}\{\d+\}|\\frac\{\d+\}\{\d+\}|\d[\d,]*(?:\.\d+)?)', s)
    return val(m.group(1)) if m else None


T = {
    'write': ('Write the question.', 'سوال لکھیں۔', 'پوښتنه ولیکئ.'),
    'mixed': ('Change each mixed number to an improper fraction first.', 'پہلے ہر مخلوط عدد کو غیر واجب کسر بنائیں۔', 'لومړی هر مخلوط عدد په ناسم کسر واړوئ.'),
    '+': ('Same denominators: add the numerators and keep the denominator.', 'نسب نما برابر ہیں: شمار کنندوں کو جمع کریں اور نسب نما وہی رکھیں۔', 'مخرجونه یو شان دي: صورتونه سره جمع کړئ او مخرج هماغه وساتئ.'),
    '-': ('Same denominators: subtract the numerators and keep the denominator.', 'نسب نما برابر ہیں: شمار کنندوں کو تفریق کریں اور نسب نما وہی رکھیں۔', 'مخرجونه یو شان دي: صورتونه تفریق کړئ او مخرج هماغه وساتئ.'),
    'x': ('Multiply the numerators together and the denominators together, then write the answer in simplest form.', 'شمار کنندوں کو آپس میں اور نسب نماؤں کو آپس میں ضرب دیں، پھر سادہ ترین شکل میں لکھیں۔', 'صورتونه سره او مخرجونه سره ضرب کړئ، بیا په ساده بڼه یې ولیکئ.'),
    '/': ('Dividing by a whole number is the same as multiplying by its reciprocal (1 over that number).', 'مکمل عدد سے تقسیم اس کے معکوس (1 بٹا وہ عدد) سے ضرب کے برابر ہے۔', 'په بشپړ عدد وېش د هغه د معکوس (1 پر هغه عدد) سره د ضرب سره برابر دی.'),
    'res': ('So the answer is', 'لہٰذا جواب ہے', 'نو ځواب دی'),
}


def S(key, extra=''):
    en, ur, ps = T[key]
    return en, ur, ps


def chain(a, op, b, ta, tb):
    """-> (rows list of TeX strings, narration keys) or None. a, b Fractions; ta, tb source tokens."""
    steps = []
    ia, ib = a, b
    fa, fb = tex(a), tex(b)
    sym = {'+': '+', '-': '-', 'x': '\\times', '/': '\\div'}[op]
    if '\\frac' in ta and re.match(r'\d+\\frac', ta) or '\\frac' in tb and re.match(r'\d+\\frac', tb):
        steps.append(('mixed', f'{tok_tex(ta)} {sym} {tok_tex(tb)} = {fa} {sym} {fb}'))
    if op in '+-':
        if a.denominator != b.denominator:
            return None
        v = a + b if op == '+' else a - b
        num = f'{a.numerator} {sym} {b.numerator}'
        row = f'{fa} {sym} {fb} = \\frac{{{num}}}{{{a.denominator}}} = {tex(v)}'
        steps.append((op, row))
    elif op == 'x':
        v = a * b
        row = f'{fa} \\times {fb} = \\frac{{{a.numerator} \\times {b.numerator}}}{{{a.denominator} \\times {b.denominator}}}'
        raw = Fraction(a.numerator * b.numerator, a.denominator * b.denominator)
        row += f' = \\frac{{{a.numerator * b.numerator}}}{{{a.denominator * b.denominator}}}'
        if tex(v) != f'\\frac{{{a.numerator * b.numerator}}}{{{a.denominator * b.denominator}}}':
            row += f' = {tex(v)}'
        steps.append(('x', row))
    else:
        if b.denominator != 1 or b == 0:
            return None
        v = a / b
        row = f'{fa} \\div {tex(b)} = {fa} \\times \\frac{{1}}{{{b.numerator}}} = \\frac{{{a.numerator}}}{{{a.denominator * b.numerator}}}'
        if tex(v) != f'\\frac{{{a.numerator}}}{{{a.denominator * b.numerator}}}':
            row += f' = {tex(v)}'
        steps.append(('/', row))
    mx = mixed(v)
    if mx:
        steps[-1] = (steps[-1][0], steps[-1][1] + f' = {mx}')
    return v, steps


def parse_item(instr, text):
    t = text.strip().strip('$').strip()
    low = instr.lower()
    m = re.fullmatch(rf'({NUM})\s*(\+|−|-|\\times|×|\\div|÷)\s*({NUM})', t.replace('$', ''))
    if m:
        op = {'+': '+', '−': '-', '-': '-', '\\times': 'x', '×': 'x', '\\div': '/', '÷': '/'}[m.group(2)]
        return m.group(1), op, m.group(3)
    m = re.fullmatch(rf'({NUM})\s*,\s*({NUM})', t.replace('$', ''))
    if m:
        if 'add' in low:
            return m.group(1), '+', m.group(2)
        if 'multiply' in low:
            return m.group(1), 'x', m.group(2)
        if 'subtract' in low:
            a, b = val(m.group(1)), val(m.group(2))
            hi, lo = (m.group(1), m.group(2)) if a >= b else (m.group(2), m.group(1))
            return hi, '-', lo
    return None


def process(path, write, state):
    src = path.read_text(encoding='utf8').split('\n')
    out, n, bad = [], 0, []
    i = 0
    while i < len(src):
        line = src[i]
        out.append(line)
        m = re.match(r'^(q|qp)\s+(\S+)\s*\|\s*(.*)$', line)
        if m:
            first = m.group(3).split(' || ')[0]
            if m.group(1) == 'q':
                state['instr'] = first
            j, ans = i + 1, []
            while j < len(src) and not re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', src[j]):
                if re.match(r'^(sol|solution|qsol|qsolve|ss|sm)\b', src[j]):
                    ans.append(j)
                j += 1
            if len(ans) == 1 and src[ans[0]].startswith('sol ') and m.group(1) == 'qp' or (m.group(1) == 'q' and len(ans) == 1 and src[ans[0]].startswith('sol ')):
                it = parse_item(state.get('instr', ''), first)
                if it:
                    ta, op, tb = it
                    a, b = val(ta), val(tb)
                    sym_dec = '.' in ta or '.' in tb
                    if sym_dec:                          # decimals: exact Decimal chain from arith4
                        import arith4
                        da, db = Decimal(ta.replace(',', '')), Decimal(tb.replace(',', ''))
                        built = arith4.build(da, op, db)
                        kv = key_value(src[ans[0]][4:])
                        if built and kv is not None and Fraction(Decimal(built[0][9:])) == kv:
                            head, _, why = src[ans[0]][4:].partition('##')
                            out.extend(src[i + 1:ans[0]])
                            out.append('solution ' + head.strip())
                            if why.strip():
                                out.append('ss ' + why.strip())
                            out.extend(built[1:])
                            i = ans[0] + 1
                            n += 1
                            continue
                        elif built:
                            bad.append(f'{path.name} {m.group(2)}: key {head_of(src[ans[0]])} vs computed {built[0][9:]}')
                    if not sym_dec:
                        res = chain(a, op, b, ta, tb)
                        kv = key_value(src[ans[0]][4:])
                        if res and kv is not None and res[0] == kv:
                            v, steps = res
                            head, _, why = src[ans[0]][4:].partition('##')
                            out.extend(src[i + 1:ans[0]])
                            out.append('solution ' + head.strip())
                            if why.strip():
                                out.append('ss ' + why.strip())
                            ex = f'{tok_tex(ta)} {"\\times" if op == "x" else "\\div" if op == "/" else op} {tok_tex(tb)}'
                            en, ur, ps = T['write']
                            out.append(f'ss {en} || {ur} || {ps}')
                            out.append(f'sm {ex}')
                            for key, row in steps:
                                en, ur, ps = T[key]
                                out.append(f'ss {en} || {ur} || {ps}')
                                out.append(f'sm {row}')
                            en, ur, ps = T['res']
                            out.append(f'ss {en} {head.strip().strip("$")}. || {ur} {head.strip().strip("$")}۔ || {ps} {head.strip().strip("$")}.')
                            i = ans[0] + 1
                            n += 1
                            continue
                        elif res:
                            bad.append(f'{path.name} {m.group(2)}: key {head_of(src[ans[0]])} vs computed {res[0]}')
        i += 1
    if write and n:
        with open(path, 'w', encoding='utf8', newline='\n') as f:
            f.write('\n'.join(out))
    return n, bad


def head_of(line):
    return line[4:].split('##')[0].strip()


if __name__ == '__main__':
    tot, allbad, state = 0, [], {}
    for p in sorted(PAGES.glob('p*.txt')):
        n, bad = process(p, '--write' in sys.argv, state)
        tot += n
        allbad += bad
    print(f'{"upgraded" if "--write" in sys.argv else "can upgrade"}: {tot}; key disagrees with computed value: {len(allbad)}')
    for b in allbad[:30]:
        print('  ', b)
