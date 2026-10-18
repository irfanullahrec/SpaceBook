"""Pak Studies XII PDF72 (spread): p.133 Ch.6 women in the economy (end); p.134 مشق Q1–Q3."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
t.p('Thus we see that women, in the form of doctors, engineers, professors, lawyers, government officers, fashion designers, bankers and investors, are rendering commendable services in the economic system of the country. This is praiseworthy, because women are half of the national population. No country can progress by paralysing half of its population. Therefore for a better future of the country it is extremely necessary that women be encouraged to take part in economic activities; in this lie the betterment and survival of the country.',
    'لہٰذا ہم دیکھتے ہیں کہ خواتین ڈاکٹرز، انجینئرز، پروفیسر، وکلاء، سرکاری آفیسر، فیشن ڈیزائنر، بینکر اور سرمایہ کاروں کی شکل میں ملک کے معاشی نظام میں قابلِ قدر خدمات انجام دے رہی ہیں۔ یہ بات قابلِ تحسین ہے کیونکہ خواتین ملکی آبادی کا نصف حصہ ہیں۔ کوئی بھی ملک آبادی کا نصف حصہ مفلوج کر کے ترقی حاصل نہیں کر سکتا۔ لہٰذا ملک کے بہتر مستقبل کے لیے یہ انتہائی ضروری ہے کہ معاشی سرگرمیوں میں حصہ لینے پر خواتین کی حوصلہ افزائی کی جائے اسی میں ملک کی بہتری اور بقاء ہے۔',
    'نو ګورو چې ښځې د ډاکټرانو، انجنیرانو، پروفیسورانو، وکیلانو، دولتي افسرانو، فېشن ډیزاینرانو، بانکوالو او پانګوالو په بڼه د هېواد په اقتصادي نظام کې د قدر وړ خدمتونه ترسره کوي. دا د ستاینې وړ ده، ځکه ښځې د هېواد د نفوس نیمایي برخه دي. هېڅ هېواد د خپل نفوس نیمه برخه شل کولو سره پرمختګ نه شي کولی. نو د هېواد د ښه راتلونکي لپاره ډېره اړینه ده چې په اقتصادي فعالیتونو کې د ګډون لپاره د ښځو هڅونه وشي؛ د هېواد ښېګڼه او بقا په همدې کې ده.')
rec = BOOK.record(t, 'pak12-ch6-text-10', 'Chapter 6 text (10)', 'بابِ ششم — متن (۱۰)', 'شپږم څپرکی — متن (۱۰)', 72, [133])

e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks with appropriate words.', '1۔ خالی جگہوں کو موزوں الفاظ سے پُر کریں۔', '۱. تش ځایونه په مناسبو کلمو ډک کړئ.')
L([('i. The land of Pakistan has been the ________ of ancient cultures and civilisations.', 'i۔ پاکستان کی سرزمین قدیم ثقافتوں اور تہذیبوں کا ________ رہی ہے۔', 'i. د پاکستان ځمکه د لرغونو کلتورونو او تمدنونو ________ پاتې شوې.'),
   ('ii. The first capital of Gandhara civilisation is ________ .', 'ii۔ گندھارا تہذیب کا پہلا دارالخلافہ ________ ہے۔', 'ii. د ګندهارا تمدن لومړۍ پلازمېنه ________ ده.'),
   ('iii. In the Gandhara period Peshawar was called ________ .', 'iii۔ گندھارا دور میں پشاور کو ________ کہتے تھے۔', 'iii. د ګندهارا په دوره کې پېښور ته ________ ویل کېده.'),
   ('iv. The most basic thing in culture is ________ .', 'iv۔ ثقافت میں سب سے بنیادی چیز ________ ہے۔', 'iv. په کلتور کې تر ټولو بنسټیز شی ________ دی.'),
   ('v. The cultural centre of Gandhara is ________ .', 'v۔ گندھارا کا ثقافتی مرکز ________ ہے۔', 'v. د ګندهارا کلتوري مرکز ________ دی.')])
e.p('2. Choose the correct words from the words given in brackets.', '2۔ بریکٹ میں دیے گئے الفاظ میں سے درست الفاظ کا انتخاب کریں۔', '۲. په قوسونو کې له ورکړل شویو کلمو سمې کلمې وټاکئ.')
L([('i. Which Chinese traveller visited Gandhara at the beginning of the seventh century CE? (Chiang Zemin, Ho Chi Minh, Hiuen Tsang)', 'i۔ ساتویں صدی عیسوی کی ابتداء میں کون سے چینی سیاح نے گندھارا کا دورہ کیا؟ (چیانگ زے چن، ہو چی من، ہیون سانگ)', 'i. د اوومې زېږدیزې پېړۍ په پیل کې کوم چیني سیلاني له ګندهارا لیدنه وکړه؟ (چیانګ زې چن، هو چي من، هیون سانګ)'),
   ('ii. The name of the famous religious book of the Hindus is — (Rig Veda, Granth, Mala)', 'ii۔ ہندوؤں کی مشہور مذہبی کتاب کا نام ہے۔ (رگ وید، گرنتھ، مالا)', 'ii. د هندوانو د مشهور مذهبي کتاب نوم دی — (رګ وېد، ګرنت، مالا)'),
   ('iii. Gandhara was part of which empire? (Iranian, Afghan, Indian)', 'iii۔ گندھارا کون سی سلطنت کا حصہ تھا؟ (ایرانی، افغانی، ہندوستانی)', 'iii. ګندهارا د کومې سلطنت برخه وه؟ (ایراني، افغاني، هندوستاني)'),
   ('iv. Which Muslim woman did Hazrat Umar (RA) appoint Price Control Officer in his period of government? (Asma bint Abu Bakr (RA), Umm Salamah (RA), Shifa bint Abdullah (RA))', 'iv۔ حضرت عمرؓ نے اپنے دورِ حکومت میں کس مسلمان خاتون کو پرائس کنٹرول آفیسر مقرر کیا تھا؟ (اسماء بنت ابوبکرؓ، امِ سلمیٰؓ، شفہ بنت عبداللہؓ)', 'iv. حضرت عمر (رض) په خپله واکمنۍ کې کومه مسلمانه ښځه د بیو د کنټرول افسره ټاکلې وه؟ (اسماء بنت ابوبکر (رض)، ام سلمی (رض)، شفاء بنت عبدالله (رض))')])
e.p('3. Identify the correct and incorrect among the following.', '3۔ مندرجہ ذیل میں صحیح اور غلط کی نشاندہی کریں۔', '۳. په لاندې کې سمې او ناسمې په نښه کړئ.')
L([('i. In the time of the Holy Prophet (peace and blessings of Allah be upon him, his family and companions) women also acquired worldly education.', 'i۔ حضور صلی اللہ علیہ وعلیٰ آلہ واصحابہ وسلم کے دور میں خواتین دُنیاوی تعلیم بھی حاصل کرتی تھیں۔', 'i. د رسول الله (صلی الله علیه وعلی آله واصحابه وسلم) په دوره کې ښځو دنیوي زده‌کړه هم کوله.'),
   ('ii. The cultural centre of Gandhara was Charsadda.', 'ii۔ گندھارا کا ثقافتی مرکز چارسدہ تھا۔', 'ii. د ګندهارا کلتوري مرکز چارسده و.'),
   ('iii. The influences of Iranian culture on Baloch culture are very great.', 'iii۔ بلوچی ثقافت پر ایرانی ثقافت کے اثرات بہت زیادہ ہیں۔', 'iii. پر بلوڅ کلتور د ایراني کلتور اغېزې ډېرې دي.'),
   ('iv. Moenjodaro was the centre of Baloch culture.', 'iv۔ موہنجوداڑو بلوچی ثقافت کا مرکز تھا۔', 'iv. موهنجوداړو د بلوڅ کلتور مرکز و.'),
   ('v. There are Greek influences on the art of sculpture of Gandhara.', 'v۔ گندھارا کے مجسمہ سازی کے فن پر یونانی اثرات ہیں۔', 'v. د ګندهارا د مجسمه جوړونې پر هنر یوناني اغېزې دي.')])
ex = BOOK.record(e, 'pak12-ch6-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 72, [134])
issues = [{'id': 'pak12-pdf072', 'unit': 6, 'printedPage': 134,
           'description': 'Q2(i) option “چیانگ زے چن” is printed for Jiang Zemin; Q2(iv) prints “امِ سلمیٰ” (for Umm Salamah) and “شفہ”; retained as printed. Faint show-through on p.133 is not content.'}]

if __name__ == '__main__':
    BOOK.save(72, [(6, rec), (6, ex)], issues=issues)
