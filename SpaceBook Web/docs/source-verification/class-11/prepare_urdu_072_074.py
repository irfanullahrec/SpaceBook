from urduhelp import *
c=cell
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def D(s,lab,t,e,p): add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab)
def V(s,ur,en,ps): add(s,f'p{len(s["paras"])+1}',en,ur,ps,boxed=True,kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Drama dialogue; verse lines are printed in blue with the verse mark.'
# scan 72 = printed 64 (blurred)
s=page(72,'p09','64','Khoobsurat Bala, part 2 (blurred scan)','خوب صورت بلا (حصہ دوم)','ښکلې بلا (دویمه برخه)','l2')
F=Flow(s)
V(s,'… بھاگ دوڑ اس طرف، طاقت ابھی ہے پاؤں میں / آرام و راحت، زندگی، سب ہیں خدا کی چھاؤں میں','… run towards this side, there is still strength in the feet; / ease, comfort, life — all are in the shade of God. (first half-line partly illegible)','… دې لور ته منډه کړه، لا ځواک په پښو کې دی / آرام او راحت، ژوند، ټول د خدای په سورې کې دي. (لومړۍ نیمه کرښه جزوي ناپېژندل)')
D(s,'بدی','(آ کر) میں ہوں جہاں کی خوشی، میں ہوں۔','(Entering) I am the happiness of the world, I am!','(راتلو سره) زه د نړۍ خوښي یم، زه یم!')
D(s,'نیکی','دنیا کی مصیبت ہے اور انسان کے بیچ دیوار۔','You are the calamity of the world and a wall between man (and God).','ته د نړۍ مصیبت یې او د انسان ترمنځ دیوال.')
D(s,'بدی','دنیا کی قسمت میرے داہنے ہاتھ میں ہے اور اس کی کنجی میرے بائیں ہاتھ میں ہے۔ تم جو بہشت کی امید میں دنیا کو روزے بنائے ہوئے ہو، میری طرف آؤ اور مہر اور دروازہ کھٹکھٹاؤ۔ میری سخاوت کے بادل موتی برسائیں گے اور تمھارے دامن کو بھی مالا مال کر دیں گے۔','The fate of the world is in my right hand and its key in my left hand. You who, in hope of Paradise, have made the world a fast, come to me and knock at my door. The clouds of my generosity will rain pearls and enrich your skirts too.','د نړۍ برخلیک زما په ښي لاس کې دی او کیلي یې زما په کیڼ لاس کې ده. تاسو چې د جنت په هیله نړۍ ته روژه جوړه کړې، زما لور ته راشئ او دروازه وټکوئ. زما د سخاوت وریځې به مروارید وورېږي او ستاسو لمن به هم ډکه کړي.')
D(s,'نیکی','تو جھوٹی ہے۔ تو آدمی کو ذلّت، مصیبت اور خوف ناک موت کے سوا کچھ نہیں دے سکتی۔','You are a liar. You cannot give man anything but disgrace, calamity and a terrible death.','ته دروغجنه یې. ته انسان ته له سپکاوي، مصیبت او ویروونکي مرګ پرته څه نشې ورکولی.')
D(s,'بدی','یہ باپ ہوتی ہے۔ یہ میری طرف آنے والوں کو روکتی ہے۔','(This one is a father-like preacher). She stops those coming towards me. (the first word is blurred)','دا … ده. دا زما لور ته راتلونکي منع کوي. (لومړی کلمه تیاره)')
D(s,'نیکی','اور تو نیک راہ چلنے والوں کو جہنم کے اندھیرے غار میں گراتی ہے۔','And you cause those who walk the righteous path to fall into the dark cave of Hell.','او ته د نېکې لارې تللونکي د دوزخ په تیاره غار کې غورځوې.')
D(s,'بدی','تو نہ ہوتی تو دنیا میں بہشت کا مزہ آتا۔','If you were not there, the world would have the taste of Paradise.','که ته نه وای نو په نړۍ کې به د جنت خوند راتلو.')
D(s,'نیکی','بدی نہ ہوتی تو خدا جہنم کو پیدا ہی نہ کرتا۔','If there were no evil, God would not have created Hell at all.','که بدي نه وای نو خدای به دوزخ پیدا نه کړی وای.')
D(s,'نیکی','بدی! لڑائی چھوڑ۔','Badi! Give up the quarrel.','بدي! جنګ پرېږده.')
D(s,'بدی','نیکی! بڑائی چھوڑ۔','Neki! Give up the boasting.','نېکي! لویوالی پرېږده.')
D(s,'بدی','ارے! یہ دنیا عاشقوں کا بازار ہے۔ اس میں کوئی میرا خریدار ہے کوئی میرا طلب گار ہے۔','Hey! This world is a market of lovers. In it someone is my buyer, someone my seeker.','ای! دا نړۍ د عاشقانو بازار دی. پدې کې څوک زما پېرېدونکی دی، څوک زما غوښتونکی دی.')
V(s,'… ایک لَے میں … سے ان کے … / … چاہتے ہیں اسی کی اور تجھ کو … / … سے بنے ہیں دل سے … شور …','(Verse lines of Neki partly illegible in this blurred scan; the surviving fragments are: “…want the very same, and you…” “…are made of the heart…”)','(د نېکۍ شعري کرښې په دې تیاره سکین کې جزوي ناپېژندل دي؛ پاتې شوي ټوټې دا دي: «…همدا غواړي او تا…» «…له زړه جوړ دي…»)')
F.done()
s['sourceNote']='Printed page 64 (scan 72): this scan is out of focus/blurred and several lines are illegible; text has been read with the help of the Word transcription (urdu-word-part2.txt) and may contain misreadings; the last two verse lines and some fragments are only partly legible (marked “…”). Speaker labels are in blue (بدی, نیکی). The verse of Neki that begins at the bottom of the page continues at the top of the next page.'+NOTE
s['vocabulary']={}
save(s)
# scan 73 = printed 65
s=page(73,'p09','65','Khoobsurat Bala, part 3','خوب صورت بلا (حصہ سوم)','ښکلې بلا (دریمه برخه)','l3')
F=Flow(s)
V(s,'جس روز روشنی میں، دیکھیں گے شکل تیری / نفرت کی ٹھوکروں سے، پھینکیں گے دور تجھ کو','On the day when they see your face in the light, / they will hurl you far with the kicks of hatred.','چې کله په رڼا کې ستا شکل وويني / د نفرت په ټکرونو به تا لرې وغورځوي')
D(s,'بدی','نادان! کبھی ایسا نہیں ہوگا۔ کیا تو نہیں جانتی کہ دنیا کی مٹی خود غرضی اور لالچ کے پانی سے گوندھی گئی ہے۔','Fool! This will never happen. Do you not know that the clay of the world has been kneaded with the water of selfishness and greed?','نادانه! داسې به هیڅکله نه وي. آیا ته نه پوهېږې چې د نړۍ خاوره د ځان غوښتنې او حرص په اوبو ګنډل شوې ده.')
D(s,'نیکی','جھوٹی! تیرا ہر لفظ عداوت سے بھرا ہے۔ دنیا کا چمن بس میری ہی کوشش سے ہرا ہے۔','Liar! Every word of yours is full of enmity. The garden of the world is green only through my effort.','دروغجنې! ستا هر کلمه له دښمنۍ ډکه ده. د نړۍ باغ یوازې زما په هڅه شین دی.')
D(s,'بدی','بس کر قیل و قال۔ اب دیکھ میرے عاشقوں کا حال۔','Enough of disputing. Now see the state of my lovers.','بس کړه بحث. اوس زما د عاشقانو حال وګوره.')
P(s,'(طغرل کا شراب پیتے دکھائی دینا، ساتھیوں کا گانا)','(Tughril is seen drinking wine; his companions sing.)','(د طغرل شراب څښل ښکارېدل، د ملګرو سندرې)')
D(s,'گانا','اے پیارے مہاراجا۔ ڈُلا رے مہاراجا۔ پیالے مے کے پی لو جی۔ پیو جانی، پیالے مے کے پی لو جی۔ اے پیارے ………','Song: O dear Maharaja! Dear Maharaja! Drink cups of wine, sir. Drink, darling, cups of wine, sir. O dear …','سندره: ای ګرانه مهاراجه! ډلا ره مهاراجه! د شرابو پیالې وڅښه جي. وڅښه جانې، د شرابو پیالې وڅښه جي. ای ګرانه ………')
V(s,'بہار آئی ہے بھر دے بادۂ گل گوں سے پیمانہ / رہے لاکھوں برس ساقی ترا آباد مے خانہ','Spring has come; fill the goblet with rose-coloured wine; / may your tavern, O cup-bearer, stay prosperous for hundreds of thousands of years.','پسرلی راغلی دی د ګلرنګ شراب سره پیمانه ډکه کړه / ساقي دې ستا میخانه لکونه کلونه آباده وي')
D(s,'دوسرا','(verse above, sung by the second companion)','The verse is sung by the second companion.','دا شعر دویم ملګری وايي.')
D(s,'بدی','میرے عاشقوں کا حال دیکھ چکی۔ اب اپنے چاہنے والوں کی ذلّت اور مصیبت دیکھ۔','You have seen the state of my lovers. Now see the disgrace and calamity of your own lovers.','ما د خپلو عاشقانو حال ولید. اوس د خپلو مینه والو سپکاوی او مصیبت وګوره.')
D(s,'نیکی','بدی! ہوئی شرط! دیکھنا میں ہارتی ہوں یا تو ہارتی ہے۔ (جانا)','Badi! It’s a bet! See whether I lose or you lose. (Exit)','بدي! شرط شو! وګوره زه بایلم که ته بایلې. (تلل)')
P(s,'(پردہ ہٹتا ہے اور شمسہ کا عالی شان مکان نظر آنا۔ سب درباریوں کا دست بستہ دکھائی دینا)','(The curtain rises and Shamsa’s magnificent palace is seen. All the courtiers are seen with folded hands.)','(پرده ځي او د شمسې عالي شان ماڼۍ ښکارېږي. ټول درباریان لاس تړلي ښکارېږي)')
for lab,t,e,p in [('پہلا چوب دار','جلال ہمراہ، کمال ہمدم، عروج مانندِ چھتر سر پر','First mace-bearer: Glory accompanies, perfection is her companion, high rank is like an umbrella over her head.','لومړی چوب دار: جلال ورسره، کمال ملګری، عروج د چتر په څېر پر سر'),
('دوسرا','زمانہ حامی، فلک محافظ، سپہر بندہ، ستارہ چاکر','Second: Time her supporter, the sky her protector, the heavens her slave, the stars her servants.','دویم: زمانه ملاتړې، اسمان ساتونکی، سپهر بنده، ستوری نوکران'),
('پہلا','نصیب دربان، قضا نگراں، قدر ثنا خواں، ہو بخت یاور','First: Fortune her doorkeeper, fate her watchman, destiny her praiser, good luck her helper.','لومړی: نصیب دربان، قضا ساتونکې، قدر ثنا خوان، بخت مرستندوی'),
('دوسرا','سحابِ قلزم، قدم قدم پر، زر و جواہر نثار سر پر','Second: Clouds from the ocean, at every step gold and jewels are showered on her head.','دویم: د سمندر وریځې، په هر ګام زر او جواهر پر سر نثار'),
('پہلا','وقار ہر سمت چھا رہا ہے، دلوں کی عظمت بڑھا رہا ہے','First: Dignity is spreading in every direction, increasing the greatness of hearts.','لومړی: وقار هر لور خپرېږي، د زړونو عظمت زیاتوي'),
('دوسرا','حضور تشریف لا رہی ہیں، کھڑے ہوں خدام سر جھکا کر','Second: Her Majesty is coming; let the servants stand with bowed heads.','دویم: حضور تشریف راوړي، خدام دې سر ټیټ کړي ودرېږي')]:
    add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab,verseMark='ع')
