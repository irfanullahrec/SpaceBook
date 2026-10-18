"""Page spec for Class 3 Nazira (Para 3 to Para 8) — every value read from the scans.
Run:  python nazira_spec3.py   (writes every Quran page via nazira_quran3.write())"""
import nazira_quran3 as nq
from nazira_quran3 import page, act, mashq, STD2

AR_DIG = nq.AR_DIG


def lesson(n, unit_no, title, s1, a1, s2, b2):
    """Header lines for the first page of lesson n (unit unit_no)."""
    u_ur, u_en, u_ps = title
    if s1 == s2:
        r = nq.rng(s1, a1, b2)
    else:
        x, y = nq.SURAH[s1], nq.SURAH[s2]
        r = (f'سورۃ {x[2]} آیت {a1} تا سورۃ {y[2]} آیت {b2}', f'Surah {x[3]} verse {a1} to Surah {y[3]} verse {b2}',
             f'سورة {x[2]} {a1} آیت تر سورة {y[2]} {b2} آیت')
    head = [f'@unit {unit_no} | سبق {n}: {u_ur} || Lesson {n}: {u_en} || {n} لوست: {u_ps}',
            f'@sec text | سبق {n} || Lesson {n} || {n} لوست',
            f'# سبق {n}: {u_ur} || Lesson {n}: {u_en} || {n} لوست: {u_ps}']
    slo = ['box prior | حاصلاتِ تعلّم || Learning outcomes || د زده کړې پایلې',
           'p اس سبق کی تکمیل پر بچّے اس قابل ہو جائیں گے کہ وہ: || After this lesson the children will be able to: || د دې لوست په پای کې به ماشومان وکولای شي چې:',
           f'- {r[0]} تجوید کے قواعد کی پہچان کرتے ہوئے درست تلفّظ کے ساتھ پڑھ سکیں۔ || read {r[1]} with correct pronunciation, recognising the tajweed rules. || {r[2]} د تجوید د قواعدو په پېژندنې سره په سم تلفظ ولولي.',
           f'- {r[0]} کو رموزِ اوقاف کا خیال رکھتے ہوئے روانی کے ساتھ پڑھ سکیں۔ || read {r[1]} fluently, observing the stopping signs. || {r[2]} د وقف نښو په پام کې نیولو سره په روانۍ ولولي.',
           'endbox']
    return head, slo


def F(ur, en, ps):
    return f'{ur} || {en} || {ps}'


READ = F('درست تلفّظ کے ساتھ پڑھنے کی مشق کیجیے اور ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔',
         'Practise reading with correct pronunciation and read to one another.', 'په سم تلفظ د لوستلو تمرین وکړئ او یو بل ته یې ولولئ.')
DEMO = STD2[1]

# ---- Lesson 1: Al-Baqarah 253 to Aal-Imran 15 (printed 19-25) ----
h, s = lesson(1, 2, ('سورۃ البقرۃ و سورۃ آل عمران', 'Al-Baqarah and Aal-Imran', 'سورة البقره او سورة آل عمران'), 2, 253, 3, 15)
page(21, 19, [(2, 253, 256)], act(F('وقف کی علامات تلاش کیجیے اور ان کے نیچے لائن (عَلٰى بَعْضٍ) لگائیے۔', 'Find the stopping signs and underline them (e.g. \'alaa ba\'d).', 'د وقف نښې ومومئ او لاندې یې کرښه وکاږئ.'),
     [F('وقف کے اصولوں کے مطابق درست طریقہ سے پڑھنے کی مشق کیجیے۔', 'Practise reading correctly according to the rules of stopping.', 'د وقف د اصولو سره سم د لوستلو تمرین وکړئ.'), DEMO]),
     'act', head=h, slo=s, issue='Para 3 (تِلْكَ الرُّسُلُ) begins at Al-Baqarah 2:253.')
