"""Urdu XII PDF117 (spread): p.224 Ghazal 9 مشق Q2–Q5 + note on غزل; p.225 Ghazal 10 author note (فیض احمد فیض, 1910–1984)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.group('lines', [
    ('2. Write the rhymes (qawāfī) of this ghazal.', '۲۔ اس غزل کے قوافی لکھیں۔', '۲. د دې غزل قافیې ولیکئ.'),
    ('3. Read this couplet:', '۳۔ یہ شعر پڑھیں:', '۳. دا بیت ولولئ:'),
    ('The months of union fly past like hours,', 'مہینے وصل کے گھڑیوں کی صورت اُڑتے جاتے ہیں', 'د وصال میاشتې د ګړیو په څېر الوزي،'),
    ('but the hours of separation pass like months.', 'مگر گھڑیاں جُدائی کی گزرتی ہیں مہینوں میں', 'خو د بېلتون ګړۍ په میاشتو کې تېرېږي.'),
    ('The figure of contrast (ṣanʿat-e taẓād) is found in this couplet. Define the figure of contrast, give further examples and point it out in this couplet.', 'اس شعر میں صنعتِ تضاد پائی جاتی ہے۔ صنعتِ تضاد کی تعریف کریں، مزید مثالیں دیں اور اس شعر میں اس کی نشان دہی کریں۔', 'په دې بیت کې د تضاد صنعت شته. د تضاد صنعت تعریف کړئ، نورې بېلګې ورکړئ او په دې بیت کې یې په نښه کړئ.'),
    ('4. Write the meanings of the following words: nukta-chīn, yad-e baiẓā, bārīk-bīn, mauj-e nafas, maḥmil-nishīn, irādat.', '۴۔ درج ذیل الفاظ کے معنی لکھیں: نکتہ چیں، یدِ بیضا، باریک بین، موجِ نفس، محمل نشیں، ارادت۔', '۴. د لاندې کلمو ماناوې ولیکئ: نیوکه‌کوونکی، ید بیضا، باریک‌بین، د ساه څپه، کجاوه‌ناست، ارادت.'),
    ('5. Read this couplet:', '۵۔ یہ شعر پڑھیں:', '۵. دا بیت ولولئ:'),
    ('Those whom I used to seek in the heavens and on the earths', 'جنھیں میں ڈھونڈتا تھا آسمانوں میں زمینوں میں', 'هغه چې ما به په اسمانونو او ځمکو کې لټول'),
    ('turned out to be the dwellers of my heart’s dark chamber.', 'وہ نکلے میرے ظلمت خانۂ دل کے مکینوں میں', 'زما د زړه د تیارې کوټې اوسېدونکي راووتل.'),
    ('Words in a text that are alike in spelling but different in meaning are called “tajnīs-e tām” (perfect paronomasia). Point out tajnīs-e tām in the couplet given above and write any two couplets in which the figure tajnīs-e tām is used.', 'کلام میں ایسے الفاظ جو املا کے لحاظ سے تو ایک جیسے ہوں مگر دونوں کا مطلب جدا ہو۔ تجنیسِ تام کہلاتا ہے۔ اوپر دیے گئے شعر میں تجنیسِ تام کی نشان دہی کریں اور کوئی سے دو ایسے اشعار لکھیں جن میں صنعتِ تجنیسِ تام کا استعمال ہو۔', 'په کلام کې داسې کلمې چې په لیکنه کې یو شان وي خو مانا یې بېله وي، "تجنیس تام" بلل کېږي. په پورتني بیت کې تجنیس تام په نښه کړئ او هر دوه داسې بیتونه ولیکئ چې پکې د تجنیس تام صنعت کارول شوی وي.'),
])
ex = BOOK.record(e, 'urdu12-u26-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 117, [224])

n = Builder()
n.h('Ghazal', 'غزل', 'غزل')
n.group('lines', [
    ('The word ghazal is an Arabic verbal noun meaning “to spin” (making thread from cotton on the spinning wheel).', 'غزل کا لفظ عربی زبان کا ایک مصدر ہے۔ جس کے معنی ’’کاتنا‘‘ (چرخے پر روئی سے سُوت ’’دھاگہ‘‘ بنانا) ہے۔', 'غزل عربي مصدر دی چې مانا یې "اوبدل/رېشل" ده (په څرخه د پنبې نه تار جوړول).'),
    ('In literary terms ghazal means to talk with women, to praise the beauty of women.', 'ادب کی رُو سے غزل کے معنی ہیں عورتوں سے باتیں کرنا، عورتوں کے حُسن جمال کی تعریف کرنا۔', 'د ادب له مخې د غزل مانا له ښځو سره خبرې کول او د ښځو د ښکلا ستاینه ده.'),
    ('The ghazal is a genre of verse in which love and affection (divine and worldly) are mentioned.', 'غزل نظم کی ایسی صنف ہے جس میں عشق و محبت (حقیقی و مجازی) کا ذکر ہوتا ہے۔', 'غزل د منظوم کلام داسې ژانر دی چې پکې د عشق او مینې (حقیقي او مجازي) یادونه کېږي.'),
    ('A ghazal has at least five couplets, and no upper limit is fixed.', 'غزل کے کم از کم اشعار کی تعداد پانچ اور زیادہ کی کوئی حد مقرر نہیں ہے۔', 'د غزل لږ تر لږه بیتونه پنځه دي او د ډېرو لپاره کومه پوله نه ده ټاکل شوې.'),
])
nt = BOOK.record(n, 'urdu12-u26-note', 'Note: the ghazal', 'غزل (تعریف)', 'غزل (تعریف)', 117, [224])

a = Builder()
a.h('Faiz Ahmad Faiz', 'فیض احمد فیضؔ', 'فیض احمد فیض')
a.p('Born: 1910 · Died: 1984', 'ولادت: ۱۹۱۰ء · وفات: ۱۹۸۴ء', 'زېږېدنه: ۱۹۱۰ز · مړینه: ۱۹۸۴ز')
for x in [
    ("Faiz Ahmad Faiz was born in Sialkot and received his early education there. After his B.A. he did B.A. Honours in Arabic and then an M.A. in English and Arabic. Faiz's practical life was very varied and eventful; for some time he also served in the army. He was arrested in the Rawalpindi Conspiracy Case and everyone was sure he would be sentenced to hanging, but he was given two and a half years' imprisonment. Faiz's first collection, “Naqsh-e-Faryadi”, was published in 1941. Because of his poetry and humanitarian ideas he also received the Lenin Peace Award.",
     'فیض احمد فیضؔ سیالکوٹ میں پیدا ہوئے۔ ابتدائی تعلیم وہیں سے حاصل کی۔ بی۔اے کرنے کے بعد عربی میں بی۔اے آنرز کیا اور پھر انگریزی اور عربی میں ایم۔اے کیا۔ فیضؔ کی عملی زندگی بڑی متنوع اور ہنگامہ خیز تھی۔ کچھ عرصے فوج میں بھی ملازمت کی۔ راولپنڈی سازش کیس میں گرفتار ہوئے اور سب کو یقین تھا کہ اُنھیں پھانسی کی سزا ہو جائے گی لیکن انھیں ڈھائی سال قید کی سزا ملی۔ فیضؔ کا پہلا مجموعہ کلام ’’نقشِ فریادی‘‘ کے نام سے ۱۹۴۱ء میں شائع ہوا۔ اپنی شاعری اور انسان دوست خیالات کی وجہ سے انھیں لینن امن ایوارڈ بھی ملا۔',
     'فیض احمد فیض په سیالکوټ کې زېږېدلی او لومړنۍ زده‌کړې یې همالته وکړې. د بي.اې وروسته یې په عربي کې بي.اې آنرز او بیا په انګرېزي او عربي کې ایم.اې وکړ. د فیض عملي ژوند ډېر رنګارنګ او پېښې‌ډک و؛ یو څه موده یې په پوځ کې هم دنده وکړه. د راولپنډۍ د دسیسې په قضیه کې ونیول شو او ټولو ډاډ درلود چې د ځړولو سزا به ورکړل شي، خو دوه نیم کاله بند ورکړل شو. د فیض لومړۍ ټولګه "نقش فریادي" په ۱۹۴۱ز کې خپره شوه. د خپلې شاعرۍ او انسان‌دوسته فکرونو له امله یې د لینن د سولې جایزه هم ترلاسه کړه.'),
    ("Among the poets connected with the Progressive Movement, Faiz Ahmad Faiz holds a very high and unique place. Faiz had a special gift for image-making; he was skilled in verbal portraiture. He is wholly a poet of aesthetics; he used artistic devices such as melody, imagery, metaphor and simile with great skill. Faiz was well acquainted with the traditions of Urdu poetry and was also familiar with Persian and English poetry. His poetry begins with romance and intuition, but the hard and bitter realities of life soon fix its permanent path. Besides personal pain he feels within himself the grief and suffering of the whole of humanity, and so his poetry becomes a beautiful blend of love and reality.",
     'ترقی پسند تحریک سے وابستہ شعرا میں فیض احمد فیضؔ کا مقام بہت بلند اور منفرد ہے۔ فیضؔ کو پیکر تراشی میں ایک خاص ملکہ تھا۔ لفظی تصویر کشی میں مہارت رکھتے تھے۔ وہ سراسر جمالیات کے شاعر ہیں۔ انھوں نے نغمگی، امیجری، استعارہ اور تشبیہ جیسے فنی لوازمات کو بڑی ہنرمندی سے استعمال کیا۔ فیضؔ اردو شاعری کی روایات سے بخوبی آگاہ تھے اور فارسی، انگریزی شاعری سے بھی واقف تھے۔ ان کی شاعری کا آغاز رومان اور وجدان سے ہوتا ہے لیکن زندگی کے سخت اور کڑے حقائق جلد ہی ان کی شاعری کی مستقل راہ متعین کر دیتے ہیں۔ ذاتی دکھ کے علاوہ عالمِ انسانیت کے رنج و الم اپنے اندر محسوس کرتے ہیں اور یوں ان کی شاعری محبت اور حقیقت کا حسین امتزاج بن جاتی ہے۔',
     'د ترقي‌پسند غورځنګ سره تړلو شاعرانو کې د فیض احمد فیض مقام ډېر لوړ او بې‌ساری دی. فیض په انځورګرۍ کې ځانګړې وړتیا درلوده؛ په لفظي انځورونو کې ماهر و. هغه بشپړ د ښکلا شاعر دی؛ نغمګي، انځورګري، استعاره او تشبیه یې په ډېر هنر کارولي. فیض د اردو شاعرۍ له دودونو ښه خبر و او له فارسي او انګرېزي شاعرۍ سره هم اشنا و. د هغه شاعري له رومان او وجدانه پیلېږي، خو د ژوند سخت او ترخه حقایق ژر د هغه د شاعرۍ دایمي لار ټاکي. له شخصي درد پرته د ټول انسانیت غم او درد په ځان کې احساسوي، او په دې ډول یې شاعري د مینې او حقیقت ښکلی ګډون کېږي.'),
    ("Collections of poetry: Naqsh-e-Faryadi, Dast-e-Saba, Zindan Nama, Dast-e-Tah-e-Sang, Sar-e-Wadi-e-Sina, Sham-e-Shehr-e-Yaran, Mere Dil Mere Musafir, Ghubar-e-Ayyam.", 'مجموعہ ہائے کلام: نقشِ فریادی، دستِ صبا، زندان نامہ، دستِ تہِ سنگ، سرِ وادیٔ سینا، شامِ شہرِ یاراں، میرے دل مرے مسافر، غبارِ ایام۔', 'د کلام ټولګې: نقش فریادي، دست صبا، زندان نامه، دست ته سنګ، سر وادي سینا، شام شهر یاران، میرے دل مرے مسافر، غبار ایام.'),
]: a.p(*x)
UT = ('Ghazal: When is your company not in my memory…', 'غزل: کب یاد میں تیرا ساتھ نہیں، کب ہات میں تیرا ہات نہیں', 'غزل: کله ستا ملګرتیا زما په یاد کې نه ده…', 'فیض احمد فیضؔ')
au = BOOK.record(a, 'urdu12-u27-author', 'About the poet: Faiz Ahmad Faiz', 'فیض احمد فیضؔ (تعارف)', 'فیض احمد فیض (پېژندنه)', 117, [225], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Faiz and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf117', 'unit': 27, 'printedPage': 225, 'description': 'Faiz died 1984 — in copyright; Ghazal 10 will be summarised couplet-wise with a sourceGap note. p.224 Q5 prints “جو املا کے لحاظ سے تو ایک جیسے ہوں … تجنیسِ تام کہلاتا ہے” (sentence fragment) — retained.'}]

if __name__ == '__main__':
    BOOK.save(117, [(26, ex), (26, nt), (27, au)], issues=issues)
