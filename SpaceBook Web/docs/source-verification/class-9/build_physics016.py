import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[15]
page.update(id='cls9-physics-page-016',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
old=s['paras']
def pair(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto)
s['paras']=[old[0],old[1],old[2],old[3],old[4],pair('Solution','حل','حل'),old[5],pair('For Standard form / scientific notation we can write the term as','معیاری صورت / سائنسی طرزِ اظہار کے لیے ہم اسے یوں لکھ سکتے ہیں','د معیاري بڼې / علمي لیکنې لپاره دا داسې لیکلای شو'),pair('In order to get mantissa (M) in which the 1st digit before the decimal is non-zero, we have to move the decimal 7 digits towards left. Therefore, the power of 10 will be positive 7, that is','ایسا مینٹیسا (M) حاصل کرنے کے لیے، جس میں اعشاری نقطے سے پہلے پہلا ہندسہ غیر صفر ہو، اعشاری نقطہ 7 ہندسے بائیں طرف منتقل کرنا ہوگا۔ لہٰذا 10 کی قوت مثبت 7 ہوگی، یعنی','د داسې مانتیسا (M) د ترلاسه کولو لپاره چې له اعشاري ټکي مخکې لومړی رقم ناصفر وي، اعشاري ټکی باید 7 رقمونه چپ لوري ته ولېږدوو. نو د 10 توان به مثبت 7 وي، یعنې'),pair('Answer','جواب','ځواب'),pair('EXTENSION EXERCISE 1.2','اضافی مشق 1.2','اضافي تمرین 1.2'),pair(old[10]['text'].removeprefix('EXTENSION EXERCISE 1.2: '),old[10]['urdu'].removeprefix('اضافی مشق 1.2: '),old[10]['pashto'].removeprefix('اضافي تمرین 1.2: ')),old[11],old[12],old[13],old[14]]
equation=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 105" role="img" aria-label="One year multiplied by four conversion-factor fractions, with year, day, hour and minute units cancelled"><g fill="currentColor" font-family="serif" font-size="23"><text x="10" y="60">1y = 1y ×</text>']
for i,(top,bottom) in enumerate([('365d','1y'),('24h','1d'),('60m','1h'),('60s','1m')]):
    x=160+i*110
    equation.append(f'<text x="{x}" y="33">{top}</text><text x="{x+13}" y="80">{bottom}</text><path d="M{x-4} 44H{x+73}" stroke="currentColor" stroke-width="2"/>')
    if i<3:
        equation.append(f'<text x="{x+83}" y="61">×</text>')
equation.append('</g><g stroke="#9f1239" stroke-width="2" fill="none"><path d="M81 65L97 42M196 36L213 13M187 84L203 61M295 36L311 13M297 84L313 61M405 36L421 13M407 84L423 61M517 84L533 61"/></g></svg>')
def simple(content,identity):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 95" role="img" aria-label="{identity}"><text x="15" y="58" fill="currentColor" font-family="serif" font-size="27">{content}</text></svg>'
normal='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 95" role="img" aria-label="1 year equals 31536000.0 times ten to the power zero seconds"><g font-family="serif" fill="currentColor" font-size="27"><text x="15" y="58">1y =</text><text x="105" y="58">31536000.0</text><text x="275" y="58">×</text><text x="310" y="58">10</text><text x="340" y="37" font-size="18">0</text><text x="365" y="58">s</text></g><path d="M105 68'+('q7 13 14 0'*7)+'" fill="none" stroke="#0284c7" stroke-width="2"/></svg>'
answer='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 95" role="img" aria-label="1 year equals 3.1536000 times ten to the power seven seconds"><g font-family="serif" fill="currentColor" font-size="27"><text x="15" y="58">1y =</text><text x="105" y="58">3.1536000</text><text x="260" y="58">×</text><text x="290" y="58">10</text><text x="320" y="37" font-size="18">7</text><text x="345" y="58">s</text></g></svg>'
visuals=[('conversion',''.join(equation)),('multiplied',simple('or 1y = 1 × 365 × 24 × 60 × 60 s','Multiplying the four conversion factors')),('seconds',simple('or 1y = 31536000 s','Seconds in one year')),('normal',normal),('answer',answer)]
s['blocks']=[b for b in s['blocks'] if b['type']!='formula']
for name,svg in visuals:
    s['blocks'].append(dict(type='formula',id='physics9-example12-'+name,svg=svg,svgUrdu=svg.replace('>or 1y','>یا 1y'),svgPashto=svg.replace('>or 1y','>یا 1y'),sourcePdfPage=16,printedPage=11))
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='heading',indices=[1]),dict(type='paragraph',indices=[2]),dict(type='heading',indices=[3]),dict(type='paragraph',indices=[4]),dict(type='heading',indices=[5]),dict(type='paragraph',indices=[6]),dict(type='visual',blockId='physics9-example12-conversion'),dict(type='visual',blockId='physics9-example12-multiplied'),dict(type='visual',blockId='physics9-example12-seconds'),dict(type='paragraph',indices=[7]),dict(type='visual',blockId='physics9-example12-normal'),dict(type='paragraph',indices=[8]),dict(type='visual',blockId='physics9-example12-answer'),dict(type='heading',indices=[9]),dict(type='heading',indices=[10]),dict(type='paragraph',indices=[11]),dict(type='heading',indices=[12]),dict(type='paragraph',indices=[13]),dict(type='heading',indices=[14]),dict(type='paragraph',indices=[15])]
n=page['numericals'][0]
n['formula']=n['formula'].replace('60 min','60 m').replace('1 min','1 m')
n['solution']=s['paras'][6]['text']+'\n\n'+n['formula']+'\n\nor 1 y = 1 × 365 × 24 × 60 × 60 s\n\nor 1 y = 31536000 s\n\n'+s['paras'][7]['text']+'\n\n1 y = 31536000.0 × 10⁰ s\n\n'+s['paras'][8]['text']+'\n\n1 y = 3.1536000 × 10⁷ s\n\nAnswer'
n.update(givenOrigin='extracted from source statement',requiredOrigin='extracted from source statement',answerOrigin='textbook')
page['sourceClarifications']=[dict(printedNotation='m in conversion-factor formula; min in surrounding prose',note='Source uses m as the minute abbreviation inside the displayed formula while prose uses min. Original notation retained.')]
page['comparison']='Fresh visual comparison of continuation sentence, Earth-mass assignment and full comma-grouped quantity, Example 1.2, all five printed calculation lines, seven decimal-shift marks, exact answer precision, leap-year extension question, week assignment and Example 1.3 question including H₂ and 0.000,000,000,074. Restored four actual fraction bars and eight unit-cancellation strokes; retained printed m rather than silently expanding to min. Removed fabricated semicolon joining separate equation lines and em dash before Answer. No assignment/extension solutions added.'
(OUT/'physics-page-016.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
