"""Islamic History XII PDF11: pp.12–13 — Saffah (reorganisation, revolts, conquests, death); Lesson 3 Abu Ja'far Mansur (accession, start). Run: python class12_ihist_page011.py"""
from class12_ihist_common import BOOK, Builder, rec


def S(b, rows):
    for h, p in rows:
        b.h(*h)
        b.p(*p)


def p11():
    b = Builder()
    S(b, [(('Provincial reorganisation:', 'صوبائی تنظیمِ نو:', 'ولایتي بیا تنظیم'),
           ('Saffah reorganised the provinces afresh. He made his relatives governors. Madinah Munawwarah, Makkah Mukarramah, Yemen and Yamamah were joined together and made one province. The governorship of this province he gave to his uncle Dawud bin Ali. He made his other uncle Abdullah bin Ali governor of Syria. The regions of Jazirah, Armenia and Azerbaijan were handed to his brother Mansur. His uncle Sulayman was the ruler of Basrah. The region of Egypt was handed to Abu \'Awn, and the province of Khurasan to Abu Muslim.', 'سفاح نے صوبوں کی نئے سرے سے تنظیم کی۔ اپنے عزیز و اقارب کو والی بنایا۔ مدینہ منورہ، مکہ مکرمہ، یمن، اور یمامہ کے علاقوں کو ملا کر ایک صوبہ بنا دیا گیا۔ اس صوبے کی گورنری اپنے چچا داؤد بن علی کو دی۔ اپنے دوسرے چچا عبداللہ بن علی کو شام کا گورنر بنا دیا۔ جزیرہ آرمینیا اور آذربائیجان کے علاقے اپنے بھائی منصور کے حوالے کئے۔ اس کا چچا سلیمان بصرہ کا حاکم تھا۔ مصر کا علاقہ ابو عون اور خراسان کا صوبہ ابو مسلم کے حوالے کیا گیا۔', 'سفاح ولایتونه له سره منظم کړل؛ خپل خپلوان یې والیان کړل. مدینه منوره، مکه مکرمه، یمن او یمامه یوځای او یو ولایت شول؛ د دې ولایت والي‌توب یې خپل تره داود بن علي ته ورکړ. خپل بل تره عبدالله بن علي یې د شام والي کړ. د جزیرې، ارمنیا او اذربایجان سیمې یې خپل ورور منصور ته وسپارلې. تره یې سلیمان د بصرې حاکم و. د مصر سیمه ابو عون ته او د خراسان ولایت ابو مسلم ته وسپارل شو.')),
          (('The killing of Yazid bin Hubayrah:', 'یزید بن ہبیرہ کا قتل:', 'د یزید بن هبیره وژنه'),
           ('Yazid bin Hubayrah was the governor of Iraq on behalf of Marwan. The city of Wasit was in his possession. Mansur and Husayn bin Qahtabah besieged it. On a few conditions Yazid handed himself and the city over to Mansur. The Caliph at first granted him safety, but later, at the instigation of Abu Muslim, had him killed by Mansur.', 'یزید بن ہبیرہ مروان کی طرف سے عراق کا گورنر تھا۔ واسط کا شہر اس کے قبضے میں تھا۔ منصور اور حسین بن قحطبہ نے محاصرہ کیا۔ چند شرائط پر یزید نے اپنے آپ کو اور شہر کو منصور کے حوالے کر دیا۔ خلیفہ نے پہلے تو امان بخشی لیکن بعد میں ابو مسلم کے اشارے پر منصور سے اسے قتل کروا دیا۔', 'یزید بن هبیره د مروان له لوري د عراق والي و؛ د واسط ښار یې په قبضه کې و. منصور او حسین بن قحطبه محاصره کړ. یزید په ځینو شرطونو ځان او ښار منصور ته وسپارل. خلیفه لومړی امان ورکړ، خو وروسته یې د ابو مسلم په اشاره منصور ته ووژلو.')),
          (('The vizierate and the killing of Abu Salamah:', 'وزارت اور ابوسلمہ کا قتل:', 'وزارت او د ابو سلمه وژنه'),
           ('Saffah established the post of vizierate in a regular way. He appointed Abu Salamah, the famous da\'i and helper of the Abbasid movement, as the first vizier. Abu Salamah had devotion to the Ahl al-Bayt; therefore Saffah had him killed by a certain Khurasani and spread it about that a Kharijite had killed him. After this the vizierate was entrusted to Khalid Barmaki. His family occupied this post for a considerable period.', 'سفاح نے وزارت کا باقاعدہ عہدہ قائم کیا۔ عباسی تحریک کے مشہور داعی اور مددگار ابو سلمہ کو پہلا وزیر مقرر کیا۔ ابو سلمہ کو اہلِ بیت سے عقیدت تھی، اس لئے سفاح نے کسی خراسانی سے اسے قتل کروا کر مشہور کر دیا کہ خارجی نے قتل کر دیا ہے۔ اس کے بعد خالد برمکی کو وزارت سونپی گئی۔ اس کا خاندان کافی عرصہ اس عہدے پر قابض رہا۔', 'سفاح د وزارت منظمه څوکۍ جوړه کړه؛ د عباسي غورځنګ مشهور داعي او مرستندوی ابو سلمه یې لومړی وزیر وټاکه. ابو سلمه له اهل بیت سره عقیدت درلود، نو سفاح د یوه خراساني له لارې ووژلو او مشهوره یې کړه چې یوه خارجي وژلی. له دې وروسته وزارت خالد برمکي ته وسپارل شو؛ کورنۍ یې ډېره موده پر دې څوکۍ وه.'))])
    r1 = rec(b, 2, 12, 11, [12])
    t = Builder()
    S(t, [(('Revolts:', 'بغاوتیں:', 'بغاوتونه'),
           ('Because of Saffah\'s bloodshed, revolts took place here and there. Governors began to become autonomous. The governors of Mosul, Armenia and Sindh revolted. Armies were sent to crush them. The supporters of the Ahl al-Bayt too revolted here and there, because the Banu Abbas themselves had set themselves up as the Ahl al-Bayt. Saffah brought all these revolts under control.', 'سفاح کی خونریزی کی وجہ سے جگہ جگہ بغاوتیں ہوئیں۔ گورنر مختار ہونے لگے۔ موصل، آرمینیا اور سندھ کے گورنروں نے بغاوت کر دی۔ ان کی سرکوبی کے لئے لشکر بھیجے گئے۔ اہلِ بیت کے حامیوں نے بھی جگہ جگہ بغاوتیں کیں کیونکہ بنو عباس خود اہلِ بیت بن بیٹھے تھے۔ سفاح نے ان تمام بغاوتوں پر قابو پا لیا۔', 'د سفاح د وینې تویولو له امله ځای ځای بغاوتونه وشول؛ والیان خپلواک کېدل پیل شول. د موصل، ارمنیا او سند والیانو بغاوت وکړ؛ د ځپلو لپاره یې لښکرې ولېږل شوې. د اهل بیت ملاتړو هم ځای ځای بغاوتونه وکړل، ځکه بنو عباس پخپله ځانونه اهل بیت ګڼل. سفاح پر دې ټولو بغاوتونو واکمن شو.')),
          (('Conquests:', 'فتوحات:', 'فتوحات'),
           ('Although in Saffah\'s era defeats had to be suffered at the hands of the Romans, later many conquests too were achieved. Khalid bin Ibrahim and Salih bin Ziyad conquered the regions of Khuttal, Chach, Farghanah and Kish on the Chinese frontier and included them in the Abbasid sultanate.', 'سفاح کے دور میں اگرچہ رومیوں سے شکست کھانی پڑیں لیکن بعد میں کئی فتوحات بھی حاصل ہوئی۔ خالد بن ابراہیم اور صالح بن زیاد نے چینی سرحد پر ختن، چاچ، فرغانہ اور کش کے علاقے فتح کر کے عباسی سلطنت میں شامل کئے۔', 'که څه هم د سفاح په دوره کې له رومیانو ماتې وخوړل شوې، خو وروسته ډېر فتوحات هم ترلاسه شول. خالد بن ابراهیم او صالح بن زیاد د چین پر پوله د ختن، چاچ، فرغانې او کش سیمې فتح کړې او په عباسي سلطنت کې یې شاملې کړې.')),
          (('Death:', 'وفات:', 'وفات'),
           ('Saffah died in 136 AH. Before his death he nominated his brother Abu Ja\'far Mansur and his nephew \'Isa bin Musa, one after the other, as successors. Just as Saffah was famous for ruthlessness and bloodshed, his prudence and generosity too were matchless. He hated luxury and pleasure-seeking. He was extremely fond of poetry and music.', 'سفاح نے ۱۳۶ھ میں وفات پائی۔ وفات سے قبل اس نے اپنے بھائی ابوجعفر منصور اور بھتیجے عیسیٰ بن موسیٰ کو یکے بعد دیگرے جانشین نامزد کیا۔ سفاح جہاں سفاکی اور خونریزی کے لئے مشہور تھا وہاں اس کا تدبر اور فیاضی بھی بے مثل تھی۔ اسے عیش و عشرت سے نفرت تھی۔ شعر و شاعری اور موسیقی کا بے حد شوقین تھا۔', 'سفاح په ۱۳۶ هـ کې وفات شو. له مړینې مخکې یې خپل ورور ابوجعفر منصور او وراره عیسی بن موسی یو په بل پسې ځای‌ناستي وټاکل. سفاح چې څومره په بې‌رحمۍ او وینې تویولو مشهور و، همغومره یې تدبیر او سخاوت هم بې‌ساری و. له عیش او عشرت کرکه یې درلوده؛ د شعر، شاعرۍ او موسیقۍ ډېر شوقي و.'))])
    r2 = rec(t, 2, 13, 11, [13])
    u = Builder()
    u.h('Abu Ja\'far Mansur', 'ابوجعفر منصور', 'ابوجعفر منصور')
    u.p('754 CE to 775 CE', '۷۵۴ء تا ۷۷۵ء', '۷۵۴ع تر ۷۷۵ع')
    u.h('Accession:', 'تخت نشینی:', 'پر تخت کېناستل')
    u.p('At the time of Saffah\'s death Mansur had gone to Makkah to perform Hajj. When he …', 'سفاح کی موت کے وقت منصور حج کرنے کے لئے مکہ گیا ہوا تھا۔ جب اسے', 'د سفاح د مړینې پر مهال منصور د حج لپاره مکې ته تللی و. کله چې هغه ته …')
    BOOK.save(11, [(2, r1), (2, r2), (3, rec(u, 3, 13, 11, [13], first=True))], complete_units=[2], issues=[{'id': 'ihist12-pdf011', 'unit': 2, 'printedPage': 12,
               'description': 'Lesson 2 (Saffah) ends on p.13 and Lesson 3 (Mansur) begins on the same page. "شکست کھانی پڑیں … فتوحات بھی حاصل ہوئی" kept as printed. Student mark "①" excluded. PDF9–10 are duplicate scans of PDF7–8 (excluded).'}])


if __name__ == '__main__':
    p11()
