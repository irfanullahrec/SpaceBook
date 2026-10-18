"""Pak Studies XII PDF96 (spread): printed pp.181–182 — Ch.9 Seventh Plan aims 3–6; Eighth Plan (1993–98) aims 1–11; overall review."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h
L = lambda rows: t.group('lines', rows)
L([('3. Making manpower trained.', '3۔ افرادی قوت کو تربیت یافتہ بنانا۔', '۳. بشري ځواک روزل شوی کول.'),
   ('4. Strengthening the national economy by working on the principle of “self-help”.', '4۔ ’’اپنی مدد آپ‘‘ کے اصول پر کام کرتے ہوئے قومی معیشت کو مضبوط بنانا۔', '۴. د "ځان سره مرسته" پر اصل کار کولو سره ملي اقتصاد پیاوړی کول.'),
   ('5. In view of the importance of the private sector, giving it its due place and making it active for the national economy.', '5۔ نجی شعبے کی اہمیت کے پیشِ نظر اسے اس کا جائز مقام دے کر ملکی معیشت کے لیے فعال بنانا۔', '۵. د خصوصي سکتور د اهمیت په پام کې نیولو سره هغه ته خپل مشروع ځای ورکول او د هېواد اقتصاد لپاره یې فعالول.'),
   ('6. Depending as little as possible on foreign aid.', '6۔ غیر ملکی امداد پر کم سے کم انحصار کرنا۔', '۶. پر بهرنۍ مرستې تر ټولو لږه تکیه کول.')])
H('Eighth Five-Year Plan (1993 to 1998)', 'آٹھواں پانچ سالہ منصوبہ (1993ء تا 1998ء)', 'اتم پنځه کلن پلان (۱۹۹۳ تر ۱۹۹۸ز)')
P('The basic objectives of the Eighth Five-Year Plan were as follows:',
  'آٹھویں پانچ سالہ منصوبے کے بنیادی مقاصد حسبِ ذیل تھے:۔',
  'د اتم پنځه کلن پلان بنسټیزې موخې دا وې:')
L([('1. Increasing national income by 7 per cent annually.', '1۔ قومی آمدنی میں سالانہ 7 فیصد اضافہ کرنا۔', '۱. په ملي عاید کې کلنۍ ۷ سلنه زیاتوالی.'),
   ('2. Increasing the agricultural sector by 4.9 per cent annually.', '2۔ زرعی شعبہ میں سالانہ 4.9 فیصد اضافہ کرنا۔', '۲. په کرنیزه برخه کې کلنۍ ۴.۹ سلنه زیاتوالی.'),
   ('3. Increasing per-capita income by up to twenty-two per cent during the eighth plan.', '3۔ آٹھویں منصوبے کے دوران فی کس آمدنی میں بائیس فیصد تک اضافہ کرنا۔', '۳. د اتم پلان په موده کې په سړي سر عاید کې تر دوه‌ویشت سلنې زیاتوالی.'),
   ('4. Creating employment opportunities for 6.2 million unemployed individuals.', '4۔ 6.2 ملین بے روزگار افراد کے لیے روزگار کے مواقع پیدا کرنا۔', '۴. د ۶.۲ میلیونو بې‌روزګارو کسانو لپاره د روزګار فرصتونه پیدا کول.'),
   ('5. Increasing the proportion of national savings to 19.9%.', '5۔ قومی بچتوں کے تناسب میں 19.9% تک اضافہ کرنا', '۵. د ملي سپمو تناسب تر ۱۹.۹٪ زیاتول.'),
   ('6. By the end of the eighth plan, reducing the budget deficit and bringing it equal to 4 per cent of GDP.', '6۔ آٹھویں منصوبے کے آخر تک بجٹ خسارہ کم کر کے جی۔ڈی۔پی کے 4 فیصد کے برابر لانا۔', '۶. د اتم پلان تر پایه د بودیجې کسر کمول او د ناخالص کورني تولید ۴ سلنې سره برابرول.'),
   ('7. In this plan, reducing the rate of population growth from 2.9 per cent to 2.7 per cent.', '7۔ اس منصوبے میں آبادی کی شرح افزائش کو 2.9 فیصد سے کم کر کے 2.7 فیصد تک کرنا۔', '۷. په دې پلان کې د نفوس د ودې کچه له ۲.۹ سلنې ۲.۷ سلنې ته راټیټول.'),
   ('8. Increasing the literacy rate to 48 per cent.', '8۔ شرحِ خواندگی میں 48 فیصد تک اضافہ کرنا۔', '۸. د سواد کچه تر ۴۸ سلنې لوړول.'),
   ('9. Reducing the infant mortality rate from 86 per thousand to 65 per thousand', '9۔ بچوں کی شرحِ اموات 86 فی ہزار سے کم کر کے 65 فی ہزار کرنا', '۹. د ماشومانو د مړینې کچه له ۸۶ په زرو څخه ۶۵ په زرو ته راټیټول'),
   ('10. Providing clean drinking water to 70.5 per cent of the population of villages and 95 per cent of the population of cities.', '10۔ دیہات کی 70.5 فیصد اور شہروں کی 95 فیصد آبادی کو پینے کا صاف پانی مہیا کرنا۔', '۱۰. د کلیو ۷۰.۵ سلنه او د ښارونو ۹۵ سلنه نفوس ته د څښلو پاکې اوبه برابرول.'),
   ('11. Providing basic health facilities at the level of every union council.', '11۔ ہر یونین کونسل کی سطح پر صحت کی بنیادی سہولیات مہیا کرنا۔', '۱۱. د هرې اتحادیې شورا په کچه بنسټیزې روغتیايي اسانتیاوې برابرول.')])
H('Overall review', 'مجموعی جائزہ', 'ټولیزه کتنه')
P('In all the five-year development plans made so far in Pakistan, there were certainly some basic weaknesses and technical faults. Besides this, there are the internal and external reasons — political chaos, drought, the Pakistan–India wars and Afghan refugees etc. — because of which no five-year plan could succeed in achieving its targets. Only the Second Five-Year Plan (1960 to 1965) was crowned with considerable success. However, according to the details of the Economic Survey of Pakistan, during the financial year (2003–2004) there has been an increase in dearness, unemployment, the trade deficit and inflation, while a reduction occurred in foreign loans and an increase in the reserves of foreign exchange. Per-capita income rose from 562 dollars annually to 652 dollars. Moreover the balance of the government’s income and expenditure remained within limits, and the difference has remained only 13 billion rupees, which a few years earlier was up to 76 billion rupees.',
  'پاکستان میں اب تک جتنے بھی پانچ سالہ ترقیاتی منصوبے بنائے گئے ہیں اُن میں کچھ بنیادی کمزوریاں اور تکنیکی خرابیاں ضرور تھیں۔ اس کے علاوہ سیاسی افراتفری، خشک سالی، پاک بھارت جنگیں اور افغان مہاجرین وغیرہ وہ اندرونی و بیرونی وجوہات ہیں جن کی بنا پر کوئی بھی پانچ سالہ منصوبہ اپنے اہداف حاصل کرنے میں کامیاب نہ ہو سکا۔ صرف دوسرا پانچ سالہ منصوبہ (1960ء تا 1965ء) کافی کامیابی سے ہمکنار رہا۔ تاہم اکنامک سروے آف پاکستان کی تفصیلات کے مطابق (2003ء-2004ء) کے مالی سال کے دوران مہنگائی، بیروزگاری، تجارتی خسارے اور افراطِ زر میں اضافہ ہوا ہے۔ جب کہ بیرونی قرضوں میں کمی واقع ہوئی اور زرِ مبادلہ کے ذخائر میں اضافہ ہوا۔ فی کس آمدنی 562 ڈالر سالانہ سے بڑھ کر 652 ڈالر ہو گئی۔ نیز حکومت کی آمدنی و اخراجات کا توازن حدود میں رہا اور صرف 13 بلین روپے کا فرق رہ گیا ہے۔ جو چند سال پہلے تک 76 بلین روپے تھا۔',
  'په پاکستان کې تر اوسه چې څومره پنځه کلن پراختیايي پلانونه جوړ شوي، په هغو کې ځینې بنسټیزې کمزورۍ او تخنیکي خرابۍ خامخا وې. سربېره پر دې سیاسي ګډوډي، وچکالي، د پاک-هند جګړې او افغان کډوال او نور هغه کورني او بهرني لاملونه دي چې له امله یې هېڅ پنځه کلن پلان په خپلو هدفونو کې بریالی نه شو. یوازې دویم پنځه کلن پلان (۱۹۶۰ تر ۱۹۶۵ز) ډېر بریالی و. خو د پاکستان د اقتصادي سروې د تفصیلاتو له مخې د (۲۰۰۳-۲۰۰۴ز) مالي کال په موده کې په ګرانۍ، بې‌روزګارۍ، سوداګریز کسر او انفلاسیون کې زیاتوالی راغلی، په داسې حال کې چې په بهرنیو پورونو کې کمښت او د اسعارو په زېرمو کې زیاتوالی راغی. سړي سر عاید له کلنۍ ۵۶۲ ډالرو ۶۵۲ ډالرو ته لوړ شو. همداراز د حکومت د عاید او لګښت توازن په پولو کې پاتې شو او یوازې ۱۳ میلیارده روپۍ توپیر پاتې دی، چې څو کاله مخکې تر ۷۶ میلیارده روپیو و.')
rec = BOOK.record(t, 'pak12-ch9-text-13', 'Chapter 9 text (13)', 'بابِ نہم — متن (۱۳)', 'نهم څپرکی — متن (۱۳)', 96, [181, 182])
rec['sourceNote'] = 'The first list continues the Seventh Plan objectives from p.180. The “overall review” paragraph runs across the page turn from p.181 to p.182; the rest of p.182 is blank in print.'
issues = [{'id': 'pak12-pdf096', 'unit': 9, 'printedPage': 181, 'description': 'Decorative pink borders on pp.181–182 and the coloured “مجموعی جائزہ” label are page ornament (not reproduced).'}]

if __name__ == '__main__':
    BOOK.save(96, [(9, rec)], issues=issues)
