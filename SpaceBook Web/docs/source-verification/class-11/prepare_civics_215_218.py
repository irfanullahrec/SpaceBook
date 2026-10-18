from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,ur,en,ps,g,**m): add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g,**m)
U='c09'
def Q(s,ur,en,ps,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',**k)
def QI(s,ur,en,ps,g): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',listGroup=g)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 9.'
def G(s,w,lat,um,em,pm):
    """glossary entry: printed Urdu word with its English term, Urdu meaning, our English/Pashto renderings"""
    add(s,f'g{len(s["paras"])+1}',f'{lat}: {em}',f'{w} ({lat}): {um}',f'{lat}: {pm}',listGroup='gloss')
def L(s,ur,en,ps): add(s,f'l{len(s["paras"])+1}',en,ur,ps,kind='heading')
# scan 215 = 108_page_2 : printed 206
s=page(215,'c09','206','Exercise (Mashq): question 3 (end), questions 4–5; practical activities','مشق: سوال 3 کا اختتام، سوال 4–5؛ عملی سرگرمیاں','تمرین: ۳ پوښتنې پای، ۴–۵ پوښتنې؛ عملي فعالیتونه','ex9c')
F=Flow(s)
QI(s,'کالم الف (باقی الفاظ): تجربہ، فرضی، قانون','Column A (remaining words): tajruba (experience), farzi (mock), qanoon (law)','کالم الف (پاتې ټکي): تجربه، فرضي، قانون','q3')
QI(s,'کالم ب (باقی الفاظ): خدمت، شکن، شرکت','Column B (remaining words): khidmat (service), shikan (-breaking), shirkat (participation)','کالم ب (پاتې ټکي): خدمت، ماتوونکی، ګډون','q3')
Q(s,'۴۔ درج ذیل سوالات کے مختصر جواب تحریر کریں:','4. Write short answers to the following questions:','۴. د لاندې پوښتنو لنډ ځوابونه ولیکئ:')
for u,e,p in [('۱۔ فعال اور ذمہ دار شہری سے کیا مراد ہے؟','1. What is meant by an active and responsible citizen?','۱. له فعال او مسؤل ښاروند نه څه مراد دی؟'),('۲۔ اگر عملی سرگرمیوں میں حصہ لینا ممکن نہ ہو تو پھر طلبہ کو کیا کرنا چاہیے؟','2. If it is not possible to take part in practical activities, what should students do?','۲. که په عملي فعالیتونو کې برخه اخیستل شونې نه وي نو بیا زده کوونکي باید څه وکړي؟'),('۳۔ فعال شرکت کی تعریف کریں۔','3. Define active participation.','۳. د فعال ګډون تعریف وکړئ.'),('۴۔ کمیونٹی سروس سے کیا مراد ہے؟','4. What is meant by community service?','۴. له ټولنیز خدمت نه څه مراد دی؟'),('۵۔ طلبہ و طالبات کیسے فعال شہری ثابت ہو سکتے ہیں؟','5. How can students prove to be active citizens?','۵. زده کوونکي څنګه فعال اتباع ثابتېدای شي؟')]:
    QI(s,u,e,p,'q4')
Q(s,'۵۔ درج ذیل سوالات کے تفصیلی جواب دیں:','5. Give detailed answers to the following questions:','۵. د لاندې پوښتنو تفصیلي ځوابونه ورکړئ:')
for u,e,p in [('۱۔ بلا واسطہ یا بالواسطہ شرکت کے ذریعے کیسے سیکھا جا سکتا ہے؟','1. How can one learn through direct or indirect participation?','۱. په مستقیم یا غیر مستقیم ګډون له لارې څنګه زده کړه کېدای شي؟'),('۲۔ فعال شہریت یا کمیونٹی سروس پر تفصیلی نوٹ لکھیں۔','2. Write a detailed note on active citizenship or community service.','۲. په فعال اتباعیت یا ټولنیز خدمت تفصیلي یادښت ولیکئ.')]:
    QI(s,u,e,p,'q5')
H(s,'عملی سرگرمیاں:','Practical activities:','عملي فعالیتونه:')
for u,e,p in [('۱۔ ایک فرضی انتخابی مہم چلائیں اور اپنے کلاس فیلوز کو ووٹ دینے پر آمادہ کریں۔','1. Run a mock election campaign and induce your classmates to vote.','۱. یوه فرضي ټاکنیزه کمپاین پرمخ یوسئ او خپل ټولګیوالو ته د رایې ورکولو هڅونه وکړئ.'),('۲۔ اپنے سکول میں ہفتۂ صفائی منائیں۔','2. Observe a cleanliness week in your school.','۲. په خپل ښوونځي کې د پاکوالي اونۍ ولمانځئ.'),('۳۔ چند مشہور سماجی تنظیموں کے نام چارٹ پر لکھیں اور ان شعبوں کو نمایاں کریں جن میں وہ سرگرمِ عمل ہیں۔','3. Write the names of a few famous social organisations on a chart and highlight the fields in which they are active.','۳. د څو مشهورو ټولنیزو تنظیمونو نومونه په چارټ ولیکئ او هغه ډګرونه څرګند کړئ چې په هغو کې فعال دي.')]:
    P(s,u,e,p)
F.done()
s['sourceNote']='Printed page 206 (scan 215): the remaining three words of each column of question 3, question 4 (five short questions), question 5 (two long questions) and a boxed panel “عملی سرگرمیاں” with three activities, the end of Chapter 9. The scan is skewed.'+NOTE
s['vocabulary']={}
save(s)
# scan 216 = 108_page_1 : printed 207 (Glossary start)
s=page(216,'farhang','207','Glossary (Farhang): alif — start','فرہنگ (Glossary): الف — آغاز','فرهنګ (Glossary): الف — پیل','gl1')
F=Flow(s)
H(s,'فرہنگ (Glossary)','Glossary','فرهنګ (Glossary)')
L(s,'(الف)','(alif)','(الف)')
G(s,'استحصال','Exploitation','کسی حالت یا شخص کی مجبوری سے ذاتی مفاد کی خاطر ناجائز فائدہ اُٹھانا۔','to take unfair advantage of the helplessness of a situation or person for personal benefit','د کوم حالت یا شخص له مجبورۍ نه د شخصي ګټې لپاره ناروا ګټه اخیستل.')
G(s,'انقلاب','Revolution','کسی حکومت یا نظام کو گرانا۔ نظام میں بنیادی تبدیلیاں۔ نظام کو تبدیل کرنا۔','to overthrow a government or system; basic changes in the system; to change the system','د کوم حکومت یا نظام ړنګول؛ په نظام کې بنسټیز بدلونونه؛ نظام بدلول.')
G(s,'انتہا پسندی','Extremism','انتہائی حربہ استعمال کرنا۔ پُرتشدد راستہ اختیار کرنا۔','to use an extreme measure; to adopt a violent path','انتهايي وسیله کارول؛ تاوتریخوالي لار خپلول.')
G(s,'ارتقائی عمل','Evolutionary Process','درجہ بدرجہ تغیر، تبدیلی یا ترقی۔','gradual change, alteration or progress','پړاو په پړاو تغیر، بدلون یا پرمختګ.')
G(s,'اطاعت','Obedience','حکم ماننا۔','to obey an order','حکم منل.')
G(s,'اخلاقیات','Morality','ذاتی ضمیر سے اچھے اور بُرے کا فیصلہ کرنا اس سے ہٹ کر کہ قانون یا ضابطے کا کیا کہنا ہے۔ انصاف کے معیار کے مطابق اچھے اور بُرے کا فیصلہ کرنا۔','to decide good and bad by one’s own conscience apart from what the law or rule says; to decide good and bad according to the standard of justice','د شخصي ضمیر له مخې د ښه او بد پرېکړه کول پرته له دې چې قانون یا ضابطه څه وايي؛ د انصاف د معیار سره سم د ښه او بد پرېکړه کول.')
G(s,'اشتراکیت','Socialism','معاشی و سیاسی نظریہ کہ آمدنی اور پیداوار کے اہم اور بڑے ذرائع قومی اور اجتماعی ملکیت قائم کیا جائے؛ ہر ایک سے اس کی استعداد اور صلاحیتوں کے مطابق کام لیا جائے اور ہر ایک کو اس کے کام کے مطابق بدلہ دیا جائے۔','the economic and political theory that the important and big means of income and production be established as national and collective property; everyone be made to work according to his capacity and abilities and everyone be given reward according to his work','اقتصادي او سیاسي نظریه چې د عاید او تولید مهمې او لویې سرچینې ملي او ډله ییز ملکیت جوړې شي؛ له هر چا نه د هغه د وړتیا او ځواک سره سم کار واخیستل شي او هر چا ته د هغه د کار سره سم بدله ورکړل شي.')
G(s,'اشتمالیت','Communism','معاشی و سیاسی نظریہ کہ آمدنی اور پیداوار کے تمام ذرائع پر قومی اور اجتماعی ملکیت قائم کیا جائے؛ ہر ایک سے اس کی استعداد اور صلاحیتوں کے مطابق کام لیا جائے اور ہر ایک کو اس کی ضرورت کے مطابق بدلہ دیا جائے۔','the economic and political theory that national and collective ownership be established over all means of income and production; everyone be made to work according to his capacity and abilities and everyone be given according to his need','اقتصادي او سیاسي نظریه چې د عاید او تولید په ټولو سرچینو ملي او ډله ییز ملکیت جوړ شي؛ له هر چا نه د هغه د وړتیا او ځواک سره سم کار واخیستل شي او هر چا ته د هغه د اړتیا سره سم بدله ورکړل شي.')
G(s,'اقلیت','Minority','ہر وہ گروہ خاص طور پر مذہبی گروہ جو کسی ملک میں اکثریت میں نہ ہو۔ مثلاً پاکستان میں عیسائی وغیرہ۔','every group, especially a religious group, that is not in the majority in a country; for example Christians in Pakistan and so on','هره هغه ډله په ځانګړې توګه مذهبي ډله چې په کوم هېواد کې اکثریت نه وي. د بېلګې په توګه په پاکستان کې عیسایان او نور.')
G(s,'اتفاق رائے','Consensus','سب کا متفق ہونا۔','everyone’s agreeing','د ټولو متفق کېدل.')
G(s,'ارتکاز','Centralization','طاقت یا دولت وغیرہ کا چند ہاتھوں میں جمع ہونا۔','the gathering of power or wealth and so on in a few hands','د ځواک یا شتمنۍ او نورو په څو لاسونو کې راټولېدل.')
F.done()
s['sourceNote']='Printed page 207 (scan 216): the blue banner “فرہنگ (Glossary)” and the first entries of the glossary under the letter “الف” (Exploitation … Centralization), each printed as Urdu word, English term in brackets and Urdu meaning. The scan is skewed.'+NOTE
s['vocabulary']={}
save(s)
# scan 217 = 109_page_2 : printed 208
s=page(217,'farhang','208','Glossary (Farhang): alif (end), be, pe, fe','فرہنگ (Glossary): الف کا اختتام، ب، پ، ف','فرهنګ (Glossary): الف پای، ب، پ، ف','gl2')
F=Flow(s)
G(s,'افسر شاہی','Bureaucracy','ایسا نظام جس میں اصل اختیارات ملک کے اعلیٰ سرکاری ملازمین کے ہاتھوں میں ہوتے ہیں۔','a system in which the real powers are in the hands of the country’s senior government employees','داسې نظام چې په هغې کې اصلي اختیارات د هېواد د لوړو دولتي کارکوونکو په لاس کې وي.')
G(s,'احساسِ مدنیت','Civic Sense','شہری ملک میں رہنے کا احساس۔ حقوق و فرائض سے واقفیت۔','the feeling of being a citizen living in a country; awareness of rights and duties','د هېواد د اتباعو په توګه د ژوند احساس؛ له حقونو او دندو نه خبرتیا.')
G(s,'اقربا پروری','Nepotism','اہلیت کے خلاف اپنے دوستوں اور رشتہ داروں کو ترجیح دینا۔','to give preference to one’s friends and relatives against merit','د وړتیا پر ضد خپلو ملګرو او خپلوانو ته ترجیح ورکول.')
L(s,'(ب)','(be)','(ب)')
G(s,'بائیکاٹ','Boycott','کسی اجلاس یا کسی اور سرگرمی میں بطور احتجاج نہ بیٹھنا یا وہاں سے نکلنا۔','not to sit in some meeting or other activity as a protest, or to walk out of it','په کومه غونډه یا نور فعالیت کې د احتجاج په توګه نه کېناستل یا له هغه ځایه وتل.')
G(s,'بار اور بنچ','Bar and Bench','بار سے مراد وکلاء اور بنچ سے مراد جج صاحبان۔','by bar are meant lawyers and by bench the judges','له بار نه مراد وکیلان او له بنچ نه مراد قاضیان دي.')
L(s,'(پ)','(pe)','(پ)')
G(s,'پالیسی','Policy','حکمتِ عملی۔','strategy','تګلاره.')
G(s,'پنشن','Pension','سرکاری ملازمین کو ملازمت سے ریٹائر ہونے کے بعد تنخواہ کا ایک خاص حصہ دینا۔','giving government employees a particular part of the salary after retiring from service','دولتي کارکوونکو ته له دندې د تقاعد وروسته د معاش یوې ځانګړې برخې ورکول.')
G(s,'پسماندہ ممالک','Under-Developed Countries','وہ ممالک جنھوں نے ابھی ترقی کا سفر شروع نہیں کیا یا جو ترقی کے راستے پر گامزن نہیں۔','countries that have not yet begun the journey of progress or that are not moving on the path of progress','هغه هېوادونه چې لا يې د پرمختګ سفر نه دی پیل کړی یا چې د پرمختګ پر لاره روان نه دي.')
G(s,'پائیدار','Sustainable','جو برقرار رہ سکے۔','that which can remain established','هغه څه چې پاتې کېدای شي.')
L(s,'(ف)','(fe)','(ف)')
G(s,'فلور کراسنگ','Floor Crossing','مقننہ میں ایک رکن کا اپنے سیاسی جماعت سے وفاداری تبدیل کرنا۔','a member in the legislature changing loyalty from his political party','په مقننه کې د یو غړي له خپل سیاسي ګوند نه د وفادارۍ بدلول.')
G(s,'فلاحی ریاست','Welfare State','وہ ریاست جو عوامی فلاح کے لیے ترجیحی بنیادوں پر کام کرے خاص طور پر صحت، تعلیم اور روزگار کو یقینی بنائے۔','the state that works on a priority basis for the public welfare, especially ensuring health, education and employment','هغه دولت چې د ولسي هوساینې لپاره په ترجیحي بنسټ کار کوي په ځانګړې توګه روغتیا، زده کړه او کار یقیني کوي.')
G(s,'فریقین','Parties','کسی معاہدہ یا تنازعہ میں دونوں اطراف کے ملوثین۔','those involved on both sides in an agreement or dispute','په کوم تړون یا شخړه کې د دواړو خواو ښکېل کسان.')
G(s,'فرقہ','Sect','کسی مذہب کے اندر نظریاتی اختلاف کی بنیاد پر قائم گروہ۔','a group formed on the basis of ideological difference within a religion','د کوم مذهب دننه د نظریاتي اختلاف پر بنسټ جوړه شوې ډله.')
G(s,'فرقہ واریت','Sectarianism','فرقوں کی بنیاد پر لڑائی، تنازعات اور اختلافات وغیرہ۔','fighting, disputes and differences and so on on the basis of sects','د فرقو پر بنسټ جګړه، شخړې او اختلافات او نور.')
F.done()
s['sourceNote']='Printed page 208 (scan 217): the end of the entries under “الف”, then those under “ب”, “پ” and “ف” (Afsar-shahi … Sectarianism). The headings (ب)، (پ)، (ف) are printed in brackets. The scan is skewed.'+NOTE
s['vocabulary']={}
save(s)
# scan 218 = 109_page_1 : printed 209
s=page(218,'farhang','209','Glossary (Farhang): te, Te, jeem','فرہنگ (Glossary): ت، ٹ، ج','فرهنګ (Glossary): ت، ټ، ج','gl3')
F=Flow(s)
L(s,'(ت)','(te)','(ت)')
G(s,'ترقی پسند','Progressive','تبدیلی چاہنے والے۔','those who want change','هغه څوک چې بدلون غواړي.')
G(s,'پُرتشدد','Violent','خون ریز اور غیر پُرامن۔','bloody and non-peaceful','وینې تویوونکی او غیرسوله ییز.')
G(s,'تنقید','Criticism','کسی چیز وغیرہ کا مثبت اور خاص طور پر منفی پہلوؤں پر روشنی ڈالنا۔','to throw light on the positive and especially negative aspects of something and so on','د کوم شي او نورو پر مثبتو او په ځانګړې توګه منفي اړخونو رڼا اچول.')
G(s,'تفویضِ اختیارات','Delegation of Powers','وہ اختیارات جو ایک اعلیٰ اپنے ماتحت کو عارضی طور پر دے۔','powers that a superior gives to his subordinate temporarily','هغه اختیارات چې یو لوړ چارواکی خپل ماتحت ته په لنډمهاله ډول ورکوي.')
G(s,'ٹیکنوکریٹ','Technocrat','پیشہ ور۔ وہ فرد جو ایک خاص شعبۂ زندگی میں ماہر ہو اور اسی اہلیت کی بنیاد پر اسے نمائندہ مقرر کیا جائے۔','a professional; a person who is expert in a particular field of life and who is appointed a representative on this very ability','مسلکي. هغه فرد چې په ځانګړې ژوندي ډګر کې ماهر وي او د همدې وړتیا پر بنسټ استازی وټاکل شي.')
G(s,'توثیق','Ratification','کسی معاہدہ وغیرہ کی مجاز حکام کی طرف سے آخری منظوری۔','final approval of an agreement and so on by the competent authorities','د کوم تړون او نورو د مجازو چارواکو له خوا وروستۍ منظوري.')
G(s,'ترقی پذیر','Developing','وہ ممالک جو ترقی کے راستے پر گامزن ہوں۔','countries that are moving on the path of progress','هغه هېوادونه چې د پرمختګ په لاره روان وي.')
G(s,'تسلیم کرنا','Recognition','کسی ملک یا حکومت کا دوسرے ممالک یا حکومتوں کی طرف سے تسلیم کرنا اور اس کے ساتھ سفارتی تعلقات قائم کرنا۔','the acknowledgement of a country or government by other countries or governments and the establishment of diplomatic relations with it','د کوم هېواد یا حکومت د نورو هېوادونو یا حکومتونو له خوا منل او له هغه سره د سفارتي اړیکو جوړول.')
G(s,'تخلیقی','Creative','مثبت، کارآمد، مفید۔','positive, useful, beneficial','مثبت، ګټور، ګټه رسوونکی.')
L(s,'(ٹ)','(Te)','(ټ)')
G(s,'ٹیرف','Tariff','کسی ملک کا درآمدات و برآمدات پر عائد کردہ ٹیکس۔','tax imposed by a country on imports and exports','د کوم هېواد له خوا پر واردات او صادراتو لګول شوی مالیه.')
G(s,'ٹرسٹ','Trust','انسانی فلاح کے لیے با اعتماد افراد کی طرف سے قائم کردہ ادارہ۔ مثلاً انصار برنی ویلفیئر ٹرسٹ۔','an institution established for human welfare by trustworthy persons; for example Ansar Burney Welfare Trust','د انساني هوساینې لپاره د باوري کسانو له خوا جوړ شوې اداره. د بېلګې په توګه انصار برني ویلفیر ټرسټ.')
L(s,'(ج)','(jeem)','(ج)')
G(s,'جلاوطن','Exile','آبائی وطن سے باہر۔','outside one’s ancestral homeland','له آبایي وطن نه بهر.')
G(s,'جدول','Schedule','کسی دستاویز عام طور پر دستور کے آخر میں تفصیلات پر مبنی حصہ۔','a part based on details, generally at the end of a document, usually a constitution','د کوم سند معمولاً دستور په پای کې پر تفصیلاتو ولاړه برخه.')
G(s,'جارحیت','Aggression','بلا وجہ کسی ملک میں فوجی مداخلت۔','military interference in a country without cause','پرته له دلیل په کوم هېواد کې پوځي مداخله.')
F.done()
s['sourceNote']='Printed page 209 (scan 218): glossary entries under the letters “ت”, “ٹ” and “ج” (Progressive … Aggression). The list of entries on this page follows the printed order; the lower part of the page is blank. The scan is skewed.'+NOTE
s['vocabulary']={}
save(s)
