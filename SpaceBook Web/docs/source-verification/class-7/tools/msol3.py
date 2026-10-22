"""msol3.py - cube roots, simultaneous linear equations, polynomial division (EN / UR / PS steps)."""
import re
from fractions import Fraction
import sympy as sp
import msol, msol2
from msol import step, ParseError, tex_num, parse_tex, val, tex

B = chr(92)


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m is not None:
        d['m'] = m
    return d


# ---------------------------------------------------------------- cube roots
def exact_cbrt(v):
    v = Fraction(v)
    def c(n):
        r = round(abs(n) ** (1 / 3))
        for k in (r - 1, r, r + 1):
            if k >= 0 and k ** 3 == abs(n):
                return k if n >= 0 else -k
        return None
    a, b = c(v.numerator), c(v.denominator)
    if a is None or b is None:
        return None
    return Fraction(a, b)


def cbrt_by_factors(text):
    ast = parse_tex(msol.clean_tex(text))
    v = val(ast)
    r = exact_cbrt(v)
    if r is None:
        raise ParseError('notcube')
    steps = [step('given', f'{B}sqrt[3]{{{tex(ast)}}}'.replace(B + 'sqrt[3]', B + 'sqrt[3]'))]
    if v.denominator == 1 and v > 1:
        n = int(v)
        ps = msol2.prime_pairs(n)
        steps.append(step('primes', f'{n} = {(" " + B + "times ").join(map(str, ps))}'))
        taken = []
        for p in sorted(set(ps)):
            taken += [p] * (ps.count(p) // 3)
        steps.append(S('Make groups of three equal factors; take one from each group:', 'تین برابر اجزا کے گروپ بنائیں؛ ہر گروپ سے ایک لیں:', 'د درې مساوي فکتورونو ډلې جوړې کړئ؛ له هرې ډلې یو واخلئ:',
                       f'{B}sqrt[3]{{{n}}} = ' + (f' {B}times '.join(map(str, taken)) if taken else '1') + f' = {int(r)}'))
    else:
        f = Fraction(v)
        steps.append(S('Take the cube root of the numerator and of the denominator:', 'شمار کنندہ اور نسب نما کا مکعب جذر الگ الگ نکالیں:', 'د صورت او مخرج مکعب جذر بېل بېل وباسئ:',
                       f'{B}frac{{{B}sqrt[3]{{{f.numerator}}}}}{{{B}sqrt[3]{{{f.denominator}}}}} = {tex_num(r)}'))
    return steps, r


# ---------------------------------------------------------------- simultaneous equations
x, y = sp.symbols('x y')


def parse_eq(t):
    t = msol.clean_tex(t)
    l, r = t.split('=', 1)
    return sp.Eq(msol2.tex_to_sympy(l), msol2.tex_to_sympy(r))


def lin_form(eq, vs):
    e = sp.expand(eq.lhs - eq.rhs)
    a = e.coeff(vs[0]); b = e.coeff(vs[1]); c = -(e - a * vs[0] - b * vs[1])
    return a, b, c


def eq_tex(a, b, c, vs):
    lhs = sp.latex(sp.expand(a * vs[0] + b * vs[1]), order='lex')
    return f'{lhs} = {sp.latex(c)}'


def simultaneous(text, method='elimination'):
    eqs = [e.strip() for e in re.split(r';|\\\\|\s{2,}', text.replace('$', '')) if '=' in e]
    if len(eqs) != 2:
        raise ParseError('two eqs')
    e1, e2 = parse_eq(eqs[0]), parse_eq(eqs[1])
    syms = sorted((e1.free_symbols | e2.free_symbols), key=lambda s: s.name)
    if len(syms) != 2:
        raise ParseError('vars')
    vs = syms
    a1, b1, c1 = lin_form(e1, vs); a2, b2, c2 = lin_form(e2, vs)
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ParseError('no unique solution')
    xs = sp.nsimplify((c1 * b2 - c2 * b1) / det); ys = sp.nsimplify((a1 * c2 - a2 * c1) / det)
    X, Yv = vs
    steps = [step('given', f'(1)\\; {eq_tex(a1, b1, c1, vs)}' + f'{B}qquad (2)\\; {eq_tex(a2, b2, c2, vs)}')]
    # eliminate the second variable
    m1 = sp.ilcm(abs(b1), abs(b2)) / abs(b1) if b1 != 0 else 1
    m2 = sp.ilcm(abs(b1), abs(b2)) / abs(b2) if b2 != 0 else 1
    if b1 == 0 or b2 == 0:
        m1 = m2 = 1
    s1, s2 = (a1 * m1, b1 * m1, c1 * m1), (a2 * m2, b2 * m2, c2 * m2)
    if (m1, m2) != (1, 1):
        steps.append(S(f'Multiply (1) by {m1} and (2) by {m2} so the coefficients of {sp.latex(Yv)} become equal in size:',
                       f'(1) کو {m1} اور (2) کو {m2} سے ضرب دیں تاکہ {sp.latex(Yv)} کے سر برابر ہو جائیں:',
                       f'(1) په {m1} او (2) په {m2} کې ضرب کړئ چې د {sp.latex(Yv)} ضریبونه برابر شي:',
                       f'(3)\\; {eq_tex(*s1, vs)}{B}qquad (4)\\; {eq_tex(*s2, vs)}'))
    same_sign = (s1[1] > 0) == (s2[1] > 0)
    op = 'subtract' if same_sign else 'add'
    if same_sign:
        ra, rc = s1[0] - s2[0], s1[2] - s2[2]
    else:
        ra, rc = s1[0] + s2[0], s1[2] + s2[2]
    steps.append(S(('Subtract' if same_sign else 'Add') + f' the equations to eliminate {sp.latex(Yv)}:', ('دونوں مساواتوں کو ' + ('تفریق' if same_sign else 'جمع') + f' کریں تاکہ {sp.latex(Yv)} ختم ہو جائے:'), ('معادلې ' + ('تفریق' if same_sign else 'جمع') + f' کړئ چې {sp.latex(Yv)} لرې شي:'),
                   f'{sp.latex(sp.expand(ra * X))} = {sp.latex(rc)}'))
    steps.append(S(f'Solve for {sp.latex(X)}:', f'{sp.latex(X)} معلوم کریں:', f'{sp.latex(X)} ومومئ:', f'{sp.latex(X)} = {sp.latex(xs)}'))
    steps.append(S(f'Put {sp.latex(X)} = {sp.latex(xs)} in equation (1):', f'(1) میں {sp.latex(X)} = {sp.latex(xs)} رکھیں:', f'په (1) کې {sp.latex(X)} = {sp.latex(xs)} کېږدئ:',
                   f'{sp.latex(sp.expand(a1 * xs + b1 * Yv), order="lex")} = {sp.latex(c1)}'))
    steps.append(S(f'Solve for {sp.latex(Yv)}:', f'{sp.latex(Yv)} معلوم کریں:', f'{sp.latex(Yv)} ومومئ:', f'{sp.latex(Yv)} = {sp.latex(ys)}'))
    steps.append(step('verify', f'{sp.latex(a1 * xs + b1 * ys)} = {sp.latex(c1)},{B}quad {sp.latex(a2 * xs + b2 * ys)} = {sp.latex(c2)}'))
    return steps, {X.name: xs, Yv.name: ys}


def key_solution_matches(key, sol):
    pairs = re.findall(r'([A-Za-z])\s*=\s*\$?(-?[\d./\\{}a-z]+(?:\s*\\frac\{[^}]*\}\{[^}]*\})?)', key.replace('−', '-'))
    got = {}
    for k, v in pairs:
        try:
            got[k] = msol2.tex_to_sympy(v)
        except Exception:
            pass
    if not got:
        return None
    return all(k in sol and sp.simplify(sol[k] - v) == 0 for k, v in got.items())


# ---------------------------------------------------------------- polynomial division
def poly_divide(text):
    parts = msol2.split_items(text)
    if len(parts) != 2:
        raise ParseError('two polys')
    n, d = [msol2.tex_to_sympy(p) for p in parts]
    syms = sorted((n.free_symbols | d.free_symbols), key=lambda s: s.name)
    q, r = sp.div(sp.expand(n), sp.expand(d), *syms[:1]) if len(syms) == 1 else sp.div(sp.expand(n), sp.expand(d))
    steps = [step('given', f'({sp.latex(n, order="lex")}) {B}div ({sp.latex(d, order="lex")})')]
    if sp.expand(q * d + r) != sp.expand(n):
        raise ParseError('div check')
    # exact division by a monomial: show term-wise
    if len(sp.Add.make_args(sp.expand(d))) == 1:
        terms = sp.Add.make_args(sp.expand(n))
        rows = ' + '.join(f'{B}frac{{{sp.latex(t)}}}{{{sp.latex(d)}}}' for t in terms)
        steps.append(S('Divide every term by the divisor:', 'ہر جز کو مقسوم علیہ پر تقسیم کریں:', 'هر جز په وېشونکي ووېشئ:', rows.replace('+ -', '- ')))
    else:
        steps.append(S('Divide step by step (long division): the quotient and remainder are', 'مرحلہ وار تقسیم (طویل تقسیم): خارجِ قسمت اور باقی', 'ګام په ګام وېش: خارج قسمت او پاتې', f'q = {sp.latex(q, order="lex")},{B}quad r = {sp.latex(r)}'))
    steps.append(step('check', f'({sp.latex(d, order="lex")})({sp.latex(q, order="lex")}) + {sp.latex(r)} = {sp.latex(sp.expand(q * d + r), order="lex")}'))
    return steps, (q if r == 0 else q + r / d)
