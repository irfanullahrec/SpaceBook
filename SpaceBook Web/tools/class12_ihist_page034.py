"""Islamic History XII PDF34: pp.60–61 — Lesson 11 Muntasir; Musta'in; Lesson 12 Mu'tazz (start). Run: python class12_ihist_page034.py"""
from class12_ihist_common import BOOK, Builder, rec, S


def p34():
    b = Builder()
    b.p('Chapter: 5', 'باب: 5', 'باب: ۵')
    b.h('Muhammad bin Ja\'far al-Muntasir billah', 'محمد بن جعفر منتصر باللہ', 'محمد بن جعفر منتصر بالله')
    b.p('861 CE to 862 CE', '۸۶۱ء تا ۸۶۲ء', '۸۶۱ع تر ۸۶۲ع')
    S(b, [(None, ('After the killing of Mutawakkil the Turks, according to their own will, made Muntasir billah caliph. Allegiance was taken from the amirs, viziers and other people. His period of caliphate was very short. He remained in power for approximately six months, but in his era some conquests too took place.', 'متوکل کے قتل کے بعد ترکوں نے اپنی مرضی کے مطابق منتصر باللہ کو خلیفہ بنا دیا۔ امراء، وزراء اور دوسرے لوگوں سے بیعت لی گئی۔ اس کا دورِ خلافت بہت مختصر تھا۔ وہ تقریباً چھ ماہ برسرِ اقتدار رہا لیکن اس کے دور میں کچھ فتوحات بھی ہوئیں۔', 'د متوکل له وژنې وروسته ترکانو د خپلې خوښې سره سم منتصر بالله خلیفه کړ؛ له امیرانو، وزیرانو او نورو خلکو بیعت واخیستل شو. د خلافت دوره یې ډېره لنډه وه؛ نږدې شپږ میاشتې واک کې و، خو په دوره کې یې ځینې فتوحات هم وشول.')),
          (('Death:', 'وفات:', 'وفات'),
           ('Six months after coming to power Muntasir fell ill, and after suffering in this illness for three days he died.', 'برسرِ اقتدار آنے کے چھ ماہ بعد منتصر بیمار ہو گیا، اور اس بیماری میں تین دن مبتلا رہنے کے بعد وفات پائی۔', 'واک ته له رسېدو شپږ میاشتې وروسته منتصر ناروغ شو، او په دې ناروغۍ کې درې ورځې اخته پاتې شو او وفات شو.')),
          (None, ('After Muntasir, Mu\'tasim\'s grandson Musta\'in billah ascended the throne. He remained ruler from 862 CE to 865 CE. He had accepted the patronage of the Turks. Mu\'tazz and Mu\'ayyad were placed under house arrest. A revolt took place in Baghdad, but the Turkish chiefs Bugha, Atamish and Wasif crushed this revolt severely. Later discord arose among these Turkish chiefs too. Atamish and Bugha were killed.', 'منتصر کے بعد معتصم کا پوتا مستعین باللہ تخت نشین ہوا۔ وہ ۸۶۲ء تا ۸۶۵ء تک حکمران رہا۔ اس نے ترکوں کی سرپرستی قبول کر لی تھی۔ معتز اور موید کو نظر بند کر دیا گیا۔ بغداد میں بغاوت ہوئی لیکن ترک سرداروں بغا، آتاش اور وصیف نے اس بغاوت کو سختی سے کچل ڈالا۔ بعد میں ان ترک سرداروں میں بھی آپس میں پھوٹ پڑ گئی۔ اتامش اور بغا قتل کر دیئے گئے۔', 'له منتصر وروسته د معتصم لمسی مستعین بالله پر تخت کېناست؛ له ۸۶۲ع تر ۸۶۵ع واکمن و. د ترکانو سرپرستي یې منلې وه؛ معتز او مؤید نظربند شول. په بغداد کې بغاوت وشو، خو ترک مشرانو بغا، اتامش او وصیف دا بغاوت په سختۍ وځپه. وروسته د دې ترک مشرانو ترمنځ هم شخړه پیدا شوه؛ اتامش او بغا ووژل شول.')),
          (('The struggle between Musta\'in and Mu\'tazz:', 'مستعین اور معتز کے درمیان کشمکش:', 'د مستعین او معتز ترمنځ کشمکش'),
           ('Musta\'in had come from Samarra to Baghdad. The Turks freed Mu\'tazz and began taking allegiance for him. At last Musta\'in …', 'مستعین سامرا سے بغداد آ چکا تھا۔ ترکوں نے معتز کو آزاد کر کے اس کی بیعت شروع کر دی۔ آخر کار مستعین', 'مستعین له سامرا بغداد ته راغلی و. ترکانو معتز خوشې کړ او د هغه بیعت یې پیل کړ. بالاخره مستعین …'))])
    r1 = rec(b, 11, 60, 34, [60], first=True)
    t = Builder()
    S(t, [(None, ('… was placed under house arrest, and he died in this house arrest. According to some narrations he was killed.', 'کو نظر بند کر دیا گیا، اور وہ اس نظر بندی میں فوت ہو گیا۔ بعض روایات کے مطابق اسے قتل کر دیا گیا۔', '… نظربند شو، او په همدې نظربندۍ کې مړ شو؛ د ځینو روایتونو له مخې ووژل شو.'))])
    r2 = rec(t, 11, 61, 34, [61])
    u = Builder()
    u.h('Abu Abdullah Muhammad bin Ja\'far al-Mu\'tazz billah', 'ابوعبداللہ محمد بن جعفر معتز باللہ', 'ابوعبدالله محمد بن جعفر معتز بالله')
    u.p('865 CE to 869 CE', '۸۶۵ء تا ۸۶۹ء', '۸۶۵ع تر ۸۶۹ع')
    S(u, [(None, ('According to the agreement Mu\'tazz billah ascended the throne and the series of his allegiance began. The majority gave him allegiance, but several walis had refused allegiance. Skirmishes kept taking place with them. Among them the walis of Palestine, Egypt, Syria and Isfahan were at the top of the list.', 'معاہدے کے مطابق معتز باللہ تخت نشین ہوا اور اس کی بیعت کا سلسلہ شروع ہوا۔ اکثریت نے اس کی بیعت کر لی لیکن کئی والیوں نے بیعت سے انکار کر دیا تھا۔ ان کے ساتھ جھڑپیں ہوتی رہیں۔ ان میں فلسطین، مصر، شام اور اصفہان کے والی سرِ فہرست تھے۔', 'د تړون له مخې معتز بالله پر تخت کېناست او د هغه د بیعت لړۍ پیل شوه. اکثریت بیعت وکړ، خو ډېرو والیانو له بیعت انکار کړی و؛ ورسره نښتې روانې وې؛ په هغوی کې د فلسطین، مصر، شام او اصفهان والیان په سر کې وو.')),
          (('Revolt of the army in Baghdad:', 'بغداد میں فوج کی بغاوت:', 'په بغداد کې د پوځ بغاوت'),
           ('Because of the political situation of the country deteriorating, the treasury had become empty. Therefore the army could not be given salary for several months. The army revolted, but ultimately they were dispersed and the situation was brought under control.', 'ملک کی سیاسی حالت خراب ہونے کی وجہ سے خزانہ خالی ہو گیا تھا۔ اس لئے فوج کو کئی ماہ تک تنخواہ نہ دی جا سکی۔ فوج نے بغاوت کر دی لیکن آخر کار ان کو منتشر کر دیا گیا۔ اور حالات پر قابو پا لیا گیا۔', 'د هېواد د سیاسي حالت د خرابېدو له امله خزانه تشه شوې وه؛ نو پوځ ته څو میاشتې معاش ورنشو کړای. پوځ بغاوت وکړ، خو بالاخره خپاره شول او پر حالاتو واک وموندل شو.')),
          (('Revolt of the Kharijite chief Musawir:', 'خارجی سردار مساور کی بغاوت:', 'د خارجي مشر مساور بغاوت'),
           ('The Kharijite chief Musawir revolted. Expeditions were sent to confront him, but there was no success, and Musawir went on achieving further successes.', 'خارجی سردار مساور نے بغاوت کر دی۔ اس کے مقابلے کے لئے مہمات روانہ کی گئیں لیکن کامیابی نہ ہوئی اور مساور مزید کامیابیاں حاصل کرتا گیا۔', 'خارجي مشر مساور بغاوت وکړه؛ د هغه مقابلې ته لښکرې ولېږل شوې، خو بریالیتوب ونشو، او مساور نورې بریاوې ترلاسه کړې.')),
          (('Establishment of the Saffarid government:', 'صفاری حکومت کا قیام:', 'د صفاري حکومت جوړېدل'),
           ('The caliph had become a puppet in the hands of the Turks. The Turks dominated power. The Saffarids took possession of the regions of Sistan and Iran and established their own government.', 'خلیفہ ترکوں کے ہاتھوں میں کٹھ پتلی بنا ہوا تھا۔ ترک اقتدار پر چھائے ہوئے تھے۔ صفاریوں نے سیستان اور ایران کے علاقوں پر قبضہ کر کے اپنی حکومت قائم کر لی۔', 'خلیفه د ترکانو په لاس کې ګوډاګی شوی و؛ ترکان پر واک خپاره وو. صفاریانو د سیستان او ایران پر سیمو قبضه وکړه او خپل حکومت یې جوړ کړ.'))])
    BOOK.save(34, [(11, r1), (11, r2), (12, rec(u, 12, 61, 34, [61], first=True))], complete_units=[11], issues=[{'id': 'ihist12-pdf034', 'unit': 11, 'printedPage': 60,
               'description': 'Lesson 11 (Muntasir, with Musta\'in) opens under "باب: 5" on p.60; Lesson 12 (Mu\'tazz) begins on p.61. Printed spellings kept ("آتاش" / "اتامش"). Student marks excluded.'}])


if __name__ == '__main__':
    p34()
