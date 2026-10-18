"""PDF80 printed152–153: ortho/para and meta directing substituents."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow80');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'phenol':('فینول','فینول'),'o-nitrophenol (55%)':('o-نائٹرو فینول (55%)','o-نایټروفینول (55%)'),'m-nitrophenol (1%)':('m-نائٹرو فینول (1%)','m-نایټروفینول (1%)'),
   'p-nitrophenol (44%)':('p-نائٹرو فینول (44%)','p-نایټروفینول (44%)'),'more stable arenium ions':('زیادہ پائیدار ایرینیم آئن','ډېر ثابت ارینیم ایونونه'),
   'less stable arenium ion':('کم پائیدار ایرینیم آئن','لږ ثابت ارینیم ایون'),'AND':('اور','او'),'nitrobenzene':('نائٹرو بینزین','نایټروبنزین'),
   'o-dinitrobenzene (6%)':('o-ڈائی نائٹرو بینزین (6%)','o-ډای نایټروبنزین (6%)'),'m-dinitrobenzene (93%)':('m-ڈائی نائٹرو بینزین (93%)','m-ډای نایټروبنزین (93%)'),
   'p-dinitrobenzene (1%)':('p-ڈائی نائٹرو بینزین (1%)','p-ډای نایټروبنزین (1%)'),'less stable arenium ions':('کم پائیدار ایرینیم آئن','لږ ثابت ارینیم ایونونه'),
   'more stable arenium ion':('زیادہ پائیدار ایرینیم آئن','ډېر ثابت ارینیم ایون'),'conc.':('مرتکز','غلیظ'),'dil. HNO₃':('ہلکا HNO₃','رقیق HNO₃')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def P(cx,cy,r):return [(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
def ring(cx,cy,r=26,dbl=(0,2,4),subs=None,charge=None,exo=False):
 s=F.ring(cx,cy,r,kek=False,subs=subs);pts=P(cx,cy,r)
 for i in dbl:
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.76;s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 if exo:x,y=pts[0];s+=line(x+4,y,x+4,y-14)
 if charge:
  v,sym=charge;x,y=pts[v];s+=t(cx+(x-cx)*1.35,cy+(y-cy)*1.35+5,sym,14)
 return s
def arenium(cx,cy,k,plus,sub,r=26):
 """sp3 at vertex k (H,E), ⊕ at vertex plus (pentadienyl-consistent)."""
 off=(plus-k)%6;edges={1:(k+2,k+4),3:(k+1,k+4),5:(k+1,k+3)}[off]
 s=ring(cx,cy,r,tuple(e%6 for e in edges),subs={0:sub});pts=P(cx,cy,r);x,y=pts[k];dx,dy=(x-cx)/r,(y-cy)/r
 a=math.atan2(dy,dx)
 for d,lab in ((-0.6,'H'),(0.6,'E')):
  ex,ey=x+18*math.cos(a+d),y+18*math.sin(a+d);s+=line(x,y,ex,ey,1.5)+t(x+28*math.cos(a+d),y+28*math.sin(a+d)+5,lab,14)
 px,py=pts[plus];s+=t(cx+(px-cx)*.5,cy+(py-cy)*.5+5,'⊕',13)
 return s
def substitution(lang,start,cond,names,sub0,sub,h=210):
 s=F.start(h)+ring(70,95,26,subs={0:sub0})+t(70,150,lb(lang,start),13)
 s+=line(110,95,215,95,2,'#222','marker-end="url(#arrow80)"')
 for i,c in enumerate(cond):s+=t(162,85 if i==0 else 98+15*i,c,12)
 for k,(v,name) in enumerate(zip((1,2,3),names)):
  x=300+k*200;s+=ring(x,85,26,subs={0:sub0,v:sub})+t(x,170 if v==3 else 148,lb(lang,name),12)
  if k<2:s+=t(x+100,90,'+',20)
 return s+'</svg>'
def resonance(lang,sub,signs,exo_label,neg):
 s=F.start(130)
 forms=[((0,2,4),None,False,sub),((2,4),(1,neg),True,exo_label),((1,4),(3,neg),True,exo_label),((1,3),(5,neg),True,exo_label),((0,2,4),None,False,sub)]
 for k,(dbl,ch,exo,lab) in enumerate(forms):
  x=80+k*170;s+=ring(x,75,26,dbl,{0:lab},ch,exo)
  if k<4:s+=t(x+85,82,'⟷',20)
 return s+'</svg>'
def stability(lang,sub,items,labels):
 s=F.start(170)
 for x,(k,plus) in zip((150,400,650),items):s+=arenium(x,80,k,plus,sub)
 s+=t(275,85,lb(lang,'AND'),15)
 for x,l in labels:s+=t(x,160,lb(lang,l),13)
 return s+'</svg>'

add('i. Ortho/Para Directing substituents','i. اورتھو/پیرا سمت دینے والے متبادلات','i. اورتو/پارا لارښوونکي بدیلونه','heading')
add('Substituents which direct the second substituent to the ortho and para positions simultaneously are called the ortho/para (o/p) directing substituents. For example, when phenol is nitrated, with dilute nitric acid, the reaction yields mainly the o–nitrophenol and p–nitrophenol. Thus the –OH group of phenol, which has directed the second substituent –NO₂ to ortho and para positions is designated as ortho/para directing. Some common ortho/para directing groups are, –OH, –NH₂, –NHR, –NR₂, –R, –X (halogens) etc. (Table 16.6).',
 'وہ متبادلات جو دوسرے متبادل کو بیک وقت اورتھو اور پیرا مقامات کی طرف بھیجتے ہیں، اورتھو/پیرا (o/p) سمت دینے والے متبادلات کہلاتے ہیں۔ مثلاً جب فینول کی ہلکے نائٹرک ایسڈ سے نائٹریشن کی جائے تو زیادہ تر o–نائٹرو فینول اور p–نائٹرو فینول بنتے ہیں۔ اس طرح فینول کا –OH گروپ، جس نے دوسرے متبادل –NO₂ کو اورتھو اور پیرا مقامات کی طرف بھیجا، اورتھو/پیرا سمت دینے والا قرار پاتا ہے۔ چند عام اورتھو/پیرا سمت دینے والے گروپ –OH، –NH₂، –NHR، –NR₂، –R، –X (ہیلوجنز) وغیرہ ہیں (جدول 16.6)۔',
 'هغه بدیلونه چې دویم بدیل په یو وخت اورتو او پارا موقعیتونو ته لارښوونه کوي، اورتو/پارا (o/p) لارښوونکي بدیلونه بلل کېږي. د بېلګې په توګه کله چې فینول له رقیق نایټریک اسید سره نایټرېټ شي، تعامل ډېری o–نایټروفینول او p–نایټروفینول ورکوي. نو د فینول –OH ګروپ، چې دویم بدیل –NO₂ یې اورتو او پارا موقعیتونو ته لارښوونه کړې، اورتو/پارا لارښوونکی ګڼل کېږي. ځینې عام اورتو/پارا لارښوونکي ګروپونه –OH، –NH₂، –NHR، –NR₂، –R، –X (هالوجنونه) او نور دي (جدول 16.6).')
visual('chem12-p80-phenol-nitration',lambda l:substitution(l,'phenol',[lb(l,'dil. HNO₃'),'25°C','−H₂O'],['o-nitrophenol (55%)','m-nitrophenol (1%)','p-nitrophenol (44%)'],'OH','NO₂'))
add('The ortho/para directing effect can be explained in terms of charge distribution and relative stability of arenium ion.','اورتھو/پیرا سمت دینے کے اثر کی وضاحت چارج کی تقسیم اور ایرینیم آئن کی اضافی پائیداری کے لحاظ سے کی جا سکتی ہے۔','د اورتو/پارا لارښوونې اغېز د چارج د وېش او د ارینیم ایون د نسبي ثبات له مخې روښانه کېدای شي.')
add('a. Charge Distribution','a. چارج کی تقسیم','a. د چارج وېش','heading')
add('Consider, the various resonance forms of phenol.','فینول کی مختلف ریزونینس صورتوں پر غور کریں۔','د فینول بېلابېلو ریزونانس بڼو ته پام وکړئ.')
visual('chem12-p80-phenol-resonance',lambda l:resonance(l,':ÖH',None,'⊕OH','⊖'))
add('As can be seen that one of the non–bonding electron pairs of oxygen of the –OH group is delocalized over the ring, making the ortho and para positions more electron rich than the meta position. The electrophile would naturally prefer to attack at these electron rich centers, to give mainly ortho and para disubstituted products.',
 'جیسا کہ دیکھا جا سکتا ہے، –OH گروپ کی آکسیجن کے غیر بندشی الیکٹرانی جوڑوں میں سے ایک حلقے پر غیر مقامی ہو جاتا ہے، جس سے اورتھو اور پیرا مقامات میٹا مقام سے زیادہ الیکٹرانوں سے بھرپور ہو جاتے ہیں۔ الیکٹروفائل فطری طور پر انہی الیکٹرانوں سے بھرپور مراکز پر حملہ ترجیحاً کرے گا اور زیادہ تر اورتھو اور پیرا دو متبادل پیداواریں دے گا۔',
 'لکه څنګه چې لیدل کېږي، د –OH ګروپ د اکسیجن له نا تړلو الکتروني جوړو څخه یوه پر کړۍ غیر ځایي کېږي، چې اورتو او پارا موقعیتونه له میټا موقعیت ډېر له الکترونونو ډک کوي. الکتروفایل په طبیعي ډول پر همدې له الکترونونو ډکو مرکزونو برید غوره کوي او ډېری اورتو او پارا دوه بدیلي محصولات ورکوي.')
add('b. Relative Stability of Arenium ion','b. ایرینیم آئن کی اضافی پائیداری','b. د ارینیم ایون نسبي ثبات','heading')
add('The intermediate arenium ion in the presence of ortho/para directing groups is more stable when the second substituent is at ortho/para positions than when it is at meta position as shown below.',
 'اورتھو/پیرا سمت دینے والے گروپوں کی موجودگی میں درمیانی ایرینیم آئن اس وقت زیادہ پائیدار ہوتا ہے جب دوسرا متبادل اورتھو/پیرا مقامات پر ہو، بہ نسبت اس کے کہ وہ میٹا مقام پر ہو، جیسا کہ نیچے دکھایا گیا ہے۔',
 'د اورتو/پارا لارښوونکو ګروپونو په شتون کې منځنی ارینیم ایون هغه وخت ډېر ثابت دی چې دویم بدیل په اورتو/پارا موقعیتونو کې وي، د میټا موقعیت په پرتله، لکه څنګه چې لاندې ښودل شوي.')
visual('chem12-p80-phenol-arenium',lambda l:stability(l,'OH',((1,0),(3,2),(2,3)),((275,'more stable arenium ions'),(650,'less stable arenium ion'))))
add('ii. Meta Directing substituents','ii. میٹا سمت دینے والے متبادلات','ii. میټا لارښوونکي بدیلونه','heading')
add('The substituents which direct the second incoming substituent to meta position, are called meta–directing substituents. For example, nitration of nitrobenzene in the presence of concentrated nitric acid and sulfuric acid at 100°C gives mainly m–dinitrobenzene. Thus the substituent –NO₂ group, which has directed the second –NO₂ group to the meta position is meta directing. Some common meta directing groups are –NO₂, –CN, –CHO, –COR, –COOH etc. (Table 16.5).',
 'وہ متبادلات جو دوسرے آنے والے متبادل کو میٹا مقام کی طرف بھیجتے ہیں، میٹا سمت دینے والے متبادلات کہلاتے ہیں۔ مثلاً 100°C پر مرتکز نائٹرک ایسڈ اور سلفیورک ایسڈ کی موجودگی میں نائٹرو بینزین کی نائٹریشن سے زیادہ تر m–ڈائی نائٹرو بینزین بنتی ہے۔ اس طرح متبادل –NO₂ گروپ، جس نے دوسرے –NO₂ گروپ کو میٹا مقام کی طرف بھیجا، میٹا سمت دینے والا ہے۔ چند عام میٹا سمت دینے والے گروپ –NO₂، –CN، –CHO، –COR، –COOH وغیرہ ہیں (جدول 16.5)۔',
 'هغه بدیلونه چې دویم راتلونکی بدیل میټا موقعیت ته لارښوونه کوي، میټا لارښوونکي بدیلونه بلل کېږي. د بېلګې په توګه په 100°C کې د غلیظ نایټریک اسید او سلفوریک اسید په شتون کې د نایټروبنزین نایټرېشن ډېری m–ډای نایټروبنزین ورکوي. نو –NO₂ بدیل ګروپ، چې دویم –NO₂ ګروپ یې میټا موقعیت ته لارښوونه کړې، میټا لارښوونکی دی. ځینې عام میټا لارښوونکي ګروپونه –NO₂، –CN، –CHO، –COR، –COOH او نور دي (جدول 16.5).')
visual('chem12-p80-nitrobenzene-nitration',lambda l:substitution(l,'nitrobenzene',[lb(l,'conc.')+' HNO₃',lb(l,'conc.')+' H₂SO₄','100°C','−H₂O'],['o-dinitrobenzene (6%)','m-dinitrobenzene (93%)','p-dinitrobenzene (1%)'],'NO₂','NO₂',215))
add('The meta–directing effect of a group may also be due to the following two reasons i.e. charge distribution and relative stability by arenium ion.','کسی گروپ کا میٹا سمت دینے کا اثر بھی درج ذیل دو وجوہ سے ہو سکتا ہے، یعنی چارج کی تقسیم اور ایرینیم آئن کی اضافی پائیداری۔','د یوه ګروپ د میټا لارښوونې اغېز هم کېدای شي د لاندې دوو دلیلونو له امله وي، یعنې د چارج وېش او د ارینیم ایون نسبي ثبات.')
add('a. Charge Distribution','a. چارج کی تقسیم','a. د چارج وېش','heading')
add('These groups withdraw electron density from ortho and para positions. Thus, meta position of the ring has relatively more electronic density than ortho and para positions, and becomes an attractive target for electrophile. It is clear from the resonance structures of nitrobenzene that ortho and para positions have small electron density compared to meta position.',
 'یہ گروپ اورتھو اور پیرا مقامات سے الیکٹرانی کثافت کھینچ لیتے ہیں۔ اس طرح حلقے کے میٹا مقام پر اورتھو اور پیرا مقامات کی نسبت زیادہ الیکٹرانی کثافت ہوتی ہے، اور یہ الیکٹروفائل کے لیے پرکشش ہدف بن جاتا ہے۔ نائٹرو بینزین کی ریزونینس ساختوں سے واضح ہے کہ اورتھو اور پیرا مقامات پر میٹا مقام کی نسبت کم الیکٹرانی کثافت ہے۔',
 'دا ګروپونه له اورتو او پارا موقعیتونو څخه الکتروني کثافت راکاږي. نو د کړۍ میټا موقعیت د اورتو او پارا موقعیتونو په پرتله نسبتاً ډېر الکتروني کثافت لري، او د الکتروفایل لپاره زړه راښکونکی هدف ګرځي. د نایټروبنزین له ریزونانس جوړښتونو څرګندېږي چې اورتو او پارا موقعیتونه د میټا موقعیت په پرتله لږ الکتروني کثافت لري.')
visual('chem12-p80-nitro-resonance',lambda l:resonance(l,'NO₂',None,'⁻O—N⁺—O⁻','⊕'))
add('b. Relative Stability of Arenium ion','b. ایرینیم آئن کی اضافی پائیداری','b. د ارینیم ایون نسبي ثبات','heading')
add('Secondly, the arenium ion formed in the presence of meta orienting groups is more stable when the second substituent is at meta position than when it is at ortho or para positions, as shown below.',
 'دوسرے، میٹا سمت دینے والے گروپوں کی موجودگی میں بننے والا ایرینیم آئن اس وقت زیادہ پائیدار ہوتا ہے جب دوسرا متبادل میٹا مقام پر ہو، بہ نسبت اس کے کہ وہ اورتھو یا پیرا مقامات پر ہو، جیسا کہ نیچے دکھایا گیا ہے۔',
 'دویم دا چې د میټا لارښوونکو ګروپونو په شتون کې جوړ شوی ارینیم ایون هغه وخت ډېر ثابت دی چې دویم بدیل په میټا موقعیت کې وي، د اورتو یا پارا موقعیتونو په پرتله، لکه څنګه چې لاندې ښودل شوي.')
visual('chem12-p80-nitro-arenium',lambda l:stability(l,'NO₂',((1,0),(3,2),(2,3)),((275,'less stable arenium ions'),(650,'more stable arenium ion'))))

record=section('16.27','Ortho/para and meta directing substituents','اورتھو/پیرا اور میٹا سمت دینے والے متبادلات','اورتو/پارا او میټا لارښوونکي بدیلونه',paras,layout,blocks,'152–153')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':80,'printedPages':[152,153]}]
record['sourceContinuesOnPdfPage']=81
issues=[{'id':'chem12-p152-table-reference','printedPage':152,'description':'Text cites "Table 16.6" (o/p directors) and "Table 16.5" (meta directors), but the orientation table on printed 154 is numbered 16.5 (pKa table also 16.5). Source references retained.'},
        {'id':'chem12-p152-resonance-drawing','printedPage':152,'description':'Phenol and nitrobenzene resonance forms reconstructed as coded rings with charge positions (⊖ at o/p for phenol, ⊕ at o/p for nitrobenzene); curly arrows of the printed drawings omitted.'}]
carry=[{'from':'16.27','to':'16.28','startsAt':'Self-assessmnet\nDraw the possible'}]
if __name__=='__main__':save(80,[record],carry=carry,issues=issues,chapter_number=16)
