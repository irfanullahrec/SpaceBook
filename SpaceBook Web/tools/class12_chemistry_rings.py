"""Shared SVG helpers for Chemistry XII aromatic pages (PDF73+)."""
from html import escape
import math

class Fig:
    def __init__(self, marker):
        self.marker = marker
    def t(self, x, y, v, size=20, color='#17212b'):
        return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
    def line(self, x, y, a, b, w=2, c='#222', extra=''):
        return f'<path d="M{x:.1f} {y:.1f}L{a:.1f} {b:.1f}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
    def start(self, h, w=850):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="{self.marker}" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#222"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>')
    def arrow(self, x1, x2, y, a='', b='', size=13):
        return (self.line(x1, y, x2, y, 2, '#222', f'marker-end="url(#{self.marker})"') + (self.t((x1 + x2) / 2, y - 9, a, size) if a else '') + (self.t((x1 + x2) / 2, y + 19, b, size) if b else ''))
    def eq(self, x1, x2, y):
        m = f'marker-end="url(#{self.marker})"'
        return self.line(x1, y - 3, x2, y - 3, 2, '#222', m) + self.line(x2, y + 3, x1, y + 3, 2, '#222', m)
    def ring(self, cx, cy, r=30, circle=False, subs=None, kek=True, plus=False):
        """Hexagon, vertex 0 at top, clockwise; subs={vertex: label}."""
        pts = [(cx + r * math.sin(math.radians(60 * i)), cy - r * math.cos(math.radians(60 * i))) for i in range(6)]
        s = '<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#222" stroke-width="2"/>'
        if circle:
            s += f'<circle cx="{cx}" cy="{cy}" r="{r * .6:.1f}" fill="none" stroke="#222" stroke-width="2"/>'
        elif kek:
            for i in (0, 2, 4):
                (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 6]; k = .78
                s += self.line(cx + (x1 - cx) * k, cy + (y1 - cy) * k, cx + (x2 - cx) * k, cy + (y2 - cy) * k)
        for i, lab in (subs or {}).items():
            x, y = pts[i]; dx, dy = (x - cx) / r, (y - cy) / r
            s += self.line(x, y, x + dx * 14, y + dy * 14) + self.t(x + dx * 28, y + dy * 28 + 6, lab, 15)
        return s

def _w(tok):
    if tok in ('—', '≡', '=', '–'): return 24
    plain = ''.join(c for c in tok if c not in '₀₁₂₃₄₅₆₇₈₉⁺⁻')
    return 12.5 * len(plain) + 8

def chain(fig, x0, y, toks, size=18, num=None, up=None, down=None, center=None):
    """Lay out tokens left→right (optionally centred on `center`); num/up/down: {token_index: label}."""
    total = sum(_w(k) for k in toks)
    if center is not None: x0 = center - total / 2
    out = ''; x = x0; cent = []
    for k in toks:
        w = _w(k); cent.append(x + w / 2); out += fig.t(x + w / 2, y, k, size); x += w
    for i, n in (num or {}).items():
        out += fig.t(cent[i] + 10, y - 16, n, 11) if up and i in up else fig.t(cent[i], y - 20, n, 11)
    for i, g in (up or {}).items():
        if g.startswith('='):
            g = g[1:]; out += fig.line(cent[i] - 3, y - 34, cent[i] - 3, y - 18) + fig.line(cent[i] + 3, y - 34, cent[i] + 3, y - 18)
        else: out += fig.line(cent[i], y - 34, cent[i], y - 18)
        out += fig.t(cent[i], y - 40, g, size - 2)
    for i, g in (down or {}).items(): out += fig.line(cent[i], y + 8, cent[i], y + 24) + fig.t(cent[i], y + 42, g, size - 2)
    return out

def _lay(fig, x, y, l, r, size=16):
    toks = [k for k in (l, '—', 'C', '—', r) if k != ''] if (l or r) else ['—', 'C', '—']
    if not l and r: toks = ['—', 'C', '—', r] if False else ['C', '—', r]
    if l and not r: toks = [l, '—', 'C']
    tot = sum(_w(k) for k in toks); cx = x - tot / 2; out = ''; cc = x
    for k in toks:
        w = _w(k); out += fig.t(cx + w / 2, y, k, size)
        if k == 'C': cc = cx + w / 2
        cx += w
    return out, cc

def carbonyl(fig, x, y, l='', r='', size=16):
    """l—C(=O)—r with the O drawn above the C."""
    o, c = _lay(fig, x, y, l, r, size)
    return o + fig.t(c, y - 36, 'O', 14) + fig.line(c - 3, y - 30, c - 3, y - 15) + fig.line(c + 3, y - 30, c + 3, y - 15)

def tetra(fig, x, y, top, l, r, bot, size=16):
    o, c = _lay(fig, x, y, l, r, size)
    s = o + fig.t(c, y - 36, top, 14) + fig.line(c, y - 30, c, y - 15)
    if bot: s += fig.line(c, y + 7, c, y + 22) + fig.t(c, y + 38, bot, 14)
    return s
