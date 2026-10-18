
import docx, re, json

docs = {}
for i in [1, 2, 3, 4, 5]:
    d = docx.Document(f'D:/SpaceBook/Books/4th/4th/Math books 4 KPK_JPGs/word/maths{i}.docx')
    docs[i] = [p.text.strip() for p in d.paragraphs if p.text.strip()]

units_meta = [
    (1, 'Whole Numbers', '1-12', [(1, 78, 238)]),
    (2, 'Addition and Subtraction', '13-21', [(1, 239, 730)]),
    (3, 'Multiplication and Division', '22-35', [(1, 731, 1327)]),
    (4, 'Factors and Multiples', '36-49', [(1, 1328, 1795), (2, 0, 200)]),
    (5, 'Fractions', '50-70', [(2, 201, 1385)]),
    (6, 'Decimals', '71-93', [(2, 1386, 2053), (3, 0, 327)]),
    (7, 'Measurements', '94-112', [(3, 328, 946)]),
    (8, 'Time', '113-129', [(3, 947, 1379), (4, 0, 184)]),
    (9, 'Geometry', '130-163', [(4, 185, 1101)]),
    (10, 'Data Handling', '164-176', [(4, 1102, 1166), (5, 0, 379)])
]

def clean_para(p):
    if not p: return ''
    if any(m in p.lower() for m in ['awaz e inqilab', 'not for sale', 'not-for-sale', 'awazeinqilab', 'camscanner']):
        return ''
    if re.match(r'^\d{1,3}$', p):
        return ''
    return p.strip()

output = []
for u_num, u_title, u_pages, spans in units_meta:
    raw_paras = []
    for d_idx, s, e in spans:
        for p in docs[d_idx][s:e]:
            c = clean_para(p)
            if c:
                raw_paras.append(c)
    
    output.append({
        'number': u_num,
        'title': u_title,
        'pages': u_pages,
        'total_cleaned_paras': len(raw_paras),
        'sample': raw_paras[:3]
    })

print(json.dumps(output, indent=2))
