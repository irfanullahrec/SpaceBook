# -*- coding: utf-8 -*-
"""
Extractor for Islamic History 12 - KPK Textbook Board
Reads 3 docx files, finds lesson boundaries, prints structure.
"""
import zipfile, xml.etree.ElementTree as ET, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Islamic History\Word"
files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR)
                if f.endswith('.docx') and not f.startswith('~$')])

all_paras = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p_tag.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt and 'camscanner' not in txt.lower():
                    all_paras.append(txt)

print(f"Total paragraphs: {len(all_paras)}")

# Find lesson/chapter heading patterns
JUNK = re.compile(r'^(Not For Sale|Hot For Sale|NUL For Sale|away|awa|LIPJ|ab\.co|ot For|CO|\(\d+\)|[\d\s\.\(\)]+)$', re.IGNORECASE)

lesson_starts = []
for i, p in enumerate(all_paras):
    # Look for "باب : N" or lesson names
    if re.match(r'^باب\s*:\s*\d', p) or re.match(r'^باب\s+\d', p):
        lesson_starts.append((i, p))
    elif re.match(r'^آغاز خلافت', p):
        lesson_starts.append((i, p))

print(f"\nFound {len(lesson_starts)} lesson start markers:")
for idx, (i, p) in enumerate(lesson_starts[:60]):
    print(f"  [{i:4d}] {repr(p[:70])}")

# Also find "مشقی سوالات" (exercise sections)
print("\n--- Exercise sections ---")
for i, p in enumerate(all_paras):
    if 'مشق' in p and ('سوال' in p or 'مشقی' in p):
        print(f"  [{i:4d}] {repr(p[:60])}")

# Print all paragraphs around TOC region
print("\n--- TOC area (paras 48-120) ---")
for i in range(48, min(125, len(all_paras))):
    p = all_paras[i]
    if len(p) < 100:
        print(f"[{i:4d}] {repr(p)}")
