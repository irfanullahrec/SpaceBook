"""HPE XII PDF12–17: pp.7–12 — heart diseases (symptoms, diagnosis, treatment, precautions, diet restrictions and diet plan table); chapter 1 exercise;
chapter 2 opener (circulatory system, heart, walls and chambers). Run: python class12_hpe_page012.py N (12–17)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, fig_heart, fig_circulation


def p12():
    b = Builder()
    b.h('Symptoms', 'علامات', 'نښې')
    P(b, [('Just as the causes of heart diseases are of different kinds, in the same way the symptoms of heart diseases of different kinds also appear in several ways, and only an expert physician can decide whether the symptoms confirm some disorder of the heart, or the patient has some problem related to the stomach, gall bladder, chest or nerves whose symptoms resemble heart trouble. The important symptoms are the following, which can be stated in identifying heart diseases.',
           'جس طرح دل کے امراض کے اسباب مختلف نوعیت کے ہیں اسی طرح مختلف نوعیت کے دل کے امراض میں علامات بھی کئی طرح سے ظاہر ہوتی ہیں اور اس بات کا فیصلہ ایک ماہر معالج کر سکتا ہے کہ علامات دل کے کسی عارضہ کی تصدیق کرتی ہیں یا مریض کو معدہ، پتہ، سینہ یا اعصاب سے متعلق کوئی مسئلہ ہے جس کی علامات دل کی تکلیف سے مشابہت رکھتی ہیں۔ اہم علامات درجہ ذیل ہیں جو کہ دل کے امراض کی نشاندہی میں بیان کی جا سکتی ہیں۔',
           'لکه څنګه چې د زړه د ناروغیو لاملونه بېلابېل ډولونه لري، همداسې د زړه په بېلابېلو ناروغیو کې نښې هم په څو ډوله ښکاره کېږي او دا پرېکړه یو ماهر ډاکټر کولی شي چې نښې د زړه د کومې ناروغۍ تصدیق کوي یا ناروغ ته د معدې، تریخي، سینې یا عصبونو اړوند کومه ستونزه ده چې نښې یې د زړه له تکلیف سره ورته والی لري. مهمې نښې دا دي چې د زړه د ناروغیو په پېژندنه کې بیانېدای شي.')])
    L(b, [('Feeling severe pain and suffocation on the left side of the chest.', 'سینے کے بائیں طرف شدید درد اور گھٹن کا احساس ہونا۔', 'د سینې په کیڼ اړخ کې د سخت درد او ساه بندېدو احساس.'),
          ('Shortness of breath and irregularity of the heartbeat.', 'سانس کا پھولنا اور دل کی دھڑکن کا بے ترتیب ہونا۔', 'د ساه لنډېدل او د زړه د درزا بې‌ترتیبي.'),
          ('A wave of pain arising in the left arm.', 'بائیں بازو میں درد کی لہر کا پیدا ہونا۔', 'په کیڼ لاس کې د درد څپه پیدا کېدل.')])
    b.h('Diagnosis', 'تشخیص', 'تشخیص')
    L(b, [('Through the E.C.G. (Electrocardiogram) an expert doctor can examine the condition of the heart.', 'ای۔ سی۔ جی (Electrocardiogram) کے ذریعے ماہر ڈاکٹر دل کی کیفیت کو جانچ سکتا ہے۔', 'د ای سي جي (Electrocardiogram) له لارې ماهر ډاکټر د زړه حالت ارزولی شي.'),
          ('Through the stethoscope (Stethoscope), directly listening to the heartbeat and the sound of breathing in the chest and checking the condition of the heart.', 'سٹیتھو سکوپ (Stethoscope) کے ذریعے براہِ راست دل کی دھڑکن اور سینے میں سانس کی آواز کو سن کر دل کی کیفیت کو جانچ لینا۔', 'د سټیتوسکوپ (Stethoscope) له لارې په مستقیم ډول د زړه درزا او په سینه کې د ساه غږ اورېدل او د زړه حالت ارزول.')])
    b.h('Treatment', 'علاج', 'درملنه')
    P(b, [('Only an expert physician of this field can propose treatment of heart diseases after seeing the individual condition of the patient, symptoms, results of blood tests, E.C.G. and other supporting results. Since the high level of cholesterol in the blood, narrowing and stiffening of the arteries and thickening of the blood are different symptoms, their medicines too are prescribed separately for every patient accordingly.',
           'دل کے امراض کا علاج بھی اس شعبے کا ماہر معالج مریض کی انفرادی کیفیت، علامات، خون کے معائنے کے نتائج، ای سی جی اور دیگر معاون نتائج کو دیکھ کر ہی تجویز کر سکتا ہے۔ کیونکہ خون میں کولیسٹرول کی بلند سطح، رگوں کی تنگی، اکڑن اور خون کا گاڑھا ہونا، جتنا مختلف علامات ہیں اسی لحاظ سے انکی ادویات بھی ہر مریض کے لیے جدا جدا تجویز کی جاتی ہیں۔',
           'د زړه د ناروغیو درملنه هم یوازې د دې برخې ماهر ډاکټر د ناروغ د انفرادي حالت، نښو، د وینې د معاینې پایلو، ای سي جي او نورو مرستندویو پایلو ته په کتو وړاندیز کولی شي. ځکه په وینه کې د کولسټرول لوړه کچه، د رګونو تنګوالی، کلکېدل او د وینې ټینګېدل بېلابېلې نښې دي، له همدې امله یې درمل هم د هر ناروغ لپاره جلا جلا وړاندیز کېږي.')])
    r = rec(b, 1, 7, 12)
    deco(r, 'A photograph of a man clutching his chest (heart pain shown in red) is decorative.')
    BOOK.save(12, [(1, r)], issues=[{'id': 'hpe12-pdf012', 'unit': 1, 'printedPage': 7,
               'description': 'Owner ballpoint scribble below the photograph is excluded. “درجہ ذیل”, “جتنا مختلف علامات ہیں”. Retained as printed.'}])


def p13():
    b = Builder()
    b.h('Precautionary measures', 'احتیاطی تدابیر', 'احتیاطي ګامونه')
    P(b, [('Besides walking, exercise according to the physician’s advice and avoiding the components of salt, ghee and fat in food, the following precautionary measures too are helpful in this regard.',
           'معالج کی تجویز کے مطابق چہل قدمی، ورزش اور کھانے میں نمک، گھی اور چربی کے اجزاء سے پرہیز کے علاوہ درج ذیل احتیاطی تدابیر بھی اس سلسلے میں معاون ہیں۔',
           'د ډاکټر د وړاندیز سره سم له ګرځېدو، تمرین او په خواړو کې له مالګې، غوړیو او وازدې څخه له پرهېز سربېره لاندې احتیاطي ګامونه هم په دې برخه کې مرسته کوي.')])
    L(b, [('A simple way of life should be adopted and as far as possible a peaceful life should be spent.', 'سادہ طرزِ زندگی اختیار کیا جائے اور حتی الامکان پُر سکون زندگی گزاری جائے۔', 'ساده ژوند غوره شي او تر وسه ارام ژوند تېر شي.'),
          ('Reasonable timings of eating, drinking, sleeping and waking should be observed.', 'کھانے پینے اور سونے جاگنے کے معقول اوقات کا لحاظ رکھا جائے۔', 'د خوړلو څښلو او ویده کېدو او ویښېدو معقولو وختونو ته پام وشي.'),
          ('Smoking and other intoxicating things should be avoided.', 'تمباکو نوشی اور دیگر نشہ آور چیزوں کے استعمال سے گریز کیا جائے۔', 'له تمباکو څکولو او نورو نشه‌يي توکو ډډه وشي.'),
          ('Contentment should be adopted in social matters and oneself should be kept free from too much mental pressure.', 'معاشرتی معاملات میں قناعت اختیار کی جائے اور خود کو بہت زیادہ ذہنی دباؤ سے آزاد رکھا جائے۔', 'په ټولنیزو چارو کې قناعت غوره شي او ځان له ډېر رواني فشار ازاد وساتل شي.'),
          ('All prescribed medicines should be used on time and no gap should be made in taking medicines.', 'تمام تجویز کردہ دواؤں کو بروقت استعمال کیا جائے اور دوا لینے میں ناغہ نہیں کرنا چاہیے۔', 'ټول وړاندیز شوي درمل په وخت وکارول شي او د درملو په اخیستو کې ناغه ونه شي.'),
          ('If someone suffers from blood pressure (high blood pressure) and diabetes, then the risk of heart diseases increases; in both these conditions great attention should be paid to abstinence.', 'اگر کوئی بلڈ پریشر (بلند فشار خون) اور ذیابیطس کا مرض لاحق ہو جائے تو دل کے امراض کا خدشہ بڑھ جاتا ہے ان دونوں حالتوں میں پرہیز کی طرف بہت توجہ دینی چاہیے۔', 'که چا ته د وینې فشار (لوړ فشار) او شکر ناروغي پېښه شي، د زړه د ناروغیو خطر زیاتېږي؛ په دې دواړو حالتونو کې پرهېز ته ډېر پام پکار دی.')])
    b.h('Dietary restrictions for the heart patient', 'دل کے مریض کے لیے غذائی پابندیاں', 'د زړه ناروغ لپاره غذايي محدودیتونه')
    P(b, [('Food is a basic need of the body. Besides air and water, every living thing needs food in order to remain alive. Whether food is obtained from plant sources or animal sources, there are some food characteristics in it which in other words are called nutrition (Nutrition). Nutrition depends on the food components present in food. Every food component performs a special work in the body, and without any component growth and health are not possible. Every part of the body needs strength and special food components according to its work. The most work in our body is done by our heart. Because the heart moves continuously, the heart works like a pump in the human body; it supplies blood to all parts of the body. Food plays a very important role in bringing the continuous work of the heart into practice in an effective way; however, in heart diseases special care is taken of food. The heart patient should use the food prescribed by the doctor. Fatty foods and such foods in which there is more cholesterol etc. should not be used at all. Below …',
           'غذا جسم کی بنیادی ضرورت ہے۔ ہر جاندار کو زندہ رہنے کے لیے ہوا اور پانی کے علاوہ غذا کی بھی ضرورت ہوتی ہے۔ غذا خواہ نباتاتی ذرائع سے حاصل ہو یا حیواناتی ذرائع سے، اس کے اندر چند ایسی غذائی خصوصیات ہوتی ہے جن کو دوسرے لفظوں میں غذائیت (Nutrition) کہتے ہیں۔ غذائیت کا دارومدار غذا میں موجود غذائی اجزا پر ہوتا ہے۔ ہر غذائی جزو جسم میں ایک خاص کام سرانجام دیتا ہے اور کسی بھی جزو کے بغیر نشوونما اور صحت ممکن نہیں۔ جسم کے ہر حصے کو اس کے کام کے مطابق طاقت اور مخصوص غذائی اجزا چاہیے ہوتے ہیں۔ ہمارے جسم میں سب سے زیادہ کام ہمارے دل کو کرنا ہوتا ہے۔ کیونکہ دل مسلسل حرکت کرتا ہے دل انسانی جسم میں ایک پمپ کی طرح کام کرتا ہے یہ جسم کے سارے حصوں کو خون فراہم کرتا ہے دل کے مسلسل کام کو موثر طریقے سے عمل میں لانے کے لیے غذا بہت اہم کردار ادا کرتی ہے تاہم دل کے امراض میں غذا کا خصوصی خیال رکھا جاتا ہے۔ دل کے مریض کو ڈاکٹر کی تجویز کردہ غذا استعمال کرنی چاہیے۔ مرغن غذائیں اور ایسی غذائیں جن میں کولیسٹرول وغیرہ زیادہ ہو، بالکل استعمال نہیں کرنی چاہیے۔ ذیل میں …',
           'خواړه د بدن بنسټیزه اړتیا ده. هر ژوندي ته د ژوندي پاتې کېدو لپاره له هوا او اوبو سربېره خوړو ته هم اړتیا وي. خواړه که له نباتي سرچینو ترلاسه شي یا له حیواني سرچینو، په کې ځینې غذايي ځانګړنې وي چې په بل عبارت تغذیه (Nutrition) ورته ویل کېږي. تغذیه په خوړو کې پر شته غذايي اجزاوو ولاړه وي. هره غذايي برخه په بدن کې یو ځانګړی کار ترسره کوي او له کومې برخې پرته وده او روغتیا شونې نه ده. د بدن هرې برخې ته د هغې د کار سره سم ځواک او ځانګړو غذايي اجزاوو ته اړتیا وي. زموږ په بدن کې تر ټولو ډېر کار زموږ زړه کوي. ځکه زړه په دوامداره ډول خوځېږي؛ زړه د انسان په بدن کې د پمپ په څېر کار کوي او د بدن ټولو برخو ته وینه رسوي. د زړه د دوامداره کار د اغېزمن ترسره کولو لپاره خواړه ډېر مهم رول لوبوي، خو د زړه په ناروغیو کې خوړو ته ځانګړې پاملرنه کېږي. د زړه ناروغ باید د ډاکټر وړاندیز شوي خواړه وکاروي. غوړ خواړه او هغه خواړه چې کولسټرول پکې ډېر وي، هېڅ باید ونه کارول شي. لاندې …')])
    r = rec(b, 1, 8, 13)
    BOOK.save(13, [(1, r)], issues=[{'id': 'hpe12-pdf013', 'unit': 1, 'printedPage': 8,
               'description': 'Owner Urdu ballpoint notes in the left margin and pen marks along the right margin are excluded. “غذائی خصوصیات ہوتی ہے”, “غذائی اجزا چاہیے ہوتے ہیں”. Retained as printed.'}])


DIET = [
 (('Meat: 6 ounces daily', 'گوشت روزانہ 6 اونس', 'غوښه: ورځنی ۶ اونسه'),
  ('Meat without fat, after removing the skin (chicken or goat), which is not fried', 'بغیر چربی والا گوشت کھال اتارنے کے بعد (مرغی یا بکرا) جو تلا ہوا نہ ہو', 'بې‌وازدې غوښه له پوټکي لرې کولو وروسته (چرګ یا وزه) چې وریته نه وي'),
  ('Fish, chicken roasted or in curry (low fat)', 'مچھلی، مرغی بھنی ہوئی یا سالن میں (کم مرغن)', 'کب، وریت چرګ یا په ښوروا کې (کم غوړ)'),
  ('Egg yolk, fatty meat, beef, head and trotters, brain, kidneys, liver etc.', 'انڈے کی زردی، چربی والا گوشت، بڑا گوشت، سری پائے، مغز، گردے، کلیجی وغیرہ', 'د هګۍ ژېړ، غوړه غوښه، د غوا غوښه، سر او پښې، مغز، پښتورګي، ځیګر او نور')),
 (('Milk', 'دودھ', 'شیدې'), ('Milk without cream and fat', 'بغیر بالائی اور چکنائی کے دودھ', 'بې‌سرشیر او بې‌غوړه شیدې'),
  ('☆ One glass of milk without cream; yoghurt made from it; buttermilk lassi', '☆ بغیر بالائی ایک گلاس دودھ اس کا بنا ہوا دہی، چاٹی کی لسی', '☆ یو ګیلاس بې‌سرشیره شیدې، له هغو جوړ مستې، د شلومبې لسي'),
  ('Milk with cream, cream, yoghurt, cheese etc.', 'بالائی والا دودھ، کریم، دہی، پنیر وغیرہ', 'سرشیره شیدې، کریم، مستې، پنیر او نور')),
 (('Eggs', 'انڈے', 'هګۍ'), ('Egg white', 'انڈے کی سفیدی', 'د هګۍ سپین'),
  ('☆ Egg white daily; once or twice a week an egg with the yolk', '☆ انڈوں کی سفیدی روزانہ ہفتے میں ایک یا دو مرتبہ انڈہ زردی سمیت', '☆ ورځنی د هګیو سپین؛ په اونۍ کې یو یا دوه ځله هګۍ له ژېړ سره'),
  ('Paratha, fatty foods', 'پراٹھا، مرغن غذائیں', 'پراټه، غوړ خواړه')),
 (('Oil: three teaspoons in a day', 'تیل چائے کے تین چمچے ایک دن میں', 'تېل: په یوه ورځ کې درې د چای کاشوغې'),
  ('Maize, olive, canola, sunflower, sesame, soya bean; bread, rice, biscuits without cream, home-made cake rusk', 'مکئی، زیتون، کینولا، سورج مکھی، تل، سویابین، ڈبل روٹی، چاول، بغیر کریم کے بسکٹ، گھر کے بنے کیک رس', 'جوار، زیتون، کینولا، لمرګل، کونجي، سویابین؛ ډبل روټي، وریجې، بې‌کریمه بسکټ، په کور کې جوړ کېک رس'),
  ('☆ Olive / groundnut oil ☆ Walnut, almond, dried fig ☆ Rusk, brown bread', '☆ زیتون/مونگ پھلی کا تیل ☆ اخروٹ، بادام، خشک انجیر ☆ رس، براؤن بریڈ', '☆ د زیتون / مومپلي تېل ☆ غوز، بادام، وچ انځر ☆ رس، نسواري ډوډۍ'),
  ('Coconut, palm oil, butter, desi ghee, ghee of any kind; bakery items, doughnuts, cream items; cheese, rice (biryani)', 'ناریل، پام کا تیل، مکھن، دیسی گھی کسی بھی قسم کا گھی، بیکری کی اشیاء، ڈونٹ کریم کی اشیاء، پنیر، چاول (بریانی)', 'ناریل، د پام تېل، کوچ، کورني غوړي، هر ډول غوړي؛ د بیکرۍ توکي، ډونټ، کریمي توکي؛ پنیر، وریجې (بریاني)')),
 (('Bread etc.', 'روٹی وغیرہ', 'ډوډۍ او نور'), ('Noodles, dried peas, beans, simple steamed potatoes', 'نوڈلز، خشک مٹر، پھلیاں، سادے دم ہوئے آلو', 'نوډلز، وچ مټر، لوبیا، ساده دم کړي کچالو'),
  ('☆ Home-made bread ☆ Food cooked in cooking oil.', '☆ گھر کی روٹی ☆ کھانے جو کوکنگ آئل میں پکے ہوں۔', '☆ کورنۍ ډوډۍ ☆ په پخلي تېلو کې پاخه خواړه.'),
  ('Fatty and salty foods', 'مرغن اور نمکین کھانے', 'غوړ او مالګین خواړه')),
 (('Fruits and vegetables', 'پھل اور سبزیاں', 'مېوې او سبزۍ'), ('Fresh fruit, dried fruit closed in tins, canned fruit with little syrup', 'تازہ پھل، ڈبوں میں بند خشک پھل، کم شیرے والے بند پھل', 'تازه مېوې، په ډبو کې بندې وچې مېوې، کم شربته بندې مېوې'),
  ('☆ Fresh fruit, fresh vegetables, salad ☆ Sugar patients can eat less sweet fruits. ☆ Boiled vegetables, all pulses', '☆ تازہ پھل، تازہ سبزیاں، سلاد ☆ شوگر کے مریض کم میٹھے پھل کھا سکتے ہیں۔ ☆ اُبلی ہوئی سبزیاں، تمام دالیں', '☆ تازه مېوې، تازه سبزۍ، سلاد ☆ د شکرې ناروغان کم خوږې مېوې خوړلی شي. ☆ ایشول شوې سبزۍ، ټول دالونه'),
  ('Coconut, ice cream, chocolate, chips, pizza etc.', 'ناریل، آئس کریم، چاکلیٹ، چپس، پیزا وغیرہ', 'ناریل، ایس کریم، چاکلېټ، چپس، پیزا او نور')),
]


def p14():
    b = Builder()
    P(b, [('… a diet plan has been given for heart patients. By acting on it heart patients and other people too can spend a healthy life.',
           'دل کے مریضوں کے لیے غذائی پلان دیا گیا ہے۔ ان پر عمل کر کے دل کے مریض اور دیگر افراد بھی صحت مند زندگی گزار سکتے ہیں۔',
           '… د زړه ناروغانو لپاره غذايي پلان ورکړل شوی. پر هغه په عمل سره د زړه ناروغان او نور کسان هم روغ ژوند تېرولی شي.')])
    H = (['Items', 'Choose', 'These can be eaten easily', 'Avoid these completely'], ['اشیا', 'منتخب کریں', 'ان کو آسانی سے کھا سکتے ہیں', 'ان سے مکمل پرہیز کیجیے'],
         ['توکي', 'غوره کړئ', 'دا په اسانۍ خوړل کېدای شي', 'له دې بشپړ پرهېز وکړئ'])
    b.table('hpe12-ch1-diet-plan', H[0], [[c[0] for c in r] for r in DIET], H[1], H[2], [[c[1] for c in r] for r in DIET], [[c[2] for c in r] for r in DIET])
    b.p('Note:', 'نوٹ:', 'یادونه:')
    L(b, [('Blood pressure patients should reduce the use of salt.', 'بلڈ پریشر کے مریض نمک کا استعمال کم کریں۔', 'د وینې فشار ناروغان دې د مالګې کارول کم کړي.'),
          ('Heart patients should always take food less than their hunger and rest for half an hour after eating.', 'دل کے مریض کھانا ہمیشہ بھوک سے کم لیں اور کھانا کھانے کے بعد آدھا گھنٹہ آرام کریں۔', 'د زړه ناروغان دې تل له لوږې کم خواړه وخوري او له خوړلو وروسته نیم ساعت استراحت وکړي.')])
    r = rec(b, 1, 9, 14)
    BOOK.save(14, [(1, r)], issues=[{'id': 'hpe12-pdf014', 'unit': 1, 'printedPage': 9,
               'description': 'The table header row is printed white on dark green and partly faint; read as “اشیا / منتخب کریں / ان کو آسانی سے کھا سکتے ہیں / ان سے مکمل پرہیز کیجیے”. The star (☆) bullets are kept as printed.'}])


def p15():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The disease of cancer occurs through uncontrolled division of the ________ of the body.', 'کینسر کا مرض جسم کے ________ کی بے قابو تقسیم سے ہوتا ہے۔', 'د سرطان ناروغي د بدن د ________ له بې‌کنټروله وېش کېږي.'),
          [('muscles', 'عضلات', 'عضلو'), ('cells', 'خلیوں', 'حجرو'), ('bones', 'ہڈیوں', 'هډوکو'), ('blood', 'خون', 'وینې')]),
         (('Lung cancer was not common before ________ .', 'پھیپھڑوں کا کینسر ________ سے پہلے عام نہیں تھا۔', 'د سږو سرطان له ________ مخکې عام نه و.'),
          [('1910', '1910', '1910'), ('1920', '1920', '1920'), ('1930', '1930', '1930'), ('1940', '1940', '1940')]),
         (('The biggest cause of lung cancer is ________ .', 'پھیپھڑوں کی کینسر کی سب سے بڑی وجہ ________ ہے۔', 'د سږو د سرطان تر ټولو لوی لامل ________ دی.'),
          [('eating too much', 'زیادہ کھانا', 'ډېر خوړل'), ('smoking', 'تمباکو نوشی', 'تمباکو څکول'), ('not exercising', 'ورزش نہ کرنا', 'تمرین نه کول'), ('obesity', 'موٹاپا', 'چاغښت')]),
         (('By living in ________ for a long time lung cancer too develops.', 'لمبے عرصے کیلئے ________ میں رہنے سے بھی پھیپھڑوں کا کینسر ہو جاتا ہے۔', 'تر اوږدې مودې په ________ کې اوسېدو سره هم د سږو سرطان کېږي.'),
          [('cities', 'شہروں', 'ښارونو'), ('polluted air', 'آلودہ فضا', 'ککړه فضا'), ('polluted water', 'آلودہ پانی', 'ککړې اوبه'), ('mountainous areas', 'پہاڑی علاقوں', 'غرنیو سیمو')]),
         (('A never-ending ________ is a sign of cancer.', 'نہ ختم ہونے والی ________ کینسر کی علامت ہے۔', 'نه ختمېدونکی ________ د سرطان نښه ده.'),
          [('fever', 'بخار', 'تبه'), ('tiredness', 'تھکاوٹ', 'ستړیا'), ('cough', 'کھانسی', 'ټوخی'), ('blood', 'خون', 'وینه')]),
         (('Alcohol is the name of ________ .', 'الکوحل ________ کا نام ہے۔', 'الکول د ________ نوم دی.'),
          [('sherbet', 'شربت', 'شربت'), ('liquor', 'شراب', 'شراب'), ('juice', 'جوس', 'جوس'), ('medicine', 'دوائی', 'درمل')]),
         (('The use of illegal medicines to increase physical strength in sports competitions is called ________ .', 'کھیلوں کے مقابلوں میں جسمانی طاقت بڑھانے کے لیے غیر قانونی ادویات کا استعمال ________ کہلاتا ہے۔', 'د لوبو په سیالیو کې د بدني ځواک د زیاتولو لپاره د غیر قانوني درملو کارول ________ بلل کېږي.'),
          [('intoxicants', 'منشیات', 'نشه‌يي توکي'), ('stamina', 'سٹیمنا', 'سټامینا'), ('doping', 'ڈوپنگ', 'ډوپینګ'), ('physiotherapy', 'فزیوتھراپی', 'فزیوتراپي')])]
    for i, (q, o) in enumerate(Q, 1):
        e.mcq(f'{i})', q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. What is cancer?', 'i۔ کینسر کیا ہے؟', 'i. سرطان څه دی؟'),
                      ('ii. State the symptoms of lung cancer in detail.', 'ii۔ پھیپھڑوں کے کینسر کی علامات تفصیل سے بیان کریں۔', 'ii. د سږو د سرطان نښې په تفصیل بیان کړئ.'),
                      ('iii. State the causes and symptoms of heart diseases.', 'iii۔ دل کے امراض کی وجوہات و علامات بیان کریں۔', 'iii. د زړه د ناروغیو لاملونه او نښې بیان کړئ.'),
                      ('iv. State precautionary measures to avoid heart diseases.', 'iv۔ دل کے امراض سے بچنے کے لیے احتیاطی تدابیر بیان کریں۔', 'iv. د زړه له ناروغیو د ژغورنې لپاره احتیاطي ګامونه بیان کړئ.')])
    r = BOOK.record(e, 'hpe12-ch1-exercise', 'Chapter 1 exercise', 'باب ۱: مشقی سوالات', '۱ څپرکی: تمریني پوښتنې', 15, [10])
    BOOK.save(15, [(1, r)], complete_units=[1], issues=[{'id': 'hpe12-pdf015', 'unit': 1, 'printedPage': 10,
               'description': 'Owner ballpoint ticks on the MCQ options and scribbles above the heading are excluded. Q1(3) “پھیپھڑوں کی کینسر”; Q1(7) asks about doping, which is the topic of chapter 3. Retained as printed.'}])


def p16():
    b = Builder()
    b.h('Chapter 2: Circulatory System and Exercise', 'باب نمبر ۲: نظامِ دورانِ خون اور ورزش', '۲ څپرکی: د وینې د جریان سیستم او تمرین')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('state blood circulation and its kinds.', 'دورانِ خون اور اس کی قسمیں بیان کر سکیں۔', 'د وینې جریان او ډولونه یې بیان کړي.'),
          ('state the effects of exercise on the cardiovascular (Cardio vascular) system.', 'کارڈیو ویسکولر (Cardio vascular) نظام پر ورزش کے اثرات بیان کر سکیں۔', 'پر زړه او رګونو (Cardio vascular) سیستم د تمرین اغېزې بیان کړي.')])
    b.h('Circulatory system', 'نظامِ دورانِ خون (Circulatory system)', 'د وینې د جریان سیستم (Circulatory system)')
    b.p('The following organs take part in this system.', 'اس نظام میں مندرجہ ذیل اعضاء حصہ لیتے ہیں۔', 'په دې سیستم کې لاندې غړي برخه اخلي.')
    b.group('lines', [('1. Heart (Heart)', '1. دل (Heart)', '1. زړه (Heart)'), ('2. Blood vessels (Blood Vessels)', '2. خون کی نالیاں (Blood Vessels)', '2. د وینې رګونه (Blood Vessels)'), ('3. Blood (Blood)', '3. خون (Blood)', '3. وینه (Blood)')])
    lab = {'subclavian': 'Subclavian vein', 'arch': 'Arch of the Aorta', 'pv': 'Pulmonary vein', 'pa': 'Pulmonary Artery', 'ivc': 'Inferior vena cava', 'thoracic': 'Thoracic Aorta', 'abdominal': 'Abdominal Aorta'}
    sv = [fig_circulation(lab, c) for c in ('The circulatory system', 'نظامِ دورانِ خون', 'د وینې د جریان سیستم')]
    b.visual('hpe12-fig-circulatory-system', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Heart', 'دل (Heart)', 'زړه (Heart)')
    P(b, [('The heart is the fountain of life of the human body. The heart is situated in the chest cavity (Chest Cavity) between the second and seventh ribs, and on both its sides are the lungs. The heart leans more to the left side than to the right side.',
           'دل انسانی جسم کا سرچشمہ حیات ہے۔ دل سینے کے خلاء (Chest Cavity) میں دوسری اور ساتویں پسلی کے درمیان واقع ہوتا ہے اور اس کے دونوں طرف پھیپھڑے ہوتے ہیں۔ دل دائیں طرف کی نسبت بائیں طرف زیادہ جھکا ہوتا ہے۔',
           'زړه د انساني بدن د ژوند سرچینه ده. زړه د سینې په تشه (Chest Cavity) کې د دویمې او اوومې پوښتۍ ترمنځ پروت دی او دواړو خواوو ته یې سږي دي. زړه د ښي اړخ په پرتله کیڼ اړخ ته ډېر کوږ وي.'),
          ('The size of the heart is generally equal to the closed fist of a person, and its weight is one pound or 270 grams. If seen in terms of structure, the length of the heart is 12 centimetres while the breadth is 9 centimetres and the thickness 6 centimetres.',
           'دل کا سائز عام طور پر انسان کی اپنی بند مٹھی کے برابر ہوتا ہے اور اس کا وزن ایک پاؤ یا 270 گرام ہوتا ہے۔ اگر ساخت کے لحاظ سے دیکھا جائے تو دل کی لمبائی 12 سینٹی میٹر جبکہ چوڑائی 9 سینٹی میٹر اور موٹائی 6 سینٹی میٹر ہوتی ہے۔',
           'د زړه اندازه عموماً د انسان د خپل تړلي موټي سره برابره وي او وزن یې یو پاؤ یا ۲۷۰ ګرامه وي. که د جوړښت له مخې وکتل شي، د زړه اوږدوالی ۱۲ سانتي متره، پلنوالی ۹ سانتي متره او پنډوالی ۶ سانتي متره وي.')])
    r = rec(b, 2, 1, 16, first=True)
    BOOK.save(16, [(2, r)], issues=[{'id': 'hpe12-pdf016', 'unit': 2, 'printedPage': 11,
               'description': 'The circulatory-system illustration is reproduced as a coded schematic with the printed English labels (“…monary Artery” is cut at the page edge and given as Pulmonary Artery). “ایک پاؤ یا 270 گرام” is retained as printed (a pao is about 233–250 g).'}])


def p17():
    b = Builder()
    P(b, [('In this way, if the walls of the heart are examined, the walls of the heart appear to consist of three layers. The outer layer is called the pericardium (Pericardium), the middle layer the myocardium (Myocardium) and in this way the inner layer the endocardium (Endocardium). From the membrane of the outer layer a special kind of fluid comes out, which is called pericardial fluid (Pericardial Fluid), because of which the movement of the heart takes place easily.',
           'اس طرح اگر دل کی دیواروں کا معائنہ کیا جائے تو دل کی دیواریں تین تہوں پر مشتمل نظر آتی ہیں۔ بیرونی تہہ کو پیری کارڈیم (Pericardium)، درمیانی تہہ کو مائیو کارڈیم (Myocardium) اور اس طرح اندرونی تہہ کو انڈو کارڈیم (Endocardium) کہتے ہیں۔ بیرونی تہہ کی جھلی سے ایک خاص قسم کی رطوبت خارج ہوتی ہیں، جسے پیری کارڈیل فلوڈ (Pericardial Fluid) کہتے ہیں جس کی وجہ سے دل کی حرکت آسانی سے ہوتی ہے۔',
           'په دې ډول که د زړه دېوالونه معاینه شي، د زړه دېوالونه له درېیو پوړونو جوړ ښکاري. بهرني پوړ ته پیریکارډیم (Pericardium)، منځني پوړ ته مایوکارډیم (Myocardium) او همداسې داخلي پوړ ته اینډوکارډیم (Endocardium) ویل کېږي. د بهرني پوړ له غشا یو ځانګړی ډول مایع وځي چې پیریکارډیل مایع (Pericardial Fluid) ورته ویل کېږي او له امله یې د زړه حرکت په اسانۍ کېږي.')])
    lab = {'svc': 'Superior Vena Cava', 'aorta': 'Aorta', 'pa': 'Pulmonary Artery', 'pv': 'Pulmonary Vein', 'ra': 'Right Atrium', 'la': 'Left Atrium', 'rv': 'Right Ventricle',
           'lv': 'Left Ventricle', 'tri': 'Tricuspid Valve', 'mitral': 'Mitral Valve', 'pulv': 'Pulmonary Valve', 'aov': 'Aortic Valve', 'ivc': 'Inferior Vena Cava'}
    sv = [fig_heart(lab, c) for c in ('Internal structure of the heart', 'دل کی اندرونی ساخت', 'د زړه داخلي جوړښت')]
    b.visual('hpe12-fig-heart-section', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Chambers of Heart', 'دل کے خانے (Chambers of Heart)', 'د زړه خونې (Chambers of Heart)')
    b.p('The human heart has four chambers.', 'انسانی دل کے چار خانے ہوتے ہیں۔', 'د انسان زړه څلور خونې لري.')
    b.group('lines', [('1. Right atrium (Right Atrium)', '1. دایاں اذن (Right Atrium)', '1. ښی اذین (Right Atrium)'), ('2. Left atrium (Left Atrium)', '2. بایاں اذن (Left Atrium)', '2. کیڼ اذین (Left Atrium)'),
                      ('3. Right ventricle (Right Ventricle)', '3. دایاں بطن (Right Ventricle)', '3. ښی بطین (Right Ventricle)'), ('4. Left ventricle (Left Ventricle)', '4. بایاں بطن (Left Ventricle)', '4. کیڼ بطین (Left Ventricle)')])
    P(b, [('The right atrium is joined with the right ventricle and the left atrium with the left ventricle through valves (Valves). These same valves maintain the one-way flow of blood inside the heart and stop the reverse flow of blood.',
           'دایاں اذن دائیں بطن کے ساتھ اور بایاں اذن بائیں بطن کے ساتھ والوز (Valves) کے ذریعے ملے ہوتے ہیں۔ یہی والوز دل کے اندر خون کے یک طرفہ بہاؤ کو برقرار رکھتے ہیں اور خون کے اُلٹے بہاؤ کو روکتے ہیں۔',
           'ښی اذین له ښي بطین سره او کیڼ اذین له کیڼ بطین سره د والونو (Valves) له لارې نښتي وي. همدا والونه د زړه دننه د وینې یو اړخیز بهیر ساتي او د وینې د شا ته بهیر مخه نیسي.')])
    r = rec(b, 2, 2, 17)
    BOOK.save(17, [(2, r)], issues=[{'id': 'hpe12-pdf017', 'unit': 2, 'printedPage': 12,
               'description': 'The heart section diagram is reproduced as a coded schematic with all printed English labels. Owner Urdu ballpoint note in the left margin is excluded. “رطوبت خارج ہوتی ہیں”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    {12: p12, 13: p13, 14: p14, 15: p15, 16: p16, 17: p17}[n]()