page(22, 20, [(2, 257, 259)], mashq(2, 260, 264), 'mashq', hw=(2, 260, 264))
page(23, 21, [(2, 265, 269)], act(F('ہمزہ ساکن والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (وَيَاْمُرُكُمْ) لگائیے۔', 'Find the words with hamzah sakin and underline them (e.g. wa ya\'murukum).', 'د ساکنې همزې کلمې ومومئ او کرښه یې وکاږئ.'),
     [F('ہمزہ ساکن والے الفاظ ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔', 'Read the words with hamzah sakin to one another with correct pronunciation.', 'د ساکنې همزې کلمې یو بل ته په سم تلفظ ولولئ.'), DEMO]), 'act')
page(24, 22, [(2, 270, 274)], mashq(2, 275, 281), 'mashq', hw=(2, 275, 281),
     extra=[F('آیت 270 کو "حدر" کے طریقے سے پڑھوائیے۔', 'Have verse 270 read in the "hadr" (quick, flowing) style.', '۲۷۰ آیت د "حدر" (چټک او روان) په طریقه ولولئ.')])
page(25, 23, [(2, 282, 282)], act(F('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (يٰٓاَيُّهَا الَّذِيْنَ) لگائیے۔', 'Find words with standing zabar, standing zer and inverted pesh and underline them (e.g. yaa ayyuhal-ladheena).', 'د ولاړ زبر، ولاړ زېر او سرچپه پېښ کلمې ومومئ او کرښه یې وکاږئ.'),
     [F('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔', 'Read these words to one another with correct pronunciation.', 'دا کلمې یو بل ته په سم تلفظ ولولئ.'), DEMO]), 'act')
page(26, 24, [(2, 283, 286)], mashq(3, 1, 8), 'mashq', hw=(3, 1, 8),
     issue='Surah Al-Baqarah ends on this page (2:286). The practice box takes the opening verses of Aal-Imran (3:1-8), which the book does not print in full.')
page(27, 25, [(3, 9, 15)], act(F('غنّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اِنَّكَ) لگائیے۔', 'Find the words with ghunnah and underline them (e.g. innaka).', 'د غنې کلمې ومومئ او کرښه یې وکاږئ.'),
     [F('غنّہ کے قواعد کا اعادہ کیجیے۔', 'Revise the rules of ghunnah.', 'د غنې قواعد تکرار کړئ.'), READ, DEMO]), 'act')

# ---- Lesson 2: Aal-Imran 16-77 (printed 26-30) ----
h, s = lesson(2, 3, ('سورۃ آل عمران (آیت 16 تا 77)', 'Aal-Imran 16-77', 'سورة آل عمران (۱۶–۷۷)'), 3, 16, 3, 77)
page(28, 26, [(3, 16, 22)], mashq(3, 23, 29), 'mashq', hw=(3, 23, 29), head=h, slo=s)
page(29, 27, [(3, 30, 37)], act(F('موٹے حروف والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (خَيْرٍ) لگائیے۔', 'Find the words with heavy letters and underline them (e.g. khayrin).', 'د درنو تورو کلمې ومومئ او کرښه یې وکاږئ.'), [READ, DEMO]), 'act')
page(30, 28, [(3, 38, 45)], mashq(3, 46, 53), 'mashq', hw=(3, 46, 53))
page(31, 29, [(3, 54, 62)], act(F('مد والے الفاظ تلاش کیجیے اور ان کے ساتھ (يٰعِيْسٰٓى) ✓ کا نشان لگائیے۔', 'Find the words with madd and put a tick ✓ beside them (e.g. yaa \'eesaa).', 'د مد کلمې ومومئ او ✓ نښه ورته کېږدئ.'), [READ, DEMO]), 'act')
page(32, 30, [(3, 63, 70)], mashq(3, 71, 77), 'mashq', hw=(3, 71, 77))

