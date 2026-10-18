"""Render a two-page spread from a Class 8 PDF and split it: python tools/half.py SUBJ idx... [--dpi 200]
Writes _render/<subj><idx>R.png (right page) and ...L.png (left page). Portrait pages are saved whole as ...P.png."""
import sys, pymupdf
from PIL import Image, ImageEnhance
PDFS = {'arabic': r'D:/SpaceBook/Books/8th/8th Arabi/PDF/Arabic Book for 8 class KPTBB.pdf'}
a = sys.argv[1:]
dpi = int(a[a.index('--dpi') + 1]) if '--dpi' in a else 200
if '--dpi' in a:
    i = a.index('--dpi'); del a[i:i + 2]
subj, idxs = a[0], [int(x) for x in a[1:]]
doc = pymupdf.open(PDFS[subj])
for n in idxs:
    pix = doc[n].get_pixmap(dpi=dpi)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    im = ImageEnhance.Contrast(im).enhance(1.3)
    w, h = im.size
    if w > h:
        for tag, box in (('R', (w // 2 - 20, 0, w, h)), ('L', (0, 0, w // 2 + 20, h))):
            c = im.crop(box); c.thumbnail((1000, 1400)); c.save(f'_render/{subj}{n}{tag}.png'); print(f'_render/{subj}{n}{tag}.png')
    else:
        im.thumbnail((1000, 1400)); im.save(f'_render/{subj}{n}P.png'); print(f'_render/{subj}{n}P.png')
