"""msol5.py - linear inequalities and graphical solution of two linear equations (EN / UR / PS)."""
import re
import sympy as sp
import msol, msol2
from msol import step, ParseError

BS = chr(92)
x, y = sp.symbols('x y')


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m is not None:
        d['m'] = m
    return d


def inequality(text):
    t = msol.clean_tex(text).replace(BS + 'le', '<=').replace(BS + 'ge', '>=').replace(BS + 'leq', '<=').replace(BS + 'geq', '>=')
    m = re.search(r'(<=|>=|<|>)', t)
    if not m:
        raise ParseError('ineq')
    op = m.group(1)
    l, r = t.split(op, 1)
    L, R = msol2.tex_to_sympy(l), msol2.tex_to_sympy(r)
    v = list((L - R).free_symbols)
    if len(v) != 1:
        raise ParseError('var')
    v = v[0]
    e = sp.expand(L - R)
    a = e.coeff(v); c = e - a * v
    if a == 0:
        raise ParseError('a0')
    bound = sp.nsimplify(-c / a)
    flip = a < 0
    newop = {'<': '>', '>': '<', '<=': '>=', '>=': '<='}[op] if flip else op
    sym = {'<': '<', '>': '>', '<=': BS + 'le ', '>=': BS + 'ge '}
    steps = [step('given', msol.clean_tex(text)),
             S(f'Move the constant to the right side: {sp.latex(a * v)} {op} {sp.latex(sp.nsimplify(R - (L - a * v)))}', f'مستقل کو دائیں طرف لے جائیں۔', 'ثابت ښي لوري ته یوسئ.', f'{sp.latex(a * v)} {sym[op]} {sp.latex(sp.nsimplify(R - (L - a * v)))}')]
    if a != 1:
        steps.append(S('Divide both sides by ' + sp.latex(a) + (' (a negative number, so the inequality sign is reversed):' if flip else ':'), 'دونوں طرف کو ' + sp.latex(a) + (' سے تقسیم کریں (منفی عدد ہے، اس لیے علامت الٹ جاتی ہے):' if flip else ' سے تقسیم کریں:'), 'دواړه خواوې په ' + sp.latex(a) + (' ووېشئ (منفي عدد دی، نو نښه بدلېږي):' if flip else ' ووېشئ:'), f'{sp.latex(v)} {sym[newop]} {sp.latex(bound)}'))
    open_circle = newop in ('<', '>')
    side = 'right' if newop in ('>', '>=') else 'left'
    steps.append(S(f'Number line: put an {"open" if open_circle else "filled"} circle at {sp.latex(bound)} and shade to the {side}.', f'عددی خط: {sp.latex(bound)} پر {"کھلا" if open_circle else "بھرا ہوا"} دائرہ لگائیں اور {"دائیں" if side == "right" else "بائیں"} طرف سایہ کریں۔', f'عددي کرښه: په {sp.latex(bound)} {"خلاص" if open_circle else "ډک"} دایره کېږدئ او {"ښي" if side == "right" else "کیڼ"} لوري ته سیوری وکړئ.'))
    res = (v, newop, bound)
    return steps, res


def key_ineq_match(key, res):
    v, op, b = res
    m = re.search(r'([a-z])\s*(<=|>=|<|>|' + re.escape(BS + 'le') + '|' + re.escape(BS + 'ge') + r')\s*(.+)', key.replace('≤', '<=').replace('≥', '>='))
    if not m:
        return None
    kop = {BS + 'le': '<=', BS + 'ge': '>='}.get(m.group(2), m.group(2))
    try:
        kb = msol2.tex_to_sympy(m.group(3).strip().strip('$').rstrip(';'))
    except Exception:
        return None
    return kop == op and sp.simplify(kb - b) == 0


def graph_system(text):
    import gen_graphs
    eqs = [e.strip() for e in re.split(r';', text.replace('$', '')) if '=' in e]
    if len(eqs) != 2:
        raise ParseError('two')
    rows = []
    sols = []
    steps = []
    for i, e in enumerate(eqs, 1):
        r = gen_graphs.two_var(msol.clean_tex(e))
        if not r:
            raise ParseError('lin')
        a, b, c = r
        pts = ', '.join(f'({xv}, {gen_graphs.L(sp.nsimplify((c - a * xv) / b))})' for xv in (0, 1, 2, 3, 4)) if b != 0 else ''
        steps.append(S(f'Line {i}: {msol.clean_tex(e)}. Table of points: {pts}.', f'لکیر {i}: {msol.clean_tex(e)}۔ نقاط کا جدول: {pts}۔', f'کرښه {i}: {msol.clean_tex(e)}. د ټکو جدول: {pts}.'))
    a1, b1, c1 = gen_graphs.two_var(msol.clean_tex(eqs[0])); a2, b2, c2 = gen_graphs.two_var(msol.clean_tex(eqs[1]))
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ParseError('parallel')
    xs = sp.nsimplify((c1 * b2 - c2 * b1) / det); ys = sp.nsimplify((a1 * c2 - a2 * c1) / det)
    steps.append(S('Plot both lines on the same axes; they cross at the solution point.', 'دونوں لکیریں ایک ہی محور پر کھینچیں؛ وہ حل کے نقطے پر ایک دوسرے کو کاٹتی ہیں۔', 'دواړه کرښې په یو شان محور وکاږئ؛ دا د حل په ټکي کې سره پرې کېږي.'))
    steps.append(S(f'The lines meet at ({sp.latex(xs)}, {sp.latex(ys)}), so x = {sp.latex(xs)}, y = {sp.latex(ys)}.', f'لکیریں ({sp.latex(xs)}, {sp.latex(ys)}) پر ملتی ہیں، لہٰذا x = {sp.latex(xs)}، y = {sp.latex(ys)}۔', f'کرښې په ({sp.latex(xs)}, {sp.latex(ys)}) کې سره ورسېږي، نو x = {sp.latex(xs)}، y = {sp.latex(ys)}.'))
    return steps, f'x = {sp.latex(xs)}, y = {sp.latex(ys)}'
