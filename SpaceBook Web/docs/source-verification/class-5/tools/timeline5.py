"""Print an SVG timeline with events alternating above and below a horizontal line.

    python timeline5.py "Title" "776 BC:Origin of first\\nOlympic games" "490 BC:..." ...
Events are drawn left to right in the order given.  Used for page transcriptions (`svg` blocks).
"""
import sys
from html import escape

title, evs = sys.argv[1], [e.split(':', 1) for e in sys.argv[2:]]
n = len(evs)
W, H, mid = 660, 320, 160
step = (W - 80) / max(1, n - 1)
out = [f'<text x="{W/2:.0f}" y="24" text-anchor="middle" font-weight="bold" font-size="17">{escape(title)}</text>',
       f'<line x1="30" y1="{mid}" x2="{W-30}" y2="{mid}" stroke="#be123c" stroke-width="3"/>']
for i, (date, text) in enumerate(evs):
    x = 40 + i * step
    up = i % 2 == 0
    by = 40 if up else mid + 30
    out.append(f'<line x1="{x:.0f}" y1="{mid}" x2="{x:.0f}" y2="{by + (90 if up else 0)}" stroke="#be123c" stroke-width="2"/>')
    out.append(f'<circle cx="{x:.0f}" cy="{mid}" r="6" fill="#be123c"/>')
    out.append(f'<rect x="{x-62:.0f}" y="{by}" width="124" height="90" rx="8" fill="#fef3c7" stroke="#b45309"/>')
    out.append(f'<text x="{x:.0f}" y="{by+20}" text-anchor="middle" font-weight="bold" font-size="14">{escape(date)}</text>')
    for k, t in enumerate(text.split('\\n')):
        out.append(f'<text x="{x:.0f}" y="{by+40+16*k}" text-anchor="middle" font-size="12">{escape(t)}</text>')
print(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n' + '\n'.join(out) + '\n</svg>')
