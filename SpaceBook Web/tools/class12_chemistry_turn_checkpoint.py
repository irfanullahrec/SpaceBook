"""Persist exact source/implementation boundary without claiming completion."""
from class12_chemistry_opening import ROOT,OUT
from datetime import datetime,timezone
import json,hashlib,os,re
now=datetime.now(timezone.utc).isoformat();reports=[]
for page in [52,53]:
 path=OUT/f'chemistry-pdf{page}-repair.json';audit=json.loads(path.read_text(encoding='utf-8'))
 reports.append({'pdfPage':page,'printedPages':[2*page-8,2*page-7],'status':'implemented_pending_final_comparison','checkedUtc':now,'artifact':path.name,'artifactSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'evidence':['Original spread inspected directly; source text and aligned Urdu/Pashto translations saved.','Focused data, layout, table, formula and multi-unit hover checks passed.'],'pending':['Final source-text/translation/alternate-view comparison.']+(['Unit16 cover molecular diagrams require coded reconstruction and review.'] if page==53 else []),'retainedSourceIssues':[x['id'] for x in audit['issues']]})
(OUT/'chemistry-verification-pages52-53.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=OUT/'chemistry-progress.json';progress=json.loads(path.read_text(encoding='utf-8'))
progress.update({'updatedUtc':now,'nextImplementationPdfPage':54,'nextSequentialImplementationPdfPage':54,'pendingTasks':['Resume implementation at PDF54 (printed100–101). Original scan inspected; nothing on54 implemented yet.','PDF54: remaining18 Unit16 outcomes, orbital/chiral graphics, introduction/types and seven hydrocarbon examples. Replace16.1; preserve16.2 continuation at Alkynes and Cycloalkynes.','Final exact-text/translation/diagram fidelity comparison32–53 remains pending; no new page marked fully verified in this execution window.','Retain pending front matter1/3/4, diagrams21/22/27/28 and companion-view synchronization26.','Review Unit14/15/16 alternate definitions/SLO/exercise views. Unit14 pre-existing worked answers/key review remain preserved.','Unit15 cover artwork44 and Unit16 cover artwork53 remain unresolved.','Keep all printed scientific issue flags. Source inspection checkpoint81 remains distinct from implementation54.']})
path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'class12 chemistry boundary54');os.close(fd);fd=None
 index=ROOT/'index.html';text=index.read_text(encoding='utf-8');text=re.sub(r'chem12_source\d+','chem12_source53',text);tmp=index.with_name('index.html.chem12.tmp');tmp.write_text(text,encoding='utf-8');os.replace(tmp,index)
 inventory=OUT/'inventory.json';data=json.loads(inventory.read_text(encoding='utf-8'));chem=next(s for s in data['subjects'] if s['subject']=='Chemistry');book=next(b for b in chem['pdfs'] if b['sha256']==progress['sourceSha256']);book['nextImplementationPdfPage']=54
 tmp=inventory.with_name('inventory.json.chem12.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(tmp,inventory)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print('Exact checkpoint saved: Chemistry next PDF54; final verification pending.')
