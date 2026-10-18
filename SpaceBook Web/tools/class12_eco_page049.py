"""Economics XII PDF49–50: pp.78–81 — chapter 4 model paper: section I short questions 1–19; section II long questions (with board years);
question 3 MCQs 1–16 (printed ✓ marks kept). Run: python class12_eco_page049.py N (49–50)."""
import sys
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model

QA = [
 ('1. What is meant by public finance?', '1۔ سرکاری مالیات سے کیا مراد ہے؟', '1. له دولتي مالیې څه مراد دی؟',
  'A. Every government reviews the expected income and expenditure of the coming year and prepares a budget or mizania; this is called public finance.', 'جواب: ہر حکومت آئندہ سال میں ہونے والی متوقع آمدنی اور خرچ کا جائزہ لیتی ہے۔ اور بجٹ یا میزانیہ تیار کرتی ہے اسے سرکاری مالیات کہا جاتا ہے۔', 'ځواب: هر حکومت د راتلونکي کال د تمه شوي عاید او لګښت کتنه کوي او بودجه یا میزانیه جوړوي؛ دې ته دولتي مالیه ویل کېږي.'),
 ('2. What are the big sources of income of the government?', '2۔ حکومت کی آمدنی کے بڑے بڑے ذرائع کونسے ہیں؟', '2. د حکومت د عاید لویې سرچینې کومې دي؟',
  'A. (i) tax revenue; (ii) price of a thing or service; (iii) state property; (iv) productive works of the government.', 'جواب: (i) محصولاتی آمدنی (ii) شے یا خدمت کی قیمت (iii) سرکاری جائیداد (iv) حکومت کے پیداواری کام', 'ځواب: (i) مالیاتي عاید؛ (ii) د شي یا خدمت بیه؛ (iii) دولتي ملکیت؛ (iv) د حکومت تولیدي کارونه.'),
 ('3. State the big principles of imposing tax.', '3۔ ٹیکس عائد کرنے کے بڑے بڑے اصول بتایئے؟', '3. د مالیې د لګولو لوی اصول ووایاست.',
  'A. (i) principle of equality; (ii) principle of certainty; (iii) principle of economy; (iv) principle of productivity; (v) principle of simplicity.', 'جواب: (i) اصول مساوات (ii) اصول تیقن (iii) اصول کفایت (iv) اصول پیداواری (v) اصول سادگی', 'ځواب: (i) د مساوات اصل؛ (ii) د ډاډ اصل؛ (iii) د کفایت اصل؛ (iv) د تولیدیت اصل؛ (v) د سادګۍ اصل.'),
 ('4. State the difference between direct tax and indirect tax.', '4۔ بلاواسطہ ٹیکس اور بالواسطہ ٹیکس میں فرق بیان کریں؟', '4. د مستقیمې او غیر مستقیمې مالیې توپیر بیان کړئ.',
  'A. Direct tax: by it is meant that tax which the taxpayer pays directly to the government and whose burden too falls on that same person; he cannot transfer it onwards, e.g. income tax. Indirect tax: that tax whose payment is the responsibility of one person but whose burden actually falls on someone else, because the one paying the tax transfers it to someone else, e.g. sales tax.', 'جواب: بلاواسطہ ٹیکس: اس سے مراد وہ ٹیکس ہے جو ٹیکس گزار براہِ راست حکومت کو ادا کرتا ہے اور اس کا بوجھ بھی اس شخص پر ہوتا وہ اس آگے منتقل نہیں کر سکتا۔ مثلاً انکم ٹیکس۔ بالواسطہ ٹیکس: وہ ٹیکس جسکی ادائیگی ایک شخص کے ذمے ہو۔ لیکن اسکا بوجھ دراصل کسی اور پر پڑے۔ کیونکہ ٹیکس دینے والا اسے کسی اور پر منتقل کر دیتا ہے مثلاً سیلز ٹیکس۔', 'ځواب: مستقیمه مالیه: له دې مراد هغه مالیه ده چې مالیه ورکوونکی یې مستقیم حکومت ته ورکوي او بار یې هم پر همغه کس وي؛ هغه یې مخکې نه شي لېږدولی، لکه د عاید مالیه. غیر مستقیمه مالیه: هغه مالیه چې ورکول یې د یوه کس پر غاړه وي خو بار یې په اصل کې پر بل چا لوېږي، ځکه مالیه ورکوونکی یې بل چا ته لېږدوي، لکه د پلور مالیه.'),
 ('5. What is the difference between proportional and progressive tax?', '5۔ متناسب اور متزائد ٹیکس میں کیا فرق ہے؟', '5. د تناسبي او زیاتېدونکې مالیې ترمنځ څه توپیر دی؟',
  'A. Proportional tax: if tax is imposed on the incomes of all people at one rate, i.e. all taxpayers give part of their income in the form of taxes in the same proportion, it is called proportional tax. Progressive tax: if, with the increase in the income of a person, the rate of tax goes on increasing, it is called progressive tax.', 'جواب: متناسب ٹیکس: اگر تمام لوگوں کی آمدنیوں پر ایک شرح سے ٹیکس لگا دیا جائے، یعنی تمام ٹیکس گزار اپنی آمدنی کا یکساں تناسب سے حصہ ٹیکسوں کی شکل میں دیں۔ تو اسے متناسب ٹیکس کہا جاتا ہے۔ متزائد ٹیکس: اگر کسی شخص کی آمدنی میں اضافہ کے ساتھ ٹیکس کی شرح بڑھتی چلی جائے تو اسے متزائد ٹیکس کہتے ہیں۔', 'ځواب: تناسبي مالیه: که د ټولو خلکو پر عایداتو په یوه نرخ مالیه ولګول شي، یعنې ټول مالیه ورکوونکي د خپل عاید برخه په یو شان تناسب د مالیو په بڼه ورکړي، تناسبي مالیه بلل کېږي. زیاتېدونکې مالیه: که د یوه کس د عاید د زیاتوالي سره د مالیې نرخ زیاتېږي، زیاتېدونکې مالیه بلل کېږي.'),
 ('6. State the principles of government expenditure.', '6۔ سرکاری اخراجات کے اصول بیان کیجئے؟', '6. د دولتي لګښتونو اصول بیان کړئ.',
  'A. (i) maximum social welfare; (ii) principle of economy; (iii) principle of sanction; (iv) elasticity.', 'جواب: (i) زیادہ سے زیادہ معاشرتی فلاح (ii) کفایت کا اصول (iii) منظوری کا اصول (iv) لچک پذیری', 'ځواب: (i) تر ټولو زیاته ټولنیزه هوساینه؛ (ii) د کفایت اصل؛ (iii) د منظورۍ اصل؛ (iv) لچک.'),
 ('7. What is a deficit budget?', '7۔ خسارے کا بجٹ کیا ہوتا ہے؟', '7. د زیان بودجه څه ده؟',
  'A. When the expenses of the government are more and income less, such a budget is called a deficit budget.', 'جواب: جب حکومت کے اخراجات زیادہ ہوں اور آمدنی کم ہو تو ایسے بجٹ کو خسارے کا بجٹ کہتے ہیں۔', 'ځواب: کله چې د حکومت لګښتونه ډېر او عاید لږ وي، داسې بودجې ته د زیان بودجه ویل کېږي.'),
 ('8. What is meant by a balanced budget?', '8۔ متوازن بجٹ سے کیا مراد ہے؟', '8. له متوازنې بودجې څه مراد دی؟',
  'A. When the income and expenses of the government are equal, such a budget is called a balanced budget.', 'جواب: جب حکومت کی آمدنی اور اخراجات برابر ہوں تو ایسے بجٹ کو متوازن بجٹ کہتے ہیں۔', 'ځواب: کله چې د حکومت عاید او لګښتونه برابر وي، داسې بودجې ته متوازنه بودجه ویل کېږي.'),
 ('9. Write four objectives of fiscal policy.', '9۔ مالیاتی پالیسی کے چار مقاصد تحریر کریں؟', '9. د مالي پالیسۍ څلور موخې ولیکئ.',
  'A. They are as follows: (i) business fluctuations; (ii) full employment; (iii) reducing the difference of incomes; (iv) maintaining a particular level of prices.', 'جواب: درج ذیل ہیں (i) کاروباری اتار چڑھاؤ (ii) کامل روزگار (iii) آمدنیوں کا فرق گھٹانا (iv) قیمتوں کی خاص سطح برقرار رکھنا', 'ځواب: دا دي: (i) سوداګریز کښته پورته کېدل؛ (ii) بشپړ روزګار؛ (iii) د عایداتو توپیر کمول؛ (iv) د بیو ځانګړې کچه ساتل.'),
 ('10. State the concept of a surplus budget.', '10۔ فاضل بجٹ کا مفہوم بتائیں؟', '10. د اضافي بودجې مفهوم ووایاست.',
  'A. When the income of the government is more and expenses less, such a budget is called a surplus budget.', 'جواب: حکومت کی آمدنی زیادہ ہو اور اخراجات کم ہوں تو ایسے بجٹ کو فاضل بجٹ کہا جاتا ہے۔', 'ځواب: کله چې د حکومت عاید ډېر او لګښتونه لږ وي، داسې بودجې ته اضافي بودجه ویل کېږي.'),
 ('11. What is meant by tax culture? (tax culture)', '11۔ محصولاتی تمدن سے کیا مراد ہے؟ (ٹیکس کلچر)', '11. له مالیاتي کلتور څه مراد دی؟ (ټیکس کلچر)',
  'A. The tax system which is established for the government to obtain income through taxes, adopting different measures in this sector, and adopting different methods and making laws in connection with obtaining the cooperation of the public regarding the payment of taxes, is called tax culture.', 'جواب: حکومت کیلئے ٹیکسوں کے ذریعہ آمدنی حاصل کرے، اس شعبہ میں مختلف تدبیر کرنے اور ٹیکسوں کی ادائیگی کے ضمن میں عوام کا تعاون حاصل کرنے کے سلسلہ میں مختلف طریقے اور قوانین وضع کرتے ہوئے جو محصولاتی نظام قائم کیا جاتا ہے اس محصولاتی تمدن (ٹیکس کلچر) کہا جاتا ہے۔', 'ځواب: هغه مالیاتي نظام چې د حکومت لپاره د مالیو له لارې د عاید د ترلاسه کولو، په دې برخه کې د بېلابېلو تدبیرونو او د مالیو د ورکړې په برخه کې د خلکو د همکارۍ د ترلاسه کولو لپاره د بېلابېلو طریقو او قوانینو د جوړولو په ترڅ کې جوړېږي، مالیاتي کلتور (ټیکس کلچر) بلل کېږي.'),
 ('12. Make clear the concept of ushr.', '12۔ عشر کا مفہوم واضح کیجئے؟', '12. د عشر مفهوم روښانه کړئ.',
  'A. Tax on agriculture is called ushr.', 'جواب: زراعت پر ٹیکس کو عشر کہا جاتا ہے۔', 'ځواب: پر کرنې مالیې ته عشر ویل کېږي.'),
 ('13. What is meant by a regressive tax?', '13۔ تنزیلی ٹیکس سے کیا مراد ہے؟', '13. له کمېدونکې مالیې څه مراد دی؟',
  'A. By it is meant such a tax whose burden falls more on those with less income and less on those with more income, e.g. imposing tax on such a thing which the poor use more, like tax on flour, pulses, bicycles etc.', 'جواب: اس سے مراد ایسا ٹیکس ہے جسکا بوجھ کم آمدنی والے پر زیادہ اور زیادہ آمدنی والے پر کم پڑے، مثلاً ایسی چیز پر ٹیکس لگانا جنکا استعمال غربا زیادہ کرتے ہیں۔ جیسے آٹے، دال، سائیکل وغیرہ پر ٹیکس۔', 'ځواب: له دې مراد داسې مالیه ده چې بار یې پر لږ عاید لرونکي ډېر او پر ډېر عاید لرونکي لږ لوېږي؛ لکه پر داسې شي مالیه لګول چې غریبان یې ډېر کاروي، لکه پر اوړو، دال، بایسکل او نورو مالیه.'),
 ('14. State the difference between fee and tax.', '14۔ فیس اور ٹیکس میں فرق بیان کریں؟', '14. د فیس او مالیې توپیر بیان کړئ.',
  'A. Fee: by it is meant that sum which people pay in exchange for obtaining some service from the government, e.g. licence or tuition fee etc. Tax: by it is meant such a payable sum on the citizens which they give to the government from their wealth or income, so that it can meet those expenses which it has to bear for the collective benefit of the public.', 'جواب: فیس: اس سے مراد وہ رقم جو لوگ حکومت سے کوئی خدمت حاصل کرنے کے عوض ادا کرتے ہیں مثلاً لائسنس یا تعلیمی فیس وغیرہ۔ ٹیکس: اس سے مراد شہریوں کے ذمے ایسی واجب الادا رقم ہے جو وہ اپنی دولت یا آمدنی سے حکومت کو دیتے ہیں تاکہ وہ ان اخراجات کو پورا کر سکے جو عوام کے اجتماعی فائدے کیلئے اٹھانے پڑتے ہیں۔', 'ځواب: فیس: له دې مراد هغه پیسې دي چې خلک یې له حکومت څخه د کوم خدمت د ترلاسه کولو په بدل کې ورکوي، لکه د جواز یا د زده‌کړې فیس او نور. مالیه: له دې مراد پر وګړو داسې د ورکړې وړ پیسې دي چې هغوی یې له خپلې شتمنۍ یا عاید حکومت ته ورکوي، تر څو هغه لګښتونه پوره کړي چې د خلکو د ټولیزې ګټې لپاره یې باید وګالي.'),
 ('15. Which basic principles of imposing tax did Adam Smith state?', '15۔ ایڈم سمتھ نے ٹیکس عائد کرنے کے کونسے بنیادی اصول بیان کیے؟', '15. اډم سمېت د مالیې د لګولو کوم بنسټیز اصول بیان کړل؟',
  'A. (i) principle of equality; (ii) principle of certainty; (iii) principle of convenience; (iv) principle of economy.', 'جواب: (i) اصول مساوات (ii) اصول تیقن (iii) اصول سہولت (iv) اصول کفایت', 'ځواب: (i) د مساوات اصل؛ (ii) د ډاډ اصل؛ (iii) د اسانتیا اصل؛ (iv) د کفایت اصل.'),
 ('16. Define fiscal policy.', '16۔ مالیاتی پالیسی کی تعریف کریں؟', '16. د مالي پالیسۍ تعریف وکړئ.',
  'A. Fiscal policy means such an action by which government taxation and government expenditure are used for these purposes: (i) to make severe ups and downs in trade activities moderate; (ii) to establish and restore such an economy which is moving towards progress, in which full employment exists, and in which, because of excess demand, there is neither inflation nor deflation.', 'جواب: مالیاتی پالیسی سے مراد ایسا عمل ہے، جس سے سرکاری محصول بندی اور سرکاری اخراجات کو ان مقاصد کیلئے استعمال کیا جاتا ہے۔ (i) تجارتی سرگرمیوں میں شدید کمی بیشی کو معتدل بنانا (ii) ایسی معیشت قائم اور بحال کرنا جو ترقی کی طرف رواں دواں ہو جس میں کامل روزگار موجود ہو۔ اور زائد از ضرورت طلب کے باعث نہ افراطِ زر ہو، نہ تفریطِ زر۔', 'ځواب: له مالي پالیسۍ مراد داسې عمل دی چې په هغه سره دولتي محصول لګونه او دولتي لګښتونه د دې موخو لپاره کارول کېږي: (i) په سوداګریزو فعالیتونو کې سخت کمښت او زیاتوالی متعادل کول؛ (ii) داسې اقتصاد جوړول او بیا رغول چې د پرمختګ پر لور روان وي، بشپړ روزګار پکې وي او د اضافي غوښتنې له امله نه انفلاسیون وي او نه تفریط زر.'),
 ('17. Write four points of difference between private and public finance.', '17۔ نجی اور سرکاری مالیات کے چار اختلافی نکات لکھیں؟', '17. د خصوصي او دولتي مالیې ترمنځ د توپیر څلور ټکي ولیکئ.',
  'A. They are as follows: (i) the government prepares the estimate of its income and expenditure (i.e. budget) for one year, but common people make their budget monthly or weekly; (ii) the government can make deficit investment, but the common public cannot; (iii) in public finance big changes are possible, but for one person to increase his income much or to decrease expenses is difficult; (iv) common individuals usually keep the account of their income and expenditure hidden, but the government does not do so.', 'جواب: درج ذیل ہیں۔ (i) حکومت اپنی آمدنی اور اخراجات کا تخمینہ (یعنی بجٹ) ایک سال کیلئے تیار کرتی ہے لیکن عام لوگ اپنا بجٹ ماہوار یا ہفت وار بناتے ہیں۔ (ii) حکومت خسارے کی سرمایہ کاری کر سکتی ہے لیکن عام عوام نہیں کر سکتیں۔ (iii) سرکاری مالیات میں بڑی بڑی تبدیلیاں ممکن ہیں لیکن ایک شخص کیلئے اپنی آمدنی کو زیادہ بڑھانا یا اخراجات کو گھٹانا دشوار ہوتا ہے۔ (iv) عام افراد اپنی آمدنی و خرچ کا حساب عموماً پوشیدہ رکھتے ہیں لیکن حکومت ایسا نہیں کرتی۔', 'ځواب: دا دي: (i) حکومت د خپل عاید او لګښتونو اټکل (یعنې بودجه) د یوه کال لپاره جوړوي، خو عام خلک خپله بودجه میاشتنۍ یا اونیزه جوړوي؛ (ii) حکومت د زیان پانګونه کولی شي، خو عام خلک یې نه شي کولی؛ (iii) په دولتي مالیه کې لوی لوی بدلونونه شوني دي، خو د یوه کس لپاره د خپل عاید ډېر زیاتول یا د لګښتونو کمول ستونزمن وي؛ (iv) عام کسان معمولاً د خپل عاید او لګښت حساب پټ ساتي، خو حکومت داسې نه کوي.'),
 ('18. State four big heads of the expenses of the government.', '18۔ حکومت کے اخراجات کی چار بڑی مدات بتائیں؟', '18. د حکومت د لګښتونو څلور لوی سرونه ووایاست.',
  'A. They are as follows: (i) the government spends on construction work, e.g. roads etc.; (ii) the government spends to improve the system of education; (iii) the government spends on maintaining health, e.g. hospitals etc.; (iv) the government spends to improve the system of defence.', 'جواب: درج ذیل ہیں۔ (i) تعمیراتی کام پر حکومت خرچ کرتی ہے مثلاً سڑکیں وغیرہ (ii) تعلیم کے نظام کو بہتر بنانے کیلئے حکومت خرچ کرتی ہے۔ (iii) صحت کو برقرار رکھنے پر حکومت خرچ کرتی ہے۔ مثلاً ہسپتال وغیرہ (iv) دفاع کے نظام کو بہتر بنانے کیلئے حکومت خرچ کرتی ہے۔', 'ځواب: دا دي: (i) حکومت پر ودانیزو کارونو لګښت کوي، لکه سړکونه او نور؛ (ii) حکومت د زده‌کړې د نظام د ښه کولو لپاره لګښت کوي؛ (iii) حکومت د روغتیا پر ساتنې لګښت کوي، لکه روغتونونه او نور؛ (iv) حکومت د دفاع د نظام د ښه کولو لپاره لګښت کوي.'),
 ('19. What is meant by private finance?', '19۔ نجی مالیات سے کیا مراد ہے؟', '19. له خصوصي مالیې څه مراد دی؟',
  'A. Common people too usually prepare their budget every month and make an estimate of income and expenditure; this is called private finance.', 'جواب: عام لوگ عموماً ہر ماہ اپنا بجٹ تیار کرتے ہیں اور آمدنی و خرچ کا تخمینہ لگاتے ہیں اسے نجی مالیات کہا جاتا ہے', 'ځواب: عام خلک هم عموماً هره میاشت خپله بودجه جوړوي او د عاید او لګښت اټکل کوي؛ دې ته خصوصي مالیه ویل کېږي.')]

