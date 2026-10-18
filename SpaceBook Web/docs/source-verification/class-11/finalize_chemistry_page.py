"""Synchronize reviewed data, reader checks, checkpoint and the current benchmark."""
import argparse,datetime,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('page',type=int)
p.add_argument('status',choices=['verified','corrected','unresolved'])
p.add_argument('note')
p.add_argument('--issue',default='')
a=p.parse_args()
file=ROOT/f'chemistry-page-{a.page}.json'
record=json.loads(file.read_text(encoding='utf-8'))
def has_gap(value):
    if isinstance(value,dict):return bool(value.get('sourceGap')) or any(has_gap(v) for v in value.values())
    if isinstance(value,list):return any(has_gap(v) for v in value)
    return isinstance(value,str) and '[scan obscured]' in value
if a.status=='verified':
    assert not has_gap(record),'A page with unresolved source fragments cannot be verified'
    assert not a.issue,'A verified page cannot have an unresolved issue'
record['auditStatus']='verified corrected' if a.status=='verified' else ('corrected; unresolved source' if a.status=='unresolved' else 'corrected; verification pending')
record['review']={'reviewedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':a.note,'unresolved':a.issue}
file.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
subprocess.run([sys.executable,str(ROOT/'install_chemistry_page.py'),str(file)],check=True)
subprocess.run(['node',str(ROOT/'verify_chemistry_pages.cjs'),str(a.page)],check=True)
subprocess.run([sys.executable,str(ROOT/'save_chemistry_checkpoint.py'),str(a.page),a.status,a.note,'--issue',a.issue],check=True)
benchmark=ROOT/'chemistry-recovery-benchmark-20261012.json'
if benchmark.exists():
    b=json.loads(benchmark.read_text(encoding='utf-8'))
    now=datetime.datetime.now(datetime.timezone.utc)
    hours=(now-datetime.datetime.fromisoformat(b['startedAtUtc'])).total_seconds()/3600
    added=[];verified=[]
    for candidate in ROOT.glob('chemistry-page-*.json'):
        item=json.loads(candidate.read_text(encoding='utf-8'))
        n=item['source']['pdfPage']
        if n>=152:
            added.append(n)
            if item.get('auditStatus','').startswith('verified') and not has_gap(item):verified.append(n)
    b.update(measuredAtUtc=now.isoformat(),elapsedHours=hours,newImplementedPages=sorted(added),newSourceVerifiedPages=sorted(verified),newImplementedPagesPerHour=round(len(added)/hours,3),newSourceVerifiedPagesPerHour=round(len(verified)/hours,3),targetAchieved=len(verified)/hours>=400)
    benchmark.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Benchmark:',b['newImplementedPagesPerHour'],'added pages/hour;',b['newSourceVerifiedPagesPerHour'],'source-verified pages/hour.')
