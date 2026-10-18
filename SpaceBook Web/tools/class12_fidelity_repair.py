"""Durable source-fidelity corrections, separate from the structural audit."""
from datetime import datetime, timezone
import hashlib
import json
from class12_source_review import OUT, ROOT

def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')

def save(path, data):
    temp = path.with_suffix(path.suffix + '.new')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)

def begin():
    path = OUT / 'progress.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('fidelityRepair'):
        return
    # Preserve the earlier evidence; its structural PASS did not prove verbatim fidelity.
    queue = list(range(189, 199)) + [200, 201] + list(range(182, 189))
    for page in data['pages']:
        if page['pdfPage'] in queue:
            page['priorReview'] = {key: page.get(key) for key in ('status', 'evidence')}
            page['status'] = 'pending_source_fidelity_review'
            page['evidence'] = 'Earlier implementation contains shortened prose or incomplete source structures. Earlier structural validation is retained in priorReview, but source fidelity requires repair.'
    data['fidelityRepair'] = {
        'startedUtc': now(), 'queue': queue, 'completedPages': [],
        'reason': 'Full source paragraphs, source typography/errors, structured tables, complete SVG labels and translated headings were not reliably preserved in recent records.',
        'nextPage': 189,
        'earlierCoverage': 'Pages before 182 retain their existing review records; this repair does not newly certify them.',
        'benchmark': {'startedUtc': now(), 'verifiedPages': [], 'processedPages': []}
    }
    data.update(phase='source_fidelity_repair', nextPage=189,
                lastFullyVerifiedPage=max(p['pdfPage'] for p in data['pages'] if p['status'] in ('corrected_verified', 'verified_unchanged')),
                nextAction='Repair PDF page 189 against the source; continue 190–201, then repair the identified source mismatches on 182–188. Keep printed calculation flags. Do not switch books until fidelity and split coverage are resolved.')
    save(path, data)

    update_inventory(data)

def update_inventory(progress):
    path = OUT / 'inventory.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    physics = next(s for s in data['subjects'] if s['subject'] == 'Physics')
    primary = next(p for p in physics['pdfs'] if p['sourcePath'] == progress['sourcePdf'])
    primary.update(reviewStatus='in_progress_incomplete', nextPage=progress['nextPage'],
                   lastFullyVerifiedPage=progress['lastFullyVerifiedPage'],
                   fidelityPendingPages=[p['pdfPage'] for p in progress['pages'] if p['status'] in ('pending_source_fidelity_review','implemented_pending_fidelity_checks')],
                   verifiedUnchangedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='verified_unchanged'],
                   correctedPages=[p['pdfPage'] for p in progress['pages'] if p['status'].startswith('corrected')],
                   correctedVerifiedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='corrected_verified'],
                   excludedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='excluded'],
                   unresolvedPages=sorted({p['pdfPage'] for p in progress['unresolvedItems']}))
    save(path, data)

def extend_queue(pages, reason):
    path=OUT/'progress.json'
    progress=json.loads(path.read_text(encoding='utf-8'))
    repair=progress['fidelityRepair']
    added=[]
    for page in pages:
        if page in repair['queue']: continue
        entry=next(item for item in progress['pages'] if item['pdfPage']==page)
        entry.setdefault('priorReview', {key:entry.get(key) for key in ('status','evidence')})
        entry.update(status='pending_source_fidelity_review',evidence=reason)
        repair['queue'].append(page);added.append(page)
    if added: repair.setdefault('scopeExtensions',[]).append({'pages':added,'reason':reason,'recordedUtc':now()})
    pending=[p for p in repair['queue'] if p not in repair['completedPages'] and p not in repair.get('pendingValidation',[])]
    repair['nextPage']=pending[0] if pending else None
    progress['nextPage']=repair['nextPage'] or 202
    progress['nextAction']=f"Continue source-fidelity repair at PDF{progress['nextPage']}; pending checks {repair.get('pendingValidation',[])}. Physics remains incomplete."
    save(path,progress);update_inventory(progress)


