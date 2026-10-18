"""PDF80 printed 151–152: Unit 5 opener (learning outcomes); 5.1 need of sampling survey, 5.1.1 key terms (population … sample)."""
from class12_statistics_common import Builder, save

o = Builder()
o.h('Unit - 5', 'یونٹ - 5', 'واحد - 5')
o.h('Sampling and Sampling Distributions', 'نمونہ گیری اور نمونہ جاتی تقسیمیں', 'نمونه اخیستنه او نمونوي وېشونه')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Define sampling, sampling unit, sampling frame and sample design', 'نمونہ گیری، نمونہ اکائی، نمونہ فریم اور نمونے کے خاکے کی تعریف کریں', 'نمونه اخیستنه، نمونوي واحد، نمونوي چوکاټ او د نمونې ډیزاین تعریف کړي'),
    ('Differentiate between finite and infinite populations, sample survey and complete enumeration. Describe advantages and limitations of sampling.', 'محدود اور لامحدود آبادیوں، نمونہ جاتی سروے اور مکمل شمار میں فرق کریں۔ نمونہ گیری کے فوائد اور حدود بیان کریں۔', 'د محدودو او بې‌پایه نفوسونو، نمونوي سروې او بشپړې شمېرنې ترمنځ توپیر وکړي. د نمونه اخیستنې ګټې او محدودیتونه بیان کړي.'),
    ('Distinguish between probability/random sampling and non-probability/non-random sampling, random sampling with and without replacement.', 'احتمالی/تصادفی نمونہ گیری اور غیر احتمالی/غیر تصادفی نمونہ گیری، واپسی کے ساتھ اور بغیر تصادفی نمونہ گیری میں امتیاز کریں۔', 'د احتمالي/تصادفي نمونه اخیستنې او غیر احتمالي/غیر تصادفي نمونه اخیستنې، له بېرته اچولو سره او پرته تصادفي نمونه اخیستنې ترمنځ توپیر وکړي.'),
    ('Differentiate between sampling and non-sampling errors', 'نمونہ جاتی اور غیر نمونہ جاتی غلطیوں میں فرق کریں', 'د نمونوي او غیر نمونوي تېروتنو ترمنځ توپیر وکړي'),
    ('Describe simple random sampling stratified random sampling and systematic random sampling.', 'سادہ تصادفی نمونہ گیری، طبقاتی تصادفی نمونہ گیری اور منظم تصادفی نمونہ گیری بیان کریں۔', 'ساده تصادفي نمونه اخیستنه، طبقه‌بندي تصادفي نمونه اخیستنه او منظمه تصادفي نمونه اخیستنه بیان کړي.'),
    ('Use the random digits/random numbers table to select a simple random sample from a given finite population.', 'دی گئی محدود آبادی سے سادہ تصادفی نمونہ منتخب کرنے کے لیے تصادفی ہندسوں/اعداد کا جدول استعمال کریں۔', 'له ورکړل شوي محدود نفوس څخه د ساده تصادفي نمونې د ټاکلو لپاره د تصادفي رقمونو/عددونو جدول وکاروي.'),
    ('Define sampling distribution of statistic and standard error of statistic, sampling distribution of sample mean.', 'شماریہ کی نمونہ جاتی تقسیم اور شماریہ کی معیاری غلطی، نمونے کے اوسط کی نمونہ جاتی تقسیم کی تعریف کریں۔', 'د احصاییې نمونوي وېش او د احصاییې معیاري تېروتنه، د نمونې د منځني نمونوي وېش تعریف کړي.'),
    ('Describe the properties of a sampling distribution of a sample mean.', 'نمونے کے اوسط کی نمونہ جاتی تقسیم کی خصوصیات بیان کریں۔', 'د نمونې د منځني د نمونوي وېش ځانګړنې بیان کړي.'),
    ('Construct the sampling distribution of sample mean to verify its properties about its mean and variance.', 'نمونے کے اوسط کی نمونہ جاتی تقسیم بنائیں تاکہ اس کے اوسط اور تغیر کی خصوصیات کی تصدیق ہو سکے۔', 'د نمونې د منځني نمونوي وېش جوړ کړي ترڅو د منځني او واریانس په اړه یې ځانګړنې تایید کړي.'),
    ('Define the sampling distribution of difference between two sample means.', 'دو نمونوں کے اوسطوں کے فرق کی نمونہ جاتی تقسیم کی تعریف کریں۔', 'د دوو نمونو د منځنیو د توپیر نمونوي وېش تعریف کړي.'),
    ('Describe the properties of sampling distribution of difference between two sample means.', 'دو نمونوں کے اوسطوں کے فرق کی نمونہ جاتی تقسیم کی خصوصیات بیان کریں۔', 'د دوو نمونو د منځنیو د توپیر د نمونوي وېش ځانګړنې بیان کړي.'),
    ('Construct the sampling distribution of difference between two samples means to verify its properties about its mean and variance.', 'دو نمونوں کے اوسطوں کے فرق کی نمونہ جاتی تقسیم بنائیں تاکہ اس کے اوسط اور تغیر کی خصوصیات کی تصدیق ہو سکے۔', 'د دوو نمونو د منځنیو د توپیر نمونوي وېش جوړ کړي ترڅو د منځني او واریانس په اړه یې ځانګړنې تایید کړي.'),
    ('Define sampling distribution of sample proportion.', 'نمونے کے تناسب کی نمونہ جاتی تقسیم کی تعریف کریں۔', 'د نمونې د تناسب نمونوي وېش تعریف کړي.'),
    ('Describe the properties of a sampling distribution of sample proportion.', 'نمونے کے تناسب کی نمونہ جاتی تقسیم کی خصوصیات بیان کریں۔', 'د نمونې د تناسب د نمونوي وېش ځانګړنې بیان کړي.'),
    ('Construct the sampling distribution of sample proportion to verify its properties about it mean and variance.', 'نمونے کے تناسب کی نمونہ جاتی تقسیم بنائیں تاکہ اس کے اوسط اور تغیر کی خصوصیات کی تصدیق ہو سکے۔', 'د نمونې د تناسب نمونوي وېش جوړ کړي ترڅو د منځني او واریانس په اړه یې ځانګړنې تایید کړي.'),
    ('Define sampling distribution of difference between two sample proportions.', 'دو نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم کی تعریف کریں۔', 'د دوو نمونو د تناسبونو د توپیر نمونوي وېش تعریف کړي.'),
    ('Describe the properties of sampling distribution of difference between two sample proportions. Construct sampling distribution of difference between two sample proportions and verify its properties about mean and variance.', 'دو نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم کی خصوصیات بیان کریں۔ دو نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم بنائیں اور اس کے اوسط اور تغیر کی خصوصیات کی تصدیق کریں۔', 'د دوو نمونو د تناسبونو د توپیر د نمونوي وېش ځانګړنې بیان کړي. د دوو نمونو د تناسبونو د توپیر نمونوي وېش جوړ کړي او د منځني او واریانس په اړه یې ځانګړنې تایید کړي.'),
])
opening = o.build('stat12-u5-opening', 'Unit 5 — Learning outcomes', 'یونٹ 5 — حاصلاتِ تعلم', 'واحد 5 — د زده کړې پایلې', 80, [151])

