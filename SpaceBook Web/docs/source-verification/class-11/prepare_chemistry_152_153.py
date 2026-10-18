"""Source transcription and translations, preserving printed exercise answers."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def section(page,title,ur,ps):
    return dict(chapter='chem11-gases',id=f'chem11-p{page}-exercise',title=title,headingUrdu=ur,headingPashto=ps,sourceLanguage='en',source=dict(pdfPage=page,printedPage=page-5),auditStatus='corrected; source and translations reviewed',paras=[])

def add(s,key,text,**meta):
    s['paras'].append(dict(id=f"chem11-p{s['source']['pdfPage']}-{key}",en=text[0],ur=text[1],ps=text[2],**meta))

s=section(152,'Numerical Questions · Descriptive Questions','عددی سوالات · تفصیلی سوالات','عددي پوښتنې · تشریحي پوښتنې')
s['sourceNote']='Printed answers are transcribed as supplied, without adding worked solutions. The source gives cm, rather than cm³, in numerical question 2 and its answer; that notation is retained.'
add(s,'numerical-heading',('Numerical Questions','عددی سوالات','عددي پوښتنې'),kind='heading',exerciseId='unit4-numerical')
numericals=[
('A mass of gas is under a pressure of 760 torr and occupies volume of 525cm³, if the pressure is doubled, what volume would the gas now occupy? Assume the temperature is constant.','گیس کی ایک مقدار 760 torr دباؤ پر ہے اور 525cm³ حجم گھیرتی ہے۔ اگر دباؤ دوگنا کر دیا جائے تو گیس اب کتنا حجم گھیرے گی؟ فرض کریں کہ درجہ حرارت مستقل ہے۔','د ګاز یوه اندازه د 760 torr فشار لاندې ده او 525cm³ حجم نیسي. که فشار دوه برابره شي، ګاز به اوس څومره حجم ونیسي؟ فرض کړئ چې تودوخه ثابته ده.','262.5cm³'),
('Hydrogen gas diffuses through a porous plate at a rate of 500cm per minute at 0°C. What is the rate of diffusion of oxygen gas through the same porous plate at 0°C?','ہائیڈروجن گیس 0°C پر ایک مسام دار پلیٹ سے 500cm فی منٹ کی رفتار سے پھیلتی ہے۔ اسی مسام دار پلیٹ سے 0°C پر آکسیجن گیس کے پھیلاؤ کی رفتار کیا ہے؟','هایدروجن ګاز په 0°C کې له یوې سوری لرونکې تختې څخه په دقیقه کې د 500cm په کچه خپرېږي. په 0°C کې له همدې تختې څخه د اکسیجن ګاز د خپرېدو کچه څومره ده؟','125cm'),
('It was desired to obtain a volume of 1000cm³ of oxygen at 100°C and 640 mm Hg. How many moles of oxygen would be required?','100°C اور 640 mm Hg پر آکسیجن کا 1000cm³ حجم حاصل کرنا مطلوب تھا۔ آکسیجن کے کتنے مول درکار ہوں گے؟','په 100°C او 640 mm Hg کې د اکسیجن د 1000cm³ حجم ترلاسه کول غوښتل کېدل. د اکسیجن څو مولونو ته به اړتیا وي؟','0.0275mol'),
('Calculate the density of CH₄ at 0°C and 1 atmosphere.','0°C اور 1 atmosphere پر CH₄ کی کثافت معلوم کریں۔','په 0°C او 1 atmosphere کې د CH₄ کثافت محاسبه کړئ.','0.7139gdm⁻³'),
('A sample of Krypton with a volume of 6.25 dm³ and a pressure of 765 torr and a temperature of 20°C is expanded to a volume of 9.55 dm³ and a pressure of 375 torr. What will be its final temperature?','کرپٹون کے ایک نمونے کا حجم 6.25 dm³، دباؤ 765 torr اور درجہ حرارت 20°C ہے۔ اسے 9.55 dm³ حجم اور 375 torr دباؤ تک پھیلایا جاتا ہے۔ اس کا آخری درجہ حرارت کیا ہوگا؟','د کریپټون یوه نمونه چې حجم یې 6.25 dm³، فشار یې 765 torr او تودوخه یې 20°C ده، تر 9.55 dm³ حجم او 375 torr فشار پورې پراخېږي. وروستۍ تودوخه به یې څومره وي؟','219.64K')]
for n,(*q,ans) in enumerate(numericals,1):
    meta=dict(exerciseId=f'unit4-numerical-{n}',questionId=f'chem11-unit4-numerical-{n}')
    add(s,f'numerical-{n}',tuple(f'{n}. '+v for v in q),role='question',**meta)
    add(s,f'numerical-{n}-answer',(f'(Answer: {ans})',f'(جواب: {ans})',f'(ځواب: {ans})'),role='source-answer',**meta)
add(s,'descriptive-heading',('Descriptive Questions','تفصیلی سوالات','تشریحي پوښتنې'),kind='heading',exerciseId='unit4-descriptive')
descriptive=[
(1,'a',('Explain the concept of diffusion and effusion of gases.','گیسوں کے پھیلاؤ اور باریک سوراخ سے اخراج کے تصورات کی وضاحت کریں۔','د ګازونو د خپرېدو او له کوچني سوري څخه د وتلو مفهوم تشریح کړئ.')),
(1,'b',('Apply the knowledge of the kinetic theory of gases and derive an expression of Graham’s law of diffusion.','گیسوں کے حرکی نظریے کے علم کو استعمال کرتے ہوئے گراہم کے قانونِ پھیلاؤ کی مساوات اخذ کریں۔','د ګازونو د کینټیک تیورۍ پوهه وکاروئ او د ګراهام د خپرېدو د قانون یوه رابطه ترلاسه کړئ.')),
(1,'c',('The rate of effusion of an unknown gas through a pinhole is found to be 0.279 times the rate of effusion of H₂ through the same pinhole. Calculate the molecular mass of the unknown gas at STP.','ایک باریک سوراخ سے نامعلوم گیس کے اخراج کی رفتار، اسی سوراخ سے H₂ کے اخراج کی رفتار کا 0.279 گنا پائی گئی ہے۔ STP پر نامعلوم گیس کی سالماتی کمیت معلوم کریں۔','له یوه کوچني سوري څخه د یوه نامعلوم ګاز د وتلو کچه، له همدغه سوري څخه د H₂ د وتلو د کچې 0.279 برابره موندل شوې ده. په STP کې د نامعلوم ګاز مالیکولي کتله محاسبه کړئ.')),
(2,'a',('State Dalton’s law of partial pressure. Write down its mathematical form.','ڈالٹن کا قانونِ جزوی دباؤ بیان کریں۔ اس کی ریاضیاتی صورت لکھیں۔','د ډالټن د جزوي فشار قانون بیان کړئ. ریاضيکي بڼه یې ولیکئ.')),
(2,'b',('Explain the significance of absolute zero, giving its value in degree Celsius and Kelvin.','مطلق صفر کی اہمیت بیان کریں اور اس کی قدر ڈگری سیلسیس اور کیلون میں دیں۔','د مطلق صفر اهمیت تشریح کړئ او ارزښت یې په سیلسیس درجو او کیلوین کې ورکړئ.')),
(2,'c',('What pressure is exerted by a mixture of 2g of helium (He), 16g of oxygen (O₂) and 10g of carbon dioxide (CO₂) at 10°C in a 5dm³ vessel?','5dm³ کے برتن میں 10°C پر 2g ہیلیم (He)، 16g آکسیجن (O₂) اور 10g کاربن ڈائی آکسائیڈ (CO₂) کے آمیزے کا دباؤ کتنا ہے؟','په یوه 5dm³ لوښي کې، په 10°C کې د 2g هیلیم (He)، 16g اکسیجن (O₂) او 10g کاربن ډای اکسایډ (CO₂) مخلوط څومره فشار اچوي؟')),
(3,'a',('How would you relate temperature to the average kinetic energy of the particles in a substance?','آپ کسی مادے کے ذرات کی اوسط حرکی توانائی اور درجہ حرارت کے درمیان تعلق کیسے بیان کریں گے؟','تاسو به تودوخه په یوه ماده کې د ذرو له منځنۍ حرکي انرژۍ سره څنګه وتړئ؟')),
(3,'b',('Explain Linde’s method for the liquefaction of gases.','گیسوں کو مائع بنانے کے لیے لنڈے کے طریقے کی وضاحت کریں۔','د ګازونو د مایع کولو لپاره د لینډې طریقه تشریح کړئ.')),
(3,'c',('Give two points of evidence to show that gases do not behave ideally under all conditions of temperature and pressure.','دو شواہد دیں جو ظاہر کریں کہ گیسیں درجہ حرارت اور دباؤ کی تمام حالتوں میں مثالی برتاؤ نہیں کرتی ہیں۔','د شواهدو دوه ټکي وړاندې کړئ چې وښيي ګازونه د تودوخې او فشار په ټولو شرایطو کې مثالي چلند نه کوي.')),
(4,'a',('Write the Van der Waals equation for a real gas. Clearly explain the meaning of the corrective terms for pressure and volume.','حقیقی گیس کے لیے وان ڈر والز مساوات لکھیں۔ دباؤ اور حجم کی تصحیحی حدوں کا مطلب واضح طور پر بیان کریں۔','د یوه حقیقي ګاز لپاره د وان در والس معادله ولیکئ. د فشار او حجم د اصلاحي حدونو مانا په څرګنده تشریح کړئ.')),
(4,'b',('The temperature of a real gas usually drops when it is allowed to enter into a low pressure (vacuum). Explain.','حقیقی گیس کو کم دباؤ (خلا) میں داخل ہونے دیا جائے تو عموماً اس کا درجہ حرارت گر جاتا ہے۔ وضاحت کریں۔','کله چې یوه حقیقي ګاز ته ټیټ فشار (خلا) ته د ننوتلو اجازه ورکړل شي، عموماً یې تودوخه ټیټېږي. تشریح یې کړئ.')),
(4,'c',('Define and describe the properties of plasma.','پلازما کی تعریف کریں اور اس کی خصوصیات بیان کریں۔','پلازما تعریف کړئ او ځانګړنې یې بیان کړئ.'))]
for n,label,q in descriptive:
    meta=dict(exerciseId=f'unit4-descriptive-{n}',questionId=f'chem11-unit4-descriptive-{n}-{label}')
    prefix=f'{n}. ({label}) ' if label=='a' else f'({label}) '
    add(s,f'descriptive-{n}-{label}',tuple(prefix+v for v in q),role='question',**meta)
    answer={(1,'c'):'25.7g',(2,'c'):'5.703atm'}.get((n,label))
    if answer:add(s,f'descriptive-{n}-{label}-answer',(f'(Answer: {answer})',f'(جواب: {answer})',f'(ځواب: {answer})'),role='source-answer',**meta)
s['vocabulary']={'porous':{'ur':'مسام دار','ps':'سوري لرونکی'},'absolute zero':{'ur':'مطلق صفر','ps':'مطلق صفر'},'partial pressure':{'ur':'جزوی دباؤ','ps':'جزوي فشار'},'liquefaction':{'ur':'گیس کو مائع بنانے کا عمل','ps':'د ګاز د مایع کولو بهیر'},'plasma':{'ur':'پلازما؛ آئنوں اور آزاد الیکٹرانوں پر مشتمل مادہ','ps':'پلازما؛ له ایونونو او ازادو الکترونونو جوړه ماده'},'pinhole':{'ur':'باریک سوراخ','ps':'د ستنې په شان کوچنی سوری'},'mixture':{'ur':'آمیزہ','ps':'مخلوط'}}
(ROOT/'chemistry-page-152.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')

s=section(153,'Descriptive Questions (continued) · PROJECT:','تفصیلی سوالات (جاری) · منصوبہ:','تشریحي پوښتنې (دوام) · پروژه:')
s['auditStatus']='corrected; unresolved scan-edge words'
s['sourceNote']='The right edge of the scan hides word endings. [scan obscured] marks those fragments; they have not been supplied from inference.'
qs=[
('5. (a) State basic postulates of kinetic molecular theory of gases.','5. (a) گیسوں کے حرکی سالماتی نظریے کے بنیادی مفروضے بیان کریں۔','5. (a) د ګازونو د کینټیک مالیکولي تیورۍ بنسټیز فرضونه بیان کړئ.'),
('(b) Explain how Graham’s law of diffusion can be derived from the Kin[scan obscured] Molecular Theory.','(b) وضاحت کریں کہ گراہم کا قانونِ پھیلاؤ Kin[اسکین میں متن چھپا ہوا ہے] سالماتی نظریے سے کیسے اخذ کیا جا سکتا ہے۔','(b) تشریح کړئ چې د ګراهام د خپرېدو قانون څنګه له Kin[په سکین کې متن پټ دی] مالیکولي تیورۍ څخه ترلاسه کېدای شي.'),
('(c) Explain the absolute zero on the basis of Charles’ law.','(c) چارلس کے قانون کی بنیاد پر مطلق صفر کی وضاحت کریں۔','(c) د چارلس د قانون پر بنسټ مطلق صفر تشریح کړئ.')]
for label,q in zip('abc',qs):
    gap={'sourceGap':{'note':'The word following “the” is cut off after “Kin” at the curved right edge; a clearer source is needed.'}} if label=='b' else {}
    add(s,'descriptive-5-'+label,q,role='question',exerciseId='unit4-descriptive-5',questionId='chem11-unit4-descriptive-5-'+label,**gap)
add(s,'project-heading',('PROJECT:','منصوبہ:','پروژه:'),kind='heading',exerciseId='unit4-project')
add(s,'project-1',('1. Use the daily weather reports in the newspapers or news and conduct [scan obscured] meteorological research to study the interrelationships among atmosphe[scan obscured] pressure (air pressure), temperature, humidity, and other weather variables. Prepare a report of a week explaining your results and present it in the class.','1. اخبارات یا خبروں میں روزانہ کی موسمی رپورٹیں استعمال کریں اور [اسکین میں متن چھپا ہوا ہے] موسمیاتی تحقیق کریں تاکہ atmosphe[اسکین میں متن چھپا ہوا ہے] دباؤ (ہوا کا دباؤ)، درجہ حرارت، نمی اور دیگر موسمی متغیرات کے باہمی تعلقات کا مطالعہ کیا جا سکے۔ اپنے نتائج کی وضاحت کرتے ہوئے ایک ہفتے کی رپورٹ تیار کریں اور اسے جماعت میں پیش کریں۔','1. په ورځپاڼو یا خبرونو کې د هوا ورځني راپورونه وکاروئ او [په سکین کې متن پټ دی] هواپېژندنیزه څېړنه وکړئ، څو د atmosphe[په سکین کې متن پټ دی] فشار (د هوا فشار)، تودوخې، لندبل او نورو موسمي متغیرونو ترمنځ اړیکې وڅېړئ. د یوې اونۍ راپور چمتو کړئ، خپلې پایلې پکې تشریح کړئ او په ټولګي کې یې وړاندې کړئ.'),role='question',exerciseId='unit4-project-1',questionId='chem11-unit4-project-1',sourceGap={'note':'The line ending after “conduct” and the end of “atmosphe…” are obscured by the page curl.'})
add(s,'project-2',('2. The pressure of air in car tyres is checked regularly for safety and to preven[scan obscured] uneven tyre wear and tear. What units of measurement are used on a typic[scan obscured] tyre gauge? Also, find out that how gauge pressure relates to atmosphe[scan obscured] pressure.','2. حفاظت اور ٹائروں کے غیر یکساں گھسنے کو preven[اسکین میں متن چھپا ہوا ہے] کے لیے گاڑی کے ٹائروں میں ہوا کا دباؤ باقاعدگی سے جانچا جاتا ہے۔ typic[اسکین میں متن چھپا ہوا ہے] ٹائر گیج پر پیمائش کی کون سی اکائیاں استعمال ہوتی ہیں؟ یہ بھی معلوم کریں کہ گیج دباؤ کا atmosphe[اسکین میں متن چھپا ہوا ہے] دباؤ سے کیا تعلق ہے۔','2. د خوندیتوب او د ټایرونو د نامساوي زړېدو د preven[په سکین کې متن پټ دی] لپاره د موټر په ټایرونو کې د هوا فشار په منظم ډول کتل کېږي. په یوه typic[په سکین کې متن پټ دی] ټایر ګیج کې د اندازه کولو کوم واحدونه کارول کېږي؟ دا هم معلومه کړئ چې د ګیج فشار له atmosphe[په سکین کې متن پټ دی] فشار سره څه اړیکه لري.'),role='question',exerciseId='unit4-project-2',questionId='chem11-unit4-project-2',sourceGap={'note':'Final letters of the words after “to”, “a” and “to” on the three lines are hidden at the curved right edge.'})
s['vocabulary']={'humidity':{'ur':'نمی','ps':'لندبل'},'weather':{'ur':'موسم','ps':'هوا'},'gauge pressure':{'ur':'گیج دباؤ','ps':'د ګیج فشار'},'postulates':{'ur':'مفروضے','ps':'فرضونه'},'meteorological':{'ur':'موسمیات سے متعلق','ps':'د هواپېژندنې اړوند'}}
(ROOT/'chemistry-page-153.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared source records for pages 152 and 153.')
