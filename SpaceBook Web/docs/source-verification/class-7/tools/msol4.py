"""msol4.py - laws of exponents with worked steps."""
import re
import sympy as sp
import msol, msol2
from msol import step, ParseError

B = chr(92)


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m is not None:
        d['m'] = m
    return d


LAW = {
    'product': ('Product law: same base, add the exponents: a^m × a^n = a^(m+n)', 'ضربی قانون: ایک ہی بنیاد ہو تو طاقتیں جمع کریں: a^m × a^n = a^(m+n)', 'د ضرب قانون: یو شان بنسټ وي نو توانونه جمع کړئ: a^m × a^n = a^(m+n)'),
    'product_exp': ('Same exponent, different bases: multiply the bases: a^m × b^m = (ab)^m', 'طاقت ایک جیسی ہو تو بنیادیں ضرب دیں: a^m × b^m = (ab)^m', 'توان یو شان وي نو بنسټونه ضرب کړئ: a^m × b^m = (ab)^m'),
    'quotient': ('Quotient law: same base, subtract the exponents: a^m ÷ a^n = a^(m−n)', 'تقسیمی قانون: ایک ہی بنیاد ہو تو طاقتیں تفریق کریں: a^m ÷ a^n = a^(m−n)', 'د وېش قانون: یو شان بنسټ وي نو توانونه تفریق کړئ: a^m ÷ a^n = a^(m−n)'),
    'power': ('Power of a power: multiply the exponents: (a^m)^n = a^(mn)', 'طاقت کی طاقت: طاقتیں ضرب کریں: (a^m)^n = a^(mn)', 'د توان توان: توانونه سره ضرب کړئ: (a^m)^n = a^(mn)'),
    'apply': ('Apply the laws of exponents:', 'قوانینِ طاقت استعمال کریں:', 'د توانونو قوانین وکاروئ:'),
}


def base_exp(t):
    """'(-8)^3' / 'x^{3}' / '\\left(\\frac{5}{8}\\right)^2' -> (base_tex, exp_tex) ; None if not a power"""
    t = msol.clean_tex(t).strip()
    # split at last top-level ^
    depth = 0
    pos = -1
    for i, ch in enumerate(t):
        if ch in '({[': depth += 1
        elif ch in ')}]': depth -= 1
        elif ch == '^' and depth == 0:
            pos = i
    if pos < 0:
        return None
    b, e = t[:pos].strip(), t[pos + 1:].strip()
    if e.startswith('{') and e.endswith('}'):
        e = e[1:-1]
    return b, e


def two_powers(text, op):
    t = msol.clean_tex(text)
    t = t.strip('()') if t.startswith('(') and t.endswith(')') and op == '\\div' else t
    parts = [p.strip() for p in t.split(op)]
    if len(parts) != 2:
        raise ParseError('two')
    a, b = base_exp(parts[0]), base_exp(parts[1])
    if not a or not b:
        raise ParseError('pow')
    return a, b


def numeric_equal(l, r):
    try:
        return sp.simplify(msol2.tex_to_sympy(l) - msol2.tex_to_sympy(r)) == 0
    except Exception:
        return True   # symbolic exponents: structural law application, nothing to evaluate


def product_law(text):
    a, b = two_powers(text, B + 'times')
    (ba, ea), (bb, eb) = a, b
    given = msol.clean_tex(text)
    if ba == bb:
        res = f'{ba}^{{{ea} + {eb}}}'
        try:
            ne = sp.simplify(msol2.tex_to_sympy(ea) + msol2.tex_to_sympy(eb)); res2 = f'{ba}^{{{sp.latex(ne)}}}'
        except Exception:
            res2 = res
        steps = [msol.step('given', given), S(*LAW['product']), S('Add the exponents:', 'طاقتیں جمع کریں:', 'توانونه جمع کړئ:', f'{res} = {res2}')]
        final = res2
    elif ea == eb:
        newb = f'({ba} {B}times {bb})'
        try:
            nb = sp.latex(sp.expand(msol2.tex_to_sympy(ba) * msol2.tex_to_sympy(bb)))
        except Exception:
            nb = f'{ba}{bb}'
        steps = [msol.step('given', given), S(*LAW['product_exp']), S('Multiply the bases:', 'بنیادیں ضرب دیں:', 'بنسټونه ضرب کړئ:', f'{newb}^{{{ea}}} = ({nb})^{{{ea}}}')]
        final = f'({nb})^{{{ea}}}'
    else:
        raise ParseError('mixed')
    return steps, final


