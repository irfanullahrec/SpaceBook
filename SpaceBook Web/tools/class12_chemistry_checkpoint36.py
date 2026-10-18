"""Save five-page draft comparison evidence without asserting final verification."""
from class12_chemistry_opening import ROOT,OUT
from datetime import datetime,timezone
import json,hashlib,os,re
now=datetime.now(timezone.utc).isoformat()
reports=[]
for page in range(32,37):
 path=OUT/f'chemistry-pdf{page}-repair.json';audit=json.loads(path.read_text(encoding='utf-8'))
 reports.append({'pdfPage':page,'printedPages':[page*2-8,page*2-7],'status':'implemented_pending_final_comparison','checkedUtc':now,'artifact':path.name,'artifactSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'evidence':['Original cached source spread inspected directly. Printed text, tables, formulas and aligned Urdu/Pashto paragraphs implemented.','Focused Chemistry data/layout/formula/hover checks passed. This does not establish whole-page visual fidelity.'],'pending':['Final exact-text and three-language figure comparison; SVG typography and geometry review.' if page<36 else 'Final exact-text and translation comparison; scientific source issues remain flagged.'],'retainedSourceIssues':[i['id'] for i in audit['issues']]})
(OUT/'chemistry-verification-pages32-36.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=OUT/'chemistry-progress.json';progress=json.loads(p.read_text(encoding='utf-8'))
progress.update({'nextImplementationPdfPage':37,'nextSequentialImplementationPdfPage':37,'updatedUtc':now,'pendingTasks':['Continue source implementation at PDF37 (printed66–67).','Final comparison of32–36; geometry and translated SVG typography are not verified.','Retain pending front matter1/3/4, diagrams21/22/27/28 and companion-view synchronization26.','Review retained printed scientific inconsistencies separately without changing source text.']})
start=datetime.fromisoformat('2026-10-11T19:35:16.785+00:00');end=datetime.fromisoformat('2026-10-11T19:46:26.598+00:00');seconds=(end-start).total_seconds()
progress['latestDraftBenchmark']={'windowStartUtc':start.isoformat(),'windowEndUtc':end.isoformat(),'elapsedSeconds':seconds,'newPdfPagesSaved':[34,35,36],'pdfDraftsPerHour':round(3*3600/seconds,1),'wholePagesVerifiedDuringWindow':0,'scope':'Actual interval after PDF33 focused validation through PDF36 validation. Three source/translation drafts; final comparison remains pending.','targetPagesPerHour':400,'targetAchieved':False}
p.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'class12 chemistry checkpoint36');os.close(fd);fd=None
 index=ROOT/'index.html';text=index.read_text(encoding='utf-8');text=re.sub(r'chem12_source\d+','chem12_source36',text);tmp=index.with_name('index.html.chem12.tmp');tmp.write_text(text,encoding='utf-8');os.replace(tmp,index)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print('Five-page evidence saved. Next37. Draft rate',progress['latestDraftBenchmark']['pdfDraftsPerHour'])
