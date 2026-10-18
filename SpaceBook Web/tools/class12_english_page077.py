"""PDF77 (printed 141–142): 'Once Upon a Time' (Gabriel Okara, 1962 — copyrighted) stanza-wise summary; About the Poet; Glossary."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
p = Builder()
p.h('Once Upon a Time', 'ایک زمانے میں', 'یو وخت و')
p.p('[Summary — the poem by Gabriel Okara (1962) is a modern copyrighted text; read it in the printed textbook, pp. 141–142.]', '[خلاصہ — گیبریل اوکارا (1962) کی نظم جدید کاپی رائٹ شدہ متن ہے؛ اسے درسی کتاب کے صفحات 141–142 میں پڑھیں۔]', '[لنډیز — د ګابریل اوکارا (1962) شعر نوی د کاپي رایټ لاندې متن دی؛ په چاپي درسي کتاب کې یې په 141–142 مخونو کې ولولئ.]')
S = [
    ('Stanzas 1–2: A father tells his son that once people laughed and shook hands sincerely, with their hearts and eyes; now they laugh only with their teeth, their cold eyes searching for advantage, and shake hands without feeling while searching his empty pockets.', 'بند 1–2: ایک باپ اپنے بیٹے کو بتاتا ہے کہ کبھی لوگ خلوص سے، دل اور آنکھوں سے ہنستے اور ہاتھ ملاتے تھے؛ اب وہ صرف دانتوں سے ہنستے ہیں، ان کی سرد آنکھیں فائدہ تلاش کرتی ہیں، اور وہ بغیر جذبے کے ہاتھ ملاتے ہوئے اس کی خالی جیبیں ٹٹولتے ہیں۔', 'بندونه 1–2: یو پلار خپل زوی ته وايي چې یو وخت خلکو په اخلاص، له زړه او سترګو خندل او لاسونه یې ورکول؛ اوس یوازې په غاښونو خاندي، سړې سترګې یې ګټه لټوي، او پرته له احساسه لاس ورکوي او د هغه تش جیبونه لټوي.'),
    ('Stanza 3: People say “Feel at home” and “Come again,” but after one or two visits the doors are shut on him.', 'بند 3: لوگ کہتے ہیں ’’اپنا گھر سمجھو‘‘ اور ’’پھر آنا‘‘، لیکن ایک دو ملاقاتوں کے بعد اس پر دروازے بند ہو جاتے ہیں۔', 'بند 3: خلک وایي "ځان په کور کې وګڼه" او "بیا راشه"، خو له یو یا دوو لیدنو وروسته دروازې پرې تړل کېږي.'),
    ('Stanzas 4–5: The father admits he too has learned to wear many “faces” — home face, office face, street face, host face, cocktail face — each with a fixed, conforming smile; he too laughs only with his teeth and says polite things he does not mean.', 'بند 4–5: باپ اعتراف کرتا ہے کہ اس نے بھی کئی ’’چہرے‘‘ پہننا سیکھ لیا ہے — گھر کا چہرہ، دفتر کا چہرہ، گلی کا چہرہ، میزبان کا چہرہ، دعوت کا چہرہ — ہر ایک پر ایک جمی ہوئی، رسمی مسکراہٹ؛ وہ بھی صرف دانتوں سے ہنستا ہے اور ایسی شائستہ باتیں کہتا ہے جن کا اسے مطلب نہیں۔', 'بندونه 4–5: پلار مني چې هغه هم ډېر "مخونه" اغوستل زده کړي — د کور مخ، د دفتر مخ، د کوڅې مخ، د کوربه مخ، د مېلمستیا مخ — هر یو په یوه ثابته، رسمي موسکا؛ هغه هم یوازې په غاښونو خاندي او داسې مؤدبانه خبرې کوي چې مطلب یې نه وي.'),
    ('Stanzas 6–7: He longs to unlearn these false ways and to be as sincere as he was when he was a child; seeing his “snake’s bare fangs” smile in the mirror, he asks his son to teach him again how to laugh and smile genuinely, as he once did.', 'بند 6–7: وہ ان جھوٹے طریقوں کو بھلانے اور ویسا ہی مخلص بننے کی آرزو کرتا ہے جیسا وہ بچپن میں تھا؛ آئینے میں اپنی ’’سانپ کے ننگے دانتوں‘‘ جیسی مسکراہٹ دیکھ کر وہ اپنے بیٹے سے کہتا ہے کہ اسے پھر سے سچے دل سے ہنسنا اور مسکرانا سکھائے، جیسے وہ کبھی کرتا تھا۔', 'بندونه 6–7: هغه هیله لري چې دا دروغجنې لارې هېرې کړي او هماغسې رښتینی شي لکه په ماشومتوب کې چې و؛ په هنداره کې د خپلې "د مار د لوڅو غاښونو" موسکا په لیدو، له خپل زوی غواړي چې بیا یې په رښتیا خندل او موسکا ور زده کړي، لکه یو وخت چې یې کوله.'),
]
for x in S: p.p(*x)
poem = BOOK.record(p, 'eng12-u15-poem-summary', 'Once Upon a Time — stanza-wise summary', 'ایک زمانے میں — بند وار خلاصہ', 'یو وخت و — بند په بند لنډیز', 77, [141, 142])
poem['sourceGap'] = 'Modern copyrighted poem (Gabriel Okara, 1962); stanza-wise summary in the app, not verbatim. Printed pp. 141–142.'
poem['sourceCoverIllustrationReview'] = 'Silhouette artwork behind the poem is decorative; not reproduced.'
a = Builder()
a.h('About the Poet:', 'شاعر کے بارے میں:', 'د شاعر په اړه:')
a.p('Gabriel Okara was born in Western Nigeria in 1921. Okara may be described as a highly original poet, uninfluenced by other poets. In 1979, he was awarded the Commonwealth Poetry Prize. Okara shows a concern regarding what happens when the ancient culture of Africa is faced with the onslaught of western culture.',
    'گیبریل اوکارا 1921 میں مغربی نائجیریا میں پیدا ہوئے۔ اوکارا کو ایک انتہائی منفرد شاعر کہا جا سکتا ہے جو دوسرے شاعروں سے متاثر نہیں۔ 1979 میں انہیں کامن ویلتھ پوئٹری پرائز دیا گیا۔ اوکارا اس بارے میں فکرمندی ظاہر کرتے ہیں کہ جب افریقہ کی قدیم ثقافت کو مغربی ثقافت کی یلغار کا سامنا ہو تو کیا ہوتا ہے۔',
    'ګابریل اوکارا په 1921 کې په لویدیځه نایجیریا کې زېږېدلی. اوکارا یو ډېر نوښتګر شاعر بلل کېدای شي چې د نورو شاعرانو تر اغېز لاندې نه دی. په 1979 کې هغه ته د مشترک‌المنافع د شعر جایزه ورکړل شوه. اوکارا د دې په اړه اندېښنه ښيي چې کله د افریقا لرغونی کلتور د لویدیځ کلتور له یرغل سره مخ شي، څه پېښېږي.')
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u15-gloss', [
    ('confirming ( v)', 'Relevant, fitting', 'متعلقہ، موزوں', 'اړوند، مناسب'),
    ('fangs (n)', 'the pointed poisonous teeth of the snake.', 'سانپ کے نوکیلے زہریلے دانت۔', 'د مار تېره زهرجن غاښونه.'),
    ('feel at home', 'feel easy, feel comfortable', 'بے تکلف محسوس کرنا، آرام محسوس کرنا', 'ارام احساس کول، ځان بې‌تکلفه احساسول'),
    ('good riddance', 'an expression used to show a feeling of relief after getting rid of someone or something unpleasant.', 'کسی ناگوار شخص یا چیز سے چھٹکارا پانے کے بعد اطمینان کا احساس ظاہر کرنے والا جملہ۔', 'یو څرګندونه چې د یو ناخوښ کس یا شي څخه د خلاصون وروسته د ارامۍ احساس ښيي.'),
    ('muting (v)', 'unexpressed, unspoken', 'غیر ظاہر شدہ، ان کہی', 'ناڅرګند، نه ویل شوی'),
    ('portrait (n)', 'Picture', 'تصویر', 'انځور'),
])
ab = BOOK.record(a, 'eng12-u15-about-glossary', 'About the Poet; Glossary', 'شاعر کے بارے میں؛ فرہنگ', 'د شاعر په اړه؛ وییپانګه', 77, [142])
ab['sourceCoverIllustrationReview'] = 'Portrait of Gabriel Okara is decorative; not reproduced.'
issues = [{'id': 'eng12-u15-copyright', 'unit': 15, 'printedPage': 141, 'description': 'The poem “Once Upon a Time” (Gabriel Okara, 1962) is modern and copyrighted; the app carries a stanza-wise summary with a sourceGap note. Glossary lists “confirming (v) — Relevant, fitting” for the poem’s “conforming” (adjective); printed as is.'}]

if __name__ == '__main__':
    BOOK.save(77, [(15, poem), (15, ab)], issues=issues)
