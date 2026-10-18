from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='p10',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def D(s,lab,t,e,p): add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Comic one-act play in colloquial Urdu; translations are free renderings.'
def run(s,items):
    for it in items:
        if it[0] is None: P(s,it[1],it[2],it[3])
        else: D(s,*it)
# scan 87 = printed 80
s=page(87,'p10','80','Taleem-e-Balighan, part 9','تعلیمِ بالغاں (حصہ نہم)','د لویانو زده‌کړه (نهمه برخه)','l9')
F=Flow(s)
run(s,[(None,'ایک بلاک بورڈ (بلیک بورڈ) ……… ایک لکڑی کا صندوق ………','……… a block-board (blackboard) … a wooden box …','……… یو بلاک بورډ (بلیک بورډ) ……… یو لرګینی صندوق ………'),
('قصاب','(لکھتے ہوئے) ایک لکڑی کا صندوق۔','Butcher: (writing) a wooden box.','قصاب: (لیکلو سره) یو لرګینی صندوق.'),
('مولوی','(جھک کر قصائی کی تحریر کو پڑھ کر) او ہو ہو ہو۔ قابلیت دیکھ رہے ہیں۔ صندوق صواد سے لکھ رہے ہیں صاحبزادے (ڈنڈا مارتا ہے)','Maulvi: (bending over and reading the butcher’s writing) Oh ho ho ho! See the ability! He is writing “sandooq” with “swad”, young man. (strikes with the stick)','مولوي: (ټیټېدو سره د قصاب لیکنه لوستلو سره) او هو هو هو. لیاقت وګورئ. صندوق په صواد لیکي صاحبزاده (لښته ورکوي)'),
('قصاب','(بگڑ کر) صندوق صواد سے ہے مولوی صاحب۔','Butcher: (getting angry) “Sandooq” is with “swad”, Maulvi Sahib.','قصاب: (غصه کېدو سره) صندوق په صواد دی مولوي صاحب.'),
('مولوی','صواد سے ہے؟','Maulvi: With “swad”?','مولوي: په صواد دی؟'),
('دونوں','صواد سے ہے۔','Both: It is with “swad”.','دواړه: په صواد دی.'),
('مولوی','ارے وہ ساگوان کا ہے نا۔ میں بھی ہمیشہ سے یہی غلطی کرتا آیا تھا۔ خدا سلامت رکھے۔ ایک دن انسپکٹر آف اسکول معائنے کے لیے تشریف لائے تو انہوں نے میری یہ غلطی دُرست کی۔','Maulvi: Oh, that is of teak, isn’t it. I too had been making this same mistake all along. May God keep him safe: one day the Inspector of Schools came for inspection and corrected this mistake of mine.','مولوي: ای هغه د ساګوان دی نه. ما هم تل همدا غلطي کوله. خدای دې ساتي. یوه ورځ د ښوونځیو انسپکټر د معاینې لپاره راغی نو هغه زما دا غلطي سمه کړه.'),
('قصاب','(حیران ہو کر) کونسی غلطی؟','Butcher: (astonished) Which mistake?','قصاب: (حیرانېدو سره) کومه غلطي؟'),
('مولوی','یہی کہ ساگوان کا صندوق «س» سے لکھنا چاہیے۔','Maulvi: Just this: that the teak box should be written with “seen”.','مولوي: همدا چې د ساګوان صندوق په «س» لیکل پکار دي.'),
('حجام','(مضحکہ اڑاتے ہوئے) ہوں۔ ساگوان کا صندوق «س» سے اور شیشم کا شی ………','Barber: (mocking) Hmm. A teak box with “seen” and a sheesham one with “shee” …','حجام: (ملنډې وهلو سره) هو. د ساګوان صندوق په «س» او د شیشمو …'),
(None,'(جملہ پورا نہیں ہو پاتا کہ مولوی صاحب کا ڈنڈا پڑ جاتا ہے)','(The sentence is not completed when Maulvi Sahib’s stick falls.)','(جمله بشپړه نه شي چې د مولوي صاحب لښته پرېوځي)'),
('مولوی','کیوں؟ شیشم کا شین سے نہیں ہو سکتا؟ ارے جو انسپکٹر صاحب چاہے وہی ہو سکتا ہے سمجھا؟','Maulvi: Why? Can’t the sheesham one be with “sheen”? Hey, whatever the Inspector Sahib wants is what can be; understood?','مولوي: ولې؟ د شیشمو په شین نه شي کېدای؟ ای هغه څه چې انسپکټر صاحب غواړي همدا کېدای شي، پوه شوې؟'),
('قصاب','(چوٹ پر تڑپ کر) ہو سکتا ہے۔ ہو سکتا ہے۔','Butcher: (writhing at the blow) It can be, it can be.','قصاب: (په ټکر تېزېدو سره) کېدای شي. کېدای شي.'),
('قصاب','(توجہ دلانے کے لیے لکھتے ہوئے) ایک لکڑی کا «س» سے صندوق ………','Butcher: (writing to draw attention) a wooden box with “seen” …','قصاب: (پام راړولو لپاره لیکلو سره) یو لرګینی په «س» صندوق ………'),
('مولوی','و نیز۔','Maulvi: and also.','مولوي: او همدارنګه.'),
('قصاب','انیس۔','Butcher: Anees.','قصاب: انیس.'),
('مولوی','ارے انیس نہیں بابا۔ و۔ نیز۔ (پہلے منھ کھول کر کرتے ہیں پھر جبڑے پھیلا کر)','Maulvi: Hey, not “Anees”, baba! “Wa… neez”. (first opening his mouth, then stretching his jaws)','مولوي: ای انیس نه بابا. او. همدارنګه. (لومړی خوله خلاصه کولو سره بیا ژامې غوړولو سره)'),
('حجام','(نقل کرتے ہوئے) و ……… نیز۔','Barber: (imitating) wa… neez.','حجام: (نقل کولو سره) او ……… همدارنګه.'),
('مولوی','ہاں شاباش۔ دیکھ حجام کو عقل ہے تیرے کو نہیں ہے۔','Maulvi: Yes, bravo! See, the barber has sense, you have none.','مولوي: هو شاباش. وګوره حجام ته عقل دی ستا ته نشته.')])
F.done()
s['sourceNote']='Printed page 80 (scan 87): continuation of the comic play (speaker labels in blue). The jokes about spelling “sandooq” with swad/seen and “neez/Anees” are as printed; the first line continues the dictation from the previous page.'+NOTE
s['vocabulary']={}
save(s)
# scan 88 = printed 81
s=page(88,'p10','81','Taleem-e-Balighan, part 10','تعلیمِ بالغاں (حصہ دہم)','د لویانو زده‌کړه (لسمه برخه)','l10')
F=Flow(s)
run(s,[('قصاب','(لکھتے ہوئے) و نیز۔','Butcher: (writing) and also.','قصاب: (لیکلو سره) او همدارنګه.'),
('مولوی','(لکھاتے ہوئے) تین گھڑے ……… مستی اتحاد ……… تنظیم ……… اور یقینِ محکم عطا کیے گئے تھے ……… (اٹھ کر گھڑوں کی طرف جاتے ہیں) سو مدرسے کے ناہنجار طالب علموں نے ……… آپس میں لڑ جھگڑ کر ……… اتحاد کے ٹکڑے ٹکڑے کر دیے ہیں۔ (ٹوٹا ہوا گھڑا اٹھا کر دکھاتے ہیں جس پر چاک سے «اتحاد» لکھا ہے)','Maulvi: (dictating) three pitchers … drunk with unity … discipline … and firm faith were granted … (getting up and going towards the pitchers) so the disgraceful students of the madrasa … by quarrelling among themselves … have broken Unity into pieces. (He picks up a broken pitcher and shows it, on which “Ittehad” is written in chalk.)','مولوي: (لیکلو سره) درې ګیډۍ ……… مستي اتحاد ……… تنظیم ……… او یقین محکم ورکړل شوي وو ……… (پاڅېدو سره ګیډیو لور ته ځي) نو د مدرسې ناهنجارو زده‌کوونکو ……… یو له بل سره جګړې کولو سره ……… د اتحاد ټوټې ټوټې کړې دي. (ماته ګیډۍ پورته کوي او ښیي چې پر هغې په چاک «اتحاد» لیکل شوی دی)'),
('قصاب','مولوی صاحب۔ یہ اتحاد کے ٹکڑے ٹکڑے کس نے کیے مولوی صاحب۔','Butcher: Maulvi Sahib, who broke this Unity into pieces, Maulvi Sahib?','قصاب: مولوي صاحب. دا د اتحاد ټوټې ټوټې چا کړې مولوي صاحب.'),
('مولوی','ہاں میں۔ خود ہی تو ڈر کے پوچھ بھی رہا ہے۔ ارے تُو گروِمندر کا تو نہیں ہے؟','Maulvi: Yes, I. You are afraid and still asking. Hey, are you not of the Guru-mandir (a rebel)?','مولوي: هو زه. پخپله ویرېدو سره پوښتنه هم کوې. ای ته د ګرو مندر خو نه یې؟'),
('قصاب','(فخر سے سینے پر ہاتھ مار کر) اجی میں تو بانس بریلی کا ہوں۔ بانس ریلی کا۔','Butcher: (proudly striking his chest) Sir, I am from Bans Bareilly. Bans Rely.','قصاب: (په ویار پر سینه لاس ټکولو سره) ای زه خو د بانس بریلي یم. بانس ریلي.'),
('مولوی','(چڑانے کے انداز میں نقل کرتے ہوئے) اجی میں تو بانس بریلی کا ہوں، بانس بریلی کا۔ کھاتے پاکستان کا۔ گاتے بانس بریلی کا۔ آج جس کو دیکھو کوئی سندھی ہے، کوئی پنجابی ہے، کوئی بلوچی ہے، کوئی پٹھان ہے۔ ہر شخص اپنی ڈیڑھ اینٹ کی مسجد الگ بنا رہا ہے اور لائق شاگرد پوچھ رہے ہیں کہ اتحاد کے ٹکڑے ٹکڑے کس نے کیے، مولوی صاحب؟ ارے ٹکڑے ٹکڑے، تو تمھارے ہونے تھے کم بختو۔','Maulvi: (mimicking him to tease) “Sir, I am from Bans Bareilly, from Bans Bareilly.” You eat Pakistan’s bread and sing of Bans Bareilly. Today whomever you look at is a Sindhi, a Punjabi, a Baloch, a Pathan. Everyone is building his own separate one-and-a-half-brick mosque, and able pupils ask who broke Unity into pieces, Maulvi Sahib? Hey, it was you who were to be torn to pieces, wretches!','مولوي: (چېړلو په انداز نقل کولو سره) ای زه خو د بانس بریلي یم، بانس بریلي. د پاکستان ډوډۍ خورئ. د بانس بریلي سندرې وایئ. نن چې چا ته وګورې څوک سندهي دی، څوک پنجابي دی، څوک بلوڅ دی، څوک پښتون دی. هر څوک خپل ډیرۍ خښته جومات جلا جوړوي او لایق شاګردان پوښتي چې د اتحاد ټوټې ټوټې چا کړې مولوي صاحب؟ ای ټوټې ټوټې خو ستاسو کېدل پکار وو بدبختانو.'),
('قصاب','(شرمندہ ہو کر لکھنے لگتا ہے) اتحاد کے ٹکڑے ٹکڑے کر دیے ہیں۔','Butcher: (embarrassed, begins writing) have broken Unity into pieces.','قصاب: (شرمېدو سره لیکل پیل کوي) د اتحاد ټوټې ټوټې کړې دي.'),
('مولوی','(دوسرا گھڑا اُٹھاتا ہے جس پر «تنظیم» لکھا ہے) تنظیم کا گلا غائب اور پیندے میں سوراخ ہو گیا ہے۔ (گھڑے کا گلا اور پیندا دکھاتے ہوئے)','Maulvi: (picks up the second pitcher on which “Tanzeem” is written) The neck of Discipline is missing and the bottom has a hole. (showing the neck and bottom of the pitcher)','مولوي: (دویمه ګیډۍ پورته کوي چې پر هغې «تنظیم» لیکل شوی دی) د تنظیم ستونی ورک او په لاندې کې سوری شوی دی. (د ګیډۍ ستونی او لاندې ښودلو سره)'),
(None,'(اس عرصے میں حجام بیڑی جلا کر پینے لگتا ہے)','(Meanwhile the barber lights a beedi and begins to smoke.)','(پدې موده کې حجام بېډۍ بلوي او څکول پیل کوي)'),
('حجام','(بیڑی پیتے ہوئے) خیر یہ اتحاد کے تو ٹکڑے ٹکڑے ہو گئے تھے۔ پر یہ تنظیم کا گلاس کس نے غائب کیا مولوی صاحب؟','Barber: (smoking a beedi) Well, Unity had been broken to pieces. But who made the glass of Discipline disappear, Maulvi Sahib?','حجام: (بېډۍ څکولو سره) ښه دا اتحاد خو ټوټې ټوټې شوی و. خو د تنظیم ګیلاس چا ورک کړ مولوي صاحب؟'),
('مولوی','(بیڑی پیتے دیکھ کر) ہائیں۔ مدرسے میں بیٹھ کر بیڑی پی رہا ہے۔ بجھا بیڑی۔ بجھا (حجام بیڑی والا ہاتھ پیچھے کر لیتا ہے اور پیٹھ مولوی صاحب کی طرف)','Maulvi: (seeing him smoke a beedi) What! Sitting in the madrasa he is smoking a beedi! Put out the beedi! Put it out! (The barber puts the beedi hand behind him and turns his back to Maulvi Sahib.)','مولوي: (بېډۍ څکول لیدلو سره) څه! په مدرسه کې ناست بېډۍ څکي. بېډۍ مړه کړه. مړه کړه (حجام د بېډۍ لاس شا ته کوي او شا مولوي صاحب لور ته)')])
F.done()
s['sourceNote']='Printed page 81 (scan 88): continuation of the comic play (speaker labels in blue). The speeches about “Unity” (اتحاد), “Discipline” (تنظیم) and the pitchers refer to the stage property described in the scene; “گرومندر”, “بانس بریلی” and “ڈیڑھ اینٹ کی مسجد” are as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 89 = printed 82
s=page(89,'p10','82','Taleem-e-Balighan, end; Exercise (Mashq): questions 1–2','تعلیمِ بالغاں کا اختتام؛ مشق: سوال 1 اور 2','د لویانو د زده‌کړې پای؛ تمرین: ۱ او ۲ پوښتنې','l11')
F=Flow(s)
run(s,[('مولوی','او ہو ہو۔ ادب ہو رہا ہے۔ مولوی صاحب سے بیڑی چھپا رہے ہیں۔ (ہاتھ سے بیڑی چھین کر) آج شاگرد مدرسے میں بیٹھ کر بیڑی پیتے ہیں، چپڑاسی افسروں سے ماچس مانگتے ہیں، افسر رشوت لیتے ہیں۔ لیڈر قوم کو دھوکا دیتے ہیں اور لائق شاگرد پوچھتے ہیں «یہ تنظیم کا گلاس کس نے غائب کیا مولوی صاحب»؟ ارے گلاس تو تمھارے غائب ہونے تھے کم بختو۔','Maulvi: Oh ho ho! You are showing respect! Hiding a beedi from Maulvi Sahib! (snatching the beedi from his hand) Today pupils sit in the madrasa and smoke beedis, peons ask officers for matches, officers take bribes, leaders deceive the nation, and able pupils ask, “Who made the glass of Discipline disappear, Maulvi Sahib?” Hey, it was you who were to disappear, wretches!','مولوي: او هو هو. ادب کېږي. له مولوي صاحب نه بېډۍ پټوي. (په لاس بېډۍ ایستلو سره) نن شاګردان په مدرسه کې ناست بېډۍ څکي، چپراسي له افسرانو نه ماچس غواړي، افسران رشوت اخلي. مشران قوم ته درغلي کوي او لایق شاګردان پوښتي «د تنظیم ګیلاس چا ورک کړ مولوي صاحب»؟ ای ګیلاس خو ستاسو ورک کېدل پکار وو بدبختانو.')])
P(s,'(لکھواتے ہوئے) لے دے کے ……… ایک یقینِ محکم رہ گیا ہے ……… جس پہ کام چالو ہے ……… اگر ……… اتحاد اور تنظیم سے ……… اب بھی سبق نہ لیا گیا ……… تو یہ قوم ……… یقینِ محکم کا بھی ……… وہی حشر کر دے گی۔','(dictating) Taking it all together … only Firm Faith is left … on which the work is going on … if … from Unity and Discipline … a lesson is still not taken … then this nation … will make … the same end of Firm Faith too.','(لیکلو سره) په ټوله کې ……… یوازې یقین محکم پاتې دی ……… چې پر هغه کار روان دی ……… که ……… له اتحاد او تنظیم نه ……… اوس هم عبرت نه وي اخیستل شوی ……… نو دا قوم ……… د یقین محکم هم ……… همغه پای به وکړي.',boxed=True)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ مندرجہ ذیل سوالوں کے مختصر جوابات لکھیں۔','1. Write short answers to the following questions.','۱. د لاندې پوښتنو لنډ ځوابونه ولیکئ.')
for t in [('الف) مولوی صاحب قرض کیوں واپس نہ کر سکے؟','(a) Why could Maulvi Sahib not return the loan?','(الف) مولوي صاحب پور ولې بېرته نشو کړای؟'),
('ب) مولوی صاحب نے اتحاد کے ٹکڑے ہونے کی کیا وجوہات بتائیں؟','(b) What reasons did Maulvi Sahib give for Unity being broken into pieces?','(ب) مولوي صاحب د اتحاد د ټوټې کېدو کوم لاملونه وښودل؟'),
('ج) مدرسۂ تعلیمِ بالغاں کہاں واقع تھا؟','(c) Where was the Madrasa Taleem-e-Balighan situated?','(ج) د لویانو د زده‌کړې مدرسه چېرته موقعیت درلود؟'),
('د) اس اقتباس میں وزیروں پر کیا طنز کیا گیا ہے؟','(d) What satire has been made on ministers in this passage?','(د) پدې اقتباس کې په وزیرانو کوم طنز شوی دی؟'),
('ہ) مولوی صاحب کس محکمہ کے نام درخواست لکھوا رہے تھے؟','(e) To which department was Maulvi Sahib getting an application written?','(ه) مولوي صاحب د کوم ریاست په نوم درخواست لیکواوه؟')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-1')
Q(s,'2۔ جملے بنائیں۔ سر پر چڑھنا، رحم و کرم پر ہونا، ستیاناس کرنا، ازراہِ مرحمت، آسمان سر پر اُٹھانا۔','2. Make sentences: sar par charhna (to take liberties), rahm-o-karam par hona (to depend on mercy), satyanas karna (to ruin), azrah-e-marhamat (out of kindness), aasman sar par uthana (to raise a great uproar).','۲. جملې جوړې کړئ: پر سر خېژېدل، په رحم او کرم کېدل، ستیاناس کول، ازراه مرحمت، اسمان پر سر پورته کول.')
F.done()
s['sourceNote']='Printed page 82 (scan 89): the end of the play (the Maulvi’s last speech, the final dictation in the box with dotted gaps), the “Mashq” title and questions 1 (five parts) and 2. The page is slightly crinkled at the top left.'+NOTE
s['vocabulary']={}
save(s)
