import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[20]
page.update(id='cls9-physics-page-021',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0];old=s['paras']
def pair(t,u,p):return dict(text=t,urdu=u,pashto=p)
old[9]['text']='If one main scale division is 1 mm, one vernier scale division is 0.9 mm, the least count is 0.1mm.'
old[15]['text']=old[15]['text'].split(': ',1)[-1] if old[15]['text'].startswith('ZERO ERROR IN VERNIER CALLIPER: ') else old[15]['text']
s['paras']=old[:12]+[old[13],pair('ZERO ERROR IN VERNIER CALLIPER','ورنیئر کیلیپر میں صفر کی غلطی','په ورنییر کالیپر کې د صفر تېروتنه'),old[15],old[16],old[17]]
diagram=s['blocks'][0];svg=diagram['svg']
# Retain eight independently checked source pointers and add the missing lower scale,
# sliding scale, retaining screw and upper inch scale labels.
insert='<g stroke="#374151" fill="#ddd"><rect x="174" y="97" width="95" height="9"/><rect x="216" y="135" width="60" height="15"/><rect x="256" y="78" width="8" height="23"/><rect x="251" y="75" width="18" height="5"/></g><g stroke="#374151">'
for i in range(181):
 x=143+i*2.35
 insert+=f'<path d="M{x} 134v-{12 if i%10==0 else 7 if i%5==0 else 4}"/>'
for i in range(11):insert+=f'<path d="M{182+i*7} 98v7M{217+i*5} 144v-7"/>'
insert+='</g><g fill="currentColor" font-family="sans-serif" font-size="8">'
for i in range(18):insert+=f'<text x="{142+i*23.5}" y="122">{i}</text>'
for i in range(1,7):insert+=f'<text x="{160+i*56}" y="117">{i}</text>'
insert+='</g>'
svg=svg.replace('<g fill="currentColor" font-family="sans-serif" font-size="14">',insert+'<g fill="currentColor" font-family="sans-serif" font-size="14">',1)
diagram.update(id='physics9-calliper-figure11',svg=svg)
def fraction(id,numerator,denominator,answer=''):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 110" role="img" aria-label="Least count fraction"><g fill="currentColor" font-family="sans-serif" font-size="24"><text x="10" y="61">Least Count =</text><text x="550" y="33" text-anchor="middle">{numerator}</text><text x="550" y="86" text-anchor="middle">{denominator}</text><text x="790" y="61">{answer}</text></g><path d="M210 52H775" stroke="currentColor" stroke-width="2"/></svg>'
 return dict(type='formula',id=id,svg=svg,svgUrdu=svg.replace('Least Count','کم ترین شمار').replace('Smallest division on main scale','مرکزی پیمانے کی سب سے چھوٹی تقسیم').replace('Total number of divisions on vernier scale','ورنیئر پیمانے کی تقسیموں کی کل تعداد'),svgPashto=svg.replace('Least Count','تر ټولو کوچنۍ اندازه').replace('Smallest division on main scale','د اصلي مقیاس تر ټولو کوچنۍ برخه').replace('Total number of divisions on vernier scale','د ورنییر مقیاس د برخو ټول شمېر'))
s['blocks']=[diagram,fraction('physics9-leastcount-general','Smallest division on main scale','Total number of divisions on vernier scale'),fraction('physics9-leastcount-numeric','1mm','10','= 0.1mm')]
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='visual',blockId=diagram['id']),dict(type='numberedList',indices=list(range(1,9))),dict(type='paragraph',indices=[9]),dict(type='heading',indices=[10]),dict(type='paragraph',indices=[11]),dict(type='visual',blockId='physics9-leastcount-general'),dict(type='paragraph',indices=[12]),dict(type='visual',blockId='physics9-leastcount-numeric'),dict(type='heading',indices=[13]),dict(type='paragraph',indices=[14]),dict(type='paragraph',indices=[15]),dict(type='numberedList',indices=[16])]
page['comparison']='Fresh rendered-page inspection: checked eight numbered figure explanations and corresponding pointers, A/B jaw labels and depth rod; restored lower metric and sliding scales, screw and inch markings in code. Preserved 0.1mm typography, separate Method 2 paragraphs, general and numeric fraction bars, zero-error heading/body and grammatical source zeros does not coincide. Step 1 retained alone; following steps remain on next page. No zero-error correction or question solution invented.'
(OUT/'physics-page-021.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
