from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_page013 import SOURCE, svg

QUESTIONS = [
 ('A charge Q is divided into two parts q and Q−q and separated by a distance R. The force of repulsion between them is maximum when:', ['A. q=Q/4','B. q=Q/3','C. q=Q/2','D. q=Q'], 'ایک بار Q کو دو حصوں q اور Q−q میں تقسیم کر کے ان کے درمیان فاصلہ R رکھا جاتا ہے۔ ان کے درمیان دفع کی قوت کب زیادہ سے زیادہ ہوگی؟', ['A. q=Q/4','B. q=Q/3','C. q=Q/2','D. q=Q'], 'یو چارج Q په q او Q−q دوو برخو وېشل کېږي او ترمنځ یې د R واټن وي. د دوی ترمنځ د دفع قوې اندازه کله اعظمي وي؟', ['A. q=Q/4','B. q=Q/3','C. q=Q/2','D. q=Q']),
 ('Three objects are brought close to each other, two at a time. A and B attract, while B and C repel. From this, we conclude that:', ['A. A and C have charges of the same sign.','B. A and C have charges of opposite signs.','C. all three objects have charges of the same sign.','D. one of the objects is neutral.'], 'تین اجسام کو باری باری دو دو کر کے قریب لایا جاتا ہے۔ A اور B ایک دوسرے کو کھینچتے ہیں، جبکہ B اور C ایک دوسرے کو دفع کرتے ہیں۔ اس سے نتیجہ نکلتا ہے کہ:', ['A. A اور C کے بار ہم علامت ہیں۔','B. A اور C کے بار مخالف علامت ہیں۔','C. تینوں اجسام کے بار ہم علامت ہیں۔','D. ایک جسم غیر باردار ہے۔'], 'درې جسمونه په وار سره دوه دوه یو بل ته نږدې کېږي. A او B یو بل جذبوي، خو B او C یو بل دفع کوي. له دې څخه پایله اخلو چې:', ['A. د A او C چارجونه هم‌نښه دي.','B. د A او C چارجونه مخالف‌نښه دي.','C. د درې واړو جسمونو چارجونه هم‌نښه دي.','D. له جسمونو یو بې‌چارج دی.']),
 (r'Object A has a charge of \(+2\,\mu\mathrm C\), and object B has a charge of \(+6\,\mu\mathrm C\). Which statement is true about the electric forces on the objects?', [r'A. \(F_{AB}=-3F_{BA}\)',r'B. \(F_{AB}=-F_{BA}\)',r'C. \(3F_{AB}=-F_{BA}\)',r'D. \(F_{AB}=3F_{BA}\)'], r'جسم A پر \(+2\,\mu\mathrm C\) اور جسم B پر \(+6\,\mu\mathrm C\) بار ہے۔ اجسام پر برقی قوتوں کے بارے میں کون سا بیان درست ہے؟', [r'A. \(F_{AB}=-3F_{BA}\)',r'B. \(F_{AB}=-F_{BA}\)',r'C. \(3F_{AB}=-F_{BA}\)',r'D. \(F_{AB}=3F_{BA}\)'], r'A جسم \(+2\,\mu\mathrm C\) او B جسم \(+6\,\mu\mathrm C\) چارج لري. پر جسمونو د برېښنايي قوو په اړه کومه وینا سمه ده؟', [r'A. \(F_{AB}=-3F_{BA}\)',r'B. \(F_{AB}=-F_{BA}\)',r'C. \(3F_{AB}=-F_{BA}\)',r'D. \(F_{AB}=3F_{BA}\)']),
 ('Some charge is given to a conductor. Its potential:', ['A. is maximum at the surface.','B. is maximum at the centre.','C. remains the same throughout the conductor.','D. is maximum somewhere between the surface and centre.'], 'ایک موصل کو کچھ بار دیا جاتا ہے۔ اس کا پوٹینشل:', ['A. سطح پر زیادہ سے زیادہ ہوتا ہے۔','B. مرکز پر زیادہ سے زیادہ ہوتا ہے۔','C. پورے موصل میں یکساں رہتا ہے۔','D. سطح اور مرکز کے درمیان کہیں زیادہ سے زیادہ ہوتا ہے۔'], 'یو هادي ته چارج ورکول کېږي. پوتنشیال یې:', ['A. پر سطح اعظمي وي.','B. په مرکز کې اعظمي وي.','C. په ټول هادي کې یو شان پاتې کېږي.','D. د سطحې او مرکز ترمنځ په کوم ځای کې اعظمي وي.']),
 ('The unit of electric field intensity is:', ['A. volt/metre','B. newton/coulomb','C. joule/(coulomb·metre)','D. volt·metre'], 'د برقی میدان شدت کی اکائی ہے:', ['A. وولٹ/میٹر','B. نیوٹن/کولومب','C. جول/(کولومب·میٹر)','D. وولٹ·میٹر'], 'د برېښنايي میدان د شدت واحد دی:', ['A. ولټ/متر','B. نیوټن/کولمب','C. جول/(کولمب·متر)','D. ولټ·متر']),
 (r'A proton is about 1840 times heavier than an electron. When it is accelerated by a potential difference of \(1\,\mathrm{kV}\), its kinetic energy will be:', [r'A. \(1840\,\mathrm{keV}\)',r'B. \(\frac1{1840}\,\mathrm{keV}\)',r'C. \(1\,\mathrm{keV}\)',r'D. \(920\,\mathrm{keV}\)'], r'پروٹون الیکٹران سے تقریباً 1840 گنا بھاری ہے۔ جب اسے \(1\,\mathrm{kV}\) کے فرقِ پوٹینشل سے تیز کیا جائے تو اس کی حرکی توانائی ہوگی:', [r'A. \(1840\,\mathrm{keV}\)',r'B. \(\frac1{1840}\,\mathrm{keV}\)',r'C. \(1\,\mathrm{keV}\)',r'D. \(920\,\mathrm{keV}\)'], r'پروټون د الکترون په پرتله شاوخوا 1840 ځله دروند دی. که د \(1\,\mathrm{kV}\) پوتنشیالي توپیر په وسیله چټک شي، حرکي انرژي به یې وي:', [r'A. \(1840\,\mathrm{keV}\)',r'B. \(\frac1{1840}\,\mathrm{keV}\)',r'C. \(1\,\mathrm{keV}\)',r'D. \(920\,\mathrm{keV}\)']),
 (r'The electric field at a distance of 20 cm from a \(2\,\mu\mathrm C\) charge is:', [r'A. \(3\times10^5\,\mathrm N\)',r'B. \(3\times10^3\,\mathrm N\)',r'C. \(9\times10^3\,\mathrm N\)',r'D. \(9\times10^5\,\mathrm N\)'], r'\(2\,\mu\mathrm C\) بار سے 20 سینٹی میٹر فاصلے پر برقی میدان ہے:', [r'A. \(3\times10^5\,\mathrm N\)',r'B. \(3\times10^3\,\mathrm N\)',r'C. \(9\times10^3\,\mathrm N\)',r'D. \(9\times10^5\,\mathrm N\)'], r'له \(2\,\mu\mathrm C\) چارج څخه د 20 سانتي‌متره په واټن کې برېښنايي میدان دی:', [r'A. \(3\times10^5\,\mathrm N\)',r'B. \(3\times10^3\,\mathrm N\)',r'C. \(9\times10^3\,\mathrm N\)',r'D. \(9\times10^5\,\mathrm N\)']),
 (r'A charge q is placed at the centre of a cube of side a. The electric flux through one side will be:', [r'A. \(\frac{q}{6\epsilon_0}\)',r'B. \(\frac{q}{\epsilon_0a^2}\)',r'C. \(\frac{q}{4\pi\epsilon_0}\)',r'D. \(\frac{q}{\epsilon_0}\)'], r'ایک بار q کو ضلع a والے مکعب کے مرکز پر رکھا جائے۔ اس کے ایک رخ سے برقی فلوکس ہوگا:', [r'A. \(\frac{q}{6\epsilon_0}\)',r'B. \(\frac{q}{\epsilon_0a^2}\)',r'C. \(\frac{q}{4\pi\epsilon_0}\)',r'D. \(\frac{q}{\epsilon_0}\)'], r'q چارج د a ضلع لرونکي مکعب په مرکز کې اېښودل شوی. د یوه مخ له لارې برېښنايي فلوکس به وي:', [r'A. \(\frac{q}{6\epsilon_0}\)',r'B. \(\frac{q}{\epsilon_0a^2}\)',r'C. \(\frac{q}{4\pi\epsilon_0}\)',r'D. \(\frac{q}{\epsilon_0}\)']),
 ('The electric flux through the surface of a sphere due to a charge q placed at its centre depends upon:', ['A. the radius of the sphere.','B. the quantity of charge outside the sphere.','C. the surface area of the sphere.','D. the quantity of charge inside the sphere.'], 'مرکز پر رکھے بار q کے باعث کرہ کی سطح سے گزرنے والا برقی فلوکس کس پر منحصر ہے؟', ['A. کرہ کے رداس پر۔','B. کرہ سے باہر کے بار کی مقدار پر۔','C. کرہ کے سطحی رقبے پر۔','D. کرہ کے اندر کے بار کی مقدار پر۔'], 'د کرې په مرکز کې د q چارج له امله د کرې له سطحې برېښنايي فلوکس پر څه شي پورې اړه لري؟', ['A. د کرې پر شعاع.','B. له کرې بهر د چارج پر مقدار.','C. د کرې پر سطحي مساحت.','D. د کرې دننه د چارج پر مقدار.']),
 (r'A one-microfarad capacitor of a TV is subjected to a 4000 V potential difference. The energy stored in the capacitor is:', [r'A. \(8\,\mathrm J\)',r'B. \(16\,\mathrm J\)',r'C. \(4\times10^{-3}\,\mathrm J\)',r'D. \(2\times10^{-3}\,\mathrm J\)'], r'ٹی وی کا ایک مائیکروفیراڈ کیپیسٹر 4000 وولٹ کے فرقِ پوٹینشل سے جوڑا جاتا ہے۔ اس میں ذخیرہ توانائی ہے:', [r'A. \(8\,\mathrm J\)',r'B. \(16\,\mathrm J\)',r'C. \(4\times10^{-3}\,\mathrm J\)',r'D. \(2\times10^{-3}\,\mathrm J\)'], r'د ټلویزیون یو مایکروفارډ کپاسیټر د 4000 ولټه پوتنشیالي توپیر لاندې دی. په کپاسیټر کې زېرمه شوې انرژي ده:', [r'A. \(8\,\mathrm J\)',r'B. \(16\,\mathrm J\)',r'C. \(4\times10^{-3}\,\mathrm J\)',r'D. \(2\times10^{-3}\,\mathrm J\)']),
 (r'In the figure below, the charge on the \(3\,\mu\mathrm F\) capacitor is:', [r'A. \(5\,\mu\mathrm F\)',r'B. \(10\,\mu\mathrm F\)',r'C. \(3\,\mu\mathrm F\)',r'D. \(6\,\mu\mathrm F\)'], r'ذیل کی شکل میں \(3\,\mu\mathrm F\) کیپیسٹر پر بار ہے:', [r'A. \(5\,\mu\mathrm F\)',r'B. \(10\,\mu\mathrm F\)',r'C. \(3\,\mu\mathrm F\)',r'D. \(6\,\mu\mathrm F\)'], r'په لاندې شکل کې پر \(3\,\mu\mathrm F\) کپاسیټر چارج دی:', [r'A. \(5\,\mu\mathrm F\)',r'B. \(10\,\mu\mathrm F\)',r'C. \(3\,\mu\mathrm F\)',r'D. \(6\,\mu\mathrm F\)']),
 ('Two parallel metal plates are 8.00 m apart. The electric field between the plates is uniform, directed toward the right, and has a magnitude of', 'دو متوازی دھاتی پلیٹوں کے درمیان فاصلہ 8.00 میٹر ہے۔ پلیٹوں کے درمیان برقی میدان یکساں ہے، دائیں طرف ہے، اور اس کی شدت ہے', 'دوه موازي فلزي تختې د 8.00 مترو په واټن کې دي. د تختو ترمنځ برېښنايي میدان یوشان دی، ښي لوري ته دی، او اندازه یې ده'),
]

