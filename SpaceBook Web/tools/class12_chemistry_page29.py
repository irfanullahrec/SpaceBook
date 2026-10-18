"""PDF29 printed50–51, configurations, unpaired electrons and binding energy."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
def table(b):blocks.append(b);layout.append({'type':'sourceDataTable','tableId':b['id']})
add('Table 14.1 Electronic Configuration of Three Series of d – block Elements','جدول 14.1 d بلاک کے عناصر کے تین سلسلوں کی الیکٹرونی ترتیب','جدول 14.1 د d بلاک د عناصرو د دریو لړیو الکتروني ترتیب')
first=[('₂₁Sc',2,1),('₂₂Ti',2,2),('₂₃V',2,3),('₂₄Cr',1,5),('₂₅Mn',2,5),('₂₆Fe',2,6),('₂₇Co',2,7),('₂₈Ni',2,8),('₂₉Cu',1,10),('₃₀Zn',2,10)]
second=[('₃₉Y',2,1),('₄₀Zr',2,2),('₄₁Nb',1,4),('₄₂Mo',1,5),('₄₃Tc',2,5),('₄₄Ru',1,7),('₄₅Rh',1,8),('₄₆Pd',0,10),('₄₇Ag',1,10),('₄₈Cd',2,10)]
third=[('₅₇La',2,1),('₇₂Hf',2,2),('₇₃Ta',2,3),('₇₄W',2,4),('₇₅Re',2,5),('₇₆Os',2,6),('₇₇Ir',2,7),('₇₈Pt',1,9),('₇₉Au',1,10),('₈₀Hg',2,10)]
sup=str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹')
def ex(n):return str(n).translate(sup)
rows=[]
for a,b,c in zip(first,second,third):
    rows.append([a[0],f'[Ar]4s{ex(a[1])},3d{ex(a[2])}',b[0],f'[Kr]5s{ex(b[1])},4d{ex(b[2])}',c[0],f'[Xe]6s{ex(c[1])},'+('' if c[0]=='₅₇La' else '4f¹⁴, ')+f'5d{ex(c[2])}'])
headers=['3d-elements: Elements','Electronic configuration','4d-elements: Elements','Electronic configuration','5d-elements: Elements','Electronic configuration']
table({'id':'chem12-table-14-1','headers':headers,'rows':rows,'translations':[{'language':'اردو','headers':['3d عناصر: عناصر','الیکٹرونی ترتیب','4d عناصر: عناصر','الیکٹرونی ترتیب','5d عناصر: عناصر','الیکٹرونی ترتیب'],'rows':rows},{'language':'پښتو','headers':['3d عناصر: عناصر','الکتروني ترتیب','4d عناصر: عناصر','الکتروني ترتیب','5d عناصر: عناصر','الکتروني ترتیب'],'rows':rows}]})
add('In the lanthanide and actinide series valence shell electrons go to ‘4f’ and ‘5f’ orbitals respectively.',
    'لینتھنائیڈ اور ایکٹینائیڈ سلسلوں میں ظرفی خول کے الیکٹرون بالترتیب 4f اور 5f آربیٹلز میں جاتے ہیں۔',
    'په لانتانایډ او اکتینایډ لړیو کې د ظرفي پوښ الکترونونه په ترتیب سره 4f او 5f اوربیټلونو ته ځي.')
head('14.1.3 Binding Energy','14.1.3 بندشی توانائی','14.1.3 د تړلو انرژي')
add('Transition metals are generally tough having great mechanical strength due to strong metallic bonding. This is because, apart from ‘s’ electrons of the outermost shell, the unpaired electrons of underlying d-orbitals also participate in binding to form metallic bonds.',
    'عبوری دھاتیں عموماً مضبوط ہوتی ہیں اور مضبوط دھاتی بندوں کی وجہ سے بڑی میکانی طاقت رکھتی ہیں۔ اس کی وجہ یہ ہے کہ بیرونی ترین خول کے s الیکٹرونوں کے علاوہ اندر کے d آربیٹلز کے غیر جوڑا الیکٹرون بھی دھاتی بند بنانے میں حصہ لیتے ہیں۔',
    'انتقالي فلزونه عموماً ټینګ وي او د پیاوړي فلزي تړون له امله ډېر میخانیکي ځواک لري. دا ځکه چې د بهرني پوښ د s الکترونونو ترڅنګ د لاندې d اوربیټلونو بې جوړې الکترونونه هم د فلزي تړونونو په جوړولو کې برخه اخلي.')
add('In moving from left to right in any transition series, the number of unpaired electrons increases up to Group – VB and VIB, after that pairing takes place and the number of unpaired electrons goes on decreasing until it becomes zero at Group – IIB.',
    'کسی عبوری سلسلے میں بائیں سے دائیں جانے پر غیر جوڑا الیکٹرونوں کی تعداد گروپ VB اور VIB تک بڑھتی ہے؛ پھر جوڑے بنتے ہیں اور غیر جوڑا الیکٹرونوں کی تعداد کم ہوتے ہوئے گروپ IIB میں صفر ہو جاتی ہے۔',
    'په هره انتقالي لړۍ کې له کیڼ څخه ښي ته په تګ د بې جوړې الکترونونو شمېر تر VB او VIB ګروپونو پورې زیاتېږي؛ بیا جوړې جوړېږي او د بې جوړې الکترونونو شمېر کمېږي تر څو په IIB ګروپ کې صفر شي.')
left=section('14.3','Transition-series configurations and binding energy','عبوری سلسلوں کی ترتیبیں اور بندشی توانائی','د انتقالي لړیو ترتیبونه او د تړلو انرژي',paras,layout,blocks,'50');left['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':29,'printedPage':50}]
paras=[];layout=[];blocks=[]
add('Table 14.2 No. of Unpaired Electrons in the 1ˢᵗ Transition Series','جدول 14.2 پہلے عبوری سلسلے میں غیر جوڑا الیکٹرونوں کی تعداد','جدول 14.2 په لومړۍ انتقالي لړۍ کې د بې جوړې الکترونونو شمېر')
ions=['Sc³⁺','Ti³⁺','V³⁺','Cr³⁺','Mn³⁺','Mn²⁺, Fe³⁺','Fe²⁺','Co²⁺','Ni²⁺','Cu²⁺','Zn²⁺'];counts=[0,1,2,3,4,5,4,3,2,1,0]
rows=[]
for electrons,(ion,count) in enumerate(zip(ions,counts)):
    occupancy=([1]*electrons) if electrons<=5 else [2]*(electrons-5)+[1]*(10-electrons)
    rows.append([ion,' '.join('[↑↓]' if n==2 else '[↑]' for n in occupancy),str(count)])
table({'id':'chem12-table-14-2','headers':['Elements','3d orbital electronic structure','No. of unpaired electrons'],'rows':rows,'translations':[{'language':'اردو','headers':['عناصر','3d آربیٹل کی الیکٹرونی ساخت','غیر جوڑا الیکٹرونوں کی تعداد'],'rows':rows},{'language':'پښتو','headers':['عناصر','د 3d اوربیټل الکتروني جوړښت','د بې جوړې الکترونونو شمېر'],'rows':rows}]})
add('Therefore, binding energy increases upto Group –VIB and then progressively decreases upto Group – IIB. For example, in 3d transition series binding energy increases upto vanadium and then decrease upto zinc.',
    'اس لیے بندشی توانائی گروپ VIB تک بڑھتی اور پھر بتدریج گروپ IIB تک کم ہوتی ہے۔ مثلاً 3d عبوری سلسلے میں بندشی توانائی وینیڈیم تک بڑھتی اور پھر زنک تک کم ہوتی ہے۔',
    'نو د تړلو انرژي تر VIB ګروپ پورې زیاتېږي او بیا ورو ورو تر IIB ګروپ پورې کمېږي. د بېلګې په توګه په 3d انتقالي لړۍ کې د تړلو انرژي تر وانادیم پورې زیاتېږي او بیا تر زنک پورې کمېږي.')
head('14.1.4 Variable Oxidation States','14.1.4 متغیر تکسیدی حالتیں','14.1.4 بدلېدونکي د اکسیدېشن حالتونه')
add('Most of the transition metals show variable oxidation states and form compounds showing more than one (variable) oxidation states because energy levels of ns and (n–1)d are very close. The involvement of the d-electrons in addition to ‘ns’ electrons in bond formation also take place. The oxidation state of 3d series is from +2 to +7 (except Cr and Cu).',
    'زیادہ تر عبوری دھاتیں متغیر تکسیدی حالتیں اور ایک سے زیادہ تکسیدی حالتوں والے مرکبات بناتی ہیں، کیونکہ ns اور (n–1)d کی توانائی کی سطحیں بہت قریب ہیں۔ بند بنانے میں ns الیکٹرونوں کے علاوہ d الیکٹرون بھی حصہ لیتے ہیں۔ 3d سلسلے کی تکسیدی حالت +2 سے +7 تک ہے (Cr اور Cu کے سوا)۔',
    'ډېری انتقالي فلزونه بدلېدونکي د اکسیدېشن حالتونه ښيي او له یوه څخه د ډېرو حالتونو لرونکي مرکبات جوړوي، ځکه د ns او (n–1)d د انرژۍ کچې ډېرې نږدې دي. د تړون په جوړولو کې د ns الکترونونو ترڅنګ d الکترونونه هم برخه اخلي. د 3d لړۍ د اکسیدېشن حالت له +2 څخه تر +7 پورې دی (له Cr او Cu پرته).')
head('Tidbit','مختصر معلومات','لنډ معلومات')
head('Valency','ظرف','ظرفیت')
add('The combining capacity of an atom is known as its valency.','ایٹم کی ملاپ کی صلاحیت اس کا ظرف کہلاتی ہے۔','د اټوم د یوځای کېدو وړتیا د هغه ظرفیت بلل کېږي.')
head('Variable Valency','متغیر ظرف','بدلېدونکی ظرفیت')
add('Some elements differ in their capacity to combine with other elements depending on the nature of the reaction; this property is called variable valency. For example, the iron in ferrous oxide shows a valency of +2, whereas in ferric oxide, it has a valency of +3.',
    'بعض عناصر کی دوسرے عناصر سے ملنے کی صلاحیت تعامل کی نوعیت کے مطابق مختلف ہوتی ہے؛ اسے متغیر ظرف کہتے ہیں۔ مثلاً فیرس آکسائیڈ میں لوہا +2 ظرف، جبکہ فیرک آکسائیڈ میں +3 ظرف دکھاتا ہے۔',
    'د ځینو عناصرو له نورو عناصرو سره د یوځای کېدو وړتیا د تعامل د ماهیت له مخې توپیر کوي؛ دا ځانګړنه بدلېدونکی ظرفیت بلل کېږي. د بېلګې په توګه په فېرس اکسایډ کې اوسپنه +2 ظرفیت ښيي، خو په فېرېک اکسایډ کې +3 ظرفیت لري.')
right=section('14.4','Unpaired electrons and variable oxidation states','غیر جوڑا الیکٹرون اور متغیر تکسیدی حالتیں','بې جوړې الکترونونه او بدلېدونکي د اکسیدېشن حالتونه',paras,layout,blocks,'51');right['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':29,'printedPage':51}]
issues=[{'id':'chem12-p51-binding-group','printedPage':51,'description':'Binding-energy prose names GroupVIB and gives vanadium as example maximum. Printed group and example are retained.'}]
if __name__=='__main__':save(29,[left,right],trim=[{'id':'14.5','startsAt':'The lowest oxidation states'}],issues=issues,chapter_number=14)
