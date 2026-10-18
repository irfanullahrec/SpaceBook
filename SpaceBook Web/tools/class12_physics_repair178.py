"""PDF178 complete example continuation, assignment and radiation properties."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,svg
from class12_physics_repair177 import record as previous,example_start
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
add('paragraph','(c) The packing fraction (binding fraction) is the binding energy per nucleon, and is given as',
 '(c) پیکنگ کسر (بندشی کسر) فی نیوکلیون بندشی توانائی ہے، اور اسے یوں دیا جاتا ہے',
 '(c) د بسته بندۍ کسر (د تړون کسر) د هر نیوکلیون د تړون انرژي ده او داسې ورکول کېږي')
add('equation',m(r'f=\frac{E_B}{A}')+'     since '+m(r'A=Z+N=11+12=23'),m(r'f=\frac{E_B}{A}')+'     چونکہ '+m(r'A=Z+N=11+12=23'),m(r'f=\frac{E_B}{A}')+'     ځکه چې '+m(r'A=Z+N=11+12=23'))
add('equation','Putting values     '+m(r'f=\frac{186.566}{23}\ \mathrm{MeV}'),'قدریں رکھنے سے     '+m(r'f=\frac{186.566}{23}\ \mathrm{MeV}'),'د ارزښتونو په اېښودلو     '+m(r'f=\frac{186.566}{23}\ \mathrm{MeV}'))
add('equation','therefore     '+m(r'f=8.11\ \mathrm{MeV}')+'     Answer','لہٰذا     '+m(r'f=8.11\ \mathrm{MeV}')+'     جواب','نو     '+m(r'f=8.11\ \mathrm{MeV}')+'     ځواب')
example_end=len(T);assignment_start=len(T)
add('heading','ASSIGNMENT 20.1','مشق20.1','دنده20.1')
add('heading','CARBON NUCLEUS','کاربن کا نیوکلئیس','د کاربن هسته')
assignment=add('paragraph','Find the mass defect, expressed in kilograms, and the binding energy for a carbon-12 nucleus.',
 'کاربن-12 کے نیوکلئیس کا کمیتی نقص، کلوگرام میں، اور بندشی توانائی معلوم کریں۔',
 'د کاربن-12 د هستې د کتلې کسر، په کیلوګرام کې، او د تړون انرژي پیدا کړئ.')
answer=add('paragraph',r'(Answer: 0.098 940 u or \(1.6429\times1028\ \mathrm{kg}\), 92.16 MeV)',r'(جواب:0.098 940 u یا \(1.6429\times1028\ \mathrm{kg}\)،92.16 MeV)',r'(ځواب:0.098 940 u یا \(1.6429\times1028\ \mathrm{kg}\)،92.16 MeV)')
assignment_end=len(T)
add('heading','20.6 RADIOACTIVITY','20.6 تابکاری','20.6 راډیواکټیفیت')
add('definition','The spontaneous release of subatomic particles or gamma rays by unstable atoms as their nuclei decay to attain stability is called radioactivity. The element which possess such property is called radioactive element.',
 'غیر مستحکم ایٹموں کے نیوکلئیسوں کے استحکام حاصل کرنے کے لیے زوال کے دوران ذیلی ایٹمی ذرات یا گاما شعاعوں کے خودبخود اخراج کو تابکاری کہتے ہیں۔ جس عنصر میں یہ خاصیت ہو وہ تابکار عنصر کہلاتا ہے۔',
 'له ناپایدارو اټومونو څخه د فرعي اټومي ذرو یا ګاما وړانګو خپل سری خپرېدل، کله چې هستې یې د پایدارۍ د ترلاسه کولو لپاره زوال کوي، راډیواکټیفیت بلل کېږي. هغه عنصر چې دا ځانګړنه لري، راډیواکټیف عنصر بلل کېږي.')
add('paragraph',r'In order to attain stability element emit three types of radiation: alpha (\(\alpha\)), in which the emitted particles are \({}^{4}\mathrm{He}\) nuclei; beta (\(\beta\)), in which the emitted particles are either electrons or positrons; and gamma (\(\gamma\)), in which the emitted ‘rays’ are high-energy photons.',
 r'استحکام حاصل کرنے کے لیے عنصر تابکاری کی تین اقسام خارج کرتا ہے: الفا (\(\alpha\))، جس میں خارج ہونے والے ذرات \({}^{4}\mathrm{He}\) کے نیوکلئیس ہوتے ہیں؛ بیٹا (\(\beta\))، جس میں خارج ہونے والے ذرات الیکٹران یا پوزیٹران ہوتے ہیں؛ اور گاما (\(\gamma\))، جس میں خارج ہونے والی ’’شعاعیں‘‘ زیادہ توانائی کے فوٹون ہوتی ہیں۔',
 r'د پایدارۍ د ترلاسه کولو لپاره عنصر درې ډوله وړانګې خپروي: الفا (\(\alpha\)) چې خپرېدونکې ذرې یې د \({}^{4}\mathrm{He}\) هستې دي؛ بېټا (\(\beta\)) چې خپرېدونکې ذرې یې الکترونونه یا پوزیترونونه دي؛ او ګاما (\(\gamma\)) چې خپرېدونکې «وړانګې» یې د لوړې انرژۍ فوټونونه دي.')
add('paragraph','Among about 3000 known nuclides, only 257 are stable. The time scale of these decay processes ranges from a small fraction of a microsecond to billions of years.',
 'تقریباً3000 معلوم نیوکلائیڈز میں سے صرف257 مستحکم ہیں۔ ان زوال کے عملوں کا زمانی پیمانہ مائیکرو سیکنڈ کے ایک چھوٹے حصے سے اربوں سال تک ہے۔',
 'له شاوخوا3000 پېژندل شوو نوکلایډونو څخه یوازې257 پایدار دي. د دې زوال بهیرونو زماني کچه د یوې مایکروثانیې له وړې برخې څخه تر میلیاردونو کلونو پورې ده.')
add('paragraph',r'When the radiation from a radioactive sample is directed into a region in which there is either an electric or a magnetic field as shown in Figure 20.7, we can separate it into three forms of radiation alpha (\(\alpha\)), beta (\(\beta\)) and gamma (\(\gamma\)). Table 20.3 gives properties of these radiations you studied in grade 10.',
 r'جب تابکار نمونے کی تابکاری کو ایسے خطے میں بھیجا جائے جہاں برقی یا مقناطیسی میدان ہو، جیسا کہ شکل20.7 میں دکھایا گیا ہے، تو ہم اسے تابکاری کی تین صورتوں الفا (\(\alpha\))، بیٹا (\(\beta\)) اور گاما (\(\gamma\)) میں الگ کر سکتے ہیں۔ جدول20.3 ان شعاعوں کی وہ خصوصیات دیتا ہے جو آپ نے جماعت10 میں پڑھی تھیں۔',
 r'کله چې د راډیواکټیف نمونې وړانګې داسې سیمې ته واستول شي چې برېښنايي یا مقناطیسي میدان ولري، لکه په20.7 شکل کې چې ښودل شوي، موږ یې په دریو بڼو، الفا (\(\alpha\))، بېټا (\(\beta\)) او ګاما (\(\gamma\))، بېلولی شو.20.3 جدول د دې وړانګو هغه ځانګړنې ورکوي چې تاسو په10 ټولګي کې لوستې وې.')
add('heading','FIGURE 20.7','شکل20.7','شکل20.7')
L.append({'type':'visual','blockId':'phys20-178-radiation-fields'})
add('paragraph','(a) Alpha, Beta and Gamma rays in electric field','(a) برقی میدان میں الفا، بیٹا اور گاما شعاعیں','(a) په برېښنايي میدان کې الفا، بېټا او ګاما وړانګې')
add('paragraph','(b) Alpha, Beta and Gamma rays in magnetic field','(b) مقناطیسی میدان میں الفا، بیٹا اور گاما شعاعیں','(b) په مقناطیسي میدان کې الفا، بېټا او ګاما وړانګې')
add('heading','TABLE 20.3 RADIOACTIVE EMISSIONS','جدول20.3 تابکار اخراج','جدول20.3 راډیواکټیف خپرېدنې')
rows=[
 (['Emission','Description','Rest mass (in u)','Charge','Penetrating power','Relative ionizing ability'],['اخراج','تفصیل','سکونی کمیت (u میں)','بار','نفوذ کی قوت','نسبتی آئن سازی کی صلاحیت'],['خپرېدنه','تشریح','د سکون کتله (په u)','چارج','د نفوذ وړتیا','د آیون جوړولو نسبي وړتیا']),
 ([r'Alpha (\(\alpha\))','Helium nuclei (two protons and two neutrons)','4.002603','+2','Stopped by sheet of paper','highest'],[r'الفا (\(\alpha\))','ہیلیم کے نیوکلئیس (دو پروٹون اور دو نیوٹرون)','4.002603','+2','کاغذ کی چادر روک دیتی ہے','سب سے زیادہ'],[r'الفا (\(\alpha\))','د هیلیم هستې (دوه پروتونونه او دوه نیوټرونونه)','4.002603','+2','د کاغذ پاڼه یې بندوي','تر ټولو لوړه']),
 ([r'Beta (\(\beta\))','electrons or positrons','0.000594','-1, +1','several millimetres of aluminum','medium'],[r'بیٹا (\(\beta\))','الیکٹران یا پوزیٹران','0.000594','-1, +1','ایلومینیم کے کئی ملی میٹر','درمیانی'],[r'بېټا (\(\beta\))','الکترونونه یا پوزیترونونه','0.000594','-1, +1','د المونیم څو ملي متره','منځنۍ']),
 ([r'Gamma (\(\gamma\))','short wavelength electromagnetic radiations','0','0','several centimetres of lead','lowest'],[r'گاما (\(\gamma\))','چھوٹے طولِ موج کی برقی مقناطیسی شعاعیں','0','0','سیسے کے کئی سینٹی میٹر','سب سے کم'],[r'ګاما (\(\gamma\))','د لنډ څپې اوږدوالي برېښنا مقناطیسي وړانګې','0','0','د سربو څو سانتي متره','تر ټولو ټیټه'])]
start=len(T)
for row in rows:ROWS[len(T)]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':list(range(start,len(T)))})
WORDS={
 'en':[['Photographic plate'],['Negative'],['Positive'],['Lead','cylinder'],['Evacuated','chamber'],['Radioactive','material'],['Magnetic field','into the paper']],
 'ur':[['فوٹوگرافی پلیٹ'],['منفی'],['مثبت'],['سیسے کا','بیلن'],['ہوا سے خالی','خانہ'],['تابکار','مادہ'],['مقناطیسی میدان','کاغذ کے اندر']],
 'ps':[['عکاسي تخته'],['منفي'],['مثبت'],['د سربو','سلنډر'],['تشه','خونه'],['راډیواکټیف','ماده'],['مقناطیسي میدان','د کاغذ دننه']]}
def lines(x,y,v):return ''.join(text(x,y+i*22,s,17) for i,s in enumerate(v))
def fields(lang):
    b='';w=WORDS[lang]
    for offset,magnetic in [(0,False),(480,True)]:
        b+=f'<g transform="translate({offset} 0)"><path d="M112 65H346V334H279V418H207V334H112Z" fill="#fff" stroke="#172033" stroke-width="2"/><rect x="112" y="65" width="234" height="13" fill="#fde047" stroke="#172033"/><path d="M188 334H222V391H258V334H292V440H188Z" fill="#334155" stroke="#172033"/><path d="M224 395l5 -10 7 5 5 -9 8 8 7 -4 2 10Z" fill="#ef4444"/>'
        if magnetic:
            for x in range(144,329,27):
                for y in range(126,316,29):b+=f'<path d="M{x-3} {y-3}l6 6m-6 0l6 -6" stroke="#0e7490" stroke-width="1.5"/>'
            b+=lines(75,206,w[6])
        else:
            b+='<rect x="186" y="213" width="6" height="93" fill="#fb7185" stroke="#334155"/><rect x="286" y="213" width="6" height="93" fill="#7dd3fc" stroke="#334155"/>'
            b+=lines(176,190,w[1])+lines(296,190,w[2])
        b+='<path d="M240 393Q238 245 195 78M240 393V78M240 393Q276 114 340 78" fill="none" stroke="#172033" stroke-width="3"/>'+text(188,108,'α',19)+text(251,108,'γ',19)+text(309,115,'β',19)
        b+='<path d="M150 385H188M326 348L310 320M313 422L260 395" stroke="#475569" fill="none"/>'
        b+=lines(231,39,w[0])+lines(132,370,w[3])+lines(366,359,w[4])+lines(363,418,w[5])+text(239,483,'(b)' if magnetic else '(a)',21)+'</g>'
    return svg(b,950,511,{'en':'Figure20.7: alpha bends slightly towards the negative electric plate or left in an into-page magnetic field; beta bends more towards the positive plate or right; gamma remains straight. Both panels retain photographic plate, evacuated chamber, lead cylinder and radioactive source.','ur':'شکل20.7: الفا برقی میدان میں منفی پلیٹ یا کاغذ کے اندر مقناطیسی میدان میں بائیں طرف قدرے مڑتی ہے؛ بیٹا مثبت پلیٹ یا دائیں طرف زیادہ مڑتی ہے؛ گاما سیدھی رہتی ہے۔ دونوں حصوں میں فوٹوگرافی پلیٹ، خالی خانہ، سیسے کا بیلن اور تابکار مادہ محفوظ ہیں۔','ps':'شکل20.7: الفا منفي برېښنايي تختې ته یا د کاغذ دننه مقناطیسي میدان کې کیڼ لور ته لږ کږېږي؛ بېټا مثبتې تختې یا ښي لور ته ډېر کږېږي؛ ګاما مستقیمه پاتې کېږي. دواړه برخې عکاسي تخته، تشه خونه، د سربو سلنډر او راډیواکټیف ماده لري.'}[lang])
def ref(n):return {'pdfPage':178,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-radioactivity-and-alpha-beta-gamma-properties-344-345','title':'Radioactivity and alpha, beta and gamma radiation','kind':'lesson','pdfPage':178,'printedPage':344,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['Assignment20.1 prints “1.6429×1028kg” with1028 on the baseline rather than a negative exponent. The malformed printed value is retained; no exponent has been silently supplied.','Table20.3 beta rest mass is0.000594u, whereas Table20.1 electron mass is0.0005485u. Both source values retained.']
sec=section(record,T,L,('تابکاری اور الفا، بیٹا اور گاما شعاعیں','راډیواکټیفیت او الفا، بېټا او ګاما وړانګې'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(344),ref(345)],sourceIssues=issues,sourceTableRows=ROWS,sourceBlocks=[{'id':'phys20-178-radiation-fields','type':'figure','sourceFigure':'20.7','svg':fields('en'),'svgUrdu':fields('ur'),'svgPashto':fields('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.5'],worked_examples=[{'id':'textbook-example-1','title':'EXAMPLE20.1 — SODIUM NUCLEUS','sourceParts':[{'sectionId':previous['id'],'indices':list(range(example_start,len(previous['paragraphs'])))},{'sectionId':record['id'],'indices':list(range(example_end))}],'answer':r'\(\Delta m=0.200286\mathrm{u}; E_B=186.566\mathrm{MeV}; f=8.11\mathrm{MeV}\) (printed results; inconsistent proton input retained).','sourceContinuationPending':None,'sourceReferences':[{'pdfPage':177,'printedPage':343,'sourcePdf':SOURCE},ref(344)]}],exercises=[{'id':'phys20-assignment-20-1','title':'ASSIGNMENT20.1 — CARBON NUCLEUS','problem':T[assignment][0],'answer':T[answer][0],'sourceSectionId':record['id'],'sourceIndices':list(range(assignment_start,assignment_end)),'sourceReferences':[ref(344)]}])
    stage_reference(178,record,'Reinspected PDF178 printed344–345. Full Example20.1(c) connected to(a/b) in canonical example view. Assignment20.1 retains its malformed printed kg answer. Restored full radioactivity definition/three paragraphs; Figure20.7 both electric and into-page magnetic panels with all labels/three paths; complete six-column emission table. All Urdu/Pashto translations supplied. Beta mass inconsistency retained; covered legacy20.5 retired.',issues)
    print('PDF178 full example continuation, assignment, radiation figure/table staged.')
