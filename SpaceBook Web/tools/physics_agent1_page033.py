from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
groups=[
 [tr('Write the number in prefix to power of ten.','اعداد کو دس کی قوت کے سابقے کی صورت میں لکھیں۔','عددونه د لس د طاقت د مختاړي په بڼه ولیکئ.'),
 tr('a. Mechanical nano-oscillators can detect a mass change as small as 10⁻²¹ kg.','a. میکانی نینو ارتعاش گر کمیت میں 10⁻²¹ کلوگرام جتنی چھوٹی تبدیلی معلوم کر سکتے ہیں۔','a. میخانیکي نانو اهتزاز کوونکي په کتله کې د 10⁻²¹ کیلوګرام په څېر کوچنی بدلون کشف کولای شي.'),
 tr('b. The nearest neutron star (a collapsed star made primarily of neutrons) is about 3.00 × 10¹⁸ m away from Earth.','b. قریب ترین نیوٹرون ستارہ (منہدم ستارہ جو بنیادی طور پر نیوٹرونوں سے بنا ہو) زمین سے تقریباً 3.00 × 10¹⁸ میٹر دور ہے۔','b. تر ټولو نږدې نیوتروني ستوری (یو نړېدلی ستوری چې عمدتاً له نیوترونونو جوړ دی) له ځمکې نږدې 3.00 × 10¹⁸ متره لرې دی.'),
 tr('c. Earth to sun distance is 149.6 million kilometere.','c. زمین سے سورج کا فاصلہ 149.6 ملین کلومیٹر ہے۔','c. له ځمکې څخه تر لمر پورې واټن 149.6 میلیونه کیلومتره دی.')],
 [tr('An angstrom (symbol Å) is a unit of length (commonly used in atomic physics), defined as 10⁻¹⁰ m which is of the order of the diameter of an atom.','اینگسٹروم (علامت Å) لمبائی کی اکائی ہے جو عام طور پر جوہری طبیعیات میں استعمال ہوتی ہے۔ اسے 10⁻¹⁰ میٹر کے طور پر تعریف کیا جاتا ہے، جو جوہر کے قطر کی سطح کا ہے۔','انګستروم (نښه Å) د اوږدوالي واحد دی چې عموماً په اټومي فزیک کې کارېږي. دا د 10⁻¹⁰ متر په توګه تعریف شوی چې د یوه اټوم د قطر په کچه دی.'),
 tr('a. How many nanometers are in 1.0 angstrom?','a. 1.0 اینگسٹروم میں کتنے نینومیٹر ہیں؟','a. په 1.0 انګستروم کې څو نانومتره دي؟'),
 tr('b. How many femtometers or fermis (the common unit of length in nuclear physics) are in 1.0 angstrom?','b. 1.0 اینگسٹروم میں کتنے فیمٹومیٹر یا فرمی (نیوکلیائی طبیعیات میں لمبائی کی عام اکائی) ہیں؟','b. په 1.0 انګستروم کې څو فېمټومتره یا فرمي (په هستوي فزیک کې د اوږدوالي عام واحد) دي؟'),
 tr('c. How many angstroms are in 1.0 m?','c. 1.0 میٹر میں کتنے اینگسٹروم ہیں؟','c. په 1.0 متر کې څو انګسترومه دي؟')],
 [tr('The speed of light is c = 299,792,458 m/s.','روشنی کی رفتار c = 299,792,458 میٹر فی سیکنڈ ہے۔','د رڼا سرعت c = 299,792,458 متره په ثانیه دی.'),
 tr('a. Write this value in scientific notation.','a. اس مقدار کو سائنسی علامتی صورت میں لکھیں۔','a. دا ارزښت په علمي نښان ولیکئ.'),
 tr('b. Express the speed of light to','b. روشنی کی رفتار کو درج ذیل تک ظاہر کریں:','b. د رڼا سرعت تر لاندې شمېرو پورې څرګند کړئ:'),
 tr('i. five significant figures,     ii. three significant figures.','i. پانچ بامعنی ہندسے؛     ii. تین بامعنی ہندسے۔','i. پنځه بامعنی شمېرې؛     ii. درې بامعنی شمېرې.')],
 [tr('Express the following in terms of powers of 10.','درج ذیل کو 10 کی قوتوں میں ظاہر کریں۔','لاندې د 10 د طاقتونو په بڼه څرګند کړئ.'),
 tr('a. 7 nanometre     b. 96 megawatt     c. 2 gigabite','a. 7 نینومیٹر     b. 96 میگاواٹ     c. 2 گیگابائٹ','a. 7 نانومتره     b. 96 مېګاواټه     c. 2 ګېګابایټه'),
 tr('d. 43 picofarad     e. 2 millimetre.','d. 43 پیکوفیرڈ     e. 2 ملی میٹر۔','d. 43 پیکوفاراډه     e. 2 ملي متره.')],
 [tr('Write the following numbers in standard form:','درج ذیل اعداد کو معیاری صورت میں لکھیں:','لاندې عددونه په معیاري بڼه ولیکئ:'),
 tr('a. Mass of Bacterial cell: 0.000,000,000,005 kg','a. بیکٹیریا کے خلیے کی کمیت: 0.000,000,000,005 کلوگرام۔','a. د باکتریايي حجرې کتله: 0.000,000,000,005 کیلوګرامه.'),
 tr('b. Diameter of Sun: 1,390,000,000 m','b. سورج کا قطر: 1,390,000,000 میٹر۔','b. د لمر قطر: 1,390,000,000 متره.')]
]
paras=[]
questions=[]
for i,group in enumerate(groups,1):
 p=group[0]
 paras.append(tr(str(i)+'. '+p['text'],str(i)+'. '+p['urdu'],str(i)+'. '+p['pashto']))
 paras.extend(group[1:])
 questions.append(dict(num=i,q=p['text'],urdu=p['urdu'],pashto=p['pashto'],subquestions=[dict(label=('a','b','c')[j] if i!=4 else ('a–c','d–e')[j],q=s['text'],urdu=s['urdu'],pashto=s['pashto']) for j,s in enumerate(group[1:])],ans='',answerProvidedInSource=False,sourcePdfPage=33,sourcePrintedPage=28))
links=['http://www.introduction-to-physics.com/','http://www.bipm.org/en/about-us/','http://www.rapidtables.com/convert/number/scientific-notation-converter.htm','http://www.flippingphysics.com/significant-figures.html']
save(dict(pdfPage=33,printedPage=28,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Numerical questions 1–5 / web links',textbookExercise=dict(numericalQuestions=questions),sections=[dict(code='source-u1-exercise-numerical',heading='Numerical Questions',paras=paras,blocks=[dict(type='question',number=q['num'],question=q['q'],subquestions=q['subquestions'],answerProvidedInSource=False) for q in questions]),dict(code='source-u1-web-links',heading='Web Links',paras=[tr(link,link,link) for link in links],blocks=[])],chapterEnd=True,comparison='All five numerical problems and subquestions retained; repaired OCR powers 10⁻²¹, 10¹⁸ and 10⁻¹⁰ against scan; original gigabite spelling retained; source links transcribed without browsing'))
render(34)
