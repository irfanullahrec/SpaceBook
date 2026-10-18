import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[28]
page.update(id='cls9-physics-page-029',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s,k=page['sections']
s['paras'][0]['text']=s['paras'][0]['text'].removeprefix('4. ZEROs to the right of the significant figure ')
s['paras'][0]['urdu']='بامعنی بھی ہو سکتے ہیں اور نہیں بھی۔ اعشاری کسروں میں اعشاری کسر کے دائیں طرف صفر بامعنی ہوتے ہیں۔ مثلاً 7.400 میں 4 بامعنی ہندسے ہیں۔ تاہم اگر عدد صحیح ہو تو بامعنی ہندسوں کی تعداد پیمائشی آلے کی درستگی سے معلوم ہوتی ہے۔ مثلاً 80,000 میں 1، 2 یا حتیٰ کہ 5 بامعنی ہندسے ہو سکتے ہیں۔'
s['paras'][0]['pashto']='بامعنی کېدای شي یا نه وي. په اعشاري کسرونو کې د اعشاري کسر ښي لوري ته صفرونه بامعنی دي. د بېلګې په توګه، په 7.400 کې 4 بامعنی شمېرې دي. خو که عدد صحیح وي، د بامعنی شمېرو شمېر د اندازه کولو د وسیلې له دقت څخه معلومېږي. د بېلګې په توګه، په 80,000 کې 1، 2 یا حتی 5 بامعنی شمېرې کېدای شي.'
s['paras'][5]['text']=s['paras'][5]['text'].replace('next one, e.g.','next one. e.g.')
s['paras'][6]['text']=s['paras'][6]['text'].replace('round off 5, e.g.','round off 5. e.g.')
s['paras']=s['paras'][:7]
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 470" role="img" aria-label="Rounding off 2.6574818 to 2.66 in successive steps"><g font-family="sans-serif" fill="currentColor" text-anchor="middle"><text x="110" y="25" font-size="21">ROUNDING OFF</text><text x="110" y="55" font-size="24">2.6574818</text>'
values=['2.6574818','2.657482','2.65748','2.6575','2.658','2.66']
for i,v in enumerate(values):
 y=100+i*68;svg+=f'<text x="110" y="{y}" font-size="24">{v}</text>'
 if i<5:
  end=110+len(v)*6;svg+=f'<path d="M{end-6} {y-22}q18 -18 13 25" fill="none" stroke="#9f3453" stroke-width="2"/><path d="M{end-9} {y-12}l8 13" stroke="#9f3453" stroke-width="2"/><path d="M110 {y+13}v20" stroke="currentColor" stroke-width="3"/>'
svg+='</g></svg>'
s['blocks']=[dict(type='vector',id='physics9-rounding-sequence',svg=svg,svgUrdu=svg.replace('ROUNDING OFF','گول کرنا'),svgPashto=svg.replace('ROUNDING OFF','ګردول'),sourceWidthRatio=.17)]
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='numberedList',indices=[1]),dict(type='heading',indices=[2]),dict(type='numberedList',indices=[3,4,5,6]),dict(type='visual',blockId='physics9-rounding-sequence')]
k['sourceLayout']=[dict(type='paragraph',indices=[i]) for i in range(len(k['paras']))]
page['comparison']='Fresh page plus 4x rounding crop review: preserved rule-4 continuation without repeating page-28 fragment, source electron mass and rule-5 grammar, four rounding rules and all nine key points. Reconstructed missing narrow rounding diagram with curved drop marks and progression 2.6574818 → 2.657482 → 2.65748 → 2.6575 → 2.658 → 2.66; corrected old mistaken second value. Native visual restricted to 17% source column.'
(OUT/'physics-page-029.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
