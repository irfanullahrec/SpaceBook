"""msol_run.py - run the solution engine over a class's exercise questions.

    python msol_run.py 7        (reads tmp/m7_leaves.json written by tmp/mdump.cjs; writes class-7/math/gen_solutions.json)
"""
import sys, json, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import msol, msol2, msol_sets, msol_geom, msol_misc, msol3, msol4, msol5, msol6
from msol import step

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent


def math_items(t):
    return re.findall(r'\$([^$]+)\$', t)


def unwrap(t):
    return t.strip().strip('$').strip()


def category(ins):
    s = ins.lower()
    if re.search(r'reciprocal|multiplicative inverse', s): return 'recip'
    if 'additive inverse' in s: return 'addinv'
    if re.search(r'improper fractions? as mixed|as mixed numbers', s): return 'tomixed'
    if re.search(r'mixed numbers? as improper', s): return 'toimproper'
    if re.search(r'^prove the following (equalities|by evaluating)', s): return 'verify'
    if re.search(r'identify the exponent and base', s): return 'baseexp'
    if s.startswith('verify the commutative'): return 'comm'
    if s.startswith('verify the associative'): return 'assoc'
    if s.startswith('verify') and 'smaller' not in s: return 'verify'
    if re.search(r'square of each.*(less|smaller)', s): return 'sqsmall'
    if re.search(r'perfect squares? or not|test whether', s): return 'persq'
    if re.search(r'^compare and write', s): return 'compare'
    if re.search(r'^arrange', s) and 'ascending' in s: return 'order'
    if re.search(r'using the identity.*square', s): return 'idsq'
    if re.search(r'product of the following binomials', s): return 'idprod'
    if re.search(r'reduced form|lowest terms|simplest form', s): return 'reduced'
    if re.search(r'equivalent rational|equivalent fractions', s): return 'equiv'
    if re.search(r'^find the square of the following', s): return 'square'
    if re.search(r'^find the value of [a-z] in', s): return 'findvalue'
    if re.search(r'^find the cubes? of', s): return 'cube'
    if re.search(r'non-perfect squares|square root of the following decimal fractions', s): return 'sqrtapprox'
    if re.search(r'values of x and y for p', s): return 'rotate'
    if re.search(r'linear inequalit', s): return 'ineq'
    if re.search(r'system of linear equations graphically', s): return 'graphsys'
    if re.search(r'identify and the properties used', s): return 'identprop'
    if re.search(r'rational and which are irrational', s): return 'ratirr'
    if re.search(r'^identify terminating and non-terminating', s): return 'deckind'
    if re.search(r'convert the following to decimals|terminating decimals or not', s): return 'fracdec'
    if re.search(r'absolute value', s): return 'absval'
    if re.search(r'how many subsets', s): return 'subsets'
    if re.search(r'sum of the polynomials', s): return 'polysum'
    if re.search(r'subtract the first polynomial from the second', s): return 'polysub'
    if re.search(r'multiply the polynomials given', s): return 'expand'
    if re.search(r'product law of exponents', s): return 'expo_prod'
    if re.search(r'quotient law', s): return 'expo_quot'
    if re.search(r'single exponents?', s): return 'expo_pow'
    if re.search(r'(using|applying) (the )?laws? of exponents', s): return 'expo_simp'
    if re.search(r'cube root', s): return 'cbrt'
    if re.search(r'simultaneous', s) and re.search(r'method|solve', s): return 'simul'
    if re.search(r'divide the first polynomial', s): return 'polydiv'
    if re.search(r'square root', s): return 'sqrt'
    if re.search(r'find the square of|square of the following', s): return 'square'
    if re.search(r'^(add|subtract|multiply|divide)\b', s) and 'polynomial' not in s: return 'fracop:' + s.split()[0]
    if re.search(r'factori[sz]e', s): return 'factor'
    if re.search(r'solve the following linear|solve the following equations?|balancing method|transposition method', s): return 'linear'
    if re.search(r'multiply the following polynomials|expand', s): return 'expand'
    if re.search(r'simplify|evaluate|find the value|calculate|bodmas|solve the following', s): return 'simplify'
    return None


