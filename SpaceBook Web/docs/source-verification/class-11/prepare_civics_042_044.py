from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
U='c01'
def Q(s,ur,en,ps,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',**k)
def QI(s,ur,en,ps,g): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',listGroup=g)
def O(s,ur,en,ps): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'civics11-{U}-q',tab='exercise')
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 9.'
def mc(s,u,e,p,opts,g):
    QI(s,u,e,p,g)
    for a,(ou,oe,op) in zip(['الف','ب','ج','د'],opts):
        O(s,f'({a}) {ou}',f'({a[0] if False else {"الف":"a","ب":"b","ج":"c","د":"d"}[a]}) {oe}',f'({a}) {op}')
# scan 42 = 021_page_1 : printed 33
s=page(42,'c01','33','Exercise (Mashq) of Chapter 1: questions 1–2','باب 1 کی مشق: سوال 1–2','د ۱ څپرکي تمرین: ۱–۲ پوښتنې','ex1')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'۱۔ درج ذیل جملوں میں خالی جگہوں کو مناسب الفاظ سے پُر کیجیے:','1. Fill in the blanks in the following sentences with suitable words:','۱. په لاندې جملو کې تش ځایونه په مناسبو ټکو ډک کړئ:')
for u,e,p in [('۱۔ بعض انسانی ________ کے مفادات، عادات و رسم و رواج وغیرہ مشترک ہوتے ہیں۔','1. The interests, habits, customs and traditions and so on of some human ________ are common.','۱. د ځينو انساني ________ ګټې، عادتونه، رسم او رواج او نور ګډ وي.'),
 ('۲۔ قواعد و ضوابط کو عملی شکل دینے کے لیے باقاعدہ مشینری یا ________ کی ضرورت ہوتی ہے۔','2. To give practical shape to rules and regulations, a regular machinery or ________ is needed.','۲. د قواعدو او ضوابطو د عملي کولو لپاره منظم ماشینري یا ________ ته اړتیا وي.'),
 ('۳۔ اچھی حکومت ________ کی نیک نامی کا باعث ہوتی ہے۔','3. A good government is the cause of the good name of ________.','۳. ښه حکومت د ________ د نېکنامۍ لامل وي.'),
 ('۴۔ آئین کے دفعات 28–8 کا تعلق ________ سے ہے۔','4. Articles 8–28 of the constitution are concerned with ________.','۴. د اساسي قانون د ۸–۲۸ دفعو اړیکه له ________ سره ده.'),
 ('۵۔ اٹھارویں آئینی ترمیم کے ذریعے صوبہ سرحد کو ________ کا نام دیا گیا۔','5. By the eighteenth constitutional amendment the North-West Frontier Province was given the name ________.','۵. د اتلسم اساسي ترمیم په ذریعه سرحد ولایت ته د ________ نوم ورکړل شو.')]:
    QI(s,u,e,p,'q1')