# ---- Lesson 3: Aal-Imran 78-132 (printed 31-35) ----
h, s = lesson(3, 4, ('سورۃ آل عمران (آیت 78 تا 132)', 'Aal-Imran 78-132', 'سورة آل عمران (۷۸–۱۳۲)'), 3, 78, 3, 132)
page(33, 31, [(3, 78, 83)], act(F('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (لَفَرِيْقًا) لگائیے۔', 'Find the words with the letters of madd and underline them (e.g. lafareeqan).', 'د مد تورو کلمې ومومئ او کرښه یې وکاږئ.'), [READ, DEMO]), 'act', head=h, slo=s)
page(34, 32, [(3, 84, 91)], mashq(3, 92, 100), 'mashq', hw=(3, 92, 100), issue='Para 4 (لَنْ تَنَالُوا) begins at Aal-Imran 3:92, inside the practice range of this page.')
page(35, 33, [(3, 101, 108)], act(F('حروفِ لین والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (وَكَيْفَ) لگائیے۔', 'Find the words with the letters of leen and underline them (e.g. wa kayfa).', 'د لین تورو کلمې ومومئ او کرښه یې وکاږئ.'), [READ, DEMO]), 'act')
page(36, 34, [(3, 109, 115)], mashq(3, 116, 121), 'mashq', hw=(3, 116, 121))
page(37, 35, [(3, 122, 132)], act(F('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (طَآئِفَتٰنِ) لگائیے۔', 'Find words with standing zabar, standing zer and inverted pesh and underline them (e.g. taa\'ifataani).', 'د ولاړو حرکتونو کلمې ومومئ او کرښه یې وکاږئ.'),
     [F('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔', 'Read these words to one another with correct pronunciation.', 'دا کلمې یو بل ته په سم تلفظ ولولئ.'), DEMO]), 'act')

# ---- Lesson 4: Aal-Imran 133-186 (printed 36-40) ----
h, s = lesson(4, 5, ('سورۃ آل عمران (آیت 133 تا 186)', 'Aal-Imran 133-186', 'سورة آل عمران (۱۳۳–۱۸۶)'), 3, 133, 3, 186)
page(38, 36, [(3, 133, 140)], mashq(3, 141, 147), 'mashq', hw=(3, 141, 147), head=h, slo=s)
page(39, 37, [(3, 148, 153)], act(F('ہمزہ ساکن والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (وَمَاْوٰىهُمُ النَّارُ) لگائیے۔', 'Find the words with hamzah sakin and underline them (e.g. wa ma\'waahumun-naar).', 'د ساکنې همزې کلمې ومومئ او کرښه یې وکاږئ.'), [READ, DEMO]), 'act')
page(40, 38, [(3, 154, 157)], mashq(3, 158, 165), 'mashq', hw=(3, 158, 165))
page(41, 39, [(3, 166, 173)], act(F('قلقلہ والے الفاظ تلاش کیجیے اور ان کے ساتھ (اَوِ ادْفَعُوْا) ✓ کا نشان لگائیے۔', 'Find the words with qalqalah and put a tick ✓ beside them (e.g. awid-fa\'oo).', 'د قلقلې کلمې ومومئ او ✓ نښه ورته کېږدئ.'), [READ, DEMO]), 'act')
page(42, 40, [(3, 174, 180)], mashq(3, 181, 186), 'mashq', hw=(3, 181, 186))

# ---- Lesson 5: Aal-Imran 187 to An-Nisa 23 (printed 41-45) ----
h, s = lesson(5, 6, ('سورۃ آل عمران و سورۃ النساء', 'Aal-Imran and An-Nisa', 'سورة آل عمران او سورة النساء'), 3, 187, 4, 23)
GHUN = act(F('غنّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (لَتُبَيِّنُنَّهٗ) لگائیے۔', 'Find the words with ghunnah and underline them (e.g. latubayyinunnahu).', 'د غنې کلمې ومومئ او کرښه یې وکاږئ.'),
           [F('غنّہ کے قواعد کا اعادہ کیجیے۔', 'Revise the rules of ghunnah.', 'د غنې قواعد تکرار کړئ.'), READ, DEMO])
page(43, 41, [(3, 187, 193)], GHUN, 'act', head=h, slo=s)
page(44, 42, [(3, 194, 200)], mashq(4, 1, 5), 'mashq', hw=(4, 1, 5),
     issue='Surah Aal-Imran ends on this page (3:200). The practice box takes the opening verses of An-Nisa (4:1-5), which the book does not print in full.')
