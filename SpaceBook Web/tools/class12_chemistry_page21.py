"""PDF21 printed34–35: GroupIVA oxides and CO2 orbital figures."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_co2_diagrams import block
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(v):add(v,v,v,'equation')
def visual(n):
    b=block(n);blocks.append(b);layout.append({'type':'visual','blockId':b['id']})
eq('SiCl₄(l) + 2H₂O(l) → SiO₂(s) + 4HCl(g)')
eq('PbCl₄(l) + 2H₂O(l) → PbO₂(s) + 4HCl(g)')
add('PbCl₂ is ionic in nature and sparingly soluble in cold water but more soluble in hot water. The solubility in water involves breakup of the ionic lattice and the hydration of Pb²⁺ and Cl⁻ ions.',
    'PbCl₂ آئنک نوعیت رکھتا ہے اور ٹھنڈے پانی میں معمولی حل پذیر، مگر گرم پانی میں زیادہ حل پذیر ہے۔ پانی میں حل ہونے میں آئنک جالی کا ٹوٹنا اور Pb²⁺ اور Cl⁻ آئنوں کی آب پوشی شامل ہے۔',
    'PbCl₂ ایوني ماهیت لري او په سړو اوبو کې لږ حل کېږي، خو په ګرمو اوبو کې ډېر حل کېږي. په اوبو کې حل کېدل د ایوني جالۍ ماتېدل او د Pb²⁺ او Cl⁻ ایونونو د اوبو پوښل رانغاړي.')
eq('PbCl₂(s) —H₂O(l)→ Pb²⁺(aq) + 2Cl⁻(aq)')
head('13.4.6 Oxides','13.4.6 آکسائیڈز','13.4.6 اکسایډونه')
add('Group–IVA elements form two types of oxides i.e. monoxide and dioxide. This is because the elements have two possible oxidation states, +2 and +4.',
    'گروپ IVA کے عناصر دو قسم کے آکسائیڈز یعنی مونو آکسائیڈ اور ڈائی آکسائیڈ بناتے ہیں۔ اس کی وجہ ان عناصر کی دو ممکنہ تکسیدی حالتیں +2 اور +4 ہیں۔',
    'د IVA ګروپ عناصر دوه ډوله اکسایډونه، یعنې مونو اکسایډ او ډای اکسایډ جوړوي. دا ځکه چې دا عناصر دوه ممکن د اکسیدېشن حالتونه، +2 او +4 لري.')
add('Monoxide, include carbon monoxide (CO), silicon monoxide (SiO), germanium monoxide (GeO), tin monoxide (SnO) and lead oxide (PbO), while the dioxide includes carbon dioxide (CO₂), silicon dioxide (SiO₂), germanium dioxide (GeO₂), tin dioxide (SnO₂) and lead dioxide (PbO₂).',
    'مونو آکسائیڈز میں کاربن مونو آکسائیڈ (CO)، سلیکان مونو آکسائیڈ (SiO)، جرمینیم مونو آکسائیڈ (GeO)، ٹن مونو آکسائیڈ (SnO) اور سیسہ آکسائیڈ (PbO) شامل ہیں، جبکہ ڈائی آکسائیڈز میں کاربن ڈائی آکسائیڈ (CO₂)، سلیکان ڈائی آکسائیڈ (SiO₂)، جرمینیم ڈائی آکسائیڈ (GeO₂)، ٹن ڈائی آکسائیڈ (SnO₂) اور سیسہ ڈائی آکسائیڈ (PbO₂) شامل ہیں۔',
    'مونو اکسایډونه کاربن مونو اکسایډ (CO)، سیلیکان مونو اکسایډ (SiO)، جرمانیم مونو اکسایډ (GeO)، ټین مونو اکسایډ (SnO) او سرب اکسایډ (PbO) رانغاړي، خو ډای اکسایډونه کاربن ډای اکسایډ (CO₂)، سیلیکان ډای اکسایډ (SiO₂)، جرمانیم ډای اکسایډ (GeO₂)، ټین ډای اکسایډ (SnO₂) او سرب ډای اکسایډ (PbO₂) رانغاړي.')
add('The oxide of carbon and silicon are non-metal oxides and are covalent in nature, whereas, oxides of germanium, tin and lead are metal oxide and are ionic in nature.',
    'کاربن اور سلیکان کے آکسائیڈز غیر دھاتی آکسائیڈز اور اشتراکی نوعیت کے ہیں، جبکہ جرمینیم، ٹن اور سیسے کے آکسائیڈز دھاتی آکسائیڈز اور آئنک نوعیت کے ہیں۔',
    'د کاربن او سیلیکان اکسایډونه نافلزي اکسایډونه دي او کووالنټ ماهیت لري، خو د جرمانیم، ټین او سرب اکسایډونه فلزي اکسایډونه دي او ایوني ماهیت لري.')
head('13.4.6.1 Structure of Carbon Dioxide and Silicon Dioxide','13.4.6.1 کاربن ڈائی آکسائیڈ اور سلیکان ڈائی آکسائیڈ کی ساخت','13.4.6.1 د کاربن ډای اکسایډ او سیلیکان ډای اکسایډ جوړښت')
add('Carbon and silicon have four electrons in their valence shells. They are both tetravalent. It means that the structure of CO₂ and SiO₂ should be similar. But the structure of SiO₂ and CO₂ are quite different from each other. The physical properties of carbon dioxide differ significantly from those of silicon dioxide. Carbon dioxide is a gas whereas silicon dioxide is a hard, high-melting point solid. The other oxides of Group – IV are also solids.',
    'کاربن اور سلیکان کے ظرفی خولوں میں چار الیکٹرون ہیں۔ دونوں چار ظرفی ہیں۔ اس کا مطلب ہے کہ CO₂ اور SiO₂ کی ساختیں ملتی جلتی ہونی چاہئیں۔ مگر SiO₂ اور CO₂ کی ساختیں ایک دوسرے سے کافی مختلف ہیں۔ کاربن ڈائی آکسائیڈ کی طبعی خصوصیات سلیکان ڈائی آکسائیڈ سے نمایاں طور پر مختلف ہیں۔ کاربن ڈائی آکسائیڈ گیس ہے، جبکہ سلیکان ڈائی آکسائیڈ سخت اور بلند نقطۂ پگھلاؤ والا ٹھوس ہے۔ گروپ IV کے دوسرے آکسائیڈز بھی ٹھوس ہیں۔',
    'کاربن او سیلیکان په خپلو ظرفي پوښونو کې څلور الکترونونه لري. دواړه څلور ظرفي دي. دا مانا لري چې د CO₂ او SiO₂ جوړښتونه باید ورته وي. خو د SiO₂ او CO₂ جوړښتونه له یو بل څخه ډېر توپیر لري. د کاربن ډای اکسایډ فزیکي ځانګړنې د سیلیکان ډای اکسایډ له ځانګړنو څخه څرګند توپیر لري. کاربن ډای اکسایډ ګاز دی، خو سیلیکان ډای اکسایډ کلک جامد دی چې د وېلې کېدو لوړ ټکی لري. د IV ګروپ نور اکسایډونه هم جامد دي.')
head('i. Structure of Carbon dioxide','i. کاربن ڈائی آکسائیڈ کی ساخت','i. د کاربن ډای اکسایډ جوړښت')
add('In CO₂ molecule, one electron from 2s orbital moves to 2p level. The hybridization in CO₂ is sp, two sp hybrid orbitals are arranged in linear form with an angle of 180° as shown in Figure 13.4.',
    'CO₂ کے سالمے میں ایک الیکٹرون 2s آربیٹل سے 2p سطح میں منتقل ہوتا ہے۔ CO₂ میں ہائبرڈائزیشن sp ہے؛ دو sp ہائبرڈ آربیٹلز 180° زاویے سے خطی صورت میں ترتیب پاتے ہیں، جیسا کہ شکل 13.4 میں دکھایا گیا ہے۔',
    'په CO₂ مالیکول کې یو الکترون له 2s اوربیټل څخه 2p کچې ته ځي. په CO₂ کې هایبرډایزېشن sp دی؛ دوه sp هایبرډ اوربیټلونه په خطي بڼه د 180° زاویې سره ترتیب شوي دي، لکه په شکل 13.4 کې چې ښودل شوي.')
visual(4)
add('Figure 13.4 sp hybridization.','شکل 13.4 sp ہائبرڈائزیشن۔','شکل 13.4 sp هایبرډایزېشن.')
add('These sp hybrid orbitals are used to form the σ-bond between the carbon and the oxygen atoms. The two 2p orbitals remain unhybridized on the sp hybridized carbon. These are used to form the π-bond with the oxygen atoms.',
    'یہ sp ہائبرڈ آربیٹلز کاربن اور آکسیجن ایٹموں کے درمیان σ بند بنانے کے لیے استعمال ہوتے ہیں۔ sp ہائبرڈائزڈ کاربن کے دو 2p آربیٹلز غیر ہائبرڈ رہتے ہیں۔ یہ آکسیجن ایٹموں کے ساتھ π بند بنانے کے لیے استعمال ہوتے ہیں۔',
    'دا sp هایبرډ اوربیټلونه د کاربن او اکسیجن د اټومونو ترمنځ د σ تړون د جوړولو لپاره کارېږي. په sp هایبرډ شوي کاربن کې دوه 2p اوربیټلونه ناهایبرډ پاتې کېږي. دا د اکسیجن له اټومونو سره د π تړون د جوړولو لپاره کارېږي.')
visual(5)
add('Figure 13.5 The hybrid orbitals of carbon and oxygen.','شکل 13.5 کاربن اور آکسیجن کے ہائبرڈ آربیٹلز۔','شکل 13.5 د کاربن او اکسیجن هایبرډ اوربیټلونه.')
add('In CO₂ molecule, each oxygen atom is sp² hybridized. One ‘p’ orbital on each oxygen atom remains unchanged and is used for the π-bond formation with the carbon atom. The sp orbitals on carbon atom form σ-bonds with the sp² orbitals on the two oxygen atoms as shown in Figure 13.6. The remaining sp² orbitals on the oxygen atoms hold lone pairs. The π-bonds between the carbon atom and each oxygen atom are formed by the overlap of parallel 2p orbitals. The sp hybridized carbon atom has two unhybridized p orbitals (Figure 13.6).',
    'CO₂ کے سالمے میں ہر آکسیجن ایٹم sp² ہائبرڈائزڈ ہے۔ ہر آکسیجن ایٹم کا ایک p آربیٹل غیر تبدیل شدہ رہتا ہے اور کاربن ایٹم کے ساتھ π بند بنانے میں استعمال ہوتا ہے۔ کاربن ایٹم کے sp آربیٹلز دونوں آکسیجن ایٹموں کے sp² آربیٹلز کے ساتھ σ بند بناتے ہیں، جیسا کہ شکل 13.6 میں دکھایا گیا ہے۔ آکسیجن ایٹموں کے باقی sp² آربیٹلز میں تنہا جوڑے ہوتے ہیں۔ کاربن اور ہر آکسیجن ایٹم کے درمیان π بند متوازی 2p آربیٹلز کے تداخل سے بنتے ہیں۔ sp ہائبرڈائزڈ کاربن ایٹم کے دو غیر ہائبرڈ p آربیٹلز ہیں (شکل 13.6)۔',
    'په CO₂ مالیکول کې د اکسیجن هر اټوم sp² هایبرډ شوی دی. د هر اکسیجن اټوم یو p اوربیټل نه بدلېږي او له کاربن اټوم سره د π تړون د جوړولو لپاره کارېږي. د کاربن اټوم sp اوربیټلونه د دواړو اکسیجن اټومونو له sp² اوربیټلونو سره σ تړونونه جوړوي، لکه په شکل 13.6 کې چې ښودل شوي. د اکسیجن د اټومونو پاتې sp² اوربیټلونه یوازینۍ جوړې لري. د کاربن اټوم او هر اکسیجن اټوم ترمنځ π تړونونه د موازي 2p اوربیټلونو په تداخل جوړېږي. sp هایبرډ شوی کاربن اټوم دوه ناهایبرډ p اوربیټلونه لري (شکل 13.6).')
visual(6)
add('Figure 13.6 Each of these p orbitals is used to form a π-bond with an oxygen atom.',
    'شکل 13.6 ان p آربیٹلز میں سے ہر ایک آکسیجن ایٹم کے ساتھ π بند بنانے میں استعمال ہوتا ہے۔',
    'شکل 13.6 له دې p اوربیټلونو څخه هر یو د اکسیجن له یوه اټوم سره د π تړون په جوړولو کې کارېږي.')
visual(7)
add('Figure 13.7 The total bonding picture for the CO₂ molecule.','شکل 13.7 CO₂ کے سالمے میں بندوں کی مکمل تصویر۔','شکل 13.7 د CO₂ مالیکول د تړونونو بشپړ انځور.')
record=section('13.17','Group IVA oxides and carbon dioxide bonding','گروپ IVA کے آکسائیڈز اور کاربن ڈائی آکسائیڈ کے بند','د IVA ګروپ اکسایډونه او د کاربن ډای اکسایډ تړونونه',paras,layout,blocks,'34–35')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':21,'printedPages':[34,35]}]
record['sourceContinuesOnPdfPage']=22
if __name__=='__main__':save(21,[record],carry=[{'from':'13.17','to':'13.18','startsAt':'ii.\nThe Structure of Silicon dioxide'}])
