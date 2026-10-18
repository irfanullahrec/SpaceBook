"""PDF22 printed36–37, source-preserving oxides and halogen introduction."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(v):add(v,v,v,'equation')
head('ii. The Structure of Silicon dioxide','ii. سلیکان ڈائی آکسائیڈ کی ساخت','ii. د سیلیکان ډای اکسایډ جوړښت')
add('Silicon atoms are bigger than carbon atoms, which mean that silicon – oxygen bond will be long as compared to carbon–oxygen bond. The ‘p’ orbital on the silicon and the oxygen are not quite close enough together to allow enough side wise overlap to give us a stable ‘π’ bond. Thus, silicon oxygen bond is a single bond –',
    'سلیکان ایٹم کاربن ایٹموں سے بڑے ہیں، جس کا مطلب ہے کہ سلیکان–آکسیجن بند، کاربن–آکسیجن بند کی نسبت لمبا ہوگا۔ سلیکان اور آکسیجن کے p آربیٹلز ایک دوسرے کے اتنے قریب نہیں کہ کافی پہلوئی تداخل سے مستحکم π بند بن سکے۔ اس لیے سلیکان–آکسیجن بند ایک یک گانہ بند ہے –',
    'د سیلیکان اټومونه د کاربن له اټومونو لوی دي، یعنې د سیلیکان–اکسیجن تړون به د کاربن–اکسیجن د تړون په پرتله اوږد وي. د سیلیکان او اکسیجن p اوربیټلونه دومره نږدې نه دي چې په کافي اړخیز تداخل یو ثابت π تړون جوړ کړي. نو د سیلیکان–اکسیجن تړون یو واحد تړون دی –')
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 270" role="img" aria-label="Silicon dioxide network"><rect width="360" height="270" fill="white"/>']
for row in range(3):
 for col in range(3):
  x=80+col*100;y=55+row*80
  svg.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" font-size="18">Si</text>')
  for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
   svg.append(f'<path d="M{x+dx*15} {y+dy*13}L{x+dx*36} {y+dy*27}" stroke="#111"/>')
  if col<2:svg.append(f'<text x="{x+50}" y="{y+6}" text-anchor="middle" font-size="18">O</text>')
  if row<2:svg.append(f'<text x="{x}" y="{y+46}" text-anchor="middle" font-size="18">O</text>')
svg.append('</svg>');svg=''.join(svg)
blocks.append({'id':'chem12-figure-13-8','svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('Figure 13.8 Structure of Silicon dioxide.','شکل 13.8 سلیکان ڈائی آکسائیڈ کی ساخت۔','شکل 13.8 د سیلیکان ډای اکسایډ جوړښت.')
add('The SiO₂ molecule is a giant covalent structure in which each silicon atom is bonded to four oxygen atoms through single covalent bonds whereas each oxygen atom is bonded to two silicon atoms.',
    'SiO₂ کا سالمہ ایک دیوہیکل اشتراکی ساخت ہے، جس میں ہر سلیکان ایٹم یک گانہ اشتراکی بندوں سے چار آکسیجن ایٹموں کے ساتھ، جبکہ ہر آکسیجن ایٹم دو سلیکان ایٹموں کے ساتھ بند بناتا ہے۔',
    'د SiO₂ مالیکول یو لوی کووالنټ جوړښت دی، چې هر سیلیکان اټوم د واحدو کووالنټ تړونونو په وسیله له څلورو اکسیجن اټومونو سره تړلی دی، خو هر اکسیجن اټوم له دوو سیلیکان اټومونو سره تړلی دی.')
head('13.4.6.2 Acid Base Behaviour of Group IV Oxides','13.4.6.2 گروپ IV کے آکسائیڈز کا تیزابی اور اساسی رویہ','13.4.6.2 د IV ګروپ د اکسایډونو تېزابي او اساسي چلند')
add('The oxides of group – IVA elements are acidic, but their acidity decreases as we move down the group. Acid – base reactions of these oxides are given below.',
    'گروپ IVA کے عناصر کے آکسائیڈز تیزابی ہیں، مگر گروپ میں نیچے جانے پر ان کی تیزابیت کم ہوتی ہے۔ ان آکسائیڈز کے تیزاب–اساس تعاملات ذیل میں دیے گئے ہیں۔',
    'د IVA ګروپ د عناصرو اکسایډونه تېزابي دي، خو په ګروپ کې ښکته تګ سره یې تېزابیت کمېږي. د دغو اکسایډونو د تېزاب–اساس تعاملونه لاندې ورکړل شوي دي.')
head('i. Group–IVA monoxides','i. گروپ IVA کے مونو آکسائیڈز','i. د IVA ګروپ مونو اکسایډونه')
add('Carbon monoxide is treated as neutral oxide but it is slightly acidic. It does not react with water. It reacts with hot and concentrated sodium hydroxide (NaOH) to produce sodium methanoate (HCOONa).',
    'کاربن مونو آکسائیڈ کو بے اثر آکسائیڈ سمجھا جاتا ہے، مگر یہ معمولی تیزابی ہے۔ یہ پانی سے تعامل نہیں کرتا۔ یہ گرم اور مرتکز سوڈیم ہائیڈرو آکسائیڈ (NaOH) سے تعامل کر کے سوڈیم میتھینوایٹ (HCOONa) بناتا ہے۔',
    'کاربن مونو اکسایډ د خنثی اکسایډ په توګه ګڼل کېږي، خو لږ تېزابي دی. دا له اوبو سره تعامل نه کوي. له ګرم او غلیظ سوډیم هایدروکسایډ (NaOH) سره تعامل کوي او سوډیم مېتانوېټ (HCOONa) جوړوي.')
eq('CO(g) + NaOH(aq) → HCOONa(aq)')
add('Germanium, tin and lead monoxides are amphoteric oxides. They can act as an acid as well as a base.',
    'جرمینیم، ٹن اور سیسے کے مونو آکسائیڈز دو خصوصیتی آکسائیڈز ہیں۔ یہ تیزاب اور اساس دونوں کے طور پر عمل کر سکتے ہیں۔',
    'د جرمانیم، ټین او سرب مونو اکسایډونه امفوتېریک اکسایډونه دي. هغوی د تېزاب او اساس دواړو په توګه عمل کولای شي.')
add('As a base:','بطور اساس:','د اساس په توګه:');eq('SnO(s) + 2HCl(aq) → SnCl₂(aq) + H₂O(l)')
add('As an acid:','بطور تیزاب:','د تېزاب په توګه:');eq('SnO(s) + 2NaOH(aq) → Na₂SnO₂(aq) + H₂O(l)')
head('ii. Group – IVA dioxides','ii. گروپ IVA کے ڈائی آکسائیڈز','ii. د IVA ګروپ ډای اکسایډونه')
add('Carbon dioxide is a slight acidic oxide. It reacts with water to a slight extent to produce hydrogen ions and hydrogencarbonate ions.',
    'کاربن ڈائی آکسائیڈ معمولی تیزابی آکسائیڈ ہے۔ یہ پانی سے معمولی حد تک تعامل کر کے ہائیڈروجن آئن اور ہائیڈروجن کاربونیٹ آئن بناتا ہے۔',
    'کاربن ډای اکسایډ لږ تېزابي اکسایډ دی. دا له اوبو سره په لږه کچه تعامل کوي او د هایدروجن ایونونه او د هایدروجن کاربونېټ ایونونه جوړوي.')
eq('CO₂(g) + H₂O(l) → H⁺(aq) + HCO₃⁻(aq)')
add('Carbon dioxide reacts with cold sodium hydroxide (NaOH) to give either sodium carbonate or sodium hydrogencarbonate solution, depending on the proportion.',
    'کاربن ڈائی آکسائیڈ ٹھنڈے سوڈیم ہائیڈرو آکسائیڈ (NaOH) سے تعامل کر کے تناسب کے مطابق سوڈیم کاربونیٹ یا سوڈیم ہائیڈروجن کاربونیٹ کا محلول بناتا ہے۔',
    'کاربن ډای اکسایډ له سړه سوډیم هایدروکسایډ (NaOH) سره تعامل کوي او د تناسب له مخې د سوډیم کاربونېټ یا سوډیم هایدروجن کاربونېټ محلول جوړوي.')
eq('CO₂(g) + 2NaOH(aq) → Na₂CO₃(aq) + H₂O(l)')
add('or','یا','یا');eq('CO₂(g) + NaOH(aq) → NaHCO₃(aq)')
add('Silicon dioxide is weakly acidic. It reacts with hot and concentrated sodium hydroxide to give sodium silicate. However, it does not react with water due to its strong covalent bonds.',
    'سلیکان ڈائی آکسائیڈ کمزور تیزابی ہے۔ یہ گرم اور مرتکز سوڈیم ہائیڈرو آکسائیڈ سے تعامل کر کے سوڈیم سلیکیٹ بناتا ہے۔ تاہم مضبوط اشتراکی بندوں کی وجہ سے پانی سے تعامل نہیں کرتا۔',
    'سیلیکان ډای اکسایډ کمزوری تېزابي دی. له ګرم او غلیظ سوډیم هایدروکسایډ سره تعامل کوي او سوډیم سیلیکېټ جوړوي. خو د خپلو پیاوړو کووالنټ تړونونو له امله له اوبو سره تعامل نه کوي.')
eq('SiO₂(s) + 2NaOH(aq) → Na₂SiO₃(aq) + H₂O(l)')
add('Germanium, tin and lead dioxides are amphoteric oxides. They can act as an acid as well as a base.',
    'جرمینیم، ٹن اور سیسے کے ڈائی آکسائیڈز دو خصوصیتی آکسائیڈز ہیں۔ یہ تیزاب اور اساس دونوں کے طور پر عمل کر سکتے ہیں۔',
    'د جرمانیم، ټین او سرب ډای اکسایډونه امفوتېریک اکسایډونه دي. هغوی د تېزاب او اساس دواړو په توګه عمل کولای شي.')
add('As a base:','بطور اساس:','د اساس په توګه:');eq('SnO₂(s) + 4HCl(aq) → SnCl₄(aq) + 2H₂O(l)')
add('For germanium and tin dioxides, hot and concentrated hydrochloric acid is used. However, for lead dioxide, cold hydrochloric acid is used. This is because, lead dioxide will decompose if the temperature increases.',
    'جرمینیم اور ٹن کے ڈائی آکسائیڈز کے لیے گرم اور مرتکز ہائیڈروکلورک تیزاب استعمال ہوتا ہے۔ تاہم سیسہ ڈائی آکسائیڈ کے لیے ٹھنڈا ہائیڈروکلورک تیزاب استعمال ہوتا ہے، کیونکہ درجہ حرارت بڑھنے پر سیسہ ڈائی آکسائیڈ تحلیل ہو جاتا ہے۔',
    'د جرمانیم او ټین د ډای اکسایډونو لپاره ګرم او غلیظ هایدروکلوریک تېزاب کارېږي. خو د سرب ډای اکسایډ لپاره سړه هایدروکلوریک تېزاب کارېږي، ځکه که تودوخه لوړه شي، سرب ډای اکسایډ تجزیه کېږي.')
add('As an acid:','بطور تیزاب:','د تېزاب په توګه:');eq('SnO₂(s) + 2NaOH(aq) → Na₂SnO₃(aq) + H₂O(l)')
add('For all reactions, hot and concentrated sodium hydroxide is used.',
    'تمام تعاملات کے لیے گرم اور مرتکز سوڈیم ہائیڈرو آکسائیڈ استعمال ہوتا ہے۔',
    'د ټولو تعاملونو لپاره ګرم او غلیظ سوډیم هایدروکسایډ کارېږي.')
head('13.5 Group–VIIA Elements: Halogens','13.5 گروپ VIIA کے عناصر: ہیلوجنز','13.5 د VIIA ګروپ عناصر: هالوجنونه')
add('Group–VIIA comprise the elements fluorine (F), chlorine (Cl), bromine (Br), iodine (I), and astatine (At). The elements are collectively known as halogens due to their salts forming tendency. All these elements are non-metals.',
    'گروپ VIIA میں فلورین (F)، کلورین (Cl)، برومین (Br)، آئیوڈین (I) اور ایسٹیٹین (At) شامل ہیں۔ نمک بنانے کے رجحان کی وجہ سے ان عناصر کو مجموعی طور پر ہیلوجنز کہتے ہیں۔ یہ سب عناصر غیر دھاتیں ہیں۔',
    'VIIA ګروپ فلورین (F)، کلورین (Cl)، برومین (Br)، ایوډین (I) او اسټاټین (At) رانغاړي. دا عناصر د مالګو د جوړولو د تمایل له امله په ګډه هالوجنونه بلل کېږي. دا ټول عناصر نافلزونه دي.')
head('13.5.1 Atomic and Physical Properties','13.5.1 ایٹمی اور طبعی خصوصیات','13.5.1 اټومي او فزیکي ځانګړنې')
add('Elements of Group – VIIA (halogens) possess seven electrons in the outermost (valence) shell, the characteristics feature being ‘ns²np⁵’ in the outer most shell. The elements and their atomic number etc. are given in Table 13.24.',
    'گروپ VIIA کے عناصر (ہیلوجنز) کے بیرونی ترین ظرفی خول میں سات الیکٹرون ہوتے ہیں؛ بیرونی ترین خول میں ns²np⁵ ان کی نمایاں خصوصیت ہے۔ عناصر، ان کے ایٹمی نمبر وغیرہ جدول 13.24 میں دیے گئے ہیں۔',
    'د VIIA ګروپ عناصر (هالوجنونه) په تر ټولو بهرني ظرفي پوښ کې اووه الکترونونه لري؛ په تر ټولو بهرني پوښ کې ns²np⁵ د هغوی ځانګړی صفت دی. عناصر، د هغوی اټومي شمېرې او نور په جدول 13.24 کې ورکړل شوي دي.')
add('Table 13.24 Elements Symbol with Atomic no and Their Electronic Configuration','جدول 13.24 عناصر کی علامتیں، ایٹمی نمبر اور ان کی الیکٹرونی ترتیب','جدول 13.24 د عناصرو نښې، اټومي شمېرې او د هغوی الکتروني ترتیب')
rows=[['₉F','1s², 2s², 2p⁵','[He] 2s, 2p⁵'],['₁₇Cl','1s², 2s², 2p⁶, 3s², 3p⁵','[Ne] 3s², 3p⁵'],['₃₅Br','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁵','[Ar]3d¹⁰, 4s², 4p⁵'],['₅₃I','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s², 4d¹⁰, 5p⁵','[Kr]4d¹⁰, 5s², 5p⁵']]
blocks.append({'id':'chem12-table-13-24','headers':['Elements','Electronic Configuration',''],'rows':rows,'translations':[{'language':'اردو','headers':['عناصر','الیکٹرونی ترتیب',''],'rows':rows},{'language':'پښتو','headers':['عناصر','الکتروني ترتیب',''],'rows':rows}]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
record=section('13.18','Silicon dioxide, oxide reactions and halogens','سلیکان ڈائی آکسائیڈ، آکسائیڈز کے تعاملات اور ہیلوجنز','سیلیکان ډای اکسایډ، د اکسایډونو تعاملونه او هالوجنونه',paras,layout,blocks,'36–37')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':22,'printedPages':[36,37]}]
issues=[{'id':'chem12-p37-fluorine-config','printedPage':37,'description':'The abbreviated fluorine configuration prints [He] 2s, 2p5 without a superscript2 on 2s, while the full configuration includes 2s2. Both printed forms preserved.'}]
if __name__=='__main__':save(22,[record],carry=[{'from':'13.18','to':'13.19','startsAt':'Halogens in the uncombined state'}],issues=issues)
