"""PDF63 (printed 113–114): Unit 12 Glossary (lean and slipper'd pantaloon … woeful); Reading Comprehension Q1–7; Writing Suggestions."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
g = Builder()
gloss(g, 'eng12-u12-gloss-b', [
    ("lean and slipper'd pantaloon", "here 'lean' means 'thin'; a slipper is what people wear indoors; a 'pantaloon' meant an old man - so this describes a thin old man who stays inside", "یہاں ’’لین‘‘ کا مطلب ’’دبلا‘‘ ہے؛ چپل وہ ہے جو لوگ گھر میں پہنتے ہیں؛ ’’پینٹالون‘‘ کا مطلب بوڑھا آدمی تھا — یعنی یہ ایک دبلے بوڑھے کا بیان ہے جو گھر میں رہتا ہے", 'دلته "لین" مانا "ډنګر" ده؛ څپلۍ هغه څه دي چې خلک یې په کور کې اغوندي؛ "پنټالون" مانا زوړ سړی و — یعنې دا د یوه ډنګر زاړه سړي بیان دی چې په کور کې پاتې کېږي'),
    ('manly(adj.)', "if someone is 'manly' they have characteristics people traditionally admire in men, e.g. being strong and brave", 'اگر کوئی ’’مردانہ‘‘ ہو تو اس میں وہ خصوصیات ہوتی ہیں جو لوگ روایتی طور پر مردوں میں پسند کرتے ہیں، مثلاً مضبوط اور بہادر ہونا', 'که څوک "نارینه‌ډوله" وي، هغه ځانګړنې لري چې خلک یې په دودیز ډول په نارینه وو کې ستایي، لکه پیاوړی او زړور کېدل'),
    ('mere(adj.)', 'here, absolute or complete (old-fashioned use)', 'یہاں، مطلق یا مکمل (پرانا استعمال)', 'دلته، مطلق یا بشپړ (زوړ کارونه)'),
    ('merely(adv.)', 'just, only', 'محض، صرف', 'یوازې، فقط'),
    ('mewling(v)', "a small weak noise that a cat makes (in modern English, 'to mew')", "بلی کی ہلکی کمزور آواز (جدید انگریزی میں 'to mew')", "د پیشو کوچنی کمزوری غږ (په عصري انګلیسي کې 'to mew')"),
    ('mistress(n)', "'mistress' means female lover but it can also mean a woman in charge", "’’مسٹریس‘‘ کا مطلب محبوبہ ہے لیکن اس کا مطلب کسی کام کی نگران عورت بھی ہو سکتا ہے", '"مسټرېس" مانا معشوقه ده خو د یوه کار مسؤله ښځه هم مانا کېدای شي'),
    ('oaths(n)', 'Promises', 'وعدے، قسمیں', 'ژمنې، قسمونه'),
    ('oblivion(n)', "if someone is 'oblivious' they don't know what is happening around them, and if they live in 'oblivion' they are completely forgotten by other people", "اگر کوئی ’’بے خبر‘‘ ہو تو اسے معلوم نہیں ہوتا کہ اس کے اردگرد کیا ہو رہا ہے، اور اگر وہ ’’گمنامی‘‘ میں رہے تو دوسرے لوگ اسے مکمل طور پر بھول جاتے ہیں", 'که څوک "بې‌خبره" وي، نه پوهېږي چې شاوخوا یې څه کېږي، او که په "هېرېدنه" کې ژوند وکړي، نور خلک یې په بشپړ ډول هېروي'),
    ('pard(n)', 'a large cat, such as a leopard (old-fashioned English)', 'بڑی بلی جیسے چیتا (پرانی انگریزی)', 'لویه پیشو لکه پړانګ (زړه انګلیسي)'),
    ('part (n)', 'here, a character in a play or drama', 'یہاں، ڈرامے کا کوئی کردار', 'دلته، په ډرامه کې کرکټر'),
    ('pipes(n)', 'a musical instrument that makes a high sound', 'ایک ساز جو باریک آواز نکالتا ہے', 'یوه موسیقي اله چې نری غږ کوي'),
    ('pouch(n)', 'a small bag for carrying money', 'رقم رکھنے کی چھوٹی تھیلی', 'د پیسو د وړلو کوچنۍ کڅوړه'),
    ('puking(v)', 'being sick, vomiting', 'قے کرنا', 'کانګې کول'),
    ('round belly', "belly means 'stomach' - so a 'round belly' is a large or fat man's stomach!", "’’بیلی‘‘ کا مطلب ’’پیٹ‘‘ ہے — یعنی ’’گول پیٹ‘‘ کسی بھاری یا موٹے آدمی کا پیٹ ہے!", '"بېلي" مانا "ګېډه" ده — یعنې "ګرده ګېډه" د لوی یا چاغ سړي ګېډه ده!'),
    ('sans(prep.)', "without (this is French for 'without')", "بغیر (یہ فرانسیسی میں 'بغیر' کے لیے ہے)", "پرته له (دا په فرانسوي کې د 'پرته' لپاره ده)"),
    ('satchel(n)', 'a shoulder bag that children sometimes use to carry books to school', 'کندھے کا بستہ جو بچے کبھی کبھی اسکول کتابیں لے جانے کے لیے استعمال کرتے ہیں', 'د اوږې بسته چې ماشومان کله کله ښوونځي ته د کتابونو د وړلو لپاره کاروي'),
    ('second childishness', "being like a child again (in modern English, we sometimes talk about a 'second childhood')", "دوبارہ بچے جیسا ہو جانا (جدید انگریزی میں کبھی کبھی 'second childhood' کہا جاتا ہے)", "بیا د ماشوم په څېر کېدل (په عصري انګلیسي کې کله کله 'second childhood' ویل کېږي)"),
    ('seeking the bubble reputation', "a bubble is empty, so by 'seeking the bubble reputation', Shakespeare means that the man does things that make him look good even if they are pointless", "بلبلہ خالی ہوتا ہے، اس لیے ’’بلبلے جیسی شہرت کی تلاش‘‘ سے شیکسپیئر کی مراد یہ ہے کہ آدمی ایسے کام کرتا ہے جو اسے اچھا دکھائیں چاہے وہ بے مقصد ہوں", 'پوکڼۍ تشه وي، نو د "پوکڼۍ په څېر شهرت لټولو" څخه د شکسپیر مطلب دا دی چې سړی داسې کارونه کوي چې ښه یې ښکاره کړي که څه هم بې‌ګټې وي'),
    ('shrunk shank', "'to shrink' means to grow smaller, and a 'shank' is a piece of meat cut from a leg of an animal - so the man's legs have grown narrower with age", "’’سکڑنا‘‘ کا مطلب چھوٹا ہونا ہے، اور ’’شینک‘‘ جانور کی ٹانگ سے کٹا گوشت کا ٹکڑا ہے — یعنی عمر کے ساتھ آدمی کی ٹانگیں پتلی ہو گئی ہیں", '"شرېنک" مانا کوچنی کېدل دي، او "شینک" د حیوان له پښې پرې شوې د غوښې ټوټه ده — یعنې د عمر سره د سړي پښې نرۍ شوې دي'),
    ('sighing(v)', 'here, sighing with sexual pleasure', 'یہاں، عشق میں آہیں بھرنا', 'دلته، په مینه کې اسوېلي کښل'),
    ('sudden and quick in quarrel', "'quarrel' is a slightly old-fashioned word for an argument; 'sudden' here means unpredictable - so in an argument this young man might suddenly and become violent", "’’کوارل‘‘ بحث کے لیے قدرے پرانا لفظ ہے؛ یہاں ’’سڈن‘‘ کا مطلب غیر متوقع ہے — یعنی بحث میں یہ نوجوان اچانک پرتشدد ہو سکتا ہے", '"کوارل" د شخړې لپاره یو څه زړه کلمه ده؛ دلته "سډن" مانا نااټکل وړ ده — یعنې په شخړه کې دا ځوان ناڅاپه تاوتریخجن کېدای شي'),
    ('time(n)', 'here, a life or lifetime', 'یہاں، زندگی یا عمر', 'دلته، ژوند یا عمر'),
    ('treble(n)', "a treble is the higher part of a piece of music - so Shakespeare is referring to a boy's high voice", 'ٹریبل موسیقی کا اونچا حصہ ہے — یعنی شیکسپیئر لڑکے کی باریک آواز کی طرف اشارہ کر رہا ہے', 'ټرېبل د موسیقۍ لوړه برخه ده — یعنې شکسپیر د هلک نري غږ ته اشاره کوي'),
    ('turning again toward', 'becoming again', 'دوبارہ بن جانا', 'بیا کېدل'),
    ("well sav'd", 'kept carefully', 'احتیاط سے رکھا ہوا', 'په پام ساتل شوی'),
    ('wise saws', 'wise sayings or phrases (old-fashioned English)', 'دانائی کے اقوال یا جملے (پرانی انگریزی)', 'حکیمانه وینا یا عبارتونه (زړه انګلیسي)'),
    ('woeful (adj.)', 'unhappy (old-fashioned English)', 'غمگین (پرانی انگریزی)', 'خپه (زړه انګلیسي)'),
])
gl = BOOK.record(g, 'eng12-u12-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 63, [113, 114])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. This poem is an extended metaphor. What are the two things being compared?', '1. یہ نظم ایک طویل استعارہ ہے۔ کن دو چیزوں کا موازنہ کیا جا رہا ہے؟', '1. دا شعر یوه اوږده استعاره ده. کوم دوه شیان پرتله کېږي؟'),
    ('2. There are seven stages or acts of a man listed in this poem. What are they?', '2. اس نظم میں انسان کے سات مراحل یا ایکٹ بیان کیے گئے ہیں۔ وہ کون سے ہیں؟', '2. په دې شعر کې د انسان اووه پړاوونه یا پردې لست شوې. هغه کوم دي؟'),
    ("3. What is meant by the word 'oblivion' in the context of the poem 'All the World's a Stage'?", '3. نظم ’’ساری دنیا ایک اسٹیج ہے‘‘ کے سیاق میں لفظ ’’oblivion‘‘ سے کیا مراد ہے؟', '3. د "ټوله نړۍ یوه سټېج ده" شعر په شرایطو کې له "oblivion" کلمې څه مراد دی؟'),
    ("4. Then a soldier, Full of strange oaths, and bearded like a pard, Jealous in honour, sudden and quick in quarrel, Seeking the bubble reputation Even in the cannon's mouth.", '4. ’’پھر سپاہی، عجیب قسموں سے بھرا اور چیتے کی طرح داڑھی والا، عزت میں غیرت مند، جھگڑے میں اچانک اور تیز، بلبلے جیسی شہرت کی تلاش میں توپ کے دہانے میں بھی۔‘‘', '4. "بیا یو سرتېری، له عجیبو قسمونو ډک او د پړانګ په څېر ږیره لرونکی، په عزت کې غیرتي، په شخړه کې ناڅاپي او ګړندی، د پوکڼۍ په څېر شهرت لټوي حتی د توپ په خوله کې."'),
    ('(a) What is the soldier ready to do?', '(a) سپاہی کیا کرنے کو تیار ہے؟', '(a) سرتېری څه کولو ته چمتو دی؟'),
    ('(b) What is the poetic device used in the second line?', '(b) دوسرے مصرعے میں کون سی شاعرانہ صنعت استعمال ہوئی ہے؟', '(b) په دویمه مسرعه کې کوم شاعرانه صنعت کارول شوی؟'),
    ("(c) What does 'bubble reputation' mean?", "(c) 'bubble reputation' کا کیا مطلب ہے؟", "(c) د 'bubble reputation' مانا څه ده؟"),
    ("5. What is the significance of the words 'entrances' and 'exits' in the poem 'The Seven Ages'?", "5. نظم ’’سات ادوار‘‘ میں الفاظ 'entrances' اور 'exits' کی کیا اہمیت ہے؟", "5. د \"اووه عمرونه\" په شعر کې د 'entrances' او 'exits' کلمو اهمیت څه دی؟"),
    ('6. Identify various figure of speech in the poem.', '6. نظم میں مختلف صنائعِ بدائع کی نشاندہی کریں۔', '6. په شعر کې بېلابېل بدیعي صنعتونه وپېژنئ.'),
    ('7. Write a well-integrated essay on different stages of human life as mentioned in the above poem, using above prewriting strategies.', '7. مندرجہ بالا نظم میں بیان کردہ انسانی زندگی کے مختلف مراحل پر، لکھنے سے پہلے کی مذکورہ حکمتِ عملیاں استعمال کرتے ہوئے، ایک مربوط مضمون لکھیں۔', '7. په پورتني شعر کې د یادو شویو د انساني ژوند د بېلابېلو پړاوونو په اړه، د لیکلو مخکې د پورته ستراتیژیو په کارولو، یوه منسجمه مقاله ولیکئ.'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Write the summary of the poem, "All the World\'s a Stage".', 'نظم ’’ساری دنیا ایک اسٹیج ہے‘‘ کا خلاصہ لکھیں۔', 'د "ټوله نړۍ یوه سټېج ده" شعر لنډیز ولیکئ.')
qs = BOOK.record(q, 'eng12-u12-comprehension', 'Reading Comprehension; Writing Suggestions', 'مطالعہ اور فہم؛ تحریری تجاویز', 'لوستل او پوهه؛ د لیکلو وړاندیزونه', 63, [114])
issues = [{'id': 'eng12-p113-114', 'unit': 12, 'printedPage': 114, 'description': "Printed text retained: glossary “might suddenly and become violent”, Q5 refers to the poem as “The Seven Ages”, Q6 “various figure of speech”. The glossary gloss for “sighing” is reproduced as printed in English; the Urdu/Pashto views give a neutral rendering (sighing in love)."}]

if __name__ == '__main__':
    BOOK.save(63, [(12, gl), (12, qs)], issues=issues)
