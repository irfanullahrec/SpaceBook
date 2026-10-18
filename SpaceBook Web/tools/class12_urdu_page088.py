"""Urdu XII PDF88 (spread): printed pp.166–167 — Lesson 16 مشق Q1–Q9."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '۱۔ درج ذیل سوالات کے جوابات لکھیں۔', '۱. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) What comments did people make about the leader not going to his own village (Muridpur)?', '(الف) لیڈر کے اپنے گاؤں (مرید پور) نہ جانے پر لوگ کیا تبصرے کرتے تھے؟', '(الف) د مشر خپل کلي (مریدپور) ته د نه تګ په اړه خلکو کومې تبصرې کولې؟'),
    ('(b) How did the nephew get his uncle declared the “national leader” of Muridpur?', '(ب) بھتیجے نے اپنے چچا کو کس طرح مرید پور کا ’’قومی لیڈر‘‘ قرار دلوایا؟', '(ب) وراره خپل تره څنګه د مریدپور "ملي مشر" وګرځاوه؟'),
    ('(c) What points did the leader collect for his speech?', '(ج) لیڈر نے اپنی تقریر کے لیے کون سے نکات اکٹھے کیے؟', '(ج) مشر د خپلې وینا لپاره کوم ټکي راټول کړل؟'),
    ('(d) How was the leader received in Muridpur?', '(د) مرید پور میں لیڈر کا استقبال کس طرح ہوا؟', '(د) په مریدپور کې د مشر هرکلی څنګه وشو؟'),
    ("(e) What was the reason for the leader's panic during the meeting?", '(ہ) جلسے کے دوران لیڈر کے بدحواس ہونے کی کیا وجہ تھی؟', '(ه) د غونډې پر مهال د مشر د وارخطايۍ لامل څه و؟'),
    ('(f) What became of the leader during the speech?', '(و) تقریر کے دوران لیڈر کا کیا حشر ہوا؟', '(و) د وینا پر مهال د مشر څه حال شو؟'),
])
e.p('2. Fill in the blanks with suitable words.', '۲۔ خالی جگہ مناسب الفاظ سے پُر کریں۔', '۲. تش ځایونه په مناسبو کلمو ډک کړئ.')
e.group('lines', [
    ('(a) May God give all you readers the ________ of fairness.', '(الف) خُدا آپ سب پڑھنے والوں کو انصاف کی ________ دے۔', '(الف) خدای دې تاسو ټولو لوستونکو ته د انصاف ________ درکړي.'),
    ('(b) Reading the letter, my ________ knew no bounds.', '(ب) خط پڑھ کر میری ________ کی انتہا نہ رہی۔', '(ب) لیک مې چې ولوست، زما ________ پای نه درلود.'),
    ('(c) The ________ of leadership rises in a single moment.', '(ج) لیڈری کا ________ ایک لمحے میں ہی چڑھ جاتا ہے۔', '(ج) د مشرۍ ________ په یوه شېبه کې خېژي.'),
    ('(d) The cloud of ________ is gathering over the head.', '(د) گھٹا سر پہ ________ کی چھا رہی ہے۔', '(د) د ________ ورېځ پر سر خوره ده.'),
    ('(e) The world was becoming ________ before my eyes.', '(ہ) دنیا میری آنکھوں کے سامنے ________ ہو رہی تھی۔', '(ه) نړۍ زما د سترګو مخې ته ________ کېده.'),
])
e.p('3. Write a summary of this essay in your own words.', '۳۔ اس مضمون کا خلاصہ اپنے الفاظ میں لکھیں۔', '۳. د دې مقالې لنډیز په خپلو کلمو ولیکئ.')
e.p('4. Find and write at least five relative (waṣlī) sentences from this essay.', '۴۔ اس مضمون سے کم از کم پانچ وصلی جملے تلاش کر کے لکھیں۔', '۴. له دې مقالې لږ تر لږه پنځه وصلي (اړیکې) جملې ومومئ او ولیکئ.')
e.p('5. Find and write at least five sentences from this essay that contain auxiliary verbs.', '۵۔ اس مضمون سے کم از کم پانچ ایسے جملے تلاش کر کے لکھیں جن میں امدادی افعال ہوں۔', '۵. له دې مقالې لږ تر لږه پنځه داسې جملې ومومئ او ولیکئ چې مرستندوی فعلونه ولري.')
e.p('6. Put diacritics on the following words according to their meanings.', '۶۔ درج ذیل الفاظ پر اُن کے معنی کے مطابق اعراب لگائیں۔', '۶. پر لاندې کلمو د هغو د ماناوو سره سم اعراب کېږدئ.')
H = (['Word', 'Meaning (1)', 'Meaning (2)'], ['لفظ', 'معنی (۱)', 'معنی (۲)'], ['کلمه', 'مانا (۱)', 'مانا (۲)'])
ur = [['جل', 'پانی', 'دھوکا'], ['دور', 'زمانہ', 'فاصلہ'], ['قسم', 'عہد، ارادہ', 'طرح، طرز'], ['گل', 'مٹی', 'پھول'], ['منت', 'التجا', 'نیت، عہد'], ['نفس', 'سانس', 'روح، وجود'], ['ملکہ', 'صلاحیت', 'بادشاہ کی بیوی']]
en = [['jl (جل)', 'jal — water', 'jul — deception'], ['dwr (دور)', 'daur — era, period', 'dūr — distance, far'], ['qsm (قسم)', 'qasam — oath, resolve', 'qism — kind, type'], ['gl (گل)', 'gil — clay, earth', 'gul — flower'], ['mnt (منت)', 'minnat — entreaty', 'mannat — vow, intention'], ['nfs (نفس)', 'nafas — breath', 'nafs — soul, self'], ['mlkh (ملکہ)', 'malaka — skill, aptitude', 'malika — queen']]
ps = [['جل', 'اوبه', 'دوکه'], ['دور', 'زمانه', 'واټن'], ['قسم', 'لوړه، اراده', 'ډول، طرز'], ['ګل', 'خاوره', 'ګل'], ['منت', 'زارۍ', 'نیت، ژمنه'], ['نفس', 'ساه', 'روح، وجود'], ['ملکه', 'وړتیا', 'د پاچا ښځه']]
e.table('urdu12-u16-iraab', H[0], en, H[1], H[2], ur, ps)
e.p('7. Write a report (rūdād) of some function or meeting.', '۷۔ کسی تقریب یا جلسے کی روداد لکھیں۔', '۷. د کومې مراسمې یا غونډې راپور ولیکئ.')
e.p('8. Write at least five sentences from this essay in which “ke” is used.', '۸۔ اس مضمون سے کم از کم پانچ ایسے جملے لکھیں جن میں ’’کہ‘‘ کا استعمال ہو۔', '۸. له دې مقالې لږ تر لږه پنځه داسې جملې ولیکئ چې پکې "که" (چې) کارول شوی وي.')
e.p('9. Below, various sentences are written according to the sense of the text. Write “correct” or “incorrect” in front of them.', '۹۔ ذیل میں متن کے مفہوم کے مطابق مختلف جملے لکھے گئے ہیں۔ آپ ان کے سامنے ’’درست‘‘ یا ’’غلط‘‘ لکھیں۔', '۹. لاندې د متن د مفهوم سره سم بېلابېلې جملې لیکل شوې. د هغو مخې ته "سمه" یا "ناسمه" ولیکئ.')
e.group('lines', [
    ('(a) I had become suspect because of not going to my homeland.', 'ا۔ میں اپنے وطن میں نہ جانے کی وجہ سے مشکوک ہو گیا تھا۔', '(الف) زه خپل وطن ته د نه تګ له امله مشکوک شوی وم.'),
    ('(b) I used to attend Congress meetings with keen enthusiasm.', 'ب۔ میں کانگریس کے جلسوں میں ذوق و شوق سے شریک ہوتا تھا۔', '(ب) زه به د کانګرس په غونډو کې په ډېره مینه ګډون کاوه.'),
    ('(c) My nephew published all the letters.', 'ج۔ میرے بھتیجے نے تمام خطوط نشر کر دیے۔', '(ج) زما وراره ټول لیکونه خپاره کړل.'),
    ('(d) The author was a resident of Muridpur.', 'د۔ مصنف مرید پور کا رہنے والا تھا۔', '(د) لیکوال د مریدپور اوسېدونکی و.'),
    ('(e) The people of Muridpur had begun to envy the author.', 'ہ۔ مرید پور کے لوگ مصنف سے حسد کرنے لگے تھے۔', '(ه) د مریدپور خلکو له لیکوال سره کینه پیل کړې وه.'),
    ('(f) Only united nations attain the height of glory.', 'و۔ متحد قومیں ہی بامِ عروج حاصل کرتی ہیں۔', '(و) یوازې متحد قومونه د عروج لوړې ته رسېږي.'),
    ('(g) Hindus and Muslims are two separate nations.', 'ز۔ ہندو اور مسلمان دو الگ الگ قومیں ہیں۔', '(ز) هندوان او مسلمانان دوه بېل بېل قومونه دي.'),
    ('(h) The president of the meeting gave a warm welcome.', 'ح۔ صدرِ جلسہ نے پرتپاک استقبال کیا۔', '(ح) د غونډې رئیس ګرم هرکلی وکړ.'),
    ('(i) The author gave an extremely effective speech.', 'ط۔ مصنف نے انتہائی مؤثر تقریر کی۔', '(ط) لیکوال ډېره اغېزمنه وینا وکړه.'),
    ('(j) When the author finished the speech, people began to praise him.', 'ی۔ مصنف نے تقریر ختم کی تو لوگوں نے تعریف شروع کر دی۔', '(ی) کله چې لیکوال وینا پای ته ورسوله، خلکو ستاینه پیل کړه.'),
])
ex = BOOK.record(e, 'urdu12-u16-exercise', 'Exercise', 'مشق', 'تمرین', 88, [166, 167])
issues = [{'id': 'urdu12-pdf088', 'unit': 16, 'printedPage': 166, 'description': 'Q1(a) calls Muridpur the leader’s “village” (گاؤں) though the text calls it a city/homeland — retained as printed. Faint background drawing behind the exercise is decorative.'}]

if __name__ == '__main__':
    BOOK.save(88, [(16, ex)], issues=issues)
