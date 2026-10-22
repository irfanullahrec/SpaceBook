"""gen_alg7.py - Class 7 / 8 algebra items computed with sympy and written as key-checked DSL lines:
simplify / sum / subtract / product / factorise polynomials and solve linear equations (with the check by substitution).
    python gen_alg7.py            -> class-7/math/dsl/alg.txt  (+ prints every item where my result differs from the printed key)
Printed-key errors are re-marked !! afterwards by `python gen_alg7.py mark` (see the printed list: each was eyeballed).
"""
import re, json, sys
from pathlib import Path
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

sys.path.insert(0, str(Path(__file__).resolve().parent))
import msol2, msol_run

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent
B = chr(92)
TR = standard_transformations + (implicit_multiplication_application, convert_xor)


def balance(s):
    out, depth = [], 0
    for c in s:
        if c == '(':
            depth += 1
        elif c == ')':
            if depth == 0:
                continue
            depth -= 1
        out.append(c)
    return ''.join(out) + ')' * depth


def to_sym(t):
    t = t.strip().strip('$').replace(B + '{', '(').replace(B + '}', ')').replace('[', '(').replace(']', ')')
    t = t.replace(B + ',', '').replace(B + ' ', '')
    t = t.replace(B + 'left', '').replace(B + 'right', '')
    t = t.replace(B + 'times', '*').replace(B + 'cdot', '*')
    t = t.replace('−', '-')
    # \frac{a}{b} -> ((a)/(b)) repeatedly
    for _ in range(6):
        t = re.sub(re.escape(B) + r'frac\{([^{}]*)\}\{([^{}]*)\}', r'((\1)/(\2))', t)
    # x \div y
    if B + 'div' in t:
        a, b = t.split(B + 'div', 1)
        t = '(' + a + ')/(' + b + ')'
    t = balance(t)
    syms = {n: sp.Symbol(n) for n in set(re.findall(r'[A-Za-z]', t))}
    return parse_expr(t, local_dict=syms, transformations=TR)


def tl(e, order='lex'):
    return sp.latex(e, order=order).replace(B + 'left(', '(').replace(B + 'right)', ')')


def math_segments(t):
    return [s.strip() for s in re.findall(r'\$([^$]+)\$', t)]


def same(a, b):
    try:
        return sp.simplify(sp.expand(a - b)) == 0
    except Exception:
        return False


def key_expr(k):
    if not k:
        return None
    k = k.replace('$', '')
    try:
        return to_sym(k)
    except Exception:
        return None


