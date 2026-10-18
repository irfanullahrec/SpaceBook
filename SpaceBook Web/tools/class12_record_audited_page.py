"""Save one or more pages inspected against their original spread."""
import json,sys
from datetime import datetime
from pathlib import Path
from class12_fidelity_repair import now,update_inventory
from class12_source_review import OUT
pages=[int(arg) for arg in sys.argv[1:]]
progress_path=OUT/'progress.json'
data=json.loads(progress_path.read_text(encoding='utf-8'))
repair=data['fidelityRepair']
claims={
6:('corrected_unresolved','Rendered PDF6 at150dpi and visually inspected printed2–3. All21 continuing unit outcomes plus closing unit-purpose paragraph match the paired text. Coulomb introduction, q=ne, capacitance transition, law statement, figure11.1 similar/opposite-force diagrams and figure11.2/Coulomb biography are active; diagrams are coded SVG and translated. The source biographical paragraph visibly clips Coulom/Coulomb wording at the right crop and its end; missing letters are marked, not guessed.',[
'Printed-page3 Coulomb biography has visibly clipped right-edge and ending text (“Coulom…”, “Frenc…”, “th…”). Alternative local scan retains the same clipping; exact missing text cannot be recovered.'
])}
for number in pages:
    status,evidence,issues=claims[number]
    entry=next(item for item in data['pages'] if item['pdfPage']==number)
    entry.update(status=status,evidence=evidence,fidelityVerifiedUtc=now())
    for issue in issues:
        record={'pdfPage':number,'issue':issue}
        if record not in data['unresolvedItems']:data['unresolvedItems'].append(record)
    if number not in repair['completedPages']:repair['completedPages'].append(number)
repair['completedPages'].sort(key=lambda n:repair['queue'].index(n))
repair['pendingValidation']=[]
pending=[number for number in repair['queue'] if number not in repair['completedPages']]
repair['nextPage']=pending[0] if pending else None
data.update(nextPage=repair['nextPage'] or 202,lastInspectedPage=max(data.get('lastInspectedPage',0),max(pages)),
    lastFullyVerifiedPage=max(item['pdfPage'] for item in data['pages'] if item['status'] in ('corrected_verified','verified_unchanged')),
    nextAction=f"Render and inspect PDF{repair['nextPage']} in sequence against the active lesson and all coded visuals. Physics remains incomplete.")
benchmark=repair['benchmark']
benchmark['processedPages']=repair['completedPages'][:]
benchmark['verifiedPages']=[n for n in repair['completedPages'] if next(x for x in data['pages'] if x['pdfPage']==n)['status']=='corrected_verified']
benchmark['measuredUtc']=now()
elapsed=(datetime.fromisoformat(benchmark['measuredUtc'])-datetime.fromisoformat(benchmark['startedUtc'])).total_seconds()
benchmark.update(elapsedSeconds=elapsed,processedPagesPerHour=round(len(benchmark['processedPages'])*3600/max(elapsed,1),2),verifiedPagesPerHour=round(len(benchmark['verifiedPages'])*3600/max(elapsed,1),2))
progress_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
update_inventory(data)
print(f"Saved PDF{','.join(map(str,pages))}; next PDF{repair['nextPage']}.")
