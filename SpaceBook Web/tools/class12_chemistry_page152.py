"""PDF152 printed298–299: purine and pyrimidine bases, sugars, phosphoric acid, nucleotides, base pairing, DNA vs RNA comparison."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow152');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'adenine':('ایڈینین','اډینین'),'guanine':('گوانین','ګوانین'),'cytosine':('سائٹوسین','سایټوسین'),'thymine':('تھائمین','تایمین'),'uracil':('یوراسل','یوراسیل'),'(present only in DNA)':('(صرف DNA میں)','(یوازې په DNA کې)'),
   '(present only in RNA)':('(صرف RNA میں)','(یوازې په RNA کې)'),'β-ribose':('β-رائبوز','β-رایبوز'),'β-2-deoxyribose':('β-2-ڈی آکسی رائبوز','β-2-ډی اکسي رایبوز'),'phosphoric acid':('فاسفورک ایسڈ','فاسفوریک اسید'),
   'deoxyribonucleotide':('ڈی آکسی رائبونیوکلیوٹائیڈ','ډی اکسي رایبونیوکلیوټایډ'),'ribonuclectide':('رائبونیوکلیوٹائیڈ','رایبونیوکلیوټایډ')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def atom(x,y,v,size=13):return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5+3.5*len(v)}" fill="#fff"/>'+t(x,y+5,v,size)) if v else ''
def ring(pts,labels,dbl,subs,cx,cy):
 """pts list; labels per vertex (None = carbon); dbl = edge indices drawn double; subs = [(vertex, dx, dy, label, double)]."""
 s='';n=len(pts)
 for i in range(n):
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%n];s+=line(x1,y1,x2,y2,1.8)
  if i in dbl:s+=line(x1+(cx-x1)*.2,y1+(cy-y1)*.2,x2+(cx-x2)*.2,y2+(cy-y2)*.2,1.8)
 for v,dx,dy,lab,d in subs:
  x,y=pts[v];s+=line(x,y,x+dx,y+dy,1.8)
  if d:s+=line(x+4*dy/math.hypot(dx,dy),y-4*dx/math.hypot(dx,dy),x+dx+4*dy/math.hypot(dx,dy),y+dy-4*dx/math.hypot(dx,dy),1.8)
  s+=t(x+dx*1.45,y+dy*1.45+5,lab,13)
 for (x,y),l in zip(pts,labels):s+=atom(x,y,l)
 return s
def hexa(cx,cy,r=30):return [(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
def purine(cx,cy,six_labels,six_dbl,six_subs,five_labels,nh_sub=True):
 P=hexa(cx,cy);s=ring(P,six_labels,six_dbl,six_subs,cx,cy)
 Q=[P[1],(P[1][0]+28,P[1][1]-10),(P[1][0]+44,cy),(P[2][0]+28,P[2][1]+10),P[2]]
 for i in range(4):s+=line(*Q[i],*Q[i+1],1.8)
 s+=line(Q[1][0]+2,Q[1][1]+6,Q[2][0]-5,Q[2][1]-3,1.8)
 for p,l in zip(Q[1:4],five_labels):s+=atom(*p,l)
 if nh_sub:s+=line(Q[3][0],Q[3][1]+8,Q[3][0],Q[3][1]+18)+t(Q[3][0],Q[3][1]+32,'H',13)
 return s
def bases(lang):
 s=F.start(370)
 s+=purine(150,80,['N' if False else None,None,None,'N','N',None][:0] or [None,None,None,'N',None,'N'],(0,2,4),[(0,0,-22,'NH₂',False)],['N',None,'N'])+t(170,155,lb(lang,'adenine'),12)
 s=s.replace(atom(*hexa(150,80)[4],None),'')
 s+=purine(440,80,[None,None,None,'N',None,'N'],(2,),[(0,0,-22,'O',True),(4,-20,10,'NH₂',False)],['N',None,'N'])
 s+=atom(*hexa(440,80)[5],'NH')+t(460,155,lb(lang,'guanine'),12)
 for k,(cx,nm,extra,top,topd,n3) in enumerate(((140,'cytosine','',('NH₂',False),False,'N'),(400,'thymine','(present only in DNA)',('O',True),True,'H—N'),(660,'uracil','(present only in RNA)',('O',True),True,'H—N'))):
  P=hexa(cx,260);subs=[(0,0,-22,top[0],top[1]),(4,-20,10,'O',True),(3,0,20,'H',False)]
  if nm=='thymine':subs.append((1,20,-10,'CH₃',False))
  dbl=(1,) if nm!='cytosine' else (1,5)
  s+=ring(P,[None,None,None,'N',None,'N' if nm=='cytosine' else n3],dbl,subs,cx,260)+t(cx,342,lb(lang,nm),12)+(t(cx,358,lb(lang,extra),12) if extra else '')
 return s+'</svg>'
def furanose(cx,cy,deoxy):
 P=[(cx,cy-34),(cx+36,cy-8),(cx+24,cy+30),(cx-24,cy+30),(cx-36,cy-8)]
 s=''.join(line(*P[i],*P[(i+1)%5],1.8) for i in range(5))+atom(*P[0],'O')
 s+=line(*P[4],P[4][0]-20,P[4][1]-14)+t(P[4][0]-44,P[4][1]-16,'CH₂OH',13)+line(*P[4],P[4][0]-4,P[4][1]+18)+t(P[4][0]-6,P[4][1]+30,'H',12)
 s+=line(*P[1],P[1][0]+18,P[1][1]-14)+t(P[1][0]+32,P[1][1]-16,'OH',13)+line(*P[1],P[1][0]+4,P[1][1]+18)+t(P[1][0]+6,P[1][1]+30,'H',12)
 s+=line(*P[3],P[3][0],P[3][1]-18)+t(P[3][0],P[3][1]-22,'H',12)+line(*P[3],P[3][0],P[3][1]+18)+t(P[3][0],P[3][1]+32,'OH',13)
 s+=line(*P[2],P[2][0],P[2][1]-18)+t(P[2][0],P[2][1]-22,'H' if deoxy else 'OH',12)+line(*P[2],P[2][0],P[2][1]+18)+t(P[2][0],P[2][1]+32,'H' if deoxy else 'OH',13)
 return s
def sugars(lang):
 s=F.start(270)+furanose(220,70,False)+t(220,145,lb(lang,'β-ribose'),12)+furanose(560,70,True)+t(560,145,lb(lang,'β-2-deoxyribose'),12)
 s+=t(400,190,'O',13)+line(397,196,397,208)+line(403,196,403,208)+t(400,225,'OH — P — OH',14)+line(400,232,400,244)+t(400,258,'OH',13)+t(520,240,lb(lang,'phosphoric acid'),12)
 return s.replace('viewBox="0 0 850 270"','viewBox="0 0 850 275"')+'</svg>'
def nucleotides(lang):
 s=F.start(270)
 for cx,deoxy,nm,base in ((250,True,'deoxyribonucleotide','cytosine'),(650,False,'ribonuclectide','uracil')):
  P=[(cx,140),(cx+36,166),(cx+24,204),(cx-24,204),(cx-36,166)]
  s+=''.join(line(*P[i],*P[(i+1)%5],1.8) for i in range(5))+atom(*P[0],'O')
  s+=line(*P[4],P[4][0]-38,P[4][1]-30)+t(P[4][0]-80,P[4][1]-34,'HO—P—O—CH₂',13)
  px=P[4][0]-104;s+=line(px-3,P[4][1]-48,px-3,P[4][1]-60)+line(px+3,P[4][1]-48,px+3,P[4][1]-60)+t(px,P[4][1]-64,'O',11)+line(px,P[4][1]-28,px,P[4][1]-18)+t(px,P[4][1]-4,'O⁻',11)
  s+=line(*P[4],P[4][0]-4,P[4][1]+16)+t(P[4][0]-6,P[4][1]+28,'H',12)+line(*P[1],P[1][0]+4,P[1][1]+16)+t(P[1][0]+6,P[1][1]+28,'H',12)
  s+=line(*P[3],P[3][0],P[3][1]+16)+t(P[3][0],P[3][1]+30,'OH',13)+line(*P[2],P[2][0],P[2][1]+16)+t(P[2][0],P[2][1]+30,'H' if deoxy else 'OH',13)
  rc=(P[1][0]+34,P[1][1]-74);H=hexa(*rc,26)
  s+=line(*P[1],*H[3],1.8)
  subs=[(0,0,-18,'NH₂' if base=='cytosine' else 'O',base!='cytosine'),(2,20,8,'O',True)]+([] if base=='cytosine' else [(1,18,-6,'H',False)])
  s+=ring(H,[None,'N',None,'N',None,None],(0,4) if base=='cytosine' else (4,),subs,*rc)
  s+=t(H[1][0]+62,H[1][1]+18,lb(lang,base),11)+t(cx,262,lb(lang,nm),12)
 return s+'</svg>'

lines([('There are two different types of purine derivatives. These are adenine and guanine.','پیورین کے دو مختلف قسم کے مشتقات ہیں۔ یہ ایڈینین اور گوانین ہیں۔','د پیورین دوه بېلابېل ډوله مشتقات شته. دا اډینین او ګوانین دي.')])
visual('chem12-p152-bases',bases)
lines([('Similarly, there are three derivatives of pyrimidine. These are cytosine, thymine and uracil.','اسی طرح پیریمیڈین کے تین مشتقات ہیں۔ یہ سائٹوسین، تھائمین اور یوراسل ہیں۔','همدارنګه د پیریمیډین درې مشتقات شته. دا سایټوسین، تایمین او یوراسیل دي.'),
 ('DNA and RNA contain two different types of sugars.','DNA اور RNA میں دو مختلف قسم کی شکر ہوتی ہے۔','DNA او RNA دوه بېلابېل ډوله بورې لري.')])
add('One is deoxyribose and the other is ribose sugar. Both these sugars are in cyclic furanose form.','ایک ڈی آکسی رائبوز اور دوسری رائبوز شکر ہے۔ یہ دونوں شکر حلقوی فیورانوز صورت میں ہیں۔','یوه ډی اکسي رایبوز او بله رایبوز بوره ده. دا دواړه بورې په حلقوي فورانوز بڼه دي.')
lines([('The third component of nucleic acid is phosphoric acid.','نیوکلک ایسڈ کا تیسرا جزو فاسفورک ایسڈ ہے۔','د نیوکلیک اسید درېیمه برخه فاسفوریک اسید دی.')])
visual('chem12-p152-sugars-phosphate',sugars)
visual('chem12-p152-nucleotides',nucleotides)
add('A DNA molecule is formed by two antiparallel long polydeoxyribonucleotide chains, which wind on each other. These two chains are held together throughout the whole length by hydrogen bonding present between their nitrogenous bases.','DNA کا سالمہ دو مخالف متوازی لمبی پولی ڈی آکسی رائبونیوکلیوٹائیڈ زنجیروں سے بنتا ہے جو ایک دوسرے پر لپٹی ہوتی ہیں۔ یہ دونوں زنجیریں پوری لمبائی میں اپنے نائٹروجنی اساسوں کے درمیان ہائیڈروجن بندوں سے جڑی رہتی ہیں۔','د DNA مالیکول له دوو ضد موازي اوږدو پولي ډی اکسي رایبونیوکلیوټایډ ځنځیرونو جوړ دی چې پر یو بل تاو شوي. دا دوه ځنځیرونه په ټول اوږدوالي کې د خپلو نایټروجني قلویاتو ترمنځ د هایدروجني تړونونو په واسطه سره ساتل کېږي.')
add('Adenine joins only to thymine while guanine joins only to cytosine. Adenine joins to thymine by two while cytosine joins to guanine by three hydrogen bondings. This pairing of bases is highly specific. Adenine will never join cytosine and guanine never joins thymine.','ایڈینین صرف تھائمین سے جڑتا ہے جبکہ گوانین صرف سائٹوسین سے جڑتا ہے۔ ایڈینین تھائمین سے دو جبکہ سائٹوسین گوانین سے تین ہائیڈروجن بندوں کے ذریعے جڑتا ہے۔ اساسوں کی یہ جوڑی بندی نہایت مخصوص ہے۔ ایڈینین کبھی سائٹوسین سے نہیں جڑے گا اور گوانین کبھی تھائمین سے نہیں جڑتا۔','اډینین یوازې له تایمین سره نښلي او ګوانین یوازې له سایټوسین سره نښلي. اډینین له تایمین سره په دوو او سایټوسین له ګوانین سره په دریو هایدروجني تړونونو نښلي. د قلویاتو دا جوړه کېدل ډېر ځانګړی دی. اډینین به هېڅکله له سایټوسین او ګوانین هېڅکله له تایمین سره ونه نښلي.')
add('Difference between DNA and RNA','DNA اور RNA میں فرق','د DNA او RNA ترمنځ توپیر','heading')
add('DNA and RNA differs in the following points from each other.','DNA اور RNA درج ذیل نکات میں ایک دوسرے سے مختلف ہیں۔','DNA او RNA په لاندې ټکو کې له یو بل سره توپیر لري.')
tb={'id':'chem12-table-dna-rna','headers':['Comparison','DNA (Deoxyribonucleic Acid)','RNA (Ribonucleic Acid)'],
 'rows':[['Location','DNA is found in the nucleus, while a small amount of DNA also present in mitochondria.','RNA is formed in the nucleolus and then moves to specialized regions of the cytoplasm depending on the type of RNA formed.'],
  ['Structure','DNA consists of two strands, arranged in a double helix. These strands are made up of subunits called nucleotides.','RNA has only one strand, but like DNA, is made up of nucleotides.'],
  ['Length','DNA is a much longer polymer than RNA. A chromosome, for example, is a single, long DNA molecule, which would be several centimetres in length when unravelled.','RNA molecules are variable in length, but much shorter than long DNA polymers.'],
  ['Sugar','The sugar in DNA is deoxyribose.','RNA contains ribose sugar.'],
  ['Bases','The bases in DNA are Adenine (A), Guanine (G), Cytosine (C) and Thymine (T).','The bases in RNA are Adenine (A), Guanine (G) and Cytosine (C) like DNA, but contains Uracil (U) rather than Thymine.'],
  ['Base Pairs','Adenine and Thymine pair (A-T) Cytosine and Guanine pair (C-G)','Adenine and Uracil pair (A-U) Cytosine and Guanine pair (C-G)'],
  ['Function','DNA replicates and stores genetic information. It is a blueprint for all genetic information contained within an organism.','RNA converts the genetic information contained within DNA to a format used to synthesize proteins and then moves it to ribosomal protein factories.']],
 'translations':[{'language':'اردو','headers':['موازنہ','DNA (ڈی آکسی رائبونیوکلک ایسڈ)','RNA (رائبونیوکلک ایسڈ)'],
  'rows':[['مقام','DNA مرکزے میں پایا جاتا ہے، جبکہ DNA کی تھوڑی مقدار مائٹوکونڈریا میں بھی موجود ہے۔','RNA نیوکلیولس میں بنتا ہے اور پھر بننے والے RNA کی قسم کے مطابق سائٹوپلازم کے مخصوص حصوں میں چلا جاتا ہے۔'],
   ['ساخت','DNA دوہرے ہیلکس میں ترتیب دی گئی دو لڑیوں پر مشتمل ہے۔ یہ لڑیاں نیوکلیوٹائیڈز کہلانے والی ذیلی اکائیوں سے بنی ہیں۔','RNA کی صرف ایک لڑی ہے، لیکن DNA کی طرح نیوکلیوٹائیڈز سے بنا ہے۔'],
   ['لمبائی','DNA، RNA سے کہیں زیادہ لمبا پولیمر ہے۔ مثلاً کروموسوم ایک واحد لمبا DNA سالمہ ہے جو کھولنے پر کئی سینٹی میٹر لمبا ہوگا۔','RNA سالمات کی لمبائی متغیر ہے، لیکن لمبے DNA پولیمرز سے بہت کم ہے۔'],
   ['شکر','DNA میں شکر ڈی آکسی رائبوز ہے۔','RNA میں رائبوز شکر ہوتی ہے۔'],
   ['اساس','DNA میں اساس ایڈینین (A)، گوانین (G)، سائٹوسین (C) اور تھائمین (T) ہیں۔','RNA میں اساس DNA کی طرح ایڈینین (A)، گوانین (G) اور سائٹوسین (C) ہیں، لیکن تھائمین کے بجائے یوراسل (U) ہوتا ہے۔'],
   ['اساسی جوڑے','ایڈینین اور تھائمین جوڑا (A-T)، سائٹوسین اور گوانین جوڑا (C-G)','ایڈینین اور یوراسل جوڑا (A-U)، سائٹوسین اور گوانین جوڑا (C-G)'],
   ['فعل','DNA نقل بناتا اور جینیاتی معلومات ذخیرہ کرتا ہے۔ یہ جاندار میں موجود تمام جینیاتی معلومات کا خاکہ ہے۔','RNA، DNA میں موجود جینیاتی معلومات کو پروٹینز کی تالیف کے قابل صورت میں بدلتا ہے اور پھر اسے رائبوسومی پروٹین کارخانوں تک لے جاتا ہے۔']]},
  {'language':'پښتو','headers':['پرتله','DNA (ډی اکسي رایبونیوکلیک اسید)','RNA (رایبونیوکلیک اسید)'],
  'rows':[['ځای','DNA په هسته کې موندل کېږي، په داسې حال کې چې د DNA لږه اندازه په مایټوکانډریا کې هم شته.','RNA په نیوکلیولس کې جوړېږي او بیا د جوړ شوي RNA د ډول له مخې د سایټوپلازم ځانګړو سیمو ته ځي.'],
   ['جوړښت','DNA له دوو تارونو جوړ دی چې په دوه ګوني هیلېکس کې ترتیب شوي. دا تارونه له نیوکلیوټایډونو په نوم فرعي واحدونو جوړ دي.','RNA یوازې یو تار لري، خو د DNA په څېر له نیوکلیوټایډونو جوړ دی.'],
   ['اوږدوالی','DNA له RNA ډېر اوږد پولیمر دی. د بېلګې په توګه کروموزوم یو واحد اوږد DNA مالیکول دی چې د خلاصېدو پر مهال به څو سانتي متره اوږد وي.','د RNA مالیکولونه متغیر اوږدوالی لري، خو له اوږدو DNA پولیمرونو ډېر لنډ دي.'],
   ['بوره','په DNA کې بوره ډی اکسي رایبوز ده.','RNA رایبوز بوره لري.'],
   ['قلوي','په DNA کې قلوي اډینین (A)، ګوانین (G)، سایټوسین (C) او تایمین (T) دي.','په RNA کې قلوي د DNA په څېر اډینین (A)، ګوانین (G) او سایټوسین (C) دي، خو د تایمین پر ځای یوراسیل (U) لري.'],
   ['د قلوي جوړې','اډینین او تایمین جوړه (A-T)، سایټوسین او ګوانین جوړه (C-G)','اډینین او یوراسیل جوړه (A-U)، سایټوسین او ګوانین جوړه (C-G)'],
   ['دنده','DNA کاپي کېږي او جنیټیکي معلومات زېرمه کوي. دا په ژوندي موجود کې د ټولو جنیټیکي معلوماتو نقشه ده.','RNA په DNA کې شته جنیټیکي معلومات په هغه بڼه بدلوي چې د پروټینونو د جوړولو لپاره کارېږي او بیا یې رایبوزومي پروټین فابریکو ته وړي.']]}]}
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
record=section('21.14','Nucleic acid components and DNA–RNA comparison','نیوکلک ایسڈ کے اجزا اور DNA–RNA کا موازنہ','د نیوکلیک اسید برخې او د DNA–RNA پرتله',paras,layout,blocks,'298–300')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':152,'printedPages':[298,299]},{'sourcePdf':SOURCE,'pdfPage':153,'printedPages':[300],'note':'Bases, Base Pairs and Function rows of the DNA/RNA table continue on printed 300 and are kept with the table.'}]
record['sourceContinuesOnPdfPage']=153
carry=[{'from':'21.14','to':'21.15','startsAt':'Deoxyribonucleic Acid\n00000000001'}]
if __name__=='__main__':save(152,[record],carry=carry,chapter_number=21)
