"""PDF73 printed138–139: alkyne hydration, bromination, ozonolysis; benzene and monosubstituted benzene nomenclature."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
import math
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b'):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x:.1f} {y:.1f}L{a:.1f} {b:.1f}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow73" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#222"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
def arrow(x1,x2,y,a='',b=''):return line(x1,y,x2,y,2,'#222','marker-end="url(#arrow73)"')+(t((x1+x2)/2,y-9,a,13) if a else '')+(t((x1+x2)/2,y+19,b,13) if b else '')
def eq(x1,x2,y):return line(x1,y-3,x2,y-3,2,'#222','marker-end="url(#arrow73)"')+line(x2,y+3,x1,y+3,2,'#222','marker-end="url(#arrow73)"')
def ring(cx,cy,r=30,circle=False,subs=None,kek=True):
 """Hexagon with vertex 0 at top; subs={vertex:'label'}"""
 pts=[(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
 s='<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'
 if circle:s+=f'<circle cx="{cx}" cy="{cy}" r="{r*.6:.1f}" fill="none" stroke="#222" stroke-width="2"/>'
 elif kek:
  for i in (0,2,4):
   (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.78
   s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 for i,lab in (subs or {}).items():
  x,y=pts[i];dx,dy=(x-cx)/r,(y-cy)/r
  s+=line(x,y,x+dx*16,y+dy*16)+t(x+dx*30,y+dy*30+6,lab,16)
 return s
L={'ethyne':('ایتھائن','ایتاین'),'vinyl alcohol':('وائنائل الکوحل','وینایل الکول'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'propyne':('پروپائن','پروپاین'),
   'propen-2-ol':('پروپین-2-اول','پروپین-2-ول'),'acetone':('ایسیٹون','اسیتون'),'1,2-dibromoethene':('1،2-ڈائی برومو ایتھین (دوہرا بند)','1،2-ډای بروموایتین'),
   '1,1,2,2-tetrabromoethane':('1،1،2،2-ٹیٹرا برومو ایتھین','1،1،2،2-ټیټرا بروموایتان'),'Alkyne':('الکائن','الکاین'),'Ozonide':('اوزونائیڈ','اوزونایډ'),
   '1,2-dicarbonyl':('1،2-ڈائی کاربونل','1،2-ډای کاربونیل'),'compound':('مرکب','مرکب'),'1,2-dicarbonyl compound':('1،2-ڈائی کاربونل مرکب','1،2-ډای کاربونیل مرکب'),
   'Carboxylic acids':('کاربوکسیلک ایسڈز','کاربوکسیلیک اسیدونه'),'OR':('یا','یا'),'bromobenzene':('برومو بینزین','بروموبنزین'),'chlorobenzene':('کلورو بینزین','کلوروبنزین'),
   'nitrobenzene':('نائٹرو بینزین','نایټروبنزین'),'toluene':('ٹولوئین','تولوین'),'(methylbenzene)':('(میتھائل بینزین)','(میتایل بنزین)'),'phenol':('فینول','فینول'),
   '(benzenol)':('(بینزینول)','(بنزینول)'),'aniline':('اینیلین','انیلین'),'(benzenamine)':('(بینزین امین)','(بنزین امین)')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]

def hydration(lang):
 s=start(210)
 s+=t(110,80,'H—C≡C—H + H—OH',19)+t(145,58,'δ+',11)+t(170,58,'δ−',11)+t(60,104,lb(lang,'ethyne'),13)+arrow(215,325,74,'H₂SO₄, HgSO₄','100°C')
 s+=t(400,40,'OH',16)+line(418,46,418,62)+t(400,80,'CH₂ = CH',19)+t(400,104,lb(lang,'vinyl alcohol'),13)+eq(470,540,74)
 s+=t(680,40,'O',16)+line(680,46,680,62)+line(686,46,686,62)+t(660,80,'CH₃ — C — H',19)+t(680,104,lb(lang,'acetaldehyde'),13)
 s+=t(115,175,'H—C≡C—CH₃ + H—OH',19)+t(174,153,'δ+',11)+t(199,153,'δ−',11)+t(60,199,lb(lang,'propyne'),13)+arrow(225,330,169,'H₂SO₄, HgSO₄','100°C')
 s+=t(420,135,'OH',16)+line(420,141,420,157)+t(410,175,'CH₂ = C — CH₃',19)+t(410,199,lb(lang,'propen-2-ol'),13)+eq(500,560,169)
 s+=t(690,135,'O',16)+line(687,141,687,157)+line(693,141,693,157)+t(690,175,'CH₃ — C — CH₃',19)+t(690,199,lb(lang,'acetone'),13)
 return s+'</svg>'
def brom(lang):
 s=start(262)
 s+=t(150,66,'H—C≡C—H + Br—Br',19)+t(80,104,lb(lang,'ethyne'),13)+arrow(290,400,60,'CCl₄')
 s+=t(540,26,'Br',16)+line(540,32,540,48)+t(520,66,'HC = CH',19)+line(500,74,500,90)+t(500,108,'Br',16)+t(520,128,lb(lang,'1,2-dibromoethene'),13)
 s+=t(85,155,'Br',16)+line(85,161,85,177)+t(140,195,'HC = CH  + Br—Br',19)+line(110,203,110,219)+t(110,237,'Br',16)+t(110,256,lb(lang,'1,2-dibromoethene'),12)
 s+=arrow(290,400,189,'CCl₄')+t(510,155,'Br   Br',16)+line(497,161,497,177)+line(530,161,530,177)+t(515,195,'HC — CH',19)+line(497,203,497,219)+line(530,203,530,219)+t(515,237,'Br   Br',16)+t(680,195,lb(lang,'1,1,2,2-tetrabromoethane'),13)
 return s+'</svg>'
def ozon(lang):
 s=start(240)
 s+=t(110,80,"R—C≡C—R′ + O₃",19)+t(80,104,lb(lang,'Alkyne'),13)+arrow(205,265,74)
 s+=t(345,40,'O—O',16)+line(330,46,330,62)+line(360,46,360,62)+t(345,80,"R—C—C—R′",19)+line(330,88,345,104)+line(360,88,345,104)+t(345,120,'O',16)+t(345,140,lb(lang,'Ozonide'),13)
 s+=arrow(430,520,74,'H₂O','−H₂O₂')+t(640,40,'O    O',16)+line(625,46,625,62)+line(655,46,655,62)+t(640,80,"R—C—C—R′",19)+t(640,104,lb(lang,'1,2-dicarbonyl'),13)+t(640,120,lb(lang,'compound'),13)
 s+=t(130,175,'O    O',16)+line(115,181,115,197)+line(145,181,145,197)+t(130,215,"R—C—C—R′",19)+t(130,239,lb(lang,'1,2-dicarbonyl compound'),13)+arrow(260,360,209,'H₂O₂')
 s+=t(455,175,'O',16)+line(455,181,455,197)+t(470,215,'R—C—OH  +',19)+t(625,175,'O',16)+line(625,181,625,197)+t(640,215,"R′—C—OH",19)+t(550,239,lb(lang,'Carboxylic acids'),13)
 return s+'</svg>'
def benzene(lang):
 s=start(170)
 pts=[(200+48*math.sin(math.radians(60*i)),85-48*math.cos(math.radians(60*i))) for i in range(6)]
 s+=ring(200,85,48)
 for x,y in pts:
  dx,dy=(x-200)/48,(y-85)/48;s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="white"/>'+t(x,y+6,'C',15)+line(x+dx*10,y+dy*10,x+dx*24,y+dy*24)+t(x+dx*34,y+dy*34+6,'H',15)
 s+=t(330,92,lb(lang,'OR'),17)+ring(450,85,42)+t(570,92,lb(lang,'OR'),17)+ring(690,85,42,circle=True)
 return s+'</svg>'
def mono(lang,kind):
 s=start(150)
 items={'basic':[({0:'Br'},'bromobenzene',None),({0:'Cl'},'chlorobenzene',None),({0:'NO₂'},'nitrobenzene',None)],
        'special':[({0:'CH₃'},'toluene','(methylbenzene)'),({0:'OH'},'phenol','(benzenol)'),({0:'NH₂'},'aniline','(benzenamine)')]}[kind]
 for x,(sub,n,m) in zip((180,425,670),items):
  s+=ring(x,80,32,subs=sub)+t(x,132,lb(lang,n),14)+(t(x,148,lb(lang,m),13) if m else '')
 return s+'</svg>'

add('16.7.8.4 Hydration','16.7.8.4 ہائیڈریشن','16.7.8.4 هایدرېشن','heading')
add('Alkynes undergo acid-catalyzed addition of water across the triple bond in the presence of mercuric ion as a catalyst. A mixture of mercuric sulfate in aqueous sulfuric acid is commonly used as the reagent. The hydration of alkynes is similar to the hydration of alkenes, and it also goes with Markovnikov orientation. The enol formed on tautomerization give corresponding aldehyde or ketone. The product is an aldehydes in case of acetylene, and ketone in case of higher alkynes.',
 'الکائنز مرکیورک آئن کی بطور عمل انگیز موجودگی میں تہرے بند پر پانی کا تیزاب سے عمل انگیز اضافہ کرتے ہیں۔ عام طور پر آبی سلفیورک ایسڈ میں مرکیورک سلفیٹ کا آمیزہ بطور عامل استعمال ہوتا ہے۔ الکائنز کی ہائیڈریشن الکینز کی ہائیڈریشن جیسی ہے اور یہ بھی مارکونیکوف سمت پر ہوتی ہے۔ بننے والا اینول ٹاٹومرائزیشن سے متعلقہ الڈیہائیڈ یا کیٹون دیتا ہے۔ ایسیٹیلین کی صورت میں پیداوار الڈیہائیڈ اور بڑے الکائنز کی صورت میں کیٹون ہوتی ہے۔',
 'الکاینونه د کتلست په توګه د مرکیوریک ایون په شتون کې پر درې ګوني تړون د اوبو اسیدي کتلستي اضافه کوي. عموماً په اوبلن سلفوریک اسید کې د مرکیوریک سلفېټ ګډوله د عامل په توګه کارېږي. د الکاینونو هایدرېشن د الکینونو هایدرېشن ته ورته دی او دا هم د مارکوفنیکوف لوري سره سم کېږي. جوړ شوی اینول په ټاټومېرېزېشن سره اړوند الدیهاید یا کیټون ورکوي. د اسیتیلین په حالت کې محصول الدیهاید او د لوړو الکاینونو په حالت کې کیټون دی.')
visual('chem12-p73-alkyne-hydration',hydration)
add('16.7.8.5 Halogenation (Bromination)','16.7.8.5 ہیلوجینیشن (برومینیشن)','16.7.8.5 هالوجینېشن (برومینېشن)','heading')
add('Bromine adds to alkynes in two steps, initially forming dibromoalkene (mainly trans) and then a tetra bromide (tetrabromoalkanes).',
 'برومین الکائنز میں دو مرحلوں میں شامل ہوتی ہے، پہلے ڈائی برومو الکین (زیادہ تر trans) اور پھر ٹیٹرا برومائیڈ (ٹیٹرا برومو الکینز) بنتا ہے۔',
 'برومین الکاینونو ته په دوو پړاوونو کې ورزیاتېږي، لومړی ډای بروموالکین (ډېری trans) او بیا ټیټرا برومایډ (ټیټرا بروموالکانونه) جوړوي.')
visual('chem12-p73-alkyne-bromination',brom)
add('Chlorine also react in similar way.','کلورین بھی اسی طرح تعامل کرتی ہے۔','کلورین هم په ورته ډول تعامل کوي.')
add('16.7.8.6 Ozonolysis','16.7.8.6 اوزونولائسز','16.7.8.6 اوزونولایسس','heading')
add('Alkynes react with ozone to form ozonides. The ozonides may be decomposed with water to give a 1,2-dicarbonyl compound, which is finally oxidized to an acid by hydrogen peroxide produced in the reaction, resulting in formation of carboxylic acids.',
 'الکائنز اوزون سے تعامل کر کے اوزونائیڈز بناتے ہیں۔ اوزونائیڈز کو پانی سے تحلیل کر کے 1،2-ڈائی کاربونل مرکب حاصل کیا جا سکتا ہے، جو آخرکار تعامل میں بننے والے ہائیڈروجن پرآکسائیڈ سے تیزاب میں تکسید ہو جاتا ہے، اور نتیجتاً کاربوکسیلک ایسڈز بنتے ہیں۔',
 'الکاینونه له اوزون سره تعامل کوي او اوزونایډونه جوړوي. اوزونایډونه له اوبو سره تجزیه کېدای شي او 1،2-ډای کاربونیل مرکب ورکوي، چې په پای کې په تعامل کې د جوړ شوي هایدروجن پېرکساید په واسطه په اسید اکسیډایز کېږي او په پایله کې کاربوکسیلیک اسیدونه جوړېږي.')
visual('chem12-p73-alkyne-ozonolysis',ozon)
add('16.8 Benzene and Substituted Benzenes','16.8 بینزین اور متبادل بینزینز','16.8 بنزین او بدیل لرونکي بنزینونه','heading')
add('Benzene is an aromatic hydrocarbon. Its molecular formula is C₆H₆. The following ring structure is usually written for benzene, where each corner represents a carbon atom. It is understood that one hydrogen atom is bonded to each carbon atom.',
 'بینزین ایک ارومیٹک ہائیڈروکاربن ہے۔ اس کا سالماتی فارمولا C₆H₆ ہے۔ بینزین کے لیے عموماً درج ذیل حلقہ ساخت لکھی جاتی ہے، جس کا ہر کونا ایک کاربن ایٹم کو ظاہر کرتا ہے۔ یہ سمجھا جاتا ہے کہ ہر کاربن ایٹم سے ایک ہائیڈروجن ایٹم جڑا ہے۔',
 'بنزین یو اروماتیک هایدروکاربن دی. مالیکولي فورمول یې C₆H₆ دی. د بنزین لپاره عموماً لاندې کړیز جوړښت لیکل کېږي، چې هر کونج یې یو کاربني اټوم ښيي. داسې ګڼل کېږي چې له هر کاربني اټوم سره یو هایدروجني اټوم تړلی دی.')
visual('chem12-p73-benzene-structures',benzene)
add('Monosubstituted and polysubstituted benzene derivatives are formed by the replacement of one or more hydrogen atoms respectively.',
 'ایک یا زیادہ ہائیڈروجن ایٹموں کی تبدیلی سے بالترتیب یک متبادل اور کثیر متبادل بینزین مشتقات بنتے ہیں۔',
 'د یوه یا ډېرو هایدروجني اټومونو د بدلون په واسطه په ترتیب سره یو بدیلي او څو بدیلي بنزیني مشتقات جوړېږي.')
add('16.8.1 Nomenclature','16.8.1 نام گذاری','16.8.1 نومول','heading')
add('Benzene and its substituted compounds are named by common names which are also accepted by the IUPAC System.','بینزین اور اس کے متبادل مرکبات کے نام عام ناموں سے رکھے جاتے ہیں جو IUPAC نظام میں بھی قبول ہیں۔','بنزین او د هغه بدیل لرونکي مرکبات په عامو نومونو نومول کېږي چې د IUPAC سیستم له خوا هم منل شوي دي.')
add('i. Monosubstituted benzene derivatives are named by putting the name of the substituent before the word benzene. For example;',
 'i. یک متبادل بینزین مشتقات کا نام لفظ بینزین سے پہلے متبادل کا نام لگا کر رکھا جاتا ہے۔ مثلاً؛',
 'i. یو بدیلي بنزیني مشتقات د بنزین له کلمې مخکې د بدیل نوم په ایښودلو نومول کېږي. د بېلګې په توګه؛')
visual('chem12-p73-mono-basic',lambda l:mono(l,'basic'))
add('Some Monosubstituted benzene derivatives have been given “Special names”. They must be remembered as such. Some of the examples are given below. Their systematic names are also given in parenthesis.',
 'بعض یک متبادل بینزین مشتقات کو ”خاص نام“ دیے گئے ہیں۔ انہیں اسی طرح یاد رکھنا چاہیے۔ چند مثالیں درج ذیل ہیں۔ ان کے نظامی نام بھی قوسین میں دیے گئے ہیں۔',
 'ځینو یو بدیلي بنزیني مشتقاتو ته ”ځانګړي نومونه“ ورکړل شوي. دا باید همداسې یاد وساتل شي. ځینې بېلګې لاندې ورکړل شوې. سیستماتیک نومونه یې هم په قوسونو کې ورکړل شوي.')
visual('chem12-p73-mono-special',lambda l:mono(l,'special'))

record=section('16.20','Alkyne hydration, bromination and ozonolysis; benzene nomenclature','الکائنز کی ہائیڈریشن، برومینیشن اور اوزونولائسز؛ بینزین کی نام گذاری','د الکاینونو هایدرېشن، برومینېشن او اوزونولایسس؛ د بنزین نومول',paras,layout,blocks,'138–139')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':73,'printedPages':[138,139]}]
record['sourceContinuesOnPdfPage']=74
issues=[{'id':'chem12-p139-benzaldehyde-continues','printedPage':139,'description':'Special-name examples continue on printed 140 (benzaldehyde, benzoic acid); kept with the next record.'}]
carry=[{'from':'16.20','to':'16.21','startsAt':'CHO\nCOOH'}]
if __name__=='__main__':save(73,[record],carry=carry,issues=issues,chapter_number=16)
