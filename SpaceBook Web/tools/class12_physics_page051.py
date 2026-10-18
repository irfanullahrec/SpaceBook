"""Sequential source correction for PDF page 51 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(p):return {'pdfPage':51,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 290" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:560px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

FORCE=[
 pair('Mathematically,','ریاضیاتی طور پر،','په ریاضي ډول،'),
 pair('F_B ∝ ILB sin θ','F_B ∝ ILB sin θ','F_B ∝ ILB sin θ'),
 pair('F_B = kILB sin θ','F_B = kILB sin θ','F_B = kILB sin θ'),
 pair('Here the constant of proportionality is k, which in SI units has the numeric value exactly equal to 1; therefore,','یہاں تناسب کا مستقل k ہے، جس کی عددی قدر SI اکائیوں میں ٹھیک 1 ہے؛ لہٰذا،','دلته د تناسب ثابت k دی، چې په SI واحدونو کې یې عددي ارزښت دقیقاً 1 دی؛ نو،'),
 pair('F_B = ILB sin θ ...(13.1)','F_B = ILB sin θ ...(13.1)','F_B = ILB sin θ ...(13.1)'),
 pair('Or in vector form,', 'یا سمتیہ صورت میں،','یا د ویکتور په بڼه،'),
 pair('F⃗_B = ILB sin θ n̂','F⃗_B = ILB sin θ n̂','F⃗_B = ILB sin θ n̂'),
 pair('or', 'یا','یا'),
 pair('F⃗_B = I(L⃗ × B⃗)','F⃗_B = I(L⃗ × B⃗)','F⃗_B = I(L⃗ × B⃗)'),
 pair('This magnetic force F_B is minimum when θ is 0° (as sin 0° = 0). If we keep B, I and L constant, the magnetic force F_B is maximum when θ is 90° (as sin 90° = 1).',
  'یہ مقناطیسی قوت F_B کم سے کم ہوتی ہے جب θ، 0° ہو (کیونکہ sin 0° = 0)۔ اگر B، I اور L مستقل رکھیں تو قوت F_B زیادہ سے زیادہ ہوتی ہے جب θ، 90° ہو (کیونکہ sin 90° = 1)۔',
  'دا مقناطیسي قوه F_B هغه وخت لږترلږه وي چې θ صفر درجې وي (ځکه sin 0° = 0). که B، I او L ثابت وساتو، قوه F_B هغه وخت اعظمي وي چې θ، 90° وي (ځکه sin 90° = 1).'),
 pair('F_B(max) = ILB sin 90°, as sin 90° = 1','F_B(max) = ILB sin 90°، کیونکہ sin 90° = 1','F_B(max) = ILB sin 90°، ځکه sin 90° = 1'),
 pair('F_B(max) = ILB ...(13.2)','F_B(max) = ILB ...(13.2)','F_B(max) = ILB ...(13.2)'),
 pair('FIGURE 13.4 — Conductor in a magnetic field','شکل 13.4 — مقناطیسی میدان میں موصل','13.4 شکل — په مقناطیسي ساحه کې هادي'),
 pair('FIGURE 13.5 — Conductor in a magnetic field','شکل 13.5 — مقناطیسی میدان میں موصل','13.5 شکل — په مقناطیسي ساحه کې هادي'),
]
DIRECTION=[
 pair('As force is a vector quantity, its direction should also be determined.','چونکہ قوت سمتی مقدار ہے، اس لیے اس کی سمت بھی معلوم کرنی چاہیے۔','ځکه قوه ویکتوري کمیت ده، لوری یې هم باید معلوم شي.'),
 pair('The direction of magnetic force F_B on a wire can be determined by Right Hand Rule II and Fleming’s left-hand rule, as shown in Figures 13.6 and 13.7 respectively.',
  'تار پر مقناطیسی قوت F_B کی سمت دایاں ہاتھ قاعدہ II اور فلیمنگ کے بائیں ہاتھ کے قاعدے سے معلوم کی جا سکتی ہے، جیسا کہ بالترتیب شکل 13.6 اور 13.7 میں ہے۔',
  'پر سیم د مقناطیسي قوې F_B لوری د ښي لاس دویم قاعدې او د فلېمینګ د چپ لاس قاعدې له مخې معلومېدای شي، لکه په ترتیب سره په 13.6 او 13.7 شکلونو کې.'),
 pair('The magnetic induction B will be one tesla if a 1 m long wire carrying a current of 1 A is placed perpendicular to the field and the force between them is 1 N. In SI, 1 T = 1 N A⁻¹ m⁻¹. In CGS, 1 G = 10⁻⁴ Tesla.',
  'اگر 1 A برقی رو والی 1 m لمبی تار کو میدان کے عموداً رکھا جائے اور ان کے درمیان قوت 1 N ہو تو مقناطیسی القا B ایک ٹیسلا ہو گا۔ SI میں 1 T = 1 N A⁻¹ m⁻¹۔ CGS میں 1 G = 10⁻⁴ Tesla۔',
  'که د 1 A جریان لرونکی 1 m اوږد سیم د ساحې پر لوري عمود کېښودل شي او د دوی ترمنځ قوه 1 N وي، مقناطیسي القا B به یو ټېسلا وي. په SI کې 1 T = 1 N A⁻¹ m⁻¹. په CGS کې 1 G = 10⁻⁴ Tesla.'),
 pair('1 T = 1 N/(A m)','1 T = 1 N/(A m)','1 T = 1 N/(A m)'),
 pair('FIGURE 13.6 — RIGHT-HAND RULE II FOR THE FORCE ON A CURRENT-CARRYING CONDUCTOR: Outstretch the fingers of the right hand in the direction of current, then bend the fingers in the direction of the magnetic field (through the shorter angle between them); the extended thumb gives the direction of force on the current-carrying wire. This rule is for conventional current or flow of positive charges. For electronic current flow, the same rule is applied but with the left hand.',
  'شکل 13.6 — کرنٹ بردار موصل پر قوت کے لیے دایاں ہاتھ قاعدہ II: دائیں ہاتھ کی انگلیاں برقی رو کی سمت پھیلائیں، پھر انہیں مقناطیسی میدان کی سمت (ان دونوں کے چھوٹے زاویے سے) موڑیں؛ پھیلا ہوا انگوٹھا کرنٹ بردار تار پر قوت کی سمت بتاتا ہے۔ یہ قاعدہ روایتی برقی رو یا مثبت باروں کے بہاؤ کے لیے ہے۔ الیکٹرانک رو کے لیے یہی قاعدہ بائیں ہاتھ سے لاگو ہوتا ہے۔',
  '13.6 شکل — پر جریان‌لرونکي هادي د قوې لپاره د ښي لاس دویم قاعده: د ښي لاس ګوتې د جریان په لوري وغځوئ، بیا یې د مقناطیسي ساحې په لوري (د دواړو ترمنځ په کوچنۍ زاویه) تاو کړئ؛ غځول شوې ګوته پر جریان‌لرونکي سیم د قوې لوری ښيي. دا قاعده د دودیز جریان یا مثبتو چارجونو د بهېدو لپاره ده. د الکتروني جریان لپاره همدا قاعده په چپ لاس پلي کېږي.'),
 pair('FIGURE 13.7 — FLEMING’S LEFT-HAND RULE FOR THE FORCE ON A CURRENT-CARRYING CONDUCTOR: Set the thumb and the first two fingers of the left hand at right angles to each other. With the first finger pointing in the direction of the field and the second finger pointing in the direction of current, the thumb gives the direction of force.',
  'شکل 13.7 — کرنٹ بردار موصل پر قوت کے لیے فلیمنگ کا بایاں ہاتھ قاعدہ: بائیں ہاتھ کا انگوٹھا اور پہلی دو انگلیاں ایک دوسرے سے قائمہ زاویے پر رکھیں۔ پہلی انگلی میدان کی سمت اور دوسری برقی رو کی سمت ہو تو انگوٹھا قوت کی سمت بتاتا ہے۔',
  '13.7 شکل — پر جریان‌لرونکي هادي د قوې لپاره د فلېمینګ د چپ لاس قاعده: د چپ لاس ګوته او لومړۍ دوه ګوتې یو بل ته په قائمه زاویه کې ونیسئ. لومړۍ ګوته د ساحې او دویمه د جریان لوري ته وي، نو ګوته د قوې لوری ښيي.'),
]
EXAMPLE=[
 pair('EXAMPLE 13.1 — MAGNETIC FORCE ON WIRE','مثال 13.1 — تار پر مقناطیسی قوت','بېلګه 13.1 — پر سیم مقناطیسي قوه'),
 pair('A wire carrying 2 A current and has length of 10 cm between the poles of a magnet is kept at an angle of 30° to the uniform field of 0.6 T. Find the force acting on the wire?',
  '2 A برقی رو لے جانے والی، مقناطیس کے قطبین کے درمیان 10 cm لمبی تار کو 0.6 T کے یکساں میدان سے 30° زاویے پر رکھا گیا ہے۔ تار پر لگنے والی قوت معلوم کریں۔',
  'د 2 A جریان لرونکی، د مقناطیس د قطبونو ترمنځ 10 cm اوږد سیم د 0.6 T یوشان میدان سره په 30° زاویه کې اېښودل شوی. پر سیم واردېدونکې قوه ومومئ.'),
 pair('GIVEN','معلوم','ورکړل شوي'),
 pair('Current I = 2 A','برقی رو I = 2 A','جریان I = 2 A'),
 pair('Length L = 10 cm = 0.01 m','لمبائی L = 10 cm = 0.01 m','اوږدوالی L = 10 cm = 0.01 m'),
 pair('Magnetic field B = 0.6 T','مقناطیسی میدان B = 0.6 T','مقناطیسي ساحه B = 0.6 T'),
 pair('Angle θ = 30°','زاویہ θ = 30°','زاویه θ = 30°'),
 pair('REQUIRED','مطلوب','اړین'),
 pair('Magnetic force F_B = ?','مقناطیسی قوت F_B = ؟','مقناطیسي قوه F_B = ؟'),
 pair('SOLUTION','حل','حل'),
 pair('The force on a current-carrying wire in a magnetic field is given by','مقناطیسی میدان میں کرنٹ بردار تار پر قوت یہ ہے:','په مقناطیسي ساحه کې پر جریان‌لرونکي سیم قوه داسې ده:'),
 pair('F_B = ILB sin θ','F_B = ILB sin θ','F_B = ILB sin θ'),
 pair('Putting values,','قدریں رکھنے سے،','د ارزښتونو په ځای کولو،'),
 pair('F_B = 2 A × 0.1 m × 0.6 N/(A m) × sin 30°','F_B = 2 A × 0.1 m × 0.6 N/(A m) × sin 30°','F_B = 2 A × 0.1 m × 0.6 N/(A m) × sin 30°'),
 pair('therefore','لہٰذا','نو'),
 pair('F_B = 0.06 N','F_B = 0.06 N','F_B = 0.06 N'),
 pair('Answer','جواب','ځواب'),
]
EDITORIAL=pair('Editorial clarification: The printed given states “10 cm = 0.01 m”, while the solution substitutes “0.1 m” and prints the answer “0.06 N”. These source values conflict; all printed lines are retained above without substitution.',
 'ادارتی وضاحت: مطبوعہ معلومات میں “10 cm = 0.01 m” لکھا ہے، جبکہ حل میں “0.1 m” رکھا گیا ہے اور جواب “0.06 N” درج ہے۔ ماخذ کی یہ قدریں باہم متضاد ہیں؛ اوپر تمام مطبوعہ سطریں برقرار رکھی گئی ہیں۔',
 'ادارتي وضاحت: په چاپ شویو ورکړل شویو معلوماتو کې “10 cm = 0.01 m” راغلي، خو په حل کې “0.1 m” کارول شوی او “0.06 N” ځواب ورکړل شوی. د سرچینې ارزښتونه سره ټکر لري؛ پورته ټولې چاپ شوې کرښې هماغسې ساتل شوې دي.')

def make(identity,title,printed,pairs,layout,titles,refs,diagram=None,kind='lesson'):
 r={'id':identity,'title':title,'kind':kind,'pdfPage':51,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']=kind;s['sourceReferences']=[ref(x) for x in refs]
 if diagram:s.update(diagram);s['content']+=diagram['diagramSvg']
 return r,s
def field_force(lang):
 T={'en':('Magnetic field B','Current I','Conductor in a magnetic field'),'ur':('مقناطیسی میدان B','برقی رو I','مقناطیسی میدان میں موصل'),'ps':('مقناطیسي ساحه B','جریان I','په مقناطیسي ساحه کې هادي')}[lang]
 b='<path d="M45 218L205 48M105 245L265 75M165 268L325 98M225 280L385 110" stroke="#2563eb" stroke-width="3"/><path d="M198 54l-2 16 14-10M258 81l-2 16 14-10" fill="#2563eb"/><path d="M70 162H418" stroke="#7c2d12" stroke-width="8"/><path d="M402 147l22 15-22 15" fill="#16a34a"/><path d="M275 140V92" stroke="#dc2626" stroke-width="3"/><path d="M268 105l7-14 7 14" fill="#dc2626"/><path d="M303 162l35-42" stroke="#334155" stroke-width="2"/><text x="355" y="55">'+T[0]+'</text><text x="430" y="169">'+T[1]+'</text><text x="230" y="205">'+T[2]+'</text><text x="280" y="100">θ</text>'
 return svg(b,'Figure 13.4: current-carrying conductor at angle θ in a magnetic field.')
def force_magnets(lang):
 T={'en':('N','S','Magnetic force','Current','Magnetic field'),'ur':('N','S','مقناطیسی قوت','برقی رو','مقناطیسی میدان'),'ps':('N','S','مقناطیسي قوه','جریان','مقناطیسي ساحه')}[lang]
 b='<rect x="60" y="72" width="115" height="150" rx="8" fill="#dc2626"/><rect x="385" y="72" width="115" height="150" rx="8" fill="#2563eb"/><text x="110" y="155" fill="white" font-size="32">'+T[0]+'</text><text x="430" y="155" fill="white" font-size="32">'+T[1]+'</text><path d="M180 145H382" stroke="#7c2d12" stroke-width="8"/><path d="M355 130l27 15-27 15" fill="#16a34a"/><path d="M280 137V78" stroke="#dc2626" stroke-width="4"/><path d="M270 92l10-18 10 18" fill="#dc2626"/><path d="M255 245V205" stroke="#2563eb" stroke-width="3"/><path d="M248 218l7-14 7 14" fill="#2563eb"/><text x="220" y="130">'+T[3]+'</text><text x="295" y="72">F</text><text x="265" y="269">'+T[4]+'</text><text x="222" y="196">'+T[2]+'</text>'
 return svg(b,'Figure 13.5: force, current and magnetic field for a conductor between magnet poles.')
def rule2(lang):
 T={'en':('Current I','Magnetic field B','Force F'),'ur':('برقی رو I','مقناطیسی میدان B','قوت F'),'ps':('جریان I','مقناطیسي ساحه B','قوه F')}[lang]
 b='<path d="M105 205L290 80" stroke="#16a34a" stroke-width="6"/><path d="M265 80l26-5-10 24" fill="#16a34a"/><path d="M110 70L290 190" stroke="#2563eb" stroke-width="6"/><path d="M265 192l27 1-15-22" fill="#2563eb"/><path d="M290 185V55" stroke="#dc2626" stroke-width="6"/><path d="M278 75l12-25 12 25" fill="#dc2626"/><circle cx="290" cy="130" r="15" fill="#f8fafc" stroke="#334155" stroke-width="2"/><text x="58" y="225">'+T[0]+'</text><text x="65" y="61">'+T[1]+'</text><text x="310" y="58">'+T[2]+'</text>'
 return svg(b,'Figure 13.6: right-hand rule II, current and field determine force direction.')
def fleming(lang):
 T={'en':('Field','Current','Force'),'ur':('میدان','برقی رو','قوت'),'ps':('ساحه','جریان','قوه')}[lang]
 b='<path d="M270 220V70" stroke="#dc2626" stroke-width="6"/><path d="M258 87l12-24 12 24" fill="#dc2626"/><path d="M270 220L110 150" stroke="#16a34a" stroke-width="6"/><path d="M130 165l-27-15 29-4" fill="#16a34a"/><path d="M270 220L420 145" stroke="#2563eb" stroke-width="6"/><path d="M398 146l28-1-16 22" fill="#2563eb"/><circle cx="270" cy="220" r="12" fill="#f8fafc" stroke="#334155" stroke-width="2"/><text x="290" y="76">'+T[2]+'</text><text x="55" y="145">'+T[0]+'</text><text x="425" y="145">'+T[1]+'</text>'
 return svg(b,'Figure 13.7: Fleming’s left-hand rule gives force, field and current directions.')

if __name__=='__main__':
 force_pairs=FORCE[:5]+[FORCE[12]]+FORCE[5:12]
 fl=make('phys13-force-magnitude-and-limits92','Force on a current-carrying conductor — magnitude and limits',92,force_pairs,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'visual'},{'type':'paragraph','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]},{'type':'equation','indices':[12]}],('کرنٹ بردار موصل پر قوت — مقدار اور حدیں','پر جریان‌لرونکي هادي قوه — کچه او حدونه'),[92],{'diagramSvg':field_force('en'),'diagramSvgUrdu':field_force('ur'),'diagramSvgPashto':field_force('ps')})
 # Keep Figure 13.5 as a separate native SVG card rather than repeating Figure 13.4.
 f5=make('phys13-figure135-conductor-force92','Figure 13.5 — conductor between magnet poles',92,[FORCE[13]],[{'type':'paragraph','indices':[0]},{'type':'visual'}],('شکل 13.5 — مقناطیس کے قطبین کے درمیان موصل','13.5 شکل — د مقناطیس د قطبونو ترمنځ هادي'),[92],{'diagramSvg':force_magnets('en'),'diagramSvgUrdu':force_magnets('ur'),'diagramSvgPashto':force_magnets('ps')})
 dr=make('phys13-force-direction-and-tesla-unit93','Direction of magnetic force and tesla unit',93,DIRECTION[:4],[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]}],('مقناطیسی قوت کی سمت اور ٹیسلا کی اکائی','د مقناطیسي قوې لوری او د ټېسلا واحد'),[93])
 r2=make('phys13-right-hand-rule-II93','Right-hand Rule II for magnetic force',93,[DIRECTION[4]],[{'type':'paragraph','indices':[0]},{'type':'visual'}],('مقناطیسی قوت کے لیے دایاں ہاتھ قاعدہ II','د مقناطیسي قوې لپاره د ښي لاس دویم قاعده'),[93],{'diagramSvg':rule2('en'),'diagramSvgUrdu':rule2('ur'),'diagramSvgPashto':rule2('ps')})
 f7=make('phys13-fleming-left-hand-rule93','Fleming’s left-hand rule',93,[DIRECTION[5]],[{'type':'paragraph','indices':[0]},{'type':'visual'}],('فلیمنگ کا بایاں ہاتھ قاعدہ','د فلېمینګ د چپ لاس قاعده'),[93],{'diagramSvg':fleming('en'),'diagramSvgUrdu':fleming('ur'),'diagramSvgPashto':fleming('ps')})
 ex_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'heading','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'heading','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'equation','indices':[13]},{'type':'paragraph','indices':[14]},{'type':'equation','indices':[15]},{'type':'paragraph','indices':[16]}]
 ex=make('phys13-example131-force-wire93','Example 13.1 — magnetic force on a wire',93,EXAMPLE,ex_layout,('مثال 13.1 — تار پر مقناطیسی قوت','بېلګه 13.1 — پر سیم مقناطیسي قوه'),[93])
 note_pairs=[EDITORIAL];nr={'id':'phys13-editorial-example131-length93','title':'Editorial clarification — Example 13.1 length conversion','kind':'editorial','pdfPage':51,'printedPage':93,'sourcePdf':SOURCE,'paragraphs':[EDITORIAL[0]]};ns=section(nr,note_pairs,[{'type':'paragraph','indices':[0]}],('ادارتی وضاحت — مثال 13.1 کی لمبائی کی تبدیلی','ادارتي وضاحت — د 13.1 بېلګې د اوږدوالي بدلون'));ns['kind']='editorial';ns['sourceReferences']=[ref(93)]
 work={'id':'textbook-example-13-1','num':'13.1','title':'Magnetic force on a wire','problem':EXAMPLE[1][0],'problemUrdu':EXAMPLE[1][1],'problemPashto':EXAMPLE[1][2],
  'given':[EXAMPLE[3][0],EXAMPLE[4][0],EXAMPLE[5][0],EXAMPLE[6][0]],'givenUrdu':[EXAMPLE[3][1],EXAMPLE[4][1],EXAMPLE[5][1],EXAMPLE[6][1]],'givenPashto':[EXAMPLE[3][2],EXAMPLE[4][2],EXAMPLE[5][2],EXAMPLE[6][2]],
  'required':[EXAMPLE[8][0]],'requiredUrdu':[EXAMPLE[8][1]],'requiredPashto':[EXAMPLE[8][2]],'steps':[EXAMPLE[i][0] for i in [11,12,13,14,15]],'stepsUrdu':[EXAMPLE[i][1] for i in [11,12,13,14,15]],'stepsPashto':[EXAMPLE[i][2] for i in [11,12,13,14,15]],'answer':'0.06 N','solutionOrigin':'textbook printed answer','sourceReferences':[ref(93)]}
 records=[fl[0],f5[0],dr[0],r2[0],f7[0],ex[0],nr];sections=[fl[1],f5[1],dr[1],r2[1],f7[1],ex[1],ns]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=2)
  sync_companions(chapter_index=2,retire_sections=['13.1'],trim_sections=[{'id':'13.2','startsAt':'13.3 MAGNETIC FLUX','title':'Unit 13 — first unchecked magnetic-flux section'}],worked_examples=[work])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==51:
  checkpoint(51,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 51, printed pages 92–93. Compared the force-proportionality derivation and equations 13.1–13.2, vector form, minimum/maximum conditions, Figures 13.4–13.7, tesla definition and both unit systems, and Example 13.1 given/required/calculation/result. Rebuilt the four textbook diagrams as translated inline SVG and synchronized the worked-example card. Preserved the printed 10 cm = 0.01 m given and the solution’s 0.1 m substitution, with a separate translated editorial clarification.',issues=['Example 13.1 printed given states 10 cm = 0.01 m; its solution substitutes 0.1 m and prints 0.06 N. The source inconsistency is retained and separately labeled.'],printed_pages=[92,93],chapter_number=13)
