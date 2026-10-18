from chemlib import *
c=cell
GL='chem11-glossary-index'
def pg(n,title,ur,ps,sid): return page(n,GL,title,ur,ps,sid)
def tx(x,y,t,size=11,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'

# ---------- 417 ----------
s=pg(417,'Authors (continued)','مصنفین (جاری)','لیکوالان (دوام)','authors-2')
add(s,'a1','Mrs. Syeeda Farheen','محترمہ سیدہ فرحین','ښاغلې سیده فرحین',kind='heading')
add(s,'a1t','She got her M. Phil degree in chemistry from Quaid-e-Azam University Islamabad. She attended seminars and workshops arranged by Khyber Pakhtunkhwa Textbook Board for development of Textbooks.','انہوں نے قائداعظم یونیورسٹی اسلام آباد سے کیمیا میں ایم فل کی ڈگری حاصل کی۔ انہوں نے خیبر پختونخوا ٹیکسٹ بک بورڈ کی طرف سے درسی کتب کی تیاری کے لیے منعقد کیے گئے سیمیناروں اور ورکشاپوں میں شرکت کی۔','هغې د قائداعظم پوهنتون اسلام اباد څخه په کیمیا کې د M. Phil درجه ترلاسه کړه. هغې د خیبر پښتونخوا ټیکسټ بوک بورډ لخوا د درسي کتابونو د جوړولو لپاره جوړ شویو سیمینارونو او ورکشاپونو کې برخه اخیستې.')
add(s,'a2','Muhammad Shoaib Awan','محمد شعیب اعوان','محمد شعیب اعوان',kind='heading')
add(s,'a2t','He did his M. Sc. in chemistry from University of Peshawar. He attended workshops & seminars related to Text books development. He has taught in Cadet College Kohat and currently working as lecturer in Peshawar Public School and College Peshawar.','انہوں نے پشاور یونیورسٹی سے کیمیا میں ایم ایس سی کیا۔ انہوں نے درسی کتب کی تیاری سے متعلق ورکشاپوں اور سیمیناروں میں شرکت کی۔ انہوں نے کیڈٹ کالج کوہاٹ میں پڑھایا ہے اور فی الحال پشاور پبلک اسکول اینڈ کالج پشاور میں لیکچرر کے طور پر کام کر رہے ہیں۔','هغه د پېښور پوهنتون څخه په کیمیا کې M. Sc. کړی. هغه د درسي کتابونو د جوړولو پورې تړلو ورکشاپونو او سیمینارونو کې برخه اخیستې. هغه په کیډټ کالج کوهاټ کې تدریس کړی او اوس مهال د پېښور پبلک سکول او کالج پېښور کې د لیکچرر په توګه کار کوي.')
add(s,'a3','Prof. Aslam Khan','پروفیسر اسلم خان','پروفیسر اسلم خان',kind='heading')
add(s,'a3t','He got his M. Phil in Chemistry from N.C.E in Physical Chemistry University of Peshawar. Currently he is working as Assistant Professor at Govt. College Peshawar.','انہوں نے پشاور یونیورسٹی سے این سی ای میں طبعی کیمیا میں کیمیا کا ایم فل حاصل کیا۔ فی الحال وہ گورنمنٹ کالج پشاور میں اسسٹنٹ پروفیسر کے طور پر کام کر رہے ہیں۔','هغه د پېښور پوهنتون څخه په فزیکي کیمیا کې د N.C.E په کیمیا کې M. Phil ترلاسه کړی. اوس مهال هغه د دولتي کالج پېښور کې د مرستیال پروفیسر په توګه کار کوي.')
s['flow']=[dict(type='paragraphs',ids=[p['id'] for p in s['paras']])]
s['vocabulary']={'authors':dict(ur='مصنفین',ps='لیکوالان')}
s['sourceNote']='Printed folio is not present (the page has no page number). This page continues the Authors list begun on the previous page with three authors. The page also shows a faint see-through ghost of the reverse side (not part of this page) which is ignored. The scan is skewed. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; ghosting from the reverse page ignored.')
save(s)

