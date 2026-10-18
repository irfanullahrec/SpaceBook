"""Record an actual timed Chemistry draft batch without upgrading fidelity status."""
from class12_chemistry_opening import ROOT,OUT
from datetime import datetime,timezone
import json,hashlib,os,re,sys,xml.etree.ElementTree as ET
first,last=int(sys.argv[1]),int(sys.argv[2]);start=datetime.fromisoformat(sys.argv[3]);end=datetime.now(timezone.utc);reports=[];svgcount=0
for page in range(first,last+1):
 path=OUT/f'chemistry-pdf{page}-repair.json';audit=json.loads(path.read_text(encoding='utf-8'))
 for section in audit['sections']:
  for block in section['sourceBlocks']:
   for field in ['svg','svgUrdu','svgPashto']:
    if field not in block:continue
    node=ET.fromstring(block[field]);assert node.tag.endswith('svg')
    assert not any(x.tag.endswith('image') for x in node.iter())
    svgcount+=1
 reports.append({'pdfPage':page,'printedPages':[2*page-8,2*page-7],'status':'implemented_pending_final_comparison','checkedUtc':end.isoformat(),'artifact':path.name,'artifactSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'evidence':['Original source visually inspected during authoring.','Complete authored English/Urdu/Pashto records saved with coded figures/tables.','Focused loading, alignment, source layout, vocabulary controller and SVG structure checks passed.'],'pending':['Independent complete source-text, translation and figure-fidelity comparison.','Final browser checks and alternate companion-view review.'],'retainedSourceIssues':[x['id'] for x in audit['issues']]})
(OUT/f'chemistry-verification-pages{first}-{last}.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=OUT/'chemistry-progress.json';p=json.loads(path.read_text(encoding='utf-8'));elapsed=(end-start).total_seconds();nextpage=p['nextSequentialImplementationPdfPage']
benchmark={'windowStartUtc':start.isoformat(),'windowEndUtc':end.isoformat(),'elapsedSeconds':round(elapsed,3),'newPdfPagesSaved':list(range(first,last+1)),'pdfDraftsPerHour':round((last-first+1)*3600/elapsed,1),'wholePagesVerifiedDuringWindow':0,'verifiedPdfPagesPerHour':0,'scope':'Observed wall-clock interval: source-authored drafts saved and focused checks completed. Parallel authoring included; first page may already have been under preparation at timer start. Whole-page verification is counted separately.','targetPagesPerHour':400,'targetAchieved':False}
p['latestDraftBenchmark']=benchmark;p.setdefault('draftBenchmarks',[]).append(benchmark)
p['updatedUtc']=end.isoformat();p['pendingTasks']=[f'Continue Chemistry at PDF{nextpage}; saved implementation through{nextpage-1}.',f'Independent final source-text, translation and diagram comparison remains pending for32–{nextpage-1}; structural checks do not upgrade whole-page status.','Preserve frontmatter1/3/4, diagrams21/22/27/28, companion synchronization26 and cover figures44/53 pending items.','Review Unit14/15/16 alternate definitions, SLOs and exercise views.','Retain all printed scientific inconsistencies and ambiguity flags.','Source inspection through80 remains distinct from implementation;81–85 cached but uninspected.','Final Chemistry browser and syntax checks requested by latest user instruction.']
path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/f'chemistry-svg-structure-pages{first}-{last}.json').write_text(json.dumps({'checkedUtc':end.isoformat(),'pdfPages':list(range(first,last+1)),'parsedLanguageSvgs':svgcount,'passed':['SVG XML valid','No raster image elements'],'scope':'Structural validation only; fidelity and right-to-left rendering remain separate.'},indent=2)+'\n',encoding='utf-8')
lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,f'class12-chemistry checkpoint{last}'.encode());os.close(fd);fd=None
 index=ROOT/'index.html';text=index.read_text(encoding='utf-8');text=re.sub(r'chem12_source\d+',f'chem12_source{nextpage-1}',text);temp=index.with_name('index.html.chem12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,index)
 inventory=OUT/'inventory.json';data=json.loads(inventory.read_text(encoding='utf-8'));subject=next(s for s in data['subjects'] if s['subject']=='Chemistry');book=next(b for b in subject['pdfs'] if b['sha256']==p['sourceSha256']);book['nextImplementationPdfPage']=nextpage
 temp=inventory.with_name('inventory.json.chem12.tmp');temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(temp,inventory)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print(json.dumps({'nextPdfPage':nextpage,'languageSvgsParsed':svgcount,'draftsPerHour':benchmark['pdfDraftsPerHour'],'wholePagesVerified':0}))
