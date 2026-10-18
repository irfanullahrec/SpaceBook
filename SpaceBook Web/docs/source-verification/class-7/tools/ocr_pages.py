"""Batch OCR (RapidOCR) of Class 7 single-page JPG scans; cached per page, skips done pages."""
import sys, json, time
from pathlib import Path
from rapidocr_onnxruntime import RapidOCR
src = Path(sys.argv[1]); out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
eng = RapidOCR()
t0 = time.time()
files = sorted(p for p in src.glob('[0-9][0-9][0-9].jpg'))
for f in files:
    target = out / (f.stem + '.json')
    if target.exists(): continue
    try:
        import numpy as np
        from PIL import Image
        im = Image.open(f).convert('RGB')
        if im.width > 1700:
            im = im.resize((1700, int(im.height * 1700 / im.width)))
        res, _ = eng(np.array(im)[:, :, ::-1])
    except Exception as e:
        print(f.stem, 'ERROR', e, flush=True); continue
    lines = [{'text': r[1], 'conf': round(float(r[2]), 3), 'box': [[int(x) for x in pt] for pt in r[0]]} for r in (res or [])]
    target.write_text(json.dumps({'file': str(f), 'lines': lines}, ensure_ascii=False), encoding='utf-8')
    print(f.stem, len(lines), round(time.time() - t0, 1), flush=True)
