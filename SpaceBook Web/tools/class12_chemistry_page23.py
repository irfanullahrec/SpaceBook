"""PDF23 printed38–39, halogen properties; all five tables preserved."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(v):add(v,v,v,'equation')
def table(n,en,ur,ps,rows,urrows,psrows,headers=None):
    add(f'Table 13.{n} '+en,f'جدول 13.{n} '+ur,f'جدول 13.{n} '+ps)
    h=headers or ['Halogen','F','Cl','Br','I'];b={'id':f'chem12-table-13-{n}','headers':h,'rows':rows,'translations':[{'language':'اردو','headers':['ہیلوجن' if n!=29 else 'بند']+h[1:],'rows':urrows},{'language':'پښتو','headers':['هالوجن' if n!=29 else 'تړون']+h[1:],'rows':psrows}]};blocks.append(b);layout.append({'type':'sourceDataTable','tableId':b['id']})
add('Halogens in the uncombined state exist as diatomic covalent molecules (F₂, Cl₂ etc). These discrete molecules are held together by weak Van der Waals’s forces, which explain the volatile nature of these elements. These elements are also poisonous in nature.',
    'ہیلوجنز غیر مرکب حالت میں دو ایٹمی اشتراکی سالموں (F₂، Cl₂ وغیرہ) کی صورت میں ہوتے ہیں۔ یہ الگ الگ سالمے کمزور وان ڈر والز قوتوں سے جڑے رہتے ہیں، جو ان عناصر کی فرار پذیر نوعیت کی وضاحت کرتی ہیں۔ یہ عناصر زہریلے بھی ہیں۔',
    'هالوجنونه په نه ترکیب شوي حالت کې د دوه اټومي کووالنټ مالیکولونو (F₂، Cl₂ او نورو) په بڼه وي. دا جلا مالیکولونه د وان در والس د کمزورو قوو په وسیله سره ساتل کېږي، چې د دې عناصرو د ژر بخار کېدونکي ماهیت تشریح کوي. دا عناصر زهرجن هم دي.')
head('13.5.1.1 Trend in Atomic Radius','13.5.1.1 ایٹمی رداس کا رجحان','13.5.1.1 د اټومي شعاع تمایل')
add('Atomic radii of Group – VII A elements increase down the group as shown in Table 13.25.',
    'گروپ VIIA کے عناصر کے ایٹمی رداس گروپ میں نیچے بڑھتے ہیں، جیسا کہ جدول 13.25 میں دکھایا گیا ہے۔',
    'د VIIA ګروپ د عناصرو اټومي شعاعوې په ګروپ کې ښکته زیاتېږي، لکه په جدول 13.25 کې چې ښودل شوي.')
v=['71','99','114','133'];table(25,'Trend in Atomic Radius in Group –VIIA elements','گروپ VIIA کے عناصر میں ایٹمی رداس کا رجحان','د VIIA ګروپ په عناصرو کې د اټومي شعاع تمایل',[['Covalent Radius (pm)']+v],[['اشتراکی رداس (pm)']+v],[['کووالنټ شعاع (pm)']+v],['Halogen','₉F','₁₇Cl','₃₅Br','₅₃I'])
head('13.5.1.2 Trend in Electronegativity','13.5.1.2 برقی منفیت کا رجحان','13.5.1.2 د برېښنا منفي توب تمایل')
add('Electronegativity of Group–VII A elements decreases gradually from fluorine to iodine down the group as shown below.',
    'گروپ VIIA کے عناصر کی برقی منفیت گروپ میں نیچے فلورین سے آئیوڈین تک بتدریج کم ہوتی ہے، جیسا کہ ذیل میں دکھایا گیا ہے۔',
    'د VIIA ګروپ د عناصرو برېښنا منفي توب په ګروپ کې ښکته له فلورین څخه ایوډین ته ورو ورو کمېږي، لکه لاندې چې ښودل شوي.')
head('Tidbit','مختصر معلومات','لنډ معلومات')
add('Fluorine is the most electronegative element of the periodic table.','فلورین دوری جدول کا سب سے زیادہ برقی منفی عنصر ہے۔','فلورین د دوراني جدول تر ټولو ډېر برېښنا منفي عنصر دی.')
v=['4.0','3.0','2.8','2.5'];table(26,'Trend in Electronegativity in Group–VIIA Elements','گروپ VIIA کے عناصر میں برقی منفیت کا رجحان','د VIIA ګروپ په عناصرو کې د برېښنا منفي توب تمایل',[['Electronegativity']+v],[['برقی منفیت']+v],[['برېښنا منفي توب']+v])
head('13.5.1.3 Trend in Electron Affinity','13.5.1.3 الیکٹرون الفت کا رجحان','13.5.1.3 د الکترون میلان تمایل')
add('Electron affinity greatly influences the chemical behaviour of atoms by accepting one or more electrons. Electron affinity of an element is defined as “the amount of energy released when an electron is accepted by an atom in the gaseous state to form an anion,” i.e.',
    'ایک یا زیادہ الیکٹرون قبول کرنے کے ذریعے الیکٹرون الفت ایٹموں کے کیمیائی رویے کو بہت متاثر کرتی ہے۔ کسی عنصر کی الیکٹرون الفت کی تعریف ہے: «گیسی حالت میں کسی ایٹم کے ایک الیکٹرون قبول کر کے منفی آئن بنانے پر خارج ہونے والی توانائی کی مقدار»، یعنی:',
    'د یوه یا ډېرو الکترونونو په منلو سره د الکترون میلان د اټومونو پر کیمیاوي چلند ډېر اغېز لري. د یوه عنصر د الکترون میلان داسې تعریفېږي: «د هغې انرژۍ اندازه چې په ګازي حالت کې د یوه اټوم له خوا د الکترون په منلو او منفي ایون په جوړولو خوشې کېږي»، یعنې:')
eq('Cl(g) + e⁻ → Cl⁻(g)     ΔH = −349 kJmol⁻¹')
add('As the energy is released, so electron affinity is given the negative sign. Electron affinity is the measure of the attraction of the nucleus of an atom for the extra electron.',
    'چونکہ توانائی خارج ہوتی ہے، اس لیے الیکٹرون الفت کو منفی نشان دیا جاتا ہے۔ الیکٹرون الفت اضافی الیکٹرون کے لیے ایٹم کے مرکزے کی کشش کا پیمانہ ہے۔',
    'ځکه چې انرژي خوشې کېږي، د الکترون میلان ته منفي نښه ورکول کېږي. د الکترون میلان د اضافي الکترون لپاره د اټوم د هستې د کشش اندازه ده.')
head('a) Variation in a Group','a) گروپ میں تبدیلی','a) په ګروپ کې بدلون')
add('As we move in a group from top to bottom, there is an increase in the atomic size, nuclear charge and shielding effect. However, the combined effect of increase in atomic size and shielding effect dominates over the effect of increase in the nuclear charge. Hence, force of attraction of the nucleus for the electron to be added decreases resulting in a decrease in electron-affinity values.',
    'گروپ میں اوپر سے نیچے جانے پر ایٹمی جسامت، مرکزی بار اور حجاب کا اثر بڑھتے ہیں۔ تاہم ایٹمی جسامت اور حجاب کے اثر میں اضافے کا مجموعی اثر، مرکزی بار میں اضافے کے اثر پر غالب ہوتا ہے۔ اس لیے شامل کیے جانے والے الیکٹرون پر مرکزے کی کشش کم ہوتی ہے، جس سے الیکٹرون الفت کی قدریں کم ہوتی ہیں۔',
    'په ګروپ کې له پاسه ښکته تګ سره اټومي اندازه، هستوي چارج او د پردې اغېز زیاتېږي. خو د اټومي اندازې او د پردې د اغېز د زیاتېدو ګډ اغېز د هستوي چارج د زیاتېدو پر اغېز غالب وي. نو د ورزیاتېدونکي الکترون لپاره د هستې د کشش قوه کمېږي او د الکترون میلان ارزښتونه ټیټېږي.')
add('However, it has been seen that fluorine has lower electron affinity than chlorine because fluorine has very small size and high charge density which opposes the electron to be added. Electron affinity generally decreases in the following order (I < Br < F < Cl).',
    'تاہم دیکھا گیا ہے کہ فلورین کی الیکٹرون الفت کلورین سے کم ہے، کیونکہ فلورین کی جسامت بہت چھوٹی اور بار کی کثافت زیادہ ہے، جو شامل کیے جانے والے الیکٹرون کی مخالفت کرتی ہے۔ الیکٹرون الفت عموماً درج ذیل ترتیب میں کم ہوتی ہے (I < Br < F < Cl)۔',
    'خو لیدل شوي چې فلورین له کلورین څخه د الکترون کم میلان لري، ځکه فلورین ډېره کوچنۍ اندازه او د چارج لوړ کثافت لري، چې د ورزیاتېدونکي الکترون مخالفت کوي. د الکترون میلان عموماً په لاندې ترتیب کمېږي (I < Br < F < Cl).')
v=['−328.0','−349.0','−324.6','−295.2'];table(27,'Trend in Electron Affinity in Group–VIIA Elements','گروپ VIIA کے عناصر میں الیکٹرون الفت کا رجحان','د VIIA ګروپ په عناصرو کې د الکترون میلان تمایل',[['Electron Affinity (kJ/mol)']+v],[['الیکٹرون الفت (kJ/mol)']+v],[['د الکترون میلان (kJ/mol)']+v])
head('13.5.1.4 Trend in Melting and Boiling Points','13.5.1.4 پگھلنے اور ابلنے کے درجوں کا رجحان','13.5.1.4 د وېلې کېدو او اېشېدو د ټکو تمایل')
add('The melting and boiling points of Group – VIIA increases down the group due to increase in strength of the Van der Waals forces. This trend is given below.',
    'وان ڈر والز قوتوں کی مضبوطی بڑھنے کی وجہ سے گروپ VIIA میں نیچے پگھلنے اور ابلنے کے درجے بڑھتے ہیں۔ یہ رجحان ذیل میں دیا گیا ہے۔',
    'د وان در والس د قوو د پیاوړتیا د زیاتېدو له امله د VIIA ګروپ د وېلې کېدو او اېشېدو ټکي په ګروپ کې ښکته لوړېږي. دا تمایل لاندې ورکړل شوی دی.')
m=['−220.0','−101.0','−7.2','+114.0'];b=['−188.0','−35.0','+58.8','+184.0'];table(28,'Trend in Melting and Boiling Points in Group–VIIA Elements','گروپ VIIA کے عناصر میں پگھلنے اور ابلنے کے درجوں کا رجحان','د VIIA ګروپ په عناصرو کې د وېلې کېدو او اېشېدو د ټکو تمایل',[['Melting point (°C)']+m,['Boiling point (°C)']+b],[['نقطۂ پگھلاؤ (°C)']+m,['نقطۂ ابال (°C)']+b],[['د وېلې کېدو ټکی (°C)']+m,['د اېشېدو ټکی (°C)']+b])
head('13.5.1.5 Bond Enthalpies','13.5.1.5 بندوں کی اینتھالپیاں','13.5.1.5 د تړونونو انتالپۍ')
add('Bond enthalpy is the amount of heat required to break one mole of covalent bonds to form individual atoms. It begins with the original substance in a gaseous state and ending with gaseous atoms.',
    'بند کی اینتھالپی اشتراکی بندوں کے ایک مول کو توڑ کر الگ الگ ایٹم بنانے کے لیے درکار حرارت کی مقدار ہے۔ یہ اصل مادے کی گیسی حالت سے شروع ہوتی ہے اور گیسی ایٹموں پر ختم ہوتی ہے۔',
    'د تړون انتالپي د هغې تودوخې اندازه ده چې د کووالنټ تړونونو د یوه مول د ماتولو او جلا اټومونو د جوړولو لپاره اړینه ده. دا د اصلي مادې له ګازي حالت څخه پیلېږي او په ګازي اټومونو پای ته رسېږي.')
eq('Cl–Cl(g) —Δ→ 2Cl(g)')
head('13.5.1.5.1 Bond Enthalpies in Halogens','13.5.1.5.1 ہیلوجنز میں بندوں کی اینتھالپیاں','13.5.1.5.1 په هالوجنونو کې د تړونونو انتالپۍ')
add('Bond breaking is an endothermic process and bond enthalpy involved is given positive sign. The bond enthalpies of halogens are given below.',
    'بند توڑنا حرارت گیر عمل ہے اور متعلقہ بند کی اینتھالپی کو مثبت نشان دیا جاتا ہے۔ ہیلوجنز کے بندوں کی اینتھالپیاں ذیل میں دی گئی ہیں۔',
    'د تړون ماتول تودوخه جذبونکی بهیر دی او اړوند د تړون انتالپي ته مثبته نښه ورکول کېږي. د هالوجنونو د تړونونو انتالپۍ لاندې ورکړل شوې دي.')
l=['144','199','228','267'];e=['159','243','193','151'];table(29,'Bond Enthalpies in Halogens','ہیلوجنز میں بندوں کی اینتھالپیاں','په هالوجنونو کې د تړونونو انتالپۍ',[['Bond length (pm)']+l,['Bond enthalpy (kJ/mol)']+e],[['بند کی لمبائی (pm)']+l,['بند کی اینتھالپی (kJ/mol)']+e],[['د تړون اوږدوالی (pm)']+l,['د تړون انتالپي (kJ/mol)']+e],['Bond','F–F','Cl–Cl','Br–Br','I–I'])
add('The abnormal behavior in F–F bond is due to its smaller size and strong repulsion amongst the non-bonded electrons (lone pair) of fluorine atoms. Hence bonds become weak, though bond is short. Thus, enthalpy of fluorine is less than the other halogens.',
    'F–F بند کا غیر معمولی رویہ چھوٹی جسامت اور فلورین ایٹموں کے غیر بندشی الیکٹرونوں (تنہا جوڑے) کے درمیان مضبوط دفع کی وجہ سے ہے۔ اس لیے بند چھوٹا ہونے کے باوجود کمزور ہوتا ہے۔ یوں فلورین کی اینتھالپی دوسرے ہیلوجنز سے کم ہے۔',
    'د F–F تړون غیر عادي چلند د کوچنۍ اندازې او د فلورین د اټومونو د نه تړون جوړوونکو الکترونونو (یوازینۍ جوړې) ترمنځ د پیاوړي دفع له امله دی. نو تړون که څه هم لنډ دی، کمزوری کېږي. په دې توګه د فلورین انتالپي له نورو هالوجنونو کمه ده.')
record=section('13.19','Halogen atomic properties and bond enthalpies','ہیلوجنز کی ایٹمی خصوصیات اور بندوں کی اینتھالپیاں','د هالوجنونو اټومي ځانګړنې او د تړونونو انتالپۍ',paras,layout,blocks,'38–39');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':23,'printedPages':[38,39]}]
issues=[{'id':'chem12-p39-fluorine-enthalpy','printedPage':39,'description':'The prose says fluorine bond enthalpy is less than the other halogens, but Table13.29 gives F–F159 and I–I151 kJ/mol. Printed prose and numbers both retained.'}]
if __name__=='__main__':save(23,[record],carry=[{'from':'13.19','to':'13.20','startsAt':'13.5.1.5.2 Bond Enthalpies in Hydrogen Halides'}],issues=issues)
