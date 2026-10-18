import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
old=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[2]
translations=[
('طبیعی مقداریں اور پیمائش','فزیکي کمیتونه او اندازه کول'),
('طبیعیات کا تعارف','د فزیک پېژندنه'),
('طبیعی مقداریں','فزیکي کمیتونه'),
('اکائیوں کا بین الاقوامی نظام','د واحدونو نړیوال سیستم'),
('معیاری صورت/ سائنسی علامت نویسی','معیاري بڼه/ علمي لیکنه'),
('سابقے (مضاعف اور ذیلی مضاعف)','مختاړي (مضاعفونه او فرعي مضاعفونه)'),
('پیمائشی آلات','د اندازه کولو وسایل'),
('بامعنی ہندسے','مانا لرونکې شمېرې'),
('حرکیات','د حرکت څېړنه'),
('سکون اور حرکت','سکون او حرکت'),
('عددی اور سمتی مقداریں','سکالرونه او وکټورونه'),
('حرکت سے متعلق اصطلاحات','له حرکت سره تړلې اصطلاحات'),
('حرکت کا گرافی تجزیہ','د حرکت ګرافیکي شننه'),
('حرکت کی مساوات','د حرکت معادلې'),
('کششِ ثقل کی وجہ سے حرکت','د جاذبې له امله حرکت'),
('قوتی حرکیات','د قوې او حرکت څېړنه'),
('قوت','قوه'),
('نیوٹن کے قوانینِ حرکت','د نیوټن د حرکت قوانین'),
('وزن','وزن'),
('مقدارِ حرکت','د حرکت مقدار'),
('منسلک اجسام','تړلي جسمونه'),
('رگڑ','رګړ'),
('یکساں دائرہ وار حرکت','یوشان دایروي حرکت')]
page=dict(id='cls9-physics-front-003',pdfPage=3,printedPage=None,status='corrected-fresh-review',kind='contents',title='CONTENTS',headingUrdu='فہرستِ مضامین',headingPashto='منځپانګه',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf',pairedParagraphs=[],sourceStructure=[],units=old['units'])
counter=0
entries=[]
for unit in page['units']:
    indices=[]
    titles=[unit['title']]+[title.replace('Newton�s','Newton’s').replace('Standard form /','Standard form/') for code,title in unit['topics']]
    for title in titles:
        urdu,pashto=translations[counter]
        page['pairedParagraphs'].append(dict(text=title,urdu=urdu,pashto=pashto))
        indices.append(counter)
        counter+=1
    unit['topics']=[[code,titles[i+1]] for i,(code,_) in enumerate(unit['topics'])]
    entries.append(dict(number=unit['number'],printedStartPage=unit['printedStartPage'],titleIndex=indices[0],topics=[dict(code=code,index=index) for (code,_),index in zip(unit['topics'],indices[1:])]))
page['sourceStructure']=[dict(type='contentsTable',headers=[dict(text='Unit No.',urdu='اکائی نمبر',pashto='د څپرکي شمېره'),dict(text='Topic',urdu='موضوع',pashto='موضوع'),dict(text='Page No.',urdu='صفحہ نمبر',pashto='د پاڼې شمېره')],entries=entries)]
page['comparison']='Fresh visual comparison of all three units, twenty topic labels, unit and topic numbers, start-page references 1/29/60 and header row. Repaired corrupted apostrophe in Newton’s and retained slash punctuation. Added semantic contents table with paired translations. Contents references do not certify instructional pages.'
assert counter==23
(OUT/'physics-page-003.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
