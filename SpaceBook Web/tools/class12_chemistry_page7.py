"""Source-aligned PDF7: printed pages 6–7."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def table(identity,en,ur,ps,headers,urheaders,psheaders,rows,urrows,psrows):
    add(en,ur,ps)
    blocks.append({'id':identity,'headers':headers,'rows':rows,'translations':[{'language':'اردو','headers':urheaders,'rows':urrows},{'language':'پښتو','headers':psheaders,'rows':psrows}]})
    layout.append({'type':'sourceDataTable','tableId':identity})
syms=['₁₁Na','₁₂Mg','₁₃Al','₁₄Si','₁₅P','₁₆S','₁₇Cl','₁₈Ar']
add('Thus, more energy is required to remove the electron from the outermost shell of the atom resulting in an increase of ionization energy. The first ionization energy values of period 3 elements are given below.',
    'چنانچہ ایٹم کے سب سے بیرونی خول سے الیکٹران نکالنے کے لیے زیادہ توانائی درکار ہوتی ہے، جس سے آئنائزیشن توانائی بڑھتی ہے۔ تیسرے دور کے عناصر کی پہلی آئنائزیشن توانائی کی قدریں نیچے دی گئی ہیں۔',
    'نو د اټوم له تر ټولو بهرني پوښ څخه د الکترون د ایستلو لپاره ډېره انرژي اړینه وي، چې د ایون کېدو انرژي زیاتوي. د درېیمې دورې د عناصرو د لومړۍ ایون کېدو انرژۍ ارزښتونه لاندې ورکړل شوي دي.')
values=['495','737','577','786','1011','1000','1251','1520']
table('chem12-table-13-4','Table 13.4 First Ionization Energy Values of Period 3ʳᵈ Elements','جدول 13.4 تیسرے دور کے عناصر کی پہلی آئنائزیشن توانائی کی قدریں','جدول 13.4 د درېیمې دورې د عناصرو د لومړۍ ایون کېدو انرژۍ ارزښتونه',
      ['Elements of period 3ʳᵈ']+syms,['تیسرے دور کے عناصر']+syms,['د درېیمې دورې عناصر']+syms,
      [['1ˢᵗ ionization energy (kJ mol⁻¹)']+values],[['پہلی آئنائزیشن توانائی (kJ mol⁻¹)']+values],[['د لومړۍ ایون کېدو انرژي (kJ mol⁻¹)']+values])
head('Tidbit','مختصر معلومات','لنډ معلومات')
head('Screening effect or shielding effect','اسکریننگ اثر یا حائلی اثر','د پردې یا حایل اغېز')
add('In a multi-electron atom, the electrons in the valence shell are attracted to the nucleus. Like same charges repel, so these electrons are repelled by the electrons present in the inner shells. On account of this, the force of attraction between the nucleus and the valence electrons decrease. This decrease in the force of attraction on the valence electrons due to the presence of electrons in the inner shells is called screening effect or shielding effect.',
    'کئی الیکٹرانوں والے ایٹم میں ظرفی خول کے الیکٹران مرکزے کی طرف کھنچتے ہیں۔ یکساں بار ایک دوسرے کو دور دھکیلتے ہیں، اس لیے اندرونی خولوں کے الیکٹران ان الیکٹرانوں کو دور دھکیلتے ہیں۔ اس وجہ سے مرکزے اور ظرفی الیکٹرانوں کے درمیان کشش کم ہوتی ہے۔ اندرونی خولوں کے الیکٹرانوں کی موجودگی سے ظرفی الیکٹرانوں پر کشش کی یہ کمی اسکریننگ اثر یا حائلی اثر کہلاتی ہے۔',
    'په څو الکتروني اټوم کې د ظرفیت پوښ الکترونونه هستې ته جذبېږي. یو شان چارجونه یو بل دفع کوي، نو د داخلي پوښونو الکترونونه دا الکترونونه دفع کوي. له همدې امله د هستې او د ظرفیت الکترونونو ترمنځ کششي قوه کمېږي. د داخلي پوښونو د الکترونونو د شتون له امله پر ظرفيتي الکترونونو د کششي قوې دا کمښت د پردې یا حایل اغېز بلل کېږي.')
add('The magnitude of the screening effect depends upon the number of inner electrons higher the number of inner electrons greater shall be the value of the screening effect. As we move downward in the group the number of shells increases gradually between the nucleus and the valence shell. These shells act like shields. These shells protect the electrons from the attraction of the nucleus.',
    'اسکریننگ اثر کی مقدار اندرونی الیکٹرانوں کی تعداد پر منحصر ہے؛ اندرونی الیکٹران جتنے زیادہ ہوں، اسکریننگ اثر اتنا زیادہ ہوتا ہے۔ گروپ میں نیچے جانے پر مرکزے اور ظرفی خول کے درمیان خولوں کی تعداد بتدریج بڑھتی ہے۔ یہ خول ڈھالوں کی طرح کام کرتے ہیں اور الیکٹرانوں کو مرکزے کی کشش سے بچاتے ہیں۔',
    'د پردې اغېز اندازه د داخلي الکترونونو په شمېر پورې اړه لري؛ هر څومره چې داخلي الکترونونه ډېر وي، د پردې اغېز هم هغومره ډېر وي. په ګروپ کې ښکته تګ سره د هستې او ظرفیت پوښ ترمنځ د پوښونو شمېر په تدریجي ډول زیاتېږي. دا پوښونه د ډالونو په څېر عمل کوي او الکترونونه د هستې له کشش څخه ساتي.')
head('13.1.1.4 Trend in Electronegativity','13.1.1.4 برقی منفیت کا رجحان','13.1.1.4 د برېښنا منفي توب تمایل')
head('Electronegativity','برقی منفیت','برېښنا منفي توب')
add('The relative tendency of an atom to attract a shared electron pair towards itself is called its electronegativity.',
    'کسی ایٹم کا مشترکہ الیکٹرانی جوڑے کو اپنی طرف کھینچنے کا نسبتی رجحان اس کی برقی منفیت کہلاتا ہے۔',
    'د یوه اټوم هغه نسبي تمایل چې ګډه الکتروني جوړه ځان ته راکاږي، د هغه برېښنا منفي توب بلل کېږي.')
head('Periodic Trends','دوری رجحانات','دوراني تمایلات')
add('In general, electronegativity decreases on moving from top to bottom in a group and increases from left to right in a period.',
    'عموماً گروپ میں اوپر سے نیچے جانے پر برقی منفیت کم ہوتی ہے اور دور میں بائیں سے دائیں جانے پر بڑھتی ہے۔',
    'په عمومي ډول، په ګروپ کې له پاس څخه ښکته تګ سره برېښنا منفي توب کمېږي او په دوره کې له کیڼ څخه ښي لوري ته تګ سره زیاتېږي.')
head('(a) Variation in a Group','(a) گروپ میں تبدیلی','(a) په یوه ګروپ کې بدلون')
add('As we move in a group from top to bottom, there is an increase in the atomic size, nuclear charge and shielding effect.',
    'گروپ میں اوپر سے نیچے جانے پر ایٹمی جسامت، مرکزی بار اور حائلی اثر بڑھتے ہیں۔',
    'په ګروپ کې له پاس څخه ښکته تګ سره اټومي اندازه، هستوي چارج او د پردې اغېز زیاتېږي.')
add('However, the combined effect of increase in atomic size, nuclear charge and shielding effect results in decrease in the force of attraction of the nucleus for the shared pair of electrons, the electronegativity decreases.',
    'تاہم ایٹمی جسامت، مرکزی بار اور حائلی اثر میں اضافے کا مشترکہ اثر مشترکہ الیکٹرانی جوڑے پر مرکزے کی کشش کم کرتا ہے، اس لیے برقی منفیت کم ہوتی ہے۔',
    'خو د اټومي اندازې، هستوي چارج او د پردې اغېز د زیاتېدو ګډ اغېز د ګډې الکتروني جوړې لپاره د هستې کششي قوه کموي، نو برېښنا منفي توب کمېږي.')
head('(b) Variation in a Period','(b) دور میں تبدیلی','(b) په یوه دوره کې بدلون')
add('As we move in a period from left to right, there is no change in the number of shells but effective nuclear charge increases. This results in decrease in atomic size and hence electronegativity increases.',
    'دور میں بائیں سے دائیں جانے پر خولوں کی تعداد نہیں بدلتی، مگر مؤثر مرکزی بار بڑھتا ہے۔ اس سے ایٹمی جسامت کم اور برقی منفیت زیادہ ہوتی ہے۔',
    'په دوره کې له کیڼ څخه ښي لوري ته تګ سره د پوښونو شمېر نه بدلېږي، خو اغېزمن هستوي چارج زیاتېږي. له دې امله اټومي اندازه کمېږي او برېښنا منفي توب زیاتېږي.')
add('Fluorine (F) is the most electronegative element and Caesium (Cs) is the least electronegative element in the periodic table. Electronegativity values of period 3 elements are given in the table.',
    'دوری جدول میں فلورین (F) کی برقی منفیت سب سے زیادہ اور سیزیم (Cs) کی سب سے کم ہے۔ تیسرے دور کے عناصر کی برقی منفیت کی قدریں جدول میں دی گئی ہیں۔',
    'په دوراني جدول کې فلورین (F) تر ټولو ډېر او سیزیم (Cs) تر ټولو لږ برېښنا منفي توب لري. د درېیمې دورې د عناصرو د برېښنا منفي توب ارزښتونه په جدول کې ورکړل شوي دي.')
values=['0.93','1.31','1.61','1.90','2.19','2.58','3.16','–']
table('chem12-table-13-5','Table 13.5 Trend in Electronegativity of 3ʳᵈ Period elements','جدول 13.5 تیسرے دور کے عناصر کی برقی منفیت کا رجحان','جدول 13.5 د درېیمې دورې د عناصرو د برېښنا منفي توب تمایل',
      ['Elements of period 3ʳᵈ']+syms,['تیسرے دور کے عناصر']+syms,['د درېیمې دورې عناصر']+syms,
      [['Electronegativity']+values],[['برقی منفیت']+values],[['برېښنا منفي توب']+values])
add('Note that electronegativity of argon (Ar) is not included. As the electronegativity is related to the tendency of an atom to attract the shared pair of electrons. As, argon does not form covalent bond(s), so no electronegativity value is assigned to argon (Ar).',
    'غور کریں کہ آرگن (Ar) کی برقی منفیت شامل نہیں کی گئی۔ برقی منفیت کسی ایٹم کے مشترکہ الیکٹرانی جوڑے کو کھینچنے کے رجحان سے متعلق ہے۔ چونکہ آرگن اشتراکی بند نہیں بناتا، اس لیے آرگن (Ar) کو برقی منفیت کی کوئی قدر نہیں دی گئی۔',
    'پام وکړئ چې د ارګون (Ar) برېښنا منفي توب نه دی شامل شوی. برېښنا منفي توب د اټوم له هغه تمایل سره تړاو لري چې ګډه الکتروني جوړه راکاږي. څرنګه چې ارګون کووالنټ تړون نه جوړوي، نو ارګون (Ar) ته د برېښنا منفي توب ارزښت نه دی ټاکل شوی.')
head('13.1.1.5 Trend in Electrical Conductivity','13.1.1.5 برقی موصلیت کا رجحان','13.1.1.5 د برېښنا لېږدونې تمایل')
head('Electrical Conductivity','برقی موصلیت','برېښنا لېږدونه')
add('Electrical conductivity is the measure of the amount of electrical current a material can carry.',
    'برقی موصلیت اس برقی رو کی مقدار کا پیمانہ ہے جو کوئی مادہ منتقل کر سکتا ہے۔',
    'برېښنا لېږدونه د هغې برېښنايي جریان د مقدار اندازه ده چې یو ماده یې لېږدولای شي.')
add('Electrical conductivity values of period 3 elements relative to aluminium are given below.',
    'ایلومینیم کے مقابلے میں تیسرے دور کے عناصر کی برقی موصلیت کی قدریں نیچے دی گئی ہیں۔',
    'له المونیم سره په پرتله کې د درېیمې دورې د عناصرو د برېښنا لېږدونې ارزښتونه لاندې ورکړل شوي دي.')
values=['0.55','0.61','1.00','0.10','0','0','0','0']
table('chem12-table-13-6-conductivity','Table 13.6 Trend in Electrical Conductivity in 3ʳᵈ Period Elements','جدول 13.6 تیسرے دور کے عناصر میں برقی موصلیت کا رجحان','جدول 13.6 د درېیمې دورې په عناصرو کې د برېښنا لېږدونې تمایل',
      ['Elements of period 3ʳᵈ']+syms,['تیسرے دور کے عناصر']+syms,['د درېیمې دورې عناصر']+syms,
      [['Electrical conductivity']+values],[['برقی موصلیت']+values],[['برېښنا لېږدونه']+values])
add('Sodium, magnesium and aluminium are all metals and are good conductors of electricity. These metals conduct electricity because they contain free electrons. Going from sodium to aluminium, the number of free electrons increases and thus the electrical conductivity increases. Silicon has a giant covalent structure. It is a semiconductor, so it is not a good conductor. Phosphorus, sulphur, chlorine and argon are non-conductor as they are non-metals.',
    'سوڈیم، میگنیشیم اور ایلومینیم سب دھاتیں اور بجلی کے اچھے موصل ہیں۔ یہ دھاتیں بجلی منتقل کرتی ہیں، کیونکہ ان میں آزاد الیکٹران ہوتے ہیں۔ سوڈیم سے ایلومینیم تک آزاد الیکٹرانوں کی تعداد بڑھتی ہے، اس لیے برقی موصلیت بڑھتی ہے۔ سلیکان کی بڑی اشتراکی ساخت ہے۔ یہ نیم موصل ہے، اس لیے اچھا موصل نہیں۔ فاسفورس، سلفر، کلورین اور آرگن غیر موصل ہیں، کیونکہ یہ غیر دھاتیں ہیں۔',
    'سوډیم، مګنیزیم او المونیم ټول فلزونه او د برېښنا ښه لېږدوونکي دي. دا فلزونه برېښنا لېږدوي، ځکه ازاد الکترونونه لري. له سوډیم څخه المونیم ته د ازادو الکترونونو شمېر زیاتېږي، نو برېښنا لېږدونه زیاتېږي. سیلیکان لوی کووالنټ جوړښت لري. دا نیمه هادي دی، نو ښه لېږدوونکی نه دی. فاسفورس، سلفر، کلورین او ارګون برېښنا نه لېږدوي، ځکه نافلزونه دي.')
head('13.1.1.6 Trend in Melting and Boiling Points','13.1.1.6 پگھلنے اور ابلنے کے درجوں کا رجحان','13.1.1.6 د وېلې کېدو او اېشېدو د ټکو تمایل')
add('The following table shows melting points and boiling points for the elements Na to Ar. Melting points and boiling points tell us how strongly the atoms in an element are held together.',
    'درج ذیل جدول Na سے Ar تک کے عناصر کے پگھلنے اور ابلنے کے درجے دکھاتا ہے۔ یہ درجے بتاتے ہیں کہ کسی عنصر کے ایٹم کتنی مضبوطی سے ایک دوسرے سے جڑے ہیں۔',
    'لاندې جدول له Na څخه تر Ar پورې د عناصرو د وېلې کېدو او اېشېدو ټکي ښيي. دا ټکي راښيي چې په یوه عنصر کې اټومونه څومره ټینګ سره تړلي دي.')
values1=['98','651','660','1410','44(white)','119','−103','−189'];values2=['883','1107','2470','2355','260','445','−35','−486']
table('chem12-table-13-6-thermal','Table 13.6 Trend in Electrical Conductivity in 3ʳᵈ Period Elements','جدول 13.6 تیسرے دور کے عناصر میں برقی موصلیت کا رجحان','جدول 13.6 د درېیمې دورې په عناصرو کې د برېښنا لېږدونې تمایل',
      ['Elements of period 3ʳᵈ','Na','Mg','Al','Si','P','S','Cl','Ar'],['تیسرے دور کے عناصر','Na','Mg','Al','Si','P','S','Cl','Ar'],['د درېیمې دورې عناصر','Na','Mg','Al','Si','P','S','Cl','Ar'],
      [['Melting point °C']+values1,['Boiling point °C']+values2],
      [['نقطۂ پگھلاؤ °C']+values1[:4]+['44(سفید)']+values1[5:],['نقطۂ ابال °C']+values2],
      [['د وېلې کېدو ټکی °C']+values1[:4]+['44(سپین)']+values1[5:],['د اېشېدو ټکی °C']+values2])
add('Sodium, magnesium and aluminium have metallic bonding, in which the nuclei of metal atoms are attracted by free electrons. Going from sodium to aluminium, the number of free electrons increases and the melting and boiling points also increase. Silicon is a metalloid with a giant covalent structure. Silicon has a very high melting and boiling points because of strong covalent bonds. P, S, Cl and Ar in period 3 are non-metals and have low melting and boiling points because they have weak Van der Waal’s forces between their molecules.',
    'سوڈیم، میگنیشیم اور ایلومینیم میں دھاتی بند ہوتے ہیں، جن میں دھاتی ایٹموں کے مرکزے آزاد الیکٹرانوں سے کشش رکھتے ہیں۔ سوڈیم سے ایلومینیم تک آزاد الیکٹرانوں کی تعداد بڑھتی ہے اور پگھلنے اور ابلنے کے درجے بھی بڑھتے ہیں۔ سلیکان ایک نیم دھات ہے جس کی بڑی اشتراکی ساخت ہے۔ مضبوط اشتراکی بندوں کی وجہ سے اس کے پگھلنے اور ابلنے کے درجے بہت زیادہ ہیں۔ تیسرے دور کے P، S، Cl اور Ar غیر دھاتیں ہیں اور ان کے سالموں کے درمیان کمزور وان ڈر والز قوتوں کی وجہ سے ان کے پگھلنے اور ابلنے کے درجے کم ہیں۔',
    'سوډیم، مګنیزیم او المونیم فلزي تړونونه لري، چې پکې د فلزي اټومونو هستې د ازادو الکترونونو له خوا جذبېږي. له سوډیم څخه المونیم ته د ازادو الکترونونو شمېر زیاتېږي او د وېلې کېدو او اېشېدو ټکي هم لوړېږي. سیلیکان نیمه فلز دی او لوی کووالنټ جوړښت لري. د پیاوړو کووالنټ تړونونو له امله د سیلیکان د وېلې کېدو او اېشېدو ټکي ډېر لوړ دي. په درېیمه دوره کې P، S، Cl او Ar نافلزونه دي او د مالیکولونو ترمنځ د کمزورو وان در والس قوو له امله د وېلې کېدو او اېشېدو ټکي یې ټیټ دي.')
record=section('13.3','Ionization energy, electronegativity and physical trends','آئنائزیشن توانائی، برقی منفیت اور طبعی رجحانات','د ایون کېدو انرژي، برېښنا منفي توب او فزیکي تمایلات',paras,layout,blocks,'6–7')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':7,'printedPages':[6,7]}]
issues=[{'id':'chem12-p7-thermal-caption','printedPage':7,'description':'The melting/boiling table repeats number 13.6 and the electrical-conductivity caption. Printed number and wording retained, with unique coded table IDs.'},
        {'id':'chem12-p7-argon-boiling','printedPage':7,'description':'Argon boiling point is printed −486 °C. Printed value retained; flagged as a source numerical inconsistency.'}]
if __name__=='__main__':save(7,[record],issues=issues)
