"""Urdu XII PDF71 (spread): p.132 Lesson 13 مشق Q4 (اعراب by meaning) + book-cover image; p.133 Lesson 14 author note (چراغ حسن حسرت, 1902–1955)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.p('4. Put diacritics (iʿrāb) on the following words according to the meanings written beside them.', '۴۔ درج ذیل الفاظ پر ان کے سامنے لکھے گئے معنی کے مطابق اعراب لگائیں۔', '۴. پر لاندې کلمو د هغو مخې ته لیکل شویو ماناوو سره سم اعراب کېږدئ.')
H = (['Word', 'Meaning (1)', 'Meaning (2)'], ['لفظ', 'معنی (۱)', 'معنی (۲)'], ['کلمه', 'مانا (۱)', 'مانا (۲)'])
ur = [['خم', 'ٹیڑھا پن', 'شراب کا مٹکا'], ['کرم', 'مہربانی', 'کیڑا'], ['کل', 'تمام، میزان', 'پُرزہ، گزرا یا آنے والا دن'], ['محقق', 'تحقیق کرنے والا', 'جس پر تحقیق کی گئی ہو'], ['منتظر', 'انتظار کرنے والا', 'جس کا انتظار کیا جائے']]
en = [['khm (خم)', 'kham — bend, crookedness', 'khum — wine jar'], ['krm (کرم)', 'karam — kindness', 'kirm — worm, insect'], ['kl (کل)', 'kul — all, total', 'kal — machine part; yesterday/tomorrow'], ['mḥqq (محقق)', 'muḥaqqiq — researcher', 'muḥaqqaq — researched, verified'], ['mntẓr (منتظر)', 'muntaẓir — one who waits', 'muntaẓar — awaited']]
ps = [['خم', 'کږوالی', 'د شرابو منګی'], ['کرم', 'مهرباني', 'چینجی'], ['کل', 'ټول، مجموعه', 'پرزه؛ تېره یا راتلونکې ورځ'], ['محقق', 'څېړونکی', 'څېړل شوی'], ['منتظر', 'انتظار کوونکی', 'هغه چې انتظار یې کېږي']]
e.table('urdu12-u13-iraab', H[0], en, H[1], H[2], ur, ps)
ex = BOOK.record(e, 'urdu12-u13-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 71, [132])
ex['sourceCoverIllustrationReview'] = 'Book-cover image (p.132): “مجموعہ مرزا فرحت اللہ بیگ” with a drawing of a worried student at an exam desk; decorative, not reproduced.'

a = Builder()
a.h('Chiragh Hasan Hasrat', 'چراغ حسن حسرت', 'چراغ حسن حسرت')
a.p('Born: 1902 · Died: 1955', 'ولادت: ۱۹۰۲ء · وفات: ۱۹۵۵ء', 'زېږېدنه: ۱۹۰۲ز · مړینه: ۱۹۵۵ز')
for x in [
    ('His real name was Chiragh Hasan, while his pen-name (takhalluṣ) was Hasrat. He was born in Baramulla, a famous area of Kashmir. He received his early education in Jammu and came to Lahore for further education. Here most people in his circle of friends were connected with journalism, so Hasrat too entered the lane of journalism. Hasrat worked on various newspapers. He began writing humorous columns under the name “Sindbad Jahazi”, in which his natural talents emerged openly. After working on various newspapers he finally joined the “Daily Imroze” and remained connected with it to his last breath.',
     'اصل نام چراغ حسن تھا جبکہ تخلص حسرت تھا۔ وہ کشمیر کے مشہور علاقے بارہ مولا میں پیدا ہوئے۔ ابتدائی تعلیم جموں سے حاصل کی۔ مزید تعلیم کے حصول کے لیے لاہور آ گئے۔ یہاں ان کے حلقۂ احباب میں اکثر لوگوں کا تعلق صحافت سے تھا۔ چنانچہ حسرت بھی کوچۂ صحافت میں جا نکلے۔ حسرت نے مختلف اخبارات میں کام کیا۔ اُنھوں نے ’’سند باد جہازی‘‘ کے نام سے فکاہیہ کالم لکھنا شروع کیے۔ ان کالموں میں حسرت کی فطری صلاحیتیں کھل کر سامنے آئیں۔ مختلف اخبارات میں کام کرتے ہوئے بالآخر ’’روزنامہ امروز‘‘ سے وابستہ ہوئے اور آخری دم تک اسی سے منسلک رہے۔',
     'اصلي نوم یې چراغ حسن و او تخلص یې حسرت. هغه د کشمیر په مشهوره سیمه بارامولا کې زېږېدلی. لومړنۍ زده کړې یې په جمون کې وکړې او د نورو زده کړو لپاره لاهور ته راغی. دلته د هغه د ملګرو په کړۍ کې ډېری خلک له ژورنالیزم سره تړلي وو، نو حسرت هم د ژورنالیزم کوڅې ته ورننوت. حسرت په بېلابېلو ورځپاڼو کې کار وکړ. د "سندباد جهازي" په نوم یې طنزي کالمونه لیکل پیل کړل، چې پکې د حسرت طبیعي وړتیاوې په ښکاره راڅرګندې شوې. په بېلابېلو ورځپاڼو کې له کار کولو وروسته په پای کې له "ورځپاڼې امروز" سره وتړل شو او تر وروستۍ ساه ورسره پاتې شو.'),
    ('Hasrat was a famous journalist and a widely popular humorist. His writings can be clearly divided into two parts: first, the columns that adorned newspapers; second, the personal sketches (khāke) he wrote introducing various personalities. In both, Hasrat’s traditional wit shines through. His humorous column-writing laid the foundation of important traditions in the world of newspapers; collections of his columns have also been published. Hasrat’s language is simple, fluent and smooth; he had a special gift for the use of words and phrases. In sketch-writing he chose personalities with whom he had deep attachment and sincerity.',
     'حسرت ایک مشہور صحافی اور مقبولِ عام مزاح نگار تھے۔ ان کے مضامین کو واضح طور پر دو حصوں میں تقسیم کیا جا سکتا ہے۔ ایک وہ کالم جو اخبارات کی زینت بنتے رہتے تھے۔ دوسرے وہ شخصی خاکے جو اُنھوں نے مختلف شخصیات کے تعارف کے طور پر لکھے۔ دونوں میں حسرت کی روایتی ظرافت جھلکتی ہے۔ ان کی فکاہیہ کالم نویسی نے اخبارات کی دنیا میں اہم روایات کی بنیاد ڈالی۔ ان کے کالموں کے مجموعے بھی شائع ہو چکے ہیں۔ حسرت کی زبان سادہ، رواں اور سلیس ہے۔ ان کو الفاظ و تراکیب کے استعمال کا خاص ملکہ تھا۔ خاکہ نگاری میں اُنھوں نے ایسی شخصیات کا انتخاب کیا، جن کے ساتھ ان کی گہری وابستگی اور خلوص تھا۔',
     'حسرت یو مشهور ژورنالیست او په عامو کې مشهور طنزلیکوال و. د هغه لیکنې په ښکاره دوه برخو وېشل کېدای شي: یو هغه کالمونه چې د ورځپاڼو ښکلا به وه؛ دویم هغه شخصي خاکې چې د بېلابېلو شخصیتونو د پېژندنې لپاره یې لیکلې. په دواړو کې د حسرت دودیز ظرافت ځلېږي. د هغه طنزي کالم‌لیکنې د ورځپاڼو په نړۍ کې د مهمو دودونو بنسټ کېښود؛ د کالمونو ټولګې یې هم خپرې شوې. د حسرت ژبه ساده، روانه او اسانه ده؛ د کلمو او ترکیبونو په کارولو کې یې ځانګړې وړتیا درلوده. په خاکه‌لیکنه کې یې داسې شخصیتونه غوره کړل چې ورسره یې ژوره تړاو او اخلاص درلود.'),
    ('Works: Fukahiyat, Harf-o-Hikayat, Kele ka Chhilka, Jadeed Jughrafiya-e-Punjab, Mardum Deeda, etc.', 'تصانیف: فکاہیات، حرف و حکایت، کیلے کا چھلکا، جدید جغرافیہ پنجاب، مردم دیدہ وغیرہ۔', 'تصنیفات: فکاهیات، حرف و حکایت، د کېلې پوستکی، د پنجاب نوې جغرافیه، مردم دیده او نور.'),
]: a.p(*x)
UT = ('Allama Iqbal', 'علّامہ اقبالؒ', 'علامه اقبال', 'چراغ حسن حسرت')
au = BOOK.record(a, 'urdu12-u14-author', 'About the author: Chiragh Hasan Hasrat', 'چراغ حسن حسرت (تعارف)', 'چراغ حسن حسرت (پېژندنه)', 71, [133], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait of Chiragh Hasan Hasrat and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf071', 'unit': 13, 'printedPage': 132, 'description': 'Lesson 13 exercise numbering ends at Q4 (p.132). Chiragh Hasan Hasrat died 1955; under Pakistani copyright (life + 50 years) the Lesson 14 sketch is public domain and will be transcribed in full.'}]

if __name__ == '__main__':
    BOOK.save(71, [(13, ex), (14, au)], issues=issues, complete_units=[13])
