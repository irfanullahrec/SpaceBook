"""msol.py - worked-solution engine for Class 7/8 Mathematics (EN / UR / PS).

Every solution is COMPUTED (fractions / sympy) and, where the textbook prints an answer, CHECKED against it;
a result that disagrees with the printed key is never emitted.

    from msol import solve_leaf
    sol = solve_leaf(instruction, part_text, key_text)   # dict {steps:[{en,ur,ps,m}], answer} or None
"""
import re
from fractions import Fraction
import sympy as sp

# ---------------------------------------------------------------- phrases (EN, UR, PS)
PH = {
    'given': ('Given:', 'دیا گیا:', 'ورکړل شوی:'),
    'brackets': ('Work out the brackets first (BODMAS):', 'پہلے قوسین حل کریں (BODMAS):', 'لومړی قوسونه حل کړئ (BODMAS):'),
    'powers': ('Work out the powers and roots:', 'طاقتیں اور جذر نکالیں:', 'توانونه او جذرونه وباسئ:'),
    'muldiv': ('Multiply / divide from left to right:', 'بائیں سے دائیں ضرب / تقسیم کریں:', 'له کیڼ څخه ښي ته ضرب / وېش وکړئ:'),
    'addsub': ('Add / subtract from left to right:', 'بائیں سے دائیں جمع / تفریق کریں:', 'له کیڼ څخه ښي ته جمع / تفریق وکړئ:'),
    'lcd': ('Make the denominators equal (LCM of the denominators):', 'نسب نما برابر کریں (نسب نماؤں کا ذواضعفِ اقل):', 'مخرجونه برابر کړئ (د مخرجونو ل.م.ګ):'),
    'combine': ('Combine the numerators:', 'شمار کنندے جمع / تفریق کریں:', 'صورتونه سره یو ځای کړئ:'),
    'recip': ('Dividing by a fraction means multiplying by its reciprocal:', 'کسر سے تقسیم کا مطلب اس کے معکوس سے ضرب ہے:', 'په کسر وېش د هغه د معکوس سره ضرب ګڼل کېږي:'),
    'simplify': ('Reduce to the simplest form:', 'مختصر ترین صورت میں لکھیں:', 'په ساده ترینه بڼه ولیکئ:'),
    'mixed': ('Convert the mixed numbers to improper fractions:', 'مخلوط اعداد کو غیر واجب کسر میں بدلیں:', 'ګډ عددونه ناسم کسرونو ته واړوئ:'),
    'ans': ('Answer:', 'جواب:', 'ځواب:'),
    'expand': ('Multiply out the brackets:', 'قوسین کھولیں (ضرب دیں):', 'قوسونه خلاص کړئ (ضرب):'),
    'collect': ('Collect like terms:', 'ہم جنس اجزا اکٹھے کریں:', 'ورته جزونه سره راټول کړئ:'),
    'common': ('Take out the common factor:', 'مشترک جزو باہر نکالیں:', 'ګډ فکتور وباسئ:'),
    'factor': ('Factorize:', 'اجزائے ضربی بنائیں:', 'فکتورونه جوړ کړئ:'),
    'check': ('Check by multiplying back:', 'واپس ضرب دے کر جانچیں:', 'بېرته ضرب کولو سره وارزوئ:'),
    'solve': ('Solve for the unknown:', 'نامعلوم کی قیمت معلوم کریں:', 'نامعلوم ارزښت ومومئ:'),
    'sub_both': ('Subtract {t} from both sides:', 'دونوں طرف سے {t} تفریق کریں:', 'له دواړو خواوو {t} تفریق کړئ:'),
    'add_both': ('Add {t} to both sides:', 'دونوں طرف {t} جمع کریں:', 'دواړو خواوو ته {t} جمع کړئ:'),
    'div_both': ('Divide both sides by {t}:', 'دونوں طرف کو {t} سے تقسیم کریں:', 'دواړه خواوې په {t} ووېشئ:'),
    'mul_both': ('Multiply both sides by {t}:', 'دونوں طرف کو {t} سے ضرب دیں:', 'دواړه خواوې په {t} کې ضرب کړئ:'),
    'verify': ('Verify: put the value back in the equation.', 'تصدیق: قیمت کو مساوات میں رکھیں۔', 'تصدیق: ارزښت بیا په معادله کې کېږدئ.'),
    'primes': ('Write the prime factors:', 'مفرد اجزائے ضربی لکھیں:', 'لومړني فکتورونه ولیکئ:'),
    'pairs': ('Make pairs of equal factors; take one from each pair:', 'برابر اجزا کے جوڑے بنائیں؛ ہر جوڑے سے ایک لیں:', 'د مساوي فکتورونو جوړې جوړې کړئ؛ له هرې جوړې یو واخلئ:'),
    'sqrt_frac': ('Take the square root of the numerator and of the denominator:', 'شمار کنندہ اور نسب نما کا جذر الگ الگ نکالیں:', 'د صورت او مخرج جذر بېل بېل وباسئ:'),
    'to_frac': ('Write as a fraction:', 'کسر کی صورت میں لکھیں:', 'د کسر په بڼه ولیکئ:'),
    'square': ('Square the number:', 'عدد کا مربع نکالیں:', 'د عدد مربع وباسئ:'),
    'additive': ('The additive inverse changes the sign:', 'جمعی معکوس علامت بدل دیتا ہے:', 'جمعي معکوس نښه بدلوي:'),
    'multinv': ('The multiplicative inverse (reciprocal) turns the fraction upside down:', 'ضربی معکوس کسر کو الٹ دیتا ہے:', 'ضربي معکوس کسر ګرځوي:'),
    'improper': ('Mixed number to improper fraction: whole × denominator + numerator:', 'مخلوط عدد سے غیر واجب کسر: مکمل × نسب نما + شمار کنندہ:', 'له ګډ عدد څخه ناسم کسر: بشپړ × مخرج + صورت:'),
    'tomixed': ('Divide the numerator by the denominator: quotient = whole part, remainder = new numerator.', 'شمار کنندہ کو نسب نما پر تقسیم کریں: خارج قسمت = مکمل حصہ، باقی = نیا شمار کنندہ۔', 'صورت په مخرج ووېشئ: خارج قسمت = بشپړ برخه، پاتې = نوی صورت.'),
    'eqfrac': ('Multiply the numerator and denominator by the same number:', 'شمار کنندہ اور نسب نما کو ایک ہی عدد سے ضرب دیں:', 'صورت او مخرج په یو شان عدد کې ضرب کړئ:'),
    'identity': ('Use the identity {t}:', 'کلیہ {t} استعمال کریں:', 'فورمول {t} وکاروئ:'),
    'group': ('Make groups and take out the common factor of each group:', 'گروپ بنائیں اور ہر گروپ کا مشترک جزو نکالیں:', 'ډلې جوړې کړئ او د هرې ډلې ګډ فکتور وباسئ:'),
}


