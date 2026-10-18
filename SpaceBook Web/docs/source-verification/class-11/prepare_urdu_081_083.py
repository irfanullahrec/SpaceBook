from urduhelp import *
c=cell
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def D(s,lab,t,e,p): add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Comic one-act play in colloquial Urdu; translations are free renderings.'
# scan 81 = printed 74
s=page(81,'p10','74','Taleem-e-Balighan, part 3','تعلیمِ بالغاں (حصہ سوم)','د لویانو زده‌کړه (دریمه برخه)','l3')
F=Flow(s)
for lab,t,e,p in [('قصاب','سات سو چھیاسی بٹے نوے۔','Butcher: Seven hundred and eighty-six divided by ninety.','قصاب: اوه سوه شپږ اتیا ویشل په نوي.'),
('مولوی','(ڈنڈا مار کر) ارے وہ تو بسم اللہ کی جگہ لکھا جاتا ہے ناکم بخت۔ آگے پڑھ۔','Maulvi: (striking him with the stick) Hey, that is what is written in place of Bismillah, you wretch! Read on.','مولوي: (لښته ورکولو سره) ای هغه خو د بسم الله پر ځای لیکل کېږي ناکامه! مخکې ولوله.'),
('قصاب','(پڑھتے ہوئے) عالی جناب عزّت مآب و فضیلت مآب …… زیرِ تعلیم۔','Butcher: (reading) Your Honour, Your Excellency and Eminence … Zer-e-Taleem (under education).','قصاب: (لوستلو سره) عالي جناب عزت مآب او فضیلت مآب …… زیر تعلیم.'),
('مولوی','(گھبرا کر) ہائیں زیرِ تعلیم (ڈنڈا) زیرِ تعلیم۔ (ڈنڈا) ارے! وہ وزیرِ تعلیم ہے نا۔ ہزار دفعہ پڑھا چکا ہوں، واؤ پر زور دے کر پڑھ۔ (سمجھاتے ہوئے) دیکھ! واؤ سے ووٹ ہے نا۔','Maulvi: (alarmed) What! Zer-e-Taleem? (stick) Zer-e-Taleem! (stick) Hey! It is Wazir-e-Taleem (Minister of Education), isn’t it? I have taught you a thousand times; read with stress on the waw. (explaining) See! From waw comes “vote”, doesn’t it?','مولوي: (ګډوډېدو سره) څه زیر تعلیم (لښته) زیر تعلیم (لښته) ای! هغه وزیر تعلیم دی نه. زرو ځله مې درښودلی، په واو زور ورکولو سره ولوله. (پوهولو سره) وګوره! له واو نه ووټ دی نه.')]:
    D(s,lab,t,e,p)
P(s,'(حجام اور قصائی توجّہ سے سنتے ہوئے۔)','(The barber and the butcher listening attentively.)','(حجام او قصاب په پام اورېدو سره.)')
for lab,t,e,p in [('دونوں','ہے!','Both: Yes!','دواړه: هو!'),
('مولوی','ووٹ کا واؤ زیرِ تعلیم کے آگے لگا دیتے ہیں، تو زیرِ تعلیم، وزیرِ تعلیم بن جاتا ہے۔','Maulvi: When we put the waw of “vote” before Zer-e-Taleem, Zer-e-Taleem becomes Wazir-e-Taleem.','مولوي: د ووټ واو د زیر تعلیم مخې ته اچوو نو زیر تعلیم وزیر تعلیم کېږي.'),
('حجام','(خوش ہو کر) واہ! کیا اللہ کی شان ہے مولوی صاحب۔','Barber: (delighted) Wah! What a wonder of God, Maulvi Sahib!','حجام: (خوشاله کېدو سره) واه! څومره د الله شان دی مولوي صاحب.'),
('مولوی','(ڈنڈا اُٹھاتے ہوئے) ہاں! بتاؤں اللہ کی شان۔','Maulvi: (raising the stick) Yes! Shall I show you God’s wonder?','مولوي: (لښته پورته کولو سره) هو! درته د الله شان وښیم.')]:
    D(s,lab,t,e,p)
