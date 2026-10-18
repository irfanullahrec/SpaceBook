# -*- coding: utf-8 -*-
"""Lessons 12-15 rebuilt from source PDF 102-114 (printed 100-112). Each entry: (verse lines, Urdu tashreeh, English, Pashto)."""

T = 'تشریح (اسپیس بک): '

HAMD = [  # PDF 102-103, printed 100-101
    (['قبضہ ہو دلوں پر کیا اور اس سے سوا تیرا', 'اک بندۂ نافرماں ہے حمد سرا تیرا'],
     'اے اللہ! دلوں پر تیرا ہی قبضہ ہے بلکہ اس سے بھی بڑھ کر ہر شے پر تیری حکومت ہے۔ تیری تعریف تو ایک نافرمان بندہ بھی کرتا ہے۔',
     'O Allah, Your hold is over hearts and over far more than that; even a disobedient servant sings Your praise.',
     'اې الله! پر زړونو ستا واک دی او له دې هم زیات؛ حتی یو نافرمانه بنده هم ستا ستاینه کوي.'),
    (['گو سب سے مقدم ہے حق تیرا ادا کرنا', 'بندے سے مگر ہوگا حق کیوں کر ادا تیرا'],
     'تیرا حق ادا کرنا سب سے پہلا فرض ہے، مگر کمزور بندہ تیرا حق پوری طرح کیسے ادا کر سکتا ہے۔',
     'Fulfilling Your right comes before everything, yet how can a mere servant ever fully pay what is due to You?',
     'ستا حق ادا کول تر هر څه مخکې دي، خو بنده به ستا حق څنګه پوره ادا کړای شي.'),
    (['محرم بھی ہے ایسا ہی جیسا کہ ہے نامحرم', 'کچھ کہہ نہ سکا جس پر یاں بھید کھلا تیرا'],
     'تیرے راز سے واقف اور ناواقف دونوں برابر ہیں؛ جس پر تیرا بھید کھلا وہ حیرت میں کچھ کہہ ہی نہ سکا۔',
     'The one who knows Your secret is no different from the stranger; whoever had Your mystery revealed could say nothing.',
     'ستا په راز خبر او ناخبر یو شان دي؛ چا ته چې ستا راز څرګند شو، هغه هېڅ ونه ویلای شول.'),
    (['جچتا نہیں نظروں میں یاں خلعتِ سلطانی', 'کملی میں مگن اپنی رہتا ہے گدا تیرا'],
     'تیرے در کا فقیر شاہی لباس کو بھی خاطر میں نہیں لاتا اور اپنی سادہ کملی ہی میں خوش رہتا ہے۔',
     "Your beggar cares nothing for a king's robe of honour; he stays content in his own simple blanket.",
     'ستا سوالګر شاهي خلعت ته هم پام نه کوي او په خپله ساده کمبله کې خوښ وي.'),
    (['عظمت تری مانے بن کچھ بن نہیں آتی یاں', 'ہیں خیرہ و سرکش بھی دم بھرتے سدا تیرا'],
     'تیری عظمت کو مانے بغیر کسی کو چارہ نہیں؛ گستاخ اور سرکش بھی ہمیشہ تیرا ہی دم بھرتے ہیں۔',
     'No one can do without acknowledging Your greatness; even the insolent and the rebellious always affirm You.',
     'بې له دې چې ستا عظمت ومني، هېڅوک چاره نه لري؛ سرکښان هم تل ستا یادونه کوي.'),
    (['تو ہی نظر آتا ہے ہر شے پہ محیط ان کو', 'جو رنج و مصیبت میں کرتے ہیں گلا تیرا'],
     'جو لوگ دکھ اور مصیبت میں تجھ سے شکوہ کرتے ہیں، وہ بھی دراصل تجھے ہی ہر چیز پر چھایا ہوا دیکھتے ہیں۔',
     'Even those who complain of You in grief and hardship see You alone encompassing everything.',
     'هغوی چې په غم او مصیبت کې له تا ګیله کوي، هم یوازې تا ته پر هر څه احاطه کوونکی ګوري.'),
    (['نشے میں وہ احساں کے سرشار ہیں اور بےخود', 'جو شکر نہیں کرتے نعمت پہ ادا تیرا'],
     'جو تیری نعمتوں کا شکر ادا نہیں کر پاتے وہ دراصل تیرے احسان کے نشے میں اتنے بےخود ہیں کہ شکر کے الفاظ نہیں ملتے۔',
     'Those who fail to thank You for Your blessings are so lost in the intoxication of Your favours that they forget themselves.',
     'څوک چې ستا د نعمتونو شکر نه ادا کوي، هغوی ستا د احسان په نشه کې دومره بې خوده دي چې شکر یې هېر شوی.'),
    (['طاعت میں ادب تیرا عصیاں سے ہے گو بڑھ کر', 'عصیاں میں ہے طاعت سے اقرار سوا تیرا'],
     'اطاعت میں ادب گناہ سے بڑھ کر ہے، مگر گناہ کے بعد شرمندگی میں بندہ تیری عظمت کا اقرار اطاعت سے بھی زیادہ کرتا ہے۔',
     'Respect for You is greater in obedience than in sin, yet in sin a servant acknowledges You even more than in obedience.',
     'په اطاعت کې ستا ادب له ګناه زیات دی، خو په ګناه کې بنده له اطاعت هم زیات ستا اقرار کوي.'),
    (['آفاق میں پھیلے گی کب تک نہ مہک تیری', 'گھر گھر لیے پھرتی ہے پیغام صبا تیرا'],
     'تیری خوشبو کب تک دنیا میں نہ پھیلے گی؛ صبح کی ہوا گھر گھر تیرا پیغام پہنچا رہی ہے۔',
     'How long can Your fragrance fail to spread across the horizons? The morning breeze carries Your message from house to house.',
     'ستا خوشبویي به تر کله په نړۍ کې نه خپرېږي؛ د سهار باد ستا پیغام کور په کور وړي.'),
    (['ہر بول ترا دل سے ٹکرا کے گزرتا ہے', 'کچھ رنگِ بیاں حالیؔ ہے سب سے جدا تیرا'],
     'مقطع: اے حالی! تیرا ہر لفظ دل کو چھو کر گزرتا ہے؛ تیرا اندازِ بیان سب سے الگ ہے۔',
     'Closing couplet: O Hali, every word of yours strikes the heart as it passes; your style of expression is unlike anyone else\'s.',
     'مقطع: اې حالي! ستا هره خبره زړه ته رسېږي؛ ستا د بیان رنګ له ټولو بېل دی.'),
]

