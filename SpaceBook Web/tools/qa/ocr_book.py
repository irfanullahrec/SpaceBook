"""OCR every scan page of a book with RapidOCR (local, offline) for the proofreading triage.

    python tools/qa/ocr_book.py "<Books/12th/12th Biology/JPG>" <outdir> [start] [end]

Page N = the N-th JPG in sorted file-name order (the scan folders hold one JPG per PDF page; names are not numbered consecutively
for books made from several source files). Writes <outdir>/p<NNN>.txt (one recognised line per row) and a names.json map
{page: file name}. Resumable: pages with an output file are skipped.
"""
import sys, os, json, time
from rapidocr_onnxruntime import RapidOCR

src, out = sys.argv[1], sys.argv[2]
start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
files = sorted(f for f in os.listdir(src) if f.lower().endswith('.jpg'))
end = int(sys.argv[4]) if len(sys.argv) > 4 else len(files)
os.makedirs(out, exist_ok=True)
json.dump({i + 1: f for i, f in enumerate(files)}, open(os.path.join(out, 'names.json'), 'w', encoding='utf8'), ensure_ascii=False)
ocr = RapidOCR()
t0 = time.time(); n = 0
for i in range(start, end + 1):
    dst = os.path.join(out, 'p%03d.txt' % i)
    if os.path.exists(dst): continue
    try:
        res, _ = ocr(os.path.join(src, files[i - 1]))
    except Exception as e:
        res = None
    lines = []
    for r in (res or []):
        box = r[0]; y = sum(p[1] for p in box) / 4; x = min(p[0] for p in box)
        lines.append((round(y / 12), x, r[1]))
    lines.sort()
    open(dst, 'w', encoding='utf8').write('\n'.join(l[2] for l in lines))
    n += 1
    if n % 20 == 0: print(i, 'pages', n, 'secs/page', round((time.time() - t0) / n, 1), flush=True)
print('done', src, flush=True)
