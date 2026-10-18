from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,ur,en,ps,g,**m): add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g,**m)
U='c05'
def Q(s,ur,en,ps,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',**k)
def QI(s,ur,en,ps,g): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'civics11-{U}-q',tab='exercise',listGroup=g)
def O(s,ur,en,ps): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'civics11-{U}-q',tab='exercise')
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 9.'
def mc(s,u,e,p,opts,g):
    QI(s,u,e,p,g)
    for k,(a,b) in zip(['الف','ب','ج','د'],zip('abcd',opts)):
        O(s,f'({k}) {b[0]}',f'({a}) {b[1]}',f'({k}) {b[2]}')
# scan 127 = 064_page_2 : printed 118
s=page(127,'c05','118','Exercise (Mashq): question 2 (items 2–5), question 3 (match the columns)','مشق: سوال 2 (۲–۵)، سوال 3 (کالم ملائیں)','تمرین: ۲ پوښتنه (۲–۵)، ۳ پوښتنه (کالمونه وصل کړئ)','ex5b')
F=Flow(s)
mc(s,'۲۔ حکومت میڈیا، مدرسہ اصلاحات اور نصاب وغیرہ کے ذریعے ________ رجحانات کی حوصلہ شکنی کر رہی ہے۔','2. The government is discouraging ________ tendencies through the media, madrasa reforms, the curriculum and so on.','۲. حکومت د رسنیو، مدرسې اصلاحاتو او نصاب او نورو له لارې ________ رجحاناتو ناهیلي کوي.',[('جمہوری','democratic','دیموکراتیک'),('انتہا پسندانہ','extremist','افراطي'),('مثبت','positive','مثبت'),('پائیدار','durable','پایدار')],'q2')
mc(s,'۳۔ اس وقت بھی پاکستان میں نسلی ٹکراؤ اور ________ خطرناک حد تک موجود ہے۔','3. Even now in Pakistan racial clash and ________ exist to a dangerous degree.','۳. اوس مهال هم په پاکستان کې نسلي ټکر او ________ خطرناک حد پورې موجود دی.',[('یکسانیت','sameness','یو شانتوب'),('تضاد','conflict','ټکر'),('بغاوت','rebellion','بغاوت'),('دولت','wealth','شتمني')],'q2')
mc(s,'۴۔ پاکستان میں ایک معیاری سیاسی ________ کا فقدان ہے۔','4. In Pakistan there is a lack of a standard political ________.','۴. په پاکستان کې د یو معیاري سیاسي ________ نشتوالی دی.',[('ثقافت','culture','کلتور'),('عدلیہ','judiciary','عدلیه'),('تعلیم','education','زده کړه'),('سکول','school','ښوونځی')],'q2')
mc(s,'۵۔ افغانستان کے حالات نے پاکستان کا ________ چھین لیا ہے۔','5. The conditions of Afghanistan have taken away Pakistan’s ________.','۵. د افغانستان حالاتو د پاکستان ________ اخیستی دی.',[('زمین','land','ځمکه'),('امن و سکون','peace and calm','امن او سکون'),('فوج','army','پوځ'),('طاقت','strength','ځواک')],'q2')
Q(s,'۳۔ کالم ملائیں:','3. Match the columns:','۳. کالمونه سره وصل کړئ:')
QI(s,'کالم الف: مفاداتی، کثیر، تہذیب و، طبقاتی، نسلی، امتیازی','Column A: mufadati (interest), kasir (multi-), tahzib o, tabqati (class), nasli (racial), imtiyazi (discriminatory)','کالم الف: ګټو، ډېر، تمدن او، طبقاتي، نسلي، امتیازي','q3')
QI(s,'کالم ب: النسلی، رویے، گروہ، فسادات، ثقافت، جنگ','Column B: al-nasli (-racial), rawaiye (attitudes), giroh (group), fasadat (riots), saqafat (culture), jang (war)','کالم ب: النسلی، رویې، ډله، فسادات، کلتور، جګړه','q3')
F.done()
s['sourceNote']='Printed page 118 (scan 127): question 2 items 2–5 (multiple choice with an answer box beside each; the first line of item 2 is cut at the top) and the heading “کالم ملائیں” of question 3 with the two columns (faint print, stored as lists; the pairing is not an answer key). Column A: مفاداتی، کثیر، تہذیب و، طبقاتی، نسلی، امتیازی; column B: النسلی، رویے، گروہ، فسادات، ثقافت، جنگ. The left edge is cut.'+NOTE
s['vocabulary']={}
save(s)
# scan 128 = 064_page_1 : printed 119
s=page(128,'c05','119','Exercise (Mashq): questions 4–5','مشق: سوال 4–5','تمرین: ۴–۵ پوښتنې','ex5c')
F=Flow(s)
Q(s,'۴۔ دیے گئے جملوں میں صحیح جملوں کو صحیح اور غلط جملوں کو غلط پر نشان لگائیں:','4. In the given sentences, mark the correct sentences “correct” and the wrong sentences “wrong”:','۴. په ورکړل شوو جملو کې سم جملې په «صحیح» او غلط جملې په «غلط» نښه کړئ:')
for u,e,p in [('۱۔ تضاد و تصادم تمام مسائل کا حل ہے۔ (صحیح / غلط)','1. Conflict and clash are the solution of all problems. (True / False)','۱. ټکر او تصادم د ټولو ستونزو حل دی. (صحیح / غلط)'),('۲۔ ثقافتوں کے درمیان تصادم ہوتے رہتے ہیں۔ (صحیح / غلط)','2. Clashes keep occurring among cultures. (True / False)','۲. د کلتورونو ترمنځ تصادمونه کېږي. (صحیح / غلط)'),('۳۔ بھارت اور پاکستان کے درمیان مسائل گفت و شنید سے حل نہیں ہو سکتے۔ (صحیح / غلط)','3. Problems between India and Pakistan cannot be solved through negotiation. (True / False)','۳. د هند او پاکستان ترمنځ ستونزې په خبرو اترو نه شي حل کېدای. (صحیح / غلط)'),('۴۔ جنگوں سے مسائل کبھی بھی حل نہیں ہوتے۔ (صحیح / غلط)','4. Problems are never solved by wars. (True / False)','۴. په جګړو ستونزې هیڅکله نه حل کېږي. (صحیح / غلط)'),('۵۔ پاکستان میں عورت کا اعلیٰ سماجی مقام ہے۔ (صحیح / غلط)','5. In Pakistan women have a high social position. (True / False)','۵. په پاکستان کې د ښځې لوړ ټولنیز مقام دی. (صحیح / غلط)'),('۶۔ پاکستان میں ایک معیاری سیاسی ثقافت کا فقدان ہے۔ (صحیح / غلط)','6. In Pakistan there is a lack of a standard political culture. (True / False)','۶. په پاکستان کې د یو معیاري سیاسي کلتور نشتوالی دی. (صحیح / غلط)'),('۷۔ مشترکہ مفادات کی کونسل ہر دو سال بعد اسلام آباد میں اجلاس منعقد کیے جاتے ہیں۔ (صحیح / غلط)','7. The Council of Common Interests holds sessions in Islamabad every two years. (True / False)','۷. د ګډو ګټو شورا هر دوه کاله وروسته په اسلام اباد کې غونډې کوي. (صحیح / غلط)'),('۸۔ مشترکہ منصوبہ پر مل کر کام کرنا مشترکہ کام کرنے کا عمل ہے۔ (صحیح / غلط)','8. Working together on a joint project is the process of working jointly. (True / False)','۸. په ګډ پلان یو ځای کار کول د ګډ کار کولو بهیر دی. (صحیح / غلط)')]:
    QI(s,u,e,p,'q4')