LONG = [('1. State the difference between private finance and public finance. (Sargodha Board 2009, Lahore Board 2010)', '1) نجی مالیات اور سرکاری مالیات میں فرق بیان کیجئے؟ (سرگودھا بورڈ 2009ء، لاہور بورڈ 2010ء)', '1. د خصوصي مالیې او دولتي مالیې توپیر بیان کړئ. (سرګودها بورډ ۲۰۰۹، لاهور بورډ ۲۰۱۰)'),
        ('2. State the principles of imposing tax. (Multan Board 2009, Sargodha Board 2010)', '2) ٹیکس عائد کرنے کے اصول بیان کریں؟ (ملتان بورڈ 2009ء، سرگودھا بورڈ 2010ء)', '2. د مالیې د لګولو اصول بیان کړئ. (ملتان بورډ ۲۰۰۹، سرګودها بورډ ۲۰۱۰)'),
        ('3. Explain the different kinds of taxes. (Bahawalpur Board 2010)', '3) ٹیکسوں کی مختلف اقسام کی وضاحت کریں؟ (بہاولپور بورڈ 2010ء)', '3. د مالیو بېلابېل ډولونه روښانه کړئ. (بهاولپور بورډ ۲۰۱۰)'),
        ('4. Give the detail of the different sources of income of the government.', '4) حکومت کے مختلف ذرائع آمدنی کی تفصیل بتایئے؟', '4. د حکومت د عاید د بېلابېلو سرچینو تفصیل ووایاست.'),
        ('5. State the benefits and harms of indirect tax. (Sargodha Board 2011)', '5) بالواسطہ ٹیکس کے فوائد اور نقصانات بیان کریں؟ (سرگودھا بورڈ 2011ء)', '5. د غیر مستقیمې مالیې ګټې او زیانونه بیان کړئ. (سرګودها بورډ ۲۰۱۱)'),
        ('6. Discuss the merits and demerits of direct tax. (Bahawalpur Board 2011, Mirpur Azad Kashmir Board 2011)', '6) براہِ راست ٹیکس کی خوبیوں اور خامیوں پر بحث کریں؟ (بہاولپور بورڈ 2011ء، میرپور آزاد کشمیر بورڈ 2011ء)', '6. د مستقیمې مالیې پر ښېګڼو او نیمګړتیاوو بحث وکړئ. (بهاولپور بورډ ۲۰۱۱، میرپور آزاد کشمیر بورډ ۲۰۱۱)'),
        ('7. Review the tax system of Pakistan. (Lahore Board 2011)', '7) پاکستان کے نظامِ محصولات کا جائزہ لیجئے؟ (لاہور بورڈ 2011ء)', '7. د پاکستان د مالیاتي نظام کتنه وکړئ. (لاهور بورډ ۲۰۱۱)'),
        ('8. Present proposals to improve the tax system in Pakistan.', '8) پاکستان میں نظامِ محصولات بہتر بنانے کے لیے تجاویز پیش کریں؟', '8. په پاکستان کې د مالیاتي نظام د ښه کولو وړاندیزونه وړاندې کړئ.')]


