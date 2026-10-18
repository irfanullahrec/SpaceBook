from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,items,g):
    for ur,en,ps in items: add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g)
def Q(s,ur,en,ps,u='p05',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 42 = printed 34
s=page(42,'p05','34','Kuchh Adab ke Baare Mein, end; Exercise (Mashq) questions 1–5','کچھ ادب کے بارے میں کا اختتام؛ مشق: سوال 1 تا 5','د ادب په اړه څه پای؛ تمرین: ۱ تر ۵ پوښتنې','l5')
F=Flow(s)
P(s,'یہ تو فن کار کا کمال ہے کہ وہ بد صورت سے بد صورت چیز میں بھی حُسن کی رعنائی اور دل کشی پیدا کر دے۔ بہر حال ادب ایک ایسا مقام ہے، جہاں فن کار کی صنّاعی بد صورت چیز کو بھی حُسن کے زیور سے آراستہ و پیراستہ کر کے پیش کر سکتی ہے۔ اس اعتبار سے ادب کا مرتبہ بہت بلند ہو جاتا ہے کیوں کہ ہماری سماجی زندگی میں کوئی اور مقام ایسا نہیں آ سکتا، جہاں بد صورت چیز کو بھی حسین بنا کر پیش کیا جا سکے۔ یہ شرف صرف فنونِ لطیفہ اور ادب کو ہی حاصل ہے۔ پس انسانی زندگی میں اس کی اہمیّت سے کسی کو انکار نہیں ہو سکتا۔','It is the artist’s perfection that he creates in even the ugliest thing the grace and charm of beauty. In any case literature is a place where the artist’s craftsmanship can present even an ugly thing adorned and decked with the jewellery of beauty. In this respect the rank of literature becomes very high, because in our social life no other place can come where even an ugly thing can be presented made beautiful. This honour belongs only to the fine arts and literature. So no one can deny its importance in human life.','دا خو د هنرمند کمال دی چې هغه له بدرنګه نه بدرنګه شي کې هم د ښکلا رنګینۍ او زړه کښونه پیدا کړي. په هر حال ادب یو داسې مقام دی چېرته چې د هنرمند صنعتګري بدرنګه شی هم د ښکلا په زیور سینګار او جوړ کړي وړاندې کولای شي. پدې لحاظ د ادب مرتبه ډېره لوړه ګرځي ځکه چې زموږ په ټولنیز ژوند کې بل داسې مقام نشي راتلای چېرته چې بدرنګه شی هم ښکلی جوړ کړي وړاندې کړای شي. دا شرف یوازې ښکلو هنرونو او ادب ته ترلاسه دی. نو په انساني ژوند کې د هغه د اهمیت انکار هیڅوک نشي کولای.')
P(s,'(تنقیدی زاویے)','(Tanqeedi Zaviye)','(تنقیدي زاویې)')
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ متن کی مدد سے خالی جگہ پُر کریں۔','1. Fill in the blanks with the help of the text.','۱. د متن په مرسته تش ځای ډک کړئ.')
for t in [('الف) انسان کے اندر ________ کا احساس سب سے زیادہ قوی ہے۔','(a) Within man the sense of ________ is the strongest.','(الف) د انسان په دننه کې د ________ احساس تر ټولو ډېر قوي دی.'),
('ب) زمانے کی ________ اس کو زیادہ سے زیادہ بناتی سنوارتی ہے۔','(b) The ________ of time makes and adorns it more and more.','(ب) د زمانې ________ هغه ډېر ډېر جوړوي او ښکلی کوي.'),
('ج) ان جذبات و احساسات کو ________ نے خود اپنے تک محدود کیوں نہیں رکھا۔','(c) Why did ________ not keep these emotions and feelings limited to himself?','(ج) دا جذبات او احساسات ________ پخپله خپل ځان پورې ولې محدود نه ساتل.'),
('د) ادب سے انسان کی ________ کی ایک بہت بڑی وجہ یہ بھی ہے۔','(d) This is also a very great reason for man’s ________ in literature.','(د) له ادب سره د انسان د ________ یو ډېر لوی لامل دا هم دی.'),
('ہ) بہر حال یہ ________ کے ابتدائی نقوش تھے۔','(e) In any case these were the early impressions of ________.','(ه) په هر حال دا د ________ لومړني نقشونه وو.'),
('و) ادب کے قدم ترقّی کی ________ پر برابر آگے بڑھتے گئے۔','(f) The steps of literature kept advancing steadily on the ________ of progress.','(و) د ادب ګامونه د ترقۍ ________ پرله پسې مخکې تلل.'),
('ز) احساسِ جمال کا ہونا ہر ________ کے اندر لازمی ہے۔','(g) The existence of a sense of beauty is essential within every ________.','(ز) د جمال احساس لرل د هر ________ په دننه کې لازمي دي.')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-1')
Q(s,'2۔ عبادت بریلوی نے اس مضمون میں کن زاویوں سے ادب کی افادیّت پر روشنی ڈالی ہے؟','2. From which angles has Ibadat Barelvi thrown light on the usefulness of literature in this essay?','۲. عبادت بریلوي پدې مضمون کې د کومو زاویو نه د ادب په ګټه رڼا اچولې ده؟')
Q(s,'3۔ تنقید کی تعریف کریں نیز بتائیے کہ زیرِ نظر مضمون «کچھ ادب کے بارے میں» کہاں تک اس پر پورا اُترتا ہے؟','3. Define criticism (tanqeed) and also state how far the present essay “Kuchh Adab ke Baare Mein” lives up to it.','۳. د تنقید تعریف وکړئ او همدارنګه ووایئ چې دا مضمون «د ادب په اړه څه» تر کومه ځایه پر هغې پوره راځي؟')
Q(s,'4۔ ادب کی اہمیّت پر نوٹ لکھیں۔','4. Write a note on the importance of literature.','۴. د ادب د اهمیت په اړه یادداشت ولیکئ.')
Q(s,'5۔ فعل کی فاعل سے مطابقت کے حوالے سے جملے دُرست کر کے لکھیں۔','5. Correct and write the sentences with regard to the agreement of the verb with the subject.','۵. د فعل د فاعل سره د مطابقت په اړه جملې سمې کړئ او ولیکئ.')
I(s,[('☆ میری کتابیں، قلم اور کاپیاں سب کچھ کھو گئے۔','☆ My books, pen and copybooks all got lost.','☆ زما کتابونه، قلم او کاپۍ ټول ورک شول.')],'ex-5')
F.done()
s['sourceNote']='Printed page 34 (scan 42): the last paragraph of the essay with source line “(تنقیدی زاویے)”, the “Mashq” title, and questions 1–5; the first star-bulleted sentence (for question 5) is at the foot and the remaining sentences continue on the next page.'+NOTE
s['vocabulary']={}
save(s)
# scan 43 = printed 35
s=page(43,'p05','35','Exercise (Mashq): question 5 (sentences), question 6; box on Urdu alphabet; teachers’ instruction','مشق: سوال 5 (جملے) اور سوال 6؛ اُردو حروفِ تہجی؛ ہدایات برائے اساتذہ','تمرین: ۵ پوښتنه (جملې) او ۶ پوښتنه؛ د اردو توري؛ د ښوونکو لارښوونې','ex')
F=Flow(s)
I(s,[('☆ چار کپ، ایک گلاس اور دو پلیٹیں ٹوٹ گئے۔','☆ Four cups, a glass and two plates got broken.','☆ څلور کپونه، یو ګیلاس او دوه پلیټونه مات شول.'),
('☆ شاہ جہاں نے عمارتیں بنوائی۔','☆ Shah Jahan had buildings made.','☆ شاهجهان ودانۍ جوړې کړې.'),
('☆ ہم نے پہاڑ کے پتھروں کو لے پائے۔','☆ We carried the stones of the mountain.','☆ موږ د غره کانړي واخیستل.'),
('☆ فضول خرچی کی وجہ سے اُس کا سرمایہ اور احترام لُٹ گئے۔','☆ Because of extravagance his capital and respect were lost.','☆ د فضول لګښت له امله د هغه سرمایه او درناوی لوټ شو.')],'ex-5')
Q(s,'6۔ سیاق و سباق کے حوالے سے درج ذیل جملوں کی تشریح کریں۔','6. With reference to context, explain the following sentences.','۶. د سیاق او سباق په اړه لاندې جملې تشریح کړئ.')
for t in [('الف) ایک طرف تو تخلیق کی فطری خواہش اور دوسری طرف اپنے آس پاس کے افراد سے دل پر بیتی ہوئی حالت کو ظاہر کر دینے کا خیال، ان دونوں عناصر نے مل کر ادب کو پیدا کیا۔','(a) On one side the natural desire for creation and on the other the idea of revealing to those around one the state that has befallen the heart: these two elements together gave birth to literature.','(الف) یو لوري د تخلیق فطري هیله او بل لوري خپلو شاوخوا افرادو ته د زړه پر تېر شوي حالت څرګندولو خیال، دغو دواړو عناصرو یو ځای ادب پیدا کړ.'),
('ب) اس اعتبار سے ادب کا مرتبہ بہت بلند ہو جاتا ہے، کیوں کہ ہماری سماجی زندگی میں کوئی اور مقام ایسا نہیں آ سکتا، جہاں بد صورت چیز کو بھی حسین بنا کر پیش کیا جا سکے۔','(b) In this respect the rank of literature becomes very high, because in our social life no other place can come where even an ugly thing can be presented made beautiful.','(ب) پدې لحاظ د ادب مرتبه ډېره لوړه ګرځي، ځکه چې زموږ په ټولنیز ژوند کې بل داسې مقام نشي راتلای چېرته چې بدرنګه شی هم ښکلی جوړ کړي وړاندې کړای شي.')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-6')
H(s,'اُردو حروفِ تہجّی','Urdu alphabet (huroof-e-tahajji)','د اردو توري')
P(s,'ا، آ، ب، پ، ت، ٹ، ث، ج، چ، ح، خ، د، ڈ، ذ، ر، ڑ، ز، ژ، س، ش، ص، ض، ط، ظ، ع، غ، ف، ق، ک، گ، ل، م، ن، و، ہ، ی، ے۔ (تعداد = 37)','ا، آ، ب، پ، ت، ٹ، ث، ج، چ، ح، خ، د، ڈ، ذ، ر، ڑ، ز، ژ، س، ش، ص، ض، ط، ظ، ع، غ، ف، ق، ک، گ، ل، م، ن، و، ہ، ی، ے (total = 37 letters)','ا، آ، ب، پ، ت، ٹ، ث، ج، چ، ح، خ، د، ڈ، ذ، ر، ڑ، ز، ژ، س، ش، ص، ض، ط، ظ، ع، غ، ف، ق، ک، گ، ل، م، ن، و، ہ، ی، ے (ټول = ۳۷ توري)',boxed=True)
P(s,'مُرکّب حروف: وہ حروف ہیں جو ہائے دو چشمی (مخلوط) سے مل کر بنتے ہیں۔ یہ کل تعداد میں پندرہ (15) ہیں: بھ، پھ، تھ، ٹھ، جھ، چھ، دھ، ڈھ، رھ، ڑھ، کھ، گھ، لھ، مھ، نھ۔','Compound letters (murakkab huroof): these are letters formed by combining with the two-eyed “he” (mukhloot). Their total number is fifteen (15): بھ، پھ، تھ، ٹھ، جھ، چھ، دھ، ڈھ، رھ، ڑھ، کھ، گھ، لھ، مھ، نھ.','مرکب توري: هغه توري دي چې د دو چشمي هاء (مخلوط) سره یو ځای جوړېږي. دا په ټولیز شمېر کې پنځلس (۱۵) دي: بھ، پھ، تھ، ٹھ، جھ، چھ، دھ، ڈھ، رھ، ڑھ، کھ، گھ، لھ، مھ، نھ.',boxed=True)
P(s,'زبان کے جدید اصولوں کے مطابق الف پہلے اور آ بعد میں آتا ہے کیوں کہ الف ایک جب کہ آ الف + الف = آ شمار کیا جاتا ہے۔ اسی طرح ہائے مخلوط (ھ) اُردو میں کبھی لفظ کے شروع میں نہیں آتا۔ ہمزہ اُردو میں پورا حرف شمار نہیں ہوتا یہ بسا اوقات بطور اضافت آتا ہے۔ مثلاً سرمایۂ اُردو، مجموعۂ کلام، تحفۂ اخلاص۔','According to the modern principles of the language, alif comes first and aa comes later, because alif is counted as one whereas aa is counted as alif + alif = aa. In the same way the mixed “he” (ھ) never comes at the beginning of a word in Urdu. Hamza is not counted as a full letter in Urdu; it often comes as a mark of izafat. For example: sarmaya-e-Urdu, majmua-e-kalam, tohfa-e-ikhlas.','د ژبې د نوو اصولو له مخې الف لومړی او آ وروسته راځي ځکه چې الف یو او آ الف + الف = آ شمېرل کېږي. همداسې مخلوط هاء (ھ) په اردو کې هیڅکله د کلمې په پیل کې نه راځي. همزه په اردو کې بشپړ توری نه شمېرل کېږي دا ډېر وختونه د اضافت په توګه راځي. مثلاً سرمایۂ اردو، مجموعۂ کلام، تحفۂ اخلاص.',boxed=True)
H(s,'ہدایات برائے اساتذہ','Instructions for teachers','د ښوونکو لپاره لارښوونې')
P(s,'طلبہ کو تنقید کی تعریف اور چند مشہور نقادوں کے نام بتائیں۔','Tell the students the definition of criticism and the names of some famous critics.','زده‌کوونکو ته د تنقید تعریف او د څو مشهورو ناقدانو نومونه ووایئ.',boxed=True)
F.done()
s['sourceNote']='Printed page 35 (scan 43): four star-bulleted sentences for question 5 (continued from the previous page), question 6 with two passages, the blue box on the Urdu alphabet (37 letters; 15 compound letters; rules on alif/aa, “ھ” and hamza) and the boxed teachers’ instruction. The sentences for question 5 are printed with deliberate agreement errors for students to correct (e.g. “لے پائے”, “لُٹ گئے”) and are transcribed as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 44 = printed 36
s=page(44,'p06','36','Mushtaq Ahmad Siddiqui (author profile)','مشتاق احمد صدیقی (مصنف کا تعارف)','مشتاق احمد صدیقي (د لیکوال پېژندنه)','author')
F=Flow(s)
H(s,'مشتاق احمد صدیقی','Mushtaq Ahmad Siddiqui','مشتاق احمد صدیقي')
P(s,'پیدایش: 2 اگست 1960ء','Born: 2 August 1960','زېږېدنه: ۲ اګست ۱۹۶۰ز')
P(s,'صوبہ خیبر پختونخوا کے مردم خیز شہر ایبٹ آباد میں پیدا ہوئے۔ پشاور یونی ورسٹی سے ایم اے (اُردو) کا امتحان امتیازی نمبروں سے پاس کیا اور دوسری پوزیشن حاصل کی۔ 1987ء سے صوبے کے مختلف کالجوں میں درس و تدریس میں مصروف رہے اور یکم اگست 2020ء کو گورنمنٹ پوسٹ گریجویٹ کالج منڈیاں ایبٹ آباد سے بحیثیّت صدر شعبۂ اُردو ملازمت سے سُبک دوش ہو چکے ہیں۔ انھوں نے ایم فل اُردو علامہ اقبال اوپن یونی ورسٹی سے مقالہ مرزا عزیز احمد دادا پوری: احوال و آثار، لکھ کر مکمل کیا جب کہ اسی یونی ورسٹی سے پی ایچ ڈی کے ریسرچ اسکالر رہے۔ ان کے پی ایچ ڈی مقالے کا عنوان «ممتاز شیریں کا ذہنی ارتقا» ہے۔','He was born in Abbottabad, the city of the Khyber Pakhtunkhwa province rich in talent. He passed the MA (Urdu) examination from Peshawar University with distinction marks and obtained second position. From 1987 he remained engaged in teaching at various colleges of the province, and on 1 August 2020 retired from service from Government Postgraduate College Mandian, Abbottabad, as head of the Urdu department. He completed his MPhil in Urdu from Allama Iqbal Open University by writing the thesis “Mirza Aziz Ahmad Dadapuri: Life and Works”, while he was a PhD research scholar at the same university. The title of his PhD thesis is “The Mental Evolution of Mumtaz Shireen”.','د خیبر پښتونخوا ولایت په مېرمنو ښار ابټ اباد کې زېږېدلی دی. د پېښور له پوهنتون نه یې د ایم اې (اردو) امتحان په امتیازي نمرو تېر کړ او دویم مقام یې ترلاسه کړ. له ۱۹۸۷ز نه د ولایت په بېلابېلو کالجونو کې په تدریس بوخت و او د ۲۰۲۰ز د اګست په لومړۍ نېټه د حکومتي پوسټ ګریجویټ کالج منډیاں ابټ اباد نه د اردو څانګې د مشر په توګه له دندې نه سبکدوش شو. هغه ایم فل اردو د علامه اقبال آزاد پوهنتون نه د «مرزا عزیز احمد دادا پوري: احوال او آثار» مقاله لیکلو سره بشپړ کړ پداسې حال کې چې د همدې پوهنتون د پي اېچ ډي څېړونکی و. د هغه د پي اېچ ډي د مقالې سرلیک «ممتاز شیرین کا ذهني ارتقا» دی.')
P(s,'ان کا طبعی رجحان تحقیق اور تنقید نگاری کی طرف رہا۔ ان کی نگارشات مختلف ادبی رسائل و جرائد اور کالج کے ادبی مجلّوں میں چھپتی رہیں، ان کے اہم مطبوعہ مضامین درج ذیل ہیں۔','His natural inclination was towards research and critical writing. His writings kept being published in various literary magazines and journals and college literary magazines; his important published articles are as follows.','د هغه طبعي رجحان د څېړنې او تنقید لیکنې لور ته و. د هغه لیکنې په بېلابېلو ادبي مجلو او ورځپاڼو او د کالج په ادبي مجلو کې چاپېدلې، د هغه مهم چاپ شوي مضامین دا دي:')
I(s,[('پیروڈی اور اُردو ادب','Parody and Urdu literature','پیروډي او اردو ادب'),
('تحقیق و تنقید کا رشتہ','The relationship of research and criticism','د څېړنې او تنقید اړیکه'),
('بنیاں انگارے! ایک جائزہ','Baniyan Angare! A review','بنیاں انګارې! یوه جایزه'),
('تصوّرِ خدا اور مفہومِ دُعا','The concept of God and the meaning of supplication','د خدای تصور او د دعا مفهوم'),
('صحرائیّت و بدویّت اقبالؒ کی نظر میں','Desert-dwelling and Bedouinism in the view of Iqbal','صحرايي والی او بدویت د اقبال په نظر کې'),
('ایہام گوئی کی تحریک کے اسباب','Causes of the movement of iham-goi (double entendre)','د ایهام ګویۍ د غورځنګ لاملونه')],'author-articles')
F.done()
s['sourceNote']='Printed page 36 (scan 44): ornamental title “مشتاق احمد صدیقی”, portrait (not reproduced), the birth box (no death box: the author is living), biography, and a blue box listing six articles in a two-column grid.'+NOTE
s['vocabulary']={}
save(s)
