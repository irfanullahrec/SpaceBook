from urduhelp import *
c=cell
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def D(s,lab,t,e,p): add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Comic one-act play in colloquial Urdu; translations are free renderings.'
def run(s,items):
    for it in items:
        if it[0] is None: P(s,it[1],it[2],it[3])
        else: D(s,*it)
# scan 84 = printed 77
s=page(84,'p10','77','Taleem-e-Balighan, part 6','تعلیمِ بالغاں (حصہ ششم)','د لویانو زده‌کړه (شپږمه برخه)','l6')
F=Flow(s)
run(s,[('مولوی','(چونک کر) ارے رے رے رے۔ ارے وکٹوریہ کہاں چھوڑا۔ تیرا گھوڑا میری جگی کھا رہا ہے۔ (دو ڈنڈے رسید کرتا ہے) بھاگ۔ ارے بھاگ۔','Maulvi: (startled) Oh no, no, no! Hey, where did you leave the Victoria? Your horse is eating my fodder bundle. (strikes two blows with the stick) Run! Hey, run!','مولوي: (ټکان خوړلو سره) ای ره ره ره! ای وکټوریه چېرته پرېښوده. ستا آس زما جګۍ خوري. (دوه لښتې ورکوي) وتښته. ای وتښته!'),
(None,'(وکٹوریہ والا ڈنڈے کھا کر باہر بھاگ جاتا ہے۔ قصائی اور حجام ہنستے ہنستے لوٹ پوٹ ہو جاتے ہیں۔)','(The Victoria-driver, taking the blows, runs outside. The butcher and the barber roll over with laughter.)','(وکټوریه والا لښتې خوړلو سره بهر تښتي. قصاب او حجام خندلو سره ولوېږي.)'),
('قصاب','(ہنستے ہوئے) مان گئے مولی صاحب مان گئے آپ کو۔','Butcher: (laughing) We admit it, Maulvi Sahib, we admit you.','قصاب: (خندلو سره) ومنل مولوي صاحب ومنل تاسو ته.'),
('حجام','(ہنستے ہوئے) مان گئے ایمان سے۔','Barber: (laughing) We admit it, on our faith.','حجام: (خندلو سره) په ایمان ومنل.'),
('مولوی','(خود بھی خوش ہوتے ہوئے) کیا بات ہے! کیا بات ہے! میں نے کوئی کارنامہ کیا ہے؟','Maulvi: (also pleased himself) What is it! What is it! Have I done some great deed?','مولوي: (پخپله هم خوښېدو سره) څه خبره ده! څه خبره ده! ما کومه کارنامه کړې ده؟'),
('قصاب','(ہنستے ہوئے) اجی بہت بڑا کارنامہ۔','Butcher: (laughing) Sir, a very great deed.','قصاب: (خندلو سره) ای ډېره لویه کارنامه.'),
('مولوی','(خوش ہو کر) اجی سنتی ہو (بیوی کو آواز دیتے ہیں) میں نے ایک کارنامہ کیا ہے (حجام اور قصائی سے) ذرا زور سے بولو بچّے کا ماموں بھی آیا ہوا ہے۔','Maulvi: (pleased) Do you hear (calling his wife) I have done a great deed (to the barber and the butcher) speak a little louder; the child’s maternal uncle has also come.','مولوي: (خوشاله کېدو سره) ای اورې (ښځې ته غږ کوي) ما یوه کارنامه کړې ده (حجام او قصاب ته) لږ په زوره ووایئ د ماشوم ماما هم راغلی دی.'),
('قصاب','(ہنستے ہوئے) اجی قرض خواہ کو بھگانے کی ترکیب، تو کچھ آپ ہی کو آتی ہے۔','Butcher: (laughing) Sir, the trick of driving off a creditor is something only you know.','قصاب: (خندلو سره) ای د پور غوښتونکي تښتولو چاره خو یوازې تاسو ته راځي.'),
('مولوی','(غصے میں دونوں کو ایک ایک ڈنڈا رسید کرتے ہوئے) چپ۔ چپ۔ کم بختوں نے قرض لینا بھی مشکل کر دیا۔ ارے بابا میں ایک غریب آدمی ہوں۔ میں نے قرض لیا، تو کیا ہوا۔ آج کل، تو بڑی بڑی حکومتیں قرض لیتی ہیں۔','Maulvi: (in anger giving each one a blow of the stick) Quiet! Quiet! The wretches have made even borrowing difficult. Hey, baba, I am a poor man. What if I took a loan? These days even big governments take loans.','مولوي: (په غصه دواړو ته یو یو لښته ورکولو سره) چوپ. چوپ. بدبختانو پور اخیستل هم ګران کړل. ای بابا زه یو غریب سړی یم. ما پور واخیست نو څه شو. نن سبا خو لوی لوی حکومتونه پور اخلي.'),
('قصاب','(توجّہ ہٹانے کے لیے خود بخود درخواست پڑھنے لگتا ہے) پچھلے ماہ سے تنخواہ نہ ملنے کے سبب مدرسے کو شاگردوں کا قرضہ ہو گیا ہے۔','Butcher: (to divert attention begins to read the application by himself) Since salary was not received since last month the madrasa has become indebted to the pupils.','قصاب: (پام اړولو لپاره پخپله درخواست لوستل پیل کوي) له تېرې میاشتې نه د تنخوا نه ملاوېدو له امله مدرسه ته د شاګردانو پور شوی دی.'),
('مولوی','(غمگین ہو کر اپنے آپ سے) اور اب تو یہ حالت ہو گئی ہے کہ شاگرد اُستاد کو تچی دکھانے لگے ہیں۔','Maulvi: (grieved, to himself) And now it has come to this state that pupils have begun to show the teacher the “tachchi”.','مولوي: (غمجن کېدو سره له ځان سره) او اوس خو دا حالت شوی دی چې شاګردان استاد ته تچي ښودل پیل کړي دي.'),
('قصاب','(لکھتے ہوئے دُہراتا ہے) تچی دکھانے لگے ہیں۔','Butcher: (repeating as he writes) have begun to show the “tachchi”.','قصاب: (لیکلو سره تکرارېږي) تچي ښودل پیل کړي دي.'),
('مولوی','(چونک کر) ارے کاٹ۔ کاٹ۔','Maulvi: (startled) Hey, strike it out! Strike it out!','مولوي: (ټکان خوړلو سره) ای پرې کړه. پرې کړه.'),
(None,'(حجام جو قینچی سے اپنی مونچھیں ٹھیک کر رہا ہے گھبرا کر وہ ازار بند جو مولوی صاحب بُن رہے تھے قینچی سے کاٹ دیتا ہے۔)','(The barber, who is trimming his moustache with scissors, in alarm cuts with the scissors the trouser-cord which Maulvi Sahib was weaving.)','(حجام چې په قینچۍ خپل برېتونه سموي ګډوډېدو سره هغه ازار بند چې مولوي صاحب ګنډل په قینچۍ پرې کوي.)')])
F.done()
s['sourceNote']='Printed page 77 (scan 84): continuation of the comic play (speaker labels in blue). “تچی” is read as printed (a slang gesture; the Maulvi’s pun is about “tachi/kainchi”).'+NOTE
s['vocabulary']={}
save(s)
# scan 85 = printed 78
s=page(85,'p10','78','Taleem-e-Balighan, part 7','تعلیمِ بالغاں (حصہ ہفتم)','د لویانو زده‌کړه (اوومه برخه)','l7')
F=Flow(s)
run(s,[('مولوی','(تڑپ کر) ہے ہے ہے۔ ارے جملہ کاٹنے کو کہا تھا، ازار بند کاٹ دیا۔ دن بھر کی محنت اور چھے آنے کا ستیاناس کر دیا۔','Maulvi: (writhing) Alas, alas, alas! Hey, I told you to strike out the sentence and you cut the trouser-cord! You have ruined a day’s labour and six annas.','مولوي: (تېزېدو سره) افسوس افسوس افسوس. ای جمله پرې کولو ویل شوي وو، ازار بند دې پرې کړ. د ورځې زحمت او شپږ آنې دې خراب کړل.'),
(None,'(مولوی صاحب ڈنڈا اٹھا کر حجام کو مارنا چاہتے ہیں وہ قینچی پیٹ کی طرف کر دیتا ہے۔ پلٹ کر قصاب کو مارنا چاہتے ہیں وہ چھرا اٹھا لیتا ہے۔ مولوی صاحب ڈر کر ڈنڈا رکھ دیتے ہیں اور پیار سے کہتے ہیں)','(Maulvi Sahib, raising the stick, wants to hit the barber; he points the scissors towards his belly. Turning, he wants to hit the butcher; he picks up the knife. Maulvi Sahib in fear puts down the stick and says lovingly:)','(مولوي صاحب لښته پورته کولو سره غواړي حجام ووهي هغه قینچۍ ګېډې لور ته کوي. اوښتلو سره غواړي قصاب ووهي هغه چړه پورته کوي. مولوي صاحب ویرېدو سره لښته کېږدي او په مینه وايي)'),
('مولوی','(حجام سے) رکھ دو بیٹا۔ رکھ دو۔ یہ تیز ہتھیار ہیں نا۔ ان کا کھیل اچھا نہیں ہوتا بیٹے! رکھ دو۔ شاباش۔','Maulvi: (to the barber) Put it down, son. Put it down. These are sharp weapons, aren’t they? Playing with them is not good, son! Put it down. Bravo.','مولوي: (حجام ته) کېږده زویه. کېږده. دا تېز وسلې دي نه. د دې لوبه ښه نه وي زویه! کېږده. شاباش.'),
(None,'(حجام مولوی صاحب کے نرم رویّے کو دیکھ کر قینچی نیچے رکھ دیتا ہے)','(The barber, seeing Maulvi Sahib’s gentle attitude, puts the scissors down.)','(حجام د مولوي صاحب نرم چلند لیدلو سره قینچۍ ښکته کېږدي)'),
('مولوی','(قصاب سے) دیکھ خلیفہ نے ہتھیار رکھ دیے ہیں تم بھی رکھ دو۔ یہ تیز ہتھیار ہیں نا بیٹے ہاتھ واتھ کٹ جائے گا۔ خون نکل آئے گا۔ رکھ دو۔ شاباش۔ (قصاب، حجام کی دیکھا دیکھی خود بھی چھرا کندے پر رکھ دیتا ہے)','Maulvi: (to the butcher) See, the khalifa has put down his weapon; you too put yours down. These are sharp weapons, son; a hand or something will be cut; blood will come out. Put it down. Bravo. (The butcher, following the barber, himself puts the knife on the block.)','مولوي: (قصاب ته) وګوره خلیفه وسله کېښوده تاسو هم کېږدئ. دا تېز وسلې دي نه زویه لاس واس به پرې شي. وینه به راوځي. کېږده. شاباش. (قصاب د حجام په لیدو پخپله هم چړه پر کنده کېږدي)'),
('مولوی','(قصاب کے دو ڈنڈے زور دار لگاتے ہیں) رکھ رکھ۔ کم بخت کہیں کے۔ کوئی قینچی دکھا رہا ہے۔ کوئی چھرا دکھا رہا ہے۔ کوئی تچی دکھا رہا ہے۔ مدرسۂ تعلیمِ بالغاں کیا ہوا اچھی خاصی ایسٹ پاکستان کی اسمبلی بنا رہے ہیں۔','Maulvi: (strikes the butcher two hard blows) Put down, put down, wretch! One is showing scissors, one is showing a knife, one is showing “tachchi”. What has become of Madrasa Taleem-e-Balighan: you are making it a regular East Pakistan Assembly.','مولوي: (قصاب ته دوه سختې لښتې ورکوي) کېږده کېږده. بدبخته چېرته. څوک قینچۍ ښیي. څوک چړه ښیي. څوک تچي ښیي. د لویانو د زده‌کړې مدرسه څه شوه ښه ښه د ختیځ پاکستان اسمبلي جوړوي.'),
(None,'(قصاب دو ڈنڈوں کی ضرب سے غصّے میں آ جاتا ہے۔)','(The butcher, from the force of two blows, becomes angry.)','(قصاب د دوو لښتو له ضرب نه په غصه کې راځي.)'),
('مولوی','چل آگے پڑھ۔','Maulvi: Come on, read on.','مولوي: ځه مخکې ولوله.'),
('قصاب','(غصے میں) شاگردوں کا قرضہ ہو گیا ہے۔ بس یہیں تک لکھائے تھے۔','Butcher: (in anger) “The pupils’ debt has occurred.” This far you had it written.','قصاب: (په غصه) د شاګردانو پور شوی دی. بس تر دې ځایه مو لیکلی وو.'),
('مولوی','تو آگے لکھ۔','Maulvi: Then write further.','مولوي: نو مخکې ولیکه.'),
('قصاب','(غصے میں) بولیے۔','Butcher: (in anger) Say it.','قصاب: (په غصه) ووایئ.'),
('مولوی','(لکھاتے ہوئے) جناب والا۔','Maulvi: (dictating) Your Honour.','مولوي: (لیکلو سره) جناب والا.')])
F.done()
s['sourceNote']='Printed page 78 (scan 85): continuation of the comic play (speaker labels in blue; stage directions in parentheses); the Maulvi’s “East Pakistan Assembly” remark is as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 86 = printed 79
s=page(86,'p10','79','Taleem-e-Balighan, part 8','تعلیمِ بالغاں (حصہ ہشتم)','د لویانو زده‌کړه (اتمه برخه)','l8')
F=Flow(s)
run(s,[('قصاب','(غصے میں جیسے ڈانٹ رہا ہو) جناب والا۔','Butcher: (in anger, as if scolding) Your Honour.','قصاب: (په غصه لکه ډانټ کوي) جناب والا.'),
(None,'(مولوی صاحب ڈنڈا اٹھانا چاہتے ہیں قصاب تیزی سے خود ڈنڈا اُٹھا لیتا ہے)','(Maulvi Sahib wants to pick up the stick; the butcher quickly picks up the stick himself.)','(مولوي صاحب غواړي لښته پورته کړي قصاب په چټکۍ پخپله لښته پورته کوي)'),
('مولوی','(بے بسی سے ڈنڈے کو دیکھتے ہوئے) ارے عاجزی سے لکھو بیٹا۔ عاجزی سے لکھو۔ مجھے چھے مہینے سے تنخواہ نہیں ملی نا۔ (پیار سے) عاجزی سے لکھو بیٹا۔','Maulvi: (looking helplessly at the stick) Hey, write humbly, son. Write humbly. I have not received a salary for six months, you see. (lovingly) Write humbly, son.','مولوي: (بې وسۍ سره لښتې ته کتلو سره) ای په عاجزۍ ولیکه زویه. په عاجزۍ ولیکه. ماته شپږ میاشتې دي تنخوا نه ده ملاؤ شوې نه. (په مینه) په عاجزۍ ولیکه زویه.'),
(None,'(قصاب، مولوی صاحب کے رویّے سے نرم پڑ کر ڈنڈا رکھ دیتا ہے)','(The butcher, softened by Maulvi Sahib’s attitude, puts down the stick.)','(قصاب د مولوي صاحب له چلند نه نرم کېدو سره لښته کېږدي)'),
('مولوی','(ڈنڈا اُٹھا کر) عاجزی سے لکھ (ڈنڈا) سے لکھ (دوسرا ڈنڈا)','Maulvi: (picking up the stick) Write humbly! (stick) Write! (another stick)','مولوي: (لښته پورته کولو سره) په عاجزۍ ولیکه (لښته) ولیکه (بله لښته)'),
(None,'(قصاب تڑپ کر رونے لگتا ہے)','(The butcher writhes and begins to cry.)','(قصاب تېزېدو سره ژړل پیل کوي)'),
('مولوی','جناب والا','Maulvi: Your Honour…','مولوي: جناب والا'),
('قصاب','(ہچکیاں لیتے ہوئے) ……… جنا ………… ب ………… والا۔','Butcher: (sobbing) … Jana … b … wala.','قصاب: (ژړا کولو سره) ……… جنا ………… ب ………… والا.'),
('مولوی','ارے رو رہا ہے کیوں؟','Maulvi: Hey, why are you crying?','مولوي: ای ولې ژاړې؟'),
('قصاب','عاجزی سے لکھ رہا ہوں نا مولوی صاحب۔ عاجزی سے لکھ رہا ہوں۔','Butcher: I am writing humbly, aren’t I, Maulvi Sahib? I am writing humbly.','قصاب: په عاجزۍ لیکم نه مولوي صاحب. په عاجزۍ لیکم.'),
('دونوں','تیری عاجزی کے قربان۔ پڑھنے والوں کے دل ٹکڑے ٹکڑے ہو جائیں گے۔ لکھو! جناب والا۔','Both: Sacrifice to your humility! The hearts of the readers will be torn to pieces. Write! Your Honour.','دواړه: ستا عاجزۍ ته قربان. لوستونکو زړونه به ټوټې ټوټې شي. ولیکئ! جناب والا.'),
('قصاب','(لکھتے ہوئے) جناب والا۔','Butcher: (writing) Your Honour.','قصاب: (لیکلو سره) جناب والا.'),
(None,'(مولوی صاحب لکھواتے ہیں۔ قصاب دُہراتا جاتا ہے۔)','(Maulvi Sahib dictates. The butcher goes on repeating.)','(مولوي صاحب لیکي. قصاب تکراروي.)'),
('مولوی','گزشتہ سال ……… حکومت کے رحم و کرم سے ……… ازراہِ مرحمت۔','Maulvi: Last year … by the mercy and kindness of the government … by way of kindness.','مولوي: تېر کال ……… د حکومت په رحم او کرم ……… ازراه مرحمت.'),
('قصاب','(لکھتے ہوئے) ازراہِ مرمت۔','Butcher: (writing) “azrah-e-marammat” (by way of repair).','قصاب: (لیکلو سره) ازراه مرمت.'),
('مولوی','مرمت نہیں۔ مرحمت۔ مرحمت (“ح” کے مخرج کو واضح کرتے ہوئے)','Maulvi: Not marammat. Marhamat. Marhamat. (making clear the point of articulation of “ح”)','مولوي: مرمت نه. مرحمت. مرحمت. («ح» مخرج څرګندولو سره)'),
('حجام','(قصائی کو سمجھاتے ہوئے) مرحمت۔ مرحمت (اپنے گلے کی طرف اشارہ کرتا ہے)','Barber: (explaining to the butcher) Marhamat. Marhamat. (pointing to his throat)','حجام: (قصاب ته پوهولو سره) مرحمت. مرحمت. (خپل ستوني ته اشاره کوي)'),
('قصاب','(لکھتے ہوئے) ازراہِ مرحمت ………','Butcher: (writing) azrah-e-marhamat …','قصاب: (لیکلو سره) ازراه مرحمت ………'),
('مولوی','(لکھاتے ہوئے) مدرسۂ تعلیمِ بالغاں کے لیے ……… ایک دری ……… ایک چھتری ………','Maulvi: (dictating) for Madrasa Taleem-e-Balighan … a carpet … an umbrella …','مولوي: (لیکلو سره) د لویانو د زده‌کړې مدرسې لپاره ……… یو دری ……… یو چتر ………')])
F.done()
s['sourceNote']='Printed page 79 (scan 86): continuation of the comic play (speaker labels in blue; stage directions in parentheses). The pun “مرمت / مرحمت” (repair / kindness) is as printed, with the Maulvi correcting the pronunciation of “ح”. The dictation continues on the next page.'+NOTE
s['vocabulary']={}
save(s)
