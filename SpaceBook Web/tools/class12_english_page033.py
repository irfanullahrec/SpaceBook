"""PDF33 (printed 53–54): Unit 6 opener 'If' (Rudyard Kipling) outcomes; poem 'If' (1910, public domain) full text."""
from class12_book_common import Book, Builder

BOOK = Book('english')
UT = ('If (Poem)', 'اگر (نظم)', 'که (شعر)')
o = Builder()
o.h('Unit 6 — If (Rudyard Kipling)', 'یونٹ 6 — اگر (رڈیارڈ کپلنگ)', 'واحد 6 — که (روډیارډ کیپلینګ)')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Read a given poem and give orally and in writing: theme and its development; personal response with justification.', 'دی گئی نظم پڑھیں اور زبانی و تحریری طور پر بیان کریں: موضوع اور اس کا ارتقا؛ جواز کے ساتھ ذاتی ردِعمل۔', 'ورکړل شوی شعر ولولي او په خوله او لیکلي ډول ووايي: موضوع او د هغې وده؛ د دلیل سره شخصي غبرګون.'),
    ('Analyze how a writer/ poet uses language to appeal to the senses through use of figurative language including similes, metaphors and imagery.', 'تجزیہ کریں کہ ایک مصنف/ شاعر تشبیہات، استعارات اور پیکر تراشی سمیت مجازی زبان کے ذریعے حواس کو متاثر کرنے کے لیے زبان کیسے استعمال کرتا ہے۔', 'تحلیل کړي چې یو لیکوال/ شاعر د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې له لارې حواسو ته د اپیل لپاره ژبه څنګه کاروي.'),
    ('Use critical thinking to respond orally and in writing to the text (post-reading) to give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read; relate what is read to his or her own feelings and experiences.', 'تنقیدی سوچ استعمال کرتے ہوئے متن پر زبانی اور تحریری ردِعمل دیں (مطالعے کے بعد) تاکہ پڑھے گئے متن کے نقطۂ ہائے نظر/ خیالات اور مسائل پر ذاتی رائے دیں اور اپنے موقف کا جواز پیش کریں؛ جو پڑھا اسے اپنے احساسات اور تجربات سے جوڑیں۔', 'د انتقادي فکر په کارولو متن ته په خوله او لیکلي ډول غبرګون وښيي (له لوستلو وروسته) ترڅو د لوستل شوي متن د لیدلورو/ نظرونو او مسایلو په اړه شخصي نظر ورکړي او د خپل دریځ دلیل وړاندې کړي؛ لوستل شوي له خپلو احساساتو او تجربو سره وتړي.'),
    ('Use a thesaurus to locate the synonyms closest to the meaning of the given words.', 'دیے گئے الفاظ کے معنی کے قریب ترین مترادفات تلاش کرنے کے لیے تھیسارس استعمال کریں۔', 'د ورکړل شویو کلمو مانا ته تر ټولو نږدې مترادفات د موندلو لپاره تیسارس وکاروي.'),
    ('Use the knowledge of roots, suffixes and affixes to determine the meaning of unfamiliar words.', 'نامانوس الفاظ کے معنی معلوم کرنے کے لیے مادوں، لاحقوں اور سابقوں کے علم کو استعمال کریں۔', 'د ناپېژندل شویو کلمو د مانا د ټاکلو لپاره د رېښو، وروستاړو او مختاړو له پوهې کار واخلي.'),
    ('Recognize and use varying intonation patterns as aid in spoken and written discourse.', 'زبانی اور تحریری گفتگو میں مدد کے طور پر لہجے کے مختلف انداز پہچانیں اور استعمال کریں۔', 'د خولې او لیکلې ګړنې د مرستې په توګه د اهنګ بېلابېلې بڼې وپېژني او وکاروي.'),
    ('Demonstrate use of noun phrases.', 'اسمی فقروں (نَون فریزز) کا استعمال کر کے دکھائیں۔', 'د نومي عبارتونو کارونه وښيي.'),
])
op = BOOK.record(o, 'eng12-u06-outcomes', 'Unit 6 — learning outcomes', 'یونٹ 6 — تعلیمی نتائج', 'واحد 6 — د زده کړې پایلې', 33, [53], unit_title=UT)

