import warnings
warnings.filterwarnings('ignore')
"""Rasterise figure generator output for checking: svgpng.py OUT.png KIND 'SPEC' [KIND 'SPEC' ...] (stacked vertically)."""
import sys, warnings
warnings.filterwarnings('ignore')
import fitz, figs
from PIL import Image
import io
out = sys.argv[1]; args = sys.argv[2:]; ims = []
for kind, spec in zip(args[::2], args[1::2]):
    svg = getattr(figs, kind)(spec)
    if 'xmlns' not in svg:
        svg = svg.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
    doc = fitz.open(stream=svg.encode(), filetype='svg')
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
    im = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
    from PIL import ImageOps
    bb = ImageOps.invert(im).getbbox()
    ims.append(im.crop((0, 0, im.width, min(im.height, bb[3] + 10))) if bb else im)
W = max(i.width for i in ims); H = sum(i.height + 10 for i in ims)
s = Image.new('RGB', (W, H), 'white'); y = 0
for i in ims:
    s.paste(i, (0, y)); y += i.height + 10
s.save(out); print(out, s.size)
