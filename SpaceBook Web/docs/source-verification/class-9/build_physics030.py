import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[29]
page.update(id='cls9-physics-page-030',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0];old=s['paras'];s.update(heading='PROJECTS',headingUrdu='منصوبے',headingPashto='پروژې')
s['paras']=[];s['sourceLayout']=[]
for i,activity in enumerate(page['activities']):
 letter='ABCDE'[i];s['paras'].append(dict(text='GROUP - '+letter,urdu='گروپ - '+letter,pashto='ګروپ - '+letter))
 para=old[2*i+1].copy();para['text']=activity['name']+': '+para['text']
 names=[('نوبیل انعام یافتگان','د نوبل جایزې ګټونکي'),('معیاری اکائیاں','معیاري واحدونه'),('پاکستان کونسل آف سائنس اینڈ ٹیکنالوجی','د پاکستان د ساینس او ټکنالوژۍ شورا'),('SI اکائیوں کی تاریخ','د SI واحدونو تاریخ'),('میٹر رول','متر خط کش')]
 para['urdu']=names[i][0]+': '+para['urdu'];para['pashto']=names[i][1]+': '+para['pashto']
 s['paras'].append(para);s['sourceLayout'] += [dict(type='heading',indices=[2*i]),dict(type='paragraph',indices=[2*i+1])]
page['comparison']='Fresh rendered-page review of every group A–E and all five full project tasks. Removed invented em-dash joining group/title; preserved group headings and source inline title-colon paragraphs, with paired translations. No illustrations on this page and no research answers substituted.'
(OUT/'physics-page-030.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
