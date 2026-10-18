"""PDF5–6: Acknowledgment; Table of Contents (units 1–19 with theme, outcomes and printed page)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
a = Builder()
a.h('Acknowledgment', 'اظہارِ تشکر', 'منندوینه')
a.p("Developing a textbook under the touchstone of a prescribed curriculum is harder than writing at free will. This becomes specifically laborious when one is to organise and arrange material according to the SLOs, Standards and Benchmarks. We have endeavoured to the best of our level to develop a textbook that will, hopefully satiate the needs of the students in the light of the National Education curriculum. We are grateful to those writers, websites and authentic sources whose copyright materials have been freely utilised in the compilation of this textbook. Our thanks are due to Mr Waheed ullah Khan( Subject Specialist English, KP Textbook board) whose technical advice helped us in cognitively arranging exercises relating to formal and lexical aspect of language and for identifying certain literary content and non-fictional material as per the demands of the Curriculum.",
    'کسی مقررہ نصاب کی کسوٹی پر درسی کتاب تیار کرنا آزادانہ لکھنے سے زیادہ مشکل ہے۔ یہ کام اس وقت خاص طور پر محنت طلب ہو جاتا ہے جب مواد کو طلبہ کے تعلیمی نتائج (SLOs)، معیارات اور سنگِ میل کے مطابق منظم اور ترتیب دینا ہو۔ ہم نے اپنی بہترین سطح تک کوشش کی ہے کہ ایسی درسی کتاب تیار کریں جو امید ہے قومی تعلیمی نصاب کی روشنی میں طلبہ کی ضروریات پوری کرے گی۔ ہم ان مصنفین، ویب سائٹس اور مستند ذرائع کے شکر گزار ہیں جن کا کاپی رائٹ مواد اس درسی کتاب کی تدوین میں آزادانہ استعمال کیا گیا ہے۔ ہم جناب وحید اللہ خان (سبجیکٹ اسپیشلسٹ انگریزی، کے پی ٹیکسٹ بک بورڈ) کے شکر گزار ہیں جن کے تکنیکی مشورے نے زبان کے صوری اور لغوی پہلو سے متعلق مشقوں کو ذہنی طور پر ترتیب دینے اور نصاب کے تقاضوں کے مطابق بعض ادبی مواد اور غیر افسانوی مواد کی نشاندہی میں ہماری مدد کی۔',
    'د یوه ټاکلي نصاب پر محک درسي کتاب جوړول له ازادې لیکنې ډېر ستونزمن دي. دا کار په ځانګړي ډول هغه وخت ستړی کوونکی کېږي چې منځپانګه د زده کوونکو د زده کړې پایلو (SLOs)، معیارونو او بنسټیزو نښو سره سم تنظیم او ترتیب شي. موږ د خپلې وسې تر وروستۍ کچې هڅه کړې چې داسې درسي کتاب جوړ کړو چې هیله ده د ملي تعلیمي نصاب په رڼا کې د زده کوونکو اړتیاوې پوره کړي. موږ د هغو لیکوالو، ویب پاڼو او معتبرو سرچینو مننه کوو چې د کاپي رایټ منځپانګه یې د دې درسي کتاب په ترتیب کې په ازاده توګه کارول شوې. زموږ مننه ښاغلي وحیدالله خان (د انګلیسي د مضمون متخصص، د خیبر پښتونخوا د درسي کتابونو بورډ) ته ده چې تخنیکي مشورو یې د ژبې له رسمي او لغوي اړخ سره د تړلو تمرینونو په ذهني ترتیب کې او د نصاب د غوښتنو سره سم د ځینو ادبي منځپانګو او غیر داستاني موادو په پېژندلو کې زموږ مرسته وکړه.')
a.p('Jaffar Ali Khan, Ali Akbar', 'جعفر علی خان، علی اکبر', 'جعفر علي خان، علي اکبر')
ack = BOOK.record(a, 'eng12-acknowledgment', 'Acknowledgment', 'اظہارِ تشکر', 'منندوینه', 5, [])

OUT = ('Reading, Writing, Oral Communication, Vocabulary and Grammar', 'پڑھنا، لکھنا، زبانی ابلاغ، ذخیرۂ الفاظ اور قواعد', 'لوستل، لیکل، د خولې اړیکه، لغات او ګرامر')
U = [
    ('1', ('Seerat-e-Tayyiba and the Muslim Youth', 'سیرتِ طیبہ اور مسلم نوجوان', 'سیرت طیبه او مسلمان ځوانان'), ('Character building', 'کردار سازی', 'د شخصیت جوړونه'), '1'),
    ('2', ('Jinnah’s Vision of Pakistan', 'پاکستان کے بارے میں جناح کا تصور', 'د پاکستان په اړه د جناح لید'), ('Tolerance, humanism, equality between groups and nation', 'رواداری، انسان دوستی، گروہوں اور قوم کے درمیان مساوات', 'زغم، انسان‌پالنه، د ډلو او ملت ترمنځ برابري'), '16'),
    ('3', ('Solitary Reaper (Poem)', 'تنہا فصل کاٹنے والی (نظم)', 'یوازینۍ لوګړه (شعر)'), ('Appreciation and preservation of nature', 'فطرت کی قدر دانی اور تحفظ', 'د طبیعت ستاینه او ساتنه'), '26'),
    ('4', ('Truck Art', 'ٹرک آرٹ', 'د ټرک هنر'), ('Respect for all professions. (Valuing disparity and equality among professions)', 'تمام پیشوں کا احترام۔ (پیشوں میں فرق اور مساوات کی قدر)', 'د ټولو مسلکونو درناوی. (د مسلکونو ترمنځ د توپیر او برابرۍ ارزښت)'), '32'),
    ('5', ('The Last Leaf', 'آخری پتا', 'وروستۍ پاڼه'), ('Humanism', 'انسان دوستی', 'انسان‌پالنه'), '42'),
    ('6', ('If (Poem)', 'اگر (نظم)', 'که (شعر)'), ('Character building', 'کردار سازی', 'د شخصیت جوړونه'), '53'),
    ('7', ('Hubble', 'ہبل', 'هبل'), ('Technology and society of future', 'ٹیکنالوجی اور مستقبل کا معاشرہ', 'ټکنالوژي او د راتلونکې ټولنه'), '61'),
    ('8', ('Lesson from the Battle of Uhud', 'غزوۂ احد سے سبق', 'د احد له غزا څخه لوست'), ('Duties and Responsibilities', 'فرائض اور ذمہ داریاں', 'دندې او مسؤلیتونه'), '77'),
    ('9', ('The Toys (Poem)', 'کھلونے (نظم)', 'لوبونې (شعر)'), ('Mercy/compassion/forgiveness/divine love', 'رحم/ہمدردی/معافی/الٰہی محبت', 'رحم/خواخوږي/بښنه/الهي مینه'), '85'),
    ('10', ('Gender Inequality and its Implications', 'صنفی عدم مساوات اور اس کے اثرات', 'جنسیتي نابرابري او د هغې پایلې'), ('Gender inequality is detrimental to society', 'صنفی عدم مساوات معاشرے کے لیے نقصان دہ ہے', 'جنسیتي نابرابري ټولنې ته زیانمنه ده'), '92'),
    ('11', ('Jahangir Khan The Conqueror', 'جہانگیر خان — فاتح', 'جهانګیر خان — فاتح'), ('Rise of Nations through National Pride', 'قومی فخر کے ذریعے قوموں کا عروج', 'د ملي ویاړ له لارې د ملتونو عروج'), '101'),
    ('12', ('All the World’s a Stage (Poem)', 'ساری دنیا ایک اسٹیج ہے (نظم)', 'ټوله نړۍ یوه سټېج ده (شعر)'), ('Transiency', 'ناپائیداری', 'ناپایښت'), '110'),
    ('13', ('Technical Education', 'فنی تعلیم', 'تخنیکي زده کړه'), ('Life Skills Education', 'زندگی کی مہارتوں کی تعلیم', 'د ژوند د مهارتونو زده کړه'), '119'),
    ('14', ('Lingkuan Gorge', 'لنگ کوان گھاٹی', 'لینګ‌کوان دره'), ('Duty and Responsibility', 'فرض اور ذمہ داری', 'دنده او مسؤلیت'), '130'),
    ('15', ('Once Upon a Time (Poem)', 'ایک زمانے میں (نظم)', 'یو وخت و (شعر)'), ('Practicing adaptability/ Social etiquettes', 'موافقت پذیری پر عمل/ سماجی آداب', 'د سمون وړتیا تمرین/ ټولنیز اداب'), '140'),
    ('16', ('Tourist Attractions in Pakistan', 'پاکستان میں سیاحتی کشش کے مقامات', 'په پاکستان کې د ګرځندوی د زړه‌راښکونکو ځایونه'), ('Tourism, Its Impact on Society', 'سیاحت، معاشرے پر اس کے اثرات', 'ګرځندوی، پر ټولنه یې اغېزې'), '150'),
    ('17', ('Désirée’s Baby', 'دیزیرے کا بچہ', 'د ډېزیرې ماشوم'), ('Equality/Fraternity/ Humanism', 'مساوات/بھائی چارہ/ انسان دوستی', 'برابري/ورورولي/ انسان‌پالنه'), '162'),
    ('18', ('Lines from the Deserted Village (Poem)', 'ویران گاؤں سے اشعار (نظم)', 'له وران کلي څخه بیتونه (شعر)'), ('Love of nature/ preservation of nature', 'فطرت سے محبت/ فطرت کا تحفظ', 'له طبیعت سره مینه/ د طبیعت ساتنه'), '176'),
    ('19', ('Lord of the Flies', 'لارڈ آف دی فلائیز', 'د مچانو بادار'), ('Civilization and Savagery', 'تہذیب اور وحشت', 'تمدن او وحشت'), '184'),
]
t = Builder()
t.h('Table of Contents', 'فہرستِ مضامین', 'د منځپانګې لړلیک')
rows = {i: [[n, ti[i], th[i], OUT[i], pg] for n, ti, th, pg in U] for i in range(3)}
t.table('eng12-toc', ['No', 'Title', 'Theme', 'Outcomes', 'Page'], rows[0], ['نمبر', 'عنوان', 'موضوع', 'نتائج', 'صفحہ'], ['شمېره', 'سرلیک', 'موضوع', 'پایلې', 'مخ'], rows[1], rows[2])
toc = BOOK.record(t, 'eng12-toc', 'Table of Contents', 'فہرستِ مضامین', 'د منځپانګې لړلیک', 5, [])
toc['sourceReferences'].append({'sourcePdf': BOOK.c['source'], 'pdfPage': 6, 'printedPages': []})
issues = [{'id': 'eng12-p5-ack-spacing', 'unit': 'FM', 'printedPage': None, 'description': 'Acknowledgment prints “Mr Waheed ullah Khan( Subject Specialist English, KP Textbook board)” with irregular spacing/capitalisation; Table of Contents lists unit 3 as “Solitary Reaper (Poem)” and unit 7 as “Hubble”. Printed wording retained.'}]

if __name__ == '__main__':
    BOOK.save(5, [('FM', ack), ('FM', toc)], issues=issues)
