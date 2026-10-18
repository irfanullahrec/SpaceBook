from enghelp import *
c=cell
U='u14'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
# ---------- scan 139 (printed 130) ----------
s=page(139,U,'130','Glossary · Reading Comprehension','فرہنگ · مطالعے کا فہم','لغتنامه · د لوست پوهه','glossary-rc')
F=Flow(s)
H(s,'gh','Glossary','فرہنگ','لغتنامه',tab='glossary')
G=[('distressing (adj)','something that gives mental pain; painful','وہ چیز جو ذہنی اذیت دے؛ تکلیف دہ','هغه څه چې ذهني درد ورکوي؛ دردناک','تکلیف دہ','دردناک'),
('feebly (adv)','weakly, infirmly (in a low and weak voice)','کمزوری سے، ناتوانی سے (دھیمی اور کمزور آواز میں)','په کمزورۍ، په ناتوانۍ (په ټیټ او کمزوري غږ)','کمزوری سے','په کمزورۍ'),
('garage (n)','auto workshop, where motor vehicles are repaired and serviced','گاڑیوں کی ورکشاپ، جہاں موٹر گاڑیوں کی مرمت اور سروس کی جاتی ہے','د موټرو کارځای، چېرته چې موټرې ترمیمېږي او سروس کېږي','ورکشاپ / گیراج','ګراج'),
('guilt (n)','regret or self-reproach that one is responsible for a wrong/misdeed','پچھتاوا یا خود ملامتی کہ انسان کسی غلط کام کا ذمہ دار ہے','پښېماني یا ځان‌ملامتي چې انسان د یو غلط کار مسؤل دی','جرم کا احساس','ګناه'),
('hardly (adv)','scarcely, barely; almost not','بمشکل، مشکل سے؛ تقریباً نہیں','په ستړیا، په سختۍ؛ نږدې نه','بمشکل','په سختۍ'),
('intently (adv)','with great concentration/attention; attentively,','بڑی توجہ/دھیان کے ساتھ؛ غور سے،','په لوی تمرکز/پاملرنې سره؛ په غور سره،','غور سے','په غور سره'),
('patiently (adv)','with patience; calmly, serenely, quietly','صبر کے ساتھ؛ پرسکون، ٹھنڈے مزاج سے، خاموشی سے','په صبر سره؛ په آرامۍ، په ارامۍ، په چوپتیا','صبر سے','په صبر سره'),
('protests (n)','complaints, objections','شکایات، اعتراضات','شکایتونه، اعتراضونه','احتجاج','اعتراضونه'),
('remote (adj)','located far away; distant','دور واقع؛ دور افتادہ','لرې موقعیت لرونکی؛ لرې','دور افتادہ','لرې'),
('tardiness (n)','unpunctuality, slackness, being late','وقت کی پابندی نہ کرنا، سستی، دیر سے آنا','د وخت پابندي نه کول، سستي، ناوخته راتلل','تاخیر','ځنډ'),
('to apologise (v)','to say sorry; to express or make an apology for some wrong doing','معذرت کرنا؛ کسی غلط کام پر معافی مانگنا یا اظہارِ ندامت کرنا','بخښنه غوښتل؛ د یو غلط کار لپاره بخښنه څرګندول','معذرت کرنا','بخښنه غوښتل'),
('to confess (v)','to acknowledge, admit ones misdeeds, faults, crimes, sins','اپنے غلط کاموں، خامیوں، جرائم، گناہوں کا اعتراف کرنا','خپلې ګناهونه، نیمګړتیاوې، جرمونه، ګناهونه منل','اعتراف کرنا','منل'),
('to contemplate (v)','to think about intently and at length; to consider calmly','غور سے اور دیر تک سوچنا؛ پرسکون انداز میں غور کرنا','په غور او اوږد وخت فکر کول؛ په ارامۍ ګڼل','غور و فکر کرنا','فکر کول'),
('to immerse (v)','to get involved deeply, to engross','گہرائی سے شامل ہونا، محو ہو جانا','په ژوره برخه اخیستل، ډوبېدل','محو ہونا','ډوبېدل'),
('to let down (idiom)','to disappoint someone; to fail to fulfil someone’s expectations','کسی کو مایوس کرنا؛ کسی کی توقعات پوری کرنے میں ناکام ہونا','یو څوک مایوسول؛ د یو چا تمې پوره کولو کې ناکام کېدل','مایوس کرنا','مایوسول'),
('to plead (v)','to appeal earnestly or humbly; to beg, to implore','سنجیدگی یا عاجزی سے اپیل کرنا؛ بھیک مانگنا، التجا کرنا','په جدیت یا عاجزۍ غوښتنه کول؛ هیله کول، زارۍ کول','التجا کرنا','زارۍ کول'),
('to relent (v)','to change one’s mind about some decided course, usu. a harsh one; to become more mild','کسی طے شدہ راستے، عموماً سخت، کے بارے میں ارادہ بدلنا؛ نرم پڑ جانا','د یو ټاکل شوې لارې، معمولاً سختې، په اړه نظر بدلول؛ نرم کېدل','نرم پڑنا','نرم کېدل'),
('utterances (n)','something said; remarks, words, statements','کہی ہوئی بات؛ ریمارکس، الفاظ، بیانات','ویل شوی شی؛ څرګندونې، کلمې، بیانونه','کہی ہوئی باتیں','وینا')]
s['tables']=[table('Glossary','فرہنگ','لغتنامه',[c('Words','الفاظ','کلمې'),c('Meanings','معنی','معناوې')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
F.tb(0)
for w,m,mu,mp,uw,pw in G: V[w.split(' (')[0]]=dict(ur=uw,ps=pw)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u14-rc','exercise')
RQ=[('Write the central idea of ‘A Long Walk Home’.','‘گھر تک ایک طویل پیدل سفر’ کا مرکزی خیال لکھیں۔','د ‘کور ته یو اوږد پیاده سفر’ مرکزي مفکوره ولیکئ.'),
('Analyze the pattern of organizing paragraphs in the text and tell what pattern has been used?','متن میں پیراگرافوں کی ترتیب کے نمونے کا تجزیہ کریں اور بتائیں کہ کون سا نمونہ استعمال کیا گیا ہے؟','په متن کې د پاراګرافونو د ترتیب بڼه تحلیل کړئ او ووایئ چې کومه بڼه کارول شوې؟'),
('What was the most distressing and painful experience for Jason?','جیسن کے لیے سب سے تکلیف دہ اور اذیت ناک تجربہ کون سا تھا؟','د جیسن لپاره تر ټولو دردناک او ستړی کوونکی تجربه کومه وه؟')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u14-rc','exercise')
F.done()
s['sourceNote']='Printed page 130. A pink "Glossary" banner and a table (Words / Meanings) of 19 rows, then a pink "Reading Comprehension" banner with questions 1–3 (the list continues on the next page). The printed meaning of "to confess (v)" reads "ones misdeeds" without an apostrophe; kept as printed. "Not For Sale" is printed at the lower right beside the page number 130 (in a diamond). The Urdu and Pashto columns of the glossary are added by us. Border lines, pink corner flags, the watermark and the phone-number strip are excluded.'
s['vocabulary']=V
save(s)
# ---------- scan 140 (printed 131) ----------
V={}
s=page(140,U,'131','Reading Comprehension (end) · Writing Suggestions · Oral Communication','مطالعے کا فہم (اختتام) · لکھنے کی تجاویز · زبانی رابطہ','د لوست پوهه (پای) · د لیکلو وړاندیزونه · شفاهي اړیکه','rc-writing-oral')
F=Flow(s)
RQ=[('What point of view has been chosen by the writer? Does it suit the writer’s purpose? Demonstrate it with reference to the text of the lesson.','مصنف نے کون سا نقطۂ نظر منتخب کیا ہے؟ کیا یہ مصنف کے مقصد کے مطابق ہے؟ سبق کے متن کے حوالے سے اس کا مظاہرہ کریں۔','لیکوال کوم لیدلوری غوره کړی؟ ایا دا د لیکوال له موخې سره سمون لري؟ د درس د متن په حواله یې وښیئ.'),
('Why did Jason’s father refuse to sit in car and decide to walk the eighteen kilometers? Was his decision justified?','جیسن کے والد نے کار میں بیٹھنے سے انکار کر کے اٹھارہ کلومیٹر پیدل چلنے کا فیصلہ کیوں کیا؟ کیا ان کا فیصلہ درست تھا؟','د جیسن پلار ولې په موټر کې له کېناستو انکار وکړ او اتلس کیلومتره پیاده تلو پرېکړه یې وکړه؟ ایا د هغه پرېکړه سمه وه؟'),
('Why was Jason’s father so angry with himself rather than his son?','جیسن کے والد اپنے بیٹے کے بجائے اپنے آپ پر اتنا ناراض کیوں تھے؟','د جیسن پلار ولې د خپل زوی پر ځای پر ځان دومره غوسه و؟'),
('How do you feel about this personal narrative?','آپ اس ذاتی بیانیے کے بارے میں کیا محسوس کرتے ہیں؟','تاسو د دې شخصي بیانیې په اړه څه احساس لرئ؟'),
('Analyze Jason’s relationship with his father? Was Jason a good son?','جیسن کے اپنے والد کے ساتھ تعلق کا تجزیہ کریں؟ کیا جیسن ایک اچھا بیٹا تھا؟','د جیسن له خپل پلار سره اړیکه تحلیل کړئ؟ ایا جیسن یو ښه زوی و؟'),
('Evaluate the character and personality of Jason’s father? Compare and contrast it with your dad’s personality.','جیسن کے والد کے کردار اور شخصیت کا جائزہ لیں؟ اس کا اپنے والد کی شخصیت سے موازنہ اور تقابل کریں۔','د جیسن د پلار کرکټر او شخصیت وارزوئ؟ د خپل پلار له شخصیت سره یې پرتله او توپیر وکړئ.')]
for i,(a,b,d) in enumerate(RQ,4): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u14-rc','exercise')
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
H(s,'pn','Personal Narrative','ذاتی بیانیہ (Personal Narrative)','شخصي بیانیه (Personal Narrative)',tab='writing')
add(s,'pn1','A personal narrative is a form of writing that shares your personal experiences, including what you did and how you felt about your experiences.','ذاتی بیانیہ تحریر کی ایک شکل ہے جو آپ کے ذاتی تجربات کا اشتراک کرتی ہے، بشمول یہ کہ آپ نے کیا کیا اور اپنے تجربات کے بارے میں آپ نے کیسا محسوس کیا۔','شخصي بیانیه د لیکنې یوه بڼه ده چې ستاسو شخصي تجربې شریکوي، په ګډون د دې چې تاسو څه کړي او د خپلو تجربو په اړه مو څه احساس کړی.',tab='writing')
add(s,'pn2','A good personal narrative has the following features:','ایک اچھے ذاتی بیانیے میں درج ذیل خصوصیات ہوتی ہیں:','یو ښه شخصي بیانیه لاندې ځانګړتیاوې لري:',tab='writing')
for k,a,b,d in [('f1','tells a story from personal experience','ذاتی تجربے سے کوئی کہانی سناتا ہے','د شخصي تجربې یوه کیسه بیانوي'),('f2','uses past tense to express the writer’s feelings','مصنف کے احساسات کے اظہار کے لیے ماضی کا صیغہ استعمال کرتا ہے','د لیکوال د احساساتو د څرګندولو لپاره تېر زمان کاروي'),('f3','employs the first-person as point of view','نقطۂ نظر کے طور پر متکلم (پہلا شخص) استعمال کرتا ہے','د لیدلوري په توګه لومړی شخص کاروي'),('f4','uses narrative techniques of dialogue, description, and pacing','مکالمے، تفصیل اور رفتار کی بیانیہ تکنیکیں استعمال کرتا ہے','د مکالمې، تشریح او سرعت بیانیه تخنیکونه کاروي'),('f5','records events in a sequence that makes sense','واقعات کو ایسی ترتیب میں درج کرتا ہے جو معنی خیز ہو','پېښې په داسې ترتیب ثبتوي چې معنا ولري'),('f6','uses transitional words, phrases, and clauses to make the sequence clear','ترتیب کو واضح کرنے کے لیے انتقالی الفاظ، فقرے اور جملے استعمال کرتا ہے','ترتیب د روښانه کولو لپاره انتقالي کلمې، عبارتونه او جملې کاروي'),('f7','uses concrete words and phrases and sensory details to describe events and people.','واقعات اور لوگوں کو بیان کرنے کے لیے ٹھوس الفاظ، فقرے اور حسی تفصیلات استعمال کرتا ہے۔','د پېښو او خلکو د تشریح لپاره کانکریټ کلمې، عبارتونه او حسي جزئیات کاروي.')]:
    add(s,k,a,b,d,tab='writing',listGroup='features')
add(s,'pn3','Taking clues from “A Long Walk Home” and above mentioned features of personal narrative, write a personal narrative, real or imaginary, and share it with class for their comments and appreciation.','“گھر تک ایک طویل پیدل سفر” اور ذاتی بیانیے کی مذکورہ بالا خصوصیات سے اشارے لیتے ہوئے ایک ذاتی بیانیہ لکھیں، حقیقی یا خیالی، اور کلاس کے ساتھ ان کے تبصروں اور پذیرائی کے لیے شیئر کریں۔','د “کور ته یو اوږد پیاده سفر” او د شخصي بیانیې پورتنیو ځانګړتیاو نه اشارې اخیستو سره یوه شخصي بیانیه ولیکئ، حقیقي یا خیالي، او د ټولګي سره یې د هغوی د تبصرو او ستاینې لپاره شریکه کړئ.',tab='writing')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'ot','Divide the class into groups of six students each: now every student in groups should give oral recount of his/her personal narrative and ask the group members for their response to the narrative.','کلاس کو چھ چھ طلبہ کے گروپوں میں تقسیم کریں: اب گروپوں میں ہر طالب علم اپنے ذاتی بیانیے کا زبانی recount دے اور گروپ کے ارکان سے بیانیے پر ان کا ردِعمل پوچھے۔','ټولګی د شپږو شپږو زده کوونکو په ډلو وويشئ: اوس په ډلو کې هر زده کوونکی د خپل شخصي بیانیې شفاهي recount ورکړي او د ډلې له غړو د بیانیې په اړه د هغوی غبرګون وغواړي.',tab='language')
F.done()
s['sourceNote']='Printed page 131. Questions 4–9 continue from the previous page; pink banners "Writing Suggestions" and "Oral Communication". Question 5 reads "eighteen kilometers" although the story says 18 miles; kept as printed. The left edge of the scan clips the first letters of some lines; read from context. A phone-number strip and the watermark are excluded. Border lines and pink corner flags are excluded. The page number 131 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 141 (printed 132) ----------
s=page(141,U,'132','Vocabulary: phrasal verbs with up/down','ذخیرۂ الفاظ: up/down کے ساتھ phrasal افعال','لغت: د up/down سره phrasal فعلونه','vocab-updown')
F=Flow(s)
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'va','A. Fill in the blanks with either up or down to complete these sentences.','الف. ان جملوں کو مکمل کرنے کے لیے خالی جگہیں up یا down سے پُر کریں۔','الف. دا جملې بشپړولو لپاره تشې په up یا down ډکې کړئ.','eng11-u14-vocab','vocabulary',sourceGap=dict(note='Item 1 is not printed: the numbering on this page runs from 2 to 14 directly after the instruction.'))
VQ=[(2,'I didn’t hear what you said. Speak ______ ______ a little.','میں نے نہیں سنا کہ آپ نے کیا کہا۔ ذرا ______ ______ بولیں۔','ما نه اورېدل چې تاسو څه وویل. ______ ______ لږ خبرې وکړئ.'),
(3,'I don’t trust him at all. Make sure everything is put ______ in writing before signing.','میں اس پر بالکل اعتماد نہیں کرتا۔ دستخط سے پہلے یقینی بنائیں کہ سب کچھ تحریر میں ______ رکھا جائے۔','زه پر هغه هېڅ باور نه لرم. له لاسلیک مخکې ډاډه شئ چې هر څه په لیکلې بڼه ______ ایښودل شي.'),
(4,'When you go to London for the meeting, please remember to bring ______ the whole issue of pay cuts.','جب آپ میٹنگ کے لیے لندن جائیں تو براہِ کرم تنخواہوں میں کٹوتی کا پورا مسئلہ ______ اٹھانا یاد رکھیں۔','کله چې تاسو د غونډې لپاره لندن ته ځئ نو مهرباني وکړئ د معاشونو د کمولو ټوله مسله ______ راوړل یاد وساتئ.'),
(5,'The speed limit is only 50 mph along this road—slow ______ a bit.','اس سڑک پر رفتار کی حد صرف 50 میل فی گھنٹہ ہے—ذرا ______ آہستہ کریں۔','پدې سړک د سرعت حد یوازې ۵۰ میله په ساعت کې دی—لږ ______ ورو کړئ.'),
(6,'Don’t get so excited or you won’t perform at your best. Calm ______!','اتنے پرجوش نہ ہوں ورنہ آپ اپنی بہترین کارکردگی نہیں دکھا سکیں گے۔ ______ ٹھنڈے ہو جائیں!','دومره په ولوله مه کېږئ که نه نو تاسو به خپل غوره کار ونه کړئ. ______ آرام شئ!'),
(7,'I can’t believe you didn’t back me ______ in my argument with Mr. Daud! I thought you were on my side.','مجھے یقین نہیں آتا کہ آپ نے مسٹر داؤد کے ساتھ میری بحث میں میری ______ حمایت نہیں کی! میں سمجھتا تھا کہ آپ میری طرف ہیں۔','زه باور نشم کولای چې تاسو د ښاغلي داود سره زما په بحث کې زما ______ ملاتړ ونه کړ! ما فکر کاوه چې تاسو زما په خوا یاست.'),
(8,'The bridge wasn’t destroyed in the storm. The army blew it ______ before leaving the city.','پل طوفان میں تباہ نہیں ہوا۔ فوج نے شہر چھوڑنے سے پہلے اسے ______ اڑا دیا۔','پله په طوفان کې نه و ړنګ شوی. پوځ له ښار څخه د وتلو مخکې ______ وچاودوه.'),
(9,'Go ______ to that policeman and ask him where we can find the museum.','اس پولیس والے کے پاس ______ جائیں اور اس سے پوچھیں کہ ہمیں عجائب گھر کہاں ملے گا۔','هغه پولیس ته ______ ورشئ او ترې وپوښتئ چې موږ موزیم چېرته موندلی شو.'),
(10,'If we don’t get this contract, we may have to sell ______ and move to another town.','اگر ہمیں یہ معاہدہ نہ ملا تو ہمیں ______ بیچنا اور کسی اور شہر منتقل ہونا پڑ سکتا ہے۔','که موږ دا قرارداد ونه مومو نو ښايي موږ باید ______ وپلورو او بل ښار ته لاړ شو.'),
(11,'If we break ______ these figures into gender, you can see how women have been affected more by this policy.','اگر ہم ان اعداد و شمار کو جنس کے لحاظ سے ______ تقسیم کریں تو آپ دیکھ سکتے ہیں کہ خواتین اس پالیسی سے زیادہ متاثر ہوئی ہیں۔','که موږ دا شمېرې د جنس له مخې ______ وویشو نو تاسو لیدلی شئ چې ښځې پدې پالیسۍ ډېرې اغېزمنې شوې.'),
(12,'They are knocking the old hospital ______ because they say it’s in a dangerous condition.','وہ پرانے ہسپتال کو ______ گرا رہے ہیں کیونکہ ان کا کہنا ہے کہ وہ خطرناک حالت میں ہے۔','هغوی زوړ روغتون ______ ړنګوي ځکه چې وايي چې دا په خطرناکه حالت کې دی.'),
(13,'Three of the oldest trees were blown ______ in the heavy winds last night.','گزشتہ رات تیز ہواؤں میں سب سے پرانے درختوں میں سے تین ______ اکھڑ گئے۔','تېره شپه په سخت بادونو کې له تر ټولو زړو ونو درې ______ وغورځېدې.'),
(14,'There is a lot of government help these days for anyone who wants to set ______ their own business.','ان دنوں ہر اس شخص کے لیے حکومت کی بہت مدد ہے جو اپنا کاروبار ______ شروع کرنا چاہتا ہے۔','پدې ورځو کې د هغه چا لپاره چې غواړي خپل کاروبار ______ پیل کړي دولت ډېره مرسته کوي.')]
for n,a,b,d in VQ: Qn(s,f'v{n}',f'{n}. {a}',f'{n}. {b}',f'{n}. {d}','eng11-u14-vocab','vocabulary')
F.done()
s['sourceNote']='Printed page 132. The pink "Vocabulary and Grammar" banner, "Vocabulary" and Part A (the words "up" and "down" are printed in bold italics in the instruction). Item 1 is not printed; the list starts at 2. Item 2 has two blanks. "Not For Sale" is printed at the lower right beside the page number 132 (in a diamond). Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 142 (printed 133) ----------
s=page(142,U,'133','Vocabulary: weather idioms','ذخیرۂ الفاظ: موسم سے متعلق محاورے','لغت: د هوا اصطلاحات','vocab-idioms')
F=Flow(s)
Qn(s,'vb','B. Consult some authentic sources to find the meaning of the idiom related to weather and then fill in the blanks with correct idiom.','ب. موسم سے متعلق محاورے کا مطلب تلاش کرنے کے لیے کچھ مستند ذرائع سے رجوع کریں اور پھر درست محاورے سے خالی جگہیں پُر کریں۔','ب. د هوا پورې اړوند اصطلاح معنا موندلو لپاره ځینې معتبرې سرچینې وګورئ او بیا په سمې اصطلاح تشې ډکې کړئ.','eng11-u14-vocab','vocabulary')
add(s,'vw','under the weather, it never rains but it pours, rain on someone’s parade, under a cloud, every cloud has a silver lining, hot under the collar, head in the clouds, blow hot and cold, storm in a teacup, make heavy weather of something, get wind of something, any port in a storm','under the weather، it never rains but it pours، rain on someone’s parade، under a cloud، every cloud has a silver lining، hot under the collar، head in the clouds، blow hot and cold، storm in a teacup، make heavy weather of something، get wind of something، any port in a storm','under the weather، it never rains but it pours، rain on someone’s parade، under a cloud، every cloud has a silver lining، hot under the collar، head in the clouds، blow hot and cold، storm in a teacup، make heavy weather of something، get wind of something، any port in a storm',tab='vocabulary',sourceGap=dict(note='The twelve idioms are printed in a two-column box: (left) under the weather, rain on someone’s parade, every cloud has a silver lining, head in the clouds, storm in a teacup, get wind of something; (right) it never rains but it pours, under a cloud, hot under the collar, blow hot and cold, make heavy weather of something, any port in a storm.'))
VQ=[('I only touched his new car and he went crazy. He is over-protective of it and made a real ______.','میں نے صرف اس کی نئی کار کو چھوا اور وہ پاگل ہو گیا۔ وہ اس کی حد سے زیادہ حفاظت کرتا ہے اور اس نے حقیقی ______ بنا دیا۔','ما یوازې د هغه نوې موټر ته لاس ووهه او هغه لېونی شو. هغه ډېر ساتي او رښتیني ______ یې جوړ کړ.'),
('He has been ______ ever since he was caught cheating in the exam. Everyone looks at him strangely and it will take him a long time before he is trusted again.','وہ امتحان میں نقل کرتے پکڑے جانے کے بعد سے ______ ہے۔ ہر کوئی اسے عجیب نظروں سے دیکھتا ہے اور دوبارہ اعتماد حاصل کرنے میں اسے بہت وقت لگے گا۔','هغه له هغه وخته ______ دی چې په ازموینه کې په درغلۍ نیول شوی. هر څوک هغه ته عجیبه ګوري او بیا باور موندلو ته به هغه ډېر وخت ونیسي.'),
('If you are feeling a bit ______ go and have a walk around the block, get some fresh air and try and calm down a bit.','اگر آپ کچھ ______ محسوس کر رہے ہیں تو بلاک کا ایک چکر لگائیں، تازہ ہوا لیں اور تھوڑا پرسکون ہونے کی کوشش کریں۔','که تاسو یو څه ______ احساسوئ نو د بلاک شاوخوا ګرځئ، تازه هوا واخلئ او لږ ارام شئ.'),
('Are you feeling a bit ______ ? You have been looking a bit tired and ill since you arrived in the office this morning.','کیا آپ کچھ ______ محسوس کر رہے ہیں؟ آج صبح دفتر پہنچنے کے بعد سے آپ کچھ تھکے اور بیمار دکھائی دے رہے ہیں۔','ایا تاسو یو څه ______ احساسوئ؟ نن سهار له دفتر ته له رارسېدو راهیسې تاسو یو څه ستړي او ناروغه ښکارئ.'),
('First the bank sent us that rude letter about our loan, then the house got broken into two, then this morning Ali lost his job! ______.','پہلے بینک نے ہمیں ہمارے قرض کے بارے میں وہ بدتمیز خط بھیجا، پھر گھر میں دو بار چوری ہوئی، پھر آج صبح علی کی نوکری چلی گئی! ______۔','لومړی بانک موږ ته د پور په اړه هغه بې‌ادبه لیک راولېږه، بیا کور دوه ځله مات شو، بیا نن سهار علي دنده له لاسه ورکړه! ______.'),
('I can never tell what mood she is going to be in. She always ______ and you have to be really careful around her.','میں کبھی نہیں بتا سکتا کہ وہ کس موڈ میں ہوگی۔ وہ ہمیشہ ______ اور آپ کو اس کے آس پاس واقعی محتاط رہنا پڑتا ہے۔','زه هېڅکله نشم ویلای چې هغه به په کوم مزاج کې وي. هغه تل ______ او تاسو باید د هغې شاوخوا ډېر احتیاط وکړئ.'),
('When I lost my job three years ago, I felt so depressed but it is true that ______ I started my own business and have been happier ever since.','جب تین سال پہلے میری نوکری گئی تو میں بہت افسردہ ہوا لیکن یہ سچ ہے کہ ______ میں نے اپنا کاروبار شروع کیا اور تب سے زیادہ خوش ہوں۔','کله چې درې کاله مخکې ما دنده له لاسه ورکړه نو زه ډېر خپه شوم خو دا رښتیا ده چې ______ ما خپل کاروبار پیل کړ او له هغه وخته ډېر خوشاله یم.'),
('We have hardly any money. You will have to accept any job they offer you because we need money desperately. We have to accept ______.','ہمارے پاس تقریباً کوئی رقم نہیں۔ آپ کو وہ کوئی بھی نوکری قبول کرنی پڑے گی جو وہ پیش کریں کیونکہ ہمیں رقم کی سخت ضرورت ہے۔ ہمیں ______ قبول کرنا ہے۔','موږ نږدې هېڅ پیسې نه لرو. تاسو باید هره دنده ومنئ چې هغوی درکړي ځکه چې موږ ته پیسو سخته اړتیا ده. موږ باید ______ ومنو.')]
for i,(a,b,d) in enumerate(VQ,1): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u14-vocab','vocabulary')
F.done()
s['sourceNote']='Printed page 133. Part B: the instruction, a boxed list of twelve weather idioms in two columns and eight sentences with blanks. The printed text of item 5 reads "got broken into two" (for "twice"); kept as printed. A top-edge strip, a phone-number strip and the watermark are excluded. Border lines and pink corner flags are excluded. The page number 133 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
