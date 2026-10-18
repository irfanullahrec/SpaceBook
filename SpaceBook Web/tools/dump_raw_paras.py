"""Dump first 50 raw paragraphs of Unit 1 (para 260 onwards) to understand structure."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
try:
    from docx import Document
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-docx', '-q'])
    from docx import Document

import os, re

DOCX_DIR = r'D:\SpaceBook\Books\12th\12th English\Word'

parts = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])
all_paras = []
for part in parts:
    doc = Document(part)
    for p in doc.paragraphs:
        t = p.text.strip()
        if t:
            all_paras.append(t)

print(f"Total paras: {len(all_paras)}")
print("\n=== Unit 1 area (paras 255-330) ===")
for i in range(255, min(330, len(all_paras))):
    print(f"[{i}] {repr(all_paras[i][:120])}")

print("\n=== Unit 2 area (paras 820-850) ===")
for i in range(820, min(855, len(all_paras))):
    print(f"[{i}] {repr(all_paras[i][:120])}")
