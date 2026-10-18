# -*- coding: utf-8 -*-
import zipfile, xml.etree.ElementTree as ET, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

D = r"D:\SpaceBook\Books\12th\12th Biology\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
V = '{urn:schemas-microsoft-com:vml}'

files = sorted(f for f in os.listdir(D) if f.endswith('.docx') and not f.startswith('~$'))
paras = []
for fn in files:
    with zipfile.ZipFile(os.path.join(D, fn)) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    for p in root.iter(NS + 'p'):
        t = ''.join(x.text for x in p.iter(NS + 't') if x.text).strip()
        has_img = any(True for _ in p.iter(A + 'blip')) or any(True for _ in p.iter(V + 'imagedata'))
        has_drawing = p.find(NS + 'drawing') is not None or p.find(NS + 'pict') is not None
        paras.append({'t': t, 'img': has_img or has_drawing, 'file': fn})

img_idx = [i for i, p in enumerate(paras) if p['img']]
print('paragraphs with images:', len(img_idx), 'of', len(paras))
for i in img_idx[10:22]:
    print('--- image at', i)
    for j in range(i - 4, i + 4):
        if 0 <= j < len(paras):
            mark = '>>' if j == i else '  '
            print(f'{mark} [{j}] {paras[j]["t"][:75]!r}')
