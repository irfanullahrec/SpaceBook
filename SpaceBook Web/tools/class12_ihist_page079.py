"""Islamic History XII PDF79: p.150 — exercise of lessons 29–30; p.151 — Lesson 31 Amir Abd al-Rahman al-Dakhil (start). Run: python class12_ihist_page079.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L

YN = (' (yes/no)', ' (ہاں/نہیں)', ' (هو/نه)')


def yn(items):
    return [(e + YN[0], u + YN[1], p + YN[2]) for e, u, p in items]


def p79():
    b = Builder()
    b.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    L(b, [('1. State the achievements of Abd al-Aziz bin Musa.', '۱۔ عبدالعزیز بن موسیٰ کے کارنامے بیان کریں', '۱. د عبدالعزیز بن موسی کارنامې بیان کړئ.'),
          ('2. Write the famous events of the era of Abd al-Aziz bin Musa.', '۲۔ عبدالعزیز بن موسیٰ کے دور کے مشہور واقعات تحریر کریں۔', '۲. د عبدالعزیز بن موسی د دورې مشهورې پېښې ولیکئ.')])
    b.p('3. Answer in yes/no.', '۳۔ ہاں/نہیں میں جواب دیں۔', '۳. په هو/نه کې ځواب ورکړئ.')
    L(b, yn([('a. The Romans remained in power until the 5th century.', 'الف: رومن ۵ صدی تک برسرِ اقتدار رہے۔', 'الف. رومیان تر پنځمې پېړۍ واک کې وو.'),
             ('b. The name of Count Julian\'s daughter was Florinda.', 'ب: کاؤنٹ جولین کی بیٹی کا نام فلورنڈا تھا۔', 'ب. د کاونټ جولین د لور نوم فلورنډا و.'),
             ('c. Musa bin Nusayr appointed his son Abd al-Aziz bin Musa wali of Andalus.', 'ج: موسیٰ بن نصیر نے اپنے بیٹے عبدالعزیز بن موسیٰ کو اندلس کا والی مقرر کیا۔', 'ج. موسی بن نصیر خپل زوی عبدالعزیز بن موسی د اندلس والي وټاکه.'),
             ('d. After Walid bin Abd al-Malik, Sulayman bin Abd al-Malik ascended the throne.', 'د: ولید بن عبدالملک کے بعد سلیمان بن عبدالملک تخت نشین ہوا۔', 'د. له ولید بن عبدالملک وروسته سلیمان بن عبدالملک پر تخت کېناست.'),
             ('e. Abd al-Aziz had married Roderick\'s widow Queen Egilona.', 'ہ: عبدالعزیز نے راڈرک کی بیوہ ملکہ ایجولونہ سے شادی کر لی تھی۔', 'ه. عبدالعزیز د راډرک له کونډې ملکې اېجیلونا سره واده کړی و.'),
             ('f. In place of Seville, Cordoba was made the capital.', 'و: اشبیلیہ کی جگہ قرطبہ دارالخلافہ بنایا گیا۔', 'و. د اشبیلیې پر ځای قرطبه پلازمېنه شوه.'),
             ('g. Pelayo\'s sultanate was 5 miles long and 3 miles wide.', 'ز: پلائیو کی سلطنت ۵ میل لمبی اور ۳ میل چوڑی تھی۔', 'ز. د پلایو سلطنت ۵ میله اوږد او ۳ میله پلن و.'),
             ('h. The Duke of Aquitaine united the small states against the Muslims.', 'ح: ڈیوک آف ایکوٹین نے چھوٹی چھوٹی ریاستوں کو مسلمانوں کے خلاف متحد کیا۔', 'ح. د اکویټین ډیوک کوچني دولتونه د مسلمانانو پر خلاف متحد کړل.'),
             ('i. Fihri was an aged elder.', 'ط: فہری ایک عمر رسیدہ بزرگ تھے۔', 'ط. فهري یو زوړ مشر و.'),
             ('j. Military cantonments were made along the river Rhône.', 'ی: دریائے رون کے ساتھ ساتھ فوجی چھاؤنیاں بنائی گئیں۔', 'ی. د رون سیند په اوږدو کې پوځي چاوڼۍ جوړې شوې.')]))
    r1 = rec(b, 30, 150, 79, [150], kind='exercise')
    t = Builder()
    t.p('Chapter: 3', 'باب: 3', 'باب: ۳')
    t.h('Amir Abd al-Rahman al-Dakhil', 'امیر عبدالرحمان الداخل', 'امیر عبدالرحمن الداخل')
    t.p('138 AH to 172 AH, corresponding to 756 CE to 788 CE', '۱۳۸ھ تا ۱۷۲ھ بمطابق ۷۵۶ء تا ۷۸۸ء', '۱۳۸ هـ تر ۱۷۲ هـ، له ۷۵۶ع تر ۷۸۸ع سره سم')
    S(t, [(None, ('When the sun of the power of the Banu Abbas shone and the dew of the Banu Umayyah began to disappear, doomsday fell upon the members of the Banu Umayyah. The supporters of the Banu Abbas began to search out and kill the members of the Banu Umayyah. Among those who, escaping this bloodshed, went to other countries was also Abd al-Rahman bin Mu\'awiyah bin Hisham bin Abd al-Malik. He turned towards Africa. His slave Badr too was with him. The governor of Africa, Abd al-Rahman bin Habib, too had turned against him; therefore he kept taking refuge, going out of one tribe into another tribe. In this way five years passed. After this he stayed in Maliba. According to Ibn Khaldun he sent his slave Badr to those people in Andalus who were sympathisers of the Marwanids. Badr fulfilled his duty in the best manner. He made all of them ready to support Abd al-Rahman. All the people promised with great joy to help Abd al-Rahman. The struggle of the Yamani and Mudari tribes had been continuing for a considerable time. Both tribes were trying to humble each other. The Yamani tribes made a full commitment to support Abd al-Rahman. When Badr became fully certain, he came back to Abd al-Rahman and informed him of all the circumstances. Abd al-Rahman set off in 138 AH. First of all a group of the people of Seville swore allegiance at the hand of Abd al-Rahman. The wali of Sidonia, \'Attab, …', 'جب بنو عباس کے اقتدار کا سورج چمکا اور بنو امیہ کی شبنم غائب ہونے لگی تو بنو امیہ کے افراد پر قیامت ٹوٹی۔ بنو عباس کے حامیوں نے بنو امیہ کے افراد کو ڈھونڈ ڈھونڈ کر قتل کرنا شروع کیا۔ اس خون ریزی سے جو لوگ بچ کر دوسرے ممالک میں چلے گئے ان میں عبدالرحمان بن معاویہ بن ہشام بن عبدالملک بھی تھا۔ اس نے افریقہ کا رخ کیا۔ اس کا غلام بدر بھی اس کے ہمراہ تھا۔ افریقہ کا گورنر عبدالرحمان بن حبیب بھی اس کے خلاف ہو گیا تھا۔ اس لئے وہ ایک قبیلہ سے نکل کر دوسرے قبیلے میں پناہ گزین ہوتا رہا۔ اس طرح پانچ سال گزر گئے۔ اس کے بعد ملیلہ میں قیام کیا۔ بقول ابن خلدون اس نے اپنے غلام بدر کو اندلس میں ان لوگوں کے پاس بھیجا جو مروانیوں کے ہمنوا تھے۔ بدر نے اپنا فرض بہترین طریقے سے پورا کیا۔ ان سب کو عبدالرحمان کا ساتھ دینے پر آمادہ کیا۔ سب لوگوں نے بڑی خوشی کے ساتھ عبدالرحمان کی مدد کرنے کا وعدہ کیا۔ یمنی اور مضری قبائل کی کشمکش کافی عرصے سے جاری تھی۔ دونوں قبائل ایک دوسرے کو نیچا دکھانے کی کوشش کر رہے تھے۔ یمنی قبائل نے عبدالرحمان کا ساتھ دینے کا بھرپور اقرار کیا۔ بدر کو جب مکمل یقین ہو گیا تو وہ واپس عبدالرحمان کے پاس آیا اور اُسے تمام حالات سے آگاہ کیا۔ عبدالرحمان ۱۳۸ھ میں روانہ ہوا۔ سب سے پہلے اہلِ اشبیلیہ کے ایک گروہ نے عبدالرحمان کے ہاتھ پر بیعت کی۔ سیدونہ کے والی عتاب نے', 'کله چې د بنو عباس د واک لمر وځلېد او د بنو امیه پرخه ورکېدل پیل شوه، پر بنو امیه وو قیامت راغی؛ د بنو عباس ملاتړو د بنو امیه غړي لټول او وژل پیل کړل. هغه کسان چې له دې وینې توییدو وژغورل شول او نورو هېوادونو ته لاړل، په هغوی کې عبدالرحمن بن معاویه بن هشام بن عبدالملک هم و؛ هغه افریقا ته مخه کړه؛ غلام یې بدر هم ورسره و. د افریقا والي عبدالرحمن بن حبیب هم د هغه مخالف شوی و؛ نو له یوې قبیلې به وتلو او بلې قبیلې ته به یې پناه وړه؛ په دې ډول پنځه کاله تېر شول. له دې وروسته یې په ملیله کې استوګنه وکړه. د ابن خلدون په وینا خپل غلام بدر یې په اندلس کې هغو خلکو ته ولېږه چې د مروانیانو همغږي وو؛ بدر خپله دنده په ښه توګه سرته ورسوله او ټول یې د عبدالرحمن ملاتړ ته چمتو کړل؛ ټولو خلکو په ډېره خوښۍ د عبدالرحمن د مرستې ژمنه وکړه. د یمني او مضري قبیلو کشمکش ډېره موده روان و؛ دواړو هڅه کوله چې یو بل ټیټ کړي؛ یمني قبیلو د عبدالرحمن د ملاتړ بشپړه ژمنه وکړه. کله چې بدر ته بشپړ ډاډ راغی، بېرته عبدالرحمن ته راغی او له ټولو حالاتو یې خبر کړ. عبدالرحمن په ۱۳۸ هـ کې روان شو؛ تر ټولو لومړی د اشبیلیې یوې ډلې د عبدالرحمن پر لاس بیعت وکړ. د سیدونې والي عتاب …'))])
    BOOK.save(79, [(30, r1), (31, rec(t, 31, 151, 79, [151], first=True))], complete_units=[30], issues=[{'id': 'ihist12-pdf079', 'unit': 30, 'printedPage': 150,
               'description': 'Exercise on p.150 covers lessons 28–30 as printed (item a, b refer to lesson 28). Student ticks on every (ہاں/نہیں) excluded; no printed key. Lesson 31 opens on p.151 under "باب: 3". Printed "ملیلہ" kept.'}])


if __name__ == '__main__':
    p79()
