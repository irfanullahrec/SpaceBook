# -*- coding: utf-8 -*-
"""Unit 8 part D — PDF 176-180 (printed 173-177): 8.7 disorders of gut, key points, exercise."""
from bio9_tools import Section
from unit8_figs import three

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def sections():
    s = Section('bio8_7', '8.7', 'Disorders of Gut', 'آنتوں کی خرابیاں', 'د کولمو اختلالات', [176, 177])
    s.h('8.7 Disorders of Gut', '8.7 آنتوں کی خرابیاں', '8.7 د کولمو اختلالات')
    s.h('a. Constipation', 'a. قبض', 'a. قبضیت')
    s.p('Constipation is a disorder of the digestive system in which faeces are not eliminated from the body at regular intervals. The symptoms of constipation are passing hard and dry stools, unusual straining at stool and abdominal bloating or discomfort.',
        'قبض نظامِ انہضام کی ایک خرابی ہے جس میں فضلہ باقاعدہ وقفوں سے جسم سے خارج نہیں ہوتا۔ قبض کی علامات سخت اور خشک پاخانہ آنا، پاخانے کے وقت غیر معمولی زور لگانا اور پیٹ کا پھولنا یا بے آرامی ہیں۔',
        'قبضیت د هاضمې سیسټم یو اختلال دی چې غایطه مواد پکې په منظمو وقفو له بدن نه وځي. د قبضیت نښې سخت او وچ غایطه مواد، د رفع حاجت پر مهال غیر عادي زور او د ګېډې پړسوب یا ناارامي دي.')
    s.p('The common causes of constipation include frequent use of spicy food, less intake of vegetables and dietary fibre and insufficient fluid intake.', 'قبض کی عام وجوہات میں مرچ مسالے والی خوراک کا بار بار استعمال، سبزیوں اور غذائی ریشے کا کم استعمال اور ناکافی سیال لینا شامل ہیں۔', 'د قبضیت عام لاملونه د مسالې لرونکو خوړو ډېر کارول، د سبزیو او غذايي فایبر لږ اخیستل او د مایعاتو ناکافي اخیستل دي.')
    s.p('Constipation is treated by taking more dietary fibre and water along with diet. Laxative medicines are also used to treat constipation.', 'قبض کا علاج غذا کے ساتھ زیادہ غذائی ریشہ اور پانی لے کر کیا جاتا ہے۔ قبض کے علاج کے لیے جلاب آور دوائیں بھی استعمال ہوتی ہیں۔', 'قبضیت د خوراک سره د ډېر غذايي فایبر او اوبو په اخیستو درملېږي. د قبضیت د درملنې لپاره مسهل درمل هم کارېږي.')
    s.callout(SI, [('The routine use of laxative medicines is discouraged because patient may become dependent on their use.', 'جلاب آور دواؤں کے معمول کے استعمال کی حوصلہ شکنی کی جاتی ہے کیونکہ مریض ان کا عادی ہو سکتا ہے۔', 'د مسهلو درملو د ورځني کارونې مخه نیول کېږي ځکه ناروغ ښايي پرې روږدی شي.')])
    s.h('b. Diarrhoea', 'b. اسہال', 'b. اسهال')
    s.p('Diarrhoea means that proper amounts of water are not absorbed from colon and the required water leaves the body along with faeces. The main symptoms of diarrhoea are frequent, watery, loose bowel movements, abdominal pain, nausea and vomiting. Diarrhoea results in dehydration, which means the body lacks enough fluid to function properly.',
        'اسہال کا مطلب ہے کہ کولون سے پانی کی مناسب مقدار جذب نہیں ہوتی اور ضروری پانی فضلے کے ساتھ جسم سے نکل جاتا ہے۔ اسہال کی اہم علامات بار بار، پانی جیسے پتلے پاخانے، پیٹ درد، متلی اور الٹی ہیں۔ اسہال سے ڈی ہائیڈریشن ہوتی ہے یعنی جسم میں ٹھیک طرح کام کرنے کے لیے کافی سیال نہیں رہتا۔',
        'اسهال دا معنا لري چې له کولون څخه د اوبو مناسب مقدار نه جذبېږي او اړینې اوبه له غایطه موادو سره له بدن وځي. د اسهال اصلي نښې ډېر ځله، اوبلن او نري دستونه، د ګېډې درد، زړه بدوالی او کانګې دي. اسهال د ډیهایډریشن لامل کېږي یعنې بدن د سم کار لپاره بسنه کوونکې مایع نه لري.')
    s.p('Diarrhea is caused by bacterial, viral or parasitic infection of the colon walls. It is treated by consuming adequate amounts of water preferably mixed with salts and nutrients to replace the loss. When diarrhoea is due to bacterial infection, it is treated by administration of antibiotics. Diarrhoea can be prevented by taking sufficient amounts of clean water and food.',
        'اسہال کولون کی دیواروں کے بیکٹیریائی، وائرل یا طفیلی انفیکشن سے ہوتا ہے۔ اس کا علاج نقصان پورا کرنے کے لیے مناسب مقدار میں پانی، بہتر ہے نمکیات اور غذائی اجزا ملا کر، پینے سے کیا جاتا ہے۔ جب اسہال بیکٹیریائی انفیکشن کی وجہ سے ہو تو اینٹی بائیوٹکس دے کر علاج کیا جاتا ہے۔ صاف پانی اور خوراک کی کافی مقدار لے کر اسہال سے بچا جا سکتا ہے۔',
        'اسهال د کولون د دېوالونو د باکتریايي، ویروسي یا پرازیتي انتان له امله رامنځته کېږي. د ضایع شوي د پوره کولو لپاره د کافي اوبو په څښلو، غوره دا چې له مالګو او غذايي موادو سره ګډې وي، درملېږي. کله چې اسهال د باکتریايي انتان له امله وي، په انټي بیوټیکونو درملېږي. د پاکو اوبو او خوړو د کافي مقدار په اخیستو د اسهال مخه نیول کېدای شي.')
    s.h('c. Ulcers', 'c. السر', 'c. زخمونه (السر)')
    s.p('An ulcer is a small erosion (hole) in the walls of the gut. It usually occurs in the walls of stomach and is called gastric ulcer. It may also develop in duodenum (duodenal ulcer) or oesophagus (oesophageal ulcer). The symptoms of ulcer include abdominal burning and pain, loss of appetite and weight loss.',
        'السر آنتوں کی دیواروں میں ایک چھوٹا کٹاؤ (سوراخ) ہے۔ یہ عموماً معدے کی دیواروں میں ہوتا ہے اور اسے معدے کا السر کہتے ہیں۔ یہ ڈیوڈینم (ڈیوڈینل السر) یا غذائی نالی (اوسوفیجیل السر) میں بھی بن سکتا ہے۔ السر کی علامات میں پیٹ میں جلن اور درد، بھوک کا ختم ہونا اور وزن میں کمی شامل ہیں۔',
        'السر د کولمو په دېوالونو کې یو کوچنی خوړل شوی ځای (سوری) دی. معمولاً د معدې په دېوالونو کې پېښېږي او معدي زخم بلل کېږي. ښايي په دیوډینم (دیوډینل زخم) یا مرۍ (د مرۍ زخم) کې هم جوړ شي. د زخم نښې د ګېډې سوځېدنه او درد، د اشتها له منځه تلل او د وزن کمېدل دي.')
    en, ur, ps = three('ulcer')
    s.fig('bio8-fig8-15', en, ur, ps, .55, caption=('Figure 8.15: Gastric ulcer', 'شکل 8.15: معدے کا السر', 'شکل 8.15: معدي زخم'))
    s.p('The basic cause of ulcers is the destruction of the gut wall by hydrochloric acid. Cigarette smoking is also an important cause of ulcer formation. Ulcer is treated with alkaline medicines. Its preventions include avoiding spicy and acidic foods.',
        'السر کی بنیادی وجہ ہائیڈروکلورک ایسڈ سے آنت کی دیوار کی تباہی ہے۔ سگریٹ نوشی بھی السر بننے کی ایک اہم وجہ ہے۔ السر کا علاج الکلائن دواؤں سے کیا جاتا ہے۔ اس سے بچاؤ میں مرچ مسالے والی اور تیزابی غذاؤں سے پرہیز شامل ہے۔',
        'د زخمونو بنسټیز لامل د هایدروکلوریک اسید له خوا د کولمو د دېوال ویجاړېدل دي. سګرټ څکول هم د زخم د جوړېدو مهم لامل دی. زخم په القلي درملو درملېږي. د مخنیوي لارې یې له مسالې لرونکو او تیزابي خوړو ډډه کول دي.')
    s.p('SpaceBook note: on PDF 177 a few letters of the last line ("avoiding", "of the", "ulcer") are faded in the scan. They are read from the visible letter shapes and context.',
        'اسپیس بک نوٹ: PDF 177 پر آخری سطر کے چند حروف ("avoiding"، "of the"، "ulcer") اسکین میں دھندلے ہیں۔ انہیں نظر آنے والے حروف اور سیاق سے پڑھا گیا ہے۔',
        'د سپېس بوک یادونه: په PDF 177 کې د وروستۍ کرښې څو توري ("avoiding"، "of the"، "ulcer") په سکن کې تت دي. د ښکاره تورو او سیاق له مخې لوستل شوي.', editorial=True)
    return [s]


