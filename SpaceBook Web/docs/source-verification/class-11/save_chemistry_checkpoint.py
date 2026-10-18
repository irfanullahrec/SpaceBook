import argparse,json,datetime
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('page',type=int)
parser.add_argument('status',choices=['verified','unresolved','corrected'])
parser.add_argument('note')
parser.add_argument('--issue',default='')
a=parser.parse_args()
root=Path(__file__).resolve().parent
path=root/'inventory.json'
j=json.loads(path.read_text(encoding='utf-8'))
b=next(book for sub in j['subjects'] if sub['subject']=='Chemistry' for book in sub['books'] if book['path'].endswith('chemistryfull.pdf'))
b['correctedPages']=sorted(set(b.get('correctedPages',[])+[a.page]))
if a.status=='verified':
 b['verifiedCorrectedPages']=sorted(set(b.get('verifiedCorrectedPages',[])+[a.page]))
 b['unresolvedPages']=[page for page in b.get('unresolvedPages',[]) if page!=a.page]
else:
 b['verifiedCorrectedPages']=[page for page in b.get('verifiedCorrectedPages',[]) if page!=a.page]
 if a.status=='unresolved':b['unresolvedPages']=sorted(set(b.get('unresolvedPages',[])+[a.page]))
b.setdefault('pageAudits',{})[str(a.page)]={'status':'verified corrected' if a.status=='verified' else a.status,'printedPage':a.page-5,'compared':a.note,'unresolved':a.issue,'validation':'Source inspection and focused syntax/reader/formula checks recorded in the progress log.'}
b['nextPage']=max(b.get('nextPage',1),a.page+1)
verified=set(b.get('verifiedCorrectedPages',[])+b.get('verifiedUnchangedPages',[]))
b['draftPages']=sorted(set(b.get('draftPages',[]))-verified-set(b.get('unresolvedPages',[])))
b['inspectedPages']=sorted(set(b.get('inspectedPages',[])+[int(page) for page in b['pageAudits']]))
b['verificationNote']='Chemistry sequential checkpoint next PDF page '+str(b['nextPage'])+'. Book incomplete; unresolved source pages '+','.join(map(str,b.get('unresolvedPages',[])))+'. Verification remains separate from inspected/corrected status.'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
path.write_text(json.dumps(j,ensure_ascii=False,indent=2),encoding='utf-8')
with (root/'progress.md').open('a',encoding='utf-8') as log:log.write('\n'+now+' — Chemistry PDF page '+str(a.page)+' '+a.status+'. '+a.note+(' Unresolved: '+a.issue if a.issue else '')+' Next page '+str(b['nextPage'])+'.\n')
print('Checkpoint saved: page',a.page,a.status,'next',b['nextPage'])
