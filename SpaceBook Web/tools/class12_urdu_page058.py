"""Urdu XII PDF58 (spread): p.106 Lesson 12 author note (الطاف فاطمہ, b.1929); p.107 'کنڈکٹر' (copyrighted) summary part 1."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Altaf Fatima', 'الطاف فاطمہ', 'الطاف فاطمه')
a.p('Born: 1929', 'ولادت: ۱۹۲۹ء', 'زېږېدنه: ۱۹۲۹ز')
for x in [
    ('Altaf Fatima was born in Lucknow. She received her early education there and after the creation of Pakistan settled permanently in Lahore with her family. After doing an M.A. and B.Ed. from the Punjab University she took up teaching. She taught Urdu literature at Islamia College for Women and APWA Girls College. She has retired from service and now lives in Lahore.',
     'الطاف فاطمہ لکھنؤ میں پیدا ہوئیں۔ ابتدائی تعلیم وہیں سے حاصل کی اور قیامِ پاکستان کے بعد اپنے خاندان سمیت لاہور میں مستقل رہائش اختیار کی۔ پنجاب یونیورسٹی سے ایم۔ اے، بی۔ ایڈ کرنے کے بعد درس و تدریس سے وابستہ ہو گئیں۔ اسلامیہ کالج برائے خواتین اور اپوا گرلز کالج میں اُردو ادب پڑھاتی رہیں۔ وہ ملازمت سے ریٹائر ہو چکی ہیں اور آج کل لاہور ہی میں مقیم ہیں۔',
     'الطاف فاطمه په لکهنو کې زېږېدلې. لومړنۍ زده کړې یې هلته وکړې او د پاکستان له جوړېدو وروسته له خپلې کورنۍ سره په لاهور کې تل لپاره مېشته شوه. د پنجاب له پوهنتون څخه یې له ایم اې او بي اېډ وروسته تدریس ته مخه کړه. د ښځو په اسلامیه کالج او د اپوا د نجونو په کالج کې یې د اردو ادب تدریس وکړ. له دندې تقاعد شوې او اوس په لاهور کې اوسېږي.'),
    ('Although she lived a long part of her life in Lahore, she stayed aloof from all kinds of literary gatherings, institutions and movements. Her stories are interpreters of reality; she has expressed the psychology of the Eastern woman. She has written on ordinary social problems and tried to find their solutions. She expresses her meaning in short, small sentences.',
     'لاہور میں رہائش اور زندگی کا ایک طویل عرصہ گزارنے کے باوجود وہ ہر طرح کی ادبی مجالس، اداروں اور تحریکوں سے لاتعلق رہیں۔ اُن کے افسانے حقیقت کے ترجمان ہیں اُنھوں نے مشرقی عورت کی نفسیات کی ترجمانی کی ہے۔ اُنھوں نے عام معاشرتی مسائل پر قلم اُٹھایا ہے اور اُن کا حل تلاش کرنے کی کوشش کی ہے۔ وہ چھوٹے چھوٹے جملوں میں اپنا مافی الضمیر بیان کرتی ہیں۔',
     'سره له دې چې د ژوند اوږده موده یې په لاهور کې تېره کړه، له هر ډول ادبي غونډو، ادارو او غورځنګونو بې‌تړاوه پاتې شوه. افسانې یې د حقیقت ژباړونکې دي؛ هغې د ختیځې ښځې ارواپوهنه انځور کړې. هغې په عامو ټولنیزو ستونزو لیکلي او د هغو د حل هڅه یې کړې. خپل مطلب په لنډو لنډو جملو کې بیانوي.'),
    ('Works: Nishan-e-Mahfil, Dastak na Do, Chalta Musafir (novels); Woh Jise Chaha Gaya, Jab Deewarein Girya Karti Hain, Tar-e-Ankaboot (short stories).', 'تصانیف: نشانِ محفل، دستک نہ دو، چلتا مسافر (ناول)۔ وہ جسے چاہا گیا، جب دیواریں گریہ کرتی ہیں، تارِ عنکبوت (افسانے)۔', 'تصنیفات: نشان محفل، دستک نه دو، چلتا مسافر (ناولونه). وه جسې چاها ګیا، جب دیوارېن ګریه کرتي هیں، تار عنکبوت (افسانې).'),
]: a.p(*x)
UT = ('The Conductor', 'کنڈکٹر', 'کنډکټر', 'الطاف فاطمہ')
au = BOOK.record(a, 'urdu12-u12-author', 'About the author: Altaf Fatima', 'الطاف فاطمہ (تعارف)', 'الطاف فاطمه (پېژندنه)', 58, [106], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait of Altaf Fatima and floral border are decorative; not reproduced.'

s = Builder()
s.h('The Conductor — Altaf Fatima', 'کنڈکٹر — الطاف فاطمہ', 'کنډکټر — الطاف فاطمه')
s.p('[Paragraph-wise summary — Altaf Fatima (d. 2018) is in copyright; read the full story in the printed textbook, pp. 107–116.]', '[پیراگراف وار خلاصہ — الطاف فاطمہ (وفات ۲۰۱۸ء) کی تحریر کاپی رائٹ میں ہے؛ مکمل افسانہ درسی کتاب کے صفحات ۱۰۷–۱۱۶ میں پڑھیں۔]', '[پراګراف په پراګراف لنډیز — د الطاف فاطمې (مړه ۲۰۱۸ز) لیکنه د کاپي رایټ لاندې ده؛ بشپړه افسانه په چاپي درسي کتاب کې په ۱۰۷–۱۱۶ مخونو کې ولولئ.]')
for x in [
    ('The narrator hears that Lalu has now built a good business in Karachi and a decent bungalow; long ago she had heard, with surprise, that he married a school teacher who accepted an under-matric husband and for years was like the strong wheel — even the steering — of his rickety cart of life. No one’s life runs in a straight line; life is a maze of circles, dead ends and tangled lines, and each must find his own way.',
     'راوی سنتی ہے کہ لالو نے اب کراچی میں اچھا بزنس جما لیا ہے اور ایک معقول بنگلہ بنا لیا ہے؛ بہت پہلے یہ سن کر حیرت ہوئی تھی کہ اس نے ایک سکول ٹیچر سے شادی کی جس نے ایک انڈر میٹرک کی شریکِ حیات بننا قبول کیا اور برسوں اس کی زندگی کی چھکڑا گاڑی کا مضبوط پہیا بلکہ اسٹیرنگ بنی رہی۔ کسی کا حال بھی خطِ مستقیم نہیں؛ زندگی دائروں، بند راستوں اور الجھے خطوط کی بھول بھلیاں ہے اور ہر ایک کو اپنی راہ خود ڈھونڈنی ہوتی ہے۔',
     'راویه اوري چې لالو اوس په کراچۍ کې ښه سوداګري جوړه کړې او یوه مناسبه بنګله یې ودانه کړې؛ ډېر مخکې یې په حیرانتیا اورېدلي وو چې له یوې ښوونځي ښوونکې سره یې واده کړی چې د یوه له میټرک ټیټ سړي ژوندملګرې کېدل یې ومنل او کلونه کلونه د هغه د ژوند د ګاډي ټینګ ټایر بلکې سټیرنګ پاتې شوه. د هیچا ژوند په سمه کرښه نه ځي؛ ژوند د دایرو، بندو لارو او ګډو وډو کرښو یوه بول‌بلیا ده او هر څوک باید خپله لاره پخپله ومومي.'),
    ('Lalu was the second son of his family. When he was in class five his progress was slow and disappointing, his features stamped with foolishness, and he stammered so that he said “ṭāf” for kāf and “ḍāf” for gāf; he had learned his whole reader by rote in this way… (continued on p. 108)',
     'لالو اپنے گھرانے کا دوسرا بیٹا تھا۔ جب وہ پانچویں جماعت میں تھا تو اس کی تعلیمی رفتار سست اور مایوس کن تھی، خدوخال پر حماقت کی چھاپ نمایاں تھی اور تُتلاہٹ ایسی کہ کاف کو ٹاف اور گاف کو ڈاف کہتا؛ اس نے اپنی پوری کنگ ریڈر اسی انداز میں رَٹ رکھی تھی… (صفحہ ۱۰۸ پر جاری)',
     'لالو د خپلې کورنۍ دویم زوی و. کله چې په پنځم ټولګي کې و، تعلیمي پرمختګ یې سست او نا امیده کوونکی و، پر څېره یې د حماقت نښه ښکاره وه، او داسې کوټه‌ژبی و چې "کاف" ته یې "ټاف" او "ګاف" ته یې "ډاف" ویل؛ خپل ټول کنګ ریډر یې په همدې ډول یاد کړی و… (په ۱۰۸ مخ کې دوام)'),
]: s.p(*x)
tx = BOOK.record(s, 'urdu12-u12-text-1', 'Lesson text — summary (1)', 'متنِ سبق — خلاصہ (۱)', 'د لوست متن — لنډیز (۱)', 58, [107])
tx['sourceGap'] = 'Altaf Fatima (d. 2018) — in copyright; paragraph-wise summary in the app, not verbatim. Printed p. 107.'
issues = [{'id': 'urdu12-pdf058', 'unit': 12, 'printedPage': 106, 'description': 'The author note gives only the birth year (۱۹۲۹ء) and says she “now lives in Lahore”; a handwritten owner note “وفات 2018ء” is added in the scan (excluded; she did die in 2018). Lesson 12 is “کنڈکٹر” (legacy dataset wrongly titled it “مائیں”).'}]

if __name__ == '__main__':
    BOOK.save(58, [(12, au), (12, tx)], issues=issues)