P(s,'(حجام ڈر کر سمٹ جاتا ہے۔)','(The barber shrinks back in fear.)','(حجام ویرېدو سره ځان ټولوي.)')
for lab,t,e,p in [('مولوی','چل! آگے پڑھ۔','Maulvi: Go on! Read on.','مولوي: ځه! مخکې ولوله.'),
('قصاب','(پڑھتے ہوئے) وزیرِ تعلیم صاحب دام اقبالہ ہو ہو ہو۔','Butcher: (reading) Wazir-e-Taleem Sahib, daam iqbaluhu — ho ho ho!','قصاب: (لوستلو سره) وزیر تعلیم صاحب دام اقباله هو هو هو.'),
('مولوی','(ڈنڈا مار کر) ہو ہو۔ ہو ہو۔ یہ ہو ہو ہاہا ہی ہی کیا کر رہا ہے؟ اسے کوئی ریڈیو پاکستان سمجھ رہا ہے کہ جہاں اقبالؒ کا نام آیا، شروع ہو گئی قوالی۔ آگے پڑھ۔','Maulvi: (striking with the stick) Ho ho! Ho ho! What are you doing, this ho-ho ha-ha hee-hee? Is someone taking it for Radio Pakistan, that as soon as Iqbal’s name came, qawwali began? Read on.','مولوي: (لښته ورکولو سره) هو هو. هو هو. دا هو هو ها ها هي هي څه کوې؟ ایا څوک دا ریډیو پاکستان ګڼي چې چېرته د اقبال نوم راغی قوالي پیل شوه. مخکې ولوله.'),
('قصاب','(پڑھتے ہوئے) دام اقبالہ (مشکل سے ادا کرتا ہے) ہم جملہ خورد و کلاں یہاں خیریت سے رہ کر آپ کی خیریت درگاہِ خداوندی سے نیک مطلوب۔','Butcher: (reading) Daam iqbaluhu (pronouncing with difficulty) — all of us, young and old, living here in good health, desire your good health from the divine court as a good wish.','قصاب: (لوستلو سره) دام اقباله (په ستونزه ادا کوي) موږ ټول واړه او لوی دلته په خیریت سره اوسېدلو سره ستاسو خیریت د خدای له دربار نه نېک مطلوب.'),
('مولوی','ہاں (ایک دم روک کر) نیک مطلوب کے آگے چاہتا ہوں بھی لکھ دے۔ یہ نہیں سمجھیں گے، تو یہ بجھ جائیں گے۔','Maulvi: Yes (stopping suddenly) after “good wish” write also “I desire”. If they do not understand it they will understand something else.','مولوي: هو (یوه شېبه ودرېدو سره) د نېک مطلوب مخې ته غواړم هم ولیکه. دا به نه پوهېږي نو بل څه به وپوهېږي.'),
('قصاب','(لکھتے ہوئے) نیک مطلوب چاہتا ہوں۔','Butcher: (writing) “I desire a good wish.”','قصاب: (لیکلو سره) نېک مطلوب غواړم.')]:
    D(s,lab,t,e,p)
F.done()
s['sourceNote']='Printed page 74 (scan 81): continuation of the comic dialogue (speaker labels in blue: قصاب, مولوی, حجام, دونوں); stage directions in parentheses. The pun “zer-e-taleem / wazir-e-taleem” (under education / minister of education) is as printed. The first words (“سات سو چھیاسی بٹے نوے”) continue the butcher’s reading from the previous page.'+NOTE
s['vocabulary']={}
save(s)
# scan 82 = printed 75
s=page(82,'p10','75','Taleem-e-Balighan, part 4','تعلیمِ بالغاں (حصہ چہارم)','د لویانو زده‌کړه (څلورمه برخه)','l4')
F=Flow(s)
for lab,t,e,p in [('مولوی','آگے پڑھ۔','Maulvi: Read on.','مولوي: مخکې ولوله.'),
('قصاب','(پڑھتے ہوئے) دیگر کوائف یہ ہیں کہ مدرسے کا کام عمدگی سے چالو ہے۔','Butcher: (reading) Other particulars are that the work of the madrasa is going on excellently.','قصاب: (لوستلو سره) نور کوائف دا دي چې د مدرسې کار په ښه ډول روان دی.'),
('مولوی','(روک کر) ہاں۔ یہ جملہ بہت اہم ہے۔ اس کے اوپر انڈر لائن کر دے۔','Maulvi: (stopping) Yes. This sentence is very important. Underline it.','مولوي: (ودرولو سره) هو. دا جمله ډېره مهمه ده. د دې پر سر انډر لاین کړه.'),
('قصاب','(حیران ہو کر) اور پر انڈر لائن کروں؟','Butcher: (astonished) And do I underline over it?','قصاب: (حیرانېدو سره) او پر سر انډر لاین کړم؟'),
('مولوی','(چڑ کر) اور نہیں، تو کیا نیچے کرے گا؟','Maulvi: (annoyed) What else, will you do it underneath?','مولوي: (غصه کېدو سره) نور نه نو څه به لاندې کوې؟'),
('قصاب','(ڈر کر) اچھا اچھا۔ (لائن لگاتے ہوئے) اور پر انڈر لائن۔ مگر پچھلے ماہ سے تنخواہ نہ ملنے کے سبب مدرسے کو شاگردوں کا قرضہ ہو گیا ہے۔','Butcher: (frightened) All right, all right. (drawing the line) “… and underline”. But since salaries have not been received for last month, the madrasa has become indebted to the pupils.','قصاب: (ویرېدو سره) ښه ښه. (کرښه کښلو سره) او پر انډر لاین. خو تېرې میاشتې نه د تنخوا نه ملاوېدو له امله مدرسه ته د شاګردانو پورونه شوي دي.')]:
    D(s,lab,t,e,p)