def quotient_law(text):
    a, b = two_powers(text, B + 'div')
    (ba, ea), (bb, eb) = a, b
    if ba != bb:
        raise ParseError('bases differ')
    try:
        ne = sp.simplify(msol2.tex_to_sympy(ea) - msol2.tex_to_sympy(eb)); res2 = f'{ba}^{{{sp.latex(ne)}}}'
    except Exception:
        res2 = f'{ba}^{{{ea} - {eb}}}'
    steps = [msol.step('given', msol.clean_tex(text)), S(*LAW['quotient']), S('Subtract the exponents:', 'طاقتیں تفریق کریں:', 'توانونه تفریق کړئ:', f'{ba}^{{{ea} - {eb}}} = {res2}')]
    return steps, res2


def power_of_power(text):
    t = msol.clean_tex(text).strip()
    inner = t
    # strip outer brackets with one more exponent: [ (b)^m ]^n
    be = base_exp(t)
    if not be:
        raise ParseError('pp')
    inside, n = be
    inside = inside.strip()
    if inside[0] in '([' and inside[-1] in ')]':
        inside = inside[1:-1]
    bm = base_exp(inside)
    if not bm:
        raise ParseError('pp2')
    b, m = bm
    try:
        e = sp.latex(sp.simplify(msol2.tex_to_sympy(m) * msol2.tex_to_sympy(n)))
    except Exception:
        e = f'{m} {B}times {n}'
    res = f'{b}^{{{e}}}'
    steps = [msol.step('given', msol.clean_tex(text)), S(*LAW['power']), S('Multiply the exponents:', 'طاقتیں ضرب دیں:', 'توانونه ضرب کړئ:', f'{b}^{{{m} {B}times {n}}} = {res}')]
    return steps, res


def simplify_expr(text):
    """numeric / symbolic expression with negative and zero exponents; sympy does the algebra."""
    e = msol2.tex_to_sympy(text)
    res = sp.simplify(sp.powsimp(sp.powdenest(e, force=True), force=True))
    steps = [msol.step('given', msol.clean_tex(text)), S(*LAW['apply'], sp.latex(res))]
    return steps, res


# ---------------------------------------------------------------- decimals, absolute value, subsets
def frac_decimal(text):
    import math
    from fractions import Fraction
    ast = msol.parse_tex(msol.clean_tex(text))
    v = msol.val(ast)
    r = Fraction(v)
    d = r.denominator
    dd = d
    fac = sp.factorint(d)
    term = all(p in (2, 5) for p in fac)
    num, den = r.numerator, r.denominator
    pf = ' \\times '.join(f'{p}^{{{e}}}' if e > 1 else str(p) for p, e in sorted(fac.items())) if d > 1 else '1'
    steps = [msol.step('given', msol.clean_tex(text)),
             S('Reduce the fraction and factorize the denominator:', 'کسر کو مختصر کریں اور نسب نما کے مفرد اجزا لکھیں:', 'کسر ساده کړئ او د مخرج فکتورونه ولیکئ:', f'{msol.tex_num(r)},\\quad {den} = {pf}'),
             S('If the denominator has only the prime factors 2 and 5 the decimal terminates; otherwise it does not terminate (it recurs).', 'اگر نسب نما کے مفرد اجزا صرف 2 اور 5 ہوں تو اعشاریہ ختم ہو جاتا ہے، ورنہ ختم نہیں ہوتا (دہراتا ہے)۔', 'که د مخرج لومړني فکتورونه یوازې 2 او 5 وي نو اعشاریه پای ته رسېږي، ګنې نه (تکراري).',
               ('\\text{Terminating}' if term else '\\text{Non-terminating (recurring)}'))]
    if term:
        steps.append(S('Divide:', 'تقسیم کریں:', 'ووېشئ:', f'{msol.tex_num(r)} = {float(r):g}'))
    else:
        dec = f'{float(r):.6f}'.rstrip('0')
        steps.append(S('Divide (the digits repeat):', 'تقسیم کریں (ہندسے دہراتے ہیں):', 'ووېشئ (رقمونه تکراري دي):', f'{msol.tex_num(r)} = {dec}\\ldots'))
    return steps, ('Terminating' if term else 'Non-terminating')


