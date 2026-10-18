"""Islamic History XII PDF110: p.210 — exercise of lesson 39 (end); p.211 — Lesson 40 Buildings of Andalus: al-Rusafah, the Jami' Mosque of Cordoba (start). Run: python class12_ihist_page110.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L

YN = (' (yes/no)', ' (ہاں/نہیں)', ' (هو/نه)')


def yn(items):
    return [(e + YN[0], u + YN[1], p + YN[2]) for e, u, p in items]


def p110():
    b = Builder()
    L(b, yn([('m. Ibn Khaldun laid the foundation of the philosophy of history.', 'م: ابن خلدون نے فلسفہ تاریخ کی بنیاد ڈالی۔', 'م. ابن خلدون د تاریخ د فلسفې بنسټ کېښود.'),
             ('n. Ibn al-Khatib belonged to Iran.', 'ن: ابن الخطیب کا تعلق ایران سے تھا۔', 'ن. ابن الخطیب له ایرانه و.'),
             ('s. Ziryab was a pupil of the famous musician Ishaq al-Mawsili.', 'س: زریاب مشہور موسیقار اسحاق موصلی کا شاگرد تھا۔', 'س. زریاب د مشهور موسیقار اسحاق موصلي شاګرد و.'),
             ('t. Ibn Rushd was appointed court physician in Marrakesh.', 'ع: ابن رشد مراکش میں درباری طبیب مقرر ہوا۔', 'ع. ابن رشد په مراکش کې درباري طبیب وټاکل شو.')]))
    r1 = rec(b, 39, 210, 110, [210], kind='exercise')
    t = Builder()
    t.p('Chapter: 9', 'باب: 9', 'باب: ۹')
    t.h('Buildings of Andalus', 'عماراتِ اُندلسیہ', 'د اندلس ودانۍ')
    S(t, [(('1. Al-Rusafah:', '۱۔ رصافہ:', '۱. رصافه'),
           ('The famous ruler of the Banu Umayyah, Hisham, had built a palace in Syria. The name of this palace was al-Rusafah. When Abd al-Rahman al-Dakhil came to power in Andalus he had a palace of the same style built outside Cordoba. Its name too was kept al-Rusafah. This palace was made more beautiful with orchards. Al-Dakhil\'s sister Umm al-Asbagh kept sending beautiful fruit trees for al-Dakhil from the garden of Syria. Al-Dakhil loved only one date-palm tree of the garden immensely. Around al-Rusafah the population kept increasing, through which this city took a beautiful form and became the centre of people\'s attention. Abu Abdullah bin al-Rafa has praised it greatly in his verses.', 'بنو امیہ کے مشہور حکمران ہشام نے شام میں ایک محل بنوایا تھا۔ اس محل کا نام رصافہ تھا۔ عبدالرحمان الداخل جب اندلس میں برسرِ اقتدار آیا تو اس نے قرطبہ کے باہر اسی طرز کا محل بنوایا۔ اس کا نام بھی رصافہ رکھا گیا۔ اس محل کو باغات سے مزید خوبصورت بنایا گیا۔ الداخل کی بہن اُمّ الاصبغ شام کے باغ سے الداخل کے لئے خوبصورت پھل دار درخت بھیجتی رہتی تھی۔ کھجور کے صرف ایک درخت کے باغ سے الداخل کو بے حد محبت تھی۔ رصافہ کے اردگرد آبادی بڑھتی گئی جس سے اس شہر نے ایک حسین و جمیل شکل اختیار کر لی اور لوگوں کی توجہ کا مرکز بن گیا۔ ابوعبداللہ بن الرفا نے اپنے اشعار میں اس کی خوب تعریف کی ہے۔', 'د بنو امیه مشهور واکمن هشام په شام کې یوه ماڼۍ جوړه کړې وه چې نوم یې «رصافه» و. کله چې عبدالرحمن الداخل په اندلس کې واک ته ورسېد، د قرطبې بهر یې د همغه طرز ماڼۍ جوړه کړه او نوم یې هم «رصافه» کېښود؛ دا ماڼۍ په باغونو لا ښکلې شوه. د الداخل خور ام الاصبغ به د شام له باغه د الداخل لپاره ښکلې مېوه‌لرونکې ونې لېږلې؛ الداخل د باغ له یوازې یوې خرما ونې سره بې‌حده مینه درلوده. د رصافې شاوخوا نفوس زیاتېده چې له امله یې دې ښار ښکلې بڼه غوره کړه او د خلکو د پام مرکز شو. ابوعبدالله بن الرفا په خپلو شعرونو کې یې ښه ستاینه کړې.')),
          (('2. The Jami\' Mosque of Cordoba:', '۲۔ جامع مسجد قرطبہ:', '۲. د قرطبې جامع جومات'),
           ('On every inch of the land of Andalus memorials of the Muslims exist, but alas the sound of the adhan is not heard. The mosque of Cordoba even today holds in its lap the story of the rise and fall of the Muslims. Its beauty cannot be described in words. This is that historic mosque in which our national poet Allama Iqbal, giving the adhan, offered the prayer and wrote verses in its praise. Abd al-Rahman al-Dakhil, in his …', 'سرزمینِ اندلس کے چپے چپے پر مسلمانوں کی یادگاریں موجود ہیں لیکن افسوس کہ اذان کی آواز سنائی نہیں دیتی۔ مسجد قرطبہ آج بھی مسلمانوں کے عروج و زوال کی داستان اپنے دامن میں سمیٹے ہوئے ہے۔ اس کے حسن کو الفاظ میں بیان نہیں کیا جا سکتا۔ یہ وہ تاریخی مسجد ہے جس میں ہمارے قومی شاعر علامہ اقبال نے اذان دے کر نماز پڑھی اور اس کی شان میں اشعار لکھے۔ اس کی تعمیر عبدالرحمان الداخل نے اپنی', 'د اندلس د ځمکې په هره لوېشت کې د مسلمانانو یادګارونه شته، خو افسوس چې د اذان غږ نه اورېدل کېږي. د قرطبې جومات نن هم د مسلمانانو د عروج او زوال کیسه په خپله لمن کې لري؛ ښکلا یې په الفاظو نه بیانېږي. دا هغه تاریخي جومات دی چې زموږ ملي شاعر علامه اقبال پکې اذان وکړ، لمونځ یې وکړ او د هغه په شان کې یې شعرونه ولیکل. د هغه جوړونه عبدالرحمن الداخل د خپل …'))])
    BOOK.save(110, [(39, r1), (40, rec(t, 40, 211, 110, [211], first=True))], complete_units=[39], issues=[{'id': 'ihist12-pdf110', 'unit': 40, 'printedPage': 211,
               'description': 'p.210 has only the last four items of the exercise; the rest of the page is blank (faint show-through excluded). Lesson 40 opens on p.211 under "باب: 9". Printed "کھجور کے صرف ایک درخت کے باغ سے" kept. Finger in the scan excluded.'}])


if __name__ == '__main__':
    p110()
