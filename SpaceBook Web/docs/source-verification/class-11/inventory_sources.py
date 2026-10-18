"""Inventory only assigned non-Mathematics source folders; never visit excluded folders."""
from pathlib import Path
import hashlib
import json
import pymupdf

root = Path(r'D:\SpaceBook\Books\11th')
out = Path(__file__).parent
mapping = {
    '11th physics': ('Physics', 0), '11th chemisty': ('Chemistry', 1),
    '11th stastic': ('Statistics', 2), '11english': ('English', 3),
    '11th Urdu': ('Urdu', 4), '11th bio': ('Biology', 5),
    '11th computer': ('Computer Science', 7), '11th civic': ('Civics', 8),
    '11th Hpe': ('Health & Physical Education', 12),
    '11TH islamyAT LAZIMI': ('Islamiat compulsory', 13),
    '11thslamyat ekhtyri': ('Islamiat Ikhtiari', 14),
    'islamic history': ('Islamic History', 15),
    '11th mutalia quran': ('Mutalia-e-Quran', 16)
}
subjects = []
seen = {}
for folder in sorted(root.iterdir(), key=lambda p: p.name.casefold()):
    if not folder.is_dir() or any(s in folder.name.casefold() for s in ('math', 'mtha', 'ریاضی')):
        continue
    name, order = mapping.get(folder.name, (folder.name, 99))
    books = []
    for path in sorted(folder.rglob('*.pdf'), key=lambda p: p.name.casefold()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        with pymupdf.open(path) as doc:
            pages = len(doc)
            metadata = doc.metadata
        duplicate = seen.get(digest)
        seen.setdefault(digest, str(path))
        books.append({'path': str(path), 'pdfPages': pages, 'sha256': digest,
                      'exactDuplicateOf': duplicate, 'metadata': metadata,
                      'relationship': 'exact duplicate' if duplicate else 'pending visual edition/split comparison',
                      'status': 'unreviewed', 'verifiedUnchangedPages': [], 'correctedPages': [],
                      'excludedPages': [], 'unresolvedPages': [], 'lastFullyVerifiedPage': 0, 'nextPage': 1})
    subjects.append({'subject': name, 'folder': str(folder), 'order': order, 'books': books})
subjects.sort(key=lambda s: (s['order'], s['folder'].casefold()))
inventory = {'assignedClass': 11, 'excluded': 'Mathematics: no files visited',
             'coverageStatus': 'incomplete', 'subjects': subjects}
(out / 'inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'subjects': len(subjects), 'pdfFiles': sum(len(s['books']) for s in subjects),
                  'pdfPagesIncludingSplits': sum(b['pdfPages'] for s in subjects for b in s['books']),
                  'physics': subjects[0]['books']}, ensure_ascii=False, indent=2))