NAAT = [  # PDF 105, printed 103
    (['سوئے طیبہ بن کے ہم زائر چلے', 'شکر کی جا ہے دن اپنے پھر چلے'],
     'ہم زائر بن کر مدینہ طیبہ کی طرف روانہ ہوئے؛ یہ شکر کا مقام ہے کہ ہمارے دن پھر گئے یعنی قسمت جاگ اٹھی۔',
     'We set out for Taiba (Madina) as pilgrims; it is a moment for thanks that our fortunes have turned.',
     'موږ د زیارت کوونکو په توګه د طیبې (مدینې) په لور روان شو؛ د شکر ځای دی چې زموږ ورځې بدلې شوې.'),
    (['یا رسول اللہ ﷺ! جلدی آیئے', 'لشکرِ اندوہ میں ہم گھر چلے'],
     'یا رسول اللہ ﷺ! جلد ہماری مدد فرمائیے، ہم غموں کے لشکر میں گھرتے جا رہے ہیں۔',
     'O Messenger of Allah ﷺ, come quickly to our aid; we are being surrounded by an army of sorrows.',
     'یا رسول الله ﷺ! ژر راشئ، موږ د غمونو په لښکر کې ګېر شوي یو.'),
    (['نخلِ دل میں تھے گناہوں کے جو برگ', 'حبِ حضرت کی ہوا سے گر چلے'],
     'دل کے درخت پر گناہوں کے جو پتے تھے، وہ حضور ﷺ کی محبت کی ہوا سے جھڑ گئے۔',
     'The leaves of sin on the tree of my heart fell away in the breeze of love for the Prophet ﷺ.',
     'د زړه پر ونه د ګناهونو کومې پاڼې وې، د رسول ﷺ د مینې په باد ورژېدې.'),
    (['کیا میسر ان کو ہوتی راہِ راست', 'چال پر کب آپ کی کافر چلے'],
     'کافروں کو سیدھا راستہ کیسے ملتا، وہ کب آپ ﷺ کے طریقے پر چلے۔',
     'How could the unbelievers have found the right path when they never walked in his way?',
     'کافرانو ته به سمه لار څنګه میسر شوې وای، دوی کله ستاسو په طریقه تللي؟'),
    (['پھر رسائی کی رسا تقدیر نے', 'پھر مدینے ہو کے ہم زائر چلے'],
     'ہماری اچھی تقدیر نے پھر رسائی دی اور ہم ایک بار پھر زائر بن کر مدینہ ہو آئے۔',
     'Our good destiny granted access once more, and again we went to Madina as pilgrims.',
     'زموږ ښه برخلیک بیا لاسرسی راکړ او موږ یو ځل بیا د زائر په توګه مدینې ته لاړو.'),
    (['شوقِ دل نے کی دوبارہ رہبری', 'آگے بھی ہو آئے تھے اب پھر چلے'],
     'دل کے شوق نے دوبارہ رہنمائی کی؛ پہلے بھی حاضری دے چکے تھے، اب پھر جا رہے ہیں۔',
     'The longing of the heart guided us again; we had been before, and now we go once more.',
     'د زړه شوق بیا لارښوونه وکړه؛ مخکې هم تللي وو، اوس بیا ځو.'),
    (['راہِ حضرت میں میں اُڑتا ہوں امیرؔ', 'اُڑ کے کیا مجھ سے کوئی طائر چلے'],
     'مقطع: اے امیر! حضور ﷺ کی راہ میں میں اتنا تیز اڑتا ہوں کہ کوئی پرندہ بھی مجھ سے آگے نہیں نکل سکتا۔',
     'Closing couplet: O Ameer, on the path of the Prophet ﷺ I fly so swiftly that no bird could outfly me.',
     'مقطع: اې امیره! د حضرت ﷺ په لار کې زه داسې الوزم چې هېڅ مرغه زما مخکې نه شي الوتلای.'),
]

