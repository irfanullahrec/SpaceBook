from physics_agent2_sequential import save_page
from physics_agent2_translations import TRANSLATIONS,TITLES
from physics_agent2_layout import LAYOUT
import math

FIELD8=[
 'The concept of electric field was first proposed by Michael Faraday, in the 19th century. He stated that the electric field around a charge is like a sphere with in which other charges are influenced by it.',
 'An electric field is defined as any region around a charge in which an electric test charge would experience an electric force.',
 'Electric field is characterized by strength and direction at every point in space. The strength and direction of electric field can be determined by placing a unit positive test charge in that field. The direction in which this unit positive test charge move or tends to move is the direction of electric field. The test charge is so small that it does not distort the original field due to the primary source.',
 r'A single vector quantity containing information about the field strength and its direction at that point is denoted by \(\vec E\) and is known as electric field intensity. If unit positive test charge \(q_0\) experience a force \(\vec F\) due to the electric field of charge q. Then',
 'the intensity of an electric field at any point is the force per unit positive test charge placed at that point.',
 r'The electric field intensity \(\vec E=\frac{\vec F}{q_0}\)',
 r'Or \(\vec F=q_0\vec E\) … (11.9)',
 r'If five charges are placed such that, as shown in figure, then the resultant force exerted by charges \(q_2,q_3,q_4\) and \(q_5\) on charge \(q_1\) is',
 r'\(\vec F_1=\vec F_{12}+\vec F_{13}+\vec F_{14}+\vec F_{15}\)',
]
FIELD9=[
 r'The SI unit of electric field intensity is newton per coulomb \(\mathrm{N\,C^{-1}}\) or volt per metre \(\mathrm{V\,m^{-1}}\).',
 'Coulomb’s law enables the electric field to be calculated for any point in space around a fixed static charge q. The magnitude of electric field is given by:',
 r'\(F=\frac{kqq_0}{r^2}\)',
 r'As \(\hat r\) is the unit vector directed from charge q to \(q_0\), so in vector form',
 r'\(\vec F=\frac{kqq_0}{r^2}\hat r\)',
 'So the field intensity is given by',
 r'\(\vec E=\frac{\vec F}{q_0}=k\frac{qq_0/r^2}{q_0}\hat r\)',
 r'\(\vec E=k\frac{q}{r^2}\hat r\) … (11.10)',
 'The strength of the field is proportional to the magnitude of the charge. Its strength decreases as the test charge moves away (unit charge) from source charge q.',
]
EXAMPLE=[
 r'Find electric field at a distance of 30 cm from a \(3\,\mu\mathrm C\) point charge.',
 'GIVEN',
 r'radius \(r=30\,\mathrm{cm}=30\times10^{-2}\,\mathrm m=0.3\,\mathrm m\)',
 r'charge \(q=3\,\mu\mathrm C=3\times10^{-6}\,\mathrm C\)',
]

def radial():
    svg='<figure><svg viewBox="0 0 360 360" role="img" aria-label="Figure 11.3: outward electric field of a positive point charge" style="max-width:420px;width:100%"><defs><marker id="phys12-f113" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#166534"/></marker></defs>'
    for i in range(16):
        angle=2*math.pi*i/16
        svg+=f'<line x1="{180+18*math.cos(angle):.2f}" y1="{180+18*math.sin(angle):.2f}" x2="{180+150*math.cos(angle):.2f}" y2="{180+150*math.sin(angle):.2f}" stroke="#166534" stroke-width="2" marker-end="url(#phys12-f113)"/>'
    svg+='<circle cx="180" cy="180" r="17" fill="#fff" stroke="#334155"/><text x="173" y="187" font-size="24">+</text><circle cx="210" cy="109" r="10" fill="#fff" stroke="#dc2626"/><text x="205" y="115">+</text><text x="226" y="112">q₀</text><text x="135" y="60">E</text><line x1="212" y1="100" x2="220" y2="77" stroke="#dc2626" stroke-width="3"/><path d="M216 82L220 73L224 85Z" fill="#dc2626"/><text x="229" y="85">F</text></svg><figcaption>Figure 11.3: Electric field intensity due to a point charge.</figcaption></figure>'
    return svg

def superposition():
    svg='<svg viewBox="0 0 340 330" role="img" aria-label="Five point charges and the four force vectors on q1" style="max-width:400px;width:100%"><defs><marker id="phys12-superposition" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#111827"/></marker></defs>'
    for x,y,label,sign in [(180,245,'q₁','+'),(35,155,'q₂','+'),(95,75,'q₃','−'),(180,45,'q₄','+'),(285,65,'q₅','+')]:
        if label!='q₁': svg+=f'<line x1="180" y1="245" x2="{x}" y2="{y}" stroke="#94a3b8"/>'
        svg+=f'<circle cx="{x}" cy="{y}" r="17" fill="{"#f9a8d4" if sign=="−" else "#7dd3fc"}"/><text x="{x-6}" y="{y+6}" font-size="20">{sign}</text><text x="{x-10}" y="{y-25}">{label}</text>'
    for x,y,label in [(252,290,'F₁₂'),(135,155,'F₁₃'),(180,310,'F₁₄'),(145,310,'F₁₅')]:
        svg+=f'<line x1="180" y1="245" x2="{x}" y2="{y}" stroke="#111827" stroke-width="2" marker-end="url(#phys12-superposition)"/><text x="{x+6}" y="{y+5}">{label}</text>'
    return svg+'</svg>'

