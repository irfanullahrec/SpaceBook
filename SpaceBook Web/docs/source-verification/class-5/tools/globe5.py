"""Print an SVG globe showing lines of latitude or longitude.

    python globe5.py lat     -> parallels every 30 deg, equator dashed, poles labelled
    python globe5.py long    -> meridians every 30 deg, prime meridian highlighted
    python globe5.py grid    -> both (a grid), with equator and prime meridian
Used for page transcriptions (`svg` blocks).
"""
import math
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else 'lat'
W, H, cx, cy, R = 420, 380, 210, 190, 150
o = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#7dd3fc" stroke="#0c4a6e" stroke-width="2"/>']
if mode in ('lat', 'grid'):
    for d in (-60, -30, 0, 30, 60):
        y = cy - R * math.sin(math.radians(d))
        hw = R * math.cos(math.radians(d))
        dash = ' stroke-dasharray="6 4" stroke-width="2.5"' if d == 0 else ''
        o.append(f'<ellipse cx="{cx}" cy="{y:.0f}" rx="{hw:.0f}" ry="{hw*0.12:.0f}" fill="none" stroke="#111"{dash}/>')
        o.append(f'<text x="{cx-hw-6:.0f}" y="{y+4:.0f}" text-anchor="end" font-size="12">{abs(d)}°</text>')
    o.append(f'<text x="{cx+R+6}" y="{cy+4}" font-size="13" font-weight="bold">Equator</text>')
if mode in ('long', 'grid'):
    for d in (-60, -30, 0, 30, 60):
        rx = abs(R * math.sin(math.radians(d)))
        st = ' stroke="#b91c1c" stroke-width="2.5"' if d == 0 else ' stroke="#111"'
        if d == 0:
            o.append(f'<line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}"{st}/>')
        else:
            o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.0f}" ry="{R}" fill="none"{st}/>')
    if mode == 'long':
        o.append(f'<text x="{cx}" y="{cy+R+18}" text-anchor="middle" font-size="12" fill="#b91c1c">0° Prime Meridian (Greenwich)</text>')
o.append(f'<text x="{cx}" y="{cy-R-8}" text-anchor="middle" font-size="13" font-weight="bold">North Pole 90°</text>')
if mode != 'long':
    o.append(f'<text x="{cx}" y="{cy+R+18}" text-anchor="middle" font-size="13" font-weight="bold">South Pole 90°</text>')
print(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n' + '\n'.join(o) + '\n</svg>')
