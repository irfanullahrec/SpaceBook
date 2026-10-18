import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[19]
page.update(id='cls9-physics-page-020',status='corrected-fresh-review-with-unresolved-visual-detail',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s.update(heading='1.6.2 VERNIER CALLIPER',headingUrdu='1.6.2 ورنیئر کیلیپر',headingPashto='1.6.2 ورنییر کالیپر')
s['paras'][0]['text']='‘A device used to measure a fraction of smallest scale division by sliding another scale over it is called vernier calliper’. It is a device used to measure small length accurately upto 0.1mm or 0.01cm.'
s['paras'][6]['text']='A vernier (sliding) scale which has markings of some multiple of the marking on the main scale. The vernier scale usually has length of 9 mm and is divided equally into 10 divisions (thus separation between two lines on vernier scale is 9/10 mm = 0.9 mm).'
s['paras'][12]['text']='Least Count = One Main Scale Division – One Vernier Scale Division'
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 290" role="img" aria-label="Vernier calliper with internal and external jaws, main and sliding scales, locking screw, thumbwheel and depth rod"><defs><linearGradient id="physics9-calliper-metal"><stop stop-color="#92908f"/><stop offset=".5" stop-color="#e8e0da"/><stop offset="1" stop-color="#9e9795"/></linearGradient></defs><g fill="url(#physics9-calliper-metal)" stroke="#6f6865" stroke-width="2"><path d="M62 104H750V162H61V276Q36 278 31 250V107L59 41L68 107Z"/><path d="M138 106V47L150 35V108H215V167H150V263L126 279V163H95V109Z"/><rect x="182" y="158" width="58" height="13"/><circle cx="250" cy="177" r="18"/><rect x="151" y="79" width="13" height="28"/><circle cx="158" cy="76" r="11"/><rect x="751" y="127" width="59" height="6"/></g><rect x="134" y="105" width="82" height="57" rx="25" fill="#ddd8d4" stroke="#7c7470"/>'
for i in range(121):
 x=236+i*3.6;svg+=f'<path d="M{x} 111v{22 if i%10==0 else 13 if i%5==0 else 8} M{x} 158v-{20 if i%10==0 else 12 if i%5==0 else 7}" stroke="#35322f"/>'
for i in range(4):svg+=f'<text x="{248+i*138}" y="143" font-size="15">{i+2}</text>'
for i in range(9):svg+=f'<text x="{240+i*51}" y="153" font-size="14">{i+4}</text>'
for i in range(11):svg+=f'<path d="M{143+i*6} 109v{13 if i%5==0 else 8}M{143+i*6} 157v-{13 if i%5==0 else 8}" stroke="#35322f"/>'
svg+='<g fill="#35322f" font-family="sans-serif" font-size="16"><text x="147" y="138">2</text><text x="170" y="130">1</text><text x="188" y="138">3</text><text x="680" y="144" font-size="10">STAINLESS</text><text x="692" y="155" font-size="10">STEEL</text></g></svg>'
note='<p class="source-review-note">Editorial source-review note: the source photograph’s tiny unit marks, maker mark and some scale digits remain indistinct at 4×. These details are not certified; the drawing preserves the visible instrument structure.</p>'
v=dict(type='vector',id='physics9-calliper-source',svg=svg+note,svgUrdu=svg+'<p class="source-review-note" dir="rtl">ماخذ کے جائزے کا ادارتی نوٹ: تصویر کی باریک اکائیوں، سازندہ کے نشان اور بعض پیمانے کے ہندسوں کی تصدیق 4× پر بھی نہیں ہو سکی۔</p>',svgPashto=svg+'<p class="source-review-note" dir="rtl">د سرچینې د کتنې یادونه: د انځور کوچنۍ واحد نښې، د جوړوونکي نښه او د مقیاس ځینې رقمونه په 4× کې هم روښانه نه دي.</p>')
s['blocks']=[v]
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='visual',blockId=v['id']),dict(type='paragraph',indices=[2]),dict(type='heading',indices=[3]),dict(type='paragraph',indices=[4]),dict(type='heading',indices=[5]),dict(type='paragraph',indices=[6]),dict(type='heading',indices=[7]),dict(type='paragraph',indices=[8]),dict(type='paragraph',indices=[9]),dict(type='heading',indices=[10]),dict(type='paragraph',indices=[11]),dict(type='paragraph',indices=[12])]
page['definitions']=[dict(term='Vernier calliper',definition=s['paras'][0]['text'],urdu=s['paras'][0]['urdu'],pashto=s['paras'][0]['pashto'],sourcePdfPage=20,sourcePrintedPage=15),dict(term='Vernier constant',definition=s['paras'][8]['text'],urdu=s['paras'][8]['urdu'],pashto=s['paras'][8]['pashto'],sourcePdfPage=20,sourcePrintedPage=15)]
page['unresolvedItems']=['Calliper photograph tiny unit/maker marks and some scale digits remain indistinct in 4x local crop; visible multilingual editorial note retained. Do not certify exact scale reproduction.']
page['comparison']='Fresh local page and 4x instrument crop inspection. Preserved quoted definition, source upto and compact 0.1mm/0.01cm, jaw A wording, original subheading order, method 1 formula. Replaced invented annotated schematic with closer unannotated code drawing of instrument, jaws, screws, depth rod and visible scales. Tiny remaining photograph markings explicitly unresolved rather than guessed.'
(OUT/'physics-page-020.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
