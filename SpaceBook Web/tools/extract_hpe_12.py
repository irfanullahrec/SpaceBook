import zipfile, xml.etree.ElementTree as ET, sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th HPE\Word"
files = sorted([
    os.path.join(DOCX_DIR, f)
    for f in os.listdir(DOCX_DIR)
    if f.endswith('.docx')
])

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def extract_paragraphs(docx_path):
    paras = []
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{NS}p'):
            texts = [t.text for t in p_tag.iter(f'{NS}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt:
                    paras.append(txt)
    return paras

all_paras = []
for f in files:
    print(f"\n=== FILE: {os.path.basename(f)} ===")
    ps = extract_paragraphs(f)
    print(f"  Total paragraphs: {len(ps)}")
    all_paras.extend(ps)

print(f"\n\n=== ALL PARAGRAPHS TOTAL: {len(all_paras)} ===\n")

# Print paragraphs that are likely headings (short, no long sentence patterns)
print("=== POTENTIAL HEADINGS (len < 80 chars) ===")
for i, p in enumerate(all_paras):
    if len(p) < 80:
        print(f"[{i:4d}] {p}")

print("\n\n=== FIRST 300 PARAGRAPHS (numbered) ===")
for i, p in enumerate(all_paras[:300]):
    print(f"[{i:4d}] {p}")