Q(s,'۵۔ درج ذیل سوالات کے مختصر جواب تحریر کریں:','5. Write short answers to the following questions:','۵. د لاندې پوښتنو لنډ ځوابونه ولیکئ:')
for u,e,p in [('۱۔ پاکستان کس طرح کثیر القومی ملک ہے؟','1. How is Pakistan a multi-national country?','۱. پاکستان څنګه ډېرقومي هېواد دی؟'),('۲۔ کن لوگوں کے ساتھ نامناسب رویے روا رکھے جاتے ہیں؟','2. With which people are improper attitudes practised?','۲. له کومو خلکو سره ناسم چلند روا ساتل کېږي؟'),('۳۔ معاشی طبقاتی ٹکراؤ کی بنیادی وجہ کیا ہے؟','3. What is the basic cause of economic class clash?','۳. د اقتصادي طبقاتي ټکر بنسټیز لامل څه دی؟'),('۴۔ پاکستان میں تشدد کے عالمی وجوہات کیا ہیں؟','4. What are the international causes of violence in Pakistan?','۴. په پاکستان کې د تاوتریخوالي نړیوال لاملونه کوم دي؟'),('۵۔ سودا بازی کی تعریف کریں۔','5. Define bargaining.','۵. د سودا کولو تعریف وکړئ.')]:
    QI(s,u,e,p,'q5')
