from enghelp import *
c=cell
U='u02'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
# ---------- scan 27 (printed 18) ----------
s=page(27,U,'18','Glossary (end)','فرہنگ (اختتام)','لغتنامه (پای)','glossary-2')
F=Flow(s)
G=[('scrap (n)','a small piece of something; fragment','کسی چیز کا چھوٹا ٹکڑا؛ ٹکڑا','د یو شي کوچنۍ ټوټه؛ ټوټه','ٹکڑا','ټوټه'),
('seagull (n)','a sea bird with long pointed wings, short legs and white plumage','لمبے نوکیلے پروں، چھوٹی ٹانگوں اور سفید پروں والا سمندری پرندہ','یو سمندري مرغه چې اوږده څوکه‌ییز وزرونه، لنډې پښې او سپین پرونه لري','سمندری چیل','سمندري ټوپک'),
('sheer (adj)','perpendicular, very steep','عمودی، بہت کھڑی ڈھلان','عمودي، ډېر ځوړ','کھڑی ڈھلان','ځوړ'),
('shrilly (adv.)','of sounds/voice – in a sharp and high-pitched manner','آوازوں کے بارے میں – تیز اور اونچی آواز میں','د غږونو په اړه – په تېز او لوړ غږ سره','تیز آواز میں','په تېز غږ'),
('swish (n)','a hissing or rustling sound of movement in air','ہوا میں حرکت کی سنسناہٹ یا سرسراہٹ کی آواز','په هوا کې د حرکت سیسیدا یا سرسراټ غږ','سرسراہٹ','سرسراټ'),
('to ascend (v)','to go or move up (a ladder, hill, slope); to climb up, to mound','اوپر جانا یا حرکت کرنا (سیڑھی، پہاڑی، ڈھلان)؛ چڑھنا، ٹیلہ بنانا','پورته تلل یا حرکت کول (زینه، غونډۍ، ځوړ)؛ پورته کېدل، غونډۍ جوړول','چڑھنا','پورته کېدل'),
('to bank against (v)','to take support of','سہارا لینا','ملاتړ اخیستل','سہارا لینا','ملاتړ اخیستل'),
('to blaze (v)','a strong fire or flame; glare','تیز آگ یا شعلہ؛ چکا چوند','قوي اور یا لمبه؛ روښنایي','دہکنا','سوځېدل'),
('to commence (v)','to begin; to start','شروع کرنا؛ آغاز کرنا','پیلول؛ پیل کول','شروع کرنا','پیلول'),
('to curvet (v)','to leap, move about, in a playful, joyful manner','کھیل اور خوشی کے انداز میں اچھلنا، حرکت کرنا','په لوبه‌ییز او خوشالۍ ډول ټوپونه وهل، حرکت کول','قلابازی کھانا','ټوپونه وهل'),
('to devour (v)','to swallow or eat up greedily or voraciously','لالچ یا بھوک سے نگل جانا یا کھا جانا','په لالچ یا لوږې خوړل یا پورته وړل','ہڑپ کرنا','خوړل'),
('to doze (v)','to sleep lightly or intermittently','ہلکی یا وقفے وقفے سے نیند لینا','سپک یا ټوټه ټوټه خوب کول','اونگھنا','ویده کېدل'),
('to flap (v)','to move (wings or arms) up and down in or as if in flying','(پروں یا بازوؤں کو) اوپر نیچے ہلانا جیسے اڑ رہے ہوں','(وزرونه یا لاسونه) پورته ښکته خوځول لکه الوتنه','پھڑپھڑانا','وزرونه وهل'),
('to gnaw (v)','to bite at or chew upon so as to wear away little by little','کاٹنا یا چبانا تاکہ تھوڑا تھوڑا کر کے گھس جائے','داسې چیچل یا ژول چې لږ لږ وخوري','کترنا','ژول'),
('to hatch (v)','to cause (the young birds) to emerge from the egg','(بچوں پرندوں کو) انڈے سے نکالنا','(ځوان مرغان) له هګۍ څخه را وېستل','انڈوں سے نکالنا','له هګۍ راوتل'),
('to lean out (v)','to extend forward as if to reach out to something','آگے کی طرف جھکنا جیسے کسی چیز تک پہنچنا ہو','مخکې ته مایلېدل لکه د یوه شي تر رسېدو','باہر جھکنا','بهر مایلېدل'),
('to muster up (v)','to summon, gather, assemble or call up','بلانا، جمع کرنا، اکٹھا کرنا یا پکارنا','رابللل، راټولول، یوځای کول یا ندا کول','جمع کرنا','راټولول'),
('to preen (v)','(of birds) to maintain feathers in healthy condition by arranging, cleaning with the bill (beak)','(پرندوں کا) چونچ سے پروں کو ترتیب دے کر اور صاف کر کے صحت مند حالت میں رکھنا','(د مرغانو) په مښوکه د پرونو په ترتیبولو او پاکولو سره په روغ حالت ساتل','پر سنوارنا','پرونه سمول'),
('to root (v)','to burrow, to rummage for something such as food','کریدنا، کھانے جیسی کسی چیز کے لیے ٹٹولنا','کیندل، د خوړو غوندې یو شي لپاره لټول','کریدنا','کیندل'),
('to seize (v)','to take hold of quickly, to grab','جلدی سے پکڑنا، جھپٹنا','ژر نیول، چنګ وهل','پکڑنا','نیول'),
('to skim (v)','to glide smoothly or lightly over a surface','سطح کے اوپر نرمی یا ہلکے سے پھسلنا','پر سطح په نرمۍ یا سپکوالي سره خوځېدل','سطح کو چھوتے ہوئے اڑنا','ښويېدل'),
('to soar (v)','to rise or fly upward in the air','ہوا میں اوپر اٹھنا یا اڑنا','په هوا کې پورته کېدل یا الوتل','بلند ہونا','پورته الوتل'),
('to stretch (v)','to draw out or extend, such as a limb of the body','کھینچنا یا بڑھانا، جیسے جسم کا کوئی عضو','را ایستل یا غځول، لکه د بدن یو غړی','پھیلانا','غځول'),
('To swoop upwards (v)','swift ascent; swift upward movement','تیز چڑھاؤ؛ تیز اوپر کی حرکت','چټک پورته کېدل؛ چټکه پورته حرکت','جھپٹ کر اوپر جانا','چټک پورته کېدل'),
('to taunt (v)','to provoke or deride with mockery, contempt or criticism','طنز، حقارت یا تنقید سے اکسانا یا مذاق اڑانا','په ملنډو، سپکاوي یا انتقاد سره پارول یا ملنډې وهل','طعنہ دینا','ملنډې وهل'),
('to trot (v)','to move at a trot','دلکی چال چلنا','په منډه ګام وهل','دلکی چلنا','څانګه وهل'),
('to upbraid (v)','to scold or rebuke angrily; to take to task','غصے سے ڈانٹنا یا سرزنش کرنا؛ باز پرس کرنا','په غوسه ملامتول یا سپکول؛ پوښتنه کول','ملامت کرنا','ملامتول'),
('whet','to sharpen','تیز کرنا','تېرول','تیز کرنا','تېرول')]
s['tables']=[table('Glossary (continued)','فرہنگ (جاری)','لغتنامه (دوام)',[c('Words','الفاظ','کلمې'),c('Meanings','معنی','معناوې')],[[c(w,ur_w,ps_w),c(m,mu,mp)] for w,m,mu,mp,ur_w,ps_w in G],tab='glossary')]
for w,m,mu,mp,ur_w,ps_w in G: V[w.replace('to ','',1) if w.startswith('to ') else w.split(' (')[0]]=dict(ur=ur_w,ps=ps_w)
build(s,27,['T:0'],[])
s['vocabulary']=V
s['sourceNote']='Printed page 18: the continuation of the Glossary table (scrap … whet), 28 rows. Printed entries kept as printed, including "To swoop upwards (v)" with a capital T and the headword "whet" without a part-of-speech label. The page number 18 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
save(s)
# ---------- scan 28 (printed 19) ----------
s=page(28,U,'19','Reading Comprehension · Writing Suggestions · Oral Communication · Vocabulary and Grammar (start)','مطالعے کا فہم · لکھنے کی تجاویز · زبانی رابطہ · ذخیرۂ الفاظ اور قواعد (آغاز)','د لوست پوهه · د لیکلو وړاندیزونه · شفاهي اړیکه · لغت او ګرامر (پیل)','rc-1')
F=Flow(s)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه',exerciseId='eng11-u02-rc')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u02-rc','exercise')
RQ=[('Why did the young Seagull have to join the company of his family?','نوجوان سمندری چیل کو اپنے خاندان کی صحبت میں کیوں شامل ہونا پڑا؟','ځوان سمندري ټوپک ولې باید د خپلې کورنۍ ملګرتیا ته ورشي؟'),
("Why don't his parents, his brothers and sister give him food?",'اس کے والدین، بھائی اور بہن اسے کھانا کیوں نہیں دیتے؟','د هغه مور پلار، ورونه او خور ولې هغه ته خواړه نه ورکوي؟'),
('What was the attitude of the family towards the young Seagull? Was it agreeable to you or not? Explain','خاندان کا نوجوان سمندری چیل کے ساتھ رویہ کیا تھا؟ کیا یہ آپ کے لیے قابلِ قبول تھا یا نہیں؟ وضاحت کریں','د کورنۍ چلند د ځوان سمندري ټوپک سره څنګه و؟ ایا دا ستاسو لپاره منلو وړ و که نه؟ تشریح کړئ'),
('Describe in your own words the feelings, actions and thoughts of the young Seagull soon after his fall.','نوجوان سمندری چیل کے گرنے کے فوراً بعد اس کے احساسات، اعمال اور خیالات کو اپنے الفاظ میں بیان کریں۔','د ځوان سمندري ټوپک د غورځېدو سمدستي وروسته احساسات، عملونه او فکرونه په خپلو کلمو کې بیان کړئ.'),
("What could be the author's purpose behind writing the story 'His First Flight'?",'کہانی ‘اس کی پہلی پرواز’ لکھنے کے پیچھے مصنف کا مقصد کیا ہو سکتا ہے؟','د کیسې ‘د هغه لومړنۍ الوتنه’ لیکلو شاته د لیکوال موخه څه کېدای شي؟'),
("Compare and contrast the attitude of the family members before and after the flight of the young sea gull in 'His First Flight'.",'‘اس کی پہلی پرواز’ میں نوجوان سمندری چیل کی پرواز سے پہلے اور بعد خاندان کے افراد کے رویے کا موازنہ اور تضاد کریں۔','په ‘د هغه لومړنۍ الوتنه’ کې د ځوان سمندري ټوپک له الوتنې مخکې او وروسته د کورنۍ د غړو چلند پرتله کړئ او توپیر یې ښودل.'),
("Identify the sentence in the first paragraph of ‘His First Flight’ which shows cause and effect.",'‘اس کی پہلی پرواز’ کے پہلے پیراگراف میں وہ جملہ پہچانیں جو علت اور معلول ظاہر کرتا ہے۔','د ‘د هغه لومړنۍ الوتنه’ په لومړي پراګراف کې هغه جمله وپېژنئ چې علت او معلول ښيي.'),
('Read any paragraph from the text to identify the main idea and the sentences that support main idea.','متن سے کوئی بھی پیراگراف پڑھیں تاکہ مرکزی خیال اور مرکزی خیال کی تائید کرنے والے جملے پہچانیں۔','له متن څخه هر پراګراف ولولئ ترڅو اصلي نظر او هغه جملې وپېژنئ چې اصلي نظر ملاتړ کوي.'),
('Read the second paragraph of the text to identify transitional devices and state their functions.','متن کا دوسرا پیراگراف پڑھیں تاکہ انتقالی ذرائع پہچانیں اور ان کے افعال بیان کریں۔','د متن دویم پراګراف ولولئ ترڅو انتقالي وسایل وپېژنئ او د هغو دندې بیان کړئ.')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u02-rc','exercise')
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'wa','A. Write down your own narrative using human characters by including their actions, spoken words, observations, thoughts and feelings.','الف. انسانی کرداروں کو استعمال کرتے ہوئے اپنا بیانیہ لکھیں جس میں ان کے اعمال، بولے گئے الفاظ، مشاہدات، خیالات اور احساسات شامل ہوں۔','a. د انساني کرکترونو په کارولو سره خپله کیسه ولیکئ چې د هغو عملونه، ویل شوې کلمې، کتنې، فکرونه او احساسات په کې شامل وي.',tab='writing')
add(s,'wb','B. Write the summary of the story ‘His First Flight’.','ب. کہانی ‘اس کی پہلی پرواز’ کا خلاصہ لکھیں۔','b. د کیسې ‘د هغه لومړنۍ الوتنه’ لنډیز ولیکئ.',tab='writing')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'ot','Work in pairs, present and explain your point of view to your partner about your early challenges (First Flight) in the grade XI.','جوڑیوں میں کام کریں، گیارہویں جماعت میں اپنی ابتدائی مشکلات (پہلی پرواز) کے بارے میں اپنا نقطۂ نظر اپنے ساتھی کے سامنے پیش اور بیان کریں۔','په جوړو کې کار وکړئ، د یوولسم ټولګي کې د خپلو لومړنیو ننګونو (لومړنۍ الوتنه) په اړه خپل لیدلوری خپل ملګري ته وړاندې او تشریح کړئ.',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'va','A. Use dictionary to identify the pronunciation of the following words with pronunciation key and then use in sentences.','الف. لغت کی مدد سے درج ذیل الفاظ کا تلفظ تلفظ کی کنجی کے ساتھ پہچانیں اور پھر جملوں میں استعمال کریں۔','a. د قاموس په مرسته د لاندې کلمو تلفظ د تلفظ کلیدي سره وپېژنئ او بیا په جملو کې یې وکاروئ.','eng11-u02-vocab','vocabulary')
add(s,'vw','gnaw, monstrous, derisively, plateau, devour','gnaw، monstrous، derisively، plateau، devour','gnaw، monstrous، derisively، plateau، devour',tab='vocabulary')
F.done()
s['sourceNote']='Printed page 19. Pink banners head "Reading Comprehension", "Writing Suggestions", "Oral Communication" and "Vocabulary and Grammar". The page number 19 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded. The Urdu and Pashto of the exercise instructions and questions are added by us.'
s['vocabulary']={}
save(s)
# ---------- scan 29 (printed 20) ----------
s=page(29,U,'20','Vocabulary (cooking words) · Grammar: collective nouns','ذخیرۂ الفاظ (کھانا پکانے کے الفاظ) · قواعد: اجتماعی اسماء','لغت (د پخلي کلمې) · ګرامر: ډله‌ییز اسمونه','vocab-2')
F=Flow(s)
Qn(s,'vb','B. Write the words related to cooking in front of their meanings.','ب. کھانا پکانے سے متعلق الفاظ ان کے معنی کے سامنے لکھیں۔','b. د پخلي پورې اړوند کلمې د هغو د معناوو مخې ته ولیکئ.','eng11-u02-vocab','vocabulary')
add(s,'cw','fry, bake, grate, boil, slice, dice, simmer, chop, sieve, mix, score, roast, peel, knead','fry، bake، grate، boil، slice، dice، simmer، chop، sieve، mix، score، roast، peel، knead','fry، bake، grate، boil، slice، dice، simmer، chop، sieve، mix، score، roast، peel، knead',tab='vocabulary',sourceGap=dict(note='The fourteen words are printed in three rows on pink strips (fry, bake, grate, boil, slice / dice, simmer, chop, sieve, mix / score, roast, peel, knead).'))
CK=[('mark with knife without cutting','چھری سے کاٹے بغیر نشان لگانا','په چاړې پرته له پرېکولو نښه کول'),('take skin off fruit/vegetable','پھل/سبزی سے چھلکا اتارنا','له میوې/سبزي څخه پوټکی لرې کول'),('cut into cubes','مکعبوں میں کاٹنا','په مکعبونو پرېکول'),('shake powder through a fine mesh/net','باریک جالی/جال سے پاؤڈر چھاننا','د پوډر د نرۍ جالۍ/جال له لارې ځغلول'),('massage with hands','ہاتھوں سے مالش کرنا','په لاسونو مالش کول'),('cook in hot water','گرم پانی میں پکانا','په ګرمو اوبو کې پخول'),('turn heat down to heat slowly','آنچ کم کر کے آہستہ آہستہ پکانا','تودوخه ټیټول او ورو ورو پخول'),('use implement to cut food into shreds','اوزار سے کھانا باریک ٹکڑوں میں کاٹنا','د وسیلې په کارولو سره خواړه په ټوټو پرېکول'),('cook using hot oil in a pan','کڑھائی میں گرم تیل سے پکانا','په پن کې په ګرمو غوړو پخول'),('cut very roughly','بہت موٹا موٹا کاٹنا','ډېر خشن پرېکول'),('stir ingredients together','اجزاء کو ملا کر ہلانا','توکي یوځای ګډول'),('cut into thin slices like paper','کاغذ کی طرح پتلی قاشوں میں کاٹنا','د کاغذ غوندې په نرمو ټوټو پرېکول'),('cook in oven without oil','تندور/اوون میں بغیر تیل کے پکانا','په اوون کې پرته له غوړو پخول'),('cook in oven with oil','تندور/اوون میں تیل کے ساتھ پکانا','په اوون کې له غوړو سره پخول')]
CK[6]=('turn heat down slowly','آنچ آہستہ آہستہ کم کرنا','تودوخه ورو ورو ټیټول')
for i,(a,b,d) in enumerate(CK,1): Qn(s,f'c{i}',f'{i}. {a} ____________',f'{i}. {b} ____________',f'{i}. {d} ____________','eng11-u02-vocab','vocabulary')
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
Qn(s,'ga','A. Write the correct collective noun in front of its meaning and then make sentences.','الف. درست اجتماعی اسم اس کے معنی کے سامنے لکھیں اور پھر جملے بنائیں۔','a. سم ډله‌ییز اسم د هغه د معنا مخې ته ولیکئ او بیا جملې جوړې کړئ.','eng11-u02-grammar','grammar')
add(s,'gw','deck, suite, set, shoal, bundle, congregation, fleet, swarm','deck، suite، set، shoal، bundle، congregation، fleet، swarm','deck، suite، set، shoal، bundle، congregation، fleet، swarm',tab='grammar')
GC=[('many insects','بہت سے کیڑے','ډېر حشرات'),('many people','بہت سے لوگ','ډېر خلک'),('many fish','بہت سی مچھلیاں','ډېر کبان'),('many ships','بہت سے جہاز','ډېرې کښتۍ'),('many papers','بہت سے کاغذات','ډېر کاغذونه'),('many rooms','بہت سے کمرے','ډېرې خونې'),('many cards','بہت سے کارڈ','ډېر کارتونه'),('many knives','بہت سی چھریاں','ډېر چاړې')]
for i,(a,b,d) in enumerate(GC,1): Qn(s,f'g{i}',f'{i}. {a} ____________',f'{i}. {b} ____________',f'{i}. {d} ____________','eng11-u02-grammar','grammar')
F.done()
s['sourceNote']='Printed page 20. In exercise B item 7 the printed text reads "turn heat down to heat slowly" (corrected here to "turn heat down slowly" in the shown sentence; printed wording: "turn heat down slowly"). The scan reads "turn heat down slowly". The page number 20 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
s['sourceNote']='Printed page 20. Cooking words are printed on pink strips in three rows; each of the 14 clues is followed by a printed blank line. Exercise A of Grammar has eight collective nouns on a pink strip and eight "many …" clues with blank lines. The page number 20 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 30 (printed 21) ----------
s=page(30,U,'21','Grammar: subject-verb agreement, singular and plural nouns','قواعد: فاعل اور فعل کی مطابقت، واحد اور جمع اسماء','ګرامر: د فاعل او فعل برابرتیا، واحد او جمع اسمونه','grammar-2')
F=Flow(s)
Qn(s,'gb','B. Choose the correct verb. Mind the noun (singular or plural).','ب. درست فعل منتخب کریں۔ اسم (واحد یا جمع) کا خیال رکھیں۔','b. سم فعل وټاکئ. اسم (واحد یا جمع) ته پام وکړئ.','eng11-u02-grammar','grammar')
GB=[('1. Ladies and gentlemen. Here is/ are the news.','1. خواتین و حضرات۔ یہ ہے / ہیں خبریں۔','1. خانمو او ښاغلو. دلته دي/ دي خبرونه.'),('2. Where is/ are my shoes.','2. میرے جوتے کہاں ہے / ہیں۔','2. زما بوټان چېرته دي/ دي.'),('3. Further information is/ are available in the office.','3. مزید معلومات دفتر میں دستیاب ہے / ہیں۔','3. نور معلومات په دفتر کې شته دي/ دي.'),('4. The stairs is/ are over there, Sir.','4. سیڑھیاں وہاں ہے / ہیں، جناب۔','4. زینې هلته دي/ دي، ښاغلیه.'),('5. The furniture in our classroom is/ are uncomfortable.','5. ہمارے کلاس روم کا فرنیچر آرام دہ نہیں ہے / ہیں۔','5. زموږ په ټولګي کې فرنیچر ناآرامه دی/ دي.'),('6. Pakistan is/ are a very nice country.','6. پاکستان ایک بہت اچھا ملک ہے / ہیں۔','6. پاکستان یو ډېر ښه هېواد دی/ دي.'),('7. Your sunglasses is/ are on the table.','7. آپ کا دھوپ کا چشمہ میز پر ہے / ہیں۔','7. ستاسو لمر عینکې پر مېز دي/ دي.'),('8. Homework is/ are boring.','8. ہوم ورک بورنگ ہے / ہیں۔','8. کورنۍ دنده ستړې کوونکې ده/ دي.'),('9. The scissors on the table is/ are mine.','9. میز پر پڑی قینچی میری ہے / ہیں۔','9. پر مېز پرتې قینچي زما دي/ دي.'),('10. Physics is/ are not easy.','10. طبیعیات آسان نہیں ہے / ہیں۔','10. فزیک اسانه نه ده/ دي.')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',a,b,d,'eng11-u02-grammar','grammar')
Qn(s,'gc','C. Use the following words in sentences. Once as a singular nouns and then as a plural nouns.','ج. درج ذیل الفاظ کو جملوں میں استعمال کریں۔ ایک بار واحد اسم کے طور پر اور پھر جمع اسم کے طور پر۔','c. لاندې کلمې په جملو کې وکاروئ. یو ځل د واحد اسم په توګه او بیا د جمع اسم په توګه.','eng11-u02-grammar','grammar')
add(s,'cw','ox, roof, potato, party, deer, chief, photo, series, wife, brother-in-law, life, family, boy, house, city, man, child, sandwich, nurse, shelf','ox، roof، potato، party، deer، chief، photo، series، wife، brother-in-law، life، family، boy، house، city، man، child، sandwich، nurse، shelf','ox، roof، potato، party، deer، chief، photo، series، wife، brother-in-law، life، family، boy، house، city، man، child، sandwich، nurse، shelf',tab='grammar',sourceGap=dict(note='The twenty words are printed in a grid of four rows and five columns on pink strips.'))
Qn(s,'gd','D. Fill in the blanks with the correct form of the given verb in parenthesis. Think about whether the noun is singular or plural.','د. خالی جگہوں کو قوسین میں دیے گئے فعل کی درست شکل سے پُر کریں۔ سوچیں کہ اسم واحد ہے یا جمع۔','d. تشې د قوس په منځ کې ورکړل شوي فعل په سمه بڼه ډکې کړئ. فکر وکړئ چې اسم واحد دی که جمع.','eng11-u02-grammar','grammar')
GD=[('1. This pair of sunglasses ____________ (be) really expensive. I\'m not paying that much!','1. دھوپ کے چشموں کا یہ جوڑا ____________ (be) واقعی مہنگا ہے۔ میں اتنا ادا نہیں کروں گا!','1. دا د لمر عینکو جوړه ____________ (be) واقعاً ګرانه ده. زه دومره نه ورکوم!'),('2. These scissors ____________ (be) blunt. Get me another pair.','2. یہ قینچی ____________ (be) کند ہے۔ مجھے دوسری جوڑی لا دیں۔','2. دا قینچي ____________ (be) نامنځلې ده. ماته بله جوړه راوړئ.'),('3. That jacket you\'re wearing is really nice but those green jeans ____________ (be) horrible.','3. آپ نے جو جیکٹ پہنی ہے وہ واقعی اچھی ہے لیکن وہ سبز جینز ____________ (be) خوفناک ہے۔','3. هغه جاکټ چې تاسو اغوستی ډېر ښه دی خو هغه شنه جینز ____________ (be) ډارونکی دی.'),('4. Physics ____________ (be) the study of the natural world.','4. طبیعیات قدرتی دنیا کا مطالعہ ____________ (be)۔','4. فزیک د طبیعي نړۍ مطالعه ____________ (be).'),('5. A lot of the news we hear on the TV ____________ (be) bad. It\'s so depressing.','5. ٹی وی پر ہم جو خبریں سنتے ہیں ان میں سے بہت سی ____________ (be) بری ہیں۔ یہ بہت افسردہ کن ہے۔','5. ډېر خبرونه چې موږ په تلویزیون کې اورو ____________ (be) بد دي. دا ډېر خپه کوونکي دي.'),('6. The police ____________ (investigate) a break-in at the National Bank last night.','6. پولیس نے گزشتہ رات نیشنل بینک میں چوری کی ____________ (investigate)۔','6. پولیسو تېره شپه په ملي بانک کې د ماتونې ____________ (investigate).'),('7. People ____________ (be) always likely to tell lies to protect themselves.','7. لوگ ہمیشہ اپنے آپ کو بچانے کے لیے جھوٹ بولنے کا امکان ____________ (be) رکھتے ہیں۔','7. خلک تل د ځان د ساتنې لپاره د دروغو ویلو ____________ (be) احتمال لري.'),('8. Think carefully before you spend that amount of money. A thousand pounds ____________ (be) a lot!','8. اتنی رقم خرچ کرنے سے پہلے احتیاط سے سوچیں۔ ایک ہزار پاؤنڈ ____________ (be) بہت ہیں!','8. دومره پیسې لګولو دمخه په احتیاط فکر وکړئ. زر پاونډه ____________ (be) ډېر دي!')]
for i,(a,b,d) in enumerate(GD,1): Qn(s,f'd{i}',a,b,d,'eng11-u02-grammar','grammar')
F.done()
s['sourceNote']='Printed page 21. In exercise B the choice "is/ are" is printed in bold. Exercise C lists twenty words on pink strips. The page number 21 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded.'
s['vocabulary']={}
save(s)
