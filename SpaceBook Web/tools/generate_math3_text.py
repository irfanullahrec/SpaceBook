import zipfile,xml.etree.ElementTree as ET,json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
source=r'D:\SpaceBook\Books\3rd\3rd Maths\Word\3rd Maths.docx'
out=r'D:\SpaceBook\SpaceBook Web\js\math_3_book_text.js'
with zipfile.ZipFile(source) as z: root=ET.fromstring(z.read('word/document.xml'))
ns='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
paras=[]
for el in root.iter(ns+'p'):
 s=''.join(x.text or '' for x in el.iter(ns+'t')).strip()
 if s: paras.append(s)
# Locate the official title block, the seven unit heads, and the appendix.
book_start=next(i for i,s in enumerate(paras) if s=='Textbook' and i>20)
unit_starts=[]
for i,s in enumerate(paras):
 if s!='Unit': continue
 nxt=paras[i+1:i+4]
 if any(str(n) in [str(k) for k in range(1,8)] for n in nxt):
  num=next(int(n) for n in nxt if n.isdigit() and int(n) in range(1,8))
  # Unit 2 extraction order puts its name before the numeral; all others put number first.
  if num not in [x[0] for x in unit_starts]: unit_starts.append((num,i))
unit_starts.sort()
expected=['Whole Numbers','Number Operations','Fractions','Measurement:','Measurement: Time','Geometry','Learning Objects:']
if len(unit_starts)!=7: raise SystemExit(f'Expected 7 unit starts, got {unit_starts}')
chapters=[]
for pos,(num,start) in enumerate(unit_starts):
 end=unit_starts[pos+1][1] if pos+1<len(unit_starts) else next((i for i in range(start+1,len(paras)) if paras[i].upper()=='AUTHORS PROFILE'),len(paras))
 lines=paras[start:end]
 # Ignore only the repeated scan watermark, which is not printed lesson content.
 lines=[s for s in lines if s.strip().lower() not in ('not for sale','awaz e inqiab.com','awaz e ingiab.com','awazeinqilab.com')]
 chapters.append({'number':num,'paragraphs':lines})
front=paras[book_start:unit_starts[0][1]]
front=[s for s in front if s.strip().lower() not in ('not for sale','awaz e inqiab.com','awaz e ingiab.com','awazeinqilab.com')]
appendix=paras[next((i for i,s in enumerate(paras) if s.upper()=='AUTHORS PROFILE'),len(paras)):]
appendix=[s for s in appendix if s.strip().lower() not in ('not for sale','awaz e inqiab.com','awaz e ingiab.com','awazeinqilab.com')]
obj={'frontMatter':front,'units':chapters,'backMatter':appendix}
with open(out,'w',encoding='utf-8',newline='\n') as f:
 f.write('// Source transcription extracted from the supplied Class 3 KPTBB Word companion.\n')
 f.write('// Kept as text data so no scanned page images are bundled or loaded by the app.\n')
 f.write('var MATH_3_BOOK_TEXT = ')
 json.dump(obj,f,ensure_ascii=False,separators=(',',':'))
 f.write(';\n')
print('Created',out,'paragraphs',sum(len(c['paragraphs']) for c in chapters),'chars',sum(sum(map(len,c['paragraphs'])) for c in chapters),'front',len(front),'appendix',len(appendix))
for c in chapters: print('Unit',c['number'],len(c['paragraphs']),'paragraphs',sum(map(len,c['paragraphs'])),'chars',repr(' · '.join(c['paragraphs'][:4])))
