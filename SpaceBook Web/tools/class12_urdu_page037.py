"""Urdu XII PDF37 (spread): printed pp.64–65 — Lesson 7 story end (source منٹو کے بہترین افسانے) and مشق Q1–Q10. Completes Lesson 7."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.p('…but his thought proved wrong. He was perfectly well. A little while later he had to take leave of the hospital.',
    '…مگر اُس کا خیال غلط ثابت ہوا۔ وہ ٹھیک ٹھاک تھا۔ تھوڑی دیر کے بعد ہی اُسے ہسپتال سے رخصت ہونا پڑا۔',
    '…خو د هغه فکر غلط ثابت شو. هغه بېخي روغ و. لږ وروسته یې له روغتونه رخصت شو.')
t.p('(Manto ke Behtareen Afsane)', '(منٹو کے بہترین افسانے)', '(د منټو غوره افسانې)')
tx = BOOK.record(t, 'urdu12-u7-text-6', 'Lesson text (6)', 'متنِ سبق (۶)', 'د لوست متن (۶)', 37, [64])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks.', '۱۔ خالی جگہ پُر کریں۔', '۱. تش ځایونه ډک کړئ.')
e.group('lines', [
    ('(a) The rhythm of his heart was ________ .', '(الف) اُس کے دل کی رفتار ________ تھی۔', '(الف) د هغه د زړه ټکان ________ و.'),
    ('(b) The patient has a heart ailment which is called ________ .', '(ب) مریض کو دل کا عارضہ ہے جسے ________ کہتے ہیں۔', '(ب) ناروغ د زړه ناروغي لري چې ________ ورته وايي.'),
    ('(c) He was conscious and could take stock of his ________ .', '(ج) وہ ہوش میں تھا اور اپنے ________ کا جائزہ لے سکتا تھا۔', '(ج) هغه په هوښ کې و او د خپل ________ کتنه یې کولی شوه.'),
    ('(d) He looked towards Manzoor with ________ eyes.', '(د) اُس نے ________ ہوئی آنکھوں سے منظور کی طرف دیکھا۔', '(د) هغه په ________ سترګو منظور ته وکتل.'),
    ("(e) In his eyes Manzoor's person had the rank of a ________ .", '(ہ) منظور کی ذات اُس کی نظر میں ________ کا درجہ رکھتی تھی۔', '(ه) د منظور شخصیت د هغه په نظر کې د ________ درجه درلوده.'),
])
e.p('2. Write answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) In what condition was Akhtar brought to the hospital?', '(الف) اختر کو کس حالت میں ہسپتال لایا گیا؟', '(الف) اختر په کوم حالت کې روغتون ته راوړل شو؟'),
    ("(b) What was the cause of Manzoor's illness?", '(ب) منظور کی بیماری کی وجہ کیا تھی؟', '(ب) د منظور د ناروغۍ لامل څه و؟'),
    ("(c) Why did Manzoor not want to go home from the hospital?", '(ج) منظور ہسپتال سے گھر کیوں نہیں جانا چاہتا تھا؟', '(ج) منظور ولې نه غوښتل له روغتونه کور ته لاړ شي؟'),
    ("(d) In Akhtar's view, what was the reason for his recovery?", '(د) اختر کے خیال میں اُس کے صحت مند ہونے کی کیا وجہ تھی؟', '(د) د اختر په فکر د هغه د روغېدو لامل څه و؟'),
    ("(e) How did the hospital staff treat Manzoor?", '(ہ) ہسپتال کے اہلکاروں کا منظور سے کیسا رویّہ تھا؟', '(ه) د روغتون کارکوونکو له منظور سره څنګه چلند کاوه؟'),
])
e.group('lines', [
    ("3. Write a paragraph on Manzoor's character.", '۳۔ منظور کے کردار پر ایک پیراگراف لکھیں۔', '۳. د منظور د کرکټر په اړه یو پراګراف ولیکئ.'),
    ('4. Write the summary of this story in your own words.', '۴۔ اس افسانے کا خلاصہ اپنے الفاظ میں لکھیں۔', '۴. د دې افسانې لنډیز په خپلو کلمو ولیکئ.'),
    ('5. Select at least five sentences from this story in which auxiliary verbs are used.', '۵۔ اس افسانے سے کم از کم ایسے پانچ جملوں کا انتخاب کریں جن میں امدادی افعال کا استعمال ہو۔', '۵. له دې افسانې لږ تر لږه پنځه داسې جملې وټاکئ چې پکې مرستندوي فعلونه کارول شوي وي.'),
    ('6. Put diacritics (iʿrāb):', '۶۔ اعراب لگائیں:', '۶. اعراب کېږدئ:'),
])
e.p('maflūj, muʿjiza, muʿayyan, masīḥā, marīz, marz, mānind [Urdu words to be vowelled]', 'مفلوج، معجزہ، معیّن، مسیحا، مریض، مرض، مانند۔', 'مفلوج، معجزه، معین، مسیحا، مریض، مرض، مانند [د اردو کلمې چې اعراب پرې کېښودل شي]')
e.p('7. Write the autobiography (āp bītī) of a patient admitted to a government hospital.', '۷۔ سرکاری ہسپتال میں داخل کسی مریض کی آپ بیتی لکھیں۔', '۷. په یوه دولتي روغتون کې د بستر شوي ناروغ ځان‌لیک (اپ بیتي) ولیکئ.')
e.p('8. Put punctuation marks at the appropriate places in the following paragraph.', '۸۔ درج ذیل پیراگراف میں مناسب مقامات پر رموزِ اوقاف لگائیں۔', '۸. په لاندې پراګراف کې په مناسبو ځایونو کې رموزِ اوقاف کېږدئ.')
e.p('In the present age electricity holds the position of a servant in homes factories and offices everywhere it is a necessity of our daily life you pressed a button the fan started the light came on the heater lit up the air-conditioner cooled the room in the refrigerator everything froze the food is ready the clothes are washed and ironed the lift took you up hundreds of feet in short as soon as you press the switch everything happens in a moment [printed without punctuation, to be punctuated]',
    'دورِ حاضر میں بجلی ایک خادمہ کی حیثیت رکھتی ہے گھروں کارخانوں اور دفتروں میں ہر جگہ یہ ہماری روزمرّہ زندگی کا لازمہ ہے بٹن دبایا پنکھا چل پڑا روشنی ہو گئی ہیٹر جل اُٹھا ایئر کنڈیشن نے کمرہ ٹھنڈا کر دیا ریفریجریٹر میں ہر چیز یخ بستہ ہو گئی کھانا تیار ہے کپڑے دُھل گئے استری ہو گئی لفٹ نے آپ کو سیکڑوں فُٹ بلندی پر پہنچا دیا غرض سوئچ دباتے ہی سب کچھ آن کی آن میں ہو جاتا ہے',
    'په اوسني وخت کې برېښنا د خدمتګارې حیثیت لري په کورونو فابریکو او دفترونو کې هر ځای دا زموږ د ورځني ژوند اړتیا ده تڼۍ مو کېکاږله پکه روانه شوه رڼا شوه هیټر بل شو ایرکنډیشن کوټه سړه کړه په یخچال کې هر شی کنګل شو ډوډۍ تیاره ده جامې ومینځل شوې اوتو شوې لفټ تاسو سلګونه فټه لوړ ته ورسولئ په لنډه توګه سویچ په کېکاږلو هر څه په یوه شېبه کې کېږي [پرته له تکي‌ایښودنې چاپ شوی، باید تکي ورکړل شي]')
e.p('9. According to the lesson, put (✓) against the sentences that are correct and (✗) against those that are wrong.', '۹۔ سبق کے مطابق جو جملے درست ہیں ان کے سامنے (✓) اور جو غلط ہیں ان کے سامنے (✗) کا نشان لگائیں۔', '۹. د لوست له مخې د سمو جملو مخې ته (✓) او د غلطو مخې ته (✗) نښه کېږدئ.')
e.group('lines', [
    ("a. A tremor was upon Akhtar's body.", 'ا۔ اختر کے بدن پر رعشہ طاری تھا۔', 'ا. د اختر پر بدن رېږدېدنه وه.'),
    ('b. Akhtar and Manzoor were of the same age.', 'ب۔ اختر اور منظور ہم عمر تھے۔', 'ب. اختر او منظور همعمره وو.'),
    ("c. Allah Almighty accepted Akhtar's prayer.", 'ج۔ اختر کی دعا اللہ تعالیٰ نے قبول کی۔', 'ج. الله تعالی د اختر دعا قبوله کړه.'),
    ('d. Manzoor recovered and went home.', 'د۔ منظور صحت یاب ہو کر گھر چلا گیا۔', 'د. منظور روغ شو او کور ته لاړ.'),
    ("e. Successful treatment alone ended Akhtar's illness.", 'ہ۔ کامیاب علاج نے ہی اختر کی بیماری ختم کی۔', 'ه. یوازې بریالۍ درملنې د اختر ناروغي پای ته ورسوله.'),
    ("f. A frail and emaciated old man lay on Manzoor's cot.", 'و۔ منظور کی چارپائی پر ایک نحیف و نزار بوڑھا پڑا تھا۔', 'و. د منظور پر کټ یو کمزوری او ډنګر زوړ سړی پروت و.'),
])
e.p('10. Write a story of about four hundred words with the title “Sacrifice and Selflessness (Īsār-o-Qurbānī)”.', '۱۰۔ تقریباً چار سو الفاظ پر مشتمل افسانہ لکھیں جس کا عنوان ایثار و قربانی ہو۔', '۱۰. شاوخوا څلور سوه کلمې یوه افسانه ولیکئ چې سرلیک یې "ایثار او قرباني" وي.')
ex = BOOK.record(e, 'urdu12-u7-exercise', 'Exercise', 'مشق', 'تمرین', 37, [64, 65])
issues = [{'id': 'urdu12-pdf037', 'unit': 7, 'printedPage': 65, 'description': 'Q8 paragraph is printed without punctuation (an exercise); kept as printed. Q9 items printed with letters ا ب ج د ہ و. Source line “(منٹو کے بہترین افسانے)” printed after the story.'}]

if __name__ == '__main__':
    BOOK.save(37, [(7, tx), (7, ex)], issues=issues, complete_units=[7])
