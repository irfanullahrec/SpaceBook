import zipfile, xml.etree.ElementTree as ET, sys, re, os

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Computer Science\Word"
docx_files = [
    "001_page_1_and_330_more_part_01_of_03.docx",
    "001_page_1_and_330_more_part_02_of_03.docx",
    "001_page_1_and_330_more_part_03_of_03.docx",
]

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def extract_paragraphs(docx_path):
    """Extract all paragraphs with style info from a .docx file."""
    paragraphs = []
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{NS}p'):
            # Get style
            style = ''
            pPr = p_tag.find(f'{NS}pPr')
            if pPr is not None:
                pStyle = pPr.find(f'{NS}pStyle')
                if pStyle is not None:
                    style = pStyle.get(f'{NS}val', '')
            # Get text
            texts = []
            for r in p_tag.iter(f'{NS}r'):
                for t in r.iter(f'{NS}t'):
                    if t.text:
                        texts.append(t.text)
            txt = ''.join(texts).strip()
            if txt:
                paragraphs.append({'text': txt, 'style': style})
    return paragraphs

# Load all paragraphs from all 3 files
all_paras = []
for fn in docx_files:
    path = os.path.join(DOCX_DIR, fn)
    paras = extract_paragraphs(path)
    print(f"File: {fn} -> {len(paras)} paragraphs")
    all_paras.extend(paras)

print(f"\nTotal paragraphs: {len(all_paras)}")

# Find unit boundaries
print("\n=== UNIT HEADERS ===")
unit_indices = []
for i, p in enumerate(all_paras):
    txt = p['text']
    # Look for UNIT-N or UNIT N patterns
    if re.match(r'^(UNIT[-\s]*\d+)', txt, re.IGNORECASE):
        print(f"[{i:4d}] STYLE={p['style']:<20} TEXT={txt[:100]}")
        unit_indices.append(i)

print(f"\nFound {len(unit_indices)} unit headers")

# Print first 30 paras of each unit
print("\n=== UNIT CONTENT PREVIEW (first 30 paras each) ===")
for ui, unit_start in enumerate(unit_indices):
    unit_end = unit_indices[ui+1] if ui+1 < len(unit_indices) else min(unit_start+200, len(all_paras))
    print(f"\n{'='*60}")
    print(f"UNIT at [{unit_start}]: {all_paras[unit_start]['text']}")
    print(f"  (spans paras {unit_start} to {unit_end-1}, total {unit_end-unit_start})")
    # First 30 paras
    for j in range(unit_start, min(unit_start+30, unit_end)):
        print(f"  [{j:4d}] {all_paras[j]['text'][:120]}")

# Find EXERCISE sections
print("\n=== EXERCISE SECTIONS ===")
for i, p in enumerate(all_paras):
    txt = p['text']
    if re.match(r'^(EXERCISE|Exercise|Self[\s-]?Assessment)', txt, re.IGNORECASE):
        print(f"[{i:4d}] STYLE={p['style']:<20} TEXT={txt[:100]}")