WAQF2 = F('وقف کے اصولوں کے مطابق درست طریقہ سے پڑھنے کی مشق کیجیے۔', 'Practise reading correctly according to the rules of stopping.', 'د وقف د اصولو سره سم د لوستلو تمرین وکړئ.')


def find(ur_rule, en_rule, ps_rule, ex_ar, ex_en, tick=False):
    """Standard 'find the words ... and underline (or tick) them' activity line."""
    if tick:
        return F(f'{ur_rule} والے الفاظ تلاش کیجیے اور ان کے ساتھ ({ex_ar}) ✓ کا نشان لگائیے۔',
                 f'Find the words with {en_rule} and put a tick ✓ beside them (e.g. {ex_en}).', f'د {ps_rule} کلمې ومومئ او ✓ نښه ورته کېږدئ.')
    return F(f'{ur_rule} والے الفاظ تلاش کیجیے اور ان کے نیچے لائن ({ex_ar}) لگائیے۔',
             f'Find the words with {en_rule} and underline them (e.g. {ex_en}).', f'د {ps_rule} کلمې ومومئ او کرښه یې وکاږئ.')


R_MADD = ('حروفِ مدّہ', 'the letters of madd', 'د مد تورو')
R_MAD = ('مد', 'madd', 'مد')
R_LEEN = ('حروفِ لین', 'the letters of leen', 'د لین تورو')
R_GHUN = ('غنّہ', 'ghunnah', 'غنې')
R_QALQ = ('قلقلہ', 'qalqalah', 'قلقلې')
R_HAMZ = ('ہمزہ ساکن', 'hamzah sakin', 'ساکنې همزې')
R_HEAVY = ('موٹے حروف', 'heavy letters', 'درنو تورو')
R_STAND = ('کھڑی زبر، کھڑی زیر اور الٹا پیش', 'standing zabar, standing zer and inverted pesh', 'ولاړ زبر، ولاړ زېر او سرچپه پېښ')
R_SHADD = ('شد', 'shadd', 'شد')
R_TANW = ('تنوین', 'tanween', 'تنوین')
R_JAZM = ('جزم', 'jazm', 'جزم')


def A(rule, ex_ar, ex_en, tick=False, items=None):
    return act(find(*rule, ex_ar, ex_en, tick), items if items is not None else [READ, DEMO])


def AW(ex_ar, ex_en):
    """Stopping-signs activity."""
    return act(F(f'وقف کی علامات تلاش کیجیے اور ان کے نیچے لائن ({ex_ar}) لگائیے۔', f'Find the stopping signs and underline them (e.g. {ex_en}).', 'د وقف نښې ومومئ او لاندې یې کرښه وکاږئ.'), [WAQF2, DEMO])


page(45, 43, [(4, 6, 10)], AW('بَلَغُوا النِّكَاحَ', 'balaghun-nikaah'), 'act')
page(46, 44, [(4, 11, 12)], mashq(4, 13, 18), 'mashq', hw=(4, 13, 18))
page(47, 45, [(4, 19, 23)], A(R_HEAVY, 'كَرْهًا', 'karhan'), 'act')

# ---- Lesson 6: An-Nisa 24-75 (printed 46-50) ----
h, s = lesson(6, 7, ('سورۃ النساء (آیت 24 تا 75)', 'An-Nisa 24-75', 'سورة النساء (۲۴–۷۵)'), 4, 24, 4, 75)
page(48, 46, [(4, 24, 28)], mashq(4, 29, 34), 'mashq', hw=(4, 29, 34), head=h, slo=s,
     issue='Para 5 (وَالْمُحْصَنٰتُ) begins at An-Nisa 4:24.')
PAIR = F('یہ الفاظ ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔', 'Read these words to one another with correct pronunciation.', 'دا کلمې یو بل ته په سم تلفظ ولولئ.')


def AS(ex_ar, ex_en, rule=R_STAND, tick=False):
    """Activity whose second item is 'read these words to one another'."""
    return A(rule, ex_ar, ex_en, tick, [PAIR, DEMO])


