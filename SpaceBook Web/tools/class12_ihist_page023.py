"""Islamic History XII PDF23: pp.38–39 — exercise of lessons 4–5 (choice items d–e, Q6 blanks). Run: python class12_ihist_page023.py"""
from class12_ihist_common import BOOK, Builder, rec, L


def p23():
    b = Builder()
    L(b, [('d. The era of Harun al-Rashid was ______. (of disorder, glorious)', 'د۔ ہارون الرشید کا دور ______ تھا۔ (انتشار کا، شاندار)', 'د. د هارون الرشید دوره ______ وه. (د ګډوډۍ، ښکلې)'),
          ('e. Harun ______ the Barmakids with his own hands. (populated, ruined)', 'ہ۔ ہارون نے برامکہ کو اپنے ہاتھوں ______ کیا۔ (آباد، برباد)', 'ه. هارون برامکه په خپلو لاسونو ______ کړل. (ودان، برباد)')])
    b.p('6. Fill in the following blanks.', '۶۔ مندرجہ ذیل خالی جگہیں پر کریں۔', '۶. لاندې تشې ډکې کړئ.')
    L(b, [('a. After Mansur\'s death ______ ascended the throne.', 'الف۔ منصور کی وفات کے بعد ______ تخت نشین ہوا۔', 'الف. د منصور له مړینې وروسته ______ پر تخت کېناست.'),
          ('b. Mahdi had the ______ released from prisons.', 'ب۔ مہدی نے ______ کو جیلوں سے رہا کروایا۔', 'ب. مهدي ______ له زندانونو خوشې کړل.'),
          ('c. The meaning of zand is ______.', 'ج۔ زند کے معنی ہیں ______', 'ج. د زند مانا ______ ده.'),
          ('d. Hakam bin Hakim, the katib of ______, had claimed divinity.', 'د۔ ______ کے کاتب حکم بن حاکم نے خدائی کا دعویٰ کیا تھا۔', 'د. د ______ کاتب حکم بن حاکم د خدايي دعوه کړې وه.'),
          ('e. ______ defeated the Romans and obtained considerable spoils.', 'ہ۔ ______ رومیوں کو شکست دے کر کافی مالِ غنیمت حاصل کیا۔', 'ه. ______ رومیان مات کړل او ډېره غنیمت یې ترلاسه کړه.'),
          ('f. ______ crushed the revolt of Egypt.', 'و۔ مصر کی بغاوت کو ______ نے کچل دیا۔', 'و. د مصر بغاوت ______ وځپله.'),
          ('g. Ya\'qub was basically a ______.', 'ز۔ یعقوب بنیادی طور پر ______ تھا۔', 'ز. یعقوب په اصل کې ______ و.'),
          ('h. Mahdi\'s era was in fact an era of ______.', 'ح۔ مہدی کا دور دراصل ______ کا دور تھا۔', 'ح. د مهدي دوره په اصل کې د ______ دوره وه.'),
          ('i. Mahdi had a magnificent palace built on the bank of the river ______.', 'ط۔ مہدی نے دریائے ______ کے کنارے شاندار محل تعمیر کروایا۔', 'ط. مهدي د ______ سیند پر غاړه ښکلې ماڼۍ جوړه کړه.'),
          ('j. A new ______ was established in \'Isa-abad.', 'ی۔ عیسیٰ آباد میں نئی ______ قائم کی گئی۔', 'ی. په عیسی‌اباد کې نوې ______ جوړه شوه.'),
          ('k. Harun al-Rashid ruled for approximately ______ years.', 'گ۔ ہارون الرشید نے تقریباً ______ سال حکومت کی۔', 'ګ. هارون الرشید نږدې ______ کاله حکومت وکړ.'),
          ('l. Harun made his tutor ______ prime minister.', 'ل۔ ہارون نے اپنے اتالیق ______ کو وزیرِ اعظم بنایا۔', 'ل. هارون خپل استاد ______ لومړی وزیر کړ.'),
          ('m. In Constantinople Queen ______ was ruling.', 'م۔ قسطنطنیہ میں ملکہ ______ حکمران تھی۔', 'م. په قسطنطنیه کې ملکه ______ واکمنه وه.'),
          ('n. ______ wrote an insulting letter to Harun.', 'ن۔ ______ نے ہارون کو توہین آمیز خط لکھا۔', 'ن. ______ هارون ته سپکاوی‌ډک لیک ولیکه.'),
          ('s. Harun, influenced by his wife ______, made a wrong decision.', 'س۔ ہارون نے اپنی بیوی ______ سے متاثر ہو کر غلط فیصلہ کیا۔', 'س. هارون د خپلې مېرمنې ______ تر اغېز لاندې غلطه پرېکړه وکړه.'),
          ('\'ayn. The Barmakids remained in power for approximately ______ years.', 'ع۔ برامکہ تقریباً ______ سال تک برسرِ اقتدار رہے۔', 'ع. برامکه نږدې ______ کاله واک کې وو.'),
          ('f. ______ of the Barmakids was killed.', 'ف۔ برامکہ کے ______ کو قتل کر دیا گیا۔', 'ف. د برامکه ______ ووژل شو.')])
    r1 = rec(b, 5, 38, 23, [38], kind='exercise')
    t = Builder()
    L(t, [('s. ______ was the mortal enemy of the Barmakids.', 'ص۔ ______ برامکہ کا جانی دشمن تھا۔', 'ص. ______ د برامکه ځاني دښمن و.'),
          ('q. Harun used to offer ______ rak\'ahs of nafl daily.', 'ق۔ ہارون روزانہ ______ رکعت نفل پڑھتا تھا۔', 'ق. هارون هره ورځ ______ رکعته نفل لمونځ کاوه.'),
          ('r. In front of ______ a cup of water was brought for Harun.', 'ر۔ ______ کے سامنے ہارون کے لئے پانی کا ایک پیالہ لایا گیا۔', 'ر. د ______ مخې ته هارون ته د اوبو یوه پیاله راوړل شوه.')])
    BOOK.save(23, [(5, r1), (5, rec(t, 5, 39, 23, [39], kind='exercise'))], complete_units=[5], issues=[{'id': 'ihist12-pdf023', 'unit': 5, 'printedPage': 38,
               'description': 'Pages 36–37 (end of Harun\'s character section and the first exercise questions 1–5 and choice items a–c) are missing from the scan — not available in any source here. On pp.38–39 every blank and choice is filled in by a student in handwriting — excluded; blanks rendered empty (no printed key). Items q and r refer to content on the missing pp.36–37.'}])


if __name__ == '__main__':
    p23()
