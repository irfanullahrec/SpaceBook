"""PDF50 (printed 87–88): Unit 9 About the Poet; Glossary; Reading Comprehension Q1–8; Writing (paraphrase); Oral; Vocabulary A weather words 1–8."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
B = '________'
a = Builder()
a.h('About the Poet', 'شاعر کے بارے میں', 'د شاعر په اړه')
a.p("Coventry Patmore (23 July 18 23 – 26 November 1896 ) was an English Victorian poet and critic best known for his narrative poem about the Victorian ideal of a happy marriage 'the Angel in the house.' Patmore was employed in the British museum upon the publication of his first book of poems in 1844. After the death of his first wife, the grief of loss became in great measure, his later theme. Like many Victorians, Coventry Patmore was a deeply religious man who readily and sincerely associated the ordinary happenings of everyday life with his religious beliefs. This poem is an example of it.",
    'کوونٹری پیٹمور (23 جولائی 1823 – 26 نومبر 1896) ایک انگریز وکٹورین شاعر اور نقاد تھے جو خوشگوار ازدواجی زندگی کے وکٹورین آئیڈیل پر اپنی بیانیہ نظم ’’دی اینجل ان دی ہاؤس‘‘ کے لیے سب سے زیادہ مشہور ہیں۔ 1844 میں ان کی نظموں کی پہلی کتاب شائع ہونے پر انہیں برٹش میوزیم میں ملازمت ملی۔ پہلی بیوی کی وفات کے بعد جدائی کا غم بڑی حد تک ان کا بعد کا موضوع بن گیا۔ بہت سے وکٹورین لوگوں کی طرح کوونٹری پیٹمور ایک گہرے مذہبی انسان تھے جو روزمرہ زندگی کے عام واقعات کو آسانی اور خلوص سے اپنے مذہبی عقائد سے جوڑ دیتے تھے۔ یہ نظم اس کی ایک مثال ہے۔',
    'کوونټري پاټمور (د 1823 د جولای 23 – د 1896 د نومبر 26) یو انګرېز ویکټوریايي شاعر او نقاد و چې د خوشاله واده د ویکټوریايي ارمان په اړه د خپل کیسه‌ییز شعر "په کور کې پرښته" له امله تر ټولو ډېر مشهور دی. په 1844 کې د هغه د شعرونو د لومړي کتاب په خپرېدو هغه په برتانوي موزیم کې وګمارل شو. د لومړۍ مېرمنې له مړینې وروسته د بېلتون غم تر ډېره د هغه وروستۍ موضوع شوه. د ډېرو ویکټوریايي خلکو په څېر کوونټري پاټمور یو ژور دیندار سړی و چې د ورځني ژوند عادي پېښې یې په اسانۍ او اخلاص سره له خپلو مذهبي باورونو سره تړلې. دا شعر یې یوه بېلګه ده.')
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u09-gloss', [
    ('abraded(v)', 'rubbed and worn', 'رگڑا اور گھسا ہوا', 'مښل شوی او زوړ شوی'),
    ('bluebells(n)', 'a kind of wild flower with a cluster of small bell-shaped blue flowers growing on a long stem.', 'ایک قسم کا جنگلی پھول جس کی لمبی ڈنڈی پر گھنٹی نما چھوٹے نیلے پھولوں کا گچھا ہوتا ہے۔', 'یو ډول ځنګلي ګل چې پر اوږده ډنډ یې د زنګ په بڼه د کوچنیو شنو ګلانو ګېډۍ وي.'),
    ('drawn(v)', 'pulled', 'کھینچا ہوا', 'کش شوی'), ('late (adj.)', 'recent', 'حالیہ', 'تازه'), ('ranged(v)', 'set out regularly', 'ترتیب سے رکھا ہوا', 'په ترتیب ایښودل شوی'),
    ('tranced breath', 'the almost extinct breath in the unconsciousness before death.', 'موت سے پہلے بے ہوشی میں تقریباً ختم ہوتی سانس۔', 'له مرګ مخکې په بې‌هوښۍ کې نږدې ختمه شوې ساه.'),
    ('wise(adj.)', 'manner', 'انداز', 'ډول'), ('wrath(n)', 'fierce anger', 'شدید غصہ', 'سخت غوسه'),
])
ab = BOOK.record(a, 'eng12-u09-about-glossary', 'About the Poet; Glossary', 'شاعر کے بارے میں؛ فرہنگ', 'د شاعر په اړه؛ وییپانګه', 50, [87])
ab['sourceCoverIllustrationReview'] = 'Portrait of Coventry Patmore is decorative; not reproduced.'

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ("1. What is the theme of the poem 'The Toys'?", '1. نظم ’’کھلونے‘‘ کا موضوع کیا ہے؟', '1. د "لوبونې" شعر موضوع څه ده؟'),
    ('2. The story behind the poem "The Toys" is a homely one. Narrate the story in your own words.', '2. نظم ’’کھلونے‘‘ کے پیچھے کہانی ایک گھریلو کہانی ہے۔ کہانی اپنے الفاظ میں بیان کریں۔', '2. د "لوبونې" شعر تر شا کیسه یوه کورنۍ کیسه ده. کیسه په خپلو ټکو کې بیان کړئ.'),
    ("3. What verse style has been adopted by the poet in the poem,' The toys '?", '3. نظم ’’کھلونے‘‘ میں شاعر نے کون سا اسلوبِ نظم اپنایا ہے؟', '3. شاعر په "لوبونې" شعر کې د شعر کوم سبک غوره کړی؟'),
    ('4. Does this style suit the mood of the poem and how?', '4. کیا یہ اسلوب نظم کی کیفیت سے مطابقت رکھتا ہے اور کیسے؟', '4. ایا دا سبک د شعر له حالت سره برابر دی او څنګه؟'),
    ('5. What is the symbolic significance of the word "Toys" in light of the poem \'The Toys\'?', '5. نظم ’’کھلونے‘‘ کی روشنی میں لفظ ’’کھلونے‘‘ کی علامتی اہمیت کیا ہے؟', '5. د "لوبونې" شعر په رڼا کې د "لوبونې" کلمې سمبولیک اهمیت څه دی؟'),
    ('6. How does the poet relate his own action to the mercy of God?', '6. شاعر اپنے عمل کو خدا کی رحمت سے کیسے جوڑتا ہے؟', '6. شاعر خپله کړنه د خدای له رحمت سره څنګه تړي؟'),
    ('7. What is the tone of the poem "The Toys"? Do you think it is in conformity with the theme of the poem? How?', '7. نظم ’’کھلونے‘‘ کا لہجہ کیا ہے؟ کیا آپ کے خیال میں یہ نظم کے موضوع سے ہم آہنگ ہے؟ کیسے؟', '7. د "لوبونې" شعر لهجه څه ده؟ ایا ستاسو په اند د شعر له موضوع سره برابره ده؟ څنګه؟'),
    ('8. What feelings does the poem "The Toys" evoke in you?', '8. نظم ’’کھلونے‘‘ آپ میں کون سے جذبات ابھارتی ہے؟', '8. د "لوبونې" شعر په تاسو کې کوم احساسات راپاروي؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Paraphrase the following lines:', 'درج ذیل اشعار کی نثر میں وضاحت (پیرا فریز) کریں:', 'لاندې بیتونه په نثر کې تشریح (پارافرېز) کړئ:')
q.group('lines', [("\"Then, fatherly not less", 'تو پدرانہ شفقت میں اس سے کم نہیں', 'نو د پلارنۍ مینې له مخې له هغه کم نه'),
                  ('Than I whom Thou hast moulded from the clay,', 'جتنا میں ہوں جسے تو نے مٹی سے گوندھا،', 'چې زه یم چې تا له خټې جوړ کړی یم،'),
                  ("Thou'lt leave Thy wrath and say,", 'تو اپنا غضب چھوڑ دے گا اور کہے گا،', 'ته به خپل غضب پرېږدې او وبه وایې،'),
                  ("'I will be sorry for their childishness'.", '’’مجھے ان کے بچپنے پر افسوس ہو گا‘‘۔', '"زه به د هغوی په ماشومتوب خواخوږی شم".')])
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p("Give oral recount in front of class of your experience, feelings emotions if you had been treated by one of your parents the same way as narrated in poem 'Toys'.", 'جماعت کے سامنے اپنے تجربے، احساسات اور جذبات کا زبانی بیان دیں اگر آپ کے والدین میں سے کسی نے آپ سے ویسا ہی سلوک کیا ہو جیسا نظم ’’کھلونے‘‘ میں بیان ہوا ہے۔', 'د ټولګي مخې ته د خپلې تجربې، احساساتو او جذبو شفاهي بیان وکړئ که ستاسو له مور یا پلار ستاسو سره هماغسې چلند کړی وي لکه څنګه چې د "لوبونې" په شعر کې بیان شوی.')
q.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
q.p('A. Fill in the following blanks with appropriate words related to weather given in the list below.', 'A. نیچے دی گئی فہرست سے موسم سے متعلق موزوں الفاظ کے ساتھ درج ذیل خالی جگہیں پُر کریں۔', 'A. لاندې تش ځایونه د لاندې لست څخه د هوا اړوند مناسبو کلمو سره ډک کړئ.')
WB = [['hazy', 'stormy', 'showery', 'rainy', 'damp'], ['dull', 'dry', 'drizzly', 'foggy', 'breezy'], ['cloudy', 'clear', 'snowy', 'bright', 'wet']]
H = [''] * 5
q.table('eng12-u09-weather-box', H, WB, H, H, WB, WB, noHeader=True)
WS = [(f"It's very {B} today. I think it's a northern wind.", f'آج بہت {B} ہے۔ میرا خیال ہے یہ شمالی ہوا ہے۔', f'نن ډېر {B} دی. فکر کوم شمالي باد دی.'),
      (f'They got married on a {B}, sunny day in June.', f'ان کی شادی جون کے ایک {B}، دھوپ والے دن ہوئی۔', f'دوی د جون په یوه {B}، لمرینه ورځ واده وکړ.'),
      (f'Wait till the weather is {B} to take a bike ride.', f'سائیکل کی سیر کے لیے موسم {B} ہونے تک انتظار کریں۔', f'د بایسکل سپرلۍ لپاره تر هغه انتظار وکړئ چې هوا {B} شي.'),
      (f"Some people prefer to hike when it's {B} rather than when it's sunny.", f'کچھ لوگ دھوپ کے بجائے {B} موسم میں پیدل سفر پسند کرتے ہیں۔', f'ځینې خلک د لمر پر ځای په {B} هوا کې پلي تګ خوښوي.'),
      (f"I hate {B}, cold days when I can't warm up.", f'مجھے {B}، سرد دن ناپسند ہیں جب میں گرم نہیں ہو پاتا۔', f'زه {B}، سړې ورځې نه خوښوم چې ځان نه شم تودولی.'),
      (f'The weather is rather {B} today. You should take a rain jacket.', f'آج موسم کچھ {B} ہے۔ آپ کو بارش کی جیکٹ ساتھ لے جانی چاہیے۔', f'نن هوا یو څه {B} ده. باید د باران جاکټ درسره واخلئ.'),
      (f'Next week will be hot and {B}.', f'اگلا ہفتہ گرم اور {B} ہو گا۔', f'راتلونکې اونۍ به ګرمه او {B} وي.'),
      (f'The weather is {B} this week. I wish it would rain.', f'اس ہفتے موسم {B} ہے۔ کاش بارش ہو جائے۔', f'پدې اونۍ هوا {B} ده. کاشکې باران وشي.')]
q.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(WS, 1)])
qs = BOOK.record(q, 'eng12-u09-comprehension', 'Reading Comprehension; Writing; Oral; Vocabulary A (1)', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A (1)', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه؛ لغات A (1)', 50, [87, 88])
issues = [{'id': 'eng12-p87-88', 'unit': 9, 'printedPage': 87, 'description': 'Printed text retained: birth year “18 23”, “the grief of loss became in great measure, his later theme”, Q3 “The toys”, oral task “feelings emotions”. The poem is printed as “The Toys”; Q5 and Q7 use both spellings.'}]

if __name__ == '__main__':
    BOOK.save(50, [(9, ab), (9, qs)], issues=issues)
