"""
Extract Quran 12 content from KPK KPTBB textbook docx files.
Uses zipfile + xml.etree.ElementTree (no python-docx dependency).
"""
import zipfile
import xml.etree.ElementTree as ET
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = r"D:\SpaceBook\Books\12th\12th Mutalia e Quran\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_para_text(p_tag):
    """Extract full text from a paragraph tag."""
    texts = [t.text for t in p_tag.iter(f'{NS}t') if t.text]
    return ''.join(texts).strip()

def get_para_style(p_tag):
    """Get paragraph style name."""
    pPr = p_tag.find(f'{NS}pPr')
    if pPr is not None:
        pStyle = pPr.find(f'{NS}pStyle')
        if pStyle is not None:
            return pStyle.get(f'{NS}val', '')
    return ''

def read_docx(path):
    """Read all paragraphs from a docx file."""
    paras = []
    with zipfile.ZipFile(path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{NS}p'):
            txt = get_para_text(p_tag)
            style = get_para_style(p_tag)
            paras.append({'text': txt, 'style': style})
    return paras

def is_surah_heading(text):
    """Check if text is a surah/chapter heading."""
    t = text.strip()
    if not t:
        return False
    patterns = [
        r'سور[ةۃ]',
        r'سبق',
        r'سُوْرَة',
        r'سُورَة',
    ]
    for p in patterns:
        if re.search(p, t):
            # Must be a heading-like short text (less than 200 chars) or contain آیات
            if len(t) < 300 or 'آیات' in t or 'آيات' in t:
                return True
    return False

def is_exercise_heading(text):
    """Check if this is an exercise/question section."""
    t = text.strip()
    keywords = ['مشق', 'سوالات', 'تمرین', 'سوال', 'جوابات', 'حل']
    return any(k in t for k in keywords) and len(t) < 150

def is_mcq_line(text):
    """Check if this looks like an MCQ."""
    t = text.strip()
    return bool(re.match(r'^[۱-۹\d][۔\.\-\)]', t)) and len(t) < 500

# ─── Read all files ──────────────────────────────────────────────────────────
docx_files = sorted([
    f for f in os.listdir(BOOK_DIR) if f.endswith('.docx')
])

all_paras = []
for fname in docx_files:
    path = os.path.join(BOOK_DIR, fname)
    paras = read_docx(path)
    print(f"\n{'='*60}")
    print(f"FILE: {fname}  ({len(paras)} paragraphs)")
    print(f"{'='*60}")
    
    # Print first 20 non-empty paras to understand structure
    shown = 0
    for i, p in enumerate(paras):
        if p['text']:
            print(f"  [{i:4d}] ({p['style'][:20]:20s}) {p['text'][:120]}")
            shown += 1
            if shown >= 20:
                print("  ...")
                break
    
    # Now print all surah headings
    print(f"\n  --- SURAH/SECTION HEADINGS ---")
    for i, p in enumerate(paras):
        t = p['text']
        if is_surah_heading(t):
            print(f"  [{i:4d}] {t[:150]}")
    
    # Print exercise headings
    print(f"\n  --- EXERCISE/QUESTION HEADINGS ---")
    for i, p in enumerate(paras):
        t = p['text']
        if is_exercise_heading(t):
            print(f"  [{i:4d}] {t[:150]}")
    
    all_paras.append({'file': fname, 'paras': paras})

print("\n\n" + "="*80)
print("SUMMARY: Total paragraphs per file")
for item in all_paras:
    print(f"  {item['file']}: {len(item['paras'])} paras")