def P(key, **kw):
    e, u, p = PH[key]
    return tuple(x.format(**kw) if kw else x for x in (e, u, p))


def step(key, m=None, **kw):
    e, u, p = P(key, **kw)
    s = {'en': e, 'ur': u, 'ps': p}
    if m is not None:
        s['m'] = m
    return s


# ---------------------------------------------------------------- number helpers
def tex_num(v, dec=None):
    """Fraction -> TeX. dec: number of decimals to keep (decimal operands stay decimals)."""
    v = Fraction(v)
    if dec is not None:
        s = f'{float(v):.{dec}f}'.rstrip('0').rstrip('.') if dec else str(int(v))
        if '.' in s or dec == 0:
            return s
    if v.denominator == 1:
        return str(v.numerator)
    sign = '-' if v < 0 else ''
    return f'{sign}\\frac{{{abs(v.numerator)}}}{{{v.denominator}}}'


def mixed_tex(v):
    v = Fraction(v)
    if v.denominator == 1 or abs(v) < 1:
        return tex_num(v)
    w = abs(v.numerator) // v.denominator
    r = Fraction(abs(v.numerator) - w * v.denominator, v.denominator)
    sign = '-' if v < 0 else ''
    return f'{sign}{w}\\frac{{{r.numerator}}}{{{r.denominator}}}'


def lcm(a, b):
    return a * b // __import__('math').gcd(a, b)


# ---------------------------------------------------------------- TeX -> AST
class ParseError(Exception):
    pass


def clean_tex(s):
    s = s.strip().strip('$').strip()
    s = s.replace('\\left', '').replace('\\right', '').replace('\\,', '').replace('\\ ', ' ')
    s = s.replace('{,}', '').replace('\\dfrac', '\\frac').replace('\\tfrac', '\\frac')
    s = s.replace('−', '-').replace('×', '\\times').replace('÷', '\\div')
    s = re.sub(r'(?<=\d),(?=\d{3}\b)', '', s)
    return s


