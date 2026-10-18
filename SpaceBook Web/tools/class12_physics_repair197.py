"""PDF197 numerical problems4–6 and every printed383 glossary entry."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];QUESTIONS=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
def numerical(n,en,ur,ps,answer):
    qi=add('numberedList',*(f'{n}. '+part for part in [en,ur,ps]));ai=add('paragraph','(Answer: '+answer+')','(جواب: '+answer+')','(ځواب: '+answer+')')
    QUESTIONS.append({'category':'numerical','number':n,'questionIndex':qi,'answerIndex':ai,'answerOrigin':'Printed textbook answer; no worked solution supplied.'})
numerical(4,r'Calculate the total energy released if 1 kg of \({}^{235}\mathrm{U}\) undergoes fission? Taking the disintegration energy per event to be Q = 208MeV.',
 r'اگر1 kg \({}^{235}\mathrm{U}\) انشقاق سے گزرے تو خارج ہونے والی کل توانائی کا حساب لگائیں؟ فی واقعہ ٹوٹ پھوٹ کی توانائی Q = 208MeV لیں۔',
 r'که1 kg \({}^{235}\mathrm{U}\) انشقاق وکړي، خوشې شوې ټوله انرژي حساب کړئ؟ د هرې پېښې د تجزیې انرژي Q = 208MeV ونیسئ.',m(r'5.32\times10^{26}\ \mathrm{MeV}'))
numerical(5,r'Determine the mass of \({}^{6}\mathrm{Li}\) when it is bombarded by deuteron, disintegrating into two alpha particles by release of 22.3 MeV (0.023940 u) energy. The mass of deuteron is 4.002603 u and that of alpha particle is 4.002603 u.',
 r'\({}^{6}\mathrm{Li}\) کی کمیت معلوم کریں، جب اس پر ڈیوٹیرون کی بمباری سے22.3 MeV (0.023940 u) توانائی خارج ہوتی ہے اور یہ دو الفا ذرات میں ٹوٹتا ہے۔ ڈیوٹیرون کی کمیت4.002603 u اور الفا ذرے کی کمیت4.002603 u ہے۔',
 r'د \({}^{6}\mathrm{Li}\) کتله معلومه کړئ، کله چې د ډیوټرون په بمبار سره22.3 MeV (0.023940 u) انرژي خوشې کړي او په دوو الفا ذرو تجزیه شي. د ډیوټرون کتله4.002603 u او د الفا ذرې کتله4.002603 u ده.','6.01504 u')
numerical(6,r'Find the energy released when \(\beta\)-decay changes \({}^{234}\mathrm{Th}\) into \({}^{234}\mathrm{Pa}\). Mass of \({}^{234}\mathrm{Th}=234.0436\ \mathrm{u}\) and \({}^{234}\mathrm{Pa}=234.0428\ \mathrm{u}\).',
 r'جب \(\beta\) زوال \({}^{234}\mathrm{Th}\) کو \({}^{234}\mathrm{Pa}\) میں بدلتا ہے تو خارج ہونے والی توانائی معلوم کریں۔ \({}^{234}\mathrm{Th}=234.0436\ \mathrm{u}\) اور \({}^{234}\mathrm{Pa}=234.0428\ \mathrm{u}\) کی کمیتیں ہیں۔',
 r'کله چې \(\beta\) زوال \({}^{234}\mathrm{Th}\) په \({}^{234}\mathrm{Pa}\) بدل کړي، خوشې شوې انرژي پیدا کړئ. کتلې یې \({}^{234}\mathrm{Th}=234.0436\ \mathrm{u}\) او \({}^{234}\mathrm{Pa}=234.0428\ \mathrm{u}\) دي.','0.26967 MeV')
exercise_end=len(T)
add('heading','GLOSSARY','فرہنگ','وییزه پانګه')
G=[
 ('Atria: the heart is divided into four chambers that are connected by heart valves. The upper two heart chambers are called atria.','اذینے: دل چار خانوں میں تقسیم ہوتا ہے جو دل کے دریچوں سے جڑے ہوتے ہیں۔ دل کے اوپر کے دو خانوں کو اذینے کہتے ہیں۔','دهلېزونه: زړه په څلورو خونو وېشل شوی چې د زړه د والو په وسیله سره نښتي دي. د زړه پورتنۍ دوه خونې دهلېزونه بلل کېږي.'),
 ('Alternating Current: the current that changes its direction many times in a second is called alternating current.','متبادل رو: وہ رو جو ایک سیکنڈ میں کئی بار اپنی سمت بدلتی ہے، متبادل رو کہلاتی ہے۔','متناوب جریان: هغه جریان چې په یوه ثانیه کې څو ځله خپل لوری بدلوي، متناوب جریان بلل کېږي.'),
 ('Ammeter: a device to measure amperes (current).','ایمیٹر: ایمپیئر (رو) ناپنے کا آلہ۔','امپېرمېټر: د امپېرو (جریان) د اندازه کولو وسیله.'),
 ('Ampere: unit of current.','ایمپیئر: رو کی اکائی۔','امپېر: د جریان واحد.'),
 ('Alternator: a device that changes mechanical energy into an alternating current (electrical energy) e.g, an AC generator.','آلٹرنیٹر: ایسا آلہ جو میکانی توانائی کو متبادل رو (برقی توانائی) میں بدلتا ہے، مثلاً AC جنریٹر۔','الټرنېټر: هغه وسیله چې میخانیکي انرژي په متناوب جریان (برېښنايي انرژۍ) بدلوي، لکه AC جنرېټر.'),
 ('Cerebrospinal fluid (CSF): a clear colorless bodily fluid found in the brain and spine.','دماغی نخاعی سیال (CSF): جسم کا شفاف، بے رنگ سیال جو دماغ اور ریڑھ میں پایا جاتا ہے۔','دماغي نخاعي مایع (CSF): د بدن یوه رڼه بې رنګه مایع چې په مغزو او شوکي ستون کې موندل کېږي.'),
 ('Conductor: a material that permits a very free exchange/movement of electrons from one atom to another.','موصل: ایسا مادہ جو الیکٹرانوں کو ایک ایٹم سے دوسرے تک بہت آزادانہ تبادلے یا حرکت کی اجازت دیتا ہے۔','هادي: هغه ماده چې الکټرونونو ته له یوه اټومه بل ته د ډېر آزاد تبادلې یا حرکت اجازه ورکوي.'),
 ('Conventional Flow: this theory states that electrons flow from positive (+) to negative (-) potential.','روایتی بہاؤ: یہ نظریہ بیان کرتا ہے کہ الیکٹران مثبت (+) سے منفی (-) پوٹینشل کی طرف بہتے ہیں۔','دودیز بهیر: دا نظریه وايي چې الکټرونونه له مثبت (+) پوټنشیال څخه منفي (-) پوټنشیال ته بهېږي.'),
 ('Current: the rate of flow of charge.','رو: بار کے بہاؤ کی شرح۔','جریان: د چارج د بهېدو کچه.'),
 ('Direct Current : unidirectional current is called Direct Current.','یک سمتی رو: ایک سمت میں بہنے والی رو کو یک سمتی رو کہتے ہیں۔','مستقیم جریان: یو لوری لرونکی جریان مستقیم جریان بلل کېږي.'),
 ('Dysfunction: abnormality in the function of an organ or part.','فعلی خرابی: کسی عضو یا حصے کے کام میں غیر معمولی حالت۔','دندیزه نیمګړتیا: د یوه غړي یا برخې په فعالیت کې غیر عادي حالت.'),
 ('Dynamoelectric machine: a dynamo or generator','ڈائنامو الیکٹرک مشین: ڈائنامو یا جنریٹر','ډایناموبرېښنايي ماشین: ډاینامو یا جنرېټر'),
 ('Disgorge: taken out from the throat what has been eaten.','اگلنا: کھائی ہوئی چیز کو حلق سے باہر نکالنا۔','بېرته راایستل: له ستوني څخه د خوړل شوي شي راایستل.'),
 ('Dynamo: from the Greek word dynamis, which means power.','ڈائنامو: یونانی لفظ dynamis سے ماخوذ، جس کا مطلب طاقت ہے۔','ډاینامو: له یوناني dynamis کلمې څخه اخیستل شوی چې د ځواک معنا لري.'),
 ('Dynamoelectric: relating to the conversion by induction of mechanical energy into electrical energy or vice versa.','ڈائنامو الیکٹرک: القا کے ذریعے میکانی توانائی کو برقی توانائی، یا برقی توانائی کو میکانی توانائی، میں تبدیل کرنے سے متعلق۔','ډایناموبرېښنايي: د القا له لارې د میخانیکي انرژۍ په برېښنايي انرژۍ یا د هغې په سرچپه بدلون پورې اړوند.'),
 ('Extra-terrestrial sources: sources that are existing or originating outside the limits of the earth.','ماورائے ارض ذرائع: وہ ذرائع جو زمین کی حدود سے باہر موجود ہوں یا وہیں سے پیدا ہوں۔','له ځمکې بهر سرچینې: هغه سرچینې چې د ځمکې له پولو بهر شته یا له هماغه ځایه راپیدا کېږي.'),
 ('Electromagnets : a device consisting of a core of magnetic material surrounded by a coil that create a magnetic field through the application of electricity.','برقی مقناطیس: ایسا آلہ جس میں مقناطیسی مادے کے قلب کے گرد کنڈلی ہوتی ہے جو بجلی لگانے سے مقناطیسی میدان پیدا کرتی ہے۔','برېښنا مقناطیسونه: هغه وسیله چې د مقناطیسي مادې له زړه جوړه ده، یوه پېچکۍ ترې چاپېره وي او د برېښنا په لګولو مقناطیسي ډګر جوړوي.'),
 ('Electromagnetic Induction: the creation of e.m.f. due to relative motion of conductor and magnet.','برق مقناطیسی القا: موصل اور مقناطیس کی نسبتی حرکت سے e.m.f. کا پیدا ہونا۔','برېښنا مقناطیسي القا: د هادي او مقناطیس د نسبي حرکت له امله د e.m.f. رامنځته کېدل.'),
 ('Electroplaque: these are cells used by electric eels, and other fish for electrogenesis.','الیکٹروپلاک: یہ وہ خلیے ہیں جنہیں برقی بام مچھلیاں اور دیگر مچھلیاں بجلی پیدا کرنے کے لیے استعمال کرتی ہیں۔','الکټروپلاک: هغه حجرې دي چې برېښنايي مارکبان او نور کبان یې د برېښنا د تولید لپاره کاروي.'),
 ('Frequency: the number of cycles in one second of alternating current.','تعدد: متبادل رو کے ایک سیکنڈ میں چکروں کی تعداد۔','فریکونسي: د متناوب جریان په یوه ثانیه کې د دورو شمېر.'),
 ('Generator: a device that changes mechanical energy into electrical energy.','جنریٹر: ایسا آلہ جو میکانی توانائی کو برقی توانائی میں بدلتا ہے۔','جنرېټر: هغه وسیله چې میخانیکي انرژي په برېښنايي انرژۍ بدلوي.'),
 ('Insulators: materials that don’t readily give up electrons, thereby restricting the flow of current.','غیر موصل: وہ مواد جو آسانی سے الیکٹران خارج نہیں کرتے اور اس طرح رو کے بہاؤ کو محدود کرتے ہیں۔','عایقونه: هغه مواد چې الکټرونونه په اسانۍ نه خوشې کوي او په دې توګه د جریان بهیر محدودوي.'),
 (r'Peak inverse voltage (PIV): the maximum voltage \(V_{m}\) the diode can withstand during reverse bias is known as peak inverse voltage (PIV).',r'بلند ترین معکوس وولٹیج (PIV): وہ زیادہ سے زیادہ وولٹیج \(V_{m}\) جسے ڈائیوڈ معکوس بائس کے دوران برداشت کر سکتا ہے، بلند ترین معکوس وولٹیج (PIV) کہلاتا ہے۔',r'لوړترین معکوس ولټاژ (PIV): هغه اعظمي ولټاژ \(V_{m}\) چې ډایوډ یې د معکوس بایس پر مهال زغملی شي، لوړترین معکوس ولټاژ (PIV) بلل کېږي.')]
for row in G:add('definition',*row)
def ref(n):return {'pdfPage':197,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-numericals-4-6-and-general-glossary-382-383','title':'Numerical problems4–6 and general glossary','kind':'lesson','pdfPage':197,'printedPage':382,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=[
 'Printed382 numerical5 gives deuteron mass4.002603u, the same as its printed alpha-particle mass; retained, including the source answer6.01504u.',
 'Printed383 Conventional Flow definition states that electrons flow from positive to negative potential; source statement retained with its known direction inconsistency.',
 'Printed382 numerical6 gives masses234.0436u and234.0428u with answer0.26967MeV; the printed answer does not agree with their straightforward mass-difference conversion. All source numbers retained without an invented worked solution.'
]
sec=section(record,T,L,('عددی مسائل4–6 اور عمومی فرہنگ','عددي مسئلې4–6 او عمومي وییزه پانګه'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(382),ref(383)],sourceBlocks=[],sourceQuestions=QUESTIONS,sourceIssues=issues)
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.20','20.21'],exercises=[{'id':'phys20-source-numericals-4-6','title':'Numerical problems4–6','sourceSectionId':record['id'],'sourceIndices':list(range(exercise_end)),'sourceReferences':[ref(382)]}])
    stage_reference(197,record,'Inspected PDF197 and retained alternate printed382/383 scan evidence. Restored all three numerical questions and supplied answers, and all23 separate printed383 glossary entries. Preserved the deuteron mass, conventional-flow statement and numerical6 answer with source flags. Urdu/Pashto translations follow every original entry/question/answer; numerical source content is reused by the exercise view. Removed fully replaced OCR sections20.20–20.21.',issues)
    print('PDF197 source correction staged; printed inconsistencies retained.')
