"""Source-compared transcription of PDF p151 (printed p146); preserves each item."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
questions = [
 (9, ('Which statement about the behaviour of the particles in a gas is not correct?', 'گیس میں ذرات کے برتاؤ کے بارے میں کون سا بیان درست نہیں ہے؟', 'په ګاز کې د ذرو د چلند په اړه کوم بیان ناسم دی؟'), [
  ('They are able to move at great speeds','وہ بہت تیز رفتاری سے حرکت کر سکتے ہیں','هغوی په ډېر سرعت خوځېدای شي'),
  ('The forces of attraction between the particles are negligible','ذرات کے درمیان کشش کی قوتیں قابلِ نظرانداز ہیں','د ذرو ترمنځ جذبي ځواکونه د پام وړ نه دي'),
  ('There is large space among the particles','ذرات کے درمیان بہت زیادہ جگہ ہے','د ذرو ترمنځ ډېر تش ځای شته'),
  ('They are arranged in regular patterns','وہ باقاعدہ نمونوں میں ترتیب یافتہ ہیں','هغوی په منظمو بڼو ترتیب شوي دي')]),
 (10, ('At the same temperature and pressure which of the following gases has the greatest density.', 'یکساں درجہ حرارت اور دباؤ پر درج ذیل میں سے کس گیس کی کثافت سب سے زیادہ ہے۔', 'په یوه تودوخه او فشار کې له لاندې ګازونو څخه د کوم یوه کثافت تر ټولو زیات دی.'), ['CO₂','SO₂','Cl₂','H₂O']),
 (11, ('Weight of one dm³ of O₂ at STP is','STP پر O₂ کے ایک dm³ کا وزن ہے','په STP کې د O₂ د یوه dm³ وزن دی'), ['1.4384 g','1.5394 g','1.6384 g','1.3384 g']),
 (12, ('The value of ideal gas constant in dm³.torr.k⁻¹.mol⁻¹','dm³.torr.k⁻¹.mol⁻¹ میں مثالی گیس مستقل کی قدر','په dm³.torr.k⁻¹.mol⁻¹ کې د مثالي ګاز د ثابت ارزښت'), ['0.0821','1.98722','62.364','8.3143']),
 (13, ('760 torr is equal to,','760 torr برابر ہے،','760 torr برابر دي له،'), [('760 Pascal','760 پاسکل','760 پاسکال'),('76 Pascal','76 پاسکل','76 پاسکال'),('101325 Pascal','101325 پاسکل','101325 پاسکال'),('1.01325 Pascal','1.01325 پاسکل','1.01325 پاسکال')]),
 (14, ('At 50°C a gas has 1atm pressure, and 20dm³ volume, its volume at STP would be','50°C پر ایک گیس کا دباؤ 1atm اور حجم 20dm³ ہے، STP پر اس کا حجم ہوگا','په 50°C کې د یوه ګاز فشار 1atm او حجم 20dm³ دی، په STP کې به یې حجم وي'), ['16.94dm³','10.92dm³','3.66dm³','42.2 dm³']),
 (15, ('Which of the following gases will have the fastest effusion rate?','درج ذیل میں سے کس گیس کے اخراج کی رفتار سب سے زیادہ ہوگی؟','له لاندې ګازونو څخه د کوم یوه د وتلو کچه به تر ټولو چټکه وي؟'), ['CH₄','NH₃','CO₂','O₂'])
]
short = [
 ('Justify that 1cm³ of hydrogen (H₂) and 1cm³ of methane (CH₄) at STP will have same number of molecules although one molecules of methane (CH₄) is 8 times heavier than that of hydrogen (H₂).','جواز دیں کہ STP پر ہائیڈروجن (H₂) کے 1cm³ اور میتھین (CH₄) کے 1cm³ میں سالموں کی تعداد برابر ہوگی، اگرچہ میتھین (CH₄) کا ایک سالمہ ہائیڈروجن (H₂) کے سالمے سے 8 گنا بھاری ہے۔','دلیل وړاندې کړئ چې په STP کې د هایدروجن (H₂) په 1cm³ او د میتان (CH₄) په 1cm³ کې د مالیکولونو شمېر یو شان وي، که څه هم د میتان (CH₄) یو مالیکول د هایدروجن (H₂) تر مالیکول 8 ځله دروند دی.'),
 ('Do you think that some of the postulates of kinetic molecular theory of gases are faulty? Write down these postulates.','کیا آپ کے خیال میں گیسوں کے حرکی سالماتی نظریے کے بعض مفروضے ناقص ہیں؟ یہ مفروضے لکھیں۔','ایا ستاسو په اند د ګازونو د کینټیک مالیکولي تیورۍ ځینې فرضونه ناسم دي؟ دغه فرضونه ولیکئ.'),
 ('Why high pressure and low temperature make the gases non-ideal?','زیادہ دباؤ اور کم درجہ حرارت گیسوں کو غیر مثالی کیوں بناتے ہیں؟','لوړ فشار او ټیټه تودوخه ولې ګازونه غیرمثالي کوي؟'),
 ('What is your opinion about rapid expansion of gases causes cooling?','گیسوں کے تیز پھیلاؤ سے ٹھنڈک پیدا ہونے کے بارے میں آپ کی کیا رائے ہے؟','د ګازونو د چټکې پراختیا له امله د یخېدو په اړه ستاسو نظر څه دی؟'),
 ('Why do you think that lighter gases can diffuse more rapidly than heavier ones?','آپ کے خیال میں ہلکی گیسیں بھاری گیسوں سے زیادہ تیزی سے کیوں پھیل سکتی ہیں؟','ستاسو په اند سپک ګازونه ولې د درنو ګازونو په پرتله چټک خپرېدای شي؟')
]
paras = []
def add(id, triple, **extra):
    paras.append(dict(id=id,en=triple[0],ur=triple[1],ps=triple[2],**extra))
for n,q,opts in questions:
    meta=dict(exerciseId=f'unit4-mcq-{n}',questionId=f'chem11-unit4-mcq-{n}')
    extra={}
    if n in (9,10,14): extra['sourceGap']={'note':'The final few letters at the curled right edge remain partly obscured in both the full-book and chapter-split scans; this line needs final source review.'}
    add(f'chem11-p151-question-{n}',tuple(f'{n}. '+s for s in q),role='question',**meta,**extra)
    for label,opt in zip('abcd',opts):
        if isinstance(opt,str): opt=(opt,opt,opt)
        add(f'chem11-p151-q{n}-{label}',tuple(label+'. '+s for s in opt),role='option',optionId=label,listGroup=f'p151-options-{n}',listType='ordered',**meta)
add('chem11-p151-short-heading',('Short Questions','مختصر سوالات','لنډې پوښتنې'),kind='heading',exerciseId='unit4-short-questions')
for n,q in enumerate(short,1):
    extra={}
    if n in (1,2,5):extra['sourceGap']={'note':'Right-edge curl partially obscures words in this question in both identical local PDF scans; retain unresolved status pending a clearer source.'}
    add(f'chem11-p151-short-{n}',tuple(f'{n}. '+s for s in q),role='question',exerciseId=f'unit4-short-{n}',questionId=f'chem11-unit4-short-{n}',**extra)
record=dict(chapter='chem11-gases',id='chem11-p151-unit4-mcq9-shortq',title='Exercise · Questions 9–15 · Short Questions',headingUrdu='مشق · سوالات 9–15 · مختصر سوالات',headingPashto='تمرین · 9–15 پوښتنې · لنډې پوښتنې',sourceLanguage='en',source=dict(pdfPage=151,printedPage=146),auditStatus='corrected; unresolved scan-edge words',sourceNote='Full-book PDF page 151 and chemistry4.pdf page 31 render identically. Curled question endings remain flagged. Source values and the wording “one molecules” are preserved.',paras=paras)
(root/'chemistry-page-151.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