def main(mark=False):
    leaves = json.load(open(APP / 'tmp' / 'm7_leaves.json', encoding='utf8'))
    want = {
        ('7.4', '2'): {'d'}, ('7.6', '1'): {'d', 'f', 'g', 'h', 'i', 'j', 'l'}, ('R7', '4'): {'a', 'b', 'c', 'd'}, ('R7', '5'): {'a', 'b', 'c', 'd'},
        ('R7', '6'): {'a', 'b', 'c', 'd'}, ('R7', '7'): {'d'}, ('7.8', '1'): {'b', 'h'}, ('7.8', '2'): {'e', 'l', 'q'}, ('7.8', '3'): {'d', 'e', 'h'},
        ('7.9', '1'): {'c'}, ('R7', '8'): {'e', 'f'},
    }
    eqs = {('8.1', '1'): {'i', 'k'}, ('8.1', '2'): {'a', 'c', 'd', 'e', 'f'}, ('R8', '4'): {'a', 'c'}}
    out, report = [], []
    for q in leaves:
        ex = msol_run.exk(q)
        w = want.get((ex, q['q']))
        e2 = eqs.get((ex, q['q']))
        if not (w or e2):
            continue
        km = msol2.split_key(q['key'])
        for no, pt in q['parts']:
            if (w and no not in w) or (e2 and no not in e2):
                continue
            key = f"{ex}|{q['q']}|{no}"
            try:
                ins = q['en'].lower()
                segs = math_segments(pt) or [pt]
                kx = key_expr(km.get(no.lower()))
                if e2:
                    eqt = segs[0].strip('$')
                    lhs_t, rhs_t = eqt.split('=', 1)
                    x = sp.Symbol('x') if 'x' in eqt else sp.Symbol('y')
                    L, Rr = to_sym(lhs_t), to_sym(rhs_t)
                    sol = sp.solve(sp.Eq(L, Rr), x)
                    if not sol:
                        raise ValueError('nosol')
                    v = sp.nsimplify(sol[0])
                    cross = sp.expand(sp.together(L - Rr).as_numer_denom()[0])
                    vt = tl(v)
                    rows = [f'{tl(L)} = {tl(Rr)}', f'{tl(sp.together(L - Rr).as_numer_denom()[0])} = 0', f'{sp.latex(x)} = {vt}',
                            f'{B}text{{Check: LHS}} = {tl(sp.nsimplify(L.subs(x, v)))},\\; {B}text{{RHS}} = {tl(sp.nsimplify(Rr.subs(x, v)))}'.replace('\\;', B + ';')]
                    res = v
                else:
                    if pt.lstrip('$ ').lower().startswith('subtract') and len(segs) == 1:
                        m = re.search(r'subtract\s+\$?(.+?)\$?\s+from\s+\$?(.+?)\$?$', pt, re.I)
                        a_t, b_t = m.group(1), m.group(2)
                        a, bb = to_sym(a_t.strip('$')), to_sym(b_t.strip('$'))
                        res = sp.expand(bb - a)
                        rows = [f'({tl(bb, "none")}) - ({tl(a, "none")})', f'{tl(res)}']
                        rows = [f'({b_t.strip("$ ")}) - ({a_t.strip("$ ")}) = {tl(res)}']
                    elif pt.lstrip('$ ').lower().startswith('subtract') and len(segs) == 2 and 'from' in pt:
                        a_t, b_t = segs[0], segs[1]
                        a, bb = to_sym(a_t), to_sym(b_t)
                        res = sp.expand(bb - a)
                        rows = [f'({b_t}) - ({a_t}) = {tl(res)}']
                    elif 'sum' in ins:
                        parts = [x for x in re.split(r',| and ', pt.strip('$')) if x.strip()]
                        # re-join pieces split inside brackets
                        buf, items = '', []
                        for p_ in parts:
                            buf = (buf + ',' + p_) if buf else p_
                            if buf.count('(') == buf.count(')'):
                                items.append(buf.strip().strip('$'))
                                buf = ''
                        es = [to_sym(i) for i in items]
                        res = sp.expand(sum(es))
                        rows = [' + '.join(f'({i})' for i in items) + f' = {tl(res)}']
                    elif 'product' in ins:
                        items = [i.strip().strip('$') for i in re.split(r',| and ', pt.replace('$', '')) if i.strip()]
                        es = [to_sym(i) for i in items]
                        res = sp.expand(sp.Mul(*es))
                        rows = [' \\times '.join(f'({i})' for i in items).replace('\\times', B + 'times') + f' = {tl(res)}']
                    elif 'factori' in ins or 'solve the following polynomials' in ins:
                        src = segs[0].strip('$')
                        if src.endswith('= 0'):
                            src = src[:-3]
                        e0 = to_sym(src)
                        if 'factori' in ins:
                            res = sp.factor(e0)
                            rows = [f'{src.strip()} = {tl(res, "none")}']
                        else:
                            res = sp.expand(e0)
                            rows = [f'{src.strip()} = {tl(res)}']
                    else:
                        src = segs[0].strip('$')
                        e0 = to_sym(src)
                        res = sp.expand(e0)
                        rows = [f'{src.strip()} = {tl(res)}']
                ans = tl(res) if not ('factori' in ins) else tl(res, 'none')
                if kx is not None and not same(res, kx) and not isinstance(res, (list, tuple)):
                    report.append((key, ans[:60], (km.get(no.lower()) or '')[:60]))
                out.append(f"{key} ~ {' ;; '.join(rows)} => {ans}")
            except Exception as e:
                report.append((key, 'ERR ' + str(e)[:70], (km.get(no.lower()) or '')[:50]))
    p = HERE / 'class-7' / 'math' / 'dsl' / 'alg.txt'
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(len(out), 'lines;', len(report), 'items to eyeball')
    for r in report:
        print('  ', r)


MARK = ['7.4|2|d', '7.6|1|d', '7.6|1|f', '7.6|1|g', '7.6|1|h', '7.6|1|i', '7.6|1|j', '7.8|1|h', 'R7|5|c', 'R7|6|b', 'R7|6|c', 'R7|6|d', 'R7|7|d', 'R7|8|f',
        '8.1|2|a', '8.1|2|e', '8.1|2|f']      # printed key differs and my result was checked by hand


NOCHECK = ['7.8|1|b', '7.8|2|e', '7.8|3|e', '8.1|1|k', 'R8|4|a']      # printed key is cut off or rounded; my result equals it


def mark_keys():
    p = HERE / 'class-7' / 'math' / 'dsl' / 'alg.txt'
    L = p.read_text(encoding='utf-8').splitlines()
    for i, ln in enumerate(L):
        if '~' in ln and ln.split('~')[0].strip() in MARK and not ln.rstrip().endswith('!!'):
            L[i] = ln.rstrip() + ' !!'
        elif '~' in ln and ln.split('~')[0].strip() in NOCHECK and not ln.rstrip().endswith('%%'):
            L[i] = ln.rstrip() + ' %%'
    p.write_text(chr(10).join(L) + chr(10), encoding='utf-8')


if __name__ == '__main__':
    main()
    mark_keys()
