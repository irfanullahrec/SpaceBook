"""Urdu XII PDF127 (spread): p.244 Ghazal 16 (Shahzad Ahmad, d.2012 — copyrighted) couplet-wise summary; p.245 مشق Q1–Q3."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('Ghazal — Shahzad Ahmad', 'غزل — شہزادؔ احمد', 'غزل — شهزاد احمد')
s.p('[Couplet-wise summary — Shahzad Ahmad (d. 2012) is in copyright; read the full ghazal (six couplets) in the printed textbook, p. 244.]', '[شعر وار خلاصہ — شہزادؔ احمد (وفات ۲۰۱۲ء) کا کلام کاپی رائٹ میں ہے؛ مکمل غزل (چھے اشعار) درسی کتاب کے صفحہ ۲۴۴ پر پڑھیں۔]', '[بیت په بیت لنډیز — د شهزاد احمد (مړ ۲۰۱۲ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ غزل (شپږ بیتونه) د درسي کتاب په ۲۴۴ مخ کې ولولئ.]')
for x in [
    ('1. If nothing else, at least this much they used to do: on seeing me they would recognise me.',
     '۱۔ اور کچھ نہ سہی، اتنا تو وہ کیا کرتے تھے کہ مجھے دیکھ کر پہچان لیا کرتے تھے۔',
     '۱. که بل څه نه، دومره خو به یې کول چې ما به یې په لیدو پېژندم.'),
    ('2. We who used to insist on everything at last submitted to your will.',
     '۲۔ ہم جو ہر بات پر اصرار کیا کرتے تھے، آخر کار تیری رضا کے پابند ہو گئے۔',
     '۲. موږ چې پر هره خبره مو ټینګار کاوه، په پای کې ستا رضا ته تابع شوو.'),
    ('3. Those honourable people who would not even drink the water of your city are now dust in your lanes.',
     '۳۔ وہ عزت والے جو تیرے شہر کا پانی تک نہ پیا کرتے تھے، اب تیری گلیوں کی خاک ہیں۔',
     '۳. هغه عزتمن چې ستا د ښار اوبه یې هم نه څښلې، اوس ستا د کوڅو خاوره دي.'),
    ('4. Now even the dignity of man counts for nothing — whereas people once took a stone for God.',
     '۴۔ اب انسان کی عظمت بھی کوئی چیز نہیں رہی، حالانکہ کبھی لوگ پتھر کو خدا مان لیا کرتے تھے۔',
     '۴. اوس د انسان عظمت هم څه شی نه دی، سره له دې چې یو وخت خلکو ډبره خدای منله.'),
    ('5. Friends, now you call me fit to be beheaded — you are the very ones who used to stitch my wounds.',
     '۵۔ دوستو! اب تم مجھے گردن زدنی کہتے ہو، حالانکہ تم وہی ہو جو میرے زخم سیا کرتے تھے۔',
     '۵. ملګرو! اوس ما د سر پرې کولو وړ بولئ، حال دا چې تاسو هماغه یاست چې زما ټپونه به مو ګنډل.'),
    ('6. (Maqṭaʿ) O Shahzad, now our eyes are fixed on the stars — once we too used to live in the earth.',
     '۶۔ (مقطع) اے شہزادؔ! اب تو ستاروں پر نظریں لگی ہیں، کبھی ہم لوگ بھی مٹی میں جیا کرتے تھے۔',
     '۶. (مقطع) اې شهزاده! اوس مو سترګې پر ستورو دي، یو وخت موږ هم په خاوره کې ژوند کاوه.'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u33-ghazal', 'Ghazal — couplet-wise summary', 'غزل — شعر وار خلاصہ', 'غزل — بیت په بیت لنډیز', 127, [244])
po['sourceGap'] = 'Shahzad Ahmad (d. 2012) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 244 (6 couplets). No source line is printed.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write answers to the following questions according to the ghazal.', '۱۔ غزل کے مطابق درج ذیل سوالات کے جوابات لکھیں۔', '۱. د غزل سره سم لاندې پوښتنو ته ځوابونه ولیکئ.'),
    ('(a) Why did the poet give up insisting?', '(ا) شاعر نے اصرار کرنا کیوں چھوڑ دیا؟', '(الف) شاعر ولې ټینګار پرېښود؟'),
    ('(b) What is meant by being the dust of the lanes?', '(ب) گلیوں کی خاک ہونے سے کیا مراد ہے؟', '(ب) د کوڅو خاوره کېدو مطلب څه دی؟'),
    ('(c) What is meant by stitching wounds?', '(ج) زخم سینے سے کیا مراد لی گئی ہے؟', '(ج) د ټپونو ګنډلو مطلب څه دی؟'),
    ("(d) What does not even drinking the water of someone's city indicate?", '(د) کسی کے شہر کا پانی تک نہ پینا، کس بات کی غمازی کرتا ہے؟', '(د) د چا د ښار اوبه هم نه څښل د څه نښه ده؟'),
    ('(e) Why has the poet fixed his eyes on the stars?', '(ہ) شاعر نے ستاروں پر نظریں کیوں لگائی ہیں؟', '(ه) شاعر ولې پر ستورو سترګې نیولې؟'),
    ('2. Write the refrain (radīf) of this ghazal.', '۲۔ اس غزل کی ردیف لکھیں۔', '۲. د دې غزل ردیف ولیکئ.'),
    ('3. Put diacritics on the following words: gardan-zadanī, riẓā, iṣrār, shahr, ʿaẓmat.', '۳۔ درج ذیل الفاظ پر اعراب لگائیں: گردن زدنی، رضا، اصرار، شہر، عظمت۔', '۳. پر لاندې کلمو اعراب کېږدئ: د سر پرې کولو وړ، رضا، اصرار، ښار، عظمت.'),
    ('3. Explain the following couplet (couplet 2: “Ākhir-kār hue terī riẓā ke pāband / ham ke har bāt pe iṣrār kiyā karte the”).', '۳۔ درج ذیل شعر کی تشریح کریں: ’’آخر کار ہوئے تیری رضا کے پابند / ہم کہ ہر بات پہ اصرار کیا کرتے تھے‘‘', '۳. لاندې بیت تشریح کړئ (دویم بیت).'),
])
ex = BOOK.record(e, 'urdu12-u33-exercise', 'Exercise', 'مشق', 'تمرین', 127, [245])
issues = [{'id': 'urdu12-pdf127', 'unit': 33, 'printedPage': 245, 'description': 'Exercise numbering repeats “۳” (two questions numbered 3) — retained as printed. Q3 (second) quotes one couplet of the copyrighted ghazal as part of the board exercise.'}]

if __name__ == '__main__':
    BOOK.save(127, [(33, po), (33, ex)], issues=issues, complete_units=[33])
