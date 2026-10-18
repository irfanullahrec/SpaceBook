"""PDF61 (printed 109–110): Unit 11 C second conditionals 1–20 (unit end); Unit 12 opener 'All the World's a Stage' outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.h('C. Second Conditionals', 'C. دوسرا شرطیہ', 'C. دویم شرطي')
w.p('Put the verb into the correct tense:', 'فعل کو درست زمانے میں لکھیں:', 'فعل په سم زمان کې ولیکئ:')
SC = ['If I ____ (be) you, I ____ (get) a new job.', 'If he ____ (be) younger, he ____ (travel) more.', 'If we ____ (not / be) friends, I ____ (be) angry with you.', 'If I ____ (have) enough money, I ____ (buy) a big house.',
      'If she ____ (not / be) always so late, she ____ (be) promoted.', 'If we ____ (win) the lottery, we ____ (travel) the world.', 'If you ____ (have) a better job, we ____ (be) able to buy a new car.', 'If I ____ (speak) perfect English, I ____ (have) a good job.',
      'If we ____ (live) in England, I ____ (speak) English.', 'If she ____ (pass) the exam, s____ (be) able to enter university.', 'She ____ (be) happier if she ____ (have) more friends.', 'We ____ (buy) a house if we ____ (decide) to stay here.',
      'They ____ (have) more money if they ____ (not / buy) so many clothes.', 'We ____ (come) to dinner if we ____ (have) time.', 'She ____ (call) him if she ____ (know) his number.', 'They ____ (go) to Murree on holiday if they ____ (like) cold weather.',
      'She ____ (pass) the exam if she ____ (study) more.', 'I ____ (marry) someone famous if I ____ (be) a movie star.', 'We never ____ (be) late again if we ____ (buy) a new car.', 'You ____ (lose) weight if you ____ (eat) less.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(SC, 1)])
for p in w.paras[2:]: p['untranslatedByDesign'] = True
ex = BOOK.record(w, 'eng12-u11-vocab-b', 'Second conditionals 1–20', 'دوسرا شرطیہ 1–20', 'دویم شرطي 1–20', 61, [109])

UT = ("All the World's a Stage (Poem)", 'ساری دنیا ایک اسٹیج ہے (نظم)', 'ټوله نړۍ یوه سټېج ده (شعر)')
o = Builder()
o.h("Unit 12 — All the World's a Stage (William Shakespeare)", 'یونٹ 12 — ساری دنیا ایک اسٹیج ہے (ولیم شیکسپیئر)', 'واحد 12 — ټوله نړۍ یوه سټېج ده (ویلیم شکسپیر)')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Read a given poem and give orally and in writing: theme and its development; personal response with justification; recognize literary techniques such as personification and alliteration.', 'دی گئی نظم پڑھیں اور زبانی و تحریری طور پر بیان کریں: موضوع اور اس کا ارتقا؛ جواز کے ساتھ ذاتی ردِعمل؛ ادبی تکنیکوں جیسے تجسیم اور تکرارِ حرفی کو پہچانیں۔', 'ورکړل شوی شعر ولولي او په خوله او لیکلي ډول ووايي: موضوع او د هغې وده؛ د دلیل سره شخصي غبرګون؛ ادبي تخنیکونه لکه تجسیم او د تورو تکرار وپېژني.'),
    ('Use critical thinking to respond orally and in writing to the text (post-reading) to: give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read; relate what is read to his or her own feelings and experiences; explore causes and consequences of a problem or an issue and propose various solutions.', 'تنقیدی سوچ استعمال کرتے ہوئے متن پر زبانی اور تحریری ردِعمل دیں (مطالعے کے بعد) تاکہ: پڑھے گئے متن کے نقطۂ ہائے نظر/ خیالات اور مسائل پر ذاتی رائے دیں اور موقف کا جواز پیش کریں؛ جو پڑھا اسے اپنے احساسات اور تجربات سے جوڑیں؛ کسی مسئلے کے اسباب و نتائج کی جستجو کریں اور مختلف حل تجویز کریں۔', 'د انتقادي فکر په کارولو متن ته په خوله او لیکلي ډول غبرګون وښيي (له لوستلو وروسته) ترڅو: د لوستل شوي متن د لیدلورو/ نظرونو او مسایلو په اړه شخصي نظر ورکړي او دریځ یې ثابت کړي؛ لوستل شوي له خپلو احساساتو او تجربو سره وتړي؛ د یوې ستونزې لاملونه او پایلې وسپړي او بېلابېل حلونه وړاندیز کړي.'),
    ('Analyze how a writer/ poet uses language to appeal to the senses through use of figurative language including similes, metaphors and imagery.', 'تجزیہ کریں کہ ایک مصنف/ شاعر تشبیہات، استعارات اور پیکر تراشی سمیت مجازی زبان کے ذریعے حواس کو متاثر کرنے کے لیے زبان کیسے استعمال کرتا ہے۔', 'تحلیل کړي چې یو لیکوال/ شاعر د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې له لارې حواسو ته د اپیل لپاره ژبه څنګه کاروي.'),
    ('Identify, analyze and construct conditional sentences', 'شرطیہ جملوں کی نشاندہی، تجزیہ اور تشکیل کریں', 'شرطي جملې وپېژني، تحلیل او جوړې کړي'),
    ('Analyze and construct simple, compound and complex sentences', 'سادہ، مرکب اور پیچیدہ جملوں کا تجزیہ اور تشکیل کریں', 'ساده، مرکبې او پېچلې جملې تحلیل او جوړې کړي'),
])
op = BOOK.record(o, 'eng12-u12-outcomes', 'Unit 12 — learning outcomes', 'یونٹ 12 — تعلیمی نتائج', 'واحد 12 — د زده کړې پایلې', 61, [110], unit_title=UT)
op['sourceCoverIllustrationReview'] = "Silhouette illustration of the seven ages of man is decorative; not reproduced. The author credit “William Shakespeare” printed at the foot of p109 belongs to Unit 12."
issues = [{'id': 'eng12-p109', 'unit': 11, 'printedPage': 109, 'description': 'Second-conditional item 10 prints “s____ (be) able to enter university” (she); the right edge of p109 is clipped (“angry with you”, “buy a big house”, “promoted”, “travel the world”, “buy a new car”, “a good job”, “enter”, “more friends”, “to stay here”, “so many clothes”, “his number”, “cold weather”), completed from context.'}]

if __name__ == '__main__':
    BOOK.save(61, [(11, ex), (12, op)], issues=issues, complete_units=[11])
