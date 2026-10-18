"""Match local alternate scan images to the primary book; this is not a page review."""
import hashlib
import json
from pathlib import Path
import pymupdf

out = Path(__file__).parent
p = out / 'inventory.json'
inventory = json.loads(p.read_text(encoding='utf-8'))
books = inventory['subjects'][0]['books']
primary = next(b for b in books if b['path'].endswith('physicsfull.pdf'))
def signatures(path):
    with pymupdf.open(path) as doc:
        return [tuple(hashlib.sha256(doc.extract_image(x[0])['image']).hexdigest()
                      for x in page.get_images(full=True)) for page in doc]
primary_signatures = signatures(primary['path'])
index = {}
for page, signature in enumerate(primary_signatures, 1):
    index.setdefault(signature, []).append(page)
mapping = []
for book in books:
    if book is primary:
        continue
    matches = [index.get(signature, []) if signature else [] for signature in signatures(book['path'])]
    exact = all(len(pages) == 1 for pages in matches)
    book['relationship'] = 'alternate scan split; every embedded page image identical to primary' if exact else 'partial scan match; unmatched pages require comparison'
    book['primarySource'] = primary['path']
    book['primaryPdfPageMap'] = matches
    book['relationshipEvidence'] = 'SHA-256 of every embedded page image, including boundaries; not visual inspection or content verification'
    if exact:
        book['coveragePolicy'] = 'Covered through primary book review; do not implement duplicate lessons'
    mapping.append({'file': Path(book['path']).name, 'matched': exact,
                    'firstPrimaryPages': matches[0], 'lastPrimaryPages': matches[-1]})
p.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(mapping))