KEY_POINTS = [
    ('Nutrients are the materials (elements and compounds) that organisms obtain and use for maintaining life.', 'غذائی اجزا وہ مادے (عناصر اور مرکبات) ہیں جو جاندار حاصل کر کے زندگی برقرار رکھنے کے لیے استعمال کرتے ہیں۔', 'غذايي مواد هغه مواد (عناصر او مرکبونه) دي چې ژوندي موجودات یې ترلاسه کوي او د ژوند د ساتلو لپاره یې کاروي.'),
    ('Plants need nitrogen to form proteins, hormones, chlorophyll, vitamins and enzymes.', 'پودوں کو پروٹینز، ہارمونز، کلوروفل، وٹامنز اور انزائمز بنانے کے لیے نائٹروجن درکار ہے۔', 'بوټي د پروټینونو، هورمونونو، کلوروفیل، ویټامینونو او انزایمونو د جوړولو لپاره نایټروجن ته اړتیا لري.'),
    ('Plants require magnesium to form chlorophyll.', 'پودوں کو کلوروفل بنانے کے لیے میگنیشیم درکار ہے۔', 'بوټي د کلوروفیل د جوړولو لپاره مګنیزیم ته اړتیا لري.'),
    ('Carbohydrates present in human food, are the major source of energy', 'انسانی خوراک میں موجود کاربوہائیڈریٹس توانائی کا بڑا ذریعہ ہیں', 'په انساني خوړو کې کاربوهایډریټونه د انرژۍ لویه سرچینه ده'),
    ('Proteins are components of the cytoplasm, membranes and organelles. They are also the major parts of muscles, ligaments and tendons. Many proteins act as enzymes.', 'پروٹینز سائٹوپلازم، جھلیوں اور عضیات کے اجزا ہیں۔ یہ عضلات، لگامنٹس اور ٹینڈنز کے بڑے حصے بھی ہیں۔ بہت سی پروٹینز انزائمز کا کام کرتی ہیں۔', 'پروټینونه د سایټوپلازم، غشاوو او اورګانیلونو برخې دي. د عضلو، اربطو او وترونو لویې برخې هم دي. ډېر پروټینونه د انزایم کار کوي.'),
    ('Dietary fiber is the indigestible part of the human food, mainly consisting of cellulose.', 'غذائی ریشہ انسانی خوراک کا ناقابلِ ہضم حصہ ہے جو زیادہ تر سیلولوز پر مشتمل ہے۔', 'غذايي فایبر د انساني خوړو نه هضمېدونکې برخه ده چې ډېری له سلولوز جوړه ده.'),
    ('Balanced diet contains carbohydrate, protein, fat, vitamins, minerals and fiber in the correct proportions', 'متوازن غذا میں کاربوہائیڈریٹ، پروٹین، چکنائی، وٹامنز، معدنیات اور ریشہ درست تناسب میں ہوتے ہیں', 'متوازن خوراک کاربوهایډریټ، پروټین، غوړ، ویټامینونه، معدنونه او فایبر په سم تناسب لري'),
    ('Protein-Energy Malnutrition means a condition in which the body is not getting required amounts of proteins or any energy producing nutrients.', 'پروٹین انرجی مال نیوٹریشن ایسی حالت ہے جس میں جسم کو پروٹینز یا توانائی پیدا کرنے والے غذائی اجزا کی درکار مقدار نہیں ملتی۔', 'د پروټین انرژۍ سوءتغذیه هغه حالت دی چې بدن پکې د پروټینونو یا انرژي تولیدوونکو غذايي موادو اړین مقدار نه ترلاسه کوي.'),
    ('Marasmus occurs in children due to less intake of carbohydrates, fats and proteins.', 'میرازمس بچوں میں کاربوہائیڈریٹس، چکنائی اور پروٹینز کی کم مقدار لینے سے ہوتا ہے۔', 'مرازمس په ماشومانو کې د کاربوهایډریټونو، غوړو او پروټینونو د لږ اخیستو له امله پېښېږي.'),
    ('Kwashiorkor occurs in children or adults due to inadequate intake of proteins', 'کواشیورکور بچوں یا بالغوں میں پروٹینز کی ناکافی مقدار لینے سے ہوتا ہے', 'کواشیورکور په ماشومانو یا لویانو کې د پروټینونو د ناکافي اخیستو له امله پېښېږي'),
    ('Teeth help in the mechanical digestion (grinding and mastication) of food', 'دانت خوراک کے میکانیکی ہضم (پیسنے اور چبانے) میں مدد دیتے ہیں', 'غاښونه د خوړو په میخانیکي هضم (اوړه کولو او ژولو) کې مرسته کوي'),
    ('The salivary glands secrete saliva which contains water, mucous, salts and salivary amylase, which breaks starch and glycogen into maltose.', 'لعابی غدود لعاب خارج کرتے ہیں جس میں پانی، بلغم، نمکیات اور سلائیوری امائلیز ہوتا ہے جو نشاستے اور گلائکوجن کو مالٹوز میں توڑتا ہے۔', 'د لاړو غدې لاړې افرازوي چې اوبه، بلغم، مالګې او د لاړو امایلېز لري چې نشایسته او ګلایکوجن په مالټوز ماتوي.'),
    ('Peristalsis is a wave like contractions and relaxations in the muscular walls of the alimentary canal by which the food is moved along the alimentary canal.', 'پیریسٹالسس نظامِ انہضام کی نالی کی عضلاتی دیواروں میں لہر نما سکڑاؤ اور پھیلاؤ ہے جس سے خوراک نالی میں آگے بڑھتی ہے۔', 'پیرسټالسس د هاضمې نل په عضلي دېوالونو کې څپې ډوله انقباضونه او انبساطونه دي چې خواړه پرې د نل په اوږدو کې مخ ته ځي.'),
    ('The gastric glands of stomach secrete gastric juice, which contains mucus, pepsinogen enzyme and hydrochloric acid.', 'معدے کے معدی غدود گیسٹرک جوس خارج کرتے ہیں جس میں بلغم، پیپسینوجن انزائم اور ہائیڈروکلورک ایسڈ ہوتا ہے۔', 'د معدې معدي غدې ګاسټریک جوس افرازوي چې بلغم، پیپسینوجن انزایم او هایدروکلوریک اسید لري.'),
    ('Duodenum is the first part of small intestine, in which the chyme meets the bile from the liver and pancreatic juice from the pancreas.', 'ڈیوڈینم چھوٹی آنت کا پہلا حصہ ہے جس میں کائم جگر سے آنے والے صفرا اور لبلبے کے رس سے ملتا ہے۔', 'دیوډینم د کوچنۍ کولمې لومړۍ برخه ده چې کایم پکې د ځيګر له صفرا او د پانقراس له جوس سره یوځای کېږي.'),
    ('Liver produces bile which breaks larger fats into smaller droplets (emulsification of fats).', 'جگر صفرا بناتا ہے جو بڑی چکنائی کو چھوٹی بوندوں میں توڑتا ہے (چکنائی کا ایملسیفیکیشن)۔', 'ځيګر صفرا جوړوي چې لوی غوړ په کوچنیو څاڅکو ماتوي (د غوړو ایملسیفیکېشن).'),
    ('Pancreas secretes pancreatic juice which contains sodium bicarbonate and enzymes trypsinogen (inactive enzyme) pancreatic amylase and lipase.', 'لبلبہ لبلبی رس خارج کرتا ہے جس میں سوڈیم بائی کاربونیٹ اور انزائمز ٹرپسینوجن (غیر فعال انزائم)، لبلبی امائلیز اور لائپیز ہوتے ہیں۔', 'پانقراس پانقراسي جوس افرازوي چې سوډیم بای کاربونېټ او انزایمونه ټریپسینوجن (غیر فعال انزایم)، پانقراسي امایلېز او لایپېز لري.'),
    ('The enzymes trypsin, pancreatic amylase and lipase acts on proteins, carbohydrates and lipids (fats) respectively.', 'انزائمز ٹرپسن، لبلبی امائلیز اور لائپیز بالترتیب پروٹینز، کاربوہائیڈریٹس اور لپڈز (چکنائی) پر عمل کرتے ہیں۔', 'انزایمونه ټریپسین، پانقراسي امایلېز او لایپېز په ترتیب سره پر پروټینونو، کاربوهایډریټونو او لیپیډونو (غوړو) عمل کوي.'),
    ('The intestinal juice contains enzymes which complete the digestion of food.', 'آنتوں کے رس میں ایسے انزائمز ہوتے ہیں جو خوراک کا ہضم مکمل کرتے ہیں۔', 'د کولمو جوس داسې انزایمونه لري چې د خوړو هضم بشپړوي.'),
    ('The inner lining of small intestine has large folds, which have millions of villi.', 'چھوٹی آنت کی اندرونی جھلی میں بڑی تہیں ہیں جن میں لاکھوں ولائی ہیں۔', 'د کوچنۍ کولمې داخلي استر لویې ګونځې لري چې میلیونونه ویلای لري.'),
    ('Colon-the longest part of large intestine absorbs most of the water and some vitamins and minerals from the material.', 'کولون، بڑی آنت کا سب سے لمبا حصہ، مادے سے زیادہ تر پانی اور کچھ وٹامنز اور معدنیات جذب کرتا ہے۔', 'کولون، د لویې کولمې تر ټولو اوږده برخه، له موادو ډېرې اوبه او ځینې ویټامینونه او معدنونه جذبوي.'),
    ('Constipation means that faeces are not eliminated from the body at regular intervals. Diarrhoea means that required water leaves the body along with faeces.', 'قبض کا مطلب ہے کہ فضلہ باقاعدہ وقفوں سے جسم سے خارج نہیں ہوتا۔ اسہال کا مطلب ہے کہ ضروری پانی فضلے کے ساتھ جسم سے نکل جاتا ہے۔', 'قبضیت دا معنا لري چې غایطه مواد په منظمو وقفو له بدن نه وځي. اسهال دا معنا لري چې اړینې اوبه له غایطه موادو سره له بدن وځي.'),
]


