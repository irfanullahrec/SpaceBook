"""Civics XII PDF70–72: pp.130–135 — ways of promoting peace at local level (end); chapter 6 exercise; chapter 7 (Peace and Diversity) opener and
objectives; peace (definitions); importance of peaceful society (begins). Run: python class12_civics_page070.py N (70–72)."""
import sys
from class12_civics_common import BOOK, Builder, rec, P
from class12_civics_page043 import TF, TFU, TFP


def p70():
    b = Builder()
    P(b, [('… solved, and after every war talks have to be held. Problems are solved not with passion but with sense. For sense the brain has to be used. Another important method is acquaintance with rights and duties. Unrest arises when people cannot distinguish between their own rights and those of others. Then an important problem is also that people talk of rights but turn away from their duties. There is a need that people not only be made acquainted with rights and duties, but a balance also be created between rights and duties.',
           'ہوتے اور ہر جنگ کے بعد بات چیت کرنی پڑتی ہے۔ مسائل جوش سے نہیں ہوش سے حل ہوتے ہیں۔ ہوش کیلئے دماغ کا اِستعمال کرنا پڑتا ہے۔ ایک اور اہم طریقہ حقوق و فرائض سے واقفیت ہے۔ بدامنی اُس وقت پیدا ہوتی ہے جب لوگ اپنے اور دوسروں کے حقوق میں فرق نہیں کر سکتے۔ پھر اہم مسئلہ یہ بھی ہے کہ لوگ حقوق کی بات تو کرتے ہیں لیکن اپنے فرائض سے روگردانی کرتے ہیں۔ ضرورت اِس بات کی ہے کہ لوگوں کو نہ صرف حقوق و فرائض سے واقف بنایا جائے بلکہ حقوق و فرائض میں توازن بھی پیدا ہو۔',
           '… حلېږي او له هرې جګړې وروسته خبرې اترې کول پکار وي. ستونزې په جوش نه، په هوش حلېږي. هوش ته د دماغ کارول پکار وي. بله مهمه لاره له حقونو او مکلفیتونو سره بلدتیا ده. بدامني هغه وخت پیدا کېږي چې خلک د خپلو او د نورو د حقونو ترمنځ توپیر نه شي کولی. بیا یوه مهمه ستونزه دا هم ده چې خلک د حقونو خبره کوي، خو له خپلو مکلفیتونو مخ اړوي. اړتیا ده چې خلک نه یوازې له حقونو او مکلفیتونو خبر کړای شي، بلکې د حقونو او مکلفیتونو ترمنځ توازن هم پیدا شي.'),
          ('The biggest thing is that there be an intention and resolve for peace and a long-lasting strategy. If in any community most people resolve that their environment and community are to be taken out of the darkness of unrest, then there is no reason why the lamps of peace should not be lit there.',
           'سب سے بڑی بات یہ ہے کہ امن کا اِرادہ اور عزم ہو اور ایک دیرپا حکمتِ عملی ہو۔ اگر کسی برادری میں اکثر لوگ یہ اِرادہ کریں کہ اپنے ماحول اور برادری کو بدامنی کی تاریکیوں سے نکالنا ہے تو کوئی وجہ نہیں کہ وہاں امن کے چراغ روشن نہ ہوں۔',
           'تر ټولو لویه خبره دا ده چې د سولې اراده او هوډ وي او یوه اوږدمهاله تګلاره وي. که په کومه ټولنه کې ډېری خلک دا اراده وکړي چې خپل چاپېریال او ټولنه باید د بدامنۍ له تیارو وباسي، نو هېڅ دلیل نشته چې هلته د سولې ډیوې بلې نه شي.')])
    r1 = rec(b, 6, 16, 70, [130])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.p('1. Fill in the blanks in the following sentences with suitable words:', '۱۔ درج ذیل جملوں کو مناسب الفاظ سے پُر کیجیے:', '۱. لاندې جملې په مناسبو کلمو ډکې کړئ:')
    e.group('lines', [('1. Political parties are the spokesmen of public wishes and ________ .', '۱۔ سیاسی جماعتیں عوامی خواہشات اور ________ کی ترجمان ہوتی ہیں۔', '۱. سیاسي ګوندونه د خلکو د هیلو او ________ ویاندویان وي.'),
                      ('2. The vote should always be given by looking at a party’s ________ or programme.', '۲۔ ووٹ ہمیشہ کسی جماعت کے ________ یا پروگرام کو دیکھ کر دینا چاہیئے۔', '۲. رایه باید تل د یوه ګوند ________ یا پروګرام ته په کتو ورکړل شي.'),
                      ('3. Modern social movements are now using modern technology and ________ .', '۳۔ جدید سماجی تحریکیں تو اب جدید ٹیکنالوجی اور ________ کو اِستعمال کر رہی ہیں۔', '۳. عصري ټولنیز غورځنګونه اوس عصري ټکنالوجي او ________ کاروي.'),
                      ('4. An independent judiciary alone plays an important role in the establishment of a ________ and welfare system.', '۴۔ آزاد عدلیہ ہی ________ و فلاحی نظام کے قیام میں اہم کردار ادا کرتی ہے۔', '۴. یوازې خپلواکه قضا د ________ او هوساینیز نظام په جوړولو کې مهم رول لوبوي.'),
                      ('5. People talk of rights but turn away from their ________ .', '۵۔ لوگ حقوق کی بات تو کرتے ہیں لیکن اپنے ________ سے روگردانی کرتے ہیں۔', '۵. خلک د حقونو خبره کوي، خو له خپلو ________ مخ اړوي.')])
    e.p('2. For the following questions, choose the suitable answer, i.e. (a), (b), (c) or (d), and write it in the box given against each question:', '۲۔ درج ذیل سوالات کے لیے موزوں جواب یعنی ا، ب، ج یا د منتخب کر کے ہر سوال کے سامنے دیئے گئے خالی خانے میں لکھیں:', '۲. د لاندې پوښتنو لپاره مناسب ځواب، یعنې الف، ب، ج یا د، وټاکئ او د هرې پوښتنې مخې ته په تش خونه کې یې ولیکئ:')
    e.mcq('1.', ('In July 1972 a peace agreement was made between India and Pakistan at ________ .', 'جولائی 1972ء میں ________ کے مقام پر بھارت اور پاکستان کے درمیان امن کا معاہدہ ہوا۔', 'د ۱۹۷۲ کال په جولای کې د ________ په ځای کې د هند او پاکستان ترمنځ د سولې تړون وشو.'),
          [('Shimla', 'شملہ', 'شمله'), ('Bombay', 'بمبئی', 'بمبۍ'), ('Agra', 'آگرہ', 'اګره'), ('Delhi', 'دہلی', 'ډهلي')], per_line=4)
    e.mcq('2.', ('For the extension of Karachi Steel Mills ________ provided one billion dollars.', 'کراچی سٹیل ملز میں توسیع کیلئے ________ نے ایک بلین ڈالر فراہم کئے۔', 'د کراچۍ سټیل ملز د پراختیا لپاره ________ یو میلیارد ډالر ورکړل.'),
          [('China', 'چین', 'چین'), ('Iran', 'ایران', 'ایران'), ('Mongolia', 'منگولیا', 'منګولیا'), ('Russia', 'روس', 'روسیه')], per_line=4)
    e.mcq('3.', ('The Muslim League government for the first time gave the State Bank of Pakistan ________ .', 'مسلم لیگ کی حکومت نے پہلی بار سٹیٹ بینک آف پاکستان کو ________ دی۔', 'د مسلم لیګ حکومت په لومړي ځل د پاکستان دولتي بانک ته ________ ورکړه.'),
          [('leave', 'چھٹی', 'رخصتي'), ('money', 'رقم', 'پیسې'), ('autonomy', 'خودمختاری', 'خپلواکي'), ('punishment', 'سزا', 'سزا')], per_line=4)
    e.mcq('4.', ('The media played a role to the point of perfection in the ________ of people in every field.', 'میڈیا نے ہر میدان میں لوگوں کی ________ میں کمال کی حد تک کردار ادا کیا۔', 'رسنیو په هر ډګر کې د خلکو په ________ کې د کمال تر حده رول ولوباوه.'),
          [('awakening', 'بیداری', 'ویښتیا'), ('hurting', 'دل آزاری', 'زړه‌ازاري'), ('misery', 'بدحالی', 'بدحالي'), ('difficulties', 'مشکلات', 'ستونزې')], per_line=4)
    e.mcq('5.', ('In society people will have to be taught tolerance, ________ and forbearance.', 'معاشرہ میں لوگوں کو برداشت، ________ اور رواداری کا درس دینا ہوگا۔', 'په ټولنه کې باید خلکو ته د زغم، ________ او رواداري درس ورکړل شي.'),
          [('awakening', 'بیداری', 'ویښتیا'), ('labour', 'محنت', 'زحمت'), ('acceptance', 'قبولیت', 'منل'), ('courage', 'ہمت', 'همت')], per_line=4)
    e.p('3. Mark the correct sentences as “correct” and the wrong sentences as “wrong”:', '۳۔ صحیح جملوں کو صحیح اور غلط جملوں کو غلط پر نشان لگائیں:', '۳. سمې جملې "سم" او ناسمې جملې "ناسم" په نښه کړئ:')
    e.group('lines', [
     ('1. There is no special difference between the constitutions of political parties and the national constitution.' + TF, '۱۔ سیاسی جماعتوں کے دساتیر اور ملکی دستور میں کوئی خاص فرق نہیں ہوتا۔' + TFU, '۱. د سیاسي ګوندونو د اساسنامو او د هېواد د اساسي قانون ترمنځ کوم ځانګړی توپیر نه وي.' + TFP),
     ('2. It is not necessary to see whether political parties acted upon most promises or not.' + TF, '۲۔ یہ دیکھنا ضروری نہیں کہ سیاسی جماعتوں نے اکثر وعدوں پر عمل کیا یا نہیں۔' + TFU, '۲. دا کتل اړین نه دي چې سیاسي ګوندونو پر ډېرو ژمنو عمل کړی که نه.' + TFP),
     ('3. For a stable political system the opposition is no less than deadly poison.' + TF, '۳۔ مستحکم سیاسی نظام کیلئے حزبِ اِختلاف زہرِ قاتل سے کم نہیں۔' + TFU, '۳. د باثباته سیاسي نظام لپاره اپوزیسیون له وژونکي زهر کم نه دی.' + TFP),
     ('4. Political parties and social movements are two names of one thing.' + TF, '۴۔ سیاسی جماعتیں اور سماجی تحاریک ایک چیز کے دو نام ہیں۔' + TFU, '۴. سیاسي ګوندونه او ټولنیز غورځنګونه د یوه شي دوه نومونه دي.' + TFP),
     ('5. Industrial development gave birth to many organisations and movements.' + TF, '۵۔ صنعتی ترقی نے کئی تنظیموں اور تحاریک کو جنم دیا۔' + TFU, '۵. صنعتي پرمختګ ډېر سازمانونه او غورځنګونه وزېږول.' + TFP),
     ('6. Pakistan, because of present world problems, is a victim of extremism.' + TF, '۶۔ پاکستان موجودہ عالمی مسائل کی وجہ سے اِنتہاپسندی کا شکار ہے۔' + TFU, '۶. پاکستان د اوسنیو نړیوالو ستونزو له امله د افراطیت ښکار دی.' + TFP),
     ('7. Problems are always solved with the gun.' + TF, '۷۔ مسائل ہمیشہ بندوق سے حل ہوتے ہیں۔' + TFU, '۷. ستونزې تل په ټوپک حلېږي.' + TFP)])
    r2 = BOOK.record(e, 'civ12-ch6-exercise-1', 'Chapter 6 exercise (1)', 'باب ۶: مشق (۱)', '۶ څپرکی: تمرین (۱)', 70, [130, 131])
    r2['sourceNote'] = 'The answer boxes and the “صحیح۔غلط” column are given as bracketed prompts.'
    BOOK.save(70, [(6, r1), (6, r2)], issues=[{'id': 'civ12-pdf070', 'unit': 6, 'printedPage': 131,
               'description': 'Q2(1)–(3) (Shimla, Karachi Steel Mills, State Bank autonomy) refer to material not in this chapter’s text. Retained as printed.'}])


