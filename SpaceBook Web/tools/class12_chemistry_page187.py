"""PDF187 printed368–369: Figure 24.5 vibrations, the infrared spectrum, Figures 24.6–24.7 (ethanol, toluene), applications of IR."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
from class12_chemistry_formula import formula_rows
import math
F=Fig('arrow187');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='lines'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
K=lambda lang,*v:v[{'en':0,'ur':1,'ps':2}[lang]]
def vib(lang):
 s=F.start(270)+t(250,20,K(lang,'Stretching vibrations','کھنچاؤ والے ارتعاشات','د کشېدو اهتزازات'),13,'#ad1457')+t(425,140,K(lang,'Bending vibrations','جھکاؤ والے ارتعاشات','د کږېدو اهتزازات'),13,'#ad1457')
 def unit(x,y,lab,arr,signs=None):
  o=line(x,y,x-24,y-30,3,'#777')+line(x,y,x+24,y-30,3,'#777')+line(x,y,x-10,y+16,2,'#999')+line(x,y,x+10,y+16,2,'#999')+f'<circle cx="{x}" cy="{y}" r="9" fill="#bdbdbd" stroke="#555"/><circle cx="{x-24}" cy="{y-30}" r="9" fill="#8e24aa"/><circle cx="{x+24}" cy="{y-30}" r="9" fill="#8e24aa"/>'
  for ax,ay,bx,by in arr:o+=line(x+ax,y+ay,x+bx,y+by,1.5,'#c62828')+f'<circle cx="{x+bx}" cy="{y+by}" r="2.5" fill="#c62828"/>'
  if signs:o+=t(x-40,y-30,signs[0],14)+t(x+40,y-30,signs[1],14)
  return o+t(x,y+36,lab,11)
 s+=unit(180,90,K(lang,'Symmetrical','متشاکل','متناظر'),[(-30,-38,-40,-50),(30,-38,40,-50)])+unit(320,90,K(lang,'Asymmetrical','غیر متشاکل','نامتناظر'),[(-30,-38,-40,-50),(30,-38,20,-26)])
 s+=unit(150,220,K(lang,'Rocking','جھولنا','ټوکېدل'),[(-36,-30,-40,-16),(36,-30,40,-16)])+unit(330,220,K(lang,'Scissoring','قینچی نما','قیچي'),[(-14,-38,-2,-40),(14,-38,2,-40)])
 s+=unit(510,220,K(lang,'Wagging','ہلنا','ښورېدل'),[],('+','+'))+unit(690,220,K(lang,'Twisting','بل کھانا','تاوېدل'),[],('+','–'))
 return s+'</svg>'
def spectrum(lang,dips,labels,title):
 X=lambda nu:60+(4000-nu)/3400*740 if nu>=2000 else 60+2000/3400*740*0.6+(2000-nu)/1400*(740-2000/3400*740*0.6)
 X=lambda nu:60+((4000-nu)/2000*370 if nu>=2000 else 370+(2000-nu)/1400*370)
 s=F.start(250)+f'<rect x="60" y="20" width="740" height="180" fill="none" stroke="#555"/>'
 for nu in (4000,3600,3200,2800,2400,2000,1800,1600,1400,1200,1000,800,600):s+=line(X(nu),20,X(nu),200,0.4,'#ccc')+t(X(nu),214,str(nu),9)
 pts=[]
 for i in range(0,3401):
  nu=4000-i;T=92
  for c,w,d in dips:T-=d*math.exp(-((nu-c)/w)**2)
  pts.append(f'{X(nu):.1f},{20+(100-max(T,2))*1.8:.1f}')
 s+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="#222" stroke-width="1.4"/>'
 for nu,y,lab in labels:s+=t(X(nu),y,lab,10,'#ad1457')
 s+=t(430,238,K(lang,'WAVENUMBERS (cm⁻¹)','ویو نمبر (cm⁻¹)','د موج شمېرې (cm⁻¹)'),11)+f'<text x="30" y="110" transform="rotate(-90 30 110)" text-anchor="middle" font-family="Arial" font-size="10">{K(lang,"% TRANSMITTANCE","% ترسیل","% تېرېدنه")}</text>'+t(560,60,title,13)
 return s+'</svg>'
def ethanol(lang):
 return spectrum(lang,[(3350,180,80),(2970,40,55),(2900,30,35),(1450,25,35),(1380,18,28),(1090,25,55),(1050,20,70),(880,15,25)],
  [(3350,190,K(lang,'O–H stretch H-bonded','O–H کھنچاؤ (H-بند)','O–H کشېدل (H-تړون)')),(2950,175,'sp³ C–H stretch'),(1460,150,'CH₂ bend'),(1380,135,'CH₃ bend'),(1050,190,'C–O stretch'),(1300,110,'O–H ip bend'),(880,120,'O–H oop bend')],'CH₃CH₂OH')
def toluene(lang):
 return spectrum(lang,[(3060,25,40),(3030,20,45),(2920,25,40),(1940,20,15),(1860,20,15),(1600,15,40),(1495,12,60),(1460,12,40),(1080,10,20),(1030,10,30),(730,15,80),(695,12,85)],
  [(3250,165,'sp² C–H stretch'),(2750,135,'sp³ C–H stretch'),(1900,95,K(lang,'mono subst.','یک متبادل','یو بدیل')),(1550,185,K(lang,'aromatic C=C stretch','ارومیٹک C=C کھنچاؤ','اروماتیک C=C کشېدل')),(710,190,K(lang,'mono subst. oop','یک متبادل oop','یو بدیل oop'))],K(lang,'toluene (C₆H₅CH₃)','ٹولوئین (C₆H₅CH₃)','ټولوین (C₆H₅CH₃)'))

visual('chem12-figure24-5',vib)
add('Figure 24.5 Different type of bond vibrations in methylene group.','شکل 24.5 میتھیلین گروپ میں بند کے ارتعاشات کی مختلف اقسام۔','شکل 24.5 په میتیلین ګروپ کې د تړون د اهتزازاتو بېلابېل ډولونه.')
add('The Infrared Spectrum','زیریں سرخ طیف','زیرسره طیف','heading')
add('The plot of wavenumber, cm⁻¹ (or sometimes wavelength in micron, μm) versus percent transmittance (%T) is called Infrared spectrum. This is recorded as percent transmittance because the spectrometer records the ratio of the intensities of the two beams.','ویو نمبر cm⁻¹ (یا بعض اوقات مائیکرون μm میں طولِ موج) اور فیصد ترسیل (%T) کے درمیان گراف کو زیریں سرخ طیف کہتے ہیں۔ اسے فیصد ترسیل کے طور پر ریکارڈ کیا جاتا ہے کیونکہ سپیکٹرومیٹر دو شعاعوں کی شدتوں کا تناسب ریکارڈ کرتا ہے۔','د موج شمېرې cm⁻¹ (یا کله کله په مایکرون μm کې د موج اوږدوالي) او سلنه تېرېدنې (%T) ترمنځ ګراف ته زیرسره طیف وايي. دا د سلنه تېرېدنې په توګه ثبتېږي ځکه سپکټرومیټر د دوو وړانګو د شدتونو نسبت ثبتوي.')
visual('chem12-p187-transmittance',lambda l:formula_rows(F,[(K(l,'percent transmittance (%T) =','فیصد ترسیل (%T) =','سلنه تېرېدنه (%T) ='),[('f','Iₛ','Iᵣ'),('t','× 100','')])],60,x0=520))
add('Where Iₛ is the intensity of the sample beam, and Iᵣ is the intensity of the reference beam. In many parts of the spectrum, the transmittance is nearly 100%, meaning that the sample is nearly transparent (no absorbance) to radiation of that wavenumber.','جہاں Iₛ نمونے کی شعاع کی شدت اور Iᵣ حوالہ شعاع کی شدت ہے۔ طیف کے بہت سے حصوں میں ترسیل تقریباً 100% ہوتی ہے، یعنی نمونہ اس ویو نمبر کی شعاعوں کے لیے تقریباً شفاف (کوئی جذب نہیں) ہے۔','چېرته چې Iₛ د نمونې د وړانګې شدت او Iᵣ د حوالې د وړانګې شدت دی. د طیف په ډېرو برخو کې تېرېدنه نږدې 100% وي، یعنې نمونه د هغې موج شمېرې وړانګو ته نږدې روڼه (بې جذبه) ده.')
add('In using infrared spectroscopy for structure determination, peaks in the range 4000–1500 cm⁻¹ are usually emphasized because this is the region in which the vibrations characteristic of particular functional groups are found and therefore called functional groups region. The region 1500–625 cm⁻¹ is known as the fingerprint region. It is highly unlikely that the IR spectra of two different compounds (except enantiomers) will show the same frequencies for all of their various complex vibrations. Hence, this region of the infrared spectrum provides a “fingerprint” of a molecule. The IR spectra of ethanol and toluene are shown in Figure 24.6 and 24.7.','ساخت کے تعین کے لیے زیریں سرخ سپیکٹروسکوپی کے استعمال میں عموماً 4000–1500 cm⁻¹ کی حد کی چوٹیوں پر زور دیا جاتا ہے کیونکہ یہ وہ خطہ ہے جس میں مخصوص فعلی گروپوں کے امتیازی ارتعاشات پائے جاتے ہیں اس لیے اسے فعلی گروپوں کا خطہ کہتے ہیں۔ 1500–625 cm⁻¹ کے خطے کو فنگر پرنٹ خطہ کہتے ہیں۔ اس کا امکان بہت کم ہے کہ دو مختلف مرکبات (اینینشیومرز کے سوا) کے IR طیف ان کے تمام پیچیدہ ارتعاشات کے لیے یکساں تعدد دکھائیں۔ لہٰذا زیریں سرخ طیف کا یہ خطہ سالمے کا ”فنگر پرنٹ“ مہیا کرتا ہے۔ ایتھانول اور ٹولوئین کے IR طیف شکل 24.6 اور 24.7 میں دکھائے گئے ہیں۔','د جوړښت د ټاکلو لپاره د زیرسره سپکټروسکوپي په کارولو کې معمولاً د 4000–1500 cm⁻¹ پولې په څوکو ټینګار کېږي ځکه دا هغه سیمه ده چې پکې د ځانګړو فعالو ګروپونو ځانګړي اهتزازات موندل کېږي او له همدې امله د فعالو ګروپونو سیمه بلل کېږي. د 1500–625 cm⁻¹ سیمه د ګوتو د نښې سیمه بلل کېږي. ډېر لږ احتمال لري چې د دوو بېلابېلو مرکباتو (پرته له انانټیومرونو) IR طیفونه د خپلو ټولو پېچلو اهتزازاتو لپاره ورته فریکونسۍ وښيي. نو د زیرسره طیف دا سیمه د مالیکول ”د ګوتو نښه“ برابروي. د ایتانول او ټولوین IR طیفونه په شکل 24.6 او 24.7 کې ښودل شوي.')
visual('chem12-figure24-6',ethanol)
add('Figure 24.6 IR spectrum of ethanol.','شکل 24.6 ایتھانول کا IR طیف۔','شکل 24.6 د ایتانول IR طیف.')
visual('chem12-figure24-7',toluene)
add('Figure 24.7 IR spectrum of toluene.','شکل 24.7 ٹولوئین کا IR طیف۔','شکل 24.7 د ټولوین IR طیف.')
add('Applications of Infrared Spectroscopy','زیریں سرخ سپیکٹروسکوپی کے استعمالات','د زیرسره سپکټروسکوپي کارونې','heading')
lines([('i. Infrared spectroscopy gives information about presence of different organic functional groups in a molecule.','i. زیریں سرخ سپیکٹروسکوپی سالمے میں مختلف نامیاتی فعلی گروپوں کی موجودگی کے بارے میں معلومات دیتی ہے۔','i. زیرسره سپکټروسکوپي په مالیکول کې د بېلابېلو عضوي فعالو ګروپونو د شتون په اړه معلومات ورکوي.'),
 ('ii. The identity of a compound can also be established by comparing the finger print region of infrared spectrum with that of a known compound.','ii. زیریں سرخ طیف کے فنگر پرنٹ خطے کا کسی معلوم مرکب سے موازنہ کر کے بھی مرکب کی شناخت قائم کی جا سکتی ہے۔','ii. د زیرسره طیف د ګوتو د نښې سیمې له یوه معلوم مرکب سره په پرتله کولو هم د مرکب هویت ټاکل کېدای شي.'),
 ('iii. The presence of some extra absorption bands, where the compounds does not absorb, shows the presence of impurities. For example the presence of cyclohexanone impurity in cyclohexanol can be readily detected by the intense carbonyl band at 1715 cm⁻¹ in spectrum of cyclohexanol.','iii. کچھ اضافی جذبی پٹیوں کی موجودگی، جہاں مرکب جذب نہیں کرتا، ملاوٹوں کی موجودگی ظاہر کرتی ہے۔ مثلاً سائیکلو ہیکسانول میں سائیکلو ہیکسانون کی ملاوٹ سائیکلو ہیکسانول کے طیف میں 1715 cm⁻¹ پر شدید کاربونل پٹی سے آسانی سے پہچانی جا سکتی ہے۔','iii. د ځینو اضافي جذب بانډونو شتون، چېرې چې مرکب جذب نه کوي، د ناپاکیو شتون ښيي. د بېلګې په توګه په سایکلوهېکسانول کې د سایکلوهېکسانون ناپاکي د سایکلوهېکسانول په طیف کې په 1715 cm⁻¹ کې د شدید کاربونیل بانډ په واسطه په اسانۍ موندل کېدای شي.'),
 ('iv. The progress of most of the reactions can also be monitored using infrared spectroscopy, by taking the spectra of small samples of reaction mixture continuously at suitable intervals of time. For example, in oxidation of cyclohexanol to that of cyclohexanone is accompanied by the disappearance of O–H band near 3600 cm⁻¹, and the appearance of C=O band at 1715 cm⁻¹','iv. مناسب وقفوں سے تعاملی آمیزے کے چھوٹے نمونوں کے طیف مسلسل لے کر زیریں سرخ سپیکٹروسکوپی سے زیادہ تر تعاملات کی پیش رفت کی نگرانی بھی کی جا سکتی ہے۔ مثلاً سائیکلو ہیکسانول کی سائیکلو ہیکسانون میں تکسید کے ساتھ تقریباً 3600 cm⁻¹ کی O–H پٹی غائب اور 1715 cm⁻¹ پر C=O پٹی ظاہر ہوتی ہے','iv. د ډېری تعاملونو پرمختګ هم د زیرسره سپکټروسکوپي په کارولو څارل کېدای شي، په مناسبو وقفو د تعاملي ګډولې د کوچنیو نمونو د طیفونو په دوامداره اخیستلو. د بېلګې په توګه د سایکلوهېکسانول سایکلوهېکسانون ته اکسیډېشن د 3600 cm⁻¹ ته نږدې د O–H بانډ له ورکېدو او په 1715 cm⁻¹ کې د C=O بانډ له ښکارېدو سره مل دی')])
record=section('24.6','IR vibrations, infrared spectra and applications','IR ارتعاشات، زیریں سرخ طیف اور استعمالات','IR اهتزازات، زیرسره طیفونه او کارونې',paras,layout,blocks,'368–369')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':187,'printedPages':[368,369]}]
record['sourceContinuesOnPdfPage']=188
record['sourceIllustrationReview']='Figures 24.6–24.7 recorded IR spectra re-drawn as schematic SVG traces with the printed band labels; band positions approximate the printed charts.'
carry=[{'from':'24.6','to':'24.7','startsAt':'Table 24.2 Infrared Absorption'}]
if __name__=='__main__':save(187,[record],carry=carry,chapter_number=24)