Q(s,'۲۔ درج ذیل سوالات کا موزوں جواب یعنی الف، ب، ج یا د منتخب کر کے ہر سوال کے سامنے دیے گئے خالی خانہ میں لکھیں:','2. Choose the suitable answer, that is (a), (b), (c) or (d), and write it in the empty box beside each question:','۲. د لاندې پوښتنو مناسب ځواب یعنې الف، ب، ج یا د غوره کړئ او د هرې پوښتنې مخې ته ورکړل شوي تش خانه کې یې ولیکئ:')
mc(s,'۱۔ حکومت وہ مشینری ہے جو ریاستی ________ چلاتی ہے۔','1. Government is the machinery that runs the state’s ________.','۱. حکومت هغه ماشینري ده چې د دولت ________ پرمخ وړي.',[('نظام','system','نظام'),('مالیات','finance','مالیات'),('سیاسیات','politics','سیاسیات'),('عدالت','court','عدالت')],'q2')
mc(s,'۲۔ ریاست کے عناصر ________ ہیں۔','2. The elements of the state are ________.','۲. د دولت عناصر ________ دي.',[('دو','two','دوه'),('تین','three','درې'),('چار','four','څلور'),('پانچ','five','پنځه')],'q2')
mc(s,'۳۔ بہترین آئین وہ ہے جو ________ طور پر موجود ہو۔','3. The best constitution is the one that exists in a ________ way.','۳. غوره اساسي قانون هغه دی چې په ________ ډول موجود وي.',[('تحریری','written','لیکلې'),('غیر تحریری','unwritten','نالیکلې'),('قانونی','legal','قانوني'),('غیر قانونی','illegal','غیرقانوني')],'q2')
mc(s,'۴۔ 1973ء کے آئین میں ________ دفعات ہیں۔','4. In the 1973 Constitution there are ________ articles.','۴. د ۱۹۷۳ز اساسي قانون کې ________ دفعې دي.',[('380','380','۳۸۰'),('280','280','۲۸۰'),('180','180','۱۸۰'),('300','300','۳۰۰')],'q2')
QI(s,'۵۔ جمہوری نظام میں کئی ادارے ________ سازی کی سرگرمیوں میں مصروف ہوتے ہیں۔','5. In a democratic system many institutions are engaged in ________-making activities.','۵. په دیموکراتیک نظام کې ډېرې ادارې د ________ جوړولو په فعالیتونو بوختې وي.','q2')
F.done()
s['sourceNote']='Printed page 33 (scan 42): the “مشق” badge, question 1 (five fill-in-the-blank sentences) and question 2 (multiple-choice items with an empty answer box beside each); the options of item 5 are printed at the top of the next page. The right edge of the photograph is cut.'+NOTE
s['vocabulary']={}
save(s)
# scan 43 = 022_page_2 : printed 34
s=page(43,'c01','34','Exercise (Mashq): question 2 (end), questions 3–4','مشق: سوال 2 کا اختتام، سوال 3–4','تمرین: ۲ پوښتنې پای، ۳–۴ پوښتنې','ex2')
F=Flow(s)
for a,o in [('الف','فیصلہ'),('ب','قانون'),('ج','آئین'),('د','حکومت')]:
    pass
O(s,'(الف) فیصلہ','(a) decision','(الف) پرېکړه')
O(s,'(ب) قانون','(b) law','(ب) قانون')
O(s,'(ج) آئین','(c) constitution','(ج) اساسي قانون')
O(s,'(د) حکومت','(d) government','(د) حکومت')
Q(s,'۳۔ کالم الف اور کالم ب کو ملائیں:','3. Match column A with column B:','۳. د «الف» او «ب» کالمونه سره وصل کړئ:')
for a,b,ea,eb,pa,pb in [('قواعد','معاشرہ','rules','society','قواعد','ټولنه'),('سرکاری','حالات','official','conditions','دولتي','حالات'),('جمہوری','نمائندے','democratic','representatives','دیموکراتیک','استازي'),('عوامی','وضوابط','public','regulations','ولسي','ضوابط'),('ہنگامی','جسٹس','emergency','justice','بېړنی','جسټس'),('چیف','ملازمین','chief','employees','چیف','کارکوونکي')]:
    QI(s,f'کالم الف: {a} — کالم ب: {b}',f'Column A: {ea} — Column B: {eb}',f'کالم الف: {pa} — کالم ب: {pb}','q3')