def O(e, u, p):
    return (e, u, p)


MCQ = [
 (('The nature of income tax is this:', 'انکم ٹیکس کی نوعیت یہ ہے:', 'د عاید مالیې ماهیت دا دی:'),
  [O('proportional', 'متناسب', 'تناسبي'), O('progressive', 'متزائد', 'زیاتېدونکې'), O('regressive', 'تنزیلی', 'کمېدونکې'), O('indirect', 'بالواسطہ', 'غیر مستقیمه')], 1),
 (('The meaning of the principle of equality of imposing tax is:', 'ٹیکس لگانے کے اصول مساوات کی مطلب ہے:', 'د مالیې د لګولو د مساوات د اصل مطلب دی:'),
  [O('taking tax at one rate', 'ایک ہی شرح سے ٹیکس لینا', 'په یوه نرخ مالیه اخیستل'), O('taking tax at a progressive rate', 'متزائد شرح سے ٹیکس لینا', 'په زیاتېدونکي نرخ مالیه اخیستل'), O('taking tax at the lowest rate', 'کم سے کم شرح سے ٹیکس لینا', 'په تر ټولو ټیټ نرخ مالیه اخیستل')], 1),
 (('The burden of this tax can be transferred to another person:', 'اس ٹیکس کا بوجھ دوسرے شخص پر منتقل کیا جا سکتا ہے:', 'د دې مالیې بار بل کس ته لېږدول کېدای شي:'),
  [O('direct tax', 'براہِ راست ٹیکس', 'مستقیمه مالیه'), O('indirect tax', 'بالواسطہ ٹیکس', 'غیر مستقیمه مالیه'), O('property tax', 'پراپرٹی ٹیکس', 'د ملکیت مالیه')], 1),
 (('The principles of imposing tax were presented by this economist:', 'ٹیکس عائد کرنے کے اصول اس ماہرِ معاشیات نے پیش کیے:', 'د مالیې د لګولو اصول دې اقتصادپوه وړاندې کړل:'),
  [O('Ricardo', 'ریکارڈو', 'ریکارډو'), O('Adam Smith', 'آدم سمتھ', 'اډم سمېت'), O('J. S. Mill', 'جے ایس مل', 'جې اېس مل'), O('Marshall', 'مارشل', 'مارشل')], 1),
 (('Excise duty is a tax of this kind:', 'ایکسائز ڈیوٹی اس قسم کا ٹیکس ہے:', 'اېکسایز ډیوټي دا ډول مالیه ده:'),
  [O('direct tax', 'براہِ راست ٹیکس', 'مستقیمه مالیه'), O('indirect tax', 'بالواسطہ ٹیکس', 'غیر مستقیمه مالیه'), O('proportional tax', 'متناسب ٹیکس', 'تناسبي مالیه'), O('non-proportional tax', 'غیر متناسب ٹیکس', 'غیر تناسبي مالیه')], 1),
 (('The nature of income tax is:', 'انکم ٹیکس کی نوعیت یہ ہوتی ہے:', 'د عاید مالیې ماهیت دی:'),
  [O('indirect', 'بالواسطہ', 'غیر مستقیمه'), O('direct', 'بلاواسطہ', 'مستقیمه'), O('regressive', 'تنزیلی', 'کمېدونکې'), O('equal rate', 'مساوی شرح', 'برابر نرخ')], 1),
 (('The best system of taxes is this:', 'ٹیکسوں کا بہترین نظام یہ ہوتا ہے:', 'د مالیو غوره نظام دا دی:'),
  [O('direct tax', 'براہِ راست ٹیکس', 'مستقیمه مالیه'), O('indirect tax', 'بالواسطہ ٹیکس', 'غیر مستقیمه مالیه'), O('which fulfils the principles of imposing tax', 'ٹیکس عائد کرنے کے اصول پورے کرے', 'چې د مالیې د لګولو اصول پوره کړي')], 2),
 (('The objective of fiscal policy:', 'مالیاتی پالیسی کا مقصد:', 'د مالي پالیسۍ موخه:'),
  [O('imposing more tax', 'زیادہ ٹیکس لگانا', 'ډېره مالیه لګول'), O('imposing less tax', 'کم ٹیکس لگانا', 'لږه مالیه لګول'), O('maintaining full employment (Full Employment) in the country', 'ملک میں کامل روزگار (Full Employment) برقرار رکھنا', 'په هېواد کې بشپړ روزګار (Full Employment) ساتل')], 2),
 (('Taxes imposed on goods are called:', 'اشیاء پر عائد کیے جانے والے ٹیکس کہلاتے ہیں:', 'پر توکو لګېدونکې مالیې بلل کېږي:'),
  [O('indirect tax', 'بالواسطہ ٹیکس', 'غیر مستقیمه مالیه'), O('direct tax', 'بلاواسطہ ٹیکس', 'مستقیمه مالیه'), O('progressive tax', 'متزائد ٹیکس', 'زیاتېدونکې مالیه'), O('proportional tax', 'متناسب ٹیکس', 'تناسبي مالیه')], 0),
 (('Which is not a source of income of the central government:', 'کونسا مرکزی حکومت کی آمدنی کا ذریعہ نہیں:', 'کوم یو د مرکزي حکومت د عاید سرچینه نه ده:'),
  [O('water rate (abiana)', 'آبیانہ', 'د اوبو محصول (آبیانه)'), O('income tax', 'آمدنی ٹیکس', 'د عاید مالیه'), O('tariff', 'ٹیرف', 'تعرفه'), O('wealth tax', 'دولت ٹیکس', 'د شتمنۍ مالیه')], 0),
 (('All those measures which the government takes for receipts and expenses are called:', 'وہ تمام اقدامات جو حکومت وصولیوں اور اخراجات کے لیے کرتی ہے کہلاتے ہیں:', 'ټول هغه ګامونه چې حکومت یې د وصولیو او لګښتونو لپاره پورته کوي، بلل کېږي:'),
  [O('agricultural policy', 'زرعی پالیسی', 'کرنیزه پالیسي'), O('fiscal policy', 'مالیاتی پالیسی', 'مالي پالیسي'), O('tax policy', 'ٹیکس پالیسی', 'مالیاتي پالیسي'), O('none of these', 'ان میں سے کوئی نہیں', 'له دې هېڅ یو')], 1),
 (('Under which principle does every person pay tax according to his capacity?', 'کس اصول کے تحت ہر شخص اپنی اہلیت کے مطابق ٹیکس ادا کرتا ہے؟', 'د کوم اصل له مخې هر کس د خپلې وړتیا سره سم مالیه ورکوي؟'),
  [O('principle of elasticity', 'اصول لچک داری', 'د لچک اصل'), O('principle of equality', 'اصول مساوات', 'د مساوات اصل'), O('principle of convenience', 'اصول سہولت', 'د اسانتیا اصل'), O('principle of diversity', 'اصول تنوع', 'د تنوع اصل')], 1),
 (('Wealth tax is:', 'دولت ٹیکس ہے:', 'د شتمنۍ مالیه ده:'),
  [O('regressive tax', 'تنزیلی ٹیکس', 'کمېدونکې مالیه'), O('value-added tax', 'زائد قدری ٹیکس', 'د زیات شوي ارزښت مالیه'), O('proportional tax', 'متناسب ٹیکس', 'تناسبي مالیه'), O('direct tax', 'براہِ راست ٹیکس', 'مستقیمه مالیه')], 3),
 (('The burden of which tax is not transferred to poor people?', 'کس ٹیکس کا بوجھ غریب لوگوں تک منتقل نہیں ہوتا؟', 'د کومې مالیې بار غریبو خلکو ته نه لېږدېږي؟'),
  [O('excise tax', 'ایکسائز ٹیکس', 'اېکسایز مالیه'), O('sales tax', 'سیلز ٹیکس', 'د پلور مالیه'), O('income tax', 'انکم ٹیکس', 'د عاید مالیه'), O('customs duty', 'کسٹم ڈیوٹی', 'ګمرکي ډیوټي')], 2),
 (('The central government collects this share of its income from taxes:', 'مرکزی حکومت اپنی آمدنی کا حصہ ٹیکسوں سے اکٹھا کرتی ہے:', 'مرکزي حکومت د خپل عاید دا برخه له مالیو راټولوي:'),
  [O('24.63%', '24.63%', '24.63%'), O('75.32%', '75.32%', '75.32%'), O('50%', '50%', '50%'), O('68%', '68%', '68%')], 1),
 (('The share of indirect taxes of the Government of Pakistan is:', 'حکومت پاکستان کا بالواسطہ ٹیکسوں کا حصہ ہے:', 'د پاکستان د حکومت د غیر مستقیمو مالیو برخه ده:'),
  [O('68%', '68%', '68%'), O('50%', '50%', '50%'), O('16%', '16%', '16%'), O('18%', '18%', '18%')], 0)]


