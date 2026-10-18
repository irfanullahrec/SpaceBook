import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[12]
page.update(id='cls9-physics-page-013',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s.update(heading='1.3 INTERNATIONAL SYSTEM OF UNITS',headingUrdu='1.3 اکائیوں کا بین الاقوامی نظام',headingPashto='1.3 د واحدونو نړیوال سیستم')
table=page['tables'][0]
table['subHeaders']=['Name','Symbol','Name','Symbol']
for translation in table['translations']:
    if translation['language']=='اردو':
        translation.update(subHeaders=['نام','علامت','نام','علامت'],headerGroups=[dict(title='بنیادی مقدار',columns=[0,1]),dict(title='SI بنیادی اکائی',columns=[2,3])])
        translation['rows'][0][1]='l, x, r (وغیرہ)'
        translation['rows'][3][1]='I یا i'
        translation['rows'][4][0]='حرارتی حرکیاتی درجۂ حرارت'
    else:
        translation.update(subHeaders=['نوم','نښه','نوم','نښه'],headerGroups=[dict(title='بنسټیز کمیت',columns=[0,1]),dict(title='د SI بنسټیز واحد',columns=[2,3])])
        translation['rows'][0][1]='l, x, r (او داسې نور)'
        translation['rows'][3][1]='I یا i'
s['blocks'][0]=dict(type='dataTable',**table)
caption=s['paras'][1]
caption['text']=caption['text'].removeprefix('INFORMATION: ')
caption['urdu']=caption['urdu'].removeprefix('معلومات: ')
caption['pashto']=caption['pashto'].removeprefix('معلومات: ')
s['paras'].append(dict(text='INFORMATION',urdu='معلومات',pashto='معلومات'))
s['paras'].append(dict(text=table['title'],urdu='جدول 1.2 بین الاقوامی نظامِ اکائیات کی بنیادی اکائیاں',pashto='جدول 1.2 د واحدونو د نړیوال سیستم بنسټیز واحدونه'))
cockpit=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 300" role="img" aria-labelledby="physics9-cockpit-title"><title id="physics9-cockpit-title">Aeroplane cockpit with measuring and information instruments for safe flight</title><rect width="430" height="300" fill="#454958"/><path d="M20 58L48 19H382L410 58L361 99H68Z" fill="#75818e" stroke="#242b39" stroke-width="6"/><path d="M122 20V87M215 20V93M309 20V86" stroke="#313947" stroke-width="7"/><path d="M20 100L60 82H369L413 103V207H19Z" fill="#68717c" stroke="#303845" stroke-width="4"/>']
for x,y in [(46,110),(103,110),(165,110),(229,110),(289,110),(345,110)]:
    cockpit.append(f'<rect x="{x}" y="{y}" width="41" height="44" rx="2" fill="#131e2d" stroke="#a4aebc" stroke-width="2"/><path d="M{x+4} {y+20}H{x+37}M{x+20} {y+6}V{y+36}" stroke="#7691ae" stroke-width="2"/>')
for x in [72,123,175,254,307,358]:
    cockpit.append(f'<circle cx="{x}" cy="178" r="15" fill="#142332" stroke="#b3bac7" stroke-width="2"/><path d="M{x} 178l7 -9" stroke="#f1f5f9" stroke-width="2"/>')
cockpit.append('<rect x="193" y="168" width="40" height="98" fill="#9097a2" stroke="#343e50" stroke-width="3"/><path d="M206 180V236M218 180V236" stroke="#1f2937" stroke-width="4"/><path d="M193 232H233" stroke="#e2e8f0" stroke-width="5"/><path d="M41 230L29 289H112L100 224Z M330 224L318 289H401L391 230Z" fill="#7c8492" stroke="#2c3544" stroke-width="4"/></svg>')
s['blocks'].append(dict(type='illustration',id='physics9-cockpit-008',svg=''.join(cockpit),sourcePdfPage=13,printedPage=8))
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='visual',blockId='physics9-cockpit-008'),dict(type='heading',indices=[7]),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[8]),dict(type='sourceDataTable',tableId='table1.2'),dict(type='heading',indices=[2]),dict(type='paragraph',indices=[3]),dict(type='heading',indices=[4]),dict(type='paragraph',indices=[5]),dict(type='paragraph',indices=[6])]
page['definitions']=[dict(term='SI Units',definition=s['paras'][0]['text'],urdu=s['paras'][0]['urdu'],pashto=s['paras'][0]['pashto'],sourcePdfPage=13,sourcePrintedPage=8)]
page['comparison']='Fresh visual comparison of section 1.3 full definition/explanation, cockpit information caption, grouped SI table headers and all 28 body cells, base-unit paragraph, and both historical SI paragraphs with quantities 37 whole 7/8, 16/12/5280/1000/100. Preserved printed French wording and I symbol for luminous intensity. Restored two-tier table headers and coded cockpit instrument layout; completed missing etc/or target-language table labels. Synced SI dictionary definition.'
(OUT/'physics-page-013.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
