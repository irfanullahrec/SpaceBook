"""PDF14 (printed 15–16): Unit 1 Activity B items 12–20, Teacher's Guideline (unit end); Unit 2 opener 'Jinnah's Vision of Pakistan' (outcomes)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
v = Builder()
v.group('lines', [
    (f'12. I wanted to her to become a member of the committee, but our boss {B} the proposal. (accept)', f'12. میں چاہتا تھا کہ وہ کمیٹی کی رکن بنے، لیکن ہمارے باس نے تجویز {B}۔ (accept — قبول کرنا)', f'12. ما غوښتل چې هغه د کمیټې غړې شي، خو زموږ مشر وړاندیز {B}. (accept — منل)'),
    (f'13. We only {B} our tickets a day before the concert took place. (send)', f'13. ہمیں کنسرٹ سے صرف ایک دن پہلے اپنے ٹکٹ {B}۔ (send — بھیجنا)', f'13. موږ خپل ټکټونه د کنسرټ یوازې یوه ورځ مخکې {B}. (send — لېږل)'),
    (f'14. Usman asked me if I could {B} him my iPad. (borrow)', f'14. عثمان نے مجھ سے پوچھا کہ کیا میں اسے اپنا آئی پیڈ {B} سکتا ہوں۔ (borrow — ادھار لینا)', f'14. عثمان له ما وپوښتل چې ایا زه هغه ته خپل ای‌پیډ {B} شم. (borrow — پور اخیستل)'),
    (f'15. My brother {B} me how to repair my bike. (learn)', f'15. میرے بھائی نے مجھے اپنی موٹر سائیکل ٹھیک کرنا {B}۔ (learn — سیکھنا)', f'15. زما ورور ماته د خپل موټرسایکل جوړول {B}. (learn — زده کول)'),
    (f'16. Smoking is {B} in public places. (allow)', f'16. عوامی مقامات پر تمباکو نوشی {B} ہے۔ (allow — اجازت دینا)', f'16. په عامه ځایونو کې سګرټ څکول {B} دي. (allow — اجازه ورکول)'),
    (f'17. He {B} his tie and took his jacket off. (tighten)', f'17. اس نے اپنی ٹائی {B} اور جیکٹ اتار دی۔ (tighten — کسنا)', f'17. هغه خپله نکټایي {B} او جاکټ یې وویست. (tighten — کلکول)'),
    (f"18. The soldiers weren't able to {B} the fortress. (attack)", f'18. سپاہی قلعے کا {B} نہ کر سکے۔ (attack — حملہ کرنا)', f'18. سرتېري ونه توانېدل چې له کلا {B}. (attack — برید کول)'),
    (f'19. A lot of bridges and motorways were {B} during the earthquake. (create)', f'19. زلزلے کے دوران بہت سے پل اور موٹر ویز {B} گئے۔ (create — بنانا)', f'19. د زلزلې پر مهال ډېر پلونه او لویې لارې {B} شوې. (create — جوړول)'),
    (f'20. The teacher {B} the pupils by giving them lines to write. (reward)', f'20. استاد نے شاگردوں کو لکھنے کے لیے سطریں دے کر {B}۔ (reward — انعام دینا)', f'20. ښوونکي زده کوونکي د لیکلو لپاره د کرښو په ورکولو {B}. (reward — انعام ورکول)'),
])
v.h("Teacher's Guideline", 'استاد کے لیے رہنمائی', 'ښوونکي ته لارښوونه')
v.p('The teacher should guide students to understand phonetic symbols and help them pronounce words from phonetic transcription and vice versa', 'استاد کو چاہیے کہ طلبہ کی صوتی علامات سمجھنے میں رہنمائی کرے اور صوتی نقل سے الفاظ ادا کرنے اور اس کے برعکس میں ان کی مدد کرے', 'ښوونکی باید زده کوونکو ته د غږیزو نښو په پوهېدو کې لارښوونه وکړي او د غږیز لیکدود څخه د کلمو په تلفظ او برعکس کې ورسره مرسته وکړي')
ex = BOOK.record(v, 'eng12-u01-activities-b', "Activity B (12–20); Teacher's Guideline", "سرگرمی B (12–20)؛ استاد کے لیے رہنمائی", "فعالیت B (12–20)؛ ښوونکي ته لارښوونه", 14, [15])

UT = ("Jinnah's Vision of Pakistan", 'پاکستان کے بارے میں جناح کا تصور', 'د پاکستان په اړه د جناح لید')
o = Builder()
o.h("Unit 2 — Jinnah's Vision of Pakistan", 'یونٹ 2 — پاکستان کے بارے میں جناح کا تصور', 'واحد 2 — د پاکستان په اړه د جناح لید')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Use pre-reading strategies to predict the content of a text from topic / picture, title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.', 'سابقہ علم، سوالات اور سیاقی اشاروں کو استعمال کرتے ہوئے موضوع / تصویر، عنوان / سرخیوں، کلیدی الفاظ اور بصری مواد وغیرہ سے متن کے مواد کی پیش گوئی کے لیے مطالعے سے پہلے کی حکمتِ عملیاں استعمال کریں۔', 'د مخکینۍ پوهې، پوښتنو او شرایطي نښو په کارولو د موضوع / انځور، سرلیک / سرټکو، کلیدي کلمو او لیدنیزو موادو څخه د متن د منځپانګې د وړاندوینې لپاره د لوستلو مخکې ستراتیژۍ وکاروي.'),
    ('Skim text to: have general idea of the text; infer theme/ main idea.', 'متن پر سرسری نظر ڈالیں تاکہ: متن کا عمومی اندازہ ہو؛ موضوع/ مرکزی خیال اخذ کریں۔', 'په متن سرسري نظر واچوي ترڅو: د متن عمومي مفکوره ولري؛ موضوع/ اصلي مفکوره استنباط کړي.'),
    ('Apply critical thinking to interact with text, use intensive reading strategies (while-reading) to scan to answer short questions', 'متن سے تعامل کے لیے تنقیدی سوچ کا اطلاق کریں، گہرے مطالعے کی حکمتِ عملیاں (دورانِ مطالعہ) استعمال کریں تاکہ مختصر سوالات کے جواب کے لیے متن میں تلاش کریں', 'له متن سره د تعامل لپاره انتقادي فکر پلي کړي، د ژورو لوستلو ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو د لنډو پوښتنو د ځوابولو لپاره متن ولټوي'),
    ('Use pronunciation key to pronounce words with developing accuracy.', 'بڑھتی ہوئی درستی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔', 'د زیاتېدونکي دقت سره د کلمو د تلفظ لپاره د تلفظ کیلي وکاروي.'),
    ('Deduce the meaning of unfamiliar words from the context using contextual clues.', 'سیاقی اشاروں کو استعمال کرتے ہوئے سیاق و سباق سے نامانوس الفاظ کے معنی اخذ کریں۔', 'د شرایطي نښو په کارولو له شرایطو څخه د ناپېژندل شویو کلمو مانا استنباط کړي.'),
    ('Illustrate use of regular and irregular verbs.', 'باقاعدہ اور بے قاعدہ افعال کے استعمال کی وضاحت کریں۔', 'د منظمو او غیرمنظمو فعلونو کارول وښيي.'),
    ('Write an introductory paragraph with a central idea and sporting details.', 'مرکزی خیال اور معاون تفصیلات کے ساتھ ایک تعارفی پیراگراف لکھیں۔', 'د یوه مرکزي نظر او ملاتړي جزییاتو سره یو پیلنی پراګراف ولیکي.'),
])
op = BOOK.record(o, 'eng12-u02-outcomes', 'Unit 2 — learning outcomes', 'یونٹ 2 — تعلیمی نتائج', 'واحد 2 — د زده کړې پایلې', 14, [16], unit_title=UT)
op['sourceCoverIllustrationReview'] = 'Portrait photograph of Quaid-e-Azam Muhammad Ali Jinnah on the opener page is decorative; not reproduced.'
issues = [{'id': 'eng12-p15-16-typos', 'unit': 1, 'printedPage': 15, 'description': 'Item 12 prints “I wanted to her to become…”; Unit 2 outcomes print “sporting details” (supporting details). Printed text retained.'}]

if __name__ == '__main__':
    BOOK.save(14, [(1, ex), (2, op)], issues=issues, complete_units=[1])