def paragraph(entry, lang):
    if len(entry) == 3:
        return entry[0] if lang == 'en' else entry[1] if lang == 'ur' else entry[2]
    stem = entry[0] if lang == 'en' else entry[2] if lang == 'ur' else entry[4]
    options = entry[1] if lang == 'en' else entry[3] if lang == 'ur' else entry[5]
    return stem + (('\n' + '\n'.join(options)) if options else '')

def capacitor_circuit(lang):
    caption={'en':'Question 11 — series capacitors connected to a 10 V battery','ur':'سوال 11 — سلسلہ وار کیپیسٹر اور 10 وولٹ بیٹری','ps':'11مه پوښتنه — په لړۍ کې کپاسیټرونه او 10 ولټه بېټرۍ'}[lang]
    body='<path d="M65 60H125M139 60H225M239 60H325M339 60H425V250H252M240 250H65V60" fill="none" stroke="#334155" stroke-width="4"/><path d="M125 45V75M139 45V75M225 45V75M239 45V75M325 45V75M339 45V75" stroke="#0f172a" stroke-width="3"/>'
    body+='<text x="103" y="28">2 μF</text><text x="203" y="28">3 μF</text><text x="304" y="28">6 μF</text><circle cx="240" cy="250" r="4" fill="#0f172a"/><circle cx="252" cy="250" r="4" fill="#0f172a"/><text x="205" y="282">+ 10 V −</text>'
    return '<figure>'+svg(body,490,285,'Three capacitors 2 microfarad, 3 microfarad and 6 microfarad in series with a 10 volt battery')+'<figcaption>'+caption+'</figcaption></figure>'

