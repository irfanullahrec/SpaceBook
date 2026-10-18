"""PDF69 printed130–131: polarimetry, alkynes, nomenclature and structure of acetylene."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b'):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x} {y}L{a} {b}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow69" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#1e88e5"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
L={'Plane-polarized':('مستوی پولرائزڈ','سطحي پولرایز شوې'),'light':('روشنی','رڼا'),'Solution of optically':('نوری طور پر فعال','د نوري فعال'),
   'active compound':('مرکب کا محلول','مرکب محلول'),'clockwise rotation':('گھڑی کی سمت گردش','د ساعت په لور ګرځښت'),
   '(dextrorotaory isomer)':('(ڈیکسٹرو روٹیٹری آئسومر)','(ډیکسټروروټېټري ایزومر)'),'anti-clockwise rotation':('گھڑی کی مخالف سمت گردش','د ساعت خلاف ګرځښت'),
   '(levorotatory)':('(لیوو روٹیٹری)','(لیووروټېټري)'),'acetylene':('ایسیٹیلین','اسیتیلین'),'methyl acetylene':('میتھائل ایسیٹیلین','میتایل اسیتیلین'),
   'dimethyl acetylene':('ڈائی میتھائل ایسیٹیلین','ډای میتایل اسیتیلین'),'ethyne':('ایتھائن','ایتاین'),'propyne':('پروپائن','پروپاین'),
   'but-1-yne':('بیوٹ-1-ائن','بیوټ-1-این'),'3-methylbut-1-yne':('3-میتھائل بیوٹ-1-ائن','3-میتایل بیوټ-1-این'),'but-2-yne':('بیوٹ-2-ائن','بیوټ-2-این'),
   '3-methylhexa-1,4-diyne':('3-میتھائل ہیکسا-1،4-ڈائی ائن','3-میتایل هېکسا-1،4-ډای این'),'4,5-dimethylhex-2-yne':('4،5-ڈائی میتھائل ہیکس-2-ائن','4،5-ډای میتایل هېکس-2-این')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]

def fig168(lang):
 s=start(215)
 s+='<circle cx="95" cy="90" r="30" fill="none" stroke="#222" stroke-width="2"/>'+line(95,64,95,116,2,'#222','marker-end="url(#arrow69)" marker-start="url(#arrow69)"')
 s+=line(130,90,250,90,3,'#1e88e5','marker-end="url(#arrow69)"')
 s+='<ellipse cx="275" cy="90" rx="12" ry="28" fill="none" stroke="#222" stroke-width="2"/><ellipse cx="365" cy="90" rx="12" ry="28" fill="none" stroke="#222" stroke-width="2"/>'+line(275,62,365,62)+line(275,118,365,118)
 s+=line(380,90,430,90,3,'#1e88e5')+line(430,40,430,155,3,'#1e88e5')+line(430,40,520,40,3,'#1e88e5','marker-end="url(#arrow69)"')+line(430,155,520,155,3,'#1e88e5','marker-end="url(#arrow69)"')
 for cy,d in ((40,1),(155,-1)):
  s+=f'<circle cx="560" cy="{cy}" r="30" fill="none" stroke="#222" stroke-width="2"/>'+line(560-14*d,cy+26,560+14*d,cy-26,2,'#222','marker-end="url(#arrow69)" marker-start="url(#arrow69)"')+line(560,cy-26,560,cy+26,1.5,'#888','stroke-dasharray="3 3"')
 s+=t(95,145,lb(lang,'Plane-polarized'),15)+t(95,163,lb(lang,'light'),15)+t(320,145,lb(lang,'Solution of optically'),15)+t(320,163,lb(lang,'active compound'),15)
 s+=t(700,40,lb(lang,'clockwise rotation'),15)+t(700,58,lb(lang,'(dextrorotaory isomer)'),15)+t(700,155,lb(lang,'anti-clockwise rotation'),15)+t(700,173,lb(lang,'(levorotatory)'),15)
 return s+'</svg>'
def common(lang):
 s=start(130)+t(425,35,'H — C ≡ C — H',22)+t(425,58,lb(lang,'acetylene'),15)
 s+=t(230,100,'CH₃ — C ≡ CH',22)+t(230,123,lb(lang,'methyl acetylene'),15)+t(620,100,'CH₃ — C ≡ C — CH₃',22)+t(620,123,lb(lang,'dimethyl acetylene'),15)
 return s+'</svg>'
def chain(x0,y,toks,size=20,num=None,up=None):
 """Lay out tokens left→right; returns svg. num: {token_index:label} below; up: {token_index:'CH₃'} substituent above."""
 out='';x=x0;cent=[]
 for k in toks:
  w=26 if k in('—','≡','=') else 13*len(k.replace('₃','').replace('₂',''))+10
  cent.append(x+w/2);out+=t(x+w/2,y,k,size);x+=w
 for i,n in (num or {}).items():out+=t(cent[i],y+20,n,12)
 for i,g in (up or {}).items():out+=t(cent[i],y-40,g,18)+line(cent[i],y-34,cent[i],y-18)
 return out,(x0+x)/2
def examples(lang):
 s=start(330)
 def put(x0,y,toks,name,num=None,up=None):
  o,c=chain(x0,y,toks,num=num,up=up);return o+t(c,y+44,lb(lang,name),15)
 s+=put(60,40,['H','—','C','≡','C','—','H'],'ethyne')
 s+=put(320,40,['H','—','C','≡','C','—','CH₃'],'propyne')
 s+=put(580,40,['H','—','C','≡','C','—','CH₂','—','CH₃'],'but-1-yne',{2:'1',4:'2',6:'3',8:'4'})
 s+=put(60,150,['H','—','C','≡','C','—','CH','—','CH₃'],'3-methylbut-1-yne',{2:'1',4:'2',6:'3',8:'4'},{6:'CH₃'})
 s+=put(540,150,['H₃C','—','C','≡','C','—','CH₃'],'but-2-ene' if False else 'but-2-yne',{0:'1',2:'2',4:'3',6:'4'})
 s+=put(40,265,['H₃C','—','C','≡','C','—','CH','—','C','≡','CH'],'3-methylhexa-1,4-diyne',{0:'6',2:'5',4:'4',6:'3',8:'2',10:'1'},{6:'CH₃'})
 s+=put(450,265,['H₃C','—','C','≡','C','—','CH','—','CH','—','CH₃'],'4,5-dimethylhex-2-yne',{0:'1',2:'2',4:'3',6:'4',8:'5',10:'6'},{6:'CH₃',8:'CH₃'})
 return s+'</svg>'

add('said to be levorotatory isomer or (–)-isomer (Figure 16.8). Polarimetry is a common method used to distinguish between enantiomers, based on their ability to rotate the plane of polarized light in opposite directions.',
 'لیوو روٹیٹری آئسومر یا (–)-آئسومر کہلاتا ہے (شکل 16.8)۔ پولری میٹری اینینشیومرز میں امتیاز کا ایک عام طریقہ ہے، جو پولرائزڈ روشنی کے مستوی کو مخالف سمتوں میں گھمانے کی ان کی صلاحیت پر مبنی ہے۔',
 'لیووروټېټري ایزومر یا (–)-ایزومر بلل کېږي (شکل 16.8). پولاریمېټري د اینانټیومرونو د توپیر یوه عامه طریقه ده، چې د پولرایز شوې رڼا د سطحې مخالفو لورو ته د ګرځولو پر وړتیا ولاړه ده.')
visual('chem12-figure16-8',fig168)
add('Figure 16.8 Rotation of plane-polarized light in different direction by two enantiomers.','شکل 16.8 دو اینینشیومرز کے ذریعے مستوی پولرائزڈ روشنی کی مختلف سمتوں میں گردش۔','شکل 16.8 د دوو اینانټیومرونو په واسطه د سطحي پولرایز شوې رڼا په بېلو لورو ګرځښت.')
add('16.7 Alkynes','16.7 الکائنز','16.7 الکاینونه','heading')
add('Alkynes are unsaturated hydrocarbons which contain a carbon–carbon triple bond. They can be represented by the general formula CₙH₂ₙ₋₂. The first and most important member of this series is acetylene (HC≡CH) and hence these are generally called acetylenes. The carbon-carbon triple bond is therefore called acetylenic bond.',
 'الکائنز غیر سیر شدہ ہائیڈروکاربن ہیں جن میں کاربن–کاربن تہرا بند ہوتا ہے۔ انہیں عمومی فارمولا CₙH₂ₙ₋₂ سے ظاہر کیا جا سکتا ہے۔ اس سلسلے کا پہلا اور سب سے اہم رکن ایسیٹیلین (HC≡CH) ہے، اسی لیے انہیں عام طور پر ایسیٹیلینز کہا جاتا ہے۔ چنانچہ کاربن–کاربن تہرے بند کو ایسیٹیلینک بند کہتے ہیں۔',
 'الکاینونه نامشبوع هایدروکاربنونه دي چې کاربن–کاربن درې ګونی تړون لري. دوی د CₙH₂ₙ₋₂ عمومي فورمول په واسطه ښودل کېدای شي. د دې لړۍ لومړی او تر ټولو مهم غړی اسیتیلین (HC≡CH) دی او له همدې امله دوی عموماً اسیتیلینونه بلل کېږي. نو کاربن–کاربن درې ګونی تړون اسیتیلیني تړون بلل کېږي.')
add('16.7.1 Nomenclature','16.7.1 نام گذاری','16.7.1 نومول','heading')
add('There are two systems for naming alkynes i.e. common and IUPAC systems.','الکائنز کے نام رکھنے کے دو نظام ہیں، یعنی عام اور IUPAC نظام۔','د الکاینونو د نومولو دوه سیستمونه دي، یعنې عام او IUPAC سیستم.')
add('(a) Common System','(a) عام نظام','(a) عام سیستم','heading')
add('The first member of the alkyne series is named as acetylene. The higher alkynes are regarded as the alkyl derivatives of acetylene. For example;',
 'الکائن سلسلے کے پہلے رکن کا نام ایسیٹیلین ہے۔ بڑے الکائنز کو ایسیٹیلین کے الکائل مشتقات سمجھا جاتا ہے۔ مثلاً؛',
 'د الکاین لړۍ لومړی غړی اسیتیلین نومول شوی. لوړ الکاینونه د اسیتیلین الکایلي مشتقات ګڼل کېږي. د بېلګې په توګه؛')
visual('chem12-p69-common-alkynes',common)
add('(b) IUPAC System','(b) IUPAC نظام','(b) IUPAC سیستم','heading')
add('The IUPAC rules for naming akynes are the same as those for alkanes, except the following.','الکائنز کے نام رکھنے کے IUPAC اصول وہی ہیں جو الکینز (اکیلے بند والے) کے لیے ہیں، سوائے درج ذیل کے۔','د الکاینونو د نومولو IUPAC قواعد د الکانونو له قواعدو سره یو شان دي، پرته له لاندې ټکو.')
for n,e,u,p in [('i','The longest continuous carbon chain must include maximum number of triple bonds.','سب سے لمبی مسلسل کاربن زنجیر میں تہرے بندوں کی زیادہ سے زیادہ تعداد شامل ہونی چاہیے۔','تر ټولو اوږد پرله پسې کاربني ځنځیر باید د درې ګونو تړونونو اعظمي شمېر ولري.'),
 ('ii','The name given to the longest chain acts as parent name, whereby the ending “–ane” of the corresponding alkane is replaced by suffix “–yne”.','سب سے لمبی زنجیر کو دیا گیا نام بنیادی نام کا کام کرتا ہے، جس میں متعلقہ الکین (اکیلے بند والے) کا اختتامیہ ”–ane“ لاحقے ”–yne“ سے بدل دیا جاتا ہے۔','تر ټولو اوږد ځنځیر ته ورکړل شوی نوم د اصلي نوم دنده ترسره کوي، چې پکې د اړوند الکان پای ”–ane“ په ”–yne“ وروستاړي بدلېږي.'),
 ('iii','Number the chain in such a way that triply bonded carbon atom gets (–C≡C–) the smallest number.','زنجیر کو اس طرح نمبر دیں کہ تہرے بند والے کاربن ایٹم (–C≡C–) کو سب سے چھوٹا نمبر ملے۔','ځنځیر داسې شمېره کړئ چې درې ګوني تړون لرونکی کاربني اټوم (–C≡C–) تر ټولو کوچنۍ شمېره ترلاسه کړي.'),
 ('iv','The position of the triple bond is indicated by the number of that triply bonded carbon atom which bears lower number and this number is written before “–yne”.','تہرے بند کا مقام اس تہرے بند والے کاربن ایٹم کے نمبر سے ظاہر کیا جاتا ہے جس کا نمبر کم ہو، اور یہ نمبر ”–yne“ سے پہلے لکھا جاتا ہے۔','د درې ګوني تړون موقعیت د هغه درې ګوني تړلي کاربني اټوم په شمېرې ښودل کېږي چې ټیټه شمېره لري، او دا شمېره له ”–yne“ مخکې لیکل کېږي.'),
 ('v','For more than one triple bonds in the molecule, the prefix di, tri, tetra etc are used before “–yne”.','سالمے میں ایک سے زیادہ تہرے بندوں کے لیے ”–yne“ سے پہلے سابقے di، tri، tetra وغیرہ استعمال ہوتے ہیں۔','په مالیکول کې د یوه نه زیاتو درې ګونو تړونونو لپاره له ”–yne“ مخکې di، tri، tetra او نور مختاړي کارول کېږي.'),
 ('vi','Name substituent groups as in alkanes, indicating their locations by the number of the main-chain carbon to which they are attached.','متبادل گروپوں کے نام الکینز (اکیلے بند والے) کی طرح رکھیں، اور ان کا مقام مرکزی زنجیر کے اس کاربن کے نمبر سے بتائیں جس سے وہ جڑے ہیں۔','بدیل ګروپونه د الکانونو په څېر ونوموئ، او موقعیت یې د اصلي ځنځیر د هغه کاربن په شمېرې وښیئ چې ورسره تړلي دي.')]:
 add(n+'. '+e,n+'. '+u,n+'. '+p)
add('The following examples will illustrate the above rules.','درج ذیل مثالیں اوپر دیے گئے اصولوں کی وضاحت کریں گی۔','لاندې بېلګې به پورته قواعد روښانه کړي.')
visual('chem12-p69-iupac-alkynes',examples)
add('Self-assessmnet','خود جانچ','ځان ارزونه','heading')
add('Draw the structures of the following alkynes: ○ 3,3,4–trimethylpent–1–yne ○ 3–methylhexa–1,4–diyne ○ 4–ethyl–3,5–dimethylhex–1–yne',
 'درج ذیل الکائنز کی ساختیں بنائیں: ○ 3،3،4–ٹرائی میتھائل پینٹ–1–ائن ○ 3–میتھائل ہیکسا–1،4–ڈائی ائن ○ 4–ایتھائل–3،5–ڈائی میتھائل ہیکس–1–ائن',
 'د لاندې الکاینونو جوړښتونه رسم کړئ: ○ 3،3،4–ټرای میتایل پېنټ–1–این ○ 3–میتایل هېکسا–1،4–ډای این ○ 4–ایتیل–3،5–ډای میتایل هېکس–1–این')
add('16.7.2 Structure','16.7.2 ساخت','16.7.2 جوړښت','heading')
add('To illustrate the structure of alkynes, we would consider the structure of acetylene as an example. In acetylene each carbon atom has two sp-hybrid orbitals which lie on the same line. Each carbon atom also has two unhybridized p orbitals, which are perpendicular to each other and to the plane of sp-hybrid orbitals. One sp-hybrid orbital of one carbon atom linearly overlaps with the sp-hybrid orbital of the other carbon atom to form sigma bond between the two carbon atoms. The other sp-hybrid orbital of both the carbon atoms overlap with 1s orbitals of the two hydrogen atom to form two C–H sigma bonds. The two unhybridized p orbitals of both the carbon atoms approach each other in a sidewise manner to form two pi bonds. (Figure 16.9)',
 'الکائنز کی ساخت واضح کرنے کے لیے ہم مثال کے طور پر ایسیٹیلین کی ساخت پر غور کریں گے۔ ایسیٹیلین میں ہر کاربن ایٹم کے دو sp-ہائبرڈ آربیٹل ہوتے ہیں جو ایک ہی خط پر ہوتے ہیں۔ ہر کاربن ایٹم کے دو غیر ہائبرڈ p آربیٹل بھی ہوتے ہیں، جو ایک دوسرے پر اور sp-ہائبرڈ آربیٹلوں کے مستوی پر عمود ہوتے ہیں۔ ایک کاربن ایٹم کا ایک sp-ہائبرڈ آربیٹل دوسرے کاربن ایٹم کے sp-ہائبرڈ آربیٹل سے سیدھا تداخل کر کے دونوں کاربن ایٹموں کے درمیان سگما بند بناتا ہے۔ دونوں کاربن ایٹموں کا دوسرا sp-ہائبرڈ آربیٹل دو ہائیڈروجن ایٹموں کے 1s آربیٹلوں سے تداخل کر کے دو C–H سگما بند بناتا ہے۔ دونوں کاربن ایٹموں کے دو غیر ہائبرڈ p آربیٹل پہلو کے رخ ایک دوسرے کے قریب آ کر دو پائی بند بناتے ہیں۔ (شکل 16.9)',
 'د الکاینونو د جوړښت د روښانه کولو لپاره به موږ د بېلګې په توګه د اسیتیلین جوړښت وڅېړو. په اسیتیلین کې هر کاربني اټوم دوه sp-هایبرېډ اوربیټالونه لري چې پر یوه کرښه پراته دي. هر کاربني اټوم دوه نا هایبرېډ شوي p اوربیټالونه هم لري، چې پر یو بل او د sp-هایبرېډ اوربیټالونو پر سطحه عمود دي. د یوه کاربني اټوم یو sp-هایبرېډ اوربیټال د بل کاربني اټوم له sp-هایبرېډ اوربیټال سره مستقیم تداخل کوي او د دوو کاربني اټومونو ترمنځ سیګما تړون جوړوي. د دواړو کاربني اټومونو بل sp-هایبرېډ اوربیټال د دوو هایدروجني اټومونو له 1s اوربیټالونو سره تداخل کوي او دوه C–H سیګما تړونونه جوړوي. د دواړو کاربني اټومونو دوه نا هایبرېډ شوي p اوربیټالونه له څنګه یو بل ته نږدې کېږي او دوه پای تړونونه جوړوي. (شکل 16.9)')

record=section('16.16','Polarimetry, alkynes nomenclature and structure','پولری میٹری، الکائنز کی نام گذاری اور ساخت','پولاریمېټري، د الکاینونو نومول او جوړښت',paras,layout,blocks,'130–131')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':69,'printedPages':[130,131]}]
record['sourceContinuesOnPdfPage']=70
issues=[{'id':'chem12-p130-printed-spellings','printedPage':130,'description':'Printed "dextrorotaory", "akynes" and "Self-assessmnet" retained in English as in the source.'}]
carry=[{'from':'16.16','to':'16.17','startsAt':'Figure 16.9 Orbital hybridization model of acetylene.'}]
if __name__=='__main__':save(69,[record],carry=carry,issues=issues,chapter_number=16)