# ---------- 418 ----------
s=pg(418,'Textbook Feedback Form','درسی کتاب کا تاثراتی فارم','د درسي کتاب د نظر فورمه','feedback-form')
add(s,'org','Khyber Pakhtunkhwa Textbook Board','خیبر پختونخوا ٹیکسٹ بک بورڈ','د خیبر پښتونخوا ټیکسټ بوک بورډ',kind='heading')
add(s,'addr','Phase – V, Hayatabad Peshawar','فیز – V، حیات آباد پشاور','فیز – V، حیات اباد پېښور')
add(s,'phone','Phone: 091-9217714-15 Fax: 091-9217163, Website: www.kptbb.gov.pk','فون: 091-9217714-15 فیکس: 091-9217163، ویب سائٹ: www.kptbb.gov.pk','تلیفون: 091-9217714-15 فکس: 091-9217163، ویب پاڼه: www.kptbb.gov.pk')
add(s,'title','TEXTBOOK FEEDBACK FORM','درسی کتاب کا تاثراتی فارم','د درسي کتاب د نظر فورمه',kind='heading')
add(s,'gr','General Remarks:','عمومی تبصرے:','عمومي څرګندونې:')
add(s,'na','Name & Address:','نام اور پتہ:','نوم او پته:')
add(s,'ce','Contact No. & Email:','رابطہ نمبر اور ای میل:','د اړیکې شمېره او بریښنالیک:')
ST=[('Overall the book is interesting and user friendly.','مجموعی طور پر کتاب دلچسپ اور صارف دوست ہے۔','په ټوله کې کتاب په زړه پورې او کاروونکي دوستانه دی.'),
('The language and content of the book is age / grade appropriate and the content is free of grammatical and punctuation errors.','کتاب کی زبان اور مواد عمر / جماعت کے مطابق ہے اور مواد گرامر اور رموزِ اوقاف کی غلطیوں سے پاک ہے۔','د کتاب ژبه او منځپانګه د عمر / ټولګي سره مناسبه ده او منځپانګه د ګرامر او ټکو د ځای کولو له غلطیو څخه پاکه ده.'),
('Content is supported with examples from real life / culture.','مواد کو حقیقی زندگی / ثقافت کی مثالوں سے سہارا دیا گیا ہے۔','منځپانګه د حقیقي ژوند / کلتور له بېلګو سره ملاتړ شوې ده.'),
('Contents / texts are authentic and updated.','مواد / متون مستند اور تازہ ترین ہیں۔','منځپانګې / متنونه اصلي او تازه شوي دي.'),
('Pictures / diagrams / graphs / illustrations are informative, relevant and clear if not, then identify them.','تصاویر / خاکے / گراف / مثالی تصویریں معلوماتی، متعلقہ اور واضح ہیں، اگر نہیں تو ان کی نشاندہی کریں۔','انځورونه / ډیاګرامونه / ګرافونه / روښانوونکي انځورونه معلوماتي، اړونده او څرګند دي، که نه نو هغه وپېژنئ.'),
('Activities, projects and additional work is suggested for reinforcement of concepts.','تصورات کو مضبوط کرنے کے لیے سرگرمیاں، منصوبے اور اضافی کام تجویز کیے گئے ہیں۔','د مفاهیمو د پیاوړتیا لپاره فعالیتونه، پروژې او اضافي کار وړاندیز شوی دی.'),
('Assessment achievements are thought provoking and comprise cognitive, psychomotor and effective skills.','تشخیصی کامیابیاں فکر انگیز ہیں اور ادراکی، نفسی حرکی اور اثر انگیز مہارتوں پر مشتمل ہیں۔','د ارزونې السته راوړنې فکر راپاروونکې دي او ادراکي، سایکوموټور او اغېزناکې مهارتونه لري.'),
('The textbook is easy to be covered within academic year.','درسی کتاب تعلیمی سال کے اندر آسانی سے مکمل کی جا سکتی ہے۔','درسي کتاب د تعلیمي کال په منځ کې په اسانۍ سره بشپړېدای شي.')]
t1=table('TEXTBOOK FEEDBACK FORM','درسی کتاب کا تاثراتی فارم','د درسي کتاب د نظر فورمه',[c('S#','نمبر شمار','ګڼه'),c('Statement','بیان','بیان'),c('Remarks','تبصرے','څرګندونې')],[[c(f'{i}.'),c(a,b,d),c('')] for i,(a,b,d) in enumerate(ST,1)])
t2=table('Observation / comments','مشاہدات / تبصرے','کتنې / نظرونه',[c('Page No.','صفحہ نمبر','پاڼې شمېره'),c('Observation/comments','مشاہدات/تبصرے','کتنې/نظرونه'),c('Suggested amendment along with rationale','وجوہات کے ساتھ تجویز کردہ ترمیم','د دلیل سره وړاندیز شوې اصلاح')],[[c(''),c(''),c('')] for _ in range(5)])
s['tables']=[t1,t2]
s['flow']=[dict(type='paragraphs',ids=['chem11-p418-org','chem11-p418-addr','chem11-p418-phone','chem11-p418-title']),dict(type='table',index=0),dict(type='table',index=1),dict(type='paragraphs',ids=['chem11-p418-gr','chem11-p418-na','chem11-p418-ce'])]
s['vocabulary']={'feedback':dict(ur='تاثرات',ps='نظر')}
s['sourceNote']='Printed folio is not present. This is the Khyber Pakhtunkhwa Textbook Board feedback form: heading block (emblem not reproduced), statement table with 8 rows (Remarks column left blank), a 5-row blank observation table (Page No. / Observation/comments / Suggested amendment along with rationale), and three blank-line prompts. The printed spellings "effective skills" and the use of "/" are retained. The scan is skewed. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; board emblem not reproduced.')
save(s)

