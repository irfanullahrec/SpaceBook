"""Print a coded SVG mind map (centre box + 4 boxes with arrows) for page transcriptions.

    python mindmap5.py "Centre text" [ID] [top] [bottom] [left] [right]
Box labels are optional (empty boxes when omitted); use "\\n" inside a label for a second line.
"""
import sys
from html import escape

centre = sys.argv[1]
mid = sys.argv[2] if len(sys.argv) > 2 else 'mm5'
labels = (sys.argv[3:7] + ['', '', '', ''])[:4]
w = max(150, 9 * len(centre) + 30)
cx = 320
pos = {0: (320, 55), 1: (320, 365), 2: (90, 210), 3: (550, 210)}


def text(i):
    lab = labels[i]
    if not lab:
        return ''
    x, y = pos[i]
    lines = lab.split('\\n')
    y0 = y - 9 * (len(lines) - 1) + 5
    return ''.join(f'<text x="{x}" y="{y0 + 18 * k}" text-anchor="middle">{escape(t)}</text>' for k, t in enumerate(lines))


print(f'''<svg viewBox="0 0 640 420" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15">
<defs><marker id="{mid}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#166534"/></marker></defs>
<g fill="#fefce8" stroke="#b45309" stroke-width="2"><rect x="{cx - w // 2}" y="180" width="{w}" height="60" rx="10"/><rect x="230" y="20" width="180" height="70" rx="10"/><rect x="230" y="330" width="180" height="70" rx="10"/><rect x="10" y="175" width="160" height="70" rx="10"/><rect x="470" y="175" width="160" height="70" rx="10"/></g>
<g stroke="#166534" stroke-width="2.5" marker-end="url(#{mid})"><line x1="{cx}" y1="178" x2="{cx}" y2="96"/><line x1="{cx}" y1="242" x2="{cx}" y2="324"/><line x1="{cx - w // 2 - 2}" y1="210" x2="176" y2="210"/><line x1="{cx + w // 2 + 2}" y1="210" x2="464" y2="210"/></g>
<text x="{cx}" y="215" text-anchor="middle" font-weight="bold">{escape(centre)}</text>{''.join(text(i) for i in range(4))}
</svg>''')