def p49():
    b = Builder()
    b.h('Model paper questions', 'ماڈل پرچہ سوالات', 'د نمونې پرچې پوښتنې')
    b.h('Subjective (Subjective), Section I (Section I)', 'انشائیہ (Subjective) حصہ اول (Section I)', 'تشریحي (Subjective)، لومړۍ برخه (Section I)')
    P(b, [('Write short answers to the following questions.', 'درج ذیل سوالات کے مختصر جوابات تحریر کریں۔', 'د لاندې پوښتنو لنډ ځوابونه ولیکئ.')])
    qa(b, QA[:8])
    r1 = model(b, 4, 1, 49, 78)
    t = Builder()
    qa(t, QA[8:16])
    t.p(*QA[16][:3])
    t.p(*QA[16][3:])
    BOOK.save(49, [(4, r1), (4, model(t, 4, 2, 49, 79))], issues=[{'id': 'eco12-pdf049', 'unit': 4, 'printedPage': 78,
               'description': 'Printed errors retained: answer 4 “اس کا بوجھ بھی اس شخص پر ہوتا وہ اس آگے منتقل نہیں کر سکتا”; answer 8 “متوان بجٹ” (for متوازن); answer 11 “اس محصولاتی تمدن” and the opening clause “حکومت کیلئے ٹیکسوں کے ذریعہ آمدنی حاصل کرے”; answer 9 “آمدنیوں کا فرق کھانا” (for گھٹانا).'}])


