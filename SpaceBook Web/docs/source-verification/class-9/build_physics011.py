import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[10]
page.update(id='cls9-physics-page-011',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s.update(headingUrdu='طبیعیات کی شاخیں',headingPashto='د فزیک څانګې')
table=page['tables'][0]
table['translations'][0]['rows'][1][0]='حرارت اور حرارتی حرکیات'
s['blocks'][0]=table.copy()
s['blocks'][0]['type']='dataTable'
s['paras'].append(dict(text=table['title'],urdu='جدول 1.1 طبیعیات کی شاخیں',pashto='جدول 1.1 د فزیک څانګې'))
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[2]),dict(type='sourceDataTable',tableId='table1.1')]
page['comparison']='Fresh 1.8x visual comparison of BRANCHES OF PHYSICS heading, introductory paragraph, TABLE 1.1 title, all three headers and all 33 cells of eleven rows, including punctuation/capitalization. Table source text verified unchanged. Repaired active merged-section layout so the full semantic table and its structured Urdu/Pashto equivalents render once; improved thermodynamics translation. Activities table uses the same corrected rows.'
(OUT/'physics-page-011.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
