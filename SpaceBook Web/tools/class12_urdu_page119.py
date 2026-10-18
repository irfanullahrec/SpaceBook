"""Urdu XII PDF119 (spread): p.228 Ghazal 11 (Ahmad Nadeem Qasmi, d.2006 — copyrighted) couplet-wise summary; p.229 مشق Q1–Q7."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('Ghazal — Ahmad Nadeem Qasmi', 'غزل — احمد ندیمؔ قاسمی', 'غزل — احمد ندیم قاسمي')
s.p('[Couplet-wise summary — Ahmad Nadeem Qasmi (d. 2006) is in copyright; read the full ghazal (seven couplets) in the printed textbook, p. 228.]', '[شعر وار خلاصہ — احمد ندیمؔ قاسمی (وفات ۲۰۰۶ء) کا کلام کاپی رائٹ میں ہے؛ مکمل غزل (سات اشعار) درسی کتاب کے صفحہ ۲۲۸ پر پڑھیں۔]', '[بیت په بیت لنډیز — د احمد ندیم قاسمي (مړ ۲۰۰۶ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ غزل (اوه بیتونه) د درسي کتاب په ۲۲۸ مخ کې ولولئ.]')
for x in [
    ('1. (Maṭlaʿ) Who says that when death comes I will die? I am a river; I will merge into the ocean — death is not an end but a joining with something greater.',
     '۱۔ (مطلع) کون کہتا ہے کہ موت آئی تو میں مر جاؤں گا؟ میں تو دریا ہوں، سمندر میں اُتر جاؤں گا — موت فنا نہیں بلکہ کسی بڑی ہستی میں مل جانا ہے۔',
     '۱. (مطلع) څوک وايي چې مرګ راشي نو زه به مړ شم؟ زه سیند یم، په سمندر کې به ورګډ شم — مرګ فنا نه، بلکې له یوه لوی وجود سره یوځای کېدل دي.'),
    ('2. Leaving your door, where else would I go? At home I would be hemmed in, in the desert I would be scattered.',
     '۲۔ تیرا در چھوڑ کر میں اور کہاں جاؤں گا؟ گھر میں گھِر جاؤں گا اور صحرا میں بکھر جاؤں گا۔',
     '۲. ستا دروازه پرېږدم نو بل چېرې به ځم؟ په کور کې به راګېر شم، په صحرا کې به خپور شم.'),
    ('3. The trouble is that if I rise from your side, wherever I go I will find only one person — you.',
     '۳۔ مشکل یہ ہے کہ تیرے پہلو سے اُٹھوں گا تو جدھر جاؤں گا صرف ایک ہی شخص (محبوب) کو پاؤں گا۔',
     '۳. ستونزه دا ده چې که ستا له څنګه پاڅېږم، هر لور ته چې لاړ شم، یوازې یو کس (محبوب) به ومومم.'),
    ('4. Now I will come to your city like a traveller and pass on like the shadow of a cloud.',
     '۴۔ اب تیرے شہر میں ایک مسافر کی طرح آؤں گا اور بادل کے سائے کی مانند گزر جاؤں گا۔',
     '۴. اوس به ستا ښار ته د مسافر په څېر راشم او د ورېځې د سیوري په څېر به تېر شم.'),
    ('5. Your promise of loyalty became a wall in my path; otherwise I had thought that I would die whenever I wished.',
     '۵۔ تیرا پیمانِ وفا راہ کی دیوار بن گیا، ورنہ سوچا تھا کہ جب چاہوں گا مر جاؤں گا۔',
     '۵. ستا د وفا ژمنه زما د لارې دیوال شو، ګنې ما فکر کړی و چې کله مې زړه وغواړي، مړ به شم.'),
    ('6. My standard differs from the healers’: when I am wounded I become even more refined.',
     '۶۔ میرا معیار چارہ سازوں سے الگ ہے کہ میں زخم کھاؤں گا تو کچھ اور سنور جاؤں گا۔',
     '۶. زما معیار له درملګرو بېل دی: چې ټپي شم، نور هم ښکلی او سمېږم.'),
    ('7. (Maqṭaʿ) O Nadeem, I burn my life like a candle; I will be extinguished, but I will have brought on the morning.',
     '۷۔ (مقطع) اے ندیمؔ! میں زندگی شمع کی مانند جلاتا ہوں؛ بجھ تو جاؤں گا مگر صبح کر جاؤں گا۔',
     '۷. (مقطع) اې ندیمه! ژوند د شمعې په څېر سوځوم؛ مړ به شم، خو سهار به راولم.'),
    ('(Baseet, December 1989)', '(بسیط، دسمبر ۱۹۸۹ء)', '(بسیط، ډسمبر ۱۹۸۹ز)'),
]: s.p(*x)
UT = ('Ghazal: Who says that when death comes I shall die', 'غزل: کون کہتا ہے کہ موت آئی تو مر جاؤں گا', 'غزل: څوک وايي چې کله مرګ راشي زه به مړ شم', 'احمد ندیمؔ قاسمی')
po = BOOK.record(s, 'urdu12-u28-ghazal', 'Ghazal — couplet-wise summary', 'غزل — شعر وار خلاصہ', 'غزل — بیت په بیت لنډیز', 119, [228], unit_title=UT)
po['sourceGap'] = 'Ahmad Nadeem Qasmi (d. 2006) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 228 (7 couplets). Qasmi’s author note appears earlier with his prose lesson.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write the opening couplet (maṭlaʿ) and closing couplet (maqṭaʿ) of this ghazal and explain them.', '۱۔ اس غزل کا مطلع اور مقطع لکھ کر ان کی تشریح کریں۔', '۱. د دې غزل مطلع او مقطع ولیکئ او تشریح یې کړئ.'),
    ('2. Write the rhymes of this ghazal.', '۲۔ اس غزل کے قوافی لکھیں۔', '۲. د دې غزل قافیې ولیکئ.'),
    ('3. Put diacritics on the following words: samandar, ṣaḥrā, miʿyār, shamʿ, ṣubḥ.', '۳۔ درج ذیل الفاظ پر اعراب لگائیں: سمندر، صحرا، معیار، شمع، صبح۔', '۳. پر لاندې کلمو اعراب کېږدئ: سمندر، صحرا، معیار، شمع، صبح.'),
    ('4. Explain the couplet (the maqṭaʿ, beginning “zindagī shamʿ kī mānind…”, printed in the textbook).', '۴۔ شعر کی تشریح کریں: ’’زندگی شمع کی مانند جلاتا ہوں ندیمؔ / بجھ تو جاؤں گا مگر صبح تو کر جاؤں گا‘‘', '۴. بیت تشریح کړئ (مقطع: "ژوند د شمعې په څېر سوځوم…").'),
    ('5. In the couplet “Terā dar chhoṛ ke maiṉ aur kidhar jāʾūṉ gā / ghar meṉ ghir jāʾūṉ gā ṣaḥrā meṉ bikhar jāʾūṉ gā”: two words identical in writing but differing in diacritics are called tajnīs-e muḥarraf. In the above couplet the word “ghar/ghir” is tajnīs-e muḥarraf, used twice in different meanings. Write two couplets that contain tajnīs-e muḥarraf.', '۵۔ ’’تیرا در چھوڑ کے میں اور کدھر جاؤں گا / گھر میں گِھر جاؤں گا صحرا میں بکھر جاؤں گا‘‘ — دو الفاظ جو تحریر میں بالکل یکساں ہوں لیکن اعراب میں فرق ہو، تجنیسِ محرّف کہلاتے ہیں۔ درج بالا شعر میں لفظ ’’گھر‘‘ تجنیسِ محرّف ہے۔ جو دو بار الگ الگ معنوں میں استعمال ہوا ہے۔ دو ایسے اشعار لکھیں جن میں تجنیسِ محرّف موجود ہو۔', '۵. په بیت "ستا دروازه پرېږدم نو بل چېرې ځم / په کور (ګهر) کې به راګېر (ګهر) شم، په صحرا کې به خپور شم" کې: دوه کلمې چې په لیکنه کې یو شان وي خو اعراب یې توپیر ولري، "تجنیس محرف" بلل کېږي. په پورتني بیت کې "ګهر" تجنیس محرف دی چې دوه ځله په بېلو ماناوو کارول شوی. دوه داسې بیتونه ولیکئ چې پکې تجنیس محرف وي.'),
    ('6. A simile (tashbīh) is used in the last couplet of the ghazal. State its elements (arkān-e tashbīh).', '۶۔ غزل کے آخری شعر میں تشبیہ استعمال ہوئی ہے۔ اس کے ارکانِ تشبیہ بیان کریں۔', '۶. د غزل په وروستي بیت کې تشبیه کارول شوې. د هغې ارکان بیان کړئ.'),
    ('7. Write answers to the following questions according to the ghazal:', '۷۔ غزل کے مطابق درج ذیل سوالوں کے جواب لکھیں:', '۷. د غزل سره سم لاندې پوښتنو ته ځوابونه ولیکئ:'),
    ('(a) What metaphor has the poet used for himself?', '(ا) شاعر نے اپنے لیے کون سا استعارہ استعمال کیا ہے؟', '(الف) شاعر د ځان لپاره کومه استعاره کارولې؟'),
    ('(b) What is meant by being scattered in the desert?', '(ب) صحرا میں بکھرنے سے کیا مراد ہے؟', '(ب) په صحرا کې د خپرېدو مطلب څه دی؟'),
    ('(c) In the third couplet, for whom is the word “shakhṣ” (person) used?', '(ج) تیسرے شعر میں شخص کا لفظ کس کے لیے استعمال ہوا ہے؟', '(ج) په درېیم بیت کې "کس" کلمه د چا لپاره کارول شوې؟'),
    ("(d) What stands in the way of the poet's death?", '(د) شاعر کی موت میں کون سی چیز حائل ہے؟', '(د) د شاعر په مرګ کې کوم شی خنډ دی؟'),
    ('(e) What is meant by becoming refined by being wounded?', '(ہ) زخم کھا کر سنورنے سے کیا مراد ہے؟', '(ه) په ټپي کېدو د ښکلي کېدو مطلب څه دی؟'),
])
ex = BOOK.record(e, 'urdu12-u28-exercise', 'Exercise', 'مشق', 'تمرین', 119, [229])
issues = [{'id': 'urdu12-pdf119', 'unit': 28, 'printedPage': 229, 'description': 'Exercise Q4–Q5 quote two couplets of the (copyrighted) ghazal as part of the board-written exercise; reproduced as short quotations only. The ghazal itself is summarised.'}]

if __name__ == '__main__':
    BOOK.save(119, [(28, po), (28, ex)], issues=issues, complete_units=[28])