def main():
    translated=[tuple(paragraph(entry,lang) for lang in ('en','ur','ps')) for entry in QUESTIONS]
    record={'id':'phys12-front-exercise11-mcq-pages46-47','title':'Exercise 11 — multiple-choice questions (continued)','kind':'exercise','pdfPage':28,'printedPage':46,'sourcePdf':SOURCE,'paragraphs':[entry[0] for entry in translated]}
    layout=[{'type':'paragraph','indices':[i]} for i in range(10)]+[{'type':'paragraph','indices':[10]},{'type':'visual'},{'type':'paragraph','indices':[11]}]
    item=section(record,translated,layout,('یونٹ 11 کی مشق — کثیر الانتخابی سوالات','د ۱۱م څپرکي تمرین — څو-غوراوي پوښتنې'))
    item.update(kind='exercise',sourceNotes=['Question 12 begins on printed page 47 and continues on PDF page 29.'],sourceReferences=[{'pdfPage':28,'printedPage':46,'sourcePdf':SOURCE},{'pdfPage':28,'printedPage':47,'sourcePdf':SOURCE}])
    item['diagramSvg']=capacitor_circuit('en');item['diagramSvgUrdu']=capacitor_circuit('ur');item['diagramSvgPashto']=capacitor_circuit('ps');item['content']+=item['diagramSvg']
    questions=[]
    for index,entry in enumerate(QUESTIONS,1):
        row={'id':f'textbook-exercise-11-q{index}','qNo':str(index),'question':entry[0],'options':entry[1] if index <= 11 else [],'sourceReferences':[{'pdfPage':28,'printedPage':46 if index <= 6 else 47}], 'solutionOrigin':'not_provided_in_textbook'}
        row['questionUrdu']=entry[2] if index <= 11 else entry[1];row['optionsUrdu']=entry[3] if index <= 11 else []
        row['questionPashto']=entry[4] if index <= 11 else entry[2];row['optionsPashto']=entry[5] if index <= 11 else []
        if index == 11:
            row['diagramSvg']=capacitor_circuit('en')
            row['diagramSvgUrdu']=capacitor_circuit('ur')
            row['diagramSvgPashto']=capacitor_circuit('ps')
            row['sourceClarification']='The printed stem asks for charge, but the answer choices are labeled in μF, a capacitance unit. The source units are preserved.'
        if index == 12:
            row['sourceClarification']='The question ends mid-sentence at the bottom of printed page 47 and continues on the next PDF page.'
        questions.append(row)
    exercise={'id':'textbook-exercise-11-mcq','exercise':'Exercise 11','title':'Exercise 11 — Multiple-choice questions','problems':questions,'sourceReferences':[{'pdfPage':28,'printedPage':46},{'pdfPage':28,'printedPage':47}]}
    upsert([record],[item])
    sync_companions(exercises=[exercise])
    from pathlib import Path
    import json
    progress=json.loads((Path(__file__).resolve().parents[1]/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))
    if progress['nextPage']==28:
        checkpoint(28,'corrected_verified',[record['id']],
          'Original spread rendered at 2.5x and inspected. MCQs 1–11 and the visible beginning of question 12 transcribed in printed order with all choices and paired Urdu/Pashto text. Question 11 capacitor circuit rebuilt as native SVG; its printed charge-versus-μF unit mismatch is recorded. Question 12 is explicitly marked as continuing on PDF page 29; no answers were added.',printed_pages=[46,47])
    elif progress['lastFullyVerifiedPage']<28:
        raise RuntimeError('Unexpected checkpoint state; refusing to advance the review ledger')

if __name__=='__main__':
    main()
