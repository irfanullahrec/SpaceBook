"""PDF61 (printed114–115): standalone source record, no shared-file writes."""
import html
from class12_chemistry_opening import pair, section, SOURCE

paras, layout, blocks = [], [], []


def add(e, u, p, kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]})
    paras.append(pair(e,u,p))


add('CH₂Cl₂ + Cl₂ ⟶ CHCl₃ + HCl', 'CH₂Cl₂ + Cl₂ ⟶ CHCl₃ + HCl', 'CH₂Cl₂ + Cl₂ ⟶ CHCl₃ + HCl', 'equation')
add('chloroform (trichloromethane)', 'کلوروفارم (ٹرائی کلورومیتھین)', 'کلوروفارم (ټرای کلورومیتان)')
add('CHCl₃ + Cl₂ ⟶ CCl₄ + HCl', 'CHCl₃ + Cl₂ ⟶ CCl₄ + HCl', 'CHCl₃ + Cl₂ ⟶ CCl₄ + HCl', 'equation')
add('carbon tetrachloride (tetrachloromethane)', 'کاربن ٹیٹراکلورائیڈ (ٹیٹراکلورومیتھین)', 'کاربن ټېټراکلورایډ (ټېټراکلورومیتان)')
add('Thus, a mixture of all the four substitution products i.e. methyl chloride, methylene chloride, chloroform and carbon tetrachloride are obtained. The extent of their concentration in the mixture depends on the relative amounts of chlorine and methane. If chlorine is taken in excess, the reaction goes to the final substitution product and carbon tetrachloride is the major product. On the contrary, when chlorine is limited and methane is in excess, the major product of the reaction is methyl chloride.',
    'اس طرح تبادلے سے بننے والی چاروں مصنوعات، یعنی میتھائل کلورائیڈ، میتھیلین کلورائیڈ، کلوروفارم اور کاربن ٹیٹراکلورائیڈ کا آمیزہ حاصل ہوتا ہے۔ آمیزے میں ان کے ارتکاز کی مقدار کلورین اور میتھین کی نسبتی مقداروں پر منحصر ہوتی ہے۔ اگر کلورین زیادہ مقدار میں لی جائے تو تعامل تبادلے کی آخری مصنوع تک پہنچتا ہے اور کاربن ٹیٹراکلورائیڈ بڑی مقدار میں حاصل ہوتا ہے۔ اس کے برعکس، جب کلورین محدود اور میتھین زیادہ مقدار میں ہو تو تعامل کی بڑی مقدار میں حاصل ہونے والی مصنوع میتھائل کلورائیڈ ہوتی ہے۔',
    'په دې توګه د ځایناستي کېدو د ټولو څلورو محصولاتو، یعنې میتیل کلورایډ، میتیلین کلورایډ، کلوروفارم او کاربن ټېټراکلورایډ مخلوط ترلاسه کېږي. په مخلوط کې د هغوی د غلظت کچه د کلورین او میتان پر نسبي مقدارونو پورې تړلې ده. که کلورین په زیاته اندازه واخیستل شي، تعامل د ځایناستي کېدو تر وروستي محصوله رسېږي او کاربن ټېټراکلورایډ عمده محصول وي. برعکس، کله چې کلورین محدود او میتان په زیاته اندازه وي، د تعامل عمده محصول میتیل کلورایډ وي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Mechanism is the step-wise description of a chemical reaction.',
    'طریق کار کسی کیمیائی تعامل کی مرحلہ وار وضاحت ہے۔',
    'میکانیزم د یوه کیمیاوي تعامل پړاو په پړاو تشریح ده.')
