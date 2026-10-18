"""PDF55 / printed102–103: hydrocarbon types, nomenclature, Table16.1.

Independent page builder. Importing does not mutate application data or progress.
"""
from html import escape
from math import sin, cos, pi
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save


def structures(kind, language):
    """Source structures as vector bonds and labels, with localized captions."""
    labels = {
        'en': ['ethyne', 'propyne', 'cyclohexyne', 'benzene', 'toluene', 'naphthalene'],
        'ur': ['ایتھائن', 'پروپائن', 'سائیکلوہیکسائن', 'بینزین', 'ٹولیون', 'نیفتھلین'],
        'ps': ['ایتاین', 'پروپاین', 'سایکلوهېکساین', 'بینزین', 'تولوین', 'نافتالین'],
    }[language]
    title = 'Alkynes and Cycloalkynes' if kind == 'alkynes' else 'Aromatic Hydrocarbons'
    title = {'ur': {'alkynes': 'الکائنز اور سائیکلوالکائنز', 'aromatics': 'ارومیٹک ہائیڈروکاربن'}, 'ps': {'alkynes': 'الکاینونه او سایکلوالکاینونه', 'aromatics': 'اروماتیک هایدروکاربنونه'}}.get(language, {}).get(kind, title)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 230" role="img" aria-label="{escape(title)}"><rect width="780" height="230" fill="white"/>']
    def text(x, y, value, size=20):
        parts.append(f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" fill="#111">{escape(value)}</text>')
    def line(a, b, width=1.8):
        parts.append(f'<path d="M{a[0]:.2f} {a[1]:.2f}L{b[0]:.2f} {b[1]:.2f}" fill="none" stroke="#111" stroke-width="{width}"/>')
    def polygon(points):
        parts.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'" fill="none" stroke="#111" stroke-width="1.8"/>')
    def inset_bond(a, b, centre):
        # A separate inset line reproduces each printed double bond.
        aa=(a[0]+(b[0]-a[0])*.14, a[1]+(b[1]-a[1])*.14)
        bb=(b[0]+(a[0]-b[0])*.14, b[1]+(a[1]-b[1])*.14)
        def inward(pt):
            dx,dy=centre[0]-pt[0],centre[1]-pt[1]
            length=(dx*dx+dy*dy)**.5
            return (pt[0]+dx*6/length,pt[1]+dy*6/length)
        line(inward(aa),inward(bb))
    if kind == 'alkynes':
        text(117, 103, 'HC≡CH', 25); text(117, 182, labels[0], 18)
        text(355, 103, 'H₃C—C≡CH', 25); text(355, 182, labels[1], 18)
        coords=[(615,35),(660,62),(660,118),(615,145),(570,118),(570,62)]
        atoms=['CH₂','C','C','CH₂','CH₂','CH₂']
        for i, (a,b) in enumerate(zip(coords, coords[1:]+coords[:1])):
            dx,dy=b[0]-a[0],b[1]-a[1];length=(dx*dx+dy*dy)**.5
            gap=14 if abs(dx)>0 else 13
            start=(a[0]+dx*gap/length,a[1]+dy*gap/length)
            end=(b[0]-dx*gap/length,b[1]-dy*gap/length)
            line(start,end)
            if i==1:
                line((start[0]-5,start[1]),(end[0]-5,end[1]))
                line((start[0]+5,start[1]),(end[0]+5,end[1]))
        for (x,y),a in zip(coords,atoms):text(x,y+6,a,18)
        text(615,182,labels[2],18)
    else:
        def ring(cx,cy,r=48):
            return [(cx+r*cos(-pi/2+i*pi/3),cy+r*sin(-pi/2+i*pi/3)) for i in range(6)]
        for cx,caption,methyl in [(130,labels[3],False),(340,labels[4],True)]:
            points=ring(cx,110);polygon(points)
            for i in (0,2,4):inset_bond(points[i],points[(i+1)%6],(cx,110))
            if methyl:
                line(points[0],(cx,42));text(cx,34,'CH₃',20)
            text(cx,199,caption,18)
        # Fused hexagons share exactly one edge and use five C=C bonds.
        left=ring(563,110);right=ring(563+48*3**.5,110)
        polygon(left);polygon(right)
        for i in (0,2,4):inset_bond(left[i],left[(i+1)%6],(563,110))
        for i in (0,2):inset_bond(right[i],right[(i+1)%6],(563+48*3**.5,110))
        text(605,199,labels[5],18)
    return ''.join(parts)+'</svg>'


