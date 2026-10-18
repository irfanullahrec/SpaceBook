"""PDF24 printed40–41: halides, oxidizing/reducing agents and acid strength."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(v):add(v,v,v,'equation')
head('13.5.1.5.2 Bond Enthalpies in Hydrogen Halides','13.5.1.5.2 ہائیڈروجن ہیلائیڈز میں بندوں کی اینتھالپیاں','13.5.1.5.2 په هایدروجن هالایډونو کې د تړونونو انتالپۍ')
add('Down the group the halogen atoms get bigger, the bonding pair of electrons get more and more distant from the nucleus, the attraction is less and the bond becomes weaker. So the bond enthalpies of hydrogen halides decreases down the group. The bond enthalpies are very important in the thermal stability of hydrogen halides.',
    'گروپ میں نیچے ہیلوجن ایٹم بڑے ہوتے ہیں، بند بنانے والا الیکٹرون جوڑا مرکزے سے مزید دور ہوتا ہے، کشش کم ہوتی ہے اور بند کمزور ہوتا ہے۔ اس لیے ہائیڈروجن ہیلائیڈز کے بندوں کی اینتھالپیاں گروپ میں نیچے کم ہوتی ہیں۔ بندوں کی اینتھالپیاں ہائیڈروجن ہیلائیڈز کے حرارتی استحکام میں بہت اہم ہیں۔',
    'په ګروپ کې ښکته د هالوجن اټومونه لویېږي، د تړون جوړوونکو الکترونونو جوړه له هستې څخه لا لیرې کېږي، کشش کمېږي او تړون کمزوری کېږي. نو د هایدروجن هالایډونو د تړونونو انتالپۍ په ګروپ کې ښکته کمېږي. د تړونونو انتالپۍ د هایدروجن هالایډونو په حرارتي ثبات کې ډېرې مهمې دي.')
add('H–F and H–Cl are stable to heat and they do not decompose easily. H–Br decomposes slightly into hydrogen and bromine on heating and H–I decomposes to an even greater extent. As the bonds get weaker, they are more easily broken. Bond enthalpies of halides are given below.',
    'H–F اور H–Cl حرارت کے مقابل مستحکم ہیں اور آسانی سے تحلیل نہیں ہوتے۔ H–Br گرم کرنے پر معمولی حد تک ہائیڈروجن اور برومین میں تحلیل ہوتا ہے، جبکہ H–I اس سے زیادہ حد تک تحلیل ہوتا ہے۔ بند کمزور ہونے پر زیادہ آسانی سے ٹوٹتے ہیں۔ ہیلائیڈز کے بندوں کی اینتھالپیاں ذیل میں دی گئی ہیں۔',
    'H–F او H–Cl د تودوخې پر وړاندې ثابت دي او په اسانه نه تجزیه کېږي. H–Br په تودولو لږ په هایدروجن او برومین تجزیه کېږي او H–I تر دې هم ډېره تجزیه کېږي. تړونونه چې کمزوري شي، په ډېره اسانۍ ماتېږي. د هالایډونو د تړونونو انتالپۍ لاندې ورکړل شوې دي.')
add('Table 13.30 Bond Enthalpies in Hydrogen Halides','جدول 13.30 ہائیڈروجن ہیلائیڈز میں بندوں کی اینتھالپیاں','جدول 13.30 په هایدروجن هالایډونو کې د تړونونو انتالپۍ')
h=['Hydrogen Halide','H–F','H–Cl','H–Br','H–I'];v=['+568.2','+431.9','+366.1','+298.3']
blocks.append({'id':'chem12-table-13-30','headers':h,'rows':[['Bond enthalpy (kJ/mol)']+v],'translations':[{'language':'اردو','headers':['ہائیڈروجن ہیلائیڈ']+h[1:],'rows':[['بند کی اینتھالپی (kJ/mol)']+v]},{'language':'پښتو','headers':['هایدروجن هالایډ']+h[1:],'rows':[['د تړون انتالپي (kJ/mol)']+v]}]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
head('13.5.2 Strength of Halogens as Oxidizing Agents','13.5.2 بطور تکسیدی عامل ہیلوجنز کی طاقت','13.5.2 د اکسیدوونکو عواملو په توګه د هالوجنونو ځواک')
add('An oxidizing agent is a substance that removes electrons from other substances during a redox reaction.',
    'تکسیدی عامل ایسا مادہ ہے جو ریڈاکس تعامل کے دوران دوسرے مادوں سے الیکٹرون چھینتا ہے۔',
    'اکسیدوونکی عامل هغه ماده ده چې د رېډاکس تعامل پر مهال له نورو مادو څخه الکترونونه لرې کوي.')
add('The oxidizing agent takes these electrons for itself, thus gaining electrons and getting reduced. An oxidizing agent is thus an electron acceptor. The halogen accepts electron during the reaction and acts as oxidizing agent.',
    'تکسیدی عامل یہ الیکٹرون خود لے لیتا ہے، یوں الیکٹرون حاصل کر کے تخفیف پاتا ہے۔ اس طرح تکسیدی عامل الیکٹرون قبول کرنے والا ہے۔ ہیلوجن تعامل کے دوران الیکٹرون قبول کرتا ہے اور تکسیدی عامل کے طور پر عمل کرتا ہے۔',
    'اکسیدوونکی عامل دا الکترونونه ځان ته اخلي، نو الکترونونه ترلاسه کوي او ارجاع کېږي. په دې توګه اکسیدوونکی عامل الکترون منونکی دی. هالوجن د تعامل پر مهال الکترون مني او د اکسیدوونکي عامل په توګه عمل کوي.')
eq('2Na(s) + Cl₂(g) → 2Na⁺Cl⁻(s)')
add('For example, fluorine is a powerful oxidizing agent. Fluorine is the most electronegative, so forming F⁻ is the most energetically favourable of the reductions. This makes fluorine the most powerful oxidizing agent.',
    'مثلاً فلورین طاقت ور تکسیدی عامل ہے۔ فلورین سب سے زیادہ برقی منفی ہے، اس لیے F⁻ بننا تخفیفی عملوں میں توانائی کے لحاظ سے سب سے زیادہ موافق ہے۔ اس سے فلورین سب سے طاقت ور تکسیدی عامل بنتا ہے۔',
    'د بېلګې په توګه فلورین پیاوړی اکسیدوونکی عامل دی. فلورین تر ټولو ډېر برېښنا منفي دی، نو د F⁻ جوړېدل د ارجاع له بهیرونو څخه د انرژۍ له پلوه تر ټولو مساعد دي. دا فلورین تر ټولو پیاوړی اکسیدوونکی عامل ګرځوي.')
add('Chlorine has the ability to take electrons from bromide ions and oxidize/change them to bromine in potassium bromide solution.',
    'کلورین پوٹاشیم برومائیڈ کے محلول میں برومائیڈ آئنوں سے الیکٹرون لے کر انہیں تکسید کر کے برومین میں بدل سکتا ہے۔',
    'کلورین د پوټاشیم برومایډ په محلول کې له برومایډ ایونونو الکترونونه اخیستلای شي او هغوی اکسیدوي او په برومین یې بدلوي.')
eq('Cl₂(g) + 2Br⁻(aq) → 2Cl⁻(aq) + Br₂(l)')
add('The bromine appears as an orange solution.','برومین نارنجی محلول کی صورت میں ظاہر ہوتا ہے۔','برومین د نارنجي محلول په بڼه څرګندېږي.')
add('Chlorine can also oxidize iodide ions to iodine in potassium iodide solution.',
    'کلورین پوٹاشیم آئیوڈائیڈ کے محلول میں آئیوڈائیڈ آئنوں کو بھی تکسید کر کے آئیوڈین بنا سکتا ہے۔',
    'کلورین د پوټاشیم ایوډایډ په محلول کې ایوډایډ ایونونه هم اکسیدولای شي او ایوډین جوړوي.')
eq('Cl₂(g) + 2I⁻(aq) → 2Cl⁻(aq) + I₂(s)')
add('The iodine appears either as a red solution or as a dark grey precipitate if the chlorine is in excess.',
    'آئیوڈین سرخ محلول کی صورت میں، یا کلورین کی زیادتی پر گہرے سرمئی رسوب کی صورت میں ظاہر ہوتا ہے۔',
    'ایوډین د سور محلول په بڼه یا، که کلورین زیات وي، د تیاره خړ رسوب په بڼه څرګندېږي.')
add('Bromine and iodine cannot regain those electrons from the chloride ions formed. This indicates that chlorine is more powerful oxidizing agent than either bromine or iodine. In short, oxidizing ability decreases down the group.',
    'برومین اور آئیوڈین بننے والے کلورائیڈ آئنوں سے وہ الیکٹرون واپس نہیں لے سکتے۔ اس سے ظاہر ہوتا ہے کہ کلورین، برومین یا آئیوڈین سے زیادہ طاقت ور تکسیدی عامل ہے۔ مختصراً، گروپ میں نیچے تکسیدی صلاحیت کم ہوتی ہے۔',
    'برومین او ایوډین له جوړو شویو کلورایډ ایونونو څخه هغه الکترونونه بېرته نه شي اخیستلای. دا ښيي چې کلورین له برومین یا ایوډین څخه پیاوړی اکسیدوونکی عامل دی. په لنډه توګه، په ګروپ کې ښکته د اکسیدولو وړتیا کمېږي.')
add('The order of decreasing power of halogens as oxidizing agent is','بطور تکسیدی عامل ہیلوجنز کی گھٹتی طاقت کی ترتیب یہ ہے:','د اکسیدوونکي عامل په توګه د هالوجنونو د کمېدونکي ځواک ترتیب دا دی:');eq('F₂ > Cl₂ > Br₂ > I₂')
head('13.5.3 The Acidity of Hydrogen Halides','13.5.3 ہائیڈروجن ہیلائیڈز کی تیزابیت','13.5.3 د هایدروجن هالایډونو تېزابیت')
add('According to Bronsted and Lowery, an acid is a proton donor. Hydrogen chloride gas is soluble in water; its solvated form is hydrochloric acid. HCl is soluble in water and produces H₃O⁺ and Cl⁻ ions.',
    'برونسٹڈ اور لووری کے مطابق تیزاب پروٹون دینے والا ہے۔ ہائیڈروجن کلورائیڈ گیس پانی میں حل پذیر ہے؛ اس کی محلول پذیر صورت ہائیڈروکلورک تیزاب ہے۔ HCl پانی میں حل ہو کر H₃O⁺ اور Cl⁻ آئن بناتا ہے۔',
    'د برونسټډ او لووري له مخې تېزاب پروټون ورکوونکی دی. هایدروجن کلورایډ ګاز په اوبو کې حل کېږي؛ محلول شوې بڼه یې هایدروکلوریک تېزاب دی. HCl په اوبو کې حل کېږي او H₃O⁺ او Cl⁻ ایونونه جوړوي.')
eq('HCl(aq) + H₂O(l) → H₃O⁺(aq) + Cl⁻(aq)')
add('This reaction shows that HCl completely dissociates in water. Hydrochloric acid is therefore a strong acid. An acid is strong if it is fully ionized in solution.',
    'یہ تعامل دکھاتا ہے کہ HCl پانی میں مکمل طور پر الگ آئنوں میں بٹتا ہے۔ اس لیے ہائیڈروکلورک تیزاب مضبوط تیزاب ہے۔ تیزاب مضبوط ہوتا ہے اگر محلول میں مکمل آئنائز ہو۔',
    'دا تعامل ښيي چې HCl په اوبو کې په بشپړ ډول په ایونونو جلا کېږي. نو هایدروکلوریک تېزاب پیاوړی تېزاب دی. تېزاب هغه وخت پیاوړی دی چې په محلول کې په بشپړ ډول ایوني شي.')
add('Hydrogen bromide and hydrogen iodide dissolve in (and react with) water and completely dissociate in water. Therefore, both HBr and HI are strong acids.',
    'ہائیڈروجن برومائیڈ اور ہائیڈروجن آئیوڈائیڈ پانی میں حل ہوتے اور اس سے تعامل کرتے ہیں، اور پانی میں مکمل طور پر الگ آئنوں میں بٹتے ہیں۔ اس لیے HBr اور HI دونوں مضبوط تیزاب ہیں۔',
    'هایدروجن برومایډ او هایدروجن ایوډایډ په اوبو کې حل کېږي او ورسره تعامل کوي او په اوبو کې په بشپړ ډول په ایونونو جلا کېږي. نو HBr او HI دواړه پیاوړي تېزابونه دي.')
add('Hydrofluoric acid is an exception to strong halogen acids. Although hydrogen fluoride dissolves in water, but hydrofluoric acid is only a weak acid. In strength, it is similar to organic acids like methanoic acid.',
    'ہائیڈروفلورک تیزاب مضبوط ہیلوجن تیزابوں سے مستثنیٰ ہے۔ اگرچہ ہائیڈروجن فلورائیڈ پانی میں حل ہوتا ہے، مگر ہائیڈروفلورک تیزاب صرف کمزور تیزاب ہے۔ طاقت میں یہ میتھینوئک تیزاب جیسے نامیاتی تیزابوں سے ملتا جلتا ہے۔',
    'هایدروفلوریک تېزاب د پیاوړو هالوجني تېزابونو استثنا دی. که څه هم هایدروجن فلورایډ په اوبو کې حل کېږي، خو هایدروفلوریک تېزاب یوازې کمزوری تېزاب دی. په ځواک کې د مېتانویک تېزاب په څېر عضوي تېزابونو ته ورته دی.')
head('13.5.4 Halide Ions as Reducing Agents and Trends in Reducing Strength Ability of Halide Ions','13.5.4 ہیلائیڈ آئن بطور تخفیفی عامل اور ان کی تخفیفی طاقت کے رجحانات','13.5.4 هالایډ ایونونه د ارجاع کوونکو عواملو په توګه او د هغوی د ارجاع ځواک تمایلات')
add('The trend in reducing power of the halide ions is opposite to the trend in oxidizing power of the halogen elements. This means that the iodide ion is the best reducing agent.',
    'ہیلائیڈ آئنوں کی تخفیفی طاقت کا رجحان ہیلوجن عناصر کی تکسیدی طاقت کے رجحان کے الٹ ہے۔ اس کا مطلب ہے کہ آئیوڈائیڈ آئن بہترین تخفیفی عامل ہے۔',
    'د هالایډ ایونونو د ارجاع ځواک تمایل د هالوجني عناصرو د اکسیدولو ځواک د تمایل مخالف دی. دا مانا لري چې ایوډایډ ایون تر ټولو ښه ارجاع کوونکی عامل دی.')
add('The more reactive halogen will displace the ions of a less reactive halogen from its solution. This is a redox reaction with the halogen acting as an oxidizing agent and the halide ion as a reducing agent. Chlorine oxidizes iodide ions to iodine and is itself reduced to chloride ions.',
    'زیادہ تعامل پذیر ہیلوجن کم تعامل پذیر ہیلوجن کے آئنوں کو اس کے محلول سے ہٹا دے گا۔ یہ ریڈاکس تعامل ہے، جس میں ہیلوجن تکسیدی عامل اور ہیلائیڈ آئن تخفیفی عامل کے طور پر عمل کرتا ہے۔ کلورین آئیوڈائیڈ آئنوں کو آئیوڈین میں تکسید کرتا ہے اور خود کلورائیڈ آئنوں میں تخفیف پاتا ہے۔',
    'ډېر تعامل کوونکی هالوجن د لږ تعامل کوونکي هالوجن ایونونه له خپل محلول څخه بې ځایه کوي. دا رېډاکس تعامل دی، چې هالوجن د اکسیدوونکي عامل او هالایډ ایون د ارجاع کوونکي عامل په توګه عمل کوي. کلورین ایوډایډ ایونونه په ایوډین اکسیدوي او پخپله په کلورایډ ایونونو ارجاع کېږي.')
eq('2I⁻(aq) + Cl₂(g) → 2Cl⁻(aq) + I₂(s)')
add('Besides this, Br⁻ reduces sulphuric acid (H₂SO₄) to SO₂, which results in a decrease of oxidation state of sulphur from ‘+6’ in H₂SO₄ to ‘+4’ in SO₂.',
    'اس کے علاوہ Br⁻، سلفیورک تیزاب (H₂SO₄) کو SO₂ میں تخفیف کرتا ہے، جس سے سلفر کی تکسیدی حالت H₂SO₄ میں +6 سے SO₂ میں +4 تک کم ہوتی ہے۔',
    'سربېره پر دې، Br⁻ سلفوریک تېزاب (H₂SO₄) په SO₂ ارجاع کوي، چې د سلفر د اکسیدېشن حالت په H₂SO₄ کې له +6 څخه په SO₂ کې +4 ته کموي.')
eq('H₂SO₄(aq) + 2H⁺(aq) + 2Br⁻(aq) → Br₂(l) + SO₂(aq) + 2H₂O(l)')
add('Iodide (I⁻) is stronger reducing agent than bromide ion (Br⁻), as it reduces H₂SO₄ to H₂S in which oxidation state of ‘S’ changes from +6 to −2.',
    'آئیوڈائیڈ (I⁻)، برومائیڈ آئن (Br⁻) سے زیادہ مضبوط تخفیفی عامل ہے، کیونکہ یہ H₂SO₄ کو H₂S میں تخفیف کرتا ہے، جس میں S کی تکسیدی حالت +6 سے −2 ہو جاتی ہے۔',
    'ایوډایډ (I⁻) له برومایډ ایون (Br⁻) څخه پیاوړی ارجاع کوونکی عامل دی، ځکه H₂SO₄ په H₂S ارجاع کوي، چې پکې د S د اکسیدېشن حالت له +6 څخه −2 ته بدلېږي.')
eq('H₂SO₄(aq) + 8H⁺(aq) + 2I⁻(aq) → I₂(s) + H₂S(g) + 4H₂O(l)')
add('The reducing agents, halides show the following trend in reducing strength:','تخفیفی عوامل، ہیلائیڈز، تخفیفی طاقت میں درج ذیل رجحان دکھاتے ہیں:','ارجاع کوونکي عوامل، هالایډونه، د ارجاع په ځواک کې لاندې تمایل ښيي:');eq('I⁻ > Br⁻ > Cl⁻ > F⁻')
record=section('13.20','Hydrogen halides and halogen redox reactions','ہائیڈروجن ہیلائیڈز اور ہیلوجنز کے ریڈاکس تعاملات','هایدروجن هالایډونه او د هالوجنونو رېډاکس تعاملونه',paras,layout,blocks,'40–41');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':24,'printedPages':[40,41]}]
issues=[{'id':'chem12-p41-iodide-redox-coefficient','printedPage':41,'description':'Printed H2SO4 reduction equation uses2I− and I2 with8H+; charge and electron balance are inconsistent. Exact printed coefficients retained, not silently changed.'}]
if __name__=='__main__':save(24,[record],carry=[{'from':'13.20','to':'13.21','startsAt':'Society, Technology And Science'}],issues=issues)
