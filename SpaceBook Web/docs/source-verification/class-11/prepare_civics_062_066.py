from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,ur,en,ps,g,**m): add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g,**m)
U='c02'
def Q(s,ur,en,ps,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',**k)
def QI(s,ur,en,ps,g): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',listGroup=g)
def O(s,ur,en,ps): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'civics11-{U}-q',tab='exercise')
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 9. Words at the cut edge of the photographed page are restored from context and the Word text.'
def mc(s,u,e,p,opts,g):
    QI(s,u,e,p,g)
    for k,(a,b) in zip(['الف','ب','ج','د'],zip('abcd',opts)):
        O(s,f'({k}) {b[0]}',f'({a}) {b[1]}',f'({k}) {b[2]}')
# scan 62 = 031_page_1 : printed 53
s=page(62,'c02','53','Basis of governments (3–4); Exercise (Mashq) of Chapter 2: question 1','حکومتوں کی بنیادیں (۳–۴)؛ باب 2 کی مشق: سوال 1','د حکومتونو بنسټونه (۳–۴)؛ د ۲ څپرکي تمرین: ۱ پوښتنه','basis2')
F=Flow(s)
H(s,'۳۔ تاریخ (History)','3. History','۳. تاریخ (History)')
P(s,'طرزِ حکومت پر اُس ملک کی تاریخ کا گہرا اثر ہوتا ہے۔ برطانیہ میں بادشاہت اور پارلیمانی طرزِ حکومت کی وجوہات میں وہاں کی بادشاہت اور پارلیمانی نظام کی ایک طویل تاریخ ہے۔','The history of a country has a deep effect on its form of government. Among the reasons for monarchy and the parliamentary form of government in Britain is the long history of monarchy and the parliamentary system there.','د حکومتي طرز په هغه هېواد تاریخ ژور اغېز لري. په برتانیه کې د پاچاهۍ او پارلماني حکومتي طرز له لاملونو د هغه ځای د پاچاهۍ او پارلماني نظام اوږد تاریخ دی.')
H(s,'۴۔ اقدار وغیرہ (Values)','4. Values, etc.','۴. ارزښتونه او نور (Values)')
P(s,'طرزِ حکومت پر کسی ملک کے عوام کے اقدار وغیرہ کا بھی اثر ہوتا ہے۔ بعض ریاستیں ایسی ہیں جن میں اُن کے معاشرتی اقدار کے مطابق حکومتیں بنائی جاتی ہیں۔ اقدار میں عوام کی مرضی شامل ہوتی ہے۔ اسلامی حکومت میں مذہبی اقدار کا بہت خیال رکھا جاتا ہے۔','The values and so on of the people of a country also affect the form of government. There are some states in which governments are formed according to their social values. The will of the people is included in values. In the Islamic government great care is taken of religious values.','د حکومتي طرز په یو هېواد د خلکو ارزښتونو او نورو هم اغېز لري. ځينې دولتونه داسې دي چې په هغو کې د هغوی د ټولنیزو ارزښتونو سره سم حکومتونه جوړېږي. په ارزښتونو کې د خلکو رضا شامله وي. په اسلامي حکومت کې د مذهبي ارزښتونو ډېر خیال ساتل کېږي.')
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'۱۔ درج ذیل جملوں میں خالی جگہوں کو مناسب الفاظ سے پُر کریں:','1. Fill in the blanks in the following sentences with suitable words:','۱. په لاندې جملو کې تش ځایونه په مناسبو ټکو ډک کړئ:')
for u,e,p in [('۱۔ بھارت اور پاکستان میں ________ جمہوریت ہے۔','1. In India and Pakistan there is ________ democracy.','۱. په هند او پاکستان کې ________ جمهوریت دی.'),('۲۔ برطانیہ میں ________ بادشاہت قائم ہے۔','2. In Britain a ________ monarchy is established.','۲. په برتانیه کې ________ پاچاهي قایمه ده.'),('۳۔ جمہوری نظام میں عوام کی تجاویز اور مطالبات کی ________ کی جاتی ہے۔','3. In the democratic system the suggestions and demands of the people are ________.','۳. په دیموکراتیک نظام کې د خلکو وړاندیزونه او غوښتنې ________ کېږي.'),('۴۔ عوام کی بھرپور ________ حکومت پر نگرانی کا ایک ذریعہ ہوتی ہے۔','4. The full ________ of the people is a means of watching the government.','۴. د خلکو بشپړ ________ پر حکومت د څارنې یوه وسیله وي.'),('۵۔ وقتی طور پر لوگ ________ کا پُرجوش استقبال کرتے ہیں۔','5. For the time being people give an enthusiastic welcome to ________.','۵. په وخت کې خلک د ________ پُرجوش هرکلی کوي.')]:
    QI(s,u,e,p,'q1')