def p50():
    b = Builder()
    qa(b, QA[17:])
    b.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(b, [('Question 2. Write detailed answers to the following questions.', 'سوال 2۔ درج ذیل سوالات کے مفصل جوابات تحریر کریں۔', '۲ پوښتنه: د لاندې پوښتنو مفصل ځوابونه ولیکئ.')])
    L(b, LONG)
    P(b, [('Question 3. More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال 3۔ ہر سوال کے ایک سے زیادہ جواب دیئے گئے ہیں ان میں سے درست جواب پر (✓) کا نشان لگائیے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(b, MCQ[:4])
    r1 = model(b, 4, 3, 50, 80)
    t = Builder()
    mcqs(t, MCQ[4:], start=5)
    BOOK.save(50, [(4, r1), (4, model(t, 4, 4, 50, 81))], complete_units=[4], issues=[{'id': 'eco12-pdf050', 'unit': 4, 'printedPage': 80,
               'description': 'Printed answer ticks kept as printed. MCQ 2 “اصول مساوات کی مطلب”; Q3 instruction prints “(P)” for the tick mark; MCQs 2–3 and 7–8 have only three options in print; answer 17 (ii) “عام عوام نہیں کر سکتیں”. MCQ 15–16 percentages printed as given (75.32%; 68%), not consistent with the 80% and 79% figures in the chapter text. Chapter 4 ends on p.81.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 49
    {49: p49, 50: p50}[n]()
