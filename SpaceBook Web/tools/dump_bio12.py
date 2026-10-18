# -*- coding: utf-8 -*-
"""Dump DOCX paragraphs with indices for inspection. Usage: python dump_bio12.py START END"""
import zipfile, xml.etree.ElementTree as ET, sys, os
sys.stdout.reconfigure(encoding='utf-8')

D = r"D:\SpaceBook\Books\12th\12th Biology\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

files = sorted(f for f in os.listdir(D) if f.endswith('.docx'))
paras = []
for fn in files:
    with zipfile.ZipFile(os.path.join(D, fn)) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    for p in root.iter(NS + 'p'):
        t = ''.join(x.text for x in p.iter(NS + 't') if x.text).strip()
        if t:
            paras.append(t)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else start + 100
print('TOTAL', len(paras))
for i in range(start, min(end, len(paras))):
    print(i, repr(paras[i][:120]))
