import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[31]
page.update(id='cls9-physics-page-032',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
c,l=page['sections']
c.update(heading='CONCEPTUAL QUESTIONS',headingUrdu='تصوری سوالات',headingPashto='مفهومي پوښتنې')
c['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='numberedList',indices=list(range(1,9)))]
l.update(heading='COMPREHENSIVE QUESTIONS',headingUrdu='جامع سوالات',headingPashto='جامع پوښتنې')
l['paras'][7]=dict(text='a. Vernier Callipers',urdu='a. ورنیئر کیلیپر',pashto='a. ورنییر کالیپر')
l['paras'].insert(8,dict(text='b. Screw gauge',urdu='b. سکرو گیج',pashto='b. سکرو ګېج'))
l['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='numberedList',indices=[1,2,3,4,5,6]),dict(type='parallelPhrases',columns=[[7],[8]]),dict(type='numberedList',indices=[9])]
n=page['textbookExercise']['lq'][5];n['urdu']+='\na. ورنیئر کیلیپر     b. سکرو گیج';n['pashto']+='\na. ورنییر کالیپر     b. سکرو ګېج'
page['comparison']='Fresh rendered-page review: checked eight conceptual and seven comprehensive questions, source grammar, instructions and exact subparts a/b. Original question text retained; split two subparts into paired parallel records and fixed omitted subpart translations in question-bank record. No answer is printed and none added.'
(OUT/'physics-page-032.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