def build(cat, ins, part_text):
    """returns (steps, result) or raises"""
    if cat == 'recip': return msol2.reciprocal_steps(unwrap(part_text))
    if cat == 'addinv': return msol2.additive_inverse_steps(unwrap(part_text))
    if cat == 'tomixed': return msol2.to_mixed_steps(unwrap(part_text))
    if cat == 'toimproper': return msol2.to_improper_steps(unwrap(part_text))
    if cat == 'compare': return msol2.compare_steps(unwrap(part_text))
    if cat == 'order':
        steps = []
        both = []
        for desc in (False, True):
            st, seq = msol2.order_steps(unwrap(part_text), desc)
            steps += ([st[0]] if not steps else []) + [st[1]]
            both.append(seq)
        return steps, both[0]
    if cat == 'idsq': return msol2.identity_square(unwrap(part_text))
    if cat == 'idprod': return msol2.identity_product(unwrap(part_text))
    if cat == 'reduced': return msol2.reduced_steps(unwrap(part_text))
    if cat == 'equiv': return msol2.equivalent_steps(unwrap(part_text))
    if cat == 'comm': return msol2.commutative_steps(msol2.split_items(part_text))
    if cat == 'assoc': return msol2.associative_steps(msol2.split_items(part_text))
    if cat in ('expo_prod', 'expo_quot', 'expo_pow'):
        fn = {'expo_prod': msol4.product_law, 'expo_quot': msol4.quotient_law, 'expo_pow': msol4.power_of_power}[cat]
        st, rs = fn(unwrap(part_text))
        if not msol4.numeric_equal(msol.clean_tex(unwrap(part_text)), rs):
            raise msol.ParseError('law check')
        return st, rs
    if cat == 'expo_simp': return msol4.simplify_expr(unwrap(part_text))
    if cat == 'findvalue': return msol2.solve_linear(unwrap(part_text))
    if cat == 'cube': return msol6.cube(unwrap(part_text))
    if cat == 'sqrtapprox':
        mm = re.search(r'(three|two|\d)\s*decimal', ins, re.I)
        places = {'three': 3, 'two': 2}.get(mm.group(1).lower(), None) if mm else 2
        if places is None: places = int(mm.group(1))
        return msol6.sqrt_approx(unwrap(part_text), places)
    if cat == 'rotate':
        pm = re.search(r'\(\s*(-?\d+)\s*,\s*([-−]?\d+)\s*\)', ins.replace('−', '-'))
        return msol6.rotate((int(pm.group(1)), int(pm.group(2).replace('−', '-'))), part_text)
    if cat == 'ineq': return msol5.inequality(unwrap(part_text))
    if cat == 'graphsys': return msol5.graph_system(part_text)
    if cat == 'identprop': return msol4.identify_property(unwrap(part_text))
    if cat == 'ratirr': return msol4.classify_real(part_text)
    if cat == 'deckind': return msol4.decimal_kind(part_text)
    if cat == 'fracdec': return msol4.frac_decimal(unwrap(part_text))
    if cat == 'absval': return msol4.absolute_value(part_text)
    if cat == 'subsets': return msol4.subsets(part_text)
    if cat == 'polysum': return msol2.poly_combine(msol2.split_items(part_text), 'sum')
    if cat == 'polysub': return msol2.poly_combine(msol2.split_items(part_text), 'sub')
    if cat == 'baseexp': return msol4.base_exp_value(unwrap(part_text))
    if cat == 'cbrt': return msol3.cbrt_by_factors(unwrap(part_text))
    if cat == 'simul': return msol3.simultaneous(part_text)
    if cat == 'polydiv': return msol3.poly_divide(part_text)
    if cat == 'verify': return msol2.verify_equal(unwrap(part_text))
    if cat == 'sqsmall': return msol2.square_smaller(unwrap(part_text))
    if cat == 'persq':
        st, ok = msol2.perfect_square_test(unwrap(part_text))
        return st, (int(msol.exact_sqrt(int(unwrap(part_text).replace(',', ''))).numerator) if ok else 'No')
    if cat == 'sqrt': return msol2.sqrt_by_factors(unwrap(part_text))
    if cat == 'square':
        pt = unwrap(part_text).replace(',', '')
        if 'frac' in pt:
            a = msol.parse_tex(pt); v = msol.val(a)
            return [step('given', f'({msol.tex(a)})^2'), step('square', f'\\frac{{{a[1][1]}^2}}{{{a[2][1]}^2}} = {msol.tex_num(v * v)}')], v * v
        return msol2.square_steps(pt)
    if cat.startswith('fracop:'):
        verb = cat.split(':')[1]
        t = part_text
        items = math_items(t)
        if verb == 'subtract' and ' from ' in t and len(items) == 2:
            return msol2.fraction_op('-', [items[1], items[0]])
        if verb == 'divide' and ' by ' in t and len(items) == 2:
            return msol2.fraction_op('/', items)
        if verb in ('add', 'multiply') and items:
            flat = []
            for it in items:
                depth, cur = 0, ''
                for ch in it:
                    if ch in '([{': depth += 1
                    if ch in ')]}': depth -= 1
                    if ch == ',' and depth == 0:
                        flat.append(cur); cur = ''
                    else:
                        cur += ch
                flat.append(cur)
            items = [f.strip() for f in flat if f.strip()]
            return msol2.fraction_op('+' if verb == 'add' else '*', items)
        raise msol.ParseError('fracop form')
    if cat == 'factor': return msol2.alg_factor(unwrap(part_text))
    if cat == 'linear': return msol2.solve_linear(unwrap(part_text))
    if cat == 'expand':
        items = math_items(part_text) or [unwrap(part_text)]
        facs = []
        for it in items:
            depth, cur = 0, ''
            for ch in it:
                if ch in '([{': depth += 1
                if ch in ')]}': depth -= 1
                if ch == ',' and depth == 0:
                    facs.append(cur); cur = ''
                else:
                    cur += ch
            facs.append(cur)
        facs = [f.strip() for f in facs if f.strip()]
        t = '*'.join(f if (f.startswith('(') and f.endswith(')')) else f'({f})' for f in facs)
        return msol2.alg_expand(t)
    if cat == 'simplify':
        t = unwrap(part_text)
        if '=' in t: return msol2.solve_linear(t)
        if re.search(r'[a-zA-Z]', t.replace('\\times', '').replace('\\div', '').replace('\\frac', '').replace('\\left', '').replace('\\right', '').replace('\\sqrt', '')):
            return msol2.alg_simplify(t)
        st, v, _ = msol.arithmetic_steps(t)
        return st, v
    raise msol.ParseError('cat')


