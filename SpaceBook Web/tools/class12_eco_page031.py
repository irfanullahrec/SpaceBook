"""Economics XII PDF31–32: pp.42–45 — chapter 2 model paper: short questions 9–24; MCQs 1–24 (printed ✓ answer marks kept).
Run: python class12_eco_page031.py N (31–32)."""
import sys
from class12_eco_common import BOOK, Builder

QA = [
 ('9. Write the definition of standard money.', '9۔ معیاری زر کی تعریف لکھیں۔', '9. د معیاري پیسو تعریف ولیکئ.',
  'A. Such money whose face and real value are equal is called standard money, e.g. if metal worth as much sum has been used as the value written on the coin, such a coin will be called standard money.', 'جواب: ایسا زر جس کی ظاہری اور حقیقی مالیت برابر ہوں معیاری زر کہلاتا ہے۔ مثلاً جتنی رقم کی دھات استعمال ہوئی ہو، سکے پر اتنی کی مالیت درج ہو تو ایسا سکہ معیادی زر کہلائے گا۔', 'ځواب: هغه پیسې چې ښکاره او حقیقي ارزښت یې برابر وي، معیاري پیسې بلل کېږي؛ لکه څومره پیسو فلز چې کارول شوی وي، پر سکه هومره ارزښت لیکل شوی وي، نو داسې سکه معیاري پیسې بلل کېږي.'),
 ('10. What is token or nominal money called?', '10۔ علامتی یا وضعی زر کسے کہتے ہیں؟', '10. نښه‌یي یا وضعي پیسو ته څه وايي؟',
  'A. Such money whose face value is more but real value less is called token money, e.g. if metal of less value has been used on some coin but a greater value is written on it, such a coin will be counted as token money.', 'جواب: ایسا زر جس کی ظاہری مالیت زیادہ لیکن حقیقی مالیت کم ہو علامتی زر کہلاتا ہے۔ مثلاً اگر کسی سکے پر دھات کم مالیت کی استعمال ہوئی ہو لیکن اس پر زائد مالیت درج کر دی جائے تو ایسا سکہ علامتی زر میں شمار ہوگا۔', 'ځواب: هغه پیسې چې ښکاره ارزښت یې ډېر خو حقیقي ارزښت یې لږ وي، نښه‌یي پیسې بلل کېږي؛ لکه که پر کومه سکه د لږ ارزښت فلز کارول شوی وي خو ډېر ارزښت پرې لیکل شوی وي، داسې سکه به نښه‌یي پیسې وګڼل شي.'),
 ('11. Write the definition of legal money.', '11۔ قانونی زر کی تعریف لکھیں۔', '11. د قانوني پیسو تعریف ولیکئ.',
  'A. By it is meant that money which has to be accepted according to the law of the country, e.g. in Pakistan coins and notes are legal money.', 'جواب: اس سے مراد وہ زر جسے ملک کے قانون کی رو سے قبول کرنا پڑتا ہے مثلاً پاکستان میں سکے اور نوٹ زرِ قانونی ہیں۔', 'ځواب: له دې مراد هغه پیسې دي چې د هېواد د قانون له مخې یې منل لازمي دي؛ لکه په پاکستان کې سکې او نوټونه قانوني پیسې دي.'),
 ('12. What is meant by limited legal money?', '12۔ محدود قانونی زر سے کیا مراد ہے؟', '12. له محدودو قانوني پیسو څه مراد دی؟',
  'A. By it is meant that money which the receiver is not compelled to accept beyond a certain limit, because moving this kind of money is difficult. In Pakistan metal coins are limited legal money.', 'جواب: اس سے مراد وہ زر ہے۔ جسے وصول کنندہ ایک خاص حد سے زیادہ قبول کرنے پر مجبور نہ ہو کیونکہ اس قسم کے زر کی منتقل کرنا مشکل ہوتا ہے پاکستان میں دھات کے سکے محدود قانونی زر ہیں۔', 'ځواب: له دې مراد هغه پیسې دي چې اخیستونکی یې له یوې ټاکلې اندازې ډېر منلو ته نه اړ کېږي، ځکه د دې ډول پیسو لېږدول ستونزمن دي. په پاکستان کې فلزي سکې محدودې قانوني پیسې دي.'),
 ('13. What is meant by unlimited legal money?', '13۔ لامحدود قانونی زر سے کیا مراد ہے؟', '13. له نامحدودو قانوني پیسو څه مراد دی؟',
  'A. By it is meant that money which the receiver is compelled to accept in every case, and for its payment the government has fixed no limit. In Pakistan paper money is unlimited legal money.', 'جواب: اس سے مراد وہ زر ہے جسے وصول کنندہ ہر حال میں قبول کرنے پر مجبور ہوتا ہے اور اس کی ادائیگی پر حکومت نے کوئی حد مقرر نہیں کی ہوتی۔ پاکستان میں کاغذی زر لامحدود قانونی زر ہے۔', 'ځواب: له دې مراد هغه پیسې دي چې اخیستونکی یې په هر حال کې منلو ته اړ دی او د هغو په تادیه حکومت هېڅ حد نه وي ټاکلی. په پاکستان کې کاغذي پیسې نامحدودې قانوني پیسې دي.'),
 ('14. Write the definition of money of account.', '14۔ حسابی زر کی تعریف لکھیں۔', '14. د حسابي پیسو تعریف ولیکئ.',
  'A. By it is meant that unit of money with reference to which sums are counted or the price of things is told, e.g. in Pakistan the money of account is the rupee, and in America the dollar, etc.', 'جواب: اس سے مراد زر کی وہ اکائی ہے جس کے حوالے سے رقم کی گنتی کی جاتی ہے یا چیزوں کی قیمت بتائی جاتی ہے۔ مثلاً پاکستان میں حسابی زر روپیہ ہے اور امریکہ کا ڈالر وغیرہ۔', 'ځواب: له دې مراد د پیسو هغه واحد دی چې د هغه په حواله د پیسو شمېرنه کېږي یا د شیانو بیه ویل کېږي؛ لکه په پاکستان کې حسابي پیسې روپۍ ده او د امریکا ډالر او نور.'),
 ('15. What is a credit card?', '15۔ کریڈٹ کارڈ کیا ہوتا ہے؟', '15. کریډیټ کارډ څه دی؟',
  'A. This is a card made of plastic which a bank issues to a person for giving credit. With the help of this card cash too can be obtained, and it is also useful in buying and selling.', 'جواب: یہ پلاسٹک کا بنا ہوا کارڈ ہوتا ہے جو بنک کسی شخص کو ادھار دینے کے لیے جاری کرتا ہے۔ اس کارڈ کی مدد سے نقد رقم بھی حاصل کی جا سکتی ہے۔ اور یہ خرید و فروخت کے کام بھی آتا ہے۔', 'ځواب: دا له پلاسټیک جوړ کارډ دی چې بانک یې یوه کس ته د پور ورکولو لپاره جاري کوي. د دې کارډ په مرسته نغدې پیسې هم اخیستل کېدای شي او په پېر و پلور کې هم کارېږي.'),
 ('16. Write four benefits of paper money.', '16۔ کاغذی زر کے چار فائدے لکھیں۔', '16. د کاغذي پیسو څلور ګټې ولیکئ.',
  'A. (i) easy transfer; (ii) low cost; (iii) saving of precious metals; (iv) emergency use.', 'جواب: (i) آسان منتقلی (ii) کم لاگت (iii) قیمتی دھاتوں کی بچت (iv) ہنگامی استعمال', 'ځواب: (i) اسانه لېږد؛ (ii) لږ لګښت؛ (iii) د قیمتي فلزاتو سپما؛ (iv) بیړنۍ کارونه.'),
 ('17. What is meant by the supply of money?', '17۔ زر کی رسد سے کیا مراد ہے؟', '17. د پیسو له عرضې څه مراد دی؟',
  'A. By the supply of money is meant that total quantity of money which is present with people.', 'جواب: زر کی رسد سے مراد زر کی وہ کل مقدار ہے جو لوگوں کے پاس موجود ہو۔', 'ځواب: له پیسو عرضې مراد د پیسو هغه ټول مقدار دی چې د خلکو سره موجود وي.'),
 ('18. Write four sources of the supply of money.', '18۔ زر کی رسد کے چار ذرائع لکھیں۔', '18. د پیسو د عرضې څلور سرچینې ولیکئ.',
  'A. (i) individual savings; (ii) business savings; (iii) government savings; (iv) bank credit.', 'جواب: (i) انفرادی بچتیں (ii) کاروباری بچتیں (iii) سرکاری بچتیں (iv) بنک کریڈٹ', 'ځواب: (i) انفرادي سپما؛ (ii) سوداګریزه سپما؛ (iii) دولتي سپما؛ (iv) بانکي کریډیټ.'),
 ('19. Write four assumptions of the quantity theory of money.', '19۔ نظریہ مقدارِ زر کے چار مفروضات لکھیں۔', '19. د پیسو د مقدار د نظریې څلور فرضیې ولیکئ.',
  'A. (i) the quantity of sale of goods should not change; (ii) the volume of direct exchange should not change; (iii) the circulation of money should remain the same; (iv) the quantity of hoards should not change.', 'جواب: (i) اشیاء کی مقدارِ فروخت نہ بدلے (ii) براہِ راست مبادلہ کا حجم نہ بدلے (iii) زر کی گردش یکساں رہے (iv) دفینوں کی مقدار نہ بدلے', 'ځواب: (i) د توکو د پلور مقدار دې بدل نه شي؛ (ii) د مستقیمې تبادلې حجم دې بدل نه شي؛ (iii) د پیسو ګرځښت دې یو شان پاتې شي؛ (iv) د دفینو مقدار دې بدل نه شي.'),
 ('20. Write four shortcomings of the quantity theory of money.', '20۔ نظریہ مقدارِ زر کی چار خامیاں لکھیں۔', '20. د پیسو د مقدار د نظریې څلور نیمګړتیاوې ولیکئ.',
  'A. (i) it is ineffective in the period of recession; (ii) it fails in dynamic conditions; (iii) the mutual relation of factors is not clear; (iv) the mutual ratio of quantity of money and value of money is not correct.', 'جواب: (i) سرد بازاری کے دور میں بے اثر ہے (ii) متحرک حالات میں ناکام ہے (iii) عوامل کا باہمی تعلق واضح نہیں (iv) مقدارِ زر اور قدرِ زر کی باہمی نسبت درست نہیں', 'ځواب: (i) د رکود په دوره کې بې‌اغېزې ده؛ (ii) په متحرکو حالاتو کې ناکامه ده؛ (iii) د عواملو دوه اړخیزه اړیکه روښانه نه ده؛ (iv) د پیسو د مقدار او ارزښت دوه اړخیز نسبت سم نه دی.'),
 ('21. What is meant by the demand for money?', '21۔ زر کی طلب سے کیا مراد ہے؟', '21. د پیسو له غوښتنې څه مراد دی؟',
  'A. By the demand for money is meant that quantity of money which people want to keep with them in cash form.', 'جواب: زر کی طلب سے مراد زر کی وہ مقدار جو لوگ نقد شکل میں اپنے پاس رکھنا چاہتے ہیں۔', 'ځواب: د پیسو له غوښتنې مراد د پیسو هغه مقدار دی چې خلک یې په نغده بڼه له ځان سره ساتل غواړي.'),
 ('22. State four difficulties of the barter system.', '22۔ بارٹر سسٹم کی چار مشکلات بتائیں۔', '22. د بارټر سیسټم څلور ستونزې ووایاست.',
  'A. (i) lack of double coincidence in wants; (ii) some goods being indivisible; (iii) difficulty in store of value; (iv) difficulties in credit transactions.', 'جواب: (i) ضرورتوں میں دوطرفہ مطابقت کا نہ ہونا (ii) بعض اشیاء کا ناقابلِ تقسیم ہونا (iii) ذخیرہ قدر میں دقت (iv) ادھار لین دین میں مشکلات', 'ځواب: (i) په اړتیاوو کې د دوه اړخیزې مطابقت نشتوالی؛ (ii) د ځینو توکو نه وېشل کېدل؛ (iii) د ارزښت په زېرمه کې ستونزه؛ (iv) په پور راکړه ورکړه کې ستونزې.'),
 ('23. What is meant by the velocity of circulation of money?', '23۔ زر کی رفتارِ گردش سے کیا مراد ہے؟', '23. د پیسو د ګرځښت له سرعت څه مراد دی؟',
  'A. By the velocity of circulation of money is meant that rate at which the stock of money circulates every year.', 'جواب: زر کی رفتارِ گردش سے مراد وہ شرح ہے، جس پر زر کا ذخیرہ ہر سال گردش کرتا ہے۔', 'ځواب: د پیسو د ګرځښت له سرعت مراد هغه نرخ دی چې د پیسو زېرمه په هغه هر کال ګرځي.'),
 ('24. Write three purposes of liquidity of money.', '24۔ زر کی نقدیت کے تین مقاصد تحریر کریں۔', '24. د پیسو د نغدینې درې موخې ولیکئ.',
  'A. (i) for daily necessities; (ii) for unexpected necessities; (iii) for estimation or speculation.', 'جواب: (i) روزمرہ ضروریات کے لیے (ii) غیر متوقع ضروریات کے لیے (iii) تخمین یا سٹہ بازی کے لیے', 'ځواب: (i) د ورځنیو اړتیاوو لپاره؛ (ii) د نه اټکل شویو اړتیاوو لپاره؛ (iii) د اټکل یا سټې لپاره.')]