REFRAIN = 'کیا کیا مچی ہیں یارو! برسات کی بہاریں'
BARSAT = [  # PDF 108-109, printed 106-107
    (['ہیں اس ہوا میں کیا کیا برسات کی بہاریں', 'سبزوں کی لہلہاہٹ، باغات کی بہاریں', 'بوندوں کی جھجھاہٹ، قطرات کی بہاریں', 'ہر بات کے تماشے، ہر گھات کی بہاریں', REFRAIN],
     'برسات کی ہوا میں ہر طرف رونق ہے: سبزہ لہلہا رہا ہے، باغ کھلے ہیں، بوندوں کی آواز آ رہی ہے اور ہر طرف تماشے ہیں۔',
     'The rainy-season air is full of delights: swaying greenery, blooming gardens, the patter of drops, a show at every turn. Oh friends, what joys the rains have stirred!',
     'د برسات په هوا کې هر ډول ښکلا ده: شنه بوټي رپېږي، باغونه غوړېدلي، د څاڅکو غږ دی او هر لوري ننداره ده. اې یارانو! د برسات بهارونه څومره ګرم دي.'),
    (['جنگل سب اپنے تن پر ہریالی سج رہے ہیں', 'گل پھول جھاڑ بوٹے کر اپنی دھج رہے ہیں', 'بجلی چمک رہی ہے بادل گرج رہے ہیں', 'اللہ کے نقارے نوبت کے بج رہے ہیں', REFRAIN],
     'جنگل ہریالی کا لباس پہنے ہیں، پھول اور پودے سجے ہوئے ہیں، بجلی چمکتی اور بادل گرجتے ہیں گویا اللہ کے نقارے بج رہے ہیں۔',
     'The forests dress themselves in green, flowers and shrubs show off their finery, lightning flashes and clouds thunder as if Allah\'s drums were beating.',
     'ځنګلونه په شنه جامه سینګار شوي، ګلونه او بوټي ښکلي ښکاري، برېښنا ځلېږي او ورېځې غړمېږي لکه د الله ډولونه چې غږېږي.'),
    (['کیا کیا رکھے ہیں یارب سامان تیری قدرت', 'بدلے ہے رنگ کیا کیا ہر آن تیری قدرت', 'سب مست ہو رہے ہیں پہچان تیری قدرت', 'تیتر پکارتے ہیں سبحان تیری قدرت', REFRAIN],
     'اے رب! تیری قدرت کے کیسے کیسے سامان ہیں، ہر لمحہ رنگ بدلتی ہے؛ سب اسے پہچان کر مست ہیں اور تیتر بھی "سبحان تیری قدرت" پکارتے ہیں۔',
     'O Lord, what wonders Your power has laid out, changing colour every moment; all rejoice in recognising it, and even the partridges cry "Glory be to Your power".',
     'اې ربه! ستا قدرت څومره سامانونه لري او هره شېبه رنګ بدلوي؛ ټول یې پېژني او مست دي، او تیتر هم "سبحان ستا قدرت" چیغې وهي.'),
    (['بولیں: بئے بٹیریں قمری پکارے: لو لو', 'پی پی: کرے پپیہا بگلے پکاریں: تُو تُو', 'کیا ہُدہُدوں کی حق حق کیا فاختوں کی ہُو ہُو', 'سب رٹ رہے ہیں تجھ کو کیا پنکھ کیا پکھیرو', REFRAIN],
     'ہر پرندہ اپنی بولی میں اللہ کو یاد کر رہا ہے: بٹیر، قمری، پپیہا، بگلے، ہدہد اور فاختائیں سب اسی کا ورد کرتے ہیں۔',
     'Every bird calls in its own voice: quails, doves, the papiha, herons, hoopoes and turtle-doves all repeat Your name.',
     'هره مرغۍ په خپله ژبه یادونه کوي: بټېرې، قمرۍ، پپیها، بګلې، هدهدې او فاختې ټولې ستا نوم تکراروي.'),
    (['کیچڑ سے ہو رہی ہے جس جا زمیں پھسلنی', 'مشکل ہوئی ہے واں سے ہر اک کو راہ چلنی', 'پھسلا جو پاؤں پگڑی مشکل ہے پھر سنبھلنی', 'جوتی گری تو واں سے کیا تاب پھر نکلنی', REFRAIN],
     'کیچڑ سے زمین پھسلنی ہو گئی ہے، چلنا مشکل ہے؛ پاؤں پھسلے تو پگڑی سنبھالنا مشکل اور جوتی گرے تو نکالنا ناممکن۔',
     'Where mud has made the ground slippery, walking is hard; if a foot slips the turban is hard to save, and a shoe that falls there cannot be pulled out.',
     'چېرې چې ځمکه له خټو ښوییده شوې، تګ ستونزمن دی؛ که پښه ښوییده شي پګړۍ ساتل ګران دي او که پڼه ولوېږي بېرته نه راوځي.'),
    (['گر کر کسی کے کپڑے دلدل میں ہیں معطر', 'پھسلا کوئی کسی کا کیچڑ میں منھ گیا بھر', 'اک دو نہیں پھسلتے کچھ اس میں آن اکثر', 'ہوتے ہیں سیکڑوں کے سر نیچے پاؤں اوپر', REFRAIN],
     'کسی کے کپڑے دلدل میں لت پت ہیں، کسی کا منہ کیچڑ سے بھر گیا؛ ایک دو نہیں بلکہ سیکڑوں لوگ پھسل کر الٹے گر رہے ہیں۔',
     "Someone's clothes are soaked in the swamp, someone slips and his face is filled with mud; not one or two but hundreds tumble head down and feet up.",
     'د چا جامې په خټو کې لړلې دي، د چا مخ له خټو ډک شو؛ یو دوه نه بلکې سلګونه ښوییږي او سر ښکته پښې پورته لوېږي.'),
]

