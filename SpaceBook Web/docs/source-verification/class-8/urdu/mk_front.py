import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages'))
def w(n, s): io.open(f"p{n:03d}.txt", "w", encoding="utf-8").write(s)

w(0, """@status front-matter
@deco Front cover: green and cream cover with the title "اُردو", a green badge "۸ جماعت ہشتم", "یکساں قومی نصاب ۲۰۲۲ء کے مطابق", "ٹیسٹ ایڈیشن", a boy at a wooden lectern and a girl in a pink scarf at a yellow lectern on a stage; a "Free From Government — NOT FOR SALE" sticker; the KPTBB crest and "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور". The website watermark lines at the top and bottom are not book content.
# اُردو — جماعت ہشتم || Urdu — Class 8 || اردو — اتم ټولګی
p یکساں قومی نصاب ۲۰۲۲ء کے مطابق || According to the Single National Curriculum 2022 || د ۲۰۲۲ یو شان ملي نصاب سره سم
p ٹیسٹ ایڈیشن || Test edition || ازمایښتي چاپ
p خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور || Khyber Pakhtunkhwa Textbook Board, Peshawar || د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور
""")
w(1, """@status blank
@deco An advertisement page of a free-download website (awazeinqilab.com) in yellow with a list of subjects; it is not part of the textbook.
@issue Advertisement page inserted in the scan set; not book content.
""")
w(2, """@status front-matter
@deco Title page: "اُردو" in green letters, "جماعت ہشتم", "یکساں قومی نصاب ۲۰۲۲ء کے مطابق", a NOT FOR SALE sticker, the KPTBB hexagonal crest and "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور".
# اُردو — جماعت ہشتم (سرورق) || Urdu — Class 8 (title page) || اردو — اتم ټولګی (سرپاڼه)
p اُردو جماعت ہشتم، یکساں قومی نصاب ۲۰۲۲ء کے مطابق، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || Urdu, Class 8, according to the Single National Curriculum 2022, Khyber Pakhtunkhwa Textbook Board, Peshawar. || اردو، اتم ټولګی، د ۲۰۲۲ یو شان ملي نصاب سره سم، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.
""")

rows1 = [(1,"حمد (نظم)",1),(2,"نعت (نظم)",6),(3,"خطبۂ حجۃ الوداع",11),(4,"آخری قدم",17),(5,"اشرفیوں کی تھیلی",23),("","جائزہ ۱",30),(6,"آلودگی",33),(7,"پنسلین کی کہانی",41),(8,"ایک مثالی طالب علم",48),(9,"کارگل کا ہیرو",56),(10,"یہ وطن تمھارا ہے (نظم)",64),("","جائزہ ۲",69),(11,"اول جلول اور کھچڑی",72),(12,"گرل گائیڈز",79),(13,"ہندسوں کا جادوگر — الخوارزمی",85)]
s = ("@status front-matter\n@issue Contents page (i). The two outer columns of the printed contents (میرے کرنے کے کام and بات سے نکلے بات) describe per-lesson activities: the first column is, for almost every lesson, الفاظ کے معانی سیکھنا، سوالات کے جوابات دینا، درست اور غلط جواب کی نشان دہی کرنا (variants: خالی جگہ پر کرنا for lessons 2, 5, 10, 15, 17; کالم ملانا for lessons 7 and 13); the second column lists speaking and listening tasks per lesson. They are summarized here, not transcribed line by line.\n"
     "## فہرست || Contents || منځپانګه\n"
     "table فہرست (صفحہ i) || Contents (page i) || منځپانګه (مخ i)\n"
     "th | سبق نمبر | اسباق | صفحہ نمبر\n")
for n, t, p in rows1: s += f"tr | {n} | {t} | {p}\n"
s += "endtable\n"
w(3, s)

