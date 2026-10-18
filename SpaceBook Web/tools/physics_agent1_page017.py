from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
solution=[
 tr('In Standard form / scientific notation we can write the term as Bondlength = 0.000000000074 × 10⁰ m',
 'معیاری صورت یا سائنسی طرزِ اظہار میں ہم یوں لکھ سکتے ہیں: بند کی لمبائی = 0.000000000074 × 10⁰ میٹر۔',
 'په معیاري یا علمي بڼه داسې لیکلای شو: د تړون اوږدوالی = 0.000000000074 × 10⁰ متره.'),
 tr('For Standard form / scientific notation in order to get mantissa (M) in which the 1st digit before the decimal is non-zero, we have to move the decimal 11 digits to the right. Therefore, the power of 10 will be negative 11, that is Bondlength = 7.4 × 10⁻¹¹ m — Answer',
 'معیاری صورت یا سائنسی طرزِ اظہار میں ایسا مینٹیسا (M) حاصل کرنے کے لیے جس میں اعشاری نقطے سے پہلے پہلا ہندسہ غیر صفر ہو، اعشاری نقطہ 11 ہندسے دائیں طرف منتقل کرنا ہوگا۔ لہٰذا 10 کی قوت منفی 11 ہوگی، یعنی بند کی لمبائی = 7.4 × 10⁻¹¹ میٹر — جواب۔',
 'په معیاري یا علمي بڼه کې د داسې مانتیسا (M) د ترلاسه کولو لپاره چې له اعشاري ټکي مخکې لومړی رقم ناصفر وي، اعشاري ټکی باید 11 رقمونه ښي لوري ته ولېږدوو. نو د 10 توان منفي 11 دی، یعنې د تړون اوږدوالی = 7.4 × 10⁻¹¹ متره — ځواب.'),
 tr('Which is the bond length for diatomic hydrogen in standard form / scientific notation.',
 'یہ دو جوہری ہائیڈروجن کے بند کی لمبائی معیاری صورت یا سائنسی طرزِ اظہار میں ہے۔',
 'دا د دوه اټومي هایدروجن د تړون اوږدوالی په معیاري یا علمي بڼه دی.'),
 tr('Assignment 1.3 AVERAGE MASS OF HOUSE FLY','مشق 1.3: گھریلو مکھی کی اوسط کمیت','دنده 1.3: د کورنۍ مچۍ منځنۍ کتله'),
 tr('Adult housefly (Musca domestica) is having a mass of only about 0.000,021,4 kg. Express this number in standard form / scientific notation.',
 'بالغ گھریلو مکھی (Musca domestica) کی کمیت صرف تقریباً 0.000,021,4 کلوگرام ہے۔ اس عدد کو معیاری صورت یا سائنسی طرزِ اظہار میں ظاہر کریں۔',
 'د بالغې کورنۍ مچۍ (Musca domestica) کتله یوازې شاوخوا 0.000,021,4 کیلوګرامه ده. دا عدد په معیاري یا علمي بڼه څرګند کړئ.')
]
prefixes=[
 tr('A mechanism through which a very small or very large number is expressed in terms of power of ten by giving a proper name to it is called prefix to the power of ten.',
 'وہ طریقہ جس میں کسی بہت چھوٹے یا بہت بڑے عدد کو دس کی قوت کی صورت میں ظاہر کرکے اسے مناسب نام دیا جائے، دس کی قوت کا سابقہ کہلاتا ہے۔',
 'هغه طریقه چې یو ډېر کوچنی یا ډېر لوی عدد د لس د توان په بڼه ښيي او مناسب نوم ورکوي، د لس د توان مختاړی بلل کېږي.'),
 tr('Prefixes makes standard form to be written even more easily. Large numbers are simply written in more convenient prefix with units.',
 'سابقے معیاری صورت کو لکھنا مزید آسان بناتے ہیں۔ بڑے اعداد کو اکائیوں کے ساتھ مناسب سابقے استعمال کرکے سادہ انداز میں لکھا جاتا ہے۔',
 'مختاړي د معیاري بڼې لیکل لا اسانه کوي. لوی عددونه له واحدونو سره په مناسبو مختاړو په ساده ډول لیکل کېږي.'),
 tr('The thickness of a paper can be written conveniently in smaller units of millimetre instead of metre. Similarly the long distance between two cities may be expressed better in a bigger unit of distance, i.e., kilometre. A useful set of prefixes in SI to replace powers of 10 are given in table 1.5.',
 'کاغذ کی موٹائی میٹر کے بجائے ملی میٹر کی چھوٹی اکائی میں آسانی سے لکھی جا سکتی ہے۔ اسی طرح دو شہروں کے درمیان طویل فاصلہ بڑی اکائی، یعنی کلومیٹر، میں بہتر طور پر ظاہر کیا جا سکتا ہے۔ SI میں 10 کی قوتوں کی جگہ استعمال ہونے والے مفید سابقے جدول 1.5 میں دیے گئے ہیں۔',
 'د کاغذ ضخامت د متر پر ځای د ملي متر په کوچني واحد کې په اسانۍ لیکل کېدای شي. همدارنګه د دوو ښارونو ترمنځ اوږد واټن په لوی واحد، یعنې کیلومتر، کې ښه څرګندېدای شي. په SI کې د 10 د توانونو پر ځای د کارېدونکو ګټورو مختاړو ټولګه په 1.5 جدول کې ورکړل شوې ده.'),
 tr('CAN YOU TELL? Name the convenient unit you will use to measure. a) width of a book b) length of a room c) diameter of a wire d) mass of candy e) mass of cricket ball.',
 'کیا آپ بتا سکتے ہیں؟ درج ذیل پیمائشوں کے لیے مناسب اکائی کے نام بتائیں: الف) کتاب کی چوڑائی ب) کمرے کی لمبائی ج) تار کا قطر د) ٹافی کی کمیت ہ) کرکٹ کی گیند کی کمیت۔',
 'آیا ویلای شئ؟ د لاندې شیانو د اندازه کولو لپاره مناسب واحدونه ونوموئ: الف) د کتاب پلنوالی ب) د خونې اوږدوالی ج) د تار قطر د) د خوږې کتله هـ) د کرکټ د توپ کتله.')
]
rows=[['Exa','10¹⁸','E','deci','10⁻¹','d'],['Peta','10¹⁵','P','centi','10⁻²','c'],['Tera','10¹²','T','milli','10⁻³','m'],['giga','10⁹','G','micro','10⁻⁶','μ'],['Mega','10⁶','M','nano','10⁻⁹','n'],['kilo','10³','k','pico','10⁻¹²','p'],['hecto','10²','h','femto','10⁻¹⁵','f'],['deca','10¹','da','atto','10⁻¹⁸','a']]
names=[['ایگزا','ڈیسی'],['پیٹا','سینٹی'],['ٹیرا','ملی'],['گیگا','مائیکرو'],['میگا','نینو'],['کلو','پیکو'],['ہیکٹو','فیمٹو'],['ڈیکا','ایٹو']]
ps=[['اېکسا','دېسي'],['پېټا','سانتي'],['ټېرا','ملي'],['ګیګا','مایکرو'],['مېګا','نانو'],['کیلو','پیکو'],['هېکټو','فېمټو'],['دېکا','اټو']]
table=dict(id='table1.5',sourceNumber='TABLE 1.5',title='TABLE 1.5 PREFIXES',sourcePdfPage=17,sourcePrintedPage=12,headers=['Prefix','Decimal Multiplier','Symbol','Prefix','Decimal Multiplier','Symbol'],rows=rows,
 translations=[dict(language=lang,headers=headers,rows=[[translation[i][0],r[1],r[2],translation[i][1],r[4],r[5]] for i,r in enumerate(rows)]) for lang,headers,translation in [('اردو',['سابقہ','اعشاری ضربی عامل','علامت','سابقہ','اعشاری ضربی عامل','علامت'],names),('پښتو',['مختاړی','اعشاري ضریب','نښه','مختاړی','اعشاري ضریب','نښه'],ps)]])
example=dict(num='1.3',title='SMALLEST MOLECULE',statement='The smallest molecule is the diatomic hydrogen (H₂), with a bond length of 0.000,000,000,074 m. Write the answer in Standard form.',given='Bond length = 0.000000000074 m',required='Standard form',formula='N = M × 10ⁿ',solution='\n\n'.join(p['text'] for p in solution[:3]),answer='7.4 × 10⁻¹¹ m',sourcePdfPages=[16,17],sourcePrintedPages=[11,12],solutionOrigin='textbook')
save(dict(pdfPage=17,printedPage=12,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Example 1.3 solution / Assignment 1.3 / 1.5 Prefixes',numericals=[example],tables=[table],sections=[dict(code='1.4',heading='1.4 Standard Form / Scientific Notation',paras=solution,blocks=[dict(type='assignment',number='1.3',question=solution[-1]['text'])]),dict(code='1.5',heading='1.5 Prefixes to Power of Ten',paras=prefixes,blocks=[dict(type='dataTable',**table)])],comparison='Completed cross-page example solution; preserved source prefix table number 1.5 and all sixteen prefixes; question labels retained without invented answers'))
render(18)
