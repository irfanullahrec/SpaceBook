"""PDF72 printed136–137: pKa table, metal acetylides, alkyne hydrogenation, dissolving-metal reduction, hydrohalogenation."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b'):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x} {y}L{a} {b}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow72" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#222"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
def arrow(x1,x2,y,a='',b=''):return line(x1,y,x2,y,2,'#222','marker-end="url(#arrow72)"')+(t((x1+x2)/2,y-9,a,13) if a else '')+(t((x1+x2)/2,y+19,b,13) if b else '')
L={'acetylene':('ایسیٹیلین','اسیتیلین'),'acetylane':('ایسیٹیلین','اسیتیلین'),'dicopper acetylide':('ڈائی کاپر ایسیٹیلائیڈ','ډای کاپر اسیتیلاید'),'(red ppt)':('(سرخ رسوب)','(سور رسوب)'),
   'disilver acetylide':('ڈائی سلور ایسیٹیلائیڈ','ډای سلور اسیتیلاید'),'(white ppt)':('(سفید رسوب)','(سپین رسوب)'),'ethyne':('ایتھائن','ایتاین'),'ethene':('ایتھین (دوہرا بند)','ایتین'),
   'ethane':('ایتھین (اکیلا بند)','ایتان'),'Non-terminal':('غیر ٹرمینل','غیر ټرمینل'),'alkyne':('الکائن','الکاین'),'trans-alkene':('ٹرانس-الکین','ټرانس-الکین'),
   'vinyl bromide':('وائنائل برومائیڈ','وینایل برومایډ'),'(bromoethene)':('(برومو ایتھین)','(بروموایتین)'),"(Markovnikov's rule)":('(مارکونیکوف کا اصول)','(د مارکوفنیکوف قاعده)'),
   '1,1-dibromoethane':('1،1-ڈائی برومو ایتھین','1،1-ډای بروموایتان'),'(a gem-dibromide)':('(ایک جیم-ڈائی برومائیڈ)','(یو جېم-ډای برومایډ)'),'propyne':('پروپائن','پروپاین'),
   '2-bromopropene':('2-برومو پروپین','2-بروموپروپین'),'2,2-dibromopropane':('2،2-ڈائی برومو پروپین','2،2-ډای بروموپروپان')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]

def metal(lang):
 s=start(165)
 s+=t(160,40,'CH ≡ CH + Cu₂Cl₂ + 2NH₄OH',19)+t(70,62,lb(lang,'acetylene'),13)+arrow(330,410,34)+t(615,40,'Cu⁺C⁻≡C⁻Cu⁺ + 2NH₄Cl + 2H₂O',19)+t(520,62,lb(lang,'dicopper acetylide'),13)+t(520,78,lb(lang,'(red ppt)'),13)
 s+=t(160,115,'HC ≡ CH + 2AgNO₃ + 2NH₄OH',19)+t(70,137,lb(lang,'acetylane'),13)+arrow(330,410,109)+t(615,115,'Ag⁺C⁻≡C⁻Ag⁺ + 2NH₄NO₃ + 2H₂O',19)+t(520,137,lb(lang,'disilver acetylide'),13)+t(520,155,lb(lang,'(white ppt)'),13)
 return s+'</svg>'
def hydrogenation(lang):
 s=start(150)
 s+=t(170,40,'HC ≡ CH  +  H₂',20)+t(110,62,lb(lang,'ethyne'),13)+arrow(300,430,34,'Ni / 230-250°C','or Pt or Pd/25°C')+t(560,40,'CH₂ = CH₂',20)+t(560,62,lb(lang,'ethene'),13)
 s+=t(170,115,'CH₂ = CH₂  +  H₂',20)+t(110,137,lb(lang,'ethene'),13)+arrow(300,430,109,'Ni / 230-250°C','or Pt or Pd/25°C')+t(560,115,'CH₃ — CH₃',20)+t(560,137,lb(lang,'ethane'),13)
 return s+'</svg>'
def dissolving(lang):
 s=start(130)+t(150,60,'R — C ≡ C — R  +  2Na',20)+t(90,86,lb(lang,'Non-terminal'),13)+t(90,102,lb(lang,'alkyne'),13)+arrow(300,400,54,'liq. NH₃','−33°C')
 s+=t(500,26,'R',17)+t(600,26,'H',17)+line(508,32,530,50)+line(592,32,570,50)+t(550,62,'C = C',20)+line(530,70,508,88)+line(570,70,592,88)+t(500,104,'H',17)+t(600,104,'R',17)
 s+=t(720,62,'+ 2NaNH₂',20)+t(550,124,lb(lang,'trans-alkene'),13)
 return s+'</svg>'
def hx(lang,kind):
 s=start(270)
 mk=lb(lang,"(Markovnikov's rule)")
 if kind=='sym':
  s+=t(150,70,'H — C ≡ C — H  +  H — Br',20)+t(220,48,'δ+',12)+t(255,48,'δ−',12)+t(90,94,lb(lang,'ethyne'),13)+arrow(320,450,64)
  s+=t(600,30,'Br',17)+line(600,36,600,52)+t(580,70,'CH₂ = CH',20)+t(580,94,lb(lang,'vinyl bromide'),13)+t(580,110,lb(lang,'(bromoethene)'),13)
  s+=t(126,165,'Br',17)+line(126,171,126,187)+t(120,205,'CH₂ = CH   +  H — Br',20)+t(153,183,'δ+',12)+t(194,183,'δ−',12)+t(90,229,lb(lang,'vinyl bromide'),13)+t(90,245,lb(lang,'(bromoethene)'),13)
  s+=arrow(320,520,199,mk)+t(640,165,'Br',17)+line(640,171,640,187)+t(615,205,'CH₃ — CH',20)+line(640,212,640,228)+t(640,246,'Br',17)+t(740,229,lb(lang,'1,1-dibromoethane'),13)+t(740,245,lb(lang,'(a gem-dibromide)'),13)
 else:
  s+=t(160,70,'H — C ≡ C — CH₃  +  H — Br',20)+t(240,48,'δ+',12)+t(273,48,'δ−',12)+t(90,94,lb(lang,'propyne'),13)+arrow(340,520,64,mk)
  s+=t(640,30,'Br',17)+line(640,36,640,52)+t(640,70,'CH₂ = C — CH₃',20)+t(640,94,lb(lang,'2-bromopropene'),13)
  s+=t(130,165,'Br',17)+line(130,171,130,187)+t(160,205,'CH₂ = C — CH₃  +  H — Br',20)+t(243,183,'δ+',12)+t(282,183,'δ−',12)+t(110,229,lb(lang,'2-bromopropene'),13)
  s+=arrow(340,520,199,mk)+t(655,165,'Br',17)+line(655,171,655,187)+t(655,205,'CH₃ — C — CH₃',20)+line(655,212,655,228)+t(655,246,'Br',17)+t(780,229,lb(lang,'2,2-dibromopropane'),13)
 return s+'</svg>'

tb={'id':'chem12-table16-5','headers':['Compounds','Hybridization','s Character (%)','pKa'],
 'rows':[['ethane','sp³','25','50'],['ethene','sp²','33.33','44'],['ethyne','sp','50','25']],
 'translations':[{'language':'اردو','headers':['مرکبات','ہائبرڈائزیشن','s کردار (%)','pKa'],'rows':[['ایتھین (اکیلا بند)','sp³','25','50'],['ایتھین (دوہرا بند)','sp²','33.33','44'],['ایتھائن','sp','50','25']]},
                 {'language':'پښتو','headers':['مرکبات','هایبرېډیزېشن','s ځانګړنه (%)','pKa'],'rows':[['ایتان','sp³','25','50'],['ایتین','sp²','33.33','44'],['ایتاین','sp','50','25']]}]}
add('Table 16.5 pKa values of Ethane, Ethene and Ethyne','جدول 16.5 ایتھین، ایتھین (دوہرا بند) اور ایتھائن کی pKa اقدار','جدول 16.5 د ایتان، ایتین او ایتاین pKa ارزښتونه')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('Because of acidic nature, acetylene and 1-alkynes react with ammonical solutions of cuprous chloride and silver nitrate to form acetylides and alkynides of these metals.',
 'تیزابی نوعیت کی وجہ سے ایسیٹیلین اور 1-الکائنز کیوپرس کلورائیڈ اور سلور نائٹریٹ کے امونیائی محلولوں سے تعامل کر کے ان دھاتوں کے ایسیٹیلائیڈز اور الکائنائیڈز بناتے ہیں۔',
 'د تېزابي طبیعت له امله اسیتیلین او 1-الکاینونه د کیوپرس کلوراید او سلور نایټرېټ له امونیایي محلولونو سره تعامل کوي او د دې فلزونو اسیتیلایډونه او الکاینایډونه جوړوي.')
visual('chem12-p72-metal-acetylides',metal)
add('Copper and silver acetylides are highly explosive in dry condition. They can, however, be decomposed by acids such as nitric acid to regenerate acetylene. Since non–terminal alkynes do not form alkynides, this reaction can be used as a test to distinguish terminal alkynes from non-terminal alkynes.',
 'کاپر اور سلور ایسیٹیلائیڈز خشک حالت میں بہت دھماکہ خیز ہوتے ہیں۔ تاہم انہیں نائٹرک ایسڈ جیسے تیزابوں سے تحلیل کر کے دوبارہ ایسیٹیلین حاصل کی جا سکتی ہے۔ چونکہ غیر ٹرمینل الکائنز الکائنائیڈز نہیں بناتے، اس لیے یہ تعامل ٹرمینل الکائنز کو غیر ٹرمینل الکائنز سے ممتاز کرنے کے ٹیسٹ کے طور پر استعمال ہو سکتا ہے۔',
 'د مسو او سپینو زرو اسیتیلایډونه په وچ حالت کې ډېر چاودېدونکي دي. خو د نایټریک اسید په څېر اسیدونو په واسطه تجزیه کېدای شي او بېرته اسیتیلین ترلاسه کېږي. څرنګه چې غیر ټرمینل الکاینونه الکاینایډونه نه جوړوي، دا تعامل د ټرمینل او غیر ټرمینل الکاینونو د توپیر لپاره د ازموینې په توګه کارېدای شي.')
add('16.7.8 Addition Reactions of Alkynes','16.7.8 الکائنز کے اضافی تعاملات','16.7.8 د الکاینونو اضافي تعاملونه','heading')
add('16.7.8.1 Hydrogenation','16.7.8.1 ہائیڈروجینیشن','16.7.8.1 هایدروجینېشن','heading')
add('The conditions for hydrogenation of alkynes are similar to those employed for alkenes. In the presence of finely divided platinum, palladium or nickel, two molecules of hydrogen add to the triple bond of an alkyne to yield an alkane. Addition of two molecules of hydrogen to alkynes occurs in two steps, initially forming the corresponding alkenes and finally alkanes.',
 'الکائنز کی ہائیڈروجینیشن کی شرائط وہی ہیں جو الکینز (دوہرے بند والے) کے لیے استعمال ہوتی ہیں۔ باریک پسے ہوئے پلاٹینم، پیلیڈیم یا نکل کی موجودگی میں ہائیڈروجن کے دو سالمات الکائن کے تہرے بند میں شامل ہو کر الکین (اکیلے بند والا) بناتے ہیں۔ الکائنز میں ہائیڈروجن کے دو سالمات کا اضافہ دو مرحلوں میں ہوتا ہے، پہلے متعلقہ الکینز (دوہرے بند والے) اور آخر میں الکینز (اکیلے بند والے) بنتے ہیں۔',
 'د الکاینونو د هایدروجینېشن شرایط د الکینونو لپاره کارېدونکو شرایطو ته ورته دي. د باریک وېشل شوي پلاتین، پالادیم یا نکل په شتون کې، د هایدروجن دوه مالیکولونه د الکاین درې ګوني تړون ته ورزیاتېږي او الکان جوړوي. الکاینونو ته د هایدروجن د دوو مالیکولونو زیاتېدل په دوو پړاوونو کې کېږي، لومړی اړوند الکینونه او په پای کې الکانونه جوړېږي.')
visual('chem12-p72-alkyne-hydrogenation',hydrogenation)
add('With efficient catalysts such as platinum, palladium, or nickel, it is usually impossible to stop the reaction at the alkene stage. However, hydrogenation of an alkyne can be stopped at the alkene stage by using a “poisoned” (partially deactivated) catalyst made by treating a good catalyst with a compound that makes the catalyst less effective. Lindlar’s catalyst is a poisoned palladium catalyst; composed of powdered barium sulfate coated with palladium, poisoned with quinoline. In an internal alkyne, syn addition gives a cis-alkene product (if cis/trans-isomerism is possible in product alkene).',
 'پلاٹینم، پیلیڈیم یا نکل جیسے مؤثر عمل انگیزوں کے ساتھ تعامل کو الکین (دوہرے بند) کے مرحلے پر روکنا عموماً ناممکن ہوتا ہے۔ تاہم الکائن کی ہائیڈروجینیشن کو ”زہر آلود“ (جزوی طور پر غیر فعال) عمل انگیز کے ذریعے الکین کے مرحلے پر روکا جا سکتا ہے، جو کسی اچھے عمل انگیز کو ایسے مرکب سے عمل کرا کر بنایا جاتا ہے جو عمل انگیز کو کم مؤثر بنا دے۔ لنڈلار کا عمل انگیز ایک زہر آلود پیلیڈیم عمل انگیز ہے؛ جو پیلیڈیم چڑھے پسے ہوئے بیریم سلفیٹ پر مشتمل ہوتا ہے اور کوئنولین سے زہر آلود کیا جاتا ہے۔ اندرونی الکائن میں syn اضافہ cis-الکین پیداوار دیتا ہے (اگر پیداواری الکین میں cis/trans آئسومرزم ممکن ہو)۔',
 'د پلاتین، پالادیم یا نکل په څېر اغېزمنو کتلستونو سره تعامل د الکین پړاو کې درول عموماً ناشوني وي. خو د الکاین هایدروجینېشن د ”زهرجن“ (په نسبي ډول غیر فعال) کتلست په کارولو د الکین پړاو کې درول کېدای شي، چې د یوه ښه کتلست له داسې مرکب سره په تعامل جوړېږي چې کتلست لږ اغېزمن کړي. د لینډلار کتلست یو زهرجن پالادیم کتلست دی؛ چې له پالادیم پوښل شوي پوډر شوي باریم سلفېټ څخه جوړ او په کینولین زهرجن شوی دی. په داخلي الکاین کې syn اضافه cis-الکین محصول ورکوي (که په محصول الکین کې cis/trans ایزومېریزم ممکن وي).')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Syn addition is the addition of two substituents to the same side of a double or triple bond.','Syn اضافہ دوہرے یا تہرے بند کی ایک ہی جانب دو متبادلات کا اضافہ ہے۔','Syn اضافه د دوه ګوني یا درې ګوني تړون یوې خوا ته د دوو بدیلونو زیاتول دي.')
add('16.7.8.2 Reduction by Dissolving Metal','16.7.8.2 حل ہوتی دھات سے تخفیف','16.7.8.2 د حلېدونکي فلز په واسطه ارجاع','heading')
add('Terminal alkynes and acetylene, react with metals such as sodium in liquid ammonia to form salts called alkynides or acetylides (Section 16.7.7). However, reduction of non-terminal alkynes to trans-alkene (anti addition), can be carried by reduction of alkynes with sodium metal in liquid ammonia.',
 'ٹرمینل الکائنز اور ایسیٹیلین مائع امونیا میں سوڈیم جیسی دھاتوں سے تعامل کر کے نمکیات بناتے ہیں جنہیں الکائنائیڈز یا ایسیٹیلائیڈز کہتے ہیں (حصہ 16.7.7)۔ تاہم غیر ٹرمینل الکائنز کی trans-الکین تک تخفیف (anti اضافہ) مائع امونیا میں سوڈیم دھات سے الکائنز کی تخفیف کے ذریعے کی جا سکتی ہے۔',
 'ټرمینل الکاینونه او اسیتیلین په مایع امونیا کې له سوډیم په څېر فلزونو سره تعامل کوي او مالګې جوړوي چې الکاینایډونه یا اسیتیلایډونه بلل کېږي (برخه 16.7.7). خو د غیر ټرمینل الکاینونو ارجاع trans-الکین ته (anti اضافه) په مایع امونیا کې د سوډیم فلز په واسطه د الکاینونو د ارجاع له لارې ترسره کېدای شي.')
visual('chem12-p72-dissolving-metal',dissolving)
add('16.7.8.3 Hydrohalogenation','16.7.8.3 ہائیڈروہیلوجینیشن','16.7.8.3 هایدروهالوجینېشن','heading')
add('Two molecules of halogen acids are added to alkynes in two steps, to form geminal dihalides. In case of symmetric alkyne, the second step follows the Markovnikov’s rule. However, addition of halogen acids to asymmetric alkynes follows Markovnikov’s rule in both the steps.',
 'ہیلوجن تیزابوں کے دو سالمات دو مرحلوں میں الکائنز میں شامل ہو کر جیمینل ڈائی ہیلائیڈز بناتے ہیں۔ متناسب الکائن کی صورت میں دوسرا مرحلہ مارکونیکوف کے اصول پر چلتا ہے۔ تاہم غیر متناسب الکائنز میں ہیلوجن تیزابوں کا اضافہ دونوں مرحلوں میں مارکونیکوف کے اصول پر ہوتا ہے۔',
 'د هالوجني اسیدونو دوه مالیکولونه په دوو پړاوونو کې الکاینونو ته ورزیاتېږي او جېمینل ډای هالایډونه جوړوي. د متقارن الکاین په حالت کې دویم پړاو د مارکوفنیکوف قاعده تعقیبوي. خو نامتقارنو الکاینونو ته د هالوجني اسیدونو زیاتېدل په دواړو پړاوونو کې د مارکوفنیکوف قاعده تعقیبوي.')
add('For a symmetrical alkyne:','متناسب الکائن کے لیے:','د متقارن الکاین لپاره:')
visual('chem12-p72-hbr-ethyne',lambda l:hx(l,'sym'))
add('For an asymmetric alkyne;','غیر متناسب الکائن کے لیے؛','د نامتقارن الکاین لپاره؛')
visual('chem12-p72-hbr-propyne',lambda l:hx(l,'asym'))

record=section('16.19','Alkyne acidity, hydrogenation, reduction and hydrohalogenation','الکائنز کی تیزابیت، ہائیڈروجینیشن، تخفیف اور ہائیڈروہیلوجینیشن','د الکاینونو تېزابیت، هایدروجینېشن، ارجاع او هایدروهالوجینېشن',paras,layout,blocks,'136–137')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':72,'printedPages':[136,137]}]
record['sourceContinuesOnPdfPage']=73
issues=[{'id':'chem12-p136-pka-table-offset','printedPage':136,'description':'Table 16.5 s-character and pKa columns are printed half a row offset; paired row-by-row (ethane 25/50, ethene 33.33/44, ethyne 50/25).'},
        {'id':'chem12-p136-printed-spellings','printedPage':136,'description':'Printed "ammonical" and "acetylane" retained in English; hydrogenation temperature printed 230-250°C here vs 200–250°C for alkenes (printed 120) — both retained.'}]
carry=[{'from':'16.19','to':'16.20','startsAt':'16.7.8.4 Hydration'}]
if __name__=='__main__':save(72,[record],carry=carry,issues=issues,chapter_number=16)