F.done()
s['sourceNote']='Printed page 119 (scan 128): question 4 (eight true/false statements, with “صحیح۔غلط” written at the left of each) and question 5 (five short questions). Statement 7 is printed as “مشترکہ مفادات کی کونسل ہر دو سال بعد اسلام آباد میں اجلاس منعقد کیے جاتے ہیں” (read as printed). The right edge is cut.'+NOTE
s['vocabulary']={}
save(s)
# scan 129 = 065_page_2 : printed 120
s=page(129,'c05','120','Exercise (Mashq): question 6; practical activities','مشق: سوال 6؛ عملی سرگرمیاں','تمرین: ۶ پوښتنه؛ عملي فعالیتونه','ex5d')
F=Flow(s)
Q(s,'۶۔ مندرجہ ذیل سوالات کے مفصل جوابات دیں:','6. Give detailed answers to the following questions:','۶. د لاندې پوښتنو مفصل ځوابونه ورکړئ:')
for u,e,p in [('۱۔ تضاد یا تصادم کیا ہے اور اس کی بنیادی وجوہات کیا ہیں؟','1. What is conflict or clash and what are its basic causes?','۱. ټکر یا تصادم څه دی او بنسټیز لاملونه یې کوم دي؟'),('۲۔ تضادات کا حل کن طریقوں سے ممکن ہے؟','2. By which methods is the resolution of conflicts possible?','۲. د ټکرونو حل په کومو طریقو شونی دی؟'),('۳۔ پاکستان میں تصادم یا تضادات کی نشاندہی کریں اور وجوہات بیان کریں۔','3. Identify the clashes or conflicts in Pakistan and describe the causes.','۳. په پاکستان کې ټکرونه یا تصادمونه وپېژنئ او لاملونه یې بیان کړئ.'),('۴۔ تضاد، تصادم، جنگ یا ٹکراؤ کے ذریعے مسائل حل کرنے کے کیا نتائج ہوتے ہیں؟','4. What are the consequences of solving problems through conflict, clash, war or collision?','۴. د ټکر، تصادم، جګړې یا شخړې له لارې د ستونزو د حل پایلې څه وي؟'),('۵۔ پاکستان میں قومی سطح پر تضادات کو کیسے دیکھا گیا ہے؟ تفصیلی جواب دیں۔','5. How have conflicts been seen at the national level in Pakistan? Give a detailed answer.','۵. په پاکستان کې په ملي کچه ټکرونه څنګه لیدل شوي دي؟ تفصیلي ځواب ورکړئ.')]:
    QI(s,u,e,p,'q6')
H(s,'عملی سرگرمیاں:','Practical activities:','عملي فعالیتونه:')
for u,e,p in [('سرگرمی نمبر 1: کلاس میں نقلی تضاد پیدا کر کے گفت و شنید کے ذریعے حل کرنے کی مشق کریں۔','Activity 1: Create a mock conflict in the class and practise resolving it through negotiation.','فعالیت ۱: په ټولګي کې نقلي ټکر پیدا کړئ او د خبرو اترو له لارې د حل مشق وکړئ.'),('سرگرمی نمبر 2: تضاد کے وجوہات پر مضمون نویسی کا مقابلہ منعقد کریں۔','Activity 2: Hold an essay-writing competition on the causes of conflict.','فعالیت ۲: د ټکر د لاملونو په اړه د مقالې لیکنې سیالي وکړئ.'),('سرگرمی نمبر 3: کلاس میں اپنے علاقے کی ایسی شخصیت کو دعوت دیں جو جرگوں کے ذریعے مقامی تضادات و مسائل حل کرنے کی مہارت رکھتے ہوں اور وہ اپنے تجربات و مشاہدات پر لیکچر دیں۔','Activity 3: Invite to the class a personality of your area who has the skill of solving local conflicts and problems through jirgas, and have him give a lecture on his experiences and observations.','فعالیت ۳: په ټولګي کې د خپلې سیمې داسې شخصیت راوغواړئ چې د جرګو له لارې د سیمه ایزو ټکرونو او ستونزو د حل مهارت لري او هغه دې پر خپلو تجربو او مشاهداتو لیکچر ورکړي.')]:
    P(s,u,e,p)
