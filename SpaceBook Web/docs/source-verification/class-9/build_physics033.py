import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[32]
page.update(id='cls9-physics-page-033',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s,w=page['sections'];items=page['textbookExercise']['numericalQuestions']
items[0]['q']='Write the number in prefix to power of ten'
items[1]['subquestions'][2]['q']='c. How many angstroms are in 1.0m?'
items[2]['subquestions']=items[2]['subquestions'][:2]+[dict(label='b.i',q='i. five significant figures,',urdu='i. پانچ بامعنی ہندسے،',pashto='i. پنځه بامعنی شمېرې،'),dict(label='b.ii',q='ii. three significant figures.',urdu='ii. تین بامعنی ہندسے۔',pashto='ii. درې بامعنی شمېرې.')]
items[3]['subquestions']=[dict(label=label,q=q,urdu=u,pashto=p) for label,q,u,p in [('a','a. 7 nanometre','a. 7 نینومیٹر','a. 7 نانومتره'),('b','b. 96 megawatt','b. 96 میگاواٹ','b. 96 مېګاواټه'),('c','c. 2 gigabite','c. 2 گیگابائٹ','c. 2 ګېګابایټه'),('d','d. 43 picofarad','d. 43 پیکوفیرڈ','d. 43 پیکوفاراډه'),('e','e. 2 millimetre.','e. 2 ملی میٹر۔','e. 2 ملي متره.')]]
s.update(heading='NUMERICAL QUESTIONS',headingUrdu='عددی سوالات',headingPashto='عددي پوښتنې');s['paras']=[];s['sourceLayout']=[]
for item in items:
 i=len(s['paras']);s['paras'].append(dict(text=f"{item['num']}. {item['q']}",urdu=f"{item['num']}. {item['urdu']}",pashto=f"{item['num']}. {item['pashto']}"));s['sourceLayout'].append(dict(type='paragraph',indices=[i]))
 indices=[]
 for sub in item['subquestions']:
  indices.append(len(s['paras']));s['paras'].append(dict(text=sub['q'],urdu=sub['urdu'],pashto=sub['pashto']))
 if item['num']==3:s['sourceLayout'] += [dict(type='numberedList',indices=indices[:2]),dict(type='parallelPhrases',columns=[[indices[2]],[indices[3]]])]
 elif item['num']==4:s['sourceLayout'] += [dict(type='parallelPhrases',columns=[[i] for i in indices[:3]]),dict(type='parallelPhrases',columns=[[i] for i in indices[3:]])]
 else:s['sourceLayout'].append(dict(type='numberedList',indices=indices))
s['blocks']=[dict(type='question',number=i['num'],question=i['q'],subquestions=i['subquestions'],answerProvidedInSource=False) for i in items]
w.update(heading='WEB LINKS',headingUrdu='ویب روابط',headingPashto='وېب تړنې');w['sourceLayout']=[dict(type='paragraph',indices=[i]) for i in range(4)]
page['comparison']='Fresh rendered-page review: verified five numerical questions, every exponent/quantity, original gigabite and kilometere spelling, bacterial grouped decimal and all four printed links. Restored subpart layout and b.i/b.ii hierarchy, five separate power-of-ten entries in 3+2 column rows, with paired translations. No numeric solutions printed or added. Unit 1 ends at printed page 28/PDF33.'
(OUT/'physics-page-033.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
