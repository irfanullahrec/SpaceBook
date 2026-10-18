"""PDF14, printed20–21: alkali-metal oxygen/oxide/chlorine reactions."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
def metals():add('(Where M = Li, Na, K, Rb, Cs)','(جہاں M = Li، Na، K، Rb، Cs)','(چې M = Li، Na، K، Rb، Cs دی)')
head('13.2.3 Reactions with Oxygen','13.2.3 آکسیجن کے ساتھ تعاملات','13.2.3 له اکسیجن سره تعاملونه')
add('Group – IA elements tarnish in air due to the formation of an oxide or hydroxide on the surface. These metals have to be stored without contact with air to prevent their oxidation. Their reactivity increases down the group.',
    'گروپ IA کے عناصر کی سطح پر آکسائیڈ یا ہائیڈرو آکسائیڈ بننے سے ہوا میں ان کی چمک ماند پڑتی ہے۔ تکسید سے بچانے کے لیے انہیں ہوا کے رابطے سے دور رکھنا ضروری ہے۔ گروپ میں نیچے جانے پر ان کی تعامل پذیری بڑھتی ہے۔',
    'د IA ګروپ عناصر په هوا کې پر سطحه د اکسایډ یا هایدروکسایډ د جوړېدو له امله خپل ځلا له لاسه ورکوي. د اکسیدېشن د مخنیوي لپاره باید له هوا سره له تماس پرته وساتل شي. په ګروپ کې ښکته تګ سره یې د تعامل وړتیا زیاتېږي.')
add('Li, Na and K are stored in oil. Cs and Rb are normally stored in a sealed glass tubes to prevent air contact.',
    'Li، Na اور K تیل میں رکھے جاتے ہیں۔ ہوا سے رابطہ روکنے کے لیے Cs اور Rb عموماً بند شیشے کی نلکیوں میں رکھے جاتے ہیں۔',
    'Li، Na او K په تېلو کې ساتل کېږي. له هوا سره د تماس د مخنیوي لپاره Cs او Rb عموماً په مهر شوو ښیښه یي نلونو کې ساتل کېږي.')
add('The group – IA elements react with oxygen to form normal oxides with general formula, M₂O.',
    'گروپ IA کے عناصر آکسیجن کے ساتھ تعامل کر کے عام آکسائیڈز بناتے ہیں، جن کا عمومی فارمولا M₂O ہے۔',
    'د IA ګروپ عناصر له اکسیجن سره تعامل کوي او عادي اکسایډونه جوړوي، چې عمومي فورمول یې M₂O دی.')
eq('4M(s) + O₂(g) → 2M₂O(s)');metals()
head('13.2.3.1 Reactions with Air or Oxygen and the formation of Normal Oxides, Peroxides, Super Oxides and their Stability','13.2.3.1 ہوا یا آکسیجن کے ساتھ تعاملات، عام آکسائیڈز، پرآکسائیڈز اور سپرآکسائیڈز کی تشکیل اور ان کا استحکام','13.2.3.1 له هوا یا اکسیجن سره تعاملونه، د عادي اکسایډونو، پراکسایډونو او سوپراکسایډونو جوړېدل او ثبات یې')
add('When the group – IA elements are heated with excess of air or oxygen, lithium forms normal oxide, Li₂O; sodium forms peroxide, Na₂O₂, whereas potassium, rubidium and caesium form superoxides having general formula MO₂.',
    'گروپ IA کے عناصر کو ہوا یا آکسیجن کی زیادہ مقدار کے ساتھ گرم کرنے پر لیتھیم عام آکسائیڈ Li₂O اور سوڈیم پرآکسائیڈ Na₂O₂ بناتا ہے، جبکہ پوٹاشیم، روبیڈیم اور سیزیم عمومی فارمولے MO₂ والے سپرآکسائیڈز بناتے ہیں۔',
    'کله چې د IA ګروپ عناصر په زیاته هوا یا اکسیجن کې تود شي، لیتیم عادي اکسایډ Li₂O او سوډیم پراکسایډ Na₂O₂ جوړوي؛ خو پوټاشیم، روبیډیم او سیزیم د MO₂ عمومي فورمول لرونکي سوپراکسایډونه جوړوي.')
eq('4Li(s) + O₂(g) → 2Li₂O(s)')
add('lithium oxide','لیتھیم آکسائیڈ','لیتیم اکسایډ')
eq('2Na(s) + O₂(g) —300°C→ Na₂O₂')
add('sodium peroxide','سوڈیم پرآکسائیڈ','سوډیم پراکسایډ')
eq('K(s) + O₂(g) → KO₂')
add('potassium superoxide','پوٹاشیم سپرآکسائیڈ','پوټاشیم سوپراکسایډ')
add('“Rb” and “Cs” catch fire in air and produce superoxide such as RbO₂ and CsO₂ respectively.',
    'Rb اور Cs ہوا میں آگ پکڑتے ہیں اور بالترتیب RbO₂ اور CsO₂ جیسے سپرآکسائیڈز بناتے ہیں۔',
    'Rb او Cs په هوا کې اور اخلي او په ترتیب سره د RbO₂ او CsO₂ په څېر سوپراکسایډونه جوړوي.')
add('Thus, the reactivity of alkali metals with oxygen increases down the group.',
    'چنانچہ گروپ میں نیچے جانے پر آکسیجن کے ساتھ الکلی دھاتوں کی تعامل پذیری بڑھتی ہے۔',
    'نو په ګروپ کې ښکته تګ سره له اکسیجن سره د القلي فلزونو د تعامل وړتیا زیاتېږي.')
head('13.2.3.2 Reactions of Oxides with Water and Dilute Acids','13.2.3.2 آکسائیڈز کے پانی اور رقیق تیزابوں کے ساتھ تعاملات','13.2.3.2 له اوبو او رقیقو تېزابونو سره د اکسایډونو تعاملونه')
head('i. Reactions of Oxides with Water','i. آکسائیڈز کے پانی کے ساتھ تعاملات','i. له اوبو سره د اکسایډونو تعاملونه')
add('Oxides of group – IA elements react with water to produce the respective bases. Group – IA elements react with oxygen to form normal oxides, peroxides or superoxides. These oxides react with water in different ways.',
    'گروپ IA کے عناصر کے آکسائیڈز پانی سے تعامل کر کے متعلقہ اساس بناتے ہیں۔ گروپ IA کے عناصر آکسیجن سے تعامل کر کے عام آکسائیڈز، پرآکسائیڈز یا سپرآکسائیڈز بناتے ہیں۔ یہ پانی کے ساتھ مختلف طریقوں سے تعامل کرتے ہیں۔',
    'د IA ګروپ د عناصرو اکسایډونه له اوبو سره تعامل کوي او اړوند اساسونه جوړوي. د IA ګروپ عناصر له اکسیجن سره په تعامل کې عادي اکسایډونه، پراکسایډونه یا سوپراکسایډونه جوړوي. دا اکسایډونه له اوبو سره په بېلابېلو لارو تعامل کوي.')
head('Normal oxides','عام آکسائیڈز','عادي اکسایډونه')
add('Normal oxide reacts with water and produce metal hydroxide. For example, Li₂O reacts with water and form lithium hydroxide.',
    'عام آکسائیڈ پانی سے تعامل کر کے دھاتی ہائیڈرو آکسائیڈ بناتا ہے۔ مثلاً Li₂O پانی سے تعامل کر کے لیتھیم ہائیڈرو آکسائیڈ بناتا ہے۔',
    'عادي اکسایډ له اوبو سره تعامل کوي او فلزي هایدروکسایډ جوړوي. د بېلګې په توګه، Li₂O له اوبو سره تعامل کوي او لیتیم هایدروکسایډ جوړوي.')
eq('Li₂O(s) + H₂O(l) → 2LiOH(aq)')
head('Peroxides','پرآکسائیڈز','پراکسایډونه')
add('Peroxides (M₂O₂) react with water and produce metal hydroxide and hydrogen peroxide. For example, Na₂O₂ reacts with water and form sodium hydroxide and hydrogen peroxide.',
    'پرآکسائیڈز (M₂O₂) پانی سے تعامل کر کے دھاتی ہائیڈرو آکسائیڈ اور ہائیڈروجن پرآکسائیڈ بناتے ہیں۔ مثلاً Na₂O₂ پانی سے تعامل کر کے سوڈیم ہائیڈرو آکسائیڈ اور ہائیڈروجن پرآکسائیڈ بناتا ہے۔',
    'پراکسایډونه (M₂O₂) له اوبو سره تعامل کوي او فلزي هایدروکسایډ او هایدروجن پراکسایډ جوړوي. د بېلګې په توګه، Na₂O₂ له اوبو سره تعامل کوي او سوډیم هایدروکسایډ او هایدروجن پراکسایډ جوړوي.')
eq('Na₂O₂(s) + 2H₂O(l) → 2NaOH(aq) + H₂O₂(aq)')
head('Super oxides','سپرآکسائیڈز','سوپراکسایډونه')
add('Super oxides (MO₂) react with water and produce metal hydroxide, hydrogen peroxide and oxygen gas. For example, KO₂ reacts with water and forms potassium hydroxide, hydrogen peroxide and oxygen gas.',
    'سپرآکسائیڈز (MO₂) پانی سے تعامل کر کے دھاتی ہائیڈرو آکسائیڈ، ہائیڈروجن پرآکسائیڈ اور آکسیجن گیس بناتے ہیں۔ مثلاً KO₂ پانی سے تعامل کر کے پوٹاشیم ہائیڈرو آکسائیڈ، ہائیڈروجن پرآکسائیڈ اور آکسیجن گیس بناتا ہے۔',
    'سوپراکسایډونه (MO₂) له اوبو سره تعامل کوي او فلزي هایدروکسایډ، هایدروجن پراکسایډ او اکسیجن ګاز جوړوي. د بېلګې په توګه، KO₂ له اوبو سره تعامل کوي او پوټاشیم هایدروکسایډ، هایدروجن پراکسایډ او اکسیجن ګاز جوړوي.')
eq('2KO₂(s) + 2H₂O(l) → 2KOH(aq) + H₂O₂(aq) + O₂(g)')
head('ii. Reactions of Oxides with Dilute Acids','ii. آکسائیڈز کے رقیق تیزابوں کے ساتھ تعاملات','ii. له رقیقو تېزابونو سره د اکسایډونو تعاملونه')
add('Oxides of group – IA elements react with dilute acids to produce the respective salts. Oxides of group – IA i.e. normal oxides, peroxides, or super oxides react with dilute acids as follows.',
    'گروپ IA کے عناصر کے آکسائیڈز رقیق تیزابوں سے تعامل کر کے متعلقہ نمک بناتے ہیں۔ گروپ IA کے عام آکسائیڈز، پرآکسائیڈز اور سپرآکسائیڈز رقیق تیزابوں کے ساتھ درج ذیل تعاملات کرتے ہیں۔',
    'د IA ګروپ د عناصرو اکسایډونه له رقیقو تېزابونو سره تعامل کوي او اړوند مالګې جوړوي. د IA ګروپ عادي اکسایډونه، پراکسایډونه او سوپراکسایډونه له رقیقو تېزابونو سره په لاندې ډول تعامل کوي.')
head('Normal oxides','عام آکسائیڈز','عادي اکسایډونه')
add('Normal oxides such as Li₂O and Na₂O react with dilute sulphuric acid (H₂SO₄) and produce the respective salts and water.',
    'عام آکسائیڈز، مثلاً Li₂O اور Na₂O، رقیق سلفیورک ایسڈ (H₂SO₄) سے تعامل کر کے متعلقہ نمک اور پانی بناتے ہیں۔',
    'عادي اکسایډونه، لکه Li₂O او Na₂O، له رقیق سلفوریک اسید (H₂SO₄) سره تعامل کوي او اړوند مالګې او اوبه جوړوي.')
eq('Li₂O(s) + H₂SO₄(aq) → Li₂SO₄(aq) + H₂O(l)')
eq('Na₂O(s) + H₂SO₄(aq) → Na₂SO₄(aq) + H₂O(l)')
head('Peroxides','پرآکسائیڈز','پراکسایډونه')
add('Peroxides, such as Na₂O₂, react with dilute sulphuric acid (H₂SO₄) and produce sodium sulphate and hydrogen peroxide.',
    'پرآکسائیڈز، مثلاً Na₂O₂، رقیق سلفیورک ایسڈ (H₂SO₄) سے تعامل کر کے سوڈیم سلفیٹ اور ہائیڈروجن پرآکسائیڈ بناتے ہیں۔',
    'پراکسایډونه، لکه Na₂O₂، له رقیق سلفوریک اسید (H₂SO₄) سره تعامل کوي او سوډیم سلفېټ او هایدروجن پراکسایډ جوړوي.')
eq('Na₂O₂(s) + H₂SO₄(aq) → Na₂SO₄(aq) + H₂O₂(l)')
head('Super oxides','سپرآکسائیڈز','سوپراکسایډونه')
add('Super oxides such as KO₂, react with dilute sulphuric acid (H₂SO₄) and produce potassium sulphate, hydrogen peroxide and oxygen gas.',
    'سپرآکسائیڈز، مثلاً KO₂، رقیق سلفیورک ایسڈ (H₂SO₄) سے تعامل کر کے پوٹاشیم سلفیٹ، ہائیڈروجن پرآکسائیڈ اور آکسیجن گیس بناتے ہیں۔',
    'سوپراکسایډونه، لکه KO₂، له رقیق سلفوریک اسید (H₂SO₄) سره تعامل کوي او پوټاشیم سلفېټ، هایدروجن پراکسایډ او اکسیجن ګاز جوړوي.')
eq('2KO₂(s) + H₂SO₄(l) → K₂SO₄(aq) + H₂O₂(aq) + O₂(g)')
head('13.2.4 Reactions with Chlorine','13.2.4 کلورین کے ساتھ تعاملات','13.2.4 له کلورین سره تعاملونه')
add('Group – IA elements react vigorously with chlorine to form metal chlorides. These metal chlorides are ionic crystalline solids. For example, sodium burns with an intense orange flame in chlorine in exactly the same way as it does in pure oxygen.',
    'گروپ IA کے عناصر کلورین سے شدت سے تعامل کر کے دھاتی کلورائیڈز بناتے ہیں۔ یہ آئنک قلمی ٹھوس مادے ہیں۔ مثلاً سوڈیم کلورین میں تیز نارنجی شعلے کے ساتھ بالکل اسی طرح جلتا ہے جیسے خالص آکسیجن میں جلتا ہے۔',
    'د IA ګروپ عناصر له کلورین سره په شدت تعامل کوي او فلزي کلورایډونه جوړوي. دا ایوني بلوري جامدونه دي. د بېلګې په توګه، سوډیم په کلورین کې په تېزه نارنجي لمبه، کټ مټ لکه په خالص اکسیجن کې، سوځي.')
record=section('13.10','Group IA oxygen, oxide and chlorine reactions','گروپ IA کے آکسیجن، آکسائیڈ اور کلورین کے تعاملات','د IA ګروپ د اکسیجن، اکسایډونو او کلورین تعاملونه',paras,layout,[],'20–21')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':14,'printedPages':[20,21]}]
if __name__=='__main__':save(14,[record],carry=[{'from':'13.10','to':'13.11','startsAt':'2Na+ Cla\n'}])
