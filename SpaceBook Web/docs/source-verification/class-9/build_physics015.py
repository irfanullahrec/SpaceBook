import json
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[14]
page.update(id='cls9-physics-page-015',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
old=s['paras']
def pair(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto)
s['paras']=[old[0],old[2],old[3],old[4],old[5],old[6],old[7],old[8],pair('Solution','حل','حل'),pair('For Standard form / scientific notation we can write the term as','معیاری صورت / سائنسی طرزِ اظہار کے لیے ہم اسے یوں لکھ سکتے ہیں','د معیاري بڼې / علمي لیکنې لپاره دا داسې لیکلای شو'),pair('For Standard form / scientific notation in order to get mantissa (M) in which the 1st digit before the decimal is non-zero, we have to move the decimal 8 digits towards left. Therefore, the power of 10 will be positive 8, that is','معیاری صورت / سائنسی طرزِ اظہار میں ایسا مینٹیسا (M) حاصل کرنے کے لیے، جس میں اعشاری نقطے سے پہلے پہلا ہندسہ غیر صفر ہو، اعشاری نقطہ 8 ہندسے بائیں طرف منتقل کرنا ہوگا۔ لہٰذا 10 کی قوت مثبت 8 ہوگی، یعنی','په معیاري بڼه / علمي لیکنه کې د داسې مانتیسا (M) د ترلاسه کولو لپاره چې له اعشاري ټکي مخکې لومړی رقم ناصفر وي، اعشاري ټکی باید 8 رقمونه چپ لوري ته ولېږدوو. نو د 10 توان به مثبت 8 وي، یعنې'),pair('Answer','جواب','ځواب'),pair('EXTENSION EXERCISE 1.1','اضافی مشق 1.1','اضافي تمرین 1.1'),pair('Why we used the word average in problem statement.','سوال کے بیان میں اوسط کا لفظ کیوں استعمال کیا گیا ہے؟','د مسئلې په بیان کې د منځني کلمه ولې کارول شوې ده؟')]
def equation(kind,field):
    if kind=='standard':
        labels={'text':['number (N)','mantissa (M)','exponent (n)'],'urdu':['عدد (N)','مینٹیسا (M)','ایکسپوننٹ (n)'],'pashto':['عدد (N)','مانتیسا (M)','توان (n)']}[field]
        body=f'<text x="10" y="65" font-size="24">{escape(labels[0])}</text><text x="160" y="65" font-size="24">=</text><text x="195" y="65" font-size="24">{escape(labels[1])}</text><text x="385" y="65" font-size="24">×</text><text x="418" y="65" font-size="24">10</text><text x="450" y="39" font-size="15">{escape(labels[2])}</text>'
    else:
        label={'text':'distance','urdu':'فاصلہ','pashto':'واټن'}[field]
        number,power=('384400000.0','0') if kind=='start' else ('3.84400000','8')
        body=f'<text x="15" y="60" font-size="26">{escape(label)}</text><text x="140" y="60" font-size="26">=</text><text x="175" y="60" font-size="26">{number}</text><text x="385" y="60" font-size="26">×</text><text x="420" y="60" font-size="26">10</text><text x="452" y="40" font-size="18">{power}</text><text x="481" y="60" font-size="26">m</text>'
        if kind=='start':
            body+='<path d="M188 67'+('q7 15 14 0'*8)+'" stroke="#0284c7" fill="none" stroke-width="2"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 100" role="img" aria-label="{escape(kind)} scientific notation" style="max-width:100%;height:auto"><g fill="currentColor" font-family="sans-serif">{body}</g></svg>'
blocks=[]
for kind in ['standard','start','answer']:
    blocks.append(dict(type='formula',id=f'physics9-example11-{kind}',svg=equation(kind,'text'),svgUrdu=equation(kind,'urdu'),svgPashto=equation(kind,'pashto'),sourcePdfPage=15,printedPage=10))
moon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 230" role="img" aria-labelledby="physics9-earthmoon-title"><title id="physics9-earthmoon-title">Earth partly visible at lower left and the Moon above it to the right</title><defs><clipPath id="physics9-earth-clip"><circle cx="28" cy="202" r="105"/></clipPath><clipPath id="physics9-moon-clip"><circle cx="220" cy="61" r="42"/></clipPath></defs><rect width="280" height="230" fill="#111b32"/><circle cx="28" cy="202" r="105" fill="#274373"/><g clip-path="url(#physics9-earth-clip)" fill="none" stroke="#becfe7" stroke-width="10" opacity=".7"><path d="M-60 133Q15 157 81 119M-50 190Q35 148 96 183M-40 215Q40 188 132 202"/></g><circle cx="220" cy="61" r="42" fill="#b9b9ca"/><g clip-path="url(#physics9-moon-clip)" fill="#77798e"><circle cx="205" cy="53" r="14"/><circle cx="232" cy="76" r="13"/><circle cx="229" cy="35" r="8"/><circle cx="198" cy="79" r="8"/><circle cx="249" cy="55" r="8"/><path d="M181 22Q205 58 190 94L168 97Z" fill="#42475e"/></g></svg>'
blocks.append(dict(type='illustration',id='physics9-earthmoon-010',svg=moon,sourcePdfPage=15,printedPage=10))
blocks.append(dict(type='extensionExercise',number='1.1',question=s['paras'][13]['text'],answerProvidedInSource=False))
s['blocks']=blocks
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='visual',blockId='physics9-example11-standard'),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[2]),dict(type='numberedList',indices=[3,4,5]),dict(type='heading',indices=[6]),dict(type='paragraph',indices=[7]),dict(type='heading',indices=[8]),dict(type='paragraph',indices=[9]),dict(type='visual',blockId='physics9-example11-start'),dict(type='paragraph',indices=[10]),dict(type='visual',blockId='physics9-example11-answer'),dict(type='heading',indices=[11]),dict(type='visual',blockId='physics9-earthmoon-010'),dict(type='heading',indices=[12]),dict(type='paragraph',indices=[13])]
n=page['numericals'][0]
n['solution']='For Standard form / scientific notation we can write the term as\n\ndistance = 384400000.0 × 10⁰ m\n\n'+s['paras'][10]['text']+'\n\ndistance = 3.84400000 × 10⁸ m\n\nAnswer'
n.update(sourceSolutionParagraphs=[s['paras'][9],s['paras'][10]],givenOrigin='extracted from source statement',requiredOrigin='extracted from source statement',solutionOrigin='textbook',answerOrigin='textbook')
page['comparison']='Fresh source review of mantissa/exponent explanation, quantities 70,000,000,000,000,000,000,000 and 7×10²² and 1×10⁻¹⁴, all three numbered conversion steps, Example 1.1 statement and full printed solution including eight movement marks and answer precision, Earth/Moon illustration and extension question. Removed non-source where n is the exponent prose, preserved exponent (n) as the printed superscript label, separated solution prose/equations/answer, and coded the missing Earth/Moon scene. No extension answer authored.'
(OUT/'physics-page-015.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
