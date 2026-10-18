"""Short-lock source section upserts and honest per-spread checkpoints."""
from class12_chemistry_opening import ROOT, OUT
import json, os, time
from datetime import datetime, timezone

def save(pdf_page, sections, trim=None, issues=None, carry=None, chapter_number=13):
    audit={'pdfPage':pdf_page,'chapterNumber':chapter_number,'sections':sections,'trim':trim or [],'issues':issues or [],'carry':carry or []}
    marker=f'// BEGIN CLASS12 CHEMISTRY PDF{pdf_page} SOURCE REPAIR'
    end=f'// END CLASS12 CHEMISTRY PDF{pdf_page} SOURCE REPAIR'
    block=marker+'\n{ const audit = '+json.dumps(audit,ensure_ascii=False,indent=2)+''';
const chapter=CHEM_12_DATA.find(item=>item.number===(audit.chapterNumber||13));
if(!chapter)throw new Error('Missing Chemistry XII source chapter');
for(const move of audit.carry){
 const origin=chapter.sections.find(item=>item.id===move.from),target=chapter.sections.find(item=>item.id===move.to);
 if(!origin||!target)throw new Error('Missing Chemistry XII continuation carry');
 const start=origin.theory.indexOf(move.startsAt);
 if(start<0&&!move.text)throw new Error('Missing Chemistry XII continuation carry boundary');
 const continuation=move.text||origin.theory.slice(start);
 if(!target.theory.startsWith(continuation)){target.theory=continuation+'\\n'+target.theory;target.content=target.theory.replace(/\\n/g,'<br>');target.sciNote='';}
}
for(const replacement of audit.sections){
 const destination=replacement.sourceChapterNumber?CHEM_12_DATA.find(item=>item.number===replacement.sourceChapterNumber):chapter;
 if(!destination)throw new Error('Missing Chemistry XII destination chapter');
 const index=destination.sections.findIndex(item=>item.id===replacement.id);
 if(index<0){
  if(!replacement.insertBefore)throw new Error('Missing Chemistry XII source section '+replacement.id);
  const before=destination.sections.findIndex(item=>item.id===replacement.insertBefore);
  if(before<0)throw new Error('Missing Chemistry XII source insert anchor');
  destination.sections.splice(before,0,replacement);
 }else destination.sections[index]=replacement;
}
for(const change of audit.trim){
 const owner=change.sourceChapterNumber?CHEM_12_DATA.find(item=>item.number===change.sourceChapterNumber):chapter;
 const target=owner&&owner.sections.find(item=>item.id===change.id);
 if(!target)throw new Error('Missing Chemistry XII continuation '+change.id);
 const boundary=target.theory.indexOf(change.startsAt);
 if(boundary<0)throw new Error('Missing Chemistry XII source boundary '+change.id);
 target.theory=target.theory.slice(boundary);target.content=target.theory.replace(/\\n/g,'<br>');target.sciNote='';
}
for(const owner of CHEM_12_DATA.filter(item=>item===chapter||audit.sections.some(section=>section.sourceChapterNumber===item.number))){
 owner.topics=owner.sections.map(section=>({...((owner.topics||[]).find(item=>item.id===section.id)||{}),...section}));
}
chapter.sourceIssues=[...(chapter.sourceIssues||[]).filter(issue=>!audit.issues.some(item=>item.id===issue.id)),...audit.issues];
}
'''+end+'\n'
    lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        os.write(fd,f'class12-chemistry pid={os.getpid()}\n'.encode());os.close(fd);fd=None
        path=ROOT/'js/chem_12_data.js';text=path.read_text(encoding='utf-8')
        if marker in text:
            start=text.index(marker);stop=text.index(end,start)+len(end);text=text[:start]+block+text[stop:]
        else:
            companion='// BEGIN CLASS12 CHEMISTRY SOURCE COMPANION SYNC'
            if companion in text:
                position=text.index(companion);text=text[:position].rstrip()+'\n\n'+block+'\n'+text[position:]
            else:text=text.rstrip()+'\n\n'+block
        temp=path.with_name(path.name+'.chem12.tmp');temp.write_text(text,encoding='utf-8')
        for attempt in range(6):
            try:
                os.replace(temp,path);break
            except PermissionError:
                if attempt==5:raise
                time.sleep(.15)
    finally:
        if fd is not None:os.close(fd)
        lock.unlink()
    (OUT/f'chemistry-pdf{pdf_page}-repair.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path=OUT/'chemistry-progress.json';p=json.loads(path.read_text(encoding='utf-8'))
    for entry in p['pages']:
        if entry['pdfPage']==pdf_page:
            entry['status']='implemented_pending_final_comparison'
            entry['evidence']='Source-aligned English, Urdu and Pashto section upsert saved with structured source tables/visuals where applicable. Final source/code comparison pending.'
    p['lastSavedUtc']=datetime.now(timezone.utc).isoformat()
    p['nextSequentialImplementationPdfPage']=max(pdf_page+1,p.get('nextSequentialImplementationPdfPage',1))
    p['nextImplementationPdfPage']=p['nextSequentialImplementationPdfPage']
    p['implementationSavedPdfPages']=sorted(set(p.get('implementationSavedPdfPages',[4,5,6])+[pdf_page]))
    p['pendingTasks']=[f'Continue sequential Chemistry implementation at PDF page {pdf_page+1}.',
                       'Final source comparison of implemented front matter/contents (PDF pages 1, 3 and 4) remains pending.',
                       'Run final source/code comparison on implemented spreads before marking whole pages verified.',
                       'Source inspection through 80 is distinct from implementation. Pages 81–85 are rendered but uninspected.']
    path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Chemistry PDF {pdf_page} saved; next sequential implementation {p['nextSequentialImplementationPdfPage']}.")
