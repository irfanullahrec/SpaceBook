"""Source-aligned PDF19, printed30–31; continuation retained for PDF20."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
head('13.3.6.1 Why is Beryllium Chloride Covalent and not Ionic?','13.3.6.1 بیریلیم کلورائیڈ اشتراکی کیوں ہے، آئنک کیوں نہیں؟','13.3.6.1 بېریلیم کلورایډ ولې کووالنټ دی او ایوني نه دی؟')
add('Beryllium at the top of the group has high electronegativity (1.57) compared with the rest of the group members. High electronegativity means that it attracts a bonding pair of electrons towards itself more strongly than the rest of the Group – IIA elements. This gives covalent character to BeCl₂.',
    'گروپ کے اوپر بیریلیم کی برقی منفیت (1.57) گروپ کے باقی ارکان سے زیادہ ہے۔ زیادہ برقی منفیت کا مطلب ہے کہ یہ بند بنانے والے الیکٹرون جوڑے کو گروپ IIA کے باقی عناصر کی نسبت زیادہ مضبوطی سے اپنی طرف کھینچتا ہے۔ اس سے BeCl₂ کو اشتراکی کردار ملتا ہے۔',
    'د ګروپ په سر کې بېریلیم د ګروپ د نورو غړو په پرتله لوړ برېښنا منفي توب (1.57) لري. لوړ برېښنا منفي توب دا مانا لري چې د IIA ګروپ د نورو عناصرو په پرتله د تړون جوړوونکو الکترونونو جوړه ځان ته په پیاوړې توګه راکاږي. دا BeCl₂ ته کووالنټ ځانګړنه ورکوي.')
head('13.3.6.2 Amphoteric Beryllium Hydroxide','13.3.6.2 دو خصوصیتی بیریلیم ہائیڈرو آکسائیڈ','13.3.6.2 امفوتېریک بېریلیم هایدروکسایډ')
add('Beryllium hydroxide can act both as an acid and as a base.','بیریلیم ہائیڈرو آکسائیڈ تیزاب اور اساس، دونوں کے طور پر عمل کر سکتا ہے۔','بېریلیم هایدروکسایډ د تېزاب او اساس دواړو په توګه عمل کولای شي.')
head('i. Beryllium Hydroxide as an Acid','i. بیریلیم ہائیڈرو آکسائیڈ بطور تیزاب','i. بېریلیم هایدروکسایډ د تېزاب په توګه')
add('Beryllium hydroxide reacts with concentrated solution of sodium hydroxide to produce sodium tetrahydroxoberyllate.',
    'بیریلیم ہائیڈرو آکسائیڈ سوڈیم ہائیڈرو آکسائیڈ کے مرتکز محلول سے تعامل کر کے سوڈیم ٹیٹراہائیڈروکسوبیریلیٹ بناتا ہے۔',
    'بېریلیم هایدروکسایډ د سوډیم هایدروکسایډ له غلیظ محلول سره تعامل کوي او سوډیم ټېټراهایدروکسوبېریلېټ جوړوي.')
add('As an acid:','بطور تیزاب:','د تېزاب په توګه:')
eq('Be(OH)₂(aq) + 2NaOH(aq) → Na₂[Be(OH)₄](aq)')
add('sodium tetrahydroxoberyllate','سوڈیم ٹیٹراہائیڈروکسوبیریلیٹ','سوډیم ټېټراهایدروکسوبېریلېټ')
head('ii. Beryllium Hydroxide as a Base','ii. بیریلیم ہائیڈرو آکسائیڈ بطور اساس','ii. بېریلیم هایدروکسایډ د اساس په توګه')
add('Beryllium hydroxide reacts with dilute hydrochloric acid producing beryllium chloride as neutralization product.',
    'بیریلیم ہائیڈرو آکسائیڈ رقیق ہائیڈروکلورک تیزاب سے تعامل کر کے تعدیل کی پیداوار کے طور پر بیریلیم کلورائیڈ بناتا ہے۔',
    'بېریلیم هایدروکسایډ له رقیق هایدروکلوریک تېزاب سره تعامل کوي او د خنثی کېدو د محصول په توګه بېریلیم کلورایډ جوړوي.')
add('As a base:','بطور اساس:','د اساس په توګه:')
eq('Be(OH)₂(aq) + 2HCl(aq) → BeCl₂(aq) + 2H₂O(l)')
head('13.4 Group – IVA Elements','13.4 گروپ IVA کے عناصر','13.4 د IVA ګروپ عناصر')
add('The Group – IVA of the periodic table is often referred to as the carbon group. This group consists of five elements carbon (C), silicon (Si), germanium (Ge), tin (Sn) and lead (Pb). This group is present in the middle of periodic table forming a link between more electropositive elements of Group – IA to IIIA and more electronegative elements of Group VA to VIIA. Each element in this group contains four valence electrons. The elements of group – IV A evidentially exhibit an intermediate character. The general electronic configuration of Group – IVA elements in valence shell is ns², np², where n varies from 2 (for carbon) to 6 (for lead), for example, the electronic configuration of carbon is 1s²,2s², 2p².',
    'دوری جدول کے گروپ IVA کو اکثر کاربن گروپ کہا جاتا ہے۔ اس میں پانچ عناصر کاربن (C)، سلیکان (Si)، جرمینیم (Ge)، ٹن (Sn) اور سیسہ (Pb) ہیں۔ یہ گروپ دوری جدول کے وسط میں گروپ IA سے IIIA کے زیادہ برقی مثبت عناصر اور گروپ VA سے VIIA کے زیادہ برقی منفی عناصر کے درمیان رابطہ بناتا ہے۔ اس گروپ کے ہر عنصر میں چار ظرفی الیکٹرون ہوتے ہیں۔ گروپ IVA کے عناصر واضح طور پر درمیانی کردار دکھاتے ہیں۔ ان کے ظرفی خول کی عمومی الیکٹرونی ترتیب ns²، np² ہے، جہاں n کاربن کے لیے 2 سے سیسے کے لیے 6 تک بدلتا ہے؛ مثلاً کاربن کی الیکٹرونی ترتیب 1s²,2s², 2p² ہے۔',
    'د دوراني جدول IVA ګروپ ته ډېری وخت د کاربن ګروپ ویل کېږي. دا ګروپ له پنځو عناصرو، کاربن (C)، سیلیکان (Si)، جرمانیم (Ge)، ټین (Sn) او سرب (Pb) څخه جوړ دی. دا د دوراني جدول په منځ کې د IA تر IIIA ګروپونو د ډېرو برېښنا مثبتو عناصرو او د VA تر VIIA ګروپونو د ډېرو برېښنا منفي عناصرو ترمنځ اړیکه جوړوي. د دې ګروپ هر عنصر څلور ظرفي الکترونونه لري. د IVA ګروپ عناصر په څرګند ډول منځنۍ ځانګړنه ښيي. په ظرفي پوښ کې یې عمومي الکتروني ترتیب ns²، np² دی، چې n د کاربن لپاره له 2 څخه د سرب لپاره تر 6 پورې بدلېږي؛ د بېلګې په توګه د کاربن الکتروني ترتیب 1s²,2s², 2p² دی.')
head('13.4.1 Physical Properties: Melting and Boiling Points','13.4.1 طبعی خصوصیات: پگھلنے اور ابلنے کے درجے','13.4.1 فزیکي ځانګړنې: د وېلې کېدو او اېشېدو ټکي')
add('The melting point of carbon is extremely high. The melting and boiling points of silicon and germanium are very high because these elements have a very stable arrangement of solid structure (diamond-type lattice). Sn and Pb have a lower melting point because only two electrons are involved in bond formation instead of four, due to inert pair effect.',
    'کاربن کا نقطۂ پگھلاؤ انتہائی بلند ہے۔ سلیکان اور جرمینیم کے پگھلنے اور ابلنے کے درجے بہت بلند ہیں، کیونکہ ان عناصر کی ٹھوس ساخت کا بندوبست بہت مستحکم ہے (ہیرے جیسی جالی)۔ Sn اور Pb کا نقطۂ پگھلاؤ کم ہے، کیونکہ غیر فعال جوڑے کے اثر کی وجہ سے بند بنانے میں چار کی بجائے صرف دو الیکٹرون حصہ لیتے ہیں۔',
    'د کاربن د وېلې کېدو ټکی ډېر لوړ دی. د سیلیکان او جرمانیم د وېلې کېدو او اېشېدو ټکي ډېر لوړ دي، ځکه دا عناصر د جامدې جوړښت ډېر ثابت ترتیب لري (د الماس په څېر جالۍ). Sn او Pb د وېلې کېدو ټیټ ټکی لري، ځکه د غیر فعالې جوړې د اغېز له امله د تړون په جوړولو کې د څلورو پر ځای یوازې دوه الکترونونه برخه اخلي.')
add('Table 13.23 Melting and Boiling Points of Group IVA Elements','جدول 13.23 گروپ IVA کے عناصر کے پگھلنے اور ابلنے کے درجے','جدول 13.23 د IVA ګروپ د عناصرو د وېلې کېدو او اېشېدو ټکي')
headers=['Elements','C','Si','Ge','Sn','Pb'];mp=['3550 (Diamond)','1410','937','232','328'];bp=['4827','2355','2830','2260','1744']
blocks.append({'id':'chem12-table-13-23','headers':headers,'rows':[['Melting point (°C)']+mp,['Boiling point (°C)']+bp],
    'translations':[{'language':'اردو','headers':['عناصر']+headers[1:],'rows':[['نقطۂ پگھلاؤ (°C)','3550 (ہیرا)']+mp[1:],['نقطۂ ابال (°C)']+bp]},
                    {'language':'پښتو','headers':['عناصر']+headers[1:],'rows':[['د وېلې کېدو ټکی (°C)','3550 (الماس)']+mp[1:],['د اېشېدو ټکی (°C)']+bp]}]})
layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
head('13.4.2 The Trend from Non-Metal to Metal','13.4.2 غیر دھات سے دھات کی طرف رجحان','13.4.2 له نافلز څخه فلز ته تمایل')
add('The change from non-metallic to metallic character with the increase of atomic number is best illustrated in this group e.g. C is non-metal, Si and Ge are metalloids, while Sn and Pb exhibit metallic character.',
    'ایٹمی نمبر بڑھنے کے ساتھ غیر دھاتی سے دھاتی کردار کی تبدیلی اس گروپ میں بہترین طور پر نمایاں ہے؛ مثلاً C غیر دھات، Si اور Ge نیم دھاتیں ہیں، جبکہ Sn اور Pb دھاتی کردار دکھاتے ہیں۔',
    'د اټومي شمېر په زیاتېدو سره له نافلزي ځانګړنې څخه فلزي ځانګړنې ته بدلون په دې ګروپ کې تر ټولو ښه څرګندېږي؛ لکه C نافلز دی، Si او Ge شبه فلزونه دي، خو Sn او Pb فلزي ځانګړنه ښيي.')
head('13.4.3 Oxidation State','13.4.3 تکسیدی حالت','13.4.3 د اکسیدېشن حالت')
add('Oxidation state is the apparent charge (positive or negative) on an atom of an element in a molecule or ion.',
    'تکسیدی حالت کسی سالمے یا آئن میں کسی عنصر کے ایٹم پر ظاہری بار (مثبت یا منفی) ہے۔',
    'د اکسیدېشن حالت په یوه مالیکول یا ایون کې د یوه عنصر پر اټوم ظاهري چارج (مثبت یا منفي) دی.')
add('Carbon and silicon show +4 oxidation states in carbonates and silicates. The remaining members can show +2 as well as +4 oxidation states. Since, the electronegativity of these elements is low; they do not have such a high tendency to form negative ions.',
    'کاربن اور سلیکان، کاربونیٹس اور سلیکیٹس میں +4 تکسیدی حالت دکھاتے ہیں۔ باقی ارکان +2 اور +4 دونوں تکسیدی حالتیں دکھا سکتے ہیں۔ چونکہ ان عناصر کی برقی منفیت کم ہے، اس لیے ان میں منفی آئن بنانے کا اتنا زیادہ رجحان نہیں ہوتا۔',
    'کاربن او سیلیکان په کاربونېټونو او سیلیکېټونو کې +4 د اکسیدېشن حالتونه ښيي. پاتې غړي +2 او +4 دواړه حالتونه ښودلای شي. ځکه چې د دې عناصرو برېښنا منفي توب ټیټ دی، د منفي ایونونو د جوړولو دومره لوړ تمایل نه لري.')
head('13.4.4 Possible Oxidation States','13.4.4 ممکنہ تکسیدی حالتیں','13.4.4 د اکسیدېشن ممکن حالتونه')
add('Oxidation state of group – IVA elements may be positive or negative depending upon the nature of the compounds. The typical oxidation state shown by elements of Groups – IVA is +4, found in compounds like CCl₄, SiCl₄ and SnO₂. However, as we move down the group, there are more and more examples, where the oxidation state is +2, such as SnCl₂, PbCl₂ and PbO.',
    'گروپ IVA کے عناصر کا تکسیدی حالت مرکبات کی نوعیت کے مطابق مثبت یا منفی ہو سکتا ہے۔ گروپ IVA کے عناصر کا عام تکسیدی حالت +4 ہے، جو CCl₄، SiCl₄ اور SnO₂ جیسے مرکبات میں ملتا ہے۔ تاہم گروپ میں نیچے جانے پر +2 تکسیدی حالت کی مثالیں بڑھتی ہیں، جیسے SnCl₂، PbCl₂ اور PbO۔',
    'د IVA ګروپ د عناصرو د اکسیدېشن حالت د مرکباتو د ماهیت له مخې مثبت یا منفي کېدای شي. د IVA ګروپ د عناصرو عادي د اکسیدېشن حالت +4 دی، چې په CCl₄، SiCl₄ او SnO₂ غوندې مرکباتو کې موندل کېږي. خو په ګروپ کې ښکته تګ سره د +2 حالت بېلګې ډېرېږي، لکه SnCl₂، PbCl₂ او PbO.')
add('However, carbon forms C⁴⁻ and C₂²⁻ ions in certain compounds, such as Be₂C(C = −4, Be = +2), Na₂C₂(C₂ = −2, Na = +1) etc. Besides this, CH₄, is not an example of carbon with an oxidation state of +4. Because carbon is more electronegative than hydrogen, so its oxidation state is −4.',
    'تاہم بعض مرکبات میں کاربن C⁴⁻ اور C₂²⁻ آئن بناتا ہے، جیسے Be₂C(C = −4، Be = +2)، Na₂C₂(C₂ = −2، Na = +1) وغیرہ۔ اس کے علاوہ CH₄، +4 تکسیدی حالت والے کاربن کی مثال نہیں ہے۔ چونکہ کاربن ہائیڈروجن سے زیادہ برقی منفی ہے، اس لیے اس کا تکسیدی حالت −4 ہے۔',
    'خو کاربن په ځینو مرکباتو کې C⁴⁻ او C₂²⁻ ایونونه جوړوي، لکه Be₂C(C = −4، Be = +2)، Na₂C₂(C₂ = −2، Na = +1) او نور. سربېره پر دې، CH₄ د +4 د اکسیدېشن حالت لرونکي کاربن بېلګه نه ده. ځکه کاربن له هایدروجن څخه ډېر برېښنا منفي دی، نو د اکسیدېشن حالت یې −4 دی.')
head('13.4.4.1 Inert Pair Effect in Formation of Ionic Bonds','13.4.4.1 آئنک بندوں کی تشکیل میں غیر فعال جوڑے کا اثر','13.4.4.1 د ایوني تړونونو په جوړولو کې د غیر فعالې جوړې اغېز')
add('The tendency of the two electrons in the outermost atomic s-orbital to remain unshared in compounds is called inert pair effect. For example, C and Si show a covalence of four due to sp³ hybridization. However, hybridization may not always be feasible in case of the lower elements of Group – IV. For hybridization to be energetically feasible, net enthalpy change involved in the following two processes should be negative.',
    'بیرونی ترین ایٹمی s آربیٹل کے دو الیکٹرونوں کا مرکبات میں غیر مشترک رہنے کا رجحان غیر فعال جوڑے کا اثر کہلاتا ہے۔ مثلاً C اور Si، sp³ ہائبرڈائزیشن کی وجہ سے چار کی اشتراکی ظرف دکھاتے ہیں۔ تاہم گروپ IV کے نچلے عناصر میں ہائبرڈائزیشن ہمیشہ ممکن نہیں ہو سکتی۔ توانائی کے لحاظ سے ہائبرڈائزیشن ممکن ہونے کے لیے درج ذیل دو عملوں میں مجموعی اینتھالپی تبدیلی منفی ہونی چاہیے۔',
    'په مرکباتو کې د تر ټولو بهرني اټومي s اوربیټل د دوو الکترونونو د نه شریکېدو تمایل د غیر فعالې جوړې اغېز بلل کېږي. د بېلګې په توګه C او Si د sp³ هایبرډایزېشن له امله څلور کووالنټ ظرفیت ښيي. خو د IV ګروپ په لاندې عناصرو کې هایبرډایزېشن تل ممکن نه وي. د انرژۍ له پلوه د هایبرډایزېشن د امکان لپاره په لاندې دوو بهیرونو کې خالص انتالپي بدلون باید منفي وي.')
record=section('13.15','Beryllium hydroxide and Group IVA oxidation states','بیریلیم ہائیڈرو آکسائیڈ اور گروپ IVA کی تکسیدی حالتیں','بېریلیم هایدروکسایډ او د IVA ګروپ د اکسیدېشن حالتونه',paras,layout,blocks,'30–31')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':19,'printedPages':[30,31]}]
record['sourceContinuesOnPdfPage']=20
if __name__=='__main__':save(19,[record],carry=[{'from':'13.15','to':'13.16','startsAt':'Promotion of one electron of the s-orbital'}])
