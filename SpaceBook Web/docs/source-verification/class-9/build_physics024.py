import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[23]
page.update(id='cls9-physics-page-024',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s['paras'][10]['text']=s['paras'][10]['text'].replace('on the thimble does','on the thimble scale does')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 290" role="img" aria-label="Figure 1.4 Screw Gauge: small sleeve view, green enlargement arrow, magnified sleeve and thimble scales"><defs><linearGradient id="physics9-sleeve-metal"><stop stop-color="#717b96"/><stop offset=".5" stop-color="#d5d5df"/><stop offset="1" stop-color="#7b7a95"/></linearGradient></defs><g fill="url(#physics9-sleeve-metal)" stroke="#353945" stroke-width="2"><rect x="8" y="127" width="116" height="18"/><path d="M120 110H185V235H120Z"/><rect x="180" y="112" width="75" height="68"/><rect x="255" y="114" width="35" height="71"/><circle cx="152" cy="132" r="12" fill="#222"/><path d="M150 145l-14 38" stroke="#eee" stroke-width="10"/><rect x="185" y="103" width="76" height="78" fill="none" stroke="#111"/><rect x="420" y="15" width="323" height="260" fill="#fff"/><path d="M422 46L448 40V253L425 272Z"/><path d="M450 49H578V249H450Z"/><path d="M578 37L739 20V263L579 245Z"/></g><path d="M274 131H352V114L402 148L353 178V160H274Z" fill="#63a693" stroke="#3f8475" stroke-width="2"/><g stroke="#222" stroke-width="2"><path d="M449 137H582"/>'
for i in range(12):
 x=490+i*10
 svg+=f'<path d="M{x} 125v-{31 if i%5==0 else 19} M{x} 153v{24 if i%5==0 else 18}"/>'
for i in range(20,36):
 y=137-(i-28)*11
 svg+=f'<path d="M581 {y}l{43 if i%5==0 else 30} -3"/>'
svg+='</g><g font-family="sans-serif" font-size="23" fill="#111"><text x="480" y="93">0</text><text x="539" y="93">5</text><text x="694" y="45">35</text><text x="694" y="100">30</text><text x="694" y="155">25</text><text x="694" y="210">20</text></g><g stroke="#222" stroke-width="1">'
for i in range(10):svg+=f'<path d="M{195+i*5} 145v-12"/>'
for i in range(6):svg+=f'<path d="M250 {123+i*9}h15"/>'
svg+='</g><g font-family="sans-serif" font-size="10" fill="#111"><text x="201" y="126">0</text><text x="236" y="126">5</text><text x="266" y="127">30</text><text x="266" y="151">25</text><text x="266" y="175">20</text></g></svg>'
s['blocks']=[dict(type='vector',number='1.4',id='physics9-screwgauge-figure14',svg=svg,svgUrdu=svg,svgPashto=svg,sourceWidthRatio=.98,sourceSizing='Printed figure spans almost the full content column; preserve aspect ratio.')]
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='visual',blockId='physics9-screwgauge-figure14'),dict(type='paragraph',indices=[1]),dict(type='numberedList',indices=[2,3,4,5,6]),dict(type='paragraph',indices=[7]),dict(type='paragraph',indices=[8]),dict(type='heading',indices=[9]),dict(type='paragraph',indices=[10])]
page['comparison']='Fresh rendered-page inspection: restored original two-part Figure 1.4 small instrument view, selection rectangle, green arrow and magnified sleeve/thimble, including 0/5 and 20/25/30/35 source numbers with datum at division 28. Removed invented 28 label and equation inside diagram. Kept figure content-column width; corrected missing scale in zero-error paragraph. Five source steps, standalone equation, result and box remain paired and distinct.'
(OUT/'physics-page-024.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