paras=[]
layout=[]
blocks=[]

def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]})
    paras.append(pair(en,ur,ps))

def figure(kind):
    identity='chem12-p55-'+kind
    blocks.append({'id':identity,'svg':structures(kind,'en'),'svgUrdu':structures(kind,'ur'),'svgPashto':structures(kind,'ps')})
    layout.append({'type':'visual','blockId':identity})

add('Alkynes and Cycloalkynes','الکائنز اور سائیکلوالکائنز','الکاینونه او سایکلوالکاینونه','heading')
figure('alkynes')
add('2. Aromatic Hydrocarbons','2. ارومیٹک ہائیڈروکاربن','2. اروماتیک هایدروکاربنونه','heading')
add('The term aromatic was derived from the Greek word aroma (fragrant), because of their pleasant smell. Aromatic hydrocarbons, were typically obtained by treatment of pleasant-smelling plant extracts. Another name for aromatic hydrocarbons is arenes. Benzene (C₆H₆) is the parent member of this class and hence aromatic is the term used for benzene and all those compounds that resemble benzene in their chemical properties. Over time, chemists discovered that many derivatives of benzene are, in fact, odorless. Nevertheless, the term aromatic is still used to describe all derivatives of benzene, regardless of whether they are fragrant or odourless. Examples of some aromatic hydrocarbons are given below.',
    'خوش گوار بو کی وجہ سے ارومیٹک کی اصطلاح یونانی لفظ اروما (خوشبودار) سے اخذ ہوئی۔ ارومیٹک ہائیڈروکاربن عموماً خوشبودار پودوں کے عصاروں کے عمل سے حاصل کیے جاتے تھے۔ ارومیٹک ہائیڈروکاربنوں کا دوسرا نام ایرینز ہے۔ بینزین (C₆H₆) اس جماعت کا بنیادی رکن ہے، اس لیے ارومیٹک کی اصطلاح بینزین اور ان تمام مرکبات کے لیے استعمال ہوتی ہے جو اپنی کیمیائی خصوصیات میں بینزین سے مشابہ ہوں۔ وقت گزرنے کے ساتھ کیمیادانوں نے دریافت کیا کہ بینزین کے بہت سے مشتقات درحقیقت بے بو ہیں۔ اس کے باوجود، بینزین کے تمام مشتقات کو بیان کرنے کے لیے اب بھی ارومیٹک کی اصطلاح استعمال ہوتی ہے، خواہ وہ خوشبودار ہوں یا بے بو۔ بعض ارومیٹک ہائیڈروکاربنوں کی مثالیں ذیل میں دی گئی ہیں۔',
    'د اروماتیک اصطلاح د دوی د خوږ بوی له امله له یوناني کلمې اروما (خوشبویه) څخه اخیستل شوې ده. اروماتیک هایدروکاربنونه عموماً د خوشبویه نباتي عصارو له پروسس څخه ترلاسه کېدل. د اروماتیک هایدروکاربنونو بل نوم ارینونه دی. بینزین (C₆H₆) د دې ډلې بنسټیز غړی دی، نو اروماتیک اصطلاح د بینزین او ټولو هغو مرکباتو لپاره کارېږي چې په کیمیاوي ځانګړنو کې له بینزین سره ورته وي. د وخت په تېرېدو کیمیاپوهانو وموندله چې د بینزین ډېر مشتقات په حقیقت کې بې بویه دي. سره له دې، اروماتیک اصطلاح لا هم د بینزین د ټولو مشتقاتو د بیان لپاره کارېږي، که خوشبویه وي او که بې بویه. د ځینو اروماتیک هایدروکاربنونو بېلګې لاندې ورکړل شوې دي.')