# ---------- 419 ----------
s=pg(419,'Back cover · Code No., Quantity, Price, Printed by','پچھلا سرورق · کوڈ نمبر، تعداد، قیمت، طبع کنندہ','شاته پوښ · کوډ نمبر، شمېر، بیه، چاپ کوونکی','back-cover')
add(s,'anthem','قومی ترانہ','قومی ترانہ','قومي ترانه',kind='heading')
add(s,'code','Code No. PSP/IFS-6-25-2021','کوڈ نمبر PSP/IFS-6-25-2021','کوډ نمبر PSP/IFS-6-25-2021')
add(s,'qty','Quantity 30,000','تعداد 30,000','شمېر 30,000')
add(s,'price','Price 193.00','قیمت 193.00','بیه 193.00')
add(s,'printed','Printed by Idara-e-Farogh-o-Adab Science','طبع کنندہ: ادارۂ فروغِ ادب سائنس (Idara-e-Farogh-o-Adab Science)','چاپ کوونکی: ادارۂ فروغِ ادب سائنس (Idara-e-Farogh-o-Adab Science)')
d=('<rect x="0" y="0" width="360" height="240" fill="#bcd8f0"/><rect x="30" y="70" width="70" height="140" fill="#d8c9a0" stroke="#887"/><rect x="260" y="70" width="70" height="140" fill="#d8c9a0" stroke="#887"/><path d="M100 90 H260 V110 Q180 160 100 110 Z" fill="#d8c9a0" stroke="#887"/>'
 '<path d="M100 210 V120 Q180 170 260 120 V210 Z" fill="#8fb9d8" fill-opacity=".7"/>'+''.join(f'<rect x="{x}" y="62" width="10" height="10" fill="#d8c9a0" stroke="#887"/>' for x in range(30,100,18))+''.join(f'<rect x="{x}" y="62" width="10" height="10" fill="#d8c9a0" stroke="#887"/>' for x in range(260,330,18))
 +'<path d="M180 20 V90" stroke="#555" stroke-width="2"/><rect x="180" y="20" width="36" height="22" fill="#0a6a3a"/><rect x="180" y="20" width="9" height="22" fill="#fff"/><rect x="188" y="62" width="0" height="0"/>'+tx(180,232,'Back cover illustration (schematic)',10,'middle',400,'#555'))
s['figures']=[dict(id='chem11-p419-fig-gate',svg=svg(360,240,'Schematic gate with two towers and an arch with a flag above it, as on the back cover',d),caption='Back cover illustration (schematic)',captionUrdu='پچھلے سرورق کی مثالی تصویر (خاکہ)',captionPashto='د شاتني پوښ انځور (سکیچ)',labels=[],sourceGap=dict(note='Photograph of a fortified gateway on the back cover is redrawn as a coded schematic; architecture details are simplified.'))]
s['flow']=[dict(type='figure',index=0),dict(type='paragraphs',ids=['chem11-p419-anthem','chem11-p419-code','chem11-p419-qty','chem11-p419-price','chem11-p419-printed'])]
s['vocabulary']={}
s['sourceNote']='Back cover of the book (no folio). The back cover shows a photograph of a fortified gateway, the Urdu heading "قومی ترانہ" (National Anthem) with the anthem text printed under it, and the line "Code No. PSP/IFS-6-25-2021 · Quantity 30,000 · Price 193.00 · Printed by Idara-e-Farogh-o-Adab Science". The anthem text itself is not transcribed here (song lyrics are not reproduced); only its heading is recorded. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Anthem text not transcribed (lyrics policy); photograph redrawn as a schematic.')
save(s)
