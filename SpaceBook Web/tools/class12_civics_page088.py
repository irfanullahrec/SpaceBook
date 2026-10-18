"""Civics XII PDF88–90: pp.166–171 — disaster management (end), planning for disaster management, activities; chapter 8 exercise;
glossary of special terms (begins, pp.170–171). Run: python class12_civics_page088.py N (88–90)."""
import sys
from class12_civics_common import BOOK, Builder, rec, P

BM = 'BM'
GLOSS_T = ('Glossary', 'مخصوص اِصطلاحات', 'ځانګړې اصطلاحګانې')


def p88():
    b = Builder()
    P(b, [('… is decision-making in the least time. In this way there should be planning for disaster management. In disaster management a reaction has to be made to events taking place. For example, in an oil factory the possibilities of fire are greater, so the company should have a plan to deal with it; but when a tragedy of this kind arises, the strength of the fire, public opinion and the cost of control may be much more than expectations.',
           'از کم وقت میں فیصلہ سازی ہے۔ اِس طرح سانحات کے اِنتظام کیلئے منصوبہ سازی ہونی چاہیئے۔ سانحات کے اِنتظام میں وقوع پذیر ہونے والے واقعات کا ردِعمل کرنا پڑتا ہے۔ مثال کے طور پر تیل کے ایک کارخانے میں آتش زنی کے اِمکانات زیادہ ہوتے ہیں لہٰذا اِس سے نمٹنے کیلئے کمپنی کے پاس (ایک) منصوبہ ہونا چاہیئے لیکن جب اِس قسم کا سانحہ پیدا ہوتا ہے تو آتش زنی کی طاقت، رائے عامہ اور قابو پانے کا خرچہ توقعات سے کہیں زیادہ بھی ہو سکتا ہے۔',
           '… په لږ تر لږه وخت کې پرېکړه کول دي. په دې ډول د ناورینونو د مدیریت لپاره پلان جوړونه پکار ده. د ناورینونو په مدیریت کې پېښېدونکو پېښو ته غبرګون ښودل پکار وي. د بېلګې په توګه د تېلو په یوه فابریکه کې د اور لګېدو امکانات ډېر وي، نو د مقابلې لپاره باید کمپنۍ یو پلان ولري؛ خو کله چې داسې ناورین پېښ شي، د اور زور، عامه رایه او د کنټرول لګښت له تمې ډېر زیات هم کېدای شي.')])
    b.h('Plan for Disaster Management', 'سانحات کے اِنتظام کیلئے منصوبہ:', 'د ناورینونو د مدیریت پلان')
    P(b, [('The best management is that in which, besides reducing dangers, there are also abilities, i.e. it should have this ability that the greatest possible opportunities of betterment be provided to affected people. Those who make plans keep both these aspects of disaster management in view. Planning for disaster management is an art. The workers who work in it should not be ordinary people; rather they should have obtained skill in dealing with disasters, and this skill is obtained through observation, study and experience. The plan for disaster management is a documentary programme. It includes all those possible activities which have to be performed during and after the occurrence of the crisis. During the tragedy the selected team gets engaged in its assigned activities and provides the opportunities to reduce losses to the minimum and to give the affected the maximum (help). Whatever kind of tragedy occurs, according to the plan the assigned team has to take the following steps:',
           'بہترین اِنتظام وہ ہے جس میں خطرات کم کرنے کے علاوہ اور صلاحیتیں بھی ہوں۔ یعنی اِس میں یہ صلاحیت ہو کہ متاثرہ لوگوں کو بہتری کے زیادہ سے زیادہ مواقع فراہم کئے جائیں۔ منصوبہ بنانے والے سانحات کے اِنتظام کے اِن دونوں پہلوؤں کو مدِنظر رکھتے ہیں۔ سانحات کے اِنتظام کی منصوبہ سازی ایک فن ہے۔ اِس میں کام کرنے والے کارکنان عام لوگ نہ ہوں بلکہ انہیں سانحات سے نمٹنے کی مہارت حاصل ہو اور یہ مہارت مشاہدے، مطالعے اور تجربے سے حاصل ہوتی ہے۔ سانحات کے اِنتظام کا منصوبہ ایک دستاویزی پروگرام ہوتا ہے۔ اِس میں وہ تمام ممکنہ سرگرمیاں شامل ہوتی ہیں جنہیں بحران وقوع پذیر ہونے کے دوران اور اِسکے بعد ادا کرنا ہوتے ہیں۔ سانحے کے دوران منتخب ٹیم اپنی مقررہ سرگرمیوں میں لگ جاتی ہے اور نقصانات کو کم سے کم اور متاثرین کو زیادہ سے زیادہ مواقع فراہم کرتی ہے۔ جس نوعیت کا سانحہ وقوع پذیر ہو تو منصوبہ کے مطابق مقررہ ٹیم کو درج ذیل اِقدامات اُٹھانے پڑتے ہیں:',
           'غوره مدیریت هغه دی چې پکې د خطرونو له کمولو سربېره نورې وړتیاوې هم وي، یعنې دا وړتیا ولري چې اغېزمنو خلکو ته د ښه والي ډېر فرصتونه برابر کړي. پلان جوړوونکي د ناورینونو د مدیریت دا دواړه اړخونه په پام کې نیسي. د ناورینونو د مدیریت پلان جوړونه یو هنر دی. په کې کار کوونکي باید عام خلک نه وي، بلکې د ناورینونو سره د مقابلې مهارت ولري او دا مهارت د کتنې، مطالعې او تجربې له لارې ترلاسه کېږي. د ناورینونو د مدیریت پلان یو سندي پروګرام وي. په کې ټول هغه شوني فعالیتونه شامل وي چې د بحران د پېښېدو پر مهال او وروسته یې ترسره کول وي. د ناورین پر مهال ټاکل شوې ډله په خپلو ټاکلو فعالیتونو بوختېږي او زیانونه تر ټولو کم او اغېزمنو ته ډېر فرصتونه برابروي. هر ډول ناورین چې پېښ شي، د پلان سره سم ټاکل شوې ډله باید دا ګامونه پورته کړي:')])
    b.group('lines', [
     ('• To take up one’s responsibility and position quickly …', '• … جلدی سے اپنی ذمہ داری اور جگہ سنبھال لینا …', '• … په چټکۍ خپل مسؤلیت او ځای ونیول …'),
     ('• … to determine the facts …', '• … حقائق کا تعین کرنا …', '• … د حقایقو ټاکل …'),
     ('• … to state one’s position …', '• … اپنا مؤقف بیان کرنا …', '• … د خپل دریځ بیانول …'),
     ('• … to get control of the problem …', '• … مسئلہ پر قابو پانا …', '• … پر ستونزه کنټرول ترلاسه کول …')])
    P(b, [('In this way, when all the members of the team pass through these activities, the tragedy comes under control in a good way. The slogan of dealing with disasters is “to remain prepared”. Preparation should not be for one kind of tragedy only; rather in the plan there should be the ability to deal with every kind of tragedy. In planning, preparation and the action of dealing, the presence of responsible people is necessary so that orders may be issued on the spot and money may be provided. In a good plan, to give answers to questions like what, when, why, where, for whom and who …',
           'اِس طرح ٹیم کے تمام اراکان جب اِن سرگرمیوں سے گزرتے ہیں تو سانحہ اچھے طریقے سے قابو میں آ جاتا ہے۔ سانحات سے نمٹنے کا نعرہ ’تیار رہنا‘ ہے۔ تیاری ایک ہی قسم کے سانحے کیلئے نہ ہو بلکہ منصوبہ میں ہر قسم کے سانحات سے نمٹنے کی صلاحیت ہونی چاہیئے۔ منصوبہ بندی، تیاری اور نمٹنے کی کارروائی میں ذمہ دار لوگوں کی موجودگی ضروری ہے تاکہ موقع پر احکامات جاری کئے جا سکیں اور رقم مہیا کی جا سکے۔ ایک اچھے منصوبے میں کیا، کب، کیوں، کہاں، کس کیلئے اور کون جیسے سوالات …',
           'په دې ډول کله چې د ډلې ټول غړي له دې فعالیتونو تېر شي، ناورین په ښه ډول کنټرولېږي. د ناورینونو سره د مقابلې شعار "چمتو اوسېدل" دی. چمتووالی دې یوازې د یوه ډول ناورین لپاره نه وي، بلکې په پلان کې دې د هر ډول ناورین سره د مقابلې وړتیا وي. په پلان جوړونې، چمتووالي او د مقابلې په کړنه کې د مسؤلو کسانو شتون اړین دی ترڅو په ځای حکمونه صادر او پیسې برابرې شي. په یوه ښه پلان کې د څه، کله، ولې، چېرته، د چا لپاره او څوک په څېر پوښتنو …')])
    r1 = rec(b, 8, 10, 88, [166], note='Most of p.166 is overprinted by mirrored ghost text from the reverse page; the four action points after “درج ذیل اِقدامات اُٹھانے پڑتے ہیں” are only partly legible and are given as the readable fragments.')
    t = Builder()
    P(t, [('… good and suitable roles are needed. The collection of these roles becomes the managing team.',
           'کے جوابات دینے کیلئے اچھے اور مناسب کرداروں کی ضرورت ہوتی ہے۔ اِن کرداروں کا مجموعہ اِنتظام کرنے والی ٹیم بن جاتی ہے۔',
           '… ځوابونو ورکولو لپاره ښو او مناسبو رولونو ته اړتیا وي. د دې رولونو ټولګه مدیریت کوونکې ډله جوړېږي.')])
    t.h('Activities', 'سرگرمیاں:', 'فعالیتونه')
    t.group('lines', [('1. Make such a plan as can effectively rehabilitate people who have been victims of accidents.', '۱۔ ایک ایسا منصوبہ بنائیے جو حادثات کے شکار لوگوں کی دوبارہ بحالی کو مؤثر بنا سکے۔', '۱. داسې یو پلان جوړ کړئ چې د پېښو ځپلو خلکو بیا رغونه اغېزمنه کړي.'),
                      ('2. Plan a management campaign to deal with a disaster, and include in it the community, civil defence and volunteers etc.', '۲۔ سانحہ سے نمٹنے کیلئے اِنتظامی مہم کی منصوبہ بندی کریں اور اِس میں کمیونٹی، شہری دفاع اور رضاکاروں وغیرہ کو شامل کریں۔', '۲. له ناورین سره د مقابلې لپاره د مدیریت کمپاین پلان جوړ کړئ او ټولنه، ملکي دفاع او رضاکاران پکې شامل کړئ.')])
    r2 = rec(t, 8, 11, 88, [167])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.p('1. Fill in the blanks in the following sentences with suitable words:', '۱۔ درج ذیل جملوں میں خالی جگہوں کو مناسب الفاظ سے پُر کریں:', '۱. په لاندې جملو کې تش ځایونه په مناسبو کلمو ډک کړئ:')
    e.group('lines', [('1. The process of learning through simulation plays an important role in ________ .', '۱۔ تلبیس کے ذریعے سیکھنے کا عمل ________ میں اہم کردار ادا کرتا ہے۔', '۱. د سیمولېشن له لارې د زده‌کړې بهیر په ________ کې مهم رول لوبوي.'),
                      ('2. The important purpose of a signature campaign is to create ________ and feeling among people.', '۲۔ دستخطی مہم کا اہم مقصد لوگوں میں ________ اور اِحساس پیدا کرنا ہے۔', '۲. د لاسلیک کمپاین مهمه موخه په خلکو کې ________ او احساس پیدا کول دي.'),
                      ('3. During a tragedy the selected team gets engaged in its assigned ________ .', '۳۔ سانحہ کے دوران منتخب ٹیم اپنی مقررہ ________ میں لگ جاتے ہیں۔', '۳. د ناورین پر مهال ټاکل شوې ډله په خپلو ټاکلو ________ بوختېږي.'),
                      ('4. Some people can be put in community service as ________ .', '۴۔ بعض لوگوں کو ________ کے طور پر کمیونٹی سروس میں لگایا جا سکتا ہے۔', '۴. ځینې خلک د ________ په توګه په ټولنیز خدمت ګمارل کېدای شي.'),
                      ('5. In the action of planning and dealing, the presence of ________ people is necessary.', '۵۔ منصوبہ سازی اور نمٹنے کی کارروائی میں ________ لوگوں کی موجودگی ضروری ہے۔', '۵. د پلان جوړونې او مقابلې په کړنه کې د ________ کسانو شتون اړین دی.')])
    ex = BOOK.record(e, 'civ12-ch8-exercise-1', 'Chapter 8 exercise (1)', 'باب ۸: مشق (۱)', '۸ څپرکی: تمرین (۱)', 88, [167])
    BOOK.save(88, [(8, r1), (8, r2), (8, ex)], issues=[{'id': 'civ12-pdf088', 'unit': 8, 'printedPage': 166,
               'description': 'p.166 is overprinted by mirrored ghost text from the reverse page (worst on the lower half); upright text was read at high magnification, and where the list of steps is illegible only the readable fragments are given. A handwritten owner note in the margin of p.166 is excluded. “اراکان”, “ادا کرنا ہوتے ہیں”; p.167 Q1(3) “منتخب ٹیم … لگ جاتے ہیں”. Retained as printed.'}])


