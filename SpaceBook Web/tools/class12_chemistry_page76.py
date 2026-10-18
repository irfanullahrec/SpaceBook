"""PDF76 printed144–145: resonance energy of benzene; reactivity; addition of hydrogen and halogens."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow76');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'cyclohexene':('سائیکلوہیکسین','سایکلوهېکسین'),'cyclohexane':('سائیکلوہیکسین (اکیلا بند)','سایکلوهېکسان'),'cyclohexa-1,3-diene':('سائیکلوہیکسا-1،3-ڈائی این','سایکلوهېکسا-1،3-ډای ین'),
   'cyclohexa-1,3,5-triene':('سائیکلوہیکسا-1،3،5-ٹرائی این','سایکلوهېکسا-1،3،5-ټرای ین'),'benzene':('بینزین','بنزین'),'toluene':('ٹولوئین','تولوین'),
   'methylcyclohexane':('میتھائل سائیکلوہیکسین','میتایل سایکلوهېکسان'),'light':('روشنی','رڼا'),'1,2,3,4,5,6-hexachlorocyclohexane':('1،2،3،4،5،6-ہیکسا کلورو سائیکلوہیکسین','1،2،3،4،5،6-هېکسا کلوروسایکلوهېکسان')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def ring(cx,cy,r=28,dbl=(),circle=False,subs=None):
 s=F.ring(cx,cy,r,kek=False,circle=circle,subs=subs)
 pts=[(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
 for i in dbl:
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.76;s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 return s
def hyd(lang,dbl,circle,name,reag,heat,nums=False):
 s=F.start(110)+ring(110,48,30,dbl,circle)+t(110,100,lb(lang,name),13)
 if nums:
  for i,n in enumerate('623451'):a=math.radians(60*i);s+=t(110+18*math.sin(a),48-18*math.cos(a)+4,n,9,'#555')
 s+=t(195,55,reag,18)+F.arrow(240,350,48,'Pt')+ring(410,48,30)+t(410,100,lb(lang,'cyclohexane'),13)+t(540,55,heat,18)
 return s+'</svg>'
def addH(lang,kind):
 y=55 if kind=='benzene' else 75;s=F.start(y+70)
 if kind=='benzene':s+=ring(150,y,30,circle=True)+t(150,y+55,lb(lang,'benzene'),13);b='cyclohexane';sub=None
 else:s+=ring(150,y,30,(0,2,4),subs={0:'CH₃'})+t(150,y+55,lb(lang,'toluene'),13);b='methylcyclohexane';sub={0:'CH₃'}
 s+=t(235,y+7,'+ 3H₂',18)+F.arrow(290,430,y,'Ni/250-300°C','or Pt or Pd/150°C')+ring(500,y,30,subs=sub)+t(500,y+55,lb(lang,b),13)
 return s+'</svg>'
def hexachloro(lang):
 s=F.start(170)+ring(150,80,30,circle=True)+t(150,135,lb(lang,'benzene'),13)+t(235,87,'+ 3Cl₂',18)+F.arrow(290,410,80,lb(lang,'light'))
 cx,cy,r=530,80,34;s+=ring(cx,cy,r)
 for i in range(6):
  a=math.radians(60*i);x,y=cx+r*math.sin(a),cy-r*math.cos(a);dx,dy=math.sin(a),-math.cos(a)
  for side,lab in ((-1,'H' if i%2==0 else 'Cl'),(1,'Cl' if i%2==0 else 'H')):
   b=a+side*math.radians(35);ex,ey=x+24*math.sin(b),y-24*math.cos(b)
   s+=line(x,y,ex,ey,1.5)+t(x+34*math.sin(b),y-34*math.cos(b)+5,lab,12)
 s+=t(cx,cy+r+56,lb(lang,'1,2,3,4,5,6-hexachlorocyclohexane'),13)
 return s.replace('viewBox="0 0 850 170"','viewBox="0 0 850 180"')+'</svg>'

add('It should be noted that the concept of resonance does not mean that these structures rapidly shifts between canonical forms. In fact, all the molecules of a substance have the same structure all the time, in which all the electrons are delocalized over the whole system involved in resonance.',
 'یاد رہے کہ ریزونینس کے تصور کا یہ مطلب نہیں کہ یہ ساختیں کینونیکل صورتوں کے درمیان تیزی سے بدلتی رہتی ہیں۔ دراصل کسی مادے کے تمام سالمات ہر وقت ایک ہی ساخت رکھتے ہیں، جس میں تمام الیکٹران ریزونینس میں شامل پورے نظام پر غیر مقامی ہوتے ہیں۔',
 'د یادونې وړ ده چې د ریزونانس مفهوم دا معنا نه لري چې دا جوړښتونه د کینونیکل بڼو ترمنځ په چټکۍ بدلېږي. په حقیقت کې د یوې مادې ټول مالیکولونه هر وخت یو شان جوړښت لري، چې پکې ټول الکترونونه په ریزونانس کې د ښکېل ټول سیستم پر سر غیر ځایي دي.')
add('Resonance Energy and Stability of Benzene','بینزین کی ریزونینس توانائی اور پائیداری','د بنزین د ریزونانس انرژي او ثبات','heading')
add('The resonance energy of a molecules is the difference between the energy of the most stable canonical form and that of the actual molecule. For benzene it can be calculated by measuring its heat of hydrogenation and comparing it with that of the most stable canonical from.',
 'کسی سالمے کی ریزونینس توانائی سب سے پائیدار کینونیکل صورت کی توانائی اور اصل سالمے کی توانائی کا فرق ہے۔ بینزین کے لیے اسے اس کی حرارتِ ہائیڈروجینیشن ناپ کر اور سب سے پائیدار کینونیکل صورت کی حرارت سے موازنہ کر کے حساب کیا جا سکتا ہے۔',
 'د یوه مالیکول د ریزونانس انرژي د تر ټولو ثابتې کینونیکل بڼې د انرژۍ او د اصلي مالیکول د انرژۍ توپیر دی. د بنزین لپاره دا د هغه د هایدروجینېشن د تودوخې په اندازه کولو او د تر ټولو ثابتې کینونیکل بڼې له تودوخې سره په پرتله کولو محاسبه کېدای شي.')
add('Hydrogenation of cyclohexene (having one double bond) evolves 120 kJ/mol heat energy to form cyclohexane.','سائیکلوہیکسین (ایک دوہرے بند والی) کی ہائیڈروجینیشن سے سائیکلوہیکسین (اکیلے بند والی) بنتے ہوئے 120 kJ/mol حرارتی توانائی خارج ہوتی ہے۔','د سایکلوهېکسین (یو دوه ګونی تړون لرونکی) هایدروجینېشن د سایکلوهېکسان د جوړېدو پر مهال 120 kJ/mol تودوخه خوشې کوي.')
visual('chem12-p76-cyclohexene',lambda l:hyd(l,(1,),False,'cyclohexene','+ H₂','+ 120kJ/mol'))
add('Hydrogenation of cyclohexa–1,3–diene (having two double bonds) evolves 232 kJ/mol to form cyclohexane, which is almost double of the value 120 kJ/mol for cyclohexene.','سائیکلوہیکسا–1،3–ڈائی این (دو دوہرے بندوں والی) کی ہائیڈروجینیشن سے سائیکلوہیکسین بنتے ہوئے 232 kJ/mol خارج ہوتی ہے، جو سائیکلوہیکسین کی 120 kJ/mol قدر کا تقریباً دوگنا ہے۔','د سایکلوهېکسا–1،3–ډای ین (دوه دوه ګوني تړونونه لرونکی) هایدروجینېشن د سایکلوهېکسان د جوړېدو پر مهال 232 kJ/mol خوشې کوي، چې د سایکلوهېکسین د 120 kJ/mol ارزښت شاوخوا دوه چنده دی.')
visual('chem12-p76-cyclohexadiene',lambda l:hyd(l,(1,3),False,'cyclohexa-1,3-diene','+ 2H₂','+ 232 kJ/mol'))
add('The molecule cyclohexa-1,3,5-triene (Kekule structure) normally written for benzene and having three double bonds, should release energy three time to that of cyclohexane (i.e. 120×3 = 360 kJ/mol), upon hydrogenation.','سالمہ سائیکلوہیکسا-1،3،5-ٹرائی این (کیکولے ساخت)، جو عموماً بینزین کے لیے لکھا جاتا ہے اور جس میں تین دوہرے بند ہیں، ہائیڈروجینیشن پر سائیکلوہیکسین کی تین گنا توانائی (یعنی 120×3 = 360 kJ/mol) خارج کرنی چاہیے۔','سایکلوهېکسا-1،3،5-ټرای ین مالیکول (د کیکولې جوړښت)، چې معمولاً د بنزین لپاره لیکل کېږي او درې دوه ګوني تړونونه لري، باید د هایدروجینېشن پر مهال د سایکلوهېکسان درې چنده انرژي (یعنې 120×3 = 360 kJ/mol) خوشې کړي.')
visual('chem12-p76-triene',lambda l:hyd(l,(0,2,4),False,'cyclohexa-1,3,5-triene','+ 3H₂','+ 360 kJ/mol',True))
add('But hydrogenation of benzene actually evolves only 208 kJ/mol.','لیکن بینزین کی ہائیڈروجینیشن حقیقتاً صرف 208 kJ/mol خارج کرتی ہے۔','خو د بنزین هایدروجینېشن په حقیقت کې یوازې 208 kJ/mol خوشې کوي.')
visual('chem12-p76-benzene-hydrogenation-energy',lambda l:hyd(l,(),True,'benzene','+ 3H₂','+ 208 kJ/mol'))
add('Thus, the measured (experimental) heat of hydrogenation of benzene is less than the expected value of the most stable canonical form by an amount of 152 kJ/mol. Benzene is, therefore, is said to be resonance stabilized by an amount of 152 kJ/mol which is known as its resonance energy.',
 'لہٰذا بینزین کی ناپی گئی (تجرباتی) حرارتِ ہائیڈروجینیشن سب سے پائیدار کینونیکل صورت کی متوقع قدر سے 152 kJ/mol کم ہے۔ اس لیے کہا جاتا ہے کہ بینزین 152 kJ/mol کی مقدار سے ریزونینس کے ذریعے پائیدار ہے، جسے اس کی ریزونینس توانائی کہتے ہیں۔',
 'نو د بنزین اندازه شوې (تجربوي) د هایدروجینېشن تودوخه د تر ټولو ثابتې کینونیکل بڼې له تمه شوي ارزښت 152 kJ/mol کمه ده. له همدې امله ویل کېږي چې بنزین د 152 kJ/mol په اندازه د ریزونانس له لارې ثابت شوی، چې د هغه د ریزونانس انرژي بلل کېږي.')
add('16.8.5 Reactivity and Reactions','16.8.5 تعامل پذیری اور تعاملات','16.8.5 تعامل وړتیا او تعاملونه','heading')
add('Due to unusual stability (resonance stabilization), benzene and its derivatives do not give addition reactions like those of alkenes. In alkenes the pi electronic cloud is localized between the two carbon atoms and thus they readily undergo addition reactions. In benzene the pi electronic cloud makes a continuous sheet above and below all the six nuclei and the pi electrons are, thus delocalized, which give benzene more stability. Benzene, therefore, prefers to undergo electrophilic substitution reactions rather than addition reactions, to retain its aromatic character.',
 'غیر معمولی پائیداری (ریزونینس سے پائیداری) کی وجہ سے بینزین اور اس کے مشتقات الکینز جیسے اضافی تعاملات نہیں دیتے۔ الکینز میں پائی الیکٹرانی بادل دو کاربن ایٹموں کے درمیان مقامی ہوتا ہے اور اس لیے یہ آسانی سے اضافی تعاملات کرتے ہیں۔ بینزین میں پائی الیکٹرانی بادل تمام چھ مرکزوں کے اوپر اور نیچے ایک مسلسل تہہ بناتا ہے اور پائی الیکٹران یوں غیر مقامی ہوتے ہیں، جو بینزین کو زیادہ پائیداری دیتے ہیں۔ چنانچہ بینزین اپنی ارومیٹک خصوصیت برقرار رکھنے کے لیے اضافی تعاملات کے بجائے الیکٹروفائلی تبادلے کے تعاملات کو ترجیح دیتی ہے۔',
 'د غیر معمولي ثبات (د ریزونانس ثبات) له امله بنزین او د هغه مشتقات د الکینونو په څېر اضافي تعاملونه نه ورکوي. په الکینونو کې پای الکتروني ورېځ د دوو کاربني اټومونو ترمنځ ځایي وي او له همدې امله په اسانۍ اضافي تعاملونه کوي. په بنزین کې پای الکتروني ورېځ د ټولو شپږو هستو پورته او لاندې یوه پرله پسې پاڼه جوړوي او پای الکترونونه په دې ډول غیر ځایي دي، چې بنزین ته ډېر ثبات ورکوي. نو بنزین د خپل اروماتیک ځانګړتیا د ساتلو لپاره د اضافي تعاملونو پر ځای الکتروفایلي بدلون تعاملونه غوره کوي.')
add('16.8.5.1 Addition Reactions','16.8.5.1 اضافی تعاملات','16.8.5.1 اضافي تعاملونه','heading')
add('Benzene is very resistant to addition reaction and requires much more vigorous conditions than generally required for alkenes and alkynes. It does not undergo electrophilic addition reaction, but may give free-radical type addition and catalytic addition reactions in proper conditions.',
 'بینزین اضافی تعامل کے خلاف بہت مزاحم ہے اور اسے الکینز اور الکائنز کے لیے عام طور پر درکار شرائط سے کہیں زیادہ سخت شرائط چاہئیں۔ یہ الیکٹروفائلی اضافی تعامل نہیں کرتی، مگر مناسب شرائط میں آزاد ریڈیکل قسم کے اضافی اور عمل انگیز اضافی تعاملات دے سکتی ہے۔',
 'بنزین د اضافي تعامل په وړاندې ډېر مقاوم دی او د الکینونو او الکاینونو لپاره له عموماً اړینو شرایطو ډېر سخت شرایط غواړي. الکتروفایلي اضافي تعامل نه کوي، خو په مناسبو شرایطو کې د ازاد رادیکال ډوله اضافي او کتلستي اضافي تعاملونه ورکولی شي.')
add('16.8.5.1.1 Addition of Hydrogen','16.8.5.1.1 ہائیڈروجن کا اضافہ','16.8.5.1.1 د هایدروجن زیاتول','heading')
add('Benzene reacts with hydrogen in the presence of Ni, Pt or Pd catalyst at elevated temperature and high pressure to form cyclohexane. The reaction is also called catalytic hydrogenation.',
 'بینزین بلند درجہ حرارت اور زیادہ دباؤ پر Ni، Pt یا Pd عمل انگیز کی موجودگی میں ہائیڈروجن سے تعامل کر کے سائیکلوہیکسین (اکیلے بند والی) بناتی ہے۔ اس تعامل کو عمل انگیز ہائیڈروجینیشن بھی کہتے ہیں۔',
 'بنزین په لوړه تودوخه او لوړ فشار کې د Ni، Pt یا Pd کتلست په شتون کې له هایدروجن سره تعامل کوي او سایکلوهېکسان جوړوي. دې تعامل ته کتلستي هایدروجینېشن هم وايي.')
visual('chem12-p76-benzene-hydrogenation',lambda l:addH(l,'benzene'))
add('Similarly toluene (a benzene derivative) upon catalytic hydrogenation yield methylcyclohexane.','اسی طرح ٹولوئین (بینزین کا ایک مشتق) عمل انگیز ہائیڈروجینیشن پر میتھائل سائیکلوہیکسین دیتی ہے۔','همدارنګه تولوین (د بنزین یو مشتق) د کتلستي هایدروجینېشن پر مهال میتایل سایکلوهېکسان ورکوي.')
visual('chem12-p76-toluene-hydrogenation',lambda l:addH(l,'toluene'))
add('16.8.5.1.2 Addition of Halogens','16.8.5.1.2 ہیلوجنز کا اضافہ','16.8.5.1.2 د هالوجنونو زیاتول','heading')
add('Benzene reacts with chlorine or bromine in the presence of light to form benzene hexachloride and benzene hexabromide respectively. The reaction follow free radical addition mechanism.',
 'بینزین روشنی کی موجودگی میں کلورین یا برومین سے تعامل کر کے بالترتیب بینزین ہیکسا کلورائیڈ اور بینزین ہیکسا برومائیڈ بناتی ہے۔ یہ تعامل آزاد ریڈیکل اضافی طریق کار پر چلتا ہے۔',
 'بنزین د رڼا په شتون کې له کلورین یا برومین سره تعامل کوي او په ترتیب سره بنزین هېکسا کلوراید او بنزین هېکسا برومایډ جوړوي. دا تعامل د ازاد رادیکال د اضافې میکانیزم تعقیبوي.')
visual('chem12-p76-hexachloro',hexachloro)

record=section('16.23','Resonance energy of benzene and addition reactions','بینزین کی ریزونینس توانائی اور اضافی تعاملات','د بنزین د ریزونانس انرژي او اضافي تعاملونه',paras,layout,blocks,'144–145')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':76,'printedPages':[144,145]}]
record['sourceContinuesOnPdfPage']=77
issues=[{'id':'chem12-p144-printed-wording','printedPage':144,'description':'Printed "canonical from", "three time" and "is, therefore, is said" retained in English; italic definition retained as plain text.'}]
carry=[{'from':'16.23','to':'16.24','startsAt':'However, when halogen is treated with toluene'}]
if __name__=='__main__':save(76,[record],carry=carry,issues=issues,chapter_number=16)