Q(s,'۴۔ دیے گئے جملوں میں صحیح جملوں کو صحیح اور غلط جملوں کو غلط پر نشان لگائیں:','4. In the given sentences, mark the correct sentences “correct” and the wrong sentences “wrong”:','۴. په ورکړل شوو جملو کې سم جملې په «صحیح» او غلط جملې په «غلط» نښه کړئ:')
for u,e,p in [('۱۔ ریاست حکومت کا ایک شعبہ ہے۔ (صحیح / غلط)','1. The state is a department of the government. (True / False)','۱. دولت د حکومت یوه څانګه ده. (صحیح / غلط)'),
 ('۲۔ جلا وطن حکومتیں مؤثر نہیں ہوتیں۔ (صحیح / غلط)','2. Governments in exile are not effective. (True / False)','۲. جلاوطنه حکومتونه مؤثر نه وي. (صحیح / غلط)'),
 ('۳۔ آئین خاص شہریوں کے حقوق کا ضامن ہوتا ہے۔ (صحیح / غلط)','3. The constitution is the guarantor of the rights of particular citizens. (True / False)','۳. اساسي قانون د ځانګړو اتباعو د حقونو ضامن وي. (صحیح / غلط)'),
 ('۴۔ آئینی ترمیم صرف ایوانِ بالا میں پیش کی جا سکتی ہے۔ (صحیح / غلط)','4. A constitutional amendment can be presented only in the upper house. (True / False)','۴. اساسي ترمیم یواځې په پورتني مجلس کې وړاندې کېدای شي. (صحیح / غلط)'),
 ('۵۔ سینٹ کا انتخاب قومی اسمبلی پانچ سال کے لیے کرتی ہے۔ (صحیح / غلط)','5. The National Assembly elects the Senate for five years. (True / False)','۵. سنا ملي مجلس د پنځو کلونو لپاره ټاکي. (صحیح / غلط)'),
 ('۶۔ حکمتِ عملی کے اصولوں کو کسی عدالت میں چیلنج نہیں کیا جا سکتا۔ (صحیح / غلط)','6. The principles of policy cannot be challenged in any court. (True / False)','۶. د تګلارې اصول په هېڅ محکمه کې نه شي ننګول کېدای. (صحیح / غلط)'),
 ('۷۔ آٹھویں ترمیم میں صدر ایوب کے دور میں صدر کے اختیارات میں اضافہ کیا گیا۔ (صحیح / غلط)','7. In the eighth amendment, in the period of President Ayub, the powers of the President were increased. (True / False)','۷. په اتم ترمیم کې د ولسمشر ایوب په دور کې د ولسمشر په اختیاراتو کې زیاتوالی راوستل شو. (صحیح / غلط)'),
 ('۸۔ غیر تحریری آئین ارتقائی عمل کا نتیجہ ہوتا ہے۔ (صحیح / غلط)','8. An unwritten constitution is the result of an evolutionary process. (True / False)','۸. نالیکلی اساسي قانون د ارتقايي بهیر پایله وي. (صحیح / غلط)'),
 ('۹۔ بیوروکریسی مستقل پیشہ ور ماہرین کو کہا جاتا ہے۔ (صحیح / غلط)','9. Bureaucracy is the name given to permanent professional experts. (True / False)','۹. بیوروکراسي ته دایمي مسلکي متخصصین ویل کېږي. (صحیح / غلط)')]:
    QI(s,u,e,p,'q4')
F.done()
s['sourceNote']='Printed page 34 (scan 43): the options of item 2.5 (decision, law, constitution, government), question 3 (match the columns: six pairs), and question 4 (nine statements to be marked “صحیح / غلط”). In the match question the printed column A (قواعد، سرکاری، جمہوری، عوامی، ہنگامی، چیف) and column B (معاشرہ، حالات، نمائندے، وضوابط، جسٹس، ملازمین) are printed in different orders; the pairs here are shown in the printed row order and are not an answer key. Statement 7 reads “ایوب” as printed (in the scan the statement is printed so, although the eighth amendment belongs to Zia’s period in the text).'+NOTE
s['vocabulary']={}
save(s)
# scan 44 = 022_page_1 : printed 35
s=page(44,'c01','35','Exercise (Mashq): questions 5–6; practical activities','مشق: سوال 5–6؛ عملی سرگرمیاں','تمرین: ۵–۶ پوښتنې؛ عملي فعالیتونه','ex3')
F=Flow(s)
Q(s,'۵۔ درج ذیل سوالات کے مختصر جواب تحریر کریں:','5. Write short answers to the following questions:','۵. د لاندې پوښتنو لنډ ځوابونه ولیکئ:')
for u,e,p in [('۱۔ ریاست اور حکومت کی تعریف کریں۔','1. Define state and government.','۱. د دولت او حکومت تعریف وکړئ.'),('۲۔ برادری کی تعریف کریں۔','2. Define community (biradari).','۲. د برادرۍ تعریف وکړئ.'),('۳۔ کسی ملک کے لیے آئین کیوں ضروری ہے؟','3. Why is a constitution necessary for a country?','۳. د یو هېواد لپاره اساسي قانون ولې لازمي دی؟'),('۴۔ آئینِ پاکستان 1973ء کے مطابق وفاقیت سے کیا مراد ہے؟','4. According to the 1973 Constitution of Pakistan, what is meant by federalism?','۴. د پاکستان د ۱۹۷۳ز اساسي قانون له مخې له فدرالیت نه څه مراد دی؟'),('۵۔ آئین میں اٹھارویں ترمیم کے اہم نکات لکھیں؟','5. Write the important points of the eighteenth amendment to the constitution.','۵. په اساسي قانون کې د اتلسم ترمیم مهم ټکي ولیکئ.'),('۶۔ غیر سیاسی عاملہ کس طرح فیصلہ سازی پر اثر انداز ہوتی ہے؟','6. How does the non-political executive influence decision-making?','۶. غیر سیاسي اجرائیه په پرېکړه کولو څنګه اغېز کوي؟')]:
    QI(s,u,e,p,'q5')
