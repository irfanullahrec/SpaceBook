import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[13]
page.update(id='cls9-physics-page-014',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s,q=page['sections']
s['paras'][1]['text']=s['paras'][1]['text'].replace('all the physical quantities','all other physical quantities')
s['paras'][1]['urdu']=s['paras'][1]['urdu'].replace('تمام طبعی مقداروں','باقی تمام طبعی مقداروں')
s['paras'][1]['pashto']=s['paras'][1]['pashto'].replace('د ټولو فزیکي کمیتونو','د نورو ټولو فزیکي کمیتونو')
p=s['paras'][2]
p['text']=p['text'].removeprefix('POINT TO PONDER: ')
p['urdu']=p['urdu'].removeprefix('غور کرنے کی بات: ')
p['pashto']=p['pashto'].removeprefix('د فکر ټکی: ')
s['paras'].append(dict(text='POINT TO PONDER',urdu='غور کرنے کی بات',pashto='د فکر ټکی'))
table=page['tables'][0]
table.update(headerGroups=[dict(title='Derived Quantity',columns=[0,1]),dict(title='Derived Unit',columns=[2,3])],subHeaders=['Name','Symbol','Name','Symbol'])
for t in table['translations']:
    if t['language']=='اردو':
        t.update(headerGroups=[dict(title='ماخوذ مقدار',columns=[0,1]),dict(title='ماخوذ اکائی',columns=[2,3])],subHeaders=['نام','علامت','نام','علامت'])
    else:
        t.update(headerGroups=[dict(title='مشتق کمیت',columns=[0,1]),dict(title='مشتق واحد',columns=[2,3])],subHeaders=['نوم','نښه','نوم','نښه'])
s['paras'].append(dict(text=table['title'],urdu='جدول 1.3 بین الاقوامی نظامِ اکائیات کے لیے ماخوذ اکائیاں',pashto='جدول 1.3 د واحدونو د نړیوال سیستم لپاره مشتق واحدونه'))
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" role="img" aria-labelledby="physics9-viruses-title"><title id="physics9-viruses-title">Several bacteriophage viruses approaching and attaching to a cell</title><rect width="360" height="250" fill="#10243c"/><path d="M0 247Q171 160 360 189V250H0Z" fill="#b99d70" stroke="#5d784e" stroke-width="10"/>']
for x,y,rotation in [(62,112,-40),(136,55,-8),(195,76,18),(261,93,-6),(313,111,6)]:
    svg.append(f'<g transform="translate({x} {y}) rotate({rotation})" fill="none" stroke="#4bc1cf" stroke-width="4"><path d="M0 -23L18 -12L17 10L0 21L-17 10L-18 -12Z" fill="#5db5c4" fill-opacity=".65"/><path d="M0 -23V21M-17 -12L17 10M18 -12L-17 10" stroke-width="1.5"/><path d="M0 21V55M-5 27H5M-5 34H5M-5 41H5M-5 48H5M0 55L-13 68L-19 78M0 55L13 68L19 78M0 55V80"/></g>')
svg.append('</svg>')
s['blocks']=[dict(type='dataTable',**table),dict(type='illustration',id='physics9-viruses-009',svg=''.join(svg),sourcePdfPage=14,printedPage=9)]
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='visual',blockId='physics9-viruses-009'),dict(type='heading',indices=[3]),dict(type='paragraph',indices=[2]),dict(type='heading',indices=[4]),dict(type='sourceDataTable',tableId='table1.3')]
q.update(heading='1.4 Standard Form / SCIENTIFIC NOTATION',headingUrdu='1.4 معیاری صورت / سائنسی طرزِ اظہار',headingPashto='1.4 معیاري بڼه / علمي لیکنه',sourceLayout=[dict(type='paragraph',indices=[0])])
page['definitions']=[dict(term='Derived Units',definition=s['paras'][1]['text'],urdu=s['paras'][1]['urdu'],pashto=s['paras'][1]['pashto'],sourcePdfPage=14,sourcePrintedPage=9)]
page['comparison']='Fresh visual review of derived-unit paragraph, diagram/caption, ten-row 40-cell derived-unit table with every symbol/exponent, and scientific-notation introduction. Corrected all the to printed all other; 4x caption crop confirmed exponent −7. Grouped table headers restored in all reading languages and bacteriophage/cell relationships reconstructed as native SVG. No response invented for the source question.'
(OUT/'physics-page-014.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
