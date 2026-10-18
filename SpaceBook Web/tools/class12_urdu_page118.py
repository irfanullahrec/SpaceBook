"""Urdu XII PDF118 (spread): p.226 Ghazal 10 (Faiz, d.1984 — copyrighted) couplet-wise summary; p.227 مشق Q1–Q5 + note شعر."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('Ghazal — Faiz Ahmad Faiz', 'غزل — فیض احمد فیضؔ', 'غزل — فیض احمد فیض')
s.p('[Couplet-wise summary — Faiz (d. 1984) is in copyright; read the full ghazal (five couplets) in the printed textbook, p. 226.]', '[شعر وار خلاصہ — فیضؔ (وفات ۱۹۸۴ء) کا کلام کاپی رائٹ میں ہے؛ مکمل غزل (پانچ اشعار) درسی کتاب کے صفحہ ۲۲۶ پر پڑھیں۔]', '[بیت په بیت لنډیز — د فیض (مړ ۱۹۸۴ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ غزل (پنځه بیتونه) د درسي کتاب په ۲۲۶ مخ کې ولولئ.]')
for x in [
    ('1. The beloved’s company is always in the memory and the beloved’s hand always in hand; the poet gives thanks that none of his nights is now a night of separation.',
     '۱۔ محبوب کا ساتھ ہمیشہ یاد میں اور اس کا ہاتھ ہمیشہ ہاتھ میں ہے؛ شاعر شکر ادا کرتا ہے کہ اب اس کی راتوں میں ہجر کی کوئی رات نہیں۔',
     '۱. د محبوب ملګرتیا تل په یاد کې او لاس یې تل په لاس کې دی؛ شاعر شکر کوي چې اوس یې په شپو کې د بېلتون هېڅ شپه نشته.'),
    ('2. If conditions “there” are hard — where heart and life must be sold — he asks the lovers whether the beloved’s lane has not always had such conditions.',
     '۲۔ اگر وہاں حالات مشکل ہیں کہ دل اور جان بیچنے پڑیں، تو وہ دل والوں سے پوچھتا ہے کہ کیا کوچۂ جاناں میں ایسے حالات نہیں ہوتے؟',
     '۲. که هلته حالات سخت دي چې زړه او ځان باید وپلورل شي، نو له زړه والو پوښتي چې ایا د محبوب په کوڅه کې داسې حالات نه وي؟'),
    ('3. The grace with which one goes to the place of slaughter remains for ever; life comes and goes, and losing it is no great matter.',
     '۳۔ جس شان سے کوئی مقتل میں جاتا ہے وہی شان سلامت رہتی ہے؛ جان تو آنی جانی ہے، اس کا جانا کوئی بڑی بات نہیں۔',
     '۳. په کوم شان چې څوک وژنځي ته ځي، هماغه شان تلپاتې کېږي؛ ژوند راتلونکی او تلونکی دی، د هغه تلل لویه خبره نه ده.'),
    ('4. The field of loyalty is not a royal court where lineage is asked: “lover” is no one’s name, and love is no one’s caste.',
     '۴۔ میدانِ وفا کوئی دربار نہیں جہاں نام و نسب پوچھا جائے؛ عاشق کسی کا نام نہیں اور عشق کسی کی ذات نہیں۔',
     '۴. د وفا ډګر کوم دربار نه دی چې هلته نوم او نسب وپوښتل شي؛ عاشق د چا نوم نه دی او مینه د چا ذات نه ده.'),
    ('5. If the game is the game of love, stake whatever you wish without fear: if you win, splendid; and even if you lose, the game is not lost.',
     '۵۔ اگر بازی عشق کی بازی ہے تو بے خوف جو چاہو داؤ پر لگا دو؛ جیت گئے تو کیا کہنا، اور ہار بھی گئے تو بازی مات نہیں۔',
     '۵. که لوبه د مینې لوبه وي، بې‌وېرې هر څه چې غواړې په شرط کېږده؛ که وګټې نو څه ښه، او که وبایلې هم، لوبه نه ده بایلل شوې.'),
    ('(Zindan Nama)', '(زندان نامہ)', '(زندان نامه)'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u27-ghazal', 'Ghazal — couplet-wise summary', 'غزل — شعر وار خلاصہ', 'غزل — بیت په بیت لنډیز', 118, [226])
po['sourceGap'] = 'Faiz Ahmad Faiz (d. 1984) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 226 (5 couplets). The first line serves as the title only.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write the rhymes (qawāfī) of this ghazal.', '۱۔ اس غزل کے قوافی لکھیں۔', '۱. د دې غزل قافیې ولیکئ.'),
    ('2. What kind of compounds are kūcha-e jānāṉ, maidān-e wafā and nām-o-nasab?', '۲۔ کوچۂ جاناں، میدانِ وفا، نام و نسب، کون سے مرکبات ہیں۔', '۲. د محبوب کوڅه، د وفا ډګر، نوم او نسب کوم ډول مرکبات دي؟'),
    ('3. Find and write the conjunctions, possessive particles and prepositions in this ghazal.', '۳۔ اس غزل میں سے حروفِ عطف، حروفِ اضافی اور حروفِ جار تلاش کر کے لکھیں۔', '۳. په دې غزل کې عطفي، اضافي او جاري حروف ومومئ او ولیکئ.'),
    ('4. In which couplet of this ghazal is the figure of contrast present?', '۴۔ اس غزل کے کس شعر میں صنعتِ تضاد موجود ہے؟', '۴. د دې غزل په کوم بیت کې د تضاد صنعت شته؟'),
    ('5. Write answers to the following questions according to the ghazal:', '۵۔ غزل کے مطابق درج ذیل سوالوں کے جواب لکھیں:', '۵. د غزل سره سم لاندې پوښتنو ته ځوابونه ولیکئ:'),
    ('(a) In the first couplet, for what has thanks been expressed?', '(ا) پہلے شعر میں کس بات پر شکر کا اظہار کیا گیا ہے؟', '(الف) په لومړي بیت کې د څه شکر څرګند شوی؟'),
    ('(b) What is meant by “selling the heart”?', '(ب) دل بیچنے سے کیا مراد ہے؟', '(ب) د "زړه پلورلو" مطلب څه دی؟'),
    ('(c) According to the third couplet, which manner has permanence?', '(ج) تیسرے شعر کے مطابق کس انداز کو دوام حاصل ہے؟', '(ج) د درېیم بیت له مخې کوم انداز تلپاتې دی؟'),
    ('(d) What is not common between the field of loyalty and ordinary life?', '(د) میدانِ وفا اور عام زندگی میں کون سی چیز مشترک نہیں ہے؟', '(د) د وفا ډګر او عادي ژوند ترمنځ کوم شی ګډ نه دی؟'),
    ('(e) Why are winning and losing given the same status in love?', '(ہ) عشق میں جیت اور ہار کو ایک جیسا مقام کیوں دیا جاتا ہے؟', '(ه) په مینه کې ګټل او بایلل ولې یو شان ګڼل کېږي؟'),
])
ex = BOOK.record(e, 'urdu12-u27-exercise', 'Exercise', 'مشق', 'تمرین', 118, [227])
n = Builder()
n.p('Shiʿr (couplet): measured speech with a purpose that expresses one idea and both of whose lines (miṣraʿ) are in the same metre is called a “shiʿr”.', 'شعر: وہ کلامِ موزوں جو بامقصد ہو، ایک خیال کو ظاہر کرے اور جس کے دونوں مصرعے ایک ہی وزن میں ہوں ’’شعر‘‘ کہلاتا ہے۔', 'شعر: هغه موزون کلام چې موخه‌ناک وي، یو فکر څرګند کړي او دواړه مصرعې یې په یوه وزن کې وي، "شعر" بلل کېږي.')
nt = BOOK.record(n, 'urdu12-u27-note', 'Note: shiʿr (couplet)', 'شعر (تعریف)', 'شعر (تعریف)', 118, [227])

if __name__ == '__main__':
    BOOK.save(118, [(27, po), (27, ex), (27, nt)], complete_units=[27])
