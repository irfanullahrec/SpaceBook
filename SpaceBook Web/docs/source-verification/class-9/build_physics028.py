import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[27]
page.update(id='cls9-physics-page-028',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
def pair(t,u,p):return dict(text=t,urdu=u,pashto=p)
s,q=page['sections'];old=s['paras']
s['paras']=[pair('or','یا','یا'),pair('therefore','لہٰذا','نو'),pair('Answer','جواب','ځواب'),old[2],old[3]]
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 145" role="img" aria-label="Example 1.6 continuation, conversion fraction with cancelled cubic centimetres"><g font-family="sans-serif" font-size="26" fill="currentColor"><text x="12" y="57">10³ cm³ = 10³ cm³ ×</text><text x="330" y="31">10⁻⁶ m³</text><text x="350" y="87">1cm³</text><text x="100" y="137">10³ cm³ = 10⁻³ m³</text></g><path d="M326 48H435" stroke="currentColor" stroke-width="2"/><path d="M202 62l41 -28M371 92l37 -32" stroke="#a52b31" stroke-width="2"/></svg>'
s['blocks']=[dict(type='formula',id='physics9-example16-continuation',svg=svg,svgUrdu=svg,svgPashto=svg,sourceWidthRatio=.73)]
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='visual',blockId='physics9-example16-continuation'),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[2]),dict(type='heading',indices=[3]),dict(type='paragraph',indices=[4])]
q.update(heading='1.7 SIGNIFICANT FIGURES',headingUrdu='1.7 بامعنی ہندسے',headingPashto='1.7 بامعنی شمېرې')
q['paras'].insert(7,pair(page['continuedParagraph'],'4. بامعنی ہندسے کے دائیں طرف صفر','4. د بامعنی شمېرې ښي لوري ته صفرونه'))
q['paras'][1]['text']=q['paras'][1]['text'].replace('up to 67','up to 67')
calc='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 145 250" role="img" aria-label="Calculator showing 1.2345678"><rect x="8" y="6" width="130" height="235" rx="6" fill="#262431" stroke="#111"/><text x="20" y="24" font-family="sans-serif" font-size="10" fill="#eee">Canon</text><rect x="91" y="15" width="34" height="16" fill="#686273"/><rect x="18" y="43" width="111" height="44" fill="#c8c2d5"/><text x="23" y="75" font-family="monospace" font-size="19" fill="#111">1.2345678</text>'
for row in range(6):
 for col in range(5):
  x,y=18+col*22,103+row*21;calc+=f'<rect x="{x}" y="{y}" width="17" height="15" rx="2" fill="#514d5f"/><text x="{x+8}" y="{y+11}" font-family="sans-serif" font-size="9" text-anchor="middle" fill="#eee">{str((5-row)*3+col) if 2<=row<=4 and col<3 else ""}</text>'
calc+='</svg>'
q['blocks']=[dict(type='illustration',id='physics9-calculator',svg=calc,svgUrdu=calc,svgPashto=calc,sourceWidthRatio=.16)]
q['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='quotation',indices=[2]),dict(type='heading',indices=[3]),dict(type='numberedList',indices=[4,5,6,7]),dict(type='heading',indices=[8]),dict(type='paragraph',indices=[9]),dict(type='visual',blockId='physics9-calculator'),dict(type='paragraph',indices=[10])]
page['definitions']=[dict(term='Significant figures',definition=q['paras'][2]['text'],urdu=q['paras'][2]['urdu'],pashto=q['paras'][2]['pashto'],sourcePdfPage=28,sourcePrintedPage=23)]
page['numericals'][0]['solution']=page['numericals'][0]['solution'].replace(' — Answer','\nAnswer')
previous=OUT/'physics-page-027.json';p=json.loads(previous.read_text(encoding='utf-8'));p['numericals']=[page['numericals'][0]];previous.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
page['comparison']='Fresh rendered-page review: continued Example 1.6 preserved with fraction, two cubic-centimetre cancellation marks and standalone answer. Verified significant-figure prose, definition, first three rules and visible rule-4 fragment. Restored small calculator displaying 1.2345678; calculator box text and erroneous/printed numerical precision retained. Example record synchronized to reviewed pages 27–28.'
(OUT/'physics-page-028.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
