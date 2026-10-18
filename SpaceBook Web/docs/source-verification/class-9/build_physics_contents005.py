import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
old=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[4]
translations=[
('اچھال کی قوت یا تیرنے کی قوت','پورته ټېل وهونکې قوه یا د لامبو قوه'),
('ارشمیدس کا اصول','د ارشمیدس اصل'),
('لچک','ارتجاعیت'),
('تناؤ، کھنچاؤ اور ینگ کا ماڈیولس','تنش، نسبي غځېدنه او د ینګ موډولس'),
('مادے کی حرارتی خصوصیات','د مادې حرارتي ځانګړنې'),
('درجۂ حرارت','تودوخه'),
('حرارت','حرارت'),
('درجۂ حرارت کی پیمائش','د تودوخې اندازه کول'),
('حرارتی پھیلاؤ','حرارتي پراخېدل'),
('حرارتی گنجائش','حرارتي ظرفیت'),
('مخفی حرارت','پټ حرارت'),
('تبخیر','تبخیر'),
('حرارت کی منتقلی','د حرارت لېږد'),
('حرارت کی ایصال','د حرارت هدایت'),
('حرارتی موصلیت','حرارتي هدایت وړتیا'),
('حرارت کی حمل','د حرارت حمل'),
('حرارت کی تابکاری','د حرارت وړانګې'),
('گرین ہاؤس اثر اور عالمی حدت','د شنو خونو اغېز او نړیواله تودوخه'),
('جوابات','ځوابونه'),
('فرہنگ','د اصطلاحاتو قاموس'),
('اشاریہ','نمایه'),
('کتابیات','کتابتونیزې سرچینې'),
('اساتذہ کے لیے تجویز','د ښوونکو لپاره وړاندیز'),
('مفید طبیعی اعداد و شمار','ګټور فزیکي معلومات'),
('کثرت سے استعمال ہونے والی ریاضیاتی علامات','ډېر کارېدونکي ریاضيکي سمبولونه'),
('بنیادی ریاضیاتی فارمولے','بنسټیز ریاضيکي فورمولونه'),
('طلبہ کے لیے تجربہ گاہ کی ہدایات','د زده کوونکو لپاره د لابراتوار لارښوونې'),
('یونانی حروفِ تہجی','یوناني الفبا')]
page=dict(id='cls9-physics-front-005',pdfPage=5,printedPage=None,status='corrected-fresh-review',kind='contents continuation',title='CONTENTS',headingUrdu='فہرستِ مضامین',headingPashto='منځپانګه',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf',pairedParagraphs=[],sourceStructure=[],units=old['units'],backMatterIndex=old['backMatterIndex'])
def add(text):
    index=len(page['pairedParagraphs'])
    urdu,pashto=translations[index]
    page['pairedParagraphs'].append(dict(text=text,urdu=urdu,pashto=pashto))
    return index
entries=[]
for unit in page['units']:
    entry=dict(topics=[])
    if not unit.get('continuation'):
        entry.update(number=unit['number'],printedStartPage=unit['printedStartPage'],titleIndex=add(unit['title']))
    unit['topics']=[[code,title.replace('Archimedes�','Archimedes’').replace('Young�s','Young’s')] for code,title in unit['topics']]
    for code,title in unit['topics']:
        entry['topics'].append(dict(code=code,index=add(title)))
    entries.append(entry)
for title,printed in page['backMatterIndex']:
    entries.append(dict(titleIndex=add(title),printedStartPage=printed,topics=[]))
headers=json.loads((OUT/'physics-page-003.json').read_text(encoding='utf-8'))['sourceStructure'][0]['headers']
page['sourceStructure']=[dict(type='contentsTable',headers=headers,entries=entries)]
page['comparison']='Fresh visual review of unit 7 continuation, units 8–9, sixteen topic labels and ten back-matter rows. Repaired corrupted apostrophes in Archimedes’ and Young’s; retained printed Up-thurst spelling. Preserved starts 197/233 and back-matter pages 252–262 as printed references; unit 7 heading not repeated on this continuation page.'
assert len(page['pairedParagraphs'])==28
(OUT/'physics-page-005.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
