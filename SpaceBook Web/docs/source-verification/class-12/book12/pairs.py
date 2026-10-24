# -*- coding: utf-8 -*-
"""Boundary sheets for chosen JPG pairs:  python -X utf8 pairs.py KEY OUT.png A:B [A:B ...]
Each tile: the lower part of JPG A (above the black line) and the upper part of JPG B (below it); the page numbers are in the corners."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine


def main():
    b = engine.Book(sys.argv[1])
    out = sys.argv[2]
    pairs = [tuple(int(x) for x in a.split(':')) for a in sys.argv[3:]]
    tiles = []
    for ja, jb in pairs:
        ia = Image.open(b.jpg_path(ja)).convert('L')
        ib = Image.open(b.jpg_path(jb)).convert('L')
        w, h = ia.size
        a = ia.crop((0, int(h * 0.60), w, h))
        c = ib.crop((0, 0, ib.size[0], int(ib.size[1] * 0.40)))
        t = Image.new('L', (max(a.width, c.width), a.height + c.height + 44), 255)
        t.paste(a, (0, 22)); t.paste(c, (0, a.height + 44))
        d = ImageDraw.Draw(t)
        d.text((4, 4), f'JPG {ja} (lower part)', fill=0)
        d.text((4, a.height + 26), f'JPG {jb} (upper part)', fill=0)
        d.line((0, a.height + 42, t.width, a.height + 42), fill=0, width=2)
        tiles.append(t)
    cols = min(3, len(tiles))
    rows = (len(tiles) + cols - 1) // cols
    W, H = max(t.width for t in tiles), max(t.height for t in tiles)
    sheet = Image.new('L', (cols * (W + 8), rows * H), 128)
    for n, t in enumerate(tiles):
        sheet.paste(t, ((n % cols) * (W + 8), (n // cols) * H))
    sheet.save(out)
    print(out, sheet.size)


main()
