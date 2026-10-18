"""Batch37–41 checkpoint; no unchecked page is marked verified."""
from class12_chemistry_opening import ROOT,OUT
from datetime import datetime,timezone
import json,hashlib,os,re,sys
last=int(sys.argv[1]) if len(sys.argv)>1 else 41
first=last-4
now=datetime.now(timezone.utc).isoformat();reports=[]
for page in range(first,last+1):
 path=OUT/f'chemistry-pdf{page}-repair.json';audit=json.loads(path.read_text(encoding='utf-8'))
 reports.append({'pdfPage':page,'printedPages':[page*2-8,page*2-7],'status':'implemented_pending_final_comparison','checkedUtc':now,'artifact':path.name,'artifactSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'evidence':['Original cached source spread directly inspected; paragraphs, equations and aligned Urdu/Pashto translations saved.','Focused Chemistry data/layout/formula/hover checks passed; original continuation carried forward before legacy record replacement.'],'pending':['Final exact-text/translation comparison.','Source geometry and translated SVG review where figures occur.'],'retainedSourceIssues':[x['id'] for x in audit['issues']]})
(OUT/f'chemistry-verification-pages{first}-{last}.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=OUT/'chemistry-progress.json';progress=json.loads(p.read_text(encoding='utf-8'));progress['updatedUtc']=now
progress['pendingTasks']=[f'Continue source implementation at PDF{last+1} (printed{2*(last+1)-8}–{2*(last+1)-7}).',f'Final exact-text, translations and figure comparison32–{last}; these are drafts, not fully verified pages.','Retain pending front matter1/3/4, diagrams21/22/27/28 and companion-view synchronization26.','Unit14 alternate exercise/SLO/definition views still need comparison; existing solved answers and key review preserved.','Unit15 cover molecule artwork44 unresolved.','Review retained printed scientific inconsistencies separately without silently changing the textbook.']
times={41:('2026-10-11T19:47:35.762+00:00','2026-10-11T19:59:09.520+00:00'),46:('2026-10-11T19:59:09.520+00:00','2026-10-11T20:09:53.583+00:00'),51:('2026-10-11T20:09:53.583+00:00','2026-10-11T20:25:43.588+00:00')}
start,end=[datetime.fromisoformat(t) for t in times[last]];seconds=(end-start).total_seconds()
progress['latestDraftBenchmark']={'windowStartUtc':start.isoformat(),'windowEndUtc':end.isoformat(),'elapsedSeconds':seconds,'newPdfPagesSaved':list(range(first,last+1)),'pdfDraftsPerHour':round(5*3600/seconds,1),'wholePagesVerifiedDuringWindow':0,'scope':f'Actual recorded focused-check interval through PDF{last} validation. Five source/translation drafts, including checkpoint work; final fidelity comparison remains pending.','targetPagesPerHour':400,'targetAchieved':False}
p.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'class12 chemistry checkpoint41');os.close(fd);fd=None
 index=ROOT/'index.html';text=index.read_text(encoding='utf-8');text=re.sub(r'chem12_source\d+',f'chem12_source{last}',text);tmp=index.with_name('index.html.chem12.tmp');tmp.write_text(text,encoding='utf-8');os.replace(tmp,index)
 inventory=OUT/'inventory.json';data=json.loads(inventory.read_text(encoding='utf-8'))
 subject=next(s for s in data['subjects'] if s['subject']=='Chemistry');book=next(b for b in subject['pdfs'] if b['sha256']==progress['sourceSha256'])
 book.update({'nextImplementationPdfPage':last+1,'fullyVerifiedPages':progress['fullyVerifiedPdfPages'],'fullyVerifiedPdfPages':progress['fullyVerifiedPdfPages'],'correctedPdfPages':progress['correctedPdfPages'],'lastFullyVerifiedPdfPage':progress['lastFullyVerifiedPdfPage']})
 tmp=inventory.with_name('inventory.json.chem12.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(tmp,inventory)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print(f'Checkpoint{last} saved; next{last+1}; measured draft rate',progress['latestDraftBenchmark']['pdfDraftsPerHour'])