add('16.4 Oxidation of Organic Compounds', '16.4 نامیاتی مرکبات کی تکسید', '16.4 د عضوي مرکباتو اکسیدېدل', 'heading')
add('Oxidation generally refers to the increase in oxidation state of an atom. Oxidation of organic compounds corresponds to an increase in the oxidation state of carbon. Oxidation of carbon occurs when a bond between carbon and an atom which is less electronegative than carbon is replaced by a bond to an atom that is more electronegative than carbon (in substitution reactions). Oxidation state of carbon increases with increase in the number of bonds between carbon and oxygen and decreases the number of carbon-hydrogen bonds, as shown in Table 16.4. We can extend the generalization that any element more electronegative than carbon will have the same effect on oxidation number as oxygen. Thus, the oxidation numbers of carbon in CH₃Cl and in CH₃OH are the same (−2).',
    'تکسید سے عموماً کسی ایٹم کی تکسیدی حالت میں اضافہ مراد ہوتا ہے۔ نامیاتی مرکبات کی تکسید کاربن کی تکسیدی حالت میں اضافے کے مطابق ہوتی ہے۔ کاربن کی تکسید اس وقت ہوتی ہے جب کاربن اور اس سے کم برقی منفی ایٹم کے درمیان بند کی جگہ ایسے ایٹم کے ساتھ بند بن جائے جو کاربن سے زیادہ برقی منفی ہو (تبادلے کے تعاملات میں)۔ کاربن اور آکسیجن کے درمیان بندوں کی تعداد بڑھنے اور کاربن–ہائیڈروجن بندوں کی تعداد گھٹنے سے کاربن کی تکسیدی حالت بڑھتی ہے، جیسا کہ جدول16.4 میں دکھایا گیا ہے۔ ہم اس عمومیت کو آگے بڑھا سکتے ہیں کہ کاربن سے زیادہ برقی منفی کوئی بھی عنصر تکسیدی عدد پر آکسیجن جیسا اثر ڈالے گا۔ لہٰذا CH₃Cl اور CH₃OH میں کاربن کے تکسیدی عدد ایک جیسے (−2) ہیں۔',
    'اکسیدېدل عموماً د یوه اټوم د اکسیدېشن حالت زیاتېدو ته ویل کېږي. د عضوي مرکباتو اکسیدېدل د کاربن د اکسیدېشن حالت له زیاتېدو سره سمون لري. کاربن هغه وخت اکسیدېږي چې د کاربن او تر هغه د لږ الکترومنفي اټوم ترمنځ تړون د کاربن او تر هغه د ډېر الکترومنفي اټوم په تړون بدل شي (د ځایناستي کېدو په تعاملونو کې). د کاربن او اکسیجن ترمنځ د تړونونو د شمېر په زیاتېدو او د کاربن–هایدروجن تړونونو د شمېر په کمېدو سره د کاربن د اکسیدېشن حالت لوړېږي، لکه په جدول16.4 کې چې ښودل شوي. موږ دا عمومي قاعده غځولای شو چې له کاربن څخه ډېر الکترومنفي هر عنصر به پر اکسیدېشن شمېر د اکسیجن په څېر اغېز ولري. نو په CH₃Cl او CH₃OH کې د کاربن د اکسیدېشن شمېر یو شان (−2) دی.')
add('Table 16.4 Oxidation Number of Carbon in One-Carbon Compounds',
    'جدول16.4 ایک کاربن والے مرکبات میں کاربن کا تکسیدی عدد',
    'جدول16.4 په یوه کاربن لرونکو مرکباتو کې د کاربن د اکسیدېشن شمېر')
rows=[['methane','CH₄','−4'],['methyl alcohol','CH₃OH','−2'],['formaldehyde','HCHO','0'],['formic acid','HCOOH','+2'],['carbon dioxide','CO₂','+4']]
blocks.append({'id':'chem12-table16-4','headers':['Compound','Formula','Oxidation state'],'rows':rows,
    'translations':[
        {'language':'اردو','headers':['مرکب','فارمولا','تکسیدی حالت'],'rows':[[name,*r[1:]] for name,r in zip(['میتھین','میتھائل الکوحل','فارملڈیہائیڈ','فارمک تیزاب','کاربن ڈائی آکسائیڈ'],rows)]},
        {'language':'پښتو','headers':['مرکب','فورمول','د اکسیدېشن حالت'],'rows':[[name,*r[1:]] for name,r in zip(['میتان','میتیل الکول','فارملډیهایډ','فارمیک اسید','کاربن ډای اکسایډ'],rows)]}]})
layout.append({'type':'sourceDataTable','tableId':'chem12-table16-4'})
add('Combustion of alkanes is an important reaction, which is also a type of oxidation reaction. Alkanes (and also other hydrocarbons), burn in air to produce carbon dioxide and water. The reaction is highly exothermic and large quantity of heat is evolved. The heat released on complete combustion of a substance is called its heat of combustion. For example,',
    'الکینز کا احتراق ایک اہم تعامل ہے جو تکسیدی تعامل کی بھی ایک قسم ہے۔ الکینز (اور دیگر ہائیڈروکاربن بھی) ہوا میں جل کر کاربن ڈائی آکسائیڈ اور پانی بناتے ہیں۔ یہ تعامل نہایت حرارت خارج کرنے والا ہے اور بہت زیادہ حرارت خارج ہوتی ہے۔ کسی مادے کے مکمل احتراق پر خارج ہونے والی حرارت اس کی حرارت احتراق کہلاتی ہے۔ مثلاً،',
    'د الکانونو سوځېدل یو مهم تعامل دی چې د اکسیدېشن د تعامل یو ډول هم دی. الکانونه (او نور هایدروکاربنونه هم) په هوا کې سوځي او کاربن ډای اکسایډ او اوبه جوړوي. دا تعامل ډېر تودوخه خارجوونکی دی او ډېره تودوخه خوشې کېږي. د یوه مادې د بشپړ سوځېدو پر مهال خوشې شوې تودوخه د هغې د سوځېدو تودوخه بلل کېږي. د بېلګې په توګه،')
