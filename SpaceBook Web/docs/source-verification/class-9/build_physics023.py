import json,re
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[22]
page.update(id='cls9-physics-page-023',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0];s.update(heading='1.6.3 SCREW GAUGE',headingUrdu='1.6.3 سکرو گیج',headingPashto='1.6.3 سکرو ګېج')
s['paras'][0]['text']='‘A device used to measure a fraction of smallest scale division by rotatory motion of circular scale over it is known as screw gauge’.'
s['paras'][3].update(text='Figure 1.3 Screw Gauge',urdu='شکل 1.3 سکرو گیج',pashto='شکل 1.3 سکرو ګېج')
diagram=s['blocks'][2];svg=diagram['svg'].replace('Datum / central line','Datum Line / Central line')
svg=svg.replace('</svg>','<g font-family="sans-serif" font-size="14" fill="currentColor"><text x="417" y="131">5</text><text x="417" y="150">0</text><text x="417" y="169">45</text></g><path d="M285 160l16 24" stroke="#374151" stroke-width="7"/></svg>')
diagram.update(id='physics9-screwgauge-figure13',svg=svg,sourceWidthRatio=.96)
for lang,mapping in [('Urdu',{'Anvil':'اینول','Spindle':'اسپنڈل','Datum Line / Central line':'حوالہ لکیر / مرکزی لکیر','Thimble':'تھمبل','Ratchet':'ریچٹ','Main scale':'مرکزی پیمانہ','Sphere':'کرہ'}),('Pashto',{'Anvil':'ثابت سر','Spindle':'خوځنده محور','Datum Line / Central line':'مرجع کرښه / مرکزي کرښه','Thimble':'تیمبل','Ratchet':'راچټ','Main scale':'اصلي مقیاس','Sphere':'کره'})]:
 translated=svg
 for a,b in mapping.items():translated=translated.replace('>'+a+'<','>'+b+'<')
 diagram['svg'+lang]=translated
photo='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 470 255" role="img" aria-label="Screw gauge with dark U-shaped frame, spindle, sleeve, knurled thimble and ratchet"><g stroke="#68686e" stroke-width="3"><path d="M60 70L43 199Q53 247 132 242L198 223V110H156V166Q156 190 115 192L86 188L89 70Z" fill="#35373e"/><rect x="88" y="70" width="90" height="13" fill="#bfc0c4"/><rect x="177" y="51" width="60" height="55" fill="#929399"/><rect x="237" y="48" width="80" height="49" fill="#d9d7df"/><rect x="317" y="44" width="84" height="55" rx="6" fill="#c4c2cc"/><rect x="402" y="62" width="31" height="18" fill="#cccbd3"/><rect x="430" y="48" width="13" height="40" rx="5" fill="#92929d"/><path d="M205 75l19 31" stroke="#303139" stroke-width="13"/></g><g font-family="sans-serif" fill="#34343c" font-size="12"><text x="265" y="53">20</text><text x="265" y="71">15</text><text x="265" y="89">10</text></g><g fill="#ddd" font-family="sans-serif" font-size="12"><text x="104" y="221">Micromar 40A</text><text x="133" y="235">0-25</text></g></svg>'
def fraction(id,n,d,result=''):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 105" role="img" aria-label="Screw gauge least count fraction"><g font-family="sans-serif" font-size="24" fill="currentColor"><text x="10" y="60">Least Count =</text><text x="545" y="29" text-anchor="middle">{n}</text><text x="545" y="86" text-anchor="middle">{d}</text><text x="830" y="60">{result}</text></g><path d="M205 49H810" stroke="currentColor" stroke-width="2"/></svg>'
 return dict(type='formula',id=id,svg=svg,svgUrdu=svg.replace('Least Count','کم ترین شمار').replace('Pitch of Screw Gauge','سکرو گیج کی پچ').replace('Total Number of Divisions on Circular Scale','دائروی پیمانے کی تقسیموں کی کل تعداد'),svgPashto=svg.replace('Least Count','تر ټولو کوچنۍ اندازه').replace('Pitch of Screw Gauge','د سکرو ګېج پچ').replace('Total Number of Divisions on Circular Scale','د دایروي مقیاس د برخو ټول شمېر'),sourceWidthRatio=.82)
s['blocks']=[dict(type='illustration',id='physics9-screwgauge-object',svg=photo,svgUrdu=photo,svgPashto=photo,sourceWidthRatio=.59),diagram,fraction('physics9-screwgauge-lc','Pitch of Screw Gauge','Total Number of Divisions on Circular Scale'),fraction('physics9-screwgauge-example','0.5mm','50','= 0.01mm')]
# Formula records are preserved as transcriptions; their display uses fraction SVGs.
s['paras'][6].update(text='e.g.',urdu='مثلاً',pashto='د بېلګې په توګه')
s['paras']=s['paras'][:6]+[s['paras'][7],s['paras'][6]]
s['sourceLayout']=[dict(type='quotation',indices=[0]),dict(type='visual',blockId='physics9-screwgauge-object'),dict(type='heading',indices=[1]),dict(type='paragraph',indices=[2]),dict(type='heading',indices=[3]),dict(type='visual',blockId=diagram['id']),dict(type='heading',indices=[4]),dict(type='paragraph',indices=[5]),dict(type='visual',blockId='physics9-screwgauge-lc'),dict(type='paragraph',indices=[6]),dict(type='paragraph',indices=[7]),dict(type='visual',blockId='physics9-screwgauge-example')]
page['definitions']=[dict(term=term,definition=s['paras'][i]['text'],urdu=s['paras'][i]['urdu'],pashto=s['paras'][i]['pashto'],sourcePdfPage=23,sourcePrintedPage=18) for term,i in [('Screw gauge',0),('Pitch',2)]]
page['comparison']='Fresh rendered-page review: restored missing standalone screw-gauge object at approximately 59% content-column width; Figure 1.3 remains almost full width. Preserved definition quotes, distinct headings, pitch/least-count prose and e.g. label; replaced flattened equations with fraction bars. Added circular-scale numbers 5/0/45 and translated seven source pointers, preserving datum wording.'
(OUT/'physics-page-023.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