D(s,'گانا','رہیں حکم سے تخت و تاج، ملک و راج، مال و منال۔ بلند نام ہو','Song: May throne and crown, country and rule, wealth and property remain by her command; may her name be exalted…','سندره: د حکم نه تخت او تاج، هېواد او واکمني، مال او دولت وي. نوم دې لوړ وي')
F.done()
s['sourceNote']='Printed page 65 (scan 73): continuation of the drama; the first two lines are a verse of Neki continued from the previous page; the poem lines of the court chant (courtiers) are marked “ع” at the left in print; stage directions in parentheses. The song continues on the next page.'+NOTE
s['vocabulary']={}
save(s)
# scan 74 = printed 66
s=page(74,'p09','66','Khoobsurat Bala, part 4','خوب صورت بلا (حصہ چہارم)','ښکلې بلا (څلورمه برخه)','l4')
F=Flow(s)
V(s,'دن بدن عزّت بڑھے، جاہ و جلال، زمیں پہ آج ہے جس طرح آسمان محیط / یونہی جہاں پہ چھایا رہے تیرا اقبال۔ رہیں ………','May honour increase day by day; your majesty and glory are on the earth today just as the sky encompasses it; / thus may your fortune keep covering the world. May … remain …','ورځ په ورځ دې عزت زیات شي، جاه او جلال، نن پر ځمکه دی لکه اسمان چې پرې احاطه کړې / همداسې دې پر نړۍ ستا اقبال خپور وي. وي ………')
P(s,'(سہیلیوں کا ناچتے اور گاتے ہوئے اندر جانا)','(The companions go inside dancing and singing.)','(ملګرې نڅا او سندرې کولو سره دننه ځي)')
D(s,'شمسہ','جاؤ! اُس ضدی کو میرے سامنے لاؤ۔ ضد کس سے؟ مجھ سے جو طوفانی سمندر کی طرح غصے میں دیوانی ہو جاتی ہے، جو دم کے دم میں آندھی کی طرح بلائے ناگہانی ہو جاتی ہے۔ اگر یہ راہ پر نہ آیا، تو پھر اس کو دنیا میں جینے کا کوئی حق نہیں۔','Shamsa: Go! Bring that stubborn one before me. Stubbornness with whom? With me, who, like a stormy sea, becomes mad in rage, who in a moment becomes a sudden calamity like a whirlwind. If he does not come to the right path, then he has no right to live in this world.','شمسه: ځئ! هغه ضدي زما مخې ته راوړئ. ضد له چا سره؟ له ما سره چې د طوفاني سمندر په څېر په غصه کې لېونۍ کېږم، چې په یوه شېبه کې د طوفان په څېر ناڅاپي بلا ګرځم. که دا په لاره رانغی نو بیا هغه ته په نړۍ کې د ژوند کوم حق نشته.')
P(s,'(قتلو کا توفیق کو پا بہ زنجیر سامنے لانا)','(Qatlu brings Tawfeeq before her in chains.)','(قتلو توفیق په ځنځیرونو سره مخې ته راوړي)')
D(s,'شمسہ','کیوں توفیق کس حال میں ہے!','Shamsa: Well, Tawfeeq, in what state are you!','شمسه: ولې توفیقه په کوم حال کې یې!')
D(s,'توفیق','کس حال میں ہے؟ شیر لوہے کے جال میں ہے۔','Tawfeeq: In what state? The lion is in a net of iron.','توفیق: په کوم حال کې؟ زمری د اوسپنې په جال کې دی.')
D(s,'شمسہ','سرکش!','Shamsa: Rebel!','شمسه: سرکشه!')
V(s,'کیوں تباہی لا رہا ہے اپنے عزّ و جاہ پر / چھوڑ دے گم راہی، آ جا اب بھی سیدھی راہ پر','Why are you bringing destruction on your honour and rank? / Give up straying; come even now on the straight path.','ولې خپل عز او جاه ته تباهي راوړې / ګمراهي پرېږده، اوس هم په سمه لار راشه')
D(s,'توفیق','دنیا میں سچی اور سیدھی راہ فقط نیکی ہے جو قبر کے دروازے سے نکال کر قیامت کے میدان سے ہوتی ہوئی بہشت کے دربار میں پہنچاتی ہے۔ باقی ہر ایک راہ ٹھوکر کہلاتی ہے، کانٹوں میں پھنساتی ہے اور آخر کار جہنم کے اندھیرے غار میں گراتی ہے۔','Tawfeeq: In this world the true and straight path is only goodness, which takes one out of the door of the grave and, passing through the field of the Resurrection, brings one to the court of Paradise. Every other path is called a stumble, entangles in thorns and finally throws one into the dark cave of Hell.','توفیق: په نړۍ کې رښتینې او سمه لار یوازې نېکي ده چې د قبر له دروازې راوباسي او د قیامت د میدان له لارې د جنت دربار ته رسوي. پاتې هره لار ټکر بلل کېږي، په خاروو کې ښکېلوي او په پای کې د دوزخ په تیاره غار کې غورځوي.')
V(s,'پروا نہیں جو آج زمانہ خلاف ہے / رستہ وہی چلوں گا، جو سیدھا و صاف ہے','No matter that today the age is against me; / I will walk only the path that is straight and clear.','پروا نشته که نن زمانه مخالفه ده / همدا لار به ځم چې سمه او پاکه ده')
V(s,'دکھ اور سکھ تو بیچ ہیں، میری نگاہ میں / میں جان بھی جو دوں گا، تو نیکی کی راہ میں','Sorrow and joy are trifles in my sight; / if I give even my life, it will be on the path of goodness.','دکھ او سکون زما په نظر کې بې ارزښته دي / که ساه هم ورکړم نو د نېکۍ په لاره کې به یې ورکړم')
D(s,'شمسہ','میں نہیں سمجھتی، نیکی کیا چیز ہے؟ جو تجھ کو اور تیرے جیسے چند بے وقوفوں کو عزیز ہے۔','Shamsa: I do not understand what this goodness is, which is dear to you and a few fools like you.','شمسه: زه نه پوهېږم چې نېکي څه شی دی؟ چې تا او ستا په څېر څو بې عقلو ته ګرانه ده.')
F.done()
s['sourceNote']='Printed page 66 (scan 74): continuation of the drama (speaker labels in blue: شمسہ, توفیق); the first two lines complete the courtiers’ song of the previous page; stage directions in parentheses. The Word transcription (urdu-word-part2.txt) was used as a cross-check for the continuation (it adds that Tawfeeq next speaks of “Neki as a pure light”).'+NOTE
s['vocabulary']={}
save(s)
