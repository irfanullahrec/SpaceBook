"""Resolve copy relationships; these thumbnails do not verify lesson content."""
import hashlib
import json
from pathlib import Path
import pymupdf
OUT=Path(__file__).resolve().parent
file=OUT/'inventory.json'
x=json.loads(file.read_text(encoding='utf-8'))
subject=x['subjects'][0]
primary=next(b for b in subject['books'] if Path(b['sourcePath']).name=='9thphysics.pdf')
def fingerprints(path):
    with pymupdf.open(path) as doc:
        return [hashlib.sha256(p.get_pixmap(matrix=pymupdf.Matrix(1/3,1/3),colorspace=pymupdf.csGRAY,alpha=False).samples).hexdigest() for p in doc]
main=fingerprints(primary['sourcePath'])
primary['relationship']='Complete primary Physics book; numbered copies compared by consecutive 24-dpi grayscale render SHA-256. Render fingerprints establish copy relationships, not text verification.'
for book in subject['books']:
    if book is primary:
        continue
    part=fingerprints(book['sourcePath'])
    starts=[i for i in range(len(main)-len(part)+1) if main[i:i+len(part)]==part]
    if len(starts)==1:
        start=starts[0]+1
        book.update(relationship='Exact consecutive rendered-page copy of complete primary book at fingerprint resolution; use as alternate scan only',primarySource=primary['sourcePath'],primaryPdfPageRange=[start,start+len(part)-1],relationshipEvidence='SHA-256 of every 24-dpi grayscale page render, matching consecutively; full-resolution source audit still required on primary')
    else:
        book['relationship']='Unresolved version: no unique consecutive exact-render match. Must review as potentially distinct until stronger comparison resolves relationship.'
file.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'file':Path(b['sourcePath']).name,'pages':b['pdfPages'],'range':b.get('primaryPdfPageRange'),'relationship':b['relationship']} for b in subject['books']],indent=2))
