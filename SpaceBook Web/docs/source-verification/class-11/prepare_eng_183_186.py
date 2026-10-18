from enghelp import *
c=cell
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def Op(s,key,en,ur,ps,ex,tab='grammar',**m): add(s,key,en,ur,ps,role='option',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
GEX='eng11-u19-grammar'; VEX='eng11-u19-vocab'
P1={'in':('میں','په'),'at':('پر','په'),'on':('پر','پر'),'for':('کے لیے','لپاره'),'by':('کے ذریعے','په وسیله'),'with':('کے ساتھ','سره'),'from':('سے','له'),'since':('جب سے','له…راهیسې'),'to':('کی طرف','ته'),'before':('سے پہلے','مخکې'),'within':('کے اندر','په ترڅ کې'),'beside':('کے پاس','ترڅنګ'),'besides':('کے علاوہ','سربېره'),'outside':('باہر','بهر'),'ago':('پہلے','مخکې'),'into':('کے اندر','دننه'),'after':('کے بعد','وروسته')}
def prep(l,words):
    parts=[w.strip() for w in words.split(',')]
    ur='، '.join(P1[w][0] for w in parts); ps='، '.join(P1[w][1] for w in parts)
    return f'{l}) {words}',f'{l}) {ur} ({words})',f'{l}) {ps} ({words})'
# ---------- scan 183 (printed 174) ----------
s=page(183,'u19','174','Dialogue (end) · Grammar: prepositions (A, 1–10)','مکالمہ (اختتام) · قواعد: حروفِ جار (الف، 1–10)','مکالمه (پای) · ګرامر: حروف جر (الف، ۱–۱۰)','dialogue-prepositions-a')
F=Flow(s)
D=[('afford it. Our business is in the red right now, but we have some good contracts coming up. We should be in the black soon–- and that property would be ideal. I’ll try calling Waqar myself. If we can’t come up with a solution, we’ll have to call off the deal and do without the bigger office.”','…کا خرچ اٹھا سکوں۔ ہمارا کاروبار ابھی خسارے میں ہے، لیکن ہمارے کچھ اچھے معاہدے آنے والے ہیں۔ ہمیں جلد منافع میں ہونا چاہیے–- اور وہ جائیداد مثالی ہوگی۔ میں خود وقار کو فون کرنے کی کوشش کروں گا۔ اگر ہم کوئی حل نہ نکال سکے تو ہمیں سودا منسوخ کرنا اور بڑے دفتر کے بغیر گزارا کرنا پڑے گا۔”','…ورته مالي وس ولرم. زموږ کاروبار اوس زیان کې دی، خو موږ ځینې ښه قراردادونه راتلونکي لرو. موږ باید ژر په ګټه کې شو–- او هغه ملکیت به مثالي وي. زه به پخپله وقار ته زنګ ووهم. که موږ حل ونه موموو نو باید معامله لغوه کړو او پرته له لوی دفتر ګذاره وکړو.”',dict(sourceGap=dict(note='The first words complete the speech of the previous page ("… help me figure out a way to afford it.").'))),
('Rubi: “Well, good luck then. It’s hard to give up a dream! Let me know what you decide.”','روبی: “خیر، پھر اچھی قسمت۔ خواب کو چھوڑنا مشکل ہوتا ہے! مجھے بتائیں کہ آپ کیا فیصلہ کرتے ہیں۔”','روبي: “ښه، نو ښه مرغلرې. د یو خوب پرېښودل ستونزمن دي! ماته ووایئ چې تاسو څه پرېکړه کوئ.”'),
('Kamal: “I will. Take care!”','کمال: “میں بتاؤں گا۔ اپنا خیال رکھیں!”','کمال: “زه به ووایم. خپل پام وساتئ!”')]
for i,(a,b,d,*m) in enumerate(D,1): add(s,f'd{i}',a,b,d,tab='vocabulary',role='question',exerciseId=VEX,**(m[0] if m else {}))
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
H(s,'gh','PREPOSITIONS AND PREPOSITIONAL PHRASES','حروفِ جار اور جاری فقرے','حروف جر او جري عبارتونه',tab='grammar')
Qn(s,'ga','A. Fill in the blanks with suitable prepositions.','الف. موزوں حروفِ جار سے خالی جگہیں پُر کریں۔','الف. تشې په مناسبو حروفو جر ډکې کړئ.',GEX,'grammar')
A=[('He lives ______ 48, MG Road.','وہ ______ 48، ایم جی روڈ پر رہتا ہے۔','هغه ______ ۴۸، ایم جي روډ اوسېږي.',['in','at','on','for']),
('We started ______ eight ______ the morning.','ہم نے ______ آٹھ بجے ______ صبح کے وقت آغاز کیا۔','موږ ______ اته بجې ______ سهار پیل کړ.',['at, in','in, at','in, on','at, on']),
('This portrait was painted ______ an artist who lived in the eighteenth century.','یہ پورٹریٹ ایک ______ فنکار نے بنایا جو اٹھارہویں صدی میں رہتا تھا۔','دا پورټریټ د یو ______ هنرمند لخوا جوړ شوی چې په اتلسمه پېړۍ کې ژوند کاوه.',['by','with','in','for']),
('We must start ______ dawn if we want to reach in time.','اگر ہم وقت پر پہنچنا چاہتے ہیں تو ہمیں ______ فجر شروع کرنا ہوگا۔','که موږ غواړو په وخت ورسېږو نو باید ______ سهار پیل کړو.',['in','on','at','with']),
('We have been waiting ______ morning.','ہم ______ صبح سے انتظار کر رہے ہیں۔','موږ ______ سهار انتظار کوو.',['for','since','from','to']),
('The traveler must reach his destination ______ sunset.','مسافر کو اپنی منزل ______ غروبِ آفتاب تک پہنچنا ہوگا۔','مسافر باید خپل منزل ______ لمر لوېدو ته ورسېږي.',['in','at','before','on']),
('The next flight is due ______ 6 pm.','اگلی پرواز ______ شام 6 بجے متوقع ہے۔','راتلونکې الوتنه ______ ماښام ۶ بجو متوقعه ده.',['in','on','at','before']),
('He ran twelve miles ______ two hours.','وہ ______ دو گھنٹے میں بارہ میل دوڑا۔','هغه ______ دوو ساعتونو کې دولس میله ودوېد.',['in','at','on','for']),
('He ran ______ the room, panting for breath.','وہ ______ کمرے میں دوڑا، ہانپتے ہوئے۔','هغه ______ خونې ته منډه کړه، په ساه ټوپونو سره.',['at','into','after','on']),
('He does not leave his house ______ 9 am.','وہ صبح 9 بجے سے ______ اپنا گھر نہیں چھوڑتا۔','هغه ______ ۹ بجو سهار خپل کور نه پرېږدي.',['in','on','before','by'])]
for i,(a,b,d,os) in enumerate(A,1):
    Qn(s,f'a{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
    for l,o in zip('abcd',os):
        e,u,p=prep(l,o); Op(s,f'a{i}{l}',e,u,p,GEX)
F.done()
s['sourceNote']='Printed page 174. The page begins with the last lines of Kamal\'s long speech and the end of the dialogue, then "GRAMMAR", the heading "PREPOSITIONS AND PREPOSITIONAL PHRASES" and Part A items 1–10, each with four lettered options a)–d) printed in a row (item 2 offers pairs such as "at, in"). The printed text of the dialogue contains the double dash "–-". The Urdu and Pashto renderings of the options are translations by us with the English preposition in brackets. The right edge of the scan clips the word "afford" at the start. Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 174 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 184 (printed 175) ----------
s=page(184,'u19','175','Grammar: prepositions (A end, B) · Teacher\'s Guideline','قواعد: حروفِ جار (الف کا اختتام، ب) · استاد کی رہنمائی','ګرامر: حروف جر (الف پای، ب) · د ښوونکي لارښوونه','prepositions-b')
F=Flow(s)
A2=[('The train departs ______ 3 am.','ٹرین صبح 3 بجے ______ روانہ ہوتی ہے۔','اورګاډی ______ ۳ بجې سهار روانېږي.',['in','at','on','within'],11),
('______ his children, his nephews and nieces were also present.','______ اس کے بچوں کے، اس کے بھتیجے بھانجیاں بھی موجود تھے۔','______ د هغه د ماشومانو، د هغه ورېرونه او خویندې هم حاضر وې.',['beside','besides','outside','before'],12),
('______ last month, I haven’t seen him even once.','______ پچھلے مہینے سے، میں نے اسے ایک بار بھی نہیں دیکھا۔','______ تېرې میاشتې، ما هغه یو ځل هم نه دی لیدلی.',['for','since','ago','from'],13),
('Faisalabad is famous ______ its textile mills.','فیصل آباد ______ اپنی ٹیکسٹائل ملوں کے لیے مشہور ہے۔','فیصل‌آباد ______ خپلو ټوکر جوړولو کارخانو لپاره مشهور دی.',['in','for','on','at'],14)]
for a,b,d,os,n in A2:
    Qn(s,f'a{n}',f'{n}. {a}',f'{n}. {b}',f'{n}. {d}',GEX,'grammar')
    for l,o in zip('abcd',os):
        e,u,p=prep(l,o); Op(s,f'a{n}{l}',e,u,p,GEX)
Qn(s,'gb','B. Complete the following sentences using appropriate prepositional phrases. Each question is followed by three suggested answers. Choose the most appropriate one.','ب. مناسب جاری فقروں (prepositional phrases) کو استعمال کرتے ہوئے درج ذیل جملے مکمل کریں۔ ہر سوال کے بعد تین تجویز کردہ جوابات ہیں۔ سب سے موزوں کا انتخاب کریں۔','ب. لاندې جملې د مناسبو جري عبارتونو (prepositional phrases) په کارولو بشپړې کړئ. هره پوښتنه وروسته درې وړاندیز شوي ځوابونه دي. تر ټولو مناسب وټاکئ.',GEX,'grammar')
B=[('______ Sherena, they all seemed pretty cordial.','______ شیرینہ کے، وہ سب کافی دوستانہ لگ رہے تھے۔','______ شیرینا، هغوی ټول ډېر دوستانه ښکارېدل.',[('except for','کے سوا','پرته له'),('except with','کے ساتھ کے علاوہ','له سره پرته'),('except from','سے کے علاوہ','له څخه پرته')]),
('______ cancer is curable.','______ کینسر قابلِ علاج ہے۔','______ سرطان د درملنې وړ دی.',[('to a great extent','بڑی حد تک','تر ډېرې کچې'),('for a great extent','بڑی حد کے لیے','د ډېرې کچې لپاره'),('in a great extent','بڑی حد میں','په ډېره کچه کې')]),
('______ the starter, I thought the meal was excellent.','______ ابتدائی ڈش کے، میں نے سمجھا کہ کھانا بہترین تھا۔','______ د پیل خواړو، ما فکر کاوه چې خواړه غوره وو.',[('apart with','کے ساتھ الگ','سره جلا'),('apart from','کے علاوہ','پرته له'),('apart for','کے لیے الگ','لپاره جلا')]),
('What is the ______ you?','آپ کے ساتھ ______ کیا ہے؟','له تاسو سره ______ څه دی؟',[('matter of','کا معاملہ','د موضوع'),('matter with','کے ساتھ مسئلہ','سره ستونزه'),('matter on','پر معاملہ','پر موضوع')]),
('My car is parked ______ the post office.','میری کار ڈاک خانے ______ کھڑی ہے۔','زما موټر د پوستې دفتر ______ ولاړ دی.',[('in front of','کے سامنے','مخې ته'),('in front','سامنے','مخکې'),('in front at','سامنے پر','مخکې په')]),
('He acted ______ my instructions.','اس نے میری ہدایات ______ عمل کیا۔','هغه زما د هدایاتو ______ عمل وکړ.',[('according with','کے ساتھ مطابق','سره مطابق'),('according to','کے مطابق','سره سم'),('accordance with','کی تعمیل میں','سره سم')]),
('He is ______ me.','وہ میرے ______ ہے۔','هغه زما سره ______ دی.',[('at enmity with','سے دشمنی میں','سره په دښمنۍ کې'),('at enmity for','کے لیے دشمنی میں','لپاره په دښمنۍ کې'),('at enmity','دشمنی میں','په دښمنۍ کې')]),
('I called him ______ my voice.','میں نے اسے اپنی آواز ______ پکارا۔','ما هغه زما د غږ ______ وغوښت.',[('at the top of','پوری قوت سے','په سر کې'),('at the top off','اوپر سے ہٹ کر','په سر کې لرې'),('with the top of','کی چوٹی کے ساتھ','د سر سره')]),
('His words are ______ the facts.','اس کے الفاظ حقائق ______ ہیں۔','د هغه کلمې له حقایقو سره ______ دي.',[('at variance with','سے مختلف','سره توپیر لري'),('at variance to','کی طرف مختلف','ته توپیر'),('at variance of','کا اختلاف','د توپیر')])]
for i,(a,b,d,os) in enumerate(B,1):
    Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
    for l,(e,u,p) in zip('abc',os): Op(s,f'b{i}{l}',f'{l}) {e}',f'{l}) {u} ({e})',f'{l}) {p} ({e})',GEX)
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students how to use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passages from English to Urdu and Urdu to English.','طلبہ کو وضاحت کریں اور اعادہ کرائیں کہ لغوی اور مجازی معنی، گرامر کی جنس اور نحو کے علم کا استعمال کر کے اقتباسات کا انگریزی سے اردو اور اردو سے انگریزی میں ترجمہ کیسے کیا جائے۔','زده کوونکو ته تشریح او تکرار کړئ چې د لغوي او مجازي معنا، ګرامري جنس او نحو پوهه په کارولو سره برخې له انګلیسي څخه اردو او له اردو څخه انګلیسي ته څنګه وژباړل شي.')
F.done()
s['sourceNote']='Printed page 175. Items 11–14 of Part A (four lettered options a)–d)), Part B (nine items, each with three lettered options a)–c) of prepositional phrases) and the pink "Teacher\'s Guideline" banner. Some of the Part B options are deliberately wrong in print (e.g. "at the top off"); they are kept as printed and the Urdu and Pashto renderings are literal translations by us with the English phrase in brackets. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 175 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 185 (printed 176) ----------
s=page(185,'u20','176','Unit 20: How to Take a Job Interview · Learning outcomes','یونٹ 20: جاب انٹرویو کیسے دیں · سیکھنے کے نتائج','واحد 20: د دندې مرکه څنګه ورکړو · د زده کړې پایلې','unit20-outcomes-1',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 20','یونٹ 20','واحد 20')
H(s,'title','How to Take a Job Interview','جاب انٹرویو کیسے دیں','د دندې مرکه څنګه ورکړو')
add(s,'au','Waheedullah','وحید اللہ','وحیدالله')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject), and supporting details.','متن کے اقتباسات کا تجزیہ کر کے موضوع/عمومی مضمون، کلیدی خیال/مرکزی فکر (عمومی موضوع کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔','د متن برخې تحلیل کړي ترڅو موضوع/عمومي مضمون، کلیدي مفکوره/مرکزي فکر (د عمومي موضوع په اړه یو بیان) او ملاتړي جزئیات وپېژني.'),
('recognize that the theme of a text is carried in a thesis statement.','پہچانیں کہ متن کا موضوع ایک مرکزی دعوے (تھیسس اسٹیٹمنٹ) میں ہوتا ہے۔','وپېژني چې د متن موضوع په مرکزي ادعا (تیسس) کې وي.'),
('analyze paragraphs to identify sentences that support the main idea through:','پیراگرافوں کا تجزیہ کر کے ایسے جملوں کی نشاندہی کریں جو درج ذیل کے ذریعے مرکزی خیال کی تائید کرتے ہیں:','پاراګرافونه تحلیل کړي ترڅو هغه جملې وپېژني چې د لاندې له لارې اصلي مفکوره ملاتړ کوي:'),
('• definition','• تعریف','• تعریف'),('• example/ illustration','• مثال/وضاحت','• بېلګه/روښانونه'),('• facts, analogies, anecdotes and quotations.','• حقائق، تمثیلیں، حکایات اور اقتباسات۔','• حقایق، تمثیلونه، حکایتونه او نقل‌قولونه.'),
('recognize that support can be in the form of a single word, a phrase, a sentence or a full paragraph.','پہچانیں کہ تائید ایک لفظ، ایک فقرے، ایک جملے یا مکمل پیراگراف کی صورت میں ہو سکتی ہے۔','وپېژني چې ملاتړ کېدای شي د یوې کلمې، عبارت، جملې یا بشپړ پاراګراف په بڼه وي.'),
('identify and recognize the functions of transitional devices used for coherence and cohesion at discourse level.','گفتگو کی سطح پر ہم آہنگی اور ربط کے لیے استعمال ہونے والے انتقالی ذرائع کے افعال کی نشاندہی کریں اور پہچانیں۔','د بحث په کچه د همغږۍ او اړیکې لپاره کارېدونکو انتقالي وسایلو دندې وپېژني.'),
('apply critical thinking to interact with text, use intensive reading strategies (while-reading) to:','متن سے تعامل کے لیے تنقیدی سوچ کو بروئے کار لائیں، گہرے مطالعے کی حکمتِ عملیاں (پڑھتے وقت) استعمال کریں تاکہ:','له متن سره د اړیکې لپاره انتقادي فکر پلي کړي، د ژورې لوست ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو:'),
('• scan to answer short questions.','• مختصر سوالات کے جواب کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي.'),
('• distinguish between what is clearly stated and what is implied.','• جو واضح طور پر بیان کیا گیا ہے اور جو ضمنی ہے ان میں فرق کریں۔','• د هغه څه چې په روښانه ډول بیان شوي او هغه چې ضمني دي ترمنځ توپیر وکړي.'),
('• comprehend/interpret text by applying critical thinking.','• تنقیدی سوچ کو بروئے کار لا کر متن کو سمجھیں/اس کی تشریح کریں۔','• د انتقادي فکر په پلي کولو سره متن وپوهېږي/تفسیر یې کړي.'),
('• comprehend various job advertisements to write in response, an effective job application, a resume and a covering letter.','• مختلف ملازمت کے اشتہارات کو سمجھ کر جواب میں ایک مؤثر درخواست، ایک ریزیومے اور ایک کور لیٹر لکھیں۔','• د دندو بېلابېل اعلانونه وپوهېږي ترڅو په ځواب کې یو اغېزناک دندې غوښتنلیک، ریزیومې او پوښونکی لیک ولیکي.'),
('demonstrate use of appropriate conventions to give a job interview:','ملازمت کا انٹرویو دینے کے لیے مناسب آداب کے استعمال کا مظاہرہ کریں:','د دندې مرکې ورکولو لپاره د مناسبو دودونو کارول وښيي:'),
('• preempt the questions for a job interview.','• ملازمت کے انٹرویو کے سوالات کا پیشگی اندازہ لگائیں۔','• د دندې د مرکې پوښتنې دمخه اټکل کړي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 176: Unit 20 opening page with the unit number, the title banner "How to Take a Job Interview", the author tag "Waheedullah" and the first part of the learning outcomes with nested bullets (the list continues on the next page; printed bullets "•" shown in the text of sub-items). The printed bullet reads "a resume´ and a covering letter" with a stray accent; kept as "a resume". Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 176 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 186 (printed 177) ----------
s=page(186,'u20','177','Learning outcomes (continued)','سیکھنے کے نتائج (جاری)','د زده کړې پایلې (دوام)','unit20-outcomes-2',layout='outcomes')
F=Flow(s)
O=[('• formulate and practice responses.','• جوابات تیار کریں اور ان کی مشق کریں۔','• ځوابونه جوړ او تمرین کړي.'),
('• learn proper etiquettes and conventions of dress, appearance, tone and body language.','• لباس، ظاہری شکل، لہجے اور جسمانی زبان کے مناسب آداب اور اصول سیکھیں۔','• د جامو، ظاهري بڼې، لهجې او د بدن د ژبې مناسب آداب او دودونه زده کړي.'),
('• introduce self.','• اپنا تعارف کرائیں۔','• ځان معرفي کړي.'),
('• demonstrate good listening skills.','• سننے کی اچھی مہارتوں کا مظاہرہ کریں۔','• د اورېدلو ښې مهارتونه وښيي.'),
('• give appropriate responses using reciprocal ability.','• باہمی صلاحیت استعمال کرتے ہوئے مناسب جوابات دیں۔','• د دوه‌اړخیزې وړتیا په کارولو مناسب ځوابونه ورکړي.'),
('• request for repetition or restatement of a query.','• سوال کو دہرانے یا دوبارہ بیان کرنے کی درخواست کریں۔','• د پوښتنې تکرار یا بیا بیانولو غوښتنه وکړي.'),
('• repeat, restate coherently to clarify own opinions and ideas.','• اپنی رائے اور خیالات کی وضاحت کے لیے مربوط انداز میں دہرائیں، دوبارہ بیان کریں۔','• د خپلو نظرونو او مفکورو د روښانه کولو لپاره په منسجم ډول تکرار او بیا بیان کړي.'),
('• support ideas and opinions with solid evidence','• خیالات اور آراء کی ٹھوس شواہد سے تائید کریں','• نظرونه او رایې په پیاوړو شواهدو ملاتړ کړي'),
('use various reference sources to refine vocabulary for interpersonal academic workplace situation including figurative, idiomatic and technical vocabulary.','باہمی، تعلیمی اور کام کی جگہ کی صورتحال کے لیے مختلف حوالہ جاتی ذرائع استعمال کر کے ذخیرۂ الفاظ کو بہتر بنائیں، بشمول علامتی، محاوراتی اور تکنیکی الفاظ۔','د شخصي، علمي او کار ځای حالتونو لپاره د لغت د ښه کولو لپاره بېلابېل مرجع سرچینې وکاروي، په ګډون د مجازي، اصطلاحي او تخنیکي لغت.'),
('use in speech and writing, all the appropriate transitional devices.','تقریر اور تحریر میں تمام مناسب انتقالی ذرائع استعمال کریں۔','په وینا او لیکنه کې ټول مناسب انتقالي وسایل وکاروي.'),
('comprehend various job advertisements to write in response, an effective job application, a resume and a covering letter.','مختلف ملازمت کے اشتہارات کو سمجھ کر جواب میں ایک مؤثر درخواست، ایک ریزیومے اور ایک کور لیٹر لکھیں۔','د دندو بېلابېل اعلانونه وپوهېږي ترڅو په ځواب کې یو اغېزناک دندې غوښتنلیک، ریزیومې او پوښونکی لیک ولیکي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
add(s,'n','A grey-toned illustration of a job interview (an interviewer and a colleague seated behind a desk facing a candidate) fills the lower part of the page; it is an illustration and is not reproduced.','صفحے کے نچلے حصے میں ملازمت کے انٹرویو کی سرمئی رنگ کی مثالی تصویر ہے (میز کے پیچھے بیٹھا انٹرویو لینے والا اور ایک ساتھی، سامنے امیدوار)؛ یہ تصویر نقل نہیں کی گئی۔','د پاڼې په ښکتنۍ برخه کې د دندې د مرکې خړ رنګه روښانونه دی (د مېز شاته ناست مرکه کوونکی او یو همکار، مخې ته نوماند)؛ دا انځور نه دی رانقل شوی.')
F.done()
s['sourceNote']='Printed page 177: the rest of the Unit 20 learning outcomes (the first line begins in the middle of the list with the sub-bullets of "demonstrate use of appropriate conventions to give a job interview") and a grey illustration of a job interview, which is not reproduced. Border lines, a pink corner flag, the watermark and coloured binding strips at the foot are excluded. The page number 177 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