P(s,'(باہر سے خان صاحب کی آواز آتی ہے۔)','(The voice of Khan Sahib comes from outside.)','(له بهر نه د خان صاحب غږ راځي.)')
for lab,t,e,p in [('وکٹوریہ والا','(باہر سے آواز) مولی صاحب۔ خو مولی صاحب۔','Victoria-driver: (voice from outside) Maulvi Sahib! Hey Maulvi Sahib!','وکټوریه والا: (له بهر غږ) مولوي صاحب! خو مولوي صاحب!'),
('مولوی','(دروازے کی طرف دیکھتے ہوئے) ارے کون؟','Maulvi: (looking towards the door) Hey, who?','مولوي: (دروازې لور ته کتلو سره) ای څوک؟'),
('قصاب','اجی آپ کا شاگرد چراغ شاہ پکار رہا ہے مولوی صاحب۔','Butcher: Sir, your pupil Chiragh Shah is calling, Maulvi Sahib.','قصاب: ای ستاسو شاګرد چراغ شاه غږ کوي مولوي صاحب.'),
('مولوی','(خوش ہو کر) اچھا۔ چراغ شاہ نے میری شاگردی قبول کر لی؟ میں تو پہلے ہی کہتا تھا کہ، «بابا اگر وزیر بننا ہے تو کم سے کم دستخط کرنا سیکھ لو»۔','Maulvi: (pleased) Good! Has Chiragh Shah accepted my pupilage? I used to say all along: “Baba, if you want to be a minister, at least learn to sign.”','مولوي: (خوشاله کېدو سره) ښه. چراغ شاه زما شاګردي ومنله؟ ما خو مخکې ویل چې «بابا که وزیر کېدل غواړې نو لږ تر لږه لاسلیک کول زده کړه».'),
('قصاب','لیکن مولوی صاحب۔ وہ تو کہتا تھا کہ اب کے میں ایک مُہر بنا لوں گا مُہر۔','Butcher: But Maulvi Sahib, he used to say that this time I will have a seal made, a seal.','قصاب: خو مولوي صاحب. هغه خو ویل چې اوس به زه یوه مهر جوړه کړم مهر.'),
('مولوی','(بے نیازی سے) ہاں، حکومت کے کام تو مُہر سے بھی چل سکتے ہیں لیکن منتخب ہونے کے بعد دوسروں کی لکھی ہوئی تقریر کو خود پڑھنا پڑتا ہے۔ نہیں تو پبلک پہچان کر نعرے لگا دیتی ہے۔','Maulvi: (indifferently) Yes, the work of government can go on with a seal too, but after being elected one has to read out a speech written by others oneself. Otherwise the public recognises one and raises slogans.','مولوي: (بې پروایۍ سره) هو، د حکومت کارونه خو په مهر هم کېدای شي خو له ټاکل کېدو وروسته د نورو لیکل شوې وینا پخپله لوستل پکار دي. که نه خلک پېژني او نارې وهي.'),
('وکٹوریہ والا','(زور سے آواز دیتا ہے) مولی صاب۔ خو مولی صاب۔','Victoria-driver: (calls loudly) Maulvi Sahib! Hey Maulvi Sahib!','وکټوریه والا: (په زوره غږ کوي) مولوي صاحب! خو مولوي صاحب!'),
('مولوی','(چڑ کر) ارے کون کم بخت ہے یہ؟','Maulvi: (annoyed) Hey, who is this wretch?','مولوي: (غصه کېدو سره) ای دا څوک بدبخت دی؟'),
('قصاب','ارے اپنا چراغ شاہ مولوی صاحب۔ چنو (حجام اور قصائی آواز دیتے ہیں)','Butcher: Hey, our own Chiragh Shah, Maulvi Sahib. Chhanu! (the barber and the butcher call out)','قصاب: ای زموږ چراغ شاه مولوي صاحب. چنو! (حجام او قصاب غږ کوي)'),
('حجام اور قصاب','ارے آ جا چنو۔ کیا باہر کھڑا مولی صاحب کر رہا ہے۔','Barber and Butcher: Hey, come, Chhanu! What are you doing standing outside, Maulvi Sahib?','حجام او قصاب: ای راشه چنو. بهر ولاړ ته څه کوې مولوي صاحب.')]:
    D(s,lab,t,e,p)
