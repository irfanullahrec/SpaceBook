"""PDF74 printed140–141: nomenclature of di- and polysubstituted benzene derivatives."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow74');t=F.t
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
# name: (urdu, pashto)
N={'benzaldehyde':('بینز الڈیہائیڈ','بنزالدیهاید'),'(benzenecarbaldehyde)':('(بینزین کاربالڈیہائیڈ)','(بنزین کاربالدیهاید)'),'benzoic acid':('بینزوئک ایسڈ','بنزویک اسید'),
 '(benzenecarboxylic acid)':('(بینزین کاربوکسیلک ایسڈ)','(بنزین کاربوکسیلیک اسید)'),'o-dibromobenzene':('o-ڈائی برومو بینزین','o-ډای بروموبنزین'),'(1,2-dibromobenzene)':('(1،2-ڈائی برومو بینزین)','(1،2-ډای بروموبنزین)'),
 'm-dibromobenzene':('m-ڈائی برومو بینزین','m-ډای بروموبنزین'),'(1,3-dibromobenzene)':('(1،3-ڈائی برومو بینزین)','(1،3-ډای بروموبنزین)'),'p-dibromobenzene':('p-ڈائی برومو بینزین','p-ډای بروموبنزین'),
 '(1,4-dibromobenzene)':('(1،4-ڈائی برومو بینزین)','(1،4-ډای بروموبنزین)'),'o-bromochlorobenzene':('o-برومو کلورو بینزین','o-بروموکلوروبنزین'),'(1-bromo-2-chlorobenzene)':('(1-برومو-2-کلورو بینزین)','(1-برومو-2-کلوروبنزین)'),
 'm-bromonitrobenzene':('m-برومو نائٹرو بینزین','m-برومونایټروبنزین'),'(1-bromo-3-nitrobenzene)':('(1-برومو-3-نائٹرو بینزین)','(1-برومو-3-نایټروبنزین)'),'o-chloropnenol':('o-کلورو فینول','o-کلوروفینول'),
 '(2-chlorophenol)':('(2-کلورو فینول)','(2-کلوروفینول)'),'m-nitroaniline':('m-نائٹرو اینیلین','m-نایټروانیلین'),'(3-nitroaniline)':('(3-نائٹرو اینیلین)','(3-نایټروانیلین)'),
 'o-xylene':('o-زائلین','o-زایلین'),'(1,2-dimethylbenzene)':('(1،2-ڈائی میتھائل بینزین)','(1،2-ډای میتایل بنزین)'),'m-xylene':('m-زائلین','m-زایلین'),'(1,3-dimethylbenzene)':('(1،3-ڈائی میتھائل بینزین)','(1،3-ډای میتایل بنزین)'),
 'p-xylene':('p-زائلین','p-زایلین'),'(1,4-dimethylbenzene)':('(1،4-ڈائی میتھائل بینزین)','(1،4-ډای میتایل بنزین)'),'o-cresol':('o-کریسول','o-کریسول'),'(2-methylphenol)':('(2-میتھائل فینول)','(2-میتایل فینول)'),
 'm-cresol':('m-کریسول','m-کریسول'),'(3-methylphenol)':('(3-میتھائل فینول)','(3-میتایل فینول)'),'p-cresol':('p-کریسول','p-کریسول'),'(4-methylphenol)':('(4-میتھائل فینول)','(4-میتایل فینول)'),
 '1,2,3-trichlorobenzene':('1،2،3-ٹرائی کلورو بینزین','1،2،3-ټرای کلوروبنزین'),'1,3,5-tribromobenzene':('1،3،5-ٹرائی برومو بینزین','1،3،5-ټرای بروموبنزین'),
 '1-bromo-2-chloro-3-fluorobenzene':('1-برومو-2-کلورو-3-فلورو بینزین','1-برومو-2-کلورو-3-فلوروبنزین'),'1-bromo-3-chloro-5-nitrobenzene':('1-برومو-3-کلورو-5-نائٹرو بینزین','1-برومو-3-کلورو-5-نایټروبنزین'),
 '2-chloro-3-fluorophenol':('2-کلورو-3-فلورو فینول','2-کلورو-3-فلوروفینول'),'2,4,6-trinitrotoluene (TNT)':('2،4،6-ٹرائی نائٹرو ٹولوئین (TNT)','2،4،6-ټرای نایټروتولوین (TNT)'),
 'mesitylene':('میسیٹیلین','میسیټیلین'),'(1,3,5-trimethylbenzene)':('(1،3،5-ٹرائی میتھائل بینزین)','(1،3،5-ټرای میتایل بنزین)'),'durene':('ڈیورین','ډیورین'),
 '(1,2,4,5-tetramethylbenzene)':('(1،2،4،5-ٹیٹرا میتھائل بینزین)','(1،2،4،5-ټیټرا میتایل بنزین)'),'picric acid':('پکرک ایسڈ','پکریک اسید'),'(2,4,6-trinitrophenol)':('(2،4،6-ٹرائی نائٹرو فینول)','(2،4،6-ټرای نایټروفینول)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def grid(items,lang,height=175,y=78,r=32):
 height+=22 if any(3 in it[0] for it in items) else 0
 s=F.start(height);n=len(items)
 for k,(subs,name,sysn,nums) in enumerate(items):
  x=850*(k+.5)/n;s+=F.ring(x,y,r,subs=subs)
  for v,lab in (nums or {}).items():
   ang=math.radians(60*v);s+=t(x+r*.62*math.sin(ang),y-r*.62*math.cos(ang)+4,lab,10,'#555')
  d=22 if 3 in subs else 0
  s+=t(x,y+r+40+d,lb(lang,name),14)+(t(x,y+r+57+d,lb(lang,sysn),13) if sysn else '')
 return s+'</svg>'
def seq(*ks):return {k:str(i+1) for i,k in enumerate(ks)}
G={'carbonyl':[({0:'CHO'},'benzaldehyde','(benzenecarbaldehyde)',None),({0:'COOH'},'benzoic acid','(benzenecarboxylic acid)',None)],
 'dibromo':[({0:'Br',1:'Br'},'o-dibromobenzene','(1,2-dibromobenzene)',seq(0,1)),({0:'Br',2:'Br'},'m-dibromobenzene','(1,3-dibromobenzene)',seq(0,1,2)),({0:'Br',3:'Br'},'p-dibromobenzene','(1,4-dibromobenzene)',seq(0,1,2,3))],
 'mixed':[({0:'Br',1:'Cl'},'o-bromochlorobenzene','(1-bromo-2-chlorobenzene)',seq(0,1)),({0:'NO₂',2:'Br'},'m-bromonitrobenzene','(1-bromo-3-nitrobenzene)',seq(2,1,0)),
          ({0:'OH',1:'Cl'},'o-chloropnenol','(2-chlorophenol)',seq(0,1)),({0:'NH₂',2:'NO₂'},'m-nitroaniline','(3-nitroaniline)',seq(0,1,2))],
 'xylene':[({0:'CH₃',1:'CH₃'},'o-xylene','(1,2-dimethylbenzene)',seq(0,1)),({0:'CH₃',2:'CH₃'},'m-xylene','(1,3-dimethylbenzene)',seq(0,1,2)),({0:'CH₃',3:'CH₃'},'p-xylene','(1,4-dimethylbenzene)',seq(0,1,2,3))],
 'cresol':[({0:'OH',1:'CH₃'},'o-cresol','(2-methylphenol)',seq(0,1)),({0:'OH',2:'CH₃'},'m-cresol','(3-methylphenol)',seq(0,1,2)),({0:'OH',3:'CH₃'},'p-cresol','(4-methylphenol)',seq(0,1,2,3))],
 'poly1':[({0:'Cl',1:'Cl',2:'Cl'},'1,2,3-trichlorobenzene',None,seq(0,1,2)),({0:'Br',2:'Br',4:'Br'},'1,3,5-tribromobenzene',None,seq(0,1,2,3,4)),({0:'Br',1:'Cl',2:'F'},'1-bromo-2-chloro-3-fluorobenzene',None,seq(0,1,2))],
 'poly2':[({0:'NO₂',4:'Cl',2:'Br'},'1-bromo-3-chloro-5-nitrobenzene',None,{2:'1',3:'2',4:'3',5:'4',0:'5',1:'6'}),({0:'OH',1:'Cl',2:'F'},'2-chloro-3-fluorophenol',None,seq(0,1,2)),
          ({0:'CH₃',1:'NO₂',3:'NO₂',5:'O₂N'},'2,4,6-trinitrotoluene (TNT)',None,seq(0,1,2,3,4,5))],
 'special':[({0:'CH₃',2:'CH₃',4:'H₃C'},'mesitylene','(1,3,5-trimethylbenzene)',seq(0,1,2,3,4,5)),({1:'CH₃',2:'CH₃',4:'H₃C',5:'H₃C'},'durene','(1,2,4,5-tetramethylbenzene)',{1:'1',2:'2',3:'3',4:'4',5:'5',0:'6'}),
            ({0:'OH',1:'NO₂',3:'NO₂',5:'O₂N'},'picric acid','(2,4,6-trinitrophenol)',seq(0,1,2,3,4,5))]}

visual('chem12-p74-carbonyl-names',lambda l:grid(G['carbonyl'],l))
add('ii. In disubstituted benzene derivatives, the relative position of substituents in 1,2-, 1,3- and 1,4-disubsituted can be represented prefixes ortho (o-), meta (m-) and para (p-) respectively. For similar substituents, the prefix di- is also used before the name of the substituents. For example',
 'ii. دو متبادل بینزین مشتقات میں 1،2-، 1،3- اور 1،4-دو متبادل میں متبادلات کی نسبتی جگہ کو بالترتیب سابقوں اورتھو (o-)، میٹا (m-) اور پیرا (p-) سے ظاہر کیا جا سکتا ہے۔ یکساں متبادلات کے لیے متبادلات کے نام سے پہلے سابقہ di- بھی استعمال ہوتا ہے۔ مثلاً',
 'ii. په دوه بدیلي بنزیني مشتقاتو کې د 1،2-، 1،3- او 1،4-دوه بدیلي مرکباتو د بدیلونو نسبي موقعیت په ترتیب سره د اورتو (o-)، میټا (m-) او پارا (p-) مختاړو په واسطه ښودل کېدای شي. د ورته بدیلونو لپاره د بدیلونو له نوم مخکې di- مختاړی هم کارېږي. د بېلګې په توګه')
visual('chem12-p74-dibromobenzenes',lambda l:grid(G['dibromo'],l,195,85))
add('If the substituents are different, they are named in alphabatical order. If one of the substituent is such that it gives special name to the molecule then the special name is used as the parent name. The other substituent, along with its position, is named before the parent name.',
 'اگر متبادلات مختلف ہوں تو ان کے نام حروفِ تہجی کی ترتیب سے رکھے جاتے ہیں۔ اگر کوئی متبادل ایسا ہو جو سالمے کو خاص نام دیتا ہو تو خاص نام کو بنیادی نام کے طور پر استعمال کیا جاتا ہے۔ دوسرے متبادل کا نام اس کی جگہ سمیت بنیادی نام سے پہلے رکھا جاتا ہے۔',
 'که بدیلونه سره بېل وي، د الفبا په ترتیب نومول کېږي. که یو بدیل داسې وي چې مالیکول ته ځانګړی نوم ورکوي، نو ځانګړی نوم د اصلي نوم په توګه کارېږي. بل بدیل له خپل موقعیت سره له اصلي نوم مخکې نومول کېږي.')
visual('chem12-p74-mixed-disubstituted',lambda l:grid(G['mixed'],l,195,85))
add('Some disubstituted benzene derivatives are given special names. For example;','بعض دو متبادل بینزین مشتقات کو خاص نام دیے گئے ہیں۔ مثلاً؛','ځینو دوه بدیلي بنزیني مشتقاتو ته ځانګړي نومونه ورکړل شوي. د بېلګې په توګه؛')
visual('chem12-p74-xylenes',lambda l:grid(G['xylene'],l,195,85))
visual('chem12-p74-cresols',lambda l:grid(G['cresol'],l,195,85))
add('iii. Polysubstituted benzene derivatives, are named similarly to disubsituted derivatives.','iii. کثیر متبادل بینزین مشتقات کے نام دو متبادل مشتقات کی طرح رکھے جاتے ہیں۔','iii. څو بدیلي بنزیني مشتقات د دوه بدیلي مشتقاتو په څېر نومول کېږي.')
for e,u,p in [('For similar atoms/groups the prefix tri-, tetra- etc. are used before the substituents.','یکساں ایٹموں/گروپوں کے لیے متبادلات سے پہلے سابقے tri-، tetra- وغیرہ استعمال ہوتے ہیں۔','د ورته اټومونو/ګروپونو لپاره له بدیلونو مخکې tri-، tetra- او نور مختاړي کارېږي.'),
 ('If different groups attached, they are named in alphabetical order.','اگر مختلف گروپ جڑے ہوں تو ان کے نام حروفِ تہجی کی ترتیب سے رکھے جاتے ہیں۔','که بېل ګروپونه تړلي وي، د الفبا په ترتیب نومول کېږي.'),
 ('To indicate the position of the substituents, the ring is numbered in such a way that all the numbers used in the name give the lowest sum. If a substituent gives special name, it should be considered at position-1, and the special name is the parent name of molecule. For example;','متبادلات کی جگہ ظاہر کرنے کے لیے حلقے کو اس طرح نمبر دیے جاتے ہیں کہ نام میں استعمال ہونے والے تمام نمبروں کا مجموعہ کم سے کم ہو۔ اگر کوئی متبادل خاص نام دیتا ہو تو اسے مقام-1 پر سمجھا جائے، اور خاص نام سالمے کا بنیادی نام ہوتا ہے۔ مثلاً؛','د بدیلونو د موقعیت د ښودلو لپاره کړۍ داسې شمېرل کېږي چې په نوم کې د کارول شویو ټولو شمېرو مجموعه تر ټولو کمه وي. که یو بدیل ځانګړی نوم ورکوي، باید په موقعیت-1 کې وګڼل شي، او ځانګړی نوم د مالیکول اصلي نوم دی. د بېلګې په توګه؛')]:
 add(e,u,p,'list')
visual('chem12-p74-polysubstituted-1',lambda l:grid(G['poly1'],l,185,85))
visual('chem12-p74-polysubstituted-2',lambda l:grid(G['poly2'],l,185,85))
add('Some polysubstituted benzene derivatives have been assigned special names. Few examples are given below. Their systematic names are given in parenthesis.',
 'بعض کثیر متبادل بینزین مشتقات کو خاص نام دیے گئے ہیں۔ چند مثالیں درج ذیل ہیں۔ ان کے نظامی نام قوسین میں دیے گئے ہیں۔',
 'ځینو څو بدیلي بنزیني مشتقاتو ته ځانګړي نومونه ورکړل شوي. څو بېلګې لاندې ورکړل شوې. سیستماتیک نومونه یې په قوسونو کې ورکړل شوي.')
visual('chem12-p74-special-polysubstituted',lambda l:grid(G['special'],l,200,85))

record=section('16.21','Nomenclature of di- and polysubstituted benzenes','دو اور کثیر متبادل بینزینز کی نام گذاری','د دوه او څو بدیلي بنزینونو نومول',paras,layout,blocks,'140–141')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':74,'printedPages':[140,141]}]
record['sourceContinuesOnPdfPage']=75
issues=[{'id':'chem12-p140-printed-spellings','printedPage':140,'description':'Printed "disubsituted", "alphabatical" and "o-chloropnenol" retained in English as in source; ring position numbers follow the printed figures.'}]
carry=[{'from':'16.21','to':'16.22','startsAt':'Polycyclic aromatic hydrocarbons also'}]
if __name__=='__main__':save(74,[record],carry=carry,issues=issues,chapter_number=16)
