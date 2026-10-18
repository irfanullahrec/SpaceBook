"""PDF184 complete detector continuation, reactions and conservation laws."""
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, arrow, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def eq(s):s=r'\('+s+r'\)';add('equation',s,s,s)
add('paragraph','In the process they ionize other atoms in their path. This results in an avalanche of electrons that produces a pulse at the detection system. Which is amplified and counted by counter and sound is produced.',
 'اس عمل میں وہ اپنے راستے کے دوسرے ایٹموں کو آئن بناتے ہیں۔ اس سے الیکٹرانوں کا ایک ریلا پیدا ہوتا ہے جو کھوجی نظام میں ایک نبض پیدا کرتا ہے۔ اسے تقویت دی جاتی ہے، شمارندہ اسے گنتا ہے اور آواز پیدا ہوتی ہے۔',
 'په دې بهیر کې دوی په خپله لاره کې نور اټومونه آیون کوي. له دې څخه د الکترونونو سېلاب جوړېږي چې د کشف په سیستم کې یوه نبض پیدا کوي. دا نبض پیاوړې کېږي، شمېرونکی یې شمېري او غږ تولیدېږي.')
add('heading','B. SOLID STATE DETECTORS','B. ٹھوس حالت کے کھوجی','B. د جامد حالت کشفوونکي')
add('paragraph','A solid state detector is a device that uses a semiconductor (usually silicon or germanium) to detect charged particles or photons. A solid state detector is usually a reverse bias PN junction diode, connected to the pulse detection system.',
 'ٹھوس حالت کا کھوجی ایسا آلہ ہے جو باردار ذرات یا فوٹونوں کا کھوج لگانے کے لیے نیم موصل (عموماً سلیکان یا جرمینیم) استعمال کرتا ہے۔ ٹھوس حالت کا کھوجی عموماً معکوس بائس والا PN جوڑ ڈائیوڈ ہوتا ہے، جو نبض کا کھوج لگانے والے نظام سے جڑا ہوتا ہے۔',
 'د جامد حالت کشفوونکی هغه وسیله ده چې د چارج لرونکو ذرو یا فوټونونو د کشف لپاره نیمه هادي (معمولاً سیلیکون یا جرمانیم) کاروي. د جامد حالت کشفوونکی معمولاً د معکوس بایس PN پیوند ډایوډ وي چې د نبض د کشف له سیستم سره نښتی وي.')
add('paragraph','A P-N junction of semiconductor is placed under reverse bias, thus no current flows. When ionizing radiation is allowed to pass through the depleted region it excites electrons into the conduction band. Thus electrons are moved towards positive terminal and holes towards negative terminal of battery, causing a temporary conduction as shown in figure 20.14. This electric pulse is then measured through an electric counter. The electronics used to analyze the pulses does more than counting.',
 'نیم موصل کے P-N جوڑ کو معکوس بائس میں رکھا جاتا ہے، اس لیے کوئی رو نہیں بہتی۔ جب آئن ساز تابکاری کو خالی خطے سے گزرنے دیا جاتا ہے تو وہ الیکٹرانوں کو موصل پٹی میں تحریک دیتی ہے۔ یوں الیکٹران بیٹری کے مثبت سرے اور سوراخ منفی سرے کی طرف حرکت کرتے ہیں، جس سے عارضی ترسیل پیدا ہوتی ہے، جیسا کہ شکل20.14 میں دکھایا گیا ہے۔ پھر برقی شمارندے سے اس برقی نبض کی پیمائش کی جاتی ہے۔ نبضوں کے تجزیے کے لیے استعمال ہونے والی برقیات محض گنتی سے زیادہ کام کرتی ہے۔',
 'د نیمه هادي P-N پیوند په معکوس بایس کې اېښودل کېږي، نو جریان نه بهېږي. کله چې آیون جوړوونکو وړانګو ته اجازه ورکړل شي چې له تشې سیمې تېرې شي، الکترونونه د هدایت بانډ ته تحریکوي. په دې توګه الکترونونه د بټرۍ مثبت قطب او تشې منفي قطب ته خوځېږي، چې لنډمهالی هدایت رامنځته کوي، لکه په20.14 شکل کې چې ښودل شوی دی. بیا دا برېښنايي نبض د برېښنايي شمېرونکي په وسیله اندازه کېږي. د نبضونو د تحلیل لپاره کارېدونکې الکترونیکي وسیلې تر شمېرلو زیات کار کوي.')