def p71():
    e = Builder()
    e.p('4. Match the columns:', '۴۔ کالم ملائیں:', '۴. ستنې سره برابرې کړئ:')
    A = [('Political', 'سیاسی', 'سیاسي'), ('Public', 'عوامی', 'ولسي'), ('Emergency', 'ہنگامی', 'بیړنی'), ('Rights', 'حقوق', 'حقونه'), ('Social', 'سماجی', 'ټولنیز'), ('Military', 'فوجی', 'پوځي'), ('Democratic', 'جمہوری', 'ډیموکراټیک'), ('Extreme (intiha)', 'اِنتہا', 'افراط')]
    B = [('Psychology', 'نفسیات', 'ارواپوهنه'), ('Change', 'تغیر', 'بدلون'), ('Dictatorship', 'آمریت', 'دیکتاتوري'), ('Consciousness', 'شعور', 'پوهاوی'), ('-ism (pasandi)', 'پسندی', 'پالنه'), ('Culture', 'ثقافت', 'کلتور'), ('and duties', 'وفرائض', 'او مکلفیتونه'), ('Conditions', 'حالات', 'حالات')]
    e.table('civ12-ch6-match', ['Column A', 'Column B'], [[a[0], b[0]] for a, b in zip(A, B)], ['کالم۔الف', 'کالم۔ب'], ['ستن الف', 'ستن ب'],
            [[a[1], b[1]] for a, b in zip(A, B)], [[a[2], b[2]] for a, b in zip(A, B)])
    e.p('5. Give short answers to the following questions:', '۵۔ درج ذیل سوالات کے مختصر جواب دیں:', '۵. د لاندې پوښتنو لنډ ځوابونه ورکړئ:')
    e.group('lines', [('1. Define a political party.', '۱۔ سیاسی جماعت کی تعریف کریں۔', '۱. سیاسي ګوند تعریف کړئ.'),
                      ('2. On what basis should the vote be given?', '۲۔ ووٹ کس بنیاد پر دینا چاہیئے؟', '۲. رایه باید پر کوم بنسټ ورکړل شي؟'),
                      ('3. What is meant by military dictatorship?', '۳۔ فوجی آمریت سے کیا مراد ہے؟', '۳. له پوځي دیکتاتورۍ څخه څه مراد دی؟'),
                      ('4. Define a social movement.', '۴۔ سماجی تحریک کی تعریف کریں۔', '۴. ټولنیز غورځنګ تعریف کړئ.'),
                      ('5. State some kinds of social movements.', '۵۔ سماجی تحریکوں کے چند اقسام بیان کریں۔', '۵. د ټولنیزو غورځنګونو څو ډولونه بیان کړئ.')])
    e.p('6. Write the answers of the following questions in detail:', '۶۔ درج ذیل سوالات کے جواب تفصیل سے تحریر کریں:', '۶. د لاندې پوښتنو ځوابونه په تفصیل ولیکئ:')
    e.group('lines', [('1. State the role of political parties in the stability of democracy in Pakistan.', '۱۔ پاکستان میں جمہوریت کے اِستحکام میں سیاسی جماعتوں کا کردار بیان کیجیے۔', '۱. په پاکستان کې د ډیموکراسۍ په ثبات کې د سیاسي ګوندونو رول بیان کړئ.'),
                      ('2. Review the government of any one political party in the light of its manifesto.', '۲۔ کسی ایک سیاسی جماعت کے حکومت کا اُسکے منشور کی روشنی میں جائزہ لیں۔', '۲. د یوه سیاسي ګوند حکومت د هغه د منشور په رڼا کې وڅېړئ.'),
                      ('3. Write a detailed note on the structure and organisation of political parties.', '۳۔ سیاسی جماعتوں کی ساخت اور تنظیم پر تفصیلی نوٹ تحریر کریں۔', '۳. د سیاسي ګوندونو پر جوړښت او تنظیم تفصیلي یادښت ولیکئ.'),
                      ('4. Make clear the importance of social movements in making Pakistan an Islamic, democratic and welfare state.', '۴۔ پاکستان کو بطورِ اِسلامی، جمہوری اور فلاحی ریاست بنانے میں سماجی تحاریک کی اہمیت واضح کیجیے۔', '۴. د پاکستان د اسلامي، ډیموکراټیک او هوساینیز دولت په توګه جوړولو کې د ټولنیزو غورځنګونو اهمیت روښانه کړئ.'),
                      ('5. State the factors which became the cause of the start of social movements.', '۵۔ وہ عوامل بیان کریں جو سماجی تحاریک کے آغاز کا سبب بنے۔', '۵. هغه لاملونه بیان کړئ چې د ټولنیزو غورځنګونو د پیل لامل شول.'),
                      ('6. Present proposals for the promotion of peace at the local level.', '۶۔ مقامی سطح پر امن کے فروغ کیلئے تجاویز پیش کریں۔', '۶. په سیمه‌ییزه کچه د سولې د پراختیا لپاره وړاندیزونه وړاندې کړئ.')])
    e.h('Practical activities:', 'عملی سرگرمیاں:', 'عملي فعالیتونه:')
    e.group('lines', [('1. Arrange a quiz on this chapter.', '۱۔ اِسی باب میں کوئز کا اہتمام کریں۔', '۱. پر دې څپرکي د پوښتنو ځوابونو سیالي جوړه کړئ.'),
                      ('2. Hold a speech competition on the merits and demerits of political parties in Pakistan.', '۲۔ پاکستان میں سیاسی جماعتوں کے فوائد و نقائص پر تقریری مقابلہ منعقد کریں۔', '۲. په پاکستان کې د سیاسي ګوندونو پر ګټو او نیمګړتیاوو د وینا سیالي جوړه کړئ.'),
                      ('3. Making groups in the class, make charts containing the important points of the manifestos of different political parties.', '۳۔ کلاس میں گروپ بنا کر مختلف سیاسی جماعتوں کے منشور کے اہم نکات پر مشتمل چارٹ بنائیں۔', '۳. په ټولګي کې ډلې جوړې کړئ او د بېلابېلو سیاسي ګوندونو د منشورونو د مهمو ټکو چارټونه جوړ کړئ.')])
    ex = BOOK.record(e, 'civ12-ch6-exercise-2', 'Chapter 6 exercise (2)', 'باب ۶: مشق (۲)', '۶ څپرکی: تمرین (۲)', 71, [132, 133])
    ex['sourceNote'] = 'The match-the-columns lists are reproduced as a two-column table in the printed order (not matched).'
    BOOK.save(71, [(6, ex)], complete_units=[6], issues=[{'id': 'civ12-pdf071', 'unit': 6, 'printedPage': 132,
               'description': 'Q6(2) “کسی ایک سیاسی جماعت کے حکومت”; activity 1 “اِسی باب میں کوئز”. The page edge of p.132 shows stray numerals “1”, “2” from an adjacent sheet, excluded. Retained as printed.'}])