def p89():
    e = Builder()
    e.p('2. For the following questions, choose the suitable answer, i.e. (a), (b), (c) or (d), and write it in the empty box given against each question:', '۲۔ درج ذیل سوالات کے لیے موزوں جواب یعنی ا، ب، ج یا د منتخب کر کے ہر سوال کے سامنے دیئے گئے خالی خانے میں لکھیں۔', '۲. د لاندې پوښتنو لپاره مناسب ځواب، یعنې الف، ب، ج یا د، وټاکئ او د هرې پوښتنې مخې ته په تش خونه کې یې ولیکئ.')
    e.mcq('1.', ('In Canada a ________ simulation programme has been started.', 'کینیڈا میں ________ تلبیس پروگرام کا آغاز کیا گیا ہے۔', 'په کاناډا کې د ________ سیمولېشن پروګرام پیل شوی.'),
          [('emergency', 'ہنگامی', 'بیړنی'), ('examination', 'اِمتحانی', 'ازموینیز'), ('real', 'اصلی', 'اصلي'), ('annual', 'سالانہ', 'کلنی')], per_line=4)
    e.mcq('2.', ('In public service messages one’s address or telephone number can be included for further ________ .', 'عوامی خدمت کے پیغامات میں مزید ________ کیلئے اپنا پتہ یا ٹیلی فون نمبر شامل کیا جا سکتا ہے۔', 'د عامه خدمت په پیغامونو کې د لا ________ لپاره خپل پته یا د ټیلیفون شمېره شاملېدای شي.'),
          [('cleanliness', 'صفائی', 'پاکوالی'), ('refinement', 'نکھار', 'ښکلا'), ('complexity', 'پیچیدگی', 'پېچلتیا'), ('information', 'معلومات', 'معلومات')], per_line=4)
    e.mcq('3.', ('In a signature campaign people are ________ face to face.', 'دستخطی مہم میں بالمشافہ لوگوں کو ________ جاتا ہے۔', 'د لاسلیک په کمپاین کې خلکو ته مخامخ ________ .'),
          [('shown', 'دکھایا', 'ښودل کېږي'), ('misled', 'ورغلایا', 'غولول کېږي'), ('explained to', 'سمجھایا', 'پوهول کېږي'), ('fed', 'کھلایا', 'خوړل کېږي')], per_line=4)
    e.mcq('4.', ('Community service is generally a ________ activity.', 'کمیونٹی سروس عموماً ایک ________ سرگرمی ہے۔', 'ټولنیز خدمت عموماً یو ________ فعالیت دی.'),
          [('useless', 'بے کار', 'بې‌کاره'), ('volunteer', 'رضاکار', 'رضاکارانه'), ('government', 'سرکاری', 'دولتي'), ('easy', 'آسان', 'اسانه')], per_line=4)
    e.mcq('5.', ('The ________ of dealing with a disaster is “to remain prepared”.', 'سانحہ سے نمٹنے کا ________ ”تیار رہنا ہے“۔', 'د ناورین سره د مقابلې ________ "چمتو اوسېدل" دی.'),
          [('prayer', 'دُعا', 'دعا'), ('ability', 'صلاحیت', 'وړتیا'), ('key', 'کُنجی', 'کیلي'), ('slogan', 'نعرہ', 'شعار')], per_line=4)
    e.p('3. Match the columns:', '۳۔ کالم ملائیں:', '۳. ستنې سره برابرې کړئ:')
    A = [('Durable', 'پائیدار', 'دوامداره'), ('Active', 'فعال', 'فعال'), ('Media', 'میڈیا', 'رسنۍ'), ('Plan', 'منصوبہ', 'پلان'), ('Documentary', 'دستاویزی', 'سندي'), ('Emergency', 'ہنگامی', 'بیړنی'), ('Natural', 'قدرتی', 'طبیعي')]
    B = [('Campaign', 'مہم', 'کمپاین'), ('-making (sazi)', 'سازی', 'جوړونه'), ('Programme', 'پروگرام', 'پروګرام'), ('Rehabilitation', 'بحالی', 'بیا رغونه'), ('Disasters', 'آفات', 'افتونه'), ('Citizenship', 'شہریت', 'تابعیت'), ('Situation', 'صورتِ حال', 'حالت')]
    e.table('civ12-ch8-match', ['Column A', 'Column B'], [[a[0], b[0]] for a, b in zip(A, B)], ['کالم۔الف', 'کالم۔ب'], ['ستن الف', 'ستن ب'],
            [[a[1], b[1]] for a, b in zip(A, B)], [[a[2], b[2]] for a, b in zip(A, B)])
    e.p('4. Give short answers to the following questions:', '۴۔ درج ذیل سوالات کے مختصر جواب پیش کیجیے:', '۴. د لاندې پوښتنو لنډ ځوابونه وړاندې کړئ:')
    e.group('lines', [('1. Why is learning done through simulation?', '۱۔ تلبیس کے ذریعے کیوں سیکھا جاتا ہے؟', '۱. ولې د سیمولېشن له لارې زده‌کړه کېږي؟'),
                      ('2. Through which means are messages of public service presented?', '۲۔ عوامی خدمت کے پیغام کن ذرائع سے پیش کئے جاتے ہیں؟', '۲. د عامه خدمت پیغامونه د کومو وسیلو له لارې وړاندې کېږي؟'),
                      ('3. Write the important benefits of a signature campaign.', '۳۔ دستخطی مہم کے اہم فوائد تحریر کریں۔', '۳. د لاسلیک کمپاین مهمې ګټې ولیکئ.'),
                      ('4. Give an example of a signature campaign.', '۴۔ دستخطی مہم کی مثال دیجیے۔', '۴. د لاسلیک کمپاین بېلګه ورکړئ.'),
                      ('5. Explain conscious and unconscious disasters.', '۵۔ شعوری اور لاشعوری سانحات کی وضاحت کریں۔', '۵. شعوري او ناشعوري ناورینونه روښانه کړئ.')])
    e.p('5. Write detailed answers to the following questions:', '۵۔ درج ذیل سوالات کے تفصیلی جواب لکھیں:', '۵. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ:')
    e.group('lines', [('1. Write a note on the process of learning through simulation.', '۱۔ تلبیس کے ذریعے سیکھنے کے عمل پر نوٹ لکھیں۔', '۱. د سیمولېشن له لارې د زده‌کړې پر بهیر یادښت ولیکئ.'),
                      ('2. Discuss the public service message in detail and also give an example.', '۲۔ پبلک سروس میسج پر تفصیلی بحث کریں اور ایک مثال بھی دیں۔', '۲. د عامه خدمت پر پیغام تفصیلي بحث وکړئ او یوه بېلګه هم ورکړئ.'),
                      ('3. What is meant by disaster management? Also discuss planning for it.', '۳۔ سانحات کے اِنتظام سے کیا مراد ہے نیز اِس کیلئے منصوبہ سازی پر بحث کیجیے۔', '۳. د ناورینونو له مدیریت څه مراد دی؟ د هغه لپاره پر پلان جوړونې هم بحث وکړئ.'),
                      ('4. Write a note on community service.', '۴۔ کمیونٹی سروس پر نوٹ لکھیں۔', '۴. پر ټولنیز خدمت یادښت ولیکئ.')])
    e.h('Practical activities:', 'عملی سرگرمیاں:', 'عملي فعالیتونه:')
    e.group('lines', [('1. Preparing a public service announcement on TV (keeping material, voice and form in view).', '۱۔ ٹی وی پر ایک عوامی خدمت کے اِعلان کی تیاری (مواد، آواز اور شکل کو مدِنظر رکھتے ہوئے)۔', '۱. په ټلوېزیون د عامه خدمت د یوه اعلان چمتو کول (مواد، غږ او بڼه په پام کې نیولو سره).'),
                      ('2. Running a signature campaign on some world or national issue.', '۲۔ کسی عالمی یا قومی مسئلہ پر دستخطی مہم چلانا۔', '۲. پر یوې نړیوالې یا ملي مسئلې د لاسلیک کمپاین چلول.'),
                      ('3. Using the internet for a signature campaign so that people sign.', '۳۔ دستخطی مہم کیلئے انٹرنٹ کا اِستعمال تاکہ لوگ دستخط کریں۔', '۳. د لاسلیک کمپاین لپاره د انټرنېټ کارول ترڅو خلک لاسلیک وکړي.')])
    ex = BOOK.record(e, 'civ12-ch8-exercise-2', 'Chapter 8 exercise (2)', 'باب ۸: مشق (۲)', '۸ څپرکی: تمرین (۲)', 89, [168, 169])
    ex['sourceNote'] = 'The match-the-columns lists are reproduced as a two-column table in the printed order (not matched). The answer boxes are given as bracketed prompts.'
    BOOK.save(89, [(8, ex)], complete_units=[8], issues=[{'id': 'civ12-pdf089', 'unit': 8, 'printedPage': 168,
               'description': 'Q2(1) refers to a Canadian simulation programme not mentioned in the chapter text; Q2(5) “”تیار رہنا ہے“” (closing quote placed after ہے); activity 3 “انٹرنٹ”. Retained as printed.'}])


