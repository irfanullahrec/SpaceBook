"""Islamiat (Ikhtiari) XII PDF79: p.148 — Hadith MCQs (f)–(j) + activities (end ch.2); p.149 — Chapter 3 opening. Run: python class12_iski_page079.py"""
from class12_iski_common import BOOK, Builder, rec, P, L

O = lambda e, u, p: (e, u, p)
MCQ = [(('(f) How did the Companion of the Messenger (may Allah be pleased with him) serve the guest of him ﷺ?', 'و۔ صحابیِ رسول رضی اللہ عنہ نے آپ صلی اللہ علیہ وآلہٖ وسلم کے مہمان کی کیسے خدمت کی؟', 'و. د رسول صحابي رضي الله عنه د هغه ﷺ د مېلمه خدمت څنګه وکړ؟'),
        [O('gave him water to drink', 'پانی پلایا', 'اوبه یې ورکړې'), O('fed him food', 'کھانا کھلایا', 'ډوډۍ یې ورکړه'), O('helped him financially', 'مالی مدد کی', 'مالي مرسته یې وکړه'), O('gave him a gift', 'تحفہ دیا', 'ډالۍ یې ورکړه')]),
       (('(g) Which deed has been declared the best after the obligatory duties?', 'ز۔ فرائض کے بعد کس عمل کو افضل قرار دیا گیا ہے؟', 'ز. له فرائضو وروسته کوم عمل غوره ګڼل شوی؟'),
        [O('feeding the needy', 'مسکینوں کو کھانا کھلانا', 'مسکینانو ته ډوډۍ ورکول'), O('showing mercy to animals', 'جانوروں پر رحم کرنا', 'پر څارویو رحم'), O('speaking gently', 'نرمی سے بات کرنا', 'په نرمۍ خبرې کول'), O('helping the poor', 'غریبوں کی مدد کرنا', 'د غریبانو مرسته')]),
       (('(h) About which organ of the human body was it said that if it works properly, the whole body remains sound?', 'ح۔ انسانی جسم کے کس عضو کے بارے میں یہ فرمایا گیا کہ اگر وہ درست کام کرے تو سارا جسم ہی درست رہتا ہے؟', 'ح. د انساني بدن د کوم غړي په اړه ویل شوي چې که سم کار وکړي، ټول بدن سم پاتې کېږي؟'),
        [O('eye', 'آنکھ', 'سترګه'), O('brain', 'دماغ', 'دماغ'), O('hand', 'ہاتھ', 'لاس'), O('heart', 'دل', 'زړه')]),
       (('(i) Which sin has been counted among the major sins?', 'ط۔ کس گناہ کو کبیرہ گناہوں میں شمار کیا گیا ہے؟', 'ط. کومه ګناه په لویو ګناهونو کې شمېرل شوې؟'),
        [O('considering others inferior', 'دوسروں کو حقیر سمجھنا', 'نور سپک ګڼل'), O('disobedience to parents', 'والدین کی نافرمانی', 'د مور و پلار نافرماني'), O('not helping others', 'دوسروں کی مدد نہ کرنا', 'د نورو مرسته نه کول'), O('quarrelling', 'جھگڑا کرنا', 'شخړه کول')]),
       (('(j) Once he ﷺ did not give a Companion (may Allah be pleased with him) permission to take part in jihad, because he ﷺ wanted that he:', 'ی۔ ایک بار آپ صلی اللہ علیہ وآلہٖ وسلم نے ایک صحابی رضی اللہ عنہ کو جہاد میں شرکت کی اجازت نہ دی کیونکہ آپ صلی اللہ علیہ وآلہٖ وسلم چاہتے تھے کہ وہ:', 'ی. یو ځل هغه ﷺ یوه صحابي رضي الله عنه ته په جهاد کې د ګډون اجازه ورنه کړه، ځکه هغه ﷺ غوښتل چې هغه:'),
        [O('first develop bravery in himself', 'پہلے اپنے اندر بہادری پیدا کر لے', 'لومړی په ځان کې زړورتیا پیدا کړي'), O('serve his parents', 'اپنے والدین کی خدمت کرے', 'د خپل مور و پلار خدمت وکړي'),
         O('take care of his health', 'اپنی صحت کا خیال رکھے', 'د خپلې روغتیا پام وساتي'), O('stay in Madinah and help people', 'مدینہ میں رہ کر لوگوں کی مدد کرے', 'په مدینه کې پاتې شي او د خلکو مرسته وکړي')])]


