"""Coded SVG graphs for Class 11 Mathematics solutions (trigonometric curves, asymptotes, marked points)."""
import math
from fractions import Fraction as F

W, H, PAD = 560, 280, 34

def pi_label(v, step):
    """Label a multiple of pi such as 3π/2, -π, 2π."""
    k = F(v / math.pi).limit_denominator(12)
    if k == 0: return '0'
    n, d = k.numerator, k.denominator
    sign = '−' if n < 0 else ''
    n = abs(n)
    num = 'π' if n == 1 else f'{n}π'
    return sign + (num if d == 1 else f'{num}/{d}')

def plot(fns, x0, x1, y0, y1, xstep=math.pi/2, ystep=1, asym=(), hlines=(), points=(), xlabels=None, title=''):
    """fns: list of (callable, colour, label). Returns an <svg> string."""
    sx = lambda x: PAD + (x - x0) / (x1 - x0) * (W - 2 * PAD)
    sy = lambda y: H - PAD - (y - y0) / (y1 - y0) * (H - 2 * PAD)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{title}" '
           f'style="width:100%;max-width:{W}px;height:auto;background:#fff;font-family:Arial,sans-serif">']
    # grid and axes
    k = math.ceil(x0 / xstep - 1e-9)
    while k * xstep <= x1 + 1e-9:
        x = k * xstep; X = sx(x)
        out.append(f'<line x1="{X:.1f}" y1="{PAD}" x2="{X:.1f}" y2="{H-PAD}" stroke="#e2e8f0" stroke-width="1"/>')
        lab = xlabels(x) if xlabels else pi_label(x, xstep)
        if abs(x) > 1e-9:
            out.append(f'<text x="{X:.1f}" y="{min(H-PAD, max(PAD, sy(0)))+14:.1f}" font-size="11" text-anchor="middle" fill="#334155">{lab}</text>')
        k += 1
    k = math.ceil(y0 / ystep - 1e-9)
    while k * ystep <= y1 + 1e-9:
        y = k * ystep; Y = sy(y)
        out.append(f'<line x1="{PAD}" y1="{Y:.1f}" x2="{W-PAD}" y2="{Y:.1f}" stroke="#e2e8f0" stroke-width="1"/>')
        if abs(y) > 1e-9:
            lab = f'{y:g}'.replace('-', '−')
            out.append(f'<text x="{min(W-PAD, max(PAD, sx(0)))-5:.1f}" y="{Y+4:.1f}" font-size="11" text-anchor="end" fill="#334155">{lab}</text>')
        k += 1
    if y0 <= 0 <= y1:
        out.append(f'<line x1="{PAD}" y1="{sy(0):.1f}" x2="{W-PAD+8}" y2="{sy(0):.1f}" stroke="#0f172a" stroke-width="1.4"/>'
                   f'<text x="{W-PAD+10}" y="{sy(0)+4:.1f}" font-size="12" fill="#0f172a">x</text>')
    if x0 <= 0 <= x1:
        out.append(f'<line x1="{sx(0):.1f}" y1="{H-PAD}" x2="{sx(0):.1f}" y2="{PAD-8}" stroke="#0f172a" stroke-width="1.4"/>'
                   f'<text x="{sx(0)+4:.1f}" y="{PAD-10}" font-size="12" fill="#0f172a">y</text>')
    for a in asym:
        out.append(f'<line x1="{sx(a):.1f}" y1="{PAD}" x2="{sx(a):.1f}" y2="{H-PAD}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4"/>')
    for c, colour in hlines:
        out.append(f'<line x1="{PAD}" y1="{sy(c):.1f}" x2="{W-PAD}" y2="{sy(c):.1f}" stroke="{colour}" stroke-width="1.6" stroke-dasharray="7 4"/>')
    # curves: sample densely, break at jumps / out of range
    for f, colour, _ in fns:
        segs, cur, n = [], [], 900
        prev = None
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n
            try: y = f(x)
            except (ZeroDivisionError, ValueError): y = None
            ok = y is not None and math.isfinite(y) and y0 - (y1 - y0) <= y <= y1 + (y1 - y0)
            if ok and prev is not None and abs(y - prev) > (y1 - y0) * 0.8: ok_jump = False
            else: ok_jump = True
            if not ok or not ok_jump:
                if len(cur) > 1: segs.append(cur)
                cur = [] if not ok else [(x, y)]
            else:
                cur.append((x, y))
            prev = y if ok else None
        if len(cur) > 1: segs.append(cur)
        for s in segs:
            pts = ' '.join(f'{sx(x):.1f},{sy(max(y0 - 0.02*(y1-y0), min(y1 + 0.02*(y1-y0), y))):.1f}' for x, y in s)
            out.append(f'<polyline points="{pts}" fill="none" stroke="{colour}" stroke-width="2.2"/>')
    for x, y, lab in points:
        out.append(f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="4" fill="#dc2626"/>')
        if lab: out.append(f'<text x="{sx(x)+5:.1f}" y="{sy(y)-7:.1f}" font-size="11" fill="#b91c1c">{lab}</text>')
    # clip strip so cut curves do not spill over the frame
    out.append(f'<rect x="0" y="0" width="{W}" height="{PAD-12}" fill="#fff"/><rect x="0" y="{H-PAD+16}" width="{W}" height="{PAD}" fill="#fff"/>')
    y_lab = 4
    for f, colour, lab in fns:
        if lab:
            out.append(f'<text x="{PAD+6}" y="{14+y_lab}" font-size="12" fill="{colour}" font-weight="700">{lab}</text>'); y_lab += 14
    out.append('</svg>')
    return ''.join(out)