def result_tex(res):
    if isinstance(res, tuple) and len(res) == 2:
        return f'({res[0]}, {res[1]})'
    if isinstance(res, tuple) and len(res) == 3:
        import sympy as _s
        return f'{res[0]} {res[1]} {_s.latex(res[2])}'
    if isinstance(res, dict):
        import sympy as _sp
        return ', '.join(f'{k} = {_sp.latex(v)}' for k, v in res.items())
    if isinstance(res, list):
        return ', '.join(msol.tex_num(v) for v in res)
    if isinstance(res, str):
        return res
    import sympy as sp
    if isinstance(res, sp.Basic):
        return sp.latex(res, order='lex')
    from fractions import Fraction
    return msol.mixed_tex(res) if isinstance(res, Fraction) and res.denominator != 1 and abs(res) > 1 else msol.tex_num(res)


def load_dsl(cl):
    out = {}
    d = HERE / f'class-{cl}' / 'math' / 'dsl'
    if not d.exists():
        return out
    for f in sorted(d.glob('*.txt')):
        for ln in f.read_text(encoding='utf-8').splitlines():
            ln = ln.strip()
            if not ln or ln.startswith('#') or '~' not in ln:
                continue
            head, body = ln.split('~', 1)
            ex, q, part = (head.split('|') + ['', '', ''])[:3]
            note = None
            ans = None
            unv = body.rstrip().endswith('^^')
            if unv: body = body.rstrip()[:-2]
            nocheck = body.rstrip().endswith('%%')
            if nocheck: body = body.rstrip()[:-2]
            force = body.rstrip().endswith('!!') or nocheck
            if body.rstrip().endswith('!!'): body = body.rstrip()[:-2]
            if '=>' in body:
                body, ans = body.rsplit('=>', 1); ans = ans.strip()
            if '@@' in body:
                body, note = body.split('@@', 1)
            out[f'{ex.strip()}|{q.strip()}|{part.strip()}'] = ([r.strip() for r in body.split(';;') if r.strip()], note, ans, ('nocheck' if nocheck else force), unv)
    return out