def O(e, u, p):
    return (e, u, p)


MCQ = [  # (question, options, index of printed ✓)
 (('The problem of double non-coincidence of wants is found in', 'ضروریات کا دوطرفہ عدم مطابقت کا مسئلہ اس میں پایا جاتا ہے۔', 'د اړتیاوو د دوه اړخیزې نه مطابقت ستونزه په دې کې موندل کېږي'),
  [O('banking', 'بنکاری', 'بانکداري'), O('transactions', 'لین دین', 'راکړه ورکړه'), O('barter system', 'بارٹر سسٹم', 'بارټر سیسټم'), O('international trade', 'بین الاقوامی تجارت', 'نړیواله سوداګري')], 2),
 (('Of the following, one is not a function of money:', 'مندرجہ ذیل میں سے ایک زر کا فریضہ نہیں:', 'له لاندې څخه یوه د پیسو دنده نه ده:'),
  [O('medium of exchange', 'آلہ مبادلہ', 'د تبادلې وسیله'), O('standard of value', 'معیادِ قدر', 'د ارزښت معیار'), O('store of value', 'ذخیرہ قدر', 'د ارزښت زېرمه'), O('stability of value', 'استحکامِ قدر', 'د ارزښت ثبات')], 3),
 (('The speculative demand (Speculative Demand) for money is a function of what?', 'زر کی تخمینی طلب (Speculative Demand) کس کا تفاعل ہے؟', 'د پیسو اټکلي غوښتنه (Speculative Demand) د څه تابع ده؟'),
  [O('investment', 'سرمایہ کاری', 'پانګونه'), O('income', 'آمدنی', 'عاید'), O('consumption', 'صرف', 'مصرف'), O('rate of interest', 'شرحِ سود', 'د سود نرخ')], 3),
 (('Barter means', 'بارٹر سے مراد ہے۔', 'له بارټر مراد دی'),
  [O('buying goods in exchange for money', 'زر کے بدلے اشیاء خریدنا', 'د پیسو په بدل کې توکي پېرل'), O('taking a thing in exchange for a thing', 'شے کے بدلے شے لینا', 'د شي په بدل کې شی اخیستل'), O('buying goods from the wholesale market', 'تھوک منڈی سے مال خریدنا', 'له عمده بازاره مال پېرل'), O('buying necessities from the retail market', 'پرچون بازار سے اشیاء ضرورت خریدنا', 'له پرچون بازاره د اړتیا توکي پېرل')], 1),
 (('This is included in the functions of money', 'زر کے فرائض میں یہ شامل ہے۔', 'د پیسو په دندو کې دا شامل دي'),
  [O('increasing the production of goods', 'اشیا کی پیداوار بڑھانا', 'د توکو تولید زیاتول'), O('reducing dearness', 'مہنگائی میں کمی کرنا', 'ګراني کمول'), O('medium of exchange', 'آلہ مبادلہ', 'د تبادلې وسیله'), O('increasing exports', 'برآمدات میں اضافہ کرنا', 'صادرات زیاتول')], 2),
 (('The kinds of money are these', 'زر کی اقسام یہ ہیں۔', 'د پیسو ډولونه دا دي'),
  [O('consumer goods', 'اشیائے صرف', 'مصرفي توکي'), O('capital goods', 'اشیائے سرمایہ', 'پانګه‌ییز توکي'), O('paper money', 'کاغذی زر', 'کاغذي پیسې'), O('raw material', 'خام مال', 'خام مواد')], 2),
 (('What is meant by the supply of money?', 'زر کی رسد سے کیا مراد ہے؟', 'د پیسو له عرضې څه مراد دی؟'),
  [O('quantity of coins', 'سکوں کی مقدار', 'د سکو مقدار'), O('quantity of notes', 'نوٹوں کی مقدار', 'د نوټونو مقدار'), O('the quantity of money which is with people', 'زر کی مقدار جو لوگوں کے پاس ہے', 'د پیسو هغه مقدار چې د خلکو سره دی'), O('government savings', 'سرکاری بچتیں', 'دولتي سپما')], 2),
 (('Liquidity preference means', 'ترجیحِ نقدیت سے مراد ہے۔', 'نغدینې ته له لومړیتوب مراد دی'),
  [O('miserliness', 'کنجوسی کرنا', 'شومتیا کول'), O('extravagance', 'اسراف کرنا', 'اسراف کول'), O('keeping money in cash form', 'روپیہ نقد شکل میں رکھنا', 'پیسې په نغده بڼه ساتل'), O('buying property', 'پراپرٹی خریدنا', 'ملکیت پېرل')], 2),
 (('Government savings mean', 'سرکاری بچتوں سے مراد ہے۔', 'له دولتي سپما مراد دی'),
  [O('income from taxes', 'ٹیکسوں کی آمدنی', 'د مالیو عاید'), O('the difference between government income and government expenditure', 'سرکاری آمدنی اور سرکاری خرچ کا فرق', 'د دولتي عاید او دولتي لګښت توپیر'), O('exports', 'برآمدات', 'صادرات'), O('quantity of notes in circulation', 'زیرِ گردش نوٹوں کی مقدار', 'د ګرځښت لاندې نوټونو مقدار')], 1),
 (('With the fall in the value of money this class remains in benefit', 'زر کی قدر کم ہو جانے سے یہ طبقہ فائدہ میں رہتا ہے۔', 'د پیسو د ارزښت په کمېدو دا طبقه په ګټه کې وي'),
  [O('fixed-income people', 'مقررہ آمدنی والے', 'ټاکلي عاید لرونکي'), O('traders and industrialists', 'تاجر و صنعت کار', 'سوداګر او صنعتکاران'), O('creditors', 'قرض خواہ', 'پور ورکوونکي'), O('farmer', 'کسان', 'بزګر')], 1),
 (('This economist presented the quantity theory of money', 'نظریہ مقدارِ زر اس ماہرِ معاشیات نے پیش کیا۔', 'د پیسو د مقدار نظریه دې اقتصادپوه وړاندې کړه'),
  [O('Keynes', 'کینز', 'کینز'), O('Crowther', 'کراؤتھر', 'کراوتر'), O('Fisher', 'فشر', 'فیشر'), O('Samuelson', 'سیموئلسن', 'سیمویلسن')], 2),
 (('Keynes presented this theory', 'کینز نے یہ نظریہ پیش کیا۔', 'کینز دا نظریه وړاندې کړه'),
  [O('quantity theory of money', 'نظریہ مقدارِ زر', 'د پیسو د مقدار نظریه'), O('theory of liquidity preference', 'نظریہ ترجیحِ زرِ نقد', 'د نغدو پیسو د لومړیتوب نظریه'), O('marginal productivity theory', 'نظریہ مختتم پیداواریت', 'د حاشیوي تولیدیت نظریه'), O('uncertainty theory of profit', 'منافع کا نظریہ غیر یقینی', 'د ګټې د ناڅرګندتیا نظریه')], 1),
 (('The relation of the quantity of money and the value of money is', 'مقدارِ زر اور قدرِ زر کا تعلق ہے۔', 'د پیسو د مقدار او د پیسو د ارزښت اړیکه ده'),
  [O('direct', 'براہِ راست', 'مستقیمه'), O('inverse', 'معکوس', 'معکوسه'), O('none', 'کوئی نہیں', 'هېڅ یوه'), O('both', 'دونوں', 'دواړه')], 1),
 (('Our monetary unit is', 'ہماری زری اکائی ہے۔', 'زموږ پولي واحد دی'),
  [O('rupee', 'روپیہ', 'روپۍ'), O('paisa', 'پیسہ', 'پیسه'), O('dollar', 'ڈالر', 'ډالر'), O('riyal', 'ریال', 'ریال')], 2),
 (('Deflation has a bad effect on', 'تفریطِ زر کا برا اثر پڑتا ہے۔', 'د تفریط زر بد اغېز لوېږي پر'),
  [O('fixed-income group', 'معینہ آمدنی گروپ', 'ټاکلي عاید ډله'), O('investor', 'سرمایہ کار', 'پانګوال'), O('farmer', 'کسان', 'بزګر'), O('buyer', 'خریدار', 'پېرودونکی')], 1),
 (('The fiscal year of Pakistan', 'پاکستان کا مالیاتی سال', 'د پاکستان مالي کال'),
  [O('1 January to 31 December', 'یکم جنوری تا 31 دسمبر', '۱ جنوري تر ۳۱ ډسمبر'), O('1 January to 30 June', 'یکم جنوری تا 30 جون', '۱ جنوري تر ۳۰ جون'), O('30 June to 31 December', '30 جون تا 31 دسمبر', '۳۰ جون تر ۳۱ ډسمبر'), O('1 July to 30 June', 'یکم جولائی تا 30 جون', '۱ جولای تر ۳۰ جون')], 3),
 (('Two parallel lines are drawn on the upper left-hand corner of', 'بائیں جانب اوپر والے کونے پر دو متوازی لکیریں کھینچی جاتی ہیں۔', 'په پورتني کیڼ کونج کې دوه موازي کرښې ایستل کېږي'),
  [O('bearer cheque', 'حامل چیک', 'حامل چک'), O('travel cheque', 'سفری چیک', 'سفري چک'), O('order cheque', 'حکمی چیک', 'حکمي چک'), O('crossed cheque', 'نشان زدہ چیک', 'نښه شوی چک')], 3),
 (('Included in the supply of money is', 'زر کی رسد میں شامل ہے۔', 'د پیسو په عرضه کې شامل دي'),
  [O('individual savings', 'انفرادی بچتیں', 'انفرادي سپما'), O('business savings', 'کاروباری بچتیں', 'سوداګریزه سپما'), O('government savings', 'سرکاری بچتیں', 'دولتي سپما'), O('all three', 'تینوں', 'درې واړه')], 3),
 (('Government securities are what kind of money?', 'سرکاری کفالتیں کس قسم کا زر ہے۔', 'دولتي تضمینونه کوم ډول پیسې دي؟'),
  [O('paper money', 'کاغذی زر', 'کاغذي پیسې'), O('near money', 'قریبی زر', 'نږدې پیسې'), O('legal money', 'قانونی زر', 'قانوني پیسې'), O('convertible deposits', 'بدل پذیری امانتیں', 'بدلېدونکي امانتونه')], 1),
 (('Of the following, which one is included in credit money?', 'درج ذیل میں سے کوئی ایک اعتباری زر میں شامل ہے۔', 'له لاندې څخه کوم یو په اعتباري پیسو کې شامل دی؟'),
  [O('paper note', 'کاغذی نوٹ', 'کاغذي نوټ'), O('standard money', 'معیاری زر', 'معیاري پیسې'), O('credit card', 'کریڈٹ کارڈ', 'کریډیټ کارډ'), O('legal money', 'قانونی زر', 'قانوني پیسې')], 2),
 (('Cheque, hundi and bank draft represent which kind of money?', 'چیک، ہنڈی اور بنک ڈرافٹ کس قسم کے زر کی نمائندگی کرتا ہے۔', 'چک، هنډۍ او بانکي ډرافټ د کوم ډول پیسو استازیتوب کوي؟'),
  [O('legal money', 'قانونی زر', 'قانوني پیسې'), O('credit money', 'اعتباری زر', 'اعتباري پیسې'), O('paper money', 'کاغذی زر', 'کاغذي پیسې'), O('gold coins', 'سونے کے سکے', 'د سرو زرو سکې')], 1),
 (('The face value of which money is equal to its real value?', 'کون سے زر کی ظاہری مالیت اس کی حقیقی مالیت کے برابر ہوتی ہے۔', 'د کومو پیسو ښکاره ارزښت د هغو له حقیقي ارزښت سره برابر وي؟'),
  [O('standard money', 'معیاری زر', 'معیاري پیسې'), O('nominal money', 'وضعی زر', 'وضعي پیسې'), O('credit money', 'اعتباری زر', 'اعتباري پیسې'), O('gold coins', 'سونے کے سکے', 'د سرو زرو سکې')], 0),
 (('On what does the transaction demand for money depend?', 'زر کی معاملاتی طلب کا انحصار کس پر ہوتا ہے۔', 'د پیسو معاملاتي غوښتنه په څه پورې اړه لري؟'),
  [O('rate of interest', 'شرح، سود', 'د سود نرخ'), O('business conditions', 'کاروباری حالات', 'سوداګریز حالات'), O('stock exchange', 'اسٹاک ایکسچینج', 'سټاک ایکسچینج'), O('income', 'آمدنی', 'عاید')], 3),
 (('With respect to what is the supply of money inelastic?', 'کس کے لحاظ سے زر کی رسد غیر لچک دار ہوتی ہے۔', 'د څه په اړه د پیسو عرضه بې‌لچکه وي؟'),
  [O('rate of interest', 'شرحِ سود', 'د سود نرخ'), O('income', 'آمدنی', 'عاید'), O('investment', 'سرمایہ کاری', 'پانګونه'), O('expenditure', 'خرچ', 'لګښت')], 0)]


