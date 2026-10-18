"""PDF8 (printed 3–4): Unit 1 reading text (end), references, Glossary (accession … dynamic)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
r = Builder()
for x in [
    ('The Last Rasool (ﷺ) lived an active and meaningful life as youth. At the very tender age of 12, he took part in trade activities and accompanied his uncle Abu Talib in a business tour to Syria. When some of the energetic youths of Arab tribes came together to form a peace committee under the name of "Half-ul-Fuzul" (The League of Virtue), the Rasool (ﷺ) didn\'t lag behind and became an active member of the committee. Similarly, when once a strife had arisen among various Arab clans over the setting of the Black Stone (Al-Hajr-ul-Aswad) in its place, it was the 35 years old Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) who helped prevent a serious conflict by resolving the issue very sagaciously.',
     'آخری رسول (ﷺ) نے جوانی میں ایک فعال اور بامعنی زندگی گزاری۔ صرف 12 سال کی کم عمری میں آپ نے تجارتی سرگرمیوں میں حصہ لیا اور اپنے چچا ابو طالب کے ساتھ شام کے تجارتی سفر پر گئے۔ جب عرب قبائل کے کچھ پُرجوش نوجوانوں نے ’’حلف الفضول‘‘ (نیکی کا معاہدہ) کے نام سے ایک امن کمیٹی بنائی تو رسول (ﷺ) پیچھے نہیں رہے اور اس کمیٹی کے فعال رکن بنے۔ اسی طرح جب ایک بار حجرِ اسود کو اس کی جگہ نصب کرنے پر مختلف عرب قبیلوں میں جھگڑا پیدا ہوا تو 35 سالہ حضرت محمد (رسول اللہ خاتم النبیین ﷺ) ہی تھے جنہوں نے نہایت دانائی سے مسئلہ حل کر کے ایک سنگین تصادم کو روکنے میں مدد کی۔',
     'وروستي رسول (ﷺ) په ځوانۍ کې فعال او معنی‌دار ژوند تېر کړ. یوازې د 12 کلونو په کم عمر کې یې په سوداګریزو فعالیتونو کې برخه واخیسته او له خپل تره ابو طالب سره شام ته په سوداګریز سفر لاړ. کله چې د عربي قبیلو ځینو پیاوړو ځوانانو د "حلف الفضول" (د نېکۍ تړون) په نوم د سولې کمیټه جوړه کړه، رسول (ﷺ) شاته پاتې نه شو او د کمیټې فعال غړی شو. همداسې کله چې یو ځل د حجر اسود د خپل ځای ته د ایښودو پر سر د بېلابېلو عربي قبیلو ترمنځ شخړه رامنځته شوه، هغه 35 کلن حضرت محمد (رسول الله خاتم النبیین ﷺ) و چې په ډېر هوښیارۍ یې مسئله حل کړه او د یوې جدي شخړې په مخنیوي کې یې مرسته وکړه.'),
    ('All these examples and many more give inspiration to the Muslim youth to play a vibrant and dynamic part instead of living an obscure and indolent life, and to utilize their vigour in the betterment and uplift of the society',
     'یہ تمام مثالیں اور ان جیسی بہت سی دوسری مثالیں مسلم نوجوانوں کو ترغیب دیتی ہیں کہ وہ گمنام اور کاہل زندگی گزارنے کے بجائے پُرجوش اور متحرک کردار ادا کریں اور اپنی توانائی کو معاشرے کی بہتری اور ترقی میں استعمال کریں',
     'دا ټولې بېلګې او ډېرې نورې مسلمانو ځوانانو ته الهام ورکوي چې د یوه ګمنام او لټ ژوند پر ځای ژوندی او فعال رول ولوبوي، او خپل ځواک د ټولنې په ښه والي او پرمختګ کې وکاروي'),
    ("In his personal life, The Rasool (ﷺ) was the embodiment of modesty and chastity, emphasizing the same upon his followers. He did not let it go even in his very private life . He declared 'Haya' to be the integral part of faith. Once, dwelling upon the significance of modesty (Haya), he said as narrated by Abu Mas'ud (رضی اللہ عنہ), \"If you do not feel ashamed then do whatever you like\". A chaste, modest and a civilized Muslim youth is the ideal of the teachings of Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ).",
     'اپنی ذاتی زندگی میں رسول (ﷺ) حیا اور پاکدامنی کا مجسم نمونہ تھے اور اپنے پیروکاروں پر بھی اسی پر زور دیتے تھے۔ آپ نے اپنی انتہائی نجی زندگی میں بھی اسے ہاتھ سے نہ جانے دیا۔ آپ نے ’’حیا‘‘ کو ایمان کا لازمی حصہ قرار دیا۔ ایک بار حیا کی اہمیت بیان کرتے ہوئے آپ نے فرمایا، جیسا کہ ابو مسعود (رضی اللہ عنہ) سے روایت ہے: ’’اگر تم میں حیا نہ رہے تو جو چاہو کرو۔‘‘ ایک پاکدامن، باحیا اور مہذب مسلم نوجوان حضرت محمد (رسول اللہ خاتم النبیین ﷺ) کی تعلیمات کا آئیڈیل ہے۔',
     'په خپل شخصي ژوند کې رسول (ﷺ) د حیا او پاکلمنۍ مجسم انځور و او پر خپلو پیروانو یې هم پر همدې ټینګار کاوه. هغه حتی په خپل ډېر شخصي ژوند کې هم دا له لاسه ورنه کړه. هغه "حیا" د ایمان لازمي برخه وګڼله. یو ځل یې د حیا د اهمیت په اړه وویل، لکه څنګه چې له ابو مسعود (رضی الله عنه) روایت دی: "که شرم نه کوې نو څه چې غواړې هغه وکړه." یو پاکلمنی، حیاناک او متمدن مسلمان ځوان د حضرت محمد (رسول الله خاتم النبیین ﷺ) د لارښوونو مثالي انځور دی.'),
    ('The beloved Rasool (ﷺ) disliked vanity and ostentation and always adhered to simplicity and austerity. Allah Almighty had put before him keys to the treasures of this world but he rejected it, preferring an extremely simple life. Often for months, no fire could be lighted in his house because of scantiness of means. He always treated the people of inferior social status with kindness and affection. He never allowed his little page to be scolded for his mistakes if any. Anas (رضی اللہ عنہ) testifies to his sublime character:',
     'پیارے رسول (ﷺ) غرور اور نمود و نمائش کو ناپسند فرماتے اور ہمیشہ سادگی اور کفایت شعاری پر قائم رہتے۔ اللہ تعالیٰ نے آپ کے سامنے اس دنیا کے خزانوں کی کنجیاں رکھیں لیکن آپ نے انہیں رد کر دیا اور انتہائی سادہ زندگی کو ترجیح دی۔ اکثر مہینوں تک وسائل کی قلت کی وجہ سے آپ کے گھر میں آگ نہیں جلتی تھی۔ آپ ہمیشہ کمتر سماجی حیثیت کے لوگوں سے مہربانی اور شفقت سے پیش آتے۔ آپ نے کبھی اپنے کم سن خادم کو اس کی غلطیوں پر، اگر کوئی ہوتیں، ڈانٹنے کی اجازت نہیں دی۔ حضرت انس (رضی اللہ عنہ) آپ کے بلند اخلاق کی گواہی دیتے ہیں:',
     'خوږ رسول (ﷺ) غرور او ځان‌ښودنه نه خوښوله او تل یې پر ساده‌ګۍ او قناعت ټینګار کاوه. الله تعالی د هغه مخې ته د دې نړۍ د خزانو کیلي ایښې وې خو هغه رد کړې او ډېر ساده ژوند یې غوره کړ. ډېری وخت د میاشتو لپاره د وسایلو د کمښت له امله د هغه په کور کې اور نه بلېده. هغه تل د ټیټ ټولنیز حیثیت لرونکو خلکو سره په مهربانۍ او شفقت چلند کاوه. هغه هېڅکله اجازه ورنه کړه چې خپل کوچنی خادم د خپلو تېروتنو، که کومې وې، له امله وغندل شي. حضرت انس (رضی الله عنه) د هغه د لوړ اخلاق شاهدي ورکوي:'),
    ('" I served the Rasool (ﷺ) for ten years. By Allah, he (ﷺ) never even said to me \'uff\' . He never said harshly, " why did you do that? Or why did you not do that?" (Sahih al- Bukhari 5691, Sahih Muslim 2309)',
     '’’میں نے دس سال رسول (ﷺ) کی خدمت کی۔ اللہ کی قسم! آپ (ﷺ) نے مجھے کبھی ’اُف‘ تک نہیں کہا۔ آپ نے کبھی سختی سے نہیں فرمایا کہ ’تم نے یہ کیوں کیا؟ یا تم نے یہ کیوں نہیں کیا؟‘‘‘ (صحیح البخاری 5691، صحیح مسلم 2309)',
     '"ما لس کاله د رسول (ﷺ) خدمت وکړ. په الله قسم، هغه (ﷺ) ماته هېڅکله "اف" هم نه دي ویلي. هغه هېڅکله په سختۍ نه دي ویلي چې "دا دې ولې وکړل؟ یا دا دې ولې ونه کړل؟"" (صحیح البخاري 5691، صحیح مسلم 2309)'),
    ('To the obedience of such a benevolent and merciful Rasool (ﷺ), The Lord has attached His own pleasure. The Holy Qur\'an says :',
     'ایسے مہربان اور رحم دل رسول (ﷺ) کی اطاعت کے ساتھ رب نے اپنی رضا وابستہ کر دی ہے۔ قرآنِ پاک فرماتا ہے:',
     'د داسې مهربان او رحمدل رسول (ﷺ) له اطاعت سره رب خپله رضا تړلې ده. قرآن کریم فرمایي:'),
    ('"Say (O Prophet) if you really love Allah, then follow me, Allah will love you and forgive you your sins. "(Surah Al Imran, Verse. 31)',
     '’’(اے نبی) کہہ دیجیے: اگر تم واقعی اللہ سے محبت کرتے ہو تو میری پیروی کرو، اللہ تم سے محبت کرے گا اور تمہارے گناہ معاف کر دے گا۔‘‘ (سورۂ آلِ عمران، آیت 31)',
     '"(ای پیغمبره) ووایه: که تاسو په رښتیا له الله سره مینه لرئ نو زما پیروي وکړئ، الله به له تاسو سره مینه وکړي او ستاسو ګناهونه به وبښي." (سورة آل عمران، آیت 31)'),
    ('It clearly denotes that the pleasure of Allah Almighty can be achieved through following the footprints of His beloved Rasool (ﷺ).',
     'یہ صاف ظاہر کرتا ہے کہ اللہ تعالیٰ کی رضا اس کے پیارے رسول (ﷺ) کے نقشِ قدم پر چل کر حاصل کی جا سکتی ہے۔',
     'دا په ښکاره ښيي چې د الله تعالی رضا د هغه د خوږ رسول (ﷺ) د پلونو په تعقیب ترلاسه کېدای شي.'),
    ('Similarly, in another verse of The Holy Qur\'an, Allah Almighty has enjoined:', 'اسی طرح قرآنِ پاک کی ایک اور آیت میں اللہ تعالیٰ نے حکم دیا ہے:', 'همداسې د قرآن کریم په بل آیت کې الله تعالی امر کړی:'),
    ('"And whatever the Messenger gives you, take it; and whatever he forbids you, abstain (from it). And fear Allah, indeed Allah is severe in punishment." (Surah Al-Hashr; verse 7)',
     '’’اور رسول تمہیں جو کچھ دیں وہ لے لو؛ اور جس چیز سے منع کریں اس سے باز رہو۔ اور اللہ سے ڈرو، بے شک اللہ سخت سزا دینے والا ہے۔‘‘ (سورۂ الحشر؛ آیت 7)',
     '"او رسول چې تاسو ته څه درکوي هغه واخلئ؛ او له څه چې مو منع کوي، له هغه ډډه وکړئ. او له الله ووېرېږئ، بې‌شکه الله سخت سزا ورکوونکی دی." (سورة الحشر؛ آیت 7)'),
    ('It has been made binding upon all to obey the beloved Rasool (ﷺ) in their lives. Since complete obedience is impossible without having a thorough knowledge of Seerat e Tayyeba, hence, it becomes mandatory for the Muslim youth to acquaint themselves with the Seerat e Tayyeba. The youth, being the backbone of the body of Ummah, must follow the teachings of the beloved Rasool (ﷺ) in letter and spirit to attain purity in their character.',
     'سب پر لازم کر دیا گیا ہے کہ وہ اپنی زندگیوں میں پیارے رسول (ﷺ) کی اطاعت کریں۔ چونکہ سیرتِ طیبہ کے مکمل علم کے بغیر کامل اطاعت ناممکن ہے، اس لیے مسلم نوجوانوں کے لیے لازم ہو جاتا ہے کہ وہ سیرتِ طیبہ سے واقفیت حاصل کریں۔ نوجوان امت کے جسم کی ریڑھ کی ہڈی ہونے کے ناطے اپنے کردار میں پاکیزگی حاصل کرنے کے لیے پیارے رسول (ﷺ) کی تعلیمات پر لفظاً و معناً عمل کریں۔',
     'پر ټولو لازمي شوې چې په خپل ژوند کې د خوږ رسول (ﷺ) اطاعت وکړي. څرنګه چې د سیرت طیبه له بشپړې پوهې پرته بشپړ اطاعت ناشونی دی، نو مسلمانو ځوانانو ته لازمه ده چې ځانونه له سیرت طیبه سره اشنا کړي. ځوانان د امت د بدن د ملا تیر په توګه باید په خپل شخصیت کې د پاکوالي د ترلاسه کولو لپاره د خوږ رسول (ﷺ) پر لارښوونو په لفظ او روح عمل وکړي.'),
]: r.p(*x)
r.h('References:', 'حوالہ جات:', 'سرچینې:')
r.group('lines', [('The spirit of Islam,', 'دی اسپرٹ آف اسلام (The spirit of Islam)،', 'د اسلام روح (The spirit of Islam)،'),
                  ("Qur'an ul Karim , translation by Justice(R) Mufti Taqi Usmani", 'قرآن الکریم، ترجمہ از جسٹس (ر) مفتی تقی عثمانی', 'قرآن الکریم، ژباړه د جسټس (متقاعد) مفتي تقي عثماني')])
rd = BOOK.record(r, 'eng12-u01-text-b', 'Reading text (2) and references', 'متن (2) اور حوالہ جات', 'متن (2) او سرچینې', 8, [3, 4])
rd['sourceCoverIllustrationReview'] = 'Photograph of the Black Stone (Hajr-e-Aswad) beside the text is decorative; not reproduced.'

GL = [
    ('accession (n)', 'attaining access to a new office or position.', 'کسی نئے عہدے یا منصب تک رسائی حاصل کرنا۔', 'نوې دندې یا مقام ته رسېدل.'),
    ('adherence(n)', 'attachment to a cause or religion.', 'کسی مقصد یا مذہب سے وابستگی۔', 'له یوه هدف یا دین سره تړاو.'),
    ('apostle (n)', 'prophet', 'پیغمبر', 'پیغمبر'),
    ('austerity(n)', 'the habit of living without sufficient money or goods.', 'کافی پیسے یا سامان کے بغیر رہنے کی عادت۔', 'له کافي پیسو یا توکو پرته د ژوند کولو عادت.'),
    ('avenge(v)', 'take revenge', 'بدلہ لینا', 'غچ اخیستل'),
    ('beacon(n)', 'a tower with a light that gives warning to passing ships ; source of guidance.', 'روشنی والا مینار جو گزرنے والے جہازوں کو خبردار کرتا ہے؛ رہنمائی کا ذریعہ۔', 'د رڼا لرونکی برج چې تېرېدونکو بېړیو ته خبرداری ورکوي؛ د لارښوونې سرچینه.'),
    ('chastity(n)', 'virtue.', 'پاکدامنی۔', 'پاکلمني.'),
    ('clan(n)', 'tribe.', 'قبیلہ۔', 'قبیله.'),
    ('dynamic(adj)', 'active.', 'متحرک۔', 'فعال.'),
]
g = Builder()
g.h('Glossary', 'فرہنگ', 'وییپانګه')
g.table('eng12-u01-gloss-a', ['Word', 'Meaning'], [[w, m] for w, m, _, _ in GL], ['لفظ', 'معنی'], ['کلمه', 'مانا'], [[w, u] for w, _, u, _ in GL], [[w, p] for w, _, _, p in GL])
gl = BOOK.record(g, 'eng12-u01-glossary-a', 'Glossary (1)', 'فرہنگ (1)', 'وییپانګه (1)', 8, [4])
issues = [{'id': 'eng12-p3-4-spellings', 'unit': 1, 'printedPage': 4, 'description': 'Printed spellings retained: “Half-ul-Fuzul” (Hilf-ul-Fudul), “Al-Hajr-ul-Aswad”, “Seerat e Tayyeba” (title spelling “Tayyiba”), “little page” (young servant). Glossary meanings are given in English as printed; Urdu/Pashto views give the meaning translated.'}]

if __name__ == '__main__':
    BOOK.save(8, [(1, rd), (1, gl)], issues=issues)
