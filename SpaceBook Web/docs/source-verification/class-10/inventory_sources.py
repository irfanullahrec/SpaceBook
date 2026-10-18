"""Inventory only non-Mathematics Class 10 sources; never mark pages reviewed."""
import hashlib
import json
import re
from pathlib import Path
import pymupdf

ROOT = Path(r'D:\SpaceBook\Books\10th')
OUT = Path(__file__).parent
ORDER = ['Physics', 'Chemistry', 'Statistics', 'English', 'Urdu', 'Biology', 'Pakistan Studies', 'Computer Science', 'Civics', 'Economics', 'General Science', 'Drawing', 'Health & Physical Education', 'Islamiat compulsory', 'Islamiat Ikhtiari', 'Islamic History', 'Mutalia-e-Quran']
ALIASES = {'10th physics':'Physics','10th Chemistry':'Chemistry','10th English':'English','10 urdu':'Urdu','10th Bio':'Biology','10th pakstudy':'Pakistan Studies','10th CS':'Computer Science','10th General Science':'General Science','10th  Drawing':'Drawing','10th HPE':'Health & Physical Education','10th Ismaiat Ikhtiari':'Islamiat Ikhtiari','10th M Q':'Mutalia-e-Quran'}

def excluded(name):
    return bool(re.search(r'math|mtha|ریاضی', name, re.I))

subjects = []
for folder in ROOT.iterdir():
    if not folder.is_dir() or excluded(folder.name):
        continue
    subject = ALIASES.get(folder.name, folder.name)
    books = []
    for source in sorted(folder.rglob('*.pdf')):
        if excluded(source.name):
            continue
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        with pymupdf.open(source) as pdf:
            books.append({'id':subject.lower().replace(' ','-')+'-'+source.stem, 'path':str(source),'sha256':digest,'pdfPages':len(pdf),'metadata':pdf.metadata,'relationship':'pending visual edition/split comparison','status':'not-reviewed','verifiedUnchangedPages':[],'correctedPages':[],'excludedPages':[],'unresolvedPages':[],'lastFullyVerifiedPage':0,'nextPage':1})
    subjects.append({'subject':subject,'folder':str(folder),'books':books})
subjects.sort(key=lambda s:(ORDER.index(s['subject']) if s['subject'] in ORDER else len(ORDER),s['folder']))
seen = {}
for subject in subjects:
    for book in subject['books']:
        if book['sha256'] in seen:
            book['relationship']='byte-identical duplicate of '+seen[book['sha256']]
        else:
            seen[book['sha256']]=book['id']
inventory={'assignedClass':10,'mathematics':'excluded entirely; folders and books not opened','freshAudit':True,'subjects':subjects,'totalPdfFiles':sum(len(s['books']) for s in subjects),'totalPdfPages':sum(b['pdfPages'] for s in subjects for b in s['books'])}
(OUT/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'subjects':len(subjects),'pdfFiles':inventory['totalPdfFiles'],'pdfPages':inventory['totalPdfPages'],'physics':subjects[0]},ensure_ascii=False,indent=2))
