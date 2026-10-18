"""Preview a figure module: python figsheet.py <module> <out> [langs]"""
import sys, os, importlib, fitz
from PIL import Image
O = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\svgprev'
m = importlib.import_module(sys.argv[1]); langs = (sys.argv[3] if len(sys.argv) > 3 else 'en,ur').split(',')
ims = []
for k in m.FN:
    for lg in langs:
        d = fitz.open(stream=m.FN[k](m.FIG[k][lg]).encode(), filetype='svg'); p = d[0].get_pixmap(dpi=50)
        ims.append(Image.frombytes('RGB', (p.width, p.height), p.samples))
cols = len(langs); cw = max(i.width for i in ims); ch = max(i.height for i in ims)
sh = Image.new('RGB', (cw * cols, ch * ((len(ims) + cols - 1) // cols)), 'white')
for i, im in enumerate(ims): sh.paste(im, ((i % cols) * cw, (i // cols) * ch))
f = os.path.join(O, sys.argv[2] + '.png'); sh.save(f); print(f)
