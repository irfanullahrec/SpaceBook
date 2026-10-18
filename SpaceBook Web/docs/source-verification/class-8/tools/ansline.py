"""ansline.py: SVG number lines for the printed answer key (beaded lines with marked points).

nl(lo, hi, step, ints, marks, pink=(), left_arrow=True, right_arrow=True, w=720)
  lo, hi  : first and last bead values;  step: bead spacing;  ints: integers labelled under the line
  marks   : [(value, 'label')] points marked with a red arrow and a label above
  pink    : values whose bead is drawn pink
"""
from fractions import Fraction


def nl(lo, hi, step, ints, marks, pink=(), left_arrow=True, right_arrow=True, w=720, title=''):
    lo, hi, step = Fraction(lo).limit_denominator(1000), Fraction(hi).limit_denominator(1000), Fraction(step).limit_denominator(1000)
    pad = 36
    span = float(hi - lo)
    sc = (w - 2 * pad) / span
    X = lambda v: pad + (float(Fraction(v).limit_denominator(1000)) - float(lo)) * sc
    y = 62
    out = []
    out.append(f'<svg viewBox="0 0 {w} 110" width="{w}" role="img" aria-label="{title}" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#0f172a">')
    x1 = X(lo) - (16 if left_arrow else 0)
    x2 = X(hi) + (16 if right_arrow else 0)
    out.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" stroke="#0f172a" stroke-width="1.6"/>')
    if left_arrow:
        out.append(f'<polygon points="{x1-2:.1f},{y} {x1+7:.1f},{y-4} {x1+7:.1f},{y+4}" fill="#0f172a"/>')
    if right_arrow:
        out.append(f'<polygon points="{x2+2:.1f},{y} {x2-7:.1f},{y-4} {x2-7:.1f},{y+4}" fill="#0f172a"/>')
    pk = {Fraction(p).limit_denominator(1000) for p in pink}
    v = lo
    while v <= hi:
        col = '#e0407a' if v in pk else '#374151'
        out.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="4.6" fill="{col}"/>')
        v += step
    for i in ints:
        out.append(f'<text x="{X(i):.1f}" y="{y+22}" text-anchor="middle">{str(i).replace("-", chr(8722))}</text>')
    for val, lab in marks:
        xm = X(val)
        out.append(f'<path d="M{xm:.1f} {y-8} l-3.5 6 h7 z" fill="#c0152b"/>')
        out.append(f'<text x="{xm:.1f}" y="{y-16}" text-anchor="middle">{lab}</text>')
    out.append('</svg>')
    return '\n'.join(out)
