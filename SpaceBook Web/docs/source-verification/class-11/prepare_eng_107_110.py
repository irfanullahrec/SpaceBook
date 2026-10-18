from enghelp import *
c=cell
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
EX='eng11-u10-grammar'
# ---------- scan 107 (printed 98) ----------
s=page(107,'u10','98','Grammar: participles (A end, B, C)','قواعد: participles (الف کا اختتام، ب، ج)','ګرامر: participles (الف پای، ب، ج)','participles-2')
F=Flow(s)
GA=[('the ______ computer (repair)','وہ ______ کمپیوٹر (repair)','هغه ______ کمپیوټر (repair)'),('the ______ students (talk)','وہ ______ طلبہ (talk)','هغه ______ زده کوونکي (talk)'),('______ fans (excite)','______ مداح (excite)','______ مینه‌وال (excite)'),('the girl ______ next door (live)','پڑوس میں ______ لڑکی (live)','هغه نجلۍ چې ګاونډ کې ______ (live)')]
for i,(a,b,d) in enumerate(GA,7): Qn(s,f'a{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gb','B. Put in the verbs in parenthesis as participles (present participle or past participle) into the blank.','ب. قوسین میں دیے گئے افعال کو participles (حالیہ یا ماضیہ) کے طور پر خالی جگہ میں لکھیں۔','ب. د قوس په منځ کې ورکړل شوي فعلونه په تشه کې د participles (حالیه یا ماضیه) په توګه ولیکئ.',EX,'grammar',sourceGap=dict(note='The printed instruction reads "particip e)" with a gap in the word "participle"; read from context.'))
GB=[('He saw his friend ______ (go) out with Murad.','اس نے اپنے دوست کو مراد کے ساتھ باہر ______ (go) دیکھا۔','هغه خپل ملګری د مراد سره بهر ______ (go) ولید.'),
('The bus crashed into the blue car ______ (drive) down the hill.','بس پہاڑی سے نیچے ______ (drive) نیلی کار سے ٹکرا گئی۔','بس د غونډۍ ښکته ______ (drive) شین موټر سره ټکر شو.'),
('Aayan hurt his leg ______ (do) karate.','آیان نے کراٹے ______ (do) اپنی ٹانگ زخمی کر لی۔','آیان کراټې ______ (do) خپله پښه ټپي کړه.'),
('The umbrella ______ (find) at the bus stop belongs to Abrar.','بس سٹاپ پر ______ (find) چھتری ابرار کی ہے۔','هغه چتر چې د بس تم ځای کې ______ (find) د ابرار دی.'),
('The people ______ (walk) in the street are all very friendly.','گلی میں ______ (walk) لوگ سب بہت دوستانہ ہیں۔','هغه خلک چې په کوڅه کې ______ (walk) ټول ډېر دوستانه دي.'),
('I heard my mother ______ (talk) on the phone.','میں نے اپنی ماں کو فون پر ______ (talk) سنا۔','ما خپله مور په تلیفون ______ (talk) واوریده.'),
('My uncle always has his car ______ (wash).','میرے چچا ہمیشہ اپنی کار ______ (wash) کرواتے ہیں۔','زما تره تل خپل موټر ______ (wash) کوي.'),
('We stood ______ (wait) for the taxi.','ہم ٹیکسی کا ______ (wait) کھڑے رہے۔','موږ د ټکسۍ لپاره ______ (wait) ولاړ وو.'),
('______ (look) down from the tower, we saw many people walking in the streets.','ٹاور سے نیچے ______ (look) ہوئے، ہم نے بہت سے لوگوں کو گلیوں میں چلتے دیکھا۔','له برج څخه ښکته ______ (look)، موږ ډېر خلک په کوڅو کې ګرځېدل ولیدل.'),
('The people drove off in a ______ (steal) car.','لوگ ایک ______ (steal) کار میں چلے گئے۔','خلک په یوه ______ (steal) موټر کې لاړل.')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gc','C. Put in the verbs in parenthesis as Past Participle into the blank.','ج. قوسین میں دیے گئے افعال کو ماضیہ (Past Participle) کے طور پر خالی جگہ میں لکھیں۔','ج. د قوس په منځ کې ورکړل شوي فعلونه په تشه کې د تېر participle په توګه ولیکئ.',EX,'grammar')
GC=[('______ watches (repair)','______ گھڑیاں (repair)','______ ساعتونه (repair)'),('______ computers (steal)','______ کمپیوٹر (steal)','______ کمپیوټرونه (steal)'),('______ fans (fascinate)','______ مداح (fascinate)','______ مینه‌وال (fascinate)'),('______ students (bore)','______ طلبہ (bore)','______ زده کوونکي (bore)'),('______ boys (confuse)','______ لڑکے (confuse)','______ هلکان (confuse)'),('______ umbrellas (forget)','______ چھتریاں (forget)','______ چترونه (forget)'),('______ girls (disappoint)','______ لڑکیاں (disappoint)','______ نجونې (disappoint)')]
for i,(a,b,d) in enumerate(GC,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
F.done()
s['sourceNote']='Printed page 98. Items 7–10 of Part A (the page begins with "7. the ___ computer (repair)"), then Part B (10 sentences) and Part C items 1–7 (the rest is on the next page). "Not For Sale" is printed at the lower right beside the page number 98 (in a diamond). Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 108 (printed 99) ----------
s=page(108,'u10','99','Grammar: participles (C end, D) · Teacher\'s Guideline','قواعد: participles (ج کا اختتام، د) · استاد کی رہنمائی','ګرامر: participles (ج پای، د) · د ښوونکي لارښوونه','participles-3')
F=Flow(s)
GC=[('______ comics (swap)','______ مزاحیہ کتابیں (swap)','______ مزاحیه کتابونه (swap)'),('______ doctors (worry)','______ ڈاکٹر (worry)','______ ډاکټران (worry)'),('______ queens (amuse)','______ ملکائیں (amuse)','______ ملکې (amuse)')]
for i,(a,b,d) in enumerate(GC,8): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gd','D. Put in the verbs in parenthesis as Present Participle into the blank.','د. قوسین میں دیے گئے افعال کو حالیہ (Present Participle) کے طور پر خالی جگہ میں لکھیں۔','د. د قوس په منځ کې ورکړل شوي فعلونه په تشه کې د حال participle په توګه ولیکئ.',EX,'grammar')
GD=[('______ dogs (bark)','______ کتے (bark)','______ سپي (bark)'),('______ children (play)','______ بچے (play)','______ ماشومان (play)'),('______ girls (scream)','______ لڑکیاں (scream)','______ نجونې (scream)'),('______ cowboys (fight)','______ چرواہے (fight)','______ غوا‌ماران (fight)'),('______ ducks (swim)','______ بطخیں (swim)','______ مرغابۍ (swim)'),('______ babies (cry)','______ بچے (cry)','______ ماشومان (cry)'),('______ water (run)','______ پانی (run)','______ اوبه (run)'),('______ teachers (sing)','______ اساتذہ (sing)','______ ښوونکي (sing)'),('______ leaves (fall)','______ پتے (fall)','______ پاڼې (fall)'),('______ people (lie)','______ لوگ (lie)','______ خلک (lie)')]
for i,(a,b,d) in enumerate(GD,1): Qn(s,f'd{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students present and past participles.','طلبہ کو حال اور ماضی کے participles کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د حال او تېر participles تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 99. Items 8–10 of Part C (the page begins with "8. ___ comics (swap)"), Part D (10 items) and the pink "Teacher\'s Guideline" banner. A large blank space separates Part D from the guideline. The upside-down header strip, border lines, the watermark and the phone-number strip are excluded. The page number 99 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 109 (printed 100) ----------
s=page(109,'u11','100','Unit 11: The Importance of Family · Learning outcomes','یونٹ 11: خاندان کی اہمیت · سیکھنے کے نتائج','واحد 11: د کورنۍ اهمیت · د زده کړې پایلې','unit11-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 11','یونٹ 11','واحد 11')
H(s,'title','The Importance of Family','خاندان کی اہمیت','د کورنۍ اهمیت')
add(s,'au','Sam Keen','سیم کین','سیم کین')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject), and supporting details.','متن کے اقتباسات کا تجزیہ کر کے موضوع/عمومی مضمون، کلیدی خیال/مرکزی فکر (عمومی موضوع کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔','د متن برخې تحلیل کړي ترڅو موضوع/عمومي مضمون، کلیدي مفکوره/مرکزي فکر (د عمومي موضوع په اړه یو بیان) او ملاتړي جزئیات وپېژني.'),
('analyze paragraphs to identify sentences that support the main idea through','پیراگرافوں کا تجزیہ کر کے ایسے جملوں کی نشاندہی کریں جو درج ذیل کے ذریعے مرکزی خیال کی تائید کرتے ہیں:','پاراګرافونه تحلیل کړي ترڅو هغه جملې وپېژني چې د لاندې له لارې اصلي مفکوره ملاتړ کوي:'),
('• definition','• تعریف','• تعریف'),('• example/ illustration','• مثال/وضاحت','• بېلګه/روښانونه'),('• cause and effect','• سبب اور اثر','• لامل او اغېز'),('• comparison and contrast','• موازنہ اور تقابل','• پرتله او توپیر'),('• facts, analogies, anecdotes and quotations.','• حقائق، تمثیلیں، حکایات اور اقتباسات۔','• حقایق، تمثیلونه، حکایتونه او نقل‌قولونه.'),
('recognize that support can be in the form of a single word, a phrase, a sentence or a full paragraph.','پہچانیں کہ تائید ایک لفظ، ایک فقرے، ایک جملے یا مکمل پیراگراف کی صورت میں ہو سکتی ہے۔','وپېژني چې ملاتړ کېدای شي د یوې کلمې، عبارت، جملې یا بشپړ پاراګراف په بڼه وي.'),
('apply critical thinking to interact with text, use intensive reading strategies (while-reading) to:','متن سے تعامل کے لیے تنقیدی سوچ کو بروئے کار لائیں، گہرے مطالعے کی حکمتِ عملیاں (پڑھتے وقت) استعمال کریں تاکہ:','له متن سره د اړیکې لپاره انتقادي فکر پلي کړي، د ژورې لوست ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو:'),
('• scan to answer short questions.','• مختصر سوالات کے جواب کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي.'),
('• make simple inferences using context of the text and prior knowledge.','• متن کے سیاق اور پیشگی علم سے سادہ نتائج اخذ کریں۔','• د متن د شرایطو او مخکني پوهې په کارولو ساده پایلې واخلي.'),
('• distinguish between what is clearly stated and what is implied.','• جو واضح طور پر بیان کیا گیا ہے اور جو ضمنی ہے ان میں فرق کریں۔','• د هغه څه چې په روښانه ډول بیان شوي او هغه چې ضمني دي ترمنځ توپیر وکړي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 100: Unit 11 opening page with the unit number, the title banner "The Importance of Family", the author tag "Sam Keen" and the first part of the learning outcomes with nested bullets (the list continues on the next page). "Not For Sale" is printed at the lower right beside the page number 100 (in a diamond). Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 110 (printed 101) ----------
s=page(110,'u11','101','Learning outcomes (continued)','سیکھنے کے نتائج (جاری)','د زده کړې پایلې (دوام)','unit11-outcomes-2',layout='outcomes')
F=Flow(s)
O=[('distinguish between language used for persuasion and propaganda:','ترغیب اور پروپیگنڈے کے لیے استعمال ہونے والی زبان میں فرق کریں:','د قانع کولو او پروپاګنډې لپاره کارېدونکې ژبې ترمنځ توپیر وکړي:'),
('• use persuasive language to enhance ideas.','• خیالات کو بہتر بنانے کے لیے ترغیبی زبان استعمال کریں۔','• د نظرونو د ښه کولو لپاره قانع کوونکې ژبه وکاروي.'),
('use special devices to support arguments e.g. appeal to logic through reasoning, appeal to emotion or ethical belief, relating a personal anecdote or analogy.','دلائل کی تائید کے لیے خصوصی حربے استعمال کریں مثلاً استدلال کے ذریعے منطق سے اپیل، جذبات یا اخلاقی عقیدے سے اپیل، ذاتی واقعہ یا تمثیل بیان کرنا۔','د استدلالونو د ملاتړ لپاره ځانګړې وسایل وکاروي لکه د استدلال له لارې منطق ته اپیل، احساساتو یا اخلاقي باور ته اپیل، شخصي پېښه یا تمثیل بیانول.'),
('anticipate and respond to opposing arguments by defending point of view with factual evidence, quotations, expert opinion, logical reasoning, and commonly held beliefs.','حقائق پر مبنی ثبوت، اقتباسات، ماہرانہ رائے، منطقی استدلال اور عام عقائد کے ساتھ اپنے نقطۂ نظر کا دفاع کرتے ہوئے مخالف دلائل کا پیشگی اندازہ لگائیں اور ان کا جواب دیں۔','د حقیقي شواهدو، نقل‌قولونو، د متخصصانو نظر، منطقي استدلال او عامو باورونو سره د خپل لیدلوري دفاع کولو سره د مخالفو استدلالونو وړاندوینه او ځواب ورکړي.'),
('demonstrate heightened awareness of conventions and dynamics of group discussion and interaction to:','گروہی بحث اور تعامل کے اصولوں اور حرکیات سے بلند آگاہی کا مظاہرہ کریں تاکہ:','د ډله‌ییزې بحث او اړیکې د دودونو او حرکیاتو لوړ پوهاوی وښيي ترڅو:'),
('• present and explain one’s point of view clearly.','• اپنے نقطۂ نظر کو واضح طور پر پیش اور بیان کریں۔','• خپل لیدلوری په روښانه ډول وړاندې او تشریح کړي.'),
('• support or modify one’s opinions with reasons.','• دلائل کے ساتھ اپنی رائے کی تائید کریں یا اسے تبدیل کریں۔','• خپل نظرونه په دلایلو سره ملاتړ یا بدل کړي.'),
('• acknowledge others’ contributions.','• دوسروں کی شراکت کو تسلیم کریں۔','• د نورو ونډه ومني.'),
('• agree and disagree politely at appropriate times.','• مناسب مواقع پر شائستگی سے اتفاق اور اختلاف کریں۔','• په مناسبو وختونو کې په ادب سره موافقه او مخالفت وکړي.'),
('• share information and ideas.','• معلومات اور خیالات کا اشتراک کریں۔','• معلومات او نظرونه شریک کړي.'),
('• clarify, rephrase, explain, expand and restate information and ideas.','• معلومات اور خیالات کی وضاحت کریں، دوبارہ بیان کریں، تشریح کریں، وسعت دیں اور دہرائیں۔','• معلومات او نظرونه روښانه کړي، بیا ووايي، تشریح کړي، پراخ کړي او بیا تکرار کړي.'),
('use various reference sources to refine vocabulary for interpersonal academic workplace situation including figurative, idiomatic and technical vocabulary.','باہمی، تعلیمی اور کام کی جگہ کی صورتحال کے لیے مختلف حوالہ جاتی ذرائع استعمال کر کے ذخیرۂ الفاظ کو بہتر بنائیں، بشمول علامتی، محاوراتی اور تکنیکی الفاظ۔','د شخصي، علمي او کار ځای حالتونو لپاره د لغت د ښه کولو لپاره بېلابېل مرجع سرچینې وکاروي، په ګډون د مجازي، اصطلاحي او تخنیکي لغت.'),
('illustrate use of infinitive and infinitive phrases.','مصدر (infinitive) اور مصدری فقروں کے استعمال کی مثال دیں۔','د مصدر (infinitive) او مصدري عبارتونو کارول وښيي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 101: continuation of the Unit 11 learning outcomes with nested bullets (the printed bullets "•" are shown in the text of the sub-items). The first line begins in the middle of the list without a heading. Border lines, pink corner flags, the watermark and the phone-number strip are excluded. The page number 101 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
