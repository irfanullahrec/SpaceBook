"""msol6.py - cubes, approximate square roots, rotation of a point, proportion with an unknown."""
import re
import math
from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction
import sympy as sp
import msol
from msol import step, ParseError

BS = chr(92)


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m is not None:
        d['m'] = m
    return d


def cube(text):
    ast = msol.parse_tex(msol.clean_tex(text))
    v = msol.val(ast)
    t = msol.tex(ast)
    c = v ** 3
    steps = [step('given', f'({t})^3'),
             S('Cube a number by multiplying it by itself three times:', 'عدد کا مکعب اسے تین بار ضرب دینے سے ملتا ہے:', 'د عدد مکعب د هغه د درې ځله ضرب څخه ترلاسه کېږي:', f'({t})^3 = {t} {BS}times {t} {BS}times {t} = {msol.tex_num(c)}')]
    return steps, c


def sqrt_approx(text, places):
    getcontext().prec = 40
    t = text.strip().strip('$').replace(',', '')
    d = Decimal(t)
    r = d.sqrt()
    q = Decimal(1).scaleb(-places)
    rr = r.quantize(q, rounding=ROUND_HALF_UP)
    lo = int(r)
    steps = [step('given', f'{BS}sqrt{{{t}}}'),
             S(f'{t} is not a perfect square: its root lies between {lo} and {lo + 1}.', f'{t} مکمل مربع نہیں: اس کا جذر {lo} اور {lo + 1} کے درمیان ہے۔', f'{t} بشپړ مربع نه دی: جذر یې د {lo} او {lo + 1} ترمنځ دی.'),
             S(f'Find the root by the division method to more decimal places, then round to {places} places:', f'تقسیم کے طریقے سے مزید اعشاریہ مقامات تک جذر نکالیں، پھر {places} مقامات تک راؤنڈ کریں:', f'د وېش په طریقه نور اعشاریه ځایونه ومومئ، بیا تر {places} ځایونو ګرد کړئ:', f'{BS}sqrt{{{t}}} = {r:.{places + 3}f}{BS}ldots {BS}approx {rr}')]
    return steps, float(rr)


def rotate(point, desc):
    x, y = point
    m = re.match(r'(\d+)°?\s*(clockwise|counterclockwise|anticlockwise)', desc.strip(), re.I)
    if not m:
        raise ParseError('rot')
    ang = int(m.group(1)); cw = m.group(2).lower() == 'clockwise'
    ccw = ang if not cw else (360 - ang) % 360
    mp = {0: (x, y), 90: (-y, x), 180: (-x, -y), 270: (y, -x)}
    nx, ny = mp[ccw]
    rule = {90: '(x, y) '+BS+'to (-y, x)', 180: '(x, y) '+BS+'to (-x, -y)', 270: '(x, y) '+BS+'to (y, -x)'}[ccw]
    steps = [step('given', f'P({x}, {y}),\; {ang}° {"clockwise" if cw else "counterclockwise"}'),
             S(f'{ang}° {"clockwise" if cw else "counterclockwise"} is the same as {ccw}° counterclockwise about the origin, with the rule:', f'{ang}° {"گھڑی کی سمت" if cw else "گھڑی کی مخالف سمت"} {ccw}° گھڑی کی مخالف سمت کے برابر ہے، قاعدہ:', f'{ang}° {"د ساعت په لور" if cw else "د ساعت پر خلاف"} د {ccw}° د ساعت پر خلاف سره برابر دی، قاعده:', rule),
             S('Substitute the coordinates:', 'محدد رکھیں:', 'همغږۍ کېږدئ:', f"P'({nx}, {ny})")]
    return steps, (nx, ny)
