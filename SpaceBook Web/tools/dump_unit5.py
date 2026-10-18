"""Dump raw paragraphs for Unit 5 (The Last Leaf) to diagnose filtering."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document
import os, re

DOCX_DIR = r'D:\SpaceBook\Books\12th\12th English\Word'
parts = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])
all_paras = []
for p in parts:
    doc = Document(p)
    for par in doc.paragraphs:
        t = par.text.strip()
        if t:
            all_paras.append(t)

# Unit 5 starts at para 1601, unit 6 at 1927
print("=== Unit 5: The Last Leaf (paras 1601-1700) ===")
for i in range(1601, min(1700, len(all_paras))):
    print(f"[{i}] {repr(all_paras[i][:120])}")
