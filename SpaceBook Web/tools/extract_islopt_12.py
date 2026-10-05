import zipfile, xml.etree.ElementTree as ET, sys, os, json, re

sys.stdout.reconfigure(encoding='utf-8')

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

BOOK_DIR = r"D:\SpaceBook\Books\12th\12th Islamiat Ikhtiari\Word"
FILES = [
    "001_and_255_more_part_01_of_04.docx",
    "001_and_255_more_part_02_of_04.docx",
    "001_and_255_more_part_03_of_04.docx",
    "001_and_255_more_part_04_of_04.docx",
]

def get_para_style(p_elem):
    """Get paragraph style name."""
    pPr = p_elem.find(f'{W}pPr')
    if pPr is not None:
        pStyle = pPr.find(f'{W}pStyle')
        if pStyle is not None:
            return pStyle.get(f'{W}val', '')
    return ''

def get_para_text(p_elem):
    """Extract full text from a paragraph element."""
    texts = []
    for t in p_elem.iter(f'{W}t'):
        if t.text:
            texts.append(t.text)
    return ''.join(texts).strip()

def is_bold(p_elem):
    """Check if paragraph has bold runs."""
    for r in p_elem.iter(f'{W}r'):
        rPr = r.find(f'{W}rPr')
        if rPr is not None:
            b = rPr.find(f'{W}b')
            if b is not None:
                val = b.get(f'{W}val', 'true')
                if val != 'false' and val != '0':
                    return True
    return False

# Extract all paragraphs from all files
all_paras = []
for fname in FILES:
    fpath = os.path.join(BOOK_DIR, fname)
    print(f"Reading: {fname}", file=sys.stderr)
    with zipfile.ZipFile(fpath) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter(f'{W}p'):
            txt = get_para_text(p)
            style = get_para_style(p)
            bold = is_bold(p)
            if txt:
                all_paras.append({'text': txt, 'style': style, 'bold': bold, 'file': fname})

print(f"\nTotal paragraphs extracted: {len(all_paras)}", file=sys.stderr)

# Print first 200 paras for inspection
print("\n=== FIRST 200 PARAGRAPHS ===")
for i, p in enumerate(all_paras[:200]):
    print(f"[{i}] style={p['style']} bold={p['bold']} | {p['text'][:120]}")

print("\n=== SEARCHING FOR CHAPTER MARKERS ===")
chapter_keywords = ['باب اول', 'باب دوم', 'باب سوم', 'باب چہارم', 'باب پنجم', 'باب ششم',
                    'بابِ اول', 'بابِ دوم', 'بابِ سوم', 'بابِ چہارم', 'بابِ پنجم', 'بابِ ششم']
for i, p in enumerate(all_paras):
    for kw in chapter_keywords:
        if kw in p['text']:
            print(f"[{i}] CHAPTER FOUND: {p['text'][:200]} | style={p['style']}")
            break

print("\n=== SEARCHING FOR EXERCISE/QUESTION SECTIONS ===")
qa_keywords = ['سوالات', 'مشق', 'قصیر', 'طویل', 'اختیاری', 'ذیلی سوال', 'سوال', 'جواب']
for i, p in enumerate(all_paras):
    for kw in qa_keywords:
        if p['text'].startswith(kw) or (kw in p['text'] and len(p['text']) < 60):
            print(f"[{i}] QA: {p['text'][:150]} | style={p['style']} bold={p['bold']}")
            break
