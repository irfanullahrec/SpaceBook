import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[21]
page.update(id='cls9-physics-page-022',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s['paras'][0].update(text='Figure 1.2 Vernier Calliper',urdu='شکل 1.2 ورنیئر کیلیپر',pashto='شکل 1.2 ورنییر کالیپر')
s['paras'][2]['text']=s['paras'][2]['text'].replace('The required length','Thus the required length')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 400" role="img" aria-label="Figure 1.2 Vernier Calliper with solid cylinder between jaws A and B and magnified view"><defs><clipPath id="physics9-reading-circle"><circle cx="459" cy="285" r="95"/></clipPath></defs><g stroke="#20242b" stroke-width="3"><path d="M70 112H640V155H109V315L79 298L65 198V116L102 112V51Q130 45 130 83V112Z" fill="#f5f3ef"/><path d="M183 108V62Q183 47 206 46V98L221 108H297V166H219L197 314L176 322V152H154V112Z" fill="#b6d0e1"/><circle cx="141" cy="267" r="48" fill="#899097"/><circle cx="246" cy="140" r="36" fill="none"/></g><g stroke="#222">'
for i in range(101):
 x=152+i*4.8
 svg+=f'<path d="M{x} 153v-{28 if i%10==0 else 17 if i%5==0 else 10}"/>'
svg+='<g fill="#222" font-family="sans-serif" font-size="15">'
for i in range(11):svg+=f'<text x="{151+i*48}" y="120">{i}</text>'
svg+='</g></g><path d="M258 185L310 222L320 209L349 254L302 244L310 235L249 201Z" fill="#b52c6c" stroke="#6d1c44" stroke-width="3"/><g font-family="sans-serif" fill="#222" font-size="22"><text x="83" y="349">A</text><text x="187" y="349">B</text><text x="270" y="291" font-size="17">Magnified</text><text x="290" y="313" font-size="17">view</text></g><g clip-path="url(#physics9-reading-circle)"><rect x="361" y="188" width="197" height="192" fill="#f8f7f1"/><rect x="361" y="318" width="197" height="64" fill="#72b9dd"/><path d="M363 212H555" stroke="#a93668" stroke-width="3"/><text x="404" y="274" font-family="sans-serif" font-size="36">2</text><text x="544" y="274" font-family="sans-serif" font-size="36">3</text>'
for i in range(15):svg+=f'<path d="M{363+i*13} 318v-{77 if i%10==4 else 38 if i%5==4 else 18}" stroke="#222" stroke-width="2"/>'
# Vernier zero lies 0.6 main divisions before the 2cm mark; sixth aligns.
for i in range(11):svg+=f'<path d="M{407.2+i*11.7} 318v{32 if i%5==0 else 22}" stroke="#222" stroke-width="2"/>'
svg+='</g><circle cx="459" cy="285" r="95" fill="none" stroke="#20242b" stroke-width="3"/></svg>'
s['blocks']=[dict(type='vector',number='1.2',id='physics9-calliper-figure12',svg=svg,svgUrdu=svg.replace('Magnified','بڑا کیا ہوا').replace('>view<','>منظر<'),svgPashto=svg.replace('Magnified','لوی شوی').replace('>view<','>لید<'),sourceWidthRatio=.96,sourceSizing='Almost full textbook content-column width; maintain original aspect ratio.')]
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='visual',blockId='physics9-calliper-figure12'),dict(type='numberedList',indices=[1,2,3,4]),dict(type='paragraph',indices=[5]),dict(type='heading',indices=[6]),dict(type='list',indices=[7,8])]
page['comparison']='Fresh local rendered-page review: replaced invented scale-only diagram and extra equation labels with complete Figure 1.2 instrument, cylinder, jaws A/B, arrow and magnified circular reading. Main 2cm mark and sixth vernier alignment retained; translated Magnified view label. Restored omitted Thus in step 3. Preserved steps 2–5, result and two lab bullets with source wording. Figure width limited to printed content-column proportions.'
(OUT/'physics-page-022.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
