"""Rasterise coded SVG blocks of a unit for local visual inspection: python svg_preview.py <unit> [lang]"""
import sys, os, fitz, bio9_tools as T
unit = int(sys.argv[1]); lang = sys.argv[2] if len(sys.argv) > 2 else 'svg'
OUT = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\svgprev'
os.makedirs(OUT, exist_ok=True)
u = next(x for x in T.load_bio() if x['number'] == unit)
for s in u['sections']:
    for b in s.get('sourceBlocks', []):
        if lang in b:
            doc = fitz.open(stream=b[lang].encode('utf-8'), filetype='svg')
            f = os.path.join(OUT, f"{b['id']}-{lang}.png"); doc[0].get_pixmap(dpi=96).save(f); print(f)
