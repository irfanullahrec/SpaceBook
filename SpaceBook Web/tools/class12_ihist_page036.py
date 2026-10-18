"""Islamic History XII PDF36: p.64 — exercise of lessons 11–13; p.65 — Lesson 14 Mu'tadid billah. Run: python class12_ihist_page036.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L


def p36():
    b = Builder()
    b.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    L(b, [('1. Write a comprehensive note on the era of government of Muhammad bin Ja\'far.', '۱۔ محمد بن جعفر کے دورِ حکومت پر جامع نوٹ لکھیں۔', '۱. د محمد بن جعفر د حکومت پر دوره جامع یادښت ولیکئ.'),
          ('2. "Ahmad bin Mutawakkil al-Mu\'tamid was a ruler in name only." Discuss.', '۲۔ ”احمد بن متوکل معتمد صرف نام کا حکمران تھا“ بحث کریں۔', '۲. «احمد بن متوکل معتمد یوازې په نامه واکمن و.» بحث وکړئ.')])
    b.p('3. Put a (✓) mark in front of the correct answer and a (✗) in front of the wrong one.', '۳۔ درست جواب کے سامنے (✓) کا نشان اور غلط کے سامنے (✗) لگائیں۔', '۳. د سم ځواب پر وړاندې (✓) او د ناسم پر وړاندې (✗) ولګوئ.')
    L(b, [('a. After the killing of Mutawakkil the Turks, according to their own will, made Muhammad bin Ja\'far caliph.', 'الف: متوکل کے قتل کے بعد ترکوں نے اپنی مرضی کے مطابق محمد بن جعفر کو خلیفہ بنایا۔', 'الف. د متوکل له وژنې وروسته ترکانو د خپلې خوښې سره سم محمد بن جعفر خلیفه کړ.'),
          ('b. The Saffarids established the Saffarid government in Sistan and Iran in the era of Mu\'tazz billah.', 'ب: صفاریوں نے سیستان اور ایران میں معتز باللہ کے دور میں صفاری حکومت قائم کر لی۔', 'ب. صفاریانو د معتز بالله په دوره کې په سیستان او ایران کې صفاري حکومت جوړ کړ.'),
          ('c. Ahmad bin Mutawakkil al-Mu\'tamid ruled for approximately 10 years.', 'ج: احمد بن متوکل معتمد نے تقریباً ۱۰ سال حکومت کی۔', 'ج. احمد بن متوکل معتمد نږدې ۱۰ کاله حکومت وکړ.')])
    b.p('4. Fill in the blanks.', '۴۔ خالی جگہیں پر کریں۔', '۴. تشې ډکې کړئ.')
    L(b, [('a. The Turks freed ______ and began his allegiance.', 'الف: ترکوں نے ______ کو آزاد کر کے اس کی بیعت شروع کر دی۔', 'الف. ترکانو ______ خوشې کړ او د هغه بیعت یې پیل کړ.'),
          ('b. At last ______ withdrew.', 'ب: آخر کار ______ دستبردار ہو گیا۔', 'ب. بالاخره ______ تېر شو.'),
          ('c. Because of not getting salary for several months the army did ______.', 'ج: کئی ماہ تک تنخواہ نہ ملنے کی وجہ سے فوج نے ______ کر دی۔', 'ج. د څو میاشتو معاش نه ترلاسه کولو له امله پوځ ______ وکړه.'),
          ('d. At the time of accession Mu\'tamid\'s age was ______.', 'د: تخت نشینی کے وقت معتمد کی عمر ______ تھی۔', 'د. پر تخت کېناستو پر مهال د معتمد عمر ______ و.'),
          ('e. ______ put an end to the Tahirid government.', 'ہ: ______ نے حکومتِ طاہریہ کا خاتمہ کر دیا۔', 'ه. ______ طاهري حکومت ختم کړ.'),
          ('f. Mu\'tamid took refuge with ______.', 'و: معتمد نے ______ کے پاس پناہ لی۔', 'و. معتمد له ______ سره پناه واخیسته.')])
    r1 = rec(b, 13, 64, 36, [64], kind='exercise')
    t = Builder()
    t.p('Chapter: 6', 'باب: 6', 'باب: ۶')
    t.h('Abu al-Abbas Ahmad bin Muwaffaq al-Mu\'tadid billah', 'ابوالعباس احمد بن موفق معتضد باللہ', 'ابوالعباس احمد بن موفق معتضد بالله')
    t.p('892 CE to 902 CE', '۸۹۲ء تا ۹۰۲ء', '۸۹۲ع تر ۹۰۲ع')
    S(t, [(None, ('Mu\'tamid had nominated his nephew Mu\'tadid billah as his heir-apparent. So after his death Mu\'tadid ascended the throne. His accession took place in Rabi\' al-Awwal 279 AH. He made Ubaydullah bin Sulayman his vizier. Mu\'tadid\'s age was approximately 37 years. He was completely different from his predecessor caliphs. He tried to get out of the claws of the Turks and also controlled other amirs. He tried to bring the dead corpse of the Abbasid government back to life. The great cause of the destruction of the Abbasid government was the selfish and arrogant amirs. To end their power Mu\'tadid began to make them fight among themselves. First of all he killed Rafi\' bin Harthamah. Later he also ended the activities of the Kharijites.', 'معتمد نے اپنے بھتیجے معتضد باللہ کو اپنا ولی عہد نامزد کیا تھا۔ چنانچہ اس کی وفات کے بعد معتضد تخت نشین ہوا۔ اس کی تخت نشینی ربیع الاول ۲۷۹ھ میں ہوئی۔ اس نے عبیداللہ بن سلیمان کو اپنا وزیر بنایا۔ معتضد کی عمر تقریباً ۳۷ سال تھی۔ یہ اپنے پیش رو خلفاء سے بالکل مختلف تھا۔ اس نے ترکوں کے پنجوں سے نکلنے کی کوشش کی اور دوسرے امراء کو بھی قابو کیا۔ عباسی حکومت کی مردہ لاش کو دوبارہ زندہ کرنے کی کوشش کی۔ عباسی حکومت کی تباہی کا بڑا سبب خود غرض اور مغرور امراء تھے۔ معتضد نے ان کی طاقت کو ختم کرنے کے لئے ان کو آپس میں لڑانا شروع کیا۔ سب سے پہلے رافع بن ہرثمہ کو قتل کر دیا۔ بعد میں خارجیوں کی سرگرمیوں کو بھی ختم کر دیا۔', 'معتمد خپل وراره معتضد بالله خپل ولیعهد ټاکلی و؛ نو له مړینې وروسته یې معتضد پر تخت کېناست. پر تخت کېناستل یې د ۲۷۹ هـ په ربیع الاول کې وشو. هغه عبیدالله بن سلیمان خپل وزیر کړ. د معتضد عمر نږدې ۳۷ کاله و؛ دا له خپلو مخکېنیو خلفاوو بېخي توپیر درلود. هغه هڅه وکړه چې د ترکانو له منګولو ووځي او نور امیران یې هم په واک کې راوستل؛ هڅه یې وکړه چې د عباسي حکومت مړ جسد بیا ژوندی کړي. د عباسي حکومت د ویجاړۍ لوی لامل ځان‌غوښتونکي او مغرور امیران وو؛ معتضد د هغوی د ځواک د ختمولو لپاره په خپل منځ کې جنګول پیل کړل. تر ټولو مخکې یې رافع بن هرثمه ووژه، او وروسته یې د خوارجو فعالیتونه هم ختم کړل.')),
          (('Death:', 'وفات:', 'وفات'),
           ('Mu\'tadid died in Rabi\' al-Awwal 289 AH, corresponding to 902 CE. According to Mas\'udi, as soon as Mu\'tadid stepped onto the throne of the caliphate, calm came to the mischief and disorder. The condition of the country had improved; war had ended. Suyuti has written that Mu\'tadid was very shrewd, valiant and brave. He restored the dignity of the caliphate. He is called the second Saffah.', 'ربیع الاول ۲۸۹ھ بمطابق ۹۰۲ء میں معتضد فوت ہوا۔ مسعودی کے مطابق معتضد کے تختِ خلافت پر قدم رکھتے ہی فتنہ و فساد میں سکون پیدا ہو گیا تھا۔ ملک کی حالت بہتر ہو گئی تھی۔ جنگ ختم ہو گئی تھی۔ سیوطی نے لکھا ہے کہ معتضد بڑا زیرک، شجاع اور بہادر تھا۔ اس نے خلافت کا وقار بحال کیا۔ اسے سفاح ثانی کہا جاتا ہے۔', 'معتضد د ۲۸۹ هـ په ربیع الاول کې، له ۹۰۲ع سره سم، مړ شو. د مسعودي په وینا، معتضد چې د خلافت پر تخت پښه کېښوده، فتنه او فساد ارام شو؛ د هېواد حالت ښه شو؛ جګړه ختمه شوه. سیوطي لیکلي چې معتضد ډېر هوښیار، زړور او باتور و؛ د خلافت وقار یې بحال کړ؛ «دویم سفاح» ورته ویل کېږي.'))])
    BOOK.save(36, [(13, r1), (14, rec(t, 14, 65, 36, [65], first=True))], complete_units=[13], issues=[{'id': 'ihist12-pdf036', 'unit': 13, 'printedPage': 64,
               'description': 'p.64: student ticks/crosses and filled blanks excluded; no printed key. Lesson 14 (Mu\'tadid) opens on p.65 under "باب: 6". A finger and book edge in the scan are excluded.'}])


if __name__ == '__main__':
    p36()
