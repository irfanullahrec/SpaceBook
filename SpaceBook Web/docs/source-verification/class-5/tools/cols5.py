"""Print an SVG structure chart: a title bar over N columns, each a header box with stacked boxes under it.

    python cols5.py "Title" "Header A:box1;box2;box3" "Header B:box1;box2" ...
Used for page transcriptions (`svg` blocks), e.g. "Structure of Federal Government".
"""
import sys
from html import escape

title, cols = sys.argv[1], [c.split(':', 1) for c in sys.argv[2:]]
n = len(cols)
cw, gap, bh = 190, 20, 44
W = n * cw + (n + 1) * gap
heads = ['#0f766e', '#4338ca', '#dc2626', '#b45309', '#7c3aed']
rows = max(len(c[1].split(';')) for c in cols)
H = 70 + 60 + rows * (bh + 14) + 20
out = [f'<rect x="{W/2-200:.0f}" y="10" width="400" height="40" rx="8" fill="#334155"/>',
       f'<text x="{W/2:.0f}" y="36" text-anchor="middle" fill="#fff" font-weight="bold" font-size="17">{escape(title)}</text>',
       f'<line x1="{gap+cw/2:.0f}" y1="64" x2="{W-gap-cw/2:.0f}" y2="64" stroke="#334155" stroke-width="3"/>',
       f'<line x1="{W/2:.0f}" y1="50" x2="{W/2:.0f}" y2="64" stroke="#334155" stroke-width="3"/>']
for i, (head, items) in enumerate(cols):
    x = gap + i * (cw + gap)
    cx = x + cw / 2
    out.append(f'<line x1="{cx:.0f}" y1="64" x2="{cx:.0f}" y2="80" stroke="#334155" stroke-width="3"/>')
    out.append(f'<rect x="{x}" y="80" width="{cw}" height="40" rx="6" fill="{heads[i % len(heads)]}"/>')
    out.append(f'<text x="{cx:.0f}" y="106" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">{escape(head)}</text>')
    y = 134
    for j, it in enumerate([s for s in items.split(';') if s]):
        out.append(f'<line x1="{cx:.0f}" y1="{y-14}" x2="{cx:.0f}" y2="{y}" stroke="#64748b" stroke-width="2"/>')
        out.append(f'<rect x="{x+10}" y="{y}" width="{cw-20}" height="{bh}" rx="6" fill="#fce7f3" stroke="#be185d"/>')
        out.append(f'<text x="{cx:.0f}" y="{y+27}" text-anchor="middle" font-size="14">{escape(it)}</text>')
        y += bh + 14
print(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n' + '\n'.join(out) + '\n</svg>')
