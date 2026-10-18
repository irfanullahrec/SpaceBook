"""Urdu XII PDF121 (spread): p.232 Ghazal 13 author note (شکیب جلالی, 1934–1966); p.233 Ghazal 13 full text (public domain)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Shakeeb Jalali', 'شکیبؔ جلالی', 'شکیب جلالي')
a.p('Born: 1934 · Died: 1966', 'ولادت: ۱۹۳۴ء · وفات: ۱۹۶۶ء', 'زېږېدنه: ۱۹۳۴ز · مړینه: ۱۹۶۶ز')
for x in [
    ("Syed Hasan Rizvi Shakeeb Jalali was born in the town of Jalali, district Aligarh. He received his early education in Badayun. Shakeeb Jalali's economic condition was poor from the beginning; because of his father's illness the responsibility of the whole household fell on him. After the creation of Pakistan he came to Pakistan and did his B.A. from Lahore. At first he worked in the offices of magazines, then joined the Education Department. His whole life passed in anguish, sorrow and bitterness. He was often ill and in the end had developed several mental and psychological ailments. He left this world at the age of only 32.",
     'سید حسن رضوی شکیبؔ جلالی قصبہ جلالی، ضلع علی گڑھ میں پیدا ہوئے۔ انھوں نے ابتدائی تعلیم بدایوں میں حاصل کی۔ شکیبؔ جلالی کی معاشی حالت شروع سے ہی خراب تھی۔ والد کی بیماری کے باعث سارے گھر کی ذمہ داری اُن پر آن پڑی۔ قیامِ پاکستان کے بعد وہ پاکستان چلے آئے اور لاہور سے بی۔اے کیا۔ ابتدا میں رسائل کے دفاتر میں ملازمت کی پھر محکمہ تعلیم میں ملازم ہو گئے۔ ان کی تمام زندگی کرب و ملال اور تلخیوں میں گزری۔ وہ اکثر بیمار رہا کرتے تھے اور آخر میں کئی ذہنی و نفسیاتی امراض کا شکار ہو گئے تھے۔ وہ صرف ۳۲ برس کی عمر میں اس دنیا سے رخصت ہو گئے۔',
     'سید حسن رضوي شکیب جلالي د علیګړ ولسوالۍ د جلالي په کلي کې زېږېدلی. لومړنۍ زده‌کړې یې په بدایون کې وکړې. د شکیب جلالي اقتصادي حال له پیله خراب و؛ د پلار د ناروغۍ له امله د ټول کور مسؤولیت پر ده راولوېد. د پاکستان له جوړېدو وروسته پاکستان ته راغی او له لاهوره یې بي.اې وکړ. په پیل کې یې د مجلو په دفترونو کې کار وکړ، بیا د ښوونې په څانګه کې ګومارل شو. ټول ژوند یې په درد، خپګان او ترخو کې تېر شو. ډېری وخت ناروغ و او په پای کې په ګڼو ذهني او رواني ناروغیو اخته شو. یوازې په ۳۲ کلنۍ کې له دې نړۍ ولاړ.'),
    ("Shakeeb Jalali's collection “Roshni Ae Roshni” very soon became popular and most of its verses came onto the lips of high and low. He began his poetry at a time when the Urdu ghazal was passing through new possibilities and experiments; mental and intellectual attitudes were changing. In that age poets were valued who showed contemporary awareness together with novelty in experience and observation. Because of modern tendencies Shakeeb Jalali very soon became distinguished. He is considered a poet of easy language, yet even in those easy words there is depth of meaning. Shakeeb Jalali also wrote a few poems, but his real skill lies in the field of the ghazal.",
     'شکیبؔ جلالی کا مجموعۂ کلام ’’روشنی اے روشنی‘‘ بہت جلد مقبول ہوا اور اس کے اکثر اشعار زبان زدِ خاص و عام ہو گئے۔ انھوں نے اپنی شاعری کا آغاز اس وقت کیا جب اردو غزل نئے امکانات اور تجربات سے گزر رہی تھی۔ ذہنی اور فکری رویّوں میں تبدیلی آ رہی تھی۔ اُس دور میں ایسے شعرا قابلِ قدر جانے جاتے تھے جن کے ہاں عصری شعور کے ساتھ ساتھ تجربات اور مشاہدات میں بھی جدّت نظر آئے۔ جدید رجحانات کے باعث شکیبؔ جلالی بہت جلد ممتاز ہو گئے۔ وہ آسان زبان کے شاعر سمجھے جاتے ہیں لیکن ان آسان الفاظ میں بھی معنوی تہہ داری موجود ہے۔ شکیبؔ جلالی نے چند ایک نظمیں بھی کہی ہیں لیکن اُن کی اصل مہارت غزل کے میدان میں ہے۔',
     'د شکیب جلالي د کلام ټولګه "روښنايي اې روښنايي" ډېر ژر مشهوره شوه او ډېری بیتونه یې د خاصو او عامو پر ژبو شول. هغه خپله شاعري هغه وخت پیل کړه چې اردو غزل د نویو امکاناتو او تجربو له لارې تېرېده؛ ذهني او فکري چلندونه بدلېدل. په هغه دور کې هغه شاعران د قدر وړ ګڼل کېدل چې له عصري شعور سره یې په تجربو او لیدنو کې هم نوښت ښکارېده. د نویو تمایلاتو له امله شکیب جلالي ډېر ژر ممتاز شو. هغه د اسانې ژبې شاعر ګڼل کېږي، خو په دې اسانو کلمو کې هم معنوي ژوروالی شته. شکیب جلالي یو څو نظمونه هم ویلي، خو اصلي مهارت یې د غزل په ډګر کې دی.'),
    ('Collection of poetry: Roshni Ae Roshni.', 'مجموعۂ کلام: روشنی اے روشنی۔', 'د کلام ټولګه: روښنايي اې روښنايي.'),
]: a.p(*x)
UT = ('Ghazal: Two or four stones did come and fall into my courtyard', 'غزل: آ کے پتھر تو مرے صحن میں دو چار گرے', 'غزل: دوه څلور ډبرې خو زما انګړ ته راغلې او ولوېدې', 'شکیبؔ جلالی')
au = BOOK.record(a, 'urdu12-u30-author', 'About the poet: Shakeeb Jalali', 'شکیبؔ جلالی (تعارف)', 'شکیب جلالي (پېژندنه)', 121, [232], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Shakeeb Jalali and floral border are decorative; not reproduced.'

t = Builder()
t.h('Ghazal — Shakeeb Jalali', 'غزل — شکیبؔ جلالی', 'غزل — شکیب جلالي')
SH = [
 [('Two or four stones did come and fall into my courtyard;', 'آ کے پتھر تو مرے صحن میں دو چار گرے', 'دوه څلور ډبرې خو زما انګړ ته راغلې او ولوېدې؛'),
  ('all the fruits that tree bore fell behind the wall.', 'جتنے اُس پیڑ کے پھل تھے، پسِ دیوار گرے', 'د هغې ونې څومره مېوې چې وې، د دیوال شا ته ولوېدې.')],
 [('If I must fall, then I shall fall at my own feet,', 'مجھے گرنا ہے تو میں، اپنے ہی قدموں میں گروں', 'که باید ولوېږم، نو زه به په خپلو پښو کې ولوېږم،'),
  ('just as the shadow of a wall falls upon the wall.', 'جس طرح سایۂ دیوار پہ دیوار گرے', 'لکه څنګه چې د دیوال سیوری پر دیوال لوېږي.')],
 [('They left darkness in the heart — the letters of light;', 'تیرگی چھوڑ گئے دل میں، اُجالے کے خطوط', 'په زړه کې یې تیاره پرېښوده — د رڼا کرښې؛'),
  ('these stars broke and fell uselessly on my house.', 'یہ ستارے مرے گھر ٹوٹ کے، بے کار گرے', 'دا ستوري زما پر کور مات شول او بې‌ګټې ولوېدل.')],
 [('Seeing my own door and roof, I tremble', 'دیکھ کر اپنے در و بام، لرز جاتا ہوں', 'خپلې دروازې او بام ته په کتو لړزم،'),
  ('whenever a wall falls in my neighbourhood.', 'مرے ہمسائے میں جب بھی کوئی دیوار گرے', 'هرکله چې زما په ګاونډ کې کوم دیوال ولوېږي.')],
 [('God knows where the thread of time will break —', 'وقت کی ڈور خدا جانے کہاں سے ٹوٹے', 'خدای خبر د وخت تار به له کومه ځایه وشلېږي —'),
  ('at what hour this hanging sword will fall on the head.', 'کس گھڑی سر پہ یہ لٹکی ہوئی تلوار گرے', 'په کومه شېبه به دا ځوړنده توره پر سر راولوېږي.')],
 [('Why do you gaze at such a height, Shakeeb?', 'دیکھتے کیوں ہو شکیبؔ اتنی بلندی کی طرف', 'شکیبه! ولې دومره لوړوالي ته ګورې؟'),
  ('Do not raise your head so, lest this turban fall.', 'نہ اُٹھایا کرو سر کو کہ یہ دستار گرے', 'سر مه پورته کوه، چې دا پګړۍ ونه لوېږي.')],
]
for sh in SH:
    t.group('lines', sh)
t.p('(Roshni Ae Roshni)', '(روشنی اے روشنی)', '(روښنايي اې روښنايي)')
po = BOOK.record(t, 'urdu12-u30-ghazal', 'Ghazal text', 'متنِ غزل', 'د غزل متن', 121, [233])
issues = [{'id': 'urdu12-pdf121', 'unit': 30, 'printedPage': 233, 'description': 'Shakeeb Jalali died 1966 → public domain in Pakistan; Ghazal 13 transcribed in full (6 couplets).'}]

if __name__ == '__main__':
    BOOK.save(121, [(30, au), (30, po)], issues=issues)
