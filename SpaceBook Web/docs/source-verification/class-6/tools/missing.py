"""Show OCR words (conf>0.8) on a page that are absent from the transcription: missing.py IDX..."""
import json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parents[1] / 'math'
for a in sys.argv[1:]:
    i = int(a)
    ocr = ' '.join(l['text'] for l in json.loads((H / 'ocr' / f'{i:03}.json').read_text(encoding='utf-8'))['lines'] if l['conf'] > 0.8)
    mine = (H / 'pages' / f'p{i:03}.txt').read_text(encoding='utf-8').lower()
    mw = re.sub(r'[^a-z]', '', mine)
    miss = [w for w in re.findall(r'[a-z]{3,}', ocr.lower()) if w not in mw]
    print(i, sorted(set(miss)))