F.done()
s['sourceNote']='Printed page 53 (scan 62): bases 3 “تاریخ” and 4 “اقدار وغیرہ” of the forms of government, the “مشق” badge and question 1 (five fill-in-the-blank sentences). Pen signatures at the right margin are ignored. The photograph is cut at the right edge.'+NOTE
s['vocabulary']={}
save(s)
# scan 63 = 032_page_2 : printed 54
s=page(63,'c02','54','Exercise (Mashq): question 2 (multiple choice), question 3 (start)','مشق: سوال 2 (کثیر انتخابی)، سوال 3 کا آغاز','تمرین: ۲ پوښتنه (څو انتخابي)، د ۳ پوښتنې پیل','ex2a')
F=Flow(s)
Q(s,'۲۔ درج ذیل سوالات کا موزوں جواب یعنی الف، ب، ج یا د منتخب کر کے ہر سوال کے سامنے دیے گئے خالی خانہ میں لکھیں:','2. Choose the suitable answer, that is (a), (b), (c) or (d), and write it in the empty box beside each question:','۲. د لاندې پوښتنو مناسب ځواب یعنې الف، ب، ج یا د غوره کړئ او د هرې پوښتنې مخې ته ورکړل شوي تش خانه کې یې ولیکئ:')
mc(s,'۱۔ ________ میں بادشاہ کو لامحدود اختیارات حاصل ہوتے ہیں۔','1. In ________ the king has unlimited powers.','۱. په ________ کې پاچا ته نامحدود اختیارات حاصل وي.',[('بادشاہت','monarchy','پاچاهي'),('وزارت','ministry','وزارت'),('آمریت','dictatorship','استبداد'),('جمہوریت','democracy','جمهوریت')],'q2')
mc(s,'۲۔ جدید جمہوریت میں تمام شہریوں کو تمام امتیازات سے بالاتر ہو کر مساوی ________ حاصل ہے۔','2. In modern democracy all citizens, rising above all distinctions, have equal ________.','۲. په نوي جمهوریت کې ټولو اتباعو ته د ټولو امتیازاتو نه پورته مساوي ________ حاصل دي.',[('حقوق','rights','حقوق'),('ملازمت','employment','دنده'),('شہریت','citizenship','اتباعیت'),('ملکیت','property','ملکیت')],'q2')
mc(s,'۳۔ آمرانہ نظام میں اختیارات کی ________ ہوتی ہے۔','3. In a dictatorial system there is ________ of powers.','۳. په استبدادي نظام کې د اختیاراتو ________ وي.',[('مرکزیت','centralisation','مرکزیت'),('تقسیم','division','ویش'),('ارتکاز','concentration','تمرکز'),('حکومت','government','حکومت')],'q2')
mc(s,'۴۔ اسلامی طرزِ حکومت میں ________ نظام ہوتا ہے۔','4. In the Islamic form of government there is a ________ system.','۴. په اسلامي حکومتي طرز کې ________ نظام وي.',[('شورائی','consultative','شورايي'),('وحدانی','unitary','واحدي'),('وفاقی','federal','فدرالي'),('صدارتی','presidential','ولسمشریز')],'q2')
mc(s,'۵۔ حضور ﷺ نے آخری خطبہ میں انسانی ________ کا منشور پیش کیا۔','5. The Holy Prophet ﷺ presented the charter of human ________ in the Last Sermon.','۵. حضور ﷺ په وروستي خطبه کې د انساني ________ منشور وړاندې کړ.',[('حقوق','rights','حقونو'),('فرائض','duties','دندو'),('خدمت','service','خدمت'),('جذبہ','spirit','جذبه')],'q2')
Q(s,'۳۔ کالم ملائیں:','3. Match the columns:','۳. کالمونه سره وصل کړئ:')
F.done()
s['sourceNote']='Printed page 54 (scan 63): question 2 (five multiple-choice items with an empty answer box beside each) and the heading of question 3 “کالم ملائیں” with the first four words of the two columns (right column: سیاسی، انتقال، اجتماعی، حزب; left column: اقتدار، اختلاف، بحران، بادشاہت); the rest of the columns is on the next page. The column headings are too faint to read.'+NOTE
s['vocabulary']={}
save(s)
# scan 64 = 032_page_1 : printed 55
s=page(64,'c02','55','Exercise (Mashq): questions 3 (end)–6','مشق: سوال 3 کا اختتام تا 6','تمرین: د ۳ پوښتنې پای تر ۶','ex2b')
F=Flow(s)
QI(s,'کالم کے مزید الفاظ: دستوری، لیکن، ابراہم، مفادات','More words of the columns: dastoori, lekin, Ibrahim, mufadat','د کالمونو نور ټکي: دستوري، لیکن، ابراهیم، ګټې','q3')
Q(s,'۴۔ دیے گئے جملوں میں صحیح جملوں کو صحیح اور غلط جملوں کو غلط پر نشان لگائیں:','4. In the given sentences, mark the correct sentences “correct” and the wrong sentences “wrong”:','۴. په ورکړل شوو جملو کې سم جملې په «صحیح» او غلط جملې په «غلط» نښه کړئ:')
for u,e,p in [('۱۔ آمریت حکومت کی ایک قسم ہے۔ (صحیح / غلط)','1. Dictatorship is a kind of government. (True / False)','۱. استبداد د حکومت یو ډول دی. (صحیح / غلط)'),('۲۔ بادشاہت کو نمائندہ حکومت بھی کہا جا سکتا ہے۔ (صحیح / غلط)','2. Monarchy can also be called representative government. (True / False)','۲. پاچاهي ته استازیتوب لرونکی حکومت هم ویلای شو. (صحیح / غلط)'),('۳۔ جمہوریت میں سیاسی جماعتیں مسائل پیدا کرنے کا سبب ہوتی ہیں۔ (صحیح / غلط)','3. In democracy political parties are a cause of creating problems. (True / False)','۳. په جمهوریت کې سیاسي ګوندونه د ستونزو د پیدا کولو لامل وي. (صحیح / غلط)'),('۴۔ آئین میں حکومت کی تبدیلی کے لیے پُرامن راستے موجود ہوتے ہیں۔ (صحیح / غلط)','4. Peaceful paths for changing the government exist in the constitution. (True / False)','۴. په اساسي قانون کې د حکومت د بدلون لپاره سوله ییزې لارې موجودې وي. (صحیح / غلط)'),('۵۔ دستور کی پاسداری ریاست میں امن و امان اور خوشحالی کی ضامن ہے۔ (صحیح / غلط)','5. Adherence to the constitution is the guarantor of peace, order and prosperity in the state. (True / False)','۵. د دستور پالنه په دولت کې د امن او هوساینې ضامن دی. (صحیح / غلط)'),('۶۔ آمریت جمہوریت کی ضد ہے۔ (صحیح / غلط)','6. Dictatorship is the opposite of democracy. (True / False)','۶. استبداد د جمهوریت ضد دی. (صحیح / غلط)'),('۷۔ ایوب خان کی ترقیاتی منصوبوں سے حوصلہ افزاء نتائج برآمد ہوئے۔ (صحیح / غلط)','7. Ayub Khan’s development projects produced encouraging results. (True / False)','۷. د ایوب خان له پرمختیايي پروژو هیله بښونکې پایلې رامنځته شوې. (صحیح / غلط)'),('۸۔ اسلامی حکومت انسانی حقوق کو یقینی بناتی ہے۔ (صحیح / غلط)','8. The Islamic government ensures human rights. (True / False)','۸. اسلامي حکومت انساني حقونه یقیني کوي. (صحیح / غلط)')]:
    QI(s,u,e,p,'q4')
