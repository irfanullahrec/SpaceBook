"""Parallel, cached OCR of rendered Mathematics scans; OCR is evidence, not verification."""
import subprocess,sys,json,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT.parents[2]
EXE=Path(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
if not EXE.is_file():raise SystemExit('OCR unavailable: '+str(EXE))
OUT=ROOT/'math/ocr';OUT.mkdir(exist_ok=True)
def process(index):
    source=APP/f'tmp/class-11/math/p{index:03}.png'
    target=OUT/f'p{index:03}.txt'
    if target.exists():return dict(scanIndex=index,cached=True)
    start=time.monotonic()
    run=subprocess.run([str(EXE),str(source),'stdout','-l','eng','--psm','3'],capture_output=True,encoding='utf-8',check=True)
    with target.open('x',encoding='utf-8') as f:f.write(run.stdout)
    return dict(scanIndex=index,cached=False,seconds=round(time.monotonic()-start,3),characters=len(run.stdout))
indices=list(map(int,sys.argv[1:]))
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(process,indices))
print(json.dumps(results))