def decimal_kind(text):
    t = text.strip().strip('$')
    rec = ('overline' in t) or ('dot' in t)
    steps = [msol.step('given', msol.clean_tex(t)),
             S('A bar or dots over digits show that they repeat for ever, so the decimal does not terminate; a decimal that just ends is terminating.', 'ہندسوں پر لکیر یا نقطے کا مطلب ہے وہ ہمیشہ دہراتے ہیں، اس لیے اعشاریہ ختم نہیں ہوتا؛ جو اعشاریہ ختم ہو جائے وہ ختم ہونے والا ہے۔', 'د رقمونو پر کرښه یا ټکي ښيي چې تل تکراري دي، نو اعشاریه پای ته نه رسېږي؛ هغه چې پای ته ورسېږي، پای ته رسېدونکې ده.',
               '\\text{Non-terminating (recurring)}' if rec else '\\text{Terminating}')]
    return steps, ('Non-terminating' if rec else 'Terminating')


def absolute_value(text):
    items = [x.strip() for x in re.split(r'\s+and\s+', text.replace('$', ''))]
    ast = msol.parse_tex(msol.clean_tex(items[0]))
    v = ast
    try:
        val_ = msol.val(ast)
        res = msol.tex(msol.leaf(abs(val_))) if val_.denominator != 1 or True else str(abs(val_))
        if msol.has_dec(ast): res = msol.tex_num(abs(val_), msol.dec_places(ast))
    except Exception:
        res = msol.clean_tex(items[0]).lstrip('-')
    steps = [msol.step('given', f'|{msol.clean_tex(items[0])}|,\\; |{msol.clean_tex(items[1]) if len(items) > 1 else ""}|'),
             S('The absolute value is the distance from zero; it is never negative:', 'مطلق قدر صفر سے فاصلہ ہے؛ یہ کبھی منفی نہیں ہوتی:', 'مطلق قیمت له صفر څخه واټن دی؛ هېڅکله منفي نه وي:', f'|x| = |-x| = {res}')]
    return steps, res


def subsets(text):
    s = text.replace('$', '').replace('−', '-')
    m = re.search(r'\{[^{}]*\}', s)
    if not m or '|' in s or 'mid' in s:
        raise ParseError('roster')
    import msol_sets
    r = msol_sets.roster(m.group(0))
    if r is None:
        raise ParseError('roster')
    n = len(r)
    steps = [msol.step('given', msol_sets.fmt(r)),
             S('A set with n elements has 2^n subsets:', 'n عناصر والے سیٹ کے 2^n ذیلی سیٹ ہوتے ہیں:', 'د n عناصرو لرونکي سیټ 2^n فرعي سیټونه لري:', f'n = {n},\\quad 2^{{{n}}} = {2 ** n}')]
    return steps, 2 ** n


