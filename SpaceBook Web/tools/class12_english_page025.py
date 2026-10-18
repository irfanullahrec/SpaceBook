"""PDF25 (printed 37–38): Unit 4 Glossary (chassis … vibrant); Reading Comprehension Q1–7."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
GL = [
    ('chassis(n)', 'the frame that a vehicle is built on', 'وہ ڈھانچہ جس پر گاڑی بنائی جاتی ہے', 'هغه چوکاټ چې موټر پرې جوړېږي'),
    ('dangling(adj.)', 'to hang or move freely; to hold something so that it hangs or moves freely', 'آزادانہ لٹکنا یا ہلنا؛ کسی چیز کو اس طرح پکڑنا کہ وہ لٹکے یا آزادی سے ہلے', 'په ازاده توګه ځوړند کېدل یا خوځېدل؛ یو شی داسې نیول چې ځوړند وي یا ازاد وخوځي'),
    ('deck(v)', 'to decorate somebody/something with something', 'کسی کو/کسی چیز کو کسی چیز سے سجانا', 'څوک/یو شی په یو شي ښکلی کول'),
    ('emblem(n)', 'a design or picture that represents a country or an organization', 'نقش یا تصویر جو کسی ملک یا ادارے کی نمائندگی کرے', 'نقش یا انځور چې د یوه هېواد یا سازمان استازیتوب کوي'),
    ('embodiment(n)', 'a person or thing that represents or is a typical example of an idea or a quality', 'وہ شخص یا چیز جو کسی خیال یا خوبی کی نمائندگی کرے یا اس کی نمایاں مثال ہو', 'هغه کس یا شی چې د یوه نظر یا ځانګړنې استازیتوب کوي یا یې عادي بېلګه وي'),
    ('fancier(n)', 'a person who has a special interest in something, especially somebody who keeps a particular type of bird or animal', 'وہ شخص جسے کسی چیز میں خاص دلچسپی ہو، خاص طور پر جو کسی خاص قسم کا پرندہ یا جانور پالے', 'هغه کس چې په یو شي کې ځانګړې علاقه لري، په ځانګړي ډول څوک چې یو ځانګړی ډول مرغه یا حیوان ساتي'),
    ('fresco(n)', 'a picture that is painted on a wall while the plaster is still wet; the method of painting in this way', 'دیوار پر پلستر گیلا ہوتے ہوئے بنائی گئی تصویر؛ اس طرح مصوری کا طریقہ', 'هغه انځور چې پر دېوال د پلستر د لوندوالي پر مهال جوړېږي؛ په دې ډول د انځورګرۍ طریقه'),
    ('fringe(n)', "the front part of somebody's hair that is cut so that it hangs over their forehead", 'کسی کے بالوں کا اگلا حصہ جو اس طرح کٹا ہو کہ پیشانی پر لٹکے', 'د یو چا د وېښتو مخکینۍ برخه چې داسې پرې شوې وي چې پر تندي ځوړنده وي'),
    ('from stem-to-stern(idiom)', 'all the way from the front of a ship to the back', 'جہاز کے اگلے حصے سے پچھلے حصے تک پوری طرح', 'د بېړۍ له مخکینۍ برخې تر شا پورې په بشپړ ډول'),
    ('guild(n)', 'an organization of people who do the same job or who have the same interests or aims', 'ایک ہی کام کرنے والے یا یکساں مفادات یا مقاصد رکھنے والے لوگوں کی تنظیم', 'د هغو خلکو سازمان چې یو کار کوي یا یو شان ګټې یا موخې لري'),
    ('inlays(n)', 'to decorate the surface of something by putting pieces of wood or metal into it in such a way that the surface remains smooth', 'کسی چیز کی سطح میں لکڑی یا دھات کے ٹکڑے اس طرح جڑ کر سجانا کہ سطح ہموار رہے', 'د یو شي سطح د لرګي یا فلز د ټوټو په ننه ایښودو داسې ښکلې کول چې سطح هواره پاتې شي'),
    ('in-residence(n)', 'Committed to live and work in a certain place, often for a specific length of time.', 'کسی خاص جگہ پر، اکثر ایک مخصوص مدت کے لیے، رہنے اور کام کرنے کا پابند۔', 'په یوه ټاکلي ځای کې، اکثرا د یوې ټاکلې مودې لپاره، د اوسېدو او کار کولو ژمن.'),
    ('jostle(v)', 'to push roughly against somebody in a crowd', 'ہجوم میں کسی کو سختی سے دھکیلنا', 'په ګڼه ګوڼه کې څوک په زور ټېل وهل'),
    ('kaleidoscope(n)', 'a toy consisting of a tube that you look through with loose pieces of coloured glass and mirrors at the end. When the tube is turned, the pieces of glass move and form different patterns', 'ایک کھلونا جو ایک نلکی پر مشتمل ہوتا ہے جس میں سے آپ دیکھتے ہیں اور اس کے سرے پر رنگین شیشے کے ڈھیلے ٹکڑے اور آئینے ہوتے ہیں۔ جب نلکی گھمائی جاتی ہے تو شیشے کے ٹکڑے ہل کر مختلف نقش بناتے ہیں', 'یوه لوبونه چې له یوه نل جوړه وي چې تاسو پکې ګورئ او په پای کې یې د رنګه ښیښې خلاصې ټوټې او هندارې وي. کله چې نل وګرځول شي، د ښیښې ټوټې خوځېږي او بېلابېل نقشونه جوړوي'),
    ('long-haul(n)', 'involving the transport of goods or passengers over long distances', 'طویل فاصلوں پر سامان یا مسافروں کی نقل و حمل سے متعلق', 'په اوږدو واټنونو د توکو یا مسافرو له لېږد سره تړلی'),
    ('magnate(n)', 'a person who is rich, powerful and successful, especially in business', 'امیر، طاقتور اور کامیاب شخص، خاص طور پر کاروبار میں', 'شتمن، ځواکمن او بریالی کس، په ځانګړي ډول په سوداګرۍ کې'),
    ('medieval(adj.)', 'connected with the Middle Ages (about AD 1000 to AD 1450)', 'قرونِ وسطیٰ (تقریباً 1000ء سے 1450ء) سے متعلق', 'له منځنیو پېړیو (شاوخوا 1000 تر 1450 ز) سره تړلی'),
    ('motif(n)', 'a design or a pattern used as a decoration', 'سجاوٹ کے طور پر استعمال ہونے والا نقش یا نمونہ', 'د ښکلا په توګه کارېدونکی نقش یا بڼه'),
    ('mural(n)', '(of a painting) large and done on a wall, sometimes on an outside wall of a building', '(تصویر) بڑی اور دیوار پر بنی ہوئی، کبھی کبھی عمارت کی بیرونی دیوار پر', '(انځور) لوی او پر دېوال جوړ شوی، کله کله د ودانۍ پر بهرني دېوال'),
    ('nostalgic(adj.)', 'having or bringing a sad feeling mixed with pleasure when you think of happy times in the past', 'ماضی کے خوشگوار وقت کو یاد کرتے ہوئے خوشی سے ملا اداسی کا احساس رکھنا یا لانا', 'د تېرو خوښو وختونو د یادولو پر مهال له خوښۍ سره ګډ د خپګان احساس لرل یا راوستل'),
    ('painstaking(adj.)', 'done with a lot of care, effort and attention to detail', 'بہت احتیاط، محنت اور تفصیل پر توجہ کے ساتھ کیا گیا', 'په ډېر پام، هڅې او جزییاتو ته د پاملرنې سره ترسره شوی'),
    ('propane(n)', 'a flammable hydrocarbon gas of the alkane series, present in natural gas and used as bottled fuel.', 'الکین سلسلے کی آتش گیر ہائیڈروکاربن گیس جو قدرتی گیس میں پائی جاتی ہے اور بوتل بند ایندھن کے طور پر استعمال ہوتی ہے۔', 'د الکېن لړۍ اور اخیستونکی هایډروکاربن ګاز چې په طبیعي ګاز کې موندل کېږي او د بوتل شوي سون توکي په توګه کارول کېږي.'),
    ('reckon(v)', 'think something or have an opinion about something', 'کچھ سوچنا یا کسی چیز کے بارے میں رائے رکھنا', 'یو څه فکر کول یا د یو شي په اړه نظر لرل'),
    ('spiff up(v)', 'to make yourself/somebody/something look neat and attractive', 'خود کو/کسی کو/کسی چیز کو صاف ستھرا اور دلکش بنانا', 'ځان/څوک/یو شی پاک او زړه‌راښکونکی ښکاره کول'),
    ('supplant(v)', 'to take the place of somebody/something (especially somebody/something older or less modern)', 'کسی کی/کسی چیز کی جگہ لینا (خاص طور پر کسی پرانے یا کم جدید کی)', 'د یو چا/یو شي ځای نیول (په ځانګړي ډول د زاړه یا لږ عصري)'),
    ('talent scout(n)', 'someone who looks for people who have the skills they want, especially in entertainment or sport', 'وہ شخص جو مطلوبہ مہارتوں والے لوگوں کو تلاش کرتا ہے، خاص طور پر تفریح یا کھیل میں', 'هغه کس چې د غوښتل شویو مهارتونو لرونکي خلک لټوي، په ځانګړي ډول په ساتېري یا ورزش کې'),
    ('upholsterer(n)', 'A person who covers a chair, etc. with soft material (= padding) and cloth or leather', 'وہ شخص جو کرسی وغیرہ کو نرم مواد (گدی) اور کپڑے یا چمڑے سے ڈھانپتا ہے', 'هغه کس چې څوکۍ او نور په نرمو موادو (ګدۍ) او ټوکر یا څرمن پوښي'),
    ('vibrant(adj.)', 'full of life and energy', 'زندگی اور توانائی سے بھرپور', 'له ژوند او انرژۍ ډک'),
]
g = Builder()
gloss(g, 'eng12-u04-gloss-b', GL)
gl = BOOK.record(g, 'eng12-u04-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 25, [37, 38])
q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.h('Answer the following Questions:', 'درج ذیل سوالات کے جواب دیں:', 'لاندې پوښتنو ته ځواب ورکړئ:')
q.group('lines', [
    ('1. Explain the connection which the writer makes between the camel caravans of past and modern decoration of trucks.', '1. ماضی کے اونٹوں کے قافلوں اور ٹرکوں کی جدید سجاوٹ کے درمیان مصنفہ کے بیان کردہ تعلق کی وضاحت کریں۔', '1. د پخوانیو اوښانو د کاروانونو او د ټرکونو د عصري ښکلا ترمنځ هغه اړیکه تشریح کړئ چې لیکوالې جوړه کړې.'),
    ('2. Which point is the writer illustrating when she gives examples of the decorations on trucks from Peshawar and Rawalpindi?', '2. پشاور اور راولپنڈی کے ٹرکوں کی سجاوٹ کی مثالیں دیتے ہوئے مصنفہ کون سا نکتہ واضح کر رہی ہیں؟', '2. لیکواله د پېښور او راولپنډۍ د ټرکونو د ښکلا د بېلګو په ورکولو کوم ټکی روښانه کوي؟'),
    ('3. Which point is the writer illustrating in the lesson "Truck Art" by giving examples of the specialists\' work?', '3. سبق ’’ٹرک آرٹ‘‘ میں ماہرین کے کام کی مثالیں دے کر مصنفہ کون سا نکتہ واضح کر رہی ہیں؟', '3. لیکواله په "د ټرک هنر" لوست کې د متخصصینو د کار د بېلګو په ورکولو کوم ټکی روښانه کوي؟'),
    ('4. Why do truckers spend so much money on decorating their trucks?', '4. ٹرک والے اپنے ٹرکوں کی سجاوٹ پر اتنا پیسہ کیوں خرچ کرتے ہیں؟', '4. ټرکوال ولې د خپلو ټرکونو پر ښکلا دومره پیسې لګوي؟'),
    ('5. Briefly describe how truck art developed from the 1940s to the 1970s?', '5. مختصراً بیان کریں کہ 1940 سے 1970 کی دہائی تک ٹرک آرٹ کیسے پروان چڑھا؟', '5. په لنډه توګه بیان کړئ چې د ټرک هنر له 1940 څخه تر 1970 لسیزې څنګه وده وکړه؟'),
    ("6. Why are truck drivers 'nostalgic' about the old Bedford trucks?", '6. ٹرک ڈرائیور پرانے بیڈفورڈ ٹرکوں کے بارے میں ’’یادِ ماضی میں کھوئے‘‘ کیوں ہیں؟', '6. ټرک چلوونکي ولې د زړو بیډفورډ ټرکونو لپاره "د تېر په یاد کې ډوب" دي؟'),
    ("7. Explain how truck art at the present time can be seen as having reached 'some kind of apogee'?", '7. وضاحت کریں کہ موجودہ دور میں ٹرک آرٹ کو کس طرح ’’ایک قسم کے عروج‘‘ پر پہنچا ہوا سمجھا جا سکتا ہے؟', '7. تشریح کړئ چې په اوسني وخت کې د ټرک هنر څنګه "یو ډول لوړې څوکې" ته رسېدلی ګڼل کېدای شي؟'),
])
rc = BOOK.record(q, 'eng12-u04-comprehension-a', 'Reading Comprehension Q1–7', 'مطالعہ اور فہم سوالات 1–7', 'لوستل او پوهه پوښتنې 1–7', 25, [38])
issues = [{'id': 'eng12-p37-38', 'unit': 4, 'printedPage': 38, 'description': 'Right edge of printed p38 slightly clipped (“camel caravans of [the] past”, “giving examples”, “‘some kind of apogee’”); text completed from context. Glossary word classes transcribed as printed (e.g. “in-residence(n)”, “inlays(n)” defined as a verb).'}]

if __name__ == '__main__':
    BOOK.save(25, [(4, gl), (4, rc)], issues=issues)
