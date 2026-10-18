"""Islamic History XII PDF47: pp.86–87 — exercise of lessons 21–22. Run: python class12_ihist_page047.py"""
from class12_ihist_common import BOOK, Builder, rec, L

YN = (' (yes/no)', ' (ہاں/نہیں)', ' (هو/نه)')


def yn(items):
    return [(e + YN[0], u + YN[1], p + YN[2]) for e, u, p in items]


def p47():
    b = Builder()
    b.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    L(b, [('1. Write a short note on Fadl bin Mustazhir.', '۱۔ فضل بن مستظہر پر مختصر نوٹ تحریر کریں۔', '۱. پر فضل بن مستظهر لنډ یادښت ولیکئ.'),
          ('2. State the services of Ahmad bin Mustadi\'.', '۲۔ احمد بن مستضی کی خدمات بیان کریں۔', '۲. د احمد بن مستضيء خدمات بیان کړئ.')])
    b.p('3. Fill in the blanks.', '۳۔ خالی جگہیں پر کریں۔', '۳. تشې ډکې کړئ.')
    L(b, [('a. Mustazhir in his lifetime had nominated his son ______ as heir-apparent.', 'الف: مستظہر نے اپنی زندگی میں اپنے بیٹے ______ کو ولی عہد نامزد کیا تھا۔', 'الف. مستظهر په خپل ژوند کې خپل زوی ______ ولیعهد ټاکلی و.'),
          ('b. The ______ did not want the caliph to restore his position.', 'ب: ______ نہیں چاہتے تھے کہ خلیفہ اپنی حیثیت بحال کرے۔', 'ب. ______ نه غوښتل چې خلیفه خپل مقام بحال کړي.'),
          ('c. ______ too had become puppets in the hands of the amirs and viziers.', 'ج: ______ بھی امراء اور وزراء کے ہاتھوں میں کٹھ پتلی بنے ہوئے تھے۔', 'ج. ______ هم د امیرانو او وزیرانو په لاس کې ګوډاګي شوي وو.'),
          ('d. In this very era ______ arose, which took the Islamic kingdoms into its grip.', 'د: اسی دور میں ______ اٹھا جس نے اسلامی مملکتوں کو اپنی لپیٹ میں لے لیا۔', 'د. په همدې دوره کې ______ راپورته شو چې اسلامي هېوادونه یې په غېږ کې ونیول.')])
    b.p('4. Answer in yes/no.', '۴۔ ہاں/نہیں میں جواب دیں۔', '۴. په هو/نه کې ځواب ورکړئ.')
    L(b, yn([('a. Abu Mansur ascended the throne in 512 AH.', 'الف: ۵۱۲ھ میں ابومنصور تخت نشین ہوا۔', 'الف. په ۵۱۲ هـ کې ابومنصور پر تخت کېناست.'),
             ('b. Abu Mansur\'s age was 27 years.', 'ب: ابومنصور کی عمر ۲۷ سال تھی۔', 'ب. د ابومنصور عمر ۲۷ کاله و.'),
             ('c. Abu Mansur wanted to get out of the Seljuq snare.', 'ج: ابومنصور سلجوقی پھندے سے نکلنا چاہتا تھا۔', 'ج. ابومنصور غوښتل له سلجوقي جاله ووځي.'),
             ('d. In 525 AH Sultan Mahmud passed away.', 'د: ۵۲۵ھ میں سلطان محمود کا انتقال ہو گیا۔', 'د. په ۵۲۵ هـ کې سلطان محمود وفات شو.'),
             ('e. The founder of the Khwarazmi government was Khwarazm Shah.', 'ہ: خوارزمی حکومت کا بانی خوارزم شاہ تھا۔', 'ه. د خوارزمي حکومت بنسټګر خوارزم شاه و.'),
             ('f. Khwarazm Shah defeated Sultan Sanjar in 536 CE.', 'و: خوارزم شاہ نے ۵۳۶ء میں سلطان سنجر کو شکست دی۔', 'و. خوارزم شاه په ۵۳۶ع کې سلطان سنجر ته ماتې ورکړه.'),
             ('g. Nur al-Din Zangi kept fighting against the Christians.', 'ز: نور الدین زنگی عیسائیوں کے خلاف لڑتا رہا۔', 'ز. نورالدین زنګي د عیسویانو پر خلاف جنګېده.'),
             ('h. After Muqtafi his son Yusuf ascended the throne.', 'ح: مقتفی کے بعد اس کا بیٹا یوسف تخت نشین ہوا۔', 'ح. له مقتفي وروسته زوی یې یوسف پر تخت کېناست.'),
             ('i. The Fatimid caliphs too had become puppets in the hands of the amirs and viziers.', 'ط: فاطمی خلفاء بھی امراء اور وزراء کے ہاتھوں میں کٹھ پتلی بن گئے تھے۔', 'ط. فاطمي خلفاء هم د امیرانو او وزیرانو په لاس کې ګوډاګي شوي وو.')]))
    r1 = rec(b, 22, 86, 47, [86], kind='exercise')
    t = Builder()
    L(t, yn([('j. In Egypt Sultan Salah al-Din Ayyubi established a government.', 'ی: مصر میں سلطان صلاح الدین ایوبی نے حکومت قائم کر لی۔', 'ی. په مصر کې سلطان صلاح الدین ایوبي حکومت جوړ کړ.'),
             ('k. After Mustadi\' his son Ahmad ascended the throne.', 'ک: مستضی کے بعد اس کا بیٹا احمد تخت نشین ہوا۔', 'ک. له مستضيء وروسته زوی یې احمد پر تخت کېناست.'),
             ('l. In September 1187 CE Bayt al-Maqdis was handed over to the Muslims.', 'ل: ستمبر ۱۱۸۷ء میں بیت المقدس مسلمانوں کے حوالے کیا گیا۔', 'ل. د ۱۱۸۷ع په سپتمبر کې بیت المقدس مسلمانانو ته وسپارل شو.'),
             ('m. The Muslim amirs paid the ransom of poor Christians.', 'م: مسلمان امراء نے غریب عیسائیوں کا فدیہ ادا کیا۔', 'م. مسلمانو امیرانو د بېوزلو عیسویانو فدیه ورکړه.'),
             ('n. Chingiz Khan and his sons played Holi with the blood of the Muslims.', 'ن: چنگیز خان اور اس کے بیٹوں نے مسلمانوں کے خون سے ہولی کھیلی۔', 'ن. چنګیز خان او زامنو یې د مسلمانانو په وینو هولي ولوبوله.')]))
    BOOK.save(47, [(22, r1), (22, rec(t, 22, 87, 47, [87], kind='exercise'))], complete_units=[22], issues=[{'id': 'ihist12-pdf047', 'unit': 22, 'printedPage': 86,
               'description': 'Student ticks on every (ہاں/نہیں) option and filled blanks ("ابومنصور", "سلجوقی", "فاطمی خلفاء", "تاتاری طوفان") excluded; no printed key. Printed "۵۳۶ء" (the lesson says ۵۳۶ھ) kept as printed in 4(f). Rest of p.87 blank after the ornament.'}])


if __name__ == '__main__':
    p47()