def base_exp_value(text):
    be = base_exp(text)
    if not be:
        raise ParseError('be')
    b, e = be
    bv = msol.val(msol.parse_tex(b)); ev = msol.val(msol.parse_tex(e))
    v = bv ** int(ev)
    steps = [msol.step('given', msol.clean_tex(text)),
             S('In a^n, a is the base and n is the exponent; the value is a multiplied by itself n times:', 'a^n میں a بنیاد اور n طاقت ہے؛ قیمت a کو n بار خود سے ضرب دینے سے ملتی ہے:', 'په a^n کې a بنسټ او n توان دی؛ ارزښت د a n ځله ضرب دی:', f'\\text{{base}} = {msol.tex(msol.parse_tex(b))},\; \\text{{exponent}} = {int(ev)},\; \\text{{value}} = {msol.tex_num(v)}')]
    return steps, f'Base {msol.tex_num(bv)}, exponent {int(ev)}, value {msol.tex_num(v)}'


J = {
    'perfect': ('{n} is a perfect {w}, so the root is the integer {r}.', '{n} ایک مکمل {wu} ہے، لہٰذا جذر عدد صحیح {r} ہے۔', '{n} بشپړ {wp} دی، نو جذر بشپړ عدد {r} دی.'),
    'nonperfect': ('{n} is not a perfect {w}, so the root is a non-terminating, non-recurring decimal.', '{n} مکمل {wu} نہیں، لہٰذا جذر غیر اختتامی اور غیر دہرانے والا اعشاریہ ہے۔', '{n} بشپړ {wp} نه دی، نو جذر نه پای ته رسېدونکی او نه تکراري اعشاریه ده.'),
    'zero': ('Division by zero is not defined, so this is not a number.', 'صفر پر تقسیم معرف نہیں، لہٰذا یہ عدد نہیں۔', 'په صفر وېش تعریف شوی نه دی، نو دا عدد نه دی.'),
    'recurring': ('A recurring (repeating) decimal can be written as a fraction.', 'دہرانے والا اعشاریہ کسر کی صورت میں لکھا جا سکتا ہے۔', 'تکراري اعشاریه د کسر په بڼه لیکل کېدی شي.'),
    'terminating': ('A terminating decimal or integer can be written as a fraction p/q.', 'ختم ہونے والا اعشاریہ یا صحیح عدد کسر p/q کی صورت میں لکھا جا سکتا ہے۔', 'پای ته رسېدونکې اعشاریه یا بشپړ عدد د کسر p/q په بڼه لیکل کېدی شي.'),
    'fraction': ('It is already a fraction p/q of integers (q is not zero).', 'یہ پہلے ہی صحیح اعداد کا کسر p/q ہے (q صفر نہیں)۔', 'دا مخکې له مخکې د بشپړو عددونو کسر p/q دی (q صفر نه دی).'),
}


def classify_real(text):
    import math
    t = text.strip().strip('$')
    m = re.fullmatch(r'\\sqrt\[3\]\{(\d+)\}', t)
    m2 = re.fullmatch(r'\\sqrt\{(\d+)\}', t)
    ctx = {}
    if m or m2:
        n = int((m or m2).group(1)); cube = bool(m)
        r = round(n ** (1 / 3)) if cube else math.isqrt(n)
        perfect = (r ** 3 == n) if cube else (r * r == n)
        kind = 'Rational' if perfect else 'Irrational'
        case = 'perfect' if perfect else 'nonperfect'
        ctx = dict(n=n, r=r, w='cube' if cube else 'square', wu='مکعب' if cube else 'مربع', wp='مکعب' if cube else 'مربع')
    elif re.search(r'\\frac\{[^}]*\}\{0\}', t) or t.endswith('/0'):
        kind, case = 'Not defined', 'zero'
    elif 'overline' in t or 'dot' in t:
        kind, case = 'Rational', 'recurring'
    elif re.fullmatch(r'-?[\d.]+', t.replace('−', '-')):
        kind, case = 'Rational', 'terminating'
    elif 'frac' in t:
        kind, case = 'Rational', 'fraction'
    else:
        raise ParseError('class')
    e, u, p = [x.format(**ctx) for x in J[case]]
    steps = [msol.step('given', t.replace('−', '-')), S(e, u, p, '\text{' + kind + '}')]
    return steps, kind
