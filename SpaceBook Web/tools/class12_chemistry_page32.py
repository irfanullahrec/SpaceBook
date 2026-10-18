"""PDF32 printed56–57: ligands, sphere, chelates and naming rules1–3."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_coordination_diagrams import block
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
def eq(v):add(v,v,v,'equation')
def visual(identity,kind):
    b=block(identity,kind);blocks.append(b);layout.append({'type':'visual','blockId':identity})
head('3. Ligand','3. لیگنڈ','3. لېګنډ')
add('The atoms, ions, or neutral molecules, which surrounds the central metal ion and donate electron pairs to it, are called ligands. They may be anions or neutral molecules. For example, K₄[Fe(CN)₆], [Ag(NH₃)₂]Cl. In these examples, the CN⁻ is anionic and NH₃ is the neutral ligand.',
    'مرکزی دھاتی آئن کے گرد موجود ایٹم، آئن یا بے بار سالمے جو اسے الیکٹرون جوڑے دیتے ہیں، لیگنڈز کہلاتے ہیں۔ یہ منفی آئن یا بے بار سالمے ہو سکتے ہیں۔ مثلاً K₄[Fe(CN)₆] اور [Ag(NH₃)₂]Cl میں CN⁻ منفی آئن اور NH₃ بے بار لیگنڈ ہے۔',
    'هغه اټومونه، ایونونه یا خنثی مالیکولونه چې د مرکزي فلزي ایون شاوخوا وي او هغه ته د الکترونونو جوړې ورکوي، لېګنډونه بلل کېږي. هغوی منفي ایونونه یا خنثی مالیکولونه کېدای شي. د بېلګې په توګه په K₄[Fe(CN)₆] او [Ag(NH₃)₂]Cl کې CN⁻ منفي ایون او NH₃ خنثی لېګنډ دی.')
add('Depending upon the number of donor atoms (or site), the ligands may be classified into various categories as follows.',
    'عطیہ دینے والے ایٹموں یا مقامات کی تعداد کے مطابق لیگنڈز کی درج ذیل قسمیں ہو سکتی ہیں۔',
    'د ورکوونکو اټومونو یا ځایونو د شمېر له مخې لېګنډونه په لاندې بېلابېلو ډلو وېشل کېدای شي.')
head('i. Monodentate or Unidentate Ligands','i. یک دندانی لیگنڈز','i. یو غاښیز لېګنډونه')
add('The ligands which possess only one donor site are called monodentate or unidentate ligands. Some examples are CN⁻, F⁻, Cl⁻, OH⁻, CO, NH₃, H₂O etc.',
    'صرف ایک عطیہ دینے والے مقام رکھنے والے لیگنڈز یک دندانی لیگنڈز کہلاتے ہیں۔ بعض مثالیں CN⁻، F⁻، Cl⁻، OH⁻، CO، NH₃ اور H₂O وغیرہ ہیں۔',
    'هغه لېګنډونه چې یوازې یو ورکوونکی ځای لري، مونودېنټېټ یا یونیډېنټېټ، یعنې یو غاښیز لېګنډونه بلل کېږي. ځینې بېلګې یې CN⁻، F⁻، Cl⁻، OH⁻، CO، NH₃ او H₂O او نور دي.')
head('ii. Multidentate or Polydentate Ligands','ii. کثیر دندانی لیگنڈز','ii. څو غاښیز لېګنډونه')
add('The ligands, which possess more than one donor sites are called multidentate, or polydentate ligands. Depending on the number of coordinating donor atoms, these are called bidentate (two), tridentate (three), tetradentate (four), pentadentate(five) and hexadentate (six) ligands. For example, ethylene diamine tetra acetic acid EDTA is an important hexadentate ligand.',
    'ایک سے زیادہ عطیہ دینے والے مقامات رکھنے والے لیگنڈز کثیر دندانی لیگنڈز کہلاتے ہیں۔ تناسقی عطیہ دینے والے ایٹموں کی تعداد کے مطابق یہ دو دندانی (دو)، سہ دندانی (تین)، چہار دندانی (چار)، پنج دندانی (پانچ) اور شش دندانی (چھ) ہیں۔ مثلاً ایتھلین ڈائی امین ٹیٹرا ایسیٹک تیزاب EDTA اہم شش دندانی لیگنڈ ہے۔',
    'له یوه څخه د ډېرو ورکوونکو ځایونو لرونکي لېګنډونه ملټيډېنټېټ یا پولیډېنټېټ، یعنې څو غاښیز لېګنډونه بلل کېږي. د کواردینېشن د ورکوونکو اټومونو له شمېر سره سم دوه غاښیز (دوه)، درې غاښیز (درې)، څلور غاښیز (څلور)، پنځه غاښیز (پنځه) او شپږ غاښیز (شپږ) بلل کېږي. د بېلګې په توګه اېتیلین ډای امین ټېټرا اسېټیک تېزاب EDTA یو مهم شپږ غاښیز لېګنډ دی.')
head('4. Coordination Number','4. تناسقی عدد','4. د کواردینېشن شمېر')
add('It refers to the total number of coordinate covalent bonds formed by the central metal ion with the ligands. For example, in [CoCl₂(NH₃)₄]Cl, [Cu(NH₃)₆]Cl₂, K₃[Cr(C₂O₄)₃] and K₄[Fe(CN)₆], six coordinate covalent bonds are formed between the ligands and the central metal ion and the coordination number is six, while in [Cu(NH₃)₄]SO₄, four coordinate covalent bonds are in between the ligand NH₃ and the central metal ion and the coordination number is four.',
    'یہ مرکزی دھاتی آئن اور لیگنڈز کے درمیان بننے والے تناسقی اشتراکی بندوں کی کل تعداد ہے۔ مثلاً [CoCl₂(NH₃)₄]Cl، [Cu(NH₃)₆]Cl₂، K₃[Cr(C₂O₄)₃] اور K₄[Fe(CN)₆] میں چھ تناسقی اشتراکی بند بنتے ہیں اور تناسقی عدد چھ ہے۔ جبکہ [Cu(NH₃)₄]SO₄ میں NH₃ لیگنڈ اور مرکزی دھاتی آئن کے درمیان چار بند ہیں اور تناسقی عدد چار ہے۔',
    'دا د مرکزي فلزي ایون او لېګنډونو ترمنځ د جوړو شوو کواردینېټ کووالنټ تړونونو ټول شمېر دی. د بېلګې په توګه په [CoCl₂(NH₃)₄]Cl، [Cu(NH₃)₆]Cl₂، K₃[Cr(C₂O₄)₃] او K₄[Fe(CN)₆] کې شپږ تړونونه جوړېږي او د کواردینېشن شمېر شپږ دی. خو په [Cu(NH₃)₄]SO₄ کې د NH₃ لېګنډ او مرکزي فلزي ایون ترمنځ څلور تړونونه دي او د کواردینېشن شمېر څلور دی.')
head('5. Coordination Sphere','5. تناسقی کرہ','5. د کواردینېشن ساحه')
add('The central atom along with the surrounding ligands are enclosed in a square bracket and forms coordination sphere. It may be anionic, cationic or neutral. For example, K₄[Fe(CN)₆], [Cu(NH₃)₄]SO₄ and [Ni(CO)₄]. In these examples, [Fe(CN)₆]⁴⁻, [Cu(NH₃)₄]²⁺, and [Ni(CO)₄]⁰ are an ionic, cationic and neutral coordination sphere respectively and K⁺ and SO₄²⁻ are the ionization sphere.',
    'مرکزی ایٹم اور اردگرد لیگنڈز مربع بریکٹ میں بند ہو کر تناسقی کرہ بناتے ہیں۔ یہ منفی، مثبت یا بے بار ہو سکتا ہے۔ مثلاً K₄[Fe(CN)₆]، [Cu(NH₃)₄]SO₄ اور [Ni(CO)₄] میں بالترتیب [Fe(CN)₆]⁴⁻، [Cu(NH₃)₄]²⁺ اور [Ni(CO)₄]⁰ منفی، مثبت اور بے بار تناسقی کرے ہیں، اور K⁺ اور SO₄²⁻ آئنائزیشن کرہ ہیں۔',
    'مرکزي اټوم له شاوخوا لېګنډونو سره په مربع قوسونو کې راځي او د کواردینېشن ساحه جوړوي. دا منفي، مثبت یا خنثی کېدای شي. د بېلګې په توګه په K₄[Fe(CN)₆]، [Cu(NH₃)₄]SO₄ او [Ni(CO)₄] کې په ترتیب سره [Fe(CN)₆]⁴⁻، [Cu(NH₃)₄]²⁺ او [Ni(CO)₄]⁰ منفي، مثبت او خنثی ساحې دي، او K⁺ او SO₄²⁻ د ایون کېدو ساحه ده.')
visual('chem12-figure-14-2','sphere')
add('Figure 14.2 Coordination sphere.','شکل 14.2 تناسقی کرہ۔','شکل 14.2 د کواردینېشن ساحه.')
add('The part present outside the bracket is called ionization sphere as it is ionisable in solution.',
    'بریکٹ کے باہر کا حصہ آئنائزیشن کرہ ہے، کیونکہ یہ محلول میں آئنائز ہو سکتا ہے۔',
    'له قوس څخه بهر برخه د ایون کېدو ساحه بلل کېږي، ځکه په محلول کې ایوني کېدای شي.')
head('6. Charge on the Coordination Sphere','6. تناسقی کرے پر بار','6. د کواردینېشن پر ساحه چارج')
add('It is the algebraic sum of the charges present on the central metal ion and the total charge on the ligands. For example, [Fe(CN)₆]⁴⁻',
    'یہ مرکزی دھاتی آئن کے بار اور لیگنڈز کے کل بار کا الجبری مجموعہ ہے۔ مثلاً [Fe(CN)₆]⁴⁻',
    'دا د مرکزي فلزي ایون د چارج او د لېګنډونو د ټول چارج الجبري مجموعه ده. د بېلګې په توګه [Fe(CN)₆]⁴⁻')
add('Charge on iron, Fe = +2','لوہے Fe پر بار = +2','پر اوسپنه Fe چارج = +2')
add('Total charge on six CN⁻ ions = −6','چھ CN⁻ آئنوں کا کل بار = −6','د شپږو CN⁻ ایونونو ټول چارج = −6')
add('Charge on the Coordination Sphere = −6 + 2 = −4','تناسقی کرے پر بار = −6 + 2 = −4','د کواردینېشن پر ساحه چارج = −6 + 2 = −4')
head('7. Chelates','7. کیلیٹس','7. کېلېټونه')
add('The bonding of a polydentate ligand to a metal ion through more than one site is called chelating ligand. These ligands produce a ring like structure called chelate. The polydentate ligand is called a chelating agent, the process of chelate formation is called chelation and the compounds formed are known as chelate compounds. Chelation increases the stability of complex. For example, ethylene diamide acts as a bidentate chelating ligand.',
    'کثیر دندانی لیگنڈ کا ایک سے زیادہ مقام سے دھاتی آئن کے ساتھ بند بنانا کیلیٹنگ لیگنڈ کہلاتا ہے۔ یہ لیگنڈز حلقے جیسی ساخت کیلیٹ بناتے ہیں۔ کثیر دندانی لیگنڈ کیلیٹنگ عامل، کیلیٹ بننے کا عمل کیلیشن اور بننے والے مرکبات کیلیٹ مرکبات کہلاتے ہیں۔ کیلیشن کمپلیکس کا استحکام بڑھاتی ہے۔ مثلاً ایتھلین ڈائی امائیڈ دو دندانی کیلیٹنگ لیگنڈ کے طور پر عمل کرتا ہے۔',
    'د څو غاښیز لېګنډ له یوه څخه د ډېرو ځایونو له لارې له فلزي ایون سره تړل کېدل کېلېټ جوړوونکی لېګنډ بلل کېږي. دا لېګنډونه د کړۍ په څېر جوړښت، کېلېټ، جوړوي. څو غاښیز لېګنډ کېلېټ جوړوونکی عامل، د جوړېدو بهیر کېلېشن او جوړ شوي مرکبات کېلېټ مرکبات بلل کېږي. کېلېشن د کمپلېکس ثبات زیاتوي. د بېلګې په توګه اېتیلین ډای امایډ د دوه غاښیز کېلېټ جوړوونکي لېګنډ په توګه عمل کوي.')
visual('chem12-p57-chelate','chelate')
head('14.2.2 Nomenclature of Coordination Compounds','14.2.2 تناسقی مرکبات کی نام گذاری','14.2.2 د کواردینېشن مرکباتو نوم اېښودنه')
add('The systematic names of complex compounds are based on rules recommended by the Inorganic Nomenclature Committee of International Union of Pure and Applied Chemistry (IUPAC). The rules for naming the coordination compounds are as follows:',
    'کمپلیکس مرکبات کے منظم نام خالص اور اطلاقی کیمیا کی بین الاقوامی یونین (IUPAC) کی غیر نامیاتی نام گذاری کمیٹی کے تجویز کردہ قواعد پر مبنی ہیں۔ تناسقی مرکبات کے نام رکھنے کے قواعد یہ ہیں:',
    'د کمپلېکس مرکباتو منظم نومونه د خالصې او تطبیقي کیمیا د نړیوالې ټولنې (IUPAC) د غیر عضوي نوم اېښودنې د کمېټې پر سپارښتل شوو اصولو ولاړ دي. د کواردینېشن مرکباتو د نوم اېښودنې اصول دا دي:')
add('1. The cation is named before the anion, as in other ionic compounds. For example, in the K₃[Fe(CN)₆] and [Co(NH₃)₄Cl₂]Cl compounds, we name the K⁺ and [Co(NH₃)₄Cl₂]⁺ cations first, respectively.',
    '1. دوسرے آئنک مرکبات کی طرح مثبت آئن کا نام منفی آئن سے پہلے ہے۔ مثلاً K₃[Fe(CN)₆] اور [Co(NH₃)₄Cl₂]Cl میں بالترتیب K⁺ اور [Co(NH₃)₄Cl₂]⁺ مثبت آئنوں کے نام پہلے ہیں۔',
    '1. د نورو ایوني مرکباتو په څېر مثبت ایون له منفي ایون څخه مخکې نومول کېږي. د بېلګې په توګه په K₃[Fe(CN)₆] او [Co(NH₃)₄Cl₂]Cl کې په ترتیب سره لومړی K⁺ او [Co(NH₃)₄Cl₂]⁺ مثبت ایونونه نوموو.')
visual('chem12-p57-naming-cation-anion','names')
add('2. In naming the complex ion, the ligand names are written in alphabetical order, before the name of the central metal ion. There should be no space between the name of the ligand and the name of the central metal ion.',
    '2. کمپلیکس آئن کے نام میں لیگنڈز کے نام حروف تہجی کی ترتیب سے مرکزی دھاتی آئن کے نام سے پہلے لکھتے ہیں۔ لیگنڈ اور مرکزی دھاتی آئن کے ناموں کے درمیان خلا نہیں ہونا چاہیے۔',
    '2. د کمپلېکس ایون په نوم اېښودنه کې د لېګنډونو نومونه په الفبايي ترتیب د مرکزي فلزي ایون له نوم څخه مخکې لیکل کېږي. د لېګنډ او مرکزي فلزي ایون د نومونو ترمنځ باید واټن نه وي.')
add('3. Numerical prefixes di, tri, tetra etc., are used for indicating the number of the same kind of ligand. Thus, the ligands in the cation [Co(NH₃)₄Cl₂]⁺ are “tetraamminedichloro”. If the ligand already contains a Greek prefix (e.g. ethylendiamine) if it is polydentate ligands the prefixes, bis-, tris-, tetrakis-, pentakis- are used instead. Numerical prefixes are not considered for determination of alphabetical order.',
    '3. ایک ہی قسم کے لیگنڈ کی تعداد کے لیے di، tri، tetra وغیرہ عددی سابقے ہیں۔ یوں [Co(NH₃)₄Cl₂]⁺ کے لیگنڈز tetraamminedichloro ہیں۔ اگر لیگنڈ میں پہلے یونانی سابقہ ہو (مثلاً ethylendiamine)، یا کثیر دندانی لیگنڈ ہو، تو bis-، tris-، tetrakis- اور pentakis- استعمال کرتے ہیں۔ حروف تہجی کی ترتیب مقرر کرنے میں عددی سابقے شمار نہیں ہوتے۔',
    '3. د یو ډول لېګنډ د شمېر لپاره di، tri، tetra او نور عددي مختاړي کارېږي. نو په [Co(NH₃)₄Cl₂]⁺ کې لېګنډونه tetraamminedichloro دي. که لېګنډ له مخکې یوناني مختاړی ولري (لکه ethylendiamine) یا څو غاښیز وي، پر ځای یې bis-، tris-، tetrakis- او pentakis- کارېږي. د الفبايي ترتیب په ټاکلو کې عددي مختاړي نه شمېرل کېږي.')
record=section('14.7','Ligands, coordination sphere and naming rules','لیگنڈز، تناسقی کرہ اور نام گذاری کے قواعد','لېګنډونه، د کواردینېشن ساحه او د نوم اېښودنې اصول',paras,layout,blocks,'56–57');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':32,'printedPages':[56,57]}]
issues=[{'id':'chem12-p57-ethylene-diamide','printedPage':57,'description':'Chelate prose and diagram caption print ethylene diamide, while the structure is an ethylenediamine-type N donor ring. Printed name retained.'},{'id':'chem12-p57-ferrocyanide-formula','printedPage':57,'description':'Naming rule1 prints K3[Fe(CN)6], whereas the adjacent named example gives K4[Fe(CN)6] potassium hexacyanoferrate(II). Both source forms retained.'}]
if __name__=='__main__':save(32,[record],trim=[{'id':'14.8','startsAt':'The oxidation number of the central metal ion'}],issues=issues,chapter_number=14)