add('heading','FIGURE 20.14','شکل20.14','شکل20.14')
L.append({'type':'visual','blockId':'phys20-184-semiconductor'})
add('paragraph','Reverse Bias PN Junction Diode','معکوس بائس والا PN جوڑ ڈائیوڈ','د معکوس بایس PN پیوند ډایوډ')
add('paragraph','It separates the pulses into hundreds of groups called channels. Therefore, the equipment is often called multi-channel analyzer.',
 'یہ نبضوں کو سینکڑوں گروہوں میں الگ کرتا ہے، جنہیں چینل کہتے ہیں۔ اس لیے اس سازوسامان کو اکثر کثیر چینلی تجزیہ کار کہا جاتا ہے۔',
 'دا نبضونه په سلګونو ډلو وېشي چې چینلونه بلل کېږي. له همدې امله دې وسیلې ته ډېری وخت څوچینلی تحلیلګر ویل کېږي.')
add('heading','20.11 NUCLEAR REACTIONS','20.11 نیوکلیائی تعاملات','20.11 هستوي تعاملونه')
add('definition','A nuclear reaction is said to occur whenever an incident nucleus, particle, or photon causes a change to occur in a target nucleus.',
 'جب کوئی وارد نیوکلئیس، ذرہ یا فوٹون کسی ہدفی نیوکلئیس میں تبدیلی پیدا کرے تو کہا جاتا ہے کہ نیوکلیائی تعامل واقع ہوا ہے۔',
 'هر کله چې یوه وارده هسته، ذره یا فوټون په یوه هدف هسته کې بدلون راولي، ویل کېږي چې هستوي تعامل رامنځته شوی دی.')
add('paragraph','Such a structural change can be brought about in the nucleus by bombarding the target by sufficiently energetic particle such as neutrons, alpha particles etc. As a results the nucleons are added, removed or rearranged within a target nucleus. A process in which nuclear transmutation is done by bombarding target nuclei with energetic light particles is known as induced nuclear reaction. In such nuclear processes the conservation laws must be followed.',
 'ہدف پر کافی توانائی والے ذرات، مثلاً نیوٹرونوں، الفا ذرات وغیرہ کی بمباری سے نیوکلئیس میں ایسی ساختی تبدیلی پیدا کی جا سکتی ہے۔ نتیجتاً ہدفی نیوکلئیس میں نیوکلیون شامل ہوتے، خارج ہوتے یا دوبارہ ترتیب پاتے ہیں۔ وہ عمل جس میں ہدفی نیوکلئیسوں پر توانائی والے ہلکے ذرات کی بمباری سے نیوکلیائی تبدیلی کی جائے، القائی نیوکلیائی تعامل کہلاتا ہے۔ ایسے نیوکلیائی عملوں میں بقائی قوانین کی پابندی ضروری ہے۔',
 'په هدف د کافي انرژۍ لرونکو ذرو، لکه نیوټرونونو، الفا ذرو او نورو، په بمبار سره په هسته کې دا ډول جوړښتي بدلون راوستل کېدای شي. په پایله کې د هدف په هسته کې نیوکلیونونه ورزیاتېږي، ایستل کېږي یا بیا تنظیمېږي. هغه بهیر چې په کې هدف هستې په انرژي لرونکو سپکو ذرو بمبار او هستوي بدلون پکې رامنځته شي، القايي هستوي تعامل بلل کېږي. په داسې هستوي بهیرونو کې باید د بقا قوانین مراعات شي.')
add('paragraph','When Nucleus X is bombarded with some light particle a the product nucleus Y and light particle b will be obtained by nuclear reaction. Mathematically',
 'جب نیوکلئیس X پر کسی ہلکے ذرے a کی بمباری کی جاتی ہے تو نیوکلیائی تعامل سے حاصل نیوکلئیس Y اور ہلکا ذرہ b ملتے ہیں۔ ریاضی کی صورت میں',
 'کله چې هسته X په یوې سپکې ذرې a بمبار شي، د هستوي تعامل له لارې د محصول هسته Y او سپکه ذره b ترلاسه کېږي. په ریاضي بڼه')
eq(r'a+X\rightarrow Y+b')
add('paragraph',r'In 1919, Ernest Rutherford observed that when an \(\alpha\) particle strikes a nitrogen nucleus, an oxygen nucleus and a proton are produced. This nuclear reaction is written as',
 r'1919 میں ارنسٹ ردرفورڈ نے مشاہدہ کیا کہ جب ایک \(\alpha\) ذرہ نائٹروجن کے نیوکلئیس سے ٹکراتا ہے تو آکسیجن کا نیوکلئیس اور ایک پروٹون پیدا ہوتے ہیں۔ اس نیوکلیائی تعامل کو یوں لکھا جاتا ہے',
 r'په1919 کې ارنسټ رادرفورډ ولیدل چې کله یوه \(\alpha\) ذره د نایتروجن له هستې سره ټکر وکړي، د اکسیجن یوه هسته او یو پروتون تولیدېږي. دا هستوي تعامل داسې لیکل کېږي')