def stage_reference(page, record, evidence, issues=None, additional_records=None):
    path = OUT / 'physics-fidelity-review.json'
    data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'method': 'Source image visually transcribed and checked; exact saved paragraph comparison guards later data changes. Structural checks are separate.', 'pages': {}}
    data['pages'][str(page)] = {'recordId': record['id'], 'paragraphs': record['paragraphs'],
        'sha256': hashlib.sha256('\n'.join(record['paragraphs']).encode('utf-8')).hexdigest(),
        'sourceInspection': evidence, 'issues': issues or [], 'stagedUtc': now(),
        'status': 'implemented_pending_checks'}
    if additional_records:
        data['pages'][str(page)]['additionalRecords']=[{'recordId':item['id'],'paragraphs':item['paragraphs'],'sha256':hashlib.sha256('\n'.join(item['paragraphs']).encode('utf-8')).hexdigest()} for item in additional_records]
    save(path, data)
    progress_path=OUT/'progress.json'
    progress=json.loads(progress_path.read_text(encoding='utf-8'))
    entry=next(item for item in progress['pages'] if item['pdfPage']==page)
    entry.update(status='implemented_pending_fidelity_checks',evidence=evidence)
    repair=progress['fidelityRepair']
    staged=sorted(int(number) for number,item in data['pages'].items() if item['status']=='implemented_pending_checks')
    repair['pendingValidation']=staged
    pending=[number for number in repair['queue'] if number not in repair['completedPages'] and number not in staged]
    repair['nextPage']=pending[0] if pending else None
    progress['nextPage']=repair['nextPage'] or 202
    progress['nextAction']=f"Validate saved fidelity repairs {staged} at the five-page boundary; continue transcription at PDF{progress['nextPage']}. Pending pages are not verified."
    save(progress_path,progress)
    update_inventory(progress)

def confirm(page, checks):
    path = OUT / 'physics-fidelity-review.json'
    refs = json.loads(path.read_text(encoding='utf-8'))
    reference = refs['pages'][str(page)]
    reference.update(status='corrected_unresolved' if reference['issues'] else 'corrected_verified',
                     verifiedUtc=now(), checks=checks)
    save(path, refs)
    path = OUT / 'progress.json'
    progress = json.loads(path.read_text(encoding='utf-8'))
    entry = next(p for p in progress['pages'] if p['pdfPage'] == page)
    entry.update(status=reference['status'], evidence=reference['sourceInspection'],
                 fidelityChecks=checks, fidelityVerifiedUtc=reference['verifiedUtc'])
    repair = progress['fidelityRepair']
    if page not in repair['completedPages']:
        repair['completedPages'].append(page)
    repair['pendingValidation']=[int(number) for number,item in refs['pages'].items() if item['status']=='implemented_pending_checks']
    pending = [p for p in repair['queue'] if p not in repair['completedPages'] and p not in repair['pendingValidation']]
    repair['nextPage'] = pending[0] if pending else None
    progress['nextPage'] = repair['nextPage'] or 202
    progress['lastFullyVerifiedPage'] = max(p['pdfPage'] for p in progress['pages'] if p['status'] in ('corrected_verified','verified_unchanged'))
    progress['nextAction'] = f"Continue source-fidelity repair at PDF page {progress['nextPage']}. Inspect every paragraph, figure and table; preserve printed defects and previous calculation flags. Physics remains incomplete."
    for issue in reference['issues']:
        item = {'pdfPage': page, 'issue': issue}
        if item not in progress['unresolvedItems']:
            progress['unresolvedItems'].append(item)
    benchmark = repair['benchmark']
    benchmark['processedPages'] = repair['completedPages'][:]
    benchmark['verifiedPages'] = [p for p in repair['completedPages'] if next(x for x in progress['pages'] if x['pdfPage']==p)['status']=='corrected_verified']
    benchmark['measuredUtc'] = now()
    elapsed = (datetime.fromisoformat(benchmark['measuredUtc'])-datetime.fromisoformat(benchmark['startedUtc'])).total_seconds()
    benchmark.update(elapsedSeconds=elapsed, verifiedPagesPerHour=round(len(benchmark['verifiedPages'])*3600/max(1,elapsed),2),
                     processedPagesPerHour=round(len(benchmark['processedPages'])*3600/max(1,elapsed),2),
                     scope='Wall-clock source-fidelity repair, including rendering, transcription, translations, coded figures and checks; unresolved pages excluded from verified rate.')
    save(path, progress)
    update_inventory(progress)

if __name__ == '__main__':
    begin()
    print('Fidelity repair checkpoint saved; next PDF page 189 unless already advanced.')
