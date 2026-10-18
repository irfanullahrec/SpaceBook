"""Fraction exercise parts -> DSL lines (qp + solution with steps).

stdin lines:  LETTER EXPR      EXPR tokens: fractions a/b, mixed w_a/b, whole numbers, operators + - x /
e.g.          b 5_2/3 + 2_5/7
              c 3/4 x 8/9
Printed question keeps the book's form (mixed numbers stay mixed). Prints to stdout.
"""
import sys
from fractions import Fraction
from math import lcm


def parse(tok):
    if '_' in tok:
        w, f = tok.split('_')
        n, d = f.split('/')
        return Fraction(int(w) * int(d) + int(n), int(d)), (int(w), int(n), int(d))
    if '/' in tok:
        n, d = tok.split('/')
        return Fraction(int(n), int(d)), (0, int(n), int(d))
    return Fraction(int(tok)), (int(tok), 0, 1)


def tex_raw(w, n, d):
    if n == 0:
        return str(w)
    return (str(w) if w else '') + f'\\dfrac{{{n}}}{{{d}}}'


def tex_imp(n, d):
    return f'\\dfrac{{{n}}}{{{d}}}' if d != 1 else str(n)


def tex_frac(f):
    """Simplified fraction shown as a mixed number when improper."""
    f = Fraction(f)
    if f.denominator == 1:
        return str(f.numerator)
    w, r = divmod(f.numerator, f.denominator)
    if w and r:
        return f'{w}\\dfrac{{{r}}}{{{f.denominator}}}'
    return f'\\dfrac{{{f.numerator}}}{{{f.denominator}}}'


OPS = {'+': '+', '-': '-', 'x': '\\times', '/': '\\div'}


def solve(expr):
    toks = expr.split()
    vals, raws, ops = [], [], []
    for i, t in enumerate(toks):
        if i % 2:
            ops.append(t)
        else:
            v, r = parse(t)
            vals.append(v)
            raws.append(r)
    q = ' '.join(tex_raw(*raws[i // 2]) if i % 2 == 0 else OPS[t] for i, t in enumerate(toks))
    lines = []
    imp = []
    for (w, n, d), v in zip(raws, vals):
        imp.append((w * d + n, d) if n else (w, 1))
    has_mixed = any(r[0] and r[1] for r in raws)
    if all(o in '+-' for o in ops):
        L = lcm(*[d for _, d in imp])
        if has_mixed:
            lines.append(('Change mixed numbers into improper fractions.', 'مخلوط اعداد کو غیر واجب کسور میں تبدیل کریں۔', 'مخلوط عددونه په ناسمو کسرونو واړوئ.',
                          ' '.join(tex_imp(*imp[i // 2]) if i % 2 == 0 else OPS[t] for i, t in enumerate(toks))))
        if len({d for _, d in imp}) > 1:
            lines.append((f'The LCM of the denominators is {L}; make every denominator {L}.', f'نسب نماؤں کا ذو اضعاف اقل {L} ہے؛ ہر نسب نما کو {L} بنائیں۔', f'د مخرجونو کوچنی مشترک ضرب {L} دی؛ هر مخرج {L} کړئ.',
                          ' '.join((f'\\dfrac{{{n} \\times {L // d}}}{{{d} \\times {L // d}}}' if d != 1 else f'\\dfrac{{{n} \\times {L}}}{{{L}}}') if i % 2 == 0 else OPS[t]
                                   for i, (t, (n, d)) in enumerate(zip(toks, [imp[k // 2] if k % 2 == 0 else (0, 1) for k in range(len(toks))])))))
        nums = [n * (L // d) for n, d in imp]
        top = ' '.join(str(nums[i // 2]) if i % 2 == 0 else OPS[t] for i, t in enumerate(toks))
        total = sum(Fraction(n, L) * (1 if i == 0 or ops[i - 1] == '+' else -1) for i, n in enumerate(nums))
        tn = total * L
        lines.append(('Add or subtract the numerators over the common denominator.', 'مشترک نسب نما پر شمار کنندہ جمع یا تفریق کریں۔', 'په ګډ مخرج د صورتونو جمع یا تفریق وکړئ.',
                      f'= \\dfrac{{{top}}}{{{L}}} = \\dfrac{{{tn.numerator if tn.denominator == 1 else tn}}}{{{L}}}'))
        result = total
    else:
        result = vals[0]
        for o, v in zip(ops, vals[1:]):
            result = result * v if o == 'x' else result / v
        if has_mixed:
            lines.append(('Change mixed numbers into improper fractions.', 'مخلوط اعداد کو غیر واجب کسور میں تبدیل کریں۔', 'مخلوط عددونه په ناسمو کسرونو واړوئ.',
                          ' '.join(tex_imp(*imp[i // 2]) if i % 2 == 0 else OPS[t] for i, t in enumerate(toks))))
        if '/' in ops:
            parts = [tex_imp(*imp[0])]
            for o, (n, d) in zip(ops, imp[1:]):
                parts += ['\\times', tex_imp(d, n) if o == '/' else tex_imp(n, d)]
            lines.append(('To divide, multiply by the reciprocal of the divisor.', 'تقسیم کے لیے مقسوم علیہ کے معکوس سے ضرب دیں۔', 'د وېش لپاره د وېشونکي په معکوس کې ضرب کړئ.', ' '.join(parts)))
        lines.append(('Multiply numerators together and denominators together, then simplify.', 'شمار کنندوں کو آپس میں اور نسب نماؤں کو آپس میں ضرب دیں، پھر مختصر کریں۔', 'صورتونه سره او مخرجونه سره ضرب کړئ، بیا یې ساده کړئ.',
                      f'= \\dfrac{{{result.numerator}}}{{{result.denominator}}}' if result.denominator != 1 else f'= {result.numerator}'))
    fin = tex_frac(result)
    lines.append(('Write the answer in its simplest form.', 'جواب کو مختصر ترین صورت میں لکھیں۔', 'ځواب په ساده بڼه ولیکئ.', f'= {fin}'))
    return q, fin, lines


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        letter, expr = line.split(' ', 1)
        q, fin, lines = solve(expr)
        print(f'qp {letter} | ${q}$')
        print(f'solution ${fin}$')
        for en, ur, ps, m in lines:
            print(f'ss {en} || {ur} || {ps}')
            print(f'sm {m}')
        print('endsolution')


if __name__ == '__main__':
    main()
