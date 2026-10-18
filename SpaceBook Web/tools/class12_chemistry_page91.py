"""PDF91 printed174–175: E1 steps, E2 mechanism, Table 17.3, substitution versus elimination."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow91');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carbocation':('کاربوکیٹائن','کاربوکاټیون'),'(trigonal planar)':('(تکونی مستوی)','(درې ګوټی سطحي)'),'base':('اساس','قلوي'),'fast':('تیز','چټک'),'isobutylene':('آئسوبیوٹیلین','ایزوبیوټیلین'),
   'elimination':('اخراج','ایستنه'),'biomolecular':('دو سالمی','دوه مالیکولي'),'ethyl bromide':('ایتھائل برومائیڈ','ایتیل برومایډ'),'transition state':('عبوری حالت','انتقالي حالت'),'ethene':('ایتھین (دوہرا بند)','ایتین'),
   '2-bromopropane':('2-برومو پروپین','2-بروموپروپان'),'sodium ethoxide':('سوڈیم ایتھوآکسائیڈ','سوډیم ایتوکساید'),'propene':('پروپین','پروپین'),'(major)':('(بڑی)','(عمده)'),'(minor)':('(چھوٹی)','(لږه)'),'ethyl isopropyl ether':('ایتھائل آئسوپروپائل ایتھر','ایتیل ایزوپروپیل ایتر')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def e1(lang):
 s=F.start(150)+chain(F,0,76,['H₃C','—','C⁺','—','C','—','H'],16,None,{2:'CH₃',4:'H'},{4:'H'},center=130)+t(118,96,'α',11)+t(165,96,'β',11)
 s+=t(250,76,'+ H₂O',16)+f'<path d="M255 62 Q240 30 205 62" fill="none" stroke="#222" stroke-width="1.5" marker-end="url(#arrow91)"/>'+F.arrow(300,380,70,lb(lang,'fast'))
 s+=t(450,50,'H₃C',14)+t(450,96,'H₃C',14)+line(466,56,480,66)+line(466,90,480,80)+t(530,76,'C = CH₂  +  H₃O⁺',16)
 s+=t(120,130,lb(lang,'carbocation'),12)+t(120,145,lb(lang,'(trigonal planar)'),12)+t(250,110,lb(lang,'base'),12)+t(500,120,lb(lang,'isobutylene'),12)
 return s+'</svg>'
def badge(lang):
 s=F.start(110,420)+'<rect x="10" y="10" width="400" height="92" rx="6" fill="white" stroke="#222"/>'+t(180,40,'E',18)+t(240,40,'2',18)
 s+=t(90,90,lb(lang,'elimination'),12)+t(330,90,lb(lang,'biomolecular'),12)+line(180,46,120,74,1,'#222','stroke-dasharray="2 3"')+line(240,46,300,74,1,'#222','stroke-dasharray="2 3"')
 return s+'</svg>'
def e2(lang):
 s=F.start(150)+t(40,84,'HŌ⁻ +',16)+f'<path d="M30 66 Q50 30 92 46" fill="none" stroke="#222" stroke-width="1.5" marker-end="url(#arrow91)"/>'
 s+=t(100,46,'H',14)+t(160,46,'Br',14)+line(100,52,100,66)+line(160,52,160,66)+t(130,84,'CH₂ — CH₂',16)+t(110,62,'β',11)+t(150,62,'α',11)
 s+=F.arrow(215,265,78)+'<path d="M290 25 L282 25 L282 110 L290 110 M440 25 L448 25 L448 110 L440 110" fill="none" stroke="#222" stroke-width="2"/>'
 s+=t(320,46,'HO--H',14)+t(400,46,'Br',14)+line(345,52,345,66,1.5,'#222','stroke-dasharray="2 2"')+line(400,52,400,66,1.5,'#222','stroke-dasharray="2 2"')+t(370,84,'CH₂ ⋯ CH₂',16)+t(454,24,'⁻',14)
 s+=F.arrow(460,510,78)+t(640,84,'CH₂ = CH₂ + H₂O + Br⁻',16)
 s+=t(40,125,lb(lang,'base'),12)+t(130,125,lb(lang,'ethyl bromide'),12)+t(365,130,lb(lang,'transition state'),12)+t(600,110,lb(lang,'ethene'),12)
 return s+'</svg>'
def ethoxide(lang):
 s=F.start(140)+t(100,30,'Br',14)+line(100,36,100,52)+t(100,70,'CH₃CHCH₃',16)+t(100,94,lb(lang,'2-bromopropane'),12)+t(270,70,'+  C₂H₅O⁻Na⁺',16)+t(280,94,lb(lang,'sodium ethoxide'),12)
 s+=F.arrow(380,460,64)+t(550,70,'CH₃CH=CH₂',16)+t(550,94,lb(lang,'propene'),12)+t(550,110,lb(lang,'(major)'),12)+t(640,70,'+',16)
 s+=t(730,30,'OC₂H₅',14)+line(730,36,730,52)+t(730,70,'CH₃CHCH₃',16)+t(730,94,lb(lang,'ethyl isopropyl ether'),12)+t(730,110,lb(lang,'(minor)'),12)
 return s+'</svg>'

add('In a fast second step, a base abstracts a proton from the carbon atom adjacent to the positive carbon (β-carbon). These reactions are usually followed by tertiary alkyl halides, like SN1 reactions. For example, reaction of tert-butyl bromide with water, upon β-elimination yield isobutylene.',
 'تیز دوسرے مرحلے میں اساس مثبت کاربن کے ملحقہ کاربن ایٹم (β-کاربن) سے پروٹان کھینچ لیتی ہے۔ SN1 تعاملات کی طرح یہ تعاملات بھی عموماً ثالثی الکائل ہیلائیڈز اپناتے ہیں۔ مثلاً ٹرشری بیوٹائل برومائیڈ کا پانی سے تعامل β-اخراج پر آئسوبیوٹیلین دیتا ہے۔',
 'په چټک دویم پړاو کې قلوي له مثبت کاربن سره د ګاونډي کاربني اټوم (β-کاربن) څخه پروټون اخلي. دا تعاملونه هم د SN1 تعاملونو په څېر معمولاً درېیمي الکایل هالایډونه تعقیبوي. د بېلګې په توګه له اوبو سره د ټرشري بیوټیل برومایډ تعامل د β-ایستنې پر مهال ایزوبیوټیلین ورکوي.')
add('Step–1: The first step is similar to SN1 (Section 17.1.6.3)','مرحلہ–1: پہلا مرحلہ SN1 جیسا ہے (حصہ 17.1.6.3)','پړاو–1: لومړی پړاو د SN1 په څېر دی (برخه 17.1.6.3)')
add('Step–2: The base abstracts β-hydrogen of carbocation and yield isobutylene.','مرحلہ–2: اساس کاربوکیٹائن کا β-ہائیڈروجن کھینچتی ہے اور آئسوبیوٹیلین بنتی ہے۔','پړاو–2: قلوي د کاربوکاټیون β-هایدروجن اخلي او ایزوبیوټیلین ورکوي.')
visual('chem12-p91-e1-step2',e1)
add('Because the rate-limiting step involves unimolecular ionization of the alkyl halide, the rate equation is first-order. The rate depends only on the concentration of the alkyl halide and not on the concentration of the base. rate = k [R–X] or rate = k [(CH₃)₃C–Br]',
 'چونکہ شرح محدود کرنے والے مرحلے میں الکائل ہیلائیڈ کی یک سالمی آئنائزیشن ہوتی ہے، اس لیے شرح کی مساوات پہلے درجے کی ہے۔ شرح صرف الکائل ہیلائیڈ کے ارتکاز پر منحصر ہے، اساس کے ارتکاز پر نہیں۔ rate = k [R–X] یا rate = k [(CH₃)₃C–Br]',
 'څرنګه چې د سرعت محدودوونکی پړاو د الکایل هالایډ یو مالیکولي ایونایزېشن رانغاړي، د سرعت معادله لومړۍ درجه ده. سرعت یوازې د الکایل هالایډ پر غلظت پورې اړه لري، نه د قلوي پر غلظت. rate = k [R–X] یا rate = k [(CH₃)₃C–Br]')
add('17.1.7.3 E2 Mechanism','17.1.7.3 E2 طریق کار','17.1.7.3 د E2 میکانیزم','heading')
visual('chem12-p91-e2-badge',badge)
add('This is a bimolecular elimination process, with both the base and the alkyl halide participating in the transition state, so this mechanism is abbreviated E2 for Elimination, bimolecular. These are generally followed by primary alkyl halides. These reactions are completed in one step like SN2 reactions.',
 'یہ دو سالمی اخراجی عمل ہے، جس کی عبوری حالت میں اساس اور الکائل ہیلائیڈ دونوں شریک ہوتے ہیں، اس لیے اس طریق کار کو اخراج، دو سالمی کے لیے E2 کہتے ہیں۔ یہ عموماً ابتدائی الکائل ہیلائیڈز اپناتے ہیں۔ یہ تعاملات SN2 تعاملات کی طرح ایک مرحلے میں مکمل ہوتے ہیں۔',
 'دا دوه مالیکولي د ایستلو بهیر دی، چې په انتقالي حالت کې یې قلوي او الکایل هالایډ دواړه ګډون کوي، نو دې میکانیزم ته د ایستنې، دوه مالیکولي لپاره E2 وايي. دا معمولاً لومړني الکایل هالایډونه تعقیبوي. دا تعاملونه د SN2 تعاملونو په څېر په یوه پړاو کې بشپړېږي.')
add('For example, reaction of ethyl bromide with hydroxide ion to form ethene follow E2 mechanism. The removal of proton from the β-carbon atom by hydroxide base and the removal of bromide ion from the α-carbon atom takes place simultaneously.',
 'مثلاً ایتھائل برومائیڈ کا ہائیڈروآکسائیڈ آئن سے تعامل جس سے ایتھین بنتی ہے، E2 طریق کار پر چلتا ہے۔ ہائیڈروآکسائیڈ اساس کے ذریعے β-کاربن ایٹم سے پروٹان کا ہٹنا اور α-کاربن ایٹم سے برومائیڈ آئن کا ہٹنا بیک وقت ہوتا ہے۔',
 'د بېلګې په توګه له هایدروکساید ایون سره د ایتیل برومایډ تعامل چې ایتین جوړوي، د E2 میکانیزم تعقیبوي. د هایدروکساید قلوي په واسطه له β-کاربني اټوم څخه د پروټون لرې کول او له α-کاربني اټوم څخه د برومایډ ایون لرې کېدل په یو وخت ترسره کېږي.')
visual('chem12-p91-e2-scheme',e2)
add('Reaction is first order with respect to each reactant, and second order overall. rate = k[substrate] [base] or rate = k [CH₃CH₂Br][⁻OH]',
 'تعامل ہر متعامل کے لحاظ سے پہلے درجے کا اور مجموعی طور پر دوسرے درجے کا ہے۔ rate = k[substrate] [base] یا rate = k [CH₃CH₂Br][⁻OH]',
 'تعامل د هر تعامل کوونکي له مخې لومړۍ درجه او په ټولیز ډول دویمه درجه دی. rate = k[substrate] [base] یا rate = k [CH₃CH₂Br][⁻OH]')
tb={'id':'chem12-table17-3','headers':['Reaction','E1','E2'],
 'rows':[['Promoting factors — Base','Weak Base','Strong Base'],['Promoting factors — Substrate','3° > 2°','1° > 2°'],['Promoting factors — Solvent','Polar protic','Polar aprotic'],['Characteristics — Kinetics','First Order','Second Order']],
 'translations':[{'language':'اردو','headers':['تعامل','E1','E2'],'rows':[['سازگار عوامل — اساس','کمزور اساس','طاقتور اساس'],['سازگار عوامل — سبسٹریٹ','3° > 2°','1° > 2°'],['سازگار عوامل — محلل','قطبی پروٹک','قطبی اپروٹک'],['خصوصیات — حرکیات','پہلا درجہ','دوسرا درجہ']]},
                 {'language':'پښتو','headers':['تعامل','E1','E2'],'rows':[['ملاتړي عوامل — قلوي','کمزوری قلوي','قوي قلوي'],['ملاتړي عوامل — سبسټرېټ','3° > 2°','1° > 2°'],['ملاتړي عوامل — محلل','قطبي پروټیک','قطبي اپروټیک'],['ځانګړنې — حرکیات','لومړۍ درجه','دویمه درجه']]}]}
add('Table 17.3 Summary of Elimination Reactions in Alkyl Halides','جدول 17.3 الکائل ہیلائیڈز میں اخراجی تعاملات کا خلاصہ','جدول 17.3 په الکایل هالایډونو کې د ایستلو تعاملونو لنډیز')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('17.1.8 Substitution versus Elimination','17.1.8 تبادلہ بمقابلہ اخراج','17.1.8 بدلون د ایستنې په وړاندې','heading')
add('We have studied that an alkyl halide and a Lewis base can react together in either a substitution or an elimination reaction (Section 17.1.5). Substitution and elimination reactions are very often in competition with each other. Two important factors i.e. nature of alkyl halide and nature of Lewis base, play a key role in deciding whether a principal reaction would be elimination or substitution.',
 'ہم پڑھ چکے ہیں کہ الکائل ہیلائیڈ اور لیوس اساس آپس میں تبادلے یا اخراج کا تعامل کر سکتے ہیں (حصہ 17.1.5)۔ تبادلے اور اخراج کے تعاملات اکثر ایک دوسرے سے مقابلہ کرتے ہیں۔ دو اہم عوامل، یعنی الکائل ہیلائیڈ کی نوعیت اور لیوس اساس کی نوعیت، یہ طے کرنے میں کلیدی کردار ادا کرتے ہیں کہ بنیادی تعامل اخراج ہو گا یا تبادلہ۔',
 'موږ لوستي چې یو الکایل هالایډ او یو لیوس قلوي کولی شي یو له بل سره د بدلون یا ایستلو تعامل وکړي (برخه 17.1.5). د بدلون او ایستلو تعاملونه ډېری له یو بل سره سیالي کوي. دوه مهم عوامل، یعنې د الکایل هالایډ طبیعت او د لیوس قلوي طبیعت، په دې پرېکړه کې کلیدي رول لوبوي چې اصلي تعامل به ایستنه وي که بدلون.')
add('Crowding around the α–carbon in molecule of substrate generally favours elimination over substitution reaction. This is due to the greater steric hindrance when the nucleophile approaches towards α–carbon atom of the substrate. Thus, greater number of alkyl groups on the substrate favours elimination over substitution because these alkyl groups stabilize the alkene more than the substitution product.',
 'سبسٹریٹ کے سالمے میں α–کاربن کے گرد ہجوم عموماً تبادلے کے مقابلے میں اخراج کے حق میں ہوتا ہے۔ اس کی وجہ یہ ہے کہ نیوکلیوفائل کے سبسٹریٹ کے α–کاربن ایٹم کی طرف بڑھنے پر فضائی رکاوٹ زیادہ ہوتی ہے۔ اس طرح سبسٹریٹ پر زیادہ الکائل گروپ تبادلے کے بجائے اخراج کے حق میں ہوتے ہیں کیونکہ یہ الکائل گروپ تبادلے کی پیداوار سے زیادہ الکین (دوہرے بند والے) کو پائیدار بناتے ہیں۔',
 'د سبسټرېټ په مالیکول کې د α–کاربن شاوخوا ګڼه ګوڼه معمولاً د بدلون پر ځای ایستنه غوره کوي. دا د هغې ډېرې فضايي خنډ له امله ده چې نیوکلیوفایل د سبسټرېټ α–کاربني اټوم ته نږدې کېږي. نو پر سبسټرېټ ډېر الکایل ګروپونه د بدلون پر ځای ایستنه غوره کوي ځکه دا الکایل ګروپونه الکین د بدلون له محصول ډېر ثابتوي.')
add('As all the bases are also nucleophiles, the competition between substitution and elimination reactions is determined by the fact whether it is a better base or a better nucleophile. A stronger base will favour elimination while a stronger nucleophile will favour substitution in the same substrate. For example, 2–bromopropane on reaction with ethoxide ion (C₂H₅O⁻) undergoes elimination and produces alkene as the major product because ethoxide is a strong base (by products are not shown).',
 'چونکہ تمام اساسیں نیوکلیوفائل بھی ہیں، اس لیے تبادلے اور اخراج کے درمیان مقابلے کا فیصلہ اس بات سے ہوتا ہے کہ وہ بہتر اساس ہے یا بہتر نیوکلیوفائل۔ ایک ہی سبسٹریٹ میں طاقتور اساس اخراج کے اور طاقتور نیوکلیوفائل تبادلے کے حق میں ہو گا۔ مثلاً 2–برومو پروپین ایتھوآکسائیڈ آئن (C₂H₅O⁻) سے تعامل پر اخراج کرتی ہے اور بڑی پیداوار کے طور پر الکین دیتی ہے کیونکہ ایتھوآکسائیڈ طاقتور اساس ہے (ضمنی پیداواریں نہیں دکھائی گئیں)۔',
 'څرنګه چې ټول قلویان نیوکلیوفایلونه هم دي، د بدلون او ایستلو ترمنځ سیالي په دې ټاکل کېږي چې ښه قلوي دی که ښه نیوکلیوفایل. په یوه سبسټرېټ کې قوي قلوي ایستنه او قوي نیوکلیوفایل بدلون غوره کوي. د بېلګې په توګه 2–بروموپروپان له ایتوکساید ایون (C₂H₅O⁻) سره په تعامل کې ایستنه کوي او الکین د عمده محصول په توګه ورکوي ځکه ایتوکساید قوي قلوي دی (جانبي محصولات نه دي ښودل شوي).')
visual('chem12-p91-ethoxide',ethoxide)
add('On the other hand the same 2–bromopropane on reaction with ethanthiolate ion (C₂H₅S⁻) undergoes substitution reaction because it is more nucleophilic and less basic than ethoxide ion.',
 'دوسری طرف وہی 2–برومو پروپین ایتھین تھائیولیٹ آئن (C₂H₅S⁻) سے تعامل پر تبادلے کا تعامل کرتی ہے کیونکہ یہ ایتھوآکسائیڈ آئن سے زیادہ نیوکلیوفائلی اور کم اساسی ہے۔',
 'له بلې خوا همدا 2–بروموپروپان له ایتان تیولېټ ایون (C₂H₅S⁻) سره په تعامل کې بدلون تعامل کوي ځکه دا له ایتوکساید ایون ډېر نیوکلیوفایلي او لږ قلوي دی.')
record=section('17.7','E1 and E2 mechanisms; substitution versus elimination','E1 اور E2 طریق کار؛ تبادلہ بمقابلہ اخراج','د E1 او E2 میکانیزمونه؛ بدلون د ایستنې په وړاندې',paras,layout,blocks,'174–175')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':91,'printedPages':[174,175]}]
record['sourceContinuesOnPdfPage']=92
issues=[{'id':'chem12-p175-ethanthiolate','printedPage':175,'description':'Printed "ethanthiolate" and E2 badge "biomolecular" retained in English.'}]
carry=[{'from':'17.7','to':'17.8','startsAt':'CH,CHCH, 2-bromopropane\n+ C,H,SNa'}]
if __name__=='__main__':save(91,[record],carry=carry,issues=issues,chapter_number=17)
