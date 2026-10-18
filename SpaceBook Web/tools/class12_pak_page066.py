"""Pak Studies XII PDF66 (spread): printed pp.121–122 — Ch.6 Sindhi culture (end), Baloch culture, cultural heritage: Indus Valley, Gandhara; Moenjodaro photo (coded SVG); historic buildings; common features (begins)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h


def ruins_svg(cap):
    """Coded flat illustration standing in for the printed photograph of the Moenjodaro ruins with the stupa mound."""
    bricks = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#b5653f" stroke="#7a3d22" stroke-width="1.2"/>'
                     for x, y, w, h in [(20, 170, 110, 55), (140, 182, 90, 43), (240, 160, 120, 65), (370, 176, 100, 49), (60, 140, 70, 30), (260, 128, 70, 32)])
    courses = ''.join(f'<line x1="20" y1="{y}" x2="470" y2="{y}" stroke="#7a3d22" stroke-width="0.6" opacity="0.5"/>' for y in range(185, 226, 10))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 270" role="img" aria-label="{cap}">'
            '<rect width="490" height="270" fill="#cfe3f2"/>'
            '<ellipse cx="380" cy="55" rx="70" ry="18" fill="#ffffff" opacity="0.8"/><ellipse cx="120" cy="40" rx="55" ry="14" fill="#ffffff" opacity="0.8"/>'
            '<path d="M150 150 Q210 60 255 70 Q290 60 300 95 Q330 120 350 150 Z" fill="#9c5a3a" stroke="#6b3a22" stroke-width="1.5"/>'
            '<path d="M240 72 Q255 42 272 70 Z" fill="#8a4c30" stroke="#6b3a22" stroke-width="1.2"/>'
            '<rect x="0" y="150" width="490" height="120" fill="#c98a5e"/>'
            f'{bricks}{courses}'
            '<path d="M20 238 H470" stroke="#7a3d22" stroke-width="2"/>'
            f'<text x="245" y="260" text-anchor="middle" font-size="15" fill="#3b2416" font-family="sans-serif">{cap}</text></svg>')


P('… unequal distribution of agricultural produce, the special dress of women, the extraordinary popularity of bangles among women, and opposition to modern education still in rural areas are a few prominent glimpses of this culture.',
  '… زرعی اجناس کی غیر مساویانہ تقسیم، خواتین کا مخصوص لباس، خواتین میں چوڑیوں کی غیر معمولی مقبولیت اور دیہی علاقوں میں اب بھی جدید تعلیم کی مخالفت اس ثقافت کی چند نمایاں جھلکیاں ہیں۔',
  '… د کرنیزو توکو نابرابر وېش، د ښځو ځانګړې جامې، په ښځو کې د بنګړو غیر معمولي شهرت، او په کلیوالو سیمو کې اوس هم د نوې زده‌کړې مخالفت د دې کلتور څو برجسته ځلکې دي.')
H('Baloch culture', 'بلوچی ثقافت', 'بلوڅ کلتور')
P('The Baloch living in rugged mountains are famous for their culture. Ancient traditions, the sardari system, special customs on occasions of marriage and happiness, embroidery on dress, special Baloch foods of many kinds, gun, sword and nomadism are the basic components of this culture. In the province of Balochistan this culture is still prevalent just as before, with all its ancient values. The influences of Iranian culture on Baloch culture are very great. Iranian influences are visible in their handicrafts and utensils too. Because of distance from modern education and the absence of means of communication, such components still exist in Baloch culture as have now disappeared in other cultures.',
  'سنگلاخ پہاڑوں کے باسی بلوچ اپنی ثقافت کے لیے مشہور ہیں۔ قدیم روایات، سرداری نظام، شادی بیاہ اور خوشی کے مواقع کی خاص رسومات، لباس پر گلکاری، انواع و اقسام کی خاص بلوچی غذائیں، بندوق، تلوار اور خانہ بدوشی اس ثقافت کے بنیادی اجزاء ہیں۔ صوبہ بلوچستان میں یہ ثقافت اپنی تمام تر قدیمی اقدار کے ساتھ اب بھی ویسے ہی رائج ہے۔ بلوچی ثقافت پر ایرانی ثقافت کے اثرات بہت زیادہ ہیں۔ ان کی دستکاریوں اور ظروف میں بھی ایرانی اثرات نمایاں ہیں۔ جدید تعلیم سے دوری، ذرائع ابلاغ کے نہ ہونے سے بلوچی ثقافت میں اب بھی ایسے اجزاء موجود ہیں جو دوسری ثقافتوں میں اب ناپید ہیں۔',
  'د کلکو غرونو اوسېدونکي بلوڅ د خپل کلتور لپاره مشهور دي. لرغوني دودونه، د سردارۍ نظام، د واده او خوښۍ د وختونو ځانګړي رسمونه، پر جامو ګلدوزي، د بلوڅو بېلابېل ځانګړي خواړه، ټوپک، توره او کوچیتوب د دې کلتور بنسټیزې برخې دي. د بلوچستان په ولایت کې دا کلتور له خپلو ټولو لرغونو ارزښتونو سره اوس هم هماغسې رواج دی. پر بلوڅ کلتور د ایراني کلتور اغېزې ډېرې دي؛ د دوی په لاسي صنایعو او لوښو کې هم ایراني اغېزې ښکاري. له نوې زده‌کړې د لرېوالي او د رسنیو د نشتوالي له امله په بلوڅ کلتور کې اوس هم داسې برخې شته چې په نورو کلتورونو کې اوس ورکې دي.')
H('Cultural heritage of Pakistan — important sites', 'پاکستان کا ثقافتی ورثہ — اہم مقامات', 'د پاکستان کلتوري میراث — مهم ځایونه')
P('The land of Pakistan has been the cradle of ancient cultures and civilisations, in which the Indus Valley Civilization (Indus Valley Civilization) and the Gandhara Civilization (Gandhara Civilization) are very important.',
  'پاکستان کی سرزمین قدیم ثقافتوں اور تہذیبوں کا گہوارہ رہی ہے۔ جس میں وادیٔ سندھ کی تہذیب (Indus Valley Civilization) اور گندھارا تہذیب (Gandhara Civilization) بہت ہی اہم ہیں۔',
  'د پاکستان ځمکه د لرغونو کلتورونو او تمدنونو زانګو پاتې شوې، چې پکې د سند د درې تمدن (Indus Valley Civilization) او د ګندهارا تمدن (Gandhara Civilization) ډېر مهم دي.')
P('With reference to the Indus Valley Civilization the most important sites are Moenjodaro and Harappa. From observation of these sites it is learnt that the civilisation of the Indus Valley was urban. The cities of Moenjodaro and Harappa were extensive and densely populated. Much labour was employed in the construction and arrangement of quarters, streets and bazaars. The streets were wide. There was an excellent arrangement of cleanliness. Pucca drains were built in the streets for the drainage of water. From this it is learnt that the people of this area were civilised. Great skill is seen in the construction of residential houses too. Besides the outer walls, floors too were made of baked bricks. In the houses there was a reasonable arrangement for fresh air and light. To escape the severity of the weather, basements were built under the houses, in which a suitable arrangement of light and air was made. The bathrooms of the houses were very spacious and clean. For drinking water there were wells.',
  'وادیٔ سندھ کی تہذیب کے حوالے سے اہم ترین مقامات موہنجوداڑو اور ہڑپہ ہیں۔ ان مقامات کے مشاہدے سے پتا چلتا ہے کہ وادیٔ سندھ کی تہذیب شہری تھی۔ موہنجوداڑو اور ہڑپہ کے شہر وسیع اور گنجان آباد تھے۔ محلوں، گلی کوچوں اور بازاروں کی تعمیر و ترتیب میں کافی محنت سے کام لیا گیا تھا۔ گلیاں کشادہ تھیں۔ صفائی کا اعلیٰ انتظام تھا۔ گلیوں میں پانی کے نکاس کے لیے پختہ نالیاں تعمیر کی گئی تھیں۔ اس سے پتہ چلتا ہے کہ اس علاقے کے لوگ تہذیب یافتہ تھے۔ رہائشی مکانات کی تعمیر میں بھی بڑا سلیقہ نظر آتا ہے۔ بیرونی دیواروں کے علاوہ فرش بھی پختہ اینٹوں سے بنائے گئے تھے۔ گھروں میں تازہ ہوا اور روشنی کا معقول انتظام تھا۔ موسم کی شدت سے بچنے کے لیے گھروں کے نیچے تہہ خانے بنائے جاتے تھے۔ جن میں روشنی اور ہوا کا مناسب بندوبست کیا جاتا تھا۔ گھر کے غسل خانے بہت کشادہ اور صاف تھے۔ پینے کے پانی کے لیے کنوئیں موجود تھے۔',
  'د سند د درې د تمدن په اړه تر ټولو مهم ځایونه موهنجوداړو او هړپه دي. د دې ځایونو له کتنې معلومېږي چې د سند د درې تمدن ښاري و. د موهنجوداړو او هړپه ښارونه پراخ او ګڼ مېشته وو. د محلو، کوڅو او بازارونو په جوړولو او ترتیب کې ډېر زیار ایستل شوی و. کوڅې پراخې وې. د صفايي غوره ترتیب و. په کوڅو کې د اوبو د وتلو لپاره پخې ویالې جوړې شوې وې. له دې معلومېږي چې د دې سیمې خلک متمدن وو. د استوګنیزو کورونو په جوړولو کې هم ډېر سلیقه ښکاري. د بهرنیو دېوالونو سربېره فرشونه هم له پخو خښتو جوړ شوي وو. په کورونو کې د تازه هوا او رڼا مناسب ترتیب و. د موسم له سختۍ د ژغورنې لپاره د کورونو لاندې تهکاوې جوړېدې، چې پکې د رڼا او هوا مناسب بندوبست کېده. د کور تشنابونه ډېر پراخ او پاک وو. د څښاک اوبو لپاره کوهیان وو.')
P('The important sites of Gandhara civilisation have been Peshawar, Charsadda, Swat and Taxila. From the political point of view Charsadda and Peshawar have been the capitals of the Gandhara period. The basic reason for the fame of Gandhara civilisation is its excellence in the fine arts, especially stone carving, which was admired throughout the world. This area remained for some time first under the influence of Iran and then of Greece. That is why the Indian, Iranian and Greek civilisations combined here and gave birth to such a great civilisation in which the characteristics of the whole civilised world were gathered.',
  'گندھارا تہذیب کے اہم مقامات پشاور، چارسدہ، سوات اور ٹیکسلا رہے ہیں۔ سیاسی لحاظ سے چارسدہ اور پشاور گندھارا دور کے دارالخلافے رہے ہیں۔ گندھارا تہذیب کی شہرت کی بنیادی وجہ فنونِ لطیفہ بالخصوص سنگ تراشی میں کمال ہے۔ جسے پوری دُنیا میں سراہا گیا۔ یہ علاقہ کچھ عرصہ تک پہلے ایران اور پھر یونان کے زیرِ اثر رہا۔ اس لیے ہندی، ایرانی اور یونانی تہذیبوں نے مل کر یہاں ایک ایسی عظیم تہذیب کو جنم دیا جس میں ساری متمدن دُنیا کی خصوصیات جمع ہو گئی تھیں۔',
  'د ګندهارا تمدن مهم ځایونه پېښور، چارسده، سوات او ټکسیلا وو. له سیاسي پلوه چارسده او پېښور د ګندهارا دورې پلازمېنې وې. د ګندهارا تمدن د شهرت بنسټیز لامل په ښکلو هنرونو، په ځانګړي ډول د ډبرو په تراشلو کې کمال دی، چې په ټوله نړۍ کې ستایل شو. دا سیمه یو څه وخت لومړی د ایران او بیا د یونان تر اغېز لاندې وه. له همدې امله هندي، ایراني او یوناني تمدنونو یوځای دلته داسې ستر تمدن وزېږاوه چې پکې د ټولې متمدنې نړۍ ځانګړنې راټولې شوې وې.')
t.visual('pak12-moenjodaro', ruins_svg('Ruins of Moenjodaro'), ruins_svg('موہنجوداڑو کے کھنڈرات'), ruins_svg('د موهنجوداړو کنډوالې'), 490 / 270)
P('The cultural centre of Gandhara was Taxila. This city was the centre of learning and art. Its seats of learning were famous. Students came here from other countries too to acquire knowledge. Countless rare specimens of stone carving and sculpture have been found in the area of Gandhara, which are at present kept for display in the museums of Taxila, Peshawar and Swat.',
  'گندھارا کا ثقافتی مرکز ٹیکسلا تھا۔ یہ شہر علم و فن کا مرکز تھا۔ یہاں کی درسگاہیں مشہور تھیں۔ جہاں دیگر ممالک سے بھی طلبہ علم حاصل کرنے کی غرض سے آتے تھے۔ گندھارا کے علاقے سے سنگ تراشی اور مجسمہ سازی کے بے شمار نادر نمونے ملے ہیں جو اس وقت ٹیکسلا، پشاور اور سوات کے عجائب گھروں میں نمائش کے لیے رکھے گئے ہیں۔',
  'د ګندهارا کلتوري مرکز ټکسیلا و. دا ښار د علم او هنر مرکز و. د دې ځای مدرسې مشهورې وې، چېرته چې له نورو هېوادونو هم زده‌کوونکي د علم زده کولو لپاره راتلل. د ګندهارا له سیمې د ډبرو تراشلو او مجسمه جوړونې بې‌شمېره نادرې بېلګې موندل شوې، چې اوس د ټکسیلا، پېښور او سوات په موزیمونو کې د نندارې لپاره ایښودل شوې.')
P('Besides the above sites, countless historic buildings also exist throughout the length and breadth of Pakistan which are part of our precious historical heritage. The names of a few of them are these:',
  'درج بالا مقامات کے علاوہ پاکستان کے طول و عرض میں بے شمار تاریخی عمارتیں بھی موجود ہیں جو ہمارے قیمتی تاریخی ورثے کا حصہ ہیں۔ ان میں سے چند کے نام یہ ہیں:۔',
  'د پورته ځایونو سربېره د پاکستان په اوږدو او پلنو کې بې‌شمېره تاریخي ودانۍ هم شته چې زموږ د قیمتي تاریخي میراث برخه دي. د ځینو نومونه یې دا دي:')
t.group('lines', [('1. Bala Hisar fort and Mohabbat Khan mosque (Peshawar)', '1۔ قلعہ بالا حصار اور مسجد مہابت خان (پشاور)', '۱. د بالا حصار کلا او د مهابت خان جومات (پېښور)'),
                  ('2. Badshahi mosque, Shahi fort and Shalimar garden (Lahore)', '2۔ بادشاہی مسجد، شاہی قلعہ اور شالامار باغ (لاہور)', '۲. بادشاهي جومات، شاهي کلا او شالامار باغ (لاهور)'),
                  ('3. Jamia mosque (Thatta)', '3۔ جامع مسجد (ٹھٹھہ)', '۳. جامع جومات (ټهټه)')])
H('Common features of Pakistani culture', 'پاکستانی ثقافت کی مشترکہ خصوصیات', 'د پاکستاني کلتور ګډې ځانګړنې')
P('The features of Pakistani culture that we see today are those of our cultural heritage of thousands of years',
  'آج پاکستانی ثقافت کے جو خد و خال ہمیں نظر آتے ہیں۔ وہ ہمارے ہزاروں سالہ ثقافتی ورثے کا',
  'نن د پاکستاني کلتور کوم څېرې چې موږ ته ښکاري، هغه زموږ د زرګونو کلونو کلتوري میراث')
rec = BOOK.record(t, 'pak12-ch6-text-4', 'Chapter 6 text (4)', 'بابِ ششم — متن (۴)', 'شپږم څپرکی — متن (۴)', 66, [121, 122])
rec['sourceNote'] = 'The uncaptioned photograph of the Moenjodaro ruins (brick walls below the stupa mound) on p.122 is replaced by a coded illustration. The last paragraph breaks at the foot of p.122 and continues on p.123 (PDF67).'
issues = [{'id': 'pak12-pdf066', 'unit': 6, 'printedPage': 122, 'description': 'The photograph on p.122 carries no caption in print; the label “Ruins of Moenjodaro” is supplied editorially from the surrounding text.'}]

if __name__ == '__main__':
    BOOK.save(66, [(6, rec)], issues=issues)
