"""Urdu XII PDF48 (spread): p.86 Lesson 9 مشق Q3–Q5 + رموزِ اوقاف وقفہ (Lesson 9 complete); p.87 Lesson 10 author note (شوکت صدیقی, 1923–2006)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.p('3. Fill in the blanks according to the text.', '۳۔ متن کے مطابق خالی جگہ پُر کریں۔', '۳. د متن له مخې تش ځایونه ډک کړئ.')
e.group('lines', [
    ('(a) She heard such ________ that the poor woman forgot even the earthquake.', '(الف) بیگم خواجہ کو وہ ________ سنائیں کہ وہ بے چاری زلزلے کو بھول گئی۔', '(الف) بېګم خواجه ته یې داسې ________ واورولې چې بېچارې زلزله هم هېره کړه.'),
    ('(b) Even two pots kept together clatter when they ________ .', '(ب) اکٹھے رکھے ہوئے دو برتن بھی ________ کر بجتے ہیں۔', '(ب) یوځای اېښي دوه لوښي هم په ________ سره ږغېږي.'),
    ('(c) In their talk there were few ________ and many curses.', '(ج) اُن کی باتوں میں ________ کم اور بددعائیں زیادہ ہوتی تھیں۔', '(ج) د هغوی په خبرو کې ________ لږ او ښېرې ډېرې وې.'),
    ('(d) As a patient is forced to eat ________ food.', '(د) جیسے مریض ________ کا کھانا کھانے پر مجبور ہوتا ہے۔', '(د) لکه څنګه چې ناروغ د ________ خوړو خوړلو ته اړ وي.'),
    ('(e) Begum Khwaja was smiling on hearing the curse of her own ________ .', '(ہ) بیگم خواجہ اپنے ________ کی بددعا سن کر مسکرا رہی تھی۔', '(ه) بېګم خواجه د خپل ________ ښېرې په اورېدو موسکا کوله.'),
])
e.p('4. Put diacritics (iʿrāb) on these words according to the meanings given in front of them.', '۴۔ ان الفاظ پر سامنے دیے گئے معنی کے مطابق اعراب لگائیں۔', '۴. پر دې کلمو د مخې ته ورکړل شویو ماناوو سره سم اعراب کېږدئ.')
H = (['Word (ʿ-l-m / m-l-k)', 'Meaning'], ['لفظ', 'معنی'], ['کلمه', 'مانا'])
rows_ur = [['عالم', 'علم والا'], ['عالم', 'حالت، دُنیا'], ['علم', 'معلومات'], ['علم', 'جھنڈا'], ['ملک', 'وطن'], ['ملک', 'جاگیر، جائداد'], ['ملک', 'فرشتہ'], ['ملک', 'بادشاہ، حاکم']]
rows_en = [['ʿālim (عالم)', 'one who has knowledge, scholar'], ['ʿālam (عالم)', 'state; world'], ['ʿilm (علم)', 'knowledge, information'], ['ʿalam (علم)', 'flag, banner'], ['mulk (ملک)', 'country, homeland'], ['milk (ملک)', 'landed estate, property'], ['malak (ملک)', 'angel'], ['malik (ملک)', 'king, ruler']]
rows_ps = [['عالم', 'د علم خاوند'], ['عالم', 'حالت؛ نړۍ'], ['علم', 'معلومات، پوهه'], ['علم', 'بیرغ'], ['ملک', 'هېواد، وطن'], ['ملک', 'جاګیر، ملکیت'], ['ملک', 'پرښته'], ['ملک', 'پاچا، حاکم']]
e.table('urdu12-u9-iraab', H[0], rows_en, H[1], H[2], rows_ur, rows_ps)
e.p('5. Identify the auxiliary verbs in this lesson.', '۵۔ اس سبق میں امدادی افعال کی نشاندہی کریں۔', '۵. په دې لوست کې مرستندوي فعلونه وپېژنئ.')
e.h('Punctuation marks (Rumūz-e-Awqāf):', 'رموزِ اوقاف:', 'د تکي‌ایښودنې نښې (رموزِ اوقاف):')
e.p('Semicolon (waqfa) ( ؛ ): Where a pause longer than the comma (saktā) is needed, the semicolon is used. It is used on the following occasions:', 'وقفہ: (؛) جب سکتے سے زیادہ ٹھہرنے کی ضرورت ہو وہاں وقفہ استعمال کیا جاتا ہے۔ اس کا استعمال درج ذیل مواقع پر ہوتا ہے۔', 'وقفه (سیمي‌کولن) ( ؛ ): چېرته چې له سکتې (کامې) زیات درېدو ته اړتیا وي، هلته وقفه کارول کېږي. په لاندې ځایونو کې کارېږي:')
e.group('list', [
    ('To separate the long parts of a sentence from one another.', 'جملے کے لمبے لمبے اجزا کو ایک دوسرے سے علیحدہ کرنے کے لیے۔', 'د جملې د اوږدو برخو د یو بل څخه د جلا کولو لپاره.'),
    ('To give greater emphasis to the different parts of sentences, as: “If you come we shall be glad; if you don’t, we shall be patient.”', 'جملوں کے مختلف اجزا پر زیادہ تاکید دینے کے لیے جیسے: تم آؤ گے تو ہمیں خوشی ہو گی؛ نہ آؤ گے، تو صبر کر لیں گے۔', 'د جملو پر بېلابېلو برخو د ډېر ټینګار لپاره، لکه: "که راشې موږ به خوشحاله شو؛ که رانه شې، صبر به وکړو."'),
    ('Where words such as warna (otherwise), is liye (therefore), lihāza (hence), agarche (although), hālānke (whereas) come between the long parts of sentences, this sign is placed to give the mind a chance to understand.', 'جن جملوں کے لمبے لمبے اجزا کے درمیان ورنہ، اس لیے، لہٰذا، اگرچہ، حالاں کہ وغیرہ جیسے الفاظ آئیں وہاں ذہن کو سمجھنے کا موقع دینے کے لیے یہ علامت لگائی جاتی ہے۔', 'چېرته چې د جملو د اوږدو برخو ترمنځ کلمې لکه "ورنه" (که نه)، "اس لیے" (نو ځکه)، "لہٰذا" (له دې امله)، "اگرچہ" (که څه هم)، "حالاں کہ" (سره له دې) راشي، هلته د ذهن د پوهېدو لپاره دا نښه ایښودل کېږي.'),
])
ex = BOOK.record(e, 'urdu12-u9-exercise-2', 'Exercise (2); punctuation — semicolon', 'مشق (۲)؛ رموزِ اوقاف — وقفہ', 'تمرین (۲)؛ رموزِ اوقاف — وقفه', 48, [86])

a = Builder()
a.h('Shaukat Siddiqui', 'شوکت صدیقی', 'شوکت صدیقي')
a.p('Born: 1923 · Died: 2006', 'ولادت: ۱۹۲۳ء · وفات: ۲۰۰۶ء', 'زېږېدنه: ۱۹۲۳ز · مړینه: ۲۰۰۶ز')
for x in [
    ('Shaukat Husain Siddiqui was born in Lucknow. He passed matric from Islamia High School, Lucknow, and after that studied privately up to the M.A. After the creation of Pakistan he came to Lahore and then settled in Karachi. He began his practical life with journalism; he was associated with Tarkash, Jadeed Adab, Faizabad, Times of Karachi, Morning News, Al-Fatah and others.',
     'شوکت حسین صدیقی لکھنؤ میں پیدا ہوئے۔ اسلامیہ ہائی سکول لکھنؤ سے میٹرک پاس کیا اور اُس کے بعد ایم۔ اے تک پرائیویٹ تعلیم حاصل کی۔ قیامِ پاکستان کے بعد لاہور آئے اور پھر کراچی میں رہائش اختیار کی۔ اُنھوں نے عملی زندگی کا آغاز صحافت سے کیا۔ وہ ترکش، جدید ادب، فیض آباد، ٹائمز آف کراچی، مارننگ نیوز اور الفتح وغیرہ سے منسلک رہے۔',
     'شوکت حسین صدیقي په لکهنو کې زېږېدلی. د لکهنو له اسلامیه عالي ښوونځي یې میټرک تېر کړ او وروسته یې تر ایم اې پورې خصوصي زده کړې وکړې. د پاکستان له جوړېدو وروسته لاهور ته راغی او بیا یې په کراچۍ کې استوګنه غوره کړه. عملي ژوند یې په ژورنالیزم پیل کړ؛ له ترکش، جدید ادب، فیض‌اباد، ټایمز اف کراچي، مارنینګ نیوز او الفتح او نورو سره تړلی و.'),
    ('Shaukat Siddiqui had literary taste from the very beginning. He began his literary life with short-story writing. His first collection of stories pointed to his future. He was at once a short-story writer, novelist, journalist and columnist. In recognition of his literary services he was awarded the “Tamgha-e-Husn-e-Karkardagi” and the “Lifetime Achievement Award”.',
     'شوکت صدیقی ابتدا ہی سے ادبی ذوق کے مالک تھے۔ اُنھوں نے ادبی زندگی کا آغاز افسانہ نگاری سے کیا۔ اُن کے افسانوں کے پہلے مجموعے نے اُن کے مستقبل کی نشاندہی کر دی۔ وہ بیک وقت ایک افسانہ نگار، ناول نگار، صحافی اور کالم نویس تھے۔ اُن کی ادبی خدمات کے اعتراف میں ’’تمغۂ حُسنِ کارکردگی‘‘ اور ’’لائف ٹائم اچیومنٹ ایوارڈ‘‘ عطا کیا گیا۔',
     'شوکت صدیقي له پیله ادبي ذوق درلود. ادبي ژوند یې په لنډې کیسې لیکنې پیل کړ. د افسانو لومړۍ ټولګې یې د راتلونکي نښه وکړه. هغه په یو وخت کې لنډې کیسې لیکوال، ناول‌لیکوال، ژورنالیست او کالم‌لیکوال و. د ادبي خدماتو په درناوي ورته "تمغه حسن کارکردګي" او "د ژوند د لاسته راوړنو جایزه" ورکړل شوې.'),
    ('Shaukat Siddiqui wrote both novels and short stories. He is an important name in the intellectual and artistic evolution of the Urdu novel. He received the Adamjee Award for his novel “Khuda ki Basti”. The secret of Shaukat Siddiqui’s success is his realism. He makes the bitter facts and problems of society the subject of his writings. Besides this, his characterisation is also noteworthy; these characters are immortal and present in the society around us. In his stories and novels Shaukat Siddiqui uses very simple, polished and widely understood language. In his work we find the finest pictures of dialogue, characterisation, depiction of emotions and of scenes.',
     'شوکت صدیقی نے ناول بھی لکھے اور افسانے بھی۔ وہ اُردو ناول کے فکری اور فنی ارتقا کے سلسلے میں ایک اہم نام ہیں۔ اُن کے ناول ’’خُدا کی بستی‘‘ پر اُنھیں آدم جی ایوارڈ ملا۔ شوکت صدیقی کی کامیابی کا راز اُن کی حقیقت نگاری ہے۔ وہ معاشرے کے تلخ حقائق اور مسائل کو اپنی تحریروں کا موضوع بناتے ہیں۔ اس کے علاوہ اُن کی کردار نگاری بھی قابلِ ذکر ہے۔ یہ کردار زندۂ جاوید اور ہمارے ارد گرد معاشرے میں موجود ہیں۔ شوکت صدیقی اپنے افسانوں اور ناولوں میں نہایت سادہ سلجھی ہوئی اور عام فہم زبان استعمال کرتے ہیں۔ اُن کے ہاں مکالمہ نگاری، کردار نگاری، جذبات نگاری اور منظر نگاری کے بہترین مرقعے ملتے ہیں۔',
     'شوکت صدیقي ناولونه هم لیکلي او افسانې هم. هغه د اردو ناول د فکري او هنري ودې په لړۍ کې مهم نوم دی. د خپل ناول "خدا کي بستي" لپاره یې ادم جي جایزه ترلاسه کړه. د شوکت صدیقي د بریا راز د هغه حقیقت‌نګاري ده. هغه د ټولنې ترخه حقیقتونه او ستونزې د خپلو لیکنو موضوع ګرځوي. سربېره پر دې، د هغه کرکټرجوړونه هم د یادونې وړ ده؛ دا کرکټرونه تل‌ژوندي او زموږ په شاوخوا ټولنه کې شته. شوکت صدیقي په خپلو افسانو او ناولونو کې ډېره ساده، سمه او عام فهمه ژبه کاروي. د هغه په لیکنو کې د خبرو اترو، کرکټرجوړونې، احساساتو او منظرو د انځورولو غوره بېلګې شته.'),
    ('Works: Teesra Aadmi, Andhera aur Andhera, Raaton ka Shehar, Kimiyagar, Kamin Gah, Khuda ki Basti, Jangloos, Char Diwari, Tantiya, Sharif Aadmi, Raat ki Aankhen, Koka Beli, etc.', 'تصانیف: تیسرا آدمی، اندھیرا اور اندھیرا، راتوں کا شہر، کیمیا گر، کمیں گاہ، خُدا کی بستی، جانگلوس، چار دیواری، تانتیا، شریف آدمی، رات کی آنکھیں، کوکا بیلی وغیرہ۔', 'تصنیفات: درېیم سړی، تیاره او تیاره، د شپو ښار، کیمیاګر، کمین‌ګاه، د خدای بستي، جانګلوس، څلور دیوالي، تانتیا، شریف سړی، د شپې سترګې، کوکا بیلي او نور.'),
]: a.p(*x)
UT = ('Black-skinned', 'سیاہ فام', 'تورپوستی', 'شوکت صدیقی')
au = BOOK.record(a, 'urdu12-u10-author', 'About the author: Shaukat Siddiqui', 'شوکت صدیقی (تعارف)', 'شوکت صدیقي (پېژندنه)', 48, [87], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait of Shaukat Siddiqui and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf048', 'unit': 9, 'printedPage': 86, 'description': 'Q4 prints each word already vowelled beside its meaning (the task is to vowel them); the table gives the meanings with romanised forms in English. Handwritten answers in Q3 blanks and names in the margin are owner notes, excluded. Lesson 10 is “سیاہ فام” by Shaukat Siddiqui (legacy dataset wrongly titled it “تیسرا آدمی”); in copyright (d. 2006), so the story will be summarised.'}]

if __name__ == '__main__':
    BOOK.save(48, [(9, ex), (10, au)], issues=issues, complete_units=[9])
