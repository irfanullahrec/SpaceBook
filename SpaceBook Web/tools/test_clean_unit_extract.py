"""
test_clean_unit_extract.py
Tests extraction and cleaning on Unit 1, Unit 3, Unit 6, and Unit 12.
"""
import docx
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th English\Word"
parts = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])
all_paras = []
for p in parts:
    doc = docx.Document(p)
    for par in doc.paragraphs:
        all_paras.append(par.text.strip())

WATERMARKS = re.compile(
    r'\b(NOT FOR SALE[\.\-]*|Whatcann?[i]?|20\d{8}|awazeinqilab(\.com)?|MON|OLE|COM|FOR SALE)\b',
    re.I
)
URDU_CHARS = re.compile(r'[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]')

def clean_para_text(t):
    # Remove watermarks
    t = WATERMARKS.sub('', t)
    # Remove standalone Urdu marginal annotations
    if len(t) < 40 and URDU_CHARS.search(t):
        urdu_len = len(URDU_CHARS.findall(t))
        if urdu_len / len(t.replace(' ', '')) > 0.4:
            return ""
    # Remove pure digit strings or page numbers
    if re.match(r'^\d+$', t.strip()):
        return ""
    if len(t.strip()) <= 2 and not t.strip().isalpha():
        return ""
    # Standardize honorifics
    t = re.sub(r'\( رسول الله خاتم [^\)]+\)', '(ﷺ)', t)
    t = re.sub(r'رسول الله خاتم [^\)]+\)', '(ﷺ)', t)
    t = re.sub(r'\b(Rasool|Prophet)\s*\([rPnAD]\)', r'\1 (ﷺ)', t)
    t = re.sub(r'\b(Rasool|Prophet)\s*\(\s*\)', r'\1 (ﷺ)', t)
    t = re.sub(r'\bhe\s*\([rPnAD]\)', 'he (ﷺ)', t)
    t = re.sub(r'\b(Abu Baker|Abu Bakr|Umar ibn Al-khattab|Osama bin Zaid|Anas|Abu Mas\'ud)\s*\(\s*\)', r'\1 (رضی اللہ عنہ)', t)
    # Typo fixes
    t = t.replace('lodiest', 'loftiest')
    t = t.replace('quaint themselves', 'acquaint themselves')
    t = t.replace('me with a message', 'came with a message')
    t = t.replace('d the young age', 'the young age')
    t = re.sub(r'\s+', ' ', t).strip()
    return t

print("=== CLEANED UNIT 1 ===")
u1_slice = all_paras[258+20 : 258+63]
cleaned_u1 = [clean_para_text(p) for p in u1_slice if clean_para_text(p)]
print(f"Cleaned paras: {len(cleaned_u1)}")
for idx, p in enumerate(cleaned_u1[:6]):
    print(f"[{idx+1}] {p[:120]}...")

print("\n=== CLEANED UNIT 12 (Shakespeare) ===")
u12_slice = all_paras[3839+19 : 3839+30]
cleaned_u12 = [clean_para_text(p) for p in u12_slice if clean_para_text(p)]
print(f"Cleaned lines: {len(cleaned_u12)}")
for idx, p in enumerate(cleaned_u12):
    print(f"[{idx+1}] {p}")
