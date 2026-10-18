# -*- coding: utf-8 -*-
"""Unit 4 part C — PDF 77-82 (printed 74-79): organelles, nucleus, prokaryotic vs eukaryotic table."""
import unit4_figs2 as G

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def f(fn, en, ur, ps):
    return fn(en), fn(ur), fn(ps)


def extend_4_3(s):
    s.pdf_pages += [77, 78, 79, 80, 81, 82]
    s.h('Endoplasmic Reticulum', 'اینڈوپلازمک ریٹیکولم', 'انډوپلازمیک ریټیکولم')
    s.p('It is a system of membranes found throughout the cell. The membranes form a series of sheets which enclose flattened sacs called cisternae. Their main function is to transport materials. Endoplasmic Reticulum is of two types:',
        'یہ جھلیوں کا ایک نظام ہے جو پورے خلیے میں پایا جاتا ہے۔ جھلیاں چادروں کا ایک سلسلہ بناتی ہیں جو چپٹی تھیلیوں کو گھیرتی ہیں جنہیں سسٹرنی کہتے ہیں۔ ان کا بنیادی کام مادوں کی ترسیل ہے۔ اینڈوپلازمک ریٹیکولم کی دو اقسام ہیں:',
        'دا د غشاوو یو سیسټم دی چې په ټوله حجره کې موندل کېږي. غشاوې د پاڼو یوه لړۍ جوړوي چې پلنې کڅوړې را ګرځوي چې سیسټرني بلل کېږي. اصلي دنده یې د موادو لېږد دی. انډوپلازمیک ریټیکولم دوه ډوله دی:')
    s.p('a. Smooth Endoplasmic Reticulum (SER): It is non-granular as the ribosomes are not attached to its surface. It plays an important role in lipid formation and transportation of materials.',
        'a. ہموار اینڈوپلازمک ریٹیکولم (SER): یہ دانے دار نہیں ہوتا کیونکہ اس کی سطح سے رائبوسومز جڑے نہیں ہوتے۔ یہ لپڈ بنانے اور مادوں کی ترسیل میں اہم کردار ادا کرتا ہے۔',
        'a. هوار انډوپلازمیک ریټیکولم (SER): دا دانه لرونکی نه دی ځکه چې رایبوزومونه یې له سطحې سره نه دي نښتي. دا د لیپیډ په جوړولو او د موادو په لېږد کې مهم رول لري.')
    s.p('b. Rough Endoplasmic Reticulum (RER): It is granular because ribosomes are attached to it. It is involved in protein synthesis. Its function is to transport materials from inside nucleus to cytoplasm and vice versa.',
        'b. کھردرا اینڈوپلازمک ریٹیکولم (RER): یہ دانے دار ہوتا ہے کیونکہ اس سے رائبوسومز جڑے ہوتے ہیں۔ یہ پروٹین سازی میں حصہ لیتا ہے۔ اس کا کام مرکزے کے اندر سے سائٹوپلازم تک اور اس کے برعکس مادوں کی ترسیل ہے۔',
        'b. زیږ انډوپلازمیک ریټیکولم (RER): دا دانه لرونکی دی ځکه چې رایبوزومونه ورسره نښتي دي. دا د پروټین په جوړولو کې ونډه لري. دنده یې د هستې له دننه سایټوپلازم ته او برعکس د موادو لېږد دی.')
    s.fig('bio4-fig4-10', *f(G.er, G.ER_EN, G.ER_UR, G.ER_PS), .55, caption=('Figure 4.10: Endoplasmic Reticulum', 'شکل 4.10: اینڈوپلازمک ریٹیکولم', 'شکل 4.10: انډوپلازمیک ریټیکولم'))
    s.h('Golgi Apparatus', 'گولجی اپریٹس', 'ګولجي اپراټس')
    s.p('It is a set of flattened sacs (cisternae) which are stacked together. It is named after its discoverer Camillo Golgi. Its function is to store the secretions, convert them into finished products and pack them into small rounded sacs called Golgi vesicles. These sacs are kept in cell or transported to exterior in the form of secretions. Plant cells have large number of stacks in their Golgi apparatus.',
        'یہ ایک دوسرے پر رکھی ہوئی چپٹی تھیلیوں (سسٹرنی) کا مجموعہ ہے۔ اس کا نام اس کے دریافت کنندہ کیمیلو گولجی کے نام پر رکھا گیا ہے۔ اس کا کام رطوبتوں کو ذخیرہ کرنا، انہیں تیار شدہ اشیا میں بدلنا اور چھوٹی گول تھیلیوں میں بند کرنا ہے جنہیں گولجی ویسیکلز کہتے ہیں۔ یہ تھیلیاں خلیے میں رکھی جاتی ہیں یا رطوبتوں کی شکل میں باہر بھیجی جاتی ہیں۔ پودوں کے خلیوں کے گولجی اپریٹس میں تہوں کی بڑی تعداد ہوتی ہے۔',
        'دا د پلنو کڅوړو (سیسټرني) یوه ټولګه ده چې پر یو بل ایښودل شوي. نوم یې د کشف کوونکي کامیلو ګولجي په نوم دی. دنده یې د افرازاتو زېرمه کول، په بشپړو محصولاتو بدلول او په کوچنیو ګردو کڅوړو کې بسته کول دي چې ګولجي ویسیکلونه بلل کېږي. دا کڅوړې په حجره کې ساتل کېږي یا د افرازاتو په بڼه بهر ته لېږل کېږي. د بوټو حجرې په خپل ګولجي اپراټس کې ډېر پوړونه لري.')
    s.fig('bio4-fig4-11', *f(G.golgi_fig, G.GO_EN, G.GO_UR, G.GO_PS), .5, caption=('Figure 4.11: Golgi Apparatus', 'شکل 4.11: گولجی اپریٹس', 'شکل 4.11: ګولجي اپراټس'))
    s.callout(SI, [('In 1906 Golgi was awarded Nobel Prize for physiology and medicine.', '1906ء میں گولجی کو فزیالوجی اور طب کا نوبل انعام دیا گیا۔', 'په 1906 کې ګولجي ته د فزیولوژي او طب نوبل جایزه ورکړل شوه.')])
    s.h('Mitochondria', 'مائٹوکونڈریا', 'مایټوکونډریا')
    s.p('Mitochondria are found in eukaryotic cells. They are bounded by a double membrane. The outer membrane is smooth. The inner membrane is folded inwards, giving rise to extensions called cristae. Cristae increase the surface area on which respiratory process takes place. Mitochondria are the powerhouse of the cell because they carry out respiration in cell and produce energy in the form of ATP.',
        'مائٹوکونڈریا یوکیریوٹک خلیوں میں پائے جاتے ہیں۔ یہ دوہری جھلی سے گھرے ہوتے ہیں۔ بیرونی جھلی ہموار ہوتی ہے۔ اندرونی جھلی اندر کی طرف تہ در تہ ہوتی ہے جس سے کرسٹی نامی ابھار بنتے ہیں۔ کرسٹی وہ سطحی رقبہ بڑھاتے ہیں جس پر تنفس کا عمل ہوتا ہے۔ مائٹوکونڈریا خلیے کا پاور ہاؤس ہیں کیونکہ یہ خلیے میں تنفس کرتے ہیں اور اے ٹی پی کی شکل میں توانائی پیدا کرتے ہیں۔',
        'مایټوکونډریا په یوکاریوټیکو حجرو کې موندل کېږي. په دوه ګونې غشا را ګرځېدلي دي. بهرنۍ غشا هواره ده. داخلي غشا دننه خوا ته قات شوې او کریسټي نومې ودې جوړوي. کریسټي هغه سطحه زیاتوي چې پرې تنفسي پروسه ترسره کېږي. مایټوکونډریا د حجرې د برېښنا کور دی ځکه چې په حجره کې تنفس کوي او د ATP په بڼه انرژي تولیدوي.')
    s.callout(SI, [('In Prokaryotes, Mitochondria are absent and it is thought that energy required is produced in the cytoplasm by anaerobic respiration or by mesosomes.',
                    'پروکیریوٹس میں مائٹوکونڈریا نہیں ہوتے اور خیال کیا جاتا ہے کہ درکار توانائی سائٹوپلازم میں غیر ہوائی تنفس یا میزوسومز کے ذریعے پیدا ہوتی ہے۔',
                    'په پروکاریوټونو کې مایټوکونډریا نشته او ګمان کېږي چې اړینه انرژي په سایټوپلازم کې د غیر هوایي تنفس یا میزوزومونو له لارې تولیدېږي.')])
    s.fig('bio4-fig4-12', *f(G.mito_fig, G.MI_EN, G.MI_UR, G.MI_PS), .5, caption=('Figure 4.12 Mitochondrion', 'شکل 4.12 مائٹوکونڈریون', 'شکل 4.12 مایټوکونډریون'))
    s.callout(SI, [('The cells which are more active e.g. liver cells have more than one thousand mitochondria. The cells which are less active e.g. cells of earlobe have very small number of mitochondria.',
                    'زیادہ فعال خلیوں مثلاً جگر کے خلیوں میں ایک ہزار سے زیادہ مائٹوکونڈریا ہوتے ہیں۔ کم فعال خلیوں مثلاً کان کی لو کے خلیوں میں مائٹوکونڈریا کی تعداد بہت کم ہوتی ہے۔',
                    'ډېرې فعالې حجرې لکه د ځيګر حجرې له زرو ډېر مایټوکونډریا لري. لږ فعالې حجرې لکه د غوږ د نرمې حجرې ډېر لږ مایټوکونډریا لري.')])
    s.h('Ribosomes', 'رائبوسومز', 'رایبوزومونه')
    s.p('These are tiny granules. They are formed in nucleolus and are either freely dispersed in the cytoplasm or attached with RER. A ribosome is made of almost equal amounts of proteins and ribosomal RNA (rRNA). Ribosomes are not bound by membranes. So they are also found in prokaryotes. Eukaryotic ribosomes are slightly larger than prokaryotic ribosomes. They are involved in protein synthesis. A ribosome consists of two sub units; the larger and the smaller subunit.',
        'یہ ننھے دانے ہیں۔ یہ نیوکلیولس میں بنتے ہیں اور یا تو سائٹوپلازم میں آزادانہ بکھرے ہوتے ہیں یا RER سے جڑے ہوتے ہیں۔ رائبوسوم تقریباً برابر مقدار میں پروٹینز اور رائبوسومل آر این اے (rRNA) سے بنا ہوتا ہے۔ رائبوسومز جھلی سے گھرے نہیں ہوتے، اس لیے یہ پروکیریوٹس میں بھی پائے جاتے ہیں۔ یوکیریوٹک رائبوسومز پروکیریوٹک رائبوسومز سے کچھ بڑے ہوتے ہیں۔ یہ پروٹین سازی میں حصہ لیتے ہیں۔ رائبوسوم دو ذیلی اکائیوں یعنی بڑی اور چھوٹی ذیلی اکائی پر مشتمل ہوتا ہے۔',
        'دا کوچنۍ دانې دي. په نیوکلیولس کې جوړېږي او یا په سایټوپلازم کې آزاد خپاره وي یا له RER سره نښتي وي. رایبوزوم شاوخوا په برابر مقدار له پروټینونو او رایبوزومي RNA (rRNA) جوړ دی. رایبوزومونه په غشا نه دي را ګرځېدلي. نو په پروکاریوټونو کې هم موندل کېږي. یوکاریوټیک رایبوزومونه له پروکاریوټیکو یو څه لوی دي. د پروټین په جوړولو کې ونډه لري. رایبوزوم له دوو فرعي واحدونو جوړ دی؛ لوی او کوچنی فرعي واحد.')
    s.fig('bio4-fig4-13', *f(G.ribosome_fig, G.RB_EN, G.RB_UR, G.RB_PS), .4, caption=('Fig. 4.13: Subunits of Ribsome', 'شکل 4.13: رائبوسوم کی ذیلی اکائیاں', 'شکل 4.13: د رایبوزوم فرعي واحدونه'))
    s.h('Plastids', 'پلاسٹڈز', 'پلاسټیډونه')
    s.p('These are membrane bound organelles which contain one or more pigments. Plastids are present only in the cells of plants and photosynthetic protists. Plastids are of three types;',
        'یہ جھلی دار عضیات ہیں جن میں ایک یا زیادہ رنگدار مادے ہوتے ہیں۔ پلاسٹڈز صرف پودوں اور ضیائی تالیف کرنے والے پروٹسٹس کے خلیوں میں ہوتے ہیں۔ پلاسٹڈز کی تین اقسام ہیں؛',
        'دا غشا لرونکي اورګانیلونه دي چې یو یا ډېر رنګونه لري. پلاسټیډونه یوازې د بوټو او فوتوسنتیټیکو پروټیسټونو په حجرو کې وي. پلاسټیډونه درې ډوله دي؛')
    s.h('Chloroplast', 'کلوروپلاسٹ', 'کلوروپلاسټ')
    s.p('The most important and abundant plastids are the chloroplasts. These are present in green parts of plants, particularly in leaves where photosynthesis takes place.',
        'سب سے اہم اور وافر پلاسٹڈز کلوروپلاسٹ ہیں۔ یہ پودوں کے سبز حصوں خاص طور پر پتوں میں ہوتے ہیں جہاں ضیائی تالیف ہوتی ہے۔',
        'تر ټولو مهم او ډېر پلاسټیډونه کلوروپلاسټونه دي. دا د بوټو په شنو برخو په ځانګړي ډول په پاڼو کې وي چېرته چې فوتوسنتز کېږي.')
    s.p('A chloroplast is bounded by a double membrane. The outer membrane is smooth while the inner membrane gives rise to sacs called thylakoids. The stack of thylakoids is known as granum (plural: grana). The thylakoids contain chlorophyll. The semi fluid present inside chloroplast is called stroma.',
        'کلوروپلاسٹ دوہری جھلی سے گھرا ہوتا ہے۔ بیرونی جھلی ہموار ہوتی ہے جبکہ اندرونی جھلی سے تھیلیاں بنتی ہیں جنہیں تھائیلاکوئیڈز کہتے ہیں۔ تھائیلاکوئیڈز کے ڈھیر کو گرینم (جمع: گرینا) کہتے ہیں۔ تھائیلاکوئیڈز میں کلوروفل ہوتا ہے۔ کلوروپلاسٹ کے اندر موجود نیم سیال کو اسٹروما کہتے ہیں۔',
        'کلوروپلاسټ په دوه ګونې غشا را ګرځېدلی دی. بهرنۍ غشا هواره ده او داخلي غشا کڅوړې جوړوي چې تایلاکویډونه بلل کېږي. د تایلاکویډونو ډېرۍ ته ګرانوم (جمع: ګرانا) ویل کېږي. تایلاکویډونه کلوروفیل لري. د کلوروپلاسټ دننه نیمه مایع ته سټروما ویل کېږي.')
    s.callout(SI, [('Mitochondria and chloroplasts have their own DNA. Mitochondria also have their own ribosomes, which are similar to the ribosomes of bacteria.',
                    'مائٹوکونڈریا اور کلوروپلاسٹ کا اپنا ڈی این اے ہوتا ہے۔ مائٹوکونڈریا کے اپنے رائبوسومز بھی ہوتے ہیں جو بیکٹیریا کے رائبوسومز سے ملتے جلتے ہیں۔',
                    'مایټوکونډریا او کلوروپلاسټونه خپل DNA لري. مایټوکونډریا خپل رایبوزومونه هم لري چې د باکتریاوو له رایبوزومونو سره ورته دي.')])
    s.fig('bio4-fig4-14', *f(G.chloroplast_fig, G.CH_EN, G.CH_UR, G.CH_PS), .55, caption=('Figure 4.14: Chloroplast', 'شکل 4.14: کلوروپلاسٹ', 'شکل 4.14: کلوروپلاسټ'))
    s.h('Chromoplast', 'کروموپلاسٹ', 'کروموپلاسټ')
    s.p('In plants, colours other than green, are due to chromoplasts. These are present in the petals of the flowers and in the ripened fruits. Due to the presence of chromoplast, the bright coloured petals of flowers attract insects for pollination.',
        'پودوں میں سبز کے علاوہ دوسرے رنگ کروموپلاسٹ کی وجہ سے ہوتے ہیں۔ یہ پھولوں کی پتیوں اور پکے ہوئے پھلوں میں ہوتے ہیں۔ کروموپلاسٹ کی موجودگی کی وجہ سے پھولوں کی چمکدار رنگ کی پتیاں پولینیشن کے لیے کیڑوں کو اپنی طرف کھینچتی ہیں۔',
        'په بوټو کې له شین پرته نور رنګونه د کروموپلاسټونو له امله وي. دا د ګلانو په پاڼو او پخو مېوو کې وي. د کروموپلاسټ د شتون له امله د ګلانو روښانه رنګه پاڼې د ګردې لپاره حشرات راکاږي.')
    s.h('Leucoplasts', 'لیوکوپلاسٹ', 'لیوکوپلاسټونه')
    s.p('Leucoplasts are colourless plastids. These are found in such parts of the plants where they store food particularly in roots.',
        'لیوکوپلاسٹ بے رنگ پلاسٹڈز ہیں۔ یہ پودوں کے ان حصوں میں پائے جاتے ہیں جہاں یہ خوراک ذخیرہ کرتے ہیں خاص طور پر جڑوں میں۔',
        'لیوکوپلاسټونه بې رنګه پلاسټیډونه دي. د بوټو په هغو برخو کې موندل کېږي چېرته چې خواړه زېرمه کوي په ځانګړي ډول په ریښو کې.')
    s.h('Cytoskeleton', 'سائٹو اسکیلیٹن', 'سایټواسکلېټن')
    s.p('It is a network of filaments (called microfilaments) and tubules (called microtubules). It is scattered in the cytoplasm. Microtubules are made of tubulin protein and are used by cells to hold their shape. Microtubules also make cilia and flagella. Microfilaments are made of actin protein. These are used by cells to change their shapes.',
        'یہ ریشوں (جنہیں مائیکرو فلامنٹس کہتے ہیں) اور نلکیوں (جنہیں مائیکرو ٹیوبولز کہتے ہیں) کا ایک جال ہے۔ یہ سائٹوپلازم میں بکھرا ہوتا ہے۔ مائیکرو ٹیوبولز ٹیوبولن پروٹین سے بنے ہوتے ہیں اور خلیات انہیں اپنی شکل برقرار رکھنے کے لیے استعمال کرتے ہیں۔ مائیکرو ٹیوبولز سیلیا اور فلیجیلا بھی بناتے ہیں۔ مائیکرو فلامنٹس ایکٹن پروٹین سے بنے ہوتے ہیں۔ خلیات انہیں اپنی شکل بدلنے کے لیے استعمال کرتے ہیں۔',
        'دا د تارونو (چې مایکروفلامنټونه بلل کېږي) او نلونو (چې مایکروټیوبولونه بلل کېږي) یوه شبکه ده. په سایټوپلازم کې خپره ده. مایکروټیوبولونه له ټیوبولین پروټین جوړ دي او حجرې یې د خپلې بڼې د ساتلو لپاره کاروي. مایکروټیوبولونه سیلیا او فلاجیلا هم جوړوي. مایکروفلامنټونه له اکټین پروټین جوړ دي. حجرې یې د خپلې بڼې د بدلولو لپاره کاروي.')
    s.fig('bio4-fig4-15', *f(G.cytoskeleton_fig, G.CY_EN, G.CY_UR, G.CY_PS), .6, caption=('Figure 4.15: Cytoskeleton', 'شکل 4.15: سائٹو اسکیلیٹن', 'شکل 4.15: سایټواسکلېټن'))
    s.h('Centriole', 'سینٹریول', 'سنټریول')
    s.p('These are hollow and cylindrical organelles present in the cells of animals and many unicellular organisms. These are two in number and are collectively called centrosome. Each centriole contains nine triplets of microtubules. Their function is to form spindle fibres during cell division. Spindle fibres help in chromosome movement during cell division.',
        'یہ کھوکھلے اور نلکی نما عضیات ہیں جو جانوروں اور بہت سے یک خلوی جانداروں کے خلیوں میں ہوتے ہیں۔ یہ تعداد میں دو ہوتے ہیں اور مل کر سینٹروسوم کہلاتے ہیں۔ ہر سینٹریول میں مائیکرو ٹیوبولز کے نو ٹرپلٹس ہوتے ہیں۔ ان کا کام خلوی تقسیم کے دوران اسپنڈل فائبرز بنانا ہے۔ اسپنڈل فائبرز خلوی تقسیم کے دوران کروموسومز کی حرکت میں مدد دیتے ہیں۔',
        'دا تش او استوانه یي اورګانیلونه دي چې د ژویو او ډېرو یو حجروي موجوداتو په حجرو کې وي. شمېر یې دوه دی او په ګډه سنټروزوم بلل کېږي. هر سنټریول د مایکروټیوبولونو نهه درې ګوني لري. دنده یې د حجروي وېش پر مهال د سپنډل تارونو جوړول دي. سپنډل تارونه د حجروي وېش پر مهال د کروموزومونو په حرکت کې مرسته کوي.')
    s.callout(('Point to remember', 'یاد رکھنے کا نکتہ', 'د یادولو ټکی'), [('In cells that contain cilia and or flagella, centrioles are involved in the formation of cilia and flagella.',
                                                                     'جن خلیوں میں سیلیا اور یا فلیجیلا ہوتے ہیں، ان میں سینٹریولز سیلیا اور فلیجیلا بنانے میں حصہ لیتے ہیں۔',
                                                                     'په هغو حجرو کې چې سیلیا او یا فلاجیلا لري، سنټریولونه د سیلیا او فلاجیلا په جوړولو کې ونډه لري.')])
    s.fig('bio4-fig4-16', *f(G.centriole_fig, G.CE_EN, G.CE_UR, G.CE_PS), .6, caption=('Figure 4.16: Centriole', 'شکل 4.16: سینٹریول', 'شکل 4.16: سنټریول'))
    s.h('Vacuole', 'ویکیول', 'واکیول')
    s.p('Vacuole is a fluid filled sac bounded by a single membrane called tonoplast. Animal cells contain more than one small vacuoles. In mature plant cells, many small vacuole fuse together to make one large central vacuole. The large vacuole contains water, salts and other materials. It pushes other materials towards cell wall and plant cell become turgid.',
        'ویکیول سیال سے بھری ایک تھیلی ہے جو ایک جھلی سے گھری ہوتی ہے جسے ٹونوپلاسٹ کہتے ہیں۔ جانوروں کے خلیوں میں ایک سے زیادہ چھوٹے ویکیول ہوتے ہیں۔ پودوں کے پختہ خلیوں میں بہت سے چھوٹے ویکیول مل کر ایک بڑا مرکزی ویکیول بناتے ہیں۔ بڑے ویکیول میں پانی، نمکیات اور دیگر مادے ہوتے ہیں۔ یہ دوسرے مادوں کو خلوی دیوار کی طرف دھکیلتا ہے اور پودے کا خلیہ تنا ہوا (ٹرجڈ) ہو جاتا ہے۔',
        'واکیول له مایع ډکه کڅوړه ده چې په یوه غشا را ګرځېدلې چې ټونوپلاسټ بلل کېږي. د ژویو حجرې له یو ډېر کوچني واکیولونه لري. د بوټو په بالغو حجرو کې ډېر کوچني واکیولونه سره یوځای کېږي او یو لوی مرکزي واکیول جوړوي. لوی واکیول اوبه، مالګې او نور مواد لري. نور مواد د حجرې دېوال ته ټېلوي او د بوټي حجره ټینګه (ټرجډ) کېږي.')
    s.p('Many organisms take in materials from outside in the form of food vacuoles. Some unicellular organisms use contractile vacuole for the excretion of wastes.',
        'بہت سے جاندار باہر سے مادے غذائی ویکیول کی شکل میں اندر لیتے ہیں۔ بعض یک خلوی جاندار فضلات کے اخراج کے لیے کونٹریکٹائل ویکیول استعمال کرتے ہیں۔',
        'ډېر موجودات له بهر څخه مواد د غذايي واکیولونو په بڼه اخلي. ځینې یو حجروي موجودات د فاضله موادو د اطراح لپاره انقباضي واکیول کاروي.')
    s.h('Lysosome', 'لائسوسوم', 'لایزوزوم')
    s.p('These are single membrane bound organelles. Lysosomes contain strong digestive enzymes. They break down food and waste materials within the cell. During its function, a lysosome fuses with the vacuole that contains the material and its enzymes break down the material.',
        'یہ ایک جھلی والے عضیات ہیں۔ لائسوسومز میں طاقتور ہاضم انزائمز ہوتے ہیں۔ یہ خلیے کے اندر خوراک اور فضلات کو توڑتے ہیں۔ اپنے کام کے دوران لائسوسوم اس ویکیول سے مل جاتا ہے جس میں مادہ ہوتا ہے اور اس کے انزائمز مادے کو توڑ دیتے ہیں۔',
        'دا یو غشا لرونکي اورګانیلونه دي. لایزوزومونه قوي هاضمه انزایمونه لري. د حجرې دننه خواړه او فاضله مواد ماتوي. د خپلې دندې پر مهال لایزوزوم له هغه واکیول سره یوځای کېږي چې مواد لري او انزایمونه یې مواد ماتوي.')
    s.fig('bio4-fig4-17', *f(G.vacuole_lysosome, G.VL_EN, G.VL_UR, G.VL_PS), .7, caption=('Figure 4.17: a) Central Vacuole in plant cell, b) Lysosome', 'شکل 4.17: a) پودے کے خلیے میں مرکزی ویکیول، b) لائسوسوم', 'شکل 4.17: a) د بوټي په حجره کې مرکزي واکیول، b) لایزوزوم'))
    s.h('Nucleus', 'مرکزہ', 'هسته')
    s.p('The most important and visible part of a cell is the nucleus. It is present in the centre of the animal cell. In mature plant cells it is pushed to the side due to the presence of large central vacuole. The nucleus is bounded by a double membrane, called nuclear envelope. Inside nucleus, there is a granular matrix called nucleoplasm in which one or two nucleoli and chromosomes are present.',
        'خلیے کا سب سے اہم اور نمایاں حصہ مرکزہ ہے۔ یہ جانور کے خلیے کے مرکز میں ہوتا ہے۔ پودوں کے پختہ خلیوں میں بڑے مرکزی ویکیول کی موجودگی کی وجہ سے یہ ایک طرف دھکیل دیا جاتا ہے۔ مرکزہ ایک دوہری جھلی سے گھرا ہوتا ہے جسے مرکزی لفافہ کہتے ہیں۔ مرکزے کے اندر ایک دانے دار میٹرکس ہوتا ہے جسے نیوکلیوپلازم کہتے ہیں جس میں ایک یا دو نیوکلیولائی اور کروموسومز ہوتے ہیں۔',
        'د حجرې تر ټولو مهمه او ښکاره برخه هسته ده. دا د ژوي د حجرې په منځ کې وي. د بوټو په بالغو حجرو کې د لوی مرکزي واکیول د شتون له امله یوې خوا ته ټېله کېږي. هسته په دوه ګونې غشا را ګرځېدلې چې هستوي پوښ بلل کېږي. د هستې دننه دانه لرونکی میټرکس دی چې نیوکلیوپلازم بلل کېږي او پکې یو یا دوه نیوکلیولونه او کروموزومونه وي.')
    s.callout(SI, [('DNA is also responsible for the transmission of characteristics to the next generation. That is why, it is called the hereditary material.',
                    'ڈی این اے اگلی نسل میں خصوصیات کی منتقلی کا بھی ذمہ دار ہے۔ اسی لیے اسے موروثی مادہ کہتے ہیں۔',
                    'DNA راتلونکي نسل ته د ځانګړتیاوو د لېږد مسؤل هم دی. له همدې امله ارثي ماده بلل کېږي.')])
    s.p('The chromosomes are more visible in a dividing cell. In non-dividing cells, chromosomes are in the form of a network of fine threads known as chromatin network. Chromosomes are made of Deoxyribonucleic acid (DNA) and proteins. DNA controls all the activities of the cell. The chromosome number is always specific for a particular species.',
        'تقسیم ہوتے ہوئے خلیے میں کروموسومز زیادہ نمایاں ہوتے ہیں۔ غیر تقسیم شدہ خلیوں میں کروموسومز باریک دھاگوں کے جال کی شکل میں ہوتے ہیں جسے کرومیٹن نیٹ ورک کہتے ہیں۔ کروموسومز ڈی آکسی رائبو نیوکلک ایسڈ (DNA) اور پروٹینز سے بنے ہوتے ہیں۔ ڈی این اے خلیے کی تمام سرگرمیوں کو کنٹرول کرتا ہے۔ کروموسومز کی تعداد کسی خاص نوع کے لیے ہمیشہ مخصوص ہوتی ہے۔',
        'په وېشل کېدونکې حجره کې کروموزومونه ډېر ښکاري. په نه وېشل کېدونکو حجرو کې کروموزومونه د نریو تارونو د شبکې په بڼه وي چې د کروماټین شبکه بلل کېږي. کروموزومونه له ډي اکسي رایبو نیوکلیک اسید (DNA) او پروټینونو جوړ دي. DNA د حجرې ټول فعالیتونه کنټرولوي. د کروموزومونو شمېر د یوې ځانګړې نوعې لپاره تل ټاکلی وي.')
    s.p('For example in human cell it is 46, in raddish 18 and in onion 16. The prokaryotic cells do not contain prominent nucleus. Rather, their chromosome is made of DNA only and is submerged in the cytoplasm.',
        'مثال کے طور پر انسانی خلیے میں یہ 46، مولی میں 18 اور پیاز میں 16 ہے۔ پروکیریوٹک خلیوں میں نمایاں مرکزہ نہیں ہوتا۔ بلکہ ان کا کروموسوم صرف ڈی این اے سے بنا ہوتا ہے اور سائٹوپلازم میں ڈوبا ہوتا ہے۔',
        'د بېلګې په توګه په انساني حجره کې 46، په ملۍ کې 18 او په پیاز کې 16 دی. پروکاریوټیکې حجرې څرګنده هسته نه لري. بلکې کروموزوم یې یوازې له DNA جوړ دی او په سایټوپلازم کې ډوب دی.')
    s.fig('bio4-fig4-18', *f(G.nucleus_fig, G.NU_EN, G.NU_UR, G.NU_PS), .5, caption=('Figure 4.18: The Nucleus', 'شکل 4.18: مرکزہ', 'شکل 4.18: هسته'))
    s.h('4.3 Differences between Prokaryotic and Eukaryotic cell', '4.3 پروکیریوٹک اور یوکیریوٹک خلیے میں فرق', '4.3 د پروکاریوټیکې او یوکاریوټیکې حجرې توپیرونه')
    s.p('All cellular organisms seem to fall into two natural groups known as prokaryotes and eukaryotes. These two groups are fundamentally different.',
        'تمام خلوی جاندار دو قدرتی گروہوں میں تقسیم معلوم ہوتے ہیں جنہیں پروکیریوٹس اور یوکیریوٹس کہتے ہیں۔ یہ دونوں گروہ بنیادی طور پر مختلف ہیں۔',
        'ټول حجروي موجودات داسې ښکاري چې په دوو طبیعي ډلو کې راځي چې پروکاریوټونه او یوکاریوټونه بلل کېږي. دا دوه ډلې بنسټیز توپیر لري.')
    s.table('bio4-tab-pro-eu', ['', 'Prokaryotic Cell', 'Eukaryotic Cell'],
            [['1', 'They lack membrane bounded nucleus.', 'The nuclear material is surrounded by a double membrane.'],
             ['2', 'Membrane bounded organelles are absent.', 'Membrane bounded organelles are present.'],
             ['3', 'Ribosome are smaller in size.', 'Ribosome are larger in size.'],
             ['4', 'Cell wall is made of peptidoglycan (a single large polymer of amino acids and sugar)', 'Cell wall is made of cellulose (plants) or chitin (fungi).'],
             ['5', 'Comparatively smaller in size (0.5 nm)', 'Larger in size (10-100 nm)'],
             ['6', 'Example are Bacteria and Cyanobacteria.', 'Examples are protista, fungi, plants and animals']],
            ['', 'پروکیریوٹک خلیہ', 'یوکیریوٹک خلیہ'],
            [['1', 'ان میں جھلی دار مرکزہ نہیں ہوتا۔', 'مرکزی مادہ دوہری جھلی سے گھرا ہوتا ہے۔'], ['2', 'جھلی دار عضیات نہیں ہوتے۔', 'جھلی دار عضیات ہوتے ہیں۔'],
             ['3', 'رائبوسوم چھوٹے ہوتے ہیں۔', 'رائبوسوم بڑے ہوتے ہیں۔'], ['4', 'خلوی دیوار پیپٹیڈوگلائکن (امائنو ایسڈز اور شکر کا ایک بڑا پولیمر) سے بنی ہوتی ہے', 'خلوی دیوار سیلولوز (پودے) یا کائٹن (فنجائی) سے بنی ہوتی ہے۔'],
             ['5', 'نسبتاً چھوٹے (0.5 nm)', 'بڑے (10-100 nm)'], ['6', 'مثالیں بیکٹیریا اور سائنو بیکٹیریا ہیں۔', 'مثالیں پروٹسٹا، فنجائی، پودے اور جانور ہیں']],
            ['', 'پروکاریوټیکه حجره', 'یوکاریوټیکه حجره'],
            [['1', 'غشا لرونکې هسته نه لري.', 'هستوي ماده په دوه ګونې غشا را ګرځېدلې ده.'], ['2', 'غشا لرونکي اورګانیلونه نشته.', 'غشا لرونکي اورګانیلونه شته.'],
             ['3', 'رایبوزومونه کوچني دي.', 'رایبوزومونه لوی دي.'], ['4', 'د حجرې دېوال له پیپټیډوګلایکان (د امینو اسیدونو او بورې یو لوی پولیمر) جوړ دی', 'د حجرې دېوال له سلولوز (بوټي) یا کایټین (فنجای) جوړ دی.'],
             ['5', 'نسبتاً کوچنۍ (0.5 nm)', 'لویه (10-100 nm)'], ['6', 'بېلګې یې باکتریا او سیانوباکتریا دي.', 'بېلګې یې پروټیسټا، فنجای، بوټي او ژوي دي']],
            ratio=1)
    s.p('SpaceBook note: the table prints cell sizes in nm (0.5 nm and 10-100 nm). Cells are usually measured in micrometres (about 0.5 μm and 10-100 μm). The printed values are kept above. The book also numbers this heading 4.3, the same number as "Cellular Structures and Functions".',
        'اسپیس بک نوٹ: جدول میں خلیوں کی جسامت نینو میٹر میں چھپی ہے (0.5 nm اور 10-100 nm)۔ خلیوں کو عموماً مائیکرو میٹر میں ناپا جاتا ہے (تقریباً 0.5 μm اور 10-100 μm)۔ چھپی ہوئی قدریں اوپر رکھی گئی ہیں۔ کتاب نے اس عنوان کو بھی 4.3 نمبر دیا ہے جو ”خلوی ساختیں اور افعال“ کا بھی نمبر ہے۔',
        'د سپېس بوک یادونه: جدول د حجرو اندازې په نانومتر کې چاپ کړې (0.5 nm او 10-100 nm). حجرې معمولاً په مایکرومتر کې اندازه کېږي (شاوخوا 0.5 μm او 10-100 μm). چاپ شوي ارزښتونه پورته ساتل شوي. کتاب دې سرلیک ته هم 4.3 شمېره ورکړې چې د ”حجروي جوړښتونه او دندې“ شمېره هم ده.', editorial=True)
