"""HPE XII PDF42–47: pp.37–42 — work giving flame or heat; protection from electricity; deliberate arson; instructions for shop, home, school, workshop,
factory; fuel; flame-giving liquid material; oxygen (with fire-safety infographic); first aid; first aid for burns. Run: python class12_hpe_page042.py N (42–47)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L


def p42():
    b = Builder()
    b.h('Work that gives flame or heat', 'شعلہ یا حرارت دینے والا کام', 'لمبه یا تودوخه ورکوونکی کار')
    P(b, [('From this work there is a fear of fire through heat, sparks and the rising of flames, e.g. welding, grinding work etc. This work is dangerous. They should be kept under strict control.',
           'اس کام سے حرارت، چنگاری اور شعلہ اٹھنے سے آگ لگنے کا اندیشہ ہوتا ہے۔ مثلاً ویلڈنگ، گرینڈنگ کا کام وغیرہ یہ کام خطرناک ہوتا ہے۔ انھیں سختی سے کنٹرول میں رکھا جائے۔',
           'له دې کار تودوخې، سپرغۍ او لمبې پورته کېدو له امله د اور لګېدو وېره وي، لکه ویلډنګ، ګرېنډنګ کار او نور. دا کار خطرناک دی. په کلکه دې تر کنټرول لاندې وساتل شي.')])
    L(b, [('Do this work only in that case when there is no alternative to it.', 'صرف اسی صورت میں یہ کام کریں جب اس کا متبادل نہ ہو۔', 'دا کار یوازې په هغه صورت کې وکړئ چې بدیل یې نه وي.'),
          ('It should be certain that those working on heat are aware of its method and control.', 'یہ یقین ہو کہ حرارت پر کام کرنے والے اس کے طریقہ کار اور کنٹرول سے آگاہ ہیں۔', 'ډاډ دې وي چې پر تودوخې کار کوونکي د هغې له طریقې او کنټرول خبر دي.'),
          ('Fire-resistant clothes should be used.', 'آگ سے مزاحمت کرنے والے کپڑے استعمال کیے جائیں۔', 'اور ضد جامې دې وکارول شي.'),
          ('Work with responsibility.', 'ذمہ داری کے ساتھ کام کریں۔', 'په مسؤلیت کار وکړئ.'),
          ('It should be checked and supervised as a routine.', 'معمول کے مطابق چیک کیا جائے اور نگرانی کی جائے۔', 'د معمول سره سم دې وکتل شي او څارنه دې وشي.'),
          ('Things that are removed should be taken to a safe place.', 'جو اشیاء ہٹائی جائیں ان کو محفوظ جگہ پہنچایا جائے۔', 'کوم توکي چې لرې کېږي، خوندي ځای ته دې ورسول شي.'),
          ('Things that catch fire should be removed with safety.', 'آگ پکڑنے والی اشیاء کو باحفاظت ہٹایا جائے۔', 'اور اخیستونکي توکي دې په خوندیتوب لرې شي.'),
          ('There should be separate staff whose responsibility relates only to fire.', 'علیحدہ سٹاف ہو جس کی ذمہ داری صرف آگ سے متعلق ہو۔', 'جلا کارکوونکي دې وي چې مسؤلیت یې یوازې له اور سره تړاو ولري.'),
          ('The workplace should be kept clean and safe.', 'کام کی جگہ کو صاف اور محفوظ رکھا جائے۔', 'د کار ځای دې پاک او خوندي وساتل شي.'),
          ('After completing the work it should certainly be checked a last time, and it should also be checked one hour after completing the work.', 'کام کو مکمل کرنے کے بعد آخری دفعہ چیک ضرور کیا جائے اور کام مکمل کرنے کے ایک گھنٹہ بعد بھی چیک کیا جائے۔', 'د کار له بشپړېدو وروسته دې خامخا وروستی ځل وکتل شي او له بشپړېدو یو ساعت وروسته دې هم وکتل شي.')])
    b.h('Protection / safety from electricity', 'بجلی سے حفاظت / بچاؤ', 'له برېښنا ساتنه / ژغورنه')
    L(b, [('The design, installation, construction and repair of all electrical installations and appliances should be safe and away from danger.', 'بجلی کی تمام تنصیبات اور آلات کے ڈیزائن، ان کی تنصیب، تعمیر و مرمت محفوظ اور خطرے سے دور ہو۔', 'د برېښنا د ټولو تاسیساتو او وسایلو ډیزاین، لګول، جوړول او ترمیم دې خوندي او له خطر لرې وي.'),
          ('The repair and installation of electrical appliances should be done by an expert electrician.', 'بجلی کے آلات کی مرمت اور تنصیب ماہر الیکٹریشن سے کروائی جائے۔', 'د برېښنايي وسایلو ترمیم او لګول دې د ماهر برېښنا‌کار له خوا وشي.'),
          ('Electrical appliances and wiring should be protected from gnawing animals.', 'بجلی کے آلات اور وائرنگ کو کترنے والے جانوروں سے بچایا جائے۔', 'برېښنايي وسایل او وایرنګ دې له ژووونکو څارویو وژغورل شي.'),
          ('Electrical appliances should be checked and the defect of the appliances should be eliminated.', 'بجلی کے آلات کو چیک کیا جائے اور آلات کے نقص کو ختم کیا جائے۔', 'برېښنايي وسایل دې وکتل شي او د وسایلو نیمګړتیا دې لرې شي.')])
    r = rec(b, 4, 10, 42)
    BOOK.save(42, [(4, r)])


def p43():
    b = Builder()
    L(b, [('Electric wires should be in good condition.', 'بجلی کی تاریں اچھی حالت میں ہوں۔', 'د برېښنا مزي دې په ښه حالت کې وي.'),
          ('If there is need of extra wires, it should be used with safety. These wires should not be kept under places of ordinary walking about and under carpets.', 'اگر اضافی تاروں کی ضرورت ہو تو اسے حفاظت سے استعمال کیا جائے۔ ان تاروں کو عام چلنے پھرنے کی جگہوں اور کارپٹ کے نیچے نہ رکھا جائے۔', 'که اضافي مزو ته اړتیا وي، په خوندیتوب دې وکارول شي. دا مزي دې د عام ګرځېدو ځایونو او غالۍ لاندې نه ساتل کېږي.'),
          ('Use one socket for one device.', 'ایک ڈیوائس کے لیے ایک ہی ساکٹ استعمال کریں۔', 'د یوه وسیلې لپاره یو ساکټ وکاروئ.')])
    b.h('Setting fire deliberately:', 'جان بوجھ کر آگ لگانا:', 'په قصدي ډول اور لګول:')
    P(b, [('Some saboteurs and ignorant people set fire to achieve their evil aims. This becomes the cause of the greatest terror at workplaces. Saboteurs, seeing material that inflames fire, set fire to it. If such material is lying around the building, it should be removed without delay. There should be appropriate security arrangements and the stored material should be protected. In this way this particular problem can be removed.',
           'کچھ تخریب کار اور جاہل لوگ اپنے مذموم عزائم حاصل کرنے کے لیے آگ لگا دیتے ہیں۔ یہ کام کرنے والی جگہوں پر سب سے زیادہ وحشت کا باعث بنتی ہے۔ تخریب کار لوگ آگ بھڑکانے والا میٹریل دیکھ کر اس میں آگ لگا دیتے ہیں۔ عمارت کے ارد گرد اگر ایسا میٹریل پڑا ہو تو اس کو بلا توقف ہٹایا جائے۔ مناسب سیکورٹی کے انتظامات ہوں، سٹور کیے گئے میٹریل کی حفاظت کی جائے۔ اس طریقے سے اس مخصوص مسئلے کو رفع کیا جا سکتا ہے۔',
           'ځینې ورانکاري او ناپوه خلک د خپلو ناوړه موخو د ترلاسه کولو لپاره اور لګوي. دا د کار په ځایونو کې د تر ټولو ډېرې وېرې لامل کېږي. ورانکاري خلک اور بلوونکي مواد ویني او اور پکې لګوي. که د ودانۍ شاوخوا داسې مواد پراته وي، بې‌ځنډه دې لرې شي. مناسب امنیتي انتظامات دې وي او زېرمه شوي مواد دې وساتل شي. په دې طریقه دا ځانګړې ستونزه لرې کېدای شي.'),
          ('Sometimes saboteurs attack workplaces (shop, school, home, factory, workshop); the workers there and other employees should remain alert to these hidden dangers. Remain alert to small incidents of fire, because these small incidents of fire become the cause of big losses.',
           'بعض دفعہ کام کی جگہوں (دکان، سکول، گھر، فیکٹری، ورکشاپ) پر تخریب کار لوگ حملہ کرتے ہیں وہاں کام کرنے والے اور دوسرے ملازمین ان چھپے ہوئے خطرات سے چوکنا رہیں۔ چھوٹے موٹے آگ لگنے کے واقعات سے الرٹ رہیں کیونکہ یہ چھوٹے موٹے آگ کے واقعات بڑے نقصان کا باعث بن جاتے ہیں۔',
           'کله کله د کار پر ځایونو (دوکان، ښوونځی، کور، فابریکه، ورکشاپ) ورانکاري خلک برید کوي؛ هلته کارکوونکي او نور کارمندان دې له دې پټو خطرونو خبر اوسي. د اور له وړو پېښو خبر اوسئ، ځکه دا وړې پېښې د لویو زیانونو لامل کېږي.')])
    b.h('Necessary instructions for shop, home, school, workshop, factory:', 'دکان، گھر، سکول، ورکشاپ، فیکٹری کیلئے ضروری ہدایات:', 'د دوکان، کور، ښوونځي، ورکشاپ، فابریکې لپاره اړینې لارښوونې:')
    L(b, [('Arranging appropriate security at different places of the building.', 'عمارت کی مختلف جگہوں پر مناسب سیکورٹی کا انتظام کرنا۔', 'د ودانۍ په بېلابېلو ځایونو کې د مناسب امنیت انتظام.'),
          ('Protecting the building from access of unconcerned persons.', 'غیر متعلقہ افراد کی رسائی سے عمارت کو بچانا۔', 'ودانۍ د نااړوندو کسانو له لاسرسي ساتل.'),
          ('Storing and protecting things that inflame/catch fire in a careful way.', 'آگ بھڑکنے / پکڑنے والی اشیاء کو محتاط طریقے سے سٹور کرنا اور حفاظت کرنا۔', 'د اور بلوونکو / اخیستونکو توکو په احتیاط زېرمه کول او ساتل.')])
    r = rec(b, 4, 11, 43)
    BOOK.save(43, [(4, r)])


def p44():
    b = Builder()
    b.h('Fuel', 'ایندھن (Fuel)', 'سونګ (Fuel)')
    P(b, [('Places where a large quantity of burning material is lying, stored or in use — there the danger is greater. Flame-giving fuel burns even in a normal environment. In this fuel liquid fuels (kerosene oil, petrol, diesel, gases) which can give flame (CNG, LPG) and solid things (wood, coal, paper, clothes, grass) are included. It is very necessary that at the workplace there be details of all such things as give flame and become the cause of fire.',
           'ایسی جگہیں جہاں بڑی مقدار میں جلنے والا مواد پڑا ہو، سٹور ہو یا استعمال میں ہو وہاں زیادہ خطرہ ہوتا ہے۔ جلنے والا یا شعلہ دینے والا ایندھن نارمل ماحول میں بھی جل جاتا ہے۔ اس ایندھن میں مائع ایندھن (مٹی کا تیل، پیٹرول، ڈیزل، گیسیں) جو شعلہ دے سکتی ہیں (سی این جی، ایل پی جی) اور ٹھوس چیزیں (لکڑی، کوئلہ، پیپر، کپڑے، گھاس) شامل ہیں۔ یہ بہت ضروری ہے کہ کام کی جگہ پر ایسی تمام چیزوں کی تفصیل موجود ہو جو شعلہ دیتی ہوں اور آگ لگنے کا سبب بنتی ہیں۔',
           'هغه ځایونه چې په لوی مقدار سوځېدونکي مواد پراته، زېرمه یا په کار کې وي، هلته خطر ډېر وي. سوځېدونکی یا لمبه ورکوونکی سونګ په عادي چاپېریال کې هم سوځي. په دې سونګ کې مایع سونګ (د خاورو تېل، پټرول، ډیزل، ګازونه) چې لمبه ورکولی شي (CNG، LPG) او جامد توکي (لرګي، سکاره، کاغذ، جامې، واښه) شامل دي. ډېره اړینه ده چې د کار په ځای کې د ټولو داسې توکو جزییات شتون ولري چې لمبه ورکوي او د اور لامل کېږي.')])
    L(b, [('The employees of the institution should be aware of their duty, of what danger they have to face.', 'ادارے کے ملازم اپنی ڈیوٹی سے آگاہ ہوں کہ انھوں نے کیسے خطرے سے نبرد آزما ہونا ہے۔', 'د ادارې کارکوونکي دې له خپلې دندې خبر وي چې له کوم خطر سره باید مقابله وکړي.'),
          ('Different things are products of different companies. The instructions of these companies are on the label. Act on these instructions during use.', 'مختلف اشیاء مختلف کمپنیوں کی پیداوار ہوتی ہیں۔ ان کمپنیوں کی ہدایات لیبل پر لگی ہوتی ہیں۔ استعمال کے دوران ان ہدایات پر عمل کریں۔', 'بېلابېل توکي د بېلابېلو شرکتونو محصولات وي. د دې شرکتونو لارښوونې پر لیبل وي. د کارولو پر مهال پر دې لارښوونو عمل وکړئ.'),
          ('Act strictly on the instructions posted at the filling station.', 'فلنگ اسٹیشن پر لگی ہدایات پر سختی سے عمل کریں۔', 'د تېلو په تمځای کې لګېدلو لارښوونو ته په کلکه عمل وکړئ.'),
          ('The passages of the building and the surrounding passages should be kept free. There should be no unnecessary parking in these passages, so that people can pass easily.', 'عمارت کے راستوں اور ارد گرد راستوں کو آزاد رکھا جائے۔ ان راستوں میں غیر ضروری پارکنگ نہ ہو۔ افراد آسانی سے گزر سکیں۔', 'د ودانۍ لارې او شاوخوا لارې دې خلاصې وساتل شي. په دې لارو کې دې غیر اړین پارکینګ نه وي ترڅو خلک په اسانۍ تېر شي.'),
          ('Where gas appliances are installed, they should be installed in the appropriate way and repaired.', 'گیس کے آلات نصب ہوں انھیں مناسب طریقے سے نصب اور مرمت کی جائے۔', 'چېرته چې ګازي وسایل لګېدلي وي، په مناسب ډول دې ولګول او ترمیم شي.'),
          ('Flame-giving appliances and material should not be kept at the workplace or in the building.', 'کام کی جگہ یا عمارت میں شعلہ دینے والے آلات و میٹریل نہ رکھے جائیں۔', 'د کار په ځای یا ودانۍ کې دې لمبه ورکوونکي وسایل او مواد کېښودل نه شي.'),
          ('If such material is necessary for work, then it should be stored in a separate building. Fire-resisting appliances should be installed there. This place should be kept under strict supervision.', 'اگر ایسے میٹریل کام کیلئے ضروری ہو تو پھر اس کو علیحدہ عمارت میں سٹور کیا جائے۔ وہاں آگ سے مزاحمت کے آلات لگے ہوں۔ اس جگہ کو کڑی نگرانی میں رکھا جائے۔', 'که داسې مواد د کار لپاره اړین وي، په جلا ودانۍ کې دې زېرمه شي. هلته دې د اور ضد وسایل لګېدلي وي. دا ځای دې تر سختې څارنې لاندې وساتل شي.')])
    b.h('Flame-giving liquid material:', 'شعلہ دینے والا مائع مواد:', 'لمبه ورکوونکي مایع مواد:')
    P(b, [('Flame-giving liquid material becomes the cause of severe danger of fire. Its vapours are heavier than air and they travel to long distances, which become the cause of smouldering.',
           'شعلہ دینے والا مائع مواد آگ کے لیے شدید خطرے کا سبب بنتا ہے۔ اس کے بخارات ہوا سے بھاری ہوتے ہیں اور لمبے فاصلے تک جاتے ہیں جو کہ سلگنے کا سبب بنتے ہیں۔',
           'لمبه ورکوونکي مایع مواد د اور د سخت خطر لامل کېږي. بخارات یې له هوا دروند وي او لرې واټنونو ته ځي چې د لوګي کېدو لامل کېږي.')])
    r = rec(b, 4, 12, 44)
    BOOK.save(44, [(4, r)], issues=[{'id': 'hpe12-pdf044', 'unit': 4, 'printedPage': 39,
               'description': '“جو شعلہ دے سکتی ہیں (سی این جی، ایل پی جی)” is placed after the list of liquid fuels in print; “اگر ایسے میٹریل … ضروری ہو”. Retained as printed.'}])


def p45():
    b = Builder()
    L(b, [('Liquid fuel should not be kept in workrooms for a long duration.', 'مائع ایندھن کام کے کمروں میں زیادہ دورانیہ کیلئے نہ رکھے جائیں۔', 'مایع سونګ دې د کار په کوټو کې د اوږدې مودې لپاره ونه ساتل شي.'),
          ('Store liquid fuel, empty buckets and half-used ones in a safe place.', 'مائع ایندھن، خالی بالٹی اور آدھے استعمال کے بعد محفوظ جگہ سٹور کریں۔', 'مایع سونګ، تشې سطلې او نیمې کارول شوې په خوندي ځای کې زېرمه کړئ.'),
          ('Liquid fuel should not leak from the container.', 'مائع ایندھن برتن میں سے لیک نہ ہو۔', 'مایع سونګ دې له لوښي ونه څڅېږي.'),
          ('Some chemicals are very dangerous. Great care should be taken in using and storing them.', 'کچھ کیمیکل بہت خطرناک ہوتے ہیں۔ ان کو استعمال کرنے اور سٹور کرنے میں بہت احتیاط کی جائے۔', 'ځینې کیمیاوي توکي ډېر خطرناک وي. د کارولو او زېرمه کولو پر مهال یې ډېر احتیاط دې وشي.')])
    b.h('Fire-safety poster (as printed in English)', 'آگ سے حفاظت کا پوسٹر (انگریزی میں مطبوعہ)', 'د اور څخه د خوندیتوب پوسټر (په انګرېزۍ چاپ)')
    rows = [('In case of fire…: 1. —; 2. Gather everyone; 3. Walk through the nearest exit; 4. Close any doors behind you to slow down the spread of fire; 5. —',),
            ('Every home should have an escape plan.',),
            ('Fire extinguisher: 1. Pull pin; 2. Hold; 3. Squeeze; 4. Sweep.',),
            ('PASS — Pull the pin; Aim at the base of fire; Squeeze lever and handle; Sweep from side to side.',),
            ('Do you know: the time you have to escape from fire; the number of deaths of children in fire incidents per year worldwide; the percentage of risk reduced by working smoke alarms; smoke inhaling kills more people than fire does.',),
            ('Common causes of home fire: unattended stove; candles/burners; LPG leakage; electrical malfunction.',)]
    b.group('lines', [(r[0], r[0], r[0]) for r in rows])
    for p in b.paras[-len(rows):]:
        p['untranslatedByDesign'] = True
    b.h('Oxygen', 'آکسیجن', 'اکسیجن')
    P(b, [('Oxygen is very necessary for the life of living things. In air there is 21% oxygen. Besides the life of living beings, oxygen is brought into industrial use. In industrial use oxygen is used in welding, flame cutting, breathing, medical, keeping food safe and packing, work of steel and chemical plants.',
           'آکسیجن جاندار اشیاء کی زندگی کیلئے بہت ہی ضروری ہے۔ ہوا میں 21% آکسیجن ہوتی ہے۔ آکسیجن جانداروں کی زندگی کے علاوہ صنعتی استعمال میں لائی جاتی ہے۔ صنعتی استعمال میں آکسیجن ویلڈنگ، شعلہ کٹنگ، سانس لینے میں، میڈیکل، خوراک کو محفوظ رکھنے اور پیکنگ، سٹیل کے کام اور کیمیکل پلانٹس میں استعمال ہوتی ہے۔',
           'اکسیجن د ژوندیو شیانو د ژوند لپاره ډېر اړین دی. په هوا کې ۲۱٪ اکسیجن وي. اکسیجن د ژوندیو له ژوند سربېره په صنعتي کار کې هم کارول کېږي. په صنعتي کار کې اکسیجن په ویلډنګ، لمبه پرې کولو، ساه اخیستو، طب، د خوړو خوندي ساتلو او بسته‌بندۍ، د فولادو کار او کیمیاوي فابریکو کې کارول کېږي.')])
    r = rec(b, 4, 13, 45)
    r['sourceNote'] = 'The full-width colour infographic (“DO YOU KNOW … IN CASE OF FIRE … COMMON CAUSES OF HOME FIRE … PASS”) is a printed English poster; its legible captions are given as text lines. The small statistic figures and steps 1 and 5 of the escape sequence are not legible in the scan.'
    BOOK.save(45, [(4, r)], issues=[{'id': 'hpe12-pdf045', 'unit': 4, 'printedPage': 40,
               'description': 'The fire-safety poster is printed in English only; its captions are retained in English in all three languages. The small figures (time to escape, number of deaths, percentage) are illegible in the scan and omitted. The first word of the oxygen paragraph line 2 is cut at the edge (“کی”). Retained as printed.'}])


def p46():
    b = Builder()
    P(b, [('The following use of oxygen can become the cause of explosion and fire.', 'آکسیجن کا درج ذیل استعمال دھماکے اور آگ کا باعث بن سکتا ہے۔', 'د اکسیجن لاندې کارونه د چاودنې او اور لامل کېدای شي.')])
    L(b, [('Leaking from appliances during the enrichment of oxygen.', 'آکسیجن کی افزودگی کے دوران آلات سے لیک ہونا۔', 'د اکسیجن د بډاینې پر مهال له وسایلو لیکېدل.'),
          ('Use of such material as is not suitable with oxygen.', 'ایسے میٹریل کا استعمال جو آکسیجن کے ساتھ موزوں نہ ہو۔', 'د داسې موادو کارول چې له اکسیجن سره مناسب نه وي.'),
          ('Using oxygen in such appliances as have not been designed for oxygen.', 'ایسے آلات میں آکسیجن کا استعمال کرنا جو آکسیجن کیلئے ڈیزائن نہ کئے گئے ہوں۔', 'په داسې وسایلو کې د اکسیجن کارول چې د اکسیجن لپاره نه وي ډیزاین شوي.'),
          ('Improper use of oxygen appliances.', 'آکسیجن کے آلات کا غیر مناسب استعمال۔', 'د اکسیجن د وسایلو نامناسب کارول.')])
    b.h('Precaution', 'احتیاط', 'احتیاط')
    L(b, [('During the enrichment of oxygen, appliances or cylinders etc. should not leak.', 'آکسیجن کی افزودگی کے دوران آلات یا سلنڈر وغیرہ لیک نہ ہو۔', 'د اکسیجن د بډاینې پر مهال وسایل یا سلنډرونه او نور دې ونه لیکېږي.'),
          ('Such appliances should be used as are suitable with oxygen.', 'ایسے آلات استعمال کیے جائیں جو آکسیجن کے ساتھ موزوں ہوں۔', 'داسې وسایل دې وکارول شي چې له اکسیجن سره مناسب وي.'),
          ('Only such appliances should be used as have been designed only for oxygen.', 'ایسے آلات ہی استعمال کئے جائیں جو صرف آکسیجن کیلئے ڈیزائن کئے گئے ہوں۔', 'یوازې داسې وسایل دې وکارول شي چې یوازې د اکسیجن لپاره ډیزاین شوي وي.'),
          ('The valve of the cylinder should always be opened slowly.', 'سلنڈر کے والو کو ہمیشہ آہستہ آہستہ کھولا جائے۔', 'د سلنډر والو دې تل ورو ورو خلاص شي.'),
          ('Where oxygen is being used, there should be no cigarette smoking there.', 'جہاں آکسیجن استعمال کی جا رہی ہو وہاں سگریٹ نوشی نہ کی جائے۔', 'چېرته چې اکسیجن کارول کېږي، هلته دې سګرټ ونه څکول شي.'),
          ('Always the cylinders and appliances of oxygen itself should be used with care and in the correct way.', 'ہمیشہ آکسیجن کے ہی سلنڈر اور آلات احتیاط اور درست طریقے سے استعمال کئے جائیں۔', 'تل دې د اکسیجن خپل سلنډرونه او وسایل په احتیاط او سمه طریقه وکارول شي.')])
    b.h('First aid', 'فرسٹ ایڈ (ابتدائی طبی امداد)', 'لومړنۍ مرسته (فرسټ اېډ)')
    P(b, [('In case of any accident, fire or injury, the precautionary measures and help that are given in the process of keeping the life of the injured intact before taking them to a hospital or doctor are called first aid (First Aid). The one giving medical aid is acquainted with the following responsibilities.',
           'کسی بھی حادثہ۔ آگ یا چوٹ کی صورت میں زخمیوں کو ہسپتال یا ڈاکٹر کے پاس پہنچانے سے پہلے اس کی زندگی کو برقرار رکھنے کے عمل میں جو احتیاطی تدابیر اور امداد دی جاتی ہے اسے ابتدائی طبی امداد (First Aid) کہا جاتا ہے۔ طبی امداد دینے والا درج ذیل ذمہ داریوں سے واقفیت رکھتا ہو۔',
           'د هرې پېښې، اور یا ټپ په صورت کې ټپيانو ته روغتون یا ډاکټر ته له رسولو مخکې د ژوند د ساتلو په بهیر کې چې کوم احتیاطي ګامونه او مرسته ورکول کېږي، لومړنۍ طبي مرسته (First Aid) ورته ویل کېږي. طبي مرسته ورکوونکی دې له لاندې مسؤلیتونو خبر وي.')])
    L(b, [('Assess the situation by himself.', 'حالات کا از خود جائزہ لے۔', 'حالات پخپله وارزوي.'),
          ('Estimating the injured correctly.', 'زخمیوں کا درست اندازہ لگانا۔', 'د ټپيانو سم اټکل کول.'),
          ('Taking to a doctor or hospital without delay according to the injury.', 'چوٹ کی مناسبت سے بلا تاخیر ڈاکٹر یا ہسپتال تک لے جانا۔', 'د ټپ سره سم بې‌ځنډه ډاکټر یا روغتون ته وړل.')])
    r = rec(b, 4, 14, 46)
    BOOK.save(46, [(4, r)], issues=[{'id': 'hpe12-pdf046', 'unit': 4, 'printedPage': 41,
               'description': '“کسی بھی حادثہ۔ آگ یا چوٹ”, “اس کی زندگی” (for the injured, plural). The right-edge line ends (“زندگی”, “کہا جاتا ہے”) are cut in the scan and completed from context. Retained as printed.'}])


def p47():
    b = Builder()
    P(b, [('If many people are victims of an accident at the same time, then estimating which patient needs more immediate first aid. In this way, through first aid the pain of the patient is reduced. He is quickly saved from danger. The patient gets calm. The courage of the patient increases and through this the patient gets support.',
           'زیادہ لوگ بیک وقت حادثہ کا شکار ہوں تو یہ اندازہ لگانا کہ کس مریض کو زیادہ جلدی طبی امداد کی ضرورت ہے۔ اس طرح طبی امداد سے مریض کا درد کم ہو جاتا ہے۔ خطرے سے جلد بچ جاتا ہے۔ مریض کو سکون ملتا ہے۔ مریض کا حوصلہ بڑھ جاتا ہے اور اس سے مریض کو سہارا مل جاتا ہے۔',
           'که ډېر خلک په یوه وخت د پېښې ښکار شي، دا اټکل کول چې کوم ناروغ ته ډېره ژر طبي مرسته پکار ده. په دې ډول په طبي مرسته د ناروغ درد کمېږي. ژر له خطر ژغورل کېږي. ناروغ ارام مومي. د ناروغ زړه‌ورتیا زیاتېږي او ملاتړ ترلاسه کوي.'),
          ('In case of burning by fire the following works should be done as first aid.', 'آگ سے جلنے کی صورت میں درج ذیل کام بطور ابتدائی طبی امداد کرنے چاہیے۔', 'د اور د سوځېدو په صورت کې لاندې کارونه دې د لومړنۍ مرستې په توګه وشي.')])
    L(b, [('If clothes catch fire, then immediately a blanket should be put on them. Start rolling on the ground.', 'اگر کپڑوں کو آگ لگ جائے تو فوراً اس پر کمبل ڈال دیا جائے۔ زمین پر لوٹنا شروع کر دیں۔', 'که جامې اور واخلي، سمدستي دې پرې کمبله واچول شي. پر ځمکه ړغړېدل پیل کړئ.'),
          ('The way of air should be closed so that the fire does not flare up further.', 'ہوا کا راستہ بند کیا جائے تاکہ مزید آگ نہ بھڑک سکے۔', 'د هوا لاره دې بنده شي ترڅو اور لا بل نه شي.'),
          ('When the fire is extinguished, cut the clothes and separate them.', 'آگ بجھ جائے تو کپڑے کاٹ کر الگ کر دیں۔', 'کله چې اور مړ شي، جامې پرې کړئ او جلا یې کړئ.'),
          ('Immediately apply Burnol or some suitable ointment on the wounds.', 'زخموں پر فوراً برنال یا کوئی موزوں مرہم لگائیں۔', 'پر ټپونو سمدستي برنال یا کومه مناسبه ملهم ولګوئ.'),
          ('If the body has been scorched, do not let anything touch it.', 'اگر جسم جھلس گیا ہو تو اس کے ساتھ کسی چیز کو نہ لگنے دیں۔', 'که بدن سوځېدلی وي، هېڅ شی ورسره مه لګوئ.'),
          ('Immediately make the patient drink warm milk, coffee or water.', 'مریض کو فوراً گرم دودھ، کافی یا پانی پلائیں۔', 'ناروغ ته سمدستي ګرمې شیدې، کافي یا اوبه ورکړئ.'),
          ('Raise the courage of the patient.', 'مریض کا حوصلہ کا بلند کریں۔', 'د ناروغ زړه‌ورتیا لوړه کړئ.'),
          ('Immediately transfer him to a hospital or burn centre (Burn Centre).', 'فوری طور پر اسے ہسپتال یا برن سنٹر (Burn Centre) منتقل کریں۔', 'سمدستي یې روغتون یا د سوځېدنې مرکز (Burn Centre) ته ولېږدوئ.')])
    r = rec(b, 4, 15, 47)
    BOOK.save(47, [(4, r)], issues=[{'id': 'hpe12-pdf047', 'unit': 4, 'printedPage': 42,
               'description': 'The lower half and left margin of p.42 are covered with owner ballpoint handwriting (repeated signatures “M.Kamran”, English sentences, a diagonal line); all excluded. “مریض کا حوصلہ کا بلند کریں”, “درج ذیل کام … کرنے چاہیے”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    {42: p42, 43: p43, 44: p44, 45: p45, 46: p46, 47: p47}[n]()
