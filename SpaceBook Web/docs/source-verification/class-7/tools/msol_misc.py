"""msol_misc.py - unit/time/speed conversions and mean / median / mode."""
import re
from fractions import Fraction
from msol import ParseError, LBL

B = chr(92)


def R(label, m):
    e, u, p = LBL[label]
    return {'en': e, 'ur': u, 'ps': p, 'm': m}


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m:
        d['m'] = m
    return d


def fmt(v, nd=2):
    v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    s = f'{float(v):.{nd}f}'.rstrip('0').rstrip('.')
    return s


def nums(t):
    return [Fraction(x.replace(',', '')) for x in re.findall(r'\d[\d,]*\.?\d*', t)]


# ---------------------------------------------------------------- speed
def speed_conv(ins, part):
    s = ins.lower()
    v = nums(part)
    if not v:
        raise ParseError('v')
    x = v[0]
    if 'into metres per second' in s:
        r = x * 1000 / 3600
        return [R('formula', '1 \\text{ km/h} = \\frac{1000}{3600} \\text{ m/s}'), R('subst', f'{fmt(x)} \\times \\frac{{1000}}{{3600}} = {fmt(r)}')], f'{fmt(r)} m/s', [r]
    if 'into kilometres per hour' in s:
        r = x * 3600 / 1000
        return [R('formula', '1 \\text{ m/s} = \\frac{3600}{1000} \\text{ km/h}'), R('subst', f'{fmt(x)} \\times \\frac{{3600}}{{1000}} = {fmt(r)}')], f'{fmt(r)} km/h', [r]
    if 'into centimetre per second' in s:
        r = x * 100 / 3600
        return [R('formula', '1 \\text{ m/h} = \\frac{100}{3600} \\text{ cm/s}'), R('subst', f'{fmt(x)} \\times \\frac{{100}}{{3600}} = {fmt(r)}')], f'{fmt(r)} cm/s', [r]
    if 'into metres per hour' in s:
        r = x * 3600 / 100
        return [R('formula', '1 \\text{ cm/s} = \\frac{3600}{100} \\text{ m/h}'), R('subst', f'{fmt(x)} \\times \\frac{{3600}}{{100}} = {fmt(r)}')], f'{fmt(r)} m/h', [r]
    raise ParseError('speed')


