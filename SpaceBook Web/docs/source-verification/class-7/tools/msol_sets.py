"""msol_sets.py - finite set operations with worked steps (union, intersection, difference, complement, verify)."""
import re
BS = chr(92)
from msol import step, ParseError

LBL = {
    'sets': ('Write the sets in roster form:', 'سیٹ فہرست کی صورت میں لکھیں:', 'سیټونه د لړلیک په بڼه ولیکئ:'),
    'op': ('Apply the operation:', 'عمل کریں:', 'عمل ترسره کړئ:'),
    'lhs': ('Left side:', 'بایاں طرف:', 'کیڼه خوا:'),
    'rhs': ('Right side:', 'دایاں طرف:', 'ښي خوا:'),
    'equal': ('Both sides are the same set, so it is verified.', 'دونوں طرف ایک ہی سیٹ ہے، لہٰذا تصدیق ہو گئی۔', 'دواړه خواوې یو ډول سیټ دی، نو تصدیق شو.'),
}


def roster(text):
    """'{2, 4, 6}' / '{0, 2, 4, ..., 18}' / '{ }' / '∅' -> frozenset or None if infinite/unsupported."""
    t = text.strip().strip('$').replace('\\{', '{').replace('\\}', '}').replace('−', '-')
    if t in ('∅', 'ϕ', '\\varnothing', '\\emptyset', '{ }', '{}'):
        return frozenset()
    if not (t.startswith('{') and t.endswith('}')):
        return None
    body = t[1:-1].strip()
    if not body:
        return frozenset()
    raw = [x.strip() for x in body.split(',') if x.strip() != '']
    if '...' in raw or '…' in raw or any('...' in x or '…' in x for x in raw):
        idx = next(i for i, x in enumerate(raw) if '...' in x or '…' in x)
        head = raw[:idx]
        tail = raw[idx + 1:]
        if not tail or len(head) < 2:
            return None
        try:
            h = [float(x) for x in head]
            e = float(tail[-1])
        except ValueError:
            # letters a, b, ..., z
            if len(head[-1]) == 1 and len(tail[-1]) == 1 and head[-1].isalpha():
                return frozenset(chr(c) for c in range(ord(head[0]), ord(tail[-1]) + 1))
            return None
        d = h[1] - h[0]
        if d == 0:
            return None
        n = int(round((e - h[0]) / d))
        vals = [h[0] + d * i for i in range(n + 1)]
        items = [int(v) if v == int(v) else v for v in vals]
        return frozenset(str(i) if not isinstance(i, str) else i for i in items) | frozenset(x for x in raw if '...' not in x and x not in ('…',))
    return frozenset(x for x in raw)


def fmt(s):
    if not s:
        return '\\varnothing'
    def key(x):
        try:
            return (0, float(x))
        except ValueError:
            return (1, x)
    return '\\{' + ', '.join(sorted(s, key=key)) + '\\}'


def parse_env(text):
    """'A = {1, 2}, B = {3}' -> {'A': set,...}  (names are single letters or letter+prime)"""
    env = {}
    for m in re.finditer(r'([A-Za-z])\s*=\s*(\{[^{}]*\}|∅|ϕ)', text.replace('−', '-')):
        s = roster(m.group(2))
        if s is None:
            raise ParseError('infinite set')
        env[m.group(1)] = s
    return env


def tokenize(expr):
    e = expr.replace('\\cup', '∪').replace('\\cap', '∩').replace('\\setminus', '−').replace('\\backslash', '−')
    e = re.sub(r'\^\{?\\?(c|prime)\}?', "'", e).replace('^c', "'").replace('^{c}', "'")
    e = e.replace('\\varnothing', '∅').replace('\\emptyset', '∅').replace('ϕ', '∅').replace('{', '(').replace('}', ')').replace('\\', '')
    return re.findall(r"[A-Za-z]'*|∅'*|∪|∩|−|-|\(|\)|'", e)


class SetEval:
    def __init__(self, env, universe=None):
        self.env = env; self.U = universe

    def ev(self, toks):
        self.t = toks; self.i = 0
        r = self.expr()
        if self.i != len(self.t):
            raise ParseError('trail')
        return r

    def expr(self):
        a = self.term()
        while self.i < len(self.t) and self.t[self.i] in ('∪', '∩', '−', '-'):
            op = self.t[self.i]; self.i += 1
            b = self.term()
            a = a | b if op == '∪' else a & b if op == '∩' else a - b
        return a

    def term(self):
        tk = self.t[self.i]
        if tk == '(':
            self.i += 1; v = self.expr(); self.i += 1
            if self.i < len(self.t) and self.t[self.i].startswith("'"):
                v = self.comp(v); self.i += 1
            return v
        self.i += 1
        base = tk.rstrip("'"); n = len(tk) - len(base)
        v = frozenset() if base == '∅' else self.env.get(base)
        if v is None:
            raise ParseError('unknown set ' + base)
        for _ in range(n):
            v = self.comp(v)
        return v

    def comp(self, v):
        if self.U is None:
            raise ParseError('no universe')
        return self.U - v


def eval_expr(expr, env, universe=None):
    return SetEval(env, universe).ev(tokenize(expr))


def op_steps(expr, text):
    env = parse_env(text)
    U = env.get('U') or env.get('ξ')
    res = eval_expr(expr, env, U)
    names = sorted({m for m in re.findall(r'[A-Za-z]', expr.replace('cup', '').replace('cap', '').replace('setminus', '').replace('varnothing', ''))})
    given = ' ,\\; '.join(f'{n} = {fmt(env[n])}' for n in names if n in env)
    ex = expr.replace('\\setminus', '-')
    steps = [step_l('sets', given), step_l('op', f'{expr} = {fmt(res)}')]
    return steps, res


