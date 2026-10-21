"""msol_geom.py - circle / cylinder / cuboid formula solutions (exact decimal arithmetic)."""
import re
from fractions import Fraction
from msol import step, ParseError, LBL

PI = Fraction(314, 100)
B = chr(92)


def num(t):
    return Fraction(t.replace(',', ''))


def fmt(v, keep=None):
    v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    # terminating decimal?
    d = v.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    if d == 1:
        s = f'{float(v):.10f}'.rstrip('0').rstrip('.')
        return s
    return f'{float(v):.4f}'.rstrip('0').rstrip('.')


def pick(text, names):
    """first number following any of the names (radius/diameter/height/length ...)"""
    for nm in names:
        m = re.search(nm + r'\s*(?:=|of|is)?\s*([\d,]*\.?\d+)', text, re.I)
        if m:
            return num(m.group(1))
        m = re.search(r'([\d,]*\.?\d+)\s*(?:cm|m|mm|in)?\s*' + nm, text, re.I)
        if m:
            return num(m.group(1))
    return None


def unit(text):
    m = re.search(r'\b(mm|cm|m|in)\b', text)
    return m.group(1) if m else ''


def R(label, rows):
    e, u, p = LBL[label]
    return {'en': e, 'ur': u, 'ps': p, 'm': rows}


def radius_of(text):
    r = pick(text, ['radius'])
    if r is not None:
        return r, None
    d = pick(text, ['diameter'])
    if d is not None:
        return d / 2, d
    return None, None


def circumference(text):
    r, d = radius_of(text)
    if r is None:
        raise ParseError('no r')
    u = unit(text)
    if d is not None:
        c = PI * d
        rows = [f'C = \\pi d', f'C = 3.14 \\times {fmt(d)} = {fmt(c)}']
    else:
        c = 2 * PI * r
        rows = [f'C = 2 \\pi r', f'C = 2 \\times 3.14 \\times {fmt(r)} = {fmt(c)}']
    return [R('formula', rows[0]), R('subst', rows[1])], c, u


def circle_area(text):
    r, d = radius_of(text)
    if r is None:
        raise ParseError('no r')
    a = PI * r * r
    steps = []
    if d is not None:
        steps.append({'en': 'Radius = diameter ÷ 2:', 'ur': 'رداس = قطر ÷ 2:', 'ps': 'شعاع = قطر ÷ 2:', 'm': f'r = {fmt(d)} \\div 2 = {fmt(r)}'})
    steps += [R('formula', 'A = \\pi r^2'), R('subst', f'A = 3.14 \\times {fmt(r)}^2 = 3.14 \\times {fmt(r * r)} = {fmt(a)}')]
    return steps, a, unit(text)


def cyl_params(text):
    r, d = radius_of(text)
    h = pick(text, ['height', 'length', 'long'])
    if r is None or h is None:
        raise ParseError('cyl')
    return r, d, h


def cyl_volume(text):
    r, d, h = cyl_params(text)
    v = PI * r * r * h
    steps = []
    if d is not None:
        steps.append({'en': 'Radius = diameter ÷ 2:', 'ur': 'رداس = قطر ÷ 2:', 'ps': 'شعاع = قطر ÷ 2:', 'm': f'r = {fmt(d)} \\div 2 = {fmt(r)}'})
    steps += [R('formula', 'V = \\pi r^2 h'), R('subst', f'V = 3.14 \\times {fmt(r)}^2 \\times {fmt(h)} = {fmt(v)}')]
    return steps, v, unit(text)


def cyl_total(text):
    r, d, h = cyl_params(text)
    a = 2 * PI * r * (r + h)
    steps = []
    if d is not None:
        steps.append({'en': 'Radius = diameter ÷ 2:', 'ur': 'رداس = قطر ÷ 2:', 'ps': 'شعاع = قطر ÷ 2:', 'm': f'r = {fmt(d)} \\div 2 = {fmt(r)}'})
    steps += [R('formula', 'A = 2 \\pi r (r + h)'), R('subst', f'A = 2 \\times 3.14 \\times {fmt(r)} \\times ({fmt(r)} + {fmt(h)}) = {fmt(a)}')]
    return steps, a, unit(text)


def cyl_curved(text):
    r, d, h = cyl_params(text)
    a = 2 * PI * r * h
    steps = []
    if d is not None:
        steps.append({'en': 'Radius = diameter ÷ 2:', 'ur': 'رداس = قطر ÷ 2:', 'ps': 'شعاع = قطر ÷ 2:', 'm': f'r = {fmt(d)} \\div 2 = {fmt(r)}'})
    steps += [R('formula', 'A = 2 \\pi r h'), R('subst', f'A = 2 \\times 3.14 \\times {fmt(r)} \\times {fmt(h)} = {fmt(a)}')]
    return steps, a, unit(text)


def cuboid(text, kind):
    nums = re.findall(r'([\d,]*\.?\d+)', text)
    if re.search(r'cube', text, re.I) and not re.search(r'cuboid', text, re.I):
        a = num(nums[0]); l = w = h = a
    else:
        if len(nums) < 3:
            raise ParseError('cuboid')
        l, w, h = (num(x) for x in nums[:3])
    if kind == 'volume':
        v = l * w * h
        return [R('formula', 'V = l \\times w \\times h'), R('subst', f'V = {fmt(l)} \\times {fmt(w)} \\times {fmt(h)} = {fmt(v)}')], v, unit(text)
    a = 2 * (l * w + w * h + l * h)
    return [R('formula', 'A = 2(lw + wh + lh)'), R('subst', f'A = 2({fmt(l)} \\times {fmt(w)} + {fmt(w)} \\times {fmt(h)} + {fmt(l)} \\times {fmt(h)}) = {fmt(a)}')], a, unit(text)


def solve(ins, part):
    s = (ins or '').lower()
    t = part or ''
    if 'circumference' in s and ('radii' in s or 'diameters' in s or 'circle' in s):
        if 'radii' in s and not re.search('radius|diameter', t, re.I): t = 'radius ' + t
        if 'diameters' in s and not re.search('radius|diameter', t, re.I): t = 'diameter ' + t
        return circumference(t), 'circumference'
    if re.search(r'area of the circles', s):
        if not re.search('radius|diameter', t, re.I): t = 'radius ' + t
        return circle_area(t), 'area'
    if 'volume of each' in s and 'cylinder' in s:
        return cyl_volume(t), 'vol'
    if 'total surface area' in s and 'cylinder' in s:
        return cyl_total(t), 'tsa'
    if re.search(r'surface area of the following prism|volume of the following prism', s) and re.search(r'cuboid|cube', t, re.I):
        return cuboid(t, 'volume' if 'volume' in s else 'area'), 'prism'
    return None
