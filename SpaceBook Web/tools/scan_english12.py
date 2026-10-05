import os, zipfile, xml.etree.ElementTree as ET, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')
docx_p = r"D:\SpaceBook\Books\12th\12th English\Word"
files = sorted([os.path.join(docx_p, f) for f in os.listdir(docx_p) if f.endswith('.docx')])

all_paras = []
for f in files:
    with zipfile.ZipFile(f) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        for p_tag in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p_tag.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt and 'camscanner' not in txt.lower():
                    all_paras.append(txt)

print('English 12 total paras:', len(all_paras))

units = []
for i, p in enumerate(all_paras):
    m = re.match(r'^Unit[\s\-]*(\d+)\b', p, re.IGNORECASE)
    if m:
        num = int(m.group(1))
        fol = all_paras[i+1:i+4]
        units.append((num, i, p, fol))

for u in units:
    print(f"Unit {u[0]} at para {u[1]}: '{u[2]}' -> {u[3]}")