Q(s,'۵۔ درج ذیل سوالات کے مختصر جواب لکھیں:','5. Write short answers to the following questions:','۵. د لاندې پوښتنو لنډ ځوابونه ولیکئ:')
for u,e,p in [('۱۔ دستوری بادشاہت سے کیا مراد ہے؟ مثال سے واضح کریں؟','1. What is meant by constitutional monarchy? Explain with an example.','۱. له اساسي پاچاهۍ نه څه مراد دی؟ په بېلګې روښانه کړئ.'),('۲۔ آمریت میں مخصوص طبقے کی کیسے اجارہ داری ہوتی ہے؟','2. How does a particular class get a monopoly in dictatorship?','۲. په استبداد کې د یوې ځانګړې طبقې اجاره داري څنګه وي؟'),('۳۔ جمہوریت کی تعریف کریں؟','3. Define democracy.','۳. د جمهوریت تعریف وکړئ؟'),('۴۔ اسلام میں اقتدارِ اعلیٰ کا تصور کیا ہے؟','4. What is the concept of sovereignty in Islam?','۴. په اسلام کې د لوړ واک تصور څه دی؟'),('۵۔ فلاحی سرگرمیوں سے کیا مراد ہے؟','5. What is meant by welfare activities?','۵. له فلاحي فعالیتونو نه څه مراد دی؟')]:
    QI(s,u,e,p,'q5')
