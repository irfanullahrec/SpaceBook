"""Pak Studies XII PDF51 (spread): printed pp.91–92 — Ch.5 joint institutions; provincial governments; Governor; provincial cabinet; provincial assembly seats (table incl. p.93 rows)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
H('Central (federal) and provincial joint institutions', 'مرکزی (وفاقی) اور صوبائی مشترکہ ادارے', 'مرکزي (فدرالي) او ولایتي ګډې ادارې')
P('To carry out certain matters between the federal and provincial governments, such institutions have been established as relate equally to both the federal and the provincial governments, for example:',
  'وفاقی اور صوبائی حکومتوں کے درمیان بعض امور کو سرانجام دینے کے لیے ایسے ادارے قائم ہیں جن کا تعلق وفاقی اور صوبائی حکومت دونوں سے یکساں ہوتا ہے۔ مثلاً',
  'د فدرالي او ولایتي حکومتونو ترمنځ د ځینو چارو د ترسره کولو لپاره داسې ادارې جوړې دي چې له فدرالي او ولایتي دواړو حکومتونو سره یو شان تړاو لري، لکه:')
t.group('lines', [('1. Planning Commission', '1۔ منصوبہ بندی کمیشن', '۱. د پلان جوړونې کمیسیون'), ('2. Council of Common Interests', '2۔ مشترکہ مفادات کی کونسل', '۲. د ګډو ګټو شورا'),
                  ('3. National Economic Council', '3۔ قومی اقتصادی کونسل', '۳. ملي اقتصادي شورا'), ('4. National Finance Commission', '4۔ قومی مالیاتی کمیشن', '۴. ملي مالي کمیسیون'),
                  ('5. Council of Islamic Ideology', '5۔ اسلامی نظریاتی کونسل', '۵. اسلامي نظریاتي شورا')])
H('The provincial governments', 'صوبائی حکومتیں (The Provincial Governments)', 'ولایتي حکومتونه (The Provincial Governments)')
P('According to the 1973 constitution of the Islamic Republic of Pakistan a parliamentary system has been introduced within the provinces. The executive head of each province is the Governor. The Chief Minister is the head of the provincial government, who runs the administration of the province with the help of provincial ministers and the Civil Secretariat. Each provincial minister has one or more departments, for whose performance he is responsible. At the provincial level there is an elected provincial assembly for legislation.',
  'اسلامی جمہوریہ پاکستان کے 1973ء کے آئین کے مطابق صوبوں کے اندر پارلیمانی نظام رائج کیا گیا ہے۔ ہر صوبے کا انتظامی سربراہ گورنر ہوتا ہے۔ وزیرِ اعلیٰ صوبائی حکومت کا سربراہ ہوتا ہے وہ صوبے کا انتظام صوبائی وزراء اور سول سیکرٹریٹ کی مدد سے چلاتا ہے۔ ہر صوبائی وزیر کے ذمے ایک یا ایک سے زیادہ محکمے ہوتے ہیں جن کی کارکردگی کا وہ ذمہ دار ہوتا ہے۔ صوبائی سطح پر قانون سازی کے لیے منتخب صوبائی اسمبلی ہوتی ہے۔',
  'د پاکستان اسلامي جمهوریت د ۱۹۷۳ز د اساسي قانون سره سم په ولایتونو کې پارلماني نظام رواج شوی. د هر ولایت اجرايي مشر والي وي. اعلی وزیر د ولایتي حکومت مشر وي، چې د ولایت اداره د ولایتي وزیرانو او ملکي دارالانشا په مرسته چلوي. هر ولایتي وزیر یوه یا له یوې زیاتې څانګې لري چې د کارکردګۍ مسؤول یې دی. په ولایتي کچه د قانون جوړونې لپاره ټاکل شوې ولایتي اسمبلي وي.')
H('The provincial Governor', 'صوبائی گورنر', 'ولایتي والي')
P('The importance that the President has as head in the country falls to the share of the Governor in the province. The duties and powers of the Governor are mentioned below.',
  'جو اہمیت ملک میں سربراہ کی حیثیت سے صدر کو حاصل ہوتی ہے وہی اہمیت صوبے میں گورنر کے حصے میں آتی ہے۔ ذیل میں گورنر کے فرائض و اختیارات کا ذکر کیا گیا ہے۔',
  'څه اهمیت چې په هېواد کې د مشر په توګه ولسمشر ته حاصل وي، هماغه اهمیت په ولایت کې والي ته ورکول کېږي. لاندې د والي دندې او واکونه یاد شوي.')
H('Executive affairs', 'انتظامی امور', 'اجرايي چارې')
P('All provincial orders are issued in the name of the Governor. In most matters the Governor is bound by the advice of the Chief Minister and the provincial cabinet. It is the duty of the Chief Minister to keep the Governor informed of his performance. The Governor will also fulfil all those responsibilities that are laid on him from time to time by the President.',
  'تمام صوبائی احکامات گورنر کے نام پر کیے جاتے ہیں۔ بیشتر امور میں گورنر، وزیرِ اعلیٰ اور صوبائی کابینہ کے مشورہ کا پابند ہے۔ وزیرِ اعلیٰ کا فرض ہے کہ گورنر کو اپنی کارکردگی سے باخبر رکھے۔ گورنر ان تمام ذمہ داریوں کو بھی پورا کرے گا جو اس پر وقتاً فوقتاً صدر کی جانب سے عائد کی جائیں گی۔',
  'ټول ولایتي امرونه د والي په نوم صادرېږي. په ډېرو چارو کې والي د اعلی وزیر او ولایتي کابینې د مشورې پابند دی. د اعلی وزیر دنده ده چې والي له خپلې کارکردګۍ خبر وساتي. والي به هغه ټول مسؤولیتونه هم پوره کوي چې وخت ناوخت د ولسمشر له خوا پرې لګول کېږي.')
H('Judicial powers', 'عدالتی اختیارات', 'قضايي واکونه')
P('When appointing the judges of the High Court, the President of the state also consults the Governor of the concerned province.',
  'ہائی کورٹ کے ججوں کا تقرر کرتے وقت صدرِ مملکت متعلقہ صوبہ کے گورنر سے بھی صلاح و مشورہ کرتا ہے۔',
  'د عالي محکمې د قاضیانو د ټاکلو پر وخت ولسمشر د اړوند ولایت له والي سره هم مشوره کوي.')
H('Duties during emergency', 'ہنگامی حالات کے دوران فرائض', 'د بېړني حالت پر مهال دندې')
P('When an emergency is imposed in the whole country or any part of the country, then after the declaration of emergency, at the behest of the federal government the Governor can himself exercise all those powers which any provincial institution other than the provincial assembly had. Thus all executive powers pass to the Governor.',
  'جب پورے ملک یا ملک کے کسی حصہ میں ہنگامی حالات کا نفاذ کیا جاتا ہے تو ہنگامی حالات کے اعلان کے بعد وفاقی حکومت کے ایما پر گورنر ایسے تمام اختیارات کا خود استعمال کر سکتا ہے جو صوبائی اسمبلی کے سوا کسی بھی صوبائی ادارے کو حاصل تھے۔ اس طرح تمام انتظامی اختیارات گورنر کے پاس چلے جاتے ہیں۔',
  'کله چې په ټول هېواد یا د هېواد په کومه برخه کې بېړنی حالت اعلان شي، نو د بېړني حالت له اعلان وروسته د فدرالي حکومت په غوښتنه والي پخپله هغه ټول واکونه کارولی شي چې له ولایتي اسمبلۍ پرته د هرې ولایتي ادارې سره وو. په دې ډول ټول اجرايي واکونه والي ته ورځي.')
H('The provincial cabinet', 'صوبائی کابینہ (The Provincial Cabinet)', 'ولایتي کابینه (The Provincial Cabinet)')
P('Because the parliamentary principle prevails in the provincial government, the real executive powers belong to the provincial Chief Minister and his cabinet. According to Article 129 of the constitution, “the provincial government will exercise its powers regarding provincial administration in the name of the Governor.” In the provincial government the Chief Minister and the ministers will perform their duties under the supervision of the Governor, who will have the status of head. According to the constitution the Governor will appoint as Chief Minister that person who has the support of the majority of members in the concerned provincial assembly.',
  'صوبائی حکومت میں پارلیمانی اصول رائج ہونے کے باعث اصل انتظامی اختیارات صوبائی وزیرِ اعلیٰ اور اس کی کابینہ کو حاصل ہیں۔ آئین کی دفعہ 129 کے مطابق ’’صوبائی حکومت صوبائی نظم و نسق کے سلسلے میں اپنے اختیارات کا استعمال گورنر کے نام پر کرے گی۔‘‘ صوبائی حکومت میں وزیرِ اعلیٰ اور وزراء اپنے فرائض گورنر کی زیرِ نگرانی سرانجام دیں گے، جسے سربراہ کی حیثیت حاصل ہوگی۔ آئین کے مطابق گورنر ایسے شخص کو وزیرِ اعلیٰ مقرر کرے گا جسے متعلقہ صوبائی اسمبلی میں اکثریتی ارکان کی حمایت حاصل ہو۔',
  'په ولایتي حکومت کې د پارلماني اصل د رواج له امله اصلي اجرايي واکونه ولایتي اعلی وزیر او د هغه کابینې ته حاصل دي. د اساسي قانون د ۱۲۹مې مادې سره سم "ولایتي حکومت به د ولایتي ادارې په برخه کې خپل واکونه د والي په نوم کاروي." په ولایتي حکومت کې اعلی وزیر او وزیران به خپلې دندې د والي تر څارنې لاندې ترسره کوي، چې د مشر حیثیت به ولري. د اساسي قانون سره سم والي به هغه کس اعلی وزیر ټاکي چې په اړوندې ولایتي اسمبلۍ کې د اکثریت غړو ملاتړ ورسره وي.')
H('The provincial assembly', 'صوبائی اسمبلی', 'ولایتي اسمبلي')
P('According to the constitution the provincial assembly consists of only one house. The number of seats in the provincial assemblies is as follows.',
  'آئین کے مطابق صوبائی اسمبلی صرف ایک ہی ایوان پر مشتمل ہوتی ہے۔ صوبائی اسمبلی میں نشستوں کی تعداد یوں ہے۔',
  'د اساسي قانون سره سم ولایتي اسمبلي یوازې له یوې جرګې جوړه وي. په ولایتي اسمبلیو کې د څوکیو شمېر دا دی:')
rows = [('Province of Balochistan (total seats)', 'صوبہ بلوچستان (کل نشستیں)', 'بلوچستان ولایت (ټولې څوکۍ)', '65'), ('Province of Khyber Pakhtunkhwa', 'صوبہ خیبر پختونخوا', 'خیبر پښتونخوا ولایت', '145'),
        ('Province of Sindh', 'صوبہ سندھ', 'سند ولایت', '168'), ('Province of Punjab', 'صوبہ پنجاب', 'پنجاب ولایت', '371')]
t.table('pak12-pa-seats', ['Province', 'Total seats'], [[r[0], r[3]] for r in rows], ['صوبہ', 'کل نشستیں'], ['ولایت', 'ټولې څوکۍ'], [[r[1], r[3]] for r in rows], [[r[2], r[3]] for r in rows])
rec = BOOK.record(t, 'pak12-ch5-text-4', 'Chapter 5 text (4)', 'بابِ پنجم — متن (۴)', 'پنځم څپرکی — متن (۴)', 51, [91, 92, 93])
rec['sourceNote'] = 'The provincial-assembly seat list begins at the foot of p.92 (Balochistan 65) and continues at the top of p.93 (KP 145, Sindh 168, Punjab 371); it is reconstructed here as one structured table.'

if __name__ == '__main__':
    BOOK.save(51, [(5, rec)])
