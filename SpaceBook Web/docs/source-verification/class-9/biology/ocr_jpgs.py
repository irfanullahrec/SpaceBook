"""OCR the separate JPG photo set (downscaled) into jpgocr/jpg-NNN.json to locate alternate copies of pages."""
import os, json, sys
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
JD = r'D:\SpaceBook\Books\9th\9th Biology\JPG'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jpgocr'); os.makedirs(OUT, exist_ok=True)
TMP = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\jpgtmp.png'
ocr = RapidOCR()
for n in range(1, 226):
    out = os.path.join(OUT, f'jpg-{n:03d}.json')
    if os.path.exists(out): continue
    im = Image.open(os.path.join(JD, f'CS Sign 09-26-2026 16.17 (1)(1)_{n}.jpg')).convert('L')
    im.thumbnail((1100, 1600)); im.save(TMP)
    res, _ = ocr(TMP)
    json.dump({'jpg': n, 'lines': [r[1] for r in (res or [])]}, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(n, flush=True)
