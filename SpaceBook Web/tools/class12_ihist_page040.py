"""Islamic History XII PDF40: p.72 — exercise blanks j–n (end); p.73 — Lesson 17 al-Muti' lillah (start). Run: python class12_ihist_page040.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L


def p40():
    b = Builder()
    L(b, [('j. In Mu\'nis\'s place ______ was appointed vizier.', 'ی: مونس کی جگہ ______ کو وزیر مقرر کیا گیا۔', 'ی. د مونس پر ځای ______ وزیر وټاکل شو.'),
          ('k. Sima\'s forces arrested ______.', 'ک: سیما کی فوجوں نے ______ کو گرفتار کر لیا۔', 'ک. د سیما پوځونو ______ ونیو.'),
          ('l. After al-Radi ______ was selected caliph.', 'ل: راضی کے بعد ______ خلیفہ منتخب ہوا۔', 'ل. له راضي وروسته ______ خلیفه وټاکل شو.'),
          ('m. Bajkam was killed at the hands of a ______.', 'م: بجکم ایک ______ کے ہاتھوں مارا گیا۔', 'م. بجکم د یوه ______ په لاس ووژل شو.'),
          ('n. Only in the khutbah the name of ______ was mentioned.', 'ن: صرف خطبے میں ______ کا نام لیا جاتا تھا۔', 'ن. یوازې په خطبه کې د ______ نوم اخیستل کېده.')])
    r1 = rec(b, 16, 72, 40, [72], kind='exercise')
    t = Builder()
    t.p('Chapter: 7', 'باب: 7', 'باب: ۷')
    t.h('Abu al-Qasim Fadl bin Muqtadir al-Muti\' lillah', 'ابوالقاسم فضل بن مقتدر مطیع اللہ', 'ابوالقاسم فضل بن مقتدر مطیع لله')
    t.p('945 CE to 974 CE', '۹۴۵ء تا ۹۷۴ء', '۹۴۵ع تر ۹۷۴ع')
    S(t, [(None, ('The Buyids were Shi\'a. Their sympathies were with the Ahl al-Bayt; so after deposing Mustakfi, Mu\'izz al-Dawlah wanted to end the Abbasid government and establish an \'Alawi government. But under political expediency he refrained from this idea, and finding Fadl bin Muqtadir of the Abbasid family, he made him caliph in 334 AH. His age was 34 years. Mustakfi too was blinded. Now in Baghdad there were three blind deposed caliphs (al-Qahir, al-Muttaqi, al-Mustakfi).', 'بویہ شیعہ تھے۔ ان کی ہمدردیاں اہلِ بیت کے ساتھ تھیں، چنانچہ مستکفی کو معزول کرنے کے بعد معز الدولہ نے عباسی حکومت ختم کر کے علوی حکومت قائم کرنا چاہی۔ لیکن سیاسی مصلحت کے تحت وہ اس خیال سے باز رہا اور خاندانِ عباسیہ کے فضل بن مقتدر کو ڈھونڈ کر ۳۳۴ھ میں خلیفہ بنا دیا۔ اس کی عمر ۳۴ سال تھی۔ مستکفی کو بھی اندھا کر دیا گیا۔ اب بغداد میں تین اندھے معزول خلفاء تھے۔ (قاہر، متقی، مستکفی)', 'بویه شیعه وو؛ همدردۍ یې له اهل بیت سره وې. نو د مستکفي له لرې کولو وروسته معز الدوله غوښتل عباسي حکومت ختم او علوي حکومت جوړ کړي؛ خو د سیاسي مصلحت له مخې له دې فکره تېر شو، او د عباسي کورنۍ فضل بن مقتدر یې پیدا کړ او په ۳۳۴ هـ کې یې خلیفه کړ؛ عمر یې ۳۴ کاله و. مستکفي هم ړوند کړای شو. اوس په بغداد کې درې ړانده لرې شوي خلفاء وو (قاهر، متقي، مستکفي).')),
          (None, ('Between the Banu Buyah (Shi\'a) and the Banu Hamdan (Sunni) the series of differences and battles continued for a considerable period, and bloody skirmishes kept taking place. At last peace was made. During this time, in 338 AH, \'Imran bin Shahin established a royal state in Batihah. In 356 AH Mu\'izz al-Dawlah set out to confront \'Imran, but fell ill and died. After his death his son Bakhtiyar ascended the throne. He was very pleasure-seeking, a lover of women and wine. He took no interest in the works of government. He made \'Abbas bin Husayn vizier, but later confiscated his property, deposed him and made Muhammad vizier.', 'بنی بویہ (شیعہ) اور بنی حمدان (سنی) کے درمیان کافی عرصہ تک اختلافات اور معرکہ آرائی کا سلسلہ جاری رہا اور خونریز جھڑپیں ہوتی رہیں۔ آخر کار صلح ہو گئی۔ اسی دوران ۳۳۸ھ میں عمران بن شاہین نے بطیحہ میں شاہی ریاست قائم کر لی۔ ۳۵۶ھ میں معز الدولہ عمران کے مقابلے کے لئے روانہ ہوا لیکن بیمار ہو کر فوت ہو گیا۔ اس کی وفات کے بعد اس کا بیٹا بختیار تخت نشین ہوا۔ وہ بڑا عیاش تھا۔ عورت اور شراب کا دلدادہ تھا۔ حکومت کے کاموں میں کوئی دلچسپی نہیں لیتا تھا۔ عباس بن حسین کو وزیر بنایا لیکن بعد میں اس کی جائیداد ضبط کر کے اسے معزول کیا اور محمد کو وزیر بنا لیا۔', 'د بني بویه (شیعه) او بني حمدان (سني) ترمنځ ډېره موده د اختلافونو او جګړو لړۍ روانه وه او خونړۍ نښتې کېدې؛ بالاخره روغه وشوه. په همدې موده کې په ۳۳۸ هـ کې عمران بن شاهین په بطیحه کې شاهي دولت جوړ کړ. په ۳۵۶ هـ کې معز الدوله د عمران مقابلې ته روان شو، خو ناروغ او مړ شو. له مړینې وروسته یې زوی بختیار پر تخت کېناست؛ ډېر عیاش او د ښځو او شرابو مینه‌وال و؛ د حکومت په کارونو کې یې لېوالتیا نه درلوده. عباس بن حسین یې وزیر کړ، خو وروسته یې جایداد ضبط او لرې کړ او محمد یې وزیر کړ.')),
          (('Roman attacks:', 'رومی حملے:', 'رومي حملې'),
           ('As long as the Muslim rulers remained powerful, the Romans maintained silence …', 'مسلمان حکمران جب تک طاقتور رہے تو رومیوں نے خاموشی اختیار کئے رکھی۔', 'تر څو چې مسلمان واکمنان پیاوړي وو، رومیانو چوپتیا غوره کړې وه …'))])
    BOOK.save(40, [(16, r1), (17, rec(t, 17, 73, 40, [73], first=True))], complete_units=[16], issues=[{'id': 'ihist12-pdf040', 'unit': 16, 'printedPage': 72,
               'description': 'p.72 exercise blanks filled in by a student (e.g. "محمد بن قاسم", "ابراہیم", "شاگرد", "خلیفہ") — excluded; blanks rendered empty. p.72 otherwise blank. Lesson 17 (Muti\') opens on p.73 under "باب: 7".'}])


if __name__ == '__main__':
    p40()
