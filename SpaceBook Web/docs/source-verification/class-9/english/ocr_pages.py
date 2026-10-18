"""Cache OCR for every page of the Class 9 English primary PDF.
Usage: python ocr_pages.py [start] [end]
Writes ocr/page-NNN.json with lines sorted top-to-bottom, left-to-right."""
import fitz, os, sys, json, time
from rapidocr_onnxruntime import RapidOCR
SRC=r'D:\SpaceBook\Books\9th\9th English\PDF\9th English.pdf'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'ocr')
VIEW=r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\eng_view'
os.makedirs(OUT,exist_ok=True); os.makedirs(VIEW,exist_ok=True)
start=int(sys.argv[1]) if len(sys.argv)>1 else 1
end=int(sys.argv[2]) if len(sys.argv)>2 else 165
d=fitz.open(SRC)
ocr=RapidOCR()
for n in range(start,end+1):
    out=os.path.join(OUT,f'page-{n:03d}.json')
    view=os.path.join(VIEW,f'p{n:03d}.png')
    if not os.path.exists(view):
        d[n-1].get_pixmap(dpi=110).save(view)
    if os.path.exists(out): continue
    t=time.time()
    tmp=os.path.join(VIEW,f'ocr_{n:03d}.png')
    d[n-1].get_pixmap(dpi=200).save(tmp)
    res,_=ocr(tmp)
    lines=[]
    for box,text,conf in (res or []):
        xs=[p[0] for p in box]; ys=[p[1] for p in box]
        lines.append({'x':round(min(xs)),'y':round(min(ys)),'w':round(max(xs)-min(xs)),'h':round(max(ys)-min(ys)),'text':text,'conf':round(float(conf),3)})
    lines.sort(key=lambda l:(round(l['y']/18),l['x']))
    json.dump({'pdfPage':n,'source':SRC,'dpi':200,'lines':lines},open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
    os.remove(tmp)
    print(n,len(lines),round(time.time()-t,1),flush=True)