figure('aromatics')
add('16.2 Alkanes and Cycloalkanes','16.2 الکینز اور سائیکلوالکینز','16.2 الکانونه او سایکلوالکانونه','heading')
add('Alkanes are open chain saturated hydrocarbons, which can be represented by the general formula CₙH₂ₙ₊₂ (where “n” is the number of carbon atoms), while cycloalkanes are cyclic saturated hydrocarbons represented by the general formula CₙH₂ₙ (n > 2). It is to be noted from the general formula of cycloalkanes, that there are two hydrogen atoms less than the corresponding alkanes. In cycloalkanes, two carbon atoms of the molecule utilize one of their valency in forming bonds with other carbon atoms for formation of cyclic ring.',
    'الکینز کھلی زنجیر والے سیر شدہ ہائیڈروکاربن ہیں جنہیں عمومی فارمولے CₙH₂ₙ₊₂ سے ظاہر کیا جا سکتا ہے (جہاں “n” کاربن ایٹموں کی تعداد ہے)، جبکہ سائیکلوالکینز حلقوی سیر شدہ ہائیڈروکاربن ہیں جنہیں عمومی فارمولے CₙH₂ₙ (n > 2) سے ظاہر کیا جاتا ہے۔ سائیکلوالکینز کے عمومی فارمولے سے واضح ہے کہ ان میں متعلقہ الکینز کی نسبت ہائیڈروجن کے دو ایٹم کم ہوتے ہیں۔ سائیکلوالکینز میں سالمے کے دو کاربن ایٹم اپنی ایک ایک ظرفیتی قوت دوسرے کاربن ایٹموں سے بند بنانے میں استعمال کرتے ہیں تاکہ حلقہ بن سکے۔',
    'الکانونه د پرانیستې ځنځیر مشبوع هایدروکاربنونه دي چې په عمومي فورمول CₙH₂ₙ₊₂ ښودل کېدای شي (دلته “n” د کاربني اټومونو شمېر دی)، خو سایکلوالکانونه کړیز مشبوع هایدروکاربنونه دي چې په عمومي فورمول CₙH₂ₙ (n > 2) ښودل کېږي. د سایکلوالکانونو له عمومي فورمول څخه باید په پام کې ونیول شي چې د اړوندو الکانونو په پرتله دوه د هایدروجن اټومونه کم لري. په سایکلوالکانونو کې د مالیکول دوه کاربني اټومونه خپل یو یو والنس له نورو کاربني اټومونو سره د تړونونو په جوړولو کې کاروي، څو کړۍ جوړه شي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('An aromatic organic compound is cyclic, planar, fully conjugated compound containing (4n+2) pi electrons; where n should be 0, 1, 2, 3 …',
    'ارومیٹک نامیاتی مرکب حلقوی، مسطح اور مکمل طور پر کنجوگیٹڈ مرکب ہوتا ہے، جس میں (4n+2) پائی الیکٹران ہوتے ہیں؛ جہاں n کی قدر 0، 1، 2، 3 … ہونی چاہیے۔',
    'اروماتیک عضوي مرکب کړیز، هوار او په بشپړ ډول کنجوګېټ شوی مرکب دی چې (4n+2) پای الکترونونه لري؛ دلته n باید 0، 1، 2، 3 … وي.')
