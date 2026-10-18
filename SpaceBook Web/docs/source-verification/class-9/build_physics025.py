import json,re
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[24]
page.update(id='cls9-physics-page-025',status='corrected-fresh-review-with-unresolved-scale-detail',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s,b=page['sections'];old=s['paras']
def pair(t,u,p):return dict(text=t,urdu=u,pashto=p)
s['paras']=[pair('LAB WORK','تجربہ گاہ کا کام','لابراتواري کار'),pair('Measure the thickness of a metal strip or a wire by using a screw gauge.','سکرو گیج سے دھات کی پٹی یا تار کی موٹائی ناپیں۔','په سکرو ګېج د فلزي پټې یا سیم پنډوالی اندازه کړئ.')]+old[1:]
s['paras'][2]['text']='ACTIVITY THICKNESS OF PHYSICS BOOK AND PAGE'
s['paras'][5]['text']='Which of the following is the accurate device for measuring length :'
s['paras'][8]['text']='ACTIVITY READINGS OF VERNIER CALLIPERS AND SCREW GAUGE'
def vernier(start,zero):
 out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 125"><rect x="1" y="1" width="338" height="123" rx="8" fill="none" stroke="currentColor"/><g stroke="currentColor" fill="currentColor" font-family="sans-serif" font-size="15">'
 for i in range(56):out+=f'<path d="M{20+i*5.6:.2f} 58v-{24 if i%10==0 else 15 if i%5==0 else 8}"/>'
 for i in range(6):out+=f'<text x="{20+i*56}" y="24" text-anchor="middle">{start+i}</text>'
 for i in range(11):out+=f'<path d="M{zero+i*5.04:.2f} 58v{20 if i%10==0 else 12 if i%5==0 else 7}"/>'
 return out+f'<path d="M10 58H330M{zero-5} 58V89H{zero+55}V58M45 115H295" fill="none"/></g></svg>'
def grid(items,id):
 out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1020 160" role="img" aria-label="Three unanswered textbook instrument-reading exercises">'
 for i,svg in enumerate(items):
  view=re.search(r'viewBox="([^"]+)"',svg).group(1)
  inner=re.sub(r'^<svg[^>]*>|</svg>$','',svg)
  out+=f'<svg x="{i*340}" width="340" height="155" viewBox="{view}">{inner}</svg>'
 out+='</svg>'
 return dict(type='vector',id=id,svg=out,svgUrdu=out,svgPashto=out,sourceWidthRatio=.99)
v=grid([vernier(0,126),vernier(2,139),vernier(1,105)],'physics9-vernier-exercises')
m=grid([x['svg'] for x in s['blocks'][3:6]],'physics9-micrometer-exercises')
note='<p class="source-review-note">Editorial source-review note: fine vernier tick alignment remains uncertain in the scanned exercises. No reading answers are supplied or certified.</p>'
v['svg']+=note;v['svgUrdu']+='<p dir="rtl">ماخذ کے جائزے کا نوٹ: اسکین میں ورنیئر کے باریک نشانات کی مطابقت غیر یقینی ہے؛ قرأت کے جوابات نہیں دیے گئے۔</p>';v['svgPashto']+='<p dir="rtl">د سرچینې یادونه: په سکین کې د ورنییر د کوچنیو نښو برابرښت ناڅرګند دی؛ د لوستنې ځوابونه نه دي ورکړل شوي.</p>'
s['blocks']=[v,m]
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[2]),dict(type='paragraph',indices=[3]),dict(type='heading',indices=[4]),dict(type='paragraph',indices=[5]),dict(type='numberedList',indices=[6,7]),dict(type='heading',indices=[8]),dict(type='paragraph',indices=[9]),dict(type='visual',blockId=v['id']),dict(type='paragraph',indices=[10]),dict(type='visual',blockId=m['id'])]
b.update(heading='1.6.4 PHYSICAL BALANCE',headingUrdu='1.6.4 طبعی ترازو',headingPashto='1.6.4 فزیکي تله')
b['paras'].append(pair(page['continuedParagraph'],'طبعی ترازو ایک عام ترازو ہی ہے جس میں دو پلڑے ہوتے ہیں اور','فزیکي تله یوه عادي تله ده چې دوه پلې لري او'))
b['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='paragraph',indices=[1])]
page['unresolvedItems']=['Fine vernier exercise tick alignment remains uncertain after 4x source crop. Retained visible note and no answer certification.']
page['comparison']='Fresh page and 4x scale crop inspection: restored separate lab heading/procedure, original activity labels, A/B options and final visible continuation paragraph. Six scale exercises restored in source three-column rows, not six large successive images, retaining labels and unanswered lines. Source fine vernier alignment explicitly unresolved; physical balance continuation awaits next page.'
(OUT/'physics-page-025.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
