import sys
import pymupdf
from PIL import Image, ImageOps, ImageEnhance
S = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\15b92a1e-eca9-4e38-83dd-7da937d60a98\scratchpad'
page = int(sys.argv[1]); dpi = int(sys.argv[2]); name = sys.argv[3]
x0, y0, x1, y1 = [float(v) for v in sys.argv[4:8]]
d = pymupdf.open(r'D:\SpaceBook\Books\8th\8th MAths\PDF\Math Book for 8 class KPTBB.pdf')
pix = d[page].get_pixmap(dpi=dpi)
pix.save(S + '\\_full.png')
im = Image.open(S + '\\_full.png').convert('RGB')
W, H = im.size
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
c = ImageOps.autocontrast(c, cutoff=1)
c = ImageEnhance.Color(c).enhance(2.5)
c.save(S + '\\' + name)
print(S + '\\' + name, c.size)
