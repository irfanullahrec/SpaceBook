"""PDF18, printed28–29: solubility, thermal stability and beryllium differences."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
eq('Ba(OH)₂(s) —H₂O→ Ba²⁺(aq) + 2OH⁻(aq)')
head('Tidbit','مختصر معلومات','لنډ معلومات')
add('Magnesium hydroxide is used in medicine (in suspension as milk of magnesia) to neutralise excess acid in the stomach and to treat constipation.',
    'میگنیشیم ہائیڈرو آکسائیڈ ادویات میں (ملک آف میگنیشیا کے معلق آمیزے کی صورت میں) معدے کے اضافی تیزاب کو بے اثر کرنے اور قبض کے علاج کے لیے استعمال ہوتا ہے۔',
    'مګنیزیم هایدروکسایډ په درملو کې (د مېلک اف مګنیزیا د تعلیق په بڼه) د معدې د اضافي تېزاب د خنثی کولو او قبض د درملنې لپاره کارول کېږي.')
eq('Mg(OH)₂(aq) + 2HCl(aq) → MgCl₂(aq) + 2H₂O(l)')
add('An aqueous solution of calcium hydroxide is called limewater and can be used as a test-reagent for carbon dioxide.',
    'کیلشیم ہائیڈرو آکسائیڈ کا آبی محلول چونے کا پانی کہلاتا ہے اور کاربن ڈائی آکسائیڈ کی جانچ کے ری ایجنٹ کے طور پر استعمال ہو سکتا ہے۔',
    'د کلسیم هایدروکسایډ اوبلن محلول د چونې اوبه بلل کېږي او د کاربن ډای اکسایډ د ازموینې د ریجنټ په توګه کارېدای شي.')
head('ii. Solubility of the Sulphates','ii. سلفیٹس کی حل پذیری','ii. د سلفېټونو د حل کېدو وړتیا')
add('Group – IIA sulphates become less soluble as we move down the group. BaSO₄ is the least soluble. This simple trend is true provided that hydrated beryllium sulphate is considered, but not for the anhydrous beryllium sulphate. The anhydrous beryllium sulphate, BeSO₄ is insoluble, whereas the hydrated form, (BeSO₄.4H₂O), is soluble. Solubility of magnesium sulphate and calcium sulphate also depends on whether the salt is hydrated or not.',
    'گروپ IIA میں نیچے جانے پر سلفیٹس کی حل پذیری کم ہوتی ہے۔ BaSO₄ سب سے کم حل پذیر ہے۔ یہ سادہ رجحان آب دار بیریلیم سلفیٹ کے لیے درست ہے، مگر بے آب بیریلیم سلفیٹ کے لیے نہیں۔ بے آب بیریلیم سلفیٹ، BeSO₄، غیر حل پذیر، جبکہ آب دار صورت (BeSO₄.4H₂O) حل پذیر ہے۔ میگنیشیم اور کیلشیم سلفیٹ کی حل پذیری بھی نمک کے آب دار یا بے آب ہونے پر منحصر ہے۔',
    'په IIA ګروپ کې ښکته تګ سره د سلفېټونو د حل کېدو وړتیا کمېږي. BaSO₄ تر ټولو لږ حل کېدونکی دی. دا ساده تمایل هغه وخت سم دی چې اوبه لرونکی بېریلیم سلفېټ په پام کې ونیول شي، خو د بې اوبو بېریلیم سلفېټ لپاره نه دی سم. بې اوبو بېریلیم سلفېټ، BeSO₄، نه حل کېږي، خو اوبه لرونکې بڼه (BeSO₄.4H₂O) حل کېږي. د مګنیزیم سلفېټ او کلسیم سلفېټ د حل کېدو وړتیا هم په دې پورې اړه لري چې مالګه اوبه لرونکې ده که نه.')
head('iii. Solubility of the Carbonates','iii. کاربونیٹس کی حل پذیری','iii. د کاربونېټونو د حل کېدو وړتیا')
add('The carbonates become less soluble down the group. All the Group – IIA carbonates are sparingly soluble, while all dissolve in acids. The trend to lower solubility is, however, broken at the bottom of the group.',
    'گروپ میں نیچے جانے پر کاربونیٹس کی حل پذیری کم ہوتی ہے۔ گروپ IIA کے سب کاربونیٹس معمولی حل پذیر ہیں، مگر سب تیزابوں میں حل ہوتے ہیں۔ تاہم گروپ کے نچلے سرے پر گھٹتی حل پذیری کا رجحان ٹوٹ جاتا ہے۔',
    'په ګروپ کې ښکته د کاربونېټونو د حل کېدو وړتیا کمېږي. د IIA ګروپ ټول کاربونېټونه لږ حل کېدونکي دي، خو ټول په تېزابونو کې حل کېږي. خو د ګروپ په لاندې سر کې د کمې حل کېدو وړتیا تمایل ماتېږي.')
add('Barium carbonate is slightly more soluble than strontium carbonate. As we move downward in the group, the energy required to break the lattice of carbonates decreases, because the positive ions get larger. The larger the ions, the more distance there is between ions. Thus, the forces holding these ions together become weaker. This increases the solubility.',
    'بیریم کاربونیٹ اسٹرونشیم کاربونیٹ سے معمولی زیادہ حل پذیر ہے۔ گروپ میں نیچے جانے پر کاربونیٹس کی جالی توڑنے کی توانائی کم ہوتی ہے، کیونکہ مثبت آئن بڑے ہوتے ہیں۔ آئن جتنے بڑے ہوں، ان کے درمیان فاصلہ اتنا زیادہ ہوتا ہے۔ چنانچہ انہیں جوڑنے والی قوتیں کمزور ہوتی ہیں اور حل پذیری بڑھتی ہے۔',
    'بېریم کاربونېټ له سټرونشیم کاربونېټ څخه لږ ډېر حل کېدونکی دی. په ګروپ کې ښکته تګ سره د کاربونېټونو د جالۍ د ماتولو اړینه انرژي کمېږي، ځکه مثبت ایونونه لویېږي. ایونونه چې لوی وي، ترمنځ واټن یې ډېر وي. نو د هغوی سره تړونکې قوې کمزورېږي او د حل کېدو وړتیا زیاتېږي.')
add('On the other hand, when the size of the positive ions become larger downward in the group, the energy released by the ions during hydration also falls because bigger ions are not so strongly attracted to the water molecules. This decreases the solubility of carbonates.',
    'دوسری طرف، گروپ میں نیچے مثبت آئن بڑے ہونے پر آب پوشی کے دوران ان کی خارج کردہ توانائی بھی کم ہوتی ہے، کیونکہ بڑے آئن پانی کے سالموں سے اتنی مضبوط کشش نہیں رکھتے۔ اس سے کاربونیٹس کی حل پذیری کم ہوتی ہے۔',
    'بل خوا، په ګروپ کې ښکته د مثبتو ایونونو د اندازې په لویېدو سره د اوبو د پوښلو پر مهال د ایونونو خوشې شوې انرژي هم کمېږي، ځکه لوی ایونونه د اوبو مالیکولونو ته دومره پیاوړی کشش نه لري. دا د کاربونېټونو د حل کېدو وړتیا کموي.')
add('The effect of decrease in hydration energy is greater than decrease in lattice energy in case of carbonates of IIA down the group. Thus, the solubility of carbonates decreases.',
    'گروپ IIA کے کاربونیٹس میں نیچے جانے پر آب پوشی کی توانائی میں کمی کا اثر جالی کی توانائی میں کمی سے زیادہ ہے۔ اس لیے کاربونیٹس کی حل پذیری کم ہوتی ہے۔',
    'د IIA ګروپ په کاربونېټونو کې ښکته د اوبو د پوښلو د انرژۍ د کمېدو اغېز د جالۍ د انرژۍ له کمېدو ډېر دی. نو د کاربونېټونو د حل کېدو وړتیا کمېږي.')
head('13.3.5 Trend in Thermal Stability of the Nitrates and Carbonates','13.3.5 نائٹریٹس اور کاربونیٹس کے حرارتی استحکام کا رجحان','13.3.5 د نایټرېټونو او کاربونېټونو د حرارتي ثبات تمایل')
head('i. Thermal Stability of the Group – IIA Nitrates','i. گروپ IIA کے نائٹریٹس کا حرارتی استحکام','i. د IIA ګروپ د نایټرېټونو حرارتي ثبات')
add('All the nitrates of this group undergo thermal decomposition to the metal oxide, nitrogen dioxide and oxygen gas. Thermal decomposition means the splitting up of a compound by heating. The following reactions describe the thermal decomposition of the nitrates (Where M = Be, Mg, Ca, Ba and Sr).',
    'اس گروپ کے سب نائٹریٹس حرارتی تحلیل سے دھاتی آکسائیڈ، نائٹروجن ڈائی آکسائیڈ اور آکسیجن گیس بناتے ہیں۔ حرارتی تحلیل کا مطلب گرم کرنے سے کسی مرکب کا ٹوٹنا ہے۔ درج ذیل تعاملات نائٹریٹس کی حرارتی تحلیل بیان کرتے ہیں (جہاں M = Be، Mg، Ca، Ba اور Sr)۔',
    'د دې ګروپ ټول نایټرېټونه په حرارتي تجزیه کې فلزي اکسایډ، نایټروجن ډای اکسایډ او اکسیجن ګاز جوړوي. حرارتي تجزیه د تودولو په وسیله د یوه مرکب ماتېدو ته ویل کېږي. لاندې تعاملونه د نایټرېټونو حرارتي تجزیه بیانوي (چې M = Be، Mg، Ca، Ba او Sr دی).')
eq('2M(NO₃)₂(s) → 2MO(s) + 4NO₂(g) + O₂(g)')
eq('2Ca(NO₃)₂(s) → 2CaO(s) + 4NO₂(g) + O₂(g)')
add('The nitrates become more thermally stable down the group, i.e. they require more heating to decompose.',
    'گروپ میں نیچے نائٹریٹس کا حرارتی استحکام بڑھتا ہے، یعنی تحلیل کے لیے زیادہ گرم کرنا پڑتا ہے۔',
    'په ګروپ کې ښکته د نایټرېټونو حرارتي ثبات زیاتېږي، یعنې د تجزیې لپاره ډېر تودول غواړي.')
head('ii. Thermal Stability of the Group – IIA Carbonates','ii. گروپ IIA کے کاربونیٹس کا حرارتی استحکام','ii. د IIA ګروپ د کاربونېټونو حرارتي ثبات')
add('All the carbonates of this group undergo thermal decomposition, to the metal oxide and carbon dioxide gas.',
    'اس گروپ کے سب کاربونیٹس حرارتی تحلیل سے دھاتی آکسائیڈ اور کاربن ڈائی آکسائیڈ گیس بناتے ہیں۔',
    'د دې ګروپ ټول کاربونېټونه په حرارتي تجزیه کې فلزي اکسایډ او کاربن ډای اکسایډ ګاز جوړوي.')
add('The following reactions describe the decomposition of the carbonate (Where M = Be, Mg, Ca, Ba and Sr).',
    'درج ذیل تعاملات کاربونیٹ کی تحلیل بیان کرتے ہیں (جہاں M = Be، Mg، Ca، Ba اور Sr)۔',
    'لاندې تعاملونه د کاربونېټ تجزیه بیانوي (چې M = Be، Mg، Ca، Ba او Sr دی).')
eq('MCO₃(s) → MO(s) + CO₂(g)')
eq('CaCO₃(s) → CaO(s) + CO₂(g)')
add('The carbonates become more thermally stable down the group, they require more heating to decompose.',
    'گروپ میں نیچے کاربونیٹس کا حرارتی استحکام بڑھتا ہے؛ تحلیل کے لیے زیادہ گرم کرنا پڑتا ہے۔',
    'په ګروپ کې ښکته د کاربونېټونو حرارتي ثبات زیاتېږي؛ د تجزیې لپاره ډېر تودول غواړي.')
head('13.3.6 How Beryllium Differs from other Members of its Group?','13.3.6 بیریلیم اپنے گروپ کے دوسرے ارکان سے کیسے مختلف ہے؟','13.3.6 بېریلیم د خپل ګروپ له نورو غړو څنګه توپیر لري؟')
add('Beryllium differs from other Group – IIA metals in many respects. This is partly due to its small size and partly due to its high electronegativity.',
    'بیریلیم گروپ IIA کی دوسری دھاتوں سے کئی لحاظ سے مختلف ہے۔ اس کی وجہ جزوی طور پر چھوٹی جسامت اور جزوی طور پر زیادہ برقی منفیت ہے۔',
    'بېریلیم د IIA ګروپ له نورو فلزونو په ډېرو برخو کې توپیر لري. دا تر یوه حده د کوچنۍ اندازې او تر یوه حده د لوړ برېښنا منفي توب له امله دی.')
bullets=[
 pair('Beryllium is the lightest of all the Group – IIA metals.','بیریلیم گروپ IIA کی سب دھاتوں میں سب سے ہلکا ہے۔','بېریلیم د IIA ګروپ د ټولو فلزونو تر ټولو سپک دی.'),
 pair('Beryllium has higher melting and boiling point compared to other elements in Group – IIA.','گروپ IIA کے دوسرے عناصر کے مقابلے میں بیریلیم کے پگھلنے اور ابلنے کے درجے زیادہ ہیں۔','د IIA ګروپ د نورو عناصرو په پرتله د بېریلیم د وېلې کېدو او اېشېدو ټکي لوړ دي.'),
 pair('Beryllium unlike other Group – IIA metals is not easily affected by dry air','گروپ IIA کی دوسری دھاتوں کے برخلاف بیریلیم خشک ہوا سے آسانی سے متاثر نہیں ہوتا۔','د IIA ګروپ د نورو فلزونو پر خلاف بېریلیم په وچه هوا په اسانه نه اغېزمنېږي.'),
 pair('Beryllium does not react with water or steam at red heat.','بیریلیم سرخ تپش پر پانی یا بھاپ سے تعامل نہیں کرتا۔','بېریلیم په سره تودوخه کې له اوبو یا بخار سره تعامل نه کوي.'),
 pair('The oxide of beryllium, BeO is amphoteric whereas, other oxides of Group – IIA metals are strong bases.','بیریلیم آکسائیڈ BeO دو خصوصیتی ہے، جبکہ گروپ IIA کی دوسری دھاتوں کے آکسائیڈز مضبوط اساس ہیں۔','د بېریلیم اکسایډ BeO امفوتېریک دی، خو د IIA ګروپ د نورو فلزونو اکسایډونه پیاوړي اساسونه دي.'),
 pair('Oxides, nitrides, chlorides etc. of Group – IIA elements are ionic, while those of beryllium are covalent.','گروپ IIA کے عناصر کے آکسائیڈز، نائٹرائیڈز اور کلورائیڈز وغیرہ آئنک، جبکہ بیریلیم کے اشتراکی ہیں۔','د IIA ګروپ د عناصرو اکسایډونه، نایټرایډونه، کلورایډونه او نور ایوني دي، خو د بېریلیم کووالنټ دي.'),
 pair('Salts of beryllium do not impart any colour during flame test unlike its other family members.','گروپ کے دوسرے ارکان کے برخلاف بیریلیم کے نمک شعلے کے امتحان میں کوئی رنگ نہیں دیتے۔','د کورنۍ د نورو غړو پر خلاف د بېریلیم مالګې د لمبې په ازموینه کې کوم رنګ نه ورکوي.'),
 pair('Beryllium oxide is insoluble in water unlike oxide of other members of its family.','گروپ کے دوسرے ارکان کے آکسائیڈز کے برخلاف بیریلیم آکسائیڈ پانی میں غیر حل پذیر ہے۔','د کورنۍ د نورو غړو د اکسایډونو پر خلاف بېریلیم اکسایډ په اوبو کې نه حل کېږي.'),
 pair('Beryllium does not liberate hydrogen from acids as observed in other Group – IIA metals.','گروپ IIA کی دوسری دھاتوں میں دیکھا جانے والا تیزابوں سے ہائیڈروجن خارج کرنا بیریلیم میں نہیں ہوتا۔','بېریلیم له تېزابونو څخه هایدروجن نه خوشې کوي، لکه د IIA ګروپ په نورو فلزونو کې چې لیدل کېږي.'),
]
start=len(paras);paras.extend(bullets);layout.append({'type':'list','indices':list(range(start,len(paras)))})
record=section('13.14','Group IIA solubility, thermal stability and beryllium','گروپ IIA کی حل پذیری، حرارتی استحکام اور بیریلیم','د IIA ګروپ د حل کېدو وړتیا، حرارتي ثبات او بېریلیم',paras,layout,[],'28–29')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':18,'printedPages':[28,29]}]
record['sourceOpeningContinuation']={'sectionId':'13.13','sourceParagraphIndex':35,'scope':'The first line strongly alkaline. completes the preceding barium hydroxide paragraph, already preserved in that aligned record.'}
issues=[{'id':'chem12-p29-beryllium-acids','printedPage':29,'description':'The last bullet says beryllium does not liberate hydrogen from acids. Printed assertion retained; scientific source-defect review remains pending.'}]
if __name__=='__main__':save(18,[record],issues=issues,carry=[{'from':'13.14','to':'13.15','startsAt':'13.3.6.1 Why is Beryllium Chloride'}])
