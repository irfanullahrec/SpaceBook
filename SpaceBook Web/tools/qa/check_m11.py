"""Numeric spot-check of Class 11 Maths step chains (js/math_11_solutions.js).

Every step may carry a TeX chain "A=B=C" in its "m" field. Each side is translated to a sympy expression and evaluated at
several random points; sides of one chain must agree. Chains that use notation the translator does not read are counted as skipped.
Also compares the last side of the last chain of a solution with the printed answer when both are plain expressions.

    python tools/qa/check_m11.py [--json out.json] [--show N]
"""
import json, re, sys, random
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

SRC = 'js/math_11_solutions.js'
raw = open(SRC, encoding='utf8').read()
data = json.loads(raw[raw.index('{'):raw.rindex('}') + 1])

FUNCS = {'sin': 'sin', 'cos': 'cos', 'tan': 'tan', 'cot': 'cot', 'sec': 'sec', 'csc': 'csc', 'ln': 'log', 'exp': 'exp',
         'arcsin': 'asin', 'arccos': 'acos', 'arctan': 'atan'}
SKIP = re.compile(r'\\(text|mathrm|mathbb|in|notin|subset|cup|cap|lim|sum|prod|int|le|ge|leq|geq|neq|ne|pm|mp|to|infty|Rightarrow|Leftrightarrow|therefore|because|angle|circ|mid|forall|exists|binom|overline|vec|hat|bar|begin|log|det|operatorname|mod|bmod|approx|cdots|ldots|dots)|[<>≤≥≠∈]|\\\\|&|\|')


def group(s, i):
    """index just after the {...} group starting at s[i]"""
    d = 0
    for j in range(i, len(s)):
        if s[j] == '{': d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0: return j + 1
    raise ValueError('unbalanced')


def tr(s):
    s = re.sub(r'([A-Za-z])_\{([^{}]*)\}', lambda m: m.group(1) + '__' + re.sub(r'\W', '', m.group(2)), s)
    s = re.sub(r'([A-Za-z])_([A-Za-z0-9])', r'\1__\2', s)
    s = re.sub(r'\\(left|right|displaystyle|,|;|!|quad|qquad|:)', ' ', s)
    s = s.replace('\\dfrac', '\\frac').replace('\\tfrac', '\\frac')
    # \frac{a}{b}
    while '\\frac' in s:
        i = s.index('\\frac'); a0 = i + 5
        while s[a0] == ' ': a0 += 1
        a1 = group(s, a0); b0 = a1
        while s[b0] == ' ': b0 += 1
        b1 = group(s, b0)
        s = s[:i] + '((' + s[a0 + 1:a1 - 1] + ')/(' + s[b0 + 1:b1 - 1] + '))' + s[b1:]
    while '\\sqrt' in s:
        i = s.index('\\sqrt'); j = i + 5
        if s[j] == '[':
            k = s.index(']', j); n = s[j + 1:k]; j = k + 1
            g1 = group(s, j); s = s[:i] + '((' + s[j + 1:g1 - 1] + ')**(1/(' + n + ')))' + s[g1:]
        else:
            g1 = group(s, j); s = s[:i] + 'sqrt(' + s[j + 1:g1 - 1] + ')' + s[g1:]
    # \sin\theta, \cos A: the argument is the single token that follows
    s = re.sub(r'\\(sin|cos|tan|cot|sec|csc)\s*(\d*\\[A-Za-z]+|\d*[A-Za-z](?![A-Za-z])|\d+)(?![A-Za-z0-9^_])', lambda m: '\\' + m.group(1) + '{(' + m.group(2) + ')}', s)
    for k, v in FUNCS.items():
        s = re.sub(r'\\' + k + r'(?![A-Za-z])', ' ' + v + ' ', s)
    s = s.replace('\\cdot', '*').replace('\\times', '*').replace('\\div', '/').replace('\\pi', 'pi')
    s = re.sub(r'\\(alpha|beta|gamma|theta|phi|lambda|mu|omega|sigma|delta)', lambda m: m.group(1) + '_', s)
    s = s.replace('{', '(').replace('}', ')').replace('^', '**').replace('−', '-').replace('!', '!')
    if '\\' in s: raise ValueError('unknown command')
    s = re.sub(r'(\d+)!', r'factorial(\1)', s)
    s = re.sub(r'(?<![A-Za-z_])e\*\*', 'E**', s)
    return s


