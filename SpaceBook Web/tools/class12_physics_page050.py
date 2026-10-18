"""Sequential source correction for PDF page 50 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(p):return {'pdfPage':50,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 285" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:560px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

FIELD=[
 pair('13.1 MAGNETIC FIELD','13.1 مقناطیسی میدان','13.1 مقناطیسي ساحه'),
 pair('A magnetic field surrounds a magnetic substance making up a permanent magnet.','ایک مقناطیسی مادے کے گرد مقناطیسی میدان ہوتا ہے جو مستقل مقناطیس بناتا ہے۔','د یوه مقناطیسي مواد شاوخوا مقناطیسي ساحه وي چې دایمي مقناطیس جوړوي.'),
 pair('In addition to containing an electric field, the region of space surrounding any moving electric charge also contains a magnetic field. When charges are not moving no such effect is seen. Magnetic field is represented by magnetic induction vector B. We can define a magnetic field “B” at some point in space in terms of the magnetic force “F_B” that the field exerts on a test object, for which we use a charged particle moving with a velocity “v”.',
  'برقی میدان کے علاوہ، حرکت کرتے ہوئے برقی بار کے گرد خلا میں مقناطیسی میدان بھی ہوتا ہے۔ جب بار حرکت نہ کر رہے ہوں تو ایسا اثر نہیں دیکھا جاتا۔ مقناطیسی میدان کو مقناطیسی القا کے سمتیہ B سے ظاہر کرتے ہیں۔ کسی مقام پر میدان B کی تعریف اس مقناطیسی قوت F_B سے کی جا سکتی ہے جو میدان آزمائشی جسم پر لگاتا ہے؛ اس کے لیے رفتار v سے حرکت کرتے ہوئے بار دار ذرّے کو استعمال کرتے ہیں۔',
  'د برېښنايي ساحې ترڅنګ، د هر خوځنده برېښنايي چارج شاوخوا فضا کې مقناطیسي ساحه هم وي. کله چې چارجونه نه خوځېږي، دا اغېز نه لیدل کېږي. مقناطیسي ساحه د مقناطیسي القا د ویکتور B په وسیله ښودل کېږي. په یوه ځای کې د B ساحه د هغې مقناطیسي قوې F_B له مخې تعریفولای شو چې ساحه یې پر ازمېښتي څیز واردوي؛ د دې لپاره په v سرعت خوځنده چارج لرونکې ذره کاروو.'),
 pair('The relationship between magnetism and electricity was discovered in 1819. During a lecture demonstration, Hans Christian Oersted found that electric current in a wire deflected a nearby compass needle. Thus a steady current through a conducting wire creates a magnetic field, as shown in Figure 13.1.',
  'مقناطیسیت اور بجلی کے تعلق کی دریافت 1819 میں ہوئی۔ لیکچر کے مظاہرے کے دوران ہانس کرسچن اورسٹڈ نے دیکھا کہ تار میں برقی رو قریب رکھی قطب نما کی سوئی کو منحرف کرتی ہے۔ یوں موصل تار میں مستقل برقی رو مقناطیسی میدان پیدا کرتی ہے، جیسا کہ شکل 13.1 میں دکھایا گیا ہے۔',
  'د مقناطیسیت او برېښنا اړیکه په 1819 کې وموندل شوه. د لکچر د یوې نندارې پر مهال هانس کریسټین اورسټډ وموندله چې په سیم کې برېښنايي جریان نږدې د قطب‌نما ستنه اړوي. نو په هادي سیم کې ثابت جریان مقناطیسي ساحه جوړوي، لکه په 13.1 شکل کې.'),
 pair('To demonstrate the magnetic field produced by the current in a wire, we can perform simple experiments.','په تار کې د برقی رو سے پیدا ہونے والا مقناطیسی میدان دکھانے کے لیے ہم سادہ تجربے کر سکتے ہیں۔','په سیم کې د جریان له خوا تولید شوې مقناطیسي ساحې د ښودلو لپاره ساده ازمېښتونه کولای شو.'),
 pair('FIGURE 13.1 — Using an apparatus similar to the one shown, Oersted was able to demonstrate a connection between magnetism and electricity by applying current to the wire.',
  'شکل 13.1 — دکھائے گئے آلے جیسے سامان سے اورسٹڈ نے تار میں برقی رو گزار کر مقناطیسیت اور بجلی کا تعلق ظاہر کیا۔','13.1 شکل — د ښودل شوي ورته وسیلې په کارولو اورسټډ په سیم کې د جریان په تېرولو د مقناطیسیت او برېښنا اړیکه وښوده.'),
 pair('OERSTED (1777–1851)','اورسٹڈ (1777–1851)','اورسټډ (1777–1851)'),
 pair('In 1806 Hans Christian Oersted became a professor at the University of Copenhagen, where his first physical researches dealt with electric currents and acoustics. In 1932 the name oersted was adopted for the physical unit of magnetic field strength.',
  '1806 میں ہانس کرسچن اورسٹڈ یونیورسٹی آف کوپن ہیگن میں پروفیسر بنے، جہاں ان کی ابتدائی طبیعیاتی تحقیق برقی روؤں اور صوتیات سے متعلق تھی۔ 1932 میں مقناطیسی میدان کی قوت کی طبیعی اکائی کے لیے اورسٹڈ نام اختیار کیا گیا۔',
  'په 1806 کې هانس کریسټین اورسټډ د کوپنهاګن پوهنتون پروفیسور شو؛ هلته یې لومړنۍ فزیکي څېړنې د برېښنايي جریانونو او غږپوهنې په اړه وې. په 1932 کې د مقناطیسي ساحې د شدت فزیکي واحد ته د اورسټډ نوم ورکړل شو.'),
]
WIRE=[
 pair('When current is passed through a long wire with compass needles placed around it in a circle, the compass needles line up with the magnetic field. Similar observations can be made through a cardboard on which iron filings are sprinkled. These iron filings form concentric circles around the wire, as shown in Figure 13.2.',
  'جب لمبی تار میں برقی رو گزاری جائے اور اس کے گرد دائرے میں قطب نما کی سوئیاں رکھی ہوں تو سوئیاں مقناطیسی میدان کے ساتھ سیدھ میں آ جاتی ہیں۔ گتے پر لوہے کا برادہ چھڑک کر بھی ایسا مشاہدہ کیا جا سکتا ہے۔ یہ برادہ تار کے گرد ہم مرکز دائرے بناتا ہے، جیسا کہ شکل 13.2 میں ہے۔',
  'کله چې په اوږده سیم کې جریان تېر شي او د سیم شاوخوا دایروي قطب‌نما ستنې کېښودل شي، ستنې له مقناطیسي ساحې سره سمېږي. ورته مشاهده پر هغه مقوا هم کېدای شي چې د اوسپنې براده پرې شیندل شوې وي. براده د سیم شاوخوا متحدالمرکزې دایرې جوړوي، لکه په 13.2 شکل کې.'),
 pair('FIGURE 13.2 (a) A current-carrying wire with compass needles lining up with the magnetic field in a circular pattern. (b) A current-carrying wire through cardboard shows concentric circles of iron filings around the wire.',
  'شکل 13.2 (a) کرنٹ بردار تار کے گرد قطب نما کی سوئیاں دائرے کی صورت میں مقناطیسی میدان کے ساتھ سیدھ میں ہیں۔ (b) گتے میں سے گزرتی کرنٹ بردار تار کے گرد لوہے کے برادے کے ہم مرکز دائرے دکھائے گئے ہیں۔',
  '13.2 شکل (a) د جریان‌لرونکي سیم شاوخوا د قطب‌نما ستنې په دایروي بڼه له مقناطیسي ساحې سره سمې دي. (b) له مقوا تېر شوی جریان‌لرونکی سیم د اوسپنې د برادې متحدالمرکزې دایرې ښيي.'),
 pair('These experiments show the orientation of a magnetic field, which is in the form of a circle around the wire. The direction of the magnetic field can be determined by Right Hand Rule I, as shown in Figure 13.3.',
  'یہ تجربے مقناطیسی میدان کی سمت دکھاتے ہیں، جو تار کے گرد دائرے کی شکل میں ہوتا ہے۔ مقناطیسی میدان کی سمت دایاں ہاتھ قاعدہ I استعمال کر کے معلوم کی جا سکتی ہے، جیسا کہ شکل 13.3 میں دکھایا گیا ہے۔',
  'دا ازمېښتونه د مقناطیسي ساحې لوری ښيي چې د سیم شاوخوا دایروي وي. د مقناطیسي ساحې لوری د ښي لاس د لومړي قاعدې له مخې معلومېدای شي، لکه په 13.3 شکل کې.'),
]
RULE=[
 pair('RIGHT-HAND RULE I FOR THE MAGNETIC FIELD FROM A CURRENT-CARRYING WIRE','د کرنٹ بردار تار کے مقناطیسی میدان کے لیے دایاں ہاتھ قاعدہ I','د جریان‌لرونکي سیم د مقناطیسي ساحې لپاره د ښي لاس لومړۍ قاعده'),
 pair('Put your thumb in the direction of current and curl your fingers around the wire; the curled fingers will show the direction of the magnetic field. This rule is for the direction of conventional current or flow of positive charges. For electronic current flow, the same rule is applied but with the left hand.',
  'انگوٹھا برقی رو کی سمت میں رکھیں اور انگلیاں تار کے گرد موڑیں؛ مڑی ہوئی انگلیاں مقناطیسی میدان کی سمت دکھائیں گی۔ یہ قاعدہ روایتی برقی رو یا مثبت باروں کے بہاؤ کی سمت کے لیے ہے۔ الیکٹرانک رو کے لیے یہی قاعدہ بائیں ہاتھ سے لاگو ہوتا ہے۔',
  'ګوته د جریان په لوري کېږدئ او ګوتې د سیم شاوخوا تاو کړئ؛ تاوې شوې ګوتې به د مقناطیسي ساحې لوری وښيي. دا قاعده د دودیز جریان یا د مثبتو چارجونو د بهېدو لپاره ده. د الکتروني جریان لپاره همدا قاعده په چپ لاس پلي کېږي.'),
]
FORCE=[
 pair('13.2 FORCE ON A CURRENT-CARRYING CONDUCTOR','13.2 کرنٹ بردار موصل پر قوت','13.2 پر جریان‌لرونکي هادي قوه'),
 pair('When a current-carrying wire is placed in a uniform magnetic field, the magnetic field of the wire and the external uniform field interact, resulting in a force on the wire as shown in Figure 13.4. This force F_B depends on the applied magnetic field B, current I in the wire, length L of the wire that lies in the field, and the sine of angle θ that the current-carrying wire makes with the field.',
  'جب کرنٹ بردار تار کو یکساں مقناطیسی میدان میں رکھا جاتا ہے تو تار کا مقناطیسی میدان بیرونی یکساں میدان سے تعامل کرتا ہے اور تار پر قوت لگتی ہے، جیسا کہ شکل 13.4 میں ہے۔ یہ قوت F_B لگائے گئے مقناطیسی میدان B، تار میں برقی رو I، میدان کے اندر تار کی لمبائی L، اور تار و میدان کے درمیان زاویہ θ کے سائن پر منحصر ہے۔',
  'کله چې جریان‌لرونکی سیم په یوشان مقناطیسي ساحه کې کېښودل شي، د سیم مقناطیسي ساحه له بهرني یوشان میدان سره تعامل کوي او پر سیم قوه واردېږي، لکه په 13.4 شکل کې. دا قوه F_B د لګېدلې مقناطیسي ساحې B، د سیم د جریان I، په ساحه کې د سیم د اوږدوالي L او د سیم او ساحې ترمنځ د θ زاویې د ساین پورې اړه لري.'),
]

def make(identity,title,printed,pairs,layout,titles,refs,diag=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':50,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(x) for x in refs]
 if diag:s.update(diag);s['content']+=diag['diagramSvg']
 return r,s

def field_svg(lang):
 L={'en':'Figure 13.1: compass needle deflected by a current-carrying wire.','ur':'شکل 13.1: کرنٹ بردار تار سے قطب نما کی سوئی منحرف ہوتی ہے۔','ps':'13.1 شکل: د جریان‌لرونکي سیم له امله د قطب‌نما ستنه اوړي.'}[lang]
 T={'en':('wire','Compass needle'),'ur':('تار','قطب نما کی سوئی'),'ps':('سیم','د قطب‌نما ستنه')}[lang]
 b='<circle cx="265" cy="145" r="88" fill="#f8fafc" stroke="#334155" stroke-width="3"/><circle cx="265" cy="145" r="4" fill="#334155"/><path d="M210 172L325 72" stroke="#7c2d12" stroke-width="8"/><path d="M265 145L302 116" stroke="#dc2626" stroke-width="6"/><path d="M265 145L233 170" stroke="#2563eb" stroke-width="6"/><path d="M205 177l16-3-7-13" fill="#16a34a"/><text x="330" y="69" font-size="16">'+T[0]+'</text><text x="280" y="124" font-size="15">I</text><text x="200" y="226" font-size="14">'+T[1]+'</text>'
 return svg(b,L)
def compass_svg(lang):
 L={'en':'Figure 13.2: compasses and iron filings show circular magnetic field lines around a current-carrying wire.','ur':'شکل 13.2: قطب نما اور لوہے کا برادہ کرنٹ بردار تار کے گرد دائرہ نما مقناطیسی میدان کی لکیریں دکھاتے ہیں۔','ps':'13.2 شکل: قطب‌نماوې او د اوسپنې براده د جریان‌لرونکي سیم شاوخوا د مقناطیسي ساحې دایروي کرښې ښيي.'}[lang]
 T={'en':('(a) compass needles','(b) iron filings'),'ur':('(a) قطب نما کی سوئیاں','(b) لوہے کا برادہ'),'ps':('(a) د قطب‌نما ستنې','(b) د اوسپنې براده')}[lang]
 b='<circle cx="155" cy="140" r="76" fill="none" stroke="#2563eb" stroke-width="2"/><circle cx="155" cy="140" r="48" fill="none" stroke="#2563eb" stroke-width="2"/><path d="M155 140V45M155 140H250M155 140V235M155 140H60" stroke="#334155" stroke-width="4"/><circle cx="155" cy="140" r="9" fill="#dc2626"/><g fill="#fff" stroke="#334155" stroke-width="2"><circle cx="88" cy="83" r="15"/><circle cx="222" cy="83" r="15"/><circle cx="88" cy="197" r="15"/><circle cx="222" cy="197" r="15"/></g><path d="M77 83h21M211 83h21M77 197h21M211 197h21" stroke="#dc2626" stroke-width="3"/><text x="105" y="270" font-size="14">'+T[0]+'</text>'
 b+='<circle cx="405" cy="140" r="76" fill="none" stroke="#2563eb" stroke-width="2"/><circle cx="405" cy="140" r="53" fill="none" stroke="#2563eb" stroke-width="2"/><circle cx="405" cy="140" r="30" fill="none" stroke="#2563eb" stroke-width="2"/><path d="M405 58V222" stroke="#7c2d12" stroke-width="8"/><circle cx="405" cy="95" r="3" fill="#b45309"/><circle cx="382" cy="130" r="3" fill="#b45309"/><circle cx="430" cy="170" r="3" fill="#b45309"/><text x="353" y="270" font-size="14">'+T[1]+'</text>'
 return svg(b,L)
def rule_svg(lang):
 L={'en':'Figure 13.3: thumb points along current; curled fingers show the magnetic field direction.','ur':'شکل 13.3: انگوٹھا برقی رو کی سمت میں ہے؛ مڑی انگلیاں مقناطیسی میدان کی سمت دکھاتی ہیں۔','ps':'13.3 شکل: ګوته د جریان په لوري ده؛ تاوې شوې ګوتې د مقناطیسي ساحې لوری ښيي.'}[lang]
 T={'en':('Current','Magnetic field'),'ur':('برقی رو','مقناطیسی میدان'),'ps':('جریان','مقناطیسي ساحه')}[lang]
 b='<path d="M280 238V66" stroke="#7c2d12" stroke-width="12"/><path d="M280 48l-15 25h30z" fill="#16a34a"/><text x="300" y="72" font-size="16">I — '+T[0]+'</text><ellipse cx="280" cy="151" rx="88" ry="44" fill="none" stroke="#2563eb" stroke-width="3"/><path d="M355 124l16 5-14 9" fill="#2563eb"/><path d="M205 178l-16-5 14-9" fill="#2563eb"/><text x="383" y="151" font-size="16">B — '+T[1]+'</text>'
 return svg(b,L)

if __name__=='__main__':
 a=make('phys13-magnetic-field-and-oersted90','13.1 Magnetic field and Oersted observation',90,FIELD,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'visual'},{'type':'heading','indices':[6]},{'type':'paragraph','indices':[7]}],('13.1 مقناطیسی میدان اور اورسٹڈ کا مشاہدہ','13.1 مقناطیسي ساحه او د اورسټډ مشاهده'),[90],{'diagramSvg':field_svg('en'),'diagramSvgUrdu':field_svg('ur'),'diagramSvgPashto':field_svg('ps')})
 b=make('phys13-circular-field-around-wire91','Circular magnetic field around a current-carrying wire',91,WIRE,[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'paragraph','indices':[2]}],('کرنٹ بردار تار کے گرد دائرہ نما مقناطیسی میدان','د جریان‌لرونکي سیم شاوخوا دایروي مقناطیسي ساحه'),[91],{'diagramSvg':compass_svg('en'),'diagramSvgUrdu':compass_svg('ur'),'diagramSvgPashto':compass_svg('ps')})
 c=make('phys13-right-hand-rule-I91','Right-hand Rule I — magnetic field around a wire',91,RULE,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'}],('دایاں ہاتھ قاعدہ I — تار کے گرد مقناطیسی میدان','د ښي لاس لومړۍ قاعده — د سیم شاوخوا مقناطیسي ساحه'),[91],{'diagramSvg':rule_svg('en'),'diagramSvgUrdu':rule_svg('ur'),'diagramSvgPashto':rule_svg('ps')})
 d=make('phys13-force-on-current-carrying-conductor91','13.2 Force on a current-carrying conductor — introduction',91,FORCE,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]}],('13.2 کرنٹ بردار موصل پر قوت — تعارف','13.2 پر جریان‌لرونکي هادي قوه — سریزه'),[91])
 records=[x[0] for x in (a,b,c,d)];sections=[x[1] for x in (a,b,c,d)]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=2)
  sync_companions(chapter_index=2,trim_sections=[{'id':'13.1','startsAt':'Mathematically F,','title':'Unit 13 — first unchecked force equation'}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==50:
  checkpoint(50,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 50, printed pages 90–91. Compared the magnetic-field definition and vector/test-charge description, Oersted discovery and biographical panel, complete current-wire/compass and iron-filings text, Right-Hand Rule I, Figure 13.2 captions, and the opening explanation of force on a current-carrying conductor. Rebuilt Figures 13.1–13.3 as native translated SVG schematics and paired all prose in English/Urdu/Pashto; retained legacy Unit 13 material from the first unchecked force derivation on printed page 92.',printed_pages=[90,91],chapter_number=13)