def gl(b, items):
    f = lambda h, d: f'{h}: {d}' if d else f'{h}:'
    b.group('lines', [(f(f'{en} ({t})', d), f(f'{u} ({t})', du), f(f'{p} ({t})', dp)) for t, en, d, u, du, p, dp in items])


def p90():
    b = Builder()
    b.h('Glossary', 'مخصوص اِصطلاحات (Glossary)', 'ځانګړې اصطلاحګانې')
    b.h('(Alif)', '(الف)', '(الف)')
    gl(b, [
     ('Socialism', 'Ishtimaliyat', '', 'اِشتمالیت', '', 'اشتمالیت', ''),
     ('Socialism and Communism', 'Ishtirakiyat and Ishtimaliyat', 'Ishtirakiyat, i.e. socialism, means a political and economic ideology in which the important means of production and income are taken into national or collective ownership. Everyone is given remuneration according to his work. Work is taken from everyone according to his ability. Man cannot exploit man, and the class system is ended, considering it an insult to humanity. This system is in China.',
      'اِشتراکیت و اِشتمالیت', 'اِشتراکیت یعنی سوشلزم سے مراد ایک ایسا سیاسی و اقتصادی نظریہ جس میں پیداوار اور آمدنی کے اہم ذرائع قومی ملکیت یا اِجتماعی ملکیت میں لئے جاتے ہیں۔ ہر ایک کو اُس کے کام کے مطابق معاوضہ دیا جاتا ہے۔ ہر ایک سے اُسکی صلاحیت کے مطابق کام لیا جاتا ہے۔ اِنسان اِنسان کا اِستحصال نہیں کر سکتا اور طبقاتی نظام اِنسانیت کی توہین سمجھ کر ختم کر دیا جاتا ہے۔ یہ نظام چین میں ہے۔',
      'اشتراکیت او اشتمالیت', 'اشتراکیت یعنې سوسیالیزم داسې سیاسي او اقتصادي نظریه ده چې پکې د تولید او عاید مهمې سرچینې ملي یا ټولیز ملکیت ته اخیستل کېږي. هر چا ته د هغه د کار سره سم معاوضه ورکول کېږي. له هر چا د هغه د وړتیا سره سم کار اخیستل کېږي. انسان د انسان استثمار نه شي کولی او طبقاتي نظام د انسانیت سپکاوی ګڼل کېږي او پای ته رسول کېږي. دا نظام په چین کې دی.'),
     ('Communism', 'Ishtimaliyat', 'Ishtimaliyat or communism is such a political and economic ideology in which all means of production and income are taken into national or collective ownership. Everyone is given remuneration according to his need. Work is taken from everyone according to his ability. Man cannot exploit man, and the class system is ended because it is an insult to humanity. This system was in the former Soviet Union.',
      'اِشتراکیت', 'اِشتراکیت یا کمیونزم ایک ایسا سیاسی و اِقتصادی نظریہ ہے جس میں پیداوار اور آمدنی کے تمام ذرائع قومی یا اِجتماعی ملکیت میں لئے جاتے ہیں۔ ہر ایک کو اُس کی ضرورت کے مطابق معاوضہ دیا جاتا ہے۔ ہر ایک سے اُسکی صلاحیت کے مطابق کام لیا جاتا ہے۔ اِنسان اِنسان کا اِستحصال نہیں کر سکتا اور طبقاتی نظام کو ختم کیا جاتا ہے کیونکہ یہ اِنسانیت کی توہین ہے۔ یہ نظام سابقہ سوویت یونین میں تھا۔',
      'اشتمالیت', 'اشتمالیت یا کمونیزم داسې سیاسي او اقتصادي نظریه ده چې پکې د تولید او عاید ټولې سرچینې ملي یا ټولیز ملکیت ته اخیستل کېږي. هر چا ته د هغه د اړتیا سره سم معاوضه ورکول کېږي. له هر چا د هغه د وړتیا سره سم کار اخیستل کېږي. انسان د انسان استثمار نه شي کولی او طبقاتي نظام پای ته رسول کېږي ځکه دا د انسانیت سپکاوی دی. دا نظام په پخواني شوروي اتحاد کې و.'),
     ('Individualism', 'Infiradiyat', 'When the state interferes as little as possible in the affairs of citizens and citizens have more freedom.', 'اِنفرادیت', 'جب ریاست شہریوں کے معاملات میں کم سے کم مداخلت کرے اور شہریوں کو زیادہ آزادی حاصل ہو۔', 'انفرادیت', 'کله چې دولت د اتباعو په چارو کې تر ټولو لږ لاسوهنه وکړي او اتباع ډېره ازادي ولري.'),
     ('Evolution', 'Irtiqa', 'Gradual development, e.g. the growth of a human or a plant.', 'اِرتقاء', 'درجہ بہ درجہ ترقی مثلاً اِنسان یا پودے کا بڑھنا۔', 'ارتقا', 'ګام په ګام پرمختګ، لکه د انسان یا بوټي وده.'),
     ('Association', 'Anjuman', 'Human organisations or institutions; an organised gathering of individuals to solve some common matter collectively.', 'انجمن', 'اِنسانی تنظیمیں یا اِدارے۔ کسی مشترکہ معاملہ کو اِجتماعی انداز میں حل کرنے کے لئے افراد کا منظم اِجتماع۔', 'انجمن', 'انساني سازمانونه یا ادارې؛ د کومې ګډې چارې د ټولیز حل لپاره د وګړو منظمه ټولګه.'),
     ('Utility', 'Ifadiyat', 'The benefit of some work, thing, individual or institution.', 'افادیت', 'کسی کام، چیز، فرد یا اِدارے کا فائدہ۔', 'ګټورتیا', 'د کوم کار، شي، فرد یا ادارې ګټه.'),
     ('Potential', 'Isti‘dad', 'Hidden abilities in an individual.', 'اِستعداد', 'کسی فرد میں پوشیدہ صلاحیتیں۔', 'استعداد', 'په یوه فرد کې پټې وړتیاوې.'),
     ('Aristotle', 'Arastu', 'A Greek philosopher of about 400 BC who is called the founder of political science.', 'ارسطو', 'تقریباً ۴۰۰ قبل از مسیح کا یونانی فلسفی جسے علمِ سیاسیات کا بانی کہا جاتا ہے۔', 'ارسطو', 'د میلاد څخه نږدې ۴۰۰ کاله مخکې یوناني فیلسوف چې د سیاسي علومو بنسټګر بلل کېږي.'),
     ('Election', 'Intikhab', 'When the public or an institution does an appointment to some office on the basis of majority opinion, this is election.', 'اِنتخاب', 'جب عوام یا اِدارہ کسی بھی عہدے کے لئے تقرری اکثریتی رائے کی بنیاد پر کرے تو یہ اِنتخاب ہے۔', 'ټاکنه', 'کله چې خلک یا اداره د کومې څوکۍ لپاره ګمارنه د اکثریت رایې پر بنسټ وکړي، دا ټاکنه ده.'),
     ('Obedience', 'Ita‘at', 'To obey, accept, act upon, accept willingly.', 'اِطاعت', 'ماننا، تسلیم کرنا، پر عمل کرنا، بخوشی قبول کرنا۔', 'اطاعت', 'منل، تسلیمول، عمل کول، په خوښۍ منل.'),
     ('Revolution', 'Inqilab', 'Immediate political change by violent methods.', 'اِنقلاب', 'پُرتشدد طریقوں سے فوری سیاسی تبدیلی۔', 'انقلاب', 'په تاوتریخجنو لارو سمدستي سیاسي بدلون.'),
     ('Discrimination', 'Imtiyaz', 'Differentiation.', 'اِمتیاز', 'تفریق۔', 'تبعیض', 'توپیر کول.'),
     ('Reforms', 'Islah', 'Making some thing or programme more effective and useful by positive change.', 'اِصلاح', 'کسی چیز یا پروگرام میں مثبت تبدیلی کر کے اِسے زیادہ مؤثر اور کارآمد بنانا۔', 'اصلاح', 'په یو شي یا پروګرام کې د مثبت بدلون له لارې هغه ډېر اغېزمن او ګټور کول.'),
     ('Renaissance', 'Ihya', 'Reviving some absent or forgotten thing or principle.', 'اِحیاء', 'کسی غائب یا فراموش کردہ چیز یا اُصول کو دوبارہ زندہ کرنا۔', 'بیا راژوندي کول', 'د کوم ورک یا هېر شوي شي یا اصل بیا ژوندي کول.')])
    r1 = BOOK.record(b, 'civ12-bm-glossary-1', 'Glossary (1)', 'مخصوص اِصطلاحات (۱)', 'ځانګړې اصطلاحګانې (۱)', 90, [170], unit_title=GLOSS_T)
    r1['sourceNote'] = 'Each entry gives the term in transliteration and the printed English equivalent in brackets. The first entry “اِشتمالیت (Socialism)” has no definition of its own in print; the next entry “(Socialism and Communism)” carries it.'
    t = Builder()
    gl(t, [
     ('Stability', 'Istihkam', 'To remain established and permanent in one place; success in running or working; durability.', 'اِستحکام', 'ایک جگہ پر قائم و دائم رہنا۔ کامیابی سے کام کرنا یا چلنا۔ پائیداری۔', 'ثبات', 'په یوه ځای کې ټینګ او تل پاتې کېدل؛ په بریالیتوب کار کول یا چلېدل؛ پایښت.'),
     ('Principle', 'Usul', 'Rule, regulation; regular method.', 'اُصول', 'قاعدہ، ضابطہ۔ باقاعدہ طریقہ۔', 'اصل', 'قاعده، ضابطه؛ منظمه طریقه.'),
     ('Centralization of Powers', 'Irtikaz-e-Ikhtiyarat', 'Handing all powers to one institution or one individual and making subordinate institutions and individuals powerless.', 'اِرتکازِ اِختیارات', 'تمام اِختیارات کو ایک اِدارے یا ایک فرد کے سپرد کرنا اور ماتحت اِداروں اور افراد کو بے اِختیار بنانا۔', 'د واکونو تمرکز', 'ټول واکونه یوې ادارې یا یوه فرد ته سپارل او لاندې ادارې او کسان بې‌واکه کول.'),
     ('Bureaucracy', 'Afsar-shahi', 'When the powers of the country are in reality under the control of the country’s highest government servants, it is called bureaucracy (afsar-shahi or naukar-shahi).', 'افسر شاہی', 'جب ملکی اِختیارات حقیقی طور پر ملک کے اعلیٰ ترین سرکاری ملازمین کے قابو میں ہوں۔ اِسے افسر شاہی یا نوکر شاہی کہا جاتا ہے۔', 'افسرسالاري', 'کله چې د هېواد واکونه په حقیقت کې د هېواد د تر ټولو لوړو دولتي کارکوونکو تر واک لاندې وي، افسرسالاري یا نوکرسالاري بلل کېږي.'),
     ('Appeal', 'Appeal', 'When one party is not satisfied with some court decision, then he applies against the decision in a higher court, which is called an appeal.', 'اپیل', 'کسی عدالتی فیصلے سے جب ایک فریق مطمئن نہ ہو تو وہ اعلیٰ عدالت میں فیصلے کے خلاف درخواست کرتا ہے جسے اپیل کہتے ہیں۔', 'استیناف', 'کله چې یو اړخ له یوې محکمې پرېکړې مطمئن نه وي، په لوړه محکمه کې د پرېکړې پر وړاندې غوښتنه کوي چې استیناف ورته ویل کېږي.'),
     ('Merit', 'Ahliyat', 'To come up fully to the required qualification and conditions.', 'اہلیت', 'مطلوبہ قابلیت و شرائط پر پورا اُترنا۔', 'وړتیا', 'په غوښتل شوې وړتیا او شرایطو بشپړ برابرېدل.'),
     ('Nepotism', 'Aqraba-parwari', 'Giving preference to relatives, friends and favourites in the distribution of government facilities or offices.', 'اقرباء پروری', 'سرکاری سہولیات یا عہدوں کی تقسیم میں رشتہ داروں، دوستوں اور منظورِ نظر افراد کو ترجیح دینا۔', 'خپلوي‌پالنه', 'د دولتي اسانتیاوو یا څوکیو په وېش کې خپلوانو، ملګرو او خوښو کسانو ته لومړیتوب ورکول.'),
     ('Victimization', 'Intiqami karrawaiyan', 'Causing trouble to political opponents; the use of state powers against them.', 'اِنتقامی کارروائیاں', 'سیاسی مخالفین کو تکلیف پہنچانا۔ اُنکے خلاف ریاستی اِختیارات کا اِستعمال۔', 'غچ اخیستونکې کړنې', 'سیاسي مخالفینو ته تکلیف رسول؛ د هغوی پر وړاندې د دولتي واکونو کارونه.'),
     ('Plato', 'Aflatun', 'A Greek philosopher of the fifth century BC who was the pupil of Socrates and the teacher of Aristotle.', 'افلاطون', 'پانچویں صدی قبل از مسیح کا یونانی فلسفی جو سقراط کا شاگرد اور ارسطو کا اُستاد تھا۔', 'افلاطون', 'د میلاد څخه مخکې د پنځمې پېړۍ یوناني فیلسوف چې د سقراط شاګرد او د ارسطو استاد و.'),
     ('Imperialism', 'Isti‘mar', 'That state which, through power and policy, occupies independent states.', 'اِستعمار', 'وہ ریاست جو طاقت اور پالیسی کے ذریعے آزاد ریاستوں پر قبضہ کرے۔', 'استعمار', 'هغه دولت چې د ځواک او پالیسۍ له لارې پر خپلواکو دولتونو قبضه وکړي.'),
     ('Dictatorship', 'Amriyat', 'Governing by oppression and force.', 'آمریت', 'ظلم و جبر سے حکومت کرنا۔', 'دیکتاتوري', 'په ظلم او زور حکومت کول.'),
     ('Arguing', 'Istidlal', 'To present an argument.', 'اِستدلال', 'دلیل پیش کرنا۔', 'استدلال', 'دلیل وړاندې کول.'),
     ('Exploitation', 'Istihsal', 'To obtain something by taking undue advantage of someone’s ignorance or weakness.', 'اِستحصال', 'ناسمجھی یا کمزوری سے ناجائز فائدہ اُٹھا کر کوئی چیز حاصل کرنا۔', 'استثمار', 'د چا له ناپوهۍ یا کمزورۍ ناروا ګټه اخیستل او کوم شی ترلاسه کول.'),
     ('Rigid', 'Ustuwar', 'In which there is no flexibility.', 'اُستوار', 'جس میں لچک نہ ہو۔', 'کلک', 'چې نرمښت پکې نه وي.'),
     ('Approval, Praising', 'Istihsan', 'To consider good, to like.', 'اِستحسان', 'اچھا جاننا، پسند کرنا۔', 'استحسان', 'ښه ګڼل، خوښول.'),
     ('Deduction', 'Istinbat', 'To draw a conclusion.', 'اِستنباط', 'نتیجہ اخذ کرنا۔', 'استنباط', 'پایله اخیستل.'),
     ('Economy', 'Iqtisadiyat', 'That science in which the production and distribution of wealth are discussed.', 'اِقتصادیات', 'وہ علم جس میں دولت کی پیداوار اور تقسیم پر بحث کی جاتی ہے۔', 'اقتصاد', 'هغه علم چې پکې د شتمنۍ پر تولید او وېش بحث کېږي.'),
     ('Features', 'Ausaf', 'Qualities and characteristics.', 'اوصاف', 'صفات و خصوصیات۔', 'ځانګړنې', 'صفتونه او ځانګړنې.'),
     ('Afro-Asian', 'Afro-Asiayi', 'The countries of Asia and Africa.', 'افروایشیائی', 'ایشیاء اور افریقہ کے ممالک۔', 'افرو–آسیايي', 'د آسیا او افریقا هېوادونه.'),
     ('ISAF — International Security Assistance Force', 'ISAF', 'The military contingents of more than forty countries under the leadership of America in Afghanistan, which are engaged against the Taliban and Al-Qaeda.', 'ایساف', 'افغانستان میں امریکہ کی سربراہی میں چالیس سے زیادہ ممالک کے فوجی دستے جو طالبان اور القاعدہ کے خلاف مصروف ہیں۔', 'ایساف', 'په افغانستان کې د امریکا په مشرۍ د څلوېښتو زیاتو هېوادونو پوځي ټولګي چې د طالبانو او القاعدې پر وړاندې بوخت دي.'),
     ('Trusteeship Council', 'UN Trusteeship Council', 'That branch of the United Nations which looks after weak areas.', 'اقوامِ متحدہ کی تولیتی کونسل', 'اقوامِ متحدہ کی وہ شاخ جو کمزور علاقوں کی دیکھ بھال کرتی ہے۔', 'د ملګرو ملتونو د قیمومیت شورا', 'د ملګرو ملتونو هغه څانګه چې د کمزورو سیمو څارنه کوي.'),
     ('Economic Coopration Organization', 'Economic Cooperation Organisation', 'An organisation for economic cooperation among Pakistan, Iran, Turkey, Afghanistan and the Central Asian Muslim countries.', 'اِقتصادی تعاون کی تنظیم', 'پاکستان، ایران، ترکی، افغانستان اور وسطی ایشیائی مسلمان ممالک کے درمیان اقتصادی تعاون کیلئے تنظیم۔', 'د اقتصادي همکارۍ سازمان', 'د پاکستان، ایران، ترکیې، افغانستان او منځنۍ آسیا د مسلمانو هېوادونو ترمنځ د اقتصادي همکارۍ سازمان.')])
    r2 = BOOK.record(t, 'civ12-bm-glossary-2', 'Glossary (2)', 'مخصوص اِصطلاحات (۲)', 'ځانګړې اصطلاحګانې (۲)', 90, [171])
    BOOK.save(90, [(BM, r1), (BM, r2)], issues=[{'id': 'civ12-pdf090', 'unit': BM, 'printedPage': 171,
               'description': 'Glossary prints “Economic Coopration Organization”, “Approva l,Praising”, “Internationa(l)” and the definition of Socialism with Ishtirakiyat as the Urdu head; “اِشتمالیت (Socialism)” appears as a heading without its own definition. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 88
    {88: p88, 89: p89, 90: p90}[n]()
