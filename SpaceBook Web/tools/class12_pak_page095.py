"""Pak Studies XII PDF95 (spread): printed pp.179–180 — Ch.9 Fifth Plan targets 4–11, outlay, review 1–11; Sixth Plan (1983–88) aims 1–8; Seventh Plan (1988–93) aims 1–2."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h
L = lambda rows: t.group('lines', rows)
L([('4. Raising the rate of domestic savings to 12.57 per cent.', '4۔ اندرونِ ملک بچتوں کی شرح 12.57 فیصد تک بڑھانا۔', '۴. د کورنیو سپمو کچه ۱۲.۵۷ سلنې ته لوړول.'),
   ('5. Increasing exports at the rate of 11 per cent annually.', '5۔ برآمدات میں 11 فیصد سالانہ کے حساب سے اضافہ کرنا۔', '۵. په صادراتو کې په کلنۍ ۱۱ سلنه حساب زیاتوالی.'),
   ('6. Increasing petroleum production to such an extent that more than 33 per cent of the total requirement can be met from domestic production.', '6۔ پیٹرولیم کی پیداوار میں اس حد تک اضافہ کرنا کہ کل ضرورت کا 33 فیصد سے زیادہ اندرونِ ملک پیداوار سے پورا کیا جا سکے۔', '۶. د پټرولیم په تولید کې دومره زیاتوالی چې د ټولې اړتیا له ۳۳ سلنې زیات له کورني تولید پوره شي.'),
   ('7. Increasing per-capita income by up to 9.2 per cent annually.', '7۔ فی کس آمدنی میں 9.2 فیصد تک سالانہ اضافہ کرنا۔', '۷. په سړي سر عاید کې تر ۹.۲ سلنې کلنی زیاتوالی.'),
   ('8. Increasing the per-capita production of energy by about 42 per cent.', '8۔ توانائی کی فی کس پیداوار میں تقریباً 42 فیصد اضافہ کرنا۔', '۸. د انرژۍ په سړي سر تولید کې شاوخوا ۴۲ سلنه زیاتوالی.'),
   ('9. Emphasising the development of rural areas and increasing the health sector in every respect; establishing new health units and hospitals; making room in hospitals for the treatment of more patients; increasing the number of doctors and nurses.', '9۔ دیہی علاقوں کی ترقی پر زور دینا اور صحت کے شعبے میں ہر جہت سے اضافہ کرنا۔ نئے ہیلتھ یونٹ اور ہسپتال قائم کرنا۔ ہسپتالوں میں مزید بیماروں کے علاج کی گنجائش نکالنا، ڈاکٹروں اور نرسوں کی تعداد میں اضافہ کرنا۔', '۹. د کلیوالو سیمو پر پرمختګ ټینګار او د روغتیا برخه له هر اړخه زیاتول؛ نوي روغتیايي واحدونه او روغتونونه جوړول؛ په روغتونونو کې د نورو ناروغانو د درملنې ځای پیدا کول؛ د ډاکټرانو او نرسانو شمېر زیاتول.'),
   ('11. Investing in basic industry and the engineering industry.', '11۔ بنیادی صنعت اور انجینئرنگ کی صنعت میں سرمایہ کاری کرنا۔', '۱۱. په بنسټیز صنعت او انجنیري صنعت کې پانګونه.')])
P('The estimate of the Fifth Five-Year Plan was 21.02 billion rupees. Of this, 14.82 billion rupees had been allocated for the government sectors and 6.20 billion rupees for the private sector.',
  'پانچویں پانچ سالہ منصوبے کا تخمینہ 21.02 بلین روپے تھا۔ اس میں سے 14.82 بلین روپے سرکاری شعبہ جات کے لیے اور 6.20 بلین روپے پرائیویٹ شعبے کے لیے مختص کیے گئے تھے۔',
  'د پنځم پنځه کلن پلان اټکل ۲۱.۰۲ میلیارده روپۍ و. له دې څخه ۱۴.۸۲ میلیارده روپۍ دولتي برخو ته او ۶.۲۰ میلیارده روپۍ خصوصي سکتور ته ځانګړې شوې وې.')
P('The Fifth Five-Year Plan came to an end in June 1983. During this period international conditions were quite unfavourable. Developing countries in particular could not remain without being affected by these unfavourable international conditions. Pakistan too could not escape these conditions. Despite this, this plan was successful in some sectors. According to a review of the government:',
  'پانچواں پانچ سالہ منصوبہ جون 1983ء کو اختتام پذیر ہوا۔ اس مدت کے دوران بین الاقوامی حالات کافی ناسازگار تھے۔ ترقی پذیر ممالک بالخصوص ان ناسازگار بین الاقوامی حالات سے متاثر ہوئے بغیر نہ رہ سکے۔ پاکستان بھی ان حالات سے نہ بچ سکا۔ اس کے باوجود یہ منصوبہ بعض شعبوں میں کامیاب رہا۔ حکومت کے ایک جائزے کے مطابق',
  'پنځم پنځه کلن پلان د ۱۹۸۳ز په جون کې پای ته ورسېد. په دې موده کې نړیوال حالات ډېر نامناسب وو. پرمختیايي هېوادونه په ځانګړي ډول له دې نامناسبو نړیوالو حالاتو پرته له اغېزمنېدو پاتې نه شول. پاکستان هم له دې حالاتو ونه ژغورل شو. سره له دې دا پلان په ځینو برخو کې بریالی و. د حکومت د یوې کتنې له مخې:')
L([('1. The Fifth Five-Year Plan completed ninety per cent of its target.', '1۔ پانچویں پانچ سالہ منصوبے نے اپنے نوے فیصد ہدف مکمل کر لیے۔', '۱. پنځم پنځه کلن پلان خپل نوي سلنه هدف بشپړ کړ.'),
   ('2. Despite unfavourable conditions the rate of increase of 6 per cent annually could be maintained.', '2۔ ناسازگار حالات کے باوجود 6 فیصد سالانہ اضافے کی شرح کو برقرار رکھا جا سکا۔', '۲. د نامناسبو حالاتو سره سره د کلنۍ ۶ سلنه زیاتوالي کچه وساتل شوه.'),
   ('3. The pace of progress in the less-developed areas of the country improved.', '3۔ ملک کے کم ترقی یافتہ علاقوں میں ترقی کی رفتار بہتر ہوئی۔', '۳. د هېواد په لږ پرمختللو سیمو کې د پرمختګ چټکتیا ښه شوه.'),
   ('4. In the province of Balochistan there was a fivefold increase in respect of development expenditure.', '4۔ صوبہ بلوچستان میں ترقیاتی اخراجات کے ضمن میں پانچ گنا اضافہ ہوا۔', '۴. د بلوچستان په ولایت کې د پراختیايي لګښتونو په برخه کې پنځه چنده زیاتوالی راغی.'),
   ('5. During the term of this plan special attention was given to the development of rural areas.', '5۔ اس منصوبے کی مدت کے دوران دیہی علاقوں کی ترقی کی طرف بالخصوص توجہ دی گئی۔', '۵. د دې پلان په موده کې د کلیوالو سیمو پرمختګ ته ځانګړې پاملرنه وشوه.'),
   ('6. At least 20 per cent of destitute, impoverished people received economic assistance by virtue of the system of zakat. This is a big step towards social and economic justice.', '6۔ کم از کم 20 فیصد نادار، مفلوک الحال لوگوں کو نظامِ زکوٰۃ کی بدولت معاشی اعانت ملی۔ سماجی و معاشی انصاف کی طرف یہ ایک بڑا قدم ہے۔', '۶. لږ تر لږه ۲۰ سلنه بې‌وزلو، بدحاله خلکو ته د زکات د نظام له برکته اقتصادي مرسته ورسېده. د ټولنیز او اقتصادي عدالت په لور دا یو لوی ګام دی.'),
   ('7. In the matter of food there was self-sufficiency to some extent.', '7۔ خوراک کے معاملے میں کسی قدر خود کفالت ہوئی۔', '۷. د خوړو په برخه کې تر یوه بریده ځان‌بسیاینه راغله.'),
   ('8. The rate of inflation, from 16 per cent five years earlier, decreased to only 5 per cent.', '8۔ افراطِ زر پانچ سال قبل کی شرح 16 فیصد سے کم ہو کر صرف 5 فیصد رہ گیا۔', '۸. د انفلاسیون کچه له پنځه کاله مخکې ۱۶ سلنې څخه یوازې ۵ سلنې ته راټیټه شوه.'),
   ('9. Industrial production made progress of 9 per cent annually.', '9۔ صنعتی پیداوار میں 9 فیصد سالانہ ترقی ہوئی۔', '۹. په صنعتي تولید کې کلنی ۹ سلنه پرمختګ وشو.'),
   ('10. To increase national industry, industrial concessions too were given.', '10۔ ملکی صنعت میں اضافے کی غرض سے صنعتی چھوٹیں بھی دی گئیں۔', '۱۰. د هېواد د صنعت د زیاتولو لپاره صنعتي معافیتونه هم ورکړل شول.'),
   ('11. The number of villages provided with electricity under this five-year plan was greater than in the thirty years before it.', '1۔ اس پانچ سالہ منصوبے کے تحت جتنے دیہاتوں کو بجلی فراہم کی گئی ان کی تعداد اس سے قبل کے تیس سالوں سے زیادہ تھی۔', '۱۱. د دې پنځه کلن پلان له مخې چې څومره کلیو ته برېښنا ورسول شوه، شمېر یې له دې مخکې د دېرشو کلونو څخه زیات و.')])
H('Sixth Five-Year Plan (1983 to 1988)', 'چھٹا پانچ سالہ منصوبہ (1983ء تا 1988ء)', 'شپږم پنځه کلن پلان (۱۹۸۳ تر ۱۹۸۸ز)')
P('The Sixth Five-Year Plan was started on 1 July 1983. The basic objectives of this plan were as follows:',
  'چھٹا پانچ سالہ منصوبہ یکم جولائی 1983ء کو شروع کیا گیا۔ اس منصوبے کے بنیادی مقاصد درج ذیل تھے:۔',
  'شپږم پنځه کلن پلان د ۱۹۸۳ز د جولای په لومړۍ پیل شو. د دې پلان بنسټیزې موخې دا وې:')
L([('1. Accelerating the pace of economic progress.', '1۔ معاشی ترقی کی رفتار کو تیز کرنا۔', '۱. د اقتصادي پرمختګ چټکتیا ګړندۍ کول.'),
   ('2. Reviving social justice.', '2۔ سماجی انصاف کا احیاء کرنا۔', '۲. د ټولنیز عدالت بیا ژوندي کول.'),
   ('3. Giving special importance to rural development.', '3۔ دیہی ترقی کو خاص اہمیت دینا۔', '۳. کلیوالي پرمختګ ته ځانګړی اهمیت ورکول.'),
   ('4. Spreading a network of roads in the villages and linking them with urban markets.', '4۔ دیہات میں سڑکوں کا جال بچھا کر انھیں شہری منڈیوں کے ساتھ منسلک کرنا۔', '۴. په کلیو کې د سړکونو جال غوړول او له ښاري بازارونو سره یې نښلول.'),
   ('5. Providing electricity to as many rural areas as possible so that a pleasant revolution in the rural economy becomes possible.', '5۔ زیادہ سے زیادہ دیہی علاقوں میں بجلی فراہم کرنا تاکہ دیہی معیشت میں ایک خوش گوار انقلاب ممکن ہو سکے۔', '۵. تر ټولو ډېرو کلیوالو سیمو ته برېښنا رسول، څو په کلیوالي اقتصاد کې یو ښه انقلاب شونی شي.'),
   ('6. Giving preference to the sectors of education and health under the plan.', '6۔ منصوبے کے تحت تعلیم و صحت کے شعبوں کو ترجیح دینا۔', '۶. د پلان له مخې د زده‌کړې او روغتیا برخو ته لومړیتوب ورکول.'),
   ('7. Implementing a special programme for the increase of employment and income throughout the country.', '7۔ ملک بھر میں روزگار اور آمدنی میں اضافے کے لیے ایک خاص پروگرام پر عمل کرنا۔', '۷. په ټول هېواد کې د روزګار او عاید د زیاتوالي لپاره پر یوه ځانګړي پروګرام عمل.'),
   ('8. Through zakat and the ushr system, financial assistance to more than 1.5 million deserving people.', '8۔ زکوٰۃ اور نظامِ عشر کے توسط سے 1.5 ملین سے زیادہ مستحقین کی مالی اعانت کرنا۔', '۸. د زکات او عشر د نظام له لارې له ۱.۵ میلیونو زیاتو مستحقینو سره مالي مرسته.')])
H('Seventh Five-Year Plan (1988 to 1993)', 'ساتواں پانچ سالہ منصوبہ (1988ء تا 1993ء)', 'اووم پنځه کلن پلان (۱۹۸۸ تر ۱۹۹۳ز)')
P('The outline of the basic objectives of the Seventh Five-Year Plan is as follows:',
  'ساتویں پانچ سالہ منصوبے کے بنیادی مقاصد کا خاکہ درج ذیل ہے:۔',
  'د اووم پنځه کلن پلان د بنسټیزو موخو خاکه دا ده:')
L([('1. Providing employment opportunities so that at least educated individuals do not fall victim to unemployment.', '1۔ روزگار کے مواقع فراہم کرنا تاکہ کم از کم تعلیم یافتہ افراد بے روزگاری کا شکار نہ ہوں۔', '۱. د روزګار فرصتونه برابرول، څو لږ تر لږه لوستي کسان د بې‌روزګارۍ ښکار نه شي.'),
   ('2. Providing basic needs, for example food, housing, health, education and other facilities, on a priority basis.', '2۔ بنیادی ضروریات مثلاً خوراک، رہائش، صحت، تعلیم و دیگر سہولیات کو ترجیحی بنیادوں پر فراہم کرنا۔', '۲. بنسټیزې اړتیاوې لکه خواړه، استوګنه، روغتیا، زده‌کړه او نورې اسانتیاوې په لومړیتوب برابرول.')])
rec = BOOK.record(t, 'pak12-ch9-text-12', 'Chapter 9 text (12)', 'بابِ نہم — متن (۱۲)', 'نهم څپرکی — متن (۱۲)', 95, [179, 180])
rec['sourceNote'] = 'The first list continues the Fifth Plan targets from p.178. The Seventh Plan objectives list continues on p.181 (PDF96).'
issues = [{'id': 'pak12-pdf095', 'unit': 9, 'printedPage': 179,
           'description': 'The Fifth Plan target list on p.179 skips item 10 (9 is followed by 11); the review list on p.180 numbers its eleventh item “1”. Retained (the structured list keeps 11 and renders the review item as 11). The outlay of 21.02 billion appears inconsistent with earlier plans (likely 210.2) — retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(95, [(9, rec)], issues=issues)
