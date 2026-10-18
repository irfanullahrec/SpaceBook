"""Inventory only non-Mathematics sources. No page is certified by this tool."""
import hashlib
import json
from pathlib import Path
import pymupdf

ROOT = Path(r'D:\SpaceBook\Books\9th')
OUT = Path(__file__).resolve().parent
if (OUT/'inventory.json').exists():
    raise SystemExit('Inventory already exists. Reuse it and preserve its review progress; do not regenerate it.')
ORDER = ['Physics', 'Chemistry', 'English', 'Urdu', 'Biology', 'Pakistan Studies', 'Computer Science', 'General Science', 'Drawing', 'Health & Physical Education', 'Islamiat compulsory', 'Islamiat Ikhtiari', 'Mutalia-e-Quran']
NAMES = {'physics':'Physics','chemistry':'Chemistry','english':'English','urdu':'Urdu','biology':'Biology','pak study':'Pakistan Studies','computer science':'Computer Science','general science':'General Science','drawing':'Drawing','hpe':'Health & Physical Education','islamyat':'Islamiat compulsory','islamiat ikhtiari':'Islamiat Ikhtiari','mq':'Mutalia-e-Quran'}
subjects = []
for folder in ROOT.iterdir():
    if not folder.is_dir():
        continue
    local = ' '.join(folder.name.lower().removeprefix('9th').split())
    if local in ('mtha','math','maths','mathematics'):
        continue
    subject = NAMES.get(local, local)
    books = []
    for pdf in sorted(folder.rglob('*.pdf')):
        with pymupdf.open(pdf) as doc:
            books.append({'sourcePath':str(pdf),'pdfPages':len(doc),'sha256':hashlib.file_digest(pdf.open('rb'),'sha256').hexdigest(),'metadata':doc.metadata,'reviewStatus':'not_reviewed','relationship':'unresolved until page fingerprints compared','inspectedPages':[],'verifiedUnchangedPages':[],'correctedPages':[],'excludedPages':[],'unresolvedPages':[],'nextPdfPage':1})
    subjects.append({'subject':subject,'sourceFolder':str(folder),'books':books})
subjects.sort(key=lambda s: (ORDER.index(s['subject']) if s['subject'] in ORDER else len(ORDER),s['sourceFolder']))
inventory={'assignedClass':9,'mathematicsExcluded':True,'subjectOrder':ORDER,'subjects':subjects,'note':'Metadata inventory is not source-page verification. Split/edition decisions remain explicit pending comparison.'}
(OUT/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Inventoried {len(subjects)} subjects, {sum(len(s['books']) for s in subjects)} PDFs, {sum(b['pdfPages'] for s in subjects for b in s['books'])} PDF pages including candidate split copies.")
