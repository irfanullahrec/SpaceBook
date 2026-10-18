"""HPE XII PDF18–23: pp.13–18 — flow of blood in the chambers, blood vessels (aorta, venae cavae, pulmonary vessels), functions of the heart, types of blood
vessels, blood (RBC, WBC, platelets), kinds of circulation (pulmonary, systemic — begins). Run: python class12_hpe_page018.py N (18–23)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, labelled, vessel_bed, lung_pair, T


def p18():
    b = Builder()
    b.h('Movement of blood in the chambers of the heart', 'دل کے خانوں میں خون کی آمد و رفت', 'د زړه په خونو کې د وینې راتګ او تګ')
    P(b, [('In both chambers on the right side of the heart impure blood (Deoxygenated Blood) is present, and in both chambers on the left side pure, i.e. oxygen-rich, blood (Oxygenated Blood) is present.',
           'دل کے دائیں طرف کے دونوں خانوں میں غیر صاف شدہ خون (Deoxygenated Blood) موجود ہوتا ہے اور بائیں طرف کے دونوں خانوں میں صاف یعنی آکسیجن سے بھرپور خون (Oxygenated Blood) ہوتا ہے۔',
           'د زړه د ښي اړخ په دواړو خونو کې ناپاکه وینه (Deoxygenated Blood) وي او د کیڼ اړخ په دواړو خونو کې پاکه، یعنې له اکسیجن ډکه وینه (Oxygenated Blood) وي.'),
          ('In the same way, between the right atrium and the right ventricle there is a valve (Valve), which is called the tricuspid (Tricuspid) valve. In the same way the middle valve (Valve) between the left atrium and the left ventricle is called the bicuspid valve (Bicuspid Valve).',
           'اسی طرح دائیں اُذن اور دائیں بطن کے درمیان ایک والو (Valve) ہوتا ہے جسے ٹرائی کسپیڈز (Tricuspid) والو بھی کہتے ہیں۔ اسی طرح بائیں اُذن اور بائیں بطن کے درمیانی والو (Valve) کو بائی کسپیڈ والو (Bicuspid Valve) کہتے ہیں۔',
           'همداسې د ښي اذین او ښي بطین ترمنځ یو والو (Valve) وي چې ټرای کسپیډ (Tricuspid) والو هم ورته ویل کېږي. همداسې د کیڼ اذین او کیڼ بطین ترمنځ والو (Valve) ته بای کسپیډ والو (Bicuspid Valve) ویل کېږي.')])
    b.h('Blood vessels', 'خون کی نالیاں', 'د وینې رګونه')
    b.h('Aorta', 'اے اورٹا (Aorta)', 'اورټا (Aorta)')
    P(b, [('This is the largest artery in the body and it arises from the left ventricle (Left ventricle) of the heart, and it supplies pure (Oxygenated Blood) blood full of nutrition to the whole body.',
           'یہ جسم میں سب سے بڑی شریان ہے اور یہ دل کے بائیں بطن یعنی (Left ventricle) سے نکلتی ہے اور یہ سارے جسم کو صاف (Oxygenated Blood) اور غذائیت سے بھرپور خون سپلائی کرتی ہے۔',
           'دا په بدن کې تر ټولو لوی شریان دی او د زړه له کیڼ بطین (Left ventricle) وځي او ټول بدن ته پاکه (Oxygenated Blood) او له تغذیې ډکه وینه رسوي.')])
    b.h('Superior vena cava and inferior vena cava', 'سپیریئر اینڈ انفیریئر وینا کیوا (Superior vena cava and inferior vena cava)', 'پورتنۍ او ښکتنۍ وینا کاوا (Superior vena cava and inferior vena cava)')
    P(b, [('These two blood vessels bring impure blood (Deoxygenated Blood) from the upper and lower parts of the body into the right atrium (Right Atrium) of the heart.',
           'یہ دونوں خون کی نالیاں جسم کے اوپر اور نچلے حصوں سے غیر صاف شدہ خون (Deoxygenated Blood) لا کر دل کے دائیں اُذن (Right Atrium) میں لاتی ہے۔',
           'دا دواړه رګونه د بدن له پورتنیو او ښکتنیو برخو ناپاکه وینه (Deoxygenated Blood) د زړه ښي اذین (Right Atrium) ته راوړي.')])
    b.h('Pulmonary Arteries', 'پلمونری شریانیں (Pulmonary Arteries)', 'د سږو شریانونه (Pulmonary Arteries)')
    P(b, [('These two arteries, leaving the right ventricle of the heart, send impure blood (Deoxygenated Blood) to the lungs for cleaning.',
           'یہ دونوں شریانیں دل کے دائیں بطن سے نکل کر غیر صاف شدہ خون (Deoxygenated Blood) پھیپھڑوں کو صاف کرنے کیلئے بھیجتی ہیں۔',
           'دا دواړه شریانونه د زړه له ښي بطین وځي او ناپاکه وینه (Deoxygenated Blood) سږو ته د پاکولو لپاره لېږي.')])
    b.h('Pulmonary Veins', 'پلمونری وریدیں (Pulmonary Veins)', 'د سږو وریدونه (Pulmonary Veins)')
    P(b, [('These veins bring pure blood (Oxygenated Blood) from the lungs back into the left atrium of the heart, i.e. …',
           'یہ وریدیں پھیپھڑوں سے صاف خون یعنی (Oxygenated Blood) واپس دل کی بائیں اُذن یعنی …',
           'دا وریدونه له سږو پاکه وینه (Oxygenated Blood) بېرته د زړه کیڼ اذین، یعنې …')])
    r = rec(b, 2, 3, 18)
    BOOK.save(18, [(2, r)], issues=[{'id': 'hpe12-pdf018', 'unit': 2, 'printedPage': 13,
               'description': '“ٹرائی کسپیڈز”, “یہ دونوں خون کی نالیاں … لاتی ہے”, “دل کی بائیں اُذن”. A small owner pen mark is excluded. Retained as printed.'}])


def p19():
    b = Builder()
    P(b, [('… (Left Atrium).', '(Left Atrium) میں لاتی ہیں۔', '… (Left Atrium) ته راوړي.')])
    b.h('2. Functions of Heart', '2. دل کے افعال (Functions of Heart)', '2. د زړه دندې (Functions of Heart)')
    P(b, [('The heart does two works at the same time, i.e. it sends pure and impure blood into different blood vessels and brings it back. The heart supplies pure blood from the left ventricle to the whole body through the aorta (Aorta). In the same way, impure blood, collected from all parts of the body, is brought into the right atrium of the heart through the superior and inferior vena cava, and then this impure blood comes down through the tricuspid valve (Tricuspid Valve) into the right ventricle, and then sends the blood into the lungs through both pulmonary arteries. Here in the lungs carbon dioxide is expelled, and taking oxygen it brings pure blood through the pulmonary veins into the left atrium of the heart. After this the pure blood comes down through the bicuspid (Bicuspid) valve into the left ventricle, and from here through the aorta pure blood is supplied to the whole body. This circulation of blood continues.',
           'دل ایک ہی وقت میں دو کام کرتا ہے یعنی صاف اور غیر صاف خون کو مختلف خون کی نالیوں میں بھیجتا اور واپس لاتا ہے۔ دل بائیں بطن سے صاف خون اے اورٹا (Aorta) کے ذریعے سارے جسم کو سپلائی کرتا ہے۔ اور اس طرح غیر صاف شدہ خون جسم کے سارے حصوں سے اکٹھا کر کے بالائی اور زیریں وینا کیوا کے ذریعے دل کے دائیں اُذن میں لاتا ہے اور پھر یہ غیر صاف شدہ خون ٹرائی کسپیڈ والو (Tricuspid Valve) کے ذریعے نیچے دائیں بطن میں آتا ہے اور پھر پھیپھڑوں کے دونوں شریانوں کے ذریعے خون پھیپھڑوں میں بھیجتا ہے۔ یہاں یہ پھیپھڑوں میں کاربن ڈائی آکسائیڈ خارج کرتا ہے اور آکسیجن لے کر پلمونری وریدوں کے ذریعے دل کے بائیں اُذن میں صاف خون لاتا ہے۔ اس کے بعد صاف خون بائی کسپیڈ (Bicuspid) والو کے ذریعے نیچے بائیں بطن میں آ جاتا ہے اور یہاں سے اے اورٹا کے ذریعے سارے جسم کو صاف خون سپلائی ہوتا ہے۔ خون کی یہ گردش جاری و ساری رہتی ہے۔',
           'زړه په یوه وخت دوه کارونه کوي، یعنې پاکه او ناپاکه وینه بېلابېلو رګونو ته لېږي او بېرته یې راوړي. زړه له کیڼ بطین پاکه وینه د اورټا (Aorta) له لارې ټول بدن ته رسوي. همداسې ناپاکه وینه د بدن له ټولو برخو راټولوي او د پورتنۍ او ښکتنۍ وینا کاوا له لارې د زړه ښي اذین ته راوړي، بیا دا ناپاکه وینه د ټرای کسپیډ والو (Tricuspid Valve) له لارې ښکته ښي بطین ته راځي او بیا د سږو د دواړو شریانونو له لارې وینه سږو ته لېږي. دلته په سږو کې کاربن ډای اکسایډ وباسي او اکسیجن اخلي او د سږو د وریدونو له لارې پاکه وینه د زړه کیڼ اذین ته راوړي. له دې وروسته پاکه وینه د بای کسپیډ (Bicuspid) والو له لارې ښکته کیڼ بطین ته راځي او له دې ځایه د اورټا له لارې ټول بدن ته پاکه وینه رسېږي. د وینې دا ګرځښت دوام لري.')])
    b.h('Types of blood vessels', 'خون کی نالیوں کی اقسام (Types of blood vessels)', 'د وینې د رګونو ډولونه (Types of blood vessels)')
    b.p('Blood vessels are of three kinds.', 'خون کی نالیاں تین قسم کی ہوتی ہیں۔', 'د وینې رګونه درې ډوله دي.')
    b.group('lines', [('a) Arteries (Arteries)', 'a) شریانیں (Arteries)', 'a) شریانونه (Arteries)'), ('b) Veins (Veins)', 'b) وریدیں (Veins)', 'b) وریدونه (Veins)'), ('c) Capillaries (Capillaries)', 'c) عروقِ شعریہ (Capillaries)', 'c) شعریه رګونه (Capillaries)')])
    shp = vessel_bed(40, 70, 360) + '<path d="M400 20 v40" stroke="#dc2626" stroke-width="3"/><path d="M40 60 v-40" stroke="#1d4ed8" stroke-width="3"/>'
    labs = lambda c: labelled(440, 190, shp, [('from heart', 400, 16, 'middle', None, None), ('to heart', 40, 16, 'middle', None, None), ('artery', 330, 150, 'middle', 360, 80),
                                             ('capillaries', 220, 150, 'middle', 220, 95), ('vein', 110, 150, 'middle', 80, 80)], c)
    sv = [labs(c) for c in ('Artery, capillaries and vein', 'شریان، عروقِ شعریہ اور ورید', 'شریان، شعریه رګونه او ورید')]
    b.visual('hpe12-fig-vessel-types', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 2, 4, 19)
    BOOK.save(19, [(2, r)], issues=[{'id': 'hpe12-pdf019', 'unit': 2, 'printedPage': 14,
               'description': 'The illustration of an artery, capillary bed and vein is reproduced as a coded schematic with the printed labels (from heart, to heart, artery, capillaries, vein). Owner ballpoint writing (“M.Kamran”, “دل کے افعال”, scribbles) is excluded. The heading is numbered “2.” in print. Retained as printed.'}])


def p20():
    b = Builder()
    b.h('A) Arteries', 'A) شریانیں (Arteries)', 'A) شریانونه (Arteries)')
    P(b, [('Arteries are those blood vessels which come out of the heart and provide pure and nutrition-rich blood to the whole body (except the arteries of the lungs). Arteries are in the depth of the muscles of our body. These are elastic; therefore even arteries empty of blood maintain their structure.',
           'شریانیں خون کی وہ نالیاں ہیں جو دل سے نکلتی ہیں اور سارے جسم کو صاف اور غذائیت سے بھرپور خون مہیا کرتی ہیں (سوائے پھیپھڑوں کے شریانوں کے)۔ شریانیں ہماری جسم کے عضلات کی گہرائی میں ہوتے ہیں۔ یہ لچکدار ہوتی ہیں اس لئے خون سے خالی شریانیں بھی اپنی ساخت کو برقرار رکھتی ہیں۔',
           'شریانونه د وینې هغه رګونه دي چې له زړه وځي او ټول بدن ته پاکه او له تغذیې ډکه وینه برابروي (پرته د سږو له شریانونو). شریانونه زموږ د بدن د عضلو په ژورو کې وي. دا نرم او ارتجاعي وي، نو له وینې خالي شریانونه هم خپل جوړښت ساتي.')])
    b.h('B) Veins', 'B) وریدیں (Veins)', 'B) وریدونه (Veins)')
    P(b, [('In the capillaries oxygen and food components from the blood change into carbon dioxide and waste substances. After this the blood comes through small veins into the right atrium of the heart. In all veins there is impure blood (except the veins of the lungs). Veins in the body are under the skin and above the muscles. Veins are less elastic, and because of the expulsion of blood a difference comes in their structure. Their colour is blue and they are seen easily in the skin.',
           'عروقِ شعریہ میں خون سے آکسیجن اور غذائی اجزاء کاربن ڈائی آکسائیڈ اور فاضل مادوں میں تبدیل ہو جاتا ہے۔ اس کے بعد خون چھوٹی وریدوں کے ذریعے دل کے دائیں اُذن میں آ جاتا ہے۔ سارے وریدوں میں غیر صاف شدہ خون ہوتا ہے (سوائے پھیپھڑوں کی وریدوں کے)۔ وریدیں جسم میں جلد کے نیچے اور عضلات کے اوپر ہوتے ہیں۔ وریدیں کم لچکدار ہوتی ہیں اور خون کے اخراج سے اُس کی ساخت میں فرق آ جاتا ہے۔ ان کی رنگت نیلی ہوتی ہے اور جلد میں آسانی کے ساتھ نظر آتی ہیں۔',
           'په شعریه رګونو کې د وینې اکسیجن او غذايي اجزا په کاربن ډای اکسایډ او اضافي موادو اوړي. له دې وروسته وینه د وړو وریدونو له لارې د زړه ښي اذین ته راځي. په ټولو وریدونو کې ناپاکه وینه وي (پرته د سږو له وریدونو). وریدونه په بدن کې تر پوستکي لاندې او له عضلو پورته وي. وریدونه لږ ارتجاعي وي او د وینې په وتلو یې په جوړښت کې توپیر راځي. رنګ یې شین وي او په پوستکي کې په اسانۍ ښکاري.')])
    b.h('C) Capillaries', 'C) عروقِ شعریہ (Capillaries)', 'C) شعریه رګونه (Capillaries)')
    P(b, [('These blood vessels, because of being fine and thin, are not seen without a microscope. Through these capillaries the exchange of oxygen and food components takes place between the plasma of the blood and the tissues (Tissues), and from here the blood takes back every kind of waste substance and carbon dioxide from the cells and tissues.',
           'یہ خون کی نالیاں باریک اور پتلی ہونے کی وجہ سے خوردبین کے بغیر نظر نہیں آتی، ان عروقِ شعریہ کے ذریعے خون کی پلازما اور بافتوں (Tissues) کے درمیان آکسیجن اور غذائی اجزاء کا تبادلہ ہوتا ہے اور یہاں سے ہی خون خلیات اور بافتوں سے ہر قسم کے بے کار مادے اور کاربن ڈائی آکسائیڈ واپس لے لیتا ہے۔',
           'دا رګونه د نریوالي او نازکوالي له امله له مایکروسکوپ پرته نه ښکاري؛ د دې شعریه رګونو له لارې د وینې د پلازما او نسجونو (Tissues) ترمنځ د اکسیجن او غذايي اجزاوو تبادله کېږي او له همدې ځایه وینه له حجرو او نسجونو هر ډول بې‌ګټې مواد او کاربن ډای اکسایډ بېرته اخلي.')])
    shp = vessel_bed(40, 60, 360) + '<path d="M300 30 l40 -10 l-8 12" stroke="#dc2626" stroke-width="4" fill="none"/><path d="M120 30 l-40 -10" stroke="#1d4ed8" stroke-width="4" fill="none"/>'
    labs = lambda c: labelled(440, 200, shp, [('Artery', 400, 150, 'middle', 390, 70), ('Arteriole', 320, 165, 'middle', 310, 80), ('Capillaries', 220, 175, 'middle', 220, 100),
                                             ('Venule', 130, 165, 'middle', 120, 80), ('Vein', 45, 150, 'middle', 50, 70)], c)
    sv = [labs(c) for c in ('Artery, arteriole, capillaries, venule and vein', 'شریان، چھوٹی شریان، عروقِ شعریہ، چھوٹی ورید اور ورید', 'شریان، وړوکی شریان، شعریه رګونه، وړوکی ورید او ورید')]
    b.visual('hpe12-fig-capillary-bed', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 2, 5, 20)
    BOOK.save(20, [(2, r)], issues=[{'id': 'hpe12-pdf020', 'unit': 2, 'printedPage': 15,
               'description': 'The capillary-bed illustration is reproduced as a coded schematic with the printed labels. “شریانیں ہماری جسم … ہوتے ہیں”, “وریدیں … اوپر ہوتے ہیں”, “اُس کی ساخت”, “نظر نہیں آتی”. Retained as printed.'}])


def p21():
    b = Builder()
    b.h('3. Blood', '3. خون (Blood)', '3. وینه (Blood)')
    P(b, [('Blood is a red-coloured liquid substance which is present in the heart and blood vessels. Blood provides oxygen and other food components to all the cells of our body and takes waste substances and carbon dioxide from the cells and gives them to the excretory system. In a healthy man there are 5 to 6 litres of blood. Blood is a compound of two things: plasma and cells. Blood consists of 55 percent plasma and 45 percent cells. In the same way plasma has 90 percent water and 10 percent such soluble compounds as are necessary for delivering nutrition to the cells of the body and for performing functions. In blood the following kinds of cells are present.',
           'خون ایک سرخ رنگ کا سیال مادہ ہے جو کہ دل اور خون کی رگوں میں موجود ہوتا ہے۔ خون ہمارے تمام جسم کے خلیات کو آکسیجن اور دوسرے غذائی اجزاء فراہم کرتا ہے اور خلیات سے بے کار مادے اور کاربن ڈائی آکسائیڈ حاصل کر کے نظامِ اخراج کو دیتا ہے۔ ایک صحت مند آدمی میں 5 سے 6 لیٹر خون ہوتا ہے۔ خون دو چیزوں کا مرکب ہے پلازما اور خلیات۔ خون 55 فیصد پلازما اور 45 فیصد خلیات پر مشتمل ہوتا ہے۔ اسی طرح پھر پلازما میں 90 فیصد پانی اور 10 فیصد ایسے حل پذیر مرکبات ہوتے ہیں جو کہ جسم کے خلیوں کو غذائیت پہنچانے اور افعال کی انجام دہی کیلئے ضروری ہوتے ہیں۔ خون میں مندرجہ ذیل قسم کے خلیے موجود ہوتے ہیں۔',
           'وینه یوه سره مایع ماده ده چې په زړه او د وینې په رګونو کې وي. وینه زموږ د بدن ټولو حجرو ته اکسیجن او نور غذايي اجزا رسوي او له حجرو بې‌ګټې مواد او کاربن ډای اکسایډ اخلي او د اطراح سیستم ته یې ورکوي. په یوه روغ سړي کې له ۵ تر ۶ لیتره وینه وي. وینه د دوو شیانو مرکب دی: پلازما او حجرې. وینه له ۵۵ سلنه پلازما او ۴۵ سلنه حجرو جوړه وي. همداسې په پلازما کې ۹۰ سلنه اوبه او ۱۰ سلنه داسې حل کېدونکي مرکبات وي چې د بدن حجرو ته د تغذیې رسولو او دندو ترسره کولو لپاره اړین وي. په وینه کې لاندې ډوله حجرې وي.')])
    b.h('1. Red Blood Cells (R.B.C)', '1. خون کے سرخ خلیات Red Blood Cells (R.B.C)', '1. د وینې سرې حجرې Red Blood Cells (R.B.C)')
    P(b, [('The red cells of blood (Red blood cells) (R.B.C), which are called erythrocytes (Erythrocytes), are made in the marrow of bones (Bone Marrow). Their age is from 90 to 120 days. In the red cells of blood there is no nucleus; rather they are filled with haemoglobin (Haemoglobin), which is a compound of protein and iron, whose work is to deliver oxygen to the cells and tissues of the body and to bring back carbon dioxide from them. In one cubic millimetre of blood there are 50 to 60 lakh red cells.',
           'خون کے سرخ خلیات (Red blood cells) (R.B.C) جنہیں اریتھروسائٹس (Erythrocytes) کہتے ہیں یہ ہڈیوں کے گودے (Bone Marrow) میں بنتے ہیں۔ اس کی عمر 90 سے لے کر 120 دن تک ہوتی ہے۔ خون کے سرخ خلیات میں نیوکلیئس نہیں ہوتا بلکہ اُن میں ہیمو گلوبن (Haemoglobin) بھرا ہوتا ہے جو کہ پروٹین اور آئرن کا مرکب ہے جس کا کام جسم کے خلیات اور بافتوں کو آکسیجن پہنچانا اور اس سے کاربن ڈائی آکسائیڈ کو واپس لانا ہوتا ہے۔ خون کے ایک مکعب ملی میٹر میں 50 سے 60 لاکھ تک سرخ خلیات ہوتے ہیں۔',
           'د وینې سرې حجرې (Red blood cells) (R.B.C) چې اریتروسایټس (Erythrocytes) ورته ویل کېږي، د هډوکو په مغز (Bone Marrow) کې جوړېږي. عمر یې له ۹۰ تر ۱۲۰ ورځو وي. د وینې په سرو حجرو کې هسته نه وي، بلکې هیموګلوبین (Haemoglobin) پکې ډک وي چې د پروټین او اوسپنې مرکب دی او کار یې د بدن حجرو او نسجونو ته اکسیجن رسول او له هغو کاربن ډای اکسایډ بېرته راوړل دي. د وینې په یوه مکعب ملي متر کې له ۵۰ تر ۶۰ لکه سرې حجرې وي.')])
    b.h('2. White Blood Cells (W.B.C)', '2. خون کے سفید خلیے White Blood Cells (W.B.C)', '2. د وینې سپینې حجرې White Blood Cells (W.B.C)')
    P(b, [('The white cells of blood are called leukocytes (Leukocytes). These too are made in the marrow of bones and the spleen (spleen). In blood there are different kinds of leukocytes. These give our body the power of resistance …',
           'خون کے سفید خلیوں کو لیوکوسائٹس (Leukocytes) کہتے ہیں۔ یہ بھی ہڈیوں کے گودے اور تلی (spleen) میں بنتے ہیں۔ خون میں مختلف قسم کے لیوکوسائٹس ہوتے ہیں۔ یہ ہمارے جسم کو قوتِ مدافعت دیتا ہے …',
           'د وینې سپینو حجرو ته لیوکوسایټس (Leukocytes) ویل کېږي. دا هم د هډوکو په مغز او توري (spleen) کې جوړېږي. په وینه کې بېلابېل ډوله لیوکوسایټس وي. دا زموږ بدن ته د دفاع ځواک ورکوي …')])
    r = rec(b, 2, 6, 21)
    deco(r, 'A close-up photograph of red blood cells beside the RBC paragraph is decorative.')
    BOOK.save(21, [(2, r)], issues=[{'id': 'hpe12-pdf021', 'unit': 2, 'printedPage': 16,
               'description': 'Owner English ballpoint writing (“Red blood cells”, “living”, “beginning”) is excluded. “اس کی عمر”, “یہ ہمارے جسم کو قوتِ مدافعت دیتا ہے”. Retained as printed.'}])


def p22():
    b = Builder()
    P(b, [('… and protects from different kinds of diseases. In one cubic millimetre of blood there are from 4 thousand up to 11 thousand of these, and their age is from a few days to a few weeks.',
           'اور مختلف قسم کی بیماریوں سے حفاظت کا کام کرتا ہے۔ یہ خون کے ایک مکعب ملی میٹر میں 4 ہزار سے لے کر گیارہ 11 ہزار تک ہوتے ہیں اور ان کی عمر چند دن سے لیکر چند ہفتوں تک ہوتی ہے۔',
           '… او له بېلابېلو ناروغیو د ساتنې کار کوي. د وینې په یوه مکعب ملي متر کې له ۴ زرو تر یوولس ۱۱ زرو پورې وي او عمر یې له څو ورځو تر څو اونیو وي.')])
    cells = ''.join(f'<circle cx="{60 + i * 85}" cy="60" r="34" fill="{f}" stroke="#334155" stroke-width="1.5"/><ellipse cx="{60 + i * 85}" cy="60" rx="{rx}" ry="{ry}" fill="#312e81"/>'
                    for i, (f, rx, ry) in enumerate([('#ffffff', 12, 20), ('#fecdd3', 16, 12), ('#c7d2fe', 18, 16), ('#bfdbfe', 24, 20), ('#e0e7ff', 20, 20)]))
    sv = [labelled(440, 130, cells, [], c) for c in ('Different kinds of white blood cells', 'خون کے سفید خلیوں کی مختلف اقسام', 'د وینې د سپینو حجرو بېلابېل ډولونه')]
    b.visual('hpe12-fig-wbc', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('3. Blood Platelets', '3. پلیٹ لیٹس (Blood Platelets)', '3. پلېټلېټونه (Blood Platelets)')
    P(b, [('These are the third kind of cells of blood. Their number in one cubic millimetre of blood is from two and a half lakh to five lakh, and its important work is the clotting of blood (Blood clotting).',
           'یہ خون کی تیسری قسم کے خلیات ہیں۔ خون میں اس کی تعداد ایک مکعب ملی میٹر میں ڈھائی لاکھ سے لیکر پانچ لاکھ تک ہوتی ہے اور اس کا اہم کام خون کا انجماد (Blood clotting) ہے۔',
           'دا د وینې درېیم ډول حجرې دي. په وینه کې یې شمېر په یوه مکعب ملي متر کې له دوه نیم لکو تر پنځه لکو پورې وي او مهم کار یې د وینې پرنډېدل (Blood clotting) دي.')])
    b.h('Kinds of blood circulation', 'دورانِ خون کے اقسام', 'د وینې د جریان ډولونه')
    b.p('Blood circulates in the body in the following ways.', 'جسم میں خون درج ذیل طریقوں سے گردش کرتا ہے۔', 'په بدن کې وینه په لاندې لارو ګرځي.')
    b.h('1. Pulmonary Circulation', '1۔ پلمونری گردش (Pulmonary Circulation)', '1. د سږو ګرځښت (Pulmonary Circulation)')
    P(b, [('In this circulation, when impure blood reaches the right atrium, from here it comes through the tricuspid valve into the right ventricle. When the right ventricle contracts, this blood goes through the right and left arteries into the lungs. Through the very fine tubes of blood, the capillaries, in the air sacs (Alveoli) present in lakhs in the lungs, the blood takes carbon dioxide and oxygen mixes into the blood. After obtaining oxygen the blood, becoming pure, comes through the veins of the lungs into the left atrium of the heart. From the left atrium of the heart the pure blood comes down through the bicuspid valve into the left ventricle. Here this pure blood becomes ready to be supplied to the whole body. This circulation is called pulmonary circulation (Pulmonary Circulation).',
           'اس گردش میں جب غیر صاف شدہ خون دائیں اُذن میں پہنچتا ہے تو یہاں سے یہ ٹرائی کسپیڈ والو کے ذریعے دائیں بطن میں آ جاتا ہے۔ دایاں بطن جب سکڑتا ہے تو یہ خون دائیں بائیں شریانوں کے ذریعے پھیپھڑوں میں چلا جاتا ہے۔ پھیپھڑوں میں موجود لاکھوں کی تعداد میں ہوا کی تھیلیاں (Alveoli) خون کے باریک نالیوں کیپیلریز کے ذریعے سے کاربن ڈائی آکسائیڈ لے لیتی ہے اور آکسیجن خون میں شامل ہو جاتی ہے۔ خون آکسیجن حاصل کرنے کے بعد صاف ہو کر پھیپھڑوں کے وریدوں کے ذریعے دل کے بائیں اُذن میں آتا ہے۔ دل کے بائیں اُذن سے صاف خون بائی کسپیڈ والو کے ذریعے نیچے بائیں بطن میں آ جاتا ہے۔ یہاں یہ صاف خون تمام جسم کو سپلائی ہونے کیلئے تیار ہوتا ہے۔ اس گردش کو پلمونری گردش (Pulmonary Circulation) کہتے ہیں۔',
           'په دې ګرځښت کې کله چې ناپاکه وینه ښي اذین ته ورسېږي، له دې ځایه د ټرای کسپیډ والو له لارې ښي بطین ته راځي. کله چې ښی بطین سره راټولېږي، دا وینه د ښي او کیڼ شریانونو له لارې سږو ته ځي. په سږو کې په لکونو هوايي کڅوړې (Alveoli) د وینې د نریو رګونو، شعریه رګونو، له لارې کاربن ډای اکسایډ اخلي او اکسیجن په وینه کې ګډېږي. وینه له اکسیجن اخیستو وروسته پاکېږي او د سږو د وریدونو له لارې د زړه کیڼ اذین ته راځي. د زړه له کیڼ اذین پاکه وینه د بای کسپیډ والو له لارې ښکته کیڼ بطین ته راځي. دلته دا پاکه وینه ټول بدن ته د رسېدو لپاره چمتو وي. دې ګرځښت ته د سږو ګرځښت (Pulmonary Circulation) ویل کېږي.')])
    r = rec(b, 2, 7, 22)
    BOOK.save(22, [(2, r)], issues=[{'id': 'hpe12-pdf022', 'unit': 2, 'printedPage': 17,
               'description': 'The row of five white-blood-cell micrographs (unlabelled in print) is reproduced as a coded schematic. “ہوا کی تھیلیاں … لے لیتی ہے”, “پھیپھڑوں کے وریدوں”. Retained as printed.'}])


def p23():
    b = Builder()
    shp = lung_pair(220, 20, '#fca5a5', 1.15) + '<rect x="195" y="40" width="16" height="200" fill="#1d4ed8"/><rect x="232" y="40" width="16" height="200" fill="#dc2626"/><ellipse cx="225" cy="160" rx="34" ry="42" fill="#ef4444" stroke="#7f1d1d"/>'
    labs = lambda c: labelled(440, 290, shp, [('Superior vena cava', 70, 40, 'end', 195, 50), ('Aorta', 360, 40, 'start', 248, 45), ('Pulmonary artery', 80, 110, 'end', 170, 110),
                                             ('Right lung', 150, 160, 'middle', None, None), ('Left lung', 300, 160, 'middle', None, None), ('Pulmonary veins', 360, 120, 'start', 270, 125),
                                             ('Inferior vena cava', 80, 230, 'end', 200, 230), ('Heart', 360, 200, 'start', 255, 175)], c)
    sv = [labs(c) for c in ('Pulmonary circulation', 'پلمونری گردش (Pulmonary circulation)', 'د سږو ګرځښت (Pulmonary circulation)')]
    b.visual('hpe12-fig-pulmonary-circulation', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('2. Systemic Circulation', '2۔ سسٹیمک گردش (Systemic Circulation)', '2. سیسټمیک ګرځښت (Systemic Circulation)')
    P(b, [('The circulation of blood in the whole body is called systemic circulation (Systemic Circulation). In this circulation pure blood (Oxygenated blood) from the left ventricle of the heart, entering through the aorta (Aorta), goes towards all the organs of the body in small arteries. These same small arteries, becoming fine, change into capillaries (Capillaries), and then the blood through the capillaries gives the food components and oxygen present in it to the tissues and cells, and takes from them waste substances and carbon dioxide, and coming from small veins into large veins it comes through the large veins into the right atrium of the heart. Of these large veins, one is called the superior vena cava (Superior Vena cava) and the other the inferior vena cava (Inferior Vena cava) …',
           'خون کا سارے جسم میں گردش سسٹیمک گردش (Systemic Circulation) کہلاتا ہے۔ خون کے اس گردش میں صاف خون (Oxygenated blood) دل کے بائیں بطن سے اے اورٹا (Aorta) کے ذریعے داخل ہو کر چھوٹی چھوٹی شریانوں میں جسم کے تمام اعضاء کی جانب چلی جاتی ہے۔ یہی چھوٹی شریانیں باریک ہو کر عروقِ شعریہ یعنی (Capillaries) میں تبدیل ہو جاتی ہیں اور پھر خون کیپیلریز کے ذریعے اپنے اندر موجود غذائی اجزاء اور آکسیجن بافتوں اور خلیات کو دے دیتا ہے اور ان سے بے کار مادے اور کاربن ڈائی آکسائیڈ چھوٹے چھوٹے وریدوں میں آ کر بڑے وریدوں کے ذریعے دل کے دائیں اُذن میں آ جاتا ہے۔ اس بڑے وریدوں میں ایک کو بالائی وینا کیوا (Superior Vena cava) دوسرے کو زیریں وینا کیوا (Inferior Vena cava) …',
           'په ټول بدن کې د وینې ګرځښت ته سیسټمیک ګرځښت (Systemic Circulation) ویل کېږي. په دې ګرځښت کې پاکه وینه (Oxygenated blood) د زړه له کیڼ بطین د اورټا (Aorta) له لارې ننوځي او په وړو وړو شریانونو کې د بدن ټولو غړو ته ځي. همدا واړه شریانونه نري کېږي او په شعریه رګونو (Capillaries) اوړي او بیا وینه د شعریه رګونو له لارې خپل غذايي اجزا او اکسیجن نسجونو او حجرو ته ورکوي او له هغو بې‌ګټې مواد او کاربن ډای اکسایډ اخلي او له وړو وریدونو لویو وریدونو ته راځي او د لویو وریدونو له لارې د زړه ښي اذین ته راځي. له دې لویو وریدونو یو ته پورتنۍ وینا کاوا (Superior Vena cava) او بل ته ښکتنۍ وینا کاوا (Inferior Vena cava) …')])
    loop = ('<rect x="40" y="20" width="160" height="300" rx="40" fill="none" stroke="#1d4ed8" stroke-width="8"/><rect x="120" y="20" width="160" height="300" rx="40" fill="none" stroke="#dc2626" stroke-width="8"/>'
            '<ellipse cx="160" cy="60" rx="50" ry="30" fill="#93c5fd"/><ellipse cx="160" cy="170" rx="40" ry="50" fill="#f87171" stroke="#7f1d1d"/><circle cx="160" cy="265" r="14" fill="#fde68a" stroke="#92400e"/><rect x="148" y="280" width="24" height="40" fill="#fde68a" stroke="#92400e"/>')
    labs2 = lambda c: labelled(360, 360, loop, [('High Pressure', 10, 100, 'start', None, None), ('Low Pressure', 290, 80, 'start', None, None), ('Lowest Pressure', 10, 220, 'start', None, None),
                                               ('Highest Pressure', 290, 220, 'start', None, None), ('Pulmonary Arteries', 160, 30, 'middle', None, None), ('Aorta', 200, 130, 'start', None, None),
                                               ('Venae Cavae', 60, 150, 'start', None, None), ('Right Atrium', 140, 160, 'end', None, None), ('Left Atrium', 185, 160, 'start', None, None),
                                               ('Right Ventricle', 140, 200, 'end', None, None), ('Left Ventricle', 185, 200, 'start', None, None)], c)
    sv2 = [labs2(c) for c in ('Pulmonary and systemic circulation with pressures', 'پلمونری اور سسٹیمک گردش اور دباؤ', 'د سږو او سیسټمیک ګرځښت او فشارونه')]
    b.visual('hpe12-fig-double-circulation', sv2[0][0], sv2[1][0], sv2[2][0], sv2[0][1])
    r = rec(b, 2, 8, 23)
    BOOK.save(23, [(2, r)], issues=[{'id': 'hpe12-pdf023', 'unit': 2, 'printedPage': 18,
               'description': 'Both circulation diagrams are reproduced as coded schematics with their printed English labels. Owner ballpoint writing in the margins (“blood cells”, names, scribbles) is excluded. “خون کا سارے جسم میں گردش … کہلاتا ہے”, “اس بڑے وریدوں میں”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    {18: p18, 19: p19, 20: p20, 21: p21, 22: p22, 23: p23}[n]()
