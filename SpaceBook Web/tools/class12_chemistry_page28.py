"""PDF28 printed48–49: transition features and electronic configurations."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
import html
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
add('Elements from caesium (atomic number 58) to lutetium (atomic number 71) make first series of f – block elements known as lanthanides. In this series of 14 metallic elements, 4f subshell are progressively filled. Elements from thorium (atomic number 90) to lawrencium (atomic number 103) make the second series of f – block elements, the actinides, in which the 5f subshell is progressively filled. The lanthanides and actinides together comprise the f-block elements, or inner transition elements.',
    'سیزیم (ایٹمی نمبر 58) سے لیوٹیشیئم (ایٹمی نمبر 71) تک عناصر f بلاک کا پہلا سلسلہ، لینتھنائیڈز، بناتے ہیں۔ 14 دھاتی عناصر کے اس سلسلے میں 4f ذیلی خول بتدریج بھرتے ہیں۔ تھوریئم (ایٹمی نمبر 90) سے لارینسیئم (ایٹمی نمبر 103) تک عناصر f بلاک کا دوسرا سلسلہ، ایکٹینائیڈز، بناتے ہیں، جس میں 5f ذیلی خول بتدریج بھرتا ہے۔ لینتھنائیڈز اور ایکٹینائیڈز مل کر f بلاک یا اندرونی عبوری عناصر بناتے ہیں۔',
    'له سیزیم (اټومي شمېره 58) څخه تر لوتېشیم (اټومي شمېره 71) پورې عناصر د f بلاک لومړۍ لړۍ، لانتانایډونه، جوړوي. د 14 فلزي عناصرو په دې لړۍ کې 4f فرعي پوښونه ورو ورو ډکېږي. له توریوم (اټومي شمېره 90) څخه تر لارنسیم (اټومي شمېره 103) پورې عناصر د f بلاک دویمه لړۍ، اکتینایډونه، جوړوي، چې پکې 5f فرعي پوښ ورو ورو ډکېږي. لانتانایډونه او اکتینایډونه په ګډه د f بلاک عناصر یا داخلي انتقالي عناصر جوړوي.')
head('Tidbit','مختصر معلومات','لنډ معلومات')
head('Typical and Non-Typical Transition Elements','عام اور غیر عام عبوری عناصر','عادي او غیر عادي انتقالي عناصر')
add('Group IIB Elements (Zn, Cd and Hg) do not have a partially filled d-subshell either as elements or in any of their ionic state. Neither do they show typical properties of transition elements to any appreciable extent (except complex formation).',
    'گروپ IIB کے عناصر (Zn، Cd اور Hg) نہ عنصری حالت میں، نہ اپنی کسی آئنک حالت میں جزوی بھرا d ذیلی خول رکھتے ہیں۔ نہ ہی یہ عبوری عناصر کی عام خصوصیات نمایاں حد تک دکھاتے ہیں (کمپلیکس بنانے کے سوا)۔',
    'د IIB ګروپ عناصر (Zn، Cd او Hg) نه د عناصرو په توګه او نه په کوم ایوني حالت کې تر یوه حده ډک d فرعي پوښ لري. هغوی د انتقالي عناصرو عادي ځانګړنې هم په څرګنده کچه نه ښيي (د کمپلېکس جوړولو پرته).')
add('Similarly, IIIB (Sc, Y and La) is another group of elements, which do not show many of the properties associated with typical transition elements.',
    'اسی طرح IIIB (Sc، Y اور La) عناصر کا ایک اور گروپ ہے جو عام عبوری عناصر سے متعلق کئی خصوصیات نہیں دکھاتا۔',
    'همدا ډول IIIB (Sc، Y او La) د عناصرو بل ګروپ دی چې له عادي انتقالي عناصرو سره تړلې ډېرې ځانګړنې نه ښيي.')
add('In order to maintain a rational classification, the elements of group IIB and group IIIB are referred to as Non-Typical Transition Elements and the elements in the remaining transition series are called Typical Transition Elements.',
    'معقول درجہ بندی برقرار رکھنے کے لیے گروپ IIB اور IIIB کے عناصر کو غیر عام عبوری عناصر اور باقی عبوری سلسلے کے عناصر کو عام عبوری عناصر کہتے ہیں۔',
    'د معقولې ډلبندۍ د ساتلو لپاره د IIB او IIIB ګروپونو عناصر غیر عادي انتقالي عناصر او د پاتې انتقالي لړۍ عناصر عادي انتقالي عناصر بلل کېږي.')
add('In previous unit, you have studied the s-block and p-block elements. In this unit, you will study the d-block elements, their general features, coordination compounds and chemistry of some important transition elements in detail. The transition elements, for the sake of convenience, are divided into two main categories.',
    'پچھلے یونٹ میں آپ s بلاک اور p بلاک کے عناصر پڑھ چکے ہیں۔ اس یونٹ میں d بلاک کے عناصر، ان کی عمومی خصوصیات، تناسقی مرکبات اور بعض اہم عبوری عناصر کی کیمیا تفصیل سے پڑھیں گے۔ سہولت کے لیے عبوری عناصر دو اہم قسموں میں تقسیم کیے جاتے ہیں۔',
    'په تېر واحد کې مو د s بلاک او p بلاک عناصر لوستي دي. په دې واحد کې به د d بلاک عناصر، د هغوی عمومي ځانګړنې، کواردینېشن مرکبات او د ځینو مهمو انتقالي عناصرو کیمیا په تفصیل ولولئ. د اسانتیا لپاره انتقالي عناصر په دوو اصلي ډلو وېشل کېږي.')
add('i. the main transition elements or the ‘d’ block elements','i. مرکزی عبوری عناصر یا d بلاک کے عناصر','i. اصلي انتقالي عناصر یا د d بلاک عناصر','list')
add('ii. the ‘f’ block elements (inner transition elements)','ii. f بلاک کے عناصر (اندرونی عبوری عناصر)','ii. د f بلاک عناصر (داخلي انتقالي عناصر)','list')
add('Here, we will discuss the main transition elements or the ‘d’ block elements only.','یہاں صرف مرکزی عبوری عناصر یا d بلاک کے عناصر پر بحث کریں گے۔','دلته به یوازې اصلي انتقالي عناصر یا د d بلاک عناصر وڅېړو.')
head('14.1 General Features','14.1 عمومی خصوصیات','14.1 عمومي ځانګړنې')
head('14.1.1 General Features of Transition Elements','14.1.1 عبوری عناصر کی عمومی خصوصیات','14.1.1 د انتقالي عناصرو عمومي ځانګړنې')
add('The General Features of Transition Elements are,','عبوری عناصر کی عمومی خصوصیات یہ ہیں:','د انتقالي عناصرو عمومي ځانګړنې دا دي:')
features=[
('They are all hard metals.','یہ سب سخت دھاتیں ہیں۔','دا ټول کلک فلزونه دي.'),
('They have high melting and boiling points. This is due to high nuclear charge and small atomic radius.','ان کے پگھلنے اور ابلنے کے درجے بلند ہیں۔ اس کی وجہ زیادہ مرکزی بار اور چھوٹا ایٹمی رداس ہے۔','د وېلې کېدو او اېشېدو لوړ ټکي لري. دا د لوړ هستوي چارج او کوچنۍ اټومي شعاع له امله دي.'),
('They form alloys with one another and also with the elements of other blocks.','یہ ایک دوسرے اور دوسرے بلاکوں کے عناصر کے ساتھ مخلوط دھاتیں بناتے ہیں۔','هغوی له یو بل او د نورو بلاکونو له عناصرو سره الیاژونه جوړوي.'),
('They are good conductors of heat and electricity.','یہ حرارت اور بجلی کے اچھے موصل ہیں۔','د تودوخې او برېښنا ښه لېږدوونکي دي.'),
('Most of these elements show variable valencies or oxidation states.','ان میں سے زیادہ تر متغیر ظرف یا تکسیدی حالتیں دکھاتے ہیں۔','د دې عناصرو ډېری بدلېدونکي ظرفیتونه یا د اکسیدېشن حالتونه ښيي.'),
('The compounds and ions of transition elements are mostly coloured in solid state and in solution respectively. Colour is due to the incomplete “d” orbitals in which electronic transition is possible.','عبوری عناصر کے مرکبات اور آئن بالترتیب ٹھوس حالت اور محلول میں زیادہ تر رنگین ہوتے ہیں۔ رنگ نامکمل d آربیٹلز کی وجہ سے ہے، جن میں الیکٹرونی انتقال ممکن ہے۔','د انتقالي عناصرو مرکبات او ایونونه په ترتیب سره په جامد حالت او محلول کې ډېری رنګین وي. رنګ د نیمګړو d اوربیټلونو له امله دی چې پکې الکتروني انتقال ممکن دی.'),
('Some of the transition elements form paramagnetic compounds because of the presence of unpaired electrons.','بعض عبوری عناصر غیر جوڑا الیکٹرونوں کی موجودگی کی وجہ سے پیرا مقناطیسی مرکبات بناتے ہیں۔','ځینې انتقالي عناصر د بې جوړې الکترونونو د شتون له امله پارامقناطیسي مرکبات جوړوي.'),
('They have the ability to form complexes because of the involvement of vacant d-orbitals.','خالی d آربیٹلز کی شرکت کی وجہ سے ان میں کمپلیکس بنانے کی صلاحیت ہے۔','د خالي d اوربیټلونو د ګډون له امله د کمپلېکسونو د جوړولو وړتیا لري.'),
]
for e,u,p in features:add(e,u,p,'list')
head('14.1.2 Electronic Structure','14.1.2 الیکٹرونی ساخت','14.1.2 الکتروني جوړښت')
add('Generally, the electronic configuration of transition elements is (n–1) d¹⁻¹⁰ns¹⁻². Scandium (Z = 21), the first transition metal in this series, has the configuration [Ar]3d¹,4s². Addition of electron to the 3d sub-shell continues until, at zinc (Z = 30), the 3d sub-shell is filled, with the 4s sub-shell still containing two electrons. However, there are two irregularities, one at chromium (Z = 24) and the other at copper (Z=29). The electronic configuration of chromium (Z = 24) is [Ar]3d⁵, 4s¹ and not [Ar]3d⁴,4s² as we might expect. A similar break in the pattern is observed for copper, whose electronic configuration is [Ar] 3d¹⁰,4s¹, rather than [Ar] 3d⁹,4s².',
    'عموماً عبوری عناصر کی الیکٹرونی ترتیب (n–1) d¹⁻¹⁰ns¹⁻² ہے۔ اس سلسلے کی پہلی عبوری دھات اسکینڈیم (Z = 21) کی ترتیب [Ar]3d¹,4s² ہے۔ 3d ذیلی خول میں الیکٹرونوں کا اضافہ زنک (Z = 30) تک جاری رہتا ہے، جہاں 3d ذیلی خول بھر جاتا ہے اور 4s میں اب بھی دو الیکٹرون ہوتے ہیں۔ تاہم دو بے قاعدگیاں ہیں، ایک کرومیم (Z = 24) اور دوسری تانبے (Z=29) پر۔ کرومیم کی ترتیب [Ar]3d⁵, 4s¹ ہے، نہ کہ متوقع [Ar]3d⁴,4s²۔ تانبے میں بھی ایسا فرق ہے؛ اس کی ترتیب [Ar] 3d¹⁰,4s¹ ہے، [Ar] 3d⁹,4s² نہیں۔',
    'په عمومي ډول د انتقالي عناصرو الکتروني ترتیب (n–1) d¹⁻¹⁰ns¹⁻² دی. سکانډیم (Z = 21)، د دې لړۍ لومړی انتقالي فلز، [Ar]3d¹,4s² ترتیب لري. 3d فرعي پوښ ته د الکترون زیاتول تر زنک (Z = 30) پورې دوام کوي، چې هلته 3d فرعي پوښ ډک وي او 4s لا هم دوه الکترونونه لري. خو دوه بې قاعدګۍ شته، یوه په کرومیم (Z = 24) او بله په مسو (Z=29) کې. د کرومیم ترتیب [Ar]3d⁵, 4s¹ دی، نه هغه [Ar]3d⁴,4s² چې تمه یې کوو. په مسو کې هم ورته بدلون لیدل کېږي؛ ترتیب یې [Ar] 3d¹⁰,4s¹ دی، نه [Ar] 3d⁹,4s².')
head('Tidbit: Aufbau Principle','مختصر معلومات: آفباؤ اصول','لنډ معلومات: د اوفباو اصل')
add('The word ‘Aufbau’ is derived from the German language and can be translated as construct or build up. Aufbau principle states that electrons are filled into atomic orbitals in the increasing order of orbital energy level. According to the Aufbau principle, the available atomic orbitals with the lowest energy state are occupied before those with higher energy state.',
    'لفظ آفباؤ جرمن زبان سے ہے اور اس کا ترجمہ تعمیر یا بنانا ہے۔ آفباؤ اصول کے مطابق الیکٹرون ایٹمی آربیٹلز میں توانائی کی بڑھتی ترتیب سے بھرتے ہیں۔ اس اصول کے مطابق کم ترین توانائی والے دستیاب آربیٹلز زیادہ توانائی والوں سے پہلے پُر ہوتے ہیں۔',
    'د اوفباو کلمه له جرمني ژبې اخیستل شوې او د جوړولو یا ودانولو په مانا ژباړل کېدای شي. د اوفباو اصل وايي چې الکترونونه د اوربیټل د انرژۍ د کچې په زیاتېدونکي ترتیب اټومي اوربیټلونه ډکوي. د دې اصل له مخې د تر ټولو ټیټې انرژۍ موجود اوربیټلونه له لوړې انرژۍ لرونکو څخه مخکې ډکېږي.')
def orbitals(lang):
 labels={'en':['Expected configuration','Observed configuration'],'ur':['متوقع ترتیب','مشاہدہ شدہ ترتیب'],'ps':['تمه شوی ترتیب','لیدل شوی ترتیب']}[lang]
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-label="Chromium and copper configurations"><rect width="760" height="260" fill="white"/>']
 def text(x,y,v,size=15):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#111">{html.escape(v)}</text>')
 text(300,25,'Cr (Z = 24)');text(600,25,'Cu (Z = 29)')
 for row in range(2):
  y=65+row*115;text(91,y+24,labels[row],13)
  for xbase,num,n4 in [(200,4 if row==0 else 5,2 if row==0 else 1),(500,9 if row==0 else 10,2 if row==0 else 1)]:
   counts=[1 if i<num else 0 for i in range(5)] if num<=5 else [2 if i<num-5 else 1 for i in range(5)]
   for i,count in enumerate(counts+[n4]):
    x=xbase+i*31+(20 if i==5 else 0);s.append(f'<path d="M{x-9} {y+31}h22" stroke="#111"/>')
    for j in range(count):
     ax=x+j*8;end=y+2 if j==0 else y+27;start=y+27 if j==0 else y+2;delta=4 if j==0 else -4
     s.append(f'<path d="M{ax} {start}V{end}m-3 {delta}l3 {-delta}l3 {delta}" stroke="{"#be123c" if i==5 else "#111"}" fill="none" stroke-width="1.5"/>')
   exponent=str(num).translate(str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹'))
   text(xbase+60,y+54,'3d'+exponent);text(xbase+175,y+54,'4s'+str(n4).translate(str.maketrans('12','¹²')))
 s.append('</svg>');return ''.join(s)
blocks.append({'id':'chem12-cr-cu-configurations','svg':orbitals('en'),'svgUrdu':orbitals('ur'),'svgPashto':orbitals('ps')});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('The reason for these irregularities is that a slightly greater stability is associated with the half-filled (3d⁵) and completely filled (3d¹⁰) subshells.',
    'ان بے قاعدگیوں کی وجہ نصف بھرے (3d⁵) اور مکمل بھرے (3d¹⁰) ذیلی خولوں کا معمولی زیادہ استحکام ہے۔',
    'د دې بې قاعدګیو لامل دا دی چې نیم ډک (3d⁵) او بشپړ ډک (3d¹⁰) فرعي پوښونه لږ ډېر ثبات لري.')
add('When the first-row transition metals form cations, electrons are removed first from the 4s orbitals and then from the 3d orbitals.',
    'پہلی قطار کی عبوری دھاتوں کے مثبت آئن بننے پر الیکٹرون پہلے 4s اور پھر 3d آربیٹلز سے نکلتے ہیں۔',
    'کله چې د لومړۍ قطار انتقالي فلزونه مثبت ایونونه جوړوي، الکترونونه لومړی له 4s او بیا له 3d اوربیټلونو لرې کېږي.')
add('The second, third and fourth transition metal series correspond to the filling of the 4d, 5d and 6d sub-shells respectively.',
    'دوسرا، تیسرا اور چوتھا عبوری دھاتی سلسلہ بالترتیب 4d، 5d اور 6d ذیلی خولوں کے بھرنے سے متعلق ہے۔',
    'دویمه، درېیمه او څلورمه انتقالي فلزي لړۍ په ترتیب سره د 4d، 5d او 6d فرعي پوښونو له ډکېدو سره تړاو لري.')
record=section('14.2','Transition features and electronic structures','عبوری خصوصیات اور الیکٹرونی ساختیں','انتقالي ځانګړنې او الکتروني جوړښتونه',paras,layout,blocks,'48–49');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':28,'printedPages':[48,49]}]
issues=[{'id':'chem12-p48-caesium58','printedPage':48,'description':'The source calls atomic number58 caesium instead of cerium. Exact printed name and number retained in all three languages.'}]
if __name__=='__main__':save(28,[record],trim=[{'id':'14.3','startsAt':'3d-elements'}],issues=issues,chapter_number=14)