def verify_steps(eq, text):
    l, r = [x.strip() for x in eq.split('=', 1)]
    env = parse_env(text)
    U = env.get('U')
    lv, rv = eval_expr(l, env, U), eval_expr(r, env, U)
    if lv != rv:
        raise ParseError('not equal')
    steps = [step_l('sets', ' ,\\; '.join(f'{n} = {fmt(v)}' for n, v in env.items())),
             step_l('lhs', f'{l} = {fmt(lv)}'), step_l('rhs', f'{r} = {fmt(rv)}'), step_l('equal', f'{l} = {r}')]
    return steps, lv


def step_l(key, m):
    e, u, p = LBL[key]
    return {'en': e, 'ur': u, 'ps': p, 'm': m}


# ---------------------------------------------------------------- relations between sets
def _two(part):
    env = parse_env(part.replace('$', ''))
    names = list(env)
    if len(names) != 2:
        raise ParseError('two sets')
    return names, env


def relation(kind, part):
    names, env = _two(part)
    a, b = env[names[0]], env[names[1]]
    A, Bn = names
    if kind == 'equal':
        res = a == b
        steps = [step_l('sets', f'{A} = {fmt(a)},\; {Bn} = {fmt(b)}'),
                 {'en': 'Equal sets have exactly the same elements (order and repetition do not matter):', 'ur': 'برابر سیٹوں کے عناصر بالکل ایک جیسے ہوتے ہیں (ترتیب اور تکرار اہم نہیں):', 'ps': 'مساوي سیټونه ورته عناصر لري (ترتیب او تکرار مهم نه دی):', 'm': f'{A} {"=" if res else chr(92) + "neq"} {Bn}'}]
        return steps, res
    if kind == 'equivalent':
        res = len(a) == len(b)
        steps = [step_l('sets', f'{A} = {fmt(a)},\; {Bn} = {fmt(b)}'),
                 {'en': 'Equivalent sets have the same number of elements:', 'ur': 'ہم وزن سیٹوں میں عناصر کی تعداد برابر ہوتی ہے:', 'ps': 'معادل سیټونه د عناصرو شمېر مساوي لري:', 'm': f'n({A}) = {len(a)},\; n({Bn}) = {len(b)}' + (' \\Rightarrow \\text{equivalent}' if res else ' \\Rightarrow \\text{not equivalent}')}]
        return steps, res
    if kind == 'overlap':
        common = a & b
        res = bool(common)
        steps = [step_l('sets', f'{A} = {fmt(a)},\; {Bn} = {fmt(b)}'),
                 {'en': 'Overlapping sets have at least one common element; disjoint sets have none:', 'ur': 'ملتے ہوئے سیٹوں میں کم از کم ایک مشترک عنصر ہوتا ہے؛ منفصل سیٹوں میں کوئی نہیں:', 'ps': 'یو بل پوښوونکي سیټونه لږ تر لږه یو ګډ عنصر لري؛ بېل سیټونه هېڅ نه لري:', 'm': f'{A} {chr(92)}cap {Bn} = {fmt(common)}' + (' \\Rightarrow \\text{overlapping}' if res else ' \\Rightarrow \\text{disjoint}')}]
        return steps, res
    raise ParseError('kind')


def subset_statement(stmt, envtext):
    env = parse_env(envtext.replace('$', ''))
    s = stmt.strip().strip('$')
    ops = [(BS + 'not' + BS + 'subseteq', lambda x, y: not x <= y), (BS + 'not' + BS + 'subset', lambda x, y: not x < y), (BS + 'subseteq', lambda x, y: x <= y), (BS + 'subset', lambda x, y: x < y), (BS + 'supseteq', lambda x, y: x >= y), (BS + 'supset', lambda x, y: x > y)]
    for op, fn in ops:
        if op in s:
            l, r = [t.strip() for t in s.split(op)]
            res = fn(env[l], env[r])
            steps = [step_l('sets', ' ,\; '.join(f'{n} = {fmt(v)}' for n, v in env.items())),
                     {'en': 'Check the statement with the elements:', 'ur': 'عناصر سے بیان جانچیں:', 'ps': 'له عناصرو سره بیان وارزوئ:', 'm': f'{s}: ' + ('\\text{true}' if res else '\\text{false}')}]
            return steps, res
    raise ParseError('stmt')


def perfect_square_parity(part, parity):
    import math
    n = int(re.sub(r'[^0-9]', '', part))
    r = math.isqrt(n)
    ok = r * r == n and (r % 2 == 0) == (parity == 'even')
    steps = [{'en': f'Find the square root of {n}:', 'ur': f'{n} کا جذر معلوم کریں:', 'ps': f'د {n} جذر ومومئ:', 'm': (f'\\sqrt{{{n}}} = {r}' if r * r == n else f'{n} \\text{{ is not a perfect square}}')},
             {'en': f'The root must be {parity} for a perfect square of an {parity} number:', 'ur': f'{parity} عدد کا مکمل مربع ہونے کے لیے جذر {parity} ہونا چاہیے:', 'ps': f'د {parity} عدد بشپړ مربع لپاره جذر باید {parity} وي:', 'm': ('\\text{' + ('Yes' if ok else 'No') + '}')}]
    return steps, ok
