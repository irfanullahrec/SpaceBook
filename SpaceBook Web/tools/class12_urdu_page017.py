"""Urdu XII PDF17 (spread): printed pp.24–25 — Lesson 3 text end (source: بیگمات کے آنسو) and مشق Q1–Q5. Completes Lesson 3."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('The second day too passed in the same way, and we kept fast upon fast in starvation. Towards evening the chaudhri’s man brought milk and sweet rice and said: “Today we had a niyāz (votive offering); this is its food, and five rupees are of zakāt. Every year we give the zakāt of our goats, but this time we have given it in cash.”',
     'دوسرا دن بھی یوں ہی گزر گیا اور فاقہ میں روزہ پر روزہ رکھا۔ شام کے قریب چودھری کا آدمی دودھ اور میٹھے چاول لایا اور بولا: آج ہمارے نیاز تھی، یہ اس کا کھانا ہے اور پانچ روپیہ زکوٰۃ کے ہیں۔ ہر سال بکریوں کی زکوٰۃ دیا کرتے ہیں مگر اب کے نقد دے دیا ہے۔',
     'دویمه ورځ هم همداسې تېره شوه او په لوږه کې مو روژه پر روژه ونیوله. ماښام ته نږدې د چوهدري سړی شیدې او خواږه وریجې راوړې او ویې ویل: "نن زموږ نیاز (نذر) و، دا د هغې خواړه دي او پنځه روپۍ د زکات دي. هر کال د وزو زکات ورکوو، خو دا ځل مو نغدې ورکړې."'),
    ('This food and money seemed to me such a blessing as if I had been given a kingdom. Joyfully I told the whole story to Mother and kept giving thanks to God, but I did not know that the turn of misfortune had cast its shadow on the man’s mind, while womankind still stood just as before upon her ancient sense of honour.',
     'یہ کھانا اور روپے مجھ کو ایسی نعمت معلوم ہوئی گویا بادشاہت مل گئی۔ خوشی خوشی والدہ کے آگے سارا قصّہ کہا۔ کہتا جاتا تھا اور خدا کا شکرانہ بھیجتا جاتا تھا، مگر یہ خبر نہ تھی کہ گردشِ فلاکت نے مرد کے خیال پر تو اثر ڈال دیا، لیکن عورت ذات جوں کی توں اپنی قدیمی غیرت داری پر قائم ہے۔',
     'دا خواړه او روپۍ ماته داسې نعمت ښکاره شول لکه پاچاهي چې راکړل شوې وي. په خوشحالۍ مې مور ته ټوله کیسه وکړه؛ ویل به مې او د خدای شکر به مې ایسته، خو نه پوهېدم چې د بدمرغۍ ګردش د نارینه پر فکر اغېز کړی، خو ښځینه لا هم هماغسې په خپل پخواني غیرت ولاړه ده.'),
    ('So I saw Mother’s colour change. Despite the weakness of starvation she changed her look and said: “Shame on your honour! You have brought charity and zakāt and are pleased. Oh, it would have been better to die than this. Although we have been wiped out, our spirit has not died. To go out into the field and die, or to kill, and to take bread by the strength of the sword, is our work; living on alms is not our way.”',
     'چنانچہ میں نے دیکھا کہ والدہ کا رنگ متغیر ہو گیا۔ باوجود فاقہ کی ناتوانی کے انھوں نے تیور بدل کر کہا: تُف ہے تیری غیرت پر، خیرات اور زکوٰۃ لے کر آیا ہے اور خوش ہوتا ہے۔ ارے اس سے مر جانا بہتر تھا۔ اگرچہ ہم مٹ گئے، مگر ہماری حرارت نہیں مٹی۔ میدان میں نکل کر مر جانا یا مار ڈالنا اور تلوار کے زور سے روٹی لینا ہمارا کام ہے، صدقہ خوری ہمارا شیوہ نہیں۔',
     'نو ومې لیدل چې د مور رنګ بدل شو. د لوږې له کمزورۍ سره سره یې تندی تریو کړ او ویې ویل: "پر ستا غیرت دې تف وي! خیرات او زکات دې راوړي او خوشحاله یې. اې، له دې خو مړه کېدل ښه وو. که څه هم موږ له منځه لاړو، خو زموږ تودوخه نه ده مړه شوې. ډګر ته وتل او مړه کېدل یا وژل او د تورې په زور ډوډۍ اخیستل زموږ کار دی؛ صدقه خوړل زموږ دود نه دی."'),
    ('At these words of Mother I broke into a sweat and my hands and feet went cold with shame. I wanted to get up and return these things, but Mother stopped me and said: “If this is what God wills, what can we do? Everything must be borne.” Saying this, she kept the food, and after breaking the fast we all ate together. Five rupees’ worth of flour was bought, with which Ramadan passed safely and well.',
     'والدہ کی ان باتوں سے مجھے پسینا آ گیا اور شرم کے مارے ہاتھ پاؤں ٹھنڈے ہو گئے۔ چاہا کہ اٹھ کر یہ چیزیں واپس کر آؤں، مگر والدہ نے روکا اور کہا: خدا ہی کو یہ منظور ہے، تو ہم کیا کریں، سب کچھ سہنا ہوگا۔ یہ کہہ کر کھانا رکھ لیا اور روزہ کھولنے کے بعد ہم سب نے مل کر کھا لیا۔ پانچ روپے کا آٹا منگوا لیا جس سے رمضان خیر و خوبی سے بسر ہو گیا۔',
     'د مور په دې خبرو خوله راته راغله او له شرمه مې لاسونه او پښې سړې شوې. ومې غوښتل چې پاڅېږم او دا شیان بېرته ورکړم، خو مور منع کړم او ویې ویل: "که د خدای همدا خوښه وي، نو موږ څه وکړو؟ هر څه باید وزغمو." دا یې وویل او خواړه یې وساتل، او د روژې له ماتولو وروسته موږ ټولو یوځای وخوړل. د پنځو روپیو اوړه مو راوغوښتل چې روژه پرې په خیر او ښه توګه تېره شوه.'),
    ('After that we stayed six months more in the village, then came back to Delhi. On coming here Mother passed away, and I married off my sister. The English government has fixed a pension of five rupees a month for me too, on which my whole life now depends.',
     'اس کے بعد چھے مہینے گاؤں میں اور رہے، پھر دہلی چلے آئے۔ یہاں آ کر والدہ کا انتقال ہو گیا اور بہن کی شادی کر دی۔ انگریزی سرکار نے میری بھی پانچ روپے ماہوار پنشن مقرر کر دی ہے، جس پر آج کل زندگی کا انحصار ہے۔',
     'له هغه وروسته شپږ میاشتې نورې په کلي کې پاتې شو، بیا ډهلي ته راغلو. دلته په راتلو مور مړه شوه او د خور واده مې وکړ. انګرېزي حکومت ماته هم د میاشتې پنځه روپۍ تقاعد ټاکلی، چې اوس مې ټول ژوند پرې ولاړ دی.'),
    ('(Begumat ke Aansoo)', '(بیگمات کے آنسو)', '(بېګمات کې انسو)'),
]: t.p(*x)
tx = BOOK.record(t, 'urdu12-u3-text-4', 'Lesson text (4)', 'متنِ سبق (۴)', 'د لوست متن (۴)', 17, [24])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '۱۔ درج ذیل سوالات کے جوابات لکھیں۔', '۱. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ("(a) Why was Mirza Saleem upset by his mother's words?", '(الف) مرزا سلیم والدہ کی باتوں سے کیوں آزردہ تھا؟', '(الف) میرزا سلیم د مور په خبرو ولې خپه و؟'),
    ('(b) What was the scene in the Jama Masjid in Ramadan in the Mughal period?', '(ب) مغلیہ دور میں رمضان میں جامع مسجد میں کیا سماں ہوتا تھا؟', '(ب) د مغلو په دوره کې په روژه کې په جامع جومات کې څه منظره وه؟'),
    ('(c) What was the condition of the Jama Masjid in Ramadan after 1857?', '(ج) ۱۸۵۷ء کے بعد رمضان میں جامع مسجد کی کیا حالت تھی؟', '(ج) له ۱۸۵۷ز وروسته په روژه کې د جامع جومات حالت څنګه و؟'),
    ('(d) Who was Mirza Shahzor?', '(د) مرزا شہ زور کون تھے؟', '(د) میرزا شهزور څوک و؟'),
    ("(e) How did the Mewatis treat Mirza Shahzor's family?", '(ہ) میواتیوں نے مرزا شہ زور کے خاندان سے کیسا برتاؤ کیا؟', '(ه) میواتیانو د میرزا شهزور له کورنۍ سره څنګه چلند وکړ؟'),
])
e.p('2. Fill in the blanks:', '۲۔ خالی جگہ پُر کریں:', '۲. تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) Mirza Saleem used to hold gatherings of singing and music in ________ .', '(الف) مرزا سلیم ________ میں گانے بجانے کی محفلیں سجاتے۔', '(الف) میرزا سلیم به په ________ کې د سندرو او موسیقۍ محفلونه جوړول.'),
    ('(b) At the courtier’s suggestion Mirza Saleem began to go to ________ .', '(ب) مصاحب کے کہنے پر مرزا سلیم ________ جانے لگے۔', '(ب) د درباري په ویلو میرزا سلیم ________ ته تلل پیل کړل.'),
    ("(c) Mirza Shahzor's mother was Mirza Saleem's ________ .", '(ج) مرزا شہ زور کی والدہ مرزا سلیم کی ________ تھی۔', '(ج) د میرزا شهزور مور د میرزا سلیم ________ وه.'),
    ('(d) The English call the War of Independence of 1857 ________ .', '(د) انگریز ۱۸۵۷ء کی جنگِ آزادی کو ________ کہتے ہیں۔', '(د) انګرېزان د ۱۸۵۷ز د خپلواکۍ جګړې ته ________ وايي.'),
    ("(e) ________ looted all the goods and belongings of Mirza Shahzor and his family.", '(ہ) ________ نے مرزا شہ زور اور اُس کے خاندان کا سارا مال و اسباب لُوٹ لیا۔', '(ه) ________ د میرزا شهزور او د هغه د کورنۍ ټول مال او سامان لوټ کړ.'),
    ('(f) The Mughal dynasty was of the lineage of ________ .', '(و) مغل خاندان ________ کی نسل سے تھا۔', '(و) د مغلو کورنۍ د ________ له نسل څخه وه.'),
])
e.p('3. Explain the following punctuation marks: colon (rābiṭa), colon-dash (tafṣīliya), brackets (qausain), dash (khaṭ).', '۳۔ درج ذیل رموزِ اوقاف کی وضاحت کریں: رابطہ، تفصیلیہ، قوسین، خط۔', '۳. لاندې رموزِ اوقاف تشریح کړئ: رابطه، تفصیلیه، قوسین، خط.')
e.p('4. Write a summary of this lesson.', '۴۔ اس سبق کا خلاصہ لکھیں۔', '۴. د دې لوست لنډیز ولیکئ.')
e.p('5. Write an essay on the personality of a close friend, teacher, dear one or relative.', '۵۔ اپنے کسی قریبی دوست، استاد، عزیز یا رشتے دار کی شخصیت پر ایک مضمون تحریر کریں۔', '۵. د خپل یوه نږدې ملګري، ښوونکي، ګران یا خپلوان د شخصیت په اړه یوه مقاله ولیکئ.')
ex = BOOK.record(e, 'urdu12-u3-exercise', 'Exercise', 'مشق', 'تمرین', 17, [25])
issues = [{'id': 'urdu12-pdf017', 'unit': 3, 'printedPage': 25, 'description': 'Exercise Q3 asks about قوسین and خط, which are not explained in Lessons 1–3 (they are not defined before this point in the book). Handwritten answers and page references in the scan are owner notes, excluded.'}]

if __name__ == '__main__':
    BOOK.save(17, [(3, tx), (3, ex)], issues=issues, complete_units=[3])
