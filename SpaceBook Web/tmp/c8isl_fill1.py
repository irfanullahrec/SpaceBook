D='D:/SpaceBook/SpaceBook Web/docs/source-verification/class-8/isl/pages/'
def add(page, prefix, sol, occurrence=0):
    f=D+f'p{page}.txt'; L=open(f,encoding='utf8').read().split('\n')
    idx=[k for k,l in enumerate(L) if l.startswith(prefix)]
    i=idx[occurrence]
    assert not L[i+1].startswith('sol'), page
    L.insert(i+1,sol)
    open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))
add('103','q 2 | معلومات مکمل کریں',
 'sol حضرت میمونہ رضی اللہ عنہا: والد حارث بن حزن، قبیلہ بنو ہلال۔ حضرت جویریہ رضی اللہ عنہا: والد حارث بن ابی ضرار، قبیلہ بنو المصطلق (ان کے سردار)۔ حضرت ام حبیبہ رضی اللہ عنہا: والد ابو سفیان بن حرب، قبیلہ قریش کی شاخ بنو امیہ۔ ## عمومی تاریخی معلومات (Derived: کتاب کی جدول خالی ہے) || Hazrat Maymunah (RA): father Harith bin Hazn, tribe Banu Hilal. Hazrat Juwayriyah (RA): father Harith bin Abi Dirar, chief of Banu al-Mustaliq. Hazrat Umm Habibah (RA): father Abu Sufyan bin Harb, Banu Umayyah of Quraysh. (Derived from general history; the table is blank in the book.) || حضرت میمونه رضي الله عنها: پلار حارث بن حزن، قبیله بنو هلال. حضرت جویریه رضي الله عنها: پلار حارث بن ابي ضرار، د بنو المصطلق مشر. حضرت ام حبیبه رضي الله عنها: پلار ابو سفیان بن حرب، د قریشو بنو امیه څانګه. (عمومي تاریخ څخه؛ جدول په کتاب کې تش دی.)')
add('124','qp د | شاہ ولی اللہ',
 'sol (د) مسلمانیت کا ## Derived: کتاب کے سبق سے مطابقت، مگر چھپی کلید دستیاب نہیں (Not verified) || Correct answer: (d) Muslimhood. Derived from the lesson; no printed key (Not verified). || سم ځواب: (د) مسلمانیت. له لوست څخه اخیستل شوی؛ چاپ شوې کلیل نشته (Not verified).')
add('124','qp ہ | اکبر کے',
 'sol (الف) شیخ عبد الحق رحمۃ اللہ علیہ نے ## سبق کے مطابق شیخ عبد الحق نے دینِ الٰہی کا مقابلہ کیا (Derived: سبق میں کتاب کا نام نہیں) || Correct answer: (a) Sheikh Abdul Haq. The lesson says he countered Din-e-Ilahi (Derived: the lesson does not name a book). || سم ځواب: (الف) شیخ عبدالحق. په لوست کې راغلي چې هغه د دین الهي مقابله وکړه (Derived).')
add('129','q 4 | معلومات مکمل کریں',
 'sol سلطان صلاح الدین ایوبی: پیدائش 1137ء/1138ء، تکریت؛ وفات 1193ء۔ سلطان محمد فاتح: پیدائش 1432ء، ادرنہ؛ وفات 1481ء۔ سلطان نور الدین زنگی: پیدائش 1118ء، حلب؛ وفات 1174ء۔ ## عمومی تاریخی معلومات (Derived: کتاب کی جدول خالی ہے) || Salahuddin Ayyubi: born 1137/38, Tikrit; died 1193. Sultan Muhammad Fatih (Mehmed II): born 1432, Edirne; died 1481. Sultan Nur ad-Din Zangi: born 1118, Aleppo; died 1174. (Derived from general history; the table is blank in the book.) || صلاح الدین ایوبي: زېږېدنه 1137/38 تکریت؛ مړینه 1193. سلطان محمد فاتح: زېږېدنه 1432 ادرنه؛ مړینه 1481. سلطان نورالدین زنګي: زېږېدنه 1118 حلب؛ مړینه 1174. (عمومي تاریخ څخه؛ جدول په کتاب کې تش دی.)')
