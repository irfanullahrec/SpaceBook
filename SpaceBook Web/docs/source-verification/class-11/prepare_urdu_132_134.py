from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n04',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. The masnavi is printed in two columns of half-lines; each right-hand half-line is paired with the left-hand one in the same row (one couplet).'
# scan 132 = printed 125
s=page(132,'n04','125','Shehzade ka Chhat par Sona aur Pari ke Haathon Aghwa Hona (Mir Hasan), part 1','شہزادے کا چھت پر سونا اور پری کے ہاتھوں اغوا ہونا (میر حسن) (حصہ اوّل)','د شهزاده په چت ویده کېدل او د پرۍ په لاس تښتول کېدل (میر حسن) (لومړۍ برخه)','poem1')
F=Flow(s)
H(s,'شہزادے کا چھت پر سونا اور پری کے ہاتھوں اغوا ہونا','The Prince Sleeping on the Roof and Being Abducted by a Fairy','د شهزاده په چت ویده کېدل او د پرۍ په لاس تښتول کېدل')
for r in [
('قضا را وہ شب تھی شبِ چار دہ','پڑا جلوہ لیتا تھا ہر طرف مہ','By chance it was the fourteenth night (of the full moon);','the moon lay shedding light on every side.','په اتفاق هغه شپه د څوارلسمې شپه وه','سپوږمۍ په هر لوري جلوه کوله'),
('نظارے سے تھا اس کے دل کو سرور','عجب عالمِ نور کا تھا ظہور','The heart was delighted with the sight of it;','a strange world of light had appeared.','د هغې له لیدو سره زړه خوښ و','د رڼا یو عجیب نړۍ څرګنده شوې وه'),
('عجب لطف تھا سیرِ مہتاب کا','کہے تو کہ دریا تھا سیماب کا','What a strange pleasure was the moonlit walk;','one might say it was a river of quicksilver.','د سپوږمۍ د سیل عجیبه خوند و','ووایه چې د سیماب سیند و'),
('ہوا شاہ زادے کا دل بے قرار','یہ دیکھی جو وہاں چاندنی کی بہار','The prince’s heart became restless','when he saw there the spring of moonlight.','د شهزاده زړه بې قراره شو','کله چې یې هلته د سپوږمۍ بهار ولید'),
('کچھ آئی جو اس مہ کے جی میں ترنگ','کہا: آج کوٹھے پہ بچھتے پلنگ','When some fancy came into that moon-like one’s mind,','he said: “Today let beds be spread on the roof.”','کله چې د هغې سپوږمۍ په زړه کې څه ولوله راغله','وې ویل: نن په چت چارپايۍ غوړول کېږي'),
('کہا شہ نے اب تو گئے دن نکل','اگر یوں ہے مرضی، تو کیا ہے خلل','The king said: “Now the days have passed;”','“if this is your wish, what is the harm?”','پاچا وویل چې اوس خو ورځې ووتې','که ستاسو همداسې خوښه ده نو څه خلل دی'),
('قضا را وہ دن تھا اسی سال کا','غلط وہم ماضی میں تھا حال کا','By chance that was a day of that same year;','a false fancy of the present was in the past.','په اتفاق هغه د همدې کال ورځ وه','په ماضي کې د حال غلط وهم و'),
('سخن مولوی کا یہ سچ ہے قدیم','کہ آگے قضا کے، ہو احمق حکیم','This saying of the Maulvi, it is true, is old:','that before fate even a physician becomes a fool.','د مولوي دا خبره رښتیا زړه ده','چې د قضا په وړاندې ګیدړ حکیم احمق کېږي'),
('وہ سونے کا جو تھا جڑاؤ پلنگ','کہ سیمیں تنوں کو ہو جس پر اُمنگ','That jewelled bed of gold,','on which silver-bodied ones feel longing.','هغه د سرو زرو جوړ شوی چارپايۍ','چې سپینو بدنو ته پرې هیله کېږي'),
('کھنچی چادر ایک اس پہ شبنم کی صاف','کہ ہو چاندنی، جس صفا کی غلاف','A sheet clear as dew was spread over it,','so pure that moonlight would be its cover.','پر هغې د شبنم صاف چادر غوړېدلی و','چې سپوږمۍ د هغې د صفایۍ پوښ وي'),
('دھرے اس پہ تکیے کئی نرم نرم','کہ محمل کو ہو جس کے دیکھے سے شرم','On it were placed several soft, soft pillows','at whose sight even the litter would feel shame.','پر هغې ډېر نرم نرم بالښتونه ایښودل شوي وو','چې د هغو په لیدو سره محمل ته شرم وي'),
('کبھی نیند میں جب کہ ہوتا تھا وہ','تو رخسار رکھ اس پہ سوتا تھا وہ','Whenever he was in sleep,','he would sleep placing his cheek on it.','کله چې به هغه په خوب کې و','نو مخ به یې پر هغې ایښود او ویده به شو'),
('چھپائے سے ہوتا نہ، حسنؔ اس کا ماند','دیے تھے لگا اس کے مکھڑے کو چاند','Hasan! Its beauty did not fade by hiding;','the moon had lent lustre to his face.','پټولو سره یې ښکلا نه ټیټېده حسنه','سپوږمۍ د هغه مخ ته ځلا ورکړې وه'),
('وہ سویا جو اس آن سے بے نظیر','رہا پاسباں اس کا بدرِ منیر','When the matchless one slept in that fashion,','the radiant full moon remained his guard.','کله چې هغه بې نظیره په دغه شان ویده شو','د هغه ساتونکی د روښانه بدر سپوږمۍ پاتې شو'),
('ہوا اُس کے سونے پہ عاشق جو ماہ','لگا دی اُدھر اس نے اپنی نگاہ','The moon, in love with his sleeping,','fixed its gaze on him.','د هغه په ویده کېدو چې سپوږمۍ عاشقه شوه','خپل نظر یې هغه لور ته ولګاوه'),
('وہ مہ اس کے کوٹھے کا ہالہ ہوا','غرض وہاں کا عالم دو بالا ہوا','That moon became the halo of his roof;','in short the scene there was doubled in splendour.','هغه سپوږمۍ د هغه د چت هاله شوه','په لنډه توګه د هلته منظر دوه چنده شو'),
('وہ پھولوں کی خوشبو، وہ سہرا پلنگ','جوانی کی نیند اور وہ سونے کا ڈھنگ','Those flowers’ fragrance, that garlanded bed,','the sleep of youth and that manner of sleeping.','د ګلانو هغه بوی، هغه سهره چارپايۍ','د ځوانۍ خوب او د ویده کېدو هغه طرز'),
('جہاں تک کہ چوکی کے تھے باری دار','ہوا جو چلی، سو گئے ایک بار','As many as were the guards on duty at the watch,','when the breeze blew, they all fell asleep at once.','چې څومره د پوستې ساتونکي وو','کله چې باد وځلېد نو ټول یو ځل ویده شول')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 125 (scan 132): title “شہزادے کا چھت پر سونا اور پری کے ہاتھوں اغوا ہونا” (two-line ornamental title), running head “میر حسن”, and 18 couplets of the masnavi “Sehr-ul-Bayan” in two columns; the right-hand half-line of each row is paired with the left-hand one. The poem continues on the next page.'+NOTE
s['vocabulary']={}
save(s)
# scan 133 = printed 126
s=page(133,'n04','126','Shehzade ka Chhat par Sona…, end; Exercise (Mashq)','شہزادے کا چھت پر سونا… (اختتام)؛ مشق','د شهزاده په چت ویده کېدل… (پای)؛ تمرین','poem2')
F=Flow(s)
for r in [
('غرض سب کو وہاں عالمِ خواب تھا','فقط جاگتا ایک مہتاب تھا','In short everyone there was in the world of sleep;','only one was awake: the moon.','په لنډه توګه ټول هلته د خوب په نړۍ کې وو','یوازې یو ویښ و: سپوږمۍ'),
('قضا را ہوا اک پری کا گزر','پڑی شاہ زادے پہ اس کی نظر','By chance a fairy passed that way;','her glance fell on the prince.','په اتفاق د یوې پرۍ تېرېدل وشول','د هغې نظر پر شهزاده ولوېد'),
('ہوئی حُسن پر اس کے جی سے نثار','وہ تخت اپنا لائی ہوا سے اُتار','She became devoted to his beauty with all her heart;','she brought her throne down from the air.','د هغه په ښکلا یې له زړه نثار شوه','خپله تخت یې له هوا نه راښکته کړ'),
('جو دیکھا، تو عالم عجب ہے یہاں','منوّر ہے سارا زمیں آسماں','When she looked, she found it a strange world here;','the whole earth and sky lit up.','کله چې یې ولید نو دلته عجیبه نړۍ ده','ټوله ځمکه او اسمان روښانه دی'),
('ہوئی دونوں کے حُسن کی ایک جوت','کہ جیسے ہوں دو چشموں کی ایک سوت','The beauty of the two became one flame,','as if two springs had one source.','د دواړو د ښکلا یوه څراغ شوه','لکه د دوو چینو یو سرچینه'),
('مئے عشق میں پھر یہ سُوجھی ترنگ','کہ لے چلیے اس کا امانت پلنگ','Then in the wine of love this fancy struck her:','“Let us carry away his trusted bed.”','بیا د مینې په شرابو کې دا ولوله راغله','چې د هغه امانت چارپايۍ یوسو'),
('محبّت کی آئی جو دل میں ہوا','وہاں سے اُسے لے اُڑی دل رُبا','As the wind of love came into her heart,','the heart-ravisher flew off with him from there.','کله چې په زړه کې د مینې باد راغی','هغه زړه ایستونکې هغه له هغه ځایه راواخیست'),
('غرض لے گئی اس کی آن میں','اُڑا کر وہ اُس کو پرستان میں','In short she took him in a moment,','flying with him to the land of fairies.','په لنډه توګه یې هغه په یوه شېبه کې یوړ','هغه یې الوتولو سره پرستان ته یوړ'),
('کبھی دل رہے خوش کبھی دردمند','زمانے کی جیسی ہے پست و بلند','Sometimes the heart is glad, sometimes pained,','as the ups and downs of time are.','کله زړه خوشاله وي کله دردمن','لکه د زمانې ټیټ او لوړ')]:
    V(s,*r)
P(s,'(مثنوی «سحر البیان»)','(Masnavi “Sehr-ul-Bayan”)','(مثنوي «سحر البیان»)')
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ چاندنی رات کا منظر اپنے الفاظ میں لکھیں۔','1. Write the scene of the moonlit night in your own words.','۱. د سپوږمۍ شپې منظر په خپلو الفاظو ولیکئ.')
Q(s,'2۔ مصرعے کی وضاحت کریں۔ «کہ آگے قضا کے، ہو احمق حکیم»۔','2. Explain the line: “that before fate even a physician becomes a fool.”','۲. مصرع تشریح کړئ. «چې د قضا په وړاندې ګیدړ حکیم احمق کېږي».')
Q(s,'3۔ مثنوی کی تعریف کریں۔','3. Define masnavi.','۳. د مثنوي تعریف وکړئ.')
Q(s,'4۔ درج ذیل الفاظ و محاورات کو جملوں میں استعمال کریں۔ شبِ چاردہ، دن نکل گئے، خلل، دو بالا، پست و بلند۔','4. Use the following words and idioms in sentences: shab-e-chaardah, din nikal gaye, khalal, do-bala, past-o-buland.','۴. لاندې الفاظ او محاورې په جملو کې وکاروئ. شب چارده، ورځې ووتې، خلل، دوه بالا، ټیټ او لوړ.')
Q(s,'5۔ اس نظم سے وہ اشعار لکھیں جن میں تشبیہ استعمال ہو۔','5. Write from this poem the couplets in which simile is used.','۵. له دې نظم نه هغه شعرونه ولیکئ چې په هغو کې تشبیه کارول شوې وي.')
Q(s,'6۔ «کبھی دل رہے خوش کبھی دردمند / زمانے کی جیسی ہے پست و بلند» اس شعر میں خوش، دردمند اور پست و بلند متضاد الفاظ ہیں۔ اس طرح کے متضاد الفاظ سے کلام میں اثر اور معنی آفرینی پیدا ہوتی ہے۔ اسے صنعتِ تضاد کہتے ہیں۔ آپ ایسے تین اشعار لکھیں جن میں صنعتِ تضاد پائی جاتی ہو۔','6. “Sometimes the heart is glad, sometimes pained, as the ups and downs of time are.” In this couplet khush, dardmand and past-o-buland are opposing words. By such opposing words, effect and richness of meaning arise in poetry. This is called the figure of opposition (sanat-e-tazaad). Write three couplets in which the figure of opposition is found.','۶. «کله زړه خوشاله وي کله دردمن / لکه د زمانې ټیټ او لوړ». پدې شعر کې خوشاله، دردمن او ټیټ او لوړ متضاد الفاظ دي. د داسې متضادو الفاظو له امله په کلام کې اغېز او معنا پیدا کېږي. هغې ته صنعت تضاد وايي. تاسو داسې درې شعرونه ولیکئ چې په هغو کې صنعت تضاد وموندل شي.')
F.done()
s['sourceNote']='Printed page 126 (scan 133): the last nine couplets of the masnavi (two columns, right half-line paired with left), source line “(مثنوی «سحر البیان»)”, the “Mashq” title and six questions (question 6 quotes a couplet in blue).'+NOTE
s['vocabulary']={}
save(s)
# scan 134 = printed 127
s=page(134,'n05','127','Mir Babar Ali Anees (poet profile)','میر ببر علی انیس (شاعر کا تعارف)','میر ببر علي انیس (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'میر ببر علی انیس','Mir Babar Ali Anees','میر ببر علي انیس')
P(s,'پیدایش: ۱۸۰۰ء — وفات: ۱۸۷۴ء','Born: 1800 — Died: 1874','زېږېدنه: ۱۸۰۰ز — وفات: ۱۸۷۴ز')
P(s,'میر ببر علی انیس میر خلیق کے فرزند اور میر حسنؔ کے پوتے تھے۔ خاندانی روایات کے مطابق انھیں گھر پر ہی تعلیم دی جاتی رہی۔ گھر کے باہر اُن کے پہلے استاد میر نجف علی فیض آبادی تھے۔ زمانۂ طالبِ علمی میں انیسؔ کو معقولات اور لسانی مسائل سے بڑی دل چسپی تھی۔ ان کے ذاتی کتب خانے میں لگ بھگ دو ہزار کے قریب نسخے تھے۔ زمانے کے رواج کے مطابق انھوں نے شہ سواری اور شمشیر زنی بھی سیکھی۔ بعد میں فوجی تربیّت بھی حاصل کی۔ ہمیشہ چاق و چوبند رہا کرتے تھے۔ طبعاً خوش مزاج اور حاضر جواب تھے۔','Mir Babar Ali Anees was the son of Mir Khaliq and the grandson of Mir Hasan. According to family traditions he was educated at home. Outside the home his first teacher was Mir Najaf Ali Faizabadi. In student days Anees had great interest in rational sciences and linguistic problems. In his personal library there were nearly two thousand copies. According to the custom of the time he also learnt horse-riding and swordsmanship. Later he also obtained military training. He used to remain always agile and alert. By nature he was cheerful and quick-witted.','میر ببر علي انیس د میر خلیق زوی او د میر حسن لمسی و. د کورنۍ د دودونو له مخې هغه ته په کور کې زده‌کړه ورکول کېده. له کوره بهر د هغه لومړنی استاد میر نجف علي فیض اباديو. د زده‌کوونکي په وخت کې انیس ته معقولاتو او ژبنیو مسایلو سره ډېره دلچسپي وه. د هغه په شخصي کتابتون کې نژدې دوه زره نسخې وې. د زمانې د رواج له مخې هغه سورلي او توره وهل هم زده کړل. وروسته یې پوځي روزنه هم ترلاسه کړه. تل چټک او ځیرک وو. په طبیعت خوشاله او حاضر ځوابه و.')
P(s,'انیسؔ نے شاعری کا آغاز غزل سے کیا، لیکن اُن کی شہرت کا مدار مرثیہ نگاری پر ہے۔ اُن کے زمانے میں مرثیہ خوانی کے لیے تحت اللفظ اور سوز کا انداز اپنایا جاتا تھا۔ انیسؔ نے دونوں طرح پڑھنے کے لیے مرثیے لکھے اور کامیاب رہے۔ اُن کا اسلوب سادہ، رواں اور آسان ہے۔ انسانی جذبات کا بیان انھوں نے جس طرح کیا ہے، شاید ہی کوئی کر سکے۔ ایک محتاط اندازے کے مطابق ان کے مرثیوں کی تعداد دو ہزار کے قریب ہے۔','Anees began poetry with the ghazal, but his fame rests on marsiya writing. In his time for marsiya recitation the style of tahtul-lafz (plain recitation) and soz (chanting) was adopted. Anees wrote marsiyas for reading both ways and succeeded. His style is simple, fluent and easy. The way he has described human emotions, hardly anyone could do. According to a careful estimate the number of his marsiyas is nearly two thousand.','انیس شاعري له غزل نه پیل کړه خو د هغه شهرت مدار پر مرثیه لیکنه دی. د هغه په وخت کې د مرثیه ویلو لپاره د تحت اللفظ او سوز انداز غوره کېده. انیس د دواړو ډولونو لوستلو لپاره مرثیې ولیکلې او بریالی پاتې شو. د هغه سټایل ساده، روان او اسانه دی. د انساني جذباتو بیان چې هغه څنګه کړی دی شاید څوک یې وکړای شي. د یو احتیاطي اندازې له مخې د هغه د مرثیو شمېر نژدې دوه زره دی.')
P(s,'میر انیسؔ کے مرثیے پانچ جلدوں میں شایع ہو چکے ہیں۔ اُنھوں نے مرثیوں کے علاوہ سلام اور رباعیات بھی کہی ہیں۔ ان رباعیات میں بھی ان کا رنگ صوفیانہ ہے۔ مگر اُن کا کمال مرثیے کے فن میں زیادہ کھل کر سامنے آتا ہے۔','Mir Anees’s marsiyas have been published in five volumes. Besides marsiyas he has also composed salaams and rubaiyat. In these rubaiyat too his colour is Sufi. But his perfection comes out more fully in the art of marsiya.','د میر انیس مرثیې په پنځو جلدونو کې خپرې شوې دي. له مرثیو پرته یې سلامونه او رباعیات هم ویلي دي. په دغو رباعیاتو کې هم د هغه رنګ صوفیانه دی. خو د هغه کمال د مرثیې په فن کې ډېر څرګندېږي.')
P(s,'مجموعۂ کلام: کلیاتِ مراثیِ انیس','Poetry collection: Kulliyat-e-Maraasi-e-Anees','د شعري ټولګه: کلیات مراثي انیس')
F.done()
s['sourceNote']='Printed page 127 (scan 134): ornamental title “میر ببر علی انیس”, portrait (not reproduced), birth/death boxes (1800 and 1874), biography and the collection name.'+NOTE
s['vocabulary']={}
save(s)
