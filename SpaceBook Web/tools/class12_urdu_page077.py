"""Urdu XII PDF77 (spread): p.144 grammar note مرکب جملے (۳) — noun clauses (Lesson 14); p.145 Lesson 15 author note (فارغ بخاری, 1917–1997)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
g = Builder()
g.h('Compound sentences (3) — subordinate clauses', 'مرکب جملے (۳) — تابع جملے', 'مرکبې جملې (۳) — تابع جملې')
g.p('The main clause is called the principal clause (khāṣ jumla) and the dependent clause is called the subordinate clause (tābiʿ jumla). Subordinate clauses are of three kinds: noun (ismī), adjectival (wasfī) and adverbial (tamīzī).',
    'اصلی جملے کو خاص جملہ اور ماتحت جملے کو تابع جملہ کہا جاتا ہے۔ تابع جملوں کی تین اقسام ہیں۔ اسمی، وصفی، تمیزی',
    'اصلي جملې ته خاصه جمله او تابع جملې ته تابع جمله ویل کېږي. تابع جملې درې ډوله دي: اسمي، وصفي، تمیزي.')
g.p('Noun clause: such clauses usually begin with “ke” (that). For example:', 'اسمی جملہ: اس طرح کے جملوں کی ابتدا عموماً ’’کہ‘‘ سے ہوتی ہے۔ جیسے:', 'اسمي جمله: د دې ډول جملو پیل عموماً په "که" (چې) کېږي. لکه:')
g.group('lines', [
    ('He said that I am ill.', 'اُس نے کہا کہ میں بیمار ہوں۔', 'هغه وویل چې زه ناروغ یم.'),
    ('Who does not know that he is a gentleman.', 'کون نہیں جانتا کہ وہ ایک شریف آدمی ہے۔', 'څوک نه پوهېږي چې هغه یو شریف سړی دی.'),
    ('There was such commotion at the meeting that it is beyond description.', 'جلسے میں وہ ہلڑبازی ہوئی کہ بیان سے باہر ہے۔', 'په غونډه کې داسې ګډوډي وشوه چې له بیانه بهر ده.'),
])
g.p('Sometimes “ke” is dropped from short phrases and quotations. For example:', 'کبھی کبھی چھوٹے فقروں اور مقولوں سے ’’کہ‘‘ حذف ہو جاتا ہے۔ مثلاً:', 'کله کله له لنډو فقرو او مقولو "که" حذفېږي. لکه:')
g.group('lines', [('I said: go, don’t come now.', 'میں نے کہا جاؤ اب نہ آنا۔', 'ما وویل: لاړ شه، اوس مه راځه.')])
g.p('Sometimes it is used to express the reason or purpose of the verb of the principal clause; in such sentences “kyūṅ ke” or “is liye” is sometimes also used before “ke”. For example:',
    'کبھی خاص جملہ کی فعل کی وجہ یا مقصد کے اظہار کے لیے استعمال ہوتا ہے ایسے جملوں میں کبھی کبھی ’’کہ‘‘ سے پہلے ’’کیوں کہ‘‘ یا ’’اس لیے‘‘ بھی استعمال ہوتا ہے۔ جیسے:',
    'کله د خاصې جملې د فعل د لامل یا موخې د څرګندولو لپاره کارېږي؛ په داسې جملو کې کله کله له "که" مخکې "کیوں که" (ځکه چې) یا "اس لیے" (له دې امله) هم کارېږي. لکه:')
g.group('lines', [
    ('Switch off the bulb so that I can sleep.', 'بلب بُجھا دو کہ میں سو سکوں۔', 'ګروپ مړ کړه چې ویده شم.'),
    ('He loves this child very much because he is his only son.', 'وہ اس بچے سے بڑی محبت کرتا ہے اس لیے کہ وہ اُس کا اکلوتا بیٹا ہے۔', 'هغه له دې ماشوم سره ډېره مینه لري ځکه چې هغه یې یوازینی زوی دی.'),
    ('I am afraid of going out because it is dark outside.', 'میں باہر جاتے ہوئے ڈرتا ہوں کیوں کہ باہر اندھیرا ہے۔', 'زه بهر وتو ته ډارېږم ځکه چې بهر تیاره ده.'),
])
g.p('Sometimes a subordinate clause comes with “aisā na ho” (lest) to express a negative phrase, as:', 'بعض اوقات تابع جملہ منفی فقرے کے اظہار کے لیے ’’ایسا نہ ہو‘‘ کے ساتھ آتا ہے جیسے:', 'ځینې وختونه تابع جمله د منفي فقرې د څرګندولو لپاره له "ایسا نہ ہو" (داسې نه شي) سره راځي، لکه:')
g.group('lines', [('Do not tease their children, lest he become angry.', 'اُن کے بچوں کو تنگ مت کرو ایسا نہ ہو کہ وہ خفا ہو جائے۔', 'د هغو ماشومان مه ځوروه، داسې نه شي چې هغه خفه شي.')])
g.p('Sometimes a noun clause is spoken to express a prayer or wish, for example:', 'بعض اوقات اسمی جملہ کسی دُعا یا تمنا کے اظہار کے لیے بولا جاتا ہے مثلاً:', 'ځینې وختونه اسمي جمله د دعا یا ارمان د څرګندولو لپاره ویل کېږي، لکه:')
g.group('lines', [
    ('I hope that he will give me my money.', 'مجھے اُمید ہے کہ وہ مجھے میری رقم دے دے گا۔', 'هیله لرم چې هغه به ما ته زما پیسې راکړي.'),
    ('May God grant that my son succeeds in his aim.', 'اللہ کرے کہ میرا بیٹا اپنے مقصد میں کامیاب ہو جائے۔', 'خدای دې وکړي چې زما زوی په خپله موخه کې بریالی شي.'),
])
g.p('If the subordinate clause mentions something impossible or absurd, “jo” will come instead of “ke”. For example:', 'تابع جملے میں ناممکن یا محال کا ذکر ہو تو ’’کہ‘‘ کی بجائے ’’جو‘‘ آئے گا۔ جیسے:', 'که په تابع جمله کې د ناشوني یا محال یادونه وي، د "که" پر ځای "جو" راځي. لکه:')
g.group('lines', [('What nerve has he, that he should behave like this in front of me.', 'اُس کی کیا جُرأت ہے جو وہ میرے سامنے ایسی حرکت کرے۔', 'هغه څه جرئت لري چې زما مخې ته داسې حرکت وکړي.')])
g.p('Make two sentences each with all the particles used in the above noun clauses.', 'درج بالا اسمی جملوں میں استعمال ہونے والے تمام حروف سے دو دو جملے بنائیں۔', 'په پورتنیو اسمي جملو کې د کارول شویو ټولو حروفو سره دوه دوه جملې جوړې کړئ.')
gr = BOOK.record(g, 'urdu12-u14-grammar-2', 'Grammar: compound sentences (3)', 'مرکب جملے (۳)', 'مرکبې جملې (۳)', 77, [144])

a = Builder()
a.h('Farigh Bukhari', 'فارغ بخاری', 'فارغ بخاري')
a.p('Born: 1917 · Died: 1997', 'ولادت: ۱۹۱۷ء · وفات: ۱۹۹۷ء', 'زېږېدنه: ۱۹۱۷ز · مړینه: ۱۹۹۷ز')
for x in [
    ('Syed Mir Ahmad Shah Bukhari was born in Peshawar. From childhood his nature was spirited. At only thirteen he joined the “Naujawan Bharat Sabha”, which played a militant role in the freedom movement. During the freedom movement and, after the creation of Pakistan, in the struggle for democracy and freedom of expression, he repeatedly endured the hardships of imprisonment.',
     'سید میر احمد شاہ بخاری پشاور میں پیدا ہوئے۔ بچپن ہی سے اُن کی طبیعت میں جولانی تھی۔ وہ صرف تیرہ سال کی عمر میں ’’نوجوان بھارت سبھا‘‘ میں شامل ہو گئے، جس نے تحریکِ آزادی میں متشدّدانہ کردار ادا کیا۔ تحریکِ آزادی اور قیامِ پاکستان کے بعد جمہوریت اور اظہارِ آزادی کے لیے جدوجہد میں بارہا قید و بند کی صعوبتیں برداشت کیں۔',
     'سید میر احمد شاه بخاري په پېښور کې زېږېدلی. له ماشومتوبه یې په طبیعت کې جوش و. یوازې په دیارلس کلنۍ کې "نوجوان بهارت سبها" سره یوځای شو، چې د خپلواکۍ په غورځنګ کې یې توندلاری رول ولوباوه. د خپلواکۍ په غورځنګ کې او د پاکستان له جوړېدو وروسته د ډیموکراسۍ او د بیان د ازادۍ لپاره په مبارزه کې یې څو ځله د بند ستونزې وزغملې.'),
    ('He was basically a scholar and poet. He was one of the founders of the Anjuman Taraqqi Pasand Musannifeen (Progressive Writers’ Association). Together with Raza Hamdani he launched the monthly “Sang-e-Meel”. The two wrote many books on Pashto language, literature and culture, including Adabiyat-e-Sarhad, Pashto Lok Geet, Sarhad ke Lok Shair, Pashto Shairi and Pashto Nasr. Zer-o-Bam, Sheeshe ke Pairahan, Khushbu ka Safar, Pyase Hath, Ghazaliya and Bichhra Sawal are collections of his poetry. In 1995 he was honoured with the Presidential Pride of Performance Award.',
     'وہ بنیادی طور پر ایک سکالر اور شاعر تھے۔ وہ انجمن ترقی پسند مصنفین کے بانیوں میں سے تھے۔ اُنھوں نے رضا ہمدانی کے ساتھ مل کر ماہنامہ ’’سنگِ میل‘‘ کا اجرا کیا۔ ان دونوں نے پشتو زبان و ادب و ثقافت سے متعلق بہت سی کتابیں تصنیف کیں۔ جن میں ادبیاتِ سرحد، پشتو لوک گیت، سرحد کے لوک شاعر، پشتو شاعری اور پشتو نثر شامل ہیں۔ زیر و بم، شیشے کے پیراہن، خوشبو کا سفر، پیاسے ہاتھ، غزلیہ، اور بچھڑا ساول اُن کی شاعری کے مجموعے ہیں۔ اُنھیں ۱۹۹۵ء میں صدارتی ایوارڈ برائے حسنِ کارکردگی سے نوازا گیا۔',
     'هغه په بنسټیز ډول یو پوه او شاعر و. د ترقي‌پسند لیکوالو د انجمن له بنسټګرو څخه و. د رضا همداني سره یې یوځای میاشتنۍ "سنګ میل" خپره کړه. دواړو د پښتو ژبې، ادب او کلتور په اړه ډېر کتابونه ولیکل، چې پکې ادبیات سرحد، پښتو لوک ګیت (ولسي سندرې)، د سرحد ولسي شاعران، پښتو شاعري او پښتو نثر شامل دي. زیر و بم، د ښیښې پېراهن، د خوشبو سفر، تږي لاسونه، غزلیه او بېل شوی ساول د هغه د شاعرۍ ټولګې دي. په ۱۹۹۵ز کې د ښه کارکردګۍ په ولسمشریز جایزه ونازول شو.'),
    ('Works: Bacha Khan, Album, Barat-e-Ashiqan (prose).', 'تصانیف: باچا خان، البم، براتِ عاشقاں (نثر)۔', 'تصنیفات: باچا خان، البم، برات عاشقان (نثر).'),
]: a.p(*x)
UT = ('The Bird of the Divine Realm (Ta’ir-e-Lahooti)', 'طائرِ لاہوتی', 'لاهوتي مرغه', 'فارغ بخاری')
au = BOOK.record(a, 'urdu12-u15-author', 'About the author: Farigh Bukhari', 'فارغ بخاری (تعارف)', 'فارغ بخاري (پېژندنه)', 77, [145], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Farigh Bukhari and floral corner ornaments are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf077', 'unit': 15, 'printedPage': 145, 'description': 'p.144 grammar note (مرکب جملے ۳) follows the Lesson 14 exercise and is attached to unit 14. p.144 prints “خاص جملہ کی فعل” (gender agreement slip) — retained. Farigh Bukhari died 1997; under Pakistani copyright (life + 50 years) Lesson 15 text is still protected and is given as a paragraph-wise summary with a sourceGap note; board-written author note and exercises are transcribed.'}]

if __name__ == '__main__':
    BOOK.save(77, [(14, gr), (15, au)], issues=issues)
