"""gen_graphs.py - write DSL lines (math/dsl/graphs.txt) for 'plot / draw the graph of' linear-equation parts:
a table of values plus the key features (intercepts, slope, vertical or horizontal line). Computed with sympy.

    python gen_graphs.py 7|8
Items depend on the learner drawing a figure, so every line is marked not verified (^^).
"""
import sys, re, json
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
import msol, msol2
import msol_run

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent
x, y = sp.symbols('x y')


def L(v):
    v = sp.nsimplify(v)
    return str(v) if v.q == 1 else f'{v.p}/{v.q}'


def one_var(eq):
    l, r = msol.clean_tex(eq).split('=', 1)
    e = sp.expand(msol2.tex_to_sympy(l) - msol2.tex_to_sympy(r))
    if e.has(y) and not e.has(x):
        return ('y', sp.solve(e, y)[0])
    if e.has(x) and not e.has(y):
        return ('x', sp.solve(e, x)[0])
    return None


def two_var(eq):
    l, r = msol.clean_tex(eq).split('=', 1)
    e = sp.expand(msol2.tex_to_sympy(l) - msol2.tex_to_sympy(r))
    if e.has(x) and e.has(y):
        a, b = e.coeff(x), e.coeff(y)
        c = -(e - a * x - b * y)
        return a, b, c
    return None


def lines_for(eq):
    eq = eq.strip().strip('$')
    t = msol.clean_tex(eq)
    ov = one_var(t)
    if ov:
        v, k = ov
        if v == 'x':
            return (f'The equation is the same as x = {L(k)}: every point has x-coordinate {L(k)}, so the graph is a vertical straight line through ({L(k)}, 0), parallel to the y-axis.|مساوات x = {L(k)} کے برابر ہے: ہر نقطے کا x-محدد {L(k)} ہے، لہٰذا گراف ({L(k)}, 0) سے گزرنے والی عمودی سیدھی لکیر ہے جو y-محور کے متوازی ہے۔|معادله د x = {L(k)} سره برابره ده: هر ټکي x-همغږي {L(k)} ده، نو ګراف له ({L(k)}, 0) تېرېدونکې عمودي سیده کرښه ده چې د y-محور سره موازي ده.',
                    f'Table of points: (' + f'{L(k)}, -2), ({L(k)}, 0), ({L(k)}, 3). Plot them and join with a ruler.|نقاط کا جدول: ({L(k)}, −2)، ({L(k)}, 0)، ({L(k)}, 3)۔ انھیں لگا کر رولر سے ملائیں۔|د ټکو جدول: ({L(k)}, −2)، ({L(k)}, 0)، ({L(k)}, 3). دا ټکي کېږدئ او په کوټکي یې ونښلوئ.'), f'Vertical line x = {L(k)}'
        return (f'The equation is the same as y = {L(k)}: every point has y-coordinate {L(k)}, so the graph is a horizontal straight line through (0, {L(k)}), parallel to the x-axis.|مساوات y = {L(k)} کے برابر ہے: ہر نقطے کا y-محدد {L(k)} ہے، لہٰذا گراف (0, {L(k)}) سے گزرنے والی افقی سیدھی لکیر ہے جو x-محور کے متوازی ہے۔|معادله د y = {L(k)} سره برابره ده: هر ټکي y-همغږي {L(k)} ده، نو ګراف له (0, {L(k)}) تېرېدونکې افقي سیده کرښه ده چې د x-محور سره موازي ده.',
                f'Table of points: (-2, {L(k)}), (0, {L(k)}), (3, {L(k)}). Plot them and join with a ruler.|نقاط کا جدول: (−2, {L(k)})، (0, {L(k)})، (3, {L(k)})۔ انھیں لگا کر رولر سے ملائیں۔|د ټکو جدول: (−2, {L(k)})، (0, {L(k)})، (3, {L(k)}). دا ټکي کېږدئ او په کوټکي یې ونښلوئ.'), f'Horizontal line y = {L(k)}'
    tv = two_var(t)
    if not tv:
        return None
    a, b, c = tv
    if b == 0 or a == 0:
        return None
    pts = []
    for xv in (-2, -1, 0, 1, 2, 3):
        pts.append((xv, sp.nsimplify((c - a * xv) / b)))
    tab = ', '.join(f'({xv}, {L(yv)})' for xv, yv in pts)
    xi = sp.nsimplify(c / a) if c != 0 else 0
    yi = sp.nsimplify(c / b) if c != 0 else 0
    slope = sp.nsimplify(-a / b)
    return (f'Solve for y: y = {sp.latex(sp.nsimplify((c - a * x) / b)).replace(chr(92) + "frac", "frac")}.|y کے لیے حل کریں: y = {sp.latex(sp.nsimplify((c - a * x) / b)).replace(chr(92) + "frac", "frac")}۔|د y لپاره حل کړئ: y = {sp.latex(sp.nsimplify((c - a * x) / b)).replace(chr(92) + "frac", "frac")}.',
            f'Table of values (x, y): {tab}.|قیمتوں کا جدول (x, y): {tab}۔|د ارزښتونو جدول (x, y): {tab}.',
            f'Intercepts: x-intercept ({L(xi)}, 0), y-intercept (0, {L(yi)}); slope = {L(slope)}.|قطع: x-قطع ({L(xi)}, 0)، y-قطع (0, {L(yi)})؛ ڈھلوان = {L(slope)}۔|پرې کېدنې: x-پرې کېدنه ({L(xi)}, 0)، y-پرې کېدنه (0, {L(yi)})؛ ټوپ = {L(slope)}.',
            'Plot the points on graph paper and join them with a ruler: the graph is a straight line.|نقاط گراف پیپر پر لگا کر رولر سے ملائیں: گراف سیدھی لکیر ہے۔|ټکي په ګراف کاغذ کېږدئ او په کوټکي یې ونښلوئ: ګراف سیده کرښه ده.'), f'Straight line through {tab.split("), ")[0]}), ...'


def main(cl):
    leaves = json.load(open(APP / 'tmp' / f'm{cl}_leaves.json', encoding='utf8'))
    out = []
    for q in leaves:
        ins = (q['en'] or '').lower()
        if not re.search(r'plot the graphs?|draw the graphs?|graph for|plot graphs|graphs? of the following', ins):
            continue
        if 'inequalit' in ins or 'simultaneous' in ins or 'system' in ins:
            continue
        for no, pt in (q['parts'] or []):
            if not pt or '$' not in pt:
                continue
            try:
                r = lines_for(pt)
            except Exception:
                r = None
            if not r:
                continue
            rows, ans = r
            out.append(f"{msol_run.exk(q)}|{q['q']}|{no} ~ @text " + ' ;; '.join(rows) + f' => {ans} ^^')
    (HERE / f'class-{cl}' / 'math' / 'dsl' / 'graphs.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(cl, len(out), 'graph items')


if __name__ == '__main__':
    main(sys.argv[1])