# ---------------------------------------------------------------- statistics
def stats(ins, part):
    s = ins.lower()
    data = [Fraction(x.replace(',', '')) for x in re.findall(r'\d[\d,]*\.?\d*', part)]
    if len(data) < 2:
        raise ParseError('data')
    lst = ', '.join(fmt(d) for d in data)
    if 'mean' in s:
        tot = sum(data)
        m = tot / len(data)
        return [S('Add all the values and divide by how many there are:', 'تمام قیمتیں جمع کر کے تعداد پر تقسیم کریں:', 'ټولې ارزښتونه سره جمع کړئ او په شمېر ووېشئ:', f'\\text{{Mean}} = \\frac{{\\text{{Sum}}}}{{n}} = \\frac{{{" + ".join(fmt(d) for d in data)}}}{{{len(data)}}} = \\frac{{{fmt(tot)}}}{{{len(data)}}} = {fmt(m)}')], fmt(m), [m]
    if 'median' in s:
        d2 = sorted(data)
        n = len(d2)
        if n % 2:
            med = d2[n // 2]
            mid = f'\\text{{middle value (position }} {n // 2 + 1}\\text{{)}} = {fmt(med)}'
        else:
            med = (d2[n // 2 - 1] + d2[n // 2]) / 2
            mid = f'\\frac{{{fmt(d2[n // 2 - 1])} + {fmt(d2[n // 2])}}}{{2}} = {fmt(med)}'
        return [S('Arrange in order:', 'ترتیب سے لکھیں:', 'په ترتیب ولیکئ:', ', '.join(fmt(d) for d in d2)), S('Find the middle value:', 'درمیانی قیمت معلوم کریں:', 'منځنی ارزښت ومومئ:', mid)], fmt(med), [med]
    if 'mode' in s:
        from collections import Counter
        c = Counter(data)
        top = max(c.values())
        modes = sorted(k for k, v in c.items() if v == top)
        return [S('Count how often each value occurs:', 'ہر قیمت کتنی بار آئی گنیں:', 'هر ارزښت څو ځله راغلی وشمېرئ:', ', '.join(f'{fmt(k)}: {v}' for k, v in sorted(c.items()))), S('The value(s) that occur most often:', 'سب سے زیادہ بار آنے والی قیمت:', 'تر ټولو ډېر راتلونکی ارزښت:', ' \\text{ and } '.join(fmt(m) for m in modes))], ' and '.join(fmt(m) for m in modes), modes
    raise ParseError('stat')


# ---------------------------------------------------------------- time
def time12to24(ins, part):
    m = re.search(r'(\d{1,2}):(\d{2})\s*(a\.m\.|p\.m\.)', part.replace(' ', ' '), re.I)
    return None


def solve(ins, part):
    s = ins.lower()
    t = part or ''
    if s.startswith('convert the speed'):
        return speed_conv(s, t)
    if re.match(r'find the (mean|median|mode)', s) and re.search(r'\d', t):
        return stats(s, t)
    return None


# ---------------------------------------------------------------- significant figures, spread
def sigfig(ins, part):
    from decimal import Decimal, ROUND_HALF_UP
    m = re.search(r'(\d+)\s*significant figures', ins)
    if not m:
        raise ParseError('sf')
    n = int(m.group(1))
    t = part.strip().replace(',', '')
    d = Decimal(t)
    if d == 0:
        raise ParseError('zero')
    exp = d.adjusted()                      # position of the first significant digit
    q = Decimal(1).scaleb(exp - n + 1)
    r = d.quantize(q, rounding=ROUND_HALF_UP)
    digits = re.sub(r'[^0-9]', '', t).lstrip('0')
    nxt = digits[n] if len(digits) > n else '0'
    steps = [S('Count significant figures from the first non-zero digit:', 'پہلے غیر صفر ہندسے سے بامعنی ہندسے گنیں:', 'له لومړي غیر صفر رقم څخه معنا لرونکي رقمونه وشمېرئ:', f'{t}'),
             S(f'Keep {n} significant figures; the next digit is {nxt}, so ' + ('round up.' if int(nxt) >= 5 else 'keep the last digit.'), f'{n} بامعنی ہندسے رکھیں؛ اگلا ہندسہ {nxt} ہے، اس لیے ' + ('اوپر راؤنڈ کریں۔' if int(nxt) >= 5 else 'آخری ہندسہ وہی رکھیں۔'), f'{n} معنا لرونکي رقمونه وساتئ؛ بل رقم {nxt} دی، نو ' + ('پورته ګرد کړئ.' if int(nxt) >= 5 else 'وروستی رقم هماغه وساتئ.'), f'{t} \\approx {r:f}'.replace('\\approx', '\\approx'))]
    out = f'{r:f}'
    if '.' in out and not '.' in t:
        out = out.split('.')[0]
    return steps, out, [Fraction(out)]


def spread(ins, part):
    data = [Fraction(x.replace(',', '')) for x in re.findall(r'\d[\d,]*\.?\d*', part)]
    if len(data) < 3:
        raise ParseError('data')
    n = len(data)
    mean = sum(data) / n
    ss = sum((x - mean) ** 2 for x in data)
    var = ss / n
    sd = float(var) ** 0.5
    rng = max(data) - min(data)
    steps = [S('Range = largest − smallest:', 'حد = بڑی قیمت − چھوٹی قیمت:', 'حد = لویه − کوچنۍ قیمت:', f'{fmt(max(data))} - {fmt(min(data))} = {fmt(rng)}'),
             S('Mean:', 'اوسط:', 'منځنی:', f'\\bar{{x}} = \\frac{{{fmt(sum(data))}}}{{{n}}} = {fmt(mean)}'),
             S('Variance = sum of squared deviations ÷ n:', 'تغیر = انحرافات کے مربعوں کا مجموعہ ÷ n:', 'تغیر = د انحرافاتو د مربع مجموعه ÷ n:', f'S^2 = \\frac{{{fmt(ss, 3)}}}{{{n}}} = {fmt(var)}'),
             S('Standard deviation = square root of the variance:', 'معیاری انحراف = تغیر کا جذر:', 'معیاري انحراف = د تغیر جذر:', f'S = \\sqrt{{{fmt(var)}}} = {sd:.3f}')]
    return steps, f'Range = {fmt(rng)}, S² = {fmt(var)}, S = {sd:.3f}', [rng, var, Fraction(sd).limit_denominator(1000)]


_old_solve = solve


def solve(ins, part):
    s = ins.lower()
    if 'significant figures' in s and re.fullmatch(r'\s*[\d,]*\.?\d+\s*', part or ''):
        return sigfig(ins, part)
    if s.startswith('find the range, variance'):
        return spread(ins, part)
    return _old_solve(ins, part)
