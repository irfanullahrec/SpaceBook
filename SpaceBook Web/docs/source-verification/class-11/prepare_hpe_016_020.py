from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u01',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u01'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
c=cell
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def torso(cx,top=40):
    return (f'<circle cx="{cx}" cy="{top+20}" r="30" fill="#ffe0d6" stroke="#8d6e63"/>'
            f'<path d="M{cx-70} {top+210} Q{cx-70} {top+90} {cx} {top+85} Q{cx+70} {top+90} {cx+70} {top+210} Z" fill="#ffe0d6" stroke="#8d6e63"/>'
            f'<rect x="{cx-6}" y="{top+30}" width="12" height="70" fill="#4a7ab5"/>'
            f'<ellipse cx="{cx-28}" cy="{top+135}" rx="24" ry="42" fill="#b05f8e" stroke="#6a1b4d"/><ellipse cx="{cx+28}" cy="{top+135}" rx="24" ry="42" fill="#b05f8e" stroke="#6a1b4d"/>'
            f'<path d="M{cx-52} {top+185} Q{cx} {top+160} {cx+52} {top+185} L{cx+52} {top+210} L{cx-52} {top+210} Z" fill="#e57373" stroke="#b71c1c"/>')
# scan 16 = printed 12
s=page(16,'u01','12','Calories of food components; calorie table','غذائی اجزا کی کیلوریز','د غذايي اجزاوو کالوري','diabetes-3')
F=Flow(s)
P(s,[('ایک گرام پروٹین میں 4 حرارے','In one gram of protein: 4 calories','په یو ګرام پروټین کې ۴ حرارې',dict(listGroup='cl')),
('ایک گرام نشاستہ میں 4.1 حرارے','In one gram of starch: 4.1 calories','په یو ګرام نشاسته کې ۴.۱ حرارې',dict(listGroup='cl')),
('ایک گرام چکنائی میں 9.3 حرارے','In one gram of fat: 9.3 calories','په یو ګرام غوړي کې ۹.۳ حرارې',dict(listGroup='cl')),
('اس ترتیب سے شوگر کے مریض کو روزانہ 1500 حرارے پورے کرنے کے لیے خوراک دینی ضروری ہے۔ درج ذیل اجزاء کی کیلوریز دی گئی ہیں۔ اس کے مطابق چارٹ بنا کر شوگر کے مریض کو دیا جائے۔','In this way food must be given to a sugar patient to make up 1500 calories daily. The calories of the following ingredients are given. According to them a chart should be made and given to the sugar patient.','پدې ترتیب د شوګر ناروغ ته هره ورځ ۱۵۰۰ حرارې پوره کولو لپاره خوراک ورکول اړین دي. د لاندې اجزاوو کالوري ورکړل شوي. د هغو سره سم چارټ جوړ کړای شي او د شوګر ناروغ ته ورکړای شي.')])
F.tb(0)
P(s,[('شوگر کے مریض کو دن میں 1500 کیلوریز سے زیادہ خوراک استعمال نہیں کرنی چاہیے اور یہ بھی تین وقفوں سے استعمال کریں۔ ڈاکٹر کی ہدایت کے مطابق دوائی، ورزش اور نیند کا خیال رکھیں۔','A sugar patient should not consume more than 1500 calories of food in a day, and this too should be taken in three intervals. According to the doctor’s instruction take care of medicine, exercise and sleep.','د شوګر ناروغ باید په ورځ کې له ۱۵۰۰ کالوریو زیات خوراک ونه کاروي او دا هم په دریو وختونو کارول پکار دي. د ډاکټر د لارښوونې سره سم د درملو، تمرین او خوب پام وساتئ.'),
('1500 کیلوریز حاصل کرنے کے لیے غذائی چارٹ دیا گیا ہے۔ اس کے مطابق خوراک کو عمر، جنس اور پیشہ کو مدنظر رکھتے ہوئے ایڈجسٹ کریں۔ خوراک میں رد و بدل کر کے استعمال کریں۔','A dietary chart is given for obtaining 1500 calories. According to it adjust the food keeping in view age, sex and occupation. Use it by varying the food.','د ۱۵۰۰ کالوریو ترلاسه کولو لپاره غذايي چارټ ورکړل شوی. د هغه سره سم خوراک د عمر، جنس او مسلک په پام کې نیولو سره سمبال کړئ. په خوراک کې بدلون راوستلو سره یې وکاروئ.')])
F.done()
s['tables']=[table('Calories obtained from food ingredients (per 100 grams)','غذائی اجزاء سے حاصل ہونے والے حرارے (100 گرام)','له غذايي اجزاوو ترلاسه کېدونکې حرارې (۱۰۰ ګرام)',[c('Ingredient','اجزا','اجزا'),c('Calories','حرارے','حرارې')],[[c('Wheat','گندم','غنم'),c('0.36')],[c('Eggs','انڈے','هګۍ'),c('148')],[c('Mutton','چھوٹا گوشت','وړوکې غوښه'),c('163')],[c('Fish','مچھلی','کب'),c('176')],[c('Beans','لوبیا','لوبیا'),c('35')],[c('Butter','مکھن','کوچه'),c('715')]])]
s['sourceNote']='Printed page 12: calories per gram, one table (the printed header “100 گرام” spans the ingredient/calorie columns; the wheat entry reads 0.36 as printed) and two closing paragraphs.'+NOTE
s['vocabulary']={}
save(s)
# scan 17 = printed 13
s=page(17,'u01','13','Diet chart for a sugar patient (1500 calories)','شوگر کے مریض کے لیے غذائی چارٹ','د شوګر ناروغ لپاره غذايي چارټ','diabetes-4')
F=Flow(s)
H(s,'شوگر کے مریض کے لیے غذائی چارٹ','Diet Chart for a Sugar Patient','د شوګر ناروغ لپاره غذايي چارټ')
F.tb(0)
F.done()
rows=[('Bread (wheat)/double roti','روٹی (گندم)/ڈبل روٹی','ډوډۍ (غنم)/ډبل ډوډۍ','3 slices','3 سلائس','۳ سلایسونه','90','45','8','0','212'),
('Fruit (orange, malta, kinno)','فروٹ (سنگترہ، مالٹا، کینو)','میوه (نارنج، مالټا، کینو)','2 medium','دو در میانے','دوه منځنۍ','450','45','0','0','180'),
('Vegetables','سبزیاں','سبزیجات','4 pieces','4 ٹکڑے','۴ ټوټې','600','20','6','0','104'),
('Milk','دودھ','شیدې','1½ cups','ڈیڑھ کپ','یو نیم پیاله','350','18','12','12','228'),
('Egg','انڈا','هګۍ','one','ایک','یوه','60','0','6','6','78'),
('Meat','گوشت','غوښه','--','--','--','150','0','35','25','365'),
('Butter','مکھن','کوچه','--','--','--','30','0','0','25','225'),
('Biscuits','بسکٹ','بسکټ','3 pieces','3 عدد','۳ دانې','32','9','7','5','108')]
s['tables']=[table('Diet chart for a sugar patient','شوگر کے مریض کے لیے غذائی چارٹ','د شوګر ناروغ لپاره غذايي چارټ',[c('Food','خوراک/غذا','خوراک/غذا'),c('Portion','حصے','برخې'),c('Grams','گرام','ګرامه'),c('Starch','نشاستہ','نشاسته'),c('Protein','لحمیات','لحمیات'),c('Fat','چکنائی','غوړي'),c('Calories','کیلوریز','کالوري')],[[c(r[0],r[1],r[2]),c(r[3],r[4],r[5]),c(r[6]),c(r[7]),c(r[8]),c(r[9]),c(r[10])] for r in rows]+[[c('Total calories','ٹوٹل کیلوریز','ټول کالوري'),c('')]*5+[c('1500')]])]
s['sourceNote']='Printed page 13: diet chart (eight foods with portion, grams, starch, protein, fat, calories) with a total of 1500 calories; the lower third of the page is blank. The printed order of columns is food, portion, grams, starch, protein, fat, calories; the table is kept in that order and the figures add to 1500.'+NOTE
s['vocabulary']={}
save(s)
# scan 18 = printed 14
s=page(18,'u01','14','Exercise questions: Chapter 1','مشقی سوالات: باب 1','تمرین پوښتنې: لومړی څپرکی','ex1')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جواب منتخب کر کے لکھیں۔','1. Select the suitable answer and write it.','۱. مناسب ځواب وټاکئ او ولیکئ.')
Q(s,'i۔ تمباکو نوشی سے ________ کا خدشہ رہتا ہے۔','i. Tobacco use carries the risk of ________.','i. تمباکو څکولو سره د ________ خدشه وي.')
for t in [('(الف) ذیابطیس','(a) diabetes','(الف) شکر ناروغي'),('(ب) دل کی بیماریوں','(b) heart diseases','(ب) د زړه ناروغیو'),('(ج) معدہ','(c) stomach','(ج) معده'),('(د) دماغی','(d) brain-related','(د) دماغي')]: O(s,*t)
Q(s,'ii۔ غذاء میں ________ کی مقدار کم کر کے دل کی بیماریوں کو کم کیا جا سکتا ہے۔','ii. By reducing the amount of ________ in food, heart diseases can be reduced.','ii. په غذا کې د ________ اندازه کمولو سره د زړه ناروغۍ کمېدای شي.')
for t in [('(الف) گوشت','(a) meat','(الف) غوښه'),('(ب) چکنائی','(b) fat','(ب) غوړي'),('(ج) لحمیات','(c) proteins','(ج) لحمیات'),('(د) پانی','(d) water','(د) اوبه')]: O(s,*t)
Q(s,'iii۔ شوگر کا مرض ________ کی خرابی کی وجہ سے پیدا ہوتا ہے۔','iii. The disease of sugar arises because of the malfunction of the ________.','iii. د شوګر ناروغي د ________ د خرابۍ له امله پیدا کېږي.')
for t in [('(الف) پتہ','(a) gall bladder','(الف) پت'),('(ب) پھیپھڑے','(b) lungs','(ب) سږي'),('(ج) لبلبہ','(c) pancreas','(ج) لبلبه'),('(د) معدہ','(d) stomach','(د) معده')]: O(s,*t)
Q(s,'iv۔ زیادہ جسمانی ________ ہونے کی وجہ سے دل کو زیادہ کام کرنا پڑتا ہے۔','iv. Because of greater bodily ________ the heart has to work more.','iv. د ډېر بدني ________ له امله زړه ته زیات کار کول پکار دي.')
for t in [('(الف) کولیسٹرول','(a) cholesterol','(الف) کولیسټرول'),('(ب) عضلات','(b) muscles','(ب) عضلات'),('(ج) وزن','(c) weight','(ج) وزن'),('(د) ورزش','(d) exercise','(د) تمرین')]: O(s,*t)
Q(s,'v۔ نمک کے ________ ذرائع فاسٹ فوڈ، ڈبے والی غذا اور سوپ ہیں۔','v. The ________ sources of salt are fast food, canned food and soup.','v. د مالګې ________ سرچینې فاسټ فوډ، په ټینونو کې خواړه او سوپ دي.')
for t in [('(الف) بڑے ذرائع','(a) big','(الف) لوی'),('(ب) پوشیدہ','(b) hidden','(ب) پټې'),('(ج) استعمال شدہ','(c) used','(ج) کارول شوې'),('(د) موجودہ','(d) present','(د) موجودې')]: O(s,*t)
Q(s,'vi۔ نمکین خوراک کا زیادہ استعمال خون کو ________ کرتا ہے۔','vi. Excess use of salty food makes the blood ________.','vi. د مالګينه خوراک ډېر کارول وینه ________ کوي.')
for t in [('(الف) گاڑھا','(a) thick','(الف) غټه'),('(ب) متوازن','(b) balanced','(ب) متوازنه'),('(ج) پتلا','(c) thin','(ج) پتلې'),('(د) تیز','(d) fast','(د) تېزه')]: O(s,*t)
H(s,'2۔ درج ذیل سوالات کے جوابات لکھیں۔','2. Write answers to the following questions.','۲. د لاندې پوښتنو ځوابونه ولیکئ.')
Q(s,'i۔ آسٹیوپوروسس کیا ہے؟ اس کی علامات اور وجوہات بیان کریں۔','i. What is osteoporosis? Describe its symptoms and causes.','i. اسټیوپوروسیس څه دی؟ د هغه نښې او لاملونه بیان کړئ.')
Q(s,'ii۔ دل کے مریض کے لیے کون سی احتیاطی تدابیر اختیار کرنی چاہئیں۔','ii. What precautionary measures should be adopted for a heart patient?','ii. د زړه ناروغ لپاره کوم احتیاطي تدبیرونه اختیارول پکار دي.')
Q(s,'iii۔ شوگر کیا ہے؟ اس سے بچاؤ کے لیے کیا کرنا چاہیے۔','iii. What is sugar (diabetes)? What should be done to prevent it?','iii. شوګر څه دی؟ د هغه له ژغورنې لپاره څه باید وشي.')
F.done()
s['sourceNote']='Printed page 14: exercise questions of Chapter 1 — six multiple-choice items (options الف–د) and three descriptive questions.'+NOTE
s['vocabulary']={}
save(s)
# scan 19 = printed 15 (chapter 2 opener + figure)
s=page(19,'u02','15','Chapter 2: Respiratory System and Exercise — opener and introduction','باب نمبر 2: نظامِ تنفس اور ورزش — آغاز','دویم څپرکی: تنفسي نظام او تمرین — پیل','ch2-open')
F=Flow(s)
add(s,'bn','Chapter 2','باب نمبر 2','دویم څپرکی')
H(s,'نظامِ تنفس اور ورزش','Respiratory System and Exercise','تنفسي نظام او تمرین')
P(s,[('اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter the students will be able to:','د دې څپرکي له لوستلو وروسته به زده‌کوونکي دې وړ شي چې هغوی:'),
('سانس لینے کے عمل اور ورزش کے دوران اس کے فعل کو بیان کر سکیں۔','describe the process of breathing and its function during exercise.','د ساه اخیستو بهیر او د تمرین پر مهال د هغه فعل بیان کړای شي.',dict(listGroup='o2')),
('سانس کے نظام اور دورانِ خون کے نظام کے درمیان تعلق جان سکیں۔','know the relationship between the respiratory system and the circulatory system.','د ساه د نظام او د وینې د دوران د نظام ترمنځ اړیکه وپېژني.',dict(listGroup='o2'))])
H(s,'تعارف:','Introduction:','پېژندنه:')
P(s,[('سانس لینے کے نظام کو نظامِ تنفس کہتے ہیں۔ ہم سانس کے ذریعے آکسیجن سے بھرپور ہوا پھیپھڑوں میں داخل کرتے ہیں اور پھر وہ ہوا جس میں کاربن ڈائی آکسائیڈ کی مقدار زیادہ ہوتی ہے ناک یا منہ کے ذریعے خارج کرتے ہیں۔ جسم کے اندر گیسوں کے تبادلے کو اندرونی تنفس کہتے ہیں۔ پھیپھڑوں میں آکسیجن داخل ہونے کے عمل کو دَرآمد تنفس (Inspiration) کہتے ہیں اور کاربن ڈائی آکسائیڈ باہر نکلنے کے عمل کو برآمد تنفس (Expiration) کہتے ہیں۔','The system of breathing is called the respiratory system. Through breathing we take air rich in oxygen into the lungs and then expel through the nose or mouth the air in which the amount of carbon dioxide is greater. The exchange of gases inside the body is called internal respiration. The process of oxygen entering the lungs is called inspiration (Inspiration) and the process of carbon dioxide going out is called expiration (Expiration).','د ساه اخیستو نظام ته تنفسي نظام وايي. موږ په ساه سره له اکسیجن ډکه هوا سږو ته داخلوو او بیا هغه هوا چې په هغې کې د کاربن ډای اکسایډ اندازه ډېره وي د پوزې یا خولې له لارې وباسو. د بدن دننه د ګازونو تبادلې ته داخلي تنفس وايي. سږو ته د اکسیجن د داخلېدو بهیر ته درآمد تنفس (Inspiration) وايي او د کاربن ډای اکسایډ د وتلو بهیر ته برآمد تنفس (Expiration) وايي.')])
F.fg(0)
F.done()
def lungfig():
    return svg(520,300,'Inspiration and expiration: two outlines of a person with the windpipe and lungs, an arrow pointing into the nose for Inspiration and out of the nose for Expiration',
      torso(130)+torso(390)+T(130,22,'Inspiration',16)+T(390,22,'Expiration',16)+
      '<line x1="40" y1="70" x2="100" y2="82" stroke="#111" stroke-width="3"/><polygon points="100,82 90,74 90,90" fill="#111"/>'+
      '<line x1="420" y1="82" x2="490" y2="70" stroke="#111" stroke-width="3"/><polygon points="490,70 480,66 480,80" fill="#111"/>')