F.done()
s['sourceNote']='Printed page 75 (scan 82): continuation of the comic dialogue (speaker labels in blue; the first line “آگے پڑھ” of the Maulvi continues from the previous page). “چنو”/“خو” and “مولی صاب” are colloquial forms as printed; the driver is labelled “وکٹوریہ والا”.'+NOTE
s['vocabulary']={}
save(s)
# scan 83 = printed 76
s=page(83,'p10','76','Taleem-e-Balighan, part 5','تعلیمِ بالغاں (حصہ پنجم)','د لویانو زده‌کړه (پنځمه برخه)','l5')
F=Flow(s)
P(s,'(خان صاحب وکٹوریہ والا، دائیں جانب کے ونگ سے داخل ہوتا ہے، بنیان اور شلوار پہنے ہوئے ہے۔ ہاتھ میں چابُک ہے۔ اندر داخل ہوتے ہی دو بار چابُک ہوا میں جھاڑتا ہے۔ چابک سے چٹاخ پٹاخ کی آوازیں نکلتی ہیں۔)','(Khan Sahib the Victoria-driver enters from the right-hand wing, wearing a vest and shalwar. In his hand is a whip. As soon as he enters he cracks the whip twice in the air. The whip makes crack-crack sounds.)','(خان صاحب وکټوریه والا د ښي لور له وینګ نه داخلېږي، بنیان او شلوار یې اغوستی. په لاس کې یې چابک دی. دننه راتلو سره دوه ځله چابک په هوا کې ټکوي. له چابک نه چټاخ پټاخ غږونه راځي.)')
P(s,'(حجام اور قصائی ڈر کر مولوی صاحب کے پیچھے آ جاتے ہیں۔ مولوی صاحب بھی خوف زدہ ہو کر اپنے پیر چار پائی کے اوپر کر لیتے ہیں۔)','(The barber and the butcher, frightened, come behind Maulvi Sahib. Maulvi Sahib, also terrified, draws his feet up on the cot.)','(حجام او قصاب ویرېدو سره د مولوي صاحب شا ته راځي. مولوي صاحب هم ویره منلو سره خپلې پښې پر چارپايۍ پورته کوي.)')
for lab,t,e,p in [('مولوی','(ڈرتے ڈرتے) ک………… کیا ……… بات ہے چنو بیٹے۔ آج اتنے دنوں کے بعد مدرسے آئے ہو اور وہ بھی بغیر کتابوں کے اور یہ ہاتھ میں چابُک کیوں ہے بیٹے؟','Maulvi: (fearfully) W… what … is the matter, Chhanu, son? Today after so many days you have come to the madrasa, and that too without books, and why is there a whip in this hand, son?','مولوي: (ویرېدو ویرېدو) څ………… څه ……… خبره ده چنو زویه. نن په دومره ورځو وروسته مدرسې ته راغلې او هغه هم پرته له کتابونو نه او په دې لاس کې چابک ولې دی زویه؟'),
('وکٹوریہ والا','(غصے میں چابُک جھاڑ کر) خو چابُک نہیں ہوگا، تو کیا ہوگا۔ پیسہ لے کے بیس دن ہو گیا۔ دینے کا نام نہیں لیتا۔ خو چابک نہیں ہوگا، تو اور کیا ہوگا؟','Victoria-driver: (cracking the whip in anger) If there won’t be a whip, what will there be? Twenty days since you took the money and you don’t even speak of giving it back. If there won’t be a whip, what else will there be?','وکټوریه والا: (په غصه کې چابک ټکولو سره) خو چابک به نه وي نو څه به وي. پیسې اخیستلو شل ورځې شوې. ورکولو نوم نه اخلې. خو چابک به نه وي نو نور به څه وي؟'),
('حجام','مولوی صاحب۔ یہ چابُک ہوتی بہت بُری چیز ہے۔ اس سے تو بڑے بڑے شیر بھی سیدھے ہو جاتے ہیں۔','Barber: Maulvi Sahib, a whip is a very bad thing. Even big lions become straight with it.','حجام: مولوي صاحب. دا چابک ډېره بده شی ده. له دې نه خو لوی لوی زمریان هم سم کېږي.'),
('مولوی','(حجام کو ڈنڈا مارتے ہوئے) ارے چپ رہ کم بخت (خان صاحب سے) ارے چنو۔ میں نے تجھ سے بیس روپے ادھار لیے تھے۔ دس روپے تو واپس کر چکا ہوں (گواہی کے طور پر حجام اور قصائی کو دیکھتے ہیں)','Maulvi: (striking the barber with the stick) Hey, shut up, wretch! (to Khan Sahib) Hey Chhanu! I had borrowed twenty rupees from you. Ten rupees I have already returned (looking at the barber and the butcher as witnesses).','مولوي: (حجام ته لښته ورکولو سره) ای چوپ شه بدبخته! (خان صاحب ته) ای چنو! ما له تا نه شل روپۍ پور اخیستي وو. لس روپۍ خو بېرته کړي دي (د ګواهۍ په توګه حجام او قصاب ته ګوري)'),
('حجام اور قصاب','(گواہی دیتے ہوئے) ہاں ہاں ہمارے سامنے دیے ہیں۔','Barber and Butcher: (giving witness) Yes, yes, he gave them in front of us.','حجام او قصاب: (ګواهي ورکولو سره) هو هو زموږ په وړاندې ورکړي دي.'),
('وکٹوریہ والا','(چابُک جھاڑ کر) خو باقی دس کا کیا ہوگا۔','Victoria-driver: (cracking the whip) And what about the remaining ten?','وکټوریه والا: (چابک ټکولو سره) خو د پاتې لسو څه به وي.'),
('حجام','(مولوی سے) ہاں باقی دس کا کیا ہوگا۔ جواب دو۔','Barber: (to the Maulvi) Yes, what about the remaining ten? Answer.','حجام: (مولوي ته) هو د پاتې لسو څه به وي. ځواب ورکړه.'),
('مولوی','ارے چنو۔ جب حکومت نے ہماری گرانٹ آدھی کر دی ہے، تو میں تیرے پورے پیسے کیسے دے سکتا ہوں۔','Maulvi: Hey Chhanu! When the government has halved our grant, how can I pay your full money?','مولوي: ای چنو! کله چې حکومت زموږ ګرانټ نیمایي کړی دی نو زه ستا پوره پیسې څنګه ورکولی شم.')]:
    D(s,lab,t,e,p)
P(s,'(وکٹوریہ والا زمین پر بیٹھتا ہے کہ یکایک اندر سے مولوی صاحب کی بیوی کی آواز آتی ہے۔)','(The Victoria-driver sits on the ground when suddenly from inside the voice of Maulvi Sahib’s wife is heard.)','(وکټوریه والا پر ځمکه کېني چې ناڅاپه له دننه نه د مولوي صاحب د ښځې غږ راځي.)')
D(s,'بیوی','(اندر سے) ارے ہے۔ یہ گھوڑا کس کا ہے۔ جگی کی جگی کھائے جا رہا ہے۔','Wife: (from inside) Hey! Whose is this horse? It is eating up the whole bundle of fodder.','ښځه: (له دننه نه) ای دا آس د چا دی. جګۍ په جګۍ خوري.')
F.done()
s['sourceNote']='Printed page 76 (scan 83): continuation of the comic play (speaker labels in blue: مولوی, وکٹوریہ والا, حجام, حجام اور قصاب, بیوی); stage directions in parentheses.'+NOTE
s['vocabulary']={}
save(s)
