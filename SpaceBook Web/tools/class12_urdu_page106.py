"""Urdu XII PDF106 (spread): p.202 Poem 3 مشق Q1–Q6 + note تمیز یا متعلق فعل; p.203 Poem 4 author note (میراجی, 1912–1949)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Describe in your own words the scene of morning presented in “Manazir-e-Sahar”.', '۱۔ مناظرِ سحر میں پیش کیا گیا صبح کا منظر اپنے الفاظ میں بیان کریں۔', '۱. د "د سهار منظرې" په نظم کې وړاندې شوې د سهار منظره په خپلو کلمو بیان کړئ.'),
    ('2. Josh is called the Poet of Nature. Explain with reference to this poem.', '۲۔ جوشؔ کو شاعرِ فطرت کہا جاتا ہے۔ اس نظم کے حوالے سے وضاحت کریں۔', '۲. جوش ته "د طبیعت شاعر" ویل کېږي. د دې نظم په حواله یې روښانه کړئ.'),
    ('3. Write a summary of the poem in your own words.', '۳۔ نظم کا خلاصہ اپنے الفاظ میں تحریر کریں۔', '۳. د نظم لنډیز په خپلو کلمو ولیکئ.'),
    ('4. In stanza 3, which things have been called “the festival of dawn” (ʿĪd-e Saḥar)?', '۴۔ بند نمبر ۳ میں کن اشیا کو ’’عیدِ سحر‘‘ سے تعبیر کیا گیا ہے؟', '۴. په درېیم بند کې کوم شیان "د سهار اختر" بلل شوي؟'),
    ('5. In stanza 5, what is meant by “the lights of God” (anwār-e Khudā)?', '۵۔ بند نمبر ۵ میں ’’انوارِ خدا‘‘ سے کیا مراد ہے؟', '۵. په پنځم بند کې "د خدای رڼاوې" څه مانا لري؟'),
    ('6. The figure of allusion (talmīḥ) means putting a famous historical event or scholarly term into verse. Identify two allusions in this poem and also explain them.', '۶۔ صنعتِ تلمیح سے مراد کلام میں کسی مشہور تاریخی واقعہ یا علمی اصطلاح کو نظم کرنا ہے۔ آپ اس نظم سے دو تلمیحات کی نشاندہی کریں اور وضاحت بھی پیش کریں۔', '۶. د تلمیح صنعت دا ده چې په کلام کې یوه مشهوره تاریخي پېښه یا علمي اصطلاح نظم کړل شي. له دې نظمه دوه تلمیحات په نښه کړئ او تشریح یې هم وړاندې کړئ.'),
])
ex = BOOK.record(e, 'urdu12-u20-exercise', 'Exercise', 'مشق', 'تمرین', 106, [202])

g = Builder()
g.h('Adverb (tamīz or mutaʿalliq-e fiʿl)', 'تمیز یا متعلق فعل', 'قید (تمیز یا متعلق فعل)')
g.p('Words that slightly increase or decrease the manner or state of a verb. Some adverbial words are given below:', 'وہ الفاظ جو فعل کی کیفیت یا حالت میں تھوڑی سی کمی بیشی کرتے ہیں۔ چند تمیزی الفاظ درج ذیل ہیں:', 'هغه کلمې چې د فعل په کیفیت یا حالت کې لږ کمی یا زیاتوالی راولي. ځینې قیدي کلمې دا دي:')
g.p('kabhī, kabhī-kabhī, kabhī nahīṉ, kabhī na kabhī, hamesha, aksar, ʿumūman, āʾe din, roz-roz, yakāyak, achānak, jald, jaldī, etc. Make two sentences each with the above adverbial words.', 'کبھی، کبھی کبھی، کبھی نہیں، کبھی نہ کبھی، ہمیشہ، اکثر، عموماً، آئے دن، روز روز، یکایک، اچانک، جلد، جلدی وغیرہ وغیرہ۔ درج بالا تمیزی الفاظ سے دو دو جملے بنائیں۔', 'کله، کله کله، هېڅکله، کله نه کله، تل، ډېری، عموماً، هره ورځ، ورځ په ورځ، ناڅاپه، ناببره، ژر، ژر ژر او نور. له پورتنیو قیدي کلمو دوه دوه جملې جوړې کړئ.')
gr = BOOK.record(g, 'urdu12-u20-grammar', 'Grammar: adverbs', 'تمیز یا متعلق فعل', 'قید', 106, [202])

a = Builder()
a.h('Meeraji', 'میراجیؔ', 'میراجي')
a.p('Born: 1912 · Died: 1949', 'ولادت: ۱۹۱۲ء · وفات: ۱۹۴۹ء', 'زېږېدنه: ۱۹۱۲ز · مړینه: ۱۹۴۹ز')
for x in [
    ("His real name was Muhammad Sanaullah Dar and his pen-name Meeraji. His ancestors came from Kashmir and, migrating under Dogra rule, had settled in Gujranwala, while Meeraji was born in Lahore. Since his father, Munshi Mahtabuddin, was employed in the railways and served at various places, Meeraji could not receive a regular education — he could not even pass the matriculation examination — but his love of reading bordered on mania and he went on studying on his own.",
     'اصل نام محمد ثنا اللہ ڈار اور تخلص میراجی تھا۔ اُن کے آباؤ اجداد کا تعلق کشمیر سے تھا جو ڈوگرہ راج میں ہجرت کر کے گوجرانوالہ میں آباد ہو گئے تھے جب کہ میراجی کی پیدائش لاہور میں ہوئی۔ چونکہ اُن کے والد منشی مہتاب الدین ریلوے میں ملازم تھے اور مختلف مقامات پر ڈیوٹی انجام دیتے رہے اس لیے میراجی باقاعدہ تعلیم حاصل نہ کر سکے۔ یہاں تک کہ میٹرک کا امتحان بھی پاس نہ کر سکے لیکن مطالعے کا شوق جنون کی حد تک تھا اور وہ اپنے طور پر مطالعہ کرتے رہے۔',
     'اصلي نوم یې محمد ثناءالله ډار او تخلص یې میراجي و. نیکونه یې له کشمیره وو، چې د ډوګره د واکمنۍ پر مهال کډه شوي او په ګوجرانواله کې مېشت شوي وو، خو میراجي په لاهور کې زېږېدلی. څرنګه چې پلار یې منشي مهتاب‌الدین په اورګاډي کې کارمند و او په بېلابېلو ځایونو کې یې دنده ترسره کوله، نو میراجي منظمې زده‌کړې ونه شوې کړای — تر دې چې د مېټرک ازموینه یې هم بریالۍ نه کړه — خو د مطالعې شوق یې تر لېونتوب پورې و او پخپله یې مطالعه کوله.'),
    ("Meanwhile the Halqa-e-Arbab-e-Zauq had been founded in Lahore. Meeraji joined it four years after its founding, and his membership brought the circle to life. He remained an active worker and organiser of the Halqa; he himself observed its rules and regulations and made others observe them too.",
     'اس عرصے میں لاہور میں حلقۂ اربابِ ذوق کا قیام عمل میں آ چکا تھا۔ حلقے کے قیام کے چار سال بعد میراجی اس میں شامل ہوئے۔ اُن کی شمولیت سے حلقے میں جان پڑ گئی۔ میراجی حلقے کے سرگرم کارکن اور منتظم رہے ہیں۔ وہ حلقے کے قواعد و ضوابط کی خود بھی پابندی کرتے اور دوسروں سے بھی کرواتے۔',
     'په دې موده کې په لاهور کې "حلقه ارباب ذوق" جوړه شوې وه. د حلقې له جوړېدو څلور کاله وروسته میراجي ورسره یوځای شو، او د هغه په ګډون حلقې ته ساه ورغله. میراجي د حلقې فعال غړی او منتظم پاتې شو؛ د حلقې قواعد او ضوابط یې پخپله هم مراعاتول او له نورو یې هم مراعاتول.'),
    ("Meeraji's whole life passed in deprivations, the remedy for which he sought in poetry. He brought the Urdu naẓm out of dazzling light and introduced it to half-lit shadows. In his poetry, instead of a complete and clear picture of life, he draws such circles and lines that, though clear, they remain veiled in ambiguity. The study of Western poets gave him the idea of making new experiments in modern poetry, and these experiments succeeded; he nurtured them in “Adabi Duniya” and the Halqa-e-Arbab-e-Zauq. He is a poet whose roots are in his own soil; that is why the earthly aspect of Indian civilisation is prominent in his poems. He took the naẓm out of external realism into the human inner self and made the surface meaning of the poem many-sided.",
     'میراجی کی ساری عمر محرومیوں میں گزری جس کا مداوا اُنھوں نے شاعری میں تلاش کیا۔ اُنھوں نے اُردو نظم کو چکا چوند روشنی سے نکال کر نیم روشن سایوں سے متعارف کرایا۔ وہ اپنی شاعری میں زندگی کی مکمل اور واضح تصویر کی بجائے ایسے دائرے اور خطوط بناتے ہیں کہ واضح ہونے کے باوجود بھی اُس پر ابہام کا پردہ پڑا رہتا ہے۔ مغربی شعرا کے مطالعے سے اُنھیں جدید شاعری میں نئے تجربات کرنے کا خیال آیا اور یہ تجربات کامیاب رہے۔ اُنھوں نے ان تجربات کو ’’ادبی دُنیا‘‘ اور حلقۂ اربابِ ذوق میں پروان چڑھایا۔ وہ ایک ایسے شاعر ہیں جس کی جڑیں اپنی دھرتی میں ہیں۔ یہی وجہ ہے کہ اُن کی نظموں میں ہندوستانی تہذیب کا ارضی پہلو نمایاں ہے۔ اُنھوں نے نظم کو خارجی حقیقت نگاری سے نکال کر انسانی باطن میں اُتارا اور نظم کی ایک سطحی معنویت کو ہمہ جہت بنایا۔',
     'د میراجي ټول عمر په محرومیتونو کې تېر شو، چې درملنه یې په شاعرۍ کې ولټوله. هغه اردو نظم له برېښنده رڼا وایست او له نیم‌روښانه سیوریو سره یې اشنا کړ. په خپله شاعرۍ کې د ژوند د بشپړ او روښانه انځور پر ځای داسې ګردونه او کرښې کاږي چې سره له روښانتیا پرې د ابهام پرده پرته وي. د لوېدیځو شاعرانو له مطالعې یې په نوې شاعرۍ کې د نویو تجربو فکر پیدا شو او دا تجربې بریالۍ شوې؛ دا تجربې یې په "ادبي دنیا" او حلقه ارباب ذوق کې وروزلې. هغه داسې شاعر دی چې ریښې یې په خپله خاوره کې دي؛ ځکه یې په نظمونو کې د هندي تمدن ځمکنی اړخ څرګند دی. هغه نظم له بهرني واقعیت‌نګارۍ وایست او د انسان باطن ته یې ښکته کړ، او د نظم سطحي مانا یې هر اړخیزه کړه.'),
    ('Collections of poetry: Meeraji ke Geet, Meeraji ki Nazmen, Geet hi Geet, Teen Rang, Paband Nazmen.', 'مجموعہ ہائے کلام: میراجی کے گیت، میراجی کی نظمیں، گیت ہی گیت، تین رنگ، پابند نظمیں۔', 'د کلام ټولګې: د میراجي سندرې، د میراجي نظمونه، سندرې سندرې، درې رنګونه، پابند نظمونه.'),
]: a.p(*x)
UT = ('The Sound of Defeat (Shikast ki Awaz)', 'شکست کی آواز', 'د ماتې غږ', 'میراجیؔ')
au = BOOK.record(a, 'urdu12-u21-author', 'About the poet: Meeraji', 'میراجیؔ (تعارف)', 'میراجي (پېژندنه)', 106, [203], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Meeraji is decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf106', 'unit': 21, 'printedPage': 203, 'description': 'p.203: the left margin of the right-hand page is cut at the gutter on several lines; the first words (“اُنھوں”, “تجربات”, “وہ”, “تہذیب”, “اور”) are reconstructed from the OCR aid. Meeraji died 1949 → public domain; Poem 4 will be transcribed in full. In the app Poem 4 is unit 21 and Poem 5 unit 22 (the legacy combined unit “شکست کی آواز اور ستارے” is superseded).'}]

if __name__ == '__main__':
    BOOK.save(106, [(20, ex), (20, gr), (21, au)], issues=issues, complete_units=[20])
