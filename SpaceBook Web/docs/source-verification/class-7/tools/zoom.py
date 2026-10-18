"""Zoom into a Class 7 Mathematics page using the higher-resolution two-page spread PDF.

Usage: zoom.py JPGINDEX [x0 y0 x1 y1] [--dpi 200]   (fractions of the single page; default whole page)
JPG index j: odd j = left half of spread (j+3)//2, even j = right half of spread (j+2)//2 (spread 0 = cover).
"""
import sys
import fitz

PDF = r'D:/SpaceBook/Books/7th/7th MAths/PDF/Math Book for 7 class KPTBB.pdf'
args = sys.argv[1:]
dpi = 200
if '--dpi' in args:
    i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
j = int(args[0])
box = [float(x) for x in args[1:5]] if len(args) >= 5 else [0, 0, 1, 1]
k, half = ((j + 3) // 2, 0) if j % 2 else ((j + 2) // 2, 1)
doc = fitz.open(PDF)
page = doc[k]
r = page.rect
w = r.width / 2
clip = fitz.Rect(half * w + box[0] * w, box[1] * r.height, half * w + box[2] * w, box[3] * r.height)
out = f'_render/z{j:03}.png'
page.get_pixmap(dpi=dpi, clip=clip).save(out)
print(out)