b = Builder()
b.h('5.1 Need of sampling survey', '5.1 نمونہ جاتی سروے کی ضرورت', '5.1 د نمونوي سروې اړتیا')
b.p('The origin of sampling is as old as our civilization and now it is a part of our day-to-day life. Human knowledge and actions are mainly based on samples, specifically, in scientific research. Sample data can either be obtained through sample surveys or experimentation which is the basic input in statistical analysis and inference.',
    'نمونہ گیری کی ابتدا ہماری تہذیب جتنی پرانی ہے اور اب یہ ہماری روزمرہ زندگی کا حصہ ہے۔ انسانی علم اور اعمال بنیادی طور پر نمونوں پر مبنی ہیں، خاص طور پر سائنسی تحقیق میں۔ نمونے کا مواد یا تو نمونہ جاتی سروے سے یا تجربات سے حاصل کیا جا سکتا ہے جو شماریاتی تجزیے اور استنباط کا بنیادی ذریعہ ہے۔',
    'د نمونه اخیستنې پیل زموږ د تمدن په اندازه زوړ دی او اوس زموږ د ورځني ژوند برخه ده. انساني پوهه او کړنې په اصل کې پر نمونو ولاړې دي، په ځانګړې توګه په علمي څېړنه کې. د نمونې معلومات یا د نمونوي سروې له لارې یا د تجربو له لارې ترلاسه کېدای شي چې د احصاییوي شننې او استنتاج بنسټیز ورودي دي.')
