"""PDF11: chlorides, printed 14–15, with source defects preserved."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
add('Dichlorine heptoxide (Cl₂O₇) reacts directly with sodium hydroxide to give sodium chlorate and water.',
    'ڈائی کلورین ہیپٹا آکسائیڈ (Cl₂O₇) براہِ راست سوڈیم ہائیڈرو آکسائیڈ کے ساتھ تعامل کر کے سوڈیم کلوریٹ اور پانی بناتا ہے۔',
    'ډای کلورین هېپټا اکسایډ (Cl₂O₇) له سوډیم هایدروکسایډ سره نېغ تعامل کوي او سوډیم کلورېټ او اوبه جوړوي.')
eq('Cl₂O₇(l) + 2NaOH(aq) → 2NaClO₄(aq) + H₂O(l)')
add('Dichlorine monoxide (Cl₂O) also reacts directly with sodium hydroxide to give sodium hypochlorite and water.',
    'ڈائی کلورین مونو آکسائیڈ (Cl₂O) بھی براہِ راست سوڈیم ہائیڈرو آکسائیڈ کے ساتھ تعامل کر کے سوڈیم ہائپوکلورائٹ اور پانی بناتا ہے۔',
    'ډای کلورین مونو اکسایډ (Cl₂O) هم له سوډیم هایدروکسایډ سره نېغ تعامل کوي او سوډیم هایپوکلورایټ او اوبه جوړوي.')
eq('Cl₂O + 2NaOH → 2NaClO + H₂O')
add('Argon (Ar) is noble gas and it does not form oxides.', 'آرگن (Ar) نجیب گیس ہے اور آکسائیڈز نہیں بناتا۔','ارګون (Ar) نجیب ګاز دی او اکسایډونه نه جوړوي.')
head('13.1.5 Chlorides of the Period 3ʳᵈ Elements','13.1.5 تیسرے دور کے عناصر کے کلورائیڈز','13.1.5 د درېیمې دورې د عناصرو کلورایډونه')
add('Chlorides are compounds formed between chlorine and another element. They are binary compounds, in which chlorine is combined with only one other element. The chlorides of Period 3ʳᵈ elements Na (sodium) to S (sulphur) are given in the following table with their physical properties.',
    'کلورائیڈز کلورین اور کسی دوسرے عنصر سے بننے والے مرکبات ہیں۔ یہ دو عنصری مرکبات ہیں جن میں کلورین صرف ایک دوسرے عنصر کے ساتھ ملتی ہے۔ تیسرے دور کے Na (سوڈیم) سے S (سلفر) تک کے عناصر کے کلورائیڈز اور ان کی طبعی خصوصیات درج ذیل جدول میں دی گئی ہیں۔',
    'کلورایډونه هغه مرکبات دي چې د کلورین او بل عنصر ترمنځ جوړېږي. دا دوه عنصري مرکبات دي، چې کلورین پکې یوازې له یوه بل عنصر سره یوځای وي. د درېیمې دورې له Na (سوډیم) څخه تر S (سلفر) پورې د عناصرو کلورایډونه او فزیکي ځانګړنې یې په لاندې جدول کې ورکړل شوي دي.')
add('Table 13.10 Chlorides of the Period 3ʳᵈ Elements and their Physical Properties','جدول 13.10 تیسرے دور کے عناصر کے کلورائیڈز اور ان کی طبعی خصوصیات','جدول 13.10 د درېیمې دورې د عناصرو کلورایډونه او فزیکي ځانګړنې یې')
headers=['Chloride','NaCl','MgCl₂','Al₂Cl₆','SiCl₄','PCl₃','S₂Cl₂']
m=['801','708','192.4','−69','−93.6','−80'];b=['1465','1418','423','57','74','136']
t={'id':'chem12-table-13-10','headers':headers,'rows':[['Physical State(20°C)','Solid','Solid','Solid','Liquid','Liquid','Liquid'],['Melting Point(°C)']+m,['Boiling Point(°C)']+b],
   'translations':[{'language':'اردو','headers':['کلورائیڈ']+headers[1:],'rows':[['طبعی حالت (20°C)','ٹھوس','ٹھوس','ٹھوس','مائع','مائع','مائع'],['نقطۂ پگھلاؤ (°C)']+m,['نقطۂ ابال (°C)']+b]},
                   {'language':'پښتو','headers':['کلورایډ']+headers[1:],'rows':[['فزیکي حالت (20°C)','جامد','جامد','جامد','مایع','مایع','مایع'],['د وېلې کېدو ټکی (°C)']+m,['د اېشېدو ټکی (°C)']+b]}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
add('There are three chlorides of sulphur, but only one is mentioned here i.e. S₂Cl₂. Al₂Cl₆ is the dimer of aluminium chloride (AlCl₃).',
    'سلفر کے تین کلورائیڈز ہیں، مگر یہاں صرف S₂Cl₂ بیان کیا گیا ہے۔ Al₂Cl₆ ایلومینیم کلورائیڈ (AlCl₃) کا ڈائی مر ہے۔',
    'د سلفر درې کلورایډونه شته، خو دلته یوازې S₂Cl₂ یاد شوی دی. Al₂Cl₆ د المونیم کلورایډ (AlCl₃) ډایمر دی.')
head('13.1.5.1 Structure','13.1.5.1 ساخت','13.1.5.1 جوړښت')
add('NaCl and MgCl₂ are ionic and consist of giant ionic lattices at room temperature. AlCl₃ is complicated due to its structural changes as temperature increases. The structure is an ionic lattice – although with a lot of covalent character. PCl₅ is structurally more complicated. The chlorides of the other elements of this period are simple covalent molecules.',
    'NaCl اور MgCl₂ آئنک ہیں اور کمرے کے درجۂ حرارت پر بڑی آئنک جالیوں پر مشتمل ہیں۔ درجۂ حرارت بڑھنے سے ساختی تبدیلیوں کی وجہ سے AlCl₃ پیچیدہ ہے۔ اس کی ساخت آئنک جالی ہے، اگرچہ اس میں کافی اشتراکی خصوصیت بھی ہے۔ PCl₅ ساختی طور پر زیادہ پیچیدہ ہے۔ اس دور کے دوسرے عناصر کے کلورائیڈز سادہ اشتراکی سالمے ہیں۔',
    'NaCl او MgCl₂ ایوني دي او د خونې په تودوخه کې له لویو ایوني جالیو جوړ دي. AlCl₃ د تودوخې په زیاتېدو سره د جوړښتي بدلونونو له امله پېچلی دی. جوړښت یې ایوني جالۍ ده، خو ډېره کووالنټ ځانګړنه هم لري. PCl₅ په جوړښتي لحاظ لا پېچلی دی. د دې دورې د نورو عناصرو کلورایډونه ساده کووالنټ مالیکولونه دي.')
head('13.1.5.2 Melting and Boiling Points','13.1.5.2 پگھلنے اور ابلنے کے درجے','13.1.5.2 د وېلې کېدو او اېشېدو ټکي')
add('NaCl and MgCl₂ are ionic and solids with high melting and boiling points. Large amount of heat is needed to break the strong ionic attractions.',
    'NaCl اور MgCl₂ آئنک، ٹھوس مادے ہیں جن کے پگھلنے اور ابلنے کے درجے زیادہ ہیں۔ مضبوط آئنک کشش توڑنے کے لیے بہت زیادہ حرارت درکار ہے۔',
    'NaCl او MgCl₂ ایوني جامدونه دي چې د وېلې کېدو او اېشېدو ټکي یې لوړ دي. د پیاوړو ایوني کششونو د ماتولو لپاره ډېره تودوخه اړینه ده.')
add('AlCl₃ is solid at room temperature, has an ionic lattice with a considerable covalent character. At 180 – 190°C (depending on the pressure), aluminium chloride converts to molecular form (dimeric form), Al₂Cl₆.',
    'AlCl₃ کمرے کے درجۂ حرارت پر ٹھوس ہے اور اس کی آئنک جالی میں قابلِ ذکر اشتراکی خصوصیت ہے۔ 180–190°C پر (دباؤ کے لحاظ سے) ایلومینیم کلورائیڈ سالماتی صورت (ڈائی مر صورت)، Al₂Cl₆، میں بدلتا ہے۔',
    'AlCl₃ د خونې په تودوخه کې جامد دی او ایوني جالۍ یې د پام وړ کووالنټ ځانګړنه لري. په 180–190°C کې (په فشار پورې اړه لري) المونیم کلورایډ مالیکولي بڼې (ډایمري بڼې)، Al₂Cl₆، ته بدلېږي.')
add('PCl₅ is a white solid, which sublimes at 163°C. As the temperature goes higher, the PCl₅ dissociates (splits up reversibly) to give PCl₃ and Cl₂.',
    'PCl₅ سفید ٹھوس مادہ ہے جو 163°C پر تصعید کرتا ہے۔ درجۂ حرارت مزید بڑھنے پر یہ قابلِ واپسی طور پر ٹوٹ کر PCl₃ اور Cl₂ بناتا ہے۔',
    'PCl₅ سپین جامد دی چې په 163°C کې تصعید کوي. د تودوخې په لا زیاتېدو سره PCl₅ په بېرته ګرځېدونکي ډول تجزیه کېږي او PCl₃ او Cl₂ جوړوي.')
eq('PCl₅(s) ⇌ PCl₃(l) + Cl₂(g)')
add('The rest are low melting point liquids.','باقی کم نقطۂ پگھلاؤ والے مائعات ہیں۔','پاتې یې د ټیټ وېلې کېدو ټکي لرونکي مایعات دي.')
head('13.1.5.3 Electrical Conductivity','13.1.5.3 برقی موصلیت','13.1.5.3 برېښنا لېږدونه')
add('NaCl and MgCl₂ are ionic in nature. They do not conduct electricity in solid state. But in molten state and aqueous solution these compounds conduct electricity.',
    'NaCl اور MgCl₂ کی نوعیت آئنک ہے۔ ٹھوس حالت میں یہ بجلی نہیں گزارتے، مگر پگھلی حالت اور آبی محلول میں بجلی گزارتے ہیں۔',
    'NaCl او MgCl₂ ایوني ماهیت لري. په جامد حالت کې برېښنا نه لېږدوي، خو په وېلې حالت او اوبلن محلول کې یې لېږدوي.')
add('AlCl₃ and PCl₅ do not conduct electricity in solid state, as the ions are not free to move. In the liquid state, they are converted into a covalent form and hence do not conduct electricity.',
    'AlCl₃ اور PCl₅ ٹھوس حالت میں بجلی نہیں گزارتے، کیونکہ ان کے آئن حرکت کرنے کے لیے آزاد نہیں ہوتے۔ مائع حالت میں یہ اشتراکی صورت میں بدل جاتے ہیں، اس لیے بجلی نہیں گزارتے۔',
    'AlCl₃ او PCl₅ په جامد حالت کې برېښنا نه لېږدوي، ځکه ایونونه یې د حرکت لپاره ازاد نه دي. په مایع حالت کې کووالنټ بڼې ته بدلېږي، نو برېښنا نه لېږدوي.')
add('The chlorides of rest of the elements of period 3ʳᵈ do not conduct electricity because they do not have any free ions or any free electrons to conduct electricity.',
    'تیسرے دور کے باقی عناصر کے کلورائیڈز بجلی نہیں گزارتے، کیونکہ بجلی گزارنے کے لیے ان میں آزاد آئن یا آزاد الیکٹران نہیں ہوتے۔',
    'د درېیمې دورې د پاتې عناصرو کلورایډونه برېښنا نه لېږدوي، ځکه د برېښنا د لېږدولو لپاره ازاد ایونونه یا ازاد الکترونونه نه لري.')
head('13.1.5.4 Solubility in Water','13.1.5.4 پانی میں حل پذیری','13.1.5.4 په اوبو کې د حل کېدو وړتیا')
add('NaCl dissolves in water and dissociates into ions to form a neutral solution of sodium chloride.',
    'NaCl پانی میں حل ہو کر آئنوں میں الگ ہوتا ہے اور سوڈیم کلورائیڈ کا غیر جانبدار محلول بناتا ہے۔',
    'NaCl په اوبو کې حل کېږي او په ایونونو وېشل کېږي، چې د سوډیم کلورایډ خنثی محلول جوړوي.')
eq('NaCl(s) —H₂O→ Na⁺(aq) + Cl⁻(aq)')
add('MgCl₂ dissolves in water and dissociates into ions to form a solution of magnesium chloride',
    'MgCl₂ پانی میں حل ہو کر آئنوں میں الگ ہوتا ہے اور میگنیشیم کلورائیڈ کا محلول بناتا ہے۔',
    'MgCl₂ په اوبو کې حل کېږي او په ایونونو وېشل کېږي، چې د مګنیزیم کلورایډ محلول جوړوي.')
eq('MgCl₂(s) —H₂O→ Mg²⁺(aq) + 2Cl⁻(aq)')
add('AlCl₃ is hydrolysed (broken down by water) to give an acidic solution containing the complex species hexaaqua aluminium (III).',
    'AlCl₃ کی آب پاشیدگی ہوتی ہے (پانی اسے توڑتا ہے) اور تیزابی محلول بنتا ہے، جس میں پیچیدہ نوع ہیکسا ایکوا ایلومینیم (III) ہوتی ہے۔',
    'AlCl₃ هایدرولیز کېږي (د اوبو په وسیله تجزیه کېږي) او تېزابي محلول جوړوي، چې پېچلی ډول هېکسا اکووا المونیم (III) پکې وي.')
eq('AlCl₃(s) + 6H₂O(l) → [Al(H₂O)₆]³⁺(aq) + 3Cl⁻(aq)')
add('The acidity is caused by the high charge density of aluminium ion (Al³⁺) polarising the water ligands (attached molecules), releasing free hydrogen ions into solution:',
    'ایلومینیم آئن (Al³⁺) کی زیادہ بار کثافت پانی کے لیگنڈز (جڑے ہوئے سالموں) کو قطبی بناتی ہے اور محلول میں آزاد ہائیڈروجن آئن خارج کرتی ہے؛ اسی سے تیزابیت پیدا ہوتی ہے:',
    'د المونیم ایون (Al³⁺) د چارج لوړه کثافت د اوبو لیګنډونه (تړلي مالیکولونه) قطبي کوي او محلول ته ازاد هایدروجن ایونونه خوشې کوي؛ له دې امله تېزابیت پیدا کېږي:')
eq('[Al(H₂O)₆]³⁺(aq) → [Al(H₂O)₅OH]²⁺(aq) + H⁺(aq)')
add('Silicon tetrachloride (SiCl₄), reacts very rapidly with water to form a strongly acidic solution. During the reaction, white fumes of hydrogen chloride gas are formed which dissolves in water forming hydrochloric acid.',
    'سلیکان ٹیٹرا کلورائیڈ (SiCl₄) پانی کے ساتھ بہت تیزی سے تعامل کر کے شدید تیزابی محلول بناتا ہے۔ تعامل میں ہائیڈروجن کلورائیڈ گیس کے سفید دھوئیں بنتے ہیں، جو پانی میں حل ہو کر ہائیڈروکلورک ایسڈ بناتے ہیں۔',
    'سیلیکان ټېټراکلورایډ (SiCl₄) له اوبو سره ډېر ژر تعامل کوي او پیاوړی تېزابي محلول جوړوي. د تعامل پر مهال د هایدروجن کلورایډ ګاز سپین لوګي جوړېږي، چې په اوبو کې حل کېږي او هایدروکلوریک اسید جوړوي.')
eq('SiCl₄(l) + 4H₂O(l) → Si(OH)₄(aq) + 4HCl(g)')
add('silicic acid','سیلیسک ایسڈ','سیلیسیک اسید')
add('Both of the phosphorus chlorides i.e. PCl₃ and PCl₅, violently react with water giving strongly acidic solutions. During the reaction, white fumes of hydrogen chloride gas are formed which dissolves in water forming hydrochloric acid.',
    'فاسفورس کے دونوں کلورائیڈز، PCl₃ اور PCl₅، پانی کے ساتھ شدت سے تعامل کر کے شدید تیزابی محلول بناتے ہیں۔ تعامل میں ہائیڈروجن کلورائیڈ گیس کے سفید دھوئیں بنتے ہیں، جو پانی میں حل ہو کر ہائیڈروکلورک ایسڈ بناتے ہیں۔',
    'د فاسفورس دواړه کلورایډونه، PCl₃ او PCl₅، له اوبو سره په شدت تعامل کوي او پیاوړي تېزابي محلولونه جوړوي. د تعامل پر مهال د هایدروجن کلورایډ ګاز سپین لوګي جوړېږي، چې په اوبو کې حل کېږي او هایدروکلوریک اسید جوړوي.')
record=section('13.7','13.1.5 Chlorides of the Period 3ʳᵈ Elements','13.1.5 تیسرے دور کے عناصر کے کلورائیڈز','13.1.5 د درېیمې دورې د عناصرو کلورایډونه',paras,layout,blocks,'14–15')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':11,'printedPages':[14,15]}]
issues=[{'id':'chem12-p14-chlorate-name','printedPage':14,'description':'Dichlorine heptoxide prose names sodium chlorate, while its printed equation gives NaClO4 (perchlorate). Both printed forms retained.'}]
if __name__=='__main__':save(11,[record],issues=issues,carry=[{'from':'13.7','to':'13.8','startsAt':'PC130\n+3H2O'}])
