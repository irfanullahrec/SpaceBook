from enghelp import *
c=cell
U='u13'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
# ---------- scan 131 (printed 122) ----------
s=page(131,U,'122','About the poet · Glossary · Reading Comprehension','شاعر کے بارے میں · فرہنگ · مطالعے کا فہم','د شاعر په اړه · لغتنامه · د لوست پوهه','poet-glossary-rc')
F=Flow(s)
H(s,'ah','About the poet:','شاعر کے بارے میں:','د شاعر په اړه:')
add(s,'ab','Percy Bysshe Shelley (4 August 1792 – 8 July 1822) is one of the major English Romantic poets, who is regarded by some as among the finest lyric and philosophical poets in the English language, and one of the most influential. The best known classic poems of Shelley include ‘Ode to the West Wind,’ ‘Ozymandias’, ‘To Skylark’, ‘The Cloud’, ‘The Mask of Anarchy’ and ‘Music When Soft Voices Die’.','پرسی بِش شیلی (4 اگست 1792 – 8 جولائی 1822) انگریزی رومانوی شاعروں میں سے ایک بڑے شاعر ہیں، جنہیں بعض لوگ انگریزی زبان کے بہترین غنائی اور فلسفیانہ شاعروں میں شمار کرتے ہیں اور سب سے زیادہ اثر انگیز شاعروں میں سے ایک سمجھتے ہیں۔ شیلی کی سب سے مشہور کلاسیکی نظموں میں ‘اوڈ ٹو دی ویسٹ ونڈ’، ‘اوزیمنڈیاس’، ‘ٹو اسکائی لارک’، ‘دی کلاؤڈ’، ‘دی ماسک آف انارکی’ اور ‘میوزک وین سافٹ وائسز ڈائی’ شامل ہیں۔','پرسي بیش شیلي (۴ اګست ۱۷۹۲ – ۸ جولای ۱۸۲۲) له انګلیسي رومانوي شاعرانو یو لوی شاعر دی، چې ځینې یې د انګلیسي ژبې له غوره غزلیزو او فلسفي شاعرانو شمېري او له تر ټولو اغېزناکو شاعرانو یو ګڼي. د شیلي تر ټولو مشهورې کلاسیکې نظمونه ‘د لویدیځ باد ته ستاینه’، ‘اوزیمنډیاس’، ‘د سکایلارک ته’، ‘ورېځ’، ‘د ګډوډۍ نقاب’ او ‘کله چې نرم غږونه مري موسیقي’ شامل دي.')
H(s,'gh','Glossary','فرہنگ','لغتنامه',tab='glossary')
G=[('antique','belonging to ancient times.','قدیم زمانوں سے تعلق رکھنے والا۔','د لرغونو وختونو پورې اړوند.','قدیم','لرغوني'),
('colossal Wreck','refers to the fallen statue of Ozymandias','اوزیمنڈیاس کے گرے ہوئے مجسمے کی طرف اشارہ ہے','د اوزیمنډیاس غورځېدلې مجسمې ته اشاره ده','عظیم کھنڈر','لوی کنډوالی'),
('Ozymandias','a Greek name for the Egyptian pharaoh Ramesses II.','مصری فرعون رعمسیس دوم کا یونانی نام۔','د مصري فرعون دوهم رعمسیس یوناني نوم.','اوزیمنڈیاس','اوزیمنډیاس'),
('shattered visage','the reference to the broken head of the sculpture','مجسمے کے ٹوٹے ہوئے سر کی طرف اشارہ','د مجسمې د ماتې شوې سر ته اشاره','ٹوٹا ہوا چہرہ','ماتې شوی مخ'),
('sneer','a contemptuous or mocking smile,','حقارت یا تمسخر بھری مسکراہٹ،','سپکاوی یا ملنډو ډک موسکا،','طنزیہ مسکراہٹ','ملنډې'),
('trunkless','lacking a body','جسم سے محروم','له بدن بې‌برخې','بے دھڑ','بې‌تنه')]
s['tables']=[table('Glossary','فرہنگ','لغتنامه',[c('Word','لفظ','کلمه'),c('Meaning','معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
F.tb(0)
for w,m,mu,mp,uw,pw in G: V[w]=dict(ur=uw,ps=pw)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u13-rc','exercise')
RQ=[('What is the theme of the poem ‘Ozymandias’.','نظم ‘اوزیمنڈیاس’ کا موضوع کیا ہے۔','د نظم ‘اوزیمنډیاس’ موضوع څه ده.'),
('Describe in your own words the anatomical conditions of the statue of king Ozymandias, as portrayed by Shelly.','شیلی کی پیش کردہ تصویر کے مطابق بادشاہ اوزیمنڈیاس کے مجسمے کی جسمانی حالت اپنے الفاظ میں بیان کریں۔','د شیلي لخوا انځور شوي د پاچا اوزیمنډیاس د مجسمې بدني حالت په خپلو الفاظو بیان کړئ.'),
('What is the tone of the poem ‘Ozymandias’?','نظم ‘اوزیمنڈیاس’ کا لہجہ کیا ہے؟','د نظم ‘اوزیمنډیاس’ لهجه څه ده؟'),
('Throughout the poem ‘Ozymandias’, Shelly uses alliteration. Give some examples and show what purpose do they serve?','نظم ‘اوزیمنڈیاس’ میں شیلی تکرارِ حروف (alliteration) استعمال کرتا ہے۔ کچھ مثالیں دیں اور بتائیں کہ وہ کیا مقصد پورا کرتی ہیں؟','د نظم ‘اوزیمنډیاس’ په اوږدو کې شیلي alliteration کاروي. څو بېلګې ورکړئ او وښیئ چې دوی کومه موخه پوره کوي؟'),
('Describe the rhyme scheme of the poem.','نظم کی قافیہ بندی بیان کریں۔','د نظم د قافیې ترتیب بیان کړئ.'),
('Describe the imagery of the poem ‘Ozymandias’. What sort of picture does it evoke? How much the imagery contributes to the tone of the poem?','نظم ‘اوزیمنڈیاس’ کی پیکر تراشی بیان کریں۔ یہ کس قسم کی تصویر ابھارتی ہے؟ پیکر تراشی نظم کے لہجے میں کتنا حصہ ڈالتی ہے؟','د نظم ‘اوزیمنډیاس’ انځورګري بیان کړئ. دا کوم ډول انځور راپورته کوي؟ انځورګري د نظم په لهجه کې څومره ونډه لري؟'),
('The inscribed lines on pedestal of the statue have ironic overtone. Explain the implied meaning of these words.','مجسمے کے چبوترے پر کندہ سطروں میں طنزیہ لہجہ ہے۔ ان الفاظ کے ضمنی معنی کی وضاحت کریں۔','د مجسمې پر چبوترې کښل شوې کرښې طنزیه لهجه لري. د دې الفاظو ضمني معنا تشریح کړئ.')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u13-rc','exercise')
F.done()
s['sourceNote']='Printed page 122. A bold-headed "About the poet:" paragraph (the textbook\'s own note) is followed by a pink "Glossary" banner and a table (Word / Meaning) of 6 rows, then a pink "Reading Comprehension" banner. The right edge of the scan clips a few line ends of the questions (e.g. "Give", "picture", "overtone."); the words are read from context. The printed text reads "Shelly" (for "Shelley") in the questions; kept as printed. The Urdu and Pashto columns of the glossary are added by us. Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 122 is printed in a diamond at the foot.'
s['vocabulary']=V
save(s)
# ---------- scan 132 (printed 123) ----------
V={}
s=page(132,U,'123','Writing Suggestions · Oral Communication · Vocabulary','لکھنے کی تجاویز · زبانی رابطہ · ذخیرۂ الفاظ','د لیکلو وړاندیزونه · شفاهي اړیکه · لغت','writing-oral-vocab')
F=Flow(s)
H(s,'wh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'ws','Write your considered views in one paragraph on the implications of these lines:','ایک پیراگراف میں ان سطروں کے مضمرات پر اپنی سوچی سمجھی رائے لکھیں:','په یو پاراګراف کې د دې کرښو د مضمراتو په اړه خپل سنجول شوي نظرونه ولیکئ:',tab='writing')
add(s,'wl','“My name is Ozymandias, King of Kings;\nLook on my Works, ye Mighty, and despair!\nNothing beside remains. Round the decay\nOf that colossal Wreck, boundless and bare\nThe lone and level sands stretch far away.”','“میرا نام اوزیمنڈیاس ہے، بادشاہوں کا بادشاہ؛\nمیرے کارنامے دیکھو، اے زورآورو، اور مایوس ہو جاؤ!\nاس کے سوا کچھ باقی نہیں۔ اس عظیم الجثہ کھنڈر کی\nبربادی کے گرد، بے کنار اور ننگی،\nتنہا اور ہموار ریت دور تک پھیلی ہے۔”','“زما نوم اوزیمنډیاس دی، د پاچاهانو پاچا؛\nزما کارنامې وګوره، ای زورورو، او نهیلی شه!\nپرته له دې هېڅ نه پاتې کېږي. د هغه لوی کنډوالې\nد ړنګېدو شاوخوا، بې‌پولې او لوڅې\nیوازینۍ او هواره شګې لرې ته غځېدلې دي.”',tab='writing',listType='poem')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'o1','Hold a debate on the topic, “The Glory of Artist Remains Longer Than the Grandeur and Glares of King”, as in the poem, the hand of artist mocks the works of king Ozymandias that has vanished in “boundless and bare, the lone and level sands stretch far away” .','موضوع “فنکار کی شان بادشاہ کی شان و شوکت اور چمک دمک سے زیادہ دیر باقی رہتی ہے” پر مباحثہ کریں، جیسا کہ نظم میں فنکار کا ہاتھ بادشاہ اوزیمنڈیاس کے کارناموں کا مذاق اڑاتا ہے جو “بے کنار اور ننگی، تنہا اور ہموار ریت دور تک پھیلی ہے” میں غائب ہو چکے ہیں۔','په موضوع “د هنرمند ویاړ د پاچا له شان او ځلا څخه ډېر پاتې کېږي” بحث وکړئ، لکه څنګه چې په نظم کې د هنرمند لاس د پاچا اوزیمنډیاس کارنامې ملنډې وهي چې په “بې‌پولې او لوڅې، یوازینۍ او هواره شګې لرې ته غځېدلې” کې ورکې شوې دي.',tab='language')
add(s,'o2','All students prepare both a pro and con position for a designated class session. During this class period two teams should be randomly selected who will then state their arguments in favour or against position. The other students will contribute differing remarks and suggestions for a more active and well-prepared class discussion.','تمام طلبہ مقررہ کلاس سیشن کے لیے حق اور مخالفت دونوں موقف تیار کریں۔ اس کلاس کے دوران دو ٹیمیں بے ترتیب منتخب کی جائیں جو پھر موقف کے حق یا خلاف اپنے دلائل پیش کریں۔ باقی طلبہ زیادہ فعال اور اچھی طرح تیار شدہ کلاس بحث کے لیے مختلف ریمارکس اور تجاویز پیش کریں گے۔','ټول زده کوونکي د ټاکل شوي ټولګي ناستې لپاره د ملاتړ او مخالفت دواړه دریځونه چمتو کړي. پدې ټولګي مهال دوه ټیمونه په تصادفي ډول وټاکل شي چې بیا به د دریځ په ګټه یا ضد خپل استدلالونه بیان کړي. نور زده کوونکي به د ډېر فعال او ښه چمتو شوي ټولګي بحث لپاره بېلابېل څرګندونې او وړاندیزونه وکړي.',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'vi','Fill in the blanks with one of the following words.','درج ذیل الفاظ میں سے ایک سے خالی جگہیں پُر کریں۔','تشې له لاندې کلمو څخه یوې سره ډکې کړئ.','eng11-u13-vocab','vocabulary')
add(s,'vw','everybody, everywhere, everything','everybody، everywhere، everything','everybody، everywhere، everything',tab='vocabulary',sourceGap=dict(note='The three words are printed on pink strips.'))
VQ=[('It’s the biggest shop in the city – they sell ______.','یہ شہر کی سب سے بڑی دکان ہے – وہ ______ بیچتے ہیں۔','دا په ښار کې تر ټولو لویه هټۍ ده – هغوی ______ پلوري.'),
('______ is hungry because it’s dinner time.','______ بھوکا ہے کیونکہ رات کے کھانے کا وقت ہے۔','______ وږی دی ځکه چې د ماښام د خوړو وخت دی.'),
('Do you have ______ you need for your holiday?','کیا آپ کے پاس ______ ہے جس کی آپ کو چھٹی کے لیے ضرورت ہے؟','ایا تاسو ______ لرئ چې د رخصتۍ لپاره ورته اړتیا لرئ؟'),
('The party was great. ______ enjoyed it.','پارٹی عمدہ تھی۔ ______ نے اس سے لطف اٹھایا۔','محفل عالي وه. ______ ورڅخه خوند واخیست.'),
('My brother knows ______ about football. He loves it.','میرا بھائی فٹ بال کے بارے میں ______ جانتا ہے۔ اسے اس سے محبت ہے۔','زما ورور د فوټبال په اړه ______ پوهېږي. هغه ورسره مینه لري.')]
for i,(a,b,d) in enumerate(VQ,1): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u13-vocab','vocabulary')
F.done()
s['sourceNote']='Printed page 123. Pink banners "Writing Suggestions", "Oral Communication" and "Vocabulary and Grammar". The writing prompt repeats the last five lines of the poem. A top-edge emblem strip and a reader\'s pencil mark are excluded. In the oral communication text the printed text has a space before the final full stop ("away” ."); kept as printed. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 123 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 133 (printed 124) ----------
s=page(133,U,'124','Vocabulary exercise (end) · Grammar: Future Progressive (A, B)','ذخیرۂ الفاظ کی مشق (اختتام) · قواعد: Future Progressive (الف، ب)','د لغت تمرین (پای) · ګرامر: Future Progressive (الف، ب)','vocab-future-progressive')
F=Flow(s)
VQ=[('The centre of Nathiagali is beautiful but there are tourists ______.','نتھیاگلی کا مرکز خوبصورت ہے لیکن ______ سیاح ہیں۔','د نتهیاګلي مرکز ښکلی دی خو ______ ګرځندوی شته.'),
('Islamabad a brilliant city, but ______ is quite expensive.','اسلام آباد ایک شاندار شہر، لیکن ______ کافی مہنگا ہے۔','اسلام‌آباد یو ښکلی ښار، خو ______ ډېر قیمتي دی.'),
('Their garden is full of flowers. There are roses and tulips ______.','ان کا باغ پھولوں سے بھرا ہے۔ ______ گلاب اور ٹیولپ ہیں۔','د هغوی باغ له ګلانو ډک دی. ______ ګلابونه او ټیولېپونه شته.'),
('I like my new job. The work is interesting and ______ is very friendly.','مجھے اپنی نئی نوکری پسند ہے۔ کام دلچسپ ہے اور ______ بہت دوستانہ ہے۔','زه خپله نوې دنده خوښوم. کار په زړه پورې دی او ______ ډېر دوستانه دی.'),
('I haven’t got a car. I travel ______ by public transport.','میرے پاس کار نہیں ہے۔ میں ______ پبلک ٹرانسپورٹ سے سفر کرتا ہوں۔','زما موټر نشته. زه ______ د عامه ترانسپورت په مټ سفر کوم.')]
for i,(a,b,d) in enumerate(VQ,6): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u13-vocab','vocabulary')
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
EX='eng11-u13-grammar'
Qn(s,'ga','A. Fill in the verbs in brackets in Future Progressive.','الف. قوسین میں دیے گئے افعال کو Future Progressive میں پُر کریں۔','الف. د قوس په منځ کې فعلونه په Future Progressive کې ډک کړئ.',EX,'grammar')
GA=[('Aayan ______ to the party on Saturday. (to come)','آیان ہفتے کو پارٹی میں ______۔ (to come)','آیان د شنبې په ورځ محفل ته ______. (to come)'),
('We ______ him tomorrow. (to meet)','ہم کل اس سے ______۔ (to meet)','موږ سبا هغه سره ______. (to meet)'),
('This time next week he ______ to Saudi Arabia. (to fly)','اگلے ہفتے اس وقت وہ سعودی عرب ______۔ (to fly)','بله اونۍ پدې وخت هغه سعودي عربستان ته ______. (to fly)'),
('At 6 o’clock on Friday they ______ the new song. (to sing)','جمعے کو چھ بجے وہ نیا گیت ______۔ (to sing)','د جمعې په شپږ بجو هغوی نوې سندره ______. (to sing)'),
('It ______ when I reach Murree. (to rain/probably)','جب میں مری پہنچوں گا تو ______۔ (to rain/probably)','کله چې زه مري ته ورسېږم نو ______. (to rain/probably)'),
('Tomorrow at nine I ______ a test. (to write)','کل نو بجے میں ایک ٹیسٹ ______۔ (to write)','سبا په نهو بجو زه یو ازموینه ______. (to write)'),
('Sania ______ a video when I arrive tonight. (to watch)','جب میں آج رات پہنچوں گا تو ثانیہ ایک ویڈیو ______۔ (to watch)','کله چې زه نن شپه ورسېږم نو ثانیه یو ویډیو ______. (to watch)'),
('You ______ pizza soon. (to eat)','آپ جلد پیزا ______۔ (to eat)','تاسو به ژر پیزا ______. (to eat)'),
('She ______ when you telephone her. (to sleep)','جب آپ اسے فون کریں گے تو وہ ______۔ (to sleep)','کله چې تاسو هغې ته زنګ وهئ نو هغه ______. (to sleep)'),
('They ______ in Medina just about now. (to arrive)','وہ بس اب مدینہ میں ______۔ (to arrive)','هغوی همدا اوس مدینې ته ______. (to arrive)')]
for i,(a,b,d) in enumerate(GA,1): Qn(s,f'a{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gb','B. Put the verbs in parenthesis into the correct form of Future Progressive.','ب. قوسین میں دیے گئے افعال کو Future Progressive کی درست شکل میں لکھیں۔','ب. د قوس په منځ کې فعلونه د Future Progressive په سمه بڼه کې ولیکئ.',EX,'grammar')
GB=[('At midnight we (sleep) ______','آدھی رات کو ہم (sleep) ______','د نیمې شپې موږ (sleep) ______'),
('This time next week we (sit) ______ at the beach.','اگلے ہفتے اس وقت ہم ساحل پر (sit) ______۔','بله اونۍ پدې وخت موږ په ساحل (sit) ______.'),
('At nine I (watch) ______ the news.','نو بجے میں خبریں (watch) ______۔','په نهو بجو زه خبرونه (watch) ______.'),
('Tonight we (cram up) ______ for our English test.','آج رات ہم اپنے انگریزی ٹیسٹ کے لیے (cram up) ______۔','نن شپه موږ د خپلې انګلیسي ازموینې لپاره (cram up) ______.'),
('They (dance) ______ all night.','وہ ساری رات (dance) ______۔','هغوی ټوله شپه (dance) ______.'),
('He (not / play) ______ all afternoon.','وہ ساری دوپہر (not / play) ______۔','هغه ټوله غرمه (not / play) ______.'),
('I (not / work) ______ all day.','میں سارا دن (not / work) ______۔','زه ټوله ورځ (not / work) ______.'),
('(eat / you) ______ at six?','کیا آپ چھ بجے (eat / you) ______؟','ایا تاسو په شپږ بجو (eat / you) ______؟'),
('(drive / she) ______ to London?','کیا وہ لندن (drive / she) ______؟','ایا هغه لندن ته (drive / she) ______؟'),
('(fight / they) ______ again?','کیا وہ پھر (fight / they) ______؟','ایا هغوی بیا (fight / they) ______؟')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
F.done()
s['sourceNote']='Printed page 124. The page begins with items 6–10 of the vocabulary exercise (the right edge clips the blank in items 6 and 8; the printed text reads "Islamabad a brilliant city" without "is"; kept as printed). Part A has ten sentences (item 7 ends with a stray "q" after "(to watch)"; not reproduced) and Part B ten items. "Not For Sale" is not printed on this page. Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 124 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 134 (printed 125) ----------
s=page(134,U,'125','Grammar: future tenses (C, D)','قواعد: مستقبل کے زمانے (ج، د)','ګرامر: راتلونکي زمانې (ج، د)','future-tenses-cd')
F=Flow(s)
Qn(s,'gc','C. Fill in the blanks using the verbs in parenthesis in the future tense.','ج. قوسین میں دیے گئے افعال کو مستقبل کے زمانے میں استعمال کرتے ہوئے خالی جگہیں پُر کریں۔','ج. د قوس په منځ کې فعلونه په راتلونکي زمان کې کاروو او تشې ډکې کړئ.',EX,'grammar')
GC=[('Zainab ______ to the party on Saturday. (to come)','زینب ہفتے کو پارٹی میں ______۔ (to come)','زینب د شنبې په ورځ محفل ته ______. (to come)'),
('We ______ him tomorrow. (to meet)','ہم کل اس سے ______۔ (to meet)','موږ سبا هغه سره ______. (to meet)'),
('This time next week he ______ to Dubai. (to fly)','اگلے ہفتے اس وقت وہ دبئی ______۔ (to fly)','بله اونۍ پدې وخت هغه دوبۍ ته ______. (to fly)'),
('At 6 o’clock on Saturday they ______ the new song. (to sing)','ہفتے کو چھ بجے وہ نیا گیت ______۔ (to sing)','د شنبې په شپږ بجو هغوی نوې سندره ______. (to sing)'),
('It ______ when I reach Naraan. (to rain/probably)','جب میں ناران پہنچوں گا تو ______۔ (to rain/probably)','کله چې زه ناران ته ورسېږم نو ______. (to rain/probably)'),
('Tomorrow at nine I ______ a test. (to write)','کل نو بجے میں ایک ٹیسٹ ______۔ (to write)','سبا په نهو بجو زه یو ازموینه ______. (to write)'),
('Sania ______ a video when I arrive tonight. (to watch)','جب میں آج رات پہنچوں گا تو ثانیہ ایک ویڈیو ______۔ (to watch)','کله چې زه نن شپه ورسېږم نو ثانیه یو ویډیو ______. (to watch)'),
('You ______ pizza soon. (to eat)','آپ جلد پیزا ______۔ (to eat)','تاسو به ژر پیزا ______. (to eat)'),
('She ______ when you telephone her. (to sleep)','جب آپ اسے فون کریں گے تو وہ ______۔ (to sleep)','کله چې تاسو هغې ته زنګ وهئ نو هغه ______. (to sleep)'),
('They ______ in Makka just about now. (to arrive)','وہ بس اب مکہ میں ______۔ (to arrive)','هغوی همدا اوس مکې ته ______. (to arrive)')]
for i,(a,b,d) in enumerate(GC,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
Qn(s,'gd','D. Fill in the correct future tense. (will future, going to or present simple)','د. درست مستقبل کا زمانہ پُر کریں۔ (will future، going to یا present simple)','د. سم راتلونکی زمانه ډکه کړئ. (will future، going to یا present simple)',EX,'grammar')
GD=[('The fridge is empty. ______ and get some food, please? (you go)','فریج خالی ہے۔ براہِ کرم ______ اور کچھ کھانا لے آئیں؟ (you go)','یخچال تش دی. مهرباني وکړئ ______ او څه خواړه راوړئ؟ (you go)'),
('We have decided that we ______ dinner at a restaurant tomorrow. (have)','ہم نے فیصلہ کیا ہے کہ ہم کل ریستوران میں رات کا کھانا ______۔ (have)','موږ پرېکړه کړې چې موږ سبا په رستورانت کې ماښام خوراک ______. (have)'),
('The weather report said that it ______ sunny tomorrow. (be)','موسم کی رپورٹ نے کہا کہ کل دھوپ ______۔ (be)','د هوا راپور ویلي چې سبا لمر ______. (be)'),
('Robina said that she ______ for him anymore. (not cook)','روبینہ نے کہا کہ وہ اب اس کے لیے ______۔ (not cook)','روبینې ویلي چې هغه نور د هغه لپاره ______. (not cook)'),
('Shakeel, ______ with us next Saturday? (you hike)','شکیل، کیا اگلے ہفتے ہمارے ساتھ ______؟ (you hike)','شکیله، ایا بله شنبه زموږ سره ______؟ (you hike)'),
('We have to hurry. The train ______ in five minutes. (leave)','ہمیں جلدی کرنی ہوگی۔ ٹرین پانچ منٹ میں ______۔ (leave)','موږ باید ګړندي شو. اورګاډی په پنځو دقیقو کې ______. (leave)'),
('They are hungry. I ______ some milk and cornflakes for breakfast. (get)','وہ بھوکے ہیں۔ میں ناشتے کے لیے کچھ دودھ اور کارن فلیکس ______۔ (get)','هغوی وږي دي. زه د ناشتې لپاره لږ شیدې او کارن فلیکس ______. (get)'),
('We ______ some money to his charity organization. (probably donate)','ہم اس کی خیراتی تنظیم کو کچھ رقم ______۔ (probably donate)','موږ د هغه خیریه سازمان ته لږ پیسې ______. (probably donate)'),
('I studied a lot for the exam. I ______ (not fail)','میں نے امتحان کے لیے بہت پڑھا۔ میں ______ (not fail)','ما د ازموینې لپاره ډېر لوستل. زه ______ (not fail)'),
('They announced that the shopping mall ______ on June 1st. (open)','انہوں نے اعلان کیا کہ شاپنگ مال یکم جون کو ______۔ (open)','هغوی اعلان وکړ چې شاپینګ مال د جون په لومړۍ ______. (open)'),
('It’s a beautiful day today. I think I ______ to the beach today. (go)','آج ایک خوبصورت دن ہے۔ میرا خیال ہے کہ میں آج ساحل پر ______۔ (go)','نن یوه ښکلې ورځ ده. زما فکر دی چې زه نن د ساحل ته ______. (go)'),
('He ______ us in English next year. (teach)','وہ اگلے سال ہمیں انگریزی ______۔ (teach)','هغه بل کال موږ ته انګلیسي ______. (teach)'),
('I feel very tired. I ______. (sleep)','میں بہت تھکا ہوا محسوس کر رہا ہوں۔ میں ______۔ (sleep)','زه ډېر ستړی احساسوم. زه ______. (sleep)'),
('I’m not sure if he ______ enough money to buy a new car next year. (have)','مجھے یقین نہیں کہ اگلے سال اس کے پاس نئی کار خریدنے کے لیے کافی رقم ______۔ (have)','زه ډاډه نه یم چې هغه به بل کال د نوي موټر اخیستو لپاره کافي پیسې ______. (have)'),
('The world championships ______ next Sunday. (end)','عالمی چیمپئن شپ اگلے اتوار کو ______۔ (end)','نړیوال اتلولي بله یکشنبه ______. (end)')]
for i,(a,b,d) in enumerate(GD,1): Qn(s,f'd{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',EX,'grammar')
F.done()
s['sourceNote']='Printed page 125. Part C repeats the sentences of Part A with changed names and places (Zainab, Dubai, Naraan, Makka); Part D has fifteen sentences. The left edge of the scan clips the first letters of the Part C heading. A phone-number strip and the watermark are excluded. Border lines and pink corner flags are excluded. The page number 125 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