CUT = '[پہلا مصرع اسکین میں اوپر سے کٹا ہوا ہے؛ نظر آنے والے حروف بانگِ درا کے مصرعے سے مطابقت رکھتے ہیں]'
TULU = [  # PDF 112-114, printed 110-112
    (['خدائے لم یزل کا دستِ قدرت تو، زباں تو ہے', 'یقیں پیدا کر اے غافل کہ مغلوبِ گماں تو ہے'],
     'اے مسلمان! تو اللہ کی قدرت کا ہاتھ اور اس کی زبان ہے؛ اے غافل یقین پیدا کر کیونکہ تو شک کا شکار ہے۔',
     'You are the hand of power and the tongue of the Eternal God; O heedless one, create certainty, for you are overpowered by doubt.',
     'ته د تلپاتې خدای د قدرت لاس او ژبه یې؛ اې غافله! یقین پیدا کړه ځکه ته د ګومان مغلوب یې.'),
    (['پرے ہے چرخِ نیلی فام سے منزل مسلماں کی', 'ستارے جس کی گردِ راہ ہوں، وہ کارواں تو ہے'],
     'مسلمان کی منزل نیلے آسمان سے بھی آگے ہے؛ تو وہ قافلہ ہے جس کی راہ کی دھول ستارے ہیں۔',
     'The Muslim\'s destination lies beyond the blue sky; you are the caravan whose road-dust is the stars.',
     'د مسلمان منزل له شین اسمان هاخوا دی؛ ته هغه کاروان یې چې ستوري یې د لارې ګرد دي.'),
    (['مکاں فانی، مکیں آنی، ازل تیرا، ابد تیرا', 'خدا کا آخری پیغام ہے تو، جاوداں تو ہے!'],
     'دنیا اور اس کے رہنے والے فانی ہیں مگر تو اللہ کا آخری پیغام (اسلام) رکھنے والا ہے، اس لیے تو ہمیشہ رہنے والا ہے۔',
     "The dwelling is mortal and its dweller passing, yet eternity is yours; you are God's final message, you are everlasting!",
     'کور فاني او اوسېدونکی تېرېدونکی دی، خو ازل او ابد ستا دي؛ ته د خدای وروستی پیغام یې، ته تلپاتې یې!'),
    (['حنا بندِ عروسِ لالہ ہے خونِ جگر تیرا', 'تری نسبت براہیمی ہے، معمارِ جہاں تو ہے!'],
     'تیری قربانیاں دنیا کی رونق کا سبب ہیں؛ تیرا تعلق حضرت ابراہیمؑ سے ہے، تو دنیا کو نئے سرے سے تعمیر کرنے والا ہے۔',
     'Your heart\'s blood is the henna that adorns the tulip-bride; your lineage is from Abraham, you are the builder of the world!',
     'ستا د ځيګر وینه د لالې ناوې نکریزې دي؛ ستا نسبت ابراهیمي دی، ته د نړۍ معمار یې!'),
    (['تری فطرت امیں ہے ممکناتِ زندگانی کی', 'جہاں کے جوہرِ مضمر کا گویا امتحاں تو ہے!'],
     'تیری فطرت میں زندگی کے تمام امکانات امانت رکھے گئے ہیں؛ دنیا کی چھپی ہوئی صلاحیتیں تیرے ذریعے ظاہر ہوتی ہیں۔',
     "Your nature holds in trust all the possibilities of life; you are, as it were, the test of the world's hidden essence!",
     'ستا فطرت د ژوند د ټولو امکاناتو امانتداره ده؛ ته ګواکې د نړۍ د پټ جوهر ازموینه یې!'),
    (['جہانِ آب و گل سے عالمِ جاوید کی خاطر', 'نبوت ساتھ جس کو لے گئی، وہ ارمغاں تو ہے!'],
     'نبوت اس فانی دنیا سے ابدی دنیا کے لیے جو تحفہ ساتھ لے گئی وہ تو ہے، یعنی امتِ مسلمہ۔',
     'You are the gift that Prophethood carried from this world of water and clay to the everlasting world!',
     'ته هغه ډالۍ یې چې نبوت له دې اوبو او خټو نړۍ د تلپاتې نړۍ لپاره له ځان سره یوړه!'),
    (['یہ نکتہ سرگذشتِ ملتِ بیضا سے ہے پیدا', 'کہ اقوامِ زمینِ ایشیا کا پاسباں تو ہے'],
     'ملتِ اسلامیہ کی تاریخ سے یہ بات واضح ہے کہ ایشیا کی قوموں کا نگہبان تو ہی ہے۔',
     'This truth emerges from the history of the bright community: you are the guardian of the nations of Asia.',
     'له روښانه ملت تاریخ دا ټکی څرګندېږي چې د اسیا د قومونو ساتونکی ته یې.'),
    (['سبق پھر پڑھ صداقت کا، عدالت کا، شجاعت کا', 'لیا جائے گا تجھ سے کام دنیا کی امامت کا'],
     'سچائی، انصاف اور بہادری کا سبق دوبارہ یاد کر، کیونکہ تجھ سے دنیا کی رہنمائی کا کام لیا جائے گا۔',
     'Learn again the lesson of truth, of justice, of courage; you will be called upon to lead the world.',
     'د رښتینولۍ، عدالت او زړورتیا درس بیا ولوله؛ له تا به د نړۍ د امامت کار واخیستل شي.'),
    (['یہی مقصودِ فطرت ہے، یہی رمزِ مسلمانی', 'اخوت کی جہانگیری، محبت کی فراوانی'],
     'فطرت کا مقصد اور مسلمانی کا راز یہی ہے کہ بھائی چارہ ساری دنیا پر چھا جائے اور محبت عام ہو۔',
     'This is the aim of nature, this is the secret of being a Muslim: brotherhood spread across the world and love in abundance.',
     'د فطرت موخه او د مسلمانۍ راز همدا دی: په ټوله نړۍ کې ورورولي او د مینې پرېمانه والی.'),
    (['بتانِ رنگ و خوں کو توڑ کر ملت میں گم ہو جا', 'نہ تورانی رہے باقی، نہ ایرانی، نہ افغانی'],
     'رنگ و نسل کے بتوں کو توڑ کر ملت میں گم ہو جا تاکہ تورانی، ایرانی اور افغانی کی تفریق باقی نہ رہے۔',
     'Break the idols of colour and blood and lose yourself in the community, so that neither Turanian, nor Iranian, nor Afghan remains.',
     'د رنګ او وینې بتان مات کړه او په ملت کې ورک شه، چې نه توراني پاتې شي، نه ایراني او نه افغان.'),
    (['میانِ شاخساراں صحبتِ مرغِ چمن کب تک', 'ترے بازو میں ہے پروازِ شاہینِ قہستانی'],
     'کب تک باغ کے کمزور پرندوں کے ساتھ شاخوں میں رہے گا؛ تیرے بازوؤں میں پہاڑی شاہین کی پرواز کی طاقت ہے۔',
     'How long will you keep company with garden birds among the branches? Your wings hold the flight of the mountain falcon.',
     'تر کله به په څانګو کې د باغ د مرغانو سره اوسې؟ ستا په وزرونو کې د غرني باز الوت دی.'),
    (['گماں آبادِ ہستی میں یقیں مردِ مسلماں کا', 'بیاباں کی شبِ تاریک میں قندیلِ رہبانی'],
     'شک سے بھری اس دنیا میں مسلمان کا یقین ایسے ہے جیسے صحرا کی اندھیری رات میں راہب کا چراغ۔',
     "In this world full of doubt, the faith of the true Muslim is like a monk's lamp in the dark night of the desert.",
     'د ګومان په دې نړۍ کې د مسلمان یقین د دښتې په تیاره شپه کې د راهب ډیوې ته ورته دی.'),
    (['مٹایا قیصر و کسریٰ کے استبداد کو جس نے', 'وہ کیا تھا؟ زورِ حیدرؓ، فقرِ بوذرؓ، صدقِ سلمانیؓ'],
     'قیصر و کسریٰ کے ظلم کو مٹانے والی طاقت حضرت علیؓ کی قوت، حضرت ابوذرؓ کا فقر اور حضرت سلمانؓ کی سچائی تھی۔',
     "What was it that destroyed the tyranny of Caesar and Chosroes? The strength of Haidar (Ali), the poverty of Abu Dharr, the truthfulness of Salman.",
     'هغه څه وو چې د قیصر او کسرا ظلم یې له منځه یووړ؟ د حیدر ځواک، د ابوذر فقر او د سلمان رښتینولي.'),
    (['ہوئے احرارِ ملت جادہ پیما کس تجمل سے', 'تماشائی شگافِ در سے ہیں صدیوں کے زندانی'],
     'ملت کے آزاد لوگ کس شان سے آگے بڑھے کہ صدیوں سے غلامی میں قید قومیں دروازے کی درز سے انھیں دیکھ رہی ہیں۔',
     'With what splendour the free men of the community set forth, while the prisoners of centuries watch through cracks in the door!',
     'د ملت ازاد خلک په څه شان روان شول، چې د پېړیو بندیان یې د دروازې له درز څخه ننداره کوي!'),
    (['ثباتِ زندگی ایمانِ محکم سے ہے دنیا میں ' + CUT, 'کہ المانی سے بھی پائندہ تر نکلا ہے تورانی'],
     'دنیا میں زندگی کی پائیداری پختہ ایمان سے ہے؛ اسی لیے ترک قوم جرمنوں سے بھی زیادہ مضبوط نکلی۔',
     'Permanence of life in this world comes from firm faith; that is why the Turanian proved more enduring than the German.',
     'په نړۍ کې د ژوند ټینګښت له ټینګ ایمان دی؛ له همدې امله توراني له الماني هم ټینګ ووت.'),
    (['جب اس انگارۂ خاکی میں ہوتا ہے یقیں پیدا', 'تو کر لیتا ہے یہ بال و پرِ روح الامیں پیدا'],
     'جب مٹی کے اس انسان میں یقین پیدا ہو جاتا ہے تو وہ جبرائیلؑ جیسے پَر پیدا کر لیتا ہے۔',
     'When certainty is born in this ember of dust, it grows the wings and feathers of the Trustworthy Spirit (Gabriel).',
     'کله چې په دې خاوري انګار کې یقین پیدا شي، دا د روح الامین (جبرائیل) وزرونه او بڼکې پیدا کوي.'),
]