Q(s,'۶۔ درج ذیل سوالات کے تفصیلی جواب تحریر کریں:','6. Write detailed answers to the following questions:','۶. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ:')
for u,e,p in [('۱۔ بادشاہت کی تعریف کریں اور اس کی نمایاں خصوصیات بیان کریں؟','1. Define monarchy and describe its main characteristics.','۱. د پاچاهۍ تعریف وکړئ او مهمې ځانګړتیاوې یې بیان کړئ؟'),('۲۔ جمہوریت سے کیا مراد ہے نیز اس کے خواص کیا ہیں؟','2. What is meant by democracy, and what are its features?','۲. له جمهوریت نه څه مراد دی او ځانګړتیاوې یې کومې دي؟')]:
    QI(s,u,e,p,'q6')
F.done()
s['sourceNote']='Printed page 55 (scan 64): the last words of the question 3 columns (printed at the top: دستوری، لیکن، ابراہم، مفادات), question 4 (eight true/false statements), question 5 (five short questions) and the start of question 6 (two long questions). The column words are not paired reliably in the scan and are stored as a list. Statement 5 is read as “دستور کی پاسداری” (the word is smudged in the scan); the numbering is as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 65 = 033_page_2 : printed 56
s=page(65,'c02','56','Exercise (Mashq): questions 6 (3–5); practical activities','مشق: سوال 6 (۳–۵)؛ عملی سرگرمیاں','تمرین: ۶ پوښتنه (۳–۵)؛ عملي فعالیتونه','ex2c')
F=Flow(s)
for u,e,p in [('۳۔ آمریت کسے کہتے ہیں اور آمریت کی خصوصیات تفصیل سے لکھیں؟','3. What is dictatorship called and write in detail the characteristics of dictatorship.','۳. استبداد ته څه ویل کېږي او د استبداد ځانګړتیاوې په تفصیل ولیکئ؟'),('۴۔ اسلام کے سیاسی نظام پر نوٹ لکھیں اور اس کی خصوصیات پر بحث کیجیے؟','4. Write a note on the political system of Islam and discuss its characteristics.','۴. د اسلام په سیاسي نظام یادښت ولیکئ او ځانګړتیاوې یې وڅېړئ؟'),('۵۔ طرزہائے حکومت کی مختلف بنیادیں کیا ہیں؟ تفصیل سے جواب دیں۔','5. What are the different bases of the forms of government? Answer in detail.','۵. د حکومتي ډولونو بېلابېل بنسټونه کوم دي؟ په تفصیل ځواب ورکړئ.')]:
    add(s,f'q{len(s["paras"])+1}',e,u,p,role='question',exerciseId='civics11-c02-q',tab='exercise',listGroup='q6')
