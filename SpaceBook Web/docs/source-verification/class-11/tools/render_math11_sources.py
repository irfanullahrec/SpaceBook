"""Render source scan indices, accounting for identical split-boundary PDF pages."""
import hashlib,json,sys
from pathlib import Path
import pymupdf
HERE=Path(__file__).resolve().parents[1];APP=HERE.parents[2]
SOURCE=APP.parent/'Books'/'11th'/'11th Maths'/'pdf'
OUT=APP/'tmp'/'class-11'/'math';OUT.mkdir(exist_ok=True)
mapping=[];duplicates=[];last=None;docs=[]
for file in sorted(SOURCE.glob('*.pdf')):
    doc=pymupdf.open(file);docs.append(doc)
    for i,page in enumerate(doc):
        images=page.get_images();assert len(images)==1,(file.name,i)
        digest=hashlib.sha256(doc.extract_image(images[0][0])['image']).hexdigest()
        item=dict(pdf=file.name,partPage=i+1,imageSha256=digest)
        if i==0 and digest==last:
            duplicates.append(dict(**item,duplicatesScanIndex=len(mapping)-1))
        else:mapping.append(dict(**item,scanIndex=len(mapping)))
        last=digest
assert len(mapping)==432 and len(duplicates)==9
inventory=dict(sourceRoot=str(SOURCE),pdfFileCount=len(docs),physicalPdfPages=sum(len(d) for d in docs),uniqueSourceScans=len(mapping),duplicates=duplicates,pages=mapping,mappingEvidence='Identical extracted JPEG byte hashes at each of the nine adjacent PDF part boundaries; no content skipped.')
(HERE/'math'/'pdf-source-map.json').write_text(json.dumps(inventory,indent=2)+'\n',encoding='utf-8')
by_name={Path(d.name).name:d for d in docs}
for index in map(int,sys.argv[1:]):
    item=mapping[index];doc=by_name[item['pdf']]
    doc[item['partPage']-1].get_pixmap(matrix=pymupdf.Matrix(1.6,1.6)).save(str(OUT/f'p{index:03}.png'))
    print(index,item['pdf'],item['partPage'])
