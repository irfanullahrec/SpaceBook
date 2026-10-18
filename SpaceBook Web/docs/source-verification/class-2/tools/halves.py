"""Split two-page spread scans into right/left halves (book reading order: right page first) and upscale for reading.

    python halves.py SUBJ OUTDIR idx [idx ...] [--scale 2]

Writes OUTDIR/hNNN_R.png (right page) and OUTDIR/hNNN_L.png (left page)."""
import sys
from pathlib import Path
from PIL import Image

args = sys.argv[1:]
scale = 2.0
if '--scale' in args:
    i = args.index('--scale')
    scale = float(args[i + 1])
    del args[i:i + 2]
subj, out, *idxs = args
out = Path(out)
out.mkdir(parents=True, exist_ok=True)
for s in idxs:
    n = int(s)
    im = Image.open(f'D:/SpaceBook/_cls2_jpg/{subj}/{n:03}.jpg').convert('RGB')
    w, h = im.size
    for tag, box in (('R', (w // 2 - 8, 0, w, h)), ('L', (0, 0, w // 2 + 8, h))):
        part = im.crop(box)
        part = part.resize((int(part.width * scale), int(part.height * scale)), Image.LANCZOS)
        p = out / f'h{n:03}_{tag}.png'
        part.save(p)
        print(p)
