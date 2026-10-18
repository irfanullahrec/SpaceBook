from enghelp import *
c=cell
U='u18'
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def Op(s,key,en,ur,ps,ex,tab='grammar',**m): add(s,key,en,ur,ps,role='option',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
VEX='eng11-u18-vocab'; GEX='eng11-u18-grammar'
OPT={'until':('جب تک','تر څو'),'up to':('تک','پورې'),'unless':('جب تک کہ نہ','تر څو چې نه'),'there':('وہاں','هلته'),'where':('جہاں','چېرته'),'when':('جب','کله'),'as':('جیسے/جتنا','لکه/څومره'),'so':('اتنا/اس لیے','دومره/نو'),'than':('سے','له'),'As':('چونکہ','ځکه چې'),'So':('اس لیے','نو'),'Therefore':('لہٰذا','له همدې امله'),'that':('کہ','چې'),'such':('ایسا','داسې'),'If':('اگر','که'),'Whether':('خواہ','که'),'Though':('اگرچہ','که څه هم'),'Unless':('جب تک نہ','تر څو چې نه')}
# ---------- scan 171 (printed 162) ----------
s=page(171,U,'162','Writing · Oral · Vocabulary: nouns that are also verbs','لکھنا · زبانی · ذخیرۂ الفاظ: اسم جو افعال بھی ہیں','لیکل · شفاهي · لغت: اسمونه چې فعلونه هم دي','writing-oral-vocab')
F=Flow(s)
H(s,'wh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'ws','Write a summary of the poem ‘A Dream Within a Dream’.','نظم ‘خواب کے اندر خواب’ کا خلاصہ لکھیں۔','د نظم ‘په خوب کې خوب’ لنډیز ولیکئ.',tab='writing')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'ot','Divide the class into groups of ten and hold a group discussion on the saying “A dream you dream alone is only a dream. A dream you dream together is reality.”','کلاس کو دس دس کے گروپوں میں تقسیم کریں اور اس قول پر گروہی بحث کریں “جو خواب آپ اکیلے دیکھتے ہیں وہ صرف ایک خواب ہے۔ جو خواب آپ مل کر دیکھتے ہیں وہ حقیقت ہے۔”','ټولګی د لسو لسو په ډلو وويشئ او پر دې متل ډله‌ییز بحث وکړئ “هغه خوب چې تاسو یوازې ګورئ یوازې یو خوب دی. هغه خوب چې تاسو یوځای ګورئ حقیقت دی.”',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'vi','Look at the list of nouns in the box below. They are also verbs. Select the correct ones to fill the blanks. You may need to make some tense changes.','نیچے خانے میں اسموں کی فہرست دیکھیں۔ یہ افعال بھی ہیں۔ خالی جگہیں پُر کرنے کے لیے درست الفاظ چنیں۔ آپ کو کچھ زمانوں میں تبدیلی کرنی پڑ سکتی ہے۔','په لاندې بکس کې د اسمونو لیست وګورئ. دا فعلونه هم دي. تشې ډکولو لپاره سم کلمې وټاکئ. ښايي تاسو ته د ځینو زمانو بدلون ته اړتیا وي.',VEX,'vocabulary')
add(s,'vw','sand, beach, hand, picture, dog, clock, man, pen, chair, radio, father, coin','sand، beach، hand، picture، dog، clock، man، pen، chair، radio، father، coin','sand، beach، hand، picture، dog، clock، man، pen، chair، radio، father، coin',tab='vocabulary',sourceGap=dict(note='The twelve words are printed on pink strips in two rows of six: sand, beach, hand, picture, dog, clock / man, pen, chair, radio, father, coin.'))
VQ=[('Try and ______ what the house will be like once the builders have finished.','کوشش کریں اور ______ کہ جب مستری کام ختم کر لیں گے تو گھر کیسا ہوگا۔','هڅه وکړئ او ______ چې کله جوړوونکي پای ته ورسوي نو کور به څنګه وي.'),
('Mr. Nasir will ______ this meeting as our usual president is ill today.','جناب ناصر اس اجلاس کی ______ کریں گے کیونکہ ہمارے معمول کے صدر آج بیمار ہیں۔','ښاغلی ناصر به دا غونډه ______ کړي ځکه چې زموږ معمولي مشر نن ناروغ دی.'),
('Shakespeare is considered to be the writer who ______ more phrases than anyone else.','شیکسپیئر کو وہ ادیب سمجھا جاتا ہے جس نے کسی بھی دوسرے سے زیادہ فقرے ______۔','شکسپیر هغه لیکوال ګڼل کېږي چې له هر بل چا ډېرې جملې یې ______.'),
('Can you help me with these leaflets Abrar? I have to ______ one to every woman who is with a child.','ابرار، کیا آپ ان پمفلٹوں میں میری مدد کر سکتے ہیں؟ مجھے ہر اس عورت کو ایک ______ کرنا ہے جو بچے کے ساتھ ہے۔','ابرار، ایا تاسو دې پاڼو کې زما سره مرسته کولای شئ؟ ما باید هغې هرې ښځې ته یو ______ چې له ماشوم سره وي.'),
('This wall is too rough. We will have to ______ it down before we can paint it.','یہ دیوار بہت کھردری ہے۔ رنگ کرنے سے پہلے ہمیں اسے ______ کرنا پڑے گا۔','دا دېوال ډېر ناهموار دی. موږ باید مخکې تر دې چې رنګ یې کړو دا ______.'),
('The smugglers ______ their boat and unloaded the stolen goods into the waiting car.','سمگلروں نے اپنی کشتی ______ اور چوری شدہ سامان انتظار کرتی کار میں اتار دیا۔','قاچاقبرانو خپله کښتۍ ______ او غلا شوي توکي یې په منتظره موټر کې ښکته کړل.'),
('That student of mine has been ______ me with stupid questions all week. Why doesn’t he go and use the library?','میرا وہ طالب علم پورا ہفتہ مجھے بے وقوفانہ سوالات سے ______ رہا ہے۔ وہ لائبریری جا کر اسے استعمال کیوں نہیں کرتا؟','زما هغه زده کوونکی ټوله اونۍ ما د نادانه پوښتنو سره ______ دی. ولې لاړ نه شي او کتابتون ونه کاروي؟'),
('A male wolf can ______ up to 200 cubs in its lifetime.','ایک نر بھیڑیا اپنی زندگی میں 200 بچوں تک ______ سکتا ہے۔','یو نارینه لیوه کولای شي په خپل ژوند کې تر ۲۰۰ پورې ماشومان ______.'),
('The snow is getting really heavy now. I think we should ______ for help down in the valley.','برف اب واقعی بھاری ہو رہی ہے۔ میرا خیال ہے ہمیں وادی میں نیچے مدد کے لیے ______ چاہیے۔','واوره اوس رښتیا دروندېږي. زما فکر دی چې موږ باید په دره کې د مرستې لپاره ______.')]
for i,(a,b,d) in enumerate(VQ,1): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',VEX,'vocabulary')
F.done()
s['sourceNote']='Printed page 162. Pink banners "Writing Suggestions", "Oral Communication" and "Vocabulary and Grammar"; the vocabulary exercise has twelve word strips and nine sentences with blanks (items 10–12 continue on the next page). The right edge of the scan clips some line ends; the missing words are read from context. "Not For Sale" is printed at the lower right beside the page number 162 (in a diamond). Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 172 (printed 163) ----------
s=page(172,U,'163','Vocabulary (end) · Grammar: adverbial phrases (A, B)','ذخیرۂ الفاظ (اختتام) · قواعد: قیدی فقرے (الف، ب)','لغت (پای) · ګرامر: قیدي عبارتونه (الف، ب)','vocab-adverbial-phrase')
F=Flow(s)
VQ=[('Why don’t you ______ a letter to your father seeing as you have a spare twenty minutes.','آپ اپنے والد کو خط ______ کیوں نہیں لیتے جبکہ آپ کے پاس بیس منٹ فالتو ہیں۔','ولې تاسو خپل پلار ته یو لیک ______ نه کوئ چې تاسو شل دقیقې اضافي لرئ.'),
('Captain, how many men were ______ the lifeboats when the ship finally sank?','کپتان، جب جہاز آخرکار ڈوبا تو کتنے آدمی لائف بوٹس ______ تھے؟','کپتانه، کله چې کښتۍ په پای کې ډوبه شوه نو څو کسان ______ د ژغورنې کښتیو کې وو؟'),
('Sir, could you get out of your car please. We have just ______ you doing over 115 mph! Do you have an explanation?','جناب، براہِ کرم اپنی کار سے باہر آئیں۔ ہم نے ابھی ______ آپ 115 میل فی گھنٹہ سے زیادہ رفتار پر تھے! کیا آپ کے پاس کوئی وضاحت ہے؟','صاحبه، مهرباني وکړئ له خپل موټر نه راووځئ. موږ همدا اوس ______ چې تاسو له ۱۱۵ میلو په ساعت ډېر سرعت کاوه! ایا تاسو کومه تشریح لرئ؟')]
for i,(a,b,d) in enumerate(VQ,10): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',VEX,'vocabulary')
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
H(s,'gh','ADVERBS PHRASE','قیدی فقرے (ADVERBS PHRASE)','قیدي عبارتونه (ADVERBS PHRASE)',tab='grammar')
add(s,'g1','An adverbial phrase is a group of words that act together as an adverb, giving more information about a verb, adjective, or other adverb in a sentence. The adverbial phrase answers the same questions as a regular adverb: how/how much, when, or where.','قیدی فقرہ الفاظ کا ایسا گروہ ہے جو مل کر قید (adverb) کے طور پر کام کرتا ہے اور جملے میں کسی فعل، صفت یا دوسرے قید کے بارے میں مزید معلومات دیتا ہے۔ قیدی فقرہ انہی سوالات کا جواب دیتا ہے جن کا عام قید دیتا ہے: کیسے/کتنا، کب، یا کہاں۔','قیدي عبارت د کلمو یوه ډله ده چې یوځای د قید (adverb) په توګه کار کوي او په جمله کې د یو فعل، صفت یا بل قید په اړه نور معلومات ورکوي. قیدي عبارت هماغه پوښتنو ته ځواب ورکوي چې عادي قید یې ورکوي: څنګه/څومره، کله، یا چېرته.',tab='grammar')
Qn(s,'ga','A. Underline the adverbial phrase in each sentence.','الف. ہر جملے میں قیدی فقرے کے نیچے لکیر کھینچیں۔','الف. په هره جمله کې قیدي عبارت لاندې کرښه وکاږئ.',GEX,'grammar')
A=[('We hope the package will arrive within the hour.','ہمیں امید ہے کہ پیکج ایک گھنٹے کے اندر پہنچ جائے گا۔','موږ هیله لرو چې بسته به د یو ساعت په ترڅ کې ورسېږي.'),
('My sister reads books almost as quickly as you do.','میری بہن تقریباً اتنی ہی تیزی سے کتابیں پڑھتی ہے جتنی آپ۔','زما خور نږدې هومره ګړندۍ کتابونه لولي لکه ته.'),
('The news reports the metro will be closed for a week.','خبروں میں بتایا گیا ہے کہ میٹرو ایک ہفتے کے لیے بند رہے گی۔','خبرونه وايي چې میټرو به د یوې اونۍ لپاره بند وي.'),
('Your pen writes better than my pen does.','آپ کا قلم میرے قلم سے بہتر لکھتا ہے۔','ستاسو قلم له زما قلم ښه لیکي.'),
('Nawab takes the bus on Tuesdays.','نواب منگل کے دن بس لیتا ہے۔','نواب د سه‌شنبې په ورځو بس اخلي.'),
('Jamal and Maryam will arrive by train.','جمال اور مریم ٹرین سے پہنچیں گے۔','جمال او مریم به په اورګاډي ورسېږي.'),
('The dog digs under the fence.','کتا باڑ کے نیچے کھودتا ہے۔','سپی د کټار لاندې کیندي.'),
('Mom helps me with my homework more often than Dad does.','امی میرے ہوم ورک میں ابو کے مقابلے میں زیادہ اکثر مدد کرتی ہیں۔','مور ماته په کورنی کار کې تر پلار ډېر ځله مرسته کوي.'),
('Asma found her purse that afternoon.','اسماء کو اس دوپہر اپنا پرس مل گیا۔','اسماء په هغه غرمه خپل پرس وموند.'),
('We flew our kites on the big hill.','ہم نے بڑی پہاڑی پر اپنی پتنگیں اڑائیں۔','موږ په لوی غونډۍ خپل کایټونه الوتل.')]
for i,(a,b,d) in enumerate(A,1): Qn(s,f'a{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
Qn(s,'gb','B. Match each main clause with an adverbial phrase to create a sentence.','ب. ہر مرکزی جملے کو ایک قیدی فقرے کے ساتھ ملا کر جملہ بنائیں۔','ب. هر اصلي جمله له یو قیدي عبارت سره وصل کړئ ترڅو جمله جوړه شي.',GEX,'grammar')
s['tables']=[table('Adverbial phrases and main clauses','قیدی فقرے اور مرکزی جملے','قیدي عبارتونه او اصلي جملې',[c('ADVERBIAL PHRASES','قیدی فقرے','قیدي عبارتونه'),c('MAIN CLAUSES','مرکزی جملے','اصلي جملې')],[
[c('1. one bleak afternoon','1. ایک اداس دوپہر','۱. یوه تیاره غرمه'),c('The dog began barking.','کتا بھونکنے لگا۔','سپي غپېدل پیل کړل.')],
[c('2. not too far away','2. زیادہ دور نہیں','۲. ډېر لرې نه'),c('Sirens began to wail.','سائرن بجنے لگے۔','سایرنونو چیغې پیل کړې.')],
[c('3. all around the world','3. پوری دنیا میں','۳. په ټوله نړۍ کې'),c('Something odd was happening.','کچھ عجیب ہو رہا تھا۔','یو عجیب څه پېښېده.')],
[c('4. across the street','4. گلی کے پار','۴. د کوڅې بلې خوا'),c('Something sinister began to stir.','کوئی شریر چیز حرکت میں آنے لگی۔','یو بدنیته شی خوځېدل پیل کړل.')],
[c('5. without warning','5. بغیر کسی انتباہ کے','۵. پرته له خبرداری'),c('She began to speak in Russian.','وہ روسی میں بولنے لگی۔','هغې په روسي خبرې پیل کړې.')],
[c('6. far beneath the surface','6. سطح سے بہت نیچے','۶. له سطحې ډېر ښکته'),c('The boys began to play catch.','لڑکے کیچ کھیلنے لگے۔','هلکانو د نیولو لوبه پیل کړه.')]],tab='grammar')]
F.tb(0)
F.done()
s['sourceNote']='Printed page 163. The page begins with items 10–12 of the vocabulary exercise, followed by "GRAMMAR", the heading "ADVERBS PHRASE" (printed as shown), a definition paragraph, Part A (ten sentences with underline instructions) and Part B (a two-column box of six adverbial phrases and six main clauses to be matched; the phrases are numbered 1–6 and the clauses are unnumbered in print). Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 163 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 173 (printed 164) ----------
s=page(173,U,'164','Grammar: adverb clauses (C, D)','قواعد: قیدی جملے (ج، د)','ګرامر: قیدي جملې (ج، د)','adverb-clause-cd')
F=Flow(s)
H(s,'gh','Adverb Clause','قیدی جملہ (Adverb Clause)','قیدي جمله (Adverb Clause)',tab='grammar')
Qn(s,'gc','C. Find out the adverb clauses in the following sentences.','ج. درج ذیل جملوں میں قیدی جملے (adverb clauses) تلاش کریں۔','ج. په لاندې جملو کې قیدي جملې (adverb clauses) ومومئ.',GEX,'grammar')
C=[('Even if it rains, I will come.','چاہے بارش ہو، میں آؤں گا۔','حتی که باران وشي، زه به راشم.'),
('When you have finished your work, you may go home.','جب آپ اپنا کام ختم کر لیں تو آپ گھر جا سکتے ہیں۔','کله چې تاسو خپل کار پای ته ورسوئ نو کور ته تللای شئ.'),
('You can put it wherever you like.','آپ اسے جہاں چاہیں رکھ سکتے ہیں۔','تاسو کولای شئ دا چېرته چې خوښوئ کېږدئ.'),
('I did not buy that watch because it was expensive.','میں نے وہ گھڑی نہیں خریدی کیونکہ وہ مہنگی تھی۔','ما هغه ساعت ونه اخیست ځکه چې قیمتي و.'),
('You must go whether you hear from him or not.','آپ کو جانا ہوگا چاہے آپ کو اس کی طرف سے خبر ملے یا نہ ملے۔','تاسو باید ولاړ شئ که له هغه نه خبر مومئ یا نه.'),
('He spoke in such a low voice that few people could hear him.','وہ اتنی دھیمی آواز میں بولا کہ بہت کم لوگ اسے سن سکے۔','هغه په داسې ټیټ غږ خبرې وکړې چې لږ خلکو واورېدل.'),
('Since you have apologized, we will take no further action against you.','چونکہ آپ نے معذرت کر لی ہے، ہم آپ کے خلاف کوئی مزید کارروائی نہیں کریں گے۔','ځکه چې تاسو بخښنه غوښتې ده، موږ به ستاسو پر ضد نوره کومه کړنه ونه کړو.'),
('I have not been well since I returned from the hills.','جب سے میں پہاڑوں سے لوٹا ہوں میری طبیعت ٹھیک نہیں۔','له هغه وخته چې له غرونو راستون شوی یم ما ښه نه یم.'),
('He was so weak that he could not stand.','وہ اتنا کمزور تھا کہ کھڑا نہ ہو سکا۔','هغه دومره کمزورى و چې ودرېدلی نه شو.'),
('As he was not there, I spoke to his mother.','چونکہ وہ وہاں نہیں تھا، میں نے اس کی ماں سے بات کی۔','ځکه چې هغه هلته نه و، ما د هغه له مور سره خبرې وکړې.')]
for i,(a,b,d) in enumerate(C,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
Qn(s,'gd','D. Underline the adverb phrases in the following sentences and then use them in new sentences.','د. درج ذیل جملوں میں قیدی فقروں کے نیچے لکیر کھینچیں اور پھر انہیں نئے جملوں میں استعمال کریں۔','د. په لاندې جملو کې قیدي عبارتونو لاندې کرښه وکاږئ او بیا یې په نوو جملو کې وکاروئ.',GEX,'grammar')
D=[('She lives in a palatial home.','وہ ایک محل نما گھر میں رہتی ہے۔','هغه په یوه ماڼۍ غوندې کور کې اوسېږي.'),
('Is there water on the moon?','کیا چاند پر پانی ہے؟','ایا په سپوږمۍ اوبه شته؟'),
('She ran into her room.','وہ بھاگ کر اپنے کمرے میں گئی۔','هغې خپلې خونې ته منډه کړه.'),
('They chatted for a while.','انہوں نے تھوڑی دیر باتیں کیں۔','هغوی یوه شېبه خبرې وکړې.'),
('She performed the task with great skill.','اس نے کام بڑی مہارت سے انجام دیا۔','هغې کار په ډېره مهارت ترسره کړ.'),
('The desert stretched towards the north.','صحرا شمال کی طرف پھیلا ہوا تھا۔','صحرا د شمال لور ته غځېدلې وه.'),
('The gun went off with a loud noise.','بندوق بلند آواز کے ساتھ چل گئی۔','ټوپک په لوړ غږ سره وچاودېد.'),
('The fishers went sailing over the sea.','ماہی گیر سمندر پر کشتی رانی کو گئے۔','کب نیونکي په سمندر باندې د کښتۍ چلولو ته ولاړل.'),
('He lay beside the heap of corn.','وہ اناج کے ڈھیر کے پاس لیٹا تھا۔','هغه د غنمو د ډېرۍ ترڅنګ پروت و.'),
('She whispered in his ear.','اس نے اس کے کان میں سرگوشی کی۔','هغې د هغه په غوږ کې پچپچ وکړه.'),
('He fought with all his might.','وہ اپنی پوری طاقت سے لڑا۔','هغه په خپل ټول ځواک وجنګېد.'),
('He shouted at the top of his voice.','وہ پوری آواز سے چلایا۔','هغه په خپل ټول غږ چیغه کړه.'),
('It must be done at any cost.','یہ ہر قیمت پر کیا جانا چاہیے۔','دا باید په هره بیه ترسره شي.'),
('Much water has run under the bridge.','پل کے نیچے سے بہت پانی بہہ چکا ہے۔','د پله لاندې ډېرې اوبه بهېدلې دي.'),
('Without pausing to consider he struck the blow.','سوچنے کے لیے رکے بغیر اس نے وار کر دیا۔','پرته له دې چې د فکر لپاره ودرېږي هغه ګوزار وکړ.')]
for i,(a,b,d) in enumerate(D,1): Qn(s,f'd{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
F.done()
s['sourceNote']='Printed page 164. The sub-heading "Adverb Clause", Part C (ten sentences) and Part D (fifteen sentences; the words "use" in the instruction is printed in bold italics). "Not For Sale" is printed at the lower right beside the page number 164 (in a diamond). Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 174 (printed 165) ----------
s=page(174,U,'165','Grammar: adverb clauses (E, F)','قواعد: قیدی جملے (ہ، و)','ګرامر: قیدي جملې (ه، و)','adverb-clause-ef')
F=Flow(s)
Qn(s,'ge','E. Fill in the blanks with a suitable words provided under the sentence to make adverbial clauses.','ہ. جملے کے نیچے دیے گئے موزوں الفاظ سے خالی جگہیں پُر کریں تاکہ قیدی جملے (adverbial clauses) بن جائیں۔','ه. په جملې لاندې ورکړل شوو مناسبو کلمو سره تشې ډکې کړئ ترڅو قیدي جملې (adverbial clauses) جوړې شي.',GEX,'grammar')
E=[('I waited for my friend ______ he arrived.','میں نے اپنے دوست کا ______ وہ آیا انتظار کیا۔','ما د خپل ملګري انتظار ______ هغه راغی وکړ.',['until','up to','unless']),
('He hid ______ his pursuers could not find him.','وہ ______ اس کا تعاقب کرنے والے اسے نہ ڈھونڈ سکے چھپ گیا۔','هغه ______ د هغه تعقیبوونکي هغه ونه موند پټ شو.',['there','where','when']),
('I am as intelligent ______ you are.','میں اتنا ہی ذہین ہوں ______ آپ ہیں۔','زه همدومره هوښیار یم ______ تاسو یاست.',['as','so','than']),
('______ he was not there, I left a message with his mother.','______ وہ وہاں نہیں تھا، میں نے اس کی ماں کو پیغام دیا۔','______ هغه هلته نه و، ما د هغه مور ته پیغام پرېښود.',['As','So','Therefore']),
('We eat ______ we may live.','ہم ______ ہم زندہ رہ سکیں کھاتے ہیں۔','موږ ______ موږ ژوندي پاتې شو خورو.',['that','so','as']),
('She was ______ tired that she could barely stand.','وہ ______ تھکی ہوئی تھی کہ بمشکل کھڑی ہو سکتی تھی۔','هغه ______ ستړې وه چې په سختۍ یې ودرېدلای شوه.',['so','such','as']),
('______ you eat too much, you may fall ill.','______ آپ بہت زیادہ کھائیں تو بیمار ہو سکتے ہیں۔','______ تاسو ډېر وخورئ نو ښايي ناروغ شئ.',['If','Whether','Unless']),
('______ he started early, he finished late.','______ اس نے جلدی شروع کیا، اس نے دیر سے ختم کیا۔','______ هغه ژر پیل کړ، هغه ناوخته پای ته ورساوه.',['As','Though','So']),
('______ you do not tell me everything, I will not be able to help you.','______ آپ مجھے سب کچھ نہ بتائیں، میں آپ کی مدد نہیں کر سکوں گا۔','______ تاسو ماته هر څه ونه وایئ، زه به ستاسو سره مرسته ونشم کولای.',['If','Unless','Whether']),
('Do not go ______ I get ready.','______ میں تیار نہ ہو جاؤں مت جاؤ۔','______ زه چمتو نشم مه ځه.',['until','unless','up to'])]
for i,(a,b,d,os) in enumerate(E,1):
    Qn(s,f'e{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
    for j,o in enumerate(os): Op(s,f'e{i}o{j+1}',o,OPT[o][0]+' ('+o+')',OPT[o][1]+' ('+o+')',GEX)
Qn(s,'gf','F. Each of these proverbial sayings contains an adverb clause. Identify the adverb clause in each sentence.','و. ان ضرب المثلوں میں سے ہر ایک میں ایک قیدی جملہ (adverb clause) ہے۔ ہر جملے میں قیدی جملے کی شناخت کریں۔','و. له دې متلونو هر یو یو قیدي جمله (adverb clause) لري. په هره جمله کې قیدي جمله وپېژنئ.',GEX,'grammar')
Fq=[('While the cat’s away, the mice will play.','جب بلی نہیں ہوتی تو چوہے کھیلتے ہیں۔','کله چې پیشو نشته، موږکان لوبې کوي.'),
('A lie travels around the world while truth is putting her boots on.','جھوٹ دنیا کا چکر لگا لیتا ہے جب تک سچ اپنے جوتے پہن رہا ہوتا ہے۔','دروغ په ټوله نړۍ ګرځي تر څو چې رښتیا خپل بوټان اغوندي.'),
('If you don’t know where you are going, any road will get you there.','اگر آپ نہیں جانتے کہ کہاں جا رہے ہیں تو کوئی بھی سڑک آپ کو وہاں پہنچا دے گی۔','که تاسو نه پوهېږئ چې چېرته ځئ نو هره لار به تاسو هلته ورسوي.'),
('Memory is deceptive because it is colored by today’s events.','یادداشت فریب دہ ہے کیونکہ اس پر آج کے واقعات کا رنگ چڑھا ہوتا ہے۔','حافظه فریب‌ورکوونکې ده ځکه چې د نن د پېښو رنګ پرې ایښودل شوی.'),
('Never look down on anybody unless you’re helping him up.','کسی کو کبھی حقیر نہ سمجھیں سوائے اس کے کہ آپ اسے اٹھانے میں مدد کر رہے ہوں۔','هېڅوک هېڅکله مه سپکوئ پرته له دې چې تاسو ورسره د پاڅولو کې مرسته کوئ.'),
('You have to kiss a lot of toads before you find a handsome prince.','خوبصورت شہزادہ ملنے سے پہلے آپ کو بہت سے مینڈکوں کو چومنا پڑتا ہے۔','تاسو باید ډېر ګوډاګي ښکل کړئ مخکې تر دې چې یو ښکلی شهزاده ومومئ.'),
('Whenever you find yourself on the side of the majority, it is time to pause and reflect.','جب بھی آپ اپنے آپ کو اکثریت کی طرف پائیں تو رک کر غور کرنے کا وقت ہے۔','هر کله چې تاسو ځان د اکثریت په لوري ومومئ نو دا د درېدو او فکر کولو وخت دی.')]
for i,(a,b,d) in enumerate(Fq,1): Qn(s,f'f{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
F.done()
s['sourceNote']='Printed page 165. Part E has ten sentences, each followed by three word choices printed on a line below it (the Urdu and Pashto of each choice are translations by us with the English word in brackets), and Part F has seven proverbial sayings. The first line of the page ("E. Fill in the blanks with a suitable words provided…") is printed with that grammar. The right edge of the scan clips a few line ends. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 165 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
