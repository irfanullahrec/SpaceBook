"""PDF9 source transcription and aligned translations (printed 10–11)."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(text):add(text,text,text,'equation')
add('If chlorine is passed over silicon powder, in a heated tube, it reacts to produce a colourless liquid silicon tetrachloride.',
    'گرم نلکی میں سلیکان کے سفوف پر کلورین گزارنے سے تعامل ہوتا ہے اور بے رنگ مائع سلیکان ٹیٹرا کلورائیڈ بنتا ہے۔',
    'که په توده نل کې د سیلیکان پر پوډر کلورین تېر شي، تعامل کوي او بې رنګه مایع سیلیکان ټېټراکلورایډ جوړوي.')
eq('Si(s) + 2Cl₂(g) → SiCl₄(l)')
add('White phosphorus burns in chlorine to produce a mixture of two chlorides. Phosphorus trichloride (Phosphorus (III) chloride) and phosphorus pentachloride (phosphorus (V) chloride). Phosphorus trichloride is colourless fuming liquid and',
    'سفید فاسفورس کلورین میں جل کر دو کلورائیڈز کا آمیزہ بناتا ہے: فاسفورس ٹرائی کلورائیڈ (فاسفورس (III) کلورائیڈ) اور فاسفورس پینٹا کلورائیڈ (فاسفورس (V) کلورائیڈ)۔ فاسفورس ٹرائی کلورائیڈ بے رنگ، دھواں چھوڑنے والا مائع ہے اور',
    'سپین فاسفورس په کلورین کې سوځي او د دوو کلورایډونو مخلوط جوړوي: فاسفورس ټرای کلورایډ (فاسفورس (III) کلورایډ) او فاسفورس پنتا کلورایډ (فاسفورس (V) کلورایډ). فاسفورس ټرای کلورایډ بې رنګه، لوګی ورکوونکی مایع دی او')
eq('P₄(s) + 6Cl₂(g) → 4PCl₃(l)')
add('phosphorus pentachloride is a straw-coloured solid.', 'فاسفورس پینٹا کلورائیڈ بھوسے کے رنگ کا ٹھوس مادہ ہے۔','فاسفورس پنتا کلورایډ د بوسو رنګه جامد دی.')
eq('P₄(s) + 10Cl₂(g) → 4PCl₅(s)')
add('If a stream of chlorine is passed over some heated sulphur, it reacts to form an orange, foul smelling liquid disulphur dichloride (S₂Cl₂).',
    'گرم سلفر پر کلورین کا بہاؤ گزارنے سے تعامل ہوتا ہے اور نارنجی، بدبودار مائع ڈائی سلفر ڈائی کلورائیڈ (S₂Cl₂) بنتا ہے۔',
    'که پر تود شوي سلفر د کلورین جریان تېر شي، تعامل کوي او نارنجي، بدبویه مایع ډای سلفر ډای کلورایډ (S₂Cl₂) جوړوي.')
eq('2S(s) + Cl₂(g) → S₂Cl₂(l)')
head('Society, Technology And Science','معاشرہ، ٹیکنالوجی اور سائنس','ټولنه، ټکنالوژي او ساینس')
add('Body need a certain amount of iodine in order to make a chemical known as thyroid hormone. Thyroid hormone controls body metabolism and other important functions in the body.',
    'تھائرائیڈ ہارمون نامی کیمیائی مادہ بنانے کے لیے جسم کو آیوڈین کی ایک خاص مقدار درکار ہوتی ہے۔ تھائرائیڈ ہارمون جسم کے تحول اور دوسرے اہم افعال کو کنٹرول کرتا ہے۔',
    'بدن د تایرایډ هورمون په نوم کیمیاوي مادې د جوړولو لپاره یوه ټاکلې اندازه ایوډین ته اړتیا لري. د تایرایډ هورمون د بدن میتابولیزم او نور مهم فعالیتونه کنټرولوي.')
add('Iodine is found primarily in seawater and in the soil especially in coastal areas. At high elevations, iodine is often deficient in the water and soil. Lack of iodine can cause an abnormal enlargement of the thyroid gland, known as a goitre.',
    'آیوڈین بنیادی طور پر سمندری پانی اور مٹی، خصوصاً ساحلی علاقوں میں پائی جاتی ہے۔ بلند علاقوں کے پانی اور مٹی میں اکثر آیوڈین کی کمی ہوتی ہے۔ آیوڈین کی کمی سے تھائرائیڈ غدود غیر معمولی طور پر بڑھ سکتا ہے، جسے گلہڑ کہتے ہیں۔',
    'ایوډین تر ډېره په سمندري اوبو او خاوره کې، په ځانګړي ډول په ساحلي سیمو کې، موندل کېږي. په لوړو سیمو کې په اوبو او خاوره کې ډېری وخت ایوډین کم وي. د ایوډین کمښت د تایرایډ غدې د غیرعادي غټېدو لامل کېدای شي، چې جاغور بلل کېږي.')
add('A goitre is an abnormal enlargement of thyroid gland. Thyroid is a butterfly-shaped gland located at the base of neck. The most common cause of goitres worldwide is a lack of iodine in the diet. Iodine deficiency may be made worse by a diet high in hormone-inhibiting foods, such as cabbage, broccoli and cauliflower.',
    'گلہڑ تھائرائیڈ غدود کا غیر معمولی بڑھنا ہے۔ تھائرائیڈ تتلی نما غدود ہے جو گردن کی جڑ میں ہوتا ہے۔ دنیا بھر میں گلہڑ کی سب سے عام وجہ غذا میں آیوڈین کی کمی ہے۔ بند گوبھی، بروکلی اور پھول گوبھی جیسی ہارمون کو روکنے والی غذاؤں کی زیادہ مقدار آیوڈین کی کمی کو مزید خراب کر سکتی ہے۔',
    'جاغور د تایرایډ غدې غیرعادي غټېدل دي. تایرایډ د پروانې په شکل غده ده چې د غاړې په بېخ کې موقعیت لري. په نړۍ کې د جاغور تر ټولو عام لامل په غذا کې د ایوډین کمښت دی. د هورمون مخنیوونکو خوړو، لکه کرم، بروکلي او ګلپي، ډېر لرونکی خوراک د ایوډین کمښت لا خرابولای شي.')
add('Our body does not naturally make iodine, so the only way to get this nutrient is through diet. Adults typically require 150μg per day. Pregnant and breastfeeding women need 200μg per day.',
    'ہمارا جسم قدرتی طور پر آیوڈین نہیں بناتا، اس لیے یہ غذائی جز صرف خوراک سے حاصل ہوتا ہے۔ بالغوں کو عموماً روزانہ 150μg درکار ہوتی ہے۔ حاملہ اور دودھ پلانے والی خواتین کو روزانہ 200μg درکار ہوتی ہے۔',
    'زموږ بدن په طبیعي ډول ایوډین نه جوړوي، نو دا غذایي ماده یوازې له خوراکه ترلاسه کېږي. لویان عموماً په ورځ کې 150μg ته اړتیا لري. امیندواره او شیدې ورکوونکې ښځې په ورځ کې 200μg ته اړتیا لري.')
head('13.1.3 Physical Properties of the Oxides','13.1.3 آکسائیڈز کی طبعی خصوصیات','13.1.3 د اکسایډونو فزیکي ځانګړنې')
add('The oxides of period 3ʳᵈ elements are following.','تیسرے دور کے عناصر کے آکسائیڈز درج ذیل ہیں۔','د درېیمې دورې د عناصرو اکسایډونه په لاندې ډول دي.')
t={'id':'chem12-p10-oxide-list','noHeader':True,'headers':[],'rows':[['Na₂O','MgO','Al₂O₃','SiO₂','P₄O₁₀','SO₃','Cl₂O₇'],['-','-','-','-','P₄O₆','SO₂','Cl₂O']],
   'translations':[]}
t['translations']=[{'language':lang,'headers':[],'rows':t['rows']} for lang in ['اردو','پښتو']];blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
add('The oxides in the top row are the oxides where period 3 elements are in their highest oxidation state. In these oxides, all the outer electrons in period 3 elements are being involved in bonding from just one in sodium to all seven outer electrons of chlorine in Cl₂O₇.',
    'اوپر کی قطار کے آکسائیڈز میں تیسرے دور کے عناصر اپنی سب سے بلند تکسیدی حالت میں ہیں۔ ان میں عناصر کے تمام بیرونی الیکٹران بند بنانے میں شامل ہیں: سوڈیم کے صرف ایک الیکٹران سے لے کر Cl₂O₇ میں کلورین کے ساتوں بیرونی الیکٹرانوں تک۔',
    'په پاسني کتار کې هغه اکسایډونه دي چې د درېیمې دورې عناصر پکې په خپل تر ټولو لوړ اکسیدېشن حالت کې دي. په دې اکسایډونو کې د عناصرو ټول بهرني الکترونونه په تړون کې برخه اخلي؛ د سوډیم له یوازې یوه الکترون څخه تر په Cl₂O₇ کې د کلورین ټولو اوو بهرنیو الکترونونو پورې.')
add('The oxides (high oxidation state) of sodium, magnesium, aluminium, silicon, phosphorous are in solid state and those of sulphur and chlorine are in liquid state. The oxides having low oxidation state of sulphur and chlorine are in gaseous state.',
    'سوڈیم، میگنیشیم، ایلومینیم، سلیکان اور فاسفورس کے بلند تکسیدی حالت والے آکسائیڈز ٹھوس ہیں، جبکہ سلفر اور کلورین کے آکسائیڈز مائع ہیں۔ سلفر اور کلورین کے کم تکسیدی حالت والے آکسائیڈز گیس حالت میں ہیں۔',
    'د سوډیم، مګنیزیم، المونیم، سیلیکان او فاسفورس د لوړ اکسیدېشن حالت اکسایډونه جامد دي، او د سلفر او کلورین اکسایډونه مایع دي. د سلفر او کلورین د ټیټ اکسیدېشن حالت اکسایډونه ګازي دي.')
head('13.1.3.1 Structure','13.1.3.1 ساخت','13.1.3.1 جوړښت')
add('Sodium, magnesium and aluminium oxides consist of giant structures containing metal ions and oxide ions. Magnesium oxide is similar in structure to sodium chloride. The crystalline aluminium oxide is known as corundum, in which oxygen ions form nearly hexagonal close-packed structure with the aluminium ions.',
    'سوڈیم، میگنیشیم اور ایلومینیم کے آکسائیڈز بڑی ساختوں پر مشتمل ہیں، جن میں دھاتی اور آکسائیڈ آئن ہوتے ہیں۔ میگنیشیم آکسائیڈ کی ساخت سوڈیم کلورائیڈ جیسی ہے۔ قلمی ایلومینیم آکسائیڈ کورنڈم کہلاتی ہے، جس میں آکسیجن کے آئن ایلومینیم آئنوں کے ساتھ تقریباً مسدسی قریب قریب بھری ہوئی ساخت بناتے ہیں۔',
    'د سوډیم، مګنیزیم او المونیم اکسایډونه لوی جوړښتونه لري چې فلزي او اکسایډ ایونونه پکې دي. د مګنیزیم اکسایډ جوړښت د سوډیم کلورایډ په څېر دی. بلوري المونیم اکسایډ کورنډم بلل کېږي؛ پکې د اکسیجن ایونونه له المونیم ایونونو سره نږدې شپږګوټیز متراکم جوړښت جوړوي.')
head('Tidbit','مختصر معلومات','لنډ معلومات')
add('Corundum, naturally occurring aluminum oxide mineral (Al₂O₃) that is, after diamond, the hardest known natural substance.',
    'کورنڈم قدرتی طور پر پائی جانے والی ایلومینیم آکسائیڈ کی معدنی شکل (Al₂O₃) ہے، جو ہیرے کے بعد سب سے سخت معلوم قدرتی مادہ ہے۔',
    'کورنډم د المونیم اکسایډ طبیعي منرال (Al₂O₃) دی، چې له الماس وروسته تر ټولو سخت پېژندل شوی طبیعي ماده ده.')
add('Silicon dioxide is covalent oxide having giant structure. There are three different crystal forms of silicon dioxide; the most suitable structure is similar to that of diamond.',
    'سلیکان ڈائی آکسائیڈ بڑی ساخت والا اشتراکی آکسائیڈ ہے۔ اس کی تین مختلف قلمی شکلیں ہیں؛ سب سے موزوں ساخت ہیرے کی ساخت جیسی ہے۔',
    'سیلیکان ډای اکسایډ لوی جوړښت لرونکی کووالنټ اکسایډ دی. د سیلیکان ډای اکسایډ درې بېلابېلې بلوري بڼې شته؛ تر ټولو مناسبه جوړښت یې د الماس په څېر دی.')
add('Phosphorus, sulphur and chlorine form molecular oxides. Some of these molecules are simple, while others are polymeric. Thus, the trend in structure in period is',
    'فاسفورس، سلفر اور کلورین سالماتی آکسائیڈز بناتے ہیں۔ کچھ سالمے سادہ اور دوسرے کثیر سالماتی ہوتے ہیں۔ چنانچہ دور میں ساخت کا رجحان یہ ہے:',
    'فاسفورس، سلفر او کلورین مالیکولي اکسایډونه جوړوي. ځینې مالیکولونه ساده او نور پولیمري دي. نو په دوره کې د جوړښت تمایل دا دی:')
add('Giant metallic ionic oxides → giant covalent oxide → molecular oxide.',
    'بڑے دھاتی آئنک آکسائیڈز ← بڑا اشتراکی آکسائیڈ ← سالماتی آکسائیڈ۔',
    'لوی فلزي ایوني اکسایډونه ← لوی کووالنټ اکسایډ ← مالیکولي اکسایډ.')
head('13.1.3.2 Melting and Boiling Points','13.1.3.2 پگھلنے اور ابلنے کے درجے','13.1.3.2 د وېلې کېدو او اېشېدو ټکي')
add('The giant structures (the metal oxides and silicon dioxide) have high melting points and boiling points because a lot of energy is needed to break the strong bonds (ionic or covalent) operating in their lattices. The oxides of phosphorus, sulphur and chlorine consist of individual molecules, some small and simple, others polymeric.',
    'بڑی ساختوں (دھاتی آکسائیڈز اور سلیکان ڈائی آکسائیڈ) کے پگھلنے اور ابلنے کے درجے زیادہ ہیں، کیونکہ ان کی جالیوں کے مضبوط آئنک یا اشتراکی بند توڑنے کے لیے بہت توانائی درکار ہوتی ہے۔ فاسفورس، سلفر اور کلورین کے آکسائیڈز الگ الگ سالموں پر مشتمل ہیں؛ کچھ چھوٹے اور سادہ، دوسرے کثیر سالماتی ہیں۔',
    'لوی جوړښتونه (فلزي اکسایډونه او سیلیکان ډای اکسایډ) د وېلې کېدو او اېشېدو لوړ ټکي لري، ځکه د هغوی په جالیو کې د پیاوړو ایوني یا کووالنټ تړونونو د ماتولو لپاره ډېره انرژي اړینه ده. د فاسفورس، سلفر او کلورین اکسایډونه له جلا مالیکولونو جوړ دي؛ ځینې کوچني او ساده او نور پولیمري دي.')
add('The attractive forces between these molecules will be dispersion forces and dipole-dipole interactions. The strength of the attractive forces depend on the size, shape and polarity of various molecules but are always much weaker than the ionic or covalent bonds present in a giant structure. These oxides are gases, liquids or low – melting solids.',
    'ان سالموں کے درمیان کششی قوتیں انتشار کی قوتیں اور دو قطبی تعاملات ہوتی ہیں۔ ان کی طاقت مختلف سالموں کی جسامت، شکل اور قطبیت پر منحصر ہے، مگر بڑی ساخت کے آئنک یا اشتراکی بندوں سے ہمیشہ بہت کمزور ہوتی ہے۔ یہ آکسائیڈز گیسیں، مائعات یا کم نقطۂ پگھلاؤ والے ٹھوس مادے ہیں۔',
    'د دې مالیکولونو ترمنځ کششي قوې د خپرېدنې قوې او دوه قطبي تعاملونه دي. د کششي قوو پیاوړتیا د بېلابېلو مالیکولونو په اندازه، شکل او قطبیت پورې اړه لري، خو تل په لوی جوړښت کې له ایوني یا کووالنټ تړونونو ډېره کمزورې وي. دا اکسایډونه ګازونه، مایعات یا د ټیټ وېلې کېدو ټکي لرونکي جامدونه دي.')
add('Table 13.8 Melting and Boiling Points of Period 3ʳᵈ Oxides','جدول 13.8 تیسرے دور کے آکسائیڈز کے پگھلنے اور ابلنے کے درجے','جدول 13.8 د درېیمې دورې د اکسایډونو د وېلې کېدو او اېشېدو ټکي')
headers=['Oxides of period 3ʳᵈ','Na₂O','MgO','Al₂O₃','SiO₂','P₄O₁₀','SO₃','Cl₂O₇'];m=['1280','2900','2040','1610','340','−17','−92'];b=['1950','3600','2977','2230','360','45','82']
t={'id':'chem12-table-13-8','headers':headers,'rows':[['Melting point (°C)']+m,['Boiling point (°C)']+b],
   'translations':[{'language':'اردو','headers':['تیسرے دور کے آکسائیڈز']+headers[1:],'rows':[['نقطۂ پگھلاؤ (°C)']+m,['نقطۂ ابال (°C)']+b]},
                   {'language':'پښتو','headers':['د درېیمې دورې اکسایډونه']+headers[1:],'rows':[['د وېلې کېدو ټکی (°C)']+m,['د اېشېدو ټکی (°C)']+b]}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
head('13.1.3.3 Electrical Conductivity','13.1.3.3 برقی موصلیت','13.1.3.3 برېښنا لېږدونه')
add('None of the period 3ʳᵈ oxides have any free or mobile electrons. It means that none of them will conduct electricity when they are in solid state. The ionic oxides can, however, conduct electricity in molten state because of the movement of ions towards the opposite electrodes.',
    'تیسرے دور کے کسی آکسائیڈ میں آزاد یا متحرک الیکٹران نہیں ہیں۔ اس لیے ٹھوس حالت میں ان میں سے کوئی بجلی نہیں گزارے گا۔ تاہم آئنک آکسائیڈز پگھلی حالت میں مخالف الیکٹروڈز کی طرف آئنوں کی حرکت کی وجہ سے بجلی گزار سکتے ہیں۔',
    'د درېیمې دورې هېڅ اکسایډ ازاد یا خوځنده الکترونونه نه لري. نو په جامد حالت کې هېڅ یو برېښنا نه لېږدوي. خو ایوني اکسایډونه په وېلې حالت کې د مخالفو الکټروډونو پر لور د ایونونو د حرکت له امله برېښنا لېږدولای شي.')
head('13.1.4 Acid-Base Behaviour of the Oxides','13.1.4 آکسائیڈز کا تیزابی و اساسی رویہ','13.1.4 د اکسایډونو تېزابي او قلوي چلند')
add('Going across period 3, from left to right the nature of the oxides changes from basic (Na₂O,MgO) to amphoteric (Al₂O₃) and then to acidic (SiO₂,P₄O₆/P₄O₁₀,SO₂/SO₃). The acidity of the oxides increases across the period.',
    'تیسرے دور میں بائیں سے دائیں جانے پر آکسائیڈز کی نوعیت اساسی (Na₂O، MgO) سے دو خصوصیتی (Al₂O₃) اور پھر تیزابی (SiO₂، P₄O₆/P₄O₁₀، SO₂/SO₃) ہو جاتی ہے۔ دور میں آکسائیڈز کی تیزابیت بڑھتی ہے۔',
    'په درېیمه دوره کې له کیڼ څخه ښي لوري ته د اکسایډونو ماهیت له قلوي (Na₂O، MgO) څخه امفوتېریک (Al₂O₃) او بیا تېزابي (SiO₂، P₄O₆/P₄O₁₀، SO₂/SO₃) ته بدلېږي. په دوره کې د اکسایډونو تېزابیت زیاتېږي.')
record=section('13.5','Chlorides and physical properties of oxides','کلورائیڈز اور آکسائیڈز کی طبعی خصوصیات','کلورایډونه او د اکسایډونو فزیکي ځانګړنې',paras,layout,blocks,'10–11')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':9,'printedPages':[10,11]}]
if __name__=='__main__':save(9,[record],carry=[{'from':'13.5','to':'13.6','startsAt':'13.1.4.1 Trend in Acid Base Behaviour'}])
