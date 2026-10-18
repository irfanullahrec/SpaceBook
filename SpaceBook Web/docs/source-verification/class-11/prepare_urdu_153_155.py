from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Couplets are stored as two-line items.'
# scan 153 = printed 146
s=page(153,'n10','146','Syed Muhammad Jafri (poet profile)','سیّد محمد جعفری (شاعر کا تعارف)','سید محمد جعفري (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'سیّد محمد جعفری','Syed Muhammad Jafri','سید محمد جعفري')
P(s,'پیدایش: ۱۹۰۵ء — وفات: ۱۹۷۶ء','Born: 1905 — Died: 1976','زېږېدنه: ۱۹۰۵ز — وفات: ۱۹۷۶ز')
P(s,'سیّد محمد جعفری نے ابتدائی تعلیم گھر پر حاصل کی۔ گورنمنٹ کالج لاہور سے بی ایس سی آنرز (کیمیا) کی سند حاصل کرنے کے بعد علم کی تشنگی بجھانے کے لیے ایم اے فارسی اور ایم اے انگریزی ادبیات کیا۔ ان کے اساتذہ میں ممتاز مزاح نگار پطرس بخاری بھی شامل تھے۔','Syed Muhammad Jafri received his early education at home. After obtaining the BSc Honours (chemistry) degree from Government College Lahore, to quench his thirst for knowledge he did an MA in Persian and an MA in English literature. Among his teachers was also the distinguished humorist Patras Bokhari.','سید محمد جعفري لومړنۍ زده‌کړه په کور ترلاسه کړه. د ګورنمنټ کالج لاهور نه د بي ایس سي آنرز (کیمیا) سند ترلاسه کولو وروسته د علم تندې ماتولو لپاره یې ایم اے فارسي او ایم اے انګلیسي ادبیات وکړل. د هغه په استادانو کې ممتاز طنز لیکوال پطرس بخاري هم شامل و.')
P(s,'سیّد محمد جعفری نے مصوّری اور خطّاطی کی تعلیم و تربیّت بھی حاصل کی۔ کچھ عرصہ محکمۂ تعلیم سے منسلک رہے۔ بعد ازاں وزارتِ اطلاعات و نشریات سے وابستہ ہو گئے اور وہیں سے ریٹائرمنٹ لی۔ سیّد محمد جعفری کا شُمار ایسے طنزیہ اور مزاحیہ شعرا میں ہوتا ہے جنھوں نے ظرافت اور طنز کو ملکی اور سماجی اصلاح کا ہتھیار بنایا۔ اُن کا طنز کاری ضرور ہے مگر اس قدر شگفتہ ہے کہ قاری کو نہ صرف لُطف اندوز کرتا ہے بل کہ غور و فکر اور اصلاح کی دعوت بھی دیتا ہے۔ وہ ملکی ثقافت اور تہذیب و تمدّن کو مغربی اثرات سے پاک دیکھنا چاہتے ہیں۔ یہی وجہ ہے کہ نظم «پُرانا کوٹ» میں اُنھوں نے غلامانہ ذہنیّت کو طنز کا نشانہ بنایا ہے اور ماضی سے عبرت حاصل کرنے کا درس دیا ہے۔','Syed Muhammad Jafri also received education and training in painting and calligraphy. For some time he was attached to the Education Department. Later he joined the Ministry of Information and Broadcasting and retired from there. Syed Muhammad Jafri is counted among those satirical and humorous poets who made wit and satire a weapon for national and social reform. His satire is certainly cutting but so lively that it not only gives the reader pleasure but also invites thought and reform. He wants to see the country’s culture and civilisation free of Western influences. This is why in the poem “Purana Coat” he has made the slavish mentality the target of satire and has given the lesson of taking warning from the past.','سید محمد جعفري د انځورګرۍ او خطاطۍ زده‌کړه او روزنه هم ترلاسه کړه. څه موده د ښوونې ریاست سره تړلی و. وروسته د معلوماتو او خپرونو وزارت سره تړلی شو او له هغه ځایه یې تقاعد واخیست. د سید محمد جعفري شمېر داسې طنزیه او مزاحیه شاعرانو کې کېږي چې ظرافت او طنز یې د ملکي او ټولنیزې اصلاح وسله وګرځاوه. د هغه طنز ضرور تېره دی خو دومره ژوندی دی چې لوستونکي ته نه یوازې خوند ورکوي بلکې غور او فکر او اصلاح ته هم بلنه ورکوي. هغه غواړي ملي کلتور او تهذیب او تمدن له لویدیځو اغېزو پاک وويني. همدا لامل دی چې په «زوړ کوټ» نظم کې یې غلامانه ذهنیت د طنز نښه ګرځولی او له ماضي نه د عبرت اخیستلو درس یې ورکړی دی.')
P(s,'مجموعۂ کلام: شوخیِ تحریر','Poetry collection: Shokhi-e-Tehreer','د شعري ټولګه: شوخي تحریر')
F.done()
s['sourceNote']='Printed page 146 (scan 153): ornamental title “سیّد محمد جعفری”, portrait (not reproduced), birth/death boxes (1905 and 1976), biography and the collection name; the printed page number is not visible in this scan (read by sequence).'+NOTE
s['vocabulary']={}
save(s)
# scan 154 = printed 147
s=page(154,'n10','147','Purana Coat (Syed Muhammad Jafri), part 1','پرانا کوٹ (سیّد محمد جعفری) (حصہ اوّل)','زوړ کوټ (سید محمد جعفري) (لومړۍ برخه)','poem1')
F=Flow(s)
H(s,'پُرانا کوٹ','Purana Coat (The Old Coat)','زوړ کوټ')
for r in [
('خریدا جاڑوں میں نیلام سے پُرانا کوٹ','جو پھٹ کے چل نہ سکے، یہ نہیں ہے ایسا نوٹ','In winter I bought an old coat at an auction;','it is not such a note that, torn, would not circulate.','په ژمي کې مې له نیلام زوړ کوټ واخیست','دا داسې نوټ نه دی چې څیرې شو او ونه چلېږي'),
('بنا ہے کوٹ یہ نیلام کی دکاں کے لیے','«صلائے عام ہے یارانِ نکتہ داں کے لیے»','This coat has been made for the auction shop;','“It is a general invitation to friends who know subtleties.”','دا کوټ د نیلام د دوکان لپاره جوړ شوی دی','«د نکته پوهو ملګرو لپاره عام بلنه ده»'),
('بڑا بزرگ ہے یہ آزمودہ کار ہے یہ','کسی مرے ہوئے گورے کی یادگار ہے یہ','It is a great elder, a tried and experienced one;','it is the memorial of some dead white man.','دا لوی بزرګ دی، آزمویل شوی دی','د کوم مړ شوي ګوري یادګار دی'),
('پرانی وضع کا بے حد عجیب جامہ ہے','پہن چکا اسے خود «واسکوڈی گاما» ہے','It is a most strange garment of an old fashion;','“Vasco da Gama” himself has already worn it.','د زړې بڼې ډېره عجیبه جامه ده','پخپله «واسکوډي ګاما» اغوستې ده'),
('نہ دیکھ کہنیوں پر اس کی خستہ سامانی','پہن چکے ہیں اسے ترک اور ایرانی','Do not look at the tattered state of its elbows;','Turks and Iranians have worn it.','د هغه د ګونځو پر خسته حالت مه ګوره','ترکانو او ایرانیانو اغوستې ده'),
('جگہ جگہ وہ پھرا مثلِ «مارکو پولو»','وہ کوٹ کوٹوں کا لیڈر ہے اس کی جے بولو','It has wandered from place to place like “Marco Polo”;','that coat is the leader of coats — cheer for it!','هغه ځای په ځای لکه «مارکو پولو» ګرځېدلی','هغه کوټ د کوټونو مشر دی د هغه ژوندی دې وي'),
('بڑا بزرگ ہے گو وہ قلیل قیمت ہے','میاں! بزرگوں کا سایہ بڑا غنیمت ہے','It is a great elder, though of low price;','Friend! the shade of elders is a great boon.','لوی بزرګ دی که څه هم ارزانه دی','ورورګلو! د بزرګانو سیوری ډېر غنیمت دی'),
('ہیں اس پہ دھبے جو سرخی کے اور سیاہی کے','نشان ہیں کسی ٹیچر کی بادشاہی کے','The stains on it of red and of ink','are the marks of some teacher’s sovereignty.','پر هغه چې د سرې او تورې رنګ داغونه دي','د کوم ښوونکي د پاچاهۍ نښې دي')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 147 (scan 154): title “پُرانا کوٹ” in an ornamental frame, running head “سیّد محمد جعفری”, and eight couplets of the poem printed in a staggered layout (each couplet’s two lines stored together; the second line of the second couplet is a quoted hemistich in quotation marks); a fold of the page crosses the top. The page ends mid-poem.'+NOTE
s['vocabulary']={}
save(s)
# scan 155 = printed 148
s=page(155,'n10','148','Purana Coat, end','پرانا کوٹ (اختتام)','زوړ کوټ (پای)','poem2')
F=Flow(s)
for r in [
('جگہ جگہ جو یہ کیڑوں کی ضربِ کاری ہے','نئی طرح کی یہ صنعت ہے، دست کاری ہے','The moths’ deep strikes everywhere on it','are a new kind of craft, a handicraft.','هر ځای چې دا د کیړو سخته ضربه ده','دا د نوې ډول صنعت دی، لاسي صنعت دی'),
('جو قدر دان ہیں، وہ جانتے ہیں قیمت کو','کہ آفتاب چرا لے گیا ہے رنگت کو','Those who are connoisseurs know the value,','that the sun has stolen its colour.','څوک چې قدر پوهان دي هغوی بیه پېژني','چې لمر یې رنګ غلا کړی دی'),
('یہ کوٹ کوٹوں کی دنیا کا باوا آدم ہے','اگرچہ ہے وہ نگہ، جو نگاہ سے کم ہے','This coat is the Adam of the world of coats,','although it is a glance which is less than a glance.','دا کوټ د کوټونو د نړۍ بابا آدم دی','که څه هم هغه نظر دی چې له نظر نه کم دی'),
('دہانِ زخم کی مانند ہنس رہے ہیں کاج','وصول کرتے ہیں چینی کی انگڑیوں سے خراج','The buttonholes are laughing like the mouths of wounds;','they extract tribute from Chinese-made … (the word “انگڑیوں” is read as printed).','د ټپ د خولې په څېر ګونځې خاندي','له چیني … خراج اخلي'),
('جگہ جگہ جو یہ دھبّے ہیں اور چکنائی','پہن چکا ہے کبھی اس کو کوئی حلوائی','The stains and greasiness here and there','show that some sweet-maker once wore it.','هر ځای چې دا داغونه او غوړي دي','ښايي کله کوم حلوایي اغوستې وي')]:
    V(s,*r)
V(s,'گذشتہ صدیوں کی تاریخ کا ورق ہے کوٹ','خریدو اس کو کہ عبرت کا اک سبق ہے کوٹ','The coat is a page of the history of past centuries;','buy it, for the coat is a lesson in warning.','کوټ د تېرو پېړیو د تاریخ پاڼه ده','هغه واخلئ چې کوټ د عبرت یو درس دی')
P(s,'(شوخیِ تحریر)','(Shokhi-e-Tehreer)','(شوخي تحریر)')
F.done()
s['sourceNote']='Printed page 148 (scan 155): five couplets and the closing couplet (centred) of the poem, with the source line “(شوخیِ تحریر)”; the lower half of the page is blank. The word “انگڑیوں” (in the fourth couplet) is read as printed (literal sense uncertain).'+NOTE
s['vocabulary']={}
save(s)
