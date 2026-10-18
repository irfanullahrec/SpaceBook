"""Islamiat (Ikhtiari) XII PDF129: pp.248–249 — Chapter 6 exercise Q1–Q4 (end ch.6). Run: python class12_iski_page129.py"""
from class12_iski_common import BOOK, Builder, rec, L

A = [('الدين', ('Month', 'مہینہ', 'میاشت')), ('الشفع', ('Covered', 'ڈھانپا ہوا', 'پټ شوی')), ('الضحى', ('Poison', 'زہر', 'زهر')),
     ('ابدًا', ('Recompense', 'جزا', 'جزا')), ('شهر', ('Navel', 'ناف', 'نامه')), ('كَتَبَ', ('Even', 'جفت', 'جفت')),
     ('مُقْنِعًا', ('Made obligatory', 'فرض کیا', 'فرض یې کړ')), ('سرّة', ('Spinal bone', 'ریڑھ کی ہڈی', 'د ملا هډوکی')),
     ('الصلب', ('Time of forenoon', 'چاشت کا وقت', 'د څاښت وخت')), ('السم', ('Forever', 'ہمیشہ', 'تل'))]
R = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']


def p129():
    b = Builder()
    b.h('Exercise', 'مشق', 'تمرین')
    b.p('Question 1: Write detailed answers to the following questions.', 'سوال 1: درج ذیل سوالات کے تفصیلی جواب لکھیں۔', 'پوښتنه ۱: د لاندې پوښتنو مفصل ځوابونه ولیکئ.')
    L(b, [('i. With reference to the surahs present in the syllabus, throw light on the literary aspect of the Holy Quran.', 'i۔ نصاب میں موجود سورتوں کے حوالے سے قرآن مجید کے ادبی پہلو پر روشنی ڈالیے۔', 'i. په نصاب کې د موجودو سورتونو په اړه د قرآن مجید پر ادبي اړخ رڼا واچوئ.'),
          ('ii. The sermons of Huzoor ﷺ are a high model of Arabic literature. Comment.', 'ii۔ حضور صلی اللہ علیہ وآلہٖ وسلم کے خطبات عربی ادب کا اعلیٰ نمونہ ہیں۔ تبصرہ کیجیے۔', 'ii. د حضور ﷺ خطبې د عربي ادب لوړه بېلګه ده. تبصره وکړئ.'),
          ('iii. Write a note on the style and literary merits of the letters of the Rightly-Guided Caliphs.', 'iii۔ خلفائے راشدین کے خطوط کے اسلوب اور ادبی محاسن پر نوٹ لکھیں۔', 'iii. د خلفای راشدینو د لیکونو پر اسلوب او ادبي ښېګڼو یادښت ولیکئ.')])
    b.p('Question 2: Give short answers to the following questions.', 'سوال 2: درج ذیل سوالات کے مختصر جواب دیں۔', 'پوښتنه ۲: د لاندې پوښتنو لنډ ځوابونه ورکړئ.')
    L(b, [('i. What did the Arabs used to say about the Holy Quran?', 'i۔ قرآن مجید کے متعلق عرب کیا کہتے تھے؟', 'i. عربانو د قرآن مجید په اړه څه ویل؟'),
          ('ii. Write two names of Surah al-Fatihah.', 'ii۔ سورۂ الفاتحہ کے دو نام لکھیں۔', 'ii. د سورة الفاتحه دوه نومونه ولیکئ.'),
          ('iii. In literary terms, which style is found in Surah al-Fatihah?', 'iii۔ سورۂ الفاتحہ میں ادبی لحاظ سے کونسا اسلوب پایا جاتا ہے؟', 'iii. په سورة الفاتحه کې په ادبي لحاظ کوم اسلوب موندل کېږي؟'),
          ('iv. In which verses of Surah al-Fatihah is saj\' found?', 'iv۔ سورۂ الفاتحہ کی کن آیات میں سجع پائی جاتی ہے؟', 'iv. د سورة الفاتحه په کومو آیتونو کې سجع موندل کېږي؟'),
          ('v. Explain the literal meaning of hijr.', 'v۔ حجر کے لغوی معنی کی وضاحت کریں۔', 'v. د «حجر» لغوي مانا وضاحت کړئ.'),
          ('vi. Who was Iram?', 'vi۔ ارم کون تھا؟', 'vi. ارم څوک و؟'),
          ('vii. What advice has Allah the Exalted given in Surah al-Duha?', 'vii۔ سورۃ الضحیٰ میں اللہ تعالیٰ نے کیا نصیحت فرمائی ہے؟', 'vii. په سورة الضحی کې الله تعالی څه نصیحت کړی؟'),
          ('viii. What change came in the sermon after the coming of Islam?', 'viii۔ اسلام آنے کے بعد خطبے میں کیا تبدیلی آئی؟', 'viii. د اسلام له راتګ وروسته په خطبه کې څه بدلون راغی؟'),
          ('ix. Write the conditions of prayer in the light of Kanz al-Daqa\'iq.', 'ix۔ کنز الدقائق کی روشنی میں نماز کی شرائط لکھیں۔', 'ix. د کنز الدقائق په رڼا کې د لمانځه شرطونه ولیکئ.'),
          ('x. Write the full name of Ibn Sina.', 'x۔ ابنِ سینا کا پورا نام لکھیں۔', 'x. د ابن سینا بشپړ نوم ولیکئ.'),
          ('xi. On what topic was \'Awarif al-Ma\'arif written?', 'xi۔ عوارف المعارف کس موضوع پر لکھی گئی؟', 'xi. عوارف المعارف پر کومه موضوع لیکل شوی؟'),
          ('xii. Whose work is Muruj al-Dhahab?', 'xii۔ مروج الذہب کس کی تصنیف ہے؟', 'xii. مروج الذهب د چا تصنیف دی؟')])
    r1 = rec(b, 6, 248, 129, [248], kind='exercise')
    t = Builder()
    t.p('Question 3: Choose the meanings of column (A) from column (B) and write them in column (C).', 'سوال 3: کالم (ب) میں سے کالم (الف) کے معانی چنیں اور کالم (ج) میں لکھیں۔', 'پوښتنه ۳: د (الف) ستون ماناوې له (ب) ستون وټاکئ او په (ج) ستون کې یې ولیکئ.')
    t.table('iski12-match-ch6', ['Column A', 'Column B', 'Column C'], [[f'{r}. {a}', f'{r}. {m[0]}', ''] for r, (a, m) in zip(R, A)],
            ['کالم الف', 'کالم ب', 'کالم ج'], ['الف ستون', 'ب ستون', 'ج ستون'],
            [[f'{r}. {a}', f'{r}۔ {m[1]}', ''] for r, (a, m) in zip(R, A)], [[f'{r}. {a}', f'{r}. {m[2]}', ''] for r, (a, m) in zip(R, A)])
    t.p('Question 4: Fill in the blanks by selecting the correct answer from the following.', 'سوال 4: درج ذیل میں سے درست جواب کا انتخاب کر کے خالی جگہ پر کریں۔', 'پوښتنه ۴: له لاندې څخه د سم ځواب په ټاکلو تشې ډکې کړئ.')
    L(t, [('i. By al-dallin are meant ______. (Muslims – Jews – Christians – polytheists)', 'i۔ الضالین سے مراد ______ ہیں۔ (مسلمان ۔ یہود ۔ نصاریٰ ۔ مشرکین)', 'i. له «الضالین» څخه ______ مراد دي. (مسلمانان ـ یهود ـ نصارا ـ مشرکین)'),
          ('ii. Hazrat Abu Bakr (may Allah be pleased with him) dispatched an army to ______ to fight the armies of the Romans. (Syria – Persia – Rome – Egypt)', 'ii۔ حضرت ابوبکر رضی اللہ عنہ نے رومیوں کی فوجوں سے لڑنے کے لیے لشکر ______ روانہ فرمایا۔ (شام ۔ فارس ۔ روم ۔ مصر)', 'ii. حضرت ابوبکر رضي الله عنه د رومیانو له پوځونو سره د جګړې لپاره لښکر ______ ته واستاوه. (شام ـ فارس ـ روم ـ مصر)'),
          ('iii. The saying of Huzoor ﷺ is: I am the most eloquent among the ______. (people – Arabs – prophets – creatures)', 'iii۔ حضور صلی اللہ علیہ وآلہٖ وسلم کا ارشاد ہے میں ______ میں سب سے زیادہ فصیح ہوں۔ (لوگوں ۔ عربوں ۔ پیغمبروں ۔ مخلوقات)', 'iii. د حضور ﷺ ارشاد دی: زه په ______ کې تر ټولو فصیح یم. (خلکو ـ عربانو ـ پیغمبرانو ـ مخلوقاتو)'),
          ('iv. Hazrat Ali bin Abi Talib (may Allah honour his face) wrote the letter to the people of ______. (Madinah – Syria – Kufah – Egypt)', 'iv۔ حضرت علی بن ابی طالب کرم اللہ وجہہٗ نے خط ______ کے لوگوں کو لکھا۔ (مدینہ ۔ شام ۔ کوفہ ۔ مصر)', 'iv. حضرت علي بن ابي طالب کرم الله وجهه لیک د ______ خلکو ته ولیکه. (مدینه ـ شام ـ کوفه ـ مصر)'),
          ('v. Kanz al-Daqa\'iq is the work of ______. (Ibn Sina – Ibn Khaldun – Hafiz al-Din al-Nasafi – Shah Waliullah)', 'v۔ کنز الدقائق ______ کی تصنیف ہے۔ (ابن سینا ۔ ابن خلدون ۔ حافظ الدین النسفی ۔ شاہ ولی اللہ)', 'v. کنز الدقائق د ______ تصنیف دی. (ابن سینا ـ ابن خلدون ـ حافظ الدین النسفي ـ شاه ولي الله)'),
          ('vi. Muruj al-Dhahab is a book written on ______. (history – tasawwuf – medicine – fiqh)', 'vi۔ مروج الذہب ______ پر لکھی ہوئی کتاب ہے۔ (تاریخ ۔ تصوف ۔ طب ۔ فقہ)', 'vi. مروج الذهب پر ______ لیکل شوی کتاب دی. (تاریخ ـ تصوف ـ طب ـ فقه)')])
    BOOK.save(129, [(6, r1), (6, rec(t, 6, 249, 129, [249], kind='exercise'))], complete_units=[6], issues=[{'id': 'iski12-pdf129', 'unit': 6, 'printedPage': 248,
               'description': 'End of Chapter 6. Matching table reproduced as printed (column B jumbled; column C left empty for the student). No printed key; blanks rendered empty.'}])


if __name__ == '__main__':
    p129()
