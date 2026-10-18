"""Pak Studies XII PDF36 (spread): printed pp.61–62 — Ch.3 latitude/longitude; scale (statement, RF, graphic) with coded scale bar; map types by scale."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
def L(r): t.group('lines', r)
P('… the correct determination of location is made by longitude and latitude. At the end of all large atlases (books of maps) the longitudes and latitudes of the important cities and places of the world are given, so that with their help these places can easily be located on the map.',
  '… محلِ وقوع کا صحیح تعین طول بلد اور عرض بلد سے کیا جاتا ہے۔ تمام بڑے اٹلس (نقشوں کی کتاب) کے آخر میں دنیا کے اہم شہروں اور مقامات کے طول بلد اور عرض بلد دیے جاتے ہیں تاکہ ان کی مدد سے ان مقامات کو آسانی سے نقشہ پر معلوم کیا جا سکے۔',
  '… د موقعیت سم ټاکل د طول البلد او عرض البلد په وسیله کېږي. د ټولو لویو اټلسونو (د نقشو کتابونو) په پای کې د نړۍ د مهمو ښارونو او ځایونو طول البلد او عرض البلد ورکول کېږي، څو د هغو په مرسته دا ځایونه په اسانۍ پر نقشه ومومل شي.')
P('Longitude and latitude are imaginary lines. The central longitude of all longitudes, which has been taken as zero degrees longitude, passes through a place called Greenwich near London. Each longitude takes four minutes to pass in front of the sun. So the difference of time between two longitudes will be these four minutes. Since the time of all places in the world has been fixed in relation to the zero-degree longitude, i.e. the longitude of Greenwich, the time of places east of Greenwich will be ahead of Greenwich time according to the difference of longitude, and the time of those to the west will be behind Greenwich time according to the difference of longitude. Now instruments have been invented which tell the location of a place at the press of a button.',
  'طول بلد اور عرض بلد فرضی خطوط ہیں۔ تمام طول بلد کا مرکزی طول بلد جس کو صفر درجہ طول بلد مانا گیا ہے۔ لندن کے قریب گرینچ نامی مقام سے گزرتا ہے۔ ہر ایک طول بلد سورج کے سامنے سے گزرنے میں چار منٹ کا وقت لیتا ہے۔ چنانچہ دو طول بلد میں وقت کا فرق یہی چار منٹ ہوں گے۔ چونکہ دنیا کے تمام مقامات کا وقت صفر درجہ طول بلد یعنی گرینچ کے طول بلد کی مناسبت سے مقرر کیا گیا ہے اس لیے جو مقامات گرینچ سے مشرق میں ہوں گے ان کا وقت گرینچ کے وقت سے طول بلد کے فرق کے مطابق آگے ہوگا۔ جو مغرب میں ہوں گے ان کا وقت طول بلد کے فرق کے مطابق گرینچ کے وقت سے پیچھے ہوگا۔ اب آلات ایجاد ہو چکے ہیں جو بٹن دبانے پر کسی مقام کا محلِ وقوع بتا دیتے ہیں۔',
  'طول البلد او عرض البلد فرضي کرښې دي. د ټولو طول البلدونو مرکزي طول البلد، چې صفر درجې طول البلد منل شوی، له لندن سره نږدې د ګرینیچ په نوم ځای تېرېږي. هر طول البلد د لمر مخې ته د تېرېدو لپاره څلور دقیقې وخت نیسي. نو د دوو طول البلدونو ترمنځ د وخت توپیر همدا څلور دقیقې وي. څرنګه چې د نړۍ د ټولو ځایونو وخت د صفر درجې طول البلد یعنې د ګرینیچ د طول البلد په تناسب ټاکل شوی، نو هغه ځایونه چې له ګرینیچ ختیځ ته وي، وخت یې د طول البلد د توپیر سره سم د ګرینیچ له وخته مخکې وي؛ او چې لوېدیځ ته وي، وخت یې د طول البلد د توپیر سره سم د ګرینیچ له وخته وروسته وي. اوس داسې الې جوړې شوې چې د تڼۍ په کېکاږلو د یوه ځای موقعیت ښيي.')
H('Scale', 'پیمانہ', 'پیمانه')
P('The ratio of the length of distances on the ground and on the map is called the “scale” of the map. If a map is made on the scale 1 centimetre = 1 kilometre, this shows that a distance of one centimetre on the map is one kilometre on the ground. The scale is always stated on every map, so that those looking at the map can know what ratio the distances on the ground and on the map have. Scales are generally expressed in three ways.',
  'زمین اور نقشے میں فاصلوں کی لمبائی کے تناسب کو نقشے کا ’’پیمانہ‘‘ کہا جاتا ہے۔ ایک نقشہ 1 سنٹی میٹر = 1 کلومیٹر کے پیمانہ پر بنا ہوا ہے تو اس سے یہ ظاہر ہوتا ہے کہ نقشے پر ایک سنٹی میٹر کا فاصلہ زمین پر ایک کلومیٹر ہے۔ ہر نقشے پر پیمانہ کا اظہار ضرور کیا جاتا ہے تاکہ نقشہ دیکھنے والوں کو پتا چل سکے کہ زمین اور نقشوں پر فاصلے کی کیا نسبت ہے۔ پیمانوں کا اظہار عام طور پر تین طرح سے کیا جاتا ہے۔',
  'پر ځمکه او نقشه کې د واټنونو د اوږدوالي تناسب ته د نقشې "پیمانه" ویل کېږي. که یوه نقشه د ۱ سانتي‌متر = ۱ کیلومتر په پیمانه جوړه شوې وي، نو دا ښيي چې پر نقشه د یوه سانتي‌متر واټن پر ځمکه یو کیلومتر دی. پر هره نقشه پیمانه خامخا ښودل کېږي، څو د نقشې لیدونکي پوه شي چې پر ځمکه او نقشه د واټن تناسب څه دی. پیمانې عموماً په درې ډوله څرګندېږي:')
L([('1. By statement (Statement of Scale)', '1۔ بیان سے (Statement of Scale)', '۱. د بیان له لارې (Statement of Scale)'),
   ('2. By representative fraction (Representative Fraction)', '2۔ کسرِ اعتباری سے (Representative Fraction)', '۲. د استازې کسر له لارې (Representative Fraction)'),
   ('3. By graphic (linear) scale (Graphic Scale)', '3۔ خطی پیمانہ سے (Graphic Scale)', '۳. د کرښې پیمانې له لارې (Graphic Scale)')])
P('1. By statement: in this method the scale of the map is given on it thus: 1 centimetre = 1 kilometre. Reading this one realises that one centimetre on the map is equal to one kilometre on the ground.',
  '1۔ بیان سے:- اس طریقے میں نقشے کا پیمانہ اس پر اس طرح دیا جاتا ہے: 1 سینٹی میٹر = 1 کلومیٹر۔ یہ پڑھ کر اندازہ ہو جاتا ہے کہ نقشے پر ایک سینٹی میٹر زمین پر ایک کلومیٹر کے برابر ہے۔',
  '۱. د بیان له لارې: په دې طریقه کې د نقشې پیمانه پرې داسې ورکول کېږي: ۱ سانتي‌متر = ۱ کیلومتر. په لوستلو سړی پوهېږي چې پر نقشه یو سانتي‌متر پر ځمکه له یوه کیلومتر سره برابر دی.')
P('2. Representative fraction: in this method the ratio of the distance given on the map to the actual distance on the ground is expressed by means of a common fraction. For example 1:100000 means that any length on the map, say one centimetre, represents a length 100,000 times as great on the ground, i.e. 100,000 centimetres. Thus:',
  '2۔ کسرِ اعتباری:- اس طریقہ میں نقشے پر دیے ہوئے فاصلے اور زمین کے اصلی فاصلے کی نسبت کو کسرِ عام کے ذریعے سے ظاہر کیا جاتا ہے۔ جیسے 1:100000 کا مطلب ہے کہ نقشے پر کوئی بھی ایک لمبائی مثلاً ایک سینٹی میٹر زمین پر 100000 گنا ویسی ہی لمبائی یعنی 100000 سینٹی میٹر کو ظاہر کرتی ہے اس طرح',
  '۲. استازی کسر: په دې طریقه کې پر نقشه د ورکړل شوي واټن او پر ځمکه د اصلي واټن تناسب د عام کسر په وسیله څرګندېږي. لکه ۱:۱۰۰۰۰۰ مطلب دا دی چې پر نقشه هر اوږدوالی، لکه یو سانتي‌متر، پر ځمکه ۱۰۰۰۰۰ چنده اوږدوالی یعنې ۱۰۰۰۰۰ سانتي‌متره ښيي. په دې ډول:')
P('Representative fraction = distance on map ÷ distance on ground = 1/100000, or 1:100000',
  'کسرِ اعتباری = نقشہ پر فاصلہ ÷ زمین پر فاصلہ = 1/100000 یا 1:100000',
  'استازی کسر = پر نقشه واټن ÷ پر ځمکه واټن = ۱/۱۰۰۰۰۰ یا ۱:۱۰۰۰۰۰')
P('3. Graphic scale: in this method a line is drawn below the map and divided into various parts, and each part shows the ratio of distances on the map and on the ground, e.g.:',
  '3۔ خطی پیمانہ: اس طریقہ میں نقشے کے نیچے ایک لکیر بنا کر اس کو مختلف حصوں میں تقسیم کر دیا جاتا ہے اور ہر حصہ نقشہ اور زمین پر فاصلوں کی نسبت کو ظاہر کرتا ہے جیسے:-',
  '۳. د کرښې پیمانه: په دې طریقه کې د نقشې لاندې یوه کرښه کښل کېږي او په بېلابېلو برخو وېشل کېږي، او هره برخه پر نقشه او ځمکه د واټنونو تناسب ښيي، لکه:')
def bar(lang):
    km = {'en': 'kilometres', 'ur': 'کلومیٹر', 'ps': 'کیلومتره'}[lang]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 70" role="img" aria-label="graphic scale 0–10 km" font-family="Segoe UI, sans-serif">',
         '<rect width="560" height="70" fill="#fff"/>']
    for i in range(10):
        x = 30 + i * 50
        s.append(f'<rect x="{x}" y="{30 if i % 2 == 0 else 38}" width="50" height="8" fill="#111"/><rect x="{x}" y="{38 if i % 2 == 0 else 30}" width="50" height="8" fill="#fff" stroke="#111"/>')
    for i in range(11):
        s.append(f'<text x="{30 + i * 50}" y="24" font-size="12" text-anchor="middle">{i}</text>')
    s.append(f'<text x="535" y="62" font-size="12" text-anchor="end">{km}</text></svg>')
    return ''.join(s)
t.visual('pak12-graphic-scale', bar('en'), bar('ur'), bar('ps'), ratio=.8)
P('The actual distance of one part is equal to one centimetre, but one kilometre is written on it, which means that a distance of one kilometre on the ground is equal to one centimetre on the map.',
  'ایک حصہ کا اصلی فاصلہ ایک سینٹی میٹر کے برابر ہے لیکن اس پر ایک کلومیٹر درج ہے۔ جس کا مطلب یہ ہے کہ زمین پر ایک کلومیٹر فاصلہ نقشے پر ایک سینٹی میٹر کے برابر ہے۔',
  'د یوې برخې اصلي واټن له یوه سانتي‌متر سره برابر دی، خو پرې یو کیلومتر لیکل شوی، چې مطلب یې دا دی چې پر ځمکه د یوه کیلومتر واټن پر نقشه له یوه سانتي‌متر سره برابر دی.')
P('By scale, maps are of three kinds.', 'پیمانوں کے لحاظ سے نقشوں کی تین قسمیں ہیں۔', 'د پیمانې له مخې نقشې درې ډوله دي:')
L([('1. Regional map', '1۔ علاقائی نقشہ (Regional Map)', '۱. سیمه‌ییزه نقشه (Regional Map)'),
   ('2. Topographical map', '2۔ سطحی نقشہ (Topographical Map)', '۲. سطحي (توپوګرافیک) نقشه (Topographical Map)'),
   ('3. Cadastral map', '3۔ رقباتی نقشہ (Cadastral Map)', '۳. د مساحت (کاډسټرل) نقشه (Cadastral Map)')])
P('1. Regional map: this map is on a small scale. It is generally used to present all information about the world, continents and countries. Details are lacking in it. In spite of this, most atlases have these very maps and they are considered very good for educational purposes.',
  '1۔ علاقائی نقشہ: یہ نقشہ چھوٹے پیمانے پر ہوتا ہے۔ یہ عموماً دُنیا، براعظموں اور ملکوں کے متعلق تمام معلومات پیش کرنے کے لیے استعمال ہوتا ہے۔ اس میں تفصیلات کی کمی ہوتی ہے۔ اس کے باوجود اکثر اٹلسوں میں یہی نقشے بنائے گئے ہیں اور تعلیمی مقاصد کے لیے بہت عمدہ تصور کیے جاتے ہیں۔',
  '۱. سیمه‌ییزه نقشه: دا نقشه په وړه پیمانه وي. عموماً د نړۍ، لویو وچو او هېوادونو په اړه د ټولو معلوماتو د وړاندې کولو لپاره کارېږي. جزییات پکې کم وي. سره له دې ډېری اټلسونو کې همدا نقشې جوړې شوې او د تعلیمي موخو لپاره ډېرې ښې ګڼل کېږي.')
rec = BOOK.record(t, 'pak12-ch3-text-9', 'Chapter 3 text (9)', 'بابِ سوم — متن (۹)', 'درېیم څپرکی — متن (۹)', 36, [61, 62])

if __name__ == '__main__':
    BOOK.save(36, [(3, rec)])