H(s,'عملی سرگرمیاں:','Practical activities:','عملي فعالیتونه:')
P(s,'سرگرمی نمبر 1: کلاس میں مختلف طرزہائے حکومت میں شہریوں کے کردار پر مباحثہ کیا جائے۔','Activity 1: A debate should be held in the class on the role of citizens in the different forms of government.','فعالیت ۱: په ټولګي کې په بېلابېلو حکومتي ډولونو کې د اتباعو د رول په اړه مباحثه وشي.')
P(s,'سرگرمی نمبر 2: جمہوریت کے موضوع پر کلاس میں تقریری مقابلہ منعقد کریں۔','Activity 2: Hold a speech competition in the class on the topic of democracy.','فعالیت ۲: د جمهوریت په موضوع په ټولګي کې د وینا سیالي ترتیب کړئ.')
F.done()
s['sourceNote']='Printed page 56 (scan 65): questions 6 (3)–(5) and a boxed panel “عملی سرگرمیاں” with two activities, the end of Chapter 2; the rest of the page is blank. The right edge is cut.'+NOTE
s['vocabulary']={}
save(s)
# scan 66 = 033_page_1 : printed 57 (chapter 3 opener)
s=page(66,'c03','57','Chapter 3: Human Rights — learning objectives','باب 3: حقوق — تدریسی مقاصد','۳ څپرکی: حقوق — د تدریس موخې','ch3')
F=Flow(s)
P(s,'باب 3','Chapter 3','۳ څپرکی')
H(s,'حقوق (Human Rights)','Rights (Human Rights)','حقوق (Human Rights)')
P(s,'تدریسی مقاصد:','Learning objectives:','د تدریس موخې:',kind='heading')
P(s,'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter students will be able to:','د دې څپرکي له لوستلو وروسته به زده کوونکي دې ته وړ شي چې:')
for u,e,p in [
 ('۱۔ انسانی حقوق کی تعریف کر سکیں۔','1. define human rights.','۱. د انساني حقونو تعریف وکړي.'),
 ('۲۔ انسانی حقوق کے تصور (اسلام کے خصوصی حوالے سے بھی) کے ارتقاء کو معلوم کر سکیں۔','2. trace the evolution of the concept of human rights (with special reference to Islam as well).','۲. د انساني حقونو د تصور (د اسلام په ځانګړي حواله هم) ارتقا معلومه کړي.'),
 ('۳۔ اعلامیہ اور کنونشن میں فرق کر سکیں۔','3. differentiate between a declaration and a convention.','۳. د اعلامیې او کنوانسیون ترمنځ توپیر وکړي.'),
 ('۴۔ اس حقیقت کو سمجھ کر تشریح کر سکیں کہ انسانی حقوق ناقابلِ تقسیم، باہمی طور پر منحصر اور متعلقہ ہیں۔','4. understand and explain the fact that human rights are indivisible, mutually dependent and interrelated.','۴. دې حقیقت ته په پوهېدو سره تشریح کړي چې انساني حقونه نه ویشل کېدونکي، په متقابل ډول متکي او اړوند دي.'),
 ('۵۔ آئینی حقوق کی سیاسی، اقتصادی، شخصی، معاشرتی اور ثقافتی حقوق میں درجہ بندی کر سکیں۔','5. classify constitutional rights into political, economic, personal, social and cultural rights.','۵. اساسي حقونه په سیاسي، اقتصادي، شخصي، ټولنیزو او کلتوري حقونو کې طبقه بندي کړي.'),
 ('۶۔ اس حد کا جائزہ لے سکیں جس حد تک پاکستانی شہریوں کے حقوق یقینی بنائے گئے ہیں۔','6. review the extent to which the rights of Pakistani citizens have been ensured.','۶. هغه حد وڅېړي چې تر کومه حده د پاکستاني اتباعو حقونه یقیني شوي دي.'),
 ('۷۔ اسلام میں دیے گئے دستوری انسانی حقوق و فرائض کا انسانی حقوق کے عالمی منشور میں دیے گئے حقوق و فرائض کے ساتھ موازنہ کر سکیں۔','7. compare the constitutional human rights and duties given in Islam with the rights and duties given in the Universal Declaration of Human Rights.','۷. په اسلام کې ورکړل شوي دستوري انساني حقونه او دندې د انساني حقونو په نړیوال منشور کې ورکړل شوو حقونو او دندو سره پرتله کړي.')]:
    I(s,u,e,p,'objectives')
F.done()
s['sourceNote']='Printed page 57 (scan 66): chapter opener with the chapter badge “باب 3”, title “حقوق (Human Rights)” and seven learning objectives. The right edge is cut; the item 6 numeral is printed “-٦”.'+NOTE
s['vocabulary']={}
save(s)