def p79():
    b = Builder()
    for q, o in MCQ:
        b.mcq('', q, o)
    b.h('Activities', 'سرگرمیاں', 'فعالیتونه')
    L(b, [('i. Make a chart of five such ahadith or Quranic verses in which good treatment of parents has been urged.', 'i۔ پانچ ایسی احادیث یا قرآنی آیات کا چارٹ بنائیں جن میں والدین سے اچھے سلوک کی تلقین کی گئی ہے۔', 'i. د داسې پنځو احادیثو یا قرآني آیتونو چارټ جوړ کړئ چې په کې له مور و پلار سره د ښه چلند سپارښتنه شوې.'),
          ('ii. Write two such ahadith in which he ﷺ used a simile.', 'ii۔ دو ایسی احادیث لکھیں جن میں آپ صلی اللہ علیہ وآلہٖ وسلم نے تشبیہ استعمال فرمائی ہے۔', 'ii. دوه داسې احادیث ولیکئ چې په کې هغه ﷺ تشبیه کارولې.'),
          ('iii. Collect a few such ahadith in which he ﷺ stressed treating animals and birds with compassion.', 'iii۔ چند ایسی احادیث جمع کریں جن میں آپ صلی اللہ علیہ وآلہٖ وسلم نے جانوروں اور پرندوں سے شفقت کا برتاؤ کرنے کی تاکید فرمائی ہے۔', 'iii. یو څو داسې احادیث راټول کړئ چې په کې هغه ﷺ له څارویو او مرغانو سره د شفقت د چلند ټینګار کړی.')])
    r1 = rec(b, 2, 148, 79, [148], kind='exercise')
    t = Builder()
    t.h('Chapter Three: Services of Muslims in academic progress', 'بابِ سوم: علمی پیش رفت میں مسلمانوں کی خدمات', 'درېیم څپرکی: په علمي پرمختګ کې د مسلمانانو خدمتونه')
    t.h('Teaching objectives', 'تدریسی مقاصد', 'تدریسي موخې')
    t.p('The purpose of this lesson is to enable the students that they:', 'اس سبق کا مقصد طلبہ اور طالبات کو اس قابل بنانا ہے کہ وہ:', 'د دې لوست موخه دا ده چې زده‌کوونکي دې ته وړ کړي چې:')
    L(t, [('1. become aware of the various branches of Islamic sciences and try to benefit from them.', '1. اسلامی علوم کے مختلف شعبوں سے آگاہ ہو سکیں اور ان سے استفادہ کی کوشش کریں۔', '۱. د اسلامي علومو له بېلابېلو څانګو خبر شي او له هغو د ګټې اخیستو هڅه وکړي.'),
          ('2. can comprehend the services of Muslims in various sciences.', '2. مختلف علوم میں مسلمانوں کی خدمات کا ادراک کر سکیں۔', '۲. په بېلابېلو علومو کې د مسلمانانو خدمتونه درک کړای شي.')])
    P(t, [('When Allah, the Lord of Honour, raised the Noble Prophet ﷺ in Arabia, at that time the darkness of ignorance had spread everywhere. Although the Arabs were unmatched in eloquence of tongue and in fluency and rhetoric, so much so that they used to call non-Arabs \'ajami, that is, dumb, yet in social, moral and religious respects those people were afflicted with errors.', 'جب عرب میں اللہ رب العزت نے نبی اکرم صلی اللہ علیہ وآلہٖ وسلم کو مبعوث فرمایا اُس وقت ہر طرف جہالت کا اندھیرا چھایا ہوا تھا۔ گو کہ عرب لوگ زبان دانی اور فصاحت و بلاغت میں بے مثال تھے حتیٰ کہ غیر عرب کو عجمی یعنی گونگا کہا کرتے تھے مگر پھر بھی معاشرتی، اخلاقی اور مذہبی لحاظ سے وہ لوگ گمراہیوں میں مبتلا تھے۔', 'کله چې الله رب العزت په عرب کې نبي اکرم ﷺ مبعوث کړ، هغه وخت هر لوري ته د جهالت تیاره خپره وه. که څه هم عربان په ژبه‌پوهنه او فصاحت و بلاغت کې بې‌ساري وو، تر دې چې غیر عربانو ته یې عجمي یعنې ګونګ ویل، خو بیا هم په ټولنیز، اخلاقي او مذهبي لحاظ هغه خلک په ګمراهیو اخته وو.'),
          ('The coming of the religion of Islam lit the lamp of knowledge and wisdom everywhere, and these very Arabs, who were known for their ignorance, came forth as the most civilised nation of all.', 'دینِ اسلام کی آمد نے ہر طرف علم و حکمت کی شمع روشن کر دی اور یہی عرب جو جہالت کی نسبت سے پہچانے جاتے تھے سب سے مہذب قوم بن کر سامنے آئے۔', 'د اسلام دین راتګ هر لوري ته د علم او حکمت څراغ بل کړ، او همدا عربان چې د جهالت په نسبت پېژندل کېدل، تر ټولو متمدن قوم شول.'),
          ('Islam has declared acquiring knowledge obligatory on every man and woman, and on this very basis Muslims acquired not only religious but also worldly sciences. The Muslim society whose foundation was laid in Madinah Munawwarah — the Muslim Ummah spread this society to the vast and extensive areas of the world. Among the prominent features of this society, first of all comes "knowledge". Keeping this very feature in view, the services of Muslims in academic progress and a few sciences have been mentioned, which are as follows.', 'اسلام نے ہر مرد و عورت پر علم حاصل کرنا فرض قرار دیا ہے اور اسی بنیاد پر مسلمانوں نے نہ صرف دینی بلکہ دنیاوی علوم کو بھی حاصل کیا۔ جس مسلم معاشرہ کی بنیاد مدینہ منورہ میں رکھی گئی اس معاشرے کو مسلمان امت نے دنیا کے وسیع و عریض علاقے تک پھیلایا۔ اس معاشرے کی نمایاں خصوصیات میں سب سے پہلے ”علم“ آتا ہے۔ اسی خصوصیت کو مدِنظر رکھتے ہوئے علمی پیش رفت میں مسلمانوں کی خدمات اور چند علوم کا تذکرہ کیا گیا ہے جو کہ مندرجہ ذیل ہے۔', 'اسلام پر هر نارینه او ښځه د علم ترلاسه کول فرض ګرځولي، او پر همدې بنسټ مسلمانانو نه یوازې دیني بلکې دنیوي علوم هم ترلاسه کړل. د کومې مسلمانې ټولنې بنسټ چې په مدینه منوره کې کېښودل شو، اسلامي امت هغه ټولنه د نړۍ پراخو سیمو ته خپره کړه. د دې ټولنې په ښکاره ځانګړنو کې تر ټولو لومړی «علم» راځي. د همدې ځانګړنې په پام کې نیولو سره په علمي پرمختګ کې د مسلمانانو خدمتونه او یو څو علوم یاد شوي، چې په لاندې ډول دي.')])
    BOOK.save(79, [(2, r1), (3, rec(t, 3, 149, 79, [149], first=True))], complete_units=[2], issues=[{'id': 'iski12-pdf079', 'unit': 2, 'printedPage': 148,
               'description': 'End of Chapter 2 (Hadith) on p.148; MCQ options printed i–iv with no printed key. p.149 opens Chapter 3; the photo is skewed and glare-faded at the left, text read through.'}])


if __name__ == '__main__':
    p79()
