"""PDF38 printed68–69: redox titration and manganese."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def eq(e):add(e,e,e,'equation')
add('14.3.2.5 Potassium Dichromate as an Oxidizing Agent in Titrations','14.3.2.5 ٹائٹریشن میں پوٹاشیم ڈائی کرومیٹ بطور تکسیدی عامل','14.3.2.5 په تیتریشنونو کې پوتاشیم ډای کرومېټ د اکسیدوونکي په توګه','heading')
add('In redox titration, a standard solution of potassium dichromate (K₂Cr₂O₇) is used to determine the unknown concentration of a solution of Fe²⁺. Dichromate ion reduces to chromium (III) ions.',
 'ریڈوکس ٹائٹریشن میں پوٹاشیم ڈائی کرومیٹ (K₂Cr₂O₇) کا معیاری محلول Fe²⁺ محلول کا نامعلوم ارتکاز معلوم کرنے کے لیے استعمال ہوتا ہے۔ ڈائی کرومیٹ آئن کرومیم(III) آئنوں میں تخفیف پاتا ہے۔',
 'په ریډوکس تیتریشن کې د پوتاشیم ډای کرومېټ (K₂Cr₂O₇) معیاري محلول د Fe²⁺ محلول د نامعلوم غلظت د معلومولو لپاره کارېږي. ډای کرومېټ ایون کرومیم(III) ایونونو ته احیا کېږي.')
add('The half-equation for the dichromate (VI) ion is:','ڈائی کرومیٹ(VI) آئن کی نصف مساوات ہے:','د ډای کرومېټ(VI) ایون نیمه معادله دا ده:')
eq('Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O')
add('and Fe(II) is oxidized to Fe(III)','اور Fe(II)، Fe(III) میں تکسید پاتا ہے','او Fe(II) په Fe(III) اکسیدېږي')
eq('6Fe²⁺ → 6Fe³⁺ + 6e⁻')
add('Combining these equations gives:','یہ مساوات ملانے سے حاصل ہوتا ہے:','د دې معادلو په یوځای کولو ترلاسه کېږي:')
eq('Cr₂O₇²⁻ + 6Fe²⁺ + 14H⁺ → 2Cr³⁺ + 6Fe³⁺ + 7H₂O')
add('Orange — Green','نارنجی — سبز','نارنجي — شین')
add('The molecular form of the equation can be written as,','مساوات کی سالماتی شکل یوں لکھی جا سکتی ہے،','د معادلې مالیکولي بڼه داسې لیکل کېدای شي،')
eq('K₂Cr₂O₇ + 6FeSO₄ + 7H₂SO₄ → K₂SO₄ + Cr₂(SO₄)₃ + 7H₂O + 3Fe₂(SO₄)₃')
add('Tidbit — Mohr’s salt','مختصر معلومات — موہر کا نمک','لنډ معلومات — د مور مالګه','heading')
add('Ferrous ammonium sulphate or Mohr’s salt [FeSO₄.(NH₄)₂SO₄.6H₂O]. Determining the unknown concentration of a solution of Fe²⁺, is actually titration against the Mohr’s salt.',
 'فیرس امونیم سلفیٹ یا موہر کا نمک [FeSO₄.(NH₄)₂SO₄.6H₂O]۔ Fe²⁺ محلول کا نامعلوم ارتکاز معلوم کرنا دراصل موہر کے نمک کے مقابل ٹائٹریشن ہے۔',
 'فېرس امونیم سلفېټ یا د مور مالګه [FeSO₄.(NH₄)₂SO₄.6H₂O]. د Fe²⁺ محلول د نامعلوم غلظت معلومول په حقیقت کې د مور مالګې پر وړاندې تیتریشن دی.')
add('14.3.3 Manganese','14.3.3 مینگنیز','14.3.3 منګنیز','heading')
add('Manganese is the third most abundant transition metal after iron and titanium. Manganese, (Mn), is silvery white, brittle metallic element used principally in making alloys. The atomic number of manganese is 25 and atomic mass 54.938 a.m.u.',
 'مینگنیز، لوہے اور ٹائٹینیم کے بعد تیسری سب سے وافر عبوری دھات ہے۔ مینگنیز (Mn) چاندی جیسا سفید، بھربھرا دھاتی عنصر ہے جو بنیادی طور پر آمیزے بنانے میں استعمال ہوتا ہے۔ اس کا جوہری عدد 25 اور جوہری کمیت 54.938 a.m.u. ہے۔',
 'منګنیز له اوسپنې او ټایټانیم وروسته درېیم ډېر موندل کېدونکی انتقالي فلز دی. منګنیز (Mn) سپین زرو ته ورته سپین، ماتېدونکی فلزي عنصر دی چې په عمده توګه د الیاژونو په جوړولو کې کارېږي. اټومي شمېره یې 25 او اټومي کتله یې 54.938 a.m.u. ده.')
add('14.3.3.1 Oxidation States','14.3.3.1 تکسیدی حالتیں','14.3.3.1 د اکسیدېشن حالتونه','heading')
add('According to the electronic configuration of manganese (3d⁵, 4s²), it shows a maximum oxidation state of +7. In addition to this state, it also shows lower oxidation states such as +6, +4, +3 and +2.',
 'مینگنیز کی الیکٹرانی ترتیب (3d⁵, 4s²) کے مطابق اس کی زیادہ سے زیادہ تکسیدی حالت +7 ہے۔ اس کے علاوہ کم حالتیں +6، +4، +3 اور +2 بھی دکھاتا ہے۔',
 'د منګنیز د الکتروني ترتیب (3d⁵, 4s²) له مخې تر ټولو لوړ اکسیدېشن حالت یې +7 دی. پر دې سربېره ټیټ حالتونه +6، +4، +3 او +2 هم ښيي.')
add('Manganese compounds in which ‘Mn’ is in +7 oxidation state, are restricted to the unstable oxide Mn₂O₇ and compounds of intensely purple permanganate ion (MnO₄⁻¹) and are powerful oxidizing agents.',
 'Mn کی +7 حالت والے مینگنیز مرکبات غیر مستحکم آکسائیڈ Mn₂O₇ اور گہرے جامنی پرمینگنیٹ آئن (MnO₄⁻¹) کے مرکبات تک محدود ہیں اور طاقتور تکسیدی عامل ہیں۔',
 'د Mn د +7 حالت منګنیزي مرکبات په ناثابت اکسایډ Mn₂O₇ او د سخت ارغواني پرمنګنېټ ایون (MnO₄⁻¹) په مرکباتو پورې محدود دي او پیاوړي اکسیدوونکي دي.','list')
add('Mn⁶⁺ is present in MnO₃ in the salt of manganic acid (H₂MnO₄). The free acid is unknown. Its salts are called manganates e.g. K₂MnO₄.',
 'Mn⁶⁺، MnO₃ میں مینگینک تیزاب (H₂MnO₄) کے نمک میں موجود ہے۔ آزاد تیزاب نامعلوم ہے۔ اس کے نمکیات مینگنیٹس کہلاتے ہیں، مثلاً K₂MnO₄۔',
 'Mn⁶⁺ په MnO₃ کې د منګانیک اسید (H₂MnO₄) په مالګه کې شته. ازاد اسید نامعلوم دی. مالګې یې منګنېټونه بلل کېږي، لکه K₂MnO₄.','list')
add('The compounds having Mn⁴⁺ are very limited in number. The most familiar compound of Mn⁴⁺ is MnO₂.','Mn⁴⁺ والے مرکبات تعداد میں بہت محدود ہیں۔ سب سے مانوس مرکب MnO₂ ہے۔','د Mn⁴⁺ مرکبات په شمېر کې ډېر محدود دي. تر ټولو اشنا مرکب یې MnO₂ دی.','list')
add('The compound of Mn³⁺ is called manganic compound. In aqueous solution Mn³⁺ ions is quite unstable since it is easily reduced to Mn²⁺ ions e.g. H₂Mn₂O₄, Mn₂(SO₄)₃.',
 'Mn³⁺ کا مرکب مینگینک مرکب کہلاتا ہے۔ آبی محلول میں Mn³⁺ آئن بہت غیر مستحکم ہے کیونکہ آسانی سے Mn²⁺ میں تخفیف پاتا ہے، مثلاً H₂Mn₂O₄ اور Mn₂(SO₄)₃۔',
 'د Mn³⁺ مرکب منګانیک مرکب بلل کېږي. په اوبلن محلول کې Mn³⁺ ایون ډېر ناثابت دی ځکه په اسانۍ Mn²⁺ ته احیا کېږي، لکه H₂Mn₂O₄ او Mn₂(SO₄)₃.','list')
eq('Mn³⁺ + 1e⁻ → Mn²⁺')
add('+2 is the most stable oxidation state of Mn in neutral or acidic solution. Mn²⁺ ion exists as pale pink hexaaquamanganese(II) [Mn(H₂O)₆]²⁺, which is quite stable to oxidation. The stability of Mn²⁺ is due to half-filled 3d orbital. The compounds of Mn²⁺ are called manganous compounds such as MnO, MnCO₃, MnSO₄, MnCl₂ etc.',
 'بے اثر یا تیزابی محلول میں Mn کی سب سے مستحکم حالت +2 ہے۔ Mn²⁺ آئن ہلکے گلابی ہیکسا ایکوا مینگنیز(II) [Mn(H₂O)₆]²⁺ کے طور پر ہے، جو تکسید کے خلاف کافی مستحکم ہے۔ استحکام نصف بھرے 3d آربیٹل کی وجہ سے ہے۔ Mn²⁺ کے مرکبات مینگنس مرکبات ہیں، جیسے MnO، MnCO₃، MnSO₄ اور MnCl₂ وغیرہ۔',
 'په خنثی یا اسیدي محلول کې د Mn تر ټولو ثابت حالت +2 دی. Mn²⁺ ایون د سپک ګلابي هېکسا اکوا منګنیز(II) [Mn(H₂O)₆]²⁺ په توګه وي، چې د اکسیدېشن پر وړاندې ښه ثابت دی. ثبات یې د نیم ډک 3d اوربیټال له امله دی. د Mn²⁺ مرکبات منګانوس مرکبات دي، لکه MnO، MnCO₃، MnSO₄ او MnCl₂ او نور.','list')
add('14.3.3.2 Potassium Manganate (VII) as an Oxidizing Agent in Organic Chemistry','14.3.3.2 نامیاتی کیمیا میں پوٹاشیم مینگنیٹ(VII) بطور تکسیدی عامل','14.3.3.2 په عضوي کیمیا کې پوتاشیم منګنېټ(VII) د اکسیدوونکي په توګه','heading')
add('Potassium manganate (VII) is a powerful oxidizing agent. It is usually used in neutral or alkaline solution in organic chemistry. Acidified potassium manganate (VII) tends to be destructively strong oxidizing agent, breaking carbon-carbon bonds. The potassium manganate (VII) solution is usually made mildly alkaline with sodium carbonate solution and the typical colour changes are:',
 'پوٹاشیم مینگنیٹ(VII) طاقتور تکسیدی عامل ہے۔ نامیاتی کیمیا میں عموماً بے اثر یا اساسی محلول میں استعمال ہوتا ہے۔ تیزابی پوٹاشیم مینگنیٹ(VII) تباہ کن حد تک مضبوط تکسیدی عامل بننے کا رجحان رکھتا ہے، جو کاربن–کاربن بند توڑتا ہے۔ اس کا محلول عموماً سوڈیم کاربونیٹ محلول سے ہلکا اساسی بناتے ہیں؛ مخصوص رنگی تبدیلیاں یہ ہیں:',
 'پوتاشیم منګنېټ(VII) پیاوړی اکسیدوونکی دی. په عضوي کیمیا کې عموماً په خنثی یا قلوي محلول کې کارېږي. اسیدي پوتاشیم منګنېټ(VII) د تخریب تر کچې د پیاوړي اکسیدوونکي تمایل لري او کاربن–کاربن تړونونه ماتوي. محلول یې عموماً په سوډیم کاربونېټ محلول لږ قلوي کېږي؛ ځانګړي رنګي بدلونونه دا دي:')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200" role="img"><g stroke="#222" stroke-width="3">'
for x,color in [(90,'#48243d'),(340,'#366a35'),(590,'#101010')]:
 svg+=f'<path d="M{x-20} 20V150Q{x} 180 {x+20} 150V20" fill="none"/><path d="M{x-18} 115H{x+18}V149Q{x} 173 {x-18} 149Z" fill="{color}"/>'
svg+='<path d="M160 90H250M410 90H500"/><path d="M250 90L236 83V97ZM500 90L486 83V97Z"/></g></svg>'
blocks.append({'id':'chem12-p69-manganate-colour-changes','svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('Original dark purple manganate (VII) ion MnO₄⁻ → Reduced to dark green manganate (VI) ion MnO₄²⁻ → Further reduced to black precipitate of MnO₂',
 'اصل گہرا جامنی مینگنیٹ(VII) آئن MnO₄⁻ → تخفیف سے گہرا سبز مینگنیٹ(VI) آئن MnO₄²⁻ → مزید تخفیف سے MnO₂ کا سیاہ رسوب',
 'اصلي سخت ارغواني منګنېټ(VII) ایون MnO₄⁻ → په احیا سخت شین منګنېټ(VI) ایون MnO₄²⁻ → په نوره احیا د MnO₂ تور رسوب')
add('i. In Testing for a C=C Double Bond','i. C=C دوہرے بند کی جانچ میں','i. د C=C دوه ګوني تړون په ازموینه کې','heading')
add('Potassium manganate (VII) oxidizes carbon-carbon double bonds and so goes through the colour changes. The colour change depends on whether the potassium manganate (VII) is used under acidic or alkaline conditions. Ethene, for example, is oxidized to ethane-1,2-diol.',
 'پوٹاشیم مینگنیٹ(VII) کاربن–کاربن دوہرے بندوں کی تکسید کرتا ہے اور یوں رنگی تبدیلیوں سے گزرتا ہے۔ رنگ کی تبدیلی اس پر منحصر ہے کہ اسے تیزابی یا اساسی شرائط میں استعمال کریں۔ مثلاً ایتھین تکسید سے ایتھین-1،2-ڈائی اول بنتا ہے۔',
 'پوتاشیم منګنېټ(VII) کاربن–کاربن دوه ګوني تړونونه اکسیدوي او له همدې امله رنګي بدلونونه کوي. رنګي بدلون په دې پورې تړلی دی چې په اسیدي یا قلوي شرایطو کې وکارول شي. لکه ایتین په اکسیدېشن ایتان-1،2-ډای اول جوړوي.')
eq('CH₂=CH₂ + H₂O + [O] → HO—CH₂—CH₂—OH')
add('Under acidic conditions, the manganate (VII) ions are reduced to manganese (II) ions.','تیزابی شرائط میں مینگنیٹ(VII) آئن مینگنیز(II) آئنوں میں تخفیف پاتے ہیں۔','په اسیدي شرایطو کې منګنېټ(VII) ایونونه منګنیز(II) ایونونو ته احیا کېږي.','list')
record=section('14.13','Dichromate titration and manganese','ڈائی کرومیٹ ٹائٹریشن اور مینگنیز','ډای کرومېټ تیتریشن او منګنیز',paras,layout,blocks,'68–69');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':38,'printedPages':[68,69]}];record['sourceContinuesOnPdfPage']=39
if __name__=='__main__':save(38,[record],issues=[{'id':'chem12-p68-mn6-wording','printedPage':68,'description':'Printed Mn6+ sentence mentions MnO3 and salt of manganic acid; retained.'},{'id':'chem12-p69-manganic-acid','printedPage':69,'description':'Printed Mn3+ examples include H2Mn2O4; retained.'}],chapter_number=14)
