"""Urdu XII PDF12 (spread): printed pp.14–15 — Lesson 2 مشق Q2–Q7 with رموزِ اوقاف: واوین، سوالیہ، ندائیہ/فجائیہ. Completes Lesson 2."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.p('2. Fill in the blanks with suitable words.', '۲۔ خالی جگہ مناسب الفاظ سے پُر کریں۔', '۲. تش ځایونه په مناسبو کلمو ډک کړئ.')
e.group('lines', [
    ('(a) Socrates’ father was a ________ .', '(الف) سقراط کا باپ ایک ________ تھا۔', '(الف) د سقراط پلار یو ________ و.'),
    ('(b) In Socrates’ view, to ________ anything is a useless act.', '(ب) سقراط کے نزدیک کسی چیز کا ________ کرنا ایک فضول کام ہے۔', '(ب) د سقراط په نظر د هر شي ________ کول یو بېځایه کار دی.'),
    ('(c) The jailer urged Socrates to ________ .', '(ج) داروغۂ جیل نے سقراط کو ________ جانے کی ترغیب دی۔', '(ج) د زندان مشر سقراط ته د ________ تګ هڅونه وکړه.'),
    ('(d) Socrates’ temperament took on the influence of ________ quickly.', '(د) سقراط کی طبیعت نے تیزی کے ساتھ ________ کا اثر قبول کیا۔', '(د) د سقراط طبیعت په چټکۍ د ________ اغېز ومانه.'),
    ('(e) Socrates considered an ________ person deserving of pity.', '(ہ) سقراط ایک ________ شخص کو واجب الرحم سمجھتا تھا۔', '(ه) سقراط یو ________ کس د رحم وړ ګڼه.'),
])
e.p('3. Write the summary of this essay in your own words.', '۳۔ اس مضمون کا خلاصہ اپنے الفاظ میں لکھیں۔', '۳. د دې مقالې لنډیز په خپلو کلمو ولیکئ.')
e.p('4. Write the following words with correct diacritics (iʿrāb).', '۴۔ درج ذیل الفاظ درست اعراب کے ساتھ لکھیں۔', '۴. لاندې کلمې په سمو اعرابو ولیکئ.')
e.p('jamādāt, pairawī, rashk-o-ḥasad, istiqlāl, ẕillat [Urdu words to be vowelled]', 'جمادات، پیروی، رشک و حسد، استقلال، ذلت۔', 'جمادات، پیروي، رشک او حسد، استقلال، ذلت [د اردو کلمې چې اعراب پرې کېښودل شي]')
e.p('5. Write a detailed essay on the life and services of a leader of the Pakistan Movement.', '۵۔ تحریکِ پاکستان کے کسی رہنما کی زندگی اور خدمات پر ایک مفصّل مضمون لکھیں۔', '۵. د پاکستان د غورځنګ د یوه مشر د ژوند او خدماتو په اړه یوه مفصله مقاله ولیکئ.')
e.h('Punctuation marks (Rumūz-e-Awqāf):', 'رموزِ اوقاف:', 'د تکي‌ایښودنې نښې (رموزِ اوقاف):')
e.p('Inverted commas (wāwain) (“ ”): When a quotation is given or someone’s saying is cited, these signs are placed at its beginning and end.', 'واوین (’’ ‘‘): جب کوئی اقتباس دیا جائے یا کسی کا قول نقل کیا جائے تو اس کے آغاز اور اختتام پر یہ علامات لگائی جاتی ہیں۔', 'اقتباس نښې (واوین) (“ ”): کله چې یو اقتباس راوړل شي یا د چا خبره نقل شي، د هغې په پیل او پای کې دا نښې ایښودل کېږي.')
e.p('How well someone has said: “God helps those who help themselves.”', 'کسی نے کیا خوب کہا ہے: ’’خدا اُن کی مدد کرتا ہے جو اپنی مدد آپ کرتے ہیں‘‘', 'یو چا څومره ښه ویلي: "خدای د هغو مرسته کوي چې د ځان مرسته پخپله کوي"')
e.p('Question mark (sawāliya) (?): This sign is placed at the end of interrogative sentences. For example:-', 'سوالیہ (؟): یہ علامت سوالیہ جملوں کے آخر میں لگائی جاتی ہے۔ جیسے:-', 'د پوښتنې نښه (سوالیه) (؟): دا نښه د پوښتنیزو جملو په پای کې ایښودل کېږي. لکه:-')
e.group('lines', [('What is it?', 'کیا ہے؟', 'څه دي؟'), ('Where are you?', 'تم کہاں ہو؟', 'ته چېرته یې؟'), ('Who won the match? etc.', 'میچ کون جیتا؟ وغیرہ', 'لوبه چا وګټله؟ او نور')])
e.p('Vocative or exclamation mark (nidāʾiya / fujāʾiya) (!): When someone is to be addressed, the vocative mark is placed; and when the expression of any emotion — love, hatred, contempt, fear, wonder, anger, joy, warning or praise — is intended, this sign is placed as an exclamation mark.',
    'ندائیہ یا فجائیہ (!): کسی کو مخاطب کرنا ہو تو ندائیہ کی علامت لگائی جاتی ہے اور کسی بھی جذبے؛ محبت، نفرت، حقارت، خوف، تعجب، غصہ، خوشی، تنبیہ یا تحسین کا اظہار کرنا مقصود ہو تو یہ علامت بطورِ فجائیہ لگائی جاتی ہے۔',
    'د ندا یا تعجب نښه (ندائیه / فجائیه) (!): کله چې څوک مخاطب کېږي، د ندا نښه ایښودل کېږي؛ او کله چې د کوم احساس — مینې، کرکې، سپکاوي، وېرې، حیرانتیا، غوسې، خوښۍ، خبرداري یا ستاینې — څرګندول موخه وي، دا نښه د تعجب په توګه ایښودل کېږي.')
e.group('lines', [('Boy! Come here a moment.', 'لڑکے! ذرا ادھر آؤ۔', 'هلکه! لږ دېخوا راشه.'), ('Beware! There is danger there.', 'خبردار! وہاں خطرہ ہے۔', 'خبردار! هلته خطر دی.'),
                  ('Well done! You will surely succeed.', 'شاباش! تم ضرور کامیاب ہو گے۔', 'شاباش! ته به خامخا بریالی شې.'), ('Alas! You could not do even this much.', 'افسوس! تم سے اتنا بھی نہ ہو سکا۔', 'افسوس! له تا دومره هم ونه شول.')])
e.p('6. Write at least five sentences using the above punctuation marks.', '۶۔ درج بالا رموزِ اوقاف کو استعمال کرتے ہوئے کم از کم پانچ جملے لکھیں۔', '۶. د پورته رموزِ اوقاف په کارولو لږ تر لږه پنځه جملې ولیکئ.')
e.p("7. Giving your opinion on the given essay, tell to what extent the author has impressed readers by describing Socrates' personality and achievements.", '۷۔ دیے گئے مضمون پر اپنی رائے کا اظہار کرتے ہوئے بتائیے کہ مصنف نے کس حد تک سقراط کی شخصیت اور کارہائے نمایاں کا ذکر کرتے ہوئے قارئین کو متاثر کیا ہے؟', '۷. پر ورکړل شوې مقالې خپل نظر څرګند کړئ او ووایئ چې لیکوال د سقراط د شخصیت او ښکاره کارنامو په یادولو تر کومه حده لوستونکي اغېزمن کړي؟')
ex = BOOK.record(e, 'urdu12-u2-exercise-2', 'Exercise (2): blanks, summary, diacritics, essay; punctuation — inverted commas, question mark, exclamation mark', 'مشق (۲): خالی جگہ، خلاصہ، اعراب، مضمون؛ رموزِ اوقاف — واوین، سوالیہ، ندائیہ', 'تمرین (۲): تش ځایونه، لنډیز، اعراب، مقاله؛ رموزِ اوقاف — واوین، سوالیه، ندائیه', 12, [14, 15])
ex['sourceCoverIllustrationReview'] = 'Engraved portrait of Socrates with the caption “سُقراط” (p.15) is a decorative illustration; not reproduced.'
issues = [{'id': 'urdu12-pdf012', 'unit': 2, 'printedPage': 14, 'description': 'Punctuation notes printed in shaded boxes. P.15 carries only Q7 and a portrait of Socrates (caption “سُقراط”).'}]

if __name__ == '__main__':
    BOOK.save(12, [(2, ex)], issues=issues, complete_units=[2])