add('CH₄ + 2O₂ ⟶ CO₂ + 2H₂O + 890.95 kJ/mol (ignition)',
    'CH₄ + 2O₂ ⟶ CO₂ + 2H₂O + 890.95 kJ/mol (آگ لگانا)',
    'CH₄ + 2O₂ ⟶ CO₂ + 2H₂O + 890.95 kJ/mol (بلول)', 'equation')
add('The reaction is of high significance, as it provides basis for their use as fuels to get heat and power. When there is an insufficient supply of oxygen, alkanes on combustion, form carbon monoxide and water or carbon soot and water.',
    'یہ تعامل بہت اہم ہے، کیونکہ یہ حرارت اور طاقت حاصل کرنے کے لیے انہیں ایندھن کے طور پر استعمال کرنے کی بنیاد فراہم کرتا ہے۔ جب آکسیجن کی فراہمی ناکافی ہو تو الکینز احتراق پر کاربن مونو آکسائیڈ اور پانی یا کاربن کی کالک اور پانی بناتے ہیں۔',
    'دا تعامل ډېر اهمیت لري، ځکه د تودوخې او ځواک د ترلاسه کولو لپاره د سون په توګه د هغوی د کارولو بنسټ برابروي. کله چې د اکسیجن رسونه ناکافي وي، الکانونه د سوځېدو پر مهال کاربن مونو اکسایډ او اوبه یا د کاربن دوده او اوبه جوړوي.')
add('2CH₄ + 3O₂ (limited) ⟶ 2CO + 4H₂O + heat (ignition)',
    '2CH₄ + 3O₂ (محدود) ⟶ 2CO + 4H₂O + حرارت (آگ لگانا)',
    '2CH₄ + 3O₂ (محدود) ⟶ 2CO + 4H₂O + تودوخه (بلول)', 'equation')
add('CH₄ + O₂ (very limited) ⟶ C + 2H₂O + heat (ignition)',
    'CH₄ + O₂ (بہت محدود) ⟶ C + 2H₂O + حرارت (آگ لگانا)',
    'CH₄ + O₂ (ډېر محدود) ⟶ C + 2H₂O + تودوخه (بلول)', 'equation')
add('Methane on heating at high pressure, with a regulated supply of oxygen and in the presence of a suitable catalyst, provides a variety of products like methyl alcohol etc. For example, when a mixture of methane and air is passed over copper catalyst at a temperature 250°C and pressure of 100 atm, as a result, by controlled oxidation process, methane is converted to methanol. Later on this methyl alcohol by controlled oxidation, can be further converted to formaldehyde.',
    'میتھین کو زیادہ دباؤ پر، آکسیجن کی منضبط فراہمی کے ساتھ اور مناسب عمل انگیز کی موجودگی میں گرم کرنے سے میتھائل الکوحل وغیرہ جیسی مختلف مصنوعات حاصل ہوتی ہیں۔ مثلاً جب میتھین اور ہوا کے آمیزے کو 250°C درجہ حرارت اور 100 atm دباؤ پر تانبے کے عمل انگیز کے اوپر سے گزارا جائے تو منضبط تکسید کے عمل کے نتیجے میں میتھین میتھانول میں تبدیل ہو جاتی ہے۔ بعد میں اس میتھائل الکوحل کو منضبط تکسید سے مزید فارملڈیہائیڈ میں تبدیل کیا جا سکتا ہے۔',
    'میتان په لوړ فشار کې، د اکسیجن له کنټرول شوې رسونې سره او د مناسب کتلېست په شتون کې د تودولو پر مهال د میتیل الکول او نورو په څېر بېلابېل محصولات ورکوي. د بېلګې په توګه، کله چې د میتان او هوا مخلوط په 250°C تودوخه او 100 atm فشار کې د مسو پر کتلېست تېر شي، د کنټرول شوي اکسیدېشن د پروسې په پایله کې میتان په میتانول بدلېږي. وروسته دا میتیل الکول د کنټرول شوي اکسیدېشن له لارې لا په فارملډیهایډ بدلېدای شي.')
