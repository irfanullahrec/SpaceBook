"""PDF153 printed300–301: Figure 21.7 DNA vs RNA, 21.5.2 nucleic acid polymers (Figure 21.8), 21.5.3 storage of genetic information, 21.6 minerals intro."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow153');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'DNA':('DNA','DNA'),'Deoxyribonucleic Acid':('ڈی آکسی رائبونیوکلک ایسڈ','ډی اکسي رایبونیوکلیک اسید'),'RNA':('RNA','RNA'),'Ribonucleic Acid':('رائبونیوکلک ایسڈ','رایبونیوکلیک اسید'),
   'Double-stranded':('دوہری لڑی والا','دوه تاري'),'sugar phosphate':('شکر فاسفیٹ','بوره فاسفېټ'),'deoxyribose':('ڈی آکسی رائبوز','ډی اکسي رایبوز'),'Base pair':('اساسی جوڑا','د قلوي جوړه'),
   'Single':('واحد','یوازینی'),'nucleobsae':('نیوکلیو بیس','نیوکلیو قلوي'),'Single-stranded':('اکہری لڑی والا','یو تاري'),'ribose':('رائبوز','رایبوز'),
   'are chains of nucleotides':('نیوکلیوٹائیڈز کی زنجیریں ہیں','د نیوکلیوټایډونو ځنځیرونه دي'),'and':('اور','او'),'Ribose':('رائبوز','رایبوز'),'(sugar)':('(شکر)','(بوره)'),'Deoxyribose':('ڈی آکسی رائبوز','ډی اکسي رایبوز'),
   'Hydrogen':('ہائیڈروجن','هایدروجني'),'bonds':('بند','تړونونه'),'Sugar-phospate backbone':('شکر–فاسفیٹ ڈھانچہ','بوره–فاسفېټ ملا تیر'),'Nucleotide unit':('نیوکلیوٹائیڈ اکائی','نیوکلیوټایډ واحد')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
C={'A':'#e53935','T':'#fb8c00','G':'#43a047','C':'#fdd835','U':'#1e88e5'}
def helix(lang):
 s=F.start(380)
 s+=t(200,26,lb(lang,'DNA'),17,'#1a237e')+t(200,46,lb(lang,'Deoxyribonucleic Acid'),13,'#1a237e')+'<circle cx="425" cy="40" r="22" fill="#4fc3f7"/>'+t(425,46,'VS',15,'#fff')+t(650,26,lb(lang,'RNA'),17,'#1a237e')+t(650,46,lb(lang,'Ribonucleic Acid'),13,'#1a237e')
 a=' '.join(f'{200+50*math.sin(i/9):.1f},{70+i*2.4:.1f}' for i in range(120));b=' '.join(f'{200-50*math.sin(i/9):.1f},{70+i*2.4:.1f}' for i in range(120))
 s+=f'<polyline points="{a}" fill="none" stroke="#1565c0" stroke-width="9" opacity=".8"/><polyline points="{b}" fill="none" stroke="#5c6bc0" stroke-width="9" opacity=".8"/>'
 for k,(p,q) in enumerate((('G','C'),('C','G'),('G','C'),('A','T'),('T','A'),('C','G'),('G','C'),('C','G'))):
  y=86+k*32;w=abs(50*math.sin((y-70)/2.4/9))
  if w>12:s+=f'<rect x="{200-w}" y="{y-5}" width="{w}" height="10" fill="{C[p]}"/><rect x="200" y="{y-5}" width="{w}" height="10" fill="{C[q]}"/>'
 s+=t(70,150,lb(lang,'Double-stranded'),12)+t(70,166,lb(lang,'sugar phosphate'),12)+t(70,182,lb(lang,'deoxyribose'),12)+t(320,170,lb(lang,'Base pair'),12)
 r=' '.join(f'{650+50*math.sin(i/9):.1f},{70+i*2.4:.1f}' for i in range(120));s+=f'<polyline points="{r}" fill="none" stroke="#1e88e5" stroke-width="9" opacity=".8"/>'
 for k,p in enumerate('CGUCAGCG'):
  y=86+k*32;x=650+50*math.sin((y-70)/2.4/9);s+=f'<rect x="{x-30}" y="{y-5}" width="28" height="10" fill="{C[p]}"/>'+t(x-16,y+4,p,9)
 s+=t(520,110,lb(lang,'Single'),12)+t(520,126,lb(lang,'nucleobsae'),12)+t(780,150,lb(lang,'Single-stranded'),12)+t(780,166,lb(lang,'sugar phosphate'),12)+t(780,182,lb(lang,'ribose'),12)
 return s+'</svg>'
def chains(lang):
 s=F.start(400)+t(260,22,lb(lang,'RNA'),16,'#1a237e')+t(425,22,lb(lang,'and'),13)+t(600,22,lb(lang,'DNA'),16,'#1a237e')+t(425,40,lb(lang,'are chains of nucleotides'),12)
 def unit(x,y,base,flip=False,dark=False):
  d=-1 if flip else 1
  o=f'<circle cx="{x-24*d}" cy="{y-10}" r="9" fill="#111"/>'+t(x-24*d,y-6,'P',9,'#fff')
  pts=[(x,y-14),(x+12,y-5),(x+8,y+10),(x-8,y+10),(x-12,y-5)]
  o+='<polygon points="'+' '.join(f'{a:.0f},{b:.0f}' for a,b in pts)+f'" fill="{"#424242" if dark else "#9e9e9e"}" stroke="#222"/>'+t(x,y+4,'S',9,'#fff')
  o+=line(x+12*d,y-2,x+34*d,y-2)+f'<rect x="{x+34*d-(0 if d>0 else 22)}" y="{y-12}" width="22" height="20" fill="{"#90caf9" if base=="U" else "#fff"}" stroke="#222"/>'+t(x+45*d,y+3,base,11)
  return o
 for k,b in enumerate('AGUACG'):
  y=80+k*50;s+=unit(200,y,b)+(line(176,y+1,176,y+40) if k<5 else '')
 for k,(a,b) in enumerate((('A','T'),('G','C'),('T','A'),('A','T'),('C','G'),('G','C'))):
  y=80+k*50;s+=unit(540,y,a)+unit(720,y,b,True,True)+line(596,y-2,664,y-2,1.5,'#555','stroke-dasharray="2 3"')+(line(516,y+1,516,y+40)+line(744,y+1,744,y+40) if k<5 else '')
 s+='<polygon points="70,140 90,126 110,140 103,162 77,162" fill="none" stroke="#222"/>'+t(90,182,lb(lang,'Ribose'),11)+t(90,196,lb(lang,'(sugar)'),11)+F.arrow(115,180,150)
 s+='<polygon points="420,140 440,126 460,140 453,162 427,162" fill="none" stroke="#222"/>'+t(440,182,lb(lang,'Deoxyribose'),11)+t(440,196,lb(lang,'(sugar)'),11)+F.arrow(465,530,150)
 s+=t(820,90,lb(lang,'Hydrogen'),11)+t(820,104,lb(lang,'bonds'),11)+t(630,300,lb(lang,'Base pair'),11)
 s+=t(90,300,lb(lang,'Sugar-phospate backbone'),11)+t(780,392,lb(lang,'Sugar-phospate backbone'),11)
 s+='<rect x="160" y="320" width="100" height="44" fill="none" stroke="#c62828" stroke-width="2"/><rect x="500" y="320" width="100" height="44" fill="none" stroke="#c62828" stroke-width="2"/>'+t(380,360,lb(lang,'Nucleotide unit'),12)
 return s+'</svg>'

visual('chem12-figure21-7',helix)
add('Figure 21.7 Difference of DNA and RNA.','شکل 21.7 DNA اور RNA میں فرق۔','شکل 21.7 د DNA او RNA توپیر.')
add('21.5.2 Nucleic Acid Polymers','21.5.2 نیوکلک ایسڈ پولیمرز','21.5.2 د نیوکلیک اسید پولیمرونه','heading')
add('Nucleic acid polymers are DNA or RNA. The polymer DNA has ‘deoxyribo nucleotide’ as its monomer. While, polymer RNA has ‘ribo nucleotide’ as its monomers.','نیوکلک ایسڈ پولیمرز DNA یا RNA ہیں۔ پولیمر DNA کا مونومر ’ڈی آکسی رائبو نیوکلیوٹائیڈ‘ ہے۔ جبکہ پولیمر RNA کے مونومر ’رائبو نیوکلیوٹائیڈ‘ ہیں۔','د نیوکلیک اسید پولیمرونه DNA یا RNA دي. د DNA پولیمر مونومر ’ډی اکسي رایبو نیوکلیوټایډ‘ دی. په داسې حال کې چې د RNA پولیمر مونومرونه ’رایبو نیوکلیوټایډ‘ دي.')
visual('chem12-figure21-8',chains)
add('Figure 21.8 Structures of DNA and RNA polymer and nucleotide.','شکل 21.8 DNA اور RNA پولیمر اور نیوکلیوٹائیڈ کی ساختیں۔','شکل 21.8 د DNA او RNA پولیمر او نیوکلیوټایډ جوړښتونه.')
add('21.5.3 Storage of Genetic Information','21.5.3 جینیاتی معلومات کا ذخیرہ','21.5.3 د جنیټیکي معلوماتو زېرمه','heading')
add('DNA is the ultimate carrier of heredity in all the living organisms. Genes are composed of DNA, which contains genetic information in the form of codes. A sequence of three nitrogenous bases on DNA strands contains code for one amino acid synthesis of protein, which occurs inside ribosomes present in the cytoplasm of living cells.','DNA تمام جانداروں میں وراثت کا حتمی حامل ہے۔ جینز DNA سے بنے ہیں جس میں جینیاتی معلومات کوڈز کی صورت میں ہوتی ہیں۔ DNA لڑیوں پر تین نائٹروجنی اساسوں کی ترتیب پروٹین کی تالیف میں ایک امائنو ایسڈ کا کوڈ رکھتی ہے، جو زندہ خلیوں کے سائٹوپلازم میں موجود رائبوسومز کے اندر ہوتی ہے۔','DNA په ټولو ژوندیو موجوداتو کې د میراث وروستی وړونکی دی. جینونه له DNA جوړ دي چې جنیټیکي معلومات د کوډونو په بڼه لري. د DNA پر تارونو د دریو نایټروجني قلویاتو ترتیب د پروټین په جوړښت کې د یوه امینو اسید کوډ لري، چې د ژوندیو حجرو په سایټوپلازم کې د شته رایبوزومونو دننه ترسره کېږي.')
add('The information stored in the form of genes, which are parts of DNA, are transmitted to the cytoplasm in the form of messenger RNA or mRNA. There is another type of RNA called transfer RNA (tRNA), which reads out the message of mRNA and brings the amino acids to the ribosome in the form of amino acid tRNA complexes. Then these amino acids are incorporated into the peptide chain. This process is called translation.','جینز کی صورت میں ذخیرہ شدہ معلومات، جو DNA کے حصے ہیں، میسنجر RNA یا mRNA کی صورت میں سائٹوپلازم تک منتقل ہوتی ہیں۔ RNA کی ایک اور قسم ٹرانسفر RNA (tRNA) ہے جو mRNA کا پیغام پڑھتی ہے اور امائنو ایسڈز کو امائنو ایسڈ–tRNA کمپلیکس کی صورت میں رائبوسوم تک لاتی ہے۔ پھر یہ امائنو ایسڈز پیپٹائیڈ زنجیر میں شامل ہو جاتے ہیں۔ اس عمل کو ٹرانسلیشن کہتے ہیں۔','هغه معلومات چې د جینونو په بڼه زېرمه شوي، چې د DNA برخې دي، د میسنجر RNA یا mRNA په بڼه سایټوپلازم ته لېږدول کېږي. د RNA بل ډول ټرانسفر RNA (tRNA) دی چې د mRNA پیغام لولي او امینو اسیدونه د امینو اسید–tRNA کمپلېکسونو په بڼه رایبوزوم ته راوړي. بیا دا امینو اسیدونه په پېپټایډ ځنځیر کې شاملېږي. دې عملیې ته ټرانسلېشن وايي.')
add('21.6 Minerals of Biological Significance','21.6 حیاتیاتی اہمیت کی معدنیات','21.6 د بیولوژیکي اهمیت منرالونه','heading')
add('Minerals essential for life are the inorganic nutrients, they are needed by living organisms for vital functions but cannot be synthesized by them. The body needs many minerals; these are called essential minerals. These essential minerals include calcium, phosphorus, potassium, sulphur, sodium, chloride, magnesium, iron, zinc, copper, manganese, iodine, selenium, molybdenum, chromium and fluoride. Minerals play important roles in …','زندگی کے لیے ضروری معدنیات غیر نامیاتی غذائی اجزا ہیں جن کی جانداروں کو حیاتی افعال کے لیے ضرورت ہوتی ہے لیکن وہ انہیں خود نہیں بنا سکتے۔ جسم کو بہت سی معدنیات کی ضرورت ہوتی ہے؛ انہیں ضروری معدنیات کہتے ہیں۔ ان ضروری معدنیات میں کیلشیم، فاسفورس، پوٹاشیم، سلفر، سوڈیم، کلورائیڈ، میگنیشیم، لوہا، زنک، تانبا، مینگنیز، آیوڈین، سیلینیم، مولبڈینم، کرومیم اور فلورائیڈ شامل ہیں۔ معدنیات … میں اہم کردار ادا کرتی ہیں','د ژوند لپاره اړین منرالونه غیر عضوي غذايي مواد دي چې ژوندي موجودات یې د حیاتي دندو لپاره اړتیا لري خو پخپله یې نه شي جوړولی. بدن ډېرو منرالونو ته اړتیا لري؛ دې ته اړین منرالونه وايي. په دې اړینو منرالونو کې کلسیم، فاسفورس، پوتاشیم، سلفر، سوډیم، کلوراید، مګنیزیم، اوسپنه، جست، مس، منګنیز، ایوډین، سلینیم، مولیبډینم، کرومیم او فلوراید شامل دي. منرالونه په … کې مهم رول لوبوي')
record=section('21.15','DNA and RNA structures, storage of genetic information, minerals','DNA اور RNA کی ساختیں، جینیاتی معلومات کا ذخیرہ، معدنیات','د DNA او RNA جوړښتونه، د جنیټیکي معلوماتو زېرمه، منرالونه',paras,layout,blocks,'300–301')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':153,'printedPages':[300,301]}]
record['sourceContinuesOnPdfPage']=154
record['sourceIllustrationReview']='Figures 21.7–21.8 helix and nucleotide-chain artwork re-drawn as labelled schematic SVG; DNA/RNA table rows printed at the top of 300 are kept with the table in 21.14.'
carry=[{'from':'21.15','to':'21.16','startsAt':'maintaining blood pressure'}]
if __name__=='__main__':save(153,[record],carry=carry,chapter_number=21)