page(49, 47, [(4, 35, 41)], A(R_LEEN, 'بَيْنِهِمَا', 'baynihimaa'), 'act')
page(50, 48, [(4, 42, 46)], mashq(4, 47, 54), 'mashq', hw=(4, 47, 54))
page(51, 49, [(4, 55, 60)], AS('اٰمَنَ', 'aamana'), 'act')
page(52, 50, [(4, 61, 68)], mashq(4, 69, 75), 'mashq', hw=(4, 69, 75))

# ---- Lesson 7: An-Nisa 76-113 (printed 51-55) ----
h, s = lesson(7, 8, ('سورۃ النساء (آیت 76 تا 113)', 'An-Nisa 76-113', 'سورة النساء (۷۶–۱۱۳)'), 4, 76, 4, 113)
page(53, 51, [(4, 76, 80)], A(R_MAD, 'فَقَاتِلُوْٓا', 'faqaatiloo', tick=True), 'act', head=h, slo=s)
page(54, 52, [(4, 81, 87)], mashq(4, 88, 91), 'mashq', hw=(4, 88, 91))
page(55, 53, [(4, 92, 95)], AS('لِمُؤْمِنٍ', 'limu\'minin', rule=R_HAMZ), 'act')
page(56, 54, [(4, 96, 101)], mashq(4, 102, 105), 'mashq', hw=(4, 102, 105))
GREV = F('غنّہ کے قواعد کا اعادہ کیجیے۔', 'Revise the rules of ghunnah.', 'د غنې قواعد تکرار کړئ.')


def AG(ex_ar, ex_en):
    return A(R_GHUN, ex_ar, ex_en, items=[GREV, READ, DEMO])


page(57, 55, [(4, 106, 113)], AG('اِنَّ اللّٰهَ', 'innallaaha'), 'act')

# ---- Lesson 8: An-Nisa 114-170 (printed 56-60) ----
h, s = lesson(8, 9, ('سورۃ النساء (آیت 114 تا 170)', 'An-Nisa 114-170', 'سورة النساء (۱۱۴–۱۷۰)'), 4, 114, 4, 170)
page(58, 56, [(4, 114, 121)], mashq(4, 122, 127), 'mashq', hw=(4, 122, 127), head=h, slo=s)
LONG = ('زبر، زیر اور پیش کے مقابلے میں ذرا لمبا کر کے پڑھی جانے والی آوازوں (حروفِ مدّہ، کھڑی زبر، کھڑی زیر، الٹا پیش)',
        'sounds read a little longer than zabar, zer and pesh (letters of madd, standing zabar, standing zer, inverted pesh)',
        'هغو غږونو (د مد توري، ولاړ زبر، ولاړ زېر، سرچپه پېښ) چې له زبر، زېر او پېښ لږ اوږد لوستل کېږي')
page(59, 57, [(4, 128, 134)], A(LONG, 'خَافَتْ', 'khaafat', items=[F('درست تلفّظ سے پڑھنے کی مشق کیجیے۔', 'Practise reading with correct pronunciation.', 'په سم تلفظ د لوستلو تمرین وکړئ.'), DEMO]), 'act')
page(60, 58, [(4, 135, 140)], mashq(4, 141, 147), 'mashq', hw=(4, 141, 147))
QALQ_T = A(R_QALQ, 'تُبْدُوْا', 'tubdoo', tick=True)
page(61, 59, [(4, 148, 154)], QALQ_T, 'act')
page(62, 60, [(4, 155, 162)], mashq(4, 163, 170), 'mashq', hw=(4, 163, 170))


def mashq2(ranges, label):
    """Practice box spanning two surahs."""
    u, e, p = label
    L = [f'box note | مشق — {u} || Practice — {e} || تمرین — {p}',
         'p کتاب کے حاشیے میں ان آیات کے چند حصے مشق کے لیے دیے گئے ہیں؛ یہاں مکمل آیات دی گئی ہیں۔ || The book\'s margin prints a few phrases from these verses for practice; the complete verses are given here. || د کتاب په حاشیه کې د دې آیتونو ځینې برخې د تمرین لپاره راغلې؛ دلته بشپړ آیتونه ورکړل شوي.']
    for s_, a_, b_ in ranges:
        if a_ == 1:
            L += nq.surah_head(s_)
        L += nq.ayah_lines(s_, a_, b_)
    return L + ['endbox']


