"""Print a radial SVG mind map: a centre ellipse with N labelled ellipses around it.

    python radial5.py "Centre" "label 1" "label 2" ...
Use "\\n" inside a label for a line break.  Used for page transcriptions (`svg` blocks).
"""
import math
import sys
from html import escape

centre, labels = sys.argv[1], sys.argv[2:]
n = max(1, len(labels))
W, H, cx, cy = 680, 440, 340, 220
rx, ry = 250, 160
fills = ['#fde68a', '#bbf7d0', '#bfdbfe', '#fbcfe8', '#ddd6fe', '#fed7aa', '#a7f3d0', '#fecaca']


def tspans(text, x, y):
    lines = text.split('\\n')
    y0 = y - 8 * (len(lines) - 1) + 5
    return ''.join(f'<text x="{x:.0f}" y="{y0 + 16 * k:.0f}" text-anchor="middle">{escape(t)}</text>' for k, t in enumerate(lines))


parts = []
for i, lab in enumerate(labels):
    a = -math.pi / 2 + 2 * math.pi * i / n
    x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="#64748b" stroke-width="2"/>')
for i, lab in enumerate(labels):
    a = -math.pi / 2 + 2 * math.pi * i / n
    x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
    parts.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="88" ry="34" fill="{fills[i % len(fills)]}" stroke="#475569"/>' + tspans(lab, x, y))
print(f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
{''.join(parts)}
<ellipse cx="{cx}" cy="{cy}" rx="85" ry="38" fill="#0f766e"/><g fill="#fff" font-weight="bold" font-size="16">{tspans(centre, cx, cy)}</g>
</svg>''')