p = Builder()
p.h('If', 'اگر', 'که')
ST = [
    [('If you can keep your head when all about you', 'اگر تم اپنے ہوش قائم رکھ سکو جب تمہارے اردگرد سب', 'که ته خپل هوش وساتلی شې کله چې ستا شاوخوا ټول'),
     ('Are losing theirs and blaming it on you,', 'اپنے ہوش کھو رہے ہوں اور الزام تم پر ڈال رہے ہوں،', 'خپل هوش له لاسه ورکوي او پړه پر تا اچوي،'),
     ('If you can trust yourself when all men doubt you,', 'اگر تم خود پر بھروسہ کر سکو جب سب لوگ تم پر شک کریں،', 'که پر ځان باور وکړای شې کله چې ټول خلک پر تا شک کوي،'),
     ('But make allowance for their doubting too;', 'لیکن ان کے شک کی بھی گنجائش رکھو؛', 'خو د هغوی شک ته هم ځای ورکړې؛'),
     ('If you can wait and not be tired by waiting,', 'اگر تم انتظار کر سکو اور انتظار سے تھکو نہیں،', 'که انتظار وکړای شې او له انتظاره ستړی نه شې،'),
     ("Or being lied about, don't deal in lies,", 'یا تمہارے بارے میں جھوٹ بولا جائے تو خود جھوٹ کا کاروبار نہ کرو،', 'یا که ستا په اړه دروغ وویل شي، ته د دروغو سودا مه کوه،'),
     ("Or being hated, don't give way to hating,", 'یا تم سے نفرت کی جائے تو خود نفرت کے آگے نہ جھکو،', 'یا که له تا کرکه وشي، ته کرکې ته تسلیم مه شه،'),
     ("And yet don't look too good, nor talk too wise:", 'اور پھر بھی نہ بہت نیک بن کر دکھاؤ، نہ بہت دانا بن کر بولو:', 'او بیا هم ځان ډېر نېک مه ښیه، او نه ډېر هوښیار خبرې کوه:')],
    [('If you can dream—and not make dreams your master;', 'اگر تم خواب دیکھ سکو — اور خوابوں کو اپنا آقا نہ بناؤ؛', 'که خوبونه ولیدلی شې — او خوبونه خپل بادار نه کړې؛'),
     ('If you can think—and not make thoughts your aim;', 'اگر تم سوچ سکو — اور سوچوں کو اپنا مقصد نہ بناؤ؛', 'که فکر وکړای شې — او فکرونه خپله موخه نه کړې؛'),
     ('If you can meet with Triumph and Disaster', 'اگر تم فتح اور تباہی دونوں سے مل سکو', 'که له بریا او ناورین سره مخ شې'),
     ('And treat those two impostors just the same;', 'اور ان دونوں فریب کاروں سے ایک جیسا سلوک کرو؛', 'او له دې دوو درغلګرو سره یو شان چلند وکړې؛'),
     ("If you can bear to hear the truth you've spoken", 'اگر تم برداشت کر سکو کہ جو سچ تم نے کہا', 'که دا وزغملی شې چې هغه رښتیا چې تا ویلې'),
     ('Twisted by knaves to make a trap for fools,', 'اسے بدمعاش توڑ مروڑ کر بے وقوفوں کے لیے جال بنا دیں،', 'بدمعاشان یې کږوي ترڅو د ساده‌ګانو لپاره لومه جوړه کړي،'),
     ('Or watch the things you gave your life to, broken,', 'یا ان چیزوں کو ٹوٹا ہوا دیکھو جن پر تم نے اپنی زندگی لگا دی،', 'یا هغه شیان مات وګورې چې خپل ژوند دې ورته ورکړی،'),
     ("And stoop and build 'em up with worn-out tools:", 'اور جھک کر انہیں گھسے پٹے اوزاروں سے پھر سے بناؤ:', 'او ټیټ شې او په زړو وسایلو یې بیا جوړ کړې:')],
    [('If you can make one heap of all your winnings', 'اگر تم اپنی ساری کمائی کا ایک ڈھیر بنا سکو', 'که خپلې ټولې ګټې یو ډېر کړای شې'),
     ('And risk it on one turn of pitch-and-toss,', 'اور اسے سکہ اچھالنے کی ایک باری پر داؤ پر لگا دو،', 'او د سکې د غورځولو پر یوه وار یې په خطر کې واچوې،'),
     ('And lose, and start again at your beginnings', 'اور ہار جاؤ، اور پھر سے بالکل شروع سے آغاز کرو', 'او وبایلې، او بیا له خپل پیله پیل وکړې'),
     ('And never breathe a word about your loss;', 'اور اپنے نقصان کے بارے میں ایک لفظ بھی منہ سے نہ نکالو؛', 'او د خپل زیان په اړه یوه کلمه هم ونه وایې؛'),
     ('If you can force your heart and nerve and sinew', 'اگر تم اپنے دل، اعصاب اور پٹھوں کو مجبور کر سکو', 'که خپل زړه، عصبونه او پلونه اړ کړای شې'),
     ('To serve your turn long after they are gone,', 'کہ وہ تمہارا ساتھ دیں ان کے ختم ہو جانے کے بہت بعد تک،', 'چې ستا خدمت وکړي ډېر وروسته له دې چې له کاره لوېدلي وي،'),
     ('And so hold on when there is nothing in you', 'اور یوں ڈٹے رہو جب تم میں کچھ باقی نہ رہے', 'او همداسې ټینګ پاتې شې کله چې په تا کې هېڅ پاتې نه وي'),
     ("Except the Will which says to them: 'Hold on!'", "سوائے اس عزم کے جو ان سے کہتا ہے: 'ڈٹے رہو!'", "پرته له هغه عزم چې هغوی ته وايي: 'ټینګ شئ!'")],
    [('If you can talk with crowds and keep your virtue,', 'اگر تم ہجوم سے بات کر سکو اور اپنی نیکی برقرار رکھو،', 'که له ګڼې ګوڼې سره خبرې وکړای شې او خپل فضیلت وساتې،'),
     ('Or walk with Kings—nor lose the common touch,', 'یا بادشاہوں کے ساتھ چلو — اور عام لوگوں سے تعلق نہ کھوؤ،', 'یا له پاچایانو سره ګام پورته کړې — او له عامو خلکو اړیکه له لاسه ورنه کړې،'),
     ('If neither foes nor loving friends can hurt you,', 'اگر نہ دشمن نہ پیار کرنے والے دوست تمہیں دکھ پہنچا سکیں،', 'که نه دښمنان او نه مینه‌ناک ملګري تا ته زیان ورسولی شي،'),
     ('If all men count with you, but none too much;', 'اگر سب لوگ تمہارے لیے اہم ہوں، مگر کوئی حد سے زیادہ نہیں؛', 'که ټول خلک تا ته ارزښت ولري، خو هېڅوک له حده زیات نه؛'),
     ('If you can fill the unforgiving minute', 'اگر تم بے رحم لمحے کو بھر سکو', 'که بې‌رحمه دقیقه ډکه کړای شې'),
     ("With sixty seconds' worth of distance run,", 'ساٹھ سیکنڈ کی دوڑ کے فاصلے سے،', 'د شپېتو ثانیو منډې د واټن په ارزښت،'),
     ("Yours is the Earth and everything that's in it,", 'تو زمین اور جو کچھ اس میں ہے سب تمہارا ہے،', 'نو ځمکه او هر څه چې پکې دي ستا دي،'),
     ("And—which is more—you'll be a Man, my son!", 'اور — جو اس سے بھی بڑھ کر ہے — تم ایک مرد بنو گے، میرے بیٹے!', 'او — چې تر دې هم زیات دی — ته به سړی شې، زما زویه!')],
]
for st in ST: p.group('lines', st)
poem = BOOK.record(p, 'eng12-u06-poem', 'If — poem text', 'اگر — نظم', 'که — شعر', 33, [54])
poem['sourceCoverIllustrationReview'] = 'Background photograph behind the poem is decorative; not reproduced. Urdu/Pashto give a line-by-line rendering.'

if __name__ == '__main__':
    BOOK.save(33, [(6, op), (6, poem)])