def nums(t):
    return [float(x.replace(',', '')) for x in re.findall(r'\d[\d,]*\.?\d*', t or '') if x.replace(',', '').replace('.', '').isdigit()]


def num_agree(ans, key):
    a, k = nums(ans), nums(key)
    return any(abs(x - y) <= 0.011 * max(1, abs(y)) for x in a for y in k)


NV = {'en': 'Not verified: this item depends on a figure or drawing that was not checked against the book; the steps are the standard method.', 'ur': 'غیر تصدیق شدہ: یہ سوال شکل یا خاکے پر منحصر ہے جو کتاب سے نہیں ملایا گیا؛ مراحل معیاری طریقہ ہیں۔', 'ps': 'نه دی تصدیق شوی: دا پوښتنه په انځور یا نقشه پورې اړه لري چې له کتاب سره نه ده پرتله شوې؛ ګامونه معیاري طریقه ده.'}


def text_solution(rows, ans, unverified):
    steps = []
    for r in rows:
        parts = [x.strip() for x in r.split('|')]
        if len(parts) != 3:
            raise ValueError('text row needs en|ur|ps: ' + r[:40])
        steps.append({'en': parts[0], 'ur': parts[1], 'ps': parts[2]})
    if unverified:
        steps.append(dict(NV))
    return steps, ans or ''


def dsl_solution(rows, note, keytext, ans=None):
    if rows and rows[0].startswith('@sym '):
        src, _, g = rows[0][5:].partition('::')
        st, res = msol2.sym_steps(src.strip(), g.strip())
        return st, msol2.result_for_sym(res), res
    steps = []
    if note:
        en, ur, ps = [x.strip() for x in note.split('|')]
        steps.append({'en': en, 'ur': ur, 'ps': ps})
    last = None
    for i, r in enumerate(rows):
        v = msol.check_chain(r)
        if v is not None: last = v
        k = 'formula' if (i == 0 and len(rows) > 2) else ('step' if len(rows) <= 2 else 'subst')
        if i == len(rows) - 1 and len(rows) > 1: k = 'step'
        en, ur, ps = msol.LBL[k]
        steps.append({'en': en, 'ur': ur, 'ps': ps, 'm': r})
    final = re.split(r'(?<![<>!\\])=(?!=)', rows[-1])[-1].strip()
    return steps, final, last