s['figures']=[dict(id='hpe11-s019-fig1',svg=lungfig(),caption='Inspiration and Expiration',captionUrdu='دَرآمدِ تنفس اور برآمدِ تنفس',captionPashto='درآمد تنفس او برآمد تنفس',labels=[lab('Inspiration','دَرآمدِ تنفس','درآمد تنفس'),lab('Expiration','برآمدِ تنفس','برآمد تنفس')],sourceGap=dict(note='Redrawn as a simple coded diagram; the original is a coloured anatomical illustration.'))]
s['sourceNote']='Printed page 15: Chapter 2 opener with two learning outcomes, the introduction to the respiratory system, and the Inspiration/Expiration illustration.'+NOTE
s['vocabulary']={}
save(s)
# scan 20 = printed 16
s=page(20,'u02','16','Organs of the respiratory system; the nose','نظامِ تنفس کے اعضاء؛ ناک','د تنفسي نظام غړي؛ پوزه','resp-1')
F=Flow(s)
P(s,[('نظامِ تنفس میں مندرجہ ذیل اعضاء حصہ لیتے ہیں:','The following organs take part in the respiratory system:','په تنفسي نظام کې لاندې غړي برخه اخلي:'),
('1۔ ناک 2۔ منہ 3۔ حلق 4۔ آلہ صوت 5۔ ہوا کی نالی 6۔ سانس کی نالی 7۔ پھیپھڑے 8۔ ڈایا فرام','1. Nose 2. Mouth 3. Throat 4. Voice box 5. Windpipe 6. Breathing tube 7. Lungs 8. Diaphragm','۱. پوزه ۲. خوله ۳. ستوني ۴. غږ آله ۵. د هوا نلۍ ۶. د ساه نلۍ ۷. سږي ۸. ډایافرام',dict(listGroup='rg'))])
F.fg(0)
H(s,'1۔ ناک (Nose):','1. Nose (Nose):','۱. پوزه (Nose):')
P(s,[('ناک سانس لینے کا ذریعہ ہے۔ ناک کے پہلے حصے میں بال ہوتے ہیں جو فلٹر کا کام کرتے ہیں۔ اس طرح ناک میں آگے ایک لعاب دار جھلی موجود ہوتی ہے جو ناک کو ہر وقت نم رکھتی ہے۔ ناک میں موجود خون کی باریک نالیاں ہوا کے درجہ حرارت کو انسانی جسم کے درجہ حرارت پر لانے کا کام سر انجام دیتی ہیں۔ اس طرح یہ ہوا پھیپھڑوں میں پہنچ کر نقصان نہیں کرتی۔','The nose is the means of breathing. In the first part of the nose there are hairs which act as a filter. In the same way, further on in the nose there is a mucous membrane which keeps the nose moist all the time. The fine blood vessels in the nose bring the temperature of the air to the temperature of the human body. In this way this air does not do harm on reaching the lungs.','پوزه د ساه اخیستو وسیله ده. د پوزې په لومړۍ برخه کې وېښتان وي چې د فلټر کار کوي. همداسې په پوزه کې مخکې یوه لاړه‌دار پرده موجوده وي چې پوزه تل لنده ساتي. په پوزه کې موجودې د وینې نازکې نلۍ د هوا د تودوخې درجه د انسان د بدن په تودوخه رسولو کار سرته رسوي. په دې ډول دا هوا سږو ته رسېدو سره زیان نه کوي.')])
F.done()
def sysfig():
    body=(torso(210,30)+T(210,22,'Respiratory system',13)+
      '<line x1="236" y1="62" x2="330" y2="52" stroke="#444"/>'+T(335,56,'Nose',13,'start')+
      '<line x1="226" y1="72" x2="330" y2="82" stroke="#444"/>'+T(335,86,'Mouth',13,'start')+
      '<line x1="216" y1="110" x2="330" y2="116" stroke="#444"/>'+T(335,120,'Trachea',13,'start')+
      '<line x1="182" y1="170" x2="90" y2="140" stroke="#444"/>'+T(10,136,'Lungs',13,'start')+
      '<line x1="170" y1="228" x2="90" y2="262" stroke="#444"/>'+T(10,270,'Diaphragm',13,'start'))
    return svg(460,290,'Labelled respiratory system: nose, mouth, trachea (windpipe), lungs and diaphragm',body)
s['figures']=[dict(id='hpe11-s020-fig1',svg=sysfig(),caption='The respiratory system (Nose, Mouth, Trachea, Lungs, Diaphragm)',captionUrdu='نظامِ تنفس: ناک، منہ، ہوا کی نالی، پھیپھڑے، ڈایا فرام',captionPashto='تنفسي نظام: پوزه، خوله، د هوا نلۍ، سږي، ډایافرام',labels=[lab('Nose','ناک','پوزه'),lab('Mouth','منہ','خوله'),lab('Trachea','ہوا کی نالی','د هوا نلۍ'),lab('Lungs','پھیپھڑے','سږي'),lab('Diaphragm','ڈایا فرام','ډایافرام')],sourceGap=dict(note='Redrawn as a simple coded diagram; the original is an anatomical outline picture with the same five labels (English and Urdu).'))]
s['sourceNote']='Printed page 16: list of eight organs of the respiratory system, the labelled diagram, and the paragraph on the nose.'+NOTE
s['vocabulary']={}
save(s)
