"""PDF70 printed132–133: acetylene orbitals, alkyne properties, stability and elimination preparation."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b'):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x} {y}L{a} {b}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow70" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#222"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
L={'Py-Orbital':('Py-آربیٹل','Py-اوربیټال'),'Pz-Orbital':('Pz-آربیٹل','Pz-اوربیټال'),'sigma bond':('سگما بند','سیګما تړون'),'sp - orbital':('sp - آربیٹل','sp - اوربیټال'),
   'pi-bond':('پائی بند','پای تړون'),'but-1-yne':('بیوٹ-1-ائن','بیوټ-1-این'),'but-2-yne':('بیوٹ-2-ائن','بیوټ-2-این'),'butane':('بیوٹین','بیوټان')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]

def orbitals(lang):
 s=start(270)
 def lobe(cx,cy,rx,ry,c,rot=0):return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{c}" stroke="#333" opacity=".85" transform="rotate({rot} {cx} {cy})"/>'
 for cx in (300,560):
  s+=lobe(cx,70,14,60,'#66bb6a')+lobe(cx,200,14,60,'#66bb6a')
  s+=lobe(cx-40,110,14,52,'#ef6c57',35)+lobe(cx+40,160,14,52,'#ef6c57',35)
 s+=lobe(430,135,120,24,'#3f51b5')+lobe(210,135,70,18,'#3f51b5')+lobe(650,135,70,18,'#3f51b5')
 s+=f'<circle cx="150" cy="135" r="20" fill="#3f51b5"/>'+t(150,142,'H',17,'white')+f'<circle cx="710" cy="135" r="20" fill="#3f51b5"/>'+t(710,142,'H',17,'white')
 for cx in (300,560):s+=f'<circle cx="{cx}" cy="135" r="11" fill="#263238"/>'+t(cx,141,'C',13,'white')
 s+=line(300,16,560,16,3,'#7b1fa2')+line(300,252,560,252,3,'#7b1fa2')+line(260,60,520,60,3,'#e53935')+line(340,215,600,215,3,'#e53935')
 s+=t(170,60,lb(lang,'Py-Orbital'),15)+t(380,40,lb(lang,'Pz-Orbital'),15)+t(430,100,lb(lang,'sigma bond'),15)+t(430,141,lb(lang,'sp - orbital'),15,'white')
 s+=t(450,205,lb(lang,'pi-bond'),15)+t(450,245,lb(lang,'pi-bond'),15)
 return s+'</svg>'
def stability(lang):
 s=start(150)
 s+=t(150,40,'HC ≡ C — CH₂ — CH₃  +  2H₂',19)+t(90,62,lb(lang,'but-1-yne'),14)+line(320,34,410,34,2,'#222','marker-end="url(#arrow70)"')+t(620,40,'CH₃—CH₂—CH₂—CH₃  +  292 kJ/mol',19)+t(560,62,lb(lang,'butane'),14)
 s+=t(150,110,'CH₃ — C ≡ C — CH₃  +  2H₂',19)+t(90,132,lb(lang,'but-2-yne'),14)+line(320,104,410,104,2,'#222','marker-end="url(#arrow70)"')+t(620,110,'CH₃—CH₂—CH₂—CH₃  +  275 kJ/mol',19)+t(560,132,lb(lang,'butane'),14)
 return s+'</svg>'

visual('chem12-figure16-9',orbitals)
add('Figure 16.9 Orbital hybridization model of acetylene.','شکل 16.9 ایسیٹیلین کا آربیٹل ہائبرڈائزیشن ماڈل۔','شکل 16.9 د اسیتیلین د اوربیټال هایبرېډیزېشن ماډل.')
add('Thus, the carbon –carbon triple bond is made up of one sigma and two pi bonds. The acetylene molecule has linear geometry with H–C–C bond angle of 180°. The carbon–carbon triple bond length is 119 pm and that of C–H bond is 106 pm.',
 'یوں کاربن–کاربن تہرا بند ایک سگما اور دو پائی بندوں سے بنا ہوتا ہے۔ ایسیٹیلین سالمے کی جیومیٹری خطی ہے اور H–C–C بند زاویہ 180° ہے۔ کاربن–کاربن تہرے بند کی لمبائی 119 pm اور C–H بند کی لمبائی 106 pm ہے۔',
 'نو کاربن–کاربن درې ګونی تړون له یوه سیګما او دوو پای تړونونو جوړ دی. د اسیتیلین مالیکول خطي جیومټري لري او د H–C–C تړون زاویه 180° ده. د کاربن–کاربن درې ګوني تړون اوږدوالی 119 pm او د C–H تړون اوږدوالی 106 pm دی.')
add('16.7.3 Physical Properties','16.7.3 طبعی خصوصیات','16.7.3 فزیکي ځانګړنې','heading')
for e,u,p in [
 ('With the exception of acetylene which has garlic like odour, all other alkynes are odourless and colourless.','ایسیٹیلین کے سوا، جس کی بو لہسن جیسی ہوتی ہے، باقی تمام الکائنز بے بو اور بے رنگ ہیں۔','پرته له اسیتیلین چې د هوږې په څېر بوی لري، نور ټول الکاینونه بې بویه او بې رنګه دي.'),
 ('The first three members (ethyne, propyne and butynes) are gases, next eight straight chain alkynes (C₅–C₁₂) are liquids and higher alkynes are solids at room temperature and pressure.','پہلے تین ارکان (ایتھائن، پروپائن اور بیوٹائنز) گیسیں ہیں، اگلے آٹھ سیدھی زنجیر والے الکائنز (C₅–C₁₂) مائع ہیں اور بڑے الکائنز کمرے کے درجہ حرارت اور دباؤ پر ٹھوس ہیں۔','لومړي درې غړي (ایتاین، پروپاین او بیوټاینونه) ګازونه دي، راتلونکي اته مستقیم ځنځیري الکاینونه (C₅–C₁₂) مایعات دي او لوړ الکاینونه د کوټې په تودوخه او فشار کې جامد دي.'),
 ('The boiling points of alkynes are slightly higher than the corresponding alkanes and alkenes and increase regularly with increase in the number of carbon atoms in the alkynes. However, their melting points do not follow a regular sequence. Instead, they change irregularly with increase in the number of carbon atoms (Table 16.4). Boiling points of terminal alkynes are lower than isomeric non-terminal alkynes.','الکائنز کے نقطۂ جوش متعلقہ الکینز (اکیلے بند والے) اور الکینز (دوہرے بند والے) سے کچھ زیادہ ہوتے ہیں اور الکائنز میں کاربن ایٹموں کی تعداد بڑھنے سے باقاعدگی سے بڑھتے ہیں۔ تاہم ان کے نقطۂ پگھلاؤ کسی باقاعدہ ترتیب پر نہیں چلتے، بلکہ کاربن ایٹموں کی تعداد بڑھنے سے بے قاعدگی سے بدلتے ہیں (جدول 16.4)۔ سرے والے (ٹرمینل) الکائنز کے نقطۂ جوش ان کے ہم ترکیب غیر ٹرمینل الکائنز سے کم ہوتے ہیں۔','د الکاینونو د ایشېدو ټکي له اړوندو الکانونو او الکینونو یو څه لوړ دي او په الکاینونو کې د کاربني اټومونو د شمېر په زیاتېدو منظم زیاتېږي. خو د ویلې کېدو ټکي یې منظم ترتیب نه لري، بلکې د کاربني اټومونو د شمېر په زیاتېدو نامنظم بدلېږي (جدول 16.4). د پای لرونکو (ټرمینل) الکاینونو د ایشېدو ټکي له ایزومري غیر ټرمینل الکاینونو ټیټ دي.'),
 ('Alkynes like alkanes and alkenes are non-polar; therefore, they are insoluble in water but readily dissolve in organic solvents such as ether, ethanol, acetone, carbon tetrachloride, benzene etc.','الکائنز، الکینز (اکیلے اور دوہرے بند والے) کی طرح، غیر قطبی ہیں؛ اس لیے یہ پانی میں حل نہیں ہوتے مگر ایتھر، ایتھانول، ایسیٹون، کاربن ٹیٹرا کلورائیڈ، بینزین وغیرہ جیسے نامیاتی محللات میں آسانی سے حل ہو جاتے ہیں۔','الکاینونه د الکانونو او الکینونو په څېر غیر قطبي دي؛ نو په اوبو کې نه حلېږي خو په عضوي محللونو لکه ایتر، ایتانول، اسیتون، کاربن ټیټراکلوراید، بنزین او نورو کې په اسانۍ حلېږي.'),
 ('The density of alkynes increases with molecular mass. They are slightly denser than the corresponding alkanes and alkenes. All alkynes are lighter than water.','الکائنز کی کثافت سالماتی کمیت کے ساتھ بڑھتی ہے۔ یہ متعلقہ الکینز (اکیلے اور دوہرے بند والے) سے کچھ زیادہ کثیف ہیں۔ تمام الکائنز پانی سے ہلکے ہیں۔','د الکاینونو کثافت له مالیکولي کتلې سره زیاتېږي. دوی له اړوندو الکانونو او الکینونو یو څه ډېر کثیف دي. ټول الکاینونه له اوبو سپک دي.')]:
 add(e,u,p,'list')
tb={'id':'chem12-table16-4-alkynes','headers':['Alkyne','Melting Points (°C)','Boiling Points (°C)'],
 'rows':[['acetylene','−81','−84'],['propyne','−101','−23'],['but-1-yne','−126','8'],['but-2-yne','−32','27'],['pent-1-yne','−101','40'],['pent-2-yne','−90','55']],
 'translations':[{'language':'اردو','headers':['الکائن','نقطۂ پگھلاؤ (°C)','نقطۂ جوش (°C)'],'rows':[['ایسیٹیلین','−81','−84'],['پروپائن','−101','−23'],['بیوٹ-1-ائن','−126','8'],['بیوٹ-2-ائن','−32','27'],['پینٹ-1-ائن','−101','40'],['پینٹ-2-ائن','−90','55']]},
                 {'language':'پښتو','headers':['الکاین','د ویلې کېدو ټکی (°C)','د ایشېدو ټکی (°C)'],'rows':[['اسیتیلین','−81','−84'],['پروپاین','−101','−23'],['بیوټ-1-این','−126','8'],['بیوټ-2-این','−32','27'],['پېنټ-1-این','−101','40'],['پېنټ-2-این','−90','55']]}]}
add('Table 16.4 Boiling and Melting Points of Some Alkynes','جدول 16.4 بعض الکائنز کے نقطۂ جوش اور نقطۂ پگھلاؤ','جدول 16.4 د ځینو الکاینونو د ایشېدو او ویلې کېدو ټکي')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('16.7.4 Relative Stabilities of alkynes','16.7.4 الکائنز کی اضافی پائیداری','16.7.4 د الکاینونو نسبي ثبات','heading')
add('Like alkenes, the alkynes also exhibit stability to varying degree. The stability of alkynes, also depends on factors like position of the triple bond in the molecule and number and nature of the substituents attached to triple bonded carbon atoms. Generally non-terminal alkynes are relatively more stable than terminal alkynes.',
 'الکینز (دوہرے بند والے) کی طرح الکائنز بھی مختلف درجے کی پائیداری ظاہر کرتے ہیں۔ الکائنز کی پائیداری بھی سالمے میں تہرے بند کے مقام اور تہرے بند والے کاربن ایٹموں سے جڑے متبادلات کی تعداد اور نوعیت جیسے عوامل پر منحصر ہے۔ عام طور پر غیر ٹرمینل الکائنز ٹرمینل الکائنز سے نسبتاً زیادہ پائیدار ہوتے ہیں۔',
 'د الکینونو په څېر الکاینونه هم په بېلابېلو کچو ثبات ښيي. د الکاینونو ثبات هم په مالیکول کې د درې ګوني تړون پر موقعیت او له درې ګوني تړلو کاربني اټومونو سره د نښتو بدیلونو پر شمېر او ډول پورې اړه لري. عموماً غیر ټرمینل الکاینونه له ټرمینل الکاینونو نسبتاً ډېر ثابت دي.')
add('The stabilities of various isomeric alkynes can be compared, by measuring their heats of hydrogenation or heats of combustion. Stable alkynes evolve small amount of heat upon combustion and hydrogenation and vice versa.',
 'مختلف ہم ترکیب الکائنز کی پائیداری کا موازنہ ان کی حرارتِ ہائیڈروجینیشن یا حرارتِ احتراق ناپ کر کیا جا سکتا ہے۔ پائیدار الکائنز احتراق اور ہائیڈروجینیشن پر کم حرارت خارج کرتے ہیں اور اس کے برعکس۔',
 'د بېلابېلو ایزومري الکاینونو ثبات د هغوی د هایدروجینېشن یا سوځېدو د تودوخې په اندازه کولو پرتله کېدای شي. ثابت الکاینونه د سوځېدو او هایدروجینېشن پر مهال لږه تودوخه خوشې کوي او برعکس.')
add('For example butyne has two isomers i.e. but-1-yne and but-2-yne. Upon hydrogenation but-1-yne releases large amount of heat than but-2-yne, therefore but-1-yne is less stable than but-2-yne.',
 'مثلاً بیوٹائن کے دو آئسومر ہیں، یعنی بیوٹ-1-ائن اور بیوٹ-2-ائن۔ ہائیڈروجینیشن پر بیوٹ-1-ائن، بیوٹ-2-ائن سے زیادہ حرارت خارج کرتا ہے، اس لیے بیوٹ-1-ائن، بیوٹ-2-ائن سے کم پائیدار ہے۔',
 'د بېلګې په توګه بیوټاین دوه ایزومرونه لري، یعنې بیوټ-1-این او بیوټ-2-این. د هایدروجینېشن پر مهال بیوټ-1-این له بیوټ-2-این ډېره تودوخه خوشې کوي، نو بیوټ-1-این له بیوټ-2-این لږ ثابت دی.')
visual('chem12-p70-butyne-hydrogenation',stability)
add('16.7.5 Preparation of Alkynes by Elimination Reactions','16.7.5 اخراجی تعاملات سے الکائنز کی تیاری','16.7.5 د ایستلو تعاملونو په واسطه د الکاینونو چمتو کول','heading')
add('Elimination reactions involve the removal of atoms or groups from two adjacent carbon atoms to form pi bond. This is also called 1,2-elimination or β-elimination (Section 17.1.7). These reactions result in the formation of unsaturated compounds. Alkyne can be prepared by the following elimination reactions.',
 'اخراجی تعاملات میں دو ملحقہ کاربن ایٹموں سے ایٹم یا گروپ ہٹا کر پائی بند بنایا جاتا ہے۔ اسے 1،2-اخراج یا β-اخراج بھی کہتے ہیں (حصہ 17.1.7)۔ ان تعاملات سے غیر سیر شدہ مرکبات بنتے ہیں۔ الکائن درج ذیل اخراجی تعاملات سے تیار کیا جا سکتا ہے۔',
 'د ایستلو تعاملونو کې له دوو ګاونډیو کاربني اټومونو څخه اټومونه یا ګروپونه لرې کېږي څو پای تړون جوړ شي. دې ته 1،2-ایستنه یا β-ایستنه هم وايي (برخه 17.1.7). دا تعاملونه نامشبوع مرکبات جوړوي. الکاین د لاندې ایستلو تعاملونو په واسطه چمتو کېدای شي.')
add('16.7.5.1 Dehydrohalogenation of Vicinal Dihalides','16.7.5.1 وسینل ڈائی ہیلائیڈز کی ڈی ہائیڈروہیلوجینیشن','16.7.5.1 د وېسینل ډای هالایډونو ډی هایدروهالوجینېشن','heading')
add('Vicinal and geminal dihalides, when treated with alcoholic potassium hydroxide or sodium amide in liquid ammonia, form alkynes. It is a two step reaction. The elimination product of the first step (vinyl halide), is treated with stronger base such as sodium amide to remove another molecule of HX.',
 'وسینل اور جیمینل ڈائی ہیلائیڈز کو الکوحلی پوٹاشیم ہائیڈروآکسائیڈ یا مائع امونیا میں سوڈیم امائیڈ سے عمل کرایا جائے تو الکائنز بنتے ہیں۔ یہ دو مرحلوں والا تعامل ہے۔ پہلے مرحلے کی اخراجی پیداوار (وائنائل ہیلائیڈ) کو سوڈیم امائیڈ جیسی زیادہ طاقتور اساس سے عمل کرا کر HX کا ایک اور سالمہ ہٹایا جاتا ہے۔',
 'وېسینل او جېمینل ډای هالایډونه چې له الکولي پوټاشیم هایدروکساید یا په مایع امونیا کې له سوډیم اماید سره تعامل وکړي، الکاینونه جوړوي. دا دوه پړاوه تعامل دی. د لومړي پړاو د ایستلو محصول (وینایل هالایډ) له قوي قلوي لکه سوډیم اماید سره تعامل ورکول کېږي څو د HX بل مالیکول لرې شي.')

record=section('16.17','Acetylene structure, alkyne properties, stability and preparation','ایسیٹیلین کی ساخت، الکائنز کی خصوصیات، پائیداری اور تیاری','د اسیتیلین جوړښت، د الکاینونو ځانګړنې، ثبات او چمتو کول',paras,layout,blocks,'132–133')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':70,'printedPages':[132,133]}]
record['sourceContinuesOnPdfPage']=71
issues=[{'id':'chem12-p133-table-number','printedPage':133,'description':'Alkyne table is printed as "Table 16.4", duplicating the earlier Table 16.4 (oxidation numbers, printed 114). Source numbering retained.'},
        {'id':'chem12-p133-table-alignment','printedPage':133,'description':'Printed melting/boiling columns are vertically offset by half a row; values paired row-by-row in printed order (acetylene −81/−84 … pent-2-yne −90/55).'}]
carry=[{'from':'16.17','to':'16.18','startsAt':'H1C-CH, + KOH'}]
if __name__=='__main__':save(70,[record],carry=carry,issues=issues,chapter_number=16)