LESSONS = {
    12: dict(poem=HAMD, kind='couplet', pdf=[102, 103], source='(کلامِ حالی)'),
    13: dict(poem=NAAT, kind='couplet', pdf=[104, 105, 106], source='(کلیاتِ امیر مینائی)'),
    14: dict(poem=BARSAT, kind='band', pdf=[107, 108, 109, 110], source='(کلیاتِ نظیر)'),
    15: dict(poem=TULU, kind='couplet', pdf=[111, 112, 113, 114], source='(بانگِ درا)'),
}
NUM = '۰۱۲۳۴۵۶۷۸۹'


def urdu_num(n):
    return ''.join(NUM[int(c)] for c in str(n))


def sections(n):
    spec = LESSONS[n]
    out = []
    for i, (lines, tash, en, ps) in enumerate(spec['poem'], 1):
        if spec['kind'] == 'band':
            head, hps, hen = f'بند {urdu_num(i)}', f'{i} بند', f'Stanza {i}'
        else:
            head, hps, hen = f'شعر {urdu_num(i)}', f'{i} شعر', f'Couplet {i}'
        if i == 1 and spec['kind'] == 'couplet':
            head += ' (مطلع)'; hen += ' (opening couplet)'
        out.append(dict(heading=head, headingPs=hps, headingEn=hen,
                        urdu='\n'.join(lines) + '\n\n' + T + tash, english=en, pashto=ps))
    return out


def full_text(n, title, poet):
    spec = LESSONS[n]
    body = '\n\n'.join('\n'.join(lines) for lines, *_ in spec['poem'])
    return f'نظم / کلام: {title}\nشاعر: {poet}\n\n{body}\n\n{spec["source"]}'