# ---- Lesson 9: An-Nisa 171 to Al-Ma'idah 36 (printed 61-65) ----
h, s = lesson(9, 10, ('سورۃ النساء و سورۃ المائدۃ', 'An-Nisa and Al-Ma\'idah', 'سورة النساء او سورة المائده'), 4, 171, 5, 36)
L9 = ('سورۃ النساء آیت 176 تا سورۃ المائدۃ آیت 2', 'Surah An-Nisa verse 176 to Surah Al-Ma\'idah verse 2', 'سورة النساء ۱۷۶ آیت تر سورة المائده ۲ آیت')
HW9 = F('ہوم ورک: بچّوں کو قرآن مجید میں سے سورۃ النساء کی آیت 176 اور سورۃ المائدۃ کی آیات 1 اور 2 گھر سے پڑھ کر آنے کی تاکید کیجیے۔',
        'Homework: ask the children to read Surah An-Nisa verse 176 and Surah Al-Ma\'idah verses 1 and 2 from the Holy Quran at home.',
        'کورنی کار: ماشومانو ته ووایاست چې د سورة النساء ۱۷۶ آیت او د سورة المائده ۱ او ۲ آیتونه په کور کې ولولي.')
page(63, 61, [(4, 171, 175)], mashq2([(4, 176, 176), (5, 1, 2)], L9), 'mashq', extra=[HW9], head=h, slo=s,
     issue='Para 6 (لَا يُحِبُّ اللّٰهُ) begins at An-Nisa 4:148 (previous lesson). Surah An-Nisa ends at 4:176 and Al-Ma\'idah begins in the practice box; the book prints the main text from Al-Ma\'idah 5:3.')
page(64, 62, [(5, 3, 5)], mashq(5, 6, 9), 'mashq', hw=(5, 6, 9))
page(65, 63, [(5, 10, 13)], mashq(5, 14, 17), 'mashq', hw=(5, 14, 17))
page(66, 64, [(5, 18, 23)], A(R_MAD, 'اَبْنٰٓؤُا', 'abnaa\'u', tick=True), 'act')
page(67, 65, [(5, 24, 31)], mashq(5, 32, 36), 'mashq', hw=(5, 32, 36))

# ---- Lesson 10: Al-Ma'idah 37-75 (printed 66-70) ----
h, s = lesson(10, 11, ('سورۃ المائدۃ (آیت 37 تا 75)', 'Al-Ma\'idah 37-75', 'سورة المائده (۳۷–۷۵)'), 5, 37, 5, 75)
page(68, 66, [(5, 37, 41)], A(R_MADD, 'يُرِيْدُوْنَ', 'yureedoona'), 'act', head=h, slo=s)
page(69, 67, [(5, 42, 45)], mashq(5, 46, 50), 'mashq', hw=(5, 46, 50),
     extra=[F('سورۃ المائدۃ کی آیت 45 کو "حدر" کے طریقے سے پڑھیے۔', 'Read Al-Ma\'idah verse 45 in the "hadr" (quick, flowing) style.', 'د سورة المائده ۴۵ آیت د "حدر" په طریقه ولولئ.')])
page(70, 68, [(5, 51, 56)], AG('وَالنَّصٰرٰٓى', 'wan-nasaaraa'), 'act')
page(71, 69, [(5, 57, 63)], mashq(5, 64, 68), 'mashq', hw=(5, 64, 68))
page(72, 70, [(5, 69, 75)], A(LONG, 'الَّذِيْنَ', 'alladheena', items=[F('درست تلفّظ سے پڑھنے کی مشق کیجیے۔', 'Practise reading with correct pronunciation.', 'په سم تلفظ د لوستلو تمرین وکړئ.'), DEMO]), 'act')

