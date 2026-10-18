import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[30]
page.update(id='cls9-physics-page-031',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0];items=page['textbookExercise']['mcqs'];s['paras']=[dict(text='EXERCISE',urdu='مشق',pashto='تمرین'),dict(text='MULTIPLE CHOICE QUESTIONS',urdu='کثیر الانتخابی سوالات',pashto='څو ځوابیزې پوښتنې')];s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='heading',indices=[1])]
for mcq in items:
 if mcq['num']==9:mcq['opts']=['0.0002m','2×10⁻⁴m','none','both A and B']
 base=len(s['paras']);s['paras'].append(dict(text=f"{mcq['num']}. {mcq['q']}",urdu=f"{mcq['num']}. {mcq['urdu']}",pashto=f"{mcq['num']}. {mcq['pashto']}"));s['sourceLayout'].append(dict(type='paragraph',indices=[base]))
 for i,label in enumerate('ABCD'):
  s['paras'].append(dict(text=label+'. '+mcq['opts'][i],urdu=label+'. '+mcq['optsUrdu'][i],pashto=label+'. '+mcq['optsPashto'][i]))
 if mcq['num'] in [3,10]:s['sourceLayout'] += [dict(type='parallelPhrases',columns=[[base+1],[base+2]]),dict(type='parallelPhrases',columns=[[base+3],[base+4]])]
 else:s['sourceLayout'].append(dict(type='parallelPhrases',columns=[[base+1],[base+2],[base+3],[base+4]]))
 mcq['answerProvidedInSource']=False
s['blocks']=[dict(type='mcq',number=m['num'],question=m['q'],options=m['opts'],answerProvidedInSource=False) for m in items]
page['comparison']='Fresh rendered-page review of all ten question statements, forty choices, numbering and source option-row order. Restored EXERCISE and MULTIPLE CHOICE QUESTIONS labels. Options now explicit paired cells, including two-row questions 3/10 and source compact 0.0002m / 2×10⁻⁴m. Preserved pre-existing clearly labelled SpaceBook study aids; no source answer key claimed and no new answers added.'
(OUT/'physics-page-031.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