add('16.2.1 Nomenclature','16.2.1 نام گذاری','16.2.1 نومول','heading')
add('The naming of organic compounds is called Organic Nomenclature. Nomenclature in organic chemistry is of two types: common (or trivial) and systematic (or IUPAC system). At the beginning of organic chemistry, each new compound was given an individual name, which was based on its source, some property or other trivial reason. For example, the compound HCOOH was given the name formic acid. The name formic acid was derived from Latin word formica meaning ant, because it was obtained from red ants. Such names, which are based on the source of the compounds are called common names or trivial names.',
    'نامیاتی مرکبات کو نام دینے کا عمل نامیاتی نام گذاری کہلاتا ہے۔ نامیاتی کیمیا میں نام گذاری کی دو قسمیں ہیں: عام (یا روایتی) اور منظم (یا IUPAC نظام)۔ نامیاتی کیمیا کے آغاز میں ہر نئے مرکب کو الگ نام دیا جاتا تھا جو اس کے ماخذ، کسی خاصیت یا کسی اور معمولی وجہ پر مبنی ہوتا تھا۔ مثلاً مرکب HCOOH کو فارمک ایسڈ کا نام دیا گیا۔ فارمک ایسڈ کا نام لاطینی لفظ فارمیکا، یعنی چیونٹی، سے اخذ ہوا کیونکہ یہ سرخ چیونٹیوں سے حاصل کیا جاتا تھا۔ ایسے نام جو مرکبات کے ماخذ پر مبنی ہوں، عام یا روایتی نام کہلاتے ہیں۔',
    'د عضوي مرکباتو د نوم ایښودلو عمل عضوي نوم‌اېښودنه بلل کېږي. په عضوي کیمیا کې نومول دوه ډوله دي: عام (یا دودیز) او منظم (یا د IUPAC سیستم). د عضوي کیمیا په پیل کې هر نوي مرکب ته جلا نوم ورکول کېده چې د هغه پر سرچینه، یوې ځانګړنې یا بل ساده دلیل ولاړ و. د بېلګې په توګه، د HCOOH مرکب ته د فارمیک اسید نوم ورکړل شو. د فارمیک اسید نوم له لاتیني کلمې فارمیکا، یعنې مېږي، څخه اخیستل شوی و، ځکه له سرو مېږیانو ترلاسه کېده. داسې نومونه چې د مرکباتو پر سرچینه ولاړ وي، عام یا دودیز نومونه بلل کېږي.')
add('With the increase in the number of organic compounds it became impossible to give names to such a large number of organic compounds. Moreover, trivial names do not give any information about the structure of the compounds. Need was, therefore, felt to name organic compounds in a systematic way. Thus, the “International Union of pure and Applied chemistry” (IUPAC) in 1957, set rules for giving systematic names to organic compounds on the basis of structure. This is known as the IUPAC system of nomenclature.',
    'نامیاتی مرکبات کی تعداد بڑھنے کے ساتھ اتنی بڑی تعداد میں مرکبات کو نام دینا ناممکن ہو گیا۔ مزید یہ کہ روایتی نام مرکبات کی ساخت کے بارے میں کوئی معلومات نہیں دیتے۔ اس لیے نامیاتی مرکبات کو منظم طریقے سے نام دینے کی ضرورت محسوس ہوئی۔ چنانچہ “خالص اور اطلاقی کیمیا کی بین الاقوامی یونین” (IUPAC) نے 1957 میں ساخت کی بنیاد پر نامیاتی مرکبات کو منظم نام دینے کے اصول مقرر کیے۔ اسے نام گذاری کا IUPAC نظام کہتے ہیں۔',
    'د عضوي مرکباتو د شمېر له زیاتېدو سره دومره ډېرو عضوي مرکباتو ته نومونه ورکول ناممکن شول. سربېره پر دې، دودیز نومونه د مرکباتو د جوړښت په اړه هېڅ معلومات نه ورکوي. له همدې امله په منظم ډول د عضوي مرکباتو د نومولو اړتیا احساس شوه. نو “د خالصې او تطبیقي کیمیا نړیوالې اتحادیې” (IUPAC) په 1957 کې د جوړښت پر بنسټ عضوي مرکباتو ته د منظمو نومونو ورکولو اصول وټاکل. دا د نومولو IUPAC سیستم بلل کېږي.')
