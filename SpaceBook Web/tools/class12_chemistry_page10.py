"""PDF10: acid/base trends and oxide reactions, printed 12–13."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
head('13.1.4.1 Trend in Acid Base Behaviour','13.1.4.1 تیزابی و اساسی رویے کا رجحان','13.1.4.1 د تېزابي او قلوي چلند تمایل')
add('As we move in 3ʳᵈ period from left to right, acidity of oxides increases, ranging from strongly basic oxides on the left to strongly acidic on the right side, with an amphoteric oxide (aluminium oxide) in the middle.',
    'تیسرے دور میں بائیں سے دائیں جانے پر آکسائیڈز کی تیزابیت بڑھتی ہے: بائیں جانب شدید اساسی آکسائیڈز اور دائیں جانب شدید تیزابی آکسائیڈز ہوتے ہیں، جبکہ درمیان میں دو خصوصیتی آکسائیڈ (ایلومینیم آکسائیڈ) ہوتا ہے۔',
    'په درېیمه دوره کې له کیڼ څخه ښي لوري ته د اکسایډونو تېزابیت زیاتېږي؛ په کیڼ کې پیاوړي قلوي اکسایډونه، په ښي کې پیاوړي تېزابي اکسایډونه او په منځ کې امفوتېریک اکسایډ (المونیم اکسایډ) دی.')
add('This trend applies only to the highest oxidation of the individual elements (see the top row of the table). For example, sulphur trioxide reacts with water to form sulphuric acid. They, however, also react with bases such as sodium hydroxide to form salts such as sodium sulphate.',
    'یہ رجحان صرف انفرادی عناصر کی سب سے بلند تکسیدی حالت پر لاگو ہوتا ہے (جدول کی اوپر والی قطار دیکھیں)۔ مثلاً سلفر ٹرائی آکسائیڈ پانی کے ساتھ تعامل کر کے سلفیورک ایسڈ بناتا ہے۔ تاہم یہ سوڈیم ہائیڈرو آکسائیڈ جیسے اساسوں کے ساتھ بھی تعامل کر کے سوڈیم سلفیٹ جیسے نمک بناتے ہیں۔',
    'دا تمایل یوازې د هر عنصر پر تر ټولو لوړ اکسیدېشن حالت تطبیقېږي (د جدول پاسنی کتار وګورئ). د بېلګې په توګه، سلفر ټرای اکسایډ له اوبو سره تعامل کوي او سلفوریک اسید جوړوي. خو دا له اساسونو، لکه سوډیم هایدروکسایډ، سره هم تعامل کوي او د سوډیم سلفېټ په څېر مالګې جوړوي.')
add('Table 13.9 Trend in Acid Base Behaviour of Period 3 Oxides.','جدول 13.9 تیسرے دور کے آکسائیڈز کے تیزابی و اساسی رویے کا رجحان۔','جدول 13.9 د درېیمې دورې د اکسایډونو د تېزابي او قلوي چلند تمایل.')
headers=['Oxide of period 3','Na₂O','MgO','Al₂O₃','SiO₂','P₄O₁₀ (P₄O₆)','SO₃ (SO₂)','Cl₂O₇ (Cl₂O)']
t={'id':'chem12-table-13-9','headers':headers,
   'rows':[['Nature of oxide','Basic (alkaline)','Basic (weakly alkaline)','Amphoteric','Acidic','Acidic','Acidic','Acidic']],
   'translations':[{'language':'اردو','headers':['تیسرے دور کا آکسائیڈ']+headers[1:],'rows':[['آکسائیڈ کی نوعیت','اساسی (الکلائن)','اساسی (کمزور الکلائن)','دو خصوصیتی','تیزابی','تیزابی','تیزابی','تیزابی']]},
                   {'language':'پښتو','headers':['د درېیمې دورې اکسایډ']+headers[1:],'rows':[['د اکسایډ ماهیت','قلوي','کمزوری قلوي','امفوتېریک','تېزابي','تېزابي','تېزابي','تېزابي']]}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
head('13.1.4.2 Reactions of Oxides with Water, Acids and Bases','13.1.4.2 آکسائیڈز کے پانی، تیزابوں اور اساسوں کے ساتھ تعاملات','13.1.4.2 له اوبو، تېزابونو او اساسونو سره د اکسایډونو تعاملونه')
add('The period 3ʳᵈ consists of elements Na to Ar. There occurs metals, metalloids and non-metals. Oxides of Period 3 elements are basic to amphoteric to acidic.',
    'تیسرا دور Na سے Ar تک کے عناصر پر مشتمل ہے۔ اس میں دھاتیں، نیم دھاتیں اور غیر دھاتیں ہیں۔ تیسرے دور کے آکسائیڈز اساسی سے دو خصوصیتی اور پھر تیزابی ہیں۔',
    'درېیمه دوره له Na څخه تر Ar پورې عناصر لري. پکې فلزونه، نیمه فلزونه او نافلزونه شته. د درېیمې دورې اکسایډونه له قلوي څخه امفوتېریک او بیا تېزابي دي.')
head('Reaction of oxides with water','آکسائیڈز کا پانی کے ساتھ تعامل','له اوبو سره د اکسایډونو تعامل')
add('The oxides of period 3ʳᵈ include oxides of metals such as Na₂O and MgO, which are basic in nature. They combine with water to form bases.',
    'تیسرے دور کے آکسائیڈز میں Na₂O اور MgO جیسے دھاتی آکسائیڈز شامل ہیں، جن کی نوعیت اساسی ہے۔ یہ پانی سے مل کر اساس بناتے ہیں۔',
    'د درېیمې دورې په اکسایډونو کې د Na₂O او MgO په څېر فلزي اکسایډونه شامل دي، چې قلوي ماهیت لري. دا له اوبو سره یوځای کېږي او اساسونه جوړوي.')
eq('Na₂O(s) + H₂O(l) → 2NaOH(aq)')
eq('MgO(s) + H₂O(l) → Mg(OH)₂(aq)')
add('Al₂O₃ does not react with H₂O, since the strength of ionic bonds holding Al₂O₃ molecules lattice together is too much strong.',
    'Al₂O₃ پانی (H₂O) کے ساتھ تعامل نہیں کرتا، کیونکہ اس کے سالموں کی جالی کو جوڑنے والے آئنک بند بہت زیادہ مضبوط ہیں۔',
    'Al₂O₃ له H₂O سره تعامل نه کوي، ځکه د Al₂O₃ د مالیکولونو جالۍ سره تړونکي ایوني تړونونه ډېر پیاوړي دي.')
add('Silicon dioxide does not react with H₂O. The covalent bonds holding the silicon and oxygen atoms together in the 3-dimensional lattice are too strong to be broken down by water molecules.',
    'سلیکان ڈائی آکسائیڈ H₂O کے ساتھ تعامل نہیں کرتا۔ سہ جہتی جالی میں سلیکان اور آکسیجن کے ایٹموں کو جوڑنے والے اشتراکی بند اتنے مضبوط ہیں کہ پانی کے سالمے انہیں نہیں توڑ سکتے۔',
    'سیلیکان ډای اکسایډ له H₂O سره تعامل نه کوي. په درې بعدي جالۍ کې د سیلیکان او اکسیجن اټومونه سره تړونکي کووالنټ تړونونه دومره پیاوړي دي چې د اوبو مالیکولونه یې نه شي ماتولای.')
add('Oxides of non-metals such as oxides of sulphur, phosphorus and chlorine react with water to form oxyacids.',
    'غیر دھاتوں، مثلاً سلفر، فاسفورس اور کلورین، کے آکسائیڈز پانی کے ساتھ تعامل کر کے آکسی تیزاب بناتے ہیں۔',
    'د نافلزونو اکسایډونه، لکه د سلفر، فاسفورس او کلورین اکسایډونه، له اوبو سره تعامل کوي او اکسي اسیدونه جوړوي.')
add('Oxides of the phosphorus such as P₄O₁₀, react with water to produce acids.',
    'فاسفورس کے آکسائیڈز، مثلاً P₄O₁₀، پانی کے ساتھ تعامل کر کے تیزاب بناتے ہیں۔',
    'د فاسفورس اکسایډونه، لکه P₄O₁₀، له اوبو سره تعامل کوي او تېزابونه جوړوي.')
eq('P₄O₁₀(s) + 6H₂O(l) → 4H₃PO₄(l)')
add('Sulphur dioxide (SO₂) and sulphur trioxide (SO₃) react with water to produce sulphurous acid and sulphuric acid respectively.',
    'سلفر ڈائی آکسائیڈ (SO₂) اور سلفر ٹرائی آکسائیڈ (SO₃) پانی کے ساتھ تعامل کر کے بالترتیب سلفیورس ایسڈ اور سلفیورک ایسڈ بناتے ہیں۔',
    'سلفر ډای اکسایډ (SO₂) او سلفر ټرای اکسایډ (SO₃) له اوبو سره تعامل کوي او په ترتیب سره سلفورس اسید او سلفوریک اسید جوړوي.')
eq('SO₂(g) + H₂O(l) → H₂SO₃(l)')
eq('SO₃(g) + H₂O(l) → H₂SO₄(l)')
add('Chlorine forms several oxides, but only two are considered here. i.e. dichlorine heptoxide (Cl₂O₇), and dichlorine monoxide (Cl₂O).',
    'کلورین کئی آکسائیڈز بناتی ہے، مگر یہاں صرف دو بیان کیے گئے ہیں: ڈائی کلورین ہیپٹا آکسائیڈ (Cl₂O₇) اور ڈائی کلورین مونو آکسائیڈ (Cl₂O)۔',
    'کلورین څو اکسایډونه جوړوي، خو دلته یوازې دوه څېړل کېږي: ډای کلورین هېپټا اکسایډ (Cl₂O₇) او ډای کلورین مونو اکسایډ (Cl₂O).')
add('Dichlorine heptoxide (Cl₂O₇) reacts with water to give the very strong acid, perchloric acid (HClO₄). While Cl₂O forms hypochlorous acid (HOCl)',
    'ڈائی کلورین ہیپٹا آکسائیڈ (Cl₂O₇) پانی کے ساتھ تعامل کر کے بہت مضبوط تیزاب، پرکلورک ایسڈ (HClO₄)، بناتا ہے، جبکہ Cl₂O ہائپوکلورس ایسڈ (HOCl) بناتا ہے۔',
    'ډای کلورین هېپټا اکسایډ (Cl₂O₇) له اوبو سره تعامل کوي او ډېر پیاوړی تېزاب، پرکلوریک اسید (HClO₄)، جوړوي؛ خو Cl₂O هایپوکلورس اسید (HOCl) جوړوي.')
eq('Cl₂O₇(l) + H₂O(l) → 2HClO₄(aq)')
eq('Cl₂O(g) + H₂O(l) ⇌ 2HOCl(aq)')
head('Reaction of Oxides with Acids and Bases','آکسائیڈز کا تیزابوں اور اساسوں کے ساتھ تعامل','له تېزابونو او اساسونو سره د اکسایډونو تعامل')
add('Na₂O and MgO react with acids to form salt and water.',
    'Na₂O اور MgO تیزابوں کے ساتھ تعامل کر کے نمک اور پانی بناتے ہیں۔',
    'Na₂O او MgO له تېزابونو سره تعامل کوي او مالګه او اوبه جوړوي.')
eq('Na₂O(s) + 2HCl(aq) → 2NaCl(aq) + H₂O(l)')
eq('MgO(s) + 2HCl(aq) → MgCl₂(aq) + H₂O(l)')
add('Aluminium oxide is amphoteric. It reacts with hot dilute hydrochloric acid and produces aluminium chloride and water.',
    'ایلومینیم آکسائیڈ دو خصوصیتی ہے۔ یہ گرم، رقیق ہائیڈروکلورک ایسڈ کے ساتھ تعامل کر کے ایلومینیم کلورائیڈ اور پانی بناتا ہے۔',
    'المونیم اکسایډ امفوتېریک دی. دا له تود رقیق هایدروکلوریک اسید سره تعامل کوي او المونیم کلورایډ او اوبه جوړوي.')
add('As a Base:','بطور اساس:','د اساس په توګه:')
eq('Al₂O₃(s) + 6HCl(aq) → 2AlCl₃(aq) + 3H₂O(l)')
add('Aluminium oxide also reacts with bases. When concentrated sodium hydroxide solution is added to aluminium oxide, complex ion (sodium tetrahydroxoaluminate (III)) is formed.',
    'ایلومینیم آکسائیڈ اساسوں کے ساتھ بھی تعامل کرتا ہے۔ اس میں سوڈیم ہائیڈرو آکسائیڈ کا مرتکز محلول ملانے سے پیچیدہ آئن (سوڈیم ٹیٹرا ہائیڈروکسو ایلومینیٹ (III)) بنتا ہے۔',
    'المونیم اکسایډ له اساسونو سره هم تعامل کوي. کله چې د سوډیم هایدروکسایډ غلیظ محلول ورزیات شي، پېچلی ایون (سوډیم ټېټرا هایدروکسو الومینېټ (III)) جوړېږي.')
add('As an Acid:','بطور تیزاب:','د تېزاب په توګه:')
eq('Al₂O₃(s) + 2NaOH(aq) + 3H₂O(l) → 2NaAl(OH)₄(aq)')
add('SiO₂ is chemically very inert and weakly acidic. It reacts with hot concentrated sodium hydroxide to produce sodium silicate and water.',
    'SiO₂ کیمیائی طور پر بہت غیر فعال اور کمزور تیزابی ہے۔ یہ گرم، مرتکز سوڈیم ہائیڈرو آکسائیڈ سے تعامل کر کے سوڈیم سلیکیٹ اور پانی بناتا ہے۔',
    'SiO₂ په کیمیاوي لحاظ ډېر غیر فعال او کمزوری تېزابي دی. له تود غلیظ سوډیم هایدروکسایډ سره تعامل کوي او سوډیم سیلیکېټ او اوبه جوړوي.')
eq('SiO₂(s) + 2NaOH(l) → Na₂SiO₃(l) + H₂O(g)')
add('Phosphorus oxides are acidic oxides, they react with alkalies to form salts and water. Phosphorus trioxide reacts with sodium hydroxide to form sodium phosphate and water.',
    'فاسفورس کے آکسائیڈز تیزابی ہیں؛ یہ الکلیوں کے ساتھ تعامل کر کے نمک اور پانی بناتے ہیں۔ فاسفورس ٹرائی آکسائیڈ سوڈیم ہائیڈرو آکسائیڈ کے ساتھ تعامل کر کے سوڈیم فاسفیٹ اور پانی بناتا ہے۔',
    'د فاسفورس اکسایډونه تېزابي اکسایډونه دي؛ له القلي موادو سره تعامل کوي او مالګې او اوبه جوړوي. فاسفورس ټرای اکسایډ له سوډیم هایدروکسایډ سره تعامل کوي او سوډیم فاسفېټ او اوبه جوړوي.')
eq('P₄O₆(s) + 12NaOH(aq) → 4Na₃PO₃(aq) + 6H₂O(l)')
add('Phosphorus pentaoxide reacts with sodium hydroxide to form sodium phosphate and water.',
    'فاسفورس پینٹا آکسائیڈ سوڈیم ہائیڈرو آکسائیڈ کے ساتھ تعامل کر کے سوڈیم فاسفیٹ اور پانی بناتا ہے۔',
    'فاسفورس پنتا اکسایډ له سوډیم هایدروکسایډ سره تعامل کوي او سوډیم فاسفېټ او اوبه جوړوي.')
eq('P₄O₁₀(s) + 12NaOH(aq) → 4Na₃PO₄(aq) + 6H₂O(l)')
add('Sulphur dioxide (SO₂) reacts with aqueous solution of sodium hydroxide and produces salt (sodium sulphite) and water. Sulphur trioxide (SO₃) reacts violently with water to produce sulphuric acid, which reacts with sodium hydroxide and produces salt (sodium sulphate).',
    'سلفر ڈائی آکسائیڈ (SO₂) سوڈیم ہائیڈرو آکسائیڈ کے آبی محلول کے ساتھ تعامل کر کے نمک (سوڈیم سلفائٹ) اور پانی بناتا ہے۔ سلفر ٹرائی آکسائیڈ (SO₃) پانی کے ساتھ شدت سے تعامل کر کے سلفیورک ایسڈ بناتا ہے، جو سوڈیم ہائیڈرو آکسائیڈ سے تعامل کر کے نمک (سوڈیم سلفیٹ) بناتا ہے۔',
    'سلفر ډای اکسایډ (SO₂) د سوډیم هایدروکسایډ له اوبلن محلول سره تعامل کوي او مالګه (سوډیم سلفایټ) او اوبه جوړوي. سلفر ټرای اکسایډ (SO₃) له اوبو سره په شدت تعامل کوي او سلفوریک اسید جوړوي، چې له سوډیم هایدروکسایډ سره په تعامل کې مالګه (سوډیم سلفېټ) جوړوي.')
eq('SO₂(g) + 2NaOH(aq) → Na₂SO₃(aq) + H₂O(l)')
eq('H₂SO₄(aq) + 2NaOH(aq) → Na₂SO₄(aq) + 2H₂O(l)')
record=section('13.6','13.1.4 Oxide acid-base behaviour and reactions','13.1.4 آکسائیڈز کا تیزابی و اساسی رویہ اور تعاملات','13.1.4 د اکسایډونو تېزابي او قلوي چلند او تعاملونه',paras,layout,blocks,'12–13')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':10,'printedPages':[12,13]}]
issues=[{'id':'chem12-p13-phosphorus-product','printedPage':13,'description':'The phosphorus trioxide reaction prose says sodium phosphate, while its printed equation gives Na3PO3. Both source forms retained.'}]
if __name__=='__main__':save(10,[record],issues=issues,carry=[{'from':'13.6','to':'13.7','startsAt':'Dichlorine heptoxide (C207) reacts directly'}])
