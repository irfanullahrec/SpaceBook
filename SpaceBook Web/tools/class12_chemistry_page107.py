"""PDF107 printed206–207: PCC oxidation, oxidation of 2°/3° alcohols, cleavage of 1,2-diols, thiols (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,_w
F=Fig('arrow107');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'1° -alcohol':('1° -الکوحل','1° -الکول'),'aldehyde':('الڈیہائیڈ','الدیهاید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'2° -alcohol':('2° -الکوحل','2° -الکول'),
   'ketone':('کیٹون','کیټون'),'isopropyl alcohol':('آئسوپروپائل الکوحل','ایزوپروپیل الکول'),'acetone':('ایسیٹون','اسیتون'),'3° -alcohol':('3° -الکوحل','3° -الکول'),'no oxidation reaction':('کوئی تکسیدی تعامل نہیں','هېڅ اکسیډېشن تعامل نشته'),
   'ethylene glycol':('ایتھیلین گلائیکول','ایتیلین ګلایکول'),'(ethane-1,2-diol)':('(ایتھین-1،2-ڈائی اول)','(ایتان-1،2-ډای ول)'),'formaldehyde':('فارم الڈیہائیڈ','فورمالدیهاید'),'propylene glycol':('پروپیلین گلائیکول','پروپیلین ګلایکول'),'(propane-1,2-diol)':('(پروپین-1،2-ڈائی اول)','(پروپان-1،2-ډای ول)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lay(x,y,l,r,size=16):
 toks=[l,'—','C','—',r];tot=sum(_w(k) for k in toks);cx=x-tot/2;out='';cc=0
 for k in toks:
  w=_w(k);out+=t(cx+w/2,y,k,size)
  if k=='C':cc=cx+w/2
  cx+=w
 return out,cc
def carbonyl(x,y,l,r):o,c=lay(x,y,l,r);return o+t(c,y-36,'O',14)+line(c-3,y-30,c-3,y-15)+line(c+3,y-30,c+3,y-15)
def tetra(x,y,top,l,r,bot):o,c=lay(x,y,l,r);return o+t(c,y-36,top,14)+line(c,y-30,c,y-15)+line(c,y+7,c,y+22)+t(c,y+38,bot,14)
def ox(lang,items,cond):
 s=F.start(130*len(items)+10)
 for i,(l,r,bot,n1,pl,pr,n2) in enumerate(items):
  y=60+130*i;s+=tetra(140,y,'OH',l,r,bot)+t(240,y,'+ [O]',16)+t(140,y+60,lb(lang,n1),12)+F.arrow(300,440,y-6,cond,'' if pl=='no oxidation reaction' else '−H₂O')
  s+=(t(580,y,lb(lang,pl),15) if pl=='no oxidation reaction' else carbonyl(580,y,pl,pr)+t(580,y+26,lb(lang,n2),12))
 return s+'</svg>'
def diol(lang):
 s=F.start(390)
 for i,(top,bot,n,n2,p2) in enumerate((('H','H','ethylene glycol','(ethane-1,2-diol)',('H','H','formaldehyde')),('CH₃','H','propylene glycol','(propane-1,2-diol)',('CH₃','H','acetaldehyde')))):
  y=70+185*i;s+=t(122,y-40,top,14)+line(122,y-34,122,y-16)+t(130,y,'H—C—OH',15)+line(122,y+8,122,y+28)+t(130,y+44,'H—C—OH',15)+line(122,y+52,122,y+68)+t(122,y+84,bot,14)
  s+=t(110,y+104,lb(lang,n),12)+t(110,y+118,lb(lang,n2),12)+t(240,y+24,'+ HIO₄',15)+F.arrow(290,350,y+18)
  s+=carbonyl(410,y+24,'H','H')+t(410,y+50,lb(lang,'formaldehyde'),12)+t(475,y+24,'+',15)+carbonyl(545,y+24,p2[0],p2[1])+t(545,y+50,lb(lang,p2[2]),12)+t(700,y+24,'+ HIO₃ + H₂O',15)
 return s+'</svg>'

add('Assume that the oxygen shown in square brackets is delivered by any of the above oxidizing agents. Oxidation of primary alcohol to aldehydes requires special oxidizing agents such as Pyridinium Chlorochromate (PCC), C₅H₅N⁺HClCrO₃⁻. PCC is formed when chromic oxide is dissolved in HCl and then treated with pyridine in dichrolomethane solvent.',
 'فرض کریں کہ مربع قوسین میں دکھائی گئی آکسیجن اوپر کے کسی بھی تکسیدی عامل سے فراہم ہوتی ہے۔ ابتدائی الکوحل کی الڈیہائیڈز تک تکسید کے لیے خاص تکسیدی عامل درکار ہیں، جیسے پیریڈینیم کلوروکرومیٹ (PCC)، C₅H₅N⁺HClCrO₃⁻۔ PCC اس وقت بنتا ہے جب کرومک آکسائیڈ کو HCl میں حل کر کے ڈائی کلورو میتھین محلل میں پیریڈین سے عمل کرایا جائے۔',
 'فرض کړئ چې په مربع قوسونو کې ښودل شوی اکسیجن د پورته هر اکسیډایز کوونکي عامل له خوا ورکول کېږي. الدیهایډونو ته د لومړني الکول اکسیډېشن ځانګړي اکسیډایز کوونکي عاملونه غواړي لکه پیریډینیم کلوروکرومېټ (PCC)، C₅H₅N⁺HClCrO₃⁻. PCC هغه وخت جوړېږي چې کرومیک اکساید په HCl کې حل او بیا په ډای کلورومیتان محلل کې له پیریډین سره تعامل وکړي.')
visual('chem12-p107-pcc',lambda l:ox(l,[('R','H','H','1° -alcohol','R','H','aldehyde'),('CH₃','H','H','ethyl alcohol','CH₃','H','acetaldehyde')],'PCC, CH₂Cl₂'))
add('Secondary alcohols are oxidized to ketones by the same reagents that oxidize primary alcohols. The further oxidation of ketones to carboxylic acids needs even more drastic conditions (Section 19.6.4).','ثانوی الکوحلز کی کیٹونز تک تکسید انہی عاملوں سے ہوتی ہے جو ابتدائی الکوحلز کی تکسید کرتے ہیں۔ کیٹونز کی مزید کاربوکسیلک ایسڈز تک تکسید کے لیے اور بھی سخت شرائط درکار ہیں (حصہ 19.6.4)۔','دویمي الکولونه د همغو عاملونو په واسطه کیټونونو ته اکسیډایز کېږي چې لومړني الکولونه اکسیډایز کوي. د کیټونونو نور اکسیډېشن کاربوکسیلیک اسیدونو ته لا سخت شرایط غواړي (برخه 19.6.4).')
visual('chem12-p107-secondary',lambda l:ox(l,[('R','H','R','2° -alcohol','R','H','ketone'),('CH₃','H','CH₃','isopropyl alcohol','CH₃','CH₃','acetone')],''))
add('Tertiary alcohols have no hydrogen on their hydroxyl-bearing carbon (α-hydrogen) and do not undergo oxidation readily.','ثالثی الکوحلز کے ہائیڈروآکسل والے کاربن پر کوئی ہائیڈروجن (α-ہائیڈروجن) نہیں ہوتا اور ان کی تکسید آسانی سے نہیں ہوتی۔','درېیمي الکولونه پر هایدروکسیل لرونکي کاربن هایدروجن (α-هایدروجن) نه لري او په اسانۍ اکسیډایز نه کېږي.')
visual('chem12-p107-tertiary',lambda l:ox(l,[('R','R','R','3° -alcohol','no oxidation reaction','','')],''))
add('18.1.7.6 Cleavage of 1, 2 diols','18.1.7.6 1،2 ڈائی اولز کی شکست','18.1.7.6 د 1،2 ډای اولونو ماتول','heading')
add('1,2–diols or vicinal diols, are dihydric alcohols containing two hydroxyl groups on adjacent carbon atoms. They are also called glycols. For example, ethylene glycol, propylene glycol etc (Section 18.1.1).','1،2–ڈائی اولز یا وسینل ڈائی اولز وہ ڈائی ہائیڈرک الکوحلز ہیں جن کے ملحقہ کاربن ایٹموں پر دو ہائیڈروآکسل گروپ ہوں۔ انہیں گلائیکولز بھی کہتے ہیں۔ مثلاً ایتھیلین گلائیکول، پروپیلین گلائیکول وغیرہ (حصہ 18.1.1)۔','1،2–ډای اولونه یا وېسینل ډای اولونه هغه ډای هایدریک الکولونه دي چې پر ګاونډیو کاربني اټومونو دوه هایدروکسیل ګروپونه لري. ګلایکولونه هم بلل کېږي. لکه ایتیلین ګلایکول، پروپیلین ګلایکول او نور (برخه 18.1.1).')
add('A characteristic reaction of vicinal diols is their oxidative cleavage. The most common reagent used for oxidative cleavage of vicinal diol is periodic acid (HIO₄). The carbon–carbon bond of the vicinal diol unit is broken and two carbonyl groups result. Periodic acid is reduced to iodic acid (HIO₃). For example cleavage of ethylene glycol with periodic acid yields two molecules of formaldehydes, while propylene glycol yields mixture of formaldehyde and acetaldehyde.',
 'وسینل ڈائی اولز کا ایک خصوصی تعامل ان کی تکسیدی شکست ہے۔ وسینل ڈائی اول کی تکسیدی شکست کے لیے سب سے عام عامل پیریوڈک ایسڈ (HIO₄) ہے۔ وسینل ڈائی اول اکائی کا کاربن–کاربن بند ٹوٹ جاتا ہے اور دو کاربونل گروپ بنتے ہیں۔ پیریوڈک ایسڈ کی تخفیف آئیوڈک ایسڈ (HIO₃) میں ہوتی ہے۔ مثلاً پیریوڈک ایسڈ سے ایتھیلین گلائیکول کی شکست فارم الڈیہائیڈ کے دو سالمات دیتی ہے، جبکہ پروپیلین گلائیکول فارم الڈیہائیڈ اور ایسیٹ الڈیہائیڈ کا آمیزہ دیتا ہے۔',
 'د وېسینل ډای اولونو ځانګړی تعامل د هغوی اکسیډیټیف ماتېدل دي. د وېسینل ډای اول د اکسیډیټیف ماتولو لپاره تر ټولو عام عامل پیریوډیک اسید (HIO₄) دی. د وېسینل ډای اول واحد کاربن–کاربن تړون ماتېږي او دوه کاربونیل ګروپونه جوړېږي. پیریوډیک اسید ایوډیک اسید (HIO₃) ته ارجاع کېږي. د بېلګې په توګه له پیریوډیک اسید سره د ایتیلین ګلایکول ماتېدل د فورمالدیهاید دوه مالیکولونه ورکوي، خو پروپیلین ګلایکول د فورمالدیهاید او اسیټالدیهاید ګډوله ورکوي.')
visual('chem12-p107-diol-cleavage',diol)
add('Self-assessmnet','خود جانچ','ځان ارزونه','heading')
add('What are the oxidation states of the iodine in HIO₄ and HIO₃?','HIO₄ اور HIO₃ میں آئیوڈین کی تکسیدی حالتیں کیا ہیں؟','په HIO₄ او HIO₃ کې د ایوډین اکسیډېشن حالتونه څه دي؟')
add('18.1.8 The Sulphur Analogues (Thiols, RSH)','18.1.8 سلفر مماثلات (تھائیولز، RSH)','18.1.8 د سلفر ورته مرکبات (تیولونه، RSH)','heading')
add('Sulfur lies just below oxygen in the periodic table, and many oxygen-containing organic compounds have sulfur analogues. The sulfur analogues of alcohols (R–OH) are thiols (R–SH). The functional group –SH of thiol is also called mercapto group or sulphydryl group. Thiols are also called mercaptans.','دوری جدول میں سلفر آکسیجن کے بالکل نیچے ہے، اور آکسیجن والے بہت سے نامیاتی مرکبات کے سلفر مماثلات ہیں۔ الکوحلز (R–OH) کے سلفر مماثلات تھائیولز (R–SH) ہیں۔ تھائیول کے فعلی گروپ –SH کو مرکیپٹو گروپ یا سلفہائیڈرل گروپ بھی کہتے ہیں۔ تھائیولز کو مرکیپٹینز بھی کہا جاتا ہے۔','په دوراني جدول کې سلفر سم د اکسیجن لاندې پروت دی، او ډېر اکسیجن لرونکي عضوي مرکبات د سلفر ورته مرکبات لري. د الکولونو (R–OH) سلفري ورته مرکبات تیولونه (R–SH) دي. د تیول فعال ګروپ –SH ته مرکاپټو ګروپ یا سلفهایډریل ګروپ هم وايي. تیولونو ته مرکاپټانونه هم وايي.')
add('Common names are formed like those of alcohols, using the name of the alkyl group with the word mercaptan. In IUPAC names, the suffix -thiol is added to the name of the corresponding alkane, and number the chain in the direction that gives the lower locant to the carbon that bears the –SH group.','عام نام الکوحلز کی طرح الکائل گروپ کے نام کے ساتھ لفظ مرکیپٹین لگا کر بنائے جاتے ہیں۔ IUPAC ناموں میں متعلقہ الکین (اکیلے بند والے) کے نام کے ساتھ لاحقہ -thiol لگایا جاتا ہے، اور زنجیر کو اس سمت سے نمبر دیا جاتا ہے جس سے –SH گروپ والے کاربن کو کم نشان دہ عدد ملے۔','عام نومونه د الکولونو په څېر د الکایل ګروپ له نوم سره د مرکاپټان کلمې په کارولو جوړېږي. په IUPAC نومونو کې د اړوند الکان له نوم سره -thiol وروستاړی ورزیاتېږي، او ځنځیر په هغه لوري شمېرل کېږي چې –SH لرونکي کاربن ته ټیټه ځای ښوونکې شمېره ورکړي.')
record=section('18.7','Oxidation of alcohols, diol cleavage and thiols','الکوحلز کی تکسید، ڈائی اول کی شکست اور تھائیولز','د الکولونو اکسیډېشن، د ډای اول ماتېدل او تیولونه',paras,layout,blocks,'206–207')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':107,'printedPages':[206,207]}]
record['sourceContinuesOnPdfPage']=108
issues=[{'id':'chem12-p206-ketone-product','printedPage':206,'description':'General 2° alcohol oxidation product printed as R—C(=O)—H labelled "ketone"; retained as printed. "dichrolomethane" retained. Last thiol sentence completed from printed 208.'}]
trim=[{'id':'18.8','startsAt':'locant to the carbon that bears'}]
if __name__=='__main__':save(107,[record],trim=[],issues=issues,chapter_number=18)