BO = chr(92) + '{'
BC = chr(92) + '}'
TOK = re.compile(r'\s*(\d+\.\d+|\d+|\\frac|\\times|\\div|\\sqrt|\\cdot|\\\{|\\\}|[+\-*/^()\[\]{}])')


def tokenize(s):
    s = clean_tex(s)
    pos, out = 0, []
    while pos < len(s):
        m = TOK.match(s, pos)
        if not m:
            if s[pos:].strip() == '':
                break
            raise ParseError('tok:' + s[pos:pos + 10])
        out.append(m.group(1)); pos = m.end()
    return out


class Parser:
    """expr := term (('+'|'-') term)* ; term := unary (('\\times'|'\\div'|'\\cdot') unary)* ;
    unary := '-' unary | pow ; pow := atom ('^' atom)? ; atom := number | frac | sqrt | group; mixed numbers a\\frac{b}{c}."""

    def __init__(self, toks):
        self.t = toks; self.i = 0

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def eat(self, x=None):
        v = self.peek()
        if v is None or (x is not None and v != x):
            raise ParseError(f'expected {x} got {v}')
        self.i += 1
        return v

    def parse(self):
        n = self.expr()
        if self.peek() is not None:
            raise ParseError('trailing')
        return n

    def expr(self):
        n = self.term()
        while self.peek() in ('+', '-'):
            op = self.eat(); n = ('bin', op, n, self.term())
        return n

    def term(self):
        n = self.unary()
        while self.peek() in ('\\times', '\\div', '\\cdot', '*', '/', '(', '[', BO):
            if self.peek() in ('(', '[', BO):
                n = ('bin', '*', n, self.unary())
                continue
            op ={'\\times': '*', '\\cdot': '*', '*': '*', '\\div': '/', '/': '/'}[self.eat()]
            n = ('bin', op, n, self.unary())
        return n

    def unary(self):
        if self.peek() == '-':
            self.eat(); return ('neg', self.unary())
        if self.peek() == '+':
            self.eat(); return self.unary()
        return self.pw()

    def pw(self):
        b = self.atom()
        if self.peek() == '^':
            self.eat()
            if self.peek() == '{':
                self.eat('{'); e = self.expr(); self.eat('}')
            else:
                e = self.atom()
            return ('pow', b, e)
        return b

    def atom(self):
        t = self.peek()
        if t is None:
            raise ParseError('eof')
        if re.fullmatch(r'\d+(\.\d+)?', t):
            self.eat()
            dec = len(t.split('.')[1]) if '.' in t else None
            if self.peek() == '\\frac' and dec is None:       # mixed number
                f = self.frac()
                return ('mix', int(t), f[1], f[2])
            return ('num', Fraction(t), dec)
        if t == '\\frac':
            f = self.frac(); return ('frac', f[1], f[2])
        if t == '\\sqrt':
            self.eat(); self.eat('{'); e = self.expr(); self.eat('}'); return ('sqrt', e)
        if t in ('(', '[', BO):
            close = {'(': ')', '[': ']', BO: BC}[t]
            sym = {'(': '(', '[': '[', BO: '{'}[t]
            self.eat(); e = self.expr(); self.eat(close); return ('grp', e, sym)
        raise ParseError('atom:' + t)

    def frac(self):
        self.eat('\\frac'); self.eat('{'); a = self.expr(); self.eat('}')
        self.eat('{'); b = self.expr(); self.eat('}')
        return ('f', a, b)


def parse_tex(s):
    return Parser(tokenize(s)).parse()


# ---------------------------------------------------------------- AST -> TeX / value
def val(n):
    k = n[0]
    if k == 'num': return n[1]
    if k == 'mix': return n[1] + Fraction(n[2][1], n[3][1]) if False else n[1] + val(n[2]) / val(n[3])
    if k == 'frac': return val(n[1]) / val(n[2])
    if k == 'neg': return -val(n[1])
    if k == 'grp': return val(n[1])
    if k == 'sqrt':
        v = val(n[1]); r = exact_sqrt(v)
        if r is None: raise ParseError('irrational')
        return r
    if k == 'pow':
        b, e = val(n[1]), val(n[2])
        if e.denominator != 1 or abs(e) > 12: raise ParseError('pow')
        return b ** int(e)
    if k == 'bin':
        a, b = val(n[2]), val(n[3]); op = n[1]
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if b == 0: raise ParseError('div0')
        return a / b
    raise ParseError(k)