reaction=r'{}^{4}_{2}\mathrm{He}+{}^{14}_{7}\mathrm{N}\rightarrow{}^{17}_{8}\mathrm{O}+{}^{1}_{1}\mathrm{H}+Q'
eq(reaction)
add('paragraph','The energy equivalent of the difference between the rest masses of the elements on both sides of nuclear reaction is called nuclear reaction energy ‘Q’. If ‘Q’ is positive energy is released in the reaction, if ‘Q’ is negative energy is absorbed in the reaction. Few other examples of nuclear reaction are',
 'نیوکلیائی تعامل کے دونوں طرف عناصر کی سکونی کمیتوں کے فرق کے مساوی توانائی کو نیوکلیائی تعامل کی توانائی ‘Q’ کہتے ہیں۔ اگر ‘Q’ مثبت ہو تو تعامل میں توانائی خارج ہوتی ہے، اور اگر ‘Q’ منفی ہو تو تعامل میں توانائی جذب ہوتی ہے۔ نیوکلیائی تعامل کی چند اور مثالیں ہیں',
 'د هستوي تعامل د دواړو خواوو د عناصرو د سکون کتلې د توپیر معادل انرژي د هستوي تعامل انرژي ‘Q’ بلل کېږي. که ‘Q’ مثبت وي، په تعامل کې انرژي خوشې کېږي؛ که ‘Q’ منفي وي، په تعامل کې انرژي جذبېږي. د هستوي تعامل څو نورې بېلګې دا دي')
e1=r'\({}^{1}_{1}\mathrm{H}+{}^{13}_{6}\mathrm{C}\rightarrow{}^{14}_{7}\mathrm{N}+\gamma\)';e2=r'\({}^{1}_{0}\mathrm{n}+{}^{10}_{5}\mathrm{B}\rightarrow{}^{7}_{3}\mathrm{Li}+{}^{4}_{2}\mathrm{He}\)'
add('equation',e1+'     and     '+e2,e1+'     اور     '+e2,e1+'     او     '+e2)
add('heading','CONSERVATION LAWS IN NUCLEAR REACTION','نیوکلیائی تعامل میں بقائی قوانین','په هستوي تعامل کې د بقا قوانین')
add('paragraph','A conservation of physical quantity means that for all the process taking place in a system that particular physical quantity remains constant. The following laws of conservation are obeyed for nuclear processes.',
 'کسی طبعی مقدار کی بقا کا مطلب ہے کہ کسی نظام میں ہونے والے تمام عملوں میں وہ خاص طبعی مقدار مستقل رہتی ہے۔ نیوکلیائی عملوں میں درج ذیل بقائی قوانین کی پابندی ہوتی ہے۔',
 'د یوې فزیکي کمیت بقا دا معنا لري چې په یوه سیستم کې د ترسره کېدونکو ټولو بهیرونو په ترڅ کې هغه ځانګړې فزیکي کمیت ثابت پاتې کېږي. په هستوي بهیرونو کې د بقا لاندې قوانین مراعاتېږي.')
