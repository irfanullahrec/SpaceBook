"""crop.py NNN x0 y0 x1 y1 [scale]  -> _render/cNNN.png  (fractions 0..1 of the page)"""
import sys
from pathlib import Path
from PIL import Image
n, x0, y0, x1, y1 = sys.argv[1], *map(float, sys.argv[2:6])
sc = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
im = Image.open(rf'D:\SpaceBook\Books\8th\8th MAths\JPG\{n}.jpg')
W, H = im.size
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
out = Path(__file__).resolve().parents[1] / '_render' / f'c{n}.png'
c.save(out)
print(out)
