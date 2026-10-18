from enghelp import *
c=cell
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
GEX='eng11-u20-grammar'
# ---------- scan 203 (printed 194) ----------
s=page(203,'u20','194','Grammar: passive voice (B end, C 1–6)','قواعد: مجہول (ب کا اختتام، ج 1–6)','ګرامر: مجهول (ب پای، ج ۱–۶)','passive-voice-bc')
F=Flow(s)
add(s,'k4b','A: Tomorrow, I hope.','الف: کل، میں امید کرتا ہوں۔','الف: سبا، زه هیله لرم.',tab='grammar')
add(s,'k5','5 B: ______? (the cars/badly/damage)','5 ب: ______؟ (the cars/badly/damage)','۵ ب: ______؟ (the cars/badly/damage)',tab='grammar',role='question',exerciseId=GEX)
add(s,'k5b','A: Yes, they are. One of them is completely destroyed.','الف: ہاں، ہیں۔ ان میں سے ایک مکمل طور پر تباہ ہو گئی ہے۔','الف: هو، دي. له هغو یوه په بشپړ ډول ویجاړه شوې ده.',tab='grammar')
add(s,'k6','6 B: ______ yet? (the removal/start)','6 ب: ______ ابھی تک؟ (the removal/start)','۶ ب: ______ لا؟ (the removal/start)',tab='grammar',role='question',exerciseId=GEX)
add(s,'k6b','A: Yes, It has. When I was there in the morning, one of the cars was just being put onto a lorry.','الف: ہاں، ہو گیا ہے۔ جب میں صبح وہاں تھا تو ایک کار کو بس لاری پر ڈالا جا رہا تھا۔','الف: هو، شوی دی. کله چې زه سهار هلته وم نو یوه موټر یوازې پر لاری اچول کېده.',tab='grammar')
add(s,'k7','7 B: You look quite depressed. Was it your car which was completely destroyed?','7 ب: آپ کافی افسردہ لگ رہے ہیں۔ کیا آپ ہی کی کار مکمل طور پر تباہ ہوئی؟','۷ ب: تاسو ډېر خپه ښکارئ. ایا ستاسو موټر وو چې په بشپړ ډول ویجاړ شو؟',tab='grammar')
add(s,'k7b','A: No, it wasn’t. But... Derek, where ______ last night? (your car/park)','الف: نہیں، ایسا نہیں تھا۔ لیکن... ڈیرک، کل رات ______ کہاں؟ (your car/park)','الف: نه، نه و. خو... ډیریک، تېره شپه ______ چېرته؟ (your car/park)',tab='grammar',role='question',exerciseId=GEX)
add(s,'k7c','B: Are you joking? My car had been parked in my garage long before the storm started.','ب: کیا آپ مذاق کر رہے ہیں؟ میری کار طوفان شروع ہونے سے بہت پہلے میرے گیراج میں کھڑی کی جا چکی تھی۔','ب: ایا تاسو ټوکې کوئ؟ زما موټر د طوفان له پیل مخکې ډېر وخت زما په ګراج کې ولاړ شوی و.',tab='grammar')
Qn(s,'gc','C. Make passive voice','ج. مجہول (passive voice) بنائیں','ج. مجهول (passive voice) جوړ کړئ',GEX,'grammar')
C=[('I think they make these cars in Japan. I think ______ in Japan. ______.','میں سمجھتا ہوں کہ وہ یہ کاریں جاپان میں بناتے ہیں۔ میں سمجھتا ہوں کہ ______ جاپان میں۔ ______۔','زه فکر کوم چې هغوی دا موټرې په جاپان کې جوړوي. زه فکر کوم ______ په جاپان کې. ______.'),
('You must not drop litter in the street in Singapore. ______ in the street in Singapore. ______.','آپ کو سنگاپور میں گلی میں کچرا نہیں پھینکنا چاہیے۔ ______ سنگاپور میں گلی میں۔ ______۔','تاسو باید په سنګاپور کې په کوڅه کې کثافات ونه غورځوئ. ______ په سنګاپور کې په کوڅه کې. ______.'),
('Someone smashed our window last night. ______ last night. ______.','کسی نے کل رات ہماری کھڑکی توڑ دی۔ ______ کل رات۔ ______۔','یو چا تېره شپه زموږ کړکۍ مات کړه. ______ تېره شپه. ______.'),
('They have already mended the TV set. You can collect it. ______ You can collect it. ______.','انہوں نے ٹی وی سیٹ پہلے ہی مرمت کر دیا ہے۔ آپ اسے لے سکتے ہیں۔ ______ آپ اسے لے سکتے ہیں۔ ______۔','هغوی ټلویزیون لا دمخه جوړ کړی دی. تاسو دا اخیستلای شئ. ______ تاسو دا اخیستلای شئ. ______.'),
('People will need more public transport in the near future. ______ in the near future. ______.','لوگوں کو قریبی مستقبل میں مزید پبلک ٹرانسپورٹ کی ضرورت ہوگی۔ ______ قریبی مستقبل میں۔ ______۔','خلک به په نږدې راتلونکي کې نوره عامه ترانسپورت ته اړتیا ولري. ______ په نږدې راتلونکي کې. ______.'),
('Don’t enter the room. They are decorating the walls. Don’t enter the room. ______ ______.','کمرے میں داخل نہ ہوں۔ وہ دیواروں کی سجاوٹ کر رہے ہیں۔ کمرے میں داخل نہ ہوں۔ ______ ______۔','خونې ته مه ننوځئ. هغوی دېوالونه سینګاروي. خونې ته مه ننوځئ. ______ ______.')]
for i,(a,b,d) in enumerate(C,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
F.done()
s['sourceNote']='Printed page 194. The page begins with the closing lines of the Part B conversation (lines 4 to 7), then Part C items 1–6, each printed as the active sentence followed by a half-written passive sentence and a blank line (shown as underscores). "Not For Sale" is printed at the lower right beside the page number 194 (in a diamond). Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 204 (printed 195) ----------
s=page(204,'u20','195','Grammar: passive voice (C end) · Teacher\'s Guideline','قواعد: مجہول (ج کا اختتام) · استاد کی رہنمائی','ګرامر: مجهول (ج پای) · د ښوونکي لارښوونه','passive-voice-c')
F=Flow(s)
C=[('You should not replace the roof at the beginning of winter. ______ at the beginning of winter. ______.','آپ کو سردیوں کے آغاز میں چھت تبدیل نہیں کرنی چاہیے۔ ______ سردیوں کے آغاز میں۔ ______۔','تاسو باید د ژمي په پیل کې چت بدل نه کړئ. ______ د ژمي په پیل کې. ______.'),
('People are spending less money on cars this year. ______ on cars this year. ______.','لوگ اس سال کاروں پر کم رقم خرچ کر رہے ہیں۔ ______ اس سال کاروں پر۔ ______۔','خلک پدې کال پر موټرو لږې پیسې لګوي. ______ پدې کال پر موټرو. ______.'),
('They had cooked the meal before 10 o’clock. ______ before 10 o’clock. ______.','انہوں نے 10 بجے سے پہلے کھانا پکا لیا تھا۔ ______ 10 بجے سے پہلے۔ ______۔','هغوی د ۱۰ بجو مخکې خواړه پخه کړي وو. ______ د ۱۰ بجو مخکې. ______.'),
('Someone was building the wall when I was there. ______ when I was there. ______.','جب میں وہاں تھا تو کوئی دیوار بنا رہا تھا۔ ______ جب میں وہاں تھا۔ ______۔','کله چې زه هلته وم یو چا دېوال جوړاوه. ______ کله چې زه هلته وم. ______.'),
('No problem. They sell this food in every shop. No problem. ______ in every shop. ______.','کوئی مسئلہ نہیں۔ وہ یہ کھانا ہر دکان میں بیچتے ہیں۔ کوئی مسئلہ نہیں۔ ______ ہر دکان میں۔ ______۔','کومه ستونزه نشته. هغوی دا خواړه په هره هټۍ کې پلوري. کومه ستونزه نشته. ______ په هره هټۍ کې. ______.'),
('They delivered more parcels last year because people bought more goods in e-shops. ______ last year because people bought more goods in e-shops.','انہوں نے پچھلے سال زیادہ پارسل پہنچائے کیونکہ لوگوں نے ای شاپس میں زیادہ سامان خریدا۔ ______ پچھلے سال کیونکہ لوگوں نے ای شاپس میں زیادہ سامان خریدا۔','هغوی تېر کال ډېرې بستې ورسولې ځکه چې خلکو په ای‌هټیو کې ډېر توکي واخیستل. ______ تېر کال ځکه چې خلکو په ای‌هټیو کې ډېر توکي واخیستل.'),
('They have not replaced the wheels yet. But they’ll let you know as soon as possible. ______ yet. But they’ll let you know as soon as possible.','انہوں نے ابھی تک پہیے تبدیل نہیں کیے۔ لیکن وہ آپ کو جلد از جلد بتا دیں گے۔ ______ ابھی تک۔ لیکن وہ آپ کو جلد از جلد بتا دیں گے۔','هغوی لا غلې نه دي بدلې کړې. خو هغوی به تاسو ته ژر تر ژره خبر درکړي. ______ لا. خو هغوی به تاسو ته ژر تر ژره خبر درکړي.')]
for i,(a,b,d) in enumerate(C,7): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the rules of change of voice in written and oral discourse.','طلبہ کو تحریری اور زبانی گفتگو میں صیغہ بدلنے (change of voice) کے قواعد کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته په لیکلې او شفاهي خبرو کې د غږ بدلولو (change of voice) قواعد تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 195. Part C items 7–13 (the page begins with item 7), each printed as the active sentence followed by a half-written passive sentence and a blank line (shown as underscores), and the pink "Teacher\'s Guideline" banner. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 195 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 205 (printed 196) ----------
s=page(205,'u21','196','Unit 21: The Road Not Taken · Learning outcomes','یونٹ 21: وہ راستہ جو نہیں چنا گیا · سیکھنے کے نتائج','واحد 21: هغه لار چې ونه ټاکل شوه · د زده کړې پایلې','unit21-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 21','یونٹ 21','واحد 21')
H(s,'title','The Road Not Taken','وہ راستہ جو نہیں چنا گیا','هغه لار چې ونه ټاکل شوه')
add(s,'au','Robert Frost','رابرٹ فراسٹ','رابرټ فراسټ')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('use critical thinking to respond orally and in writing to the text (post-reading ) to:','تنقیدی سوچ استعمال کر کے متن (پڑھنے کے بعد) کا زبانی اور تحریری جواب دیں تاکہ:','انتقادي فکر وکاروي ترڅو متن ته (له لوستلو وروسته) په شفاهي او لیکلي ډول ځواب ورکړي ترڅو:'),
('• give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read.','• پڑھے گئے متن میں موجود نقطہ ہائے نظر/خیالات اور مسائل سے متعلق ذاتی رائے دیں اور اپنے موقف کا جواز پیش کریں۔','• په لوستل شوي متن کې د لیدلورو/نظرونو او مسایلو په اړه شخصي نظر ورکړي او خپل دریځ توجیه کړي.'),
('• relate what is read to his or her own feelings and experiences.','• جو کچھ پڑھا گیا اسے اپنے احساسات اور تجربات سے جوڑیں۔','• هغه څه چې لوستل شوي د خپلو احساساتو او تجربو سره وتړي.'),
('• scan to answer short questions.','• مختصر سوالات کے جواب دینے کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي.'),
('read a given poem and give orally and in writing:','دی گئی نظم پڑھیں اور زبانی اور تحریری طور پر دیں:','ورکړل شوې نظم ولولي او په شفاهي او لیکلي ډول ورکړي:'),
('• theme and its development.','• موضوع اور اس کی نشوونما۔','• موضوع او د هغې پرمختګ.'),
('• personal response with justification.','• جواز کے ساتھ ذاتی ردِعمل۔','• د توجیه سره شخصي غبرګون.'),
('recognize literary techniques such as personification and alliteration.','ادبی تکنیکوں مثلاً تشخیص (جان ڈالنا) اور تکرارِ حروف کو پہچانیں۔','ادبي تخنیکونه لکه شخصیت‌بخښنه او د توري تکرار وپېژني.'),
('analyze how a writer/ poet uses language to:','تجزیہ کریں کہ ایک مصنف/شاعر زبان کو کیسے استعمال کرتا ہے تاکہ:','تحلیل کړي چې یو لیکوال/شاعر ژبه څنګه کاروي ترڅو:'),
('• appeal to the senses through use of figurative language including similes, metaphors and imagery','• تشبیہات، استعارات اور پیکر تراشی سمیت علامتی زبان کے ذریعے حواس سے اپیل کرے','• د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې په کارولو سره حواسو ته اپیل وکړي'),
('• set tone.','• لہجہ قائم کرے۔','• لهجه جوړه کړي.'),
('recognize and use varying intonation patterns as aids in spoken and written to highlight focus in meaning.','بولنے اور لکھنے میں معنی کے مرکز کو نمایاں کرنے کے لیے مدد کے طور پر مختلف لہجے کے نمونوں کو پہچانیں اور استعمال کریں۔','په خبرو او لیکنه کې د معنا د تمرکز د روښانه کولو لپاره د مرستې په توګه بېلابېل د غږ لوړ ټیټ بڼې وپېژني او وکاروي.'),
('use various reference sources to refine vocabulary for interpersonal academic workplace situation including figurative, idiomatic and technical vocabulary.','باہمی، تعلیمی اور کام کی جگہ کی صورتحال کے لیے مختلف حوالہ جاتی ذرائع استعمال کر کے ذخیرۂ الفاظ کو بہتر بنائیں، بشمول علامتی، محاوراتی اور تکنیکی الفاظ۔','د شخصي، علمي او کار ځای حالتونو لپاره د لغت د ښه کولو لپاره بېلابېل مرجع سرچینې وکاروي، په ګډون د مجازي، اصطلاحي او تخنیکي لغت.'),
('apply rules of capitalization wherever applicable.','جہاں قابلِ اطلاق ہو بڑے حروف (capitalization) کے قواعد لاگو کریں۔','چېرته چې پلي کېدونکي وي د لویو توریو (capitalization) قواعد پلي کړي.'),
('illustrate use of all punctuation marks wherever applicable.','جہاں قابلِ اطلاق ہو تمام رموزِ اوقاف کے استعمال کی مثال دیں۔','چېرته چې پلي کېدونکي وي د ټولو ټکو نښو کارول وښيي.'),
('use the pronunciation key to pronounce words with developing accuracy.','بڑھتی ہوئی درستگی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔','د وده کوونکې سموالي سره د کلمو د تلفظ لپاره د تلفظ کلیدي وکاروي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 196: Unit 21 opening page with the unit number, the title banner "The Road Not Taken", the poet tag "Robert Frost" and the learning outcomes with nested bullets (printed bullets "•" shown in the text of sub-items). "Not For Sale" is printed at the lower right beside the page number 196 (in a diamond). Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 206 (printed 197) ----------
s=page(206,'u21','197','The Road Not Taken (poem)','وہ راستہ جو نہیں چنا گیا (نظم)','هغه لار چې ونه ټاکل شوه (نظم)','poem')
F=Flow(s)
H(s,'t','The Road Not Taken','وہ راستہ جو نہیں چنا گیا','هغه لار چې ونه ټاکل شوه')
add(s,'s1','Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;','ایک زرد جنگل میں دو راستے الگ ہوئے،\nاور افسوس کہ میں دونوں پر سفر نہ کر سکا\nاور ایک مسافر ہوتے ہوئے، میں دیر تک کھڑا رہا\nاور ایک کو جہاں تک ہو سکا دیکھتا رہا\nجہاں وہ جھاڑیوں میں مڑ جاتا تھا؛','په یوه ژېړ ځنګل کې دوه لارې جلا شوې،\nاو افسوس چې زه دواړو باندې سفر نشم کولای\nاو یو مسافر وم، ډېر وخت ولاړ وم\nاو یوې ته مې تر هغه ځایه کتل چېرته چې وس مې و\nچېرته چې هغه په بوټو کې کوږېده؛',listType='poem')
add(s,'s2','Then took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,','بعد میں دوسرا لیا، جو اتنا ہی خوبصورت تھا،\nاور شاید زیادہ حق رکھتا تھا،\nکیونکہ وہ گھاس بھرا تھا اور استعمال کا منتظر تھا؛\nاگرچہ اس بارے میں وہاں سے گزرنے والوں نے\nدونوں کو واقعی تقریباً ایک جیسا گھسا دیا تھا،','بیا بل مې واخیست، چې هومره ښکلی و،\nاو ښايي ډېر حق یې درلود،\nځکه چې واښه‌ناک و او د کارونې انتظار یې کاوه؛\nکه څه هم د دې په اړه هلته تېرېدونکو\nدواړه رښتیا نږدې یو شان زړې کړي وې،',listType='poem')
add(s,'s3','And both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.','اور اس صبح دونوں برابر پڑے تھے\nایسے پتوں میں جنہیں کسی قدم نے کالا نہیں کیا تھا۔\nآہ، میں نے پہلا راستہ کسی اور دن کے لیے رکھ لیا!\nپھر بھی یہ جانتے ہوئے کہ راستہ راستے سے کیسے ملتا ہے،\nمجھے شک تھا کہ میں کبھی واپس آؤں گا۔','او هغه سهار دواړه برابر پراته وو\nپه داسې پاڼو کې چې هېڅ ګام تور نه و کړی.\nاوه، ما لومړۍ لار د بلې ورځې لپاره وساتله!\nبیا هم پوهېدو سره چې لار څنګه لارې ته رسېږي،\nما ته شک و چې ایا به هېڅکله بېرته راشم.',listType='poem')
add(s,'s4','I shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.','میں یہ بات آہ بھر کے بیان کروں گا\nکہیں برسوں اور برسوں بعد:\nایک جنگل میں دو راستے الگ ہوئے، اور میں—\nمیں نے وہ لیا جس پر کم لوگ چلے تھے،\nاور اسی نے سب فرق پیدا کر دیا۔','زه به دا په اوسوېلي سره ووایم\nځای ځای د پېړیو او پېړیو وروسته:\nپه یوه ځنګل کې دوه لارې جلا شوې، او زه—\nما هغه واخیستله چې لږ ورباندې تللي وو،\nاو هغې ټول توپیر رامنځته کړ.',listType='poem')
add(s,'by','Robert Frost','رابرٹ فراسٹ','رابرټ فراسټ')
add(s,'n','A black-and-white photograph of a forest path through bare trees lies across the lower part of the page; it is a photograph and is not reproduced.','صفحے کے نچلے حصے میں ننگے درختوں کے بیچ جنگل کے راستے کی سیاہ و سفید تصویر ہے؛ یہ تصویر نقل نہیں کی گئی۔','د پاڼې په ښکتنۍ برخه کې د لوڅو ونو ترمنځ د ځنګل د لارې توربسپین انځور دی؛ دا انځور نه دی رانقل شوی.')
F.done()
s['sourceNote']='Printed page 197: the poem "The Road Not Taken" by Robert Frost (1916; public domain, printed in full) in four stanzas, with the author line at the lower right. A black-and-white forest photograph runs along the foot of the page and is not reproduced. A binding strip at the foot is ignored. Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 197 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
