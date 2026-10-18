"""Urdu XII PDF57 (spread): printed pp.104–105 — Lesson 11 مشق Q2–Q7. Completes Lesson 11."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.p('2. Fill in the blanks:', '۲۔ خالی جگہ پُر کریں:', '۲. تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) He did not have the ________ of keeping up with the times.', '(ا) ان کو زمانے کے ساتھ چلنے کا ________ نہیں آتا تھا۔', '(ا) هغه د زمانې سره د تګ ________ نه درلود.'),
    ('(b) Out of fear his ________ got choked.', '(ب) خوف کے مارے اس کی ________ بندھ گئی۔', '(ب) له وېرې یې ________ بند شو.'),
    ('(c) In the cold weather he was sitting outside ________ in the sun.', '(ج) وہ سردی کے موسم میں باہر بیٹھا دھوپ ________ رہا تھا۔', '(ج) هغه د یخنۍ په موسم کې بهر ناست په لمر کې ________ .'),
    ('(d) ________ boasts is not a good thing.', '(د) شیخی ________ اچھی بات نہیں۔', '(د) د ځان ستاینه ________ ښه خبره نه ده.'),
    ('(e) The landlord scolded the tenant in harsh ________ .', '(ہ) مالک مکان نے کرایا دار کو سخت ________ میں ڈانٹا۔', '(ه) د کور مالک کرایه‌دار په سختو ________ وورټه.'),
])
e.p('3. Explain the following passages with reference to the context: (a) the passage on p.101 beginning “He was so straightforward and guileless that he hardly seemed human…” and ending “…so no one was his friend.”; (b) the passage on p.102 beginning “For three days Master Ilyas sat on his cot with his quilt over his head like an igloo…” and ending “…‘Yes, I was feeling a little cold.’”',
    '۳۔ سیاق و سباق کے حوالے سے درج ذیل عبارتوں کی تشریح کریں: (ا) صفحہ ۱۰۱ کی وہ عبارت جو ’’وہ اتنے سیدھے اور اس قدر بے پیچ تھے کہ انسان ہی نہیں لگتے تھے…‘‘ سے شروع ہو کر ’’…اس لیے کوئی بھی ان کا دوست نہیں تھا۔‘‘ پر ختم ہوتی ہے؛ (ب) صفحہ ۱۰۲ کی وہ عبارت جو ’’مسلسل تین دن تک ماسٹر الیاس اپنی رضائی سر پر اگلو کی طرح اوڑھ کر…‘‘ سے شروع ہو کر ’’…ہاں جی تھوڑی سردی لگ رہی تھی۔‘‘ پر ختم ہوتی ہے۔ [دونوں عبارتیں درسی کتاب میں مکمل درج ہیں۔]',
    '۳. د سیاق و سباق په حواله لاندې متنونه تشریح کړئ: (ا) د ۱۰۱ مخ هغه متن چې په "هغه دومره ساده او بې‌چله و چې انسان نه ښکارېده…" پیلېږي او په "…نو هیڅوک یې ملګری نه و." پای ته رسېږي؛ (ب) د ۱۰۲ مخ هغه متن چې په "درې ورځې پرلپسې ماسټر الیاس خپله بړستن د ایګلو په څېر پر سر اغوستې…" پیلېږي او په "…هو جي، لږ یخني مې کېده." پای ته رسېږي. [دواړه متنونه په درسي کتاب کې بشپړ راغلي.]')
e.p('4. Fill in the blanks according to idiomatic usage (rozmarra):', '۴۔ روز مرہ کے مطابق خالی جگہ پُر کریں:', '۴. د ورځنۍ محاورې سره سم تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) He came forward grinding his ________ in anger.', '(الف) وہ غصے سے ________ پیستا ہوا آگے بڑھا۔', '(الف) هغه له غوسې ________ چیچل او مخکې راغی.'),
    ("(b) When he heard the news of Pakistan's victory he went ________ with joy.", '(ب) جب اُس نے پاکستان کی جیت کی خبر سنی تو خوشی سے ________ ہو گیا۔', '(ب) کله چې یې د پاکستان د بري خبر واورېد، له خوښۍ ________ شو.'),
    ('(c) Dust in your ________ — what ominous things you are saying!', '(ج) تمھارے ________ میں خاک، کیسی منحوس باتیں کر رہے ہو۔', '(ج) ستا په ________ کې دې خاوره شي، څه نحسې خبرې کوې!'),
    ("(d) You have dusted off your ________ and gone after my child.", '(د) تم تو ________ جھاڑ کر میرے بچے کے پیچھے پڑ گئے ہو۔', '(د) ته خو ________ وڅنډل او زما د ماشوم پسې شوې.'),
    ('(e) I could not watch this frightful scene and out of fear shut my ________ .', '(ہ) میں یہ خوفناک منظر نہ دیکھ سکا اور ڈر کے مارے اپنی ________ بند کر لیں۔', '(ه) دا ډارونکې منظره مې ونه شوه کتلی او له وېرې مې خپلې ________ پټې کړې.'),
])
e.p('5. Correct the sentences:', '۵۔ جملے درست کریں:', '۵. جملې سمې کړئ:')
e.group('lines', [
    ('(a) “Our homeland is progressing day by day.” [as printed]', '(الف) ہمارا وطن دن بدن ترقی کر رہا ہے۔', '(الف) "زموږ وطن ورځ په ورځ پرمختګ کوي." [لکه چې چاپ شوې]'),
    ('(b) “He was looking at me with amazement (ḥairāngī).”', '(ب) وہ حیرانگی سے میری طرف دیکھ رہا تھا۔', '(ب) "هغه په حیرانګۍ ماته کتل."'),
    ('(c) “My heart greatly wishes that I go on Hajj.”', '(ج) میرا بڑا دل کرتا ہے کہ حج پر جاؤں۔', '(ج) "زما زړه ډېر غواړي چې حج ته لاړ شم."'),
    ('(d) “I have come to say an important thing to you.”', '(د) میں آپ سے ایک ضروری بات کہنے آیا ہوں۔', '(د) "زه تاسو ته د یوې مهمې خبرې ویلو ته راغلی یم."'),
    ('(e) “Hearing his cries, people ran to help.”', '(ہ) اس کی چیخ و پکار سن کر لوگ مدد کے لیے دوڑے۔', '(ه) "د هغه چیغې په اورېدو خلک د مرستې لپاره ورمنډه شول."'),
])
e.p('6. Put punctuation marks at the appropriate places in the following sentences:', '۶۔ درج ذیل جملوں میں مناسب مقامات پر رموزِ اوقاف لگائیں:', '۶. په لاندې جملو کې په مناسبو ځایونو کې رموزِ اوقاف کېږدئ:')
e.group('lines', [
    ('(a) Whenever you see him he is riding the horse of the wind (building castles in the air)', '(الف) اسے جب دیکھو ہوا کے گھوڑے پر سوار ہوتا ہے', '(الف) هر کله یې چې ووینې، د باد پر اس سپور وي (هوايي ماڼۍ جوړوي)'),
    ('(b) The important points of this essay are these', '(ب) اس مضمون کے اہم نکات یہ ہیں', '(ب) د دې مقالې مهم ټکي دا دي'),
    ('(c) The Messenger of Allah ﷺ said all human beings are equal', '(ج) رسول اللہ صلی اللہ علیہ وسلم نے فرمایا سب انسان برابر ہیں', '(ج) رسول الله ﷺ وفرمایل ټول انسانان برابر دي'),
    ('(d) Boy what are you doing here', '(د) لڑکے تم یہاں کیا کر رہے ہو', '(د) هلکه ته دلته څه کوې'),
    ('(e) “Not everyone who shakes hands is a friend” — this line of Ahmad Faraz is based on truth', '(ہ) دوست ہوتا نہیں ہر ہاتھ ملانے والا احمد فراز کا یہ مصرع حقیقت پر مبنی ہے', '(ه) "هر لاس ورکوونکی دوست نه وي" — د احمد فراز دا مصرع پر حقیقت ولاړه ده'),
])
e.p('7. In Urdu the following verbs are used as auxiliary (helping) verbs. With their help make two sentences each in which they are used as auxiliary verbs: dēnā, lēnā, ānā, ḍālnā, jānā, paṛnā, uṭhnā.', '۷۔ اُردو میں درج ذیل افعال بطور معاون افعال استعمال کیے جاتے ہیں۔ آپ ان کی مدد سے دو دو جملے بنائیں۔ جن میں یہ بطور امدادی یا معاون فعل استعمال ہوں۔ دینا، لینا، آنا، ڈالنا، جانا، پڑنا، اُٹھنا', '۷. په اردو کې لاندې فعلونه د مرستندویو فعلونو په توګه کارول کېږي. د هغو په مرسته دوه دوه جملې جوړې کړئ چې پکې د مرستندوي فعل په توګه کارول شوي وي: دینا، لینا، انا، ډالنا، جانا، پړنا، اټهنا.')
for p in e.paras:
    pass
ex = BOOK.record(e, 'urdu12-u11-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 57, [104, 105])
issues = [{'id': 'urdu12-pdf057', 'unit': 11, 'printedPage': 104, 'description': 'The scan is heavily annotated by hand: answers written in every blank of Q2 and Q4, corrections over Q5, and seven handwritten sentences under Q7. These are owner notes and are excluded; the printed blanks were reconstructed from the printed text around them (Q5(e) ends “…مدد کے لیے دوڑے” with a handwritten addition). Q3 quotes two passages of the copyrighted story; the app gives page references instead.'}]

if __name__ == '__main__':
    BOOK.save(57, [(11, ex)], issues=issues, complete_units=[11])