# ---- Lesson 11: Al-Ma'idah 76 to Al-An'am 8 (printed 71-75) ----
h, s = lesson(11, 12, ('سورۃ المائدۃ و سورۃ الانعام', 'Al-Ma\'idah and Al-An\'am', 'سورة المائده او سورة الانعام'), 5, 76, 6, 8)
page(73, 71, [(5, 76, 82)], mashq(5, 83, 89), 'mashq', hw=(5, 83, 89), head=h, slo=s,
     issue='Para 7 (وَاِذَا سَمِعُوْا) begins at Al-Ma\'idah 5:83, inside the practice range of this page.')
page(74, 72, [(5, 90, 95)], A(R_QALQ, 'رِجْسٌ', 'rijsun', tick=True), 'act')
page(75, 73, [(5, 96, 103)], mashq(5, 104, 108), 'mashq', hw=(5, 104, 108))
page(76, 74, [(5, 109, 113)], A(R_LEEN, 'يَوْمَ', 'yawma'), 'act')
page(77, 75, [(5, 114, 120)], mashq(6, 1, 8), 'mashq', hw=(6, 1, 8),
     issue='Surah Al-Ma\'idah ends on this page (5:120). The practice box takes the opening verses of Al-An\'am (6:1-8), which the book does not print in full.')

# ---- Lesson 12: Al-An'am 9-73 (printed 76-80) ----
h, s = lesson(12, 13, ('سورۃ الانعام (آیت 9 تا 73)', 'Al-An\'am 9-73', 'سورة الانعام (۹–۷۳)'), 6, 9, 6, 73)
page(78, 76, [(6, 9, 18)], mashq(6, 19, 26), 'mashq', hw=(6, 19, 26), head=h, slo=s)
page(79, 77, [(6, 27, 34)], A(R_MAD, 'تَرٰٓى', 'taraa', tick=True), 'act')
page(80, 78, [(6, 35, 43)], mashq(6, 44, 51), 'mashq', hw=(6, 44, 51))
page(81, 79, [(6, 52, 58)], A(R_HEAVY, 'تَطْرُدِ الَّذِيْنَ', 'tatrudil-ladheena'), 'act')
page(82, 80, [(6, 59, 67)], mashq(6, 68, 73), 'mashq', hw=(6, 68, 73))

# ---- Lesson 13: Al-An'am 74-110 (printed 81-83) ----
h, s = lesson(13, 14, ('سورۃ الانعام (آیت 74 تا 110)', 'Al-An\'am 74-110', 'سورة الانعام (۷۴–۱۱۰)'), 6, 74, 6, 110)
page(83, 81, [(6, 74, 81)], mashq(6, 82, 90), 'mashq', hw=(6, 82, 90), head=h, slo=s)
page(84, 82, [(6, 91, 94)], AG('اَنْزَلَ اللّٰهُ', 'anzalallaahu'), 'act')
page(85, 83, [(6, 95, 101)], mashq(6, 102, 110), 'mashq', hw=(6, 102, 110),
     extra=[F('سورۃ الانعام کی آیت 96 کو "حدر" کے طریقے سے پڑھوائیے۔', 'Have Al-An\'am verse 96 read in the "hadr" (quick, flowing) style.', 'د سورة الانعام ۹۶ آیت د "حدر" په طریقه ولولئ.')])

# ---- Lesson 14: Al-An'am 111 to Al-A'raf 11 (printed 84-88) ----
h, s = lesson(14, 15, ('سورۃ الانعام و سورۃ الاعراف', 'Al-An\'am and Al-A\'raf', 'سورة الانعام او سورة الاعراف'), 6, 111, 7, 11)
page(86, 84, [(6, 111, 118)], mashq(6, 119, 124), 'mashq', hw=(6, 119, 124), head=h, slo=s,
     extra=[F('بچّوں کو جزم اور شد کی مدد سے آیات کے سرخ رنگ والے حصوں کو پڑھنے میں مدد کیجیے اور آیات درست تلفّظ کے ساتھ روانی میں پڑھنے کی مشق کروائیے۔',
              'Help the children read the red parts of the verses using jazm and shadd, and have them practise reading fluently with correct pronunciation.',
              'له ماشومانو سره د جزم او شد په مرسته د آیتونو د سرو برخو په لوستلو کې مرسته وکړئ او په روانۍ د لوستلو تمرین ورکړئ.')],
     issue='Para 8 (وَلَوْ اَنَّنَا) begins at Al-An\'am 6:111.')
