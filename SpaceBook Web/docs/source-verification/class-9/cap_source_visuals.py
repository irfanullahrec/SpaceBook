import os
from pathlib import Path
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 app=ROOT/'js/app.js';t=app.read_text(encoding='utf-8')
 old='style="width:${width}%;max-width:100%;margin:.5rem auto;"'
 new='style="width:${width}%;max-width:min(100%,${Math.round(520 * width / 100)}px);margin:.5rem auto;"'
 if old not in t:raise ValueError('Sizing wrapper changed; inspect first')
 app.write_text(t.replace(old,new,1),encoding='utf-8')
 data=ROOT/'js/data_phys.js';t=data.read_text(encoding='utf-8')
 old='if (chapter.sourceReview.complete) chapter.pageRange ='
 new='if (freshReviewed.length === reviewed.length && freshReviewed.some(page => page.chapterEnd)) chapter.pageRange ='
 if old not in t:raise ValueError('Review range clause changed')
 data.write_text(t.replace(old,new,1),encoding='utf-8')
finally:
 os.close(fd);lock.unlink()
