"""HPE XII PDF54–59: pp.49–54 — chapter 5 (Verbal and Physical Violence) complete with exercise; chapter 6 (Sports and Biomechanical Principles)
opener, motion, force, Newton’s laws, equilibrium, centre of gravity. Run: python class12_hpe_page054.py N (54–59)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p54():
    b = Builder()
    b.h('Chapter 5: Verbal and Physical Violence', 'باب نمبر ۵: زبانی و جسمانی تشدد', '۵ څپرکی: ژبنی او فزیکي تاوتریخوالی')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('know the difference between physical and verbal violence.', 'جسمانی اور زبانی تشدد کا فرق جان سکیں۔', 'د فزیکي او ژبني تاوتریخوالي توپیر وپېژني.'),
          ('identify such individual and social factors as promote behaviour based on cooperation and respect, and discourage behaviour based on violence and disrespect.', 'ایسے انفرادی اور معاشرتی عوامل کی نشاندہی کر سکیں جو تعاون اور احترام پر مبنی رویے کو فروغ دیں اور تشدد اور عدم احترام پر مبنی رویے کی حوصلہ شکنی کریں۔', 'هغه انفرادي او ټولنیز لاملونه وپېژني چې پر همکارۍ او درناوي ولاړ چلند وده ورکړي او پر تاوتریخوالي او بې‌احترامۍ ولاړ چلند ونه هڅوي.')])
    b.h('Physical and verbal violence', 'جسمانی اور زبانی تشدد', 'فزیکي او ژبنی تاوتریخوالی')
    P(b, [('It is such an oppressive behaviour as one individual causes harm to other individuals physically, mentally and emotionally, and becomes the cause of physical and verbal violence. Therefore in every case a reason should be created to avoid it; rather people should themselves be aware of the results arising from physical and verbal violence and should make other individuals aware too.',
           'یہ ایسا ظالمانہ رویہ ہے جو دوسرے فرد یا افراد کو جسمانی، ذہنی اور جذباتی لحاظ سے نقصان پہنچاتا ہے اور جسمانی و زبانی تشدد کا باعث بنتا ہے۔ لہٰذا کسی بھی صورت اس سے بچنے کا سبب پیدا کیا جائے بلکہ جسمانی اور زبانی تشدد سے پیدا ہونے والے نتائج سے خود بھی آگاہ رہیں اور دیگر افراد کو بھی آگاہ کیا جائے۔',
           'دا داسې ظالمانه چلند دی چې بل فرد یا افرادو ته په فزیکي، رواني او احساساتي لحاظ زیان رسوي او د فزیکي او ژبني تاوتریخوالي لامل کېږي. نو په هر صورت دې له دې د ژغورنې لامل پیدا شي، بلکې له فزیکي او ژبني تاوتریخوالي پیدا شویو پایلو پخپله خبر اوسئ او نور کسان هم خبر کړئ.')])
    b.h('Difference between physical and verbal violence', 'جسمانی اور زبانی تشدد میں فرق', 'د فزیکي او ژبني تاوتریخوالي توپیر')
    P(b, [('In physical violence physical pain is caused to another individual. For example:', 'جسمانی تشدد میں دوسرے فرد کو جسمانی تکلیف پہنچائی جاتی ہے۔ مثلاً', 'په فزیکي تاوتریخوالي کې بل فرد ته بدني تکلیف رسول کېږي. د بېلګې په توګه:')])
    L(b, [('Wounding some individual.', 'کسی فرد کو زخمی کرنا۔', 'یو فرد ټپي کول.'),
          ('Laying hands on someone’s collar.', 'کسی کے گریبان پر ہاتھ ڈالنا۔', 'د چا پر ګرېوان لاس اچول.'),
          ('Hitting someone with something or throwing it towards him with the aim of wounding.', 'کسی کو کوئی چیز مارنا یا اس کی طرف زخمی کرنے کی غرض سے پھینکنا۔', 'چا ته کوم شی وهل یا د ټپي کولو په موخه ور ګوزارول.'),
          ('Causing harm to life, property and honour.', 'جان، مال اور عزت کو نقصان پہنچانا۔', 'ځان، مال او عزت ته زیان رسول.')])
    r = rec(b, 5, 1, 54, first=True)
    deco(r, 'A black silhouette of one figure striking another is decorative.')
    BOOK.save(54, [(5, r)], issues=[{'id': 'hpe12-pdf054', 'unit': 5, 'printedPage': 49,
               'description': 'The second objective line is cut at the left edge (“رویے کو”). “لہٰذا کسی بھی صورت اس سے بچنے کا سبب پیدا کیا جائے”. Retained as printed.'}])


def p55():
    b = Builder()
    P(b, [('Verbal violence means the use of improper words against someone, and such words as are unpleasant for others and hurt them or from which provocation spreads, for example:',
           'زبانی تشدد سے مراد کسی کے خلاف نازیبا الفاظ کا استعمال اور ایسے کلمات جو دوسروں کو ناگوار گزرے اور دل آزاری ہو یا اس سے اشتعال پھیلے مثلاً',
           'له ژبني تاوتریخوالي مراد د چا پر وړاندې د ناوړه کلمو کارول او داسې خبرې دي چې نورو ته ناخوښه وي او زړه یې ازار کړي یا ترې پارونه خپره شي، لکه:')])
    L(b, [('Calling by bad names.', 'بُرے ناموں سے پکارنا۔', 'په بدو نومونو بلل.'), ('Threatening.', 'دھمکی دینا۔', 'ګواښل.'), ('Spreading rumours.', 'افواہ پھیلانا۔', 'اوازې خپرول.'),
          ('Slandering.', 'تہمت لگانا۔', 'تور لګول.'), ('Mocking.', 'مذاق اُڑانا۔', 'ټوکې پرې کول.'), ('Abusing.', 'گالی گلوچ کرنا۔', 'کنځل کول.'),
          ('Lying and misstatement.', 'جھوٹ اور غلط بیانی کرنا۔', 'دروغ او ناسم بیان.'), ('Provoking.', 'اشتعال دلانا۔', 'پارول.'),
          ('Presenting the matter of someone’s home in a wrong manner.', 'کسی کے گھر کی بات کو غلط انداز میں پیش کرنا۔', 'د چا د کور خبره په ناسم ډول وړاندې کول.'),
          ('Writing wrong messages or nonsense on the mobile phone.', 'موبائل فون پر غلط میسیج یا لغو باتیں لکھنا۔', 'په ګرځنده ټیلیفون ناسم پیغامونه یا بې‌ځایه خبرې لیکل.')])
    P(b, [('All these acts come in the category of verbal violence, from which the matter can reach provocation and quarrel, and its results can also be dangerous.',
           'یہ تمام کام زبانی تشدد کے زمرے میں آتے ہیں جن سے اشتعال اور جھگڑے تک بات پہنچ سکتی ہے اور اس کے خطرناک نتائج بھی ہو سکتے ہیں۔',
           'دا ټول کارونه د ژبني تاوتریخوالي په ډله کې راځي چې له امله یې خبره تر پارونې او شخړې رسېدای شي او خطرناکې پایلې یې هم کېدای شي.')])
    b.h('Individual violence', 'انفرادی تشدد', 'انفرادي تاوتریخوالی')
    P(b, [('Every human wants that in society he be seen with respect. Some powerful people try to forcibly suppress others on the strength of power, or try to dominate them, or try to adopt negative behaviour and tricks against other individuals so that they can keep their awe and authority established.',
           'ہر انسان چاہتا ہے کہ معاشرے میں اسے عزت کی نگاہ سے دیکھا جائے۔ بعض طاقتور لوگ زبردستی دوسروں کو طاقت کے بل بوتے پر دبانے کی کوشش کرتے ہیں یا ان پر حاوی ہونے کی کوشش کرتے ہیں یا دوسرے افراد کے خلاف منفی رویہ اور چالیں چلنے کی کوشش کرتے ہیں تاکہ وہ اپنا رعب و دبدبہ قائم رکھ سکے۔',
           'هر انسان غواړي چې په ټولنه کې په درنه سترګه وکتل شي. ځینې ځواکمن خلک هڅه کوي چې په زور د ځواک په مټ نور وځپي یا پرې برلاسي شي یا د نورو کسانو پر وړاندې منفي چلند او چلونه وکاروي ترڅو خپل رعب او دبدبه وساتي.')])
    L(b, [('Through this he hurts others.', 'اس سے وہ دوسروں کی دل آزاری کرتا ہے۔', 'په دې سره د نورو زړونه ازاروي.')])
    r = rec(b, 5, 2, 55)
    BOOK.save(55, [(5, r)], issues=[{'id': 'hpe12-pdf055', 'unit': 5, 'printedPage': 50,
               'description': 'Large owner ballpoint signatures and scribbles over the left half of the list (names, “M Kamran”, Urdu writing) are excluded; the printed list is legible beneath. “کلمات جو دوسروں کو ناگوار گزرے”, “تاکہ وہ اپنا رعب … قائم رکھ سکے”. Retained as printed.'}])


def p56():
    b = Builder()
    L(b, [('He forcibly plays with their emotions.', 'جبراً ان کے جذبات سے کھیلتا ہے۔', 'په زور د هغوی له احساساتو لوبې کوي.'),
          ('He uses his power without justification.', 'اپنی طاقت کا بلا جواز استعمال کرتا ہے۔', 'خپل ځواک بې‌جوازه کاروي.')])
    P(b, [('This behaviour, instead of giving him respect, creates hatred in the hearts of others, from which at any time someone, getting fed up, takes such a step as becomes unbearable for both, so much so that incidents up to murder happen.',
           'یہ رویہ اسے عزت دینے کے بجائے دوسروں کے دلوں میں نفرت پیدا کرتا ہے جس سے کسی بھی وقت کوئی تنگ آ کر ایسا قدم اٹھا لیتا ہے جو دونوں کے لیے ناقابلِ برداشت ہو جاتا ہے یہاں تک کہ قتل تک کے واقعات ہو جاتے ہیں۔',
           'دا چلند هغه ته د عزت ورکولو پر ځای د نورو په زړونو کې کرکه پیدا کوي چې له امله یې هر وخت څوک تنګ شي او داسې ګام پورته کړي چې دواړو ته د زغم وړ نه وي، تر دې چې د وژنې پېښې هم کېږي.')])
    b.h('Social violence', 'معاشرتی تشدد', 'ټولنیز تاوتریخوالی')
    P(b, [('Society too is formed by the meeting of humans; in it are included all matters of individual and collective, verbal and physical violence, because of which disorder arises in society, and individuals who are victims of insecurity become compelled to such steps as become a canker for society.',
           'معاشرہ بھی انسانوں کے ملنے سے بنتا ہے اس میں انفرادی و اجتماعی، زبانی و جسمانی تشدد کی تمام باتیں شامل ہوتی ہیں جن کی وجہ سے معاشرے میں بگاڑ پیدا ہوتا ہے اور عدمِ تحفظ کے شکار افراد ایسے اقدامات پر مجبور ہو جاتے ہیں جو معاشرے کیلئے ناسور بن جاتے ہیں۔',
           'ټولنه هم د انسانانو له یوځای کېدو جوړېږي؛ په کې د انفرادي او ټولیز، ژبني او فزیکي تاوتریخوالي ټولې خبرې شاملې وي چې له امله یې په ټولنه کې خرابي پیدا کېږي او د ناامنۍ ښکار کسان داسې ګامونو ته اړ کېږي چې ټولنې ته ناسور ګرځي.'),
          ('In social violence a group of a few individuals deliberately harasses others. It makes them restless and tries to display its power, and tries to forcibly get its word or order obeyed. In society a trend of violence is born and becomes the cause of the deterioration of society.',
           'معاشرتی تشدد میں چند افراد کا گروپ جان بوجھ کر دوسروں کو تنگ کرتا ہے۔ انھیں بے سکون کرتا ہے اور اپنی طاقت کا مظاہرہ کرنے کی کوشش کرتا ہے اور زبردستی اپنی بات یا حکم منوانے کی کوشش کرتا ہے۔ معاشرہ میں تشدد کا رجحان جنم لیتا ہے اور معاشرے کی ابتری کا باعث بنتا ہے۔',
           'په ټولنیز تاوتریخوالي کې د څو کسانو ډله په قصد نور ځوروي، بې‌ارامه یې کوي او د خپل ځواک د ښودلو هڅه کوي او په زور د خپلې خبرې یا حکم د منلو هڅه کوي. په ټولنه کې د تاوتریخوالي تمایل زېږي او د ټولنې د خرابۍ لامل کېږي.')])
    b.h('Positive and negative activities', 'مثبت اور منفی سرگرمیاں', 'مثبت او منفي فعالیتونه')
    b.h('Positive activities', 'مثبت سرگرمیاں', 'مثبت فعالیتونه')
    P(b, [('Mixing in society; taking part individually and collectively in sorrow and pain; helping others; resolving matters with soft tone and love; creating tolerance; helping others; making others aware of unethical and illegal works; protecting the honour, life and property of others; remembering others with good words in their absence; taking part in good works and social works; being of use to one’s companions, neighbours and relatives in times of difficulty, etc. — these activities end negative trends in society and prove helpful in ending every kind of hooliganism.',
           'معاشرے میں میل ملاپ، انفرادی اور اجتماعی طور پر دکھ درد میں شرکت کرنا، دوسروں کی مدد کرنا، نرم لہجے اور پیار سے معاملات کو سلجھانا، برداشت پیدا کرنا، دوسروں کی مدد کرنا، غیر اخلاقی اور غیر قانونی کاموں سے دوسروں کو آگاہ کرنا، دوسروں کی عزت جان و مال کی حفاظت کرنا، عدم موجودگی میں اچھے الفاظ سے دوسروں کو یاد کرنا، اچھے کاموں میں اور سماجی کاموں میں حصہ لینا، مشکل کے وقت اپنے ساتھیوں محلہ داروں رشتے داروں کے کام آنا وغیرہ یہ سرگرمیاں معاشرے سے منفی رجحانات کا خاتمہ کرتی ہیں اور ہر قسم کی غنڈہ گردی کا خاتمہ کرنے میں معاون ثابت ہوتی ہیں۔',
           'په ټولنه کې ګډ ژوند، په انفرادي او ټولیز ډول په غم او درد کې ګډون، د نورو مرسته، په نرم لهجه او مینه د چارو حل، زغم پیدا کول، د نورو مرسته، نور له غیر اخلاقي او غیر قانوني کارونو خبرول، د نورو د عزت، ځان او مال ساتنه، د نشتوالي پر مهال نور په ښو ټکو یادول، په ښو او ټولنیزو کارونو کې برخه اخیستل، د ستونزې پر مهال د خپلو ملګرو، ګاونډیانو او خپلوانو په کار راتلل او نور — دا فعالیتونه له ټولنې منفي تمایلات له منځه وړي او د هر ډول غنډه‌ګرۍ په پای ته رسولو کې مرستندوي ثابتېږي.')])
    r = rec(b, 5, 3, 56)
    BOOK.save(56, [(5, r)], issues=[{'id': 'hpe12-pdf056', 'unit': 5, 'printedPage': 51,
               'description': '“دوسروں کی مدد کرنا” appears twice in the list of positive activities. Retained as printed.'}])


def p57():
    b = Builder()
    b.h('Negative activities', 'منفی سرگرمیاں', 'منفي فعالیتونه')
    P(b, [('Verbal violence, physical violence and all forms of individual violence come in negative activities: calling by a wrong name, using insulting words, wounding, using such words religiously and sexually as hurt, causing harm to someone’s good name, causing harm to someone’s property and wealth, dishonouring, threatening etc. — all these activities are called negative activities. Through them disorder arises personally and socially, whose dangerous results come forward.',
           'زبانی تشدد، جسمانی تشدد اور انفرادی تشدد کی تمام صورتیں منفی سرگرمیوں میں آتی ہیں۔ غلط نام سے پکارنا، توہین آمیز الفاظ استعمال کرنا، زخمی کرنا، مذہبی اور جنسی طور پر ایسے الفاظ استعمال کرنا جن سے دل آزاری ہو۔ کسی کی نیک نامی کو نقصان پہنچانا، کسی کی جائیداد و مال کو نقصان پہنچانا، آبرو ریزی کرنا، دھمکی دینا وغیرہ یہ تمام سرگرمیاں منفی سرگرمیاں کہلاتی ہیں۔ ان سے ذاتی اور معاشرتی طور پر بگاڑ پیدا ہوتا ہے جس کے خطرناک نتائج سامنے آتے ہیں۔',
           'ژبنی تاوتریخوالی، فزیکي تاوتریخوالی او د انفرادي تاوتریخوالي ټولې بڼې په منفي فعالیتونو کې راځي: په ناسم نوم بلل، سپکاوي‌لرونکي ټکي کارول، ټپي کول، په دیني او جنسي ډول داسې ټکي کارول چې زړه ازار کړي، د چا نېک نوم ته زیان رسول، د چا ملکیت او مال ته زیان رسول، بې‌عزتي کول، ګواښل او نور — دا ټول فعالیتونه منفي فعالیتونه بلل کېږي. له دوی شخصي او ټولنیزه خرابي پیدا کېږي چې خطرناکې پایلې یې مخې ته راځي.')])
    r = rec(b, 5, 4, 57)
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('Write the answers to the following questions.', 'درج ذیل سوالوں کے جوابات تحریر کریں۔', 'د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('1) Define violence and write a note on physical violence.', '1) تشدد کی تعریف کریں اور جسمانی تشدد پر نوٹ لکھیں۔', '1) تاوتریخوالی تعریف کړئ او پر فزیکي تاوتریخوالي یادښت ولیکئ.'),
                      ('2) Explain the activities that increase and reduce violence.', '2) تشدد کو بڑھانے اور کم کرنے والی سرگرمیوں کی وضاحت کریں۔', '2) د تاوتریخوالي زیاتوونکي او کموونکي فعالیتونه روښانه کړئ.'),
                      ('3) Make clear the difference between physical and verbal violence.', '3) جسمانی اور زبانی تشدد کا فرق واضح کریں۔', '3) د فزیکي او ژبني تاوتریخوالي توپیر روښانه کړئ.')])
    ex = BOOK.record(e, 'hpe12-ch5-exercise', 'Chapter 5 exercise', 'باب ۵: مشقی سوالات', '۵ څپرکی: تمریني پوښتنې', 57, [52])
    BOOK.save(57, [(5, r), (5, ex)], complete_units=[5])


def p58():
    b = Builder()
    b.h('Chapter 6: Sports and Biomechanical Principles', 'باب نمبر ۶: کھیل اور بائیو مکینیکل اصول', '۶ څپرکی: لوبې او بایومیخانیکي اصول')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('use biomechanical principles to improve their performance during gymnastics and games.', 'جمناسٹک اور کھیلوں کے دوران اپنی کارکردگی کی بہتری کے لیے بائیو مکینیکل اصول استعمال کر سکیں۔', 'د جمناسټیک او لوبو پر مهال د خپلو کړنو د ښه والي لپاره بایومیخانیکي اصول وکاروي.'),
          ('give a practical demonstration of the use of the skills of motion, concepts, power and biomechanical principles of motion (e.g. basketball, volleyball, cricket, hockey and long jump etc.).', 'حرکت کی مہارتوں، تصورات، طاقت اور حرکت کے بائیو مکینیکل اصولوں کے استعمال کا عملی مظاہرہ کر سکیں (جیسا کہ باسکٹ بال، والی بال، کرکٹ، ہاکی اور لانگ جمپ وغیرہ)۔', 'د حرکت د مهارتونو، تصورونو، ځواک او د حرکت د بایومیخانیکي اصولو د کارولو عملي ښودنه وکړي (لکه باسکټبال، والیبال، کرکټ، هاکي او اوږد ټوپ او نور).')])
    b.h('Biomechanical principles', 'بائیو مکینیکل اصول', 'بایومیخانیکي اصول')
    P(b, [('The study of the motion of the human body and living things under the influence of force is called biomechanics. The motion of living things is according to biomechanical principles. By understanding them and acting on them performance can be improved. In sports the following biomechanical principles are of importance.',
           'قوت کے زیرِ اثر انسانی جسم اور جانداروں کی حرکت کے مطالعے کو بائیو مکینکس کہتے ہیں۔ جانداروں کی حرکت بائیو مکینیکل اصول کے مطابق ہوتی ہے۔ ان کو سمجھنے اور ان پر عمل کرنے سے پرفارمنس کو بہتر کیا جا سکتا ہے۔ کھیلوں میں مندرجہ ذیل بائیو مکینیکل اصول اہمیت کے حامل ہیں۔',
           'د ځواک تر اغېز لاندې د انسان بدن او ژوندیو د حرکت مطالعې ته بایومیخانیک ویل کېږي. د ژوندیو حرکت د بایومیخانیکي اصولو سره سم وي. د دوی په پوهېدو او پرې عمل کولو سره کړنې ښې کېدای شي. په لوبو کې لاندې بایومیخانیکي اصول اهمیت لري.')])
    b.h('Motion', 'حرکت (Motion)', 'حرکت (Motion)')
    P(b, [('If some body is changing its place with respect to another body or the environment, it is called motion.', 'اگر کوئی جسم دوسرے جسم یا ماحول کے لحاظ سے اپنی جگہ تبدیل کر رہا ہو تو اسے حرکت کہتے ہیں۔', 'که یو جسم د بل جسم یا چاپېریال په پرتله خپل ځای بدلوي، حرکت ورته ویل کېږي.')])
    b.h('Force', 'قوت (Force)', 'ځواک (Force)')
    P(b, [('Force is that agent which produces motion in a stationary body or stops the motion of a moving body.', 'قوت وہ عامل ہے جو کسی ساکن جسم میں حرکت پیدا کرے یا پھر کسی متحرک جسم کی حرکت کو روکے۔', 'ځواک هغه عامل دی چې په ولاړ جسم کې حرکت پیدا کړي یا د خوځنده جسم حرکت ودروي.')])
    r = rec(b, 6, 1, 58, first=True)
    BOOK.save(58, [(6, r)])


def p59():
    b = Builder()
    b.h('Newton’s laws of Motion', 'نیوٹن کے قوانینِ حرکت (Newton\'s laws of Motion)', 'د نیوټن د حرکت قوانین (Newton\'s laws of Motion)')
    P(b, [('Newton’s laws related to motion have a basic status in present physical science. These laws are as follows.', 'حرکت کے متعلق نیوٹن کے قوانین موجودہ طبعی سائنس میں بنیادی حیثیت کے حامل ہیں۔ یہ قوانین مندرجہ ذیل ہیں۔', 'د حرکت اړوند د نیوټن قوانین په اوسني فزیکي ساینس کې بنسټیز دریځ لري. دا قوانین دا دي.')])
    b.h('First law of Motion', 'پہلا قانونِ حرکت (First law of Motion)', 'د حرکت لومړی قانون (First law of Motion)')
    P(b, [('In the absence of any external force, a stationary body always remains at rest, and a moving body continues its motion with uniform speed in a straight line. This law is also called the law of inertia.', 'کسی بیرونی قوت کی غیر موجودگی میں ایک ساکن جسم ہمیشہ ساکن رہتا ہے اور متحرک جسم یکساں رفتار کے ساتھ خطِ مستقیم پر اپنی حرکت جاری رکھتا ہے۔ اس قانون کو جمود کا قانون بھی کہتے ہیں۔', 'د کوم بهرني ځواک په نشتوالي کې یو ولاړ جسم تل ولاړ پاتې کېږي او خوځنده جسم په یو شان سرعت پر مستقیمه کرښه خپل حرکت ته دوام ورکوي. دې قانون ته د جمود قانون هم ویل کېږي.')])
    b.h('Second law of Motion', 'دوسرا قانونِ حرکت (Second law of Motion)', 'د حرکت دویم قانون (Second law of Motion)')
    P(b, [('When some external force acts on some body, it produces acceleration in that body in its own direction. The magnitude of this acceleration is directly proportional to the external force and inversely proportional to the mass.', 'جب کوئی بیرونی قوت کسی جسم پر عمل کرتی ہے تو وہ اپنی ہی سمت میں اس جسم میں اسراع پیدا کرتی ہے۔ اس اسراع کی مقدار بیرونی قوت کے راست متناسب ہوتی ہے اور کمیت کے بالعکس متناسب ہوتی ہے۔', 'کله چې یو بهرنی ځواک پر یوه جسم عمل کوي، په خپل لوري کې په هغه جسم کې تعجیل پیدا کوي. د دې تعجیل اندازه له بهرني ځواک سره مستقیماً متناسبه او له کتلې سره معکوساً متناسبه وي.')])
    b.h('Third law of Motion', 'تیسرا قانونِ حرکت (Third law of Motion)', 'د حرکت درېیم قانون (Third law of Motion)')
    P(b, [('Every action of force has a reaction. Action and reaction are equal to each other but in opposite directions.', 'ہر قوت کے عمل کا ایک ردِ عمل ہوتا ہے۔ عمل اور رد عمل آپس میں برابر مگر مخالف سمت میں ہوتے ہیں۔', 'د ځواک هر عمل یو غبرګون لري. عمل او غبرګون سره برابر خو مخالف لوري ته وي.')])
    b.h('Equilibrium', 'توازن (Equilibrium)', 'توازن (Equilibrium)')
    P(b, [('When several forces act on a body at the same time and that body does not change its state of rest or state of motion, then this state of the body is called the state of equilibrium.', 'جب کسی جسم پر بیک وقت متعدد قوتیں عمل کرتی ہیں اور وہ جسم اپنی حالتِ سکون یا حالتِ حرکت نہیں بدلتا تو اس حالت کو جسم کی حالتِ توازن کہتے ہیں۔', 'کله چې پر یوه جسم په یو وخت څو ځواکونه عمل وکړي او هغه جسم د سکون یا حرکت حالت بدل نه کړي، دې حالت ته د جسم د توازن حالت ویل کېږي.')])
    b.h('Centre of Gravity', 'مرکزِ ثقل (Centre of Gravity)', 'د جاذبې مرکز (Centre of Gravity)')
    P(b, [('In every body there is a special point where the whole weight of the body acts. This is called the centre of gravity.', 'ہر جسم میں ایک خاص نقطہ ہوتا ہے جہاں پر جسم کا سارا وزن عمل کرتا ہے۔ اس کو مرکزِ ثقل کہتے ہیں۔', 'په هر جسم کې یو ځانګړی ټکی وي چې د جسم ټول وزن پرې عمل کوي. دې ته د جاذبې مرکز ویل کېږي.')])
    r = rec(b, 6, 2, 59)
    deco(r, 'A photograph of an arch of balanced pebbles by the sea beside the equilibrium paragraph is decorative.')
    BOOK.save(59, [(6, r)])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 54
    {54: p54, 55: p55, 56: p56, 57: p57, 58: p58, 59: p59}[n]()
