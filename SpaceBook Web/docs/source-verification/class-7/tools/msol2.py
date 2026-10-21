"""msol2.py - algebra, equations, roots, fraction operations and the answer-key checker for msol.py."""
import re
from fractions import Fraction
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import msol
from msol import step, tex_num, ParseError, parse_tex, val, tex

TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
X, Y = sp.symbols('x y')


# ------------------------------------------------------------ TeX <-> sympy
def _frac_to_div(s):
    """replace \\frac{A}{B} (balanced braces) by ((A)/(B)), innermost last."""
    while True:
        i = s.find('\\frac')
        if i < 0:
            return s
        j = i + 5
        def grab(k):
            while k < len(s) and s[k] == ' ': k += 1
            if s[k] != '{': return None, k
            d, st = 0, k
            while k < len(s):
                if s[k] == '{': d += 1
                elif s[k] == '}':
                    d -= 1
                    if d == 0: return s[st + 1:k], k + 1
                k += 1
            return None, k
        A, k = grab(j)
        Bv, k2 = grab(k)
        if A is None or Bv is None:
            raise ParseError('frac')
        mixed = i > 0 and s[i - 1].isdigit()
        s = s[:i] + ('+' if mixed else '') + '((' + A + ')/(' + Bv + '))' + s[k2:]


def tex_to_sympy(s):
    s = msol.clean_tex(s)
    s = s.replace('\\times', '*').replace('\\div', '/').replace('\\cdot', '*')
    s = _frac_to_div(s)
    s = s.replace('{', '(').replace('}', ')').replace('\\', '')
    s = s.replace('[', '(').replace(']', ')')
    return parse_expr(s, transformations=TRANS, evaluate=True)


def poly_tex(e):
    return sp.latex(sp.expand(e), order='lex')


def same_value(a, b):
    try:
        return sp.simplify(a - b) == 0
    except Exception:
        return False


# ------------------------------------------------------------ key handling
def split_key(key):
    """'a) 1/2 b) x+1' -> {'a': '1/2', 'b': 'x+1'};  single answers -> {'': text}"""
    if not key:
        return {}
    pos = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r'(?:^|(?<=\s)|(?<=;))\(?\b([a-zA-Z]|i{1,3}|iv|v)\)\s', key)]
    if not pos:
        return {'': key.strip()}
    out = {}
    for i, (st, en, name) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(key)
        out[name.lower()] = key[en:end].strip().rstrip(';').strip()
    return out


def key_matches(key_text, result):
    """result: sympy expr / Fraction / list / str. Compare permissively."""
    if key_text is None:
        return None
    k = key_text.strip().rstrip('.')
    k = re.sub(r'^\$?\s*[A-Za-z]\s*=\s*', '', k)
    try:
        symres = isinstance(result, sp.Basic) and bool(result.free_symbols)
        kk = tex_to_sympy(re.sub(r'^Rs\.?\s*', '', k if symres else re.sub(r'(?<=\d)\s*([A-Za-z%]+/?[A-Za-z]*)$', '', k)))
    except Exception:
        kk = None
    if kk is not None:
        try:
            r = sp.nsimplify(result) if not isinstance(result, sp.Basic) else result
            if same_value(r, kk):
                return True
            if abs(float(r) - float(kk)) < 1e-3 * max(1, abs(float(kk))):
                return True
        except Exception:
            pass
    # mixed-number key like "-10\\frac{1}{5}"
    m = re.match(r'^\$?(-?)\s*(\d+)\s*\\frac\{(\d+)\}\{(\d+)\}\$?$', k)
    if m:
        v = Fraction(int(m.group(2))) + Fraction(int(m.group(3)), int(m.group(4)))
        v = -v if m.group(1) else v
        try:
            return float(result) == float(v)
        except Exception:
            return False
    return False


# ------------------------------------------------------------ steps: algebra
def alg_expand(expr_tex):
    e = tex_to_sympy(expr_tex)
    res = sp.expand(e)
    steps = [step('given', sp.latex(e, order='lex') if False else msol.clean_tex(expr_tex))]
    if e != res:
        steps.append(step('expand', poly_tex(e) if False else sp.latex(res, order='lex')))
    return steps, res


