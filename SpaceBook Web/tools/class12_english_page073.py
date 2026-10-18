"""PDF73 (printed 133–134): 'Lingkuan Gorge' (end) — summary; About the Author; Glossary (apparently … depot)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
r = Builder()
S = [
    ('Through the gap the narrator sees, in a searchlight beam, dozens of men clinging to the cliff and drilling holes for dynamite. Cheng-yu cannot see his father, but his father has told him he can see the boy whenever he turns round, so the boy sits there to be seen. He also looks after his little sister until his mother comes home.',
     'درز سے راوی سرچ لائٹ کی روشنی میں درجنوں آدمیوں کو چٹان سے چمٹے ڈائنامائٹ کے لیے سوراخ کرتے دیکھتا ہے۔ چینگ یو اپنے والد کو نہیں دیکھ سکتا، لیکن اس کے والد نے اسے بتایا ہے کہ جب بھی وہ مڑتے ہیں لڑکے کو دیکھ سکتے ہیں، اس لیے لڑکا وہاں بیٹھتا ہے تاکہ دکھائی دے۔ وہ اپنی ماں کے گھر آنے تک اپنی ننھی بہن کی دیکھ بھال بھی کرتا ہے۔',
     'له درز څخه راوي د سرچ‌لایټ په رڼا کې لسګونه سړي ویني چې په غره نښتي دي او د ډینامایټ لپاره سوري کوي. چېنګ یو خپل پلار نه شي لیدلی، خو پلار یې ورته ویلي چې هرکله راوګرځي هلک لیدلی شي، نو هلک هلته ناست وي چې ولیدل شي. هغه تر هغه چې مور یې کور ته راشي د خپلې کوچنۍ خور پالنه هم کوي.'),
    ('His mother stands in the snow by a telephone pole on the road below, directing traffic. The narrator imagines the family — father on the cliff, mother on the road, children in the cave — unable to see one another clearly but bound by love and duty, each looking forward to their reunion.',
     'اس کی ماں نیچے سڑک پر ٹیلی فون کے کھمبے کے پاس برف میں کھڑی ٹریفک کنٹرول کر رہی ہے۔ راوی اس خاندان کا تصور کرتا ہے — باپ چٹان پر، ماں سڑک پر، بچے غار میں — جو ایک دوسرے کو صاف نہیں دیکھ سکتے لیکن محبت اور فرض کے بندھن میں بندھے ہیں اور ہر ایک ملاپ کے لمحے کا منتظر ہے۔',
     'مور یې لاندې پر سړک د ټیلیفون پایې ته نږدې په واوره کې ولاړه ده او ترافیک تنظیموي. راوي دا کورنۍ تصور کوي — پلار پر غره، مور پر سړک، ماشومان په سمڅه کې — چې یو بل په روښانه ډول نه شي لیدلی خو د مینې او دندې په تړاو تړلي دي او هر یو د بیا یوځای کېدو شېبې ته انتظار کوي.'),
    ('When the sleepy boy is told to go to bed, he refuses: “Papa and mama say a man should never leave his post.” Moved, the narrator hugs him, gives up his rest and walks on through the night to reach his own work.',
     'جب نیند سے بوجھل لڑکے سے سونے کو کہا جاتا ہے تو وہ انکار کر دیتا ہے: ’’ابا اور اماں کہتے ہیں کہ آدمی کو کبھی اپنی جگہ نہیں چھوڑنی چاہیے۔‘‘ متاثر ہو کر راوی اسے گلے لگاتا ہے، اپنا آرام ترک کرتا ہے اور رات بھر چل کر اپنے کام تک پہنچنے کے لیے روانہ ہو جاتا ہے۔',
     'کله چې خوبجن هلک ته ویل کېږي چې ویده شي، انکار کوي: "پلار او مور وایي چې سړی باید هېڅکله خپل پوسټ پرې نه ږدي." راوي اغېزمن کېږي، هغه په غېږ کې نیسي، خپله دمه پرېږدي او د شپې په اوږدو کې خپل کار ته د رسېدو لپاره روانېږي.'),
    ('(Translated anonymously from the Chinese)', '(چینی سے گمنام ترجمہ)', '(له چینایي ژبې څخه بې‌نومه ژباړه)'),
]
for x in S: r.p(*x)
rd = BOOK.record(r, 'eng12-u14-text-summary-b', 'Reading text — summary (2)', 'متن — خلاصہ (2)', 'متن — لنډیز (2)', 73, [133, 134])
rd['sourceGap'] = 'Modern copyrighted story (Tu Peng-Cheng, English translation); paragraph-wise summary, not verbatim.'
rd['sourceCoverIllustrationReview'] = 'Photograph of a cave interior is decorative; not reproduced.'
a = Builder()
a.h('About the Author', 'مصنف کے بارے میں', 'د لیکوال په اړه')
a.p("After growing up in a poor family in the province of Shenshi (also spelled Shaanxi) TuPeng-cheng (born 1921) worked as a correspondent for the New China News during China's civil war in the late 1940's. His many notes about battles he witnessed, became important sources for his later fiction, including his acclaimed war novel, Defend Yenan, published in 1954.",
    'شینشی (جسے شانسی بھی لکھا جاتا ہے) صوبے کے ایک غریب خاندان میں پروان چڑھنے کے بعد تو پنگ چینگ (پیدائش 1921) نے 1940 کی دہائی کے آخر میں چین کی خانہ جنگی کے دوران ’’نیو چائنا نیوز‘‘ کے نامہ نگار کے طور پر کام کیا۔ ان جنگوں کے بارے میں ان کے بہت سے نوٹس جن کے وہ عینی شاہد تھے، ان کے بعد کے افسانوں کے اہم ماخذ بنے، جن میں 1954 میں شائع ہونے والا ان کا مشہور جنگی ناول ’’ڈیفنڈ ینان‘‘ بھی شامل ہے۔',
    'د شېنشي (چې شانشي هم لیکل کېږي) ولایت په یوه بېوزله کورنۍ کې له لویېدو وروسته، تو پنګ چېنګ (زېږون 1921) د 1940 لسیزې په وروستیو کې د چین د کورنۍ جګړې پر مهال د "نوي چین خبرونو" د خبریال په توګه کار وکړ. د هغو جګړو په اړه د هغه ډېر یادښتونه چې شاهد یې و، د هغه د وروستیو داستانونو مهمې سرچینې شوې، په ګډون د هغه د ستایل شوي جګړه‌ییز ناول "ینان ساتنه" چې په 1954 کې خپور شو.')
a.p("Winning praise throughout China for his depiction of military life, Tu enjoyed a flourishing career throughout the 1950s. In 1958 he published his next major novel In Peacetime, which describes workers constructing the Paoki to Chengtu (Baoji to Chengdu) Railway. Tu fell from favour in the 1960s when the government rewrote its history and condemned several former leaders whom Tu had praised in his fiction. His work was banned in China until 1978 when a thaw in the nation's totalitarian regime allowed Tu to resume his writing career.",
    'فوجی زندگی کی عکاسی پر پورے چین میں تعریف پانے والے تو نے 1950 کی پوری دہائی میں ایک کامیاب کیریئر گزارا۔ 1958 میں انہوں نے اپنا اگلا بڑا ناول ’’ان پیس ٹائم‘‘ شائع کیا جس میں پاؤکی سے چینگتو (باؤجی سے چینگدو) ریلوے بنانے والے مزدوروں کا بیان ہے۔ 1960 کی دہائی میں جب حکومت نے اپنی تاریخ دوبارہ لکھی اور ان کئی سابق رہنماؤں کی مذمت کی جن کی تو نے اپنے افسانوں میں تعریف کی تھی تو وہ معتوب ہو گئے۔ ان کی تخلیقات پر چین میں 1978 تک پابندی رہی، جب ملک کی مطلق العنان حکومت میں نرمی آئی اور تو اپنا تحریری کام دوبارہ شروع کر سکے۔',
    'د پوځي ژوند د انځورولو له امله په ټول چین کې ستایل شوی، تو د 1950 لسیزې په اوږدو کې بریالی مسلک درلود. په 1958 کې یې خپل بل لوی ناول "د سولې په وخت کې" خپور کړ چې د پاوکي-چېنګتو (باوجي-چېنګدو) اورګاډي لیکې جوړوونکي کارګران بیانوي. تو په 1960 لسیزه کې هغه وخت له نظره ولوېد چې حکومت خپل تاریخ بیا ولیکه او ګڼ هغه پخواني مشران یې وغندل چې تو په خپلو داستانونو کې ستایلي وو. د هغه اثار په چین کې تر 1978 پورې منع وو، کله چې د هېواد په استبدادي نظام کې نرمښت راغی او تو ته یې اجازه ورکړه چې خپل لیکنیز کار بیا پیل کړي.')
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u14-gloss-a', [
    ('apparently(adv.)', 'Readily seen or understood; evident, obvious', 'آسانی سے دیکھا یا سمجھا جانے والا؛ واضح، ظاہر', 'په اسانۍ لیدل کېدونکی یا پوهېدونکی؛ ښکاره، څرګند'),
    ('crisscrossing(v)', 'To move or cause to move in a crosswise pattern', 'آڑی ترچھی شکل میں حرکت کرنا یا کروانا', 'په تقاطعي بڼه حرکت کول یا حرکت ته اړ کول'),
    ('depot(n)', 'A storehouse or warehouse for supplies, usually the military', 'رسد کا ذخیرہ یا گودام، عموماً فوجی', 'د توکو زېرمتون یا ګودام، معمولاً پوځي'),
])
ab = BOOK.record(a, 'eng12-u14-about-glossary-a', 'About the Author; Glossary (1)', 'مصنف کے بارے میں؛ فرہنگ (1)', 'د لیکوال په اړه؛ وییپانګه (1)', 73, [134])
issues = [{'id': 'eng12-p134', 'unit': 14, 'printedPage': 134, 'description': "About the Author printed spellings retained: “Shenshi”, “TuPeng-cheng”, “1940’s”. The story text (pp131–134) itself prints “Me rubbed his eyes” (He)."}]

if __name__ == '__main__':
    BOOK.save(73, [(14, rd), (14, ab)], issues=issues)