def mark(opts, k):
    return [tuple(x + ' ✓' for x in o) if i == k else o for i, o in enumerate(opts)]


def p31():
    b = Builder()
    for qe, qu, qp, ae, au, ap in QA[:11]:
        b.p(qe, qu, qp)
        b.p(ae, au, ap)
    r1 = BOOK.record(b, 'eco12-ch2-model-2', 'Chapter 2 model paper questions (2)', 'باب 2: ماڈل پرچہ سوالات (۲)', '۲ څپرکی: د نمونې پرچې پوښتنې (۲)', 31, [42])
    t = Builder()
    for qe, qu, qp, ae, au, ap in QA[11:]:
        t.p(qe, qu, qp)
        t.p(ae, au, ap)
    t.h('Choose the correct answer', 'درست جواب کا انتخاب کریں', 'سم ځواب وټاکئ')
    P_ = ('2. Four possible answers have been given for each question; of them put the mark (✓) on the correct answer.', '2۔ ہر سوال کے چار ممکنہ جوابات دیئے گئے ہیں ان میں سے درست جواب پر (✓) کا نشان لگائیں۔', '2. د هرې پوښتنې څلور احتمالي ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')
    t.p(*P_)
    for i, (q, o, k) in enumerate(MCQ[:5], 1):
        t.mcq(f'{i}.', q, mark(o, k), per_line=2)
    r2 = BOOK.record(t, 'eco12-ch2-model-3', 'Chapter 2 model paper questions (3)', 'باب 2: ماڈل پرچہ سوالات (۳)', '۲ څپرکی: د نمونې پرچې پوښتنې (۳)', 31, [43])
    BOOK.save(31, [(2, r1), (2, r2)], issues=[{'id': 'eco12-pdf031', 'unit': 2, 'printedPage': 42,
               'description': 'Printed errors retained: answer 9 “معیادی زر” for معیاری; answer 12 “زر کی منتقل کرنا”; MCQ 2 option (B) “معیادِ قدر”. The ✓ answer marks are printed in the book and kept.'}])