def alg_factor(expr_tex):
    e = tex_to_sympy(expr_tex)
    res = sp.factor(e)
    steps = [step('given', msol.clean_tex(expr_tex))]
    ex = sp.expand(e)
    g = sp.gcd_list([t for t in sp.Add.make_args(ex)]) if len(sp.Add.make_args(ex)) > 1 else 1
    if g not in (1, -1) and res != e:
        rest = sp.expand(ex / g)
        steps.append(step('common', f'{sp.latex(g)}\\left({sp.latex(rest, order="lex")}\\right)'))
        fr = sp.factor(rest)
        if fr != rest:
            steps.append(step('factor', f'{sp.latex(g)}\\left({sp.latex(fr)}\\right)' if fr.is_Mul or True else sp.latex(res)))
    else:
        steps.append(step('factor', sp.latex(res)))
    steps.append(step('check', f'{sp.latex(res)} = {sp.latex(sp.expand(res), order="lex")}'))
    return steps, res


def alg_simplify(expr_tex):
    e = tex_to_sympy(expr_tex)
    res = sp.expand(e)
    steps = [step('given', msol.clean_tex(expr_tex))]
    if sp.expand(e) != e:
        steps.append(step('expand', sp.latex(res, order='lex')))
    return steps, res


def solve_linear(eq_tex):
    """a one-variable linear equation 'lhs = rhs' (x or y). Returns steps, value."""
    t = msol.clean_tex(eq_tex)
    if '=' not in t:
        raise ParseError('noeq')
    l, r = t.split('=', 1)
    L, R = tex_to_sympy(l), tex_to_sympy(r)
    syms = (L - R).free_symbols
    if len(syms) != 1:
        raise ParseError('vars')
    v = list(syms)[0]
    sol = sp.solve(sp.Eq(L, R), v)
    if len(sol) != 1:
        raise ParseError('sol')
    s = sol[0]
    steps = [step('given', msol.clean_tex(eq_tex))]
    Lx, Rx = sp.expand(L), sp.expand(R)
    if (Lx, Rx) != (L, R) or sp.latex(Lx) != sp.latex(L):
        steps.append(step('expand', f'{sp.latex(Lx, order="lex")} = {sp.latex(Rx, order="lex")}'))
    # collect variable terms to the left
    a1 = Lx.coeff(v); a2 = Rx.coeff(v)
    c1 = Lx - a1 * v; c2 = Rx - a2 * v
    if a2 != 0:
        steps.append(step('sub_both', f'{sp.latex(Lx - a2 * v, order="lex")} = {sp.latex(Rx - a2 * v, order="lex")}', t=sp.latex(a2 * v)))
        Lx, Rx = Lx - a2 * v, Rx - a2 * v
    c = sp.expand(Lx - Lx.coeff(v) * v)
    if c != 0:
        key = 'sub_both' if c > 0 else 'add_both'
        t = sp.latex(c if c > 0 else -c)
        steps.append(step(key, f'{sp.latex(Lx.coeff(v) * v, order="lex")} = {sp.latex(sp.expand(Rx - c), order="lex")}', t=t))
        Rx = sp.expand(Rx - c); Lx = Lx.coeff(v) * v
    a = Lx.coeff(v)
    if a != 1:
        steps.append(step('div_both', f'{sp.latex(v)} = {sp.latex(s)}', t=sp.latex(a)))
    chk = f'{sp.latex(L.subs(v, s))} = {sp.latex(R.subs(v, s))}'
    steps.append(step('verify', chk))
    return steps, s


# ------------------------------------------------------------ steps: roots and squares
def prime_pairs(n):
    f = sp.factorint(n)
    parts = []
    for p, e in sorted(f.items()):
        parts += [p] * e
    return parts