def exact_sqrt(v):
    v = Fraction(v)
    if v < 0: return None
    import math
    a, b = math.isqrt(v.numerator), math.isqrt(v.denominator)
    if a * a == v.numerator and b * b == v.denominator:
        return Fraction(a, b)
    return None


def tex(n, top=True):
    k = n[0]
    if k == 'num': return tex_num(n[1], n[2])
    if k == 'mix': return f'{n[1]}\\frac{{{tex(n[2])}}}{{{tex(n[3])}}}'
    if k == 'frac': return f'\\frac{{{tex(n[1])}}}{{{tex(n[2])}}}'
    if k == 'neg': return '-' + tex(n[1], False)
    if k == 'grp':
        o = {'(': '(', '[': '[', '{': '\\{'}[n[2]]; c = {'(': ')', '[': ']', '{': '\\}'}[n[2]]
        return f'\\left{o}{tex(n[1])}\\right{c}'
    if k == 'sqrt': return f'\\sqrt{{{tex(n[1])}}}'
    if k == 'pow': return f'{tex(n[1], False)}^{{{tex(n[2])}}}'
    if k == 'bin':
        op = {'+': '+', '-': '-', '*': '\\times', '/': '\\div'}[n[1]]
        r = tex(n[3]) if n[3][0] != 'neg' else '(' + tex(n[3]) + ')'
        return f'{tex(n[2])} {op} {r}'
    raise ParseError(k)


def is_atom(n):
    return n[0] in ('num', 'mix', 'frac') or (n[0] == 'neg' and is_atom(n[1]))


def has_dec(n):
    if n[0] == 'num': return n[2] is not None
    return any(has_dec(c) for c in n[1:] if isinstance(c, tuple))


def dec_places(n):
    if n[0] == 'num': return n[2] or 0
    return max([dec_places(c) for c in n[1:] if isinstance(c, tuple)] or [0])


def leaf(v):
    v = Fraction(v)
    if v.denominator == 1:
        return ('num', v, None) if v >= 0 else ('neg', ('num', -v, None))
    f = ('frac', ('num', Fraction(abs(v.numerator)), None), ('num', Fraction(v.denominator), None))
    return f if v > 0 else ('neg', f)


def mk(v, like):
    """AST leaf for a Fraction result; decimal operands give a decimal result when it terminates."""
    f = Fraction(v)
    if has_dec(like):
        d = dec_places(like)
        for dd in range(d, d + 8):
            if (f * 10 ** dd).denominator == 1:
                return ('num', f, dd) if f >= 0 else ('neg', ('num', -f, dd))
    return leaf(f)


def reduce_level(n):
    """Evaluate every operation of the highest precedence found in this (grp-free) expression. Returns new node."""
    ops = collect(n)
    if not ops: return n
    top = min(ops)  # 0 pow/sqrt, 1 muldiv, 2 addsub
    return apply_level(n, top)


def collect(n, acc=None):
    acc = set() if acc is None else acc
    k = n[0]
    if k in ('pow', 'sqrt'):
        acc.add(0)
        for c in n[1:]:
            if isinstance(c, tuple): collect(c, acc)
    elif k == 'bin':
        acc.add(1 if n[1] in '*/' else 2)
        collect(n[2], acc); collect(n[3], acc)
    elif k == 'neg':
        collect(n[1], acc)
    elif k == 'mix':
        pass
    elif k == 'frac':
        pass
    return acc


def apply_level(n, level):
    k = n[0]
    if k == 'pow' and level == 0:
        return mk(val(n), n)
    if k == 'sqrt' and level == 0:
        return mk(val(n), n)
    if k == 'bin':
        l, r = apply_level(n[2], level), apply_level(n[3], level)
        lev = 1 if n[1] in '*/' else 2
        if lev == level and is_atom(l) and is_atom(r):
            res = val(('bin', n[1], l, r))
            return mk(res, ('bin', n[1], l, r))
        return ('bin', n[1], l, r)
    if k == 'neg':
        return ('neg', apply_level(n[1], level))
    return n


def flatten_left(n):
    """Left-associative chains: a op b op c is ((a op b) op c) already, so reduce_level handles leftmost pairs only;
    repeat until no op of that level remains reducible."""
    return n


def contains_grp(n):
    if n[0] == 'grp': return True
    return any(contains_grp(c) for c in n[1:] if isinstance(c, tuple))


