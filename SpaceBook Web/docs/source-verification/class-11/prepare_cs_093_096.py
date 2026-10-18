from cshelp import *
c=cell
U='u3'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
def CAP(s,k,en,ur,ps): add(s,k,en,ur,ps,kind='caption')
NOTE=' Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def fmt(n,i,boxes,top,cap,cu,cp):
    # boxes: list of (label,width)
    x=20;b=''
    tw=sum(w for _,w in boxes)
    b+=f'<text x="20" y="16" font-size="13" font-family="Arial,sans-serif" fill="#111">{top}</text>'
    for lab_,w in boxes:
        b+=f'<rect x="{x}" y="26" width="{w}" height="40" fill="#fff" stroke="#111" stroke-width="1.5"/>'+T(x+w/2,52,lab_,14,'middle',700)
        x+=w
    return dict(id=f'cs11-s{n:03}-fig{i}',svg=svg(x+30,80,cap,b),caption=cap,captionUrdu=cu,captionPashto=cp,labels=[lab(l,l,l) for l,_ in boxes])
# ---------- scan 93 (printed 84) ----------
s=page(93,U,'84','Arithmetic (end); logical; shift; c. Program Control Instructions; 3.2.2 Instruction Format — start','ریاضیاتی (اختتام)؛ منطقی؛ شفٹ؛ ج۔ پروگرام کنٹرول ہدایات؛ ۳.۲.۲ ہدایت کی شکل — آغاز','ریاضیاتي (پای)؛ منطقي؛ شفټ؛ ج. د پروګرام کنټرول لارښوونې؛ ۳.۲.۲ د لارښوونې بڼه — پیل','p084')
F=Flow(s)
add(s,'a','The execution of arithmetic instructions requires bringing the operands in the operational registers so that the data can be processed by ALU. Such functionality is implemented generally within instruction execution steps.','ریاضیاتی ہدایات پر عمل کے لیے آپرینڈز کو آپریشنل رجسٹرز میں لانا ضروری ہے تاکہ اے ایل یو ڈیٹا پراسیس کر سکے۔ ایسی فعالیت عموماً ہدایت کے عمل کے مراحل کے اندر نافذ ہوتی ہے۔','د ریاضیاتي لارښوونو پلي کول دا غواړي چې عملوندونه په عملیاتي رجسترونو کې راوړل شي ترڅو ډېټا د ALU په واسطه پروسس شي. داسې فعالیت معمولاً د لارښوونې د پلي کېدو په ګامونو کې پلي کېږي.')
H(s,'h1','ii. Logical Instructions','ii۔ منطقی ہدایات','ii. منطقي لارښوونې')
add(s,'b','AND, OR, NOT, XOR operate on binary data stored in registers.','اینڈ، اور، ناٹ، ایکس اور رجسٹرز میں محفوظ بائنری ڈیٹا پر عمل کرتے ہیں۔','AND، OR، NOT، XOR په رجسترونو کې ساتل شوې بائنري ډېټا عمل کوي.')
H(s,'h2','iii. Shift Instructions','iii۔ شفٹ ہدایات','iii. شفټ لارښوونې')
add(s,'c','Shift operation is used for transfer of bits either to the left or to the right of an operand.','شفٹ عمل آپرینڈ کے بٹس کو بائیں یا دائیں منتقل کرنے کے لیے استعمال ہوتا ہے۔','شفټ عمل د عملوند د بټونو کیڼ یا ښي لوري ته لېږد لپاره کارول کېږي.')
H(s,'h3','c. Program Control Instructions','ج۔ پروگرام کنٹرول ہدایات','ج. د پروګرام کنټرول لارښوونې')
add(s,'d','These instructions specify conditions for altering the sequence of program execution or in other words the content of PC (program counter) register. Program control or transfer of control is a way of altering the order in which statements are executed. There are a number of instructions used like JMP (Jump) and LOOP.','یہ ہدایات پروگرام کے عمل کی ترتیب کو تبدیل کرنے کی شرائط، یا دوسرے لفظوں میں پی سی (پروگرام کاؤنٹر) رجسٹر کے مواد کی وضاحت کرتی ہیں۔ پروگرام کنٹرول یا کنٹرول کی منتقلی اس ترتیب کو تبدیل کرنے کا ایک طریقہ ہے جس میں بیانات چلائے جاتے ہیں۔ بہت سی ہدایات استعمال ہوتی ہیں جیسے جے ایم پی (جمپ) اور لوپ۔','دا لارښوونې د پروګرام د پلي کېدو د ترتیب د بدلولو شرایط ټاکي یا په بل عبارت د PC (پروګرام شمېرونکي) رجستر منځپانګه. د پروګرام کنټرول یا د کنټرول لېږد یوه لار ده چې په هغې د بیاناتو د پلي کېدو ترتیب بدلېږي. ډیرې لارښوونې کارول کېږي لکه JMP (ټوپ) او LOOP.')
L(s,[('j1','The JMP instruction jumps to begin the execution at another location.','جے ایم پی ہدایت کسی دوسرے مقام پر عمل شروع کرنے کے لیے چھلانگ لگاتی ہے۔','د JMP لارښوونه په بل ځای کې د پلي کېدو د پیل لپاره ټوپ وهي.'),('j2','The LOOP instruction is used when number of statements are to be repeated.','لوپ ہدایت اس وقت استعمال ہوتی ہے جب کئی بیانات کو دہرانا ہو۔','د LOOP لارښوونه هغه وخت کارول کېږي کله چې د څو بیاناتو تکرار پکار وي.')],'jl')
H(s,'h4','3.2.2 Instruction Format','۳.۲.۲ ہدایت کی شکل','۳.۲.۲ د لارښوونې بڼه')
add(s,'e','An instruction format defines the layout of the bits of an instruction. An instruction format must include an Op-code (Operation-Code) and zero or more Operands. The Op-code will always be present.','ہدایت کی شکل ہدایت کے بٹس کی ترتیب متعین کرتی ہے۔ ہدایت کی شکل میں ایک او پی کوڈ (آپریشن کوڈ) اور صفر یا زیادہ آپرینڈز لازماً شامل ہوں۔ او پی کوڈ ہمیشہ موجود رہے گا۔','د لارښوونې بڼه د لارښوونې د بټونو ترتیب ټاکي. د لارښوونې بڼه باید یو Op-code (عملیې کوډ) او صفر یا ډیر عملوندونه ولري. Op-code به تل شتون ولري.')
L(s,[('f1','Op-Code','او پی کوڈ','اپ-کوډ (Op-Code)'),('f2','Operand','آپرینڈ','عملوند')],'fmt')
add(s,'f','Op-Code field of an instruction is a group of bits that define various processor operations such as LOAD, STORE, ADD, and SHIFT to be performed on some data stored in registers or memory.','ہدایت کا او پی کوڈ فیلڈ بٹس کا ایک گروپ ہے جو مختلف پراسیسر اعمال، جیسے لوڈ، اسٹور، ایڈ اور شفٹ، متعین کرتا ہے جو رجسٹرز یا میموری میں محفوظ کسی ڈیٹا پر انجام دیے جانے ہوں۔','د لارښوونې Op-Code ساحه د بټونو یوه ډله ده چې مختلف پروسیسر عملونه لکه LOAD، STORE، ADD او SHIFT ټاکي چې په رجسترونو یا حافظه کې ساتل شوې ځینې ډېټا ترسره کېږي.')
F.done()
fin(s,'Printed page 84: the end of the arithmetic instructions (continuing from page 83), ii. Logical Instructions, iii. Shift Instructions, c. Program Control Instructions (with JMP and LOOP), “3.2.2 Instruction Format” and the start of the Op-Code explanation. The left edge of the lines is clipped.')
# ---------- scan 94 (printed 85) ----------
s=page(94,U,'85','Instruction formats: zero-address and one-address','ہدایت کی اشکال: صفر پتہ اور ایک پتہ','د لارښوونې بڼې: صفر پته او یوه پته','p085')
F=Flow(s)
add(s,'a','Operand address field can be data, or can refer to data – i.e. address of data, or can be labels, which may be the address of an instruction to be executed next.','آپرینڈ ایڈریس فیلڈ ڈیٹا ہو سکتا ہے، یا ڈیٹا کا حوالہ، یعنی ڈیٹا کا پتہ ہو سکتا ہے، یا لیبلز ہو سکتے ہیں جو اگلی چلائی جانے والی ہدایت کا پتہ ہو سکتے ہیں۔','د عملوند پتې ساحه ډېټا کېدای شي، یا ډېټا ته اشاره کېدای شي – یعنې د ډېټا پته، یا لیبلونه کېدای شي چې د راتلونکې پلي کېدونکې لارښوونې پته وي.')
add(s,'b','Different instruction formats are used. A few of them are explained below.','مختلف ہدایتی اشکال استعمال ہوتی ہیں۔ ان میں سے چند نیچے بیان کی گئی ہیں۔','مختلفې د لارښوونې بڼې کارول کېږي. له هغو نه څو لاندې تشریح شوي دي.')
L(s,[('t1','Zero-Address Instruction','صفر پتہ ہدایت','د صفر پتې لارښوونه'),('t2','One-Address Instruction','ایک پتہ ہدایت','د یوې پتې لارښوونه'),('t3','Two-Address Instruction','دو پتہ ہدایت','د دوو پتو لارښوونه')],'fm')
H(s,'h1','a. Zero Address Instruction','الف۔ صفر پتہ ہدایت','الف. د صفر پتې لارښوونه')
add(s,'c','The Zero Address instruction format requires only op-code, having no operand to work with. Example of the Zero Address instruction format is HALT, STOP, which do not have any address.','صفر پتہ ہدایت کی شکل میں صرف او پی کوڈ درکار ہوتا ہے، اس کے ساتھ کام کرنے کے لیے کوئی آپرینڈ نہیں ہوتا۔ صفر پتہ ہدایت کی شکل کی مثال ہالٹ، اسٹاپ ہے جن کا کوئی پتہ نہیں ہوتا۔','د صفر پتې لارښوونې بڼه یوازې op-code غواړي، له هغې سره د کار لپاره هیڅ عملوند نشته. د صفر پتې لارښوونې بڼې بېلګه HALT، STOP دي چې هیڅ پته نه لري.')
s['figures']=[fmt(94,1,[('Op-Code',160)],'0.....................7 bits','Zero-address instruction format (7-bit op-code)','صفر پتہ ہدایت کی شکل (۷ بٹ او پی کوڈ)','د صفر پتې لارښوونې بڼه (۷ بټه op-code)')]
F.fg(0)
add(s,'d','Example: STOP','مثال: اسٹاپ','بېلګه: STOP')
H(s,'h2','b. One Address Instruction','ب۔ ایک پتہ ہدایت','ب. د یوې پتې لارښوونه')
add(s,'e','One Address instruction format requires one op-code and one operand. Example of the one address instruction format is LDA (Load Accumulator), JMP (Jump) etc. These instructions require one address to do the operation. Like JMP requires one address in order to jump to that specific address location.','ایک پتہ ہدایت کی شکل میں ایک او پی کوڈ اور ایک آپرینڈ درکار ہوتا ہے۔ ایک پتہ ہدایت کی شکل کی مثال ایل ڈی اے (لوڈ ایکیومولیٹر)، جے ایم پی (جمپ) وغیرہ ہیں۔ ان ہدایات کو عمل کے لیے ایک پتہ درکار ہوتا ہے۔ جیسے جے ایم پی کو اس مخصوص پتے والے مقام پر چھلانگ لگانے کے لیے ایک پتہ درکار ہوتا ہے۔','د یوې پتې لارښوونې بڼه یو op-code او یو عملوند غواړي. د یوې پتې لارښوونې بڼې بېلګه LDA (ایکیومولېټر پورته کول)، JMP (ټوپ) او نور دي. دا لارښوونې د عمل لپاره یوه پته غواړي. لکه JMP یوه پته غواړي ترڅو په هغه ځانګړې پته ځای ټوپ ووهي.')
s['figures'].append(fmt(94,2,[('Op-Code',170),('Operand',200)],'0.....................7, 8.........................20 bits','One-address instruction format (op-code and one operand)','ایک پتہ ہدایت کی شکل (او پی کوڈ اور ایک آپرینڈ)','د یوې پتې لارښوونې بڼه (op-code او یو عملوند)'))
F.fg(1)
add(s,'f','Example: JMP AX','مثال: جے ایم پی اے ایکس','بېلګه: JMP AX')
F.done()
fin(s,'Printed page 85: the operand explanation (continuing from page 84), the list of three instruction formats, “a. Zero Address Instruction” and “b. One Address Instruction”, each with a box diagram of bit fields (redrawn here as coded SVGs; the captions are supplied here, not printed). The headings “a.” and “b.” are printed in a faded colour.')
# ---------- scan 95 (printed 86) ----------
s=page(95,U,'86','c. Two Address Instruction; 3.2.3 Instruction Cycle: fetch and decode — start','ج۔ دو پتہ ہدایت؛ ۳.۲.۳ ہدایتی چکر: حاصل کرنا اور سمجھنا — آغاز','ج. د دوو پتو لارښوونه؛ ۳.۲.۳ د لارښوونې دوره: راوړل او پوهېدل — پیل','p086')
F=Flow(s)
H(s,'h1','c. Two Address Instruction','ج۔ دو پتہ ہدایت','ج. د دوو پتو لارښوونه')
add(s,'a','Two Address instruction format requires one op-code and two operands. Example of such instruction format is the MOV (Move), which moves data from the memory location to the register and from register to the memory location.','دو پتہ ہدایت کی شکل میں ایک او پی کوڈ اور دو آپرینڈز درکار ہوتے ہیں۔ ایسی ہدایتی شکل کی مثال ایم او وی (مو) ہے جو ڈیٹا کو میموری مقام سے رجسٹر میں اور رجسٹر سے میموری مقام میں منتقل کرتی ہے۔','د دوو پتو لارښوونې بڼه یو op-code او دوه عملوندونه غواړي. د داسې لارښوونې بڼې بېلګه MOV (خوځول) ده چې ډېټا د حافظې له ځای نه رجستر ته او له رجستر نه د حافظې ځای ته لېږدوي.')
s['figures']=[fmt(95,1,[('Op-Code',130),('Operand',150),('Operand',150)],'0.....................7, 8................19, 20..................31 bits','Two-address instruction format (op-code and two operands)','دو پتہ ہدایت کی شکل (او پی کوڈ اور دو آپرینڈز)','د دوو پتو لارښوونې بڼه (op-code او دوه عملوندونه)')]
F.fg(0)
add(s,'b','Example: ADD A, B','مثال: ایڈ اے، بی','بېلګه: ADD A, B')
H(s,'h2','3.2.3 Instruction Cycle','۳.۲.۳ ہدایتی چکر','۳.۲.۳ د لارښوونې دوره')
add(s,'c','Instruction cycle (sometimes called fetch-and-execute cycle, fetch-decode-execute cycle) is the basic operation cycle of a computer. It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions. This cycle is repeated continuously by the central processing unit (CPU), from booting of computer till it is shut down.','ہدایتی چکر (جسے کبھی کبھی حاصل کرنے اور چلانے کا چکر، حاصل کرنے سمجھنے چلانے کا چکر بھی کہتے ہیں) کمپیوٹر کا بنیادی عملی چکر ہے۔ یہ وہ عمل ہے جس کے ذریعے کمپیوٹر اپنی میموری سے پروگرام کی ہدایت حاصل کرتا ہے، طے کرتا ہے کہ ہدایت کن اعمال کا تقاضا کرتی ہے اور ان اعمال کو انجام دیتا ہے۔ یہ چکر مرکزی پراسیسنگ یونٹ (سی پی یو) کمپیوٹر کے بوٹ ہونے سے بند ہونے تک مسلسل دہراتا ہے۔','د لارښوونې دوره (ځینې وخت ورته راوړل-او-پلي کولو دوره، راوړل-پوهېدل-پلي کولو دوره هم ویل کېږي) د کمپیوټر بنسټیزه عملیه دوره ده. دا هغه پروسه ده چې د هغې په واسطه کمپیوټر د خپلې حافظې نه د پروګرام لارښوونه راباسي، ټاکي چې لارښوونه کوم عملونه غواړي، او هغه عملونه ترسره کوي. دا دوره د مرکزي پروسس واحد (CPU) په واسطه د کمپیوټر له بوټ کېدو نه تر بندېدو پورې پرله پسې تکرارېږي.')
add(s,'d','There are typically four stages of an instruction cycle that the CPU carries out:','ہدایتی چکر کے عموماً چار مراحل ہوتے ہیں جو سی پی یو انجام دیتا ہے:','د لارښوونې د دورې معمولاً څلور پړاوونه دي چې CPU یې ترسره کوي:')
L(s,[('s1','Fetch the instruction from memory','ہدایت میموری سے حاصل کرنا','لارښوونه له حافظې نه راوړل'),('s2','Decode the instruction','ہدایت کو سمجھنا','لارښوونه پوهېدل'),('s3','Execute the instruction','ہدایت کو چلانا','لارښوونه پلي کول'),('s4','Store the result','نتیجہ محفوظ کرنا','پایله ساتل')],'stg')
H(s,'h3','a. Fetch the instruction','الف۔ ہدایت حاصل کرنا','الف. لارښوونه راوړل')
add(s,'e','The instruction is fetched from the memory address that is currently in the Program Counter (PC), and store it in the Instruction Register (IR).','ہدایت اس میموری پتے سے حاصل کی جاتی ہے جو اس وقت پروگرام کاؤنٹر (پی سی) میں ہے اور اسے انسٹرکشن رجسٹر (آئی آر) میں محفوظ کیا جاتا ہے۔','لارښوونه له هغه حافظې پتې راوړل کېږي چې اوس مهال په پروګرام شمېرونکي (PC) کې ده، او په لارښوونې رجستر (IR) کې ساتل کېږي.')
H(s,'h4','b. Decode the instruction','ب۔ ہدایت کو سمجھنا','ب. لارښوونه پوهېدل')
add(s,'f','The instruction decoder interprets the instruction. If the instruction has an indirect address, the effective address is read from main memory, and any','انسٹرکشن ڈی کوڈر ہدایت کی تشریح کرتا ہے۔ اگر ہدایت کا بالواسطہ پتہ ہو تو مؤثر پتہ مین میموری سے پڑھا جاتا ہے اور کوئی بھی','د لارښوونې ډیکوډر لارښوونه تشریح کوي. که لارښوونه غیرمستقیمه پته ولري، مؤثره پته له اصلي حافظې نه لوستل کېږي او هر',cont=True)
F.done()
fin(s,'Printed page 86: “c. Two Address Instruction” with a box diagram of bit fields (redrawn here as a coded SVG; the caption is supplied here), “3.2.3 Instruction Cycle” with its four stages and the start of “b. Decode the instruction” (the sentence continues on the next page).')
# ---------- scan 96 (printed 87) ----------
s=page(96,U,'87','Decode, execute, store; Figure 3.5; 3.2.4 CISC and RISC architecture — start','سمجھنا، چلانا، محفوظ کرنا؛ شکل ۳.۵؛ ۳.۲.۴ سی آئی ایس سی اور آر آئی ایس سی تعمیر — آغاز','پوهېدل، پلي کول، ساتل؛ انځور ۳.۵؛ ۳.۲.۴ CISC او RISC جوړښت — پیل','p087')
F=Flow(s)
add(s,'a','required data is fetched from main memory to be processed and then placed into data registers. During this phase the instruction inside the IR (instruction register) gets decoded.','مطلوبہ ڈیٹا مین میموری سے پراسیس کے لیے حاصل کیا جاتا ہے اور پھر ڈیٹا رجسٹرز میں رکھا جاتا ہے۔ اس مرحلے کے دوران آئی آر (انسٹرکشن رجسٹر) کے اندر ہدایت سمجھ لی جاتی ہے۔','اړین ډېټا له اصلي حافظې نه د پروسس لپاره راوړل کېږي او بیا د ډېټا رجسترونو کې ایښودل کېږي. پدې پړاو کې د IR (د لارښوونې رجستر) دننه لارښوونه پوهېږي.',cont=True)
H(s,'h1','c. Execute the instruction','ج۔ ہدایت کو چلانا','ج. لارښوونه پلي کول')
add(s,'b','The CU passes the decoded information as a sequence of control signals to the relevant function units of the CPU to perform the actions required by the instruction such as reading values from registers, passing them to the ALU to perform mathematical or logic functions on them, and writing the result back to a register.','سی یو ڈی کوڈ شدہ معلومات کو کنٹرول اشاروں کی ایک ترتیب کے طور پر سی پی یو کی متعلقہ فعال اکائیوں کو منتقل کرتا ہے تاکہ ہدایت کے مطلوبہ اعمال انجام دیے جائیں جیسے رجسٹرز سے قدریں پڑھنا، انہیں اے ایل یو کو دینا تاکہ ان پر ریاضیاتی یا منطقی افعال کیے جائیں، اور نتیجہ واپس رجسٹر میں لکھنا۔','CU ډیکوډ شوي معلومات د کنټرول سیګنالونو د یوې لړۍ په توګه د CPU اړوندو فعالو واحدونو ته لېږدوي ترڅو هغه عملونه ترسره شي چې لارښوونه یې غواړي لکه له رجسترونو نه ارزښتونه لوستل، ALU ته یې ورکول ترڅو پر هغو ریاضیاتي یا منطقي دندې وشي، او پایله بېرته رجستر ته لیکل.')
H(s,'h2','d. Store results','د۔ نتائج محفوظ کرنا','د. پایلې ساتل')
add(s,'c','The result generated by the operation is stored in the main memory, or sent to an output device. But this condition is not always required.','عمل سے پیدا ہونے والا نتیجہ مین میموری میں محفوظ کیا جاتا ہے یا آؤٹ پٹ آلے کو بھیجا جاتا ہے۔ لیکن یہ شرط ہمیشہ درکار نہیں ہوتی۔','د عمل لخوا جوړه شوې پایله په اصلي حافظه کې ساتل کېږي، یا د وتلو وسیلې ته لېږل کېږي. خو دا شرط تل نه غوښتل کېږي.')
def cyc():
    b=('<rect x="120" y="10" width="100" height="44" rx="8" fill="#9c5ab0" stroke="#555"/>'+T(170,28,'FETCH',13,'middle',700,'#fff')+T(170,44,'Instruction',12,'middle',700,'#fff')
       +'<rect x="220" y="110" width="110" height="44" rx="8" fill="#6a4aa8" stroke="#555"/>'+T(275,128,'DECODE',13,'middle',700,'#fff')+T(275,144,'instruction',12,'middle',700,'#fff')
       +'<rect x="20" y="110" width="110" height="44" rx="8" fill="#b9d6df" stroke="#555"/>'+T(75,128,'EXECUTE',13,'middle',700,'#fff')+T(75,144,'instruction',12,'middle',700,'#fff')
       +'<path d="M230 62 Q268 78 278 104" fill="none" stroke="#111" stroke-width="1.8"/><polygon points="278,108 272,98 284,100" fill="#111"/>'
       +'<path d="M216 170 Q175 176 140 166" fill="none" stroke="#111" stroke-width="1.8"/><polygon points="136,164 148,160 146,172" fill="#111"/>'
       +'<path d="M60 104 Q70 80 112 62" fill="none" stroke="#111" stroke-width="1.8"/><polygon points="116,60 104,60 108,70" fill="#111"/>')
    return svg(350,185,'Instruction cycle: fetch, decode and execute instruction in a loop',b)