def keypoints_section():
    s = Section('bio8_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [178])
    s.ul(KEY_POINTS)
    return s


NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'
MCQS = [
    ('i. The deficiency of which macronutrients causes chlorosis in plants?', ['Carbon', 'Oxygen', 'Nitrogen', 'Calcium'], 2, NOTE + ' Nitrogen deficiency causes yellowing of leaves (8.1.1). The unit names magnesium as the usual cause of chlorosis, but magnesium is not among the printed options.'),
    ('ii. All of the following are elements that plants need in very small amounts (micronutrients) except:', ['Hydrogen', 'Iron', 'Chlorine', 'Copper'], 0, NOTE + ' Hydrogen is a macronutrient (Table 8.1).'),
    ('iii. Which substance, is used by plants to make proteins?', ['Carbon dioxide', 'Oxygen', 'Nitrates', 'Vitamins'], 2, NOTE + ' Nitrogen, taken up as nitrates, is part of every amino acid.'),
    ('iv. What happens when food reaches the stomach?', ['No digestion occurs in the stomach.', 'The food moves quickly into the small intestine.', 'Juices mix with the food and stomach muscles squeeze it.', 'The food is completely digested and is absorbed into the circulatory system.'], 2, NOTE),
    ('v. Which of the following does NOT manufacture digestive juices?', ['Oesophagus', 'Stomach', 'Pancreas', 'Intestine'], 0, NOTE),
    ('vi. What is absorbed from the material when it is in the large intestine?', ['Water', 'Vitamins', 'Salts', 'All of these'], 3, NOTE + ' The colon absorbs most of the water and some vitamins and minerals.'),
    ('vii. Which of the following is NOT a function of salivary glands?', ['Start digestion of proteins', 'Helps in the lubrication', 'Secrete saliva', 'Makes taste possible'], 0, NOTE + ' Salivary amylase digests starch and glycogen, not proteins.'),
    ('viii. The cardiac sphincter serves as a valve between:', ['Stomach and duodenum', 'Oesophagus and stomach', 'Duodenum and ileum', 'Jejunum and caecum'], 1, NOTE),
    ('ix. The function of the liver is to:', ['Metabolize carbohydrates, lipids and proteins', 'Break mature red blood cells.', 'Detoxify the chemicals', 'All of the above'], 3, NOTE),
    ('x. The digestive enzyme pepsin secreted by gastric glands begins the digestion of;', ['Carbohydrates', 'Proteins', 'Fats', 'Vitamins'], 1, NOTE + ' The options are printed in two columns (a and c on the left, b and d on the right).'),
]
SQ = ['i. List all parts (in order) of the human digestive system through which food passes.', 'ii. How is food mechanically broken down during digestion?',
      'iii. How does the digestion and absorption of fats differ from the digestion and absorption of carbohydrates and proteins.', 'iv. Enlist five environmental hazards related to the use of fertilizers.',
      'v. What is malnutrition? Why it is considered to be a health hazard?', 'vi. Discuss the role of dietary fiber in balanced diet.']
LQ = ['i. Overtake of nutrition can lead to serious health disorders. Evaluate the statement by giving examples.', 'ii. List down major enzymes in the human digestive system. Elaborate their role in digestion.',
      'iii. Explain the importance of water in the human body', 'iv. Explain the role of oral cavity and pharynx in the digestive system.', 'v. Describe the structure of a villus, including the roles of capillaries and lacteals.']
LAB = 'SpaceBook-authored answer based on this unit (the textbook prints no answers):\n'
SQ_ANS = [
    'Oral cavity, pharynx, oesophagus, stomach, small intestine (duodenum, jejunum, ileum), large intestine (caecum, colon, rectum) and out through the anus.',
    'Incisors cut and bite, canines tear, and premolars and molars grind and chew the food. The tongue keeps food between the teeth. In the stomach the muscular walls contract and churn the food into smaller particles.',
    'Fats are first emulsified by bile into small droplets and then digested by lipase into fatty acids and glycerol, which are absorbed into the lacteals. Carbohydrates and proteins are digested by amylases and by pepsin and trypsin, and their products (simple sugars and amino acids) enter the blood capillaries of the villi and go to the liver through the hepatic portal vein.',
    'The unit lists four hazards: increased soil salinity and acidity, emission of the greenhouse gas nitrous oxide from stored and applied nitrogen fertilizers, NO₃⁻ leaching into groundwater that harms human and animal health, and eutrophication of surface water. A fifth commonly given hazard is depletion of oxygen in water bodies caused by algal growth, which makes survival difficult for aquatic organisms.',
    'Malnutrition is taking a diet in which the required nutrients are not in enough quantity or are over the required quantity. It is a health hazard because it causes PEM (marasmus, kwashiorkor), mineral deficiency diseases (anaemia, goiter, osteoporosis, rickets) and problems of over intake such as obesity, heart disease and constipation, and severe malnutrition may cause death.',
    'Dietary fiber (roughage) is indigestible, mostly cellulose. It speeds up the passage of food through the gut, which reduces the risk of constipation and colon cancer. Soluble fiber forms a gel that traps cholesterol and so controls blood cholesterol. Colon bacteria also use fibre and nourish colon cells.',
]
LQ_ANS = [
    'Over intake of high-calorie food causes overweight and obesity, with hypertension and liver, renal and heart disorders. Excess fat is deposited in artery walls (arteriosclerosis), leading to cardio-vascular disease, hypertension and diabetes. Over-intake of vitamin D causes nausea, fatigue, vomiting and renal damage. Over-intake of vitamin A causes dry itchy skin, painful swelling of legs and hands and enlargement of the spleen.',
    'Salivary amylase (mouth): starch and glycogen to maltose. Pepsin (stomach, from pepsinogen activated by HCl): proteins to peptides. Trypsin (pancreas, from trypsinogen activated by a duodenal enzyme): proteins to amino acids. Pancreatic amylase: remaining starch to simple sugars. Lipase: emulsified fats to fatty acids and glycerol. Intestinal juice enzymes (ileum): break down leftover proteins, carbohydrates and fats and complete digestion.',
    'Water makes about 70% of the body. It is the solvent for metabolic reactions, carries O₂, CO₂ and nutrients in blood, bathes cells as interstitial fluid, is a reactant in hydrolysis, stabilizes body temperature, lubricates as part of mucus, and flushes toxic wastes such as urea through the kidneys. An adult needs about two litres a day; losing too much causes dehydration.',
    'In the oral cavity, teeth carry out mechanical digestion and the tongue tastes, moves food between the teeth and helps swallowing. Three pairs of salivary glands secrete saliva: mucous lubricates, sodium bicarbonate kills germs and makes food alkaline, and salivary amylase starts the digestion of starch and glycogen into maltose. Food is formed into a bolus. The pharynx passes the bolus to the oesophagus; swallowing starts voluntarily and becomes a reflex. The epiglottis closes the glottis and the soft palate and uvula close the nasopharynx so food does not enter the windpipe or nose.',
    'Villi are finger-like projections on the folds of the small intestine lining. Each villus has a one-cell-thick epithelium with microvilli that greatly increase the surface area. Inside are blood capillaries, which absorb simple sugars, amino acids, vitamins, minerals and water and drain into the hepatic portal vein to the liver, and a lacteal (lymph vessel), which absorbs fatty acids and glycerol and pours them into the blood stream.',
]


def exercise():
    return dict(sourcePdfPages=[179, 180], sourcePrintedPages=[176, 177], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=LAB + a, sourceSection='B. Give short answers to the following questions.') for q, a in zip(SQ, SQ_ANS)],
                detailedQuestions=[dict(q=q, answer=LAB + a, sourceSection='C. Give detailed answers to the following questions.') for q, a in zip(LQ, LQ_ANS)],
                activities=[dict(title='Activities 8.1', desc="Test for the presence of starch (iodine test); reducing sugars (Benedict's test); protein (Biuret test); and lipids (ethanol emulsion test).", sourcePrintedPage=158),
                            dict(title='Activity 8.2', desc='The quality and quantity of food intake affects health and therefore, poor food intake may lead to certain food related disorders. Mention few of such disorders from your own environment, discuss how they are affecting the general population and how the nutrition could be improved considering the economic conditions of the people.', sourcePrintedPage=162)])