def innermost_grp_reduce(n):
    """Reduce inside innermost groups; returns (newnode, changed)."""
    k = n[0]
    if k == 'grp':
        inner, ch = innermost_grp_reduce(n[1])
        if ch: return ('grp', inner, n[2]), True
        # inner has no group
        if is_atom(n[1]):
            return n[1], True
        red = reduce_level(n[1])
        return (red if is_atom(red) else ('grp', red, n[2])), True
    if k in ('bin',):
        a, c1 = innermost_grp_reduce(n[2])
        if c1: return ('bin', n[1], a, n[3]), True
        b, c2 = innermost_grp_reduce(n[3])
        if c2: return ('bin', n[1], n[2], b), True
        return n, False
    if k in ('neg', 'pow', 'sqrt'):
        a, c = innermost_grp_reduce(n[1])
        if c: return (k, a) + n[2:], True
        if k == 'pow':
            b, c = innermost_grp_reduce(n[2])
            if c: return (k, n[1], b), True
    return n, False


def normalize_atoms(n):
    """mixed numbers -> improper fractions for computation (shown as a step)."""
    k = n[0]
    if k == 'mix':
        v = n[1] + val(n[2]) / val(n[3])
        f = Fraction(v)
        return ('frac', ('num', Fraction(f.numerator), None), ('num', Fraction(f.denominator), None))
    if isinstance(n, tuple):
        return tuple(normalize_atoms(c) if isinstance(c, tuple) else c for c in n)
    return n


def has_mixed(n):
    return n[0] == 'mix' or any(has_mixed(c) for c in n[1:] if isinstance(c, tuple))


def simp_frac_node(n):
    """Reduce a lone fraction/num node to lowest terms."""
    return n


def arithmetic_steps(expr_tex):
    """Returns (steps, final Fraction) or raises ParseError."""
    ast = parse_tex(expr_tex)
    total = val(ast)
    steps = [step('given', tex(ast))]
    cur = ast
    if has_mixed(cur):
        cur = normalize_atoms(cur)
        steps.append(step('mixed', tex(cur)))
    guard = 0
    while not is_atom(cur) and guard < 40:
        guard += 1
        if contains_grp(cur):
            nxt, ch = innermost_grp_reduce(cur)
            key = 'brackets'
        else:
            lv = min(collect(cur) or {9})
            nxt = reduce_level(cur); key = {0: 'powers', 1: 'muldiv', 2: 'addsub'}.get(lv)
            if nxt == cur: break
        if nxt == cur: break
        # single-op fraction add/sub with different denominators: show the LCD form first
        steps.append(step(key, tex(nxt)))
        cur = nxt
    final = val(cur)
    # present final reduced (mixed) form
    last = tex(cur)
    steps = dedupe(steps)
    return steps, final, ast


def dedupe(steps):
    out = []
    for s in steps:
        if out and out[-1].get('m') == s.get('m'): continue
        out.append(s)
    return out


# ---------------------------------------------------------------- authored rows (DSL)
LBL = {
    'formula': ('Formula / rule:', 'کلیہ / اصول:', 'فورمول / قاعده:'),
    'subst': ('Substitute the values and calculate:', 'قیمتیں رکھ کر حساب کریں:', 'ارزښتونه کېږدئ او حساب وکړئ:'),
    'step': ('Calculate:', 'حساب کریں:', 'حساب وکړئ:'),
}


def check_chain(row):
    """row 'a = b = c': when every segment is a plain number expression, they must all agree (a rounded decimal segment
    may differ from an exact one by half a unit of its last printed digit). Returns last value or None."""
    segs = [x.strip() for x in re.split(r'(?<![<>!\\])=(?!=)', row) if x.strip()]
    vals, tols = [], []
    for sg in segs:
        try:
            vals.append(val(parse_tex(sg)))
        except Exception:
            vals.append(None); tols.append(None); continue
        m = re.fullmatch(r'-?\d[\d,]*\.(\d+)', sg)
        tols.append(Fraction(51, 100) * Fraction(1, 10 ** len(m.group(1))) if m else Fraction(0))
    known = [(v, t) for v, t in zip(vals, tols) if v is not None]
    for i in range(len(known)):
        for j in range(i + 1, len(known)):
            if abs(known[i][0] - known[j][0]) > max(known[i][1], known[j][1]):
                raise ParseError('chain mismatch: ' + row)
    return known[-1][0] if known else None
