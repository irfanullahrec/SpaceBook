"""HPE XII PDF36–41: pp.31–36 — precautionary measures against fire (cooking, heating, heater, electrical appliances, candle); protective guideline for
fire prevention (policy, building, public education, planning); sale of appliances; protective areas; preventing the spread of fire (heat); protection
from heat, machines and appliances, heaters. Run: python class12_hpe_page036.py N (36–41)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L


def p36():
    b = Builder()
    b.h('Precautionary measures for protection from fire', 'آگ سے بچاؤ کیلئے احتیاطی تدابیر', 'له اور د ژغورنې احتیاطي ګامونه')
    P(b, [('Since carelessness during cooking becomes the cause of many domestic losses, care should therefore be taken during cooking. If such an accident happens during cooking, then shut off the supply of gas and electricity so that fuel is not available for further loss. In the kitchen, things that catch fire such as furniture, clothes, paper and others should not be kept. Care and repair of the gas stove, stove and electrical appliances should be kept in mind. Even a small defect should not be considered minor; this very defect later becomes the cause of greater loss.',
           'چونکہ کوکنگ کے دوران بے احتیاطی بہت سے گھریلو نقصانات کا باعث بنتی ہے اس لیے کوکنگ کے دوران احتیاط برتی جائے۔ اگر کوکنگ کے دوران ایسا حادثہ پیش آ جائے تو گیس اور بجلی کی سپلائی بند کر دیں تاکہ مزید نقصان کے لیے ایندھن نہ ملے۔ کچن میں فرنیچر، کپڑے، پیپر اور دوسری آگ پکڑنے والی اشیا نہ رکھی جائیں۔ گیس کے چولہے، سٹوپ اور بجلی کے آلات کی دیکھ بھال اور مرمت کا خیال رکھا جائے۔ چھوٹے سے چھوٹے نقص کو بھی ہلکا نہ سمجھا جائے۔ یہی نقص بعد ازاں زیادہ نقصان کا باعث بن جاتا ہے۔',
           'څرنګه چې د پخلي پر مهال بې‌احتیاطي د ډېرو کورنیو زیانونو لامل کېږي، نو د پخلي پر مهال دې احتیاط وشي. که د پخلي پر مهال داسې پېښه وشي، د ګاز او برېښنا رسول بند کړئ ترڅو د نور زیان لپاره سونګ برابر نه شي. په پخلنځي کې دې فرنیچر، جامې، کاغذ او نور اور اخیستونکي توکي ونه ساتل شي. د ګاز بټۍ، سټوپ او برېښنايي وسایلو څارنې او ترمیم ته دې پام وشي. تر ټولو کوچنۍ نیمګړتیا دې هم سپکه ونه ګڼل شي؛ همدا نیمګړتیا وروسته د ډېر زیان لامل کېږي.'),
          ('For example, gas leaks from a gas stove. If this is left thinking it a minor leakage, it can later become the cause of heavy loss. It should be repaired properly or a good-quality stove should be bought.',
           'مثال کے طور پر گیس کے چولہے سے گیس لیکیج ہوتی ہے۔ اگر اس کو معمولی لیکیج خیال کر کے چھوڑ دی جائے تو یہ بعد میں بھاری نقصان کا سبب بن سکتی ہے۔ اس کو درست طریقے سے مرمت کروائی جائے یا اچھی کوالٹی کا چولہا خرید جائے۔',
           'د بېلګې په توګه له ګازي بټۍ ګاز لیکېږي. که دا معمولي لیکیج وګڼل شي او پرېښودل شي، وروسته د دروند زیان لامل کېدای شي. په سمه توګه دې ترمیم شي یا د ښه کیفیت بټۍ دې واخیستل شي.'),
          ('A checklist related to the kitchen should be made and fixed on the wall, because sometimes some work is forgotten, e.g. whether the main valve is closed, the ventilator is open, there is no leakage in the stove, etc.',
           'کچن سے متعلق چیک لسٹ بنا کر دیوار کے ساتھ لگائی جائے کیونکہ بعض دفعہ کچھ کام بھول جاتے ہیں۔ مثلاً مین والو بند کیا ہے۔ روشندان کھلا ہے۔ چولہے میں لیکیج تو نہیں ہے وغیرہ۔',
           'د پخلنځي اړوند چک لېست دې جوړ او پر دېوال ولګول شي، ځکه کله کله ځینې کارونه هېرېږي، لکه اصلي والو بند دی، کړکۍ (روښانه‌دان) خلاصه ده، په بټۍ کې لیکیج خو نشته او نور.')])
    b.h('Heating', 'حرارت (Heating)', 'تودوخه (Heating)')
    P(b, [('In homes heat is the second cause in accidents of fire. Especially in the winter season more incidents happen. Defective heaters of light gas and electricity become the cause of more trouble. If the curtains of windows, bed sheets and clothes are near these appliances, they catch fire smouldering.',
           'گھروں میں آگ کے حادثات میں حرارت دوسری وجہ ہے۔ خاص کر سردی کے موسم میں زیادہ واقعات ہوتے ہیں۔ ہلکے گیس اور بجلی کے ناقص ہیٹر زیادہ مصیبت کا سبب بنتے ہیں۔ اگر کھڑکی کے پردے، بستر کی چادریں، کپڑے ان آلات کے نزدیک ہوں۔ تو یہ سلگتے ہوئے آگ پکڑ لیتے ہیں۔',
           'په کورونو کې د اور په پېښو کې تودوخه دویم لامل دی. په ځانګړې توګه د ژمي په موسم کې ډېرې پېښې کېږي. د ګاز او برېښنا ټیټ کیفیت ناقص هیټرونه د ډېرې ستونزې لامل کېږي. که د کړکۍ پردې، د بستر څادرونه او جامې دې وسایلو ته نږدې وي، نو لوګي کېږي او اور اخلي.')])
    b.h('Heater', 'ہیٹر', 'هیټر')
    P(b, [('On every side of the heater there should be empty space up to one metre. In this space no thing that catches fire should be kept. The heater should be kept away from furniture, bed sheets, people and pets. In the winter season the heater etc. should be checked. In winter, while sleeping at night, close the valve of the heater.',
           'ہیٹر کے ہر طرف ایک میٹر تک خالی جگہ ہو۔ اس جگہ میں آگ پکڑنے والی کوئی چیز نہ رکھی جائے۔ ہیٹر کو فرنیچر، بیڈ شیٹ، لوگوں اور پالتوں جانوروں سے دور رکھا جائے۔ سردیوں کے موسم میں ہیٹر وغیرہ کو چیک کیا جائے۔ سردیوں میں رات کو سوتے وقت ہیٹر کا والو بند کریں۔',
           'د هیټر هرې خوا ته تر یوه متره تشه ځای وي. په دې ځای کې دې هېڅ اور اخیستونکی شی کېښودل نه شي. هیټر دې له فرنیچر، بستر څادر، خلکو او کورنیو څارویو لرې وساتل شي. د ژمي په موسم کې دې هیټر او نور وکتل شي. په ژمي کې د شپې د ویده کېدو پر مهال د هیټر والو بند کړئ.')])
    r = rec(b, 4, 4, 36)
    BOOK.save(36, [(4, r)], issues=[{'id': 'hpe12-pdf036', 'unit': 4, 'printedPage': 31,
               'description': 'A dark scan blotch at the top left does not hide text. “معمولی لیکیج خیال کر کے چھوڑ دی جائے”, “چولہا خرید جائے”, “پالتوں جانوروں”. Retained as printed.'}])


def p37():
    b = Builder()
    b.h('Electrical appliances', 'بجلی کے آلات', 'برېښنايي وسایل')
    P(b, [('In homes, buildings and schools electrical appliances are installed. Because of old and rotten electric wires they can become the cause of an accident at any time. Check the electric wiring to see that they do not get hot on load. If they get hot on load, change them and install good quality. For things with more load such as freezer, refrigerator, oven, iron etc., power plugs should be installed.',
           'گھروں، عمارتوں اور سکولوں میں بجلی کے آلات نصب ہوتے ہیں۔ بجلی کی تاریں پرانی اور بوسیدہ ہونے کی وجہ سے کسی بھی وقت حادثے کا باعث بن سکتی ہے۔ بجلی کی وائرنگ کو چیک کریں کہ یہ لوڈ پڑنے پر گرم تو نہیں ہوتے۔ اگر لوڈ پڑنے پر گرم ہوتے ہیں تو ان کو تبدیل کر کے اچھی کوالٹی کی لگوائیں۔ زیادہ لوڈ والی چیزوں مثلاً فریزر، ریفریجریٹر، اوون، استری وغیرہ کے لیے پاور پلگ لگوائے جائیں۔',
           'په کورونو، ودانیو او ښوونځیو کې برېښنايي وسایل لګول شوي وي. د برېښنا مزي د زړښت او خرابېدو له امله هر وخت د پېښې لامل کېدای شي. د برېښنا وایرنګ وګورئ چې د بار پر وخت ګرم خو نه کېږي. که د بار پر وخت ګرمېږي، بدل یې کړئ او ښه کیفیت ولګوئ. د ډېر بار لرونکو توکو لکه فریزر، یخچال، اوون، اوتو او نورو لپاره دې پاور پلګونه ولګول شي.')])
    b.h('Candle', 'موم بتی', 'شمع')
    P(b, [('A candle too becomes the cause of fire through carelessness, because the flame of a candle is open. If going out of the room, extinguish the candle. Leaving a candle burning in the room is inviting danger or an accident. At night while sleeping do not leave the candle burning. Besides this, keep things that start fire, e.g. matches, lighters etc., out of the reach of children.',
           'موم بتی بھی بے احتیاطی کی وجہ سے آگ کا سبب بنتی ہے۔ کیونکہ موم بتی کا شعلہ کھلا ہوتا ہے۔ اگر کمرے سے باہر جا رہے ہوں تو موم بتی بجھا دیں۔ کمرے میں موم بتی کو سلگتے ہوئے چھوڑنا خطرے یا حادثے کو دعوت دینا ہے۔ رات کو سوتے وقت موم بتی کو جلتا ہوا نہ چھوڑیں۔ اس کے علاوہ آگ لگانے والی اشیاء مثلاً ماچس، لائٹر وغیرہ بچوں کی پہنچ سے دور رکھیں۔',
           'شمع هم د بې‌احتیاطۍ له امله د اور لامل کېږي، ځکه د شمعې لمبه خلاصه وي. که له کوټې بهر ځئ، شمع مړه کړئ. په کوټه کې بله شمع پرېښودل خطر یا پېښې ته بلنه ده. د شپې د ویده کېدو پر وخت شمع بله مه پرېږدئ. سربېره پر دې اور لګوونکي توکي، لکه اورلګیت، لایټر او نور، د ماشومانو له لاسرسي لرې وساتئ.')])
    b.h('Protective guideline for protection from fire', 'آگ سے بچاؤ کے لیے حفاظتی گائیڈ لائن', 'له اور د ژغورنې ساتنیز لارښود')
    b.h('Policy for protection from fire', 'آگ سے بچاؤ کیلئے پالیسی', 'له اور د ژغورنې پالیسي')
    P(b, [('Policies should be made for buildings for protection from fire. These policies should be strictly implemented, and in this regard no concession of any kind should be given.',
           'عمارتوں کو آگ سے بچاؤ کیلئے پالیسیاں بنائی جائیں۔ ان پالیسیوں پر سختی سے عمل درآمد کروایا جائے۔ اور اس سلسلے میں کسی قسم کی کوئی رعایت نہ دی جائے۔',
           'د ودانیو د اور څخه د ژغورنې لپاره پالیسۍ جوړې شي. پر دې پالیسیو دې په کلکه عمل وشي او په دې برخه کې دې هېڅ ډول اسانتیا ورنه کړل شي.')])
    L(b, [('Facilities should be kept in the building according to the law.', 'عمارت میں قانون کے مطابق سہولیات رکھی جائیں۔', 'په ودانۍ کې دې د قانون سره سم اسانتیاوې وساتل شي.'),
          ('The necessary measures related to protection from fire should have been taken in the building.', 'آگ سے بچاؤ کے متعلق عمارت میں ضروری اقدامات کئے گئے ہوں۔', 'له اور د ژغورنې اړوند اړین ګامونه دې په ودانۍ کې اخیستل شوي وي.')])
    r = rec(b, 4, 5, 37)
    BOOK.save(37, [(4, r)], issues=[{'id': 'hpe12-pdf037', 'unit': 4, 'printedPage': 32,
               'description': 'The heading “بجلی کے آلات” is partly smudged in the scan. “تاریں … حادثے کا باعث بن سکتی ہے”, “یہ لوڈ پڑنے پر گرم تو نہیں ہوتے”. Retained as printed.'}])


def p38():
    b = Builder()
    L(b, [('Those living and working in the building should be aware of the laws and instructions.', 'عمارت میں رہنے والے اور کام والے قوانین اور ہدایات سے آگاہ ہوں۔', 'په ودانۍ کې اوسېدونکي او کارکوونکي دې له قوانینو او لارښوونو خبر وي.'),
          ('Emergency routes should be made and they should be made clear with signs.', 'ایمرجنسی راستے بنائے جائیں اور انھیں اشاروں سے واضح کیا جائے۔', 'بیړنۍ لارې دې جوړې شي او په نښو دې روښانه شي.'),
          ('Such electrical appliances should be installed as do not become too hot, and in case of any fault do not give a flame nor start to smoulder.', 'بجلی کے ایسے آلات نصب کئے جائیں جو زیادہ گرم نہ ہوں اور کسی فالٹ کی صورت میں شعلہ نہ دیں اور نہ ہی سلگنا شروع کر دیں۔', 'داسې برېښنايي وسایل دې ولګول شي چې ډېر ګرم نه شي او د کومې خرابۍ په صورت کې لمبه ورنه کړي او لوګي هم پیل نه کړي.'),
          ('Fire-extinguishing appliances should be easily available.', 'آگ بجھانے والے آلات آسانی سے دستیاب ہوں۔', 'د اور مړ کولو وسایل دې په اسانۍ برابر وي.'),
          ('Fire-extinguishing appliances should be of good quality and in proper condition.', 'آگ بجھانے والے آلات اچھی کوالٹی اور درست حالت میں ہوں۔', 'د اور مړ کولو وسایل دې ښه کیفیت او سم حالت ولري.'),
          ('If different solutions, e.g. acid or chemicals, are used inside the building, then work with extreme attention and care while storing and using them.', 'اگر مختلف محلول مثلاً تیزاب، کیمیکل عمارت کے اندر استعمال ہوتے ہوں تو ان کو سٹور کرنے اور استعمال کرنے کے دوران انتہائی توجہ اور احتیاط سے کام لیں۔', 'که بېلابېل محلولونه لکه تیزاب، کیمیاوي توکي په ودانۍ کې کارول کېږي، د زېرمه کولو او کارولو پر مهال ډېر پام او احتیاط وکړئ.'),
          ('Do not use smouldering and flame-giving things without need.', 'سلگنے اور شعلہ دینے والے اشیاء بغیر ضرورت کے استعمال نہ کریں۔', 'لوګي کوونکي او لمبه ورکوونکي توکي له اړتیا پرته مه کاروئ.'),
          ('Get the building checked from time to time. If some fault comes, close the building until the defect is removed.', 'وقفے وقفے سے عمارت کی چیکنگ کروائیں۔ اگر کوئی فالٹ آئے تو عمارت کو اس وقت تک بند کر دیں جب تک نقص دور نہیں کیا جاتا۔', 'وخت په وخت ودانۍ وګورئ. که کومه خرابي راشي، ودانۍ تر هغه بنده کړئ چې نیمګړتیا لرې نه شي.'),
          ('Get a fire-alarm system installed in the building.', 'عمارت میں فائر الارم سسٹم نصب کروائیں۔', 'په ودانۍ کې د اور خبرتیا سیستم ولګوئ.'),
          ('Practical training should be given to the staff of the building and awareness should be further increased.', 'عمارت کے عملے کی عملی تربیت کی جائے اور آگاہی کو مزید بڑھایا جائے۔', 'د ودانۍ کارکوونکو ته دې عملي روزنه ورکړل شي او پوهاوی دې لا زیات شي.'),
          ('The staff of the building should be made to practise on an annual basis.', 'عمارت کے عملے کی سالانہ بنیادوں پر مشق کروائی جائے۔', 'د ودانۍ کارکوونکو ته دې په کلني ډول تمرین ورکړل شي.')])
    b.h('Sale and purchase of appliances', 'آلات کی خرید و فروخت', 'د وسایلو پېر او پلور')
    P(b, [('The sale and purchase of fire appliances and things should be with approved persons, i.e. they should have a government licence and permit, and these persons should be responsible for making, storing, transporting, selling and using these appliances and things.',
           'آگ کے آلات و اشیاء کی خرید و فروخت منظور شدہ افراد کے پاس ہو۔ یعنی ان کے پاس گورنمنٹ کا لائسنس اور پرمٹ ہو یہ افراد ان آلات و اشیاء کو بنانے، سٹور کرنے، لانے لے جانے، فروخت کرنے اور استعمال کرنے کے ذمہ دار ہوں۔',
           'د اور د وسایلو او توکو پېر او پلور دې د منظور شویو کسانو سره وي، یعنې حکومتي جواز او اجازه‌لیک ولري او دا کسان دې د دې وسایلو او توکو د جوړولو، زېرمه کولو، وړلو راوړلو، پلورلو او کارولو مسؤل وي.')])
    L(b, [('The stores, shopkeepers or traders who keep fire-extinguishing appliances should be supervised so that they keep their …', 'آگ بجھانے کے آلات رکھنے والے سٹوروں، دکانداروں یا تجارت کرنے والوں کی نگرانی کرنی چاہیے تاکہ وہ ان …', 'د اور مړ کولو وسایل ساتونکو پلورنځیو، دوکاندارانو یا سوداګرو څارنه دې وشي ترڅو خپل …')])
    r = rec(b, 4, 6, 38)
    BOOK.save(38, [(4, r)], issues=[{'id': 'hpe12-pdf038', 'unit': 4, 'printedPage': 33,
               'description': '“رہنے والے اور کام والے”, “سلگنے اور شعلہ دینے والے اشیاء”. The end of the third bullet is cut at the left edge (“سلگنا”). Retained as printed.'}])


def p39():
    b = Builder()
    P(b, [('… appliances according to the standard.', 'آلات کو معیار کے مطابق رکھیں۔', '… وسایل د معیار سره سم وساتي.')])
    L(b, [('The place and quantity of flame-giving things should be kept limited.', 'شعلہ دینے والی اشیاء کی جگہ اور مقدار کو محدود رکھنا چاہیے۔', 'د لمبه ورکوونکو توکو ځای او مقدار دې محدود وساتل شي.'),
          ('In different buildings the number of persons should not be more than the capacity. For example, in assembly halls, hospitals, schools, theatres, care centres for old people, child-care centres etc., in these buildings instructions and appliances for dealing with an emergency should be present.', 'مختلف عمارتوں میں افراد کی تعداد گنجائش سے زیادہ نہ ہو۔ مثال کے طور پر اسمبلی ہال، ہسپتال، سکول، تھیٹر، بوڑھے افراد کے دیکھ بھال کے سینٹر، بچوں کے دیکھ بھال کے سینٹر وغیرہ ان عمارتوں میں ایمرجنسی سے نمٹنے کیلئے ہدایات اور آلات موجود ہوں۔', 'په بېلابېلو ودانیو کې دې د کسانو شمېر له ظرفیت زیات نه وي. د بېلګې په توګه اسمبلۍ تالار، روغتون، ښوونځی، تیاتر، د زړو کسانو د پاملرنې مرکزونه، د ماشومانو د پاملرنې مرکزونه او نور؛ په دې ودانیو کې دې له بیړني حالت سره د مقابلې لارښوونې او وسایل شتون ولري.')])
    b.h('Education of protection from fire for the public', 'عوام کیلئے آگ سے بچاؤ کی تعلیم', 'د خلکو لپاره له اور د ژغورنې زده‌کړه')
    L(b, [('Programmes of protection from fire should be started. In schools and colleges trained staff should go and give lectures to students on different topics related to protection from fire. Such programmes should be held at intervals during the year.', 'آگ سے بچاؤ کے پروگرام شروع کیے جائیں۔ سکولوں، کالجوں میں تربیت یافتہ عملہ جا کر طلباء کو آگ سے بچاؤ کے متعلق مختلف عنوانات پر لیکچر دیں۔ ایسے پروگرام سال میں وقفے وقفے سے کروائے جائیں۔', 'له اور د ژغورنې پروګرامونه دې پیل شي. په ښوونځیو او کالجونو کې روزل شوي کارکوونکي دې ورشي او زده‌کوونکو ته د اور څخه د ژغورنې پر بېلابېلو موضوعاتو لکچر ورکړي. داسې پروګرامونه دې په کال کې وخت په وخت جوړ شي.'),
          ('In the curriculum of educational institutions material should be included about the causes of fire and the use of appliances that help in controlling fire.', 'تعلیمی اداروں کے نصاب میں آگ لگنے کی وجوہات اور آگ پر قابو پانے میں مدد دینے والے آلات کے استعمال کے بارے میں مواد شامل کیا جائے۔', 'د تعلیمي ادارو په نصاب کې دې د اور لګېدو د لاملونو او د اور په کنټرول کې مرستندویو وسایلو د کارولو په اړه مواد شامل شي.')])
    b.h('Planning for protection from fire', 'آگ سے بچاؤ کی منصوبہ بندی', 'له اور د ژغورنې پلان جوړونه')
    P(b, [('Planning for protection from fire in a building is necessary. Planning in the building is the responsibility of the owner of the building. Inside the building systems should be installed for dealing with an emergency, e.g. emergency alarm, emergency doors, circuit breakers etc. Training of its staff and planning for protection from fire should be made compulsory on the institution and on the owner of the building.',
           'عمارت میں آگ سے بچاؤ کیلئے منصوبہ بندی ضروری ہے۔ عمارت میں منصوبہ بندی کرنا، عمارت کے مالک کی ذمہ داری ہے۔ عمارت کے اندر ایمرجنسی سے نمٹنے کیلئے سسٹم لگے ہوں۔ مثلاً ایمرجنسی الارم، ایمرجنسی دروازے، سرکٹ بریکر وغیرہ۔ ادارے پر اپنے سٹاف اور عمارت کے مالک پر اپنے سٹاف کی تربیت اور آگ سے بچاؤ کیلئے منصوبہ بندی کو لازمی قرار دی جائے۔',
           'په ودانۍ کې له اور د ژغورنې لپاره پلان جوړونه اړینه ده. په ودانۍ کې پلان جوړول د ودانۍ د مالک مسؤلیت دی. د ودانۍ دننه دې له بیړني حالت سره د مقابلې سیستمونه لګېدلي وي، لکه بیړنی الارم، بیړنۍ دروازې، سرکټ بریکرونه او نور. پر ادارې او د ودانۍ پر مالک دې د خپلو کارکوونکو روزنه او له اور د ژغورنې پلان جوړونه اړینه وګرځول شي.')])
    b.h('Planning for protection from fire', 'آگ سے بچاؤ کیلئے منصوبہ بندی', 'له اور د ژغورنې لپاره پلان جوړونه')
    P(b, [('In a building or institution special care should be taken of the following things.', 'عمارت یا ادارے میں مندرجہ ذیل باتوں کا خاص خیال رکھا جائے۔', 'په ودانۍ یا اداره کې دې لاندې خبرو ته ځانګړې پاملرنه وشي.')])
    L(b, [('A diary of necessary phone numbers.', 'ضروری فون نمبروں کی ڈائری۔', 'د اړینو ټیلیفون شمېرو ډایري.'),
          ('Water, gas and electricity lines and valves.', 'پانی، گیس اور بجلی کے لائنز اور والو۔', 'د اوبو، ګاز او برېښنا لیکې او والونه.')])
    r = rec(b, 4, 7, 39)
    BOOK.save(39, [(4, r)], issues=[{'id': 'hpe12-pdf039', 'unit': 4, 'printedPage': 34,
               'description': 'The heading “آگ سے بچاؤ کی/کیلئے منصوبہ بندی” is printed twice in succession. Large owner pen strokes over the public-education paragraph and owner Urdu notes are excluded. “منصوبہ بندی کو لازمی قرار دی جائے”. Retained as printed.'}])


def p40():
    b = Builder()
    L(b, [('A special place for dangerous material.', 'خطرناک میٹیریل کے لیے مخصوص جگہ۔', 'د خطرناکو موادو لپاره ځانګړی ځای.'),
          ('Information about the structure, drawing and site plan of the building.', 'عمارت کے ڈھانچے، ڈرائنگ اور سائٹ پلان کی معلومات۔', 'د ودانۍ د جوړښت، نقشې او ساحې پلان معلومات.'),
          ('Schedule of repair of life-saving systems and appliances.', 'زندگی بچانے والے سسٹم اور آلات کی مرمت کا شیڈول۔', 'د ژوند ژغورونکو سیستمونو او وسایلو د ترمیم مهالوېش.'),
          ('Method of practical training and drill of staff.', 'سٹاف کی عملی تربیت اور مشق کا طریقہ کار۔', 'د کارکوونکو د عملي روزنې او تمرین طریقه.')])
    b.h('Protective areas', 'حفاظتی علاقے', 'ساتنیزې سیمې')
    P(b, [('The benefit of planning for protection from fire is that the fire-extinguishing staff know in which direction they have to go inside the building, and at which place what is built, e.g. store, room, washroom, stairs. From this the staff can be saved from dangerous material and can find this material and take it out. This planning not only helps in extinguishing fire and in access to dangerous material, but is also necessary for the safety of the fire-extinguishing staff.',
           'آگ سے بچاؤ کی منصوبہ بندی کا فائدہ یہ ہوتا ہے کہ آگ بجھانے والے عملہ کو علم ہوتا ہے کہ اس نے عمارت کے اندر کس طرف جانا ہے۔ کس کس جگہ پر کیا بنا ہوا ہے مثلاً سٹور، کمرہ، واش روم، سیڑھیاں۔ اس سے عملہ خطرناک میٹریل سے بچ سکتا ہے اور اس میٹریل کو ڈھونڈ کر باہر نکال سکتا ہے۔ یہ منصوبہ بندی نہ صرف آگ بجھانے اور خطرناک میٹریل تک رسائی میں مدد دیتا ہے بلکہ آگ بجھانے والے عملے کی حفاظت کیلئے بھی ضروری ہے۔',
           'له اور د ژغورنې د پلان جوړونې ګټه دا ده چې اور وژونکي کارکوونکي پوهېږي چې په ودانۍ کې کومې خوا ته ځي او په کوم ځای کې څه جوړ دي، لکه زېرمتون، کوټه، تشناب، زینې. له دې کارکوونکي له خطرناکو موادو ژغورل کېدای شي او دا مواد موندلی او بهر ایستلی شي. دا پلان جوړونه نه یوازې د اور په مړ کولو او خطرناکو موادو ته په لاسرسي کې مرسته کوي، بلکې د اور وژونکو کارکوونکو د خوندیتوب لپاره هم اړینه ده.')])
    b.h('Preventing fire from spreading', 'آگ کو پھیلنے سے روکنا', 'د اور د خپرېدو مخنیوی')
    P(b, [('For fire to burn three elements are needed. These are heat, oxygen and fuel. Without heat, oxygen and fuel fire cannot burn. To stop fire from spreading, if one or more of these three elements is removed, the fire will go out.',
           'آگ کو جلنے کیلئے تین عناصر کی ضرورت ہوتی ہے۔ یہ حرارت، آکسیجن اور ایندھن ہیں۔ حرارت، آکسیجن اور ایندھن کے بغیر آگ نہیں جل سکتی۔ آگ کو پھیلنے سے روکنے کیلئے ان تین عناصر میں سے ایک کو ہٹائیں یا ایک سے زیادہ کو ہٹا دیں تو آگ بجھ جائے گی۔',
           'اور د سوځېدو لپاره درېیو عناصرو ته اړتیا لري. دا تودوخه، اکسیجن او سونګ دي. له تودوخې، اکسیجن او سونګ پرته اور نه شي بلېدای. د اور د خپرېدو د مخنیوي لپاره که له دې درېیو عناصرو یو یا له یوه زیات لرې کړئ، اور به مړ شي.')])
    b.h('1. Heat', '1۔ حرارت (Heat)', '1. تودوخه (Heat)')
    P(b, [('During work heat is produced, e.g. heat is necessary to cook food in a pot or on a griddle. This heat should be kept under control and kept away from fuel. Heat is produced from different works. During this, work should be done with more attention. It is necessary that a checklist related to this work be made so that no work remains forgotten.',
           'کام کے دوران حرارت پیدا ہوتی ہے مثلاً کھانا پکانے کیلئے پتیلی یا توے کیلئے حرارت ضروری ہوتی ہے۔ اس حرارت کو کنٹرول میں رکھا جائے اور ایندھن سے دور رکھا جائے۔ حرارت مختلف کاموں سے پیدا ہوتی ہے۔ اس دوران زیادہ توجہ سے کام لیا جائے۔ ضروری ہے کہ اس کام سے متعلق چیک لسٹ بنائی جائے تاکہ کوئی کام بھولے سے نہ رہ جائے۔',
           'د کار پر مهال تودوخه پیدا کېږي، لکه د خوړو پخولو لپاره دېګ یا تبي ته تودوخه اړینه ده. دا تودوخه دې تر کنټرول لاندې او له سونګ لرې وساتل شي. تودوخه له بېلابېلو کارونو پیدا کېږي. په دې وخت کې دې ډېر پام وشي. اړینه ده چې د دې کار اړوند چک لېست جوړ شي ترڅو کوم کار هېر پاتې نه شي.')])
    r = rec(b, 4, 8, 40)
    BOOK.save(40, [(4, r)], issues=[{'id': 'hpe12-pdf040', 'unit': 4, 'printedPage': 35,
               'description': 'A small owner pen mark is excluded. “یہ منصوبہ بندی … مدد دیتا ہے”. Retained as printed.'}])


def p41():
    b = Builder()
    b.h('Protection from heat', 'حرارت سے حفاظت', 'له تودوخې ساتنه')
    L(b, [('People should be aware of their responsibilities.', 'افراد اپنی ذمہ داریوں سے آگاہ ہوں۔', 'کسان دې له خپلو مسؤلیتونو خبر وي.'),
          ('Chimneys should be inspected and cleaned daily.', 'چمنیوں کا معائنہ اور صفائی روزانہ کی جائے۔', 'بخارۍ دې هره ورځ معاینه او پاکې شي.'),
          ('In the building, offices, shops and residential flats should be built separately. Necessary arrangements should be made there.', 'عمارت میں دفتر، دکانیں، رہائشی فلیٹس علیحدہ علیحدہ بنائے جائیں۔ وہاں پر ضروری انتظامات کیے جائیں۔', 'په ودانۍ کې دې دفترونه، دوکانونه او د اوسېدو فلیټونه جلا جلا جوړ شي. هلته دې اړین انتظامات وشي.'),
          ('Whenever food is being cooked, stand near it till the end.', 'جب بھی کھانا بنا رہے ہوں۔ اس کے پاس آخر تک کھڑے رہیں۔', 'کله چې خواړه پخوئ، تر پایه ورسره ولاړ اوسئ.')])
    b.h('Machines and appliances', 'مشین اور آلات', 'ماشینونه او وسایل')
    P(b, [('If machines and appliances are not installed in the proper way, they can become the cause of fire.', 'مشین اور آلات اگر درست طریقے سے نصب نہ ہو تو آگ کا سبب بن سکتی ہے۔', 'که ماشینونه او وسایل په سمه توګه ونه لګول شي، د اور لامل کېدای شي.')])
    L(b, [('Make sure that all working appliances are safe from excessive heat or catching fire.', 'یہ تسلی کریں کہ تمام کام کرنے والے آلات زیادہ حرارت یا آگ پکڑنے سے محفوظ ہوں۔', 'ډاډ ترلاسه کړئ چې ټول کاري وسایل له ډېرې تودوخې یا اور اخیستو خوندي دي.'),
          ('There should be a proper arrangement of ventilation in the home.', 'گھر میں ہوا کی آمد و رفت کا مناسب انتظام ہو۔', 'په کور کې دې د هوا د تګ راتګ مناسب انتظام وي.'),
          ('The electric wiring in homes should be correct.', 'گھروں میں بجلی کی وائرنگ درست ہو۔', 'په کورونو کې دې د برېښنا وایرنګ سم وي.'),
          ('Heat-producing appliances should be kept correct and clean, such as burners, oven, stove, freezer etc.; necessary flame-giving material (oil, petrol, diesel, gas) should be kept away from these appliances.', 'حرارت پیدا کرنے والے آلات کو درست اور صاف رکھا جائے جیسے برنر، اوون، سٹوپ، فریزر وغیرہ ان آلات سے ضروری شعلہ دینے والے میٹریل (تیل، پیٹرول، ڈیزل، گیس) سے دور رکھا جائے۔', 'تودوخه پیدا کوونکي وسایل دې سم او پاک وساتل شي، لکه برنر، اوون، سټوپ، فریزر او نور؛ له دې وسایلو دې لمبه ورکوونکي مواد (تېل، پټرول، ډیزل، ګاز) لرې وساتل شي.'),
          ('There should be a proper arrangement for the care of machines and appliances, e.g. opening the machines, cleaning, changing oil, repairing parts, getting new parts installed etc.', 'مشینوں اور آلات کی دیکھ بھال کا مناسب انتظام ہو مثلاً مشینوں کو کھولنا، صفائی کرنا، تیل تبدیل کرنا، پرزے مرمت کرنا، پرزے نئے لگوانا وغیرہ۔', 'د ماشینونو او وسایلو د پاملرنې مناسب انتظام دې وي، لکه د ماشینونو پرانیستل، پاکول، تېل بدلول، د پرزو ترمیم، نوي پرزې لګول او نور.')])
    b.h('Heaters', 'ہیٹر (Heaters)', 'هیټرونه (Heaters)')
    L(b, [('Do not use light heaters unnecessarily.', 'غیر ضروری طور پر ہلکے ہیٹر استعمال نہ کریں۔', 'بې‌ضرورته ټیټ کیفیت هیټرونه مه کاروئ.'),
          ('Emergency switches and control buttons should be installed with them.', 'ان کے ساتھ ایمرجنسی سوئچ اور کنٹرول کرنے والے بٹن لگے ہوں۔', 'ورسره دې بیړني سویچونه او د کنټرول تڼۍ لګېدلې وي.'),
          ('When going out of the room or going to sleep, turn off the heater.', 'جب کمرے سے باہر جائیں یا سونے لگیں تو ہیٹر بند کر دیں۔', 'کله چې له کوټې بهر ځئ یا ویده کېږئ، هیټر بند کړئ.'),
          ('Remaining things should remain at a distance of one metre from them.', 'باقی اشیاء ان سے ایک میٹر کے فاصلے پر رہیں۔', 'نور توکي دې له دوی یو متر لرې وي.'),
          ('Do not keep them near dry clothes.', 'خشک کپڑوں کے پاس نہ رکھیں۔', 'وچو جامو ته یې نږدې مه ږدئ.')])
    r = rec(b, 4, 9, 41)
    BOOK.save(41, [(4, r)], issues=[{'id': 'hpe12-pdf041', 'unit': 4, 'printedPage': 36,
               'description': '“مشین اور آلات اگر درست طریقے سے نصب نہ ہو تو آگ کا سبب بن سکتی ہے”; the stove bullet lists “فریزر” among heat-producing appliances. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 36
    {36: p36, 37: p37, 38: p38, 39: p39, 40: p40, 41: p41}[n]()