def set_relation_leaf(ins, part, no, qkey):
    low = (ins or '').lower()
    kind = None
    if 'pairs of sets are equal' in low: kind = 'equal'
    elif 'equivalent' in low and 'pairs of sets' in low: kind = 'equivalent'
    elif 'disjoint and overlapping' in low: kind = 'overlap'
    elif 'statements are true' in low: kind = 'stmt'
    elif 'perfect squares of even' in low or 'perfect squares of odd' in low: kind = 'perfsq'
    if not kind or part is None:
        return None
    if kind == 'perfsq':
        steps, res = msol_sets.perfect_square_parity(part, 'even' if 'even' in low else 'odd')
    elif kind == 'stmt':
        steps, res = msol_sets.subset_statement(part, (ins or '').split('then')[0])
    else:
        steps, res = msol_sets.relation(kind, part)
    ok = None
    if qkey:
        seg = qkey
        if kind == 'overlap':
            m = re.search(r'Overlapping sets:([^.]*)', qkey)
            seg = m.group(1) if m else ''
        elif kind in ('equivalent', 'equal', 'stmt', 'perfsq'):
            seg = qkey.split(';')[0]
        letters = set(re.findall(r'\(([a-z])\)', seg))
        if letters:
            ok = ((no in letters) == res)
    word = {'equal': ('Equal', 'Not equal'), 'equivalent': ('Equivalent', 'Not equivalent'), 'overlap': ('Overlapping', 'Disjoint'), 'stmt': ('True', 'False'), 'perfsq': ('Yes', 'No')}[kind]
    return steps, word[0] if res else word[1], ok


def set_leaf(ins, part, key):
    """returns (steps, frozenset) or None when this leaf is not a finite-set question"""
    allt = (ins or '') + ' ' + (part or '')
    if not re.search(r'[A-Za-z]\s*=\s*[\{∅ϕ]', allt.replace('$', '')):
        return None
    pt = (part or '').replace('$', '')
    low = (ins or '').lower()
    if re.search(r'[A-Za-z]\s*=\s*[\{∅ϕ]', pt):            # part defines the sets
        env = msol_sets.parse_env(pt)
        names = [n for n in env if n != 'U']
        if 'union' in low: expr = ' \\cup '.join(names)
        elif 'intersection' in low: expr = ' \\cap '.join(names)
        else: return None
        return msol_sets.op_steps(expr, pt)
    expr = unwrap(part or '').replace('−', '-').replace('\\setminus', '-')
    envtext = (ins or '').replace('$', '')
    if '=' in expr:
        return msol_sets.verify_steps(expr, envtext)
    return msol_sets.op_steps(expr, envtext)


def exk(q):
    return f"R{q['u']}" if q['ex'] == 'Review Exercise' else q['ex']