def prepare():
    TITLES.update({'phys12-front-field8':('11.2 برقی میدان اور اس کی شدت','11.2 برېښنايي میدان او شدت یې'),'phys12-front-field9':('نقطہ بار کی وجہ سے برقی میدان','د نقطوي چارج له امله برېښنايي میدان'),'phys12-front-example112-start':('مثال 11.2: سوال اور دی گئی معلومات','بېلګه 11.2: پوښتنه او ورکړل شوي معلومات')})
    TRANSLATIONS['phys12-front-field8']=[
      ('برقی میدان کا تصور سب سے پہلے مائیکل فیراڈے نے انیسویں صدی میں پیش کیا۔ اس نے کہا کہ کسی بار کے گرد برقی میدان ایک کرہ کی طرح ہے جس کے اندر دوسرے بار اس سے متاثر ہوتے ہیں۔','د برېښنايي میدان مفهوم لومړی مایکل فاراډې په نولسمه پېړۍ کې وړاندې کړ. هغه وویل چې د چارج شاوخوا برېښنايي میدان د یوې کرې په څېر دی چې دننه یې نور چارجونه تر اغېز لاندې راځي.'),
      ('برقی میدان کسی بار کے گرد اس خطے کو کہتے ہیں جہاں آزمائشی برقی بار برقی قوت محسوس کرے۔','برېښنايي میدان د چارج شاوخوا هغې سیمې ته ویل کېږي چې هلته یو برېښنايي ازمایښتي چارج برېښنايي قوه احساس کړي.'),
      ('برقی میدان فضا کے ہر نقطے پر شدت اور سمت رکھتا ہے۔ اس کی شدت اور سمت میدان میں اکائی مثبت آزمائشی بار رکھ کر معلوم کی جا سکتی ہیں۔ یہ مثبت آزمائشی بار جس سمت حرکت کرے یا حرکت کا رجحان رکھے، وہی برقی میدان کی سمت ہوتی ہے۔ آزمائشی بار اتنا چھوٹا ہوتا ہے کہ اصل منبع کے میدان کو تبدیل نہیں کرتا۔','برېښنايي میدان د فضا په هره نقطه کې شدت او لوری لري. د میدان شدت او لوری په هغه کې د واحد مثبت ازمایښتي چارج په ایښودلو معلومېدای شي. دا مثبت ازمایښتي چارج چې کوم لوري ته حرکت کوي یا د حرکت تمایل لري، هماغه د برېښنايي میدان لوری دی. ازمایښتي چارج دومره کوچنی وي چې د اصلي منبع میدان نه بدلوي.'),
      (r'کسی نقطے پر میدان کی شدت اور سمت کی معلومات رکھنے والی واحد سمتی مقدار کو \(\vec E\) سے ظاہر کرتے ہیں اور برقی میدان کی شدت کہتے ہیں۔ اگر اکائی مثبت آزمائشی بار \(q_0\)، بار q کے میدان کی وجہ سے قوت \(\vec F\) محسوس کرے تو',r'په یوه نقطه کې د میدان د شدت او لوري معلومات لرونکې واحده ویکټوري اندازه په \(\vec E\) ښودل کېږي او د برېښنايي میدان شدت ورته ویل کېږي. که واحد مثبت ازمایښتي چارج \(q_0\) د q چارج د میدان له امله قوه \(\vec F\) احساس کړي، نو'),
      ('کسی نقطے پر برقی میدان کی شدت اس نقطے پر رکھے گئے فی اکائی مثبت آزمائشی بار پر قوت ہے۔','په یوه نقطه کې د برېښنايي میدان شدت پر هغه ځای ایښودل شوي واحد مثبت ازمایښتي چارج وارده قوه ده.'),
      (r'برقی میدان کی شدت \(\vec E=\frac{\vec F}{q_0}\)',r'د برېښنايي میدان شدت \(\vec E=\frac{\vec F}{q_0}\)'),
      (r'یا \(\vec F=q_0\vec E\) … (11.9)',r'یا \(\vec F=q_0\vec E\) … (11.9)'),
      (r'اگر پانچ بار شکل کے مطابق رکھے جائیں تو \(q_2,q_3,q_4\) اور \(q_5\) کی وجہ سے \(q_1\) پر حاصل قوت یہ ہے:',r'که پنځه چارجونه د شکل له مخې کېښودل شي، نو د \(q_2,q_3,q_4\) او \(q_5\) له امله پر \(q_1\) حاصله قوه دا ده:'),
      (FIELD8[8],FIELD8[8]),
    ]
    TRANSLATIONS['phys12-front-field9']=[
      (r'برقی میدان کی شدت کی بین الاقوامی اکائی نیوٹن فی کولوم \(\mathrm{N\,C^{-1}}\) یا وولٹ فی میٹر \(\mathrm{V\,m^{-1}}\) ہے۔',r'د برېښنايي میدان د شدت نړیوال واحد نیوټن پر کولم \(\mathrm{N\,C^{-1}}\) یا ولټ پر متر \(\mathrm{V\,m^{-1}}\) دی.'),
      ('کولوم کے قانون سے ساکن بار q کے گرد فضا کے کسی بھی نقطے پر برقی میدان معلوم کیا جا سکتا ہے۔ برقی میدان کے لیے قوت کی مقدار یوں دی گئی ہے:','د کولم قانون د ثابت ساکن چارج q شاوخوا د فضا په هره نقطه کې د برېښنايي میدان محاسبه ممکنوي. د برېښنايي میدان لپاره د قوې مقدار داسې ورکړل شوی دی:'),
      (FIELD9[2],FIELD9[2]),
      (r'چونکہ \(\hat r\) بار q سے \(q_0\) کی طرف اکائی سمتیہ ہے، اس لیے سمتی صورت میں',r'څرنګه چې \(\hat r\) له q چارج څخه \(q_0\) ته واحد ویکټور دی، نو په ویکټوري بڼه'),
      (FIELD9[4],FIELD9[4]),
      ('لہٰذا میدان کی شدت یوں دی جاتی ہے:','نو د میدان شدت داسې ورکول کېږي:'),
      (FIELD9[6],FIELD9[6]),(FIELD9[7],FIELD9[7]),
      ('میدان کی شدت بار کی مقدار کے راست متناسب ہے۔ آزمائشی بار (اکائی بار) کو منبع بار q سے دور لے جانے پر میدان کی شدت کم ہو جاتی ہے۔','د میدان شدت د چارج له مقدار سره مستقیم تناسب لري. کله چې ازمایښتي چارج (واحد چارج) له منبع چارج q څخه لرې ځي، د میدان شدت کمېږي.'),
    ]
    TRANSLATIONS['phys12-front-example112-start']=[
      (r'\(3\,\mu\mathrm C\) نقطہ بار سے 30 سینٹی میٹر فاصلے پر برقی میدان معلوم کریں۔',r'له \(3\,\mu\mathrm C\) نقطوي چارج څخه د 30 سانتي متره په واټن کې برېښنايي میدان محاسبه کړئ.'),
      ('دی گئی معلومات','ورکړل شوي معلومات'),
      (r'فاصلہ \(r=30\,\mathrm{cm}=30\times10^{-2}\,\mathrm m=0.3\,\mathrm m\)',r'واټن \(r=30\,\mathrm{cm}=30\times10^{-2}\,\mathrm m=0.3\,\mathrm m\)'),
      (r'بار \(q=3\,\mu\mathrm C=3\times10^{-6}\,\mathrm C\)',r'چارج \(q=3\,\mu\mathrm C=3\times10^{-6}\,\mathrm C\)'),
    ]
    LAYOUT.update({
      'phys12-front-field8':[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3,4]},{'type':'equation','indices':[5]},{'type':'equation','indices':[6]},{'type':'visual'},{'type':'paragraph','indices':[7]},{'type':'equation','indices':[8]}],
      'phys12-front-field9':[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'visual'}],
      'phys12-front-example112-start':[{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'lines','indices':[2,3]}],
    })

def records():
    return [
      {'id':'phys12-front-field8','printedPage':8,'title':'11.2 Electric field and its intensity','kind':'lesson','paragraphs':FIELD8,'diagramHtml':superposition(),'definitions':[{'term':'Electric field','text':FIELD8[1]},{'term':'Electric field intensity','text':FIELD8[4]}],'diagrams':[{'type':'charge-force-superposition','chargeSigns':[1,1,-1,1,1],'forceTarget':'q1','forceVectors':['F12','F13','F14','F15']}]},
      {'id':'phys12-front-field9','printedPage':9,'title':'Electric field intensity due to a point charge','kind':'lesson','paragraphs':FIELD9,'diagramHtml':radial(),'diagrams':[{'figure':'11.3','type':'radial-point-charge-field','sourceSign':1,'testChargeSign':1,'fieldDirection':'outward'}]},
      {'id':'phys12-front-example112-start','printedPage':9,'title':'Example 11.2 — Given','kind':'lesson','paragraphs':EXAMPLE,'continuedOnNextPdfPage':10},
    ]

if __name__ == '__main__':
    prepare()
    save_page(9,records())
