import json
import os
import sys
import time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
def write_shared(path, content):
    for attempt in range(4):
        try:
            path.write_text(content, encoding='utf-8')
            return
        except OSError as error:
            if error.errno != 22 or attempt == 3:
                raise
            time.sleep(.2)
page = json.loads((OUT/sys.argv[1]).read_text(encoding='utf-8'))
if 'pairedParagraphs' in page:
    page['paragraphs'] = [p['text'] for p in page['pairedParagraphs']]
lock = ROOT/'tmp/class-content-shared.lock'
fd = os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 front-matter upsert\n')
    data = ROOT/'js/data_phys.js'
    text = data.read_text(encoding='utf-8')
    marker = text.index('// Agent 1 sequential Class 9 Physics source review\n')
    start = text.index('const pages = ',marker)+len('const pages = ')
    decoder = json.JSONDecoder()
    pos = start+1
    while True:
        while text[pos].isspace() or text[pos] == ',':
            pos += 1
        if text[pos] == ']':
            replacement=json.dumps(page,ensure_ascii=False,indent=2)
            write_shared(data,text[:pos].rstrip()+',\n'+replacement+'\n'+text[pos:])
            break
        old, length = decoder.raw_decode(text[pos:])
        if old['pdfPage'] == page['pdfPage']:
            replacement=json.dumps(page,ensure_ascii=False,indent=2)
            write_shared(data,text[:pos]+replacement+text[pos+length:])
            break
        pos += length
    app=ROOT/'js/app.js'
    text=app.read_text(encoding='utf-8')
    old="${page.pairedParagraphs.map((para, index) => renderInteractiveParagraphHtml(para.text, para.urdu, para.pashto, `${page.id}-${index}`, true)).join('<div style=\"height:.75rem\"></div>')}"
    new="${renderClass9PhysicsFrontMatterBlocks(page)}"
    if old in text:
        helper='''function renderClass9PhysicsFrontMatterBlocks(page) {
  const render = index => {
    const para = page.pairedParagraphs[index];
    return renderInteractiveParagraphHtml(para.text, para.urdu, para.pashto, `${page.id}-${index}`, true);
  };
  if (!page.sourceStructure) return page.pairedParagraphs.map((_, index) => render(index)).join('<div style="height:.75rem"></div>');
  return page.sourceStructure.map(block => {
    if (block.type === 'heading') return `<div role="heading" aria-level="4" style="font-weight:700;margin-top:1rem;">${block.indices.map(render).join('')}</div>`;
    if (block.type === 'list') return `<ul>${block.indices.map(index => `<li>${render(index)}</li>`).join('')}</ul>`;
    return block.indices.map(render).join('<div style="height:.5rem"></div>');
  }).join('');
}

'''
        text=text.replace('function renderClass9PhysicsFrontMatter(ch) {',helper+'function renderClass9PhysicsFrontMatter(ch) {',1).replace(old,new,1)
        app.write_text(text,encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
checkpoint=json.loads((OUT/'checkpoint.json').read_text(encoding='utf-8'))
checkpoint['correctedPages']=sorted(set(checkpoint['correctedPages']+[page['pdfPage']]))
if page.get('unresolvedItems'):
    checkpoint['unresolvedPages']=sorted(set(checkpoint['unresolvedPages']+[page['pdfPage']]))
    checkpoint.setdefault('unresolvedItems',{})[str(page['pdfPage'])]=page['unresolvedItems']
checkpoint['fullyReviewedWithoutUnresolvedItems']=[n for n in checkpoint['correctedPages'] if n not in checkpoint['unresolvedPages']]
checkpoint['lastFullyVerifiedPdfPage']=max(checkpoint['fullyReviewedWithoutUnresolvedItems'],default=0)
checkpoint['lastContiguouslyVerifiedPdfPage']=next((n-1 for n in range(1,max(checkpoint['correctedPages'])+2) if n not in checkpoint['fullyReviewedWithoutUnresolvedItems']),0)
checkpoint['lastReviewedPdfPage']=max(checkpoint.get('lastReviewedPdfPage',0),page['pdfPage'])
checkpoint['nextPdfPage']=max(checkpoint['nextPdfPage'],page['pdfPage']+1)
if page.get('chapter'):
    checkpoint['currentChapter']=page['chapter']
checkpoint['inspectedButNotCompletedPages']=[]
checkpoint['nextAction']=f"Render, visually inspect and compare Physics PDF page {checkpoint['nextPdfPage']}; do not trust old completion records."
(OUT/'checkpoint.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inventory=json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
book=inventory['subjects'][0]['books'][0]
book.update(inspectedPages=checkpoint['correctedPages'],correctedPages=checkpoint['correctedPages'],unresolvedPages=checkpoint['unresolvedPages'],lastReviewedPdfPage=checkpoint['lastReviewedPdfPage'],lastFullyVerifiedPdfPage=checkpoint['lastFullyVerifiedPdfPage'],fullyReviewedWithoutUnresolvedItems=checkpoint['fullyReviewedWithoutUnresolvedItems'],nextPdfPage=checkpoint['nextPdfPage'])
(OUT/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Saved existing Physics PDF page {page['pdfPage']} record.")