def sqrt_by_factors(num_text):
    """integer, decimal or fraction (a/b, mixed). Returns steps, exact value"""
    s = msol.clean_tex(num_text)
    try:
        ast = parse_tex(s)
    except ParseError:
        raise
    v = val(ast)
    root = msol.exact_sqrt(v)
    if root is None:
        raise ParseError('notsq')
    steps = [step('given', f'\\sqrt{{{tex(ast)}}}')]
    if v.denominator == 1 and v >= 1:
        n = int(v)
        ps = prime_pairs(n)
        steps.append(step('primes', f'{n} = {" \\times ".join(map(str, ps))}'))
        taken = []
        for p in sorted(set(ps)):
            taken += [p] * (ps.count(p) // 2)
        steps.append(step('pairs', f'\\sqrt{{{n}}} = ' + (' \\times '.join(map(str, taken)) if taken else '1') + f' = {int(root)}'))
    else:
        f = Fraction(v)
        steps.append(step('to_frac', f'\\frac{{{f.numerator}}}{{{f.denominator}}}'))
        a, b = exact_int(f.numerator), exact_int(f.denominator)
        steps.append(step('sqrt_frac', f'\\frac{{\\sqrt{{{f.numerator}}}}}{{\\sqrt{{{f.denominator}}}}} = \\frac{{{a}}}{{{b}}}'))
        if msol.has_dec(ast):
            steps.append(step('ans', f'{float(root):g}'))
    return steps, root


def exact_int(n):
    return msol.exact_sqrt(n).numerator


def square_steps(n):
    n = int(n)
    return [step('given', f'{n}^2'), step('square', f'{n} \\times {n} = {n * n}')], n * n


# ------------------------------------------------------------ steps: fraction operations / inverses
def frac_nodes(texts):
    return [parse_tex(t) for t in texts]


def fraction_op(op, items):
    """items: TeX strings, op in + - * /. Builds the left-to-right expression and runs the BODMAS stepper.
    For two-fraction add/sub shows the LCD step."""
    joiner = {'+': ' + ', '-': ' - ', '*': ' \\times ', '/': ' \\div '}[op]
    parts = []
    for t in items:
        t = msol.clean_tex(t)
        parts.append(f'({t})' if (t.startswith('-') and parts) else t)
    expr = joiner.join(parts)
    steps, final, ast = msol.arithmetic_steps(expr)
    if op in '+-' and len(items) == 2:
        a, b = [msol.normalize_atoms(parse_tex(t)) for t in items]
        try:
            va, vb = val(a), val(b)
            if va.denominator != vb.denominator:
                L = msol.lcm(va.denominator, vb.denominator)
                ka, kb = L // va.denominator, L // vb.denominator
                mid = f'\\frac{{{va.numerator * ka}}}{{{L}}} {op} ' + (f'\\frac{{{vb.numerator * kb}}}{{{L}}}' if vb >= 0 else f'\\left(\\frac{{{vb.numerator * kb}}}{{{L}}}\\right)')
                steps.insert(1 if len(steps) > 1 else 1, step('lcd', mid))
        except Exception:
            pass
    return steps, final


def reciprocal_steps(t):
    v = val(parse_tex(t))
    r = 1 / v
    return [step('given', msol.clean_tex(t)), step('multinv', tex_num(r))], r


def additive_inverse_steps(t):
    v = val(parse_tex(t))
    return [step('given', msol.clean_tex(t)), step('additive', tex_num(-v))], -v


def to_improper_steps(t):
    ast = parse_tex(t)
    if ast[0] != 'mix':
        raise ParseError('nomix')
    w, n, d = ast[1], val(ast[2]), val(ast[3])
    num = w * int(d) + int(n)
    return [step('given', msol.clean_tex(t)), step('improper', f'\\frac{{{w} \\times {int(d)} + {int(n)}}}{{{int(d)}}} = \\frac{{{num}}}{{{int(d)}}}')], Fraction(num, int(d))


def to_mixed_steps(t):
    v = val(parse_tex(t))
    steps = [step('given', msol.clean_tex(t)), step('tomixed', msol.mixed_tex(v))]
    return steps, v


# ------------------------------------------------------------ verify identities, fraction squares
def verify_equal(eq_tex):
    t = msol.clean_tex(eq_tex)
    if '=' not in t:
        raise ParseError('noeq')
    l, r = [x.strip() for x in t.split('=', 1)]
    sl, vl, _ = msol.arithmetic_steps(l)
    sr, vr, _ = msol.arithmetic_steps(r)
    steps = [step('given', t)]
    lt = f'\\text{{LHS}} = {sl[-1]["m"]}' if sl[-1].get('m') else ''
    rt = f'\\text{{RHS}} = {sr[-1]["m"]}'
    # compact: show each side's chain end values
    steps.append({'en': 'Work out the left side:', 'ur': 'بایاں طرف حل کریں:', 'ps': 'کیڼه خوا حل کړئ:', 'm': ' = '.join(x['m'] for x in sl[1:] if x.get('m')) or sl[0]['m']})
    steps.append({'en': 'Work out the right side:', 'ur': 'دایاں طرف حل کریں:', 'ps': 'ښي خوا حل کړئ:', 'm': ' = '.join(x['m'] for x in sr[1:] if x.get('m')) or sr[0]['m']})
    if vl != vr:
        raise ParseError('not equal')
    steps.append({'en': 'Both sides are equal, so it is verified.', 'ur': 'دونوں طرف برابر ہیں، لہٰذا تصدیق ہو گئی۔', 'ps': 'دواړه خواوې برابرې دي، نو تصدیق شو.', 'm': 'LHS = RHS'})
    return steps, vl


def square_smaller(t):
    v = val(parse_tex(t))
    sq = v * v
    if not sq < v:
        raise ParseError('not smaller')
    steps = [step('given', msol.clean_tex(t)),
             {'en': 'Square it:', 'ur': 'مربع نکالیں:', 'ps': 'مربع یې وباسئ:', 'm': f'({msol.tex(parse_tex(t))})^2 = {tex_num(sq, msol.dec_places(parse_tex(t)) * 2 if msol.has_dec(parse_tex(t)) else None)}'},
             {'en': 'Compare with the number:', 'ur': 'عدد سے موازنہ کریں:', 'ps': 'له عدد سره پرتله کړئ:', 'm': f'{tex_num(sq, msol.dec_places(parse_tex(t)) * 2 if msol.has_dec(parse_tex(t)) else None)} < {msol.tex(parse_tex(t))}'}]
    return steps, sq


def perfect_square_test(n):
    n = int(str(n).replace(',', ''))
    ps = prime_pairs(n)
    f = sp.factorint(n)
    steps = [step('given', str(n)), step('primes', f'{n} = ' + ' \\times '.join(map(str, ps)))]
    ok = all(e % 2 == 0 for e in f.values())
    idx = ' \\times '.join(f'{p}^{{{e}}}' for p, e in sorted(f.items()))
    steps.append({'en': 'Group equal factors in pairs: every prime must appear an even number of times.', 'ur': 'برابر اجزا کے جوڑے بنائیں: ہر مفرد عدد جفت بار آنا چاہیے۔', 'ps': 'مساوي فکتورونه جوړې کړئ: هر لومړنی عدد باید جفت ځله راشي.', 'm': idx})
    steps.append({'en': ('All powers are even, so it IS a perfect square.' if ok else 'Some power is odd, so it is NOT a perfect square.'), 'ur': ('تمام طاقتیں جفت ہیں، لہٰذا یہ مکمل مربع ہے۔' if ok else 'کوئی طاقت طاق ہے، لہٰذا یہ مکمل مربع نہیں۔'), 'ps': ('ټول توانونه جفت دي، نو دا بشپړ مربع دی.' if ok else 'یو توان طاق دی، نو دا بشپړ مربع نه دی.')})
    return steps, ok


# ------------------------------------------------------------ compare / order
def parse_vals(text):
    """'50,856 ; 26,700' | '$\\frac{4}{7}, \\frac{1}{3}$' | '-5, +4, -13' -> list of (tex, Fraction)"""
    t = text.strip().strip('$')
    parts = re.split(r'\s*;\s*|\s*,\s*(?![^{]*\})(?=\s*[+\-\\d.])', t)
    out = []
    for p in parts:
        p = p.strip().rstrip('.')
        if not p:
            continue
        p = p.replace('+', '', 1) if p.startswith('+') else p
        # thousands separators "50,856" were split by comma: rejoin handled by regex below
        out.append((p, val(parse_tex(p))))
    return out


def join_thousands(text):
    return re.sub(r'(?<=\d),(?=\d{3}(?!\d))', '', text)


def compare_steps(text):
    items = parse_vals(join_thousands(text))
    if len(items) != 2:
        raise ParseError('cmp')
    (ta, a), (tb, b) = items
    sym = '>' if a > b else '<' if a < b else '='
    fa, fb = tex(parse_tex(ta)), tex(parse_tex(tb))
    steps = [step('given', f'{fa} \\;,\\; {fb}')]
    if (a.denominator != 1 or b.denominator != 1) and (a.denominator != b.denominator):
        L = msol.lcm(a.denominator, b.denominator)
        steps.append({'en': 'Write both with the same denominator (or as decimals) and compare:', 'ur': 'دونوں کو ایک جیسے نسب نما (یا اعشاریہ) میں لکھ کر موازنہ کریں:', 'ps': 'دواړه په یو شان مخرج (یا اعشاریه) کې ولیکئ او پرتله یې کړئ:', 'm': f'\\frac{{{a.numerator * L // a.denominator}}}{{{L}}} \\;\\text{{and}}\\; \\frac{{{b.numerator * L // b.denominator}}}{{{L}}}'})
    steps.append({'en': 'Compare:', 'ur': 'موازنہ:', 'ps': 'پرتله:', 'm': f'{fa} {sym} {fb}'})
    return steps, sym


def order_steps(text, descending=False):
    items = parse_vals(join_thousands(text))
    if len(items) < 2:
        raise ParseError('ord')
    asc = sorted(items, key=lambda x: x[1])
    seq = asc[::-1] if descending else asc
    show = lambda l: ' ,\\; '.join(msol.tex(parse_tex(t)) for t, _ in l)
    steps = [step('given', show(items)),
             {'en': 'Arrange from the smallest to the largest:' if not descending else 'Arrange from the largest to the smallest:', 'ur': 'چھوٹے سے بڑے کی ترتیب:' if not descending else 'بڑے سے چھوٹے کی ترتیب:', 'ps': 'له کوچني څخه لوی ته:' if not descending else 'له لوي څخه کوچني ته:', 'm': show(seq)}]
    return steps, [v for _, v in seq]


# ------------------------------------------------------------ identities
def _terms2(e):
    ts = sp.Add.make_args(sp.expand(e))
    return ts


def identity_square(expr_tex):
    """(p + q)^2 or (p - q)^2 for a binomial given as 'p + q' / 'p - q'"""
    b = tex_to_sympy(expr_tex)
    ts = sp.Add.make_args(b)
    if len(ts) != 2:
        raise ParseError('binomial')
    p, q = ts
    res = sp.expand(b ** 2)
    sign = '-' if q.could_extract_minus_sign() else '+'
    qq = -q if sign == '-' else q
    steps = [step('given', f'({msol.clean_tex(expr_tex)})^2'),
             step('identity', f'(a {sign} b)^2 = a^2 {sign} 2ab + b^2', t=f'(a {sign} b)^2'),
             {'en': 'Put a = %s and b = %s:' % (sp.latex(p), sp.latex(qq)), 'ur': 'a = %s اور b = %s رکھیں:' % (sp.latex(p), sp.latex(qq)), 'ps': 'a = %s او b = %s کېږدئ:' % (sp.latex(p), sp.latex(qq)),
              'm': f'({sp.latex(p)})^2 {sign} 2({sp.latex(p)})({sp.latex(qq)}) + ({sp.latex(qq)})^2 = {sp.latex(res, order="lex")}'}]
    return steps, res


def identity_product(expr_tex):
    e = tex_to_sympy(expr_tex)
    res = sp.expand(e)
    f = sp.factor_list(e)[1] if False else None
    steps = [step('given', msol.clean_tex(expr_tex)), step('identity', '(a + b)(a - b) = a^2 - b^2', t='(a + b)(a - b) = a^2 - b^2'),
             step('expand', sp.latex(res, order='lex'))]
    return steps, res


def sym_steps(expr_src, given_tex):
    ns = {'x': X, 'y': Y}
    syms = {n: sp.Symbol(n) for n in set(re.findall(r'[A-Za-z]', expr_src))}
    e = sp.sympify(expr_src, locals=syms)
    res = sp.expand(e)
    steps = [step('given', given_tex)]
    if sp.latex(res) != given_tex:
        steps.append(step('expand', sp.latex(res, order='lex')))
        steps.append(step('collect', sp.latex(res, order='lex')))
    return dedupe_m(steps), res


def dedupe_m(steps):
    out = []
    for s in steps:
        if out and out[-1].get('m') == s.get('m'):
            continue
        out.append(s)
    return out


def result_for_sym(res):
    return sp.latex(res, order='lex')


# ------------------------------------------------------------ reduced form, equivalents, properties
def reduced_steps(t):
    v = val(parse_tex(t))
    ast = parse_tex(t)
    if ast[0] not in ('frac',):
        raise ParseError('frac')
    a, b = int(val(ast[1])), int(val(ast[2]))
    import math
    g = math.gcd(abs(a), abs(b))
    r = Fraction(a, b)
    steps = [step('given', msol.clean_tex(t)),
             {'en': f'HCF of {abs(a)} and {abs(b)} is {g}; divide the numerator and denominator by it:', 'ur': f'{abs(a)} اور {abs(b)} کا ع.م.ا {g} ہے؛ شمار کنندہ اور نسب نما کو اس سے تقسیم کریں:', 'ps': f'د {abs(a)} او {abs(b)} ل.م.ق {g} دی؛ صورت او مخرج پر هغه ووېشئ:', 'm': f'\\frac{{{a} \\div {g}}}{{{b} \\div {g}}} = {tex_num(r)}'}]
    return steps, r


def equivalent_steps(t):
    ast = parse_tex(t)
    if ast[0] != 'frac':
        raise ParseError('frac')
    a, b = int(val(ast[1])), int(val(ast[2]))
    rows = ' ,\\; '.join(f'\\frac{{{a} \\times {k}}}{{{b} \\times {k}}} = \\frac{{{a * k}}}{{{b * k}}}' for k in (2, 3, 4))
    return [step('given', msol.clean_tex(t)), step('eqfrac', rows)], Fraction(a, b)


def commutative_steps(items):
    a, b = [val(parse_tex(x)) for x in items[:2]]
    ta, tb = [tex(parse_tex(x)) for x in items[:2]]
    steps = [step('given', f'a = {ta},\\; b = {tb}'),
             {'en': 'Addition: a + b and b + a', 'ur': 'جمع: a + b اور b + a', 'ps': 'جمع: a + b او b + a', 'm': f'{ta} + {tb} = {tex_num(a + b)},\\quad {tb} + {ta} = {tex_num(b + a)}'},
             {'en': 'Multiplication: a × b and b × a', 'ur': 'ضرب: a × b اور b × a', 'ps': 'ضرب: a × b او b × a', 'm': f'{ta} \\times {tb} = {tex_num(a * b)},\\quad {tb} \\times {ta} = {tex_num(b * a)}'},
             {'en': 'The results are equal, so the commutative property holds.', 'ur': 'نتائج برابر ہیں، لہٰذا تبدیلی خاصیت درست ہے۔', 'ps': 'پایلې برابرې دي، نو تبادلوي ځانګړتیا سمه ده.'}]
    return steps, a + b


def associative_steps(items):
    a, b, c = [val(parse_tex(x)) for x in items[:3]]
    ta, tb, tc = [tex(parse_tex(x)) for x in items[:3]]
    steps = [step('given', f'a = {ta},\\; b = {tb},\\; c = {tc}'),
             {'en': 'Addition: (a + b) + c and a + (b + c)', 'ur': 'جمع: (a + b) + c اور a + (b + c)', 'ps': 'جمع: (a + b) + c او a + (b + c)', 'm': f'({ta} + {tb}) + {tc} = {tex_num((a + b) + c)},\\quad {ta} + ({tb} + {tc}) = {tex_num(a + (b + c))}'},
             {'en': 'Multiplication: (a × b) × c and a × (b × c)', 'ur': 'ضرب: (a × b) × c اور a × (b × c)', 'ps': 'ضرب: (a × b) × c او a × (b × c)', 'm': f'({ta} \\times {tb}) \\times {tc} = {tex_num((a * b) * c)},\\quad {ta} \\times ({tb} \\times {tc}) = {tex_num(a * (b * c))}'},
             {'en': 'Both pairs are equal, so the associative property holds.', 'ur': 'دونوں جوڑے برابر ہیں، لہٰذا شراکتی خاصیت درست ہے۔', 'ps': 'دواړه جوړې برابرې دي، نو ملګرتیا ځانګړتیا سمه ده.'}]
    return steps, (a + b) + c


def split_items(text):
    t = text.strip().strip('$')
    depth, cur, out = 0, '', []
    for ch in t:
        if ch in '([{': depth += 1
        if ch in ')]}': depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


def poly_combine(items, mode):
    es = [tex_to_sympy(i) for i in items]
    ts = [msol.clean_tex(i) for i in items]
    if mode == 'sum':
        res = sp.expand(sum(es)); given = ' + '.join(f'({t})' for t in ts)
    else:
        res = sp.expand(es[1] - es[0]); given = f'({ts[1]}) - ({ts[0]})'
    steps = [step('given', given), step('expand', sp.latex(res, order='lex')), step('collect', sp.latex(res, order='lex'))]
    return dedupe_m(steps), res