s['figures']=[dict(id='cs11-s096-fig1',svg=cyc(),caption='Figure 3.5 Instruction Cycle',captionUrdu='شکل ۳.۵ ہدایتی چکر',captionPashto='انځور ۳.۵ د لارښوونې دوره',labels=[lab('FETCH Instruction','ہدایت حاصل کرنا','لارښوونه راوړل'),lab('DECODE instruction','ہدایت سمجھنا','لارښوونه پوهېدل'),lab('EXECUTE instruction','ہدایت چلانا','لارښوونه پلي کول')])]
F.fg(0)
H(s,'h3','3.2.4 CISC and RISC architecture','۳.۲.۴ سی آئی ایس سی اور آر آئی ایس سی تعمیر','۳.۲.۴ CISC او RISC جوړښت')
add(s,'d','There are two major types of CPUs, which are classified according to the instruction set philosophy adopted by their designers. They are:','سی پی یوز کی دو بڑی اقسام ہیں جنہیں ان کے ڈیزائنرز کی اپنائی ہوئی ہدایتی سیٹ کی فلسفے کے مطابق تقسیم کیا جاتا ہے۔ وہ یہ ہیں:','د CPUs دوه لوی ډولونه شته چې د هغو د ډیزاینرانو د منل شوې د لارښوونو د سیټ د فلسفې مطابق وېشل کېږي. هغوی دا دي:')
L(s,[('t1','CISC (complex instruction set computer)','سی آئی ایس سی (پیچیدہ ہدایتی سیٹ کمپیوٹر)','CISC (پیچلی لارښوونو سیټ کمپیوټر)'),('t2','RISC (Reduced instruction set computer)','آر آئی ایس سی (کم کردہ ہدایتی سیٹ کمپیوٹر)','RISC (کم شوی لارښوونو سیټ کمپیوټر)')],'cr')
F.done()
fin(s,'Printed page 87: the end of “b. Decode the instruction” (continuing from page 86), c. Execute the instruction, d. Store results, Figure 3.5 Instruction Cycle (a triangle of three boxes FETCH Instruction, DECODE instruction and EXECUTE instruction with arrows; redrawn here as a coded SVG) and the start of “3.2.4 CISC and RISC architecture”. The headings c. and d. are printed in a faded colour.')