Q(s,'۶۔ درج ذیل سوالات کے تفصیلی جواب تحریر کیجیے:','6. Write detailed answers to the following questions:','۶. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ:')
for u,e,p in [('۱۔ حکومت اور ریاست میں فرق واضح کریں نیز حکومت کا قیام کیوں ضروری ہے؟','1. Explain the difference between government and state, and why is the establishment of government necessary?','۱. د حکومت او دولت ترمنځ توپیر روښانه کړئ او دا چې د حکومت جوړېدل ولې لازمي دي؟'),('۲۔ آئین سے کیا مراد ہے اور ایک اچھے آئین کی نمایاں خصوصیات کون کون سی ہیں؟','2. What is meant by a constitution and what are the main characteristics of a good constitution?','۲. له اساسي قانون نه څه مراد دی او د یوه ښه اساسي قانون مهمې ځانګړتیاوې کومې دي؟'),('۳۔ پاکستان کے 1973ء کے آئین کی نمایاں خصوصیات کیا ہیں؟','3. What are the main features of the 1973 Constitution of Pakistan?','۳. د پاکستان د ۱۹۷۳ز اساسي قانون مهمې ځانګړتیاوې کومې دي؟'),('۴۔ پاکستان کے دستور میں کی گئی ترامیم پر نوٹ لکھیں نیز ان ترامیم سے جو مسائل ابھرے ان کا ذکر کریں؟','4. Write a note on the amendments made in the constitution of Pakistan and also mention the problems that arose from these amendments.','۴. د پاکستان په دستور کې شوو ترمیمونو یادښت ولیکئ او همدارنګه هغه ستونزې چې له دغو ترمیمونو راپورته شوې بیان کړئ.'),('۵۔ تحریری اور غیر تحریری آئین کیا ہیں اور ان کے نقائص و فوائد بیان کریں؟','5. What are written and unwritten constitutions? State their defects and benefits.','۵. لیکلی او نالیکلی اساسي قانون څه دي او د هغو نیمګړتیاوې او ګټې بیان کړئ؟'),('۶۔ سیاسی نظام سے کیا مراد ہے نیز اس کی خصوصیات بیان کریں؟','6. What is meant by a political system, and describe its characteristics.','۶. له سیاسي نظام نه څه مراد دی او ځانګړتیاوې یې بیان کړئ؟'),('۷۔ فیصلہ ساز سیاسی اداروں اور ان کی سرگرمیوں پر نوٹ لکھیں؟','7. Write a note on the decision-making political institutions and their activities.','۷. پرېکړه کوونکو سیاسي ادارو او د هغوی په فعالیتونو یادښت ولیکئ.')]:
    QI(s,u,e,p,'q6')
H(s,'عملی سرگرمیاں','Practical activities','عملي فعالیتونه')
P(s,'سرگرمی نمبر 1: اس باب میں کلاس میں کوئز کا اہتمام کریں۔','Activity 1: Arrange a quiz in the class on this chapter.','فعالیت ۱: په دې څپرکي کې په ټولګي کې کوئز ترتیب کړئ.')
P(s,'سرگرمی نمبر 2: دستور 1973ء پر کلاس میں تقریری مقابلہ کریں۔','Activity 2: Hold a speech competition in the class on the 1973 Constitution.','فعالیت ۲: د ۱۹۷۳ز دستور په اړه په ټولګي کې د وینا سیالي وکړئ.')
F.done()
s['sourceNote']='Printed page 35 (scan 44): question 5 (six short-answer questions), question 6 (seven long-answer questions) and “عملی سرگرمیاں” with two activities, the end of Chapter 1. The right edge is cut.'+NOTE
s['vocabulary']={}
save(s)
