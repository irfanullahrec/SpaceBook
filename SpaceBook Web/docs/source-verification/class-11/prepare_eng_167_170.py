from enghelp import *
c=cell
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
GEX='eng11-u17-grammar'
# ---------- scan 167 (printed 158) ----------
s=page(167,'u17','158','Grammar: position of adverbs (end) · Teacher\'s Guideline','قواعد: قیود کی جگہ (اختتام) · استاد کی رہنمائی','ګرامر: د قیدونو ځای (پای) · د ښوونکي لارښوونه','adverb-position-end')
F=Flow(s)
GQ=[('He got dressed. (in a hurry)','اس نے کپڑے پہنے۔ (in a hurry)','هغه جامې واغوستې. (in a hurry)'),
('She realized her mistake. (at once)','اسے اپنی غلطی کا احساس ہوا۔ (at once)','هغې خپله غلطي پوه شوه. (at once)'),
('We are invited to parties at the weekends. (often)','ہمیں ہفتے کے آخر میں پارٹیوں میں مدعو کیا جاتا ہے۔ (often)','موږ د اونۍ په پای کې محفلونو ته بلل کېږو. (often)'),
('She has done everything – she has been a soldier. (even)','اس نے سب کچھ کیا ہے – وہ سپاہی بھی رہی ہے۔ (even)','هغې هر څه کړي دي – هغه سرتېرې هم وه. (even)'),
('I have finished painting the house. (almost)','میں نے گھر پر رنگ کرنا تقریباً ختم کر لیا ہے۔ (almost)','ما د کور رنګول نږدې بشپړ کړي دي. (almost)'),
('Could you switch the light? (off)','کیا آپ بتی بند کر دیں گے؟ (off)','ایا تاسو څراغ بند کولای شئ؟ (off)'),
('We go to our native place in summer. (usually)','ہم گرمیوں میں اپنے آبائی علاقے جاتے ہیں۔ (usually)','موږ په اوړي کې خپل اصلي ځای ته ځو. (usually)'),
('Your sewing machine needs some oil. (just)','آپ کی سلائی مشین کو کچھ تیل چاہیے۔ (just)','ستاسو د ګنډلو ماشین ته لږ غوړي په کار دي. (just)'),
('It will rain this evening. (probably)','آج شام بارش ہوگی۔ (probably)','نن ماښام به باران وشي. (probably)')]
for i,(a,b,d) in enumerate(GQ,4): Qn(s,f'g{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of varying positions of adverbs.','طلبہ کو قیود (adverbs) کی مختلف جگہوں کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د قیدونو (adverbs) د بېلابېلو ځایونو کارول تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 158. Items 4–12 of the adverb-position exercise (the page begins with "4. He got dressed. (in a hurry)"), then a large blank space and the pink "Teacher\'s Guideline" banner. Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 158 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 168 (printed 159) ----------
s=page(168,'u18','159','Unit 18: A Dream Within a Dream · Learning outcomes','یونٹ 18: خواب کے اندر خواب · سیکھنے کے نتائج','واحد 18: په خوب کې خوب · د زده کړې پایلې','unit18-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 18','یونٹ 18','واحد 18')
H(s,'title','A Dream Within a Dream','خواب کے اندر خواب','په خوب کې خوب')
add(s,'au','Edgar Allan Poe','ایڈگر ایلن پو','اېډګر ایلن پو')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('use critical thinking to respond orally and in writing to the text (post-reading) to:','تنقیدی سوچ استعمال کر کے متن (پڑھنے کے بعد) کا زبانی اور تحریری جواب دیں تاکہ:','انتقادي فکر وکاروي ترڅو متن ته (له لوستلو وروسته) په شفاهي او لیکلي ډول ځواب ورکړي ترڅو:'),
('• give a personal opinion and justify stance related to viewpoints/ideas and issues in the text read.','• پڑھے گئے متن میں موجود نقطہ ہائے نظر/خیالات اور مسائل سے متعلق ذاتی رائے دیں اور اپنے موقف کا جواز پیش کریں۔','• په لوستل شوي متن کې د لیدلورو/نظرونو او مسایلو په اړه شخصي نظر ورکړي او خپل دریځ توجیه کړي.'),
('• relate what is read to his or her own feelings and experiences.','• جو کچھ پڑھا گیا اسے اپنے احساسات اور تجربات سے جوڑیں۔','• هغه څه چې لوستل شوي د خپلو احساساتو او تجربو سره وتړي.'),
('• scan to answer short questions.','• مختصر سوالات کے جواب دینے کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي.'),
('read a given poem and give orally and in writing:','دی گئی نظم پڑھیں اور زبانی اور تحریری طور پر دیں:','ورکړل شوې نظم ولولي او په شفاهي او لیکلي ډول ورکړي:'),
('• theme and its development.','• موضوع اور اس کی نشوونما۔','• موضوع او د هغې پرمختګ.'),
('• personal response with justification.','• جواز کے ساتھ ذاتی ردِعمل۔','• د توجیه سره شخصي غبرګون.'),
('• recognize literary techniques such as personification and alliteration.','• ادبی تکنیکوں مثلاً تشخیص (جان ڈالنا) اور تکرارِ حروف کو پہچانیں۔','• ادبي تخنیکونه لکه شخصیت‌بخښنه او د توري تکرار وپېژني.'),
('analyze how a writer/ poet uses language to:','تجزیہ کریں کہ ایک مصنف/شاعر زبان کو کیسے استعمال کرتا ہے تاکہ:','تحلیل کړي چې یو لیکوال/شاعر ژبه څنګه کاروي ترڅو:'),
('• appeal to the senses through use of figurative language including similes, metaphors and imagery','• تشبیہات، استعارات اور پیکر تراشی سمیت علامتی زبان کے ذریعے حواس سے اپیل کرے','• د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې په کارولو سره حواسو ته اپیل وکړي'),
('• set tone.','• لہجہ قائم کرے۔','• لهجه جوړه کړي.'),
('develop focus for own writing by identifying audience and purpose','سامعین اور مقصد کی شناخت کر کے اپنی تحریر کے لیے مرکزِ توجہ تیار کریں','د لیدونکو او موخې په پېژندلو سره د خپلې لیکنې لپاره تمرکز وده کړي'),
('demonstrate heighten awareness of conventions and dynamic of group discussion and interaction to present and explain one point of view clearly, support or modify one’s opinion with reason and agree or disagree politely at appropriate time.','گروہی بحث اور تعامل کے اصولوں اور حرکیات سے بلند آگاہی کا مظاہرہ کریں تاکہ اپنے نقطۂ نظر کو واضح طور پر پیش اور بیان کریں، دلائل کے ساتھ اپنی رائے کی تائید کریں یا اسے تبدیل کریں اور مناسب وقت پر شائستگی سے اتفاق یا اختلاف کریں۔','د ډله‌ییزې بحث او اړیکې د دودونو او حرکیاتو لوړ پوهاوی وښيي ترڅو خپل لیدلوری په روښانه ډول وړاندې او تشریح کړي، خپل نظر په دلایلو سره ملاتړ یا بدل کړي او په مناسب وخت په ادب سره موافقه یا مخالفت وکړي.'),
('use appropriate vocabulary and correct spelling in their own writing.','اپنی تحریر میں موزوں ذخیرۂ الفاظ اور درست املا استعمال کریں۔','په خپله لیکنه کې مناسب لغت او سمه املا وکاروي.'),
('Identify and use adverbial phrases.','قیدی فقروں (adverbial phrases) کی شناخت کریں اور استعمال کریں۔','قیدي عبارتونه (adverbial phrases) وپېژني او وکاروي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 159: Unit 18 opening page with the unit number, the title banner "A Dream Within a Dream", the poet tag "Edgar Allan Poe" and the learning outcomes with nested bullets (printed bullets "•" shown in the text of sub-items). The printed text reads "heighten awareness" and "dynamic of group discussion"; kept as printed. Coloured page-edge markings at the right margin are ignored. Border lines, pink corner flags and the watermark are excluded. The page number 159 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 169 (printed 160) ----------
s=page(169,'u18','160','A Dream Within a Dream (poem)','خواب کے اندر خواب (نظم)','په خوب کې خوب (نظم)','poem')
F=Flow(s)
H(s,'t','A Dream Within a Dream','خواب کے اندر خواب','په خوب کې خوب')
add(s,'s1','Take this kiss upon the brow!\nAnd, in parting from you now,\nThus much let me avow —\nYou are not wrong, who deem\nThat my days have been a dream;\nYet if hope has flown away\nIn a night, or in a day,\nIn a vision, or in none,\nIs it therefore the less gone?\nAll that we see or seem\nIs but a dream within a dream.','یہ بوسہ پیشانی پر لے لو!\nاور، اب تم سے بچھڑتے ہوئے،\nاتنا مجھے اقرار کرنے دو —\nتم غلط نہیں ہو، جو سمجھتے ہو\nکہ میرے دن ایک خواب تھے؛\nلیکن اگر امید اڑ گئی\nکسی رات میں، یا کسی دن میں،\nکسی نظارے میں، یا کسی میں نہیں،\nتو کیا وہ اس لیے کم گئی؟\nجو کچھ ہم دیکھتے ہیں یا نظر آتے ہیں\nوہ بس خواب کے اندر خواب ہے۔','دا ښکل پر تندي واخله!\nاو، اوس له تا نه د جلا کېدو پر مهال،\nدومره ما ته د اعتراف اجازه راکړه —\nته غلط نه یې، چې ګڼې\nچې زما ورځې یو خوب وې؛\nخو که هیله الوتلې وي\nپه یوه شپه کې، یا په یوه ورځ کې،\nپه یوه لیدلو کې، یا په هېڅ کې،\nنو ایا ځکه لږ تللې ده؟\nهر څه چې موږ وینو یا ښکارو\nیوازې په خوب کې یو خوب دی.',listType='poem')
add(s,'s2','I stand amid the roar\nOf a surf-tormented shore,\nAnd I hold within my hand\nGrains of the golden sand —\nHow few! yet how they creep\nThrough my fingers to the deep,\nWhile I weep — while I weep!\nO God! Can I not grasp\nThem with a tighter clasp?\nO God! can I not save\nOne from the pitiless wave?\nIs all that we see or seem\nBut a dream within a dream?','میں شور کے بیچ کھڑا ہوں\nموجوں سے ستائے ہوئے ساحل کے،\nاور میں اپنے ہاتھ میں تھامے ہوں\nسنہری ریت کے ذرے —\nکتنے کم! پھر بھی کیسے رینگتے ہیں\nمیری انگلیوں سے گہرائی کی طرف،\nجبکہ میں روتا ہوں — جبکہ میں روتا ہوں!\nاے خدا! کیا میں انہیں\nزیادہ مضبوط گرفت سے نہیں پکڑ سکتا؟\nاے خدا! کیا میں ایک کو بھی\nبے رحم لہر سے نہیں بچا سکتا؟\nکیا جو کچھ ہم دیکھتے ہیں یا نظر آتے ہیں\nبس خواب کے اندر خواب ہے؟','زه د غړمبا په منځ کې ولاړ یم\nد څپو پر ځورول شوي ساحل،\nاو زه په خپل لاس کې نیولې یم\nد زرینو شګو دانې —\nڅومره لږې! خو څنګه خوځي\nزما د ګوتو له لارې ژورې ته،\nپداسې حال کې چې زه ژاړم — پداسې حال کې چې زه ژاړم!\nای خدایه! ایا زه نشم کولای\nهغوی په ډېرې کلکې نیونې ونیسم؟\nای خدایه! ایا زه نشم کولای\nیوه هم له بې‌رحمه څپې وژغورم؟\nایا هر څه چې موږ وینو یا ښکارو\nیوازې په خوب کې یو خوب دی؟',listType='poem')
add(s,'by','Edgar Allan Poe','ایڈگر ایلن پو','اېډګر ایلن پو')
add(s,'n','A pink-and-purple graphic of an hourglass with falling sand is printed at the right of the poem; it is a picture and is not reproduced.','نظم کے دائیں طرف گرتی ریت والی ریت گھڑی کا گلابی اور جامنی گرافک ہے؛ یہ تصویر نقل نہیں کی گئی۔','د نظم په ښي لوري د پرېوتونکو شګو لرونکې د شګو ساعت ګلابي او ارغواني ګرافیک دی؛ دا انځور نه دی رانقل شوی.')
F.done()
s['sourceNote']='Printed page 160: the poem "A Dream Within a Dream" by Edgar Allan Poe (1849; public domain, printed in full) in two stanzas, with the author line at the foot. A graphic of an hourglass runs down the right side and partly covers the right ends of two lines ("Through my fingers to the deep," is clipped as "Through my finge… the deep," and "While I weep — while I weep!" as "wh… I weep!"); the missing words are read from the poem\'s known text. A strip of the next page and the phone-number strip are excluded. Border lines, a pink corner flag and the watermark are excluded. The page number 160 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 170 (printed 161) ----------
s=page(170,'u18','161','About the poet · Glossary · Reading Comprehension','شاعر کے بارے میں · فرہنگ · مطالعے کا فہم','د شاعر په اړه · لغتنامه · د لوست پوهه','poet-glossary-rc')
F=Flow(s)
H(s,'ah','About the poet:','شاعر کے بارے میں:','د شاعر په اړه:')
add(s,'ab','Edgar Allan Poe (January 19, 1809 – October 7, 1849) was an American writer, editor, and literary critic. Poe is best known for his poetry and short stories. He is widely regarded as a central figure of Romanticism in the United States and of American literature as a whole. Some of his famous poems are : ’Al Aaraaf’, ‘Annabel Lee’ , ‘The Bells’, ‘The City in the Sea’, ‘The Conqueror Worm’, ‘A Dream Within a Dream”, ‘Eldorado’, ‘Eulalie’, ‘The Haunted Palace’, ‘To Helen’, ‘Lenore’, etc.','ایڈگر ایلن پو (19 جنوری 1809 – 7 اکتوبر 1849) ایک امریکی ادیب، مدیر اور ادبی نقاد تھے۔ پو اپنی شاعری اور مختصر کہانیوں کے لیے بہترین جانے جاتے ہیں۔ انہیں وسیع پیمانے پر ریاستہائے متحدہ میں رومانویت کی ایک مرکزی شخصیت اور مجموعی طور پر امریکی ادب کی شخصیت سمجھا جاتا ہے۔ ان کی کچھ مشہور نظمیں یہ ہیں: ‘ال عراف’، ‘اینابیل لی’، ‘دی بیلز’، ‘دی سٹی ان دی سی’، ‘دی کنکرر ورم’، ‘اے ڈریم وِد اِن اے ڈریم’، ‘ایلڈوراڈو’، ‘یولالی’، ‘دی ہانٹڈ پیلس’، ‘ٹو ہیلن’، ‘لینور’ وغیرہ۔','اېډګر ایلن پو (۱۹ جنوري ۱۸۰۹ – ۷ اکتوبر ۱۸۴۹) یو امریکايي لیکوال، مدیر او ادبي انتقاد کوونکی و. پو د خپلې شاعرۍ او لنډو کیسو لپاره ښه پېژندل کېږي. هغه په پراخه کچه په متحده ایالاتو کې د رومانتیزم یو مرکزي شخصیت او په ټوله کې د امریکايي ادب یو شخصیت ګڼل کېږي. د هغه ځینې مشهورې نظمونه دا دي: ‘ال عراف’، ‘اینابیل لي’، ‘ګنټې’، ‘په سمندر کې ښار’، ‘فاتح چینجی’، ‘په خوب کې خوب’، ‘الدوراډو’، ‘یولالي’، ‘ځورېدلې ماڼۍ’، ‘هیلن ته’، ‘لینور’ او نور.')
H(s,'gh','Glossary','فرہنگ','لغتنامه',tab='glossary')
G=[('avow','assert or confess openly','کھل کر دعویٰ کرنا یا اعتراف کرنا','په څرګنده ادعا کول یا ومنل','اقرار کرنا','اعتراف کول'),
('clasp','grasp (something) tightly with one’s hand.','(کسی چیز کو) اپنے ہاتھ سے مضبوطی سے پکڑنا۔','(یو شی) په خپل لاس کلکه نیول.','گرفت','کلکه نیول'),
('surf-tormented','being bothered, harassed, or pounded by the surf of the ocean.','سمندر کی موجوں سے ستایا جانا، تنگ کیا جانا یا ٹکرایا جانا۔','د سمندر د څپو لخوا ځورول کېدل، ځورول کېدل یا ټکر کېدل.','موجوں سے ستایا ہوا','د څپو ځورول شوی')]
s['tables']=[table('Glossary','فرہنگ','لغتنامه',[c('Word','لفظ','کلمه'),c('Meaning','معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
F.tb(0)
for w,m,mu,mp,uw,pw in G: V[w]=dict(ur=uw,ps=pw)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u18-rc','exercise')
RQ=[('What idea does the parting of beloved bring into Poe’s mind?','محبوب سے جدائی پو کے ذہن میں کون سا خیال لاتی ہے؟','د محبوب جلا کېدل د پو په ذهن کې کومه مفکوره راولي؟'),
('What is the theme of the poem? And how is it developed in the poem ‘A Dream Within a Dream’?','نظم کا موضوع کیا ہے؟ اور نظم ‘خواب کے اندر خواب’ میں اسے کیسے آگے بڑھایا گیا ہے؟','د نظم موضوع څه دی؟ او په نظم ‘په خوب کې خوب’ کې دا څنګه پرمختللی دی؟'),
('What metaphor does the poet use for his inability to hold reality and fleeting times? Explain.','شاعر حقیقت اور گزرتے وقت کو تھامنے میں اپنی ناکامی کے لیے کون سا استعارہ استعمال کرتا ہے؟ وضاحت کریں۔','شاعر د حقیقت او تېرېدونکي وخت د نیولو کې د خپلې نا توانۍ لپاره کوم استعاره کاروي؟ تشریح کړئ.'),
('What is the tone of the poem ‘A Dream Within a Dream’? Illustrate it with references from the poem.','نظم ‘خواب کے اندر خواب’ کا لہجہ کیا ہے؟ نظم کے حوالوں سے اس کی وضاحت کریں۔','د نظم ‘په خوب کې خوب’ لهجه څه ده؟ د نظم له حوالو سره یې روښانه کړئ.'),
('What type of imagery is used in the poem ‘A Dream Within a Dream’? What feelings does it evoke in you? Analyze.','نظم ‘خواب کے اندر خواب’ میں کس قسم کی پیکر تراشی استعمال ہوئی ہے؟ یہ آپ میں کون سے جذبات ابھارتی ہے؟ تجزیہ کریں۔','په نظم ‘په خوب کې خوب’ کې کوم ډول انځورګري کارول شوې؟ دا ستاسو کې کوم احساسات راپاروي؟ تحلیل کړئ.'),
('Pick out the examples of alliteration from the poem ‘A Dream within a Dream’ also describe its rhyme scheme. How does these poetic devices contribute to the music of the poem?','نظم ‘خواب کے اندر خواب’ سے تکرارِ حروف (alliteration) کی مثالیں چنیں اور اس کی قافیہ بندی بھی بیان کریں۔ یہ شعری حربے نظم کی موسیقیت میں کیسے حصہ ڈالتے ہیں؟','له نظم ‘په خوب کې خوب’ څخه د alliteration بېلګې وټاکئ او د قافیې ترتیب هم بیان کړئ. دا شعري وسایل د نظم په موسیقیتوب کې څنګه ونډه اخلي؟'),
('Why does the poet call life a dream within a dream?','شاعر زندگی کو خواب کے اندر خواب کیوں کہتا ہے؟','شاعر ژوند ولې په خوب کې خوب بولي؟'),
('What did the poem ‘A Dream within a Dream’ make you think of? And how did it make you feel? Evaluate.','نظم ‘خواب کے اندر خواب’ نے آپ کو کس بارے میں سوچنے پر مجبور کیا؟ اور اس نے آپ کو کیسا محسوس کرایا؟ جائزہ لیں۔','نظم ‘په خوب کې خوب’ تاسو د کوم شي په اړه فکر ته اړ کړل؟ او تاسو ته یې څه احساس درکړ؟ وارزوئ.')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u18-rc','exercise')
F.done()
s['sourceNote']='Printed page 161. A bold-headed "About the poet:" paragraph (the textbook\'s own note; the printed text has stray quote marks, e.g. "’Al Aaraaf’", "‘A Dream Within a Dream”", and a space before the colon; kept as printed), a pink "Glossary" banner and a table (Word / Meaning) of 3 rows ("surf-tormented" is hyphenated across two lines in the cell), then a pink "Reading Comprehension" banner with eight questions. The Urdu and Pashto columns of the glossary are added by us. A phone-number strip, the watermark and coloured page-edge markings are excluded. Border lines and pink corner flags are excluded. The page number 161 is printed in a diamond at the foot.'
s['vocabulary']=V
save(s)