add('2CH₄ + O₂ ⟶ 2CH₃OH (Cu/250°C/100 atm)',
    '2CH₄ + O₂ ⟶ 2CH₃OH (Cu/250°C/100 atm)',
    '2CH₄ + O₂ ⟶ 2CH₃OH (Cu/250°C/100 atm)', 'equation')
add('16.5 Alkenes','16.5 الکینز (دوہرے بند والے)','16.5 الکینونه','heading')
add('Alkenes are the unsaturated hydrocarbons which contain a carbon-carbon double bond. They can be represented by the general formula CₙH₂ₙ. They are also known as olefins; derived from Latin oleum meaning ‘oil’ and ficare meaning ‘to form’, because their lower members form oily derivatives on treatment with chlorine or bromine.',
    'الکینز غیر سیر شدہ ہائیڈروکاربن ہیں جن میں کاربن–کاربن دوہرا بند ہوتا ہے۔ انہیں عمومی فارمولے CₙH₂ₙ سے ظاہر کیا جا سکتا ہے۔ انہیں اولیفنز بھی کہتے ہیں؛ یہ نام لاطینی الفاظ oleum، یعنی ”تیل“ اور ficare، یعنی ”بنانا“ سے اخذ کیا گیا ہے، کیونکہ ان کے ابتدائی ارکان کلورین یا برومین کے ساتھ عمل کرنے پر تیل جیسے مشتقات بناتے ہیں۔',
    'الکینونه نامشبوع هایدروکاربنونه دي چې د کاربن–کاربن دوه ګونی تړون لري. هغوی په عمومي فورمول CₙH₂ₙ ښودل کېدای شي. هغوی د اولیفینونو په نوم هم پېژندل کېږي؛ دا نوم له لاتیني oleum څخه چې «تېل» معنا لري او ficare څخه چې «جوړول» معنا لري اخیستل شوی، ځکه د هغوی ټیټ غړي له کلورین یا برومین سره د تعامل پر مهال غوړ مشتقات جوړوي.')
add('16.5.1 Nomenclature','16.5.1 نام گذاری','16.5.1 نومول','heading')
add('There are two systems for naming alkenes i.e. Common and IUPAC system.',
    'الکینز کی نام گذاری کے دو نظام ہیں، یعنی عام نظام اور IUPAC نظام۔',
    'د الکینونو د نومولو دوه سیستمونه شته، یعنې عام سیستم او د IUPAC سیستم.')
add('(a) Common System','(a) عام نظام','(a) عام سیستم','heading')
add('The common names of fist four members are derived from those of the corresponding alkanes by replacing the ending “ane” with “–ylene”.',
    'پہلے چار ارکان کے عام نام متعلقہ الکینز کے ناموں کے آخر میں ”ane“ کی جگہ ”–ylene“ لگانے سے اخذ کیے جاتے ہیں۔',
    'د لومړیو څلورو غړو عام نومونه د اړوندو الکانونو له نومونو څخه د پای «ane» په «–ylene» بدلولو سره اخیستل کېږي.')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 120" role="img"><g font-family="Arial,sans-serif" font-size="23" fill="#17212b" text-anchor="middle"><text x="180" y="38">CH₂ = CH₂</text><text x="550" y="38">CH₃ – CH = CH₂</text><text x="180" y="82" font-size="20">ethylene</text><text x="550" y="82" font-size="20">propylene</text></g></svg>'
blocks.append({'id':'chem12-p115-common-alkene-names','svg':svg,'svgUrdu':svg.replace('>ethylene<','>ایتھیلین<').replace('>propylene<','>پروپیلین<'),'svgPashto':svg.replace('>ethylene<','>ایتیلین<').replace('>propylene<','>پروپیلین<')})
layout.append({'type':'visual','blockId':'chem12-p115-common-alkene-names'})

record=section('16.8','Oxidation of organic compounds and introduction to alkenes',
               'نامیاتی مرکبات کی تکسید اور الکینز کا تعارف',
               'د عضوي مرکباتو اکسیدېدل او د الکینونو پېژندنه',paras,layout,blocks,'114–115')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':61,'printedPages':[114,115]}]
record['sourceChapterNumber']=16
record['sourceContinuesOnPdfPage']=62
issues=[{'id':'chem12-p115-fist-typo','pdfPage':61,'printedPage':115,
         'description':'Printed Common System paragraph says “fist four members”. Retained in English; Urdu and Pashto translate the evident intended “first four members”.','status':'source_printed_typo_retained'}]

# BEFORE replacement, preserve later legacy content with carry=[{
# 'from':'16.8','to':'16.9','startsAt':'Greek letters, a, B, y'}].
# The preceding legacy list fragments V./i./ii. are OCR reading-order debris.
# This module intentionally does not call save() or change shared application data.
