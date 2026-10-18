"""Islamic History XII PDF109: p.208 — Ziryab (end), Ibn Rushd, Ibn Hayyan; p.209 — exercise of lesson 39 (start). Run: python class12_ihist_page109.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L

YN = (' (yes/no)', ' (ہاں/نہیں)', ' (هو/نه)')


def yn(items):
    return [(e + YN[0], u + YN[1], p + YN[2]) for e, u, p in items]


def p109():
    b = Builder()
    S(b, [(None, ('… [astrology,] literature and poetry too he had expertise. Ziryab remembered approximately a thousand ragas and raginis. He invented instruments of music. He used glass vessels. He introduced the method of parting the hair at a slant. Many dishes too are attributed to him. He presented the concept of wearing clothes of suitable colours according to the season. According to S. P. Scott, "parting the hair at a slant, walking bare-headed, eating with knife and fork, the variety of dishes and the difference of garments, and many new things of this nation are inventions of his mind. The genealogical way of life of present Europe is derived from this very [source]." Ziryab died in 238 AH.', 'ادب اور شاعری میں بھی مہارت حاصل تھی۔ زریاب کو تقریباً ہزار راگ اور راگنیاں یاد تھیں۔ اس نے موسیقی کے آلات ایجاد کئے۔ شیشے کے برتنوں کو استعمال کیا۔ ٹیڑھی مانگ نکالنے کا طریقہ رائج کیا۔ کئی کھانے بھی آپ سے منسوب ہیں۔ موسم کے مطابق موزوں رنگوں کے کپڑے پہننے کا تصور پیش کیا۔ ایس پی سکاٹ کے مطابق ”ٹیڑھی مانگ نکالنا، ننگے سر چلنا، چھری کانٹے کے ساتھ کھانا، کھانوں کا تنوع اور ملبوسات کا اختلاف اور اس قوم کی کئی نئی چیزیں اس کے دماغ کی اختراع ہیں۔ موجودہ یورپ کا شجر ساز طریق بود و ماند اسی سے ماخوذ ہے۔“ زریاب ۲۳۸ھ میں فوت ہوا۔', '… ادب او شاعرۍ کې یې هم مهارت درلود. زریاب ته نږدې زر راګونه او راګڼۍ یاد وې؛ هغه د موسیقۍ الات ایجاد کړل؛ د ښیښې لوښي یې وکارول؛ د کږې مانګې (د ویښتو کږ چاک) طریقه یې رواج کړه؛ ډېر خواړه هم ورته منسوب دي؛ د موسم سره سم د مناسبو رنګونو جامو اغوستو تصور یې وړاندې کړ. د اېس پي سکاټ په وینا «کږه مانګه، سرلوڅ ګرځېدل، په چاړه او پنجه خوړل، د خوړو تنوع او د جامو توپیر او د دې قوم ډېر نوي شیان د هغه د ذهن اختراع دي؛ د اوسنۍ اروپا د ژوند دود له همدې اخیستل شوی.» زریاب په ۲۳۸ هـ کې مړ شو.')),
          (('12. Ibn Rushd', '۱۲۔ ابن رشد', '۱۲. ابن رشد'),
           ('Ibn Rushd belonged to a scholarly family. He was born in Cordoba in 1126 CE. In 1169 CE he was appointed qadi of Seville. In Marrakesh he was appointed court physician in place of Ibn Tufayl. Ibn Rushd had expertise in medicine and astronomy, and he explained the writings of Aristotle in an excellent manner, by which the Europe of today is very much impressed. He died in Marrakesh in 1198 CE.', 'ابن رشد کا تعلق علمی گھرانے سے تھا۔ ۱۱۲۶ء میں قرطبہ میں پیدا ہوا۔ ۱۱۶۹ء میں اشبیلہ کا قاضی مقرر ہوا۔ مراکش میں ابن طفیل کی جگہ درباری طبیب مقرر ہوا۔ ابن رشد کو طب اور فلکیات میں مہارت حاصل تھی اور اس نے ارسطو کی تصنیفات کی اعلیٰ پیرائے میں تشریح کی، جس سے آج کا یورپ بہت متاثر ہے۔ مراکش میں ۱۱۹۸ء میں فوت ہوا۔', 'ابن رشد له یوې علمي کورنۍ و؛ په ۱۱۲۶ع کې په قرطبه کې زېږېدلی؛ په ۱۱۶۹ع کې د اشبیلیې قاضي وټاکل شو؛ په مراکش کې د ابن طفیل پر ځای درباري طبیب وټاکل شو. ابن رشد په طب او فلکیاتو کې مهارت درلود او د ارسطو لیکنې یې په غوره ډول شرح کړې، چې نننۍ اروپا ترې ډېره اغېزمنه ده. هغه په ۱۱۹۸ع کې په مراکش کې مړ شو.')),
          (('13. Ibn Hayyan', '۱۳۔ ابن حیان', '۱۳. ابن حیان'),
           ('He was the son of Khalaf bin Husayn, the freed slave of Abd al-Malik bin Marwan. Ibn Hayyan is counted among the renowned historians of Andalus. On the conditions of Andalus two of his books have the status of authority. The book al-Muqtabis fi Tarikh consists of ten large volumes. The book al-Matin consists of sixty large volumes. Ibn Hayyan also had command of morphology and grammar. Ibn Hayyan was born in 987 CE and died in 1076 CE.', 'عبدالملک بن مروان کے آزاد کردہ غلام خلف بن حسین کا بیٹا تھا۔ ابن حیان کا شمار اندلس کے نامور مورخین میں ہوتا ہے۔ اندلس کے حالات پر اس کی دو کتابیں سند کی حیثیت رکھتی ہیں۔ کتاب المقتبس فی تاریخ دس بڑی جلدوں پر مشتمل ہے۔ کتاب المبین ساٹھ بڑی جلدوں پر مشتمل ہے۔ ابن حیان کو علمِ صرف اور نحو پر بھی عبور حاصل تھا۔ ابن حیان ۹۸۷ء میں پیدا ہوا اور ۱۰۷۶ء میں فوت ہوا۔', 'هغه د عبدالملک بن مروان د آزاد کړي غلام خلف بن حسین زوی و. ابن حیان د اندلس په نامتو مورخینو کې شمېرل کېږي؛ د اندلس پر حالاتو یې دوه کتابونه د سند حیثیت لري: «المقتبس في تاریخ» په لسو لویو ټوکونو کې او «المتین» (چاپ: المبین) په شپېتو لویو ټوکونو کې. ابن حیان پر صرف او نحو هم واک درلود. هغه په ۹۸۷ع کې زېږېدلی او په ۱۰۷۶ع کې مړ شو.'))])
    r1 = rec(b, 39, 208, 109, [208])
    t = Builder()
    t.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    L(t, [('1. State briefly the achievements of Yahya bin Yahya al-Laythi.', '۱۔ یحییٰ بن یحییٰ لیثی کے کارنامے مختصر طور پر بیان کریں۔', '۱. د یحیی بن یحیی لیثي کارنامې لنډې بیان کړئ.'),
          ('2. State the life of Ibn Khaldun in detail.', '۲۔ ابن خلدون کے حالاتِ زندگی تفصیلاً بیان کریں۔', '۲. د ابن خلدون د ژوند حالات په تفصیل بیان کړئ.'),
          ('3. Write the achievements of Ziryab.', '۳۔ زریاب کے کارنامے تحریر کریں۔', '۳. د زریاب کارنامې ولیکئ.'),
          ('4. Write a short note on Ibn Rushd.', '۴۔ ابن رشد پر مختصر نوٹ تحریر کریں۔', '۴. پر ابن رشد لنډ یادښت ولیکئ.')])
    t.p('5. Draw a circle around the correct answer.', '۵۔ درست جواب کے گرد دائرہ لگائیے۔', '۵. د سم ځواب شاوخوا کړۍ رسم کړئ.')
    L(t, yn([('a. Yahya bin Laythi was called the Wise Man of Andalus.', 'الف: یحییٰ بن لیثی عاقل اندلس کہلاتا تھا۔', 'الف. یحیی بن لیثي ته د اندلس عاقل ویل کېده.'),
             ('b. In the West the Maliki school obtained the support of the king because of Yahya.', 'ب: مغرب میں مالکی مذہب کو یحییٰ کی وجہ سے بادشاہ کی حمایت حاصل ہوئی۔', 'ب. په لوېدیځ کې مالکي مذهب د یحیی له امله د پاچا ملاتړ ترلاسه کړ.'),
             ('c. Qadi Mundhir bin Sa\'id al-Balluti was also a poet of high calibre.', 'ج: قاضی منذر بن سعید البلوطی اعلیٰ پایہ کے شاعر بھی تھے۔', 'ج. قاضي منذر بن سعید البلوطي لوړ پایه شاعر هم و.'),
             ('d. Qadi Muhammad Bashir was a pupil of Imam Malik.', 'د: قاضی محمد بشیر امام مالک کے شاگرد تھے۔', 'د. قاضي محمد بشیر د امام مالک شاګرد و.'),
             ('e. In al-Zahrawi\'s book there are also pictures of surgical instruments.', 'ہ: زہراوی کتاب میں آلاتِ جراحی کی تصاویر بھی ہیں۔', 'ه. د زهراوي په کتاب کې د جراحۍ د الاتو انځورونه هم شته.'),
             ('f. Abu Marwan was the matchless physician of his era.', 'و: ابومروان اپنے دور کے بے مثال طبیب تھے۔', 'و. ابو مروان د خپلې دورې بې‌ساری طبیب و.'),
             ('g. Ibn Jubayr came to Bayt al-Maqdis in the era of Salah al-Din Ayyubi.', 'ز: ابن جبیر صلاح الدین ایوبی کے دور میں بیت المقدس آیا۔', 'ز. ابن جبیر د صلاح الدین ایوبي په دوره کې بیت المقدس ته راغی.'),
             ('h. The name of al-Idrisi holds a high place in history.', 'ح: ادریسی کا نام تاریخ میں اعلیٰ مقام رکھتا ہے۔', 'ح. د ادریسي نوم په تاریخ کې لوړ مقام لري.'),
             ('i. Al-Idrisi received education from the University of Cordoba.', 'ط: ادریسی نے قرطبہ یونیورسٹی سے تعلیم حاصل کی۔', 'ط. ادریسي د قرطبې له پوهنتونه زده‌کړه وکړه.'),
             ('j. Ibn Khaldun was born in Tunis.', 'ی: ابن خلدون تونس میں پیدا ہوا۔', 'ی. ابن خلدون په تونس کې زېږېدلی.'),
             ('k. Muhammad V, ruler of Granada, gave Ibn Khaldun a splendid welcome.', 'ک: محمد خامس حاکم غرناطہ نے ابن خلدون کا شاندار استقبال کیا۔', 'ک. د غرناطې حاکم محمد پنځم د ابن خلدون ښکلی هرکلی وکړ.'),
             ('l. Ibn Khaldun was given the title of Ra\'is al-Mu\'arrikhin.', 'ل: ابن خلدون کو رئیس المورخین کا خطاب دیا گیا۔', 'ل. ابن خلدون ته د رئیس المورخین لقب ورکړل شو.')]))
    BOOK.save(109, [(39, r1), (39, rec(t, 39, 209, 109, [209], kind='exercise'))], issues=[{'id': 'ihist12-pdf109', 'unit': 39, 'printedPage': 208,
               'description': 'Printed as is: "شجر ساز طریق بود و ماند" (in the Scott quotation, d.1929), "کتاب المبین" (for المتین), "قاضی محمد بشیر". The exercise item (ل) on p.209 is partly cut at the page edge; read from the visible text. Finger in the scan excluded; no student marks on p.209; no printed key.'}])


if __name__ == '__main__':
    p109()