add('paragraph','• Conservation of charge','• بار کی بقا','• د چارج بقا')
add('paragraph','• Conservation of Energy (mass inclusive)','• توانائی کی بقا (کمیت سمیت)','• د انرژۍ بقا (د کتلې په ګډون)')
add('paragraph','• Conservation of linear and angular momentum','• خطی اور زاویائی معیارِ حرکت کی بقا','• د خطي او زاویوي مومنټم بقا')
add('paragraph','• Conservation of nucleon number','• نیوکلیونوں کی تعداد کی بقا','• د نیوکلیونونو د شمېر بقا')
add('paragraph','The two conservation laws will be discussed.','دو بقائی قوانین پر بحث کی جائے گی۔','د بقا پر دوو قوانینو به بحث وشي.')
add('heading','A. CONSERVATION OF NUCLEON NUMBER','A. نیوکلیونوں کی تعداد کی بقا','A. د نیوکلیونونو د شمېر بقا')
add('paragraph','Before and after the reaction the sum of number of protons and neutrons should remain constant.','تعامل سے پہلے اور بعد میں پروٹونوں اور نیوٹرونوں کی تعداد کا مجموعہ مستقل رہنا چاہیے۔','له تعامل مخکې او وروسته باید د پروتونونو او نیوټرونونو د شمېر مجموعه ثابته پاتې شي.')
add('equation','Number of nucleons on LHS - Number of nucleons on RHS','بائیں طرف نیوکلیونوں کی تعداد - دائیں طرف نیوکلیونوں کی تعداد','په کیڼ اړخ کې د نیوکلیونونو شمېر - په ښي اړخ کې د نیوکلیونونو شمېر')
add('paragraph','For example in the reaction','مثلاً تعامل میں','د بېلګې په توګه په تعامل کې')
eq(reaction)
add('paragraph','We can see that on both sides there are (14 + 4 = 17 + 1 = 18) nucleons.','ہم دیکھ سکتے ہیں کہ دونوں طرف (14 + 4 = 17 + 1 = 18) نیوکلیون ہیں۔','موږ لیدلی شو چې په دواړو خواوو کې (14 + 4 = 17 + 1 = 18) نیوکلیونونه شته.')
def detector(lang):
    b='<rect x="142" y="151" width="86" height="138" fill="#fb7185" stroke="#334155" stroke-width="2"/><rect x="228" y="151" width="145" height="138" fill="#cffafe" stroke="#334155" stroke-width="2"/><rect x="373" y="151" width="86" height="138" fill="#f9a8d4" stroke="#334155" stroke-width="2"/>'+text(184,230,'P',30)+text(417,230,'N',30)
    b+='<path d="M142 222H69V420H296M313 420H531V222H459" stroke="#172033" fill="none" stroke-width="3"/><path d="M296 406V434M313 391V449" stroke="#172033" stroke-width="5"/><circle cx="69" cy="222" r="10" fill="#fde68a" stroke="#172033" stroke-width="3"/><circle cx="531" cy="222" r="10" fill="#fde68a" stroke="#172033" stroke-width="3"/>'
    for x in (273,296,319):
        b+=f'<path d="M{x} 18q-14 9 0 18t0 18t0 18t0 18t0 18V146" stroke="#7c2d12" fill="none" stroke-width="3"/>'+arrow(x,127,x,147,'#7c2d12')
    b+=arrow(300,310,232,310,'#172033')+arrow(300,310,369,310,'#172033')+'<path d="M228 299V320M373 299V320" stroke="#172033" stroke-width="2"/>'
    label={'en':'Depletion region','ur':'خالی خطہ','ps':'تشه سیمه'}[lang]
    b+=text(301,350,label,23)
    return svg(b,600,470,{'en':'Figure20.14: incoming radiation reaches the depletion region between P and N; closed circuit connects P to the short negative battery plate and N to the long positive plate, preserving reverse bias.','ur':'شکل20.14: آنے والی تابکاری P اور N کے درمیان خالی خطے تک پہنچتی ہے؛ بند سرکٹ میں P بیٹری کی چھوٹی منفی پلیٹ اور N بڑی مثبت پلیٹ سے جڑا ہے، اس طرح معکوس بائس برقرار ہے۔','ps':'شکل20.14: راتلونکې وړانګې د P او N ترمنځ تشې سیمې ته رسېږي؛ په تړلي سرکټ کې P د بټرۍ له لنډې منفي تختې او N له اوږدې مثبتې تختې سره نښتی دی او معکوس بایس ساتي.'}[lang])
record={'id':'phys20-semiconductor-detectors-nuclear-reactions-conservation-356-357','title':'Semiconductor detectors, nuclear reactions and conservation','kind':'lesson','pdfPage':184,'printedPage':356,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=['The printed nucleon-conservation line uses a dash between “Number of nucleons on LHS” and “Number of nucleons on RHS”, although the surrounding prose states equality. The visible dash is retained.']
sec=section(record,T,L,('نیم موصل کھوجی، نیوکلیائی تعاملات اور بقا','نیمه هادي کشفوونکي، هستوي تعاملونه او بقا'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[{'pdfPage':184,'printedPage':n,'sourcePdf':SOURCE} for n in (356,357)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-184-semiconductor','type':'figure','sourceFigure':'20.14','svg':detector('en'),'svgUrdu':detector('ur'),'svgPashto':detector('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(184,record,'Visually reinspected PDF184 printed356–357. Restored Geiger avalanche continuation, both solid-state detector paragraphs and separate multi-channel paragraph, complete nuclear-reaction definition/explanation, Rutherford equation, both other reaction equations, all four conservation laws and full nucleon example. Figure20.14 reconstructed as a closed reverse-bias PN circuit with incoming radiation and depletion bracket. All prose/labels translated. Printed dash in conservation statement retained and recorded.',issues)
    print('PDF184 complete source and circuit staged.')
