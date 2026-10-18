"""PDF88 printed168–169: substitution vs elimination, C–X bond energies, SN introduction, important concepts, carbocations."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow88');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'alkyl halide':('الکائل ہیلائیڈ','الکایل هالایډ'),'nucleophile':('نیوکلیوفائل','نیوکلیوفایل'),'product':('پیداوار','محصول'),'(substrate)':('(سبسٹریٹ)','(سبسټرېټ)'),
   'halide ion':('ہیلائیڈ آئن','هالایډ ایون'),'(nucleofuge)':('(نیوکلیوفیوج)','(نیوکلیوفیوج)'),'top view':('اوپر سے منظر','له پاسه منظره'),'side view':('پہلو سے منظر','له اړخه منظره'),'vacant':('خالی','تش'),'p orbital':('p آربیٹل','p اوربیټال')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def sn(lang,sub):
 s=F.start(110)+t(200,40,'R — X',18)+t(275,40,'+',18)+t(350,40,'N̈u⁻',18)+F.arrow(410,510,34)+t(600,40,'R — Nu',18)+t(690,40,'+',18)+t(740,40,'X⁻',18)
 s+=t(200,64,lb(lang,'alkyl halide'),12)+t(350,64,lb(lang,'nucleophile'),12)+t(600,64,lb(lang,'product'),12)
 if sub:s+=t(200,80,lb(lang,'(substrate)'),12)+t(740,64,lb(lang,'halide ion'),12)+t(740,80,lb(lang,'(nucleofuge)'),12)
 return s+'</svg>'
def cation(lang):
 s=F.start(220);cx,cy=200,110
 for ang in (90,210,330):
  a=math.radians(ang);x,y=cx+60*math.cos(a),cy-60*math.sin(a);mx,my=(cx+x)/2,(cy+y)/2
  s+=f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="30" ry="13" fill="#b3e5fc" stroke="#333" transform="rotate({-ang:.1f} {mx:.1f} {my:.1f})"/>'+t(mx,my+5,'sp²',12)
  s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="#fff59d" stroke="#333"/>'+t(x,y+5,'H',13)
 s+=t(cx,cy+6,'C⁺',15)+t(cx,205,lb(lang,'top view'),13)
 x0=560;s+=f'<ellipse cx="{x0}" cy="62" rx="16" ry="34" fill="#29b6f6"/><ellipse cx="{x0}" cy="150" rx="16" ry="34" fill="#2e7d32"/>'+t(x0,112,'C⁺',15)
 s+=line(x0+12,106,x0+60,106)+t(x0+72,112,'H',15)+line(x0-12,104,x0-55,98,1.5,'#222','stroke-dasharray="2 3"')+t(x0-65,100,'H',15)+line(x0-10,112,x0-50,124,4)+t(x0-60,132,'H',15)
 s+=t(x0+80,30,lb(lang,'vacant'),13)+t(x0+80,46,lb(lang,'p orbital'),13)+t(x0,205,lb(lang,'side view'),13)
 return s+'</svg>'

add('The halogen atom is a good leaving group and detaches from carbon atom, with its bonding electron pair to form a stable halide ion. When a nucleophile attacks on α–carbon and replaces the halide ion, the reaction is a nucleophilic substitution. When the halide ion leaves along with another atom (often H) from the adjacent carbon atom, it forms a new pi bond, the reaction is an elimination. In elimination reactions, a molecule of HX is lost from the alkyl halide to give an alkene. These elimination reactions are called dehydrohalogenation (Section 16.5.5.2), because a hydrogen halide has been removed from the alkyl halide. Substitution and elimination reactions often compete with each other (Section 17.1.8).',
 'ہیلوجن ایٹم ایک اچھا خارج ہونے والا گروپ ہے اور اپنے بندشی الیکٹرانی جوڑے کے ساتھ کاربن ایٹم سے الگ ہو کر پائیدار ہیلائیڈ آئن بناتا ہے۔ جب نیوکلیوفائل α–کاربن پر حملہ کر کے ہیلائیڈ آئن کی جگہ لے لے تو تعامل نیوکلیوفائلی تبادلہ ہے۔ جب ہیلائیڈ آئن ملحقہ کاربن ایٹم سے کسی اور ایٹم (اکثر H) کے ساتھ خارج ہو کر نیا پائی بند بنائے تو تعامل اخراج ہے۔ اخراجی تعاملات میں الکائل ہیلائیڈ سے HX کا ایک سالمہ نکل کر الکین (دوہرے بند والا) بنتا ہے۔ ان اخراجی تعاملات کو ڈی ہائیڈروہیلوجینیشن (حصہ 16.5.5.2) کہتے ہیں، کیونکہ الکائل ہیلائیڈ سے ہائیڈروجن ہیلائیڈ نکالا گیا ہے۔ تبادلے اور اخراج کے تعاملات اکثر ایک دوسرے سے مقابلہ کرتے ہیں (حصہ 17.1.8)۔',
 'هالوجني اټوم ښه وتونکی ګروپ دی او له خپلې تړونې الکتروني جوړې سره له کاربني اټوم جلا کېږي او ثابت هالایډ ایون جوړوي. کله چې نیوکلیوفایل پر α–کاربن برید وکړي او د هالایډ ایون ځای ونیسي، تعامل نیوکلیوفایلي بدلون دی. کله چې هالایډ ایون د ګاونډي کاربني اټوم له بل اټوم (ډېری H) سره ووځي او نوی پای تړون جوړ کړي، تعامل ایستنه ده. د ایستلو په تعاملونو کې له الکایل هالایډ څخه د HX یو مالیکول له لاسه ځي او الکین جوړېږي. دې ایستلو تعاملونو ته ډی هایدروهالوجینېشن (برخه 16.5.5.2) وايي، ځکه له الکایل هالایډ څخه هایدروجن هالایډ لرې شوی. د بدلون او ایستلو تعاملونه ډېری له یو بل سره سیالي کوي (برخه 17.1.8).')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Besides alkyl halides, many other types of compounds undergo substitution and elimination reactions. Substitutions and eliminations are introduced in this unit using the alkyl halides as examples. In unit 18, we encounter substitutions and eliminations in alcohols.',
 'الکائل ہیلائیڈز کے علاوہ بہت سی دوسری اقسام کے مرکبات بھی تبادلے اور اخراج کے تعاملات کرتے ہیں۔ اس یونٹ میں تبادلے اور اخراج کو الکائل ہیلائیڈز کی مثالوں سے متعارف کرایا گیا ہے۔ یونٹ 18 میں ہم الکوحلز میں تبادلے اور اخراج دیکھیں گے۔',
 'له الکایل هالایډونو پرته ډېر نور ډوله مرکبات هم د بدلون او ایستلو تعاملونه کوي. په دې واحد کې بدلون او ایستنه د الکایل هالایډونو په بېلګو معرفي شوي. په 18 واحد کې به په الکولونو کې بدلون او ایستنه وګورو.')
add('The strength of carbon–halogen bond decreases down the group from fluorine to iodine. This can be explained on the basis of their bond energies that are given in the Table 17.1. The table shows that iodo compounds are most reactive while fluoro compounds are least reactive. Therefore, the reactivity of alkyl halides increases from fluorine to iodine and the reactivity order is; R–I > R–Br > R–Cl > R–F.',
 'کاربن–ہیلوجن بند کی مضبوطی گروپ میں فلورین سے آئیوڈین کی طرف کم ہوتی ہے۔ اس کی وضاحت جدول 17.1 میں دی گئی بند توانائیوں کی بنیاد پر کی جا سکتی ہے۔ جدول سے ظاہر ہے کہ آئیوڈو مرکبات سب سے زیادہ اور فلورو مرکبات سب سے کم تعامل پذیر ہیں۔ چنانچہ الکائل ہیلائیڈز کی تعامل پذیری فلورین سے آئیوڈین کی طرف بڑھتی ہے اور ترتیب یہ ہے؛ R–I > R–Br > R–Cl > R–F۔',
 'د کاربن–هالوجن تړون قوت په ګروپ کې له فلورین څخه ایوډین ته کمېږي. دا د هغوی د تړون د انرژیو پر بنسټ روښانه کېدای شي چې په جدول 17.1 کې ورکړل شوې. جدول ښيي چې ایوډو مرکبات تر ټولو ډېر او فلورو مرکبات تر ټولو لږ تعامل کوونکي دي. نو د الکایل هالایډونو تعامل وړتیا له فلورین څخه ایوډین ته زیاتېږي او ترتیب یې دا دی؛ R–I > R–Br > R–Cl > R–F.')
tb={'id':'chem12-table17-1-bond-energy','headers':['Bond','Bond Energy (kJ/mol)'],'rows':[['C–F','467'],['C–Cl','346'],['C–Br','290'],['C–I','228']],
 'translations':[{'language':'اردو','headers':['بند','بند توانائی (kJ/mol)'],'rows':[['C–F','467'],['C–Cl','346'],['C–Br','290'],['C–I','228']]},{'language':'پښتو','headers':['تړون','د تړون انرژي (kJ/mol)'],'rows':[['C–F','467'],['C–Cl','346'],['C–Br','290'],['C–I','228']]}]}
add('Table 17.1 Bond Energies of Carbon-Halogen Bond','جدول 17.1 کاربن–ہیلوجن بند کی بند توانائیاں','جدول 17.1 د کاربن–هالوجن تړون انرژۍ')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('17.1.6 Nucleophilic Substitution (SN) Reactions','17.1.6 نیوکلیوفائلی تبادلے (SN) کے تعاملات','17.1.6 نیوکلیوفایلي بدلون (SN) تعاملونه','heading')
add('17.1.6.1 General Introduction','17.1.6.1 عمومی تعارف','17.1.6.1 عمومي پېژندنه','heading')
add('Alkyl halides undergo nucleophilic substitution reactions in which a stronger nucleophile replaces the halide ion (Section 16.1.5). A general example of such a reaction is given as;','الکائل ہیلائیڈز نیوکلیوفائلی تبادلے کے تعاملات کرتے ہیں جن میں زیادہ طاقتور نیوکلیوفائل ہیلائیڈ آئن کی جگہ لیتا ہے (حصہ 16.1.5)۔ ایسے تعامل کی ایک عمومی مثال یہ ہے؛','الکایل هالایډونه نیوکلیوفایلي بدلون تعاملونه کوي چې پکې قوي نیوکلیوفایل د هالایډ ایون ځای نیسي (برخه 16.1.5). د داسې تعامل یوه عمومي بېلګه دا ده؛')
visual('chem12-p88-sn-general',lambda l:sn(l,False))
add('Alkyl halides undergo nucleophilic substitution reactions by two different types of mechanisms i.e. unimolecular (SN1) and bimolecular (SN2) nucleophilic substitution.','الکائل ہیلائیڈز دو مختلف طریق کار سے نیوکلیوفائلی تبادلے کے تعاملات کرتے ہیں، یعنی یک سالمی (SN1) اور دو سالمی (SN2) نیوکلیوفائلی تبادلہ۔','الکایل هالایډونه په دوو بېلو میکانیزمونو نیوکلیوفایلي بدلون تعاملونه کوي، یعنې یو مالیکولي (SN1) او دوه مالیکولي (SN2) نیوکلیوفایلي بدلون.')
add('17.1.6.2 Important Concepts','17.1.6.2 اہم تصورات','17.1.6.2 مهم مفاهیم','heading')
add('17.1.6.2.1 Substrate and Leaving Group','17.1.6.2.1 سبسٹریٹ اور خارج ہونے والا گروپ','17.1.6.2.1 سبسټرېټ او وتونکی ګروپ','heading')
add('The molecule which undergoes nucleophilic substitution reaction is called substrate. The group or species which leaves the substrate or which is being replaced by the incoming nucleophile is called leaving group or nucleofuge. In the above reaction, alkyl halide is substrates and halogen (halide ion) is the leaving group.',
 'جو سالمہ نیوکلیوفائلی تبادلے کا تعامل کرے اسے سبسٹریٹ کہتے ہیں۔ جو گروپ یا نوع سبسٹریٹ کو چھوڑے یا آنے والے نیوکلیوفائل سے بدلی جائے اسے خارج ہونے والا گروپ یا نیوکلیوفیوج کہتے ہیں۔ اوپر کے تعامل میں الکائل ہیلائیڈ سبسٹریٹ اور ہیلوجن (ہیلائیڈ آئن) خارج ہونے والا گروپ ہے۔',
 'هغه مالیکول چې نیوکلیوفایلي بدلون تعامل کوي، سبسټرېټ بلل کېږي. هغه ګروپ یا ډول چې سبسټرېټ پرېږدي یا د راتلونکي نیوکلیوفایل په واسطه بدلېږي، وتونکی ګروپ یا نیوکلیوفیوج بلل کېږي. په پورته تعامل کې الکایل هالایډ سبسټرېټ او هالوجن (هالایډ ایون) وتونکی ګروپ دی.')
visual('chem12-p88-substrate',lambda l:sn(l,True))
add('17.1.6.2.2 Nucleophile and Base','17.1.6.2.2 نیوکلیوفائل اور اساس','17.1.6.2.2 نیوکلیوفایل او قلوي','heading')
add('Any species neutral or negatively charged with an unshared pair of electrons can act both as a base and a nucleophile. Nucleophile is a species which donates electron pair to an electrophilic center in a molecule and undergoes nucleophilic substitution or addition reactions. A nucleophile is generally represented by N̈u. The strength of nucleophile is called nucleophilicity and is a measure of how fast a nucleophile displaces a leaving group from a suitable substrate.',
 'کوئی بھی غیر جانبدار یا منفی چارج والی نوع جس کے پاس غیر مشترک الیکٹرانی جوڑا ہو، اساس اور نیوکلیوفائل دونوں کا کام کر سکتی ہے۔ نیوکلیوفائل وہ نوع ہے جو سالمے کے الیکٹروفائلی مرکز کو الیکٹرانی جوڑا دیتی ہے اور نیوکلیوفائلی تبادلے یا اضافے کے تعاملات کرتی ہے۔ نیوکلیوفائل کو عموماً N̈u سے ظاہر کیا جاتا ہے۔ نیوکلیوفائل کی طاقت کو نیوکلیوفلیسٹی کہتے ہیں اور یہ اس بات کی پیمائش ہے کہ نیوکلیوفائل کسی مناسب سبسٹریٹ سے خارج ہونے والے گروپ کو کتنی تیزی سے ہٹاتا ہے۔',
 'هر بې چارجه یا منفي چارج لرونکی ډول چې نه شریکه الکتروني جوړه ولري، هم د قلوي او هم د نیوکلیوفایل دنده ترسره کولی شي. نیوکلیوفایل هغه ډول دی چې د مالیکول الکتروفایلي مرکز ته الکتروني جوړه ورکوي او نیوکلیوفایلي بدلون یا اضافي تعاملونه کوي. نیوکلیوفایل معمولاً په N̈u ښودل کېږي. د نیوکلیوفایل قوت ته نیوکلیوفیلیسیټي وايي او دا اندازه کوي چې نیوکلیوفایل له یوه مناسب سبسټرېټ څخه وتونکی ګروپ څومره چټک لرې کوي.')
add('But a base is a species which has affinity for proton, and donate electron pair to a proton in a reaction, and generally represented by B̈. Base give elimination reaction in alkyl halides. The strength of base is called basicity and represented in terms of equilibrium constant for abstraction of a proton.',
 'لیکن اساس وہ نوع ہے جو پروٹان کی طرف رغبت رکھتی ہے اور تعامل میں پروٹان کو الیکٹرانی جوڑا دیتی ہے، اور عموماً B̈ سے ظاہر کی جاتی ہے۔ اساس الکائل ہیلائیڈز میں اخراجی تعامل دیتی ہے۔ اساس کی طاقت کو اساسیت کہتے ہیں اور اسے پروٹان کھینچنے کے توازنی مستقل کے لحاظ سے ظاہر کیا جاتا ہے۔',
 'خو قلوي هغه ډول دی چې پروټون ته میلان لري، او په تعامل کې پروټون ته الکتروني جوړه ورکوي، او معمولاً په B̈ ښودل کېږي. قلوي په الکایل هالایډونو کې د ایستلو تعامل ورکوي. د قلوي قوت ته قلویت وايي او د پروټون د اخیستلو د توازن ثابت له مخې ښودل کېږي.')
add('17.1.6.2.3 Carbocations and their Stability','17.1.6.2.3 کاربوکیٹائنز اور ان کی پائیداری','17.1.6.2.3 کاربوکاټیونونه او د هغوی ثبات','heading')
add('A carbocation is an ion in which a carbon atom has a positive charge and three bonds. Carbocation is formed when an electrophile adds to carbon-carbon double bond or when halogen atom detaches from the carbon atom of an alkyl halide as halide ion. The positive carbon of alkyl carbocation is sp²-hybridized and has trigonal planar structure, with empty unhybridized p orbital perpendicular to the plane, as shown in (Figure 17.2).',
 'کاربوکیٹائن وہ آئن ہے جس میں کاربن ایٹم پر مثبت چارج اور تین بند ہوں۔ کاربوکیٹائن اس وقت بنتا ہے جب الیکٹروفائل کاربن–کاربن دوہرے بند میں شامل ہو یا جب ہیلوجن ایٹم الکائل ہیلائیڈ کے کاربن ایٹم سے ہیلائیڈ آئن کے طور پر الگ ہو۔ الکائل کاربوکیٹائن کا مثبت کاربن sp²-ہائبرڈ ہوتا ہے اور اس کی ساخت تکونی مستوی ہوتی ہے، جس میں خالی غیر ہائبرڈ p آربیٹل مستوی پر عمود ہوتا ہے، جیسا کہ (شکل 17.2) میں دکھایا گیا ہے۔',
 'کاربوکاټیون هغه ایون دی چې پکې کاربني اټوم مثبت چارج او درې تړونونه لري. کاربوکاټیون هغه وخت جوړېږي چې الکتروفایل کاربن–کاربن دوه ګوني تړون ته ورزیات شي یا کله چې هالوجني اټوم د هالایډ ایون په توګه د الکایل هالایډ له کاربني اټوم جلا شي. د الکایل کاربوکاټیون مثبت کاربن sp²-هایبرېډ دی او درې ګوټي سطحي جوړښت لري، چې تش نا هایبرېډ شوی p اوربیټال پر سطحه عمود دی، لکه څنګه چې په (شکل 17.2) کې ښودل شوی.')
visual('chem12-figure17-2',cation)
add('Figure 17.2 Trigonal planar structure of methyl cation.','شکل 17.2 میتھائل کیٹائن کی تکونی مستوی ساخت۔','شکل 17.2 د میتایل کاټیون درې ګوټی سطحي جوړښت.')
record=section('17.4','Substitution vs elimination, SN concepts and carbocations','تبادلہ بمقابلہ اخراج، SN تصورات اور کاربوکیٹائنز','بدلون او ایستنه، د SN مفاهیم او کاربوکاټیونونه',paras,layout,blocks,'168–169')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':88,'printedPages':[168,169]}]
record['sourceContinuesOnPdfPage']=89
issues=[{'id':'chem12-p168-table-section-refs','printedPage':168,'description':'Bond-energy table printed as "Table 17.1" (boiling-point table on printed 166 is "Table 7.1"); "(Section 16.1.5)" cross-reference retained as printed.'}]
carry=[{'from':'17.4','to':'17.5','startsAt':'Carbocations are classified as primary'}]
if __name__=='__main__':save(88,[record],carry=carry,issues=issues,chapter_number=17)