def p72():
    b = Builder()
    b.h('Chapter 7: Peace and Diversity', 'باب ۷: امن اور تنوع (Peace and Diversity)', '۷ څپرکی: سوله او تنوع')
    b.h('Teaching objectives', 'تدریسی مقاصد', 'د تدریس موخې')
    b.p('After the study of this chapter the students will be able to:', 'اِس باب کے مطالعہ کے بعد طلبہ اِس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    b.group('lines', [
     ('1. define the word “peace”.', '۱۔ لفظ ’امن‘ کی تعریف کر سکیں۔', '۱. د "سولې" کلمه تعریف کړي.'),
     ('2. explain the importance of a peaceful society.', '۲۔ ایک پرامن معاشرہ کے اہمیت کی وضاحت کر سکیں۔', '۲. د یوې سوله‌ییزې ټولنې اهمیت روښانه کړي.'),
     ('3. identify the characteristics of a peaceful society.', '۳۔ ایک پرامن معاشرہ کے خصوصیات کی نشاندہی کر سکیں۔', '۳. د یوې سوله‌ییزې ټولنې ځانګړنې وپېژني.'),
     ('4. identify the causes of conflicts and wars at the local, national and world level.', '۴۔ مقامی، قومی اور عالمی سطح پر تنازعات اور جنگوں کے وجوہات کی نشاندہی کر سکیں۔', '۴. په سیمه‌ییزه، ملي او نړیواله کچه د شخړو او جګړو لاملونه وپېژني.'),
     ('5. identify the results of conflicts and wars at the local, national and world level.', '۵۔ مقامی، قومی اور عالمی سطح پر تنازعات اور جنگوں کے نتائج کی نشاندہی کر سکیں۔', '۵. په سیمه‌ییزه، ملي او نړیواله کچه د شخړو او جګړو پایلې وپېژني.'),
     ('6. identify those groups which are most affected by conflicts and wars at the local, national and world level.', '۶۔ اُن گروہوں کی نشاندہی کر سکیں جو مقامی، قومی اور عالمی سطح پر تنازعات اور جنگوں سے سب سے زیادہ متاثر ہوتے ہیں۔', '۶. هغه ډلې وپېژني چې په سیمه‌ییزه، ملي او نړیواله کچه له شخړو او جګړو تر ټولو ډېرې اغېزمنې کېږي.'),
     ('7. define these words: discrimination, diversity, prejudice, stereotype and scapegoating.', '۷۔ اِن الفاظ کے تعریف کر سکیں: اِمتیازات، تنوع، تعصب، سٹیریو ٹائپ اور قربانی کا بکرا بنانا۔', '۷. دا کلمې تعریف کړي: تبعیض، تنوع، تعصب، کلیشه (سټیریوټایپ) او قرباني وزه جوړول.'),
     ('8. state the prominent features of diverse societies.', '۸۔ متنوع معاشروں کے نمایاں خدوخال بیان کر سکیں۔', '۸. د متنوعو ټولنو څرګندې ځانګړنې بیان کړي.'),
     ('9. identify the problems of diversity in Pakistani society.', '۹۔ پاکستانی سماج میں تنوع کے مسائل کی نشاندہی کر سکیں۔', '۹. په پاکستاني ټولنه کې د تنوع ستونزې وپېژني.'),
     ('10. identify the parts of different cultures, values and beliefs in our lives and our society.', '۱۰۔ ہماری زندگیوں اور ہمارے معاشرہ میں مختلف ثقافتوں، اقدار اور عقائد کے حصوں کی نشاندہی کر سکیں۔', '۱۰. زموږ په ژوند او ټولنه کې د بېلابېلو کلتورونو، ارزښتونو او عقایدو برخې وپېژني.'),
     ('11. distinguish between Pakistani and world cultures with reference to diversity.', '۱۱۔ تنوع کے حوالے سے پاکستانی اور عالمی ثقافتوں میں فرق کر سکیں۔', '۱۱. د تنوع په اړه د پاکستاني او نړیوالو کلتورونو ترمنځ توپیر وکړي.'),
     ('12. identify those methods through which world diversity can be strengthened.', '۱۲۔ اُن طریقوں کی نشاندہی کر سکیں جن کے ذریعے عالمی تنوع کو مضبوط بنایا جا سکے۔', '۱۲. هغه لارې وپېژني چې له لارې یې نړیوال تنوع پیاوړی کېدای شي.'),
     ('13. identify the ways of value diversity in Pakistan.', '۱۳۔ پاکستان میں اقداری تنوع کے طریقوں کی نشاندہی کر سکیں۔', '۱۳. په پاکستان کې د ارزښتي تنوع لارې وپېژني.'),
     ('14. identify those components of a way of life which become the cause of promoting diversity and tolerance in society.', '۱۴۔ ایک طرزِ حیات کے اُن اجزاء کی نشاندہی کر سکیں جو معاشرہ میں تنوع اور رواداری کے فروغ کا باعث بنتے ہیں۔', '۱۴. د ژوند د یوې طریقې هغه برخې وپېژني چې په ټولنه کې د تنوع او رواداري د پراختیا لامل کېږي.')])
    r1 = rec(b, 7, 1, 72, [134], first=True)
    t = Builder()
    t.h('Peace', 'امن (Peace)', 'سوله')
    P(t, [('Peace is called the opposite of war, and its different definitions are somewhat as follows:', 'امن جنگ کی ضد کو کہا جاتا ہے اور اِس کے مختلف تعاریف کچھ اِس طرح ہیں:', 'سوله د جګړې ضد ته ویل کېږي او بېلابېل تعریفونه یې څه داسې دي:')])
    t.group('lines', [
     ('1. According to the Encarta Encyclopedia, “Peace is the name of freedom from war or conflict, a condition free from noise and chaos, and non-violence and absence of chaos in the country.”', '۱۔ اِنکارٹا اِنسائیکلوپیڈیا کے مطابق ”امن جنگ یا تنازعہ سے آزادی، شور اور افراتفری سے پاک کیفیت اور ملک میں عدم تشدد و عدم افراتفری کا نام ہے۔“', '۱. د انکارټا پوهنغونډ په وینا: "سوله له جګړې یا شخړې ازادي، له شور او ګډوډۍ پاک حالت او په هېواد کې د تاوتریخوالي او ګډوډۍ نشتوالي نوم دی."'),
     ('2. According to the Advanced Oxford Dictionary, “Peace is called the condition free from anxiety, noise and chaos.”', '۲۔ ایڈوانس آکسفورڈ ڈکشنری کے مطابق ”امن اِضطراب، شور اور افراتفری سے آزاد حالت کو کہا جاتا ہے۔“', '۲. د اډوانس اکسفورډ قاموس په وینا: "سوله له اضطراب، شور او ګډوډۍ ازاد حالت ته ویل کېږي."'),
     ('3. According to Chambers Advanced Practical Dictionary, “Peace is the name of the condition of reconciliation, calm, safety and contentment.”', '۳۔ چم ایڈوانس پریکٹیکل ڈکشنری کے مطابق ”امن صلح، سکون، سلامتی اور آسودگی کی کیفیت کا نام ہے۔“', '۳. د چیمبرز اډوانس پرکټیکل قاموس په وینا: "سوله د پخلاینې، ارامۍ، سلامتۍ او سوکالۍ د حالت نوم دی."')])
    P(t, [('War and violence are inhuman acts, and causing harm to anyone’s life and property through them is an immoral activity. In history the concept of peace has always been connected with ethics, divine will and economic and social utility. No moral code or religion wants unrest. The majority of people desire peace.',
           'جنگ اور تشدد غیر اِنسانی افعال ہیں اور اِن کے ذریعے کسی کے جان و مال کو نقصان پہنچانا غیر اخلاقی سرگرمی ہے۔ تاریخ میں امن کا تصور ہمیشہ اخلاقیات، خدائی مرضی اور اقتصادی و سماجی افادیت سے منسلک رہا ہے۔ کوئی اخلاقی ضابطہ یا مذہب بدامنی نہیں چاہتا۔ لوگوں کی اکثریت امن کی خواہشمند ہوتی ہے۔',
           'جګړه او تاوتریخوالی غیر انساني کړنې دي او د دوی له لارې د چا ځان او مال ته زیان رسول غیر اخلاقي فعالیت دی. په تاریخ کې د سولې تصور تل له اخلاقو، الهي ارادې او اقتصادي او ټولنیزې ګټورتیا سره تړلی پاتې شوی. هېڅ اخلاقي ضابطه یا دین بدامني نه غواړي. د خلکو اکثریت د سولې غوښتونکی وي.'),
          ('A big cause of unrest in the countries of the Third World is that some individuals or groups use force illegally, although according to the constitution and law the authority to use force belongs only to government institutions. However the government too should not use force without need. Governmental power should be used only in such circumstances when national or collective interests demand it.',
           'تیسری دُنیا کی ممالک میں بدامنی کا ایک بڑا سبب یہ ہے کہ بعض افراد یا گروہ غیر قانونی طور پر طاقت کا اِستعمال کرتے ہیں حالانکہ آئین اور قانون کی رو سے طاقت کے اِستعمال کا اِختیار صرف سرکاری اِداروں کو حاصل ہے۔ تاہم حکومت کو بھی بلاضرورت طاقت کا اِستعمال نہیں کرنا چاہیئے۔ صرف ایسے حالات میں حکومتی طاقت اِستعمال کی جائے جب قومی یا اِجتماعی مفادات اِس کا تقاضا کریں۔',
           'د درېیمې نړۍ په هېوادونو کې د بدامنۍ یو لوی لامل دا دی چې ځینې کسان یا ډلې په غیر قانوني ډول ځواک کاروي، سره له دې چې د اساسي قانون او قانون له مخې د ځواک د کارونې واک یوازې دولتي ادارو ته دی. خو حکومت هم باید بې‌اړتیا ځواک ونه کاروي. حکومتي ځواک دې یوازې په داسې حالاتو کې وکارول شي چې ملي یا ټولیزې ګټې یې غوښتنه وکړي.')])
    t.h('Importance of Peaceful Society', 'پُرامن معاشرے کی اہمیت (Importance of Peaceful Society)', 'د سوله‌ییزې ټولنې اهمیت')
    P(t, [('The basic purpose of human society, state and government and law is the establishment of peace. Before the establishment of social life and institutions there was unrest. There was no calm in man’s life. Difficulties and lawlessness had made life miserable. If studied carefully, social life came into being to face human difficulties, dangers and troubles, which first of all …',
           'اِنسانی معاشرہ، ریاست و حکومت اور قانون کا بنیادی مقصد امن کا قیام ہے۔ معاشرتی زندگی و اِداروں کے قیام سے پہلے بدامنی تھی۔ اِنسان کی زندگی میں سکون نہیں تھا۔ مشکلات اور لاقانونیت نے زندگی اجیرن بنا رکھی تھی۔ اگر بغور مطالعہ کیا جائے تو اِنسانی مشکلات و خطرات اور پریشانیوں کا مقابلہ کرنے کیلئے معاشرتی زندگی وجود پذیر ہوئی جس نے سب سے …',
           'د انساني ټولنې، دولت او حکومت او قانون بنسټیزه موخه د سولې ټینګول دي. د ټولنیز ژوند او ادارو له جوړېدو مخکې بدامني وه. د انسان په ژوند کې ارامي نه وه. ستونزو او بې‌قانونۍ ژوند ستونزمن کړی و. که په غور مطالعه وشي، د انساني ستونزو، خطرونو او کړاوونو سره د مقابلې لپاره ټولنیز ژوند رامنځته شو چې تر ټولو …')])
    r2 = rec(t, 7, 2, 72, [135])
    BOOK.save(72, [(7, r1), (7, r2)], issues=[{'id': 'civ12-pdf072', 'unit': 7, 'printedPage': 135,
               'description': 'p.134 objectives 2, 3, 4, 7 use “کے” for “کی” (“معاشرہ کے اہمیت”, “جنگوں کے وجوہات”, “الفاظ کے تعریف”); p.135 “چم ایڈوانس پریکٹیکل ڈکشنری” (Chambers), “اِس کے مختلف تعاریف”, “تیسری دُنیا کی ممالک”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 70
    {70: p70, 71: p71, 72: p72}[n]()
