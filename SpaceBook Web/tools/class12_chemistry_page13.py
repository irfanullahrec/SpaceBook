"""PDF13: GroupIA configurations and property trends, printed18–19."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
rows=[['₃₇Rb','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s¹','[Kr]5s¹'],
      ['₅₅Cs','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s², 4d¹⁰, 5p⁶, 6s¹','[Xe]6s¹'],
      ['₈₇Fr','[Kr] 4d¹⁰, 5p⁶, 6s², 4f¹⁴, 5d¹⁰, 6p⁶, 7s¹','[Rn]7s¹']]
t={'id':'chem12-table-13-11-continuation','noHeader':True,'headers':[],'rows':rows,'translations':[{'language':lang,'headers':[],'rows':rows} for lang in ['اردو','پښتو']]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
def table(number,caption,urcaption,pscaption,labels,ur_labels,ps_labels,values):
    add(caption,urcaption,pscaption)
    t={'id':f'chem12-table-13-{number}','headers':['Elements','Li','Na','K','Rb','Cs'],'rows':[[label]+row for label,row in zip(labels,values)],
       'translations':[{'language':'اردو','headers':['عناصر','Li','Na','K','Rb','Cs'],'rows':[[label]+row for label,row in zip(ur_labels,values)]},
                       {'language':'پښتو','headers':['عناصر','Li','Na','K','Rb','Cs'],'rows':[[label]+row for label,row in zip(ps_labels,values)]}]}
    blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
add('Like all metals, they are good conductor of heat and electricity. They are softer than other metals. They can be cut with a knife. They are lighter than other elements and have low melting points, boiling points and densities.',
    'تمام دھاتوں کی طرح یہ حرارت اور بجلی کے اچھے موصل ہیں۔ یہ دوسری دھاتوں سے نرم ہیں اور چاقو سے کاٹے جا سکتے ہیں۔ دوسرے عناصر سے ہلکے ہیں اور ان کے پگھلنے اور ابلنے کے درجے اور کثافتیں کم ہیں۔',
    'د ټولو فلزونو په څېر، دا د تودوخې او برېښنا ښه لېږدوونکي دي. له نورو فلزونو نرم دي او په چاړه پرې کېدای شي. له نورو عناصرو سپک دي او د وېلې کېدو او اېشېدو ټکي او کثافتونه یې ټیټ دي.')
head('13.2.1 Atomic and Physical Properties','13.2.1 ایٹمی اور طبعی خصوصیات','13.2.1 اټومي او فزیکي ځانګړنې')
add('The elements in a group behave in similar way but they also show trends of variations in properties as given below.',
    'کسی گروپ کے عناصر یکساں انداز میں برتاؤ کرتے ہیں، مگر ان کی خصوصیات میں تبدیلیوں کے رجحانات بھی ظاہر ہوتے ہیں، جیسا کہ نیچے دیا گیا ہے۔',
    'په یوه ګروپ کې عناصر په ورته ډول چلند کوي، خو په ځانګړنو کې د بدلون تمایلات هم ښيي، لکه لاندې چې ورکړل شوي دي.')
head('13.2.1.1 Trend in Atomic Radius','13.2.1.1 ایٹمی رداس کا رجحان','13.2.1.1 د اټومي شعاع تمایل')
add('As we move in group from lithium to caesium, an extra shell of electrons is added to next element. The addition of extra shells increases the atomic radius from Li to Cs.',
    'گروپ میں لیتھیم سے سیزیم تک جانے پر اگلے عنصر میں الیکٹرانوں کا ایک اضافی خول شامل ہوتا ہے۔ اضافی خولوں کی وجہ سے Li سے Cs تک ایٹمی رداس بڑھتا ہے۔',
    'په ګروپ کې له لیتیم څخه سیزیم ته تګ سره په راتلونکي عنصر کې د الکترونونو یو اضافي پوښ زیاتېږي. د اضافي پوښونو زیاتېدل له Li څخه Cs ته اټومي شعاع لویوي.')
table(12,'Table 13.12 Trend in Atomic Radius in Group IA Elements','جدول 13.12 گروپ IA کے عناصر میں ایٹمی رداس کا رجحان','جدول 13.12 د IA ګروپ په عناصرو کې د اټومي شعاع تمایل',['Atomic Radius (pm)'],['ایٹمی رداس (pm)'],['اټومي شعاع (pm)'],[['152','186','227','248','265']])
head('13.2.1.2 Trend in First Ionization Energy','13.2.1.2 پہلی آئنائزیشن توانائی کا رجحان','13.2.1.2 د لومړۍ ایون کېدو انرژۍ تمایل')
add('As we move in group from lithium to caesium the ionization energy decreases, due to the addition of extra shells from Li to Cs. So the removal of electron become easier.',
    'گروپ میں لیتھیم سے سیزیم تک آئنائزیشن توانائی کم ہوتی ہے، کیونکہ Li سے Cs تک اضافی خول شامل ہوتے ہیں۔ اس لیے الیکٹران نکالنا آسان ہوتا جاتا ہے۔',
    'په ګروپ کې له لیتیم څخه سیزیم ته د ایون کېدو انرژي کمېږي، ځکه له Li څخه Cs ته اضافي پوښونه زیاتېږي. نو د الکترون ایستل اسانه کېږي.')
table(13,'Table 13.13 Trend in First Ionization Energy in Group IA Elements','جدول 13.13 گروپ IA کے عناصر میں پہلی آئنائزیشن توانائی کا رجحان','جدول 13.13 د IA ګروپ په عناصرو کې د لومړۍ ایون کېدو انرژۍ تمایل',['1ˢᵗ Ionization Energy (kJ/mol)'],['پہلی آئنائزیشن توانائی (kJ/mol)'],['د لومړۍ ایون کېدو انرژي (kJ/mol)'],[['520','496','419','403','376']])
head('13.2.1.3 Trend in Electronegativity','13.2.1.3 برقی منفیت کا رجحان','13.2.1.3 د برېښنا منفي توب تمایل')
add('Elements of group – IA are metals and are highly electropositive, so their electronegativity values are very low. As we move in group from lithium to caesium their electronegativities decrease in the same order.',
    'گروپ IA کے عناصر دھاتیں ہیں اور بہت زیادہ برقی مثبت ہیں، اس لیے ان کی برقی منفیت کی قدریں بہت کم ہیں۔ گروپ میں لیتھیم سے سیزیم تک ان کی برقی منفیت اسی ترتیب میں کم ہوتی ہے۔',
    'د IA ګروپ عناصر فلزونه دي او ډېر برېښنا مثبت دي، نو د برېښنا منفي توب ارزښتونه یې ډېر ټیټ دي. په ګروپ کې له لیتیم څخه سیزیم ته د هغوی برېښنا منفي توب په همدې ترتیب کمېږي.')
table(14,'Table 13.14 Trend in Electronegativity in Group IA Elements','جدول 13.14 گروپ IA کے عناصر میں برقی منفیت کا رجحان','جدول 13.14 د IA ګروپ په عناصرو کې د برېښنا منفي توب تمایل',['Electronegativity'],['برقی منفیت'],['برېښنا منفي توب'],[['0.98','0.93','0.82','0.82','0.79']])
head('13.2.1.4 Trend in Melting and Boiling Points','13.2.1.4 پگھلنے اور ابلنے کے درجوں کا رجحان','13.2.1.4 د وېلې کېدو او اېشېدو د ټکو تمایل')
add('The binding forces between the atoms in crystal lattice of these metals are relatively weak. So these metals are soft and possess low melting and boiling points, which decrease down the group.',
    'ان دھاتوں کی قلمی جالی میں ایٹموں کے درمیان بندش کی قوتیں نسبتاً کمزور ہیں۔ اس لیے یہ دھاتیں نرم ہیں اور ان کے پگھلنے اور ابلنے کے درجے کم ہیں، جو گروپ میں نیچے جانے پر کم ہوتے ہیں۔',
    'د دې فلزونو په بلوري جالۍ کې د اټومونو ترمنځ تړونکې قوې نسبتاً کمزورې دي. نو دا فلزونه نرم دي او د وېلې کېدو او اېشېدو ټیټ ټکي لري، چې په ګروپ کې ښکته تګ سره ټیټېږي.')
table(15,'Table 13.15 Trend in Melting and Boiling Points in Group IA Elements','جدول 13.15 گروپ IA کے عناصر میں پگھلنے اور ابلنے کے درجوں کا رجحان','جدول 13.15 د IA ګروپ په عناصرو کې د وېلې کېدو او اېشېدو د ټکو تمایل',['Melting point (°C)','Boiling point (°C)'],['نقطۂ پگھلاؤ (°C)','نقطۂ ابال (°C)'],['د وېلې کېدو ټکی (°C)','د اېشېدو ټکی (°C)'],[['180.5','97.8','63.7','39.0','28.6'],['1,326','883','756','688','690']])
head('13.2.1.5 Trend in Density','13.2.1.5 کثافت کا رجحان','13.2.1.5 د کثافت تمایل')
add('Density is defined as mass per unit volume of a substance.','کثافت کسی مادے کے فی اکائی حجم کمیت کو کہتے ہیں۔','کثافت د یوې مادې په واحد حجم کې کتلې ته ویل کېږي.')
add('Density increases with an increase in atomic mass and decreases with an increase in atomic volume.',
    'ایٹمی کمیت بڑھنے سے کثافت بڑھتی ہے اور ایٹمی حجم بڑھنے سے کم ہوتی ہے۔',
    'د اټومي کتلې په زیاتېدو سره کثافت زیاتېږي او د اټومي حجم په زیاتېدو سره کمېږي.')
add('Generally, we see that in alkali metals down the group, both the atomic size and atomic mass increase but the increase in atomic mass compensates the bigger atomic size. As a result, the density of alkali metals increases down the group. Potassium is, however, lighter than sodium.',
    'عموماً الکلی دھاتوں کے گروپ میں نیچے جانے پر ایٹمی جسامت اور کمیت دونوں بڑھتی ہیں، مگر کمیت میں اضافہ بڑی ایٹمی جسامت کی تلافی کرتا ہے۔ نتیجتاً گروپ میں نیچے الکلی دھاتوں کی کثافت بڑھتی ہے۔ تاہم پوٹاشیم سوڈیم سے ہلکا ہے۔',
    'په عمومي ډول، د القلي فلزونو په ګروپ کې ښکته تګ سره اټومي اندازه او کتله دواړه زیاتېږي، خو د اټومي کتلې زیاتوالی د لویې اټومي اندازې اغېز جبرانوي. په پایله کې په ګروپ کې ښکته د القلي فلزونو کثافت زیاتېږي. خو پوټاشیم له سوډیم څخه سپک دی.')
table(16,'Table 13.16 Trend in Density in Group IA Elements','جدول 13.16 گروپ IA کے عناصر میں کثافت کا رجحان','جدول 13.16 د IA ګروپ په عناصرو کې د کثافت تمایل',['Density at 20 °C (g/cm³)'],['20 °C پر کثافت (g/cm³)'],['په 20 °C کې کثافت (g/cm³)'],[['0.53','0.97','0.86','1.53','1.88']])
head('13.2.2 Trend in Reactivity with Water','13.2.2 پانی کے ساتھ تعامل پذیری کا رجحان','13.2.2 له اوبو سره د تعامل وړتیا تمایل')
add('Group – IA elements are very good reducing agents. They all react vigorously with water reducing it to hydrogen gas.',
    'گروپ IA کے عناصر بہت اچھے اختزالی عوامل ہیں۔ یہ سب پانی کے ساتھ شدت سے تعامل کر کے اسے ہائیڈروجن گیس میں مختزل کرتے ہیں۔',
    'د IA ګروپ عناصر ډېر ښه ارجاع کوونکي عوامل دي. دا ټول له اوبو سره په شدت تعامل کوي او هغه هایدروجن ګاز ته ارجاع کوي.')
eq('M(s) → M⁺(aq) + 1e⁻')
eq('H₂O(l) + 1e⁻ → ½ H₂(g) + OH⁻(aq)')
eq('M(s) + H₂O(l) → MOH(aq) + ½ H₂(g)')
add('(Where M = Li, Na, K, Rb, Cs)','(جہاں M = Li، Na، K، Rb، Cs)','(چې M = Li، Na، K، Rb، Cs دی)')
add('Lithium reacts slowly with water while sodium reacts vigorously. Potassium reacts even more vigorously, while Rb and Cs explode violently in contact with water. They all on reaction with water produce the respective hydroxides.',
    'لیتھیم پانی کے ساتھ آہستہ، جبکہ سوڈیم شدت سے تعامل کرتا ہے۔ پوٹاشیم اس سے بھی زیادہ شدت سے تعامل کرتا ہے، جبکہ Rb اور Cs پانی کے رابطے میں زور سے پھٹتے ہیں۔ پانی سے تعامل کر کے یہ سب اپنے متعلقہ ہائیڈرو آکسائیڈز بناتے ہیں۔',
    'لیتیم له اوبو سره ورو او سوډیم په شدت تعامل کوي. پوټاشیم لا ډېر شدید تعامل کوي، خو Rb او Cs له اوبو سره په تماس کې په شدت چاودنه کوي. له اوبو سره په تعامل کې دا ټول خپل اړوند هایدروکسایډونه جوړوي.')
record=section('13.9','Group IA atomic and physical trends','گروپ IA کے ایٹمی اور طبعی رجحانات','د IA ګروپ اټومي او فزیکي تمایلات',paras,layout,blocks,'18–19')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':13,'printedPages':[18,19]}]
issues=[{'id':'chem12-p19-boiling-trend','printedPage':19,'description':'The prose says boiling points decrease down GroupIA, but the printed table gives Rb688°C and Cs690°C. Printed prose and both values retained.'}]
if __name__=='__main__':save(13,[record],issues=issues,carry=[{'from':'13.9','to':'13.10','startsAt':'13.2.3\nReactions with Oxygen'}])
