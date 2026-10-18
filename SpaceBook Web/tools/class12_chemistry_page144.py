"""PDF144 printed282–283: Figure 21.2 protein structure levels, 21.2.3 properties, 21.2.4 importance of proteins."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow144');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Primary structure':('ابتدائی ساخت','لومړنی جوړښت'),'amino acid sequence':('امائنو ایسڈ ترتیب','د امینو اسید ترتیب'),'Alpha–helix':('الفا–ہیلکس','الفا–هیلېکس'),'β-pleated':('β-پلیٹیڈ','β-قات شوی'),'helix':('ہیلکس','هیلېکس'),
   'Secondary structure':('ثانوی ساخت','دویم جوړښت'),'regular sub-structures':('باقاعدہ ذیلی ساختیں','منظم فرعي جوړښتونه'),'Haemoglobin':('ہیموگلوبن','هیموګلوبین'),'Tertiary structure':('ثالثی ساخت','درېیم جوړښت'),
   'three–dimensional structure':('سہ جہتی ساخت','درې اړخیز جوړښت'),'(Attractions between alpha':('(الفا ہیلکس اور β-پلیٹیڈ','(د الفا هیلېکسونو او β-قات شویو'),'helixes and β-pleated sheets)':('شیٹس کے درمیان کشش)','پاڼو ترمنځ کشش)'),
   'Quaternary structure':('چہارمی ساخت','څلورم جوړښت'),'complex of protein molecules':('پروٹین سالمات کا کمپلیکس','د پروټین مالیکولونو کمپلېکس'),'(more than one amino acid chain)':('(ایک سے زیادہ امائنو ایسڈ زنجیر)','(له یوه ډېر امینو اسید ځنځیر)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def fig(lang):
 s=F.start(470)
 aa=['Asp','Arg','Ala','Gln','Glu','Phe','Gly','Asn','Ser','Tyr','Pro','Trp','Ile','Leu','Cys']
 cols=['#ef5350','#ef9a9a','#ff8a65','#ffb74d','#fff176','#aed581','#81c784','#4db6ac','#4fc3f7','#64b5f6','#9575cd','#ba68c8','#f06292','#a1887f','#90a4ae']
 pts=[(70,120),(90,96),(120,76),(160,62),(205,54),(250,52),(295,56),(335,66),(330,100),(290,108),(250,112),(210,116),(170,120),(130,124),(95,128)]
 s+=t(200,22,lb(lang,'Primary structure'),13,'#ad1457')+t(200,38,lb(lang,'amino acid sequence'),12)
 for (x,y),a,c in zip(pts,aa,cols):s+=f'<ellipse cx="{x}" cy="{y}" rx="20" ry="11" fill="{c}" stroke="#555"/>'+t(x,y+4,a,10)
 # helix
 hp=' '.join(f'{360+i*3:.0f},{110+10*math.sin(i*0.9):.1f}' for i in range(60))
 s+=f'<polyline points="{hp}" fill="none" stroke="#9e9d24" stroke-width="5"/>'+line(350,115,345,120,2)+t(450,145,lb(lang,'Alpha–helix'),12)
 s+='<path d="M110 230 L150 200 L170 215 L130 245 Z" fill="#cfd8dc" stroke="#555"/><path d="M140 180 L190 210 L180 225 L130 195 Z" fill="#cfd8dc" stroke="#555"/>'
 s+=t(70,220,lb(lang,'β-pleated'),12)+t(70,236,lb(lang,'helix'),12)+t(200,275,lb(lang,'Secondary structure'),13,'#ad1457')+t(200,291,lb(lang,'regular sub-structures'),12)
 # quaternary (haemoglobin): four coloured blobs
 for (x,y),c in zip(((120,360),(190,355),(130,420),(200,415)),('#e53935','#fb8c00','#43a047','#fdd835')):s+=f'<ellipse cx="{x}" cy="{y}" rx="45" ry="32" fill="{c}" opacity=".75" stroke="#333"/>'
 s+=t(160,318,lb(lang,'Haemoglobin'),12)+t(160,462,lb(lang,'Quaternary structure'),13,'#ad1457')
 s+=t(430,420,lb(lang,'complex of protein molecules'),12)+t(430,436,lb(lang,'(more than one amino acid chain)'),12)+line(250,425,350,425,1,'#888','stroke-dasharray="3 3"')
 # tertiary: helix + sheet arrows
 for k in range(3):
  hp=' '.join(f'{560+18*math.sin(i*0.9)+k*40:.1f},{280+i*3:.0f}' for i in range(30));s+=f'<polyline points="{hp}" fill="none" stroke="#{["8d6e63","f06292","616161"][k]}" stroke-width="4"/>'
 s+='<path d="M690 290 L720 270 L750 290 L735 290 L735 360 L705 360 L705 290 Z" fill="#c62828" opacity=".8"/>'
 s+=t(660,390,lb(lang,'Tertiary structure'),13,'#ad1457')+t(660,406,lb(lang,'three–dimensional structure'),12)+t(660,422,lb(lang,'(Attractions between alpha'),12)+t(660,438,lb(lang,'helixes and β-pleated sheets)'),12)
 return s+'</svg>'

visual('chem12-figure21-2',fig)
add('Figure 21.2 Different structure levels of proteins.','شکل 21.2 پروٹینز کی ساخت کی مختلف سطحیں۔','شکل 21.2 د پروټینونو د جوړښت بېلابېلې کچې.')
add('21.2.3 Properties','21.2.3 خصوصیات','21.2.3 ځانګړنې','heading')
add('Proteins are complex organic compounds. The physical and chemical properties of proteins are,','پروٹینز پیچیدہ نامیاتی مرکبات ہیں۔ پروٹینز کی طبعی اور کیمیائی خصوصیات یہ ہیں،','پروټینونه پېچلي عضوي مرکبات دي. د پروټینونو فزیکي او کیمیاوي ځانګړنې دا دي،')
add('1. Physical Properties of Proteins','1. پروٹینز کی طبعی خصوصیات','1. د پروټینونو فزیکي ځانګړنې','heading')
lines([('Proteins are colourless and usually tasteless.','پروٹینز بے رنگ اور عموماً بے ذائقہ ہوتے ہیں۔','پروټینونه بې رنګه او معمولاً بې خونده دي.'),
 ('The proteins range in shape from simple crystalloid spherical structures to long fibrillar structures. Two shapes have been recognized: (a). Globular proteins: They are spherical in shape. (b). Fibrillar proteins: They are in thread-like structure.','پروٹینز کی شکل سادہ قلمی کروی ساختوں سے لمبی ریشے دار ساختوں تک ہوتی ہے۔ دو شکلیں پہچانی گئی ہیں: (a). گلوبیولر پروٹینز: یہ کروی شکل کے ہوتے ہیں۔ (b). فائبرلر پروٹینز: یہ دھاگے جیسی ساخت میں ہوتے ہیں۔','د پروټینونو بڼه له ساده قلمي کروي جوړښتونو تر اوږدو ریښه لرونکو جوړښتونو پورې ده. دوه بڼې پېژندل شوې: (a). ګلوبولر پروټینونه: کروي بڼه لري. (b). فایبرلر پروټینونه: د تار په څېر جوړښت لري.'),
 ('The proteins generally have high molecular weights.','پروٹینز کے سالماتی وزن عموماً زیادہ ہوتے ہیں۔','پروټینونه عموماً لوړ مالیکولي وزنونه لري.'),
 ('Protein denaturation is the changes in the properties of a protein or loss of biologic activity.','پروٹین کی ڈی نیچریشن پروٹین کی خصوصیات میں تبدیلی یا حیاتیاتی سرگرمی کا ختم ہونا ہے۔','د پروټین ډینېچرېشن د پروټین په ځانګړنو کې بدلون یا د بیولوژیکي فعالیت له لاسه ورکول دي.'),
 ('Like amino acids, the proteins are amphoteric in nature because they contain both acidic (–COOH) and basic (amino) group.','امائنو ایسڈز کی طرح پروٹینز بھی ایمفوٹیرک ہیں کیونکہ ان میں تیزابی (–COOH) اور اساسی (امائنو) دونوں گروپ ہوتے ہیں۔','د امینو اسیدونو په څېر، پروټینونه امفوټېریک دي ځکه چې اسیدي (–COOH) او قلوي (امینو) دواړه ګروپونه لري.'),
 ('The solubility of proteins is influenced by pH.','پروٹینز کی حل پذیری pH سے متاثر ہوتی ہے۔','د پروټینونو حلېدنه د pH په واسطه اغېزمنه کېږي.'),
 ('All protein solutions rotate the plane of polarized light to the left, i.e., these are levorotatory.','پروٹین کے تمام محلول پولرائزڈ روشنی کی سطح کو بائیں جانب گھماتے ہیں، یعنی یہ لیوو روٹیٹری ہیں۔','د پروټین ټول محلولونه د پولرایز شوې رڼا سطحه کیڼ لور ته تاووي، یعنې لیوو روټېټري دي.')])
add('2. Chemical Properties of Proteins','2. پروٹینز کی کیمیائی خصوصیات','2. د پروټینونو کیمیاوي ځانګړنې','heading')
add('The chemical properties of proteins are,','پروٹینز کی کیمیائی خصوصیات یہ ہیں،','د پروټینونو کیمیاوي ځانګړنې دا دي،')
lines([('Hydrolysis: Proteins are hydrolysed by a variety of hydrolytic agents, such as acidic agents and basic (alkaline) agents.','ہائیڈرولائسز: پروٹینز مختلف ہائیڈرولائٹک عاملوں جیسے تیزابی عاملوں اور اساسی (القلی) عاملوں سے ہائیڈرولائز ہوتے ہیں۔','هایدرولایسس: پروټینونه د بېلابېلو هایدرولایټیک عاملونو لکه اسیدي عاملونو او قلوي عاملونو په واسطه هایدرولایز کېږي.'),
 ('They react with both acids and bases.','یہ تیزابوں اور اساسوں دونوں سے تعامل کرتے ہیں۔','دوی له اسیدونو او قلویاتو دواړو سره تعامل کوي.'),
 ('They can be precipitated from their solutions by salts of heavy metals, heat and alcohols etc.','انہیں بھاری دھاتوں کے نمکیات، حرارت اور الکوحلز وغیرہ سے ان کے محلولوں سے رسوب کی صورت میں الگ کیا جا سکتا ہے۔','دوی د درنو فلزاتو د مالګو، تودوخې او الکولونو او نورو په واسطه له خپلو محلولونو رسوب کېدای شي.'),
 ('When proteins are strongly heated or treated with certain reagents they lose their structural organization and their biological functions. This is known as coagulation of proteins.','جب پروٹینز کو زیادہ گرم کیا جائے یا بعض عاملوں سے عمل کیا جائے تو ان کی ساختی تنظیم اور حیاتیاتی افعال ختم ہو جاتے ہیں۔ اسے پروٹینز کا جمنا (کوایگولیشن) کہتے ہیں۔','کله چې پروټینونه ډېر تود شي یا له ځینو عاملونو سره عمل وشي، خپل جوړښتي تنظیم او بیولوژیکي دندې له لاسه ورکوي. دې ته د پروټینونو کلکېدل (کواګولېشن) وايي.')])
add('21.2.4 Importance of Proteins','21.2.4 پروٹینز کی اہمیت','21.2.4 د پروټینونو اهمیت','heading')
add('Proteins are the most significant biological compounds of living beings. They play an important role in many fundamental biological processes and functions. They are very versatile and have many different functions in the body. These are most critical to life and perform different types of functions. Some of these are,','پروٹینز جانداروں کے سب سے اہم حیاتیاتی مرکبات ہیں۔ یہ بہت سے بنیادی حیاتیاتی عمل اور افعال میں اہم کردار ادا کرتے ہیں۔ یہ بہت ہمہ جہت ہیں اور جسم میں ان کے بہت سے مختلف افعال ہیں۔ یہ زندگی کے لیے نہایت اہم ہیں اور مختلف اقسام کے افعال انجام دیتے ہیں۔ ان میں سے چند یہ ہیں،','پروټینونه د ژوندیو موجوداتو تر ټولو مهم بیولوژیکي مرکبات دي. په ډېرو بنسټیزو بیولوژیکي عملیو او دندو کې مهم رول لوبوي. ډېر هر اړخیز دي او په بدن کې ډېرې بېلابېلې دندې لري. دا د ژوند لپاره ډېر مهم دي او بېلابېل ډولونه دندې ترسره کوي. ځینې یې دا دي،')
lines([('Proteins are the most abundant intra-cellular macromolecules and form more than 50% of the dry weight of most organisms.','پروٹینز خلیے کے اندر سب سے زیادہ پائے جانے والے بڑے سالمات ہیں اور زیادہ تر جانداروں کے خشک وزن کا 50% سے زیادہ بناتے ہیں۔','پروټینونه د حجرې دننه تر ټولو ډېر موندل کېدونکي لوی مالیکولونه دي او د ډېری ژوندیو موجوداتو د وچ وزن له 50% ډېر جوړوي.'),
 ('Many of the proteins act as living catalysts called enzymes. Enzymes increase the rate of biological reactions to the extent required by the body.','بہت سے پروٹینز جاندار عمل انگیز کے طور پر کام کرتے ہیں جنہیں خامرے کہتے ہیں۔ خامرے حیاتیاتی تعاملات کی شرح کو جسم کی ضرورت کے مطابق بڑھاتے ہیں۔','ډېر پروټینونه د ژوندیو کتلستونو په توګه عمل کوي چې انزایمونه بلل کېږي. انزایمونه د بیولوژیکي تعاملونو کچه د بدن د اړتیا تر حده زیاتوي.'),
 ('They act as barrier such as skin and bacterial cell walls.','یہ رکاوٹ کے طور پر کام کرتے ہیں جیسے جلد اور بیکٹیریا کی خلوی دیواریں۔','دوی د خنډ په توګه عمل کوي لکه پوستکی او د باکتریاوو حجروي دېوالونه.'),
 ('They act as storage depots, such as ferritin for iron storage in blood.','یہ ذخیرہ گاہ کے طور پر کام کرتے ہیں، جیسے خون میں لوہے کے ذخیرے کے لیے فیریٹن۔','دوی د زېرمتونونو په توګه عمل کوي، لکه په وینه کې د اوسپنې د زېرمې لپاره فیریټین.'),
 ('The nucleoproteins act as carrier of genetic information or characters. They serve as basis of inheritance of heredity characters from parents to off springs (in the form of genes).','نیوکلیو پروٹینز جینیاتی معلومات یا خصوصیات کے حامل کے طور پر کام کرتے ہیں۔ یہ والدین سے اولاد میں موروثی خصوصیات کی منتقلی (جینز کی صورت میں) کی بنیاد ہیں۔','نیوکلیو پروټینونه د جنیټیکي معلوماتو یا ځانګړنو د وړونکو په توګه عمل کوي. دا له مور و پلار څخه اولاد ته د میراثي ځانګړنو د لېږد (د جینونو په بڼه) اساس دي.'),
 ('Hormones are proteins in nature. They regulate the growth of living organism and control a number of other physiological functions.','ہارمونز اپنی فطرت میں پروٹینز ہیں۔ یہ جاندار کی نشوونما کو منظم کرتے ہیں اور کئی دوسرے فعلیاتی افعال کو کنٹرول کرتے ہیں۔','هورمونونه په طبیعت کې پروټینونه دي. د ژوندي موجود وده تنظیموي او یو شمېر نورې فزیولوژیکي دندې کنټرولوي.'),
 ('Some proteins serve as carrier of different substances inside the body. For example, haemoglobin is a protein in red blood cells that acts as carrier of oxygen, ceruloplasmin, is a protein acts as carrier of copper in the blood plasma.','بعض پروٹینز جسم کے اندر مختلف مادوں کے حامل کے طور پر کام کرتے ہیں۔ مثلاً ہیموگلوبن سرخ خونی خلیوں میں ایک پروٹین ہے جو آکسیجن کا حامل ہے، سیرولوپلازمن ایک پروٹین ہے جو خون کے پلازما میں تانبے کا حامل ہے۔','ځینې پروټینونه په بدن کې د بېلابېلو موادو د وړونکو په توګه کار کوي. د بېلګې په توګه هیموګلوبین د وینې په سرو حجرو کې یو پروټین دی چې د اکسیجن وړونکی دی، سیرولوپلازمین یو پروټین دی چې د وینې په پلازما کې د مسو وړونکی دی.')])
record=section('21.6','Protein structure levels, properties and importance','پروٹین کی ساخت کی سطحیں، خصوصیات اور اہمیت','د پروټین د جوړښت کچې، ځانګړنې او اهمیت',paras,layout,blocks,'282–283')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':144,'printedPages':[282,283]}]
record['sourceContinuesOnPdfPage']=145
record['sourceIllustrationReview']='Figure 21.2 ribbon artwork re-drawn as labelled schematic SVG (amino-acid bead chain, alpha-helix, beta-sheet, tertiary fold, haemoglobin quaternary assembly).'
carry=[{'from':'21.6','to':'21.7','startsAt':'Some proteins contribute to the structure'}]
if __name__=='__main__':save(144,[record],carry=carry,chapter_number=21)
