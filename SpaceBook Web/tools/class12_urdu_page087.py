"""Urdu XII PDF87 (spread): printed pp.164–165 — Lesson 16 'مرید پور کا پیر' (Patras Bokhari, d.1958) text part 6 (end; source پطرس کے مضامین)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ("“Dear compatriots! Some people say that the climate of India is bad, that is, such that in India there are many defects … do you understand? (pause …) There are defects, but this thing, that is, the matter to which I have pointed, is as it were not quite correct.” (Laughter.)",
     '’’پیارے ہم وطنو! بعض لوگ کہتے ہیں کہ ہندوستان کی آب و ہوا خراب یعنی ایسی ہے کہ ہندوستان میں بہت سے نقص ہیں۔۔۔ سمجھے آپ؟ (وقفہ۔۔۔) نقص ہیں لیکن یہ بات یعنی امر جس کی طرف میں نے اشارہ کیا ہے۔ گویا چنداں صحیح نہیں‘‘۔ (قہقہہ)۔',
     '"ګرانو هېوادوالو! ځینې خلک وايي چې د هندوستان اقلیم خراب دی، یعنې داسې دی چې په هندوستان کې ډېر نیمګړتیاوې دي … پوه شوئ؟ (وقفه …) نیمګړتیاوې شته، خو دا خبره، یعنې هغه موضوع چې ما ورته اشاره وکړه، ګواکې چندان سمه نه ده." (قهقهه)'),
    ("My senses were failing. I could not understand what, after all, the thread of the speech had been. Suddenly I remembered the story of the bullocks and the way seemed to clear somewhat.",
     'حواس معطل ہو رہے تھے۔ سمجھ میں نہ آتا تھا کہ آخر تقریر کا سلسلہ کیا تھا۔ یکلخت بیلوں کی کہانی یاد آئی اور راستہ کچھ صاف ہوتا دکھائی دیا۔',
     'حواس مې له کاره وتل. نه پوهېدم چې د وینا لړۍ اخر څه وه. ناڅاپه مې د غوایانو کیسه را په یاد شوه او لار یو څه پاکه ښکاره شوه.'),
    ("“Well, the thing in fact is that in one place two bullocks lived together who, in spite of the climate and foreign rule —” (loud laughter)",
     '’’ہاں تو بات دراصل یہ ہے کہ ایک جگہ دو بیل اکٹھے رہتے تھے جو باوجود آب و ہوا اور غیر ملکی حکومت کے‘‘ (زور کا قہقہہ)',
     '"هو، نو خبره په اصل کې دا ده چې په یوه ځای کې دوه غوایان یوځای اوسېدل چې سره له اقلیم او بهرني حکومته —" (لوړه قهقهه)'),
    ("Having got this far I felt the discourse was becoming somewhat incoherent. I said, let’s start the story of the bundle of sticks.",
     'یہاں تک پہنچ کر محسوس کیا کہ کلام کچھ بے ربط سا ہو رہا ہے۔ میں نے کہا، چلو وہ لکڑی کے گٹھے کی کہانی شروع کر دیں۔',
     'تر دې ځایه چې ورسېدم، احساس مې کړ چې خبرې یو څه بې‌ربطه کېږي. ما وویل، راځه د لرګیو د بنډل کیسه پیل کړو.'),
    ("“For example, take a bundle of sticks. Sticks are often expensive. The reason is that there is much poverty in India. As it were, since most people are poor. Therefore, as it were, a bundle of sticks — that is, you see, if —” (Loud and prolonged laughter)",
     '’’مثلاً آپ لکڑیوں کے ایک گٹھے کو لیجیے۔ لکڑیاں اکثر مہنگی ملتی ہیں۔ وجہ یہ ہے کہ ہندوستان میں افلاس بہت ہے۔ گویا چونکہ اکثر غریب ہیں۔ اس لیے گویا لکڑیوں کا گٹھا یعنی آپ دیکھیے نا کہ اگر‘‘۔ (بلند اور طویل قہقہہ)',
     '"د بېلګې په توګه، د لرګیو یو بنډل واخلئ. لرګي ډېری وخت ګران وي. لامل یې دا دی چې په هندوستان کې بېوزلي ډېره ده. ګواکې ځکه چې ډېری غریبان دي. نو ګواکې د لرګیو بنډل — یعنې تاسو وګورئ کنه چې که —" (لوړه او اوږده قهقهه)'),
    ("“Gentlemen! If you do not use your reason, your nation will be destroyed. Ill-omen is hovering.” (Laughter and uproar … “Throw him out, we won’t listen.”) Sheikh Saadi has said: “When one of a people commits a folly…” (A voice came: “What is he babbling?”) Well, let that pass. In any case, no one can doubt this:",
     '’’حضرات! اگر آپ نے عقل سے کام نہ لیا تو آپ کی قوم فنا ہو جائے گی۔ نحوست منڈلا رہی ہے۔‘‘ (قہقہے اور شور و غوغا۔۔۔ اسے باہر نکالو۔ ہم نہیں سنتے) شیخ سعدی نے کہا ہے کہ ’’چو از قومے یکے بے دانشی کرد‘‘ (آواز آئی: کیا بکتا ہے) خیر اس بات کو جانے دیجیے۔ بہر حال اس بات میں تو کسی کو شبہ نہیں ہو سکتا کہ:',
     '"درنو خلکو! که تاسو له عقل نه کار وانه خیست، ستاسو قوم به فنا شي. نحوست راګرځي." (قهقهې او شور ماشور … "دی بهر کړئ، موږ نه اورو.") شیخ سعدي ویلي: "چې د یوه قوم یو کس ناپوهي وکړه…" (غږ راغی: "څه بکواس کوي؟") خیر، دا خبره پرېږدئ. هر څنګه، په دې خبره کې خو هېچا ته شک نه شي کېدای چې:'),
]: t.p(*x)
t.group('lines', [
    ('Come, nightingale, let us join in sighs and laments;', 'آ عندلیب مل کے کریں آہ و زاریاں', 'راځه بلبله، چې یوځای اسوېلي او ژړا وکړو؛'),
    ('You cry “alas, the rose!” and I shall cry “alas, my heart!”', 'تو ہائے گل پکار میں چلاؤں ہائے دل', 'ته "اې ګله!" چغه وهه او زه به "اې زړه!" چغې وهم.'),
])
for x in [
    ("This verse quickened my circulation. At the same time the people’s uproar grew too. So I began speaking with great fervour:",
     'اس شعر نے دورانِ خون کو تیز کر دیا۔ ساتھ ہی لوگوں کا شور بھی زیادہ ہو گیا۔ چنانچہ میں بڑے جوش سے بولنے لگا:',
     'دې بیت زما د وینې جریان چټک کړ. ورسره د خلکو شور هم زیات شو. نو په ډېر جوش مې خبرې پیل کړې:'),
    ("“The nations that today have climbed the sky of awakening — their lives are a highway for people, and their governments are shaking the foundations of the four corners of the world. (The people’s uproar and laughter grew even more.) The ears of the leaders of you people are bound with the bandage of selfishness. The history of the world is witness to the fact that all the departments of life ……”",
     '’’جو قومیں اس وقت بیداری کے آسمان پر چڑھی ہوئی ہیں، اُن کی زندگیاں لوگوں کے لیے شاہراہ ہیں اور ان کی حکومتیں چار دانگِ عالم کی بنیادیں ہلا رہی ہیں۔ (لوگوں کا شور اور ہنسی اور بھی بڑھتی گئی) آپ کے لیڈروں کے کانوں پر خود غرضی کی پٹی بندھی ہوئی ہے۔ دنیا کی تاریخ اس بات کی شاہد ہے کہ زندگی کے وہ تمام شعبے۔۔۔‘‘',
     '"هغه قومونه چې نن د بېدارۍ پر اسمان ختلي، ژوند یې د خلکو لپاره لویه لار ده، او حکومتونه یې د نړۍ د څلورو ګوټونو بنسټونه ښوروي. (د خلکو شور او خندا لا زیاته شوه) ستاسو د مشرانو پر غوږونو د ځان‌غوښتنې پټۍ تړل شوې. د نړۍ تاریخ پر دې شاهد دی چې د ژوند هغه ټولې څانګې …"'),
    ("But the people’s clamour and laughter grew so loud that I could not even hear my own voice. Most people had stood up and were shouting at the tops of their voices ____ I was trembling from head to foot. Someone in the crowd, like the first drop of rain, plucked up courage and threw an empty cigarette packet at me. After this four or five paper pellets fell around me on the stage, but I kept up my speech.",
     'لیکن لوگوں کا غوغا اور قہقہے اتنے بلند ہو گئے کہ میں اپنی آواز بھی نہ سن سکتا تھا۔ اکثر لوگ اٹھ کھڑے ہوئے تھے اور گلا پھاڑ پھاڑ کر کہہ رہے تھے ____ میں سر سے پاؤں تک کانپ رہا تھا۔ ہجوم میں سے کسی شخص نے بارش کے پہلے قطرے کی طرح ہمت کر کے سگریٹ کی ایک خالی ڈبیا مجھ پر پھینک دی۔ اس کے بعد چار پانچ کاغذ کی گولیاں میرے اردگرد سٹیج پر آ گریں لیکن میں نے اپنی تقریر کا سلسلہ جاری رکھا۔',
     'خو د خلکو شور ماشور او قهقهې دومره لوړې شوې چې خپل غږ مې هم نه شو اورېدلی. ډېری خلک پاڅېدلي وو او په لوړو چغو یې ویل ____ زه له سره تر پښو رپېدم. له ګڼې ګوڼې یو چا، د باران د لومړي څاڅکي په څېر، زړه وکړ او د سګرټو یوه تشه ډبلۍ یې راباندې وغورځوله. له دې وروسته څلور پنځه د کاغذ ګولۍ زما شاوخوا پر سټیج ولوېدې، خو ما خپله وینا روانه وساته.'),
    ('“Gentlemen! Remember, you will be ruined.”', '’’حضرات! تم یاد رکھو تم تباہ ہو جاؤ گے‘‘', '"درنو خلکو! یاد ولرئ، تاسو به تباه شئ."'),
    ('“You are two bullocks ……”', '’’تم دو بیل ہو ……‘‘', '"تاسو دوه غوایان یاست ……"'),
    ("But when the shower only increased, I thought it best to withdraw from this unreasonable assembly. I jumped from the stage and in one leap made for the outside through the door. The crowd too rushed after me. I did not turn to look back but ran straight on. From time to time some unsuitable words were reaching my ears. Hearing them I quickened my pace still more and made straight for the station. A train was standing at the platform. I dashed into it headlong. A moment later that train moved off from there.",
     'لیکن جب بوچھاڑ بڑھتی ہی گئی۔ تو میں نے اس نامعقول مجمع سے کنارہ کشی ہی مناسب سمجھی۔ اسٹیج سے پھلانگا اور زقند بھر کے دروازے میں سے باہر کا رخ کیا۔ ہجوم بھی میرے پیچھے لپکا۔ میں نے مڑ کر پیچھے نہ دیکھا بلکہ سیدھا بھاگتا گیا۔ وقتاً فوقتاً بعض نامناسب کلمے میرے کانوں تک پہنچ رہے تھے۔ اُن کو سن کر میں نے اپنی رفتار اور بھی تیز کر دی اور سیدھا اسٹیشن کا رخ کیا۔ ایک ٹرین پلیٹ فارم پر کھڑی تھی۔ میں بے تحاشا اس میں گھس گیا۔ ایک لمحے کے بعد وہ ٹرین وہاں سے چل دی۔',
     'خو کله چې د شیانو ورښت زیاتېده، نو ما د دې ناپوهې ګڼې ګوڼې څخه ګوښه کېدل مناسب وګڼل. له سټیج نه ټوپ شوم او په یوه ټوپ له دروازې بهر شوم. ګڼه ګوڼه هم زما پسې راوځغلېده. ما شا ته ونه کتل، بلکې سیخ وځغاستم. کله ناکله ځینې نامناسبې کلمې زما غوږونو ته رسېدې. هغه مې چې واورېدې، خپل چټکتیا مې لا زیاته کړه او سیخ سټېشن ته ورغلم. یو ریل ګاډی پر پلېټ‌فارم ولاړ و. په بېړه ورننوتم. یوه شېبه وروسته هغه ریل له هغه ځایه روان شو.'),
    ("Since that day, to this day, neither has Muridpur invited me nor have I ever felt any wish to go there.",
     'اُس دن کے بعد آج تک نہ مرید پور نے مجھے مدعو کیا ہے نہ مجھے خود وہاں جانے کی کبھی خواہش پیدا ہوئی ہے۔',
     'له هغې ورځې تر نن پورې نه مریدپور ما رابللی او نه ما ته پخپله هلته د تلو هیله پیدا شوې.'),
    ('(Patras ke Mazameen)', '(پطرس کے مضامین)', '(د پطرس مضامین)'),
]: t.p(*x)
rec = BOOK.record(t, 'urdu12-u16-text-6', 'Lesson text (6)', 'متنِ سبق (۶)', 'د لوست متن (۶)', 87, [164, 165])
issues = [{'id': 'urdu12-pdf087', 'unit': 16, 'printedPage': 164, 'description': 'Sa‘di’s Persian half-line “چو از قومے یکے بے دانشی کرد” is quoted as printed (public domain). Ellipses and dashes in the speech (“۔۔۔”, “____”) are the author’s and retained.'}]

if __name__ == '__main__':
    BOOK.save(87, [(16, rec)], issues=issues)
