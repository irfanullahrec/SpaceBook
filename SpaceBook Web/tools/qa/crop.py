"""crop.py <jpg> <x0> <y0> <x1> <y1> <out.png> [scale]  : crop a region of a scan (coordinates of the displayed image) and enlarge it for reading"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]); x0, y0, x1, y1 = map(int, sys.argv[2:6]); sc = float(sys.argv[7]) if len(sys.argv) > 7 else 2
print(im.size)
c = im.crop((x0, y0, x1, y1)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS); c.save(sys.argv[6])