F.done()
s['sourceNote']='Printed page 120 (scan 129): question 6 (five long questions) and a boxed panel “عملی سرگرمیاں” with three activities, the end of Chapter 5. The lower half of the page is blank. The right edge is cut; the page is skewed.'+NOTE
s['vocabulary']={}
save(s)
# scan 130 = 065_page_1 : printed 121 (chapter 6 opener)
s=page(130,'c06','121','Chapter 6: Intellectual Skills — learning objectives','باب 6: علمی مہارتیں — تدریسی مقاصد','۶ څپرکی: علمي مهارتونه — د تدریس موخې','ch6')
F=Flow(s)
P(s,'باب 6','Chapter 6','۶ څپرکی')
H(s,'علمی مہارتیں (Intellectual Skills)','Intellectual Skills','علمي مهارتونه (Intellectual Skills)')
P(s,'تدریسی مقاصد:','Learning objectives:','د تدریس موخې:',kind='heading')
P(s,'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter students will be able to:','د دې څپرکي له لوستلو وروسته به زده کوونکي دې ته وړ شي چې:')
for u,e,p in [
 ('۱۔ لفظ تفتیش کی تعریف کر سکیں۔','1. define the word inquiry (investigation).','۱. د تفتیش د ټکي تعریف وکړي.'),
 ('۲۔ تفتیشی عمل کے مراحل کی شناخت کر سکیں۔','2. identify the stages of the process of inquiry.','۲. د تفتیش د بهیر پړاوونه وپېژني.'),
 ('۳۔ مقامی یا ملکی کمیونٹی میں اہم مسائل اور واقعات کی نشاندہی کے قابل بن جائیں۔','3. become able to identify important problems and events in the local or national community.','۳. په سیمه ایزه یا ملي ټولنه کې مهمې ستونزې او پېښې وپېژني.'),
 ('۴۔ مقامی یا ملکی کمیونٹی میں اہم مسائل یا واقعات پر طلبہ اپنی مرضی کے ساتھ تفتیش کر سکیں۔','4. students be able to carry out an inquiry, of their own choice, on important problems or events in the local or national community.','۴. زده کوونکي په سیمه ایزه یا ملي ټولنه کې په مهمو ستونزو یا پېښو د خپلې خوښې سره تفتیش وکړي.'),
 ('۵۔ تعصب اور پروپیگنڈہ کی تعریف کر سکیں۔','5. define prejudice and propaganda.','۵. د تعصب او پروپېګنډا تعریف وکړي.'),
 ('۶۔ اُن آلات و وسائل (دیکھنے، پڑھنے اور سننے والے) کی شناخت کر سکیں جو تعصب پیدا کرتے ہیں۔','6. identify those tools and means (for seeing, reading and listening) that create prejudice.','۶. هغه وسایل او آلې (لیدو، لوستلو او اورېدلو) وپېژني چې تعصب پیدا کوي.'),
 ('۷۔ پروپیگنڈہ کے مختلف طریقوں کی نشاندہی کر سکیں۔','7. identify the different methods of propaganda.','۷. د پروپېګنډا بېلابېلې طریقې وپېژني.'),
 ('۸۔ مختلف اخبارات اور میگزین کی مختلف رپورٹوں میں یکسانیت اور اختلاف کا موازنہ کر سکیں۔','8. compare the similarity and difference in different reports of different newspapers and magazines.','۸. د بېلابېلو ورځپاڼو او مجلو په بېلابېلو راپورونو کې یو شانتوب او اختلاف پرتله کړي.'),
 ('۹۔ دی گئی معلومات سے منطقی نتائج اخذ کر سکیں۔','9. draw logical conclusions from the given information.','۹. له ورکړل شوو معلوماتو نه منطقي پایلې واخلي.')]:
    I(s,u,e,p,'objectives')
F.done()
s['sourceNote']='Printed page 121 (scan 130): chapter opener with the chapter badge “باب 6”, title “علمی مہارتیں (Intellectual Skills)” and nine learning objectives (the front contents list this chapter as “علمی مہارتیں”). The chapter title in the book’s chapter list (“Practical Skills”) was written before this page was read; the printed English caption here is “Intellectual Skills”. Some objective lines are printed slanted, and items 6 and 8 wrap onto a second line.'+NOTE
s['vocabulary']={}
save(s)