def p32():
    b = Builder()
    for i, (q, o, k) in enumerate(MCQ[5:15], 6):
        b.mcq(f'{i}.', q, mark(o, k), per_line=2)
    r1 = BOOK.record(b, 'eco12-ch2-model-4', 'Chapter 2 model paper questions (4)', 'باب 2: ماڈل پرچہ سوالات (۴)', '۲ څپرکی: د نمونې پرچې پوښتنې (۴)', 32, [44])
    t = Builder()
    for i, (q, o, k) in enumerate(MCQ[15:], 16):
        t.mcq(f'{i}.', q, mark(o, k), per_line=2)
    r2 = BOOK.record(t, 'eco12-ch2-model-5', 'Chapter 2 model paper questions (5)', 'باب 2: ماڈل پرچہ سوالات (۵)', '۲ څپرکی: د نمونې پرچې پوښتنې (۵)', 32, [45])
    BOOK.save(32, [(2, r1), (2, r2)], complete_units=[2], issues=[{'id': 'eco12-pdf032', 'unit': 2, 'printedPage': 44,
               'description': 'Printed answer marks kept as printed, including doubtful ones: MCQ 14 ticks (C) “dollar” although the Pakistani monetary unit is the rupee (A); MCQ 15 ticks (B) “investor” for the bad effect of deflation; MCQ 10 ticks traders/industrialists. MCQ 23 option (A) “شرح، سود” (stray comma). Chapter 2 ends on p.45.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 31
    {31: p31, 32: p32}[n]()