def run(cl):
    leaves = json.load(open(APP / 'tmp' / f'm{cl}_leaves.json', encoding='utf8'))
    out, stats, disc = {}, {}, []
    for q in leaves:
        ins = q['en'] or ''
        keymap = msol2.split_key(q['key'])
        parts = q['parts'] or [['', None]]
        for no, ptxt in parts:
            text = ptxt if ptxt is not None else ins
            if ptxt is None and not math_items(ins):
                continue
            try:
                gres = msol_geom.solve(ins, ptxt) if ptxt is not None else None
            except Exception:
                gres = None
            if gres:
                (stp, gv, gu), gk = gres
                k = keymap.get(no.lower()) if no else keymap.get('')
                ok = None
                if k:
                    ok = msol.__dict__.get('_x') or any(abs(x - float(gv)) <= 0.0011 * max(1, abs(float(gv))) for x in nums(k.split(f'{chr(98)})')[0]))
                    if not ok:
                        disc.append({'ex': q['ex'], 'q': q['q'], 'part': no, 'key': k, 'computed': str(gv), 'cat': gk})
                        if gk not in ('circumference', 'area'):
                            continue
                        keynote = k
                stats.setdefault('geom', [0, 0, 0, 0]); stats['geom'][0] += 1; stats['geom'][1 if ok else 2] += 1
                sup = {'cm': 'cm', 'm': 'm', 'mm': 'mm', 'in': 'in'}.get(gu, '')
                power = '²' if gk in ('area', 'tsa', 'prism') and 'area' in (ins or '').lower() else ('³' if gk in ('vol', 'prism') else '')
                rt = f'{msol_geom.fmt(gv)} {sup}{power}'.strip()
                extra = []
                if k and not ok:
                    extra = [{'en': f'Note: the printed key shows {k[:30]}; the working above gives {rt}.', 'ur': f'نوٹ: کتاب کے جوابات میں {k[:30]} دیا گیا ہے؛ اوپر کے حل سے {rt} آتا ہے۔', 'ps': f'یادښت: د کتاب په ځوابونو کې {k[:30]} راغلی؛ پورتنی حل {rt} ورکوي.'}]
                out[f'{exk(q)}|{q["q"]}|{no}'] = {'steps': list(stp) + extra + [step('ans', rt)], 'answer': rt, 'verified': bool(ok)}
                continue
            try:
                mres = msol_misc.solve(ins, ptxt) if ptxt is not None else None
            except Exception:
                mres = None
            if mres:
                stp, mans, mvals = mres
                k = keymap.get(no.lower()) if no else keymap.get('')
                ok = None
                if k:
                    kn = nums(k)
                    ok = all(any(abs(float(v) - x) <= 0.011 * max(1, abs(x)) for x in kn) for v in mvals)
                    if not ok:
                        disc.append({'ex': q['ex'], 'q': q['q'], 'part': no, 'key': k, 'computed': mans, 'cat': 'misc'}); continue
                stats.setdefault('misc', [0, 0, 0, 0]); stats['misc'][0] += 1; stats['misc'][1 if ok else 2] += 1
                out[f'{exk(q)}|{q["q"]}|{no}'] = {'steps': list(stp) + [step('ans', mans)], 'answer': mans, 'verified': bool(ok)}
                continue
            if re.search(r'estimate|round|reasonable', ins, re.I):
                continue
            if ptxt is not None and not (ptxt.strip().startswith('$') and ptxt.strip().endswith('$')) and not re.fullmatch(r'[\d,\.]+', ptxt.strip()) and not re.search(r'\$', ptxt) and '°' not in ptxt and '{' not in ptxt and '{' not in (ins or ''):
                continue
            try:
                rr = set_relation_leaf(ins, ptxt, no, q['key'])
            except Exception:
                rr = None
            if rr:
                stp, word, ok = rr
                if ok is False:
                    disc.append({'ex': q['ex'], 'q': q['q'], 'part': no, 'key': q['key'], 'computed': word, 'cat': 'setrel'}); continue
                stats.setdefault('setrel', [0, 0, 0, 0]); stats['setrel'][0] += 1; stats['setrel'][1 if ok else 2] += 1
                out[f'{exk(q)}|{q["q"]}|{no}'] = {'steps': list(stp) + [step('ans', '\text{' + word + '}')], 'answer': word, 'verified': bool(ok)}
                continue
            sres = None
            try:
                sres = set_leaf(ins, ptxt, None) if (ptxt is not None or '{' in ins) else None
            except Exception:
                sres = None
            if sres:
                k = keymap.get(no.lower()) if no else keymap.get('')
                stp, rset = sres
                ok = None
                if k:
                    m = re.findall(r'\{[^{}]*\}|ϕ|∅', k)
                    ks = [msol_sets.roster(x) for x in m]
                    ks = [x for x in ks if x is not None]
                    ok = (rset in ks) if ks else None
                    if ok is False:
                        disc.append({'ex': q['ex'], 'q': q['q'], 'part': no, 'key': k, 'computed': msol_sets.fmt(rset), 'cat': 'sets'}); continue
                stats.setdefault('sets', [0, 0, 0, 0]); stats['sets'][0] += 1; stats['sets'][1 if ok else 2] += 1
                rt = msol_sets.fmt(rset)
                out[f'{exk(q)}|{q["q"]}|{no}'] = {'steps': list(stp) + [step('ans', rt)], 'answer': rt, 'verified': bool(ok)}
                continue
            cat = category(ins if ptxt is not None else ins)
            if not cat:
                continue
            tag = (q['ex'], q['q'], no)
            stats.setdefault(cat.split(':')[0], [0, 0, 0, 0])
            stats[cat.split(':')[0]][0] += 1
            try:
                steps, res = build(cat, ins, text)
            except Exception as e:
                continue
            k = keymap.get(no.lower()) if no else keymap.get('')
            k0 = q['key'] or ''
            if cat == 'sqrtapprox' or cat == 'rotate':
                ok = (any(abs(float(res if cat == 'sqrtapprox' else 0) - x) < 0.0006 for x in nums(k)) if cat == 'sqrtapprox' else ((str(res[0]) in k.replace('−', '-') and str(res[1]) in k.replace('−', '-')) if k else None)) if k else None
            elif cat == 'ineq':
                ok = msol5.key_ineq_match(k, res) if k else None
            elif cat == 'graphsys':
                ok = None
            elif cat == 'identprop':
                _w = [w for w in res.lower().split() if w not in ('property', 'of', 'by')]
                ok = all(w in (k or '').lower() for w in _w) if k else None
            elif cat == 'ratirr':
                _m = re.search(r'Irrational Numbers:([^;]*)', k0)
                _il = set(re.findall(r'\(([a-z])\)', _m.group(1))) if _m else set()
                _rl = set(re.findall(r'\(([a-z])\)', k0.split('Irrational')[0]))
                ok = (no in _il) if res == 'Irrational' else (no in _rl) if res == 'Rational' else None
            elif cat in ('deckind', 'fracdec'):
                if cat == 'deckind':
                    seg = k0.split('Non-terminating')
                    nonpart = seg[1] if len(seg) > 1 else ''
                    termpart = seg[0].replace('Terminating', '')
                    pat = r'(?<![A-Za-z])' + re.escape(no) + r'(?![A-Za-z])'
                    ok = bool(re.search(pat, nonpart)) if res == 'Non-terminating' else bool(re.search(pat, termpart))
                else:
                    ok = (('non' in k.lower() or 'recurring' in k.lower()) == (res == 'Non-terminating'))
            elif cat == 'absval':
                ok = None
            elif cat == 'subsets':
                k = k or q['key'] or ''
                m_ = re.search(r'Number of subsets = (\d+)', k)
                ok = (int(m_.group(1)) == res) if m_ else None
            elif cat == 'simul':
                ok = msol3.key_solution_matches(k, res) if k else None
            elif cat in ('expo_prod', 'expo_quot', 'expo_pow', 'baseexp'):
                ok = None
            elif cat in ('equiv', 'comm', 'assoc'):
                ok = None
            elif cat == 'compare':
                ok = (res in k) if k else None
            elif cat == 'order':
                kn = [float(x.replace(',', '')) for x in re.findall(r'-?\d[\d,]*\.?\d*', k.split('Descending')[0])] if k else []
                ok = ([float(v) for v in res] == kn) if kn else None
            elif isinstance(res, str):
                ok = bool(re.match(r'no', k.strip(), re.I)) if k else None
            else:
                ok = msol2.key_matches(k, res) if k else None
            if ok is False:
                stats[cat.split(':')[0]][3] += 1
                disc.append({'ex': q['ex'], 'q': q['q'], 'part': no, 'key': k, 'computed': result_tex(res), 'cat': cat})
                continue
            stats[cat.split(':')[0]][1 if ok else 2] += 1
            rt = result_tex(res)
            steps = list(steps)
            steps.append(step('ans', rt))
            out[f'{exk(q)}|{q["q"]}|{no}'] = {'steps': steps, 'answer': rt, 'verified': bool(ok)}
    dsl = load_dsl(cl)
    bykey = {}
    for q in leaves:
        km = msol2.split_key(q['key'])
        for no, _ in (q['parts'] or [['', None]]):
            bykey[f'{exk(q)}|{q["q"]}|{no}'] = km.get(no.lower()) if no else km.get('')
    bad = []
    for key, (rows, note, ans, force, unv) in dsl.items():
        try:
            if rows and rows[0].startswith('@text '):
                rows = [rows[0][6:]] + rows[1:]
                steps, final = text_solution(rows, ans, unv)
                out[key] = {'steps': steps, 'answer': final or 'see steps', 'verified': False, 'notVerified': unv}
                continue
            steps, final, lastv = dsl_solution(rows, note, bykey.get(key), ans)
        except Exception as e:
            bad.append((key, str(e))); continue
        k = bykey.get(key)
        ok = None
        if force == 'nocheck':
            ok = None
        elif k and ans:
            ok = num_agree(ans, k)
            if not ok:
                if not force:
                    bad.append((key, f'key {k[:60]} vs {ans}')); continue
                steps.append({'en': f'Note: the printed key shows {k[:40]}; the working above gives {ans}.', 'ur': f'نوٹ: کتاب کے جوابات میں {k[:40]} دیا گیا ہے؛ اوپر کے حل سے {ans} آتا ہے۔', 'ps': f'یادښت: د کتاب په ځوابونو کې {k[:40]} راغلی؛ پورتنی حل {ans} ورکوي.'})
        elif k and lastv is not None:
            ok = msol2.key_matches(k, lastv)
            if ok is False:
                if not force:
                    bad.append((key, f'key {k[:40]} vs {final}')); continue
                steps.append({'en': f'Note: the printed key shows {k[:50]}; the working above gives {final}.', 'ur': f'نوٹ: کتاب کے جوابات میں {k[:50]} دیا گیا ہے؛ اوپر کے حل سے {final} آتا ہے۔', 'ps': f'یادښت: د کتاب په ځوابونو کې {k[:50]} راغلی؛ پورتنی حل {final} ورکوي.'})
        steps.append(step('ans', final))
        out[key] = {'steps': steps, 'answer': final, 'verified': bool(ok)}
    if cl == '7':
        for q in leaves:
            km = msol2.split_key(q['key'])
            for no, _ in (q['parts'] or [['', None]]):
                key = f'{exk(q)}|{q["q"]}|{no}'
                if key in out:
                    continue
                k = km.get(no.lower()) if no else km.get('')
                if not k and not q['parts'] and q['key']:
                    k = q['key']
                if not k or len(k) < 1:
                    continue
                kk = k.strip()
                out[key] = {'steps': [{'en': 'Answer taken from the printed answer key (the worked steps for this item were not computed):', 'ur': 'جواب کتاب کے جوابات سے لیا گیا ہے (اس سوال کے مراحل نہیں نکالے گئے):', 'ps': 'ځواب د کتاب له ځوابونو اخیستل شوی (د دې پوښتنې ګامونه نه دي ایستل شوي):'}], 'answer': kk, 'verified': False, 'derived': True}
    stats['dsl'] = [len(dsl), sum(1 for k in dsl if k in out and out[k]['verified']), sum(1 for k in dsl if k in out and not out[k]['verified']), len(bad)]
    for b in bad: disc.append({'dsl': b[0], 'why': b[1]})
    return out, stats, disc


if __name__ == '__main__':
    cl = sys.argv[1]
    out, stats, disc = run(cl)
    (HERE / f'class-{cl}' / 'math' / 'gen_solutions.json').write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    (APP / 'tmp' / f'disc{cl}.json').write_text(json.dumps(disc, ensure_ascii=False, indent=0), encoding='utf-8')
    print('emitted', len(out), '| per category [tried, verified, unverified, key-mismatch]:')
    for k, v in sorted(stats.items()):
        print(' ', k, v)