page(87, 85, [(6, 125, 130)], mashq(6, 131, 137), 'mashq', hw=(6, 131, 137))
page(88, 86, [(6, 138, 142)], mashq(6, 143, 146), 'mashq', hw=(6, 143, 146),
     extra=[F('حروفِ مدّہ کے تصورات کا اعادہ اور درست ادائی کے لیے عملی مظاہرہ کروائیے۔', 'Revise the letters of madd and demonstrate their correct reading.', 'د مد توري تکرار کړئ او سم ادا یې عملي وښیئ.')])
JS = F('بچّوں کو جزم اور شد کی علامات کا اعادہ کروائیے اور آیات کے سرخ رنگ والے حصوں کو پڑھنے میں مدد کیجیے۔', 'Revise the jazm and shadd signs and help the children read the red parts of the verses.', 'د جزم او شد نښې تکرار کړئ او د آیتونو د سرو برخو په لوستلو کې مرسته وکړئ.')
page(89, 87, [(6, 147, 151)], mashq(6, 152, 157), 'mashq', hw=(6, 152, 157), extra=[JS])
page(90, 88, [(6, 158, 165)], mashq(7, 1, 11), 'mashq', hw=(7, 1, 11),
     extra=[F('ہر بچّے کو ایک ایک آیت پڑھنے کا موقع دیجیے۔', 'Give every child the chance to read one verse.', 'هر ماشوم ته د یوه آیت د لوستلو فرصت ورکړئ.')],
     issue='Surah Al-An\'am ends on this page (6:165). The practice box takes the opening verses of Al-A\'raf (7:1-11), which the book does not print in full.')

# ---- Lesson 15: Al-A'raf 12-87 (printed 89-...) ----
h, s = lesson(15, 16, ('سورۃ الاعراف (آیت 12 تا 87)', 'Al-A\'raf 12-87', 'سورة الاعراف (۱۲–۸۷)'), 7, 12, 7, 87)
page(91, 89, [(7, 12, 22)], mashq(7, 23, 30), 'mashq', hw=(7, 23, 30), head=h, slo=s,
     extra=[F('بچّوں کو جزم اور شد کی مدد سے آیات کے سرخ رنگ والے حصوں کو پڑھنے میں مدد کیجیے اور آیات درست تلفّظ کے ساتھ روانی میں پڑھنے کی مشق کروائیے۔',
              'Help the children read the red parts of the verses using jazm and shadd, and have them practise reading fluently with correct pronunciation.',
              'له ماشومانو سره د جزم او شد په مرسته د سرو برخو په لوستلو کې مرسته وکړئ او په روانۍ د لوستلو تمرین ورکړئ.')])
page(92, 90, [(7, 31, 37)], mashq(7, 38, 43), 'mashq', hw=(7, 38, 43))
page(93, 91, [(7, 44, 51)], mashq(7, 52, 57), 'mashq', hw=(7, 52, 57),
     extra=[F('حروفِ مدّہ کے تصورات کا اعادہ اور درست ادائی کے لیے عملی مظاہرہ کروائیے۔', 'Revise the letters of madd and demonstrate their correct reading.', 'د مد توري تکرار کړئ او سم ادا یې عملي وښیئ.')])
page(94, 92, [(7, 58, 67)], mashq(7, 68, 73), 'mashq', hw=(7, 68, 73), extra=[JS])
page(95, 93, [(7, 74, 81)], mashq(7, 82, 87), 'mashq', hw=(7, 82, 87),
     extra=[F('ہر بچّے کو ایک ایک آیت پڑھنے کا موقع دیجیے۔', 'Give every child the chance to read one verse.', 'هر ماشوم ته د یوه آیت د لوستلو فرصت ورکړئ.')],
     issue='This is the last Quran page of the book (Al-A\'raf 7:87), which is where Para 8 ends.')

if __name__ == '__main__':
    nq.write()