gram = [
("لغت کا استعمال، مذکر مؤنث کا تصور، الفاظ کے جملے بنانا","مصرعے کا مفہوم لکھنا، اشعار کی تشریح لکھنا","چارٹ تیار کرنا، موضوع سے متعلق غور و فکر کرنا"),
("واحد جمع اور جمع الجمع کا تصور","نظم کی روشنی میں کسی موضوع پر مختصر نوٹ لکھنا، شعر کا مفہوم لکھنا، نظم کی تلخیص لکھنا","نظم زبانی یاد کرنا اور ترنم سے پڑھنا، ذرائع ابلاغ یا انٹرنیٹ سے نعت تلاش کر کے جماعت میں سنانا"),
("الفاظ متضاد کا تصور","موضوع سے متعلق تفصیل سے لکھنا، پیراگراف پڑھنا اور درست املا لکھنا","چارٹ تیار کرنا، کتب بینی کی عادت ڈالنا"),
("متشابہ الفاظ کا تصور","سبق کا عنوان تجویز کرنا، اشاروں کی مدد سے کہانی لکھنا","اضافی مطالعہ کرنا، فلاحی کاموں میں حصہ لینا"),
("حروفِ فجائیہ کا تصور، الفاظ کے جملے بنانا","سبق کا مرکزی خیال لکھنا، سبق کے کسی حصے کو اپنے الفاظ میں لکھنا، اقتباس پڑھ کر خیالی کہانی لکھنا","پسندیدہ کہانی دوستوں کو سنانا، اخبار یا میگزین سے اخلاقی کہانی تلاش کرنا، پہیلیاں بوجھنا"),
("تلمیح کا تصور، الفاظ متضاد کو جملوں میں استعمال کرنا","موضوع سے متعلق تفصیلی تبصرہ لکھنا، آلودگی سے محفوظ رہنے کی تدابیر لکھنا","اسکول میں ہفتہ صفائی منانا، اپنے نام کا پودا لگانا، آلودگی سے متعلق دوسروں کو آگاہی دینا"),
("جملوں میں تکرارِ لفظی کی غلطی کا تصور، متشابہ الفاظ کی پہچان اور استعمال","موضوع سے متعلق مکالمہ لکھنا، سبق کے کسی حصے کو اپنے الفاظ میں لکھنا","سبق سے متعلق اضافی معلومات اکٹھی کرنا، ایجادات سے پہلے کی دنیا کا تصوراتی خاکہ بیان کرنا"),
("فاعل کے لحاظ سے فعل کی اقسام کا تصور","سبق کے کسی حصے سے متعلق پیراگراف لکھنا، دوست کے نام خط لکھنا","موضوع سے متعلق مباحثہ منعقد کرنا، اپنی ذات میں تبدیلی لانے کے لیے اچھی عادتیں اپنانا"),
("اسمِ صفت کی اقسام کا تصور","سبق کے مرکزی کردار کے بارے میں لکھنا، کسی عنوان پر مضمون لکھنا","کسی مقام کے بارے میں اضافی معلومات جمع کرنا، اضافی مطالعہ کی عادت ڈالنا، مکالمہ تیار کرنا"),
("گروہی یا متلازم الفاظ کا تصور","مصرعے میں چھپے پیغام سے متعلق لکھنا، نظم کے بند کی تشریح لکھنا، موضوع سے متعلق تقریر تیار کرنا","نظم کا پیغام سمجھنا، چارٹ تیار کرنا، اضافی مطالعہ کے لیے کوئی کتاب حاصل کر کے پڑھنا"),
("حروفِ علت اور حروفِ تاکید کا تصور، محاوروں کو جملوں میں استعمال کرنا","کہانی کا خلاصہ لکھنا، کہانی کے کردار سے متعلق اپنے الفاظ میں لکھنا","اپنی پسند کی اخلاقی کہانی پڑھنا، سبق کے مصنف کی دیگر تصانیف کے بارے میں جاننا"),
("تذکیر و تانیث کے اصول جاننا، الفاظ کو جملوں میں استعمال کر کے ان کی تذکیر و تانیث واضح کرنا","اشاروں کی مدد سے مکالمہ لکھنا، موضوع سے متعلق نوٹ لکھنا","چارٹ تیار کرنا، کسی موضوع سے متعلق ذرائع ابلاغ اور انٹرنیٹ سے معلومات جمع کرنا"),
("الفاظ متضاد کا تصور","دیے گئے موضوع پر ۳۰۰ الفاظ پر مشتمل مضمون لکھنا، موضوع سے متعلق ایک پیراگراف لکھنا","چارٹ تیار کرنا، انٹرنیٹ یا رسائل کی مدد سے تصویر حاصل کر کے کاپی میں لگانا"),
]
s = ("@status front-matter\n@issue Contents page (ii): the grammar (قواعد سیکھیں), writing (کچھ نیا لکھیں) and activity (ہمارے کرنے کے کام) columns per lesson. The lesson-number column is cut off in the scan; the rows follow the lessons of pages i and iii in order (the blue bands are the review sections), so the rows are listed here in printed order. The rows are read from a slightly curved page; the second-last row prints the same grammar topic (الفاظ متضاد کا تصور) as row 3 and the last row prints الفاظ متضاد کا تصور as well.\n"
     "## قواعد، تحریر اور سرگرمیاں (فہرست ii) || Grammar, writing and activities (contents ii) || ګرامر، لیک او فعالیتونه (منځپانګه ii)\n"
     "table قواعد، تحریر، سرگرمیاں || Grammar, writing, activities || ګرامر، لیک، فعالیتونه\n"
     "th | قواعد سیکھیں | کچھ نیا لکھیں | ہمارے کرنے کے کام\n")
for a, b, c in gram: s += f"tr | {a} | {b} | {c}\n"
s += "endtable\n"
w(4, s)

rows3 = [(14,"قومی و ملی اتحاد",91),(15,"سارے حسیں نظارے میرے وطن کے اندر (نظم)",99),("","جائزہ ۳",103),(16,"خوبصورت پاکستان",106),(17,"تم تو ٹھہری ہو",114),(18,"پاکستان کی تہذیب و ثقافت",122),(19,"پرانا کوٹ (نظم)",128),(20,"ہاکی — ہمارا قومی کھیل",133),("","جائزہ ۴",139),(21,"شہری دفاع",142),(22,"ظفر علی خان",149),(23,"آدمی نامہ (نظم)",156),(24,"اقبال رحمۃ اللہ علیہ کا تصورِ خودی",162),(25,"یا رب دلِ مسلم کو (نظم)",167),("","جائزہ ۵",172),("","کلی جائزہ",176)]
s = ("@status front-matter\n@issue Contents page (iii): lessons 14–25, reviews 3–5 and the overall review (کلی جائزہ). The activity columns are summarized as on page i. The title of lesson 17 is read as printed in the contents (تم تو ٹھہری ہو) and is to be checked against the lesson page.\n"
     "## فہرست (جاری) || Contents (continued) || منځپانګه (دوام)\n"
     "table فہرست (صفحہ iii) || Contents (page iii) || منځپانګه (مخ iii)\n"
     "th | سبق نمبر | اسباق | صفحہ نمبر\n")
for n, t, p in rows3: s += f"tr | {n} | {t} | {p}\n"
s += "endtable\n"
w(5, s)
