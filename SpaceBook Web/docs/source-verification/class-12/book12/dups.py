# -*- coding: utf-8 -*-
"""Find repeated scans: python -X utf8 dups.py KEY  -> lists JPG pairs (j, earlier) whose pictures are nearly identical."""
import sys, numpy as np
from PIL import Image
sys.path.insert(0, '.')
import engine

def main():
    b = engine.Book(sys.argv[1])
    n = len(sorted(b.cfg.JPG.glob('*.jpg')))
    small = []
    for j in range(n):
        im = Image.open(b.jpg_path(j)).convert('L').resize((40, 56), Image.BILINEAR)
        a = np.asarray(im, dtype=np.float32).ravel()
        a = (a - a.mean()) / (a.std() + 1e-6)
        small.append(a)
    out = []
    for j in range(n):
        best = (0, None)
        for k in range(max(0, j - 8), j):
            r = float(np.dot(small[j], small[k]) / len(small[j]))
            if r > best[0]:
                best = (r, k)
        if best[0] > 0.30:
            out.append((j, best[1], round(best[0], 3)))
    print('repeated scans:', out)

main()
