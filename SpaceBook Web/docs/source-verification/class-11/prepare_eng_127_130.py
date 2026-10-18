from enghelp import *
c=cell
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
EX='eng11-u12-grammar'
# ---------- scan 127 (printed 118) ----------
s=page(127,'u12','118','Grammar: gerund or infinitive (B)','قواعد: gerund یا infinitive (ب)','ګرامر: gerund یا infinitive (ب)','gerund-infinitive-b')
F=Flow(s)
Qn(s,'gb','B. Use the verbs in parenthesis either as gerund or the infinitive:','ب. قوسین میں دیے گئے افعال کو gerund یا infinitive کے طور پر استعمال کریں:','ب. د قوس په منځ کې ورکړل شوي فعلونه د gerund یا infinitive په توګه وکاروئ:',EX,'grammar')
GB=[('I couldn’t sleep so I tried (drink) some hot milk.','میں سو نہیں سکا تو میں نے کچھ گرم دودھ (drink) پینے کی کوشش کی۔','زه ویده نه شوم نو ما هڅه وکړه لږ ګرم شیدې (drink) وڅښم.'),
('She tried (reach) the book on the high shelf but she was too small.','اس نے اونچے شیلف پر رکھی کتاب تک (reach) پہنچنے کی کوشش کی لیکن وہ بہت چھوٹی تھی۔','هغې هڅه وکړه چې پر لوړ المارۍ کتاب ته (reach) ورسېږي خو هغه ډېره کوچنۍ وه.'),
('They tried (get) to the party on time but the bus was delayed.','انہوں نے وقت پر پارٹی میں (get) پہنچنے کی کوشش کی لیکن بس دیر سے آئی۔','هغوی هڅه وکړه چې په وخت محفل ته (get) ورسېږي خو بس ځنډېدلې وه.'),
('We tried (open) the window, but it was so hot outside, it didn’t help.','ہم نے کھڑکی (open) کھولنے کی کوشش کی، لیکن باہر اتنی گرمی تھی کہ اس سے کوئی فائدہ نہ ہوا۔','موږ هڅه وکړه چې کړکۍ (open) خلاصه کړو، خو بهر دومره ګرمي وه چې هېڅ ګټه یې ونه کړه.'),
('He tried (get) a job in a newspaper firm but they wouldn’t hire him.','اس نے ایک اخبار کی کمپنی میں نوکری (get) حاصل کرنے کی کوشش کی لیکن انہوں نے اسے ملازمت نہیں دی۔','هغه هڅه وکړه چې په یوه ورځپاڼې شرکت کې دنده (get) ومومي خو هغوی هغه نه استخدام کړ.'),
('He tried (get) a job in a newspaper firm but he still wasn’t satisfied.','اس نے ایک اخبار کی کمپنی میں نوکری (get) کر کے دیکھی لیکن وہ پھر بھی مطمئن نہ ہوا۔','هغه په یوه ورځپاڼې شرکت کې دنده (get) هڅه وکړه خو بیا هم قانع نه شو.'),
('You should stop (smoke), it’s not good for your health.','آپ کو (smoke) سگریٹ نوشی بند کر دینی چاہیے، یہ آپ کی صحت کے لیے اچھی نہیں۔','تاسو باید (smoke) سګرېټ څکول بند کړئ، دا ستاسو روغتیا ته ښه نه دي.'),
('We stopped (study) because we were tired.','ہم نے (study) پڑھنا بند کر دیا کیونکہ ہم تھک گئے تھے۔','موږ (study) زدکړه بنده کړه ځکه چې ستړي شوي وو.'),
('They will stop (have) lunch at twelve.','وہ بارہ بجے دوپہر کا کھانا (have) کھانے کے لیے رک جائیں گے۔','هغوی به په دولس بجو د غرمې خوراک (have) لپاره ودرېږي.'),
('We stopped (have) a rest because we were really sleepy.','ہم آرام (have) کرنے کے لیے رک گئے کیونکہ ہمیں واقعی نیند آ رہی تھی۔','موږ د آرام (have) لپاره ودرېدو ځکه چې موږ ته رښتیا خوب راتلو.'),
('Oh no! I forgot (buy) milk.','اوہ نہیں! میں دودھ (buy) خریدنا بھول گیا۔','اوه نه! زه شیدې (buy) اخیستل هېر کړل.'),
('Please don’t forget (pick up) some juice on your way home.','براہِ کرم گھر آتے ہوئے کچھ جوس (pick up) لے آنا نہ بھولیں۔','مهرباني وکړئ د کور په لاره کې لږ جوس (pick up) اخیستل مه هېروئ.'),
('I forget (lock) the door, but I’m sure I must have locked it.','مجھے دروازہ (lock) بند کرنا یاد نہیں، لیکن مجھے یقین ہے کہ میں نے اسے بند کیا ہوگا۔','زه د دروازې (lock) تړل نه یادوم، خو زه ډاډه یم چې ما به یې تړلی وي.'),
('Have we studied this before? I’ve forgotten (learn) it.','کیا ہم نے پہلے یہ پڑھا ہے؟ میں اسے (learn) سیکھنا بھول گیا ہوں۔','ایا موږ دا مخکې لوستلی؟ زه دا (learn) زده کول هېر کړي یم.'),
('Please remember (bring) your homework.','براہِ کرم اپنا ہوم ورک (bring) لانا یاد رکھیں۔','مهرباني وکړئ خپل کورنی کار (bring) راوړل یاد وساتئ.'),
('I remember (go) to the beach as a child.','مجھے بچپن میں ساحل پر (go) جانا یاد ہے۔','زه په ماشومتوب کې د ساحل ته (go) تګ یادوم.'),
('Finally I remembered (bring) your book! Here it is.','آخرکار مجھے آپ کی کتاب (bring) لانا یاد آ گیا! یہ لیں۔','په پای کې ما ستاسو کتاب (bring) راوړل یاد کړل! دا واخلئ.'),
('Do you remember (eat) steak in that little restaurant in Lahore?','کیا آپ کو لاہور کے اس چھوٹے ریستوران میں اسٹیک (eat) کھانا یاد ہے؟','ایا تاسو د لاهور په هغه کوچني رستورانت کې سټېک (eat) خوړل یادوئ؟'),
('I regret (tell) you the train has been delayed.','مجھے آپ کو یہ (tell) بتاتے ہوئے افسوس ہے کہ ٹرین تاخیر کا شکار ہے۔','زه په افسوس سره تاسو ته (tell) وایم چې اورګاډی ځنډېدلی دی.'),
('I regret (tell) Nighat my secret. Now she has told everyone.','مجھے نگہت کو اپنا راز (tell) بتانے پر افسوس ہے۔ اب اس نے سب کو بتا دیا ہے۔','زه په نګهت ته خپل راز (tell) ویلو پښېمانه یم. اوس هغې ټولو ته ویلي دي.')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
F.done()
s['sourceNote']='Printed page 118. Part B: twenty sentences, each with the verb to be used given in parentheses. Items 5 and 6 are printed with identical wording up to "…newspaper firm but"; kept as printed. Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 118 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 128 (printed 119) ----------
s=page(128,'u12','119','Grammar: gerund or infinitive (C, D) · Teacher\'s Guideline','قواعد: gerund یا infinitive (ج، د) · استاد کی رہنمائی','ګرامر: gerund یا infinitive (ج، د) · د ښوونکي لارښوونه','gerund-infinitive-cd')
F=Flow(s)
Qn(s,'gc','C. Replace the gerund by an infinitive and the infinitive by a gerund in the following sentences.','ج. درج ذیل جملوں میں gerund کو infinitive سے اور infinitive کو gerund سے بدلیں۔','ج. په لاندې جملو کې gerund په infinitive او infinitive په gerund بدل کړئ.',EX,'grammar')
GC=[('To laugh is better than to frown.','ہنسنا بھنویں چڑھانے سے بہتر ہے۔','خندل تر ترخه کتلو ښه دي.'),('Writing a story is not easy.','کہانی لکھنا آسان نہیں۔','کیسه لیکل اسانه نه دي.'),('He likes to collect books and does not like giving them away.','اسے کتابیں جمع کرنا پسند ہے اور انہیں دے دینا پسند نہیں۔','هغه کتابونه راټولول خوښوي او د هغو ورکول نه خوښوي.'),('Flying kites is a good sport, but to bet on them is bad.','پتنگ اڑانا ایک اچھا کھیل ہے، لیکن ان پر شرط لگانا برا ہے۔','کایټ الوتل یوه ښه لوبه ده، خو پر هغو شرط لګول بد دي.'),('He likes to read and to write.','اسے پڑھنا اور لکھنا پسند ہے۔','هغه لوستل او لیکل خوښوي.'),('She likes cooking and painting.','اسے کھانا پکانا اور مصوری پسند ہے۔','هغه پخلی او انځورګري خوښوي.'),('Seeing is believing.','دیکھنا یقین کرنا ہے۔','لیدل باور کول دي.'),('She loves making dolls.','اسے گڑیاں بنانا پسند ہے۔','هغه ګوډۍ جوړول خوښوي.'),('To wait for people who were late made him angry.','دیر سے آنے والے لوگوں کا انتظار کرنے نے اسے غصہ دلایا۔','د هغو خلکو انتظار کول چې ناوخته وو هغه غوسه کړ.'),('To sell insurance is a pretty boring job.','بیمہ بیچنا ایک خاصا بورنگ کام ہے۔','بیمه پلورل یو ډېر ستړی کوونکی کار دی.')]
for i,(a,b,d) in enumerate(GC,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gd','D. Decide whether the following sentences contain a Gerund or a Progressive.','د. فیصلہ کریں کہ درج ذیل جملوں میں Gerund ہے یا Progressive۔','د. پرېکړه وکړئ چې لاندې جملې Gerund لري که Progressive.',EX,'grammar')
GD=[('He likes reading books.','اسے کتابیں پڑھنا پسند ہے۔','هغه کتابونه لوستل خوښوي.'),('He is reading books.','وہ کتابیں پڑھ رہا ہے۔','هغه کتابونه لولي.'),('Reading books can be great fun.','کتابیں پڑھنا بہت مزے کا ہو سکتا ہے۔','کتابونه لوستل ډېر خوندور کېدای شي.'),('He is interested in reading books.','وہ کتابیں پڑھنے میں دلچسپی رکھتا ہے۔','هغه د کتابونو په لوستلو کې لیوالتیا لري.'),('He was reading books.','وہ کتابیں پڑھ رہا تھا۔','هغه کتابونه لوستل.'),('He has been reading books for two hours.','وہ دو گھنٹے سے کتابیں پڑھ رہا ہے۔','هغه دوه ساعته کتابونه لولي.'),('Instead of reading books Henry went to bed.','کتابیں پڑھنے کے بجائے ہنری سونے چلا گیا۔','د کتابونو د لوستلو پر ځای هنري ویده شو.'),('Do you like reading books?','کیا آپ کو کتابیں پڑھنا پسند ہے؟','ایا تاسو کتابونه لوستل خوښوئ؟'),('He had been reading books.','وہ کتابیں پڑھتا رہا تھا۔','هغه کتابونه لوستل.'),('His hobby is reading books.','اس کا شوق کتابیں پڑھنا ہے۔','د هغه شوق کتابونه لوستل دي.')]
for i,(a,b,d) in enumerate(GD,1): Qn(s,f'd{i}',f'{i}. {a} (Gerund/ Progressive)',f'{i}. {b} (Gerund / Progressive)',f'{i}. {d} (Gerund / Progressive)',EX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of gerund and gerund phrases.','طلبہ کو gerund اور gerund فقروں کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د gerund او gerund عبارتونو کارول تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 119. The left edge of the scan clips the first letters of the first lines ("C. Replace…"). Part C has ten sentences, Part D ten sentences each followed at the right by "(Gerund/ Progressive)", then the pink "Teacher\'s Guideline" banner. The upside-down header strip, border lines, pink corner flags, the watermark and the phone-number strip are excluded. The page number 119 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 129 (printed 120) ----------
s=page(129,'u13','120','Unit 13: Ozymandias · Learning outcomes','یونٹ 13: اوزیمنڈیاس · سیکھنے کے نتائج','واحد 13: اوزیمنډیاس · د زده کړې پایلې','unit13-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 13','یونٹ 13','واحد 13')
H(s,'title','Ozymandias','اوزیمنڈیاس','اوزیمنډیاس')
add(s,'au','Percy Bysshe Shelley','پرسی بِش شیلی','پرسي بیش شیلي')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('read a given poem and give orally and in writing:','دی گئی نظم پڑھیں اور زبانی اور تحریری طور پر دیں:','ورکړل شوې نظم ولولي او په شفاهي او لیکلي ډول ورکړي:'),
('• theme and its development.','• موضوع اور اس کی نشوونما۔','• موضوع او د هغې پرمختګ.'),
('• personal response with justification.','• جواز کے ساتھ ذاتی ردِعمل۔','• د توجیه سره شخصي غبرګون.'),
('recognize literary techniques such as personification and alliteration.','ادبی تکنیکوں مثلاً تشخیص (جان ڈالنا) اور تکرارِ حروف کو پہچانیں۔','ادبي تخنیکونه لکه شخصیت‌بخښنه او د توري تکرار وپېژني.'),
('analyze how a writer/ poet uses language to:','تجزیہ کریں کہ ایک مصنف/شاعر زبان کو کیسے استعمال کرتا ہے تاکہ:','تحلیل کړي چې یو لیکوال/شاعر ژبه څنګه کاروي ترڅو:'),
('• appeal to the senses through use of figurative language including similes, metaphors and imagery','• تشبیہات، استعارات اور پیکر تراشی سمیت علامتی زبان کے ذریعے حواس سے اپیل کرے','• د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې په کارولو سره حواسو ته اپیل وکړي'),
('• set tone','• لہجہ قائم کرے','• لهجه جوړه کړي'),
('use appropriate vocabulary and correct spelling in their own writing.','اپنی تحریر میں موزوں ذخیرۂ الفاظ اور درست املا استعمال کریں۔','په خپله لیکنه کې مناسب لغت او سمه املا وکاروي.'),
('identify, change the form of and use future continuous tenses.','future continuous زمانوں کی شناخت کریں، ان کی شکل بدلیں اور انہیں استعمال کریں۔','د future continuous زمانې وپېژني، بڼه یې بدله کړي او وکاروي.'),
('illustrate use of tenses.','زمانوں کے استعمال کی مثال دیں۔','د زمانو کارول وښيي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
add(s,'n','A black-and-white photograph of a toppled colossal stone statue (a large head lying in the sand beside two standing legs) fills the lower part of the page; it is a photograph and is not reproduced. A reader\'s blue pen scribble and an arrow above it are ignored.','صفحے کے نچلے حصے میں ایک گرے ہوئے عظیم الجثہ پتھر کے مجسمے (ریت میں پڑا بڑا سر اور دو کھڑی ٹانگیں) کی سیاہ و سفید تصویر ہے؛ یہ تصویر نقل نہیں کی گئی۔ قاری کی نیلی قلم کی لکیریں اور اوپر تیر نظر انداز کیے گئے ہیں۔','د پاڼې په ښکتنۍ برخه کې د یو غورځېدلي ستر ډبرین مجسمې (په شګو کې پروت لوی سر او دوه ولاړې پښې) توربسپین انځور دی؛ دا انځور نه دی رانقل شوی. د لوستونکي نیلي قلم کرښې او پورته غشی له پامه غورځول شوي.')
F.done()
s['sourceNote']='Printed page 120: Unit 13 opening page with the unit number, the title banner "Ozymandias", the poet tag "Percy Bysshe Shelley", the learning outcomes with nested bullets (printed bullets "•" shown in the text of sub-items) and a black-and-white photograph of a fallen colossal statue head, which is not reproduced. A blue scribble in the margin is ignored. Border lines, pink corner flags and the watermark are excluded. The page number 120 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 130 (printed 121) ----------
s=page(130,'u13','121','Ozymandias (poem)','اوزیمنڈیاس (نظم)','اوزیمنډیاس (نظم)','poem')
F=Flow(s)
H(s,'t','Ozymandias','اوزیمنڈیاس','اوزیمنډیاس')
add(s,'s1','I met a traveller from an antique land,\nWho said—“Two vast and trunkless legs of stone\nStand in the desert. . . . Near them, on the sand,\nHalf sunk a shattered visage lies, whose frown,\nAnd wrinkled lip, and sneer of cold command,\nTell that its sculptor well those passions read\nWhich yet survive, stamped on these lifeless things,\nThe hand that mocked them, and the heart that fed;','میں ایک قدیم سرزمین سے آئے ہوئے مسافر سے ملا،\nجس نے کہا—“پتھر کی دو وسیع بے دھڑ ٹانگیں\nصحرا میں کھڑی ہیں۔ . . . ان کے قریب، ریت پر،\nآدھا دھنسا ہوا ایک ٹوٹا ہوا چہرہ پڑا ہے، جس کی تیوری،\nشکن زدہ ہونٹ اور سرد حکم کی طنزیہ مسکراہٹ\nبتاتے ہیں کہ اس کے مجسمہ ساز نے ان جذبات کو خوب پڑھا\nجو ان بے جان چیزوں پر نقش ہو کر اب بھی باقی ہیں،\nوہ ہاتھ جس نے انہیں طنز کا نشانہ بنایا، اور وہ دل جس نے انہیں پالا؛','ما یو مسافر له یوې لرغونې خاورې سره ولید،\nچې ویې ویل—“د ډبرې دوه پراخې بې‌تنې پښې\nپه صحرا کې ولاړې دي. . . . د هغو ترڅنګ، په شګو،\nنیم ډوب شوی ماتې شوی مخ پروت دی، چې تندی یې،\nپړسېدلی شونډ او د سړې قومانده ملنډې\nوايي چې د هغه مجسمه‌جوړوونکي دا احساسات ښه لوستي\nچې لا هم پاتې دي، پر دې بې‌ژوندیو شیانو ټاپه شوي،\nهغه لاس چې هغوی ته یې ملنډې وهلې، او هغه زړه چې ځواب یې ورکاوه؛',listType='poem')
add(s,'s2','And on the pedestal, these words appear:\nMy name is Ozymandias, King of Kings;\nLook on my Works, ye Mighty, and despair!\nNothing beside remains. Round the decay\nOf that colossal Wreck, boundless and bare\nThe lone and level sands stretch far away.”','اور چبوترے پر یہ الفاظ دکھائی دیتے ہیں:\nمیرا نام اوزیمنڈیاس ہے، بادشاہوں کا بادشاہ؛\nمیرے کارنامے دیکھو، اے زورآورو، اور مایوس ہو جاؤ!\nاس کے سوا کچھ باقی نہیں۔ اس عظیم الجثہ کھنڈر کی\nبربادی کے گرد، بے کنار اور ننگی،\nتنہا اور ہموار ریت دور تک پھیلی ہے۔”','او پر خوځنده دا کلمې ښکاري:\nزما نوم اوزیمنډیاس دی، د پاچاهانو پاچا؛\nزما کارنامې وګوره، ای زورورو، او نهیلی شه!\nپرته له دې هېڅ نه پاتې کېږي. د هغه لوی کنډوالې\nد ړنګېدو شاوخوا، بې‌پولې او لوڅې\nیوازینۍ او هواره شګې لرې ته غځېدلې دي.”',listType='poem')
add(s,'by','Percy Bysshe Shelley','پرسی بِش شیلی','پرسي بیش شیلي')
F.done()
s['sourceNote']='Printed page 121: the sonnet "Ozymandias" by Percy Bysshe Shelley (1818; public domain, printed in full) shown as an octave and a sestet with a blank line between; the quotation of the traveller opens in the first line of the octave and closes at the end of the sestet (the closing mark is printed after "away."). The author line is printed at the lower right. Reader underlines under many words are ignored. Border lines, pink corner flags, the watermark and the phone-number strip are excluded. The page number 121 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
