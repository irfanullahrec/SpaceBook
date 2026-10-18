# -*- coding: utf-8 -*-
"""Dump all paragraphs of the 12th Computer Science docx parts to a text file
with index, style, bold flag, and page-break markers for structural analysis."""
import os, zipfile, xml.etree.ElementTree as ET, sys, re

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Computer Science\Word"
OUT = r"D:\SpaceBook\SpaceBook Web\tools\comp12_dump.txt"

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR)
                if f.endswith('.docx') and not f.startswith('~$')])

lines = []
idx = 0
for f in files:
    lines.append(f"########## FILE: {os.path.basename(f)} ##########")
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter(NS + 'p'):
            texts = []
            all_bold = True
            has_run = False
            page_break = False
            for r in p.iter(NS + 'r'):
                has_run = True
                rPr = r.find(NS + 'rPr')
                b = rPr is not None and rPr.find(NS + 'b') is not None
                if not b:
                    all_bold = False
                for t in r.iter(NS + 't'):
                    if t.text:
                        texts.append(t.text)
                for br in r.iter(NS + 'br'):
                    if br.get(NS + 'type') == 'page':
                        page_break = True
            txt = ''.join(texts)
            # style
            style = ''
            pPr = p.find(NS + 'pPr')
            if pPr is not None:
                pStyle = pPr.find(NS + 'pStyle')
                if pStyle is not None:
                    style = pStyle.get(NS + 'val', '')
            if page_break:
                lines.append(f"[{idx:04d}] <<PAGEBREAK>>")
                idx += 1
            if not txt.strip():
                continue
            flag = ('B' if (all_bold and has_run) else ' ')
            lines.append(f"[{idx:04d}] [{flag}] [{style}] {txt}")
            idx += 1

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines))
print(f"Wrote {len(lines)} lines to {OUT}")
