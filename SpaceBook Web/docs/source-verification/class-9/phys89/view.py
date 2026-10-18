"""Render physics PDF pages to JPEG in scratchpad: python view.py 202 203 ... (pdf page numbers, 1-based)"""
import sys, fitz
SRC = r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf'
OUT = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\ph'
import os; os.makedirs(OUT, exist_ok=True)
d = fitz.open(SRC)
for a in sys.argv[1:]:
    n = int(a)
    pix = d[n - 1].get_pixmap(dpi=110)
    pix.save(f'{OUT}/p{n:03d}.jpg', jpg_quality=78)
print('ok')
