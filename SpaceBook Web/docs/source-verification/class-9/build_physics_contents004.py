import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
old=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[3]
translations=[
('قوتوں کا گھمانے والا اثر','د قوو څرخولی اغېز'),
('قوت کے خاکے','د قوې شکلونه'),
('قوتوں کا جمع','د قوو جمع کول'),
('قوتوں کی تحلیل','د قوو تجزیه'),
('مرکزِ کمیت','د کتلې مرکز'),
('قوت کا مومنٹ','د قوې مومنټ'),
('قوتوں کا جوڑا','د قوو جوړه'),
('توازن','تعادل'),
('استحکام','ثبات'),
('کششِ ثقل','جاذبه'),
('عالمگیر کششِ ثقل کا قانون','د نړیوالې جاذبې قانون'),
('زمین کی کمیت','د ځمکې کتله'),
('ثقلی میدان','د جاذبې میدان'),
('بلندی کے ساتھ ‘g’ میں تبدیلی','له لوړوالي سره د ‘g’ بدلون'),
('مصنوعی سیارچوں کی حرکت','د مصنوعي سپوږمکیو حرکت'),
('کام اور توانائی','کار او انرژي'),
('کام','کار'),
('توانائی اور اس کی صورتیں','انرژي او د هغې بڼې'),
('حرکی توانائی','حرکتي انرژي'),
('وضعی توانائی','پوتانسیلي انرژي'),
('توانائی کی تبدیلی اور بقا','د انرژۍ بدلون او ساتنه'),
('توانائی کے بڑے ذرائع','د انرژۍ مهمې سرچینې'),
('کارکردگی','موثریت'),
('طاقت','توان'),
('مادے کی خصوصیات','د مادې ځانګړنې'),
('مادے کا حرکی سالماتی نمونہ','د مادې حرکتي مالیکولي موډل'),
('کثافت','کثافت'),
('دباؤ','فشار'),
('فضائی دباؤ','اتموسفېري فشار'),
('پاسکل کا اصول','د پاسکال اصل'),
('مائع کا دباؤ','د مایع فشار')]
page=dict(id='cls9-physics-front-004',pdfPage=4,printedPage=None,status='corrected-fresh-review',kind='contents continuation',title='CONTENTS',headingUrdu='فہرستِ مضامین',headingPashto='منځپانګه',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf',pairedParagraphs=[],sourceStructure=[],units=old['units'])
counter=0
entries=[]
for unit in page['units']:
    indices=[]
    titles=[unit['title']]+[title.replace('�g�','‘g’') for code,title in unit['topics']]
    for title in titles:
        urdu,pashto=translations[counter]
        page['pairedParagraphs'].append(dict(text=title,urdu=urdu,pashto=pashto))
        indices.append(counter)
        counter+=1
    unit['topics']=[[code,titles[i+1]] for i,(code,_) in enumerate(unit['topics'])]
    entries.append(dict(number=unit['number'],printedStartPage=unit['printedStartPage'],titleIndex=indices[0],topics=[dict(code=code,index=index) for (code,_),index in zip(unit['topics'],indices[1:])]))
headers=json.loads((OUT/'physics-page-003.json').read_text(encoding='utf-8'))['sourceStructure'][0]['headers']
page['sourceStructure']=[dict(type='contentsTable',headers=headers,entries=entries)]
page['comparison']='Fresh 1.6x local visual comparison of units 4–7, all 27 topic labels, unit/topic numbering and printed starts 99/129/148/171. Restored corrupted quotation marks around g. Semantic table and explicit translations supplied; no instructional-page verification inferred from contents.'
assert counter==31
(OUT/'physics-page-004.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
