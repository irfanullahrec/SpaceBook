"""Install + verify + checkpoint a Mutalia-e-Quran Hakeem (Compulsory) scan page. Usage: finalize_eng_page.py N status "scope note" [--issue text]"""
import argparse,datetime,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('page',type=int)
p.add_argument('status',choices=['verified','corrected','unresolved'])
p.add_argument('note')
p.add_argument('--issue',default='')
a=p.parse_args()
file=ROOT/f'mq-page-{a.page}.json'
record=json.loads(file.read_text(encoding='utf-8'))
record['auditStatus']='verified corrected' if a.status=='verified' else ('corrected; unresolved source' if a.status=='unresolved' else 'corrected; verification pending')
record['review']={'reviewedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':a.note,'unresolved':a.issue}
file.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
subprocess.run([sys.executable,str(ROOT/'install_mq_page.py'),str(file)],check=True)
subprocess.run(['node',str(ROOT/'verify_mq_pages.cjs'),str(a.page)],check=True)
prog=ROOT/'mq-progress.json'
j=json.loads(prog.read_text(encoding='utf-8')) if prog.exists() else {'book':'Mutalia-e-Quran Hakeem (Compulsory) 11 (193 scans)','pages':{}}
j['pages'][str(a.page)]={'status':a.status,'printedPage':record['source']['printedPage'],'scope':a.note,'unresolved':a.issue}
j['nextScan']=max(j.get('nextScan',1),a.page+1)
prog.write_text(json.dumps(j,ensure_ascii=False,indent=1),encoding='utf-8')
print('Checkpoint saved: scan',a.page,a.status,'next',j['nextScan'])
