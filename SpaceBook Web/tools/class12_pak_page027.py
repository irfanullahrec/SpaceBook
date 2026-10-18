"""Pak Studies XII PDF27 (spread): p.45 Ch.2 Questions Q3–Q9; p.46 Chapter 3 'ارضِ پاکستان' opening."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.p('3. Identify the correct and incorrect among the following.', '3۔ مندرجہ ذیل میں سے صحیح اور غلط کی نشاندہی کریں۔', '۳. په لاندې کې سمې او ناسمې په نښه کړئ.')
L([('i. Sir Cyril Radcliffe presented the plan for the partition of India.', 'i۔ سر سائیرل ریڈکلف نے ہندوستان کی تقسیم کا منصوبہ پیش کیا۔', 'i. سر سیرل رډکلیف د هندوستان د وېش پلان وړاندې کړ.'),
   ('ii. With the inclusion of Pathankot in Bharat it got the land route to reach Kashmir.', 'ii۔ بھارت میں پٹھان کوٹ کی شمولیت سے اُسے کشمیر تک پہنچنے کا زمینی راستہ مل گیا۔', 'ii. په بهارت کې د پټهانکوټ په شاملېدو هغه ته کشمیر ته د رسېدو ځمکنۍ لار ورکړل شوه.'),
   ('iii. Calcutta was the capital of the province of Bengal.', 'iii۔ کلکتہ صوبہ بنگال کا دارالخلافہ تھا۔', 'iii. کلکته د بنګال ولایت پلازمېنه وه.'),
   ('iv. After the establishment of Pakistan the country did not face any shortage of government employees.', 'iv۔ قیامِ پاکستان کے بعد ملک کو سرکاری ملازمین کی کوئی کمی درپیش نہ ہوئی۔', 'iv. د پاکستان له جوړېدو وروسته هېواد ته د دولتي کارکوونکو هېڅ کمښت پېښ نه شو.'),
   ('v. Gandhi helped get Pakistan its share in the joint assets.', 'v۔ گاندھی نے پاکستان کو مشترکہ اثاثوں میں حصہ دلوانے میں مدد کی۔', 'v. ګاندي د ګډو شتمنیو په برخه کې پاکستان ته د برخې په ورکولو کې مرسته وکړه.')])
e.p('4. Write short answers to the following.', '4۔ درج ذیل کے مختصر جوابات لکھیں۔', '۴. لاندې ته لنډ ځوابونه ولیکئ.')
L([('i. Which areas acquired disputed status under the Radcliffe Award?', 'i۔ ریڈکلف ایوارڈ کے تحت کون سے علاقے متنازعہ حیثیت اختیار کر گئے؟', 'i. د رډکلیف پرېکړې له مخې کومې سیمې شخړه‌ییزې شوې؟'),
   ('ii. Why was Pakistan entangled in problems at the time of partition?', 'ii۔ تقسیمِ ہند کے وقت پاکستان کو کیوں مسائل میں اُلجھا دیا گیا؟', 'ii. د هند د وېش پر وخت پاکستان ولې په ستونزو کې ونښلول شو؟'),
   ('iii. Why was the Muslim-majority area of district Gurdaspur included in Bharat?', 'iii۔ ضلع گورداسپور مسلم اکثریت والا علاقہ کیوں بھارت میں شامل کر دیا گیا؟', 'iii. د ګورداسپور ولسوالۍ مسلم اکثریت سیمه ولې په بهارت کې شامله شوه؟'),
   ('iv. Why was Field Marshal Auchinleck removed from his post?', 'iv۔ فیلڈ مارشل آچنلک کو اُس کے عہدے سے کیوں ہٹا دیا گیا؟', 'iv. فیلډ مارشال اوچنلک ولې له خپلې څوکۍ لرې شو؟'),
   ('v. What did the Quaid-e-Azam urge students most?', 'v۔ قائدِاعظم نے طلبہ کو کس بات کی زیادہ تلقین کی؟', 'v. قائد اعظم زده‌کوونکو ته د کومې خبرې ډېر تلقین وکړ؟')])
L([('5. Keeping the historical background in view, present a possible solution to the Kashmir problem.', '5۔ تاریخی پس منظر کو سامنے رکھتے ہوئے مسئلہ کشمیر کا امکانی حل پیش کریں۔', '۵. تاریخي شالید په پام کې نیولو سره د کشمیر د مسئلې شوني حل وړاندې کړئ.'),
   ('6. Why did the canal water dispute arise between Pakistan and Bharat? What steps did both countries take to solve it? Write a comprehensive note.', '6۔ پاکستان اور بھارت میں نہری تنازعہ کیوں پیدا ہوا؟ دونوں ممالک نے اس کے حل کے لیے کیا اقدامات کیے؟ ایک جامع نوٹ لکھیں۔', '۶. د پاکستان او بهارت ترمنځ د ویالو د اوبو شخړه ولې پیدا شوه؟ دواړو هېوادونو د هغې د حل لپاره څه ګامونه پورته کړل؟ یو جامع یادښت ولیکئ.'),
   ('7. Throw light on the leadership abilities of the Quaid-e-Azam as Governor-General of Pakistan.', '7۔ پاکستان کے گورنر جنرل کی حیثیت سے قائدِاعظم کی قائدانہ صلاحیتوں پر روشنی ڈالیں۔', '۷. د پاکستان د ګورنر جنرال په توګه د قائد اعظم پر مشرتابه وړتیاوو رڼا واچوئ.'),
   ('8. Which qualities are necessary for a good leader?', '8۔ ایک اچھے راہنما کے لیے کن کن خصوصیات کا ہونا ضروری ہے؟', '۸. د یوه ښه مشر لپاره کومې ځانګړنې اړینې دي؟'),
   ('9. In your opinion, what can be the best solution of disputes between nations? Discuss in the present global context.', '9۔ آپ کے خیال میں قوموں کے درمیان اختلافی مسائل کا بہترین حل کیا ہو سکتا ہے۔ موجودہ عالمی تناظر میں بحث کریں۔', '۹. ستاسو په نظر د ملتونو ترمنځ د اختلافي مسایلو غوره حل څه کېدای شي؟ د اوسني نړیوال حالت په رڼا کې بحث وکړئ.')])
ex = BOOK.record(e, 'pak12-ch2-exercise-2', 'Questions (2)', 'سوالات (۲)', 'پوښتنې (۲)', 27, [45])

t = Builder()
t.p('Chapter Three', 'بابِ سوم', 'درېیم څپرکی')
t.h('The Land of Pakistan', 'ارضِ پاکستان', 'د پاکستان ځمکه')
for x in [
 ('If we look at the map of the continent of Asia, we shall find that to its south lies a peninsula-like piece of land which is called South Asia. The Himalaya mountains and their branches separate it from the northern part of the continent. The land of Pakistan is spread in the north-western part of South Asia between longitudes 61° and 76° east and latitudes 24° and 37° north. Its total area is 796,096 square kilometres. Together with the Northern Areas and the Western Tribal Areas the total area becomes 868,591 square kilometres.',
  'براعظم ایشیا کے نقشے پر نظر ڈالیں تو معلوم ہوگا کہ اس کے جنوب میں ایک جزیرہ نما قطعہ زمین واقع ہے جو جنوبی ایشیا کہلاتا ہے۔ اس کو کوہِ ہمالیہ اور اس کی شاخیں براعظم کے شمالی حصے سے جدا کرتی ہیں۔ جنوبی ایشیا کے شمال مغربی حصے میں سرزمینِ پاکستان 61° اور 76° طول بلد مشرقی اور 24° اور 37° عرض بلد شمالی کے درمیان پھیلی ہوئی ہے۔ اس کا کل رقبہ 796096 مربع کلومیٹر ہے۔ شمالی علاقہ جات اور مغربی قبائلی علاقہ جات کو ملا کر کل رقبہ 868591 مربع کلومیٹر ہو جاتا ہے۔',
  'که د اسیا لویې وچې نقشې ته وګورو، معلومېږي چې په سویل کې یې یوه ټاپووزمه ډوله ځمکه پرته ده چې سویلي اسیا بلل کېږي. د همالیا غرونه او د هغو څانګې یې د لویې وچې له شمالي برخې جلا کوي. د سویلي اسیا په شمال لوېدیځه برخه کې د پاکستان خاوره د ۶۱° او ۷۶° ختیځ طول البلد او ۲۴° او ۳۷° شمالي عرض البلد ترمنځ پرته ده. ټوله مساحت یې ۷۹۶۰۹۶ مربع کیلومتره دی. د شمالي سیمو او لوېدیځو قبایلي سیمو په یوځای کولو ټوله مساحت ۸۶۸۵۹۱ مربع کیلومتره کېږي.'),
 ('To the north of Pakistan lie the mountain ranges of the Himalaya and the Karakoram. Here the Wakhan strip, an area of Afghanistan, separates Pakistan from Tajikistan. To the north-west lies Afghanistan. To the west is the Islamic country of Iran. To the north-east of Pakistan, besides the occupied state of Jammu and Kashmir, lie the areas of the People’s Republic of China, Xinjiang and Tibet. To the east lie the areas of Bharat, Punjab and Rajputana. To the south of Pakistan are the Arabian Sea and the Indian Ocean.',
  'پاکستان کے شمال میں کوہِ ہمالیہ اور کوہِ قراقرم کا پہاڑی سلسلہ ہے۔ یہاں افغانستان کے علاقے واخان کی ایک پٹی پاکستان کو تاجکستان سے جدا کرتی ہے۔ شمال مغرب میں افغانستان واقع ہے۔ مغرب میں ایران کا اسلامی ملک ہے۔ پاکستان کے شمال مشرق میں مقبوضہ ریاست جموں و کشمیر کے علاوہ جمہوریہ چین کے علاقے سینکیانگ (XINJIANG) اور تبت واقع ہیں۔ مشرق میں بھارت کے علاقے پنجاب اور راجپوتانہ واقع ہیں۔ پاکستان کے جنوب میں بحیرۂ عرب اور بحرِ ہند ہے۔',
  'د پاکستان په شمال کې د همالیا او قراقرم غرنۍ لړۍ دي. دلته د افغانستان د واخان سیمې یوه پټۍ پاکستان له تاجکستانه جلا کوي. په شمال لوېدیځ کې افغانستان پروت دی. په لوېدیځ کې د ایران اسلامي هېواد دی. د پاکستان په شمال ختیځ کې له نیول شوي جمون او کشمیر ریاست پرته د چین جمهوریت سیمې سینکیانګ (XINJIANG) او تبت پرتې دي. په ختیځ کې د بهارت سیمې پنجاب او راجپوتانه پرتې دي. د پاکستان په سویل کې عربي سمندر او هند سمندر دي.'),
 ('According to the census of 2017 our population has exceeded 207.7 million.',
  '2017ء کی مردم شماری کے مطابق ہماری آبادی 207.7 ملین سے تجاوز کر چکی ہے۔',
  'د ۲۰۱۷ز د سرشمېرنې له مخې زموږ نفوس له ۲۰۷.۷ میلیونو اوښتی دی.'),
]: t.p(*x)
t.h('Importance of Pakistan’s location', 'پاکستان کے محلِ وقوع کی اہمیت', 'د پاکستان د موقعیت اهمیت')
for x in [
 ('Pakistan is located, geographically and politically, at the centre of Asia and in one of the most sensitive regions of the world. Pakistan’s location is of great importance for international trade, regional integrity and the interests of the Islamic world. Only a few regions in the world are as important in terms of location.',
  'پاکستان جغرافیائی اور سیاسی لحاظ سے ایشیا کے مرکز اور دنیا کے حساس ترین خطے میں واقع ہے۔ پاکستان کا محلِ وقوع بین الاقوامی تجارت، علاقائی سالمیت، اور اسلامی دنیا کے مفادات کے لیے بہت اہمیت کا حامل ہے۔ دنیا میں چند ہی علاقے محلِ وقوع کے لحاظ سے اتنے اہم ہیں۔',
  'پاکستان په جغرافیایي او سیاسي لحاظ د اسیا په مرکز او د نړۍ په تر ټولو حساسه سیمه کې پروت دی. د پاکستان موقعیت د نړیوالې سوداګرۍ، سیمه‌ییزې بشپړتیا او د اسلامي نړۍ د ګټو لپاره ډېر اهمیت لري. په نړۍ کې یوازې څو سیمې د موقعیت له پلوه دومره مهمې دي.'),
 ('Pakistan lies in the middle of the Islamic world, which is spread from Morocco in the west to Indonesia in the east. In the north are the Muslim states of Central Asia and China’s province of Xinjiang. Most of these countries are rich in the wealth of oil. The Muslim countries of South-East Asia, with some mineral and agricultural products, …',
  'پاکستان دنیائے اسلام کے درمیان میں واقع ہے جو مغرب میں مراکش سے لے کر مشرق میں انڈونیشیا تک پھیلی ہوئی ہے۔ شمال میں وسطِ ایشیا کی مسلم ریاستیں اور چین کا صوبہ سینکیانگ ہے۔ ان میں سے اکثر ممالک تیل کی دولت سے مالا مال ہیں۔ جنوب مشرق کے مسلم ممالک بعض معدنی اور زرعی پیداوار کے …',
  'پاکستان د اسلامي نړۍ په منځ کې پروت دی، چې په لوېدیځ کې له مراکش نه تر ختیځ کې اندونیزیا پورې غځېدلې. په شمال کې د منځنۍ اسیا مسلمان هېوادونه او د چین سینکیانګ ولایت دی. ډېری دا هېوادونه د تېلو له شتمنۍ ډک دي. د سویل ختیځ مسلمان هېوادونه د ځینو کاني او کرنیزو تولیداتو …'),
]: t.p(*x)
UT = ('The Land of Pakistan', 'ارضِ پاکستان', 'د پاکستان ځمکه')
tx = BOOK.record(t, 'pak12-ch3-text-1', 'Chapter 3 text (1)', 'بابِ سوم — متن (۱)', 'درېیم څپرکی — متن (۱)', 27, [46], unit_title=UT)
issues = [{'id': 'pak12-pdf027', 'unit': 3, 'printedPage': 46, 'description': 'Contents list chapter 3 at p.46 and the legacy app chapter 3 has the same title; legacy units 3–11 titles partly differ from print (e.g. ch.7 Pakistani languages) and are superseded as each chapter is authored.'}]

if __name__ == '__main__':
    BOOK.save(27, [(2, ex), (3, tx)], issues=issues, complete_units=[2])
