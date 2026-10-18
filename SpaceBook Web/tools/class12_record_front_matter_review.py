"""Save direct visual checks for the first five source PDF pages."""
import json
from datetime import datetime
from pathlib import Path
from class12_fidelity_repair import now,update_inventory
from class12_source_review import OUT

path=OUT/'progress.json'
data=json.loads(path.read_text(encoding='utf-8'))
manifest_path=OUT/'physics-fidelity-review.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
for number in range(1,6):manifest.get('pages',{}).pop(str(number),None)
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
results={
1:('corrected_verified','PDF1 freshly rendered at150dpi and inspected. Cover title A Textbook of Physics (section heading), Grade XII, free-from-government notice, NOT FOR SALE, publisher and emblem match active coded record and translations. Collage is decorative cover art.'),
2:('excluded','PDF2 freshly rendered110dpi and inspected: third-party website/app advertisement only; no textbook lesson content.'),
3:('corrected_verified','PDF3 freshly rendered110dpi and inspected. Urdu quotation and attribution, English anti-corruption slogan, Grade-XII title and publisher match active paired records in source order; decoration excluded.'),
4:('corrected_unresolved','PDF4 freshly rendered110dpi and inspected. Publisher/NOC/credits and preface text and boundaries match active records. Two faint reviewer names remain explicitly marked unreadable; not guessed.'),
5:('corrected_verified','PDF5 freshly rendered110dpi and inspected. All12 contents entries/page numbers and printed page1 Unit11 heading, question and nine Coulomb/electrostatics outcomes match active coded/translated records; copier image is decorative context.')}
for item in data['pages']:
    if item['pdfPage'] in results:
        status,evidence=results[item['pdfPage']]
        item.update(status=status,evidence=evidence,fidelityVerifiedUtc=now())
repair=data['fidelityRepair']
repair['pendingValidation']=[]
for number in range(1,6):
    if number not in repair['completedPages']:repair['completedPages'].append(number)
repair['completedPages'].sort(key=lambda number:repair['queue'].index(number))
repair['nextPage']=6
data.update(nextPage=6,lastInspectedPage=5,
    nextAction='Freshly inspect PDF page6 in sequence; continue Physics through page201. Earlier review claims remain preserved separately; no Mathematics content inspected.',
    lastFullyVerifiedPage=max(item['pdfPage'] for item in data['pages'] if item['status'] in ('corrected_verified','verified_unchanged')))
benchmark=repair['benchmark']
benchmark['processedPages']=repair['completedPages'][:]
benchmark['verifiedPages']=[number for number in repair['completedPages'] if next(item for item in data['pages'] if item['pdfPage']==number)['status']=='corrected_verified']
benchmark['measuredUtc']=now()
elapsed=(datetime.fromisoformat(benchmark['measuredUtc'])-datetime.fromisoformat(benchmark['startedUtc'])).total_seconds()
benchmark.update(elapsedSeconds=elapsed,
    processedPagesPerHour=round(len(benchmark['processedPages'])*3600/max(1,elapsed),2),
    verifiedPagesPerHour=round(len(benchmark['verifiedPages'])*3600/max(1,elapsed),2))
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
update_inventory(data)
print('PDF1–5 recorded; page2 excluded, page4 unresolved; next PDF page6.')