b.h('5.1.1 Key terms and definitions', '5.1.1 اہم اصطلاحات اور تعریفیں', '5.1.1 کلیدي اصطلاحګانې او تعریفونه')
b.h('◆ Population', '◆ آبادی', '◆ نفوس')
b.p('A group of individuals or objects about which we wish to know something is called population or universe.', 'افراد یا اشیاء کا وہ گروہ جس کے بارے میں ہم کچھ جاننا چاہتے ہیں، آبادی یا کائنات کہلاتا ہے۔', 'د افرادو یا شیانو هغه ډله چې غواړو د هغې په اړه څه پوه شو، نفوس یا کائنات بلل کېږي.')
b.h('◆ Finite population', '◆ محدود آبادی', '◆ محدود نفوس')
b.p('If the number of individuals or items of a population are fixed and limited, it is known as finite population e.g. the population of government hospitals in Pakistan, students in a college, workers in a factory, etc. Finite population usually consists of existing items.',
    'اگر کسی آبادی کے افراد یا اشیاء کی تعداد مقررہ اور محدود ہو تو اسے محدود آبادی کہتے ہیں، مثلاً پاکستان میں سرکاری ہسپتالوں کی آبادی، کسی کالج کے طلبہ، کسی کارخانے کے کارکن وغیرہ۔ محدود آبادی عموماً موجود اشیاء پر مشتمل ہوتی ہے۔',
    'که د یوه نفوس د افرادو یا توکو شمېر ټاکلی او محدود وي، محدود نفوس بلل کېږي، لکه په پاکستان کې د دولتي روغتونونو نفوس، په یوه کالج کې زده کوونکي، په یوه فابریکه کې کارګران او نور. محدود نفوس معمولاً له شته توکو جوړ وي.')
b.h('◆ Infinite population', '◆ لامحدود آبادی', '◆ بې‌پایه نفوس')
b.p('If the population consists of an infinite number of items, it is called infinite population. For example, the population of all real numbers is lying between 10 and 20, the population of stars in the sky etc.', 'اگر آبادی لامحدود تعداد میں اشیاء پر مشتمل ہو تو اسے لامحدود آبادی کہتے ہیں۔ مثلاً 10 اور 20 کے درمیان تمام حقیقی اعداد کی آبادی، آسمان میں ستاروں کی آبادی وغیرہ۔', 'که نفوس له بې‌پایه شمېر توکو جوړ وي، بې‌پایه نفوس بلل کېږي. د بېلګې په توګه د 10 او 20 ترمنځ د ټولو حقیقي عددونو نفوس، په اسمان کې د ستورو نفوس او نور.')
b.h('◆ Sampling unit', '◆ نمونہ اکائی', '◆ نمونوي واحد')
b.p('A single element or group of elements of a population from which required information can be obtained is called sampling unit or unit of the population. For example, if a population has 100 mango trees, then a single mango tree is the sampling unit. A unit may either be natural (e.g. a person, a family, a tree, an animal etc.) or artificial (e.g. a village, districts, a plot of specified size etc.).',
    'آبادی کا وہ واحد عنصر یا عناصر کا گروہ جس سے مطلوبہ معلومات حاصل کی جا سکیں، نمونہ اکائی یا آبادی کی اکائی کہلاتا ہے۔ مثلاً اگر کسی آبادی میں 100 آم کے درخت ہوں تو ایک آم کا درخت نمونہ اکائی ہے۔ اکائی یا تو قدرتی ہو سکتی ہے (مثلاً شخص، خاندان، درخت، جانور وغیرہ) یا مصنوعی (مثلاً گاؤں، اضلاع، مخصوص سائز کا قطعہ وغیرہ)۔',
    'د نفوس هغه یو عنصر یا د عناصرو ډله چې اړین معلومات ترې ترلاسه کېدای شي، نمونوي واحد یا د نفوس واحد بلل کېږي. د بېلګې په توګه که یو نفوس 100 د امبو ونې ولري، نو د امبو یوه ونه نمونوي واحد دی. واحد کېدای شي طبیعي وي (لکه یو کس، یوه کورنۍ، یوه ونه، یو څاروی او نور) یا مصنوعي (لکه یو کلی، ولسوالۍ، د ټاکلې اندازې یوه ټوټه ځمکه او نور).')
b.h('◆ Sample', '◆ نمونہ', '◆ نمونه')
b.p('A part or fraction of a population is called sample. In everyday life decision about population is made on the basis of a sample, therefore, it is', 'آبادی کے کسی حصے یا جز کو نمونہ کہتے ہیں۔ روزمرہ زندگی میں آبادی کے بارے میں فیصلہ نمونے کی بنیاد پر کیا جاتا ہے، لہٰذا یہ', 'د نفوس یوې برخې یا ټوټې ته نمونه وایي. په ورځني ژوند کې د نفوس په اړه پرېکړه د نمونې پر بنسټ کېږي، نو دا')
rec = b.build('stat12-p080-sampling-terms', '5.1 Need of sampling survey — key terms', '5.1 نمونہ جاتی سروے کی ضرورت — اہم اصطلاحات', '5.1 د نمونوي سروې اړتیا — کلیدي اصطلاحګانې', 80, [152])

if __name__ == '__main__':
    save(80, [(5, opening), (5, rec)])
