"""PDF95 printed182–183: amine–water hydrogen bonding, structure of amines, basicity, Table 17.4."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow95');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'1° or 2° amine:':('1° یا 2° امائن:','1° یا 2° امین:'),'hydrogen bond donor and acceptor':('ہائیڈروجن بند دینے اور لینے والا','د هایدروجني تړون ورکوونکی او اخیستونکی'),'3° amine:':('3° امائن:','3° امین:'),
   'hydrogen bond acceptor only':('صرف ہائیڈروجن بند لینے والا','یوازې د هایدروجني تړون اخیستونکی'),'ammonia':('امونیا','امونیا'),'trimethylamine':('ٹرائی میتھائل امائن','ټرای میتایل امین'),
   '1°-amine':('1°-امائن','1°-امین'),'1°-ammonium salt':('1°-امونیم نمک','1°-امونیم مالګه'),'1°-ammonium ion':('1°-امونیم آئن','1°-امونیم ایون'),'methyl amine':('میتھائل امائن','میتایل امین'),
   '(weaker base)':('(کمزور اساس)','(کمزوری قلوي)'),'(stronger base)':('(طاقتور اساس)','(قوي قلوي)'),'stabilized by the alkyl group':('الکائل گروپ سے پائیدار','د الکایل ګروپ په واسطه ثابت شوی')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def amine(x,y,a,b,c,lone=True):
 s=t(x,y+5,'N',16)+line(x-8,y-6,x-24,y-20)+t(x-30,y-24,a,14)+line(x-8,y+6,x-24,y+20)+t(x-32,y+32,b,14)+line(x-12,y+2,x-36,y+4)+t(x-46,y+10,c,14)
 if lone:s+=f'<ellipse cx="{x+24}" cy="{y}" rx="12" ry="8" fill="none" stroke="#222"/>'+t(x+24,y+4,':',12)
 return s
def water(x,y):return t(x,y+5,'O',16)+line(x-6,y+8,x-16,y+24)+t(x-20,y+38,'H',14)+f'<ellipse cx="{x+18}" cy="{y-14}" rx="10" ry="7" fill="none" stroke="#222"/><ellipse cx="{x+18}" cy="{y+16}" rx="10" ry="7" fill="none" stroke="#222"/>'
def hb(lang):
 s=F.start(320)
 s+=amine(130,60,'H','R','R')+t(185,64,'⋯⋯H',15)+line(205,58,225,62)+water(240,70)
 s+=water(520,60)+t(560,64,'⋯⋯',15)+t(600,64,'H',14)+line(608,60,624,62)+t(636,66,'N',16)+line(646,58,662,46)+t(670,42,'R',14)+line(646,72,662,84)+t(670,96,'R',14)+f'<ellipse cx="612" cy="86" rx="10" ry="7" fill="none" stroke="#222"/>'
 s+=t(390,140,lb(lang,'1° or 2° amine:'),12)+t(390,156,lb(lang,'hydrogen bond donor and acceptor'),12)
 s+=amine(330,230,'R','R','R')+t(385,234,'⋯H',15)+line(400,228,418,234)+water(430,240)
 s+=t(390,296,lb(lang,'3° amine:'),12)+t(390,312,lb(lang,'hydrogen bond acceptor only'),12)
 return s+'</svg>'
def pyramid(x,y,subs,angle,name):
 s='<ellipse cx="%d" cy="%d" rx="14" ry="18" fill="none" stroke="#222"/>'%(x,y-40)+t(x,y-38,'••',12)+t(x,y+5,'N',16)+line(x,y-22,x,y-12)
 s+=line(x-8,y+4,x-34,y+16)+t(x-44,y+22,subs[0],14)+line(x+8,y+2,x+34,y-2,1.5,'#222','stroke-dasharray="2 2"')+t(x+48,y+2,subs[1],14)+line(x-2,y+10,x-4,y+30,4)+t(x-4,y+46,subs[2],14)+t(x+46,y+46,angle,14)+t(x,y+66,name,12)
 return s
def struct(lang):return F.start(190)+pyramid(250,100,('H','H','H'),'107.5°',lb(lang,'ammonia'))+pyramid(580,100,('H₃C','CH₃','CH₃'),'108°',lb(lang,'trimethylamine'))+'</svg>'
def salt(lang):
 s=F.start(160)+t(200,40,'R—N̈H₂  +  H—X',17)+t(170,62,lb(lang,'1°-amine'),12)+F.arrow(320,420,34)+t(560,40,'R—N⁺H₃ X⁻',17)+t(560,62,lb(lang,'1°-ammonium salt'),12)
 s+=t(200,120,'R—N̈H₂(aq)  +  H₂O(l)',17)+t(170,142,lb(lang,'1°-amine'),12)+F.eq(340,440,114)+t(580,120,'R—N⁺H₃(aq)  +  ⁻OH(aq)',17)+t(560,142,lb(lang,'1°-ammonium ion'),12)
 return s+'</svg>'
def basic(lang):
 s=F.start(200)+t(150,50,'H—N̈—H  +  H₂O',17)+t(105,74,lb(lang,'ammonia'),12)+F.eq(270,370,44)+t(500,50,'H—N⁺H₃  +  ⁻OH',17)+t(700,40,'pKb = 4.74',14)+t(700,58,lb(lang,'(weaker base)'),12)
 s+=t(150,130,'H₃C—N̈H₂  +  H₂O',17)+t(105,154,lb(lang,'methyl amine'),12)+F.eq(270,370,124)+t(500,130,'H₃C→N⁺H₃  +  ⁻OH',17)+t(700,120,'pKb = 3.36',14)+t(700,138,lb(lang,'(stronger base)'),12)+t(500,170,lb(lang,'stabilized by the alkyl group'),12)
 return s+'</svg>'

visual('chem12-p95-amine-water-hbond',hb)
add('17.3.3 Structure of Amines','17.3.3 امائنز کی ساخت','17.3.3 د امینونو جوړښت','heading')
add('Amines are derivatives of ammonia molecule where one or more hydrogen atoms have been replaced by alkyl or aryl groups. Since, ammonia molecule has trigonal pyramidal shape, the resulting amines also have the same geometry. Nitrogen atom in amine is sp³-hybridized with a lone-pair in one of its sp³–hybrid orbital. The bond angles in amines are close to 107.5°.',
 'امائنز امونیا سالمے کے وہ مشتقات ہیں جن میں ایک یا زیادہ ہائیڈروجن ایٹم الکائل یا ایرائل گروپوں سے بدل دیے گئے ہوں۔ چونکہ امونیا سالمے کی شکل تکونی ہرمی ہے، اس لیے حاصل ہونے والے امائنز کی جیومیٹری بھی یہی ہوتی ہے۔ امائن میں نائٹروجن ایٹم sp³-ہائبرڈ ہوتا ہے جس کے ایک sp³–ہائبرڈ آربیٹل میں تنہا جوڑا ہوتا ہے۔ امائنز میں بند زاویے 107.5° کے قریب ہیں۔',
 'امینونه د امونیا د مالیکول هغه مشتقات دي چې پکې یو یا ډېر هایدروجني اټومونه په الکایل یا اریل ګروپونو بدل شوي وي. څرنګه چې د امونیا مالیکول درې ګوټی هرمي شکل لري، جوړ شوي امینونه هم همدا جیومټري لري. په امین کې نایتروجني اټوم sp³-هایبرېډ دی چې په یوه sp³–هایبرېډ اوربیټال کې یوازینۍ جوړه لري. په امینونو کې د تړون زاویې 107.5° ته نږدې دي.')
visual('chem12-p95-amine-structure',struct)
add('17.3.4 Basicity of Amines','17.3.4 امائنز کی اساسیت','17.3.4 د امینونو قلویت','heading')
add('Due to the presence of a lone pair of electrons on the nitrogen atoms, amines are capable of accepting a proton and are basic in nature. Amines react with acids to form ammonium salts.','نائٹروجن ایٹموں پر الیکٹرانوں کے تنہا جوڑے کی موجودگی کی وجہ سے امائنز پروٹان قبول کرنے کی صلاحیت رکھتے ہیں اور فطرتاً اساسی ہیں۔ امائنز تیزابوں سے تعامل کر کے امونیم نمکیات بناتے ہیں۔','پر نایتروجني اټومونو د الکترونونو د یوازینۍ جوړې د شتون له امله امینونه د پروټون د منلو وړتیا لري او په طبیعت کې قلوي دي. امینونه له اسیدونو سره تعامل کوي او د امونیم مالګې جوړوي.')
add('Amines are weak bases and, therefore when dissolved in water, it abstracts a proton from water to form ammonium and hydroxide ion, and the following equilibrium is established.','امائنز کمزور اساسیں ہیں، اس لیے پانی میں حل ہونے پر یہ پانی سے پروٹان کھینچ کر امونیم اور ہائیڈروآکسائیڈ آئن بناتے ہیں، اور درج ذیل توازن قائم ہوتا ہے۔','امینونه کمزوري قلوي دي، نو کله چې په اوبو کې حل شي، له اوبو پروټون اخلي او امونیم او هایدروکساید ایون جوړوي، او لاندې توازن رامنځته کېږي.')
visual('chem12-p95-amine-salt',salt)
add('Aliphatic amines are stronger bases than ammonia. This is due to the electron donating alkyl group which increases the electronic density of nitrogen, thereby increasing its power of accepting a proton from an acid, and also stabilizes the conjugate acid, ammonium ion.','ایلیفیٹک امائنز امونیا سے زیادہ طاقتور اساسیں ہیں۔ اس کی وجہ الیکٹران دینے والا الکائل گروپ ہے جو نائٹروجن کی الیکٹرانی کثافت بڑھاتا ہے، جس سے تیزاب سے پروٹان قبول کرنے کی اس کی طاقت بڑھتی ہے، اور یہ مزدوج تیزاب، یعنی امونیم آئن، کو بھی پائیدار بناتا ہے۔','الیفاتیک امینونه له امونیا قوي قلوي دي. دا د الکترون ورکوونکي الکایل ګروپ له امله دی چې د نایتروجن الکتروني کثافت زیاتوي، په دې توګه له اسید څخه د پروټون د منلو ځواک یې زیاتوي، او مزدوج اسید، یعنې امونیم ایون، هم ثابتوي.')
visual('chem12-p95-amine-basicity',basic)
add('The greater the number of alkyl groups, the greater will be the electronic density on nitrogen and therefore, greater will be the power of nitrogen to accept proton. We might expect tertiary aliphatic amines would be the strongest and primary aliphatic amines would be weakest. However in aqueous solutions, secondary is more basic than primary and tertiary aliphatic amines. Because ammonium ions (conjugate acid) are charged, they are strongly solvated by water and the energy of solvation contributes to their stability. The additional alkyl groups around the ammonium ions of tertiary amines decrease the number of water molecules that can approach closely and solvate the ions. However, ammonium ions of primary and secondary amines are more stabilized by water through solvation. But the opposing trends of inductive stabilization and steric hindrance of solvation are balanced for secondary alkyl amines, which make them stronger bases than primary or tertiary alkyl amines in aqueous solutions. The pKb values of some amines in water are given in Table 17.4.',
 'الکائل گروپوں کی تعداد جتنی زیادہ ہو گی، نائٹروجن پر الیکٹرانی کثافت اتنی ہی زیادہ ہو گی اور اس لیے نائٹروجن کی پروٹان قبول کرنے کی طاقت اتنی ہی زیادہ ہو گی۔ ہم توقع کر سکتے ہیں کہ ثالثی ایلیفیٹک امائنز سب سے طاقتور اور ابتدائی سب سے کمزور ہوں گے۔ تاہم آبی محلولوں میں ثانوی امائنز ابتدائی اور ثالثی ایلیفیٹک امائنز سے زیادہ اساسی ہیں۔ چونکہ امونیم آئن (مزدوج تیزاب) چارج والے ہیں، اس لیے پانی انہیں مضبوطی سے سولویٹ کرتا ہے اور سولویشن کی توانائی ان کی پائیداری میں حصہ ڈالتی ہے۔ ثالثی امائنز کے امونیم آئنوں کے گرد اضافی الکائل گروپ ان پانی کے سالمات کی تعداد گھٹا دیتے ہیں جو قریب آ کر آئنوں کو سولویٹ کر سکیں۔ تاہم ابتدائی اور ثانوی امائنز کے امونیم آئن سولویشن کے ذریعے پانی سے زیادہ پائیدار ہوتے ہیں۔ لیکن ثانوی الکائل امائنز کے لیے انڈکٹو استحکام اور سولویشن کی فضائی رکاوٹ کے مخالف رجحانات متوازن ہو جاتے ہیں، جو انہیں آبی محلولوں میں ابتدائی یا ثالثی الکائل امائنز سے زیادہ طاقتور اساس بناتے ہیں۔ پانی میں بعض امائنز کی pKb اقدار جدول 17.4 میں دی گئی ہیں۔',
 'د الکایل ګروپونو شمېر چې څومره ډېر وي، پر نایتروجن الکتروني کثافت به هومره ډېر وي او له همدې امله د نایتروجن د پروټون د منلو ځواک به هومره ډېر وي. ښايي تمه وکړو چې درېیمي الیفاتیک امینونه به تر ټولو قوي او لومړني به تر ټولو کمزوري وي. خو په اوبلنو محلولونو کې دویمي امینونه له لومړنیو او درېیمیو الیفاتیکو امینونو ډېر قلوي دي. څرنګه چې امونیم ایونونه (مزدوج اسید) چارج لري، د اوبو په واسطه په کلکه سولویټ کېږي او د سولویشن انرژي یې په ثبات کې ونډه لري. د درېیمیو امینونو د امونیم ایونونو شاوخوا اضافي الکایل ګروپونه د هغو اوبو د مالیکولونو شمېر کموي چې نږدې راتلای او ایونونه سولویټ کولی شي. خو د لومړنیو او دویمیو امینونو امونیم ایونونه د سولویشن له لارې د اوبو په واسطه ډېر ثابتېږي. د دویمیو الکایل امینونو لپاره د انډکټیو ثبات او د سولویشن د فضايي خنډ مخالف رجحانات سره متوازن کېږي، چې په اوبلنو محلولونو کې یې له لومړنیو یا درېیمیو الکایل امینونو قوي قلوي کوي. په اوبو کې د ځینو امینونو pKb ارزښتونه په جدول 17.4 کې ورکړل شوي.')
tb={'id':'chem12-table17-4','headers':['1°–amines','pKb','2°–amines','pKb','3°–amines','pKb'],
 'rows':[['methyl amine','3.36','dimethyl amine','3.28','trimethyl amine','4.25'],['ethyl amine','3.36','diethyl amine','3.01','triethyl amine','3.24'],['n-propyl amine','3.32','di-n-propyl amine','3.00','tri-n-propyl amine','3.35']],
 'translations':[{'language':'اردو','headers':['1°–امائنز','pKb','2°–امائنز','pKb','3°–امائنز','pKb'],'rows':[['میتھائل امائن','3.36','ڈائی میتھائل امائن','3.28','ٹرائی میتھائل امائن','4.25'],['ایتھائل امائن','3.36','ڈائی ایتھائل امائن','3.01','ٹرائی ایتھائل امائن','3.24'],['n-پروپائل امائن','3.32','ڈائی-n-پروپائل امائن','3.00','ٹرائی-n-پروپائل امائن','3.35']]},
                 {'language':'پښتو','headers':['1°–امینونه','pKb','2°–امینونه','pKb','3°–امینونه','pKb'],'rows':[['میتایل امین','3.36','ډای میتایل امین','3.28','ټرای میتایل امین','4.25'],['ایتیل امین','3.36','ډای ایتیل امین','3.01','ټرای ایتیل امین','3.24'],['n-پروپیل امین','3.32','ډای-n-پروپیل امین','3.00','ټرای-n-پروپیل امین','3.35']]}]}
add('Table 17.4 pKb Values of some Amines in Water Solvent','جدول 17.4 پانی کے محلل میں بعض امائنز کی pKb اقدار','جدول 17.4 په اوبو محلل کې د ځینو امینونو pKb ارزښتونه')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
record=section('17.11','Structure and basicity of amines','امائنز کی ساخت اور اساسیت','د امینونو جوړښت او قلویت',paras,layout,blocks,'182–183')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':95,'printedPages':[182,183]}]
record['sourceContinuesOnPdfPage']=96
carry=[{'from':'17.11','to':'17.12','startsAt':'17.3.5 Preparation of Amines'}]
if __name__=='__main__':save(95,[record],carry=carry,chapter_number=17)
