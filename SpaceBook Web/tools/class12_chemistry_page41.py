"""PDF41 printed74–75: iron carbonate, thiocyanate and copper reactions."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def eq(e):add(e,e,e,'equation')
add('Iron (II) Ions and Carbonate Ions','آئرن(II) آئن اور کاربونیٹ آئن','د اوسپنې(II) ایونونه او کاربونېټ ایونونه','heading')
add('When iron (II) ion combines with carbonate ion, it produces precipitate of iron (II) carbonate.','آئرن(II) آئن کاربونیٹ آئن سے ملے تو آئرن(II) کاربونیٹ کا رسوب بناتا ہے۔','چې د اوسپنې(II) ایون له کاربونېټ ایون سره یوځای شي، د اوسپنې(II) کاربونېټ رسوب جوړوي.')
eq('Fe²⁺(aq) + CO₃²⁻(aq) → FeCO₃(s)')
add('Iron (III) Ions and Carbonate Ions','آئرن(III) آئن اور کاربونیٹ آئن','د اوسپنې(III) ایونونه او کاربونېټ ایونونه','heading')
add('The hexaaquairon (III) ion is acidic to react with the weakly basic carbonate ion. If we add sodium carbonate solution to a solution of hexaaquairon (III) ions, it produces the precipitate of metal hydroxide.',
 'ہیکسا ایکوا آئرن(III) آئن تیزابی ہے اور کمزور اساسی کاربونیٹ آئن سے تعامل کرتا ہے۔ اس کے محلول میں سوڈیم کاربونیٹ محلول ڈالیں تو دھاتی ہائیڈرو آکسائیڈ کا رسوب بنتا ہے۔',
 'هېکسا اکوا اوسپنې(III) ایون اسیدي دی او له کمزوري قلوي کاربونېټ ایون سره تعامل کوي. که محلول ته یې سوډیم کاربونېټ محلول زیات کړو، د فلزي هایدروکسایډ رسوب جوړوي.')
add('In this reaction, the carbonate ions remove hydrogen ions from the hexaaqua ion and produce the neutral complex.','اس تعامل میں کاربونیٹ آئن ہیکسا ایکوا آئن سے ہائیڈروجن آئن نکال کر بے بار کمپلیکس بناتے ہیں۔','په دې تعامل کې کاربونېټ ایونونه له هېکسا اکوا ایون څخه هایدروجن ایونونه لرې کوي او خنثی کمپلېکس جوړوي.')
add('Depending on the properties of carbonates ions to hexaaqua ions, we will get either hydrogen carbonate ions or carbon dioxide gas which is formed by the reaction between the hydrogen ions and carbonate ions. The more usually used equation shows the formation of carbon dioxide.',
 'کاربونیٹ آئنوں کی ہیکسا ایکوا آئنوں کے مقابل خصوصیات کے لحاظ سے ہائیڈروجن کاربونیٹ آئن یا کاربن ڈائی آکسائیڈ گیس حاصل ہوگی، جو ہائیڈروجن اور کاربونیٹ آئنوں کے تعامل سے بنتی ہے۔ زیادہ استعمال ہونے والی مساوات کاربن ڈائی آکسائیڈ بننا دکھاتی ہے۔',
 'هېکسا اکوا ایونونو ته د کاربونېټ ایونونو د ځانګړنو له مخې به هایدروجن کاربونېټ ایونونه یا کاربن ډای اکسایډ ګاز ترلاسه کړو، چې د هایدروجن او کاربونېټ ایونونو په تعامل جوړېږي. ډېره کارېدونکې معادله د کاربن ډای اکسایډ جوړېدل ښيي.')
eq('2[Fe(H₂O)₆]³⁺ + 3CO₃²⁻ → 2[Fe(H₂O)₃(OH)₃] + 3CO₂ + 3H₂O')
add('Reaction of Iron (III) ions with Thiocyanate ions','تھیوسائنائیٹ آئنوں سے آئرن(III) آئنوں کا تعامل','له تیوسیانېټ ایونونو سره د اوسپنې(III) ایونونو تعامل','heading')
add('Iron(III) ions reacts with thiocyanate ions, SCN⁻ (from sodium or potassium or ammonium thiocyanate solution) and an intense blood red solution containing the ion [Fe(SCN)(H₂O)₅]²⁺ is produced. This test confirms the presence of iron (III) ion in solution.',
 'آئرن(III) آئن تھیوسائنائیٹ آئنوں SCN⁻ (سوڈیم، پوٹاشیم یا امونیم تھیوسائنائیٹ محلول سے) سے تعامل کرتے ہیں اور [Fe(SCN)(H₂O)₅]²⁺ آئن والا گہرا خون جیسا سرخ محلول بنتا ہے۔ یہ جانچ محلول میں آئرن(III) آئن کی موجودگی کی تصدیق ہے۔',
 'د اوسپنې(III) ایونونه له تیوسیانېټ ایونونو SCN⁻ (د سوډیم، پوتاشیم یا امونیم تیوسیانېټ له محلول څخه) سره تعامل کوي او د [Fe(SCN)(H₂O)₅]²⁺ ایون لرونکی سخت وینې ته ورته سور محلول جوړېږي. دا ازموینه په محلول کې د اوسپنې(III) ایون شتون تاییدوي.')
add('14.3.5 Copper','14.3.5 تانبا','14.3.5 مس','heading')
add('Copper (Cu), is brownish-red metallic element that is one of the most widely used metals. Copper is one of the two common yellow metals (the other being gold), although a thin coating of copper (I) oxide, Cu₂O, often makes copper look reddish.',
 'تانبا (Cu) بھورا سرخ دھاتی عنصر ہے جو سب سے زیادہ استعمال ہونے والی دھاتوں میں ہے۔ تانبا دو عام پیلی دھاتوں میں سے ایک ہے (دوسری سونا ہے)، اگرچہ کاپر(I) آکسائیڈ Cu₂O کی باریک تہہ اکثر اسے سرخی مائل دکھاتی ہے۔',
 'مس (Cu) نسواري سور فلزي عنصر دی چې له تر ټولو ډېرو کارېدونکو فلزونو څخه دی. مس له دوو عامو ژېړو فلزونو یو دی (بل سره زر دي)، که څه هم د مسو(I) اکسایډ Cu₂O نری پوښ یې ډېر وخت سور ښکاره کوي.')
add('The atomic number of copper is 29 and its atomic mass is 63.546 a.m.u.','تانبے کا جوہری عدد 29 اور جوہری کمیت 63.546 a.m.u. ہے۔','د مسو اټومي شمېره 29 او اټومي کتله 63.546 a.m.u. ده.')
add('14.3.5.1 Oxidation States','14.3.5.1 تکسیدی حالتیں','14.3.5.1 د اکسیدېشن حالتونه','heading')
add('Copper shows a variety of oxidation states ranging from +1 to +4 in its compounds. The two principal oxidation states of copper are +1 and +2.','تانبا مرکبات میں +1 سے +4 تک مختلف تکسیدی حالتیں دکھاتا ہے۔ دو بنیادی حالتیں +1 اور +2 ہیں۔','مس په مرکباتو کې له +1 تر +4 بېلابېل اکسیدېشن حالتونه ښيي. دوه اصلي حالتونه یې +1 او +2 دي.')
add('Copper (I) compounds are expected to be diamagnetic in nature and are usually colourless. Examples of these compounds are Cu₂O, CuCl, CuBr etc. In solid compounds copper (I) is often the more stable state at moderate temperatures. The compounds of this ion are called cuprous compounds.',
 'کاپر(I) مرکبات سے ڈائی میگنیٹک ہونے کی توقع ہے اور عموماً بے رنگ ہیں۔ مثالیں Cu₂O، CuCl اور CuBr وغیرہ ہیں۔ ٹھوس مرکبات میں معتدل درجہ حرارت پر کاپر(I) اکثر زیادہ مستحکم حالت ہے۔ اس آئن کے مرکبات کیوپرس مرکبات ہیں۔',
 'د مسو(I) مرکبات تمه کېږي ډایمقناطیسي وي او عموماً بې رنګه دي. بېلګې یې Cu₂O، CuCl او CuBr دي. په جامدو مرکباتو کې په منځنیو تودوخې درجو کې مس(I) ډېر وخت ثابت حالت وي. د دې ایون مرکبات کیوپرس مرکبات دي.','list')
add('The copper (II) ion is usually more stable in aqueous solutions. Compounds of this ion are called cupric compounds and are usually coloured. Examples are CuO, CuF₂, CuCl₂, CuCO₃, CuSO₄ etc.',
 'کاپر(II) آئن آبی محلولوں میں عموماً زیادہ مستحکم ہے۔ اس کے مرکبات کیوپرک مرکبات ہیں اور عموماً رنگین ہیں۔ مثالیں CuO، CuF₂، CuCl₂، CuCO₃ اور CuSO₄ وغیرہ ہیں۔',
 'د مسو(II) ایون په اوبلنو محلولونو کې عموماً ډېر ثابت دی. مرکبات یې کیوپرېک مرکبات دي او عموماً رنګین دي. بېلګې یې CuO، CuF₂، CuCl₂، CuCO₃ او CuSO₄ دي.','list')
add('Copper (III) is most characteristically found in oxides. A simple example is potassium cuprate, KCuO₂, a blue–black solid. The best studied copper (III) compounds are the cuprate superconductors. Yttrium barium copper oxide (YBa₂Cu₃O₇) consists of both Cu (II) and Cu (III) centres.',
 'کاپر(III) خاص طور پر آکسائیڈز میں ملتا ہے۔ سادہ مثال پوٹاشیم کیوپریٹ KCuO₂، نیلا سیاہ ٹھوس ہے۔ سب سے زیادہ مطالعہ شدہ کاپر(III) مرکبات کیوپریٹ فوق موصل ہیں۔ اٹریئم بیریم کاپر آکسائیڈ (YBa₂Cu₃O₇) میں Cu(II) اور Cu(III) دونوں مراکز ہیں۔',
 'مس(III) په ځانګړي ډول په اکسایډونو کې موندل کېږي. ساده بېلګه یې پوتاشیم کیوپرېټ KCuO₂، نیلي تور جامد دی. تر ټولو ډېر څېړل شوي د مسو(III) مرکبات کیوپرېټ فوق هادي دي. ایتریم باریم مس اکسایډ (YBa₂Cu₃O₇) د Cu(II) او Cu(III) دواړو مرکزونه لري.','list')
add('Like oxide, fluoride is a highly basic anion and is known to stabilize metal ions in high oxidation states. Indeed, both copper (III) and even copper (IV) fluorides are known, K₃CuF₆ and Cs₂CuF₆, respectively.',
 'آکسائیڈ کی طرح فلورائیڈ انتہائی اساسی منفی آئن ہے اور بلند تکسیدی حالتوں کے دھاتی آئنوں کو مستحکم کرتا ہے۔ کاپر(III) اور حتیٰ کہ کاپر(IV) فلورائیڈز بالترتیب K₃CuF₆ اور Cs₂CuF₆ معلوم ہیں۔',
 'د اکسایډ په څېر فلورایډ ډېر قلوي منفي ایون دی او په لوړو اکسیدېشن حالتونو کې فلزي ایونونه ثابتوي. د مسو(III) او حتی د مسو(IV) فلورایډونه په ترتیب K₃CuF₆ او Cs₂CuF₆ پېژندل شوي دي.','list')
add('14.3.5.2 The Reaction of Hexaaquacopper (II) Ions with Hydroxide Ions, Ammonia and Carbonate Ions','14.3.5.2 ہائیڈرو آکسائیڈ آئنوں، امونیا اور کاربونیٹ آئنوں سے ہیکسا ایکوا کاپر(II) آئنوں کا تعامل','14.3.5.2 له هایدروکسایډ ایونونو، امونیا او کاربونېټ ایونونو سره د هېکسا اکوا مسو(II) ایونونو تعامل','heading')
add('Reactions of Hexaaquacopper (II) Ions with Hydroxide Ions','ہائیڈرو آکسائیڈ آئنوں سے ہیکسا ایکوا کاپر(II) آئنوں کے تعاملات','له هایدروکسایډ ایونونو سره د هېکسا اکوا مسو(II) ایونونو تعاملونه','heading')
add('Hydroxide ions (sodium hydroxide solution) remove hydrogen ions from the water ligands attached to the copper ion.','ہائیڈرو آکسائیڈ آئن (سوڈیم ہائیڈرو آکسائیڈ محلول) کاپر آئن سے جڑے آبی لیگنڈز سے ہائیڈروجن آئن نکالتے ہیں۔','هایدروکسایډ ایونونه (د سوډیم هایدروکسایډ محلول) د مسو ایون پورې تړلو اوبنیو لېګنډونو څخه هایدروجن ایونونه لرې کوي.')
add('The hydrogen ion has been removed from two of the water molecules, as a result a complex with no charge (a neutral complex) is produced. This complex is insoluble in water and so precipitation occurs.',
 'دو آبی سالموں سے ہائیڈروجن آئن نکالا گیا ہے، اس لیے بے بار (بے اثر) کمپلیکس بنتا ہے۔ یہ پانی میں ناقابل حل ہے، اس لیے رسوب بنتا ہے۔',
 'له دوو اوبنیو مالیکولونو هایدروجن ایون لرې شوی، نو بې چارج (خنثی) کمپلېکس جوړېږي. دا په اوبو کې نه حل کېږي، نو رسوب جوړېږي.')
eq('[Cu(H₂O)₆]²⁺ + 2OH⁻ → [Cu(H₂O)₄(OH)₂] + 2H₂O')
add('Blue solution — Blue ppt','نیلا محلول — نیلا رسوب','نیلي محلول — نیلي رسوب')
add('Reaction of Hexaaquacopper (II) Ions with Ammonia','امونیا سے ہیکسا ایکوا کاپر(II) آئنوں کا تعامل','له امونیا سره د هېکسا اکوا مسو(II) ایونونو تعامل','heading')
add('The ammonia acts both a base and a ligand. When a small amount of ammonia is added to solution of hexaaquacopper (II) ions, it pulls out the H⁺ ions from the complex ion and produce neutral complex.',
 'امونیا اساس اور لیگنڈ دونوں کا کام کرتی ہے۔ ہیکسا ایکوا کاپر(II) محلول میں تھوڑی امونیا ڈالیں تو وہ کمپلیکس سے H⁺ آئن نکالتی اور بے بار کمپلیکس بناتی ہے۔',
 'امونیا هم قلوي او هم لېګنډ دی. د هېکسا اکوا مسو(II) محلول ته لږه امونیا زیاته شي، له کمپلېکس څخه H⁺ ایونونه راباسي او خنثی کمپلېکس جوړوي.')
eq('[Cu(H₂O)₆]²⁺ + 2NH₃ → [Cu(H₂O)₄(OH)₂] + 2NH₄⁺')
add('Blue (solution) — Blue ppt','نیلا (محلول) — نیلا رسوب','نیلي (محلول) — نیلي رسوب')
add('The precipitate dissolves in excess ammonia.','رسوب زائد امونیا میں حل ہوتا ہے۔','رسوب په زیاته امونیا کې حل کېږي.')
add('The ammonia replaces water as a ligand to give tetraamminediaquacopper (II) ions.','امونیا بطور لیگنڈ پانی کی جگہ لے کر ٹیٹرا امین ڈائی ایکوا کاپر(II) آئن بناتی ہے۔','امونیا د لېګنډ په توګه د اوبو ځای نیسي او ټېټرا امین ډای اکوا مسو(II) ایونونه جوړوي.')
eq('[Cu(H₂O)₄(OH)₂] + 4NH₃ → [Cu(NH₃)₄(H₂O)₂]²⁺ + 2H₂O + 2OH⁻')
add('Blue ppt — Blue solution','نیلا رسوب — نیلا محلول','نیلي رسوب — نیلي محلول')
record=section('14.16','Iron carbonate and copper chemistry','آئرن کاربونیٹ اور تانبے کی کیمیا','د اوسپنې کاربونېټ او د مسو کیمیا',paras,layout,[],'74–75');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':41,'printedPages':[74,75]}]
if __name__=='__main__':save(41,[record],carry=[{'from':'14.16','to':'14.17','startsAt':'Reaction of Hexaaquacopper (11) Ions with Carbonate Ions'}],issues=[{'id':'chem12-p74-cuprous-colour','printedPage':74,'description':'Printed cuprous colourless generalization includesCu2O; retained.'}],chapter_number=14)
