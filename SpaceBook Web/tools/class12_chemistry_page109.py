"""PDF109 printed210–211: phenol resonance, physical properties, acidity of phenols, preparation (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow109');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'dipolar resonance structures':('دو قطبی ریزونینس ساختیں','دوه قطبي ریزونانس جوړښتونه'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'ethoxide ion':('ایتھوآکسائیڈ آئن','ایتوکساید ایون'),
   'phenol':('فینول','فینول'),'phenoxide ion':('فینو آکسائیڈ آئن','فینوکساید ایون'),'sodium phenoxide':('سوڈیم فینو آکسائیڈ','سوډیم فینوکساید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def P(cx,cy,r):return [(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
def ring(cx,cy,r=26,dbl=(0,2,4),sub=None,charge=None,exo=False):
 s=F.ring(cx,cy,r,kek=False,subs={0:sub} if sub else None);pts=P(cx,cy,r)
 for i in dbl:
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.76;s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 if exo:x,y=pts[0];s+=line(x+4,y,x+4,y-14)
 if charge:x,y=pts[charge];s+=t(cx+(x-cx)*1.35,cy+(y-cy)*1.35+5,'⊖',14)
 return s
def resonance(lang,sub,exo_sub,brace):
 s=F.start(150)
 forms=[((0,2,4),None,False,sub),((2,4),1,True,exo_sub),((1,4),3,True,exo_sub),((1,3),5,True,exo_sub),((0,2,4),None,False,sub)]
 for k,(dbl,ch,exo,lab) in enumerate(forms):
  x=80+k*170;s+=ring(x,80,26,dbl,lab,ch,exo)
  if k<4:s+=t(x+85,87,'⟷',20)
 if brace:s+=f'<path d="M230 125 Q230 135 390 135 Q420 135 420 145 Q420 135 450 135 Q610 135 610 125" fill="none" stroke="#222"/>'+t(420,148,lb(lang,'dipolar resonance structures'),12)
 return s.replace('viewBox="0 0 850 150"','viewBox="0 0 850 160"')+'</svg>'
def ion(lang,kind):
 s=F.start(90)
 if kind=='ethyl':s+=t(200,40,'CH₃—CH₂—OH  +  H₂O',17)+t(160,62,lb(lang,'ethyl alcohol'),12)+F.eq(330,420,34)+t(560,40,'CH₃—CH₂—O⁻  +  H₃O⁺',17)+t(540,62,lb(lang,'ethoxide ion'),12)+t(740,32,'Ka = 10⁻¹⁶',13)+t(740,52,'pKa = 16',13)
 else:s+=ring(110,45,24)+line(134,45,150,45)+t(200,51,'OH  +  H₂O',16)+t(110,84,lb(lang,'phenol'),12)+F.eq(280,370,45)+ring(430,45,24)+line(454,45,470,45)+t(510,51,'O⁻  +  H₃O⁺',16)+t(430,84,lb(lang,'phenoxide ion'),12)+t(720,40,'Ka = 10⁻¹⁰',13)+t(720,60,'pKa = 10',13)
 return s+'</svg>'
def salts(lang):
 s=F.start(250)
 for i,(reag,extra) in enumerate((('+ NaOH','+ H₂O'),('+ Na','+ ½H₂'))):
  y=70+130*i;s+=ring(170,y,26,sub='OH')+t(170,y+48,lb(lang,'phenol'),12)+t(260,y+6,reag,16)+F.arrow(320,420,y)+ring(500,y,26,sub='O⁻Na⁺')+t(500,y+48,lb(lang,'sodium phenoxide'),12)+t(620,y+6,extra,16)
 return s+'</svg>'

add('double-bond character that results from conjugation of the unshared electron pair of oxygen with the aromatic ring.','(یہ جملہ پچھلے حصے میں مکمل کیا گیا ہے؛) آکسیجن کے غیر مشترک الیکٹرانی جوڑے کی ارومیٹک حلقے سے کنجوگیشن کی ریزونینس صورتیں:','(دا جمله په تېره برخه کې بشپړه شوې؛) د اروماتیکې کړۍ سره د اکسیجن د نه شریکې الکتروني جوړې د کانجوګېشن ریزونانس بڼې:')
paras.pop();layout.pop()
visual('chem12-p109-phenol-resonance',lambda l:resonance(l,':ÖH','⊕OH',True))
add('18.2.3 Physical Properties','18.2.3 طبعی خصوصیات','18.2.3 فزیکي ځانګړنې','heading')
for e,u,p in [('Phenols are colourless liquids or low melting crystalline solids at room temperature and pressure.','فینولز کمرے کے درجہ حرارت اور دباؤ پر بے رنگ مائع یا کم نقطۂ پگھلاؤ والے قلمی ٹھوس ہیں۔','فینولونه د کوټې په تودوخه او فشار کې بې رنګه مایعات یا د ټیټ ویلې کېدو ټکي کرسټلي جامدات دي.'),
 ('They have a characteristic odour.','ان کی مخصوص بو ہوتی ہے۔','ځانګړی بوی لري.'),
 ('The boiling points of phenols are slightly higher than that of aliphatic alcohols of comparable molecular weights, due to the presence of stronger hydrogen bonding in phenols than in alcohols. The melting and boiling points of phenols is 41°C and 182°C respectively.','الکوحلز کے مقابلے میں فینولز میں زیادہ مضبوط ہائیڈروجن بندش کی وجہ سے فینولز کے نقطۂ جوش ملتے جلتے سالماتی وزن کے ایلیفیٹک الکوحلز سے قدرے زیادہ ہیں۔ فینولز کے نقطۂ پگھلاؤ اور نقطۂ جوش بالترتیب 41°C اور 182°C ہیں۔','په فینولونو کې د الکولونو په پرتله د قوي هایدروجني تړون د شتون له امله د فینولونو د ایشېدو ټکي د ورته مالیکولي وزن لرونکو الیفاتیکو الکولونو یو څه لوړ دي. د فینولونو د ویلې کېدو او ایشېدو ټکي په ترتیب سره 41°C او 182°C دي.'),
 ('Due to stronger hydrogen bonding, phenols are more soluble in water than alcohols of comparable molecular mass.','زیادہ مضبوط ہائیڈروجن بندش کی وجہ سے فینولز ملتی جلتی سالماتی کمیت کے الکوحلز سے پانی میں زیادہ حل پذیر ہیں۔','د قوي هایدروجني تړون له امله فینولونه د ورته مالیکولي کتلې لرونکو الکولونو په پرتله په اوبو کې ډېر حلېږي.')]:
 add(e,u,p,'list')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Phenol and its derivatives are used as disinfectant and germicide.','فینول اور اس کے مشتقات جراثیم کش اور ضد جراثیم کے طور پر استعمال ہوتے ہیں۔','فینول او د هغه مشتقات د ضد عفوني او میکروب وژونکو په توګه کارېږي.')
add('18.2.4 Acidity of Phenols','18.2.4 فینولز کی تیزابیت','18.2.4 د فینولونو تېزابیت','heading')
add('Phenols are much more acidic than alcohols and water but are less acidic than carboxylic acids. This is clear from the pKa values of these compounds, given in Table 8.2.','فینولز الکوحلز اور پانی سے کہیں زیادہ تیزابی ہیں مگر کاربوکسیلک ایسڈز سے کم تیزابی ہیں۔ یہ ان مرکبات کی pKa اقدار سے واضح ہے جو جدول 8.2 میں دی گئی ہیں۔','فینولونه له الکولونو او اوبو ډېر تېزابي دي خو له کاربوکسیلیک اسیدونو لږ تېزابي دي. دا د دې مرکباتو له pKa ارزښتونو څرګندېږي چې په جدول 8.2 کې ورکړل شوي.')
tb={'id':'chem12-table18-2','headers':['Compound','Formula','Ka (approx)','pKa'],'rows':[['Phenol','Ph–OH','10⁻¹⁰','10'],['Alcohols','R–OH','10⁻¹⁶–10⁻¹⁸','16 – 18'],['Carboxylic acids','R–COOH','≈ 10⁻⁵','≈ 5'],['Water','H–OH','1.8×10⁻¹⁶','15.7']],
 'translations':[{'language':'اردو','headers':['مرکب','فارمولا','Ka (تقریباً)','pKa'],'rows':[['فینول','Ph–OH','10⁻¹⁰','10'],['الکوحلز','R–OH','10⁻¹⁶–10⁻¹⁸','16 – 18'],['کاربوکسیلک ایسڈز','R–COOH','≈ 10⁻⁵','≈ 5'],['پانی','H–OH','1.8×10⁻¹⁶','15.7']]},
                 {'language':'پښتو','headers':['مرکب','فورمول','Ka (نږدې)','pKa'],'rows':[['فینول','Ph–OH','10⁻¹⁰','10'],['الکولونه','R–OH','10⁻¹⁶–10⁻¹⁸','16 – 18'],['کاربوکسیلیک اسیدونه','R–COOH','≈ 10⁻⁵','≈ 5'],['اوبه','H–OH','1.8×10⁻¹⁶','15.7']]}]}
add('Table 18.2 Ka and pKa Values of some Compounds','جدول 18.2 بعض مرکبات کی Ka اور pKa اقدار','جدول 18.2 د ځینو مرکباتو Ka او pKa ارزښتونه')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('To help us understand why phenols are more acidic than alcohols, let’s compare the ionization equilibria for phenol and ethyl alcohol.','یہ سمجھنے کے لیے کہ فینولز الکوحلز سے زیادہ تیزابی کیوں ہیں، فینول اور ایتھائل الکوحل کے آئنائزیشن توازن کا موازنہ کرتے ہیں۔','د دې د پوهېدو لپاره چې فینولونه ولې له الکولونو ډېر تېزابي دي، راځئ د فینول او ایتیل الکول د ایونایزېشن توازنونه پرتله کړو.')
visual('chem12-p109-ethanol-ionization',lambda l:ion(l,'ethyl'))
visual('chem12-p109-phenol-ionization',lambda l:ion(l,'phenol'))
add('The negative charge in ethoxide ion is localized on oxygen and is stabilized only by solvation forces. While in phenoxide ion the negative charge spreads throughout the benzene ring and is thereby dispersed. This delocalization of the charge accounts for the stability of the phenoxide ion. The acidic nature of phenols, as compared to alcohols, can be attributed to the formation of stable phenoxide ions after loss of proton.',
 'ایتھوآکسائیڈ آئن میں منفی چارج آکسیجن پر مقامی ہوتا ہے اور صرف سولویشن قوتوں سے پائیدار ہوتا ہے۔ جبکہ فینو آکسائیڈ آئن میں منفی چارج پورے بینزین حلقے میں پھیل کر بکھر جاتا ہے۔ چارج کی یہ غیر مقامیت فینو آکسائیڈ آئن کی پائیداری کی وجہ ہے۔ الکوحلز کے مقابلے میں فینولز کی تیزابی نوعیت پروٹان کھونے کے بعد پائیدار فینو آکسائیڈ آئن بننے سے منسوب کی جا سکتی ہے۔',
 'په ایتوکساید ایون کې منفي چارج پر اکسیجن ځایي دی او یوازې د سولویشن د ځواکونو په واسطه ثابتېږي. په داسې حال کې چې په فینوکساید ایون کې منفي چارج په ټوله بنزیني کړۍ کې خپرېږي او په دې توګه ویشل کېږي. د چارج دا غیر ځایي کېدنه د فینوکساید ایون د ثبات لامل ده. د الکولونو په پرتله د فینولونو تېزابي طبیعت د پروټون له لاسه ورکولو وروسته د ثابت فینوکساید ایون جوړېدو ته منسوب کېدای شي.')
visual('chem12-p109-phenoxide-resonance',lambda l:resonance(l,':Ö:⁻',':O',False))
add('Being more acidic, phenol reacts with NaOH or KOH or sodium metal to form salt. Alcohols do not undergo reaction with NaOH and KOH but can react with sodium metal only.','زیادہ تیزابی ہونے کی وجہ سے فینول NaOH یا KOH یا سوڈیم دھات سے تعامل کر کے نمک بناتا ہے۔ الکوحلز NaOH اور KOH سے تعامل نہیں کرتے بلکہ صرف سوڈیم دھات سے تعامل کر سکتے ہیں۔','ډېر تېزابي کېدو له امله فینول له NaOH یا KOH یا سوډیم فلز سره تعامل کوي او مالګه جوړوي. الکولونه له NaOH او KOH سره تعامل نه کوي خو یوازې له سوډیم فلز سره تعامل کولی شي.')
visual('chem12-p109-phenoxide-salts',salts)
add('18.2.5 Preparation of Phenols','18.2.5 فینولز کی تیاری','18.2.5 د فینولونو چمتو کول','heading')
add('Phenols can be prepared by the following methods.','فینولز درج ذیل طریقوں سے تیار کیے جا سکتے ہیں۔','فینولونه په لاندې طریقو چمتو کېدای شي.')
add('18.2.5.1 From Benzenesulphonic acid','18.2.5.1 بینزین سلفونک ایسڈ سے','18.2.5.1 له بنزین سلفونیک اسید څخه','heading')
add('This method involves the fusion of sodium benzenesulphonate with solid sodium hydroxide at 300–350°C. The benzenesulphonic acid is prepared by sulfonation of benzene with fuming sulphuric acid (Section 16.8.5.2.3).','اس طریقے میں سوڈیم بینزین سلفونیٹ کو 300–350°C پر ٹھوس سوڈیم ہائیڈروآکسائیڈ کے ساتھ پگھلایا جاتا ہے۔ بینزین سلفونک ایسڈ دھواں دار سلفیورک ایسڈ سے بینزین کی سلفونیشن کر کے تیار کیا جاتا ہے (حصہ 16.8.5.2.3)۔','په دې طریقه کې سوډیم بنزین سلفونېټ په 300–350°C کې له جامد سوډیم هایدروکساید سره ویلې کېږي. بنزین سلفونیک اسید د لوګی لرونکي سلفوریک اسید سره د بنزین د سلفونېشن په واسطه جوړېږي (برخه 16.8.5.2.3).')
record=section('18.9','Physical properties, acidity and preparation of phenols','فینولز کی طبعی خصوصیات، تیزابیت اور تیاری','د فینولونو فزیکي ځانګړنې، تېزابیت او چمتو کول',paras,layout,blocks,'210–211')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':109,'printedPages':[210,211]}]
record['sourceContinuesOnPdfPage']=110
issues=[{'id':'chem12-p210-table-ref','printedPage':210,'description':'Text cites "Table 8.2" for the table printed as Table 18.2; retained.'}]
trim=[{'id':'18.10','startsAt':'211\n03'}]
if __name__=='__main__':save(109,[record],trim=trim,issues=issues,chapter_number=18)
