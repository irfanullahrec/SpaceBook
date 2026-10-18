import json
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[11]
page.update(id='cls9-physics-page-012',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s,q=page['sections']
labels=[dict(text='Battery and starter',urdu='بیٹری اور سٹارٹر',pashto='بیټرۍ او سټارټر'),dict(text='Engine and Coolant',urdu='انجن اور ٹھنڈا کرنے والا سیال',pashto='انجن او سړوونکی مایع'),dict(text='Back view mirrors',urdu='پیچھے دیکھنے والے آئینے',pashto='د شا لید هندارې'),dict(text='Spinning motion of the wheels, tires',urdu='پہیوں اور ٹائروں کی گھومنے کی حرکت',pashto='د څرخونو او ټایرونو څرخېدونکی حرکت'),dict(text='Back view mirrors',urdu='پیچھے دیکھنے والے آئینے',pashto='د شا لید هندارې')]
def svg(field):
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 350" role="img" aria-labelledby="physics9-car-title-'+field+'" style="max-width:100%;height:auto"><title id="physics9-car-title-'+field+'">Physics in car: battery, engine, wheel rotation and two source mirror callouts</title><rect width="860" height="350" fill="#222c40"/><g fill="#a5c9ef" fill-opacity=".45" stroke="#b6dcff" stroke-width="3"><path d="M226 237L257 171L372 136L407 95L555 80L649 110L667 164L627 210L473 265L285 278Z"/><path d="M380 141L419 107L547 94L611 121L518 158Z"/><path d="M234 235L367 198L470 251L289 270Z"/><path d="M288 204L351 180L397 201L330 226Z"/><path d="M403 189L524 149L604 177L483 219Z"/><path d="M280 188L311 178L326 191L294 204Z"/><ellipse cx="373" cy="264" rx="31" ry="40" fill="#334155"/><ellipse cx="627" cy="191" rx="26" ry="37" fill="#334155"/><path d="M372 231V295M345 264H402M353 239L395 288M351 286L396 243M627 158V223M603 191H650" fill="none"/><path d="M490 146L512 137L520 150L497 160Z"/></g><g stroke="#f8fafc" stroke-width="2" fill="none"><path d="M180 84L296 188M180 160L340 202M182 265L265 236M709 105L628 180M683 270L507 150"/></g>']
    positions=[(15,58,180,50),(15,134,180,50),(15,239,180,50),(675,74,180,67),(607,254,222,52)]
    for label,(x,y,w,h) in zip(labels,positions):
        text=escape(label[field])
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="#fff" stroke="#334155"/><foreignObject x="{x+5}" y="{y+4}" width="{w-10}" height="{h-8}"><div xmlns="http://www.w3.org/1999/xhtml" style="font-size:14px;text-align:center;line-height:1.4;direction:{"ltr" if field=="text" else "rtl"}">{text}</div></foreignObject>')
    out.append('</svg>')
    return ''.join(out)
diagram=dict(type='vectorDiagram',id='physics9-car-007',svg=svg('text'),svgUrdu=svg('urdu'),svgPashto=svg('pashto'),labels=labels,sourcePdfPage=12,printedPage=7)
s['blocks']=[diagram]
s['paras'].pop(2)
s['paras'][2]=dict(text='Measurement',urdu='پیمائش',pashto='اندازه کول')
s['paras'].append(dict(text='Recall',urdu='یاد کریں',pashto='را په یاد کړئ'))
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='visual',blockId='physics9-car-007'),dict(type='heading',indices=[2,5]),dict(type='paragraph',indices=[3]),dict(type='paragraph',indices=[4])]
q.update(heading='1.2 PHYSICAL QUANTITIES',headingUrdu='1.2 طبیعی مقداریں',headingPashto='1.2 فزیکي کمیتونه')
q['paras'][3]=dict(text='CAN YOU TELL?',urdu='کیا آپ بتا سکتے ہیں؟',pashto='آیا ویلای شئ؟')
q['paras'].append(dict(text='Are there quantities which we can not measure?',urdu='کیا ایسی مقداریں ہیں جنہیں ہم ناپ نہیں سکتے؟',pashto='آیا داسې کمیتونه شته چې موږ یې اندازه کولای نه شو؟'))
q['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='paragraph',indices=[2]),dict(type='quotation',indices=[3,8]),dict(type='heading',indices=[4]),dict(type='paragraph',indices=[5]),dict(type='heading',indices=[6]),dict(type='paragraph',indices=[7])]
page['definitions']=[]
for term,p in [('Measurement',s['paras'][3]),('Unit',s['paras'][4]),('Physical Quantity',q['paras'][0]),('Base Quantities',q['paras'][5]),('Derived Quantities',q['paras'][7])]:
    page['definitions'].append(dict(term=term,definition=p['text'],urdu=p['urdu'],pashto=p['pashto'],sourcePdfPage=12,sourcePrintedPage=7))
activity=page['activities'][0]
activity.update(diagramSvg=diagram['svg'],diagramSvgUrdu=diagram['svgUrdu'],diagramSvgPashto=diagram['svgPashto'],sourceLabels=labels)
page['comparison']='Fresh visual comparison of Activity 1.1, question, all five car labels/arrows, recall definition, Unit paragraph, physical-quantity definition and paragraphs, question callout, and both category definitions. Corrected missing second Back view mirrors label and preserved its printed arrow to the front lamp rather than silently changing the book. Replaced fabricated semicolon label paragraph with paired SVG labels in all three languages. Source definitions synchronized to existing SLO dictionary records; no answers added.'
(OUT/'physics-page-012.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
