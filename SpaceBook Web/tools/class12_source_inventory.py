"""Read-only source inventory; never traverse excluded subject folders."""
from pathlib import Path
import hashlib
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT.parent / 'Books/12th'
OUT = ROOT / 'docs/source-verification/class-12'
ORDER = ['Physics', 'Chemistry', 'Statistics', 'English', 'Urdu', 'Biology',
         'Pakistan Studies', 'Computer Science', 'Civics', 'Economics',
         'Health & Physical Education', 'Islamiat Ikhtiari', 'Islamic History', 'Mutalia-e-Quran']
ALIASES = {'Pak Studies': 'Pakistan Studies', 'HPE': 'Health & Physical Education',
           'Mutalia e Quran': 'Mutalia-e-Quran'}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    subjects = []
    hashes = {}
    for folder in SOURCES.iterdir():
        if not folder.is_dir() or re.search(r'math|mtha|ریاضی', folder.name, re.I):
            continue
        name = re.sub(r'^12th\s+', '', folder.name)
        name = ALIASES.get(name, name)
        books = []
        for source in sorted(folder.rglob('*.pdf')):
            digest = hashlib.file_digest(source.open('rb'), 'sha256').hexdigest()
            with pymupdf.open(source) as document:
                count = len(document)
                metadata = document.metadata
            split = bool(re.search(r'part[_ -]?\d+|chapter', source.name, re.I))
            books.append({'sourcePath': str(source), 'sha256': digest,
                          'totalPdfPages': count, 'metadata': metadata,
                          'role': 'split_candidate' if split else 'complete_book_candidate',
                          'exactDuplicateOf': hashes.get(digest),
                          'relationshipStatus': 'Exact byte duplicate' if digest in hashes else
                          'Edition and visual relationship require source inspection; not inferred from filename',
                          'reviewStatus': 'not_reviewed', 'verifiedUnchangedPages': [],
                          'correctedPages': [], 'excludedPages': [], 'unresolvedPages': []})
            hashes.setdefault(digest, str(source))
        subjects.append({'subject': name, 'sourceFolder': str(folder), 'pdfs': books})
    subjects.sort(key=lambda subject: ORDER.index(subject['subject']) if subject['subject'] in ORDER else len(ORDER))
    result = {'assignedClass': 12, 'exclusion': 'Mathematics completely excluded; folders not traversed',
              'subjectOrder': ORDER, 'subjects': subjects,
              'totals': {'subjects': len(subjects), 'pdfs': sum(len(s['pdfs']) for s in subjects),
                         'pdfPagesIncludingUnresolvedSplitRelationships': sum(b['totalPdfPages'] for s in subjects for b in s['pdfs'])}}
    (OUT / 'inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result['totals']))
    for subject in subjects:
        print(subject['subject']+': '+', '.join(Path(b['sourcePath']).name+' ('+str(b['totalPdfPages'])+')' for b in subject['pdfs']))

if __name__ == '__main__':
    main()
