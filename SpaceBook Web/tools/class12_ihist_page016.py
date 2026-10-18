"""Islamic History XII PDF16: p.22 — Lesson 3 exercise blanks (end); p.23 — Lesson 4 Mahdi (start). Run: python class12_ihist_page016.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L


def p16():
    b = Builder()
    L(b, [('c. In ______ AH Hulagu attacked Baghdad.', 'ج۔ ______ھ میں ہلاکو نے بغداد پر حملہ کیا۔', 'ج. په ______ هـ کې هلاکو پر بغداد حمله وکړه.'),
          ('d. Abdullah bin Ali was appointed governor of ______.', 'د۔ عبداللہ بن علی کو ______ کا گورنر مقرر کیا گیا۔', 'د. عبدالله بن علي د ______ والي وټاکل شو.'),
          ('e. ______ was the governor of Iraq on behalf of Marwan.', 'ہ۔ ______ مروان کی طرف سے عراق کا گورنر تھا۔', 'ه. ______ د مروان له لوري د عراق والي و.'),
          ('f. Saffah appointed ______ the first vizier.', 'و۔ ______ کو سفاح نے پہلا وزیر مقرر کیا', 'و. سفاح ______ لومړی وزیر وټاکه.'),
          ('g. Saffah died in ______ Hijri.', 'ز۔ سفاح ______ ہجری میں فوت ہوا۔', 'ز. سفاح په ______ هجري کې مړ شو.'),
          ('h. Saffah had appointed ______ heir-apparent.', 'ح۔ سفاح نے ______ کو ولی عہد مقرر کیا تھا۔', 'ح. سفاح ______ ولیعهد ټاکلی و.'),
          ('i. At the time of Saffah\'s death Mansur was in ______.', 'ط۔ سفاح کی موت کے وقت منصور ______ میں تھا۔', 'ط. د سفاح د مړینې پر مهال منصور په ______ کې و.'),
          ('j. Abdullah bin Ali revolted in ______.', 'ی۔ عبداللہ بن علی نے ______ میں بغاوت کی۔', 'ی. عبدالله بن علي په ______ کې بغاوت وکړ.'),
          ('k. The Kharijite chief Hassan bin Mujahid revolted ______.', 'ک۔ خارجی سردار حسان بن مجاہد نے ______ بغاوت کی۔', 'ک. خارجي مشر حسان بن مجاهد ______ بغاوت وکړه.'),
          ('l. ______ conquered the regions of Kohistan, Tabaristan and Damavand.', 'ل۔ ______ نے کوہستان، طبرستان اور دماند کے علاقے فتح کئے۔', 'ل. ______ د کوهستان، طبرستان او دماوند سیمې فتح کړې.'),
          ('m. Mansur announced religious ______.', 'م۔ منصور نے مذہبی ______ کا اعلان کیا۔', 'م. منصور د مذهبي ______ اعلان وکړ.'),
          ('n. ______ established the government of the Banu Umayyah in Spain.', 'ن۔ ______ نے سپین میں بنو امیہ کی حکومت قائم کی۔', 'ن. ______ په هسپانیه کې د بنو امیه حکومت جوړ کړ.'),
          ('s. Mansur made ______ vizier.', 'س۔ ______ کو منصور نے وزیر بنایا۔', 'س. منصور ______ وزیر کړ.'),
          ('\'ayn. The governors of provinces were called ______.', 'ع۔ صوبوں کے گورنر ______ کہلاتے تھے۔', 'ع. د ولایتونو والیانو ته ______ ویل کېده.'),
          ('f. Besides the vizier Mansur established the post of ______.', 'ف۔ منصور نے وزیر کے علاوہ ______ کا عہدہ قائم کیا۔', 'ف. منصور له وزیر سربېره د ______ څوکۍ جوړه کړه.'),
          ('s. Saffah had appointed ______ second heir-apparent.', 'ص۔ سفاح نے ______ کو دوسرا ولی عہد مقرر کیا تھا۔', 'ص. سفاح ______ دویم ولیعهد ټاکلی و.'),
          ('q. Mansur was ______ of fasting and prayer.', 'ق۔ منصور صوم و صلوٰۃ کا ______ تھا۔', 'ق. منصور د روژې او لمانځه ______ و.'),
          ('r. ______ himself used to lead the Fajr prayer.', 'ر۔ ______ نمازِ فجر خود پڑھاتا تھا۔', 'ر. ______ پخپله د سهار لمونځ ورکاوه.')])
    r1 = rec(b, 3, 22, 16, [22], kind='exercise')
    t = Builder()
    t.p('Chapter: 2', 'باب: 2', 'باب: ۲')
    t.table('ihist12-ch2-caliphs', ['Caliph', 'Period'], [['Mahdi', '775 CE to 785 CE'], ['Hadi', '785 CE to 786 CE'], ['Harun al-Rashid', '786 CE to 809 CE']],
            ['خلیفہ', 'دور'], ['خلیفه', 'دوره'], [['مہدی', '۷۷۵ء تا ۷۸۵ء'], ['ہادی', '۷۸۵ء تا ۷۸۶ء'], ['ہارون الرشید', '۷۸۶ء تا ۸۰۹ء']],
            [['مهدي', '۷۷۵ع تر ۷۸۵ع'], ['هادي', '۷۸۵ع تر ۷۸۶ع'], ['هارون الرشید', '۷۸۶ع تر ۸۰۹ع']])
    t.h('Mahdi', 'مہدی', 'مهدي')
    t.p('775 CE to 785 CE', '۷۷۵ء تا ۷۸۵ء', '۷۷۵ع تر ۷۸۵ع')
    S(t, [(('Introduction and accession:', 'تعارف و تخت نشینی:', 'پېژندنه او پر تخت کېناستل'),
           ('According to Saffah\'s testament, \'Isa bin Musa ought to have received the government. But Mansur had forcibly deprived him of the throne and appointed his own son Abu Abdullah Muhammad as his successor. So after Mansur\'s death Abu Abdullah Muhammad Mahdi ascended the throne. Abu Abdullah was a soft-hearted and generous caliph. He had spacious mosques built in big cities. His era was an era of prosperity. Trade progressed considerably. People were given pensions. The postal system was improved. A network of roads was laid in the country.', 'سفاح کی وصیت کے مطابق عیسیٰ بن موسیٰ کو حکومت ملنی چاہیے تھی۔ لیکن منصور نے زبردستی اسے تخت سے محروم کر کے اپنے بیٹے ابوعبداللہ محمد کو اپنا جانشین مقرر کر لیا تھا۔ چنانچہ منصور کی موت کے بعد ابوعبداللہ محمد مہدی تخت نشین ہوا۔ ابوعبداللہ نرم دل اور سخی خلیفہ تھا۔ بڑے بڑے شہروں میں وسیع مسجدیں بنوائیں۔ اس کا دور خوشحالی کا دور تھا۔ تجارت میں کافی ترقی ہوئی۔ لوگوں کو پنشن دی گئیں۔ ڈاک کا نظام بہتر بنایا گیا۔ ملک میں سڑکوں کا جال بچھا دیا گیا۔', 'د سفاح د وصیت له مخې حکومت باید عیسی بن موسی ته رسېدلی وای. خو منصور په زور هغه له تخته بې‌برخې کړ او خپل زوی ابوعبدالله محمد یې ځای‌ناستی وټاکه. نو د منصور له مړینې وروسته ابوعبدالله محمد مهدي پر تخت کېناست. ابوعبدالله نرم‌زړی او سخي خلیفه و؛ په لویو ښارونو کې یې پراخ جوماتونه جوړ کړل. دوره یې د هوساینې دوره وه؛ سوداګرۍ ښه پرمختګ وکړ؛ خلکو ته تقاعدي معاشونه ورکړل شول؛ د پوستې نظام ښه شو؛ او په هېواد کې د سړکونو جال وغوړول شو.')),
          (('Release of the family of Ali:', 'آلِ علی کی رہائی:', 'د علي د کورنۍ خوشې کول'),
           ('Mansur was strongly against the Ahl al-Bayt. He had treated them very harshly. Mahdi released them from the prisons. He returned their confiscated properties to them.', 'منصور اہلِ بیت کے سخت خلاف تھا۔ اس نے ان پر بہت سختیاں کی تھیں۔ مہدی نے ان کو جیلوں سے رہا کر دیا۔ ان کی ضبط شدہ جائیدادیں ان کو واپس دے دیں۔', 'منصور د اهل بیت سخت مخالف و او ډېرې سختۍ یې پرې کړې وې. مهدي هغوی له زندانونو خوشې کړل او ضبط شوي جایدادونه یې ورته بېرته ورکړل.'))])
    BOOK.save(16, [(3, r1), (4, rec(t, 4, 23, 16, [23], first=True))], complete_units=[3], issues=[{'id': 'ihist12-pdf016', 'unit': 3, 'printedPage': 22,
               'description': 'p.22: all blanks are filled in by a student in handwriting (e.g. "656", "شام", "136") — excluded; blanks rendered empty (no printed key). Lesson 4 (Mahdi) opens on p.23 under the book heading "باب: 2" with a period chart (structured table). Student marks on p.23 excluded.'}])


if __name__ == '__main__':
    p16()