add('16.2.1.1 Nomenclature of Alkanes','16.2.1.1 الکینز کی نام گذاری','16.2.1.1 د الکانونو نومول','heading')
add('Alkanes are named by both common and IUPAC systems.','الکینز کو عام اور IUPAC دونوں نظاموں کے مطابق نام دیے جاتے ہیں۔','الکانونه د عام او IUPAC دواړو سیستمونو له مخې نومول کېږي.')
add('(a) Common System','(a) عام نظام','(a) عام سیستم','heading')
add('The first four members of the series are named as methane (CH₄), ethane (C₂H₆), propane (C₃H₈) and butane (C₄H₁₀) while the rest are named by using the Greek prefixes that indicate number of carbon atoms in the molecule. Thus the prefix pent (5) is used for the compound having five carbon atoms, hex (6) for six, hept (7) for seven, oct (8) for eight, non (9) for nine and dec (10) for ten carbon atoms. (see table 16.1). The suffix “–ane” should be added with above prefixes for complete name.',
    'اس سلسلے کے پہلے چار ارکان کے نام میتھین (CH₄)، ایتھین (C₂H₆)، پروپین (C₃H₈) اور بیوٹین (C₄H₁₀) ہیں، جبکہ باقیوں کے نام یونانی سابقوں سے رکھے جاتے ہیں جو سالمے میں کاربن ایٹموں کی تعداد ظاہر کرتے ہیں۔ یوں پانچ کاربن ایٹموں والے مرکب کے لیے سابقہ پینٹ (5)، چھ کے لیے ہیکس (6)، سات کے لیے ہیپٹ (7)، آٹھ کے لیے آکٹ (8)، نو کے لیے نون (9) اور دس کاربن ایٹموں کے لیے ڈیک (10) استعمال ہوتا ہے۔ (جدول16.1 دیکھیے)۔ مکمل نام کے لیے ان سابقوں کے ساتھ لاحقہ “–ane” شامل کرنا چاہیے۔',
    'د لړۍ لومړي څلور غړي میتان (CH₄)، ایتان (C₂H₆)، پروپان (C₃H₈) او بیوټان (C₄H₁₀) نومېږي، خو پاتې غړي په یوناني مختاړو نومول کېږي چې په مالیکول کې د کاربني اټومونو شمېر ښيي. نو د پنځو کاربني اټومونو لرونکي مرکب لپاره پینټ (5)، د شپږو لپاره هېکس (6)، د اوو لپاره هېپټ (7)، د اتو لپاره اوکټ (8)، د نهو لپاره نون (9) او د لسو کاربني اټومونو لپاره ډېک (10) مختاړی کارېږي. (جدول16.1 وګورئ). د بشپړ نوم لپاره باید له دغو مختاړو سره “–ane” وروستاړی ورزیات شي.')
add('Table 16.1 Name and Formulae of First 10 Alkanes','جدول16.1 پہلے10 الکینز کے نام اور فارمولے','جدول16.1 د لومړیو10 الکانونو نومونه او فورمولونه')

names=['methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane']
ur_names=['میتھین','ایتھین','پروپین','بیوٹین','پینٹین','ہیکسین','ہیپٹین','آکٹین','نونین','ڈیکین']
ps_names=['میتان','ایتان','پروپان','بیوټان','پینټان','هېکسان','هېپټان','اوکټان','نونان','ډېکان']
formulae=['CH₄','C₂H₆','C₃H₈','C₄H₁₀','C₅H₁₂','C₆H₁₄','C₇H₁₆','C₈H₁₈','C₉H₂₀','C₁₀H₂₂']
def table_rows(labels):
    return [[str(i+1),labels[i],formulae[i],str(i+6),labels[i+5],formulae[i+5]] for i in range(5)]
table_id='chem12-table16-1'
blocks.append({'id':table_id,'headers':['No. of Carbon Atoms','Name','Molecular Formula']*2,'rows':table_rows(names),'translations':[
    {'language':'اردو','headers':['کاربن ایٹموں کی تعداد','نام','سالماتی فارمولا']*2,'rows':table_rows(ur_names)},
    {'language':'پښتو','headers':['د کاربني اټومونو شمېر','نوم','مالیکولي فورمول']*2,'rows':table_rows(ps_names)}]})
layout.append({'type':'sourceDataTable','tableId':table_id})
record=section('16.2','Hydrocarbon types and alkane nomenclature','ہائیڈروکاربن کی اقسام اور الکینز کی نام گذاری','د هایدروکاربنونو ډولونه او د الکانونو نومول',paras,layout,blocks,'102–103')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':55,'printedPages':[102,103]}]
record['sourceContinuesOnPdfPage']=56

if __name__=='__main__':
    save(55,[record],trim=[{'id':'16.3','startsAt':'The prefix n-'}],chapter_number=16)