TR = standard_transformations + (implicit_multiplication_application, convert_xor)


def to_expr(side):
    t = tr(side.strip())
    if not t.strip(): raise ValueError('empty')
    names = {'I': sp.I, 'E': sp.E, 'pi': sp.pi, 'i': sp.I}
    return parse_expr(t, local_dict=names, transformations=TR, evaluate=True)


def split_eq(m):
    parts, d, cur = [], 0, ''
    for c in m:
        if c in '({[': d += 1
        elif c in ')}]': d -= 1
        if c == '=' and d == 0: parts.append(cur); cur = ''
        else: cur += c
    parts.append(cur)
    return [p for p in parts if p.strip()]


def num(e, env):
    try:
        v = complex(sp.N(e.subs(env), 20))
    except Exception:
        return None
    return v


def agree(a, b):
    return abs(a - b) <= 1e-6 * max(1, abs(a), abs(b))


random.seed(11)
stats = dict(solutions=len(data), steps=0, chains=0, skipped=0, checked=0, ok=0, mismatch=0, answers_checked=0, answers_mismatch=0)
bad, bad_ans = [], []
for sid, sol in data.items():
    last = None
    for st in sol.get('steps', []):
        stats['steps'] += 1
        m = st.get('m')
        if not m or m.count('=') < 1: continue
        stats['chains'] += 1
        if SKIP.search(m): stats['skipped'] += 1; continue
        try:
            sides = [to_expr(p) for p in split_eq(m)]
        except Exception:
            stats['skipped'] += 1; continue
        if len(sides) < 2 or not all(isinstance(x, sp.Expr) for x in sides): stats['skipped'] += 1; continue
        # a lone symbol on a side is a definition / substitution ("a_n = ...", "D = ..."): compare only the remaining sides
        sides = [x for x in sides if not (x.is_Symbol or (x.is_Function and not x.free_symbols))] if sum(1 for x in sides if x.is_Symbol) else sides
        if len(sides) < 2: stats['skipped'] += 1; continue
        # equations being solved ("... = 0" with unknowns) are not identities
        if any(x.free_symbols for x in sides) and any(x == 0 for x in sides): stats['skipped'] += 1; continue
        # symbolic sides next to purely numeric ones are definitions / substitutions: compare the numeric sides only
        numeric = [x for x in sides if not x.free_symbols]
        if len(numeric) >= 2 and len(numeric) < len(sides): sides = numeric
        syms = sorted(set().union(*[s.free_symbols for s in sides]), key=str)
        good = 0; fail = False
        for _ in range(4):
            env = {s: sp.Rational(random.randint(13, 29), 10) * random.choice([1, 1, -1]) if not (s.name.endswith('_')) else sp.Rational(random.randint(7, 15), 10) for s in syms}
            vals = [num(s, env) for s in sides]
            if any(v is None or v != v for v in vals): continue
            good += 1
            if not all(agree(vals[0], v) for v in vals[1:]): fail = True; break
        if good == 0: stats['skipped'] += 1; continue
        stats['checked'] += 1
        if fail: stats['mismatch'] += 1; bad.append((sid, m))
        else: stats['ok'] += 1
        last = (m, sides)
    # printed answer vs last side of last chain
    ans = sol.get('answer')
    if last and isinstance(ans, str) and not SKIP.search(ans.replace('$', '')):
        try:
            a = to_expr(ans.replace('$', ''))
            if not (a.free_symbols or last[1][-1].free_symbols):
                stats['answers_checked'] += 1
                va, vb = num(a, {}), num(last[1][-1], {})
                if va is not None and vb is not None and not agree(va, vb): stats['answers_mismatch'] += 1; bad_ans.append((sid, ans, last[0]))
        except Exception:
            pass
print(json.dumps(stats))
show = int(sys.argv[sys.argv.index('--show') + 1]) if '--show' in sys.argv else 15
for sid, m in bad[:show]: print('CHAIN', sid, m[:160])
for sid, a, m in bad_ans[:show]: print('ANSWER', sid, a, '| last chain:', m[:120])
if '--json' in sys.argv:
    json.dump({'stats': stats, 'chains': bad, 'answers': bad_ans}, open(sys.argv[sys.argv.index('--json') + 1], 'w'), ensure_ascii=False, indent=1)
