from cshelp import *
c=cell
U='u8'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
NOTE=' Screenshots are not reproduced; each screenshot is redrawn as simplified coded SVG with the legible printed labels. Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def shell(w,h,title,body,label):
    b=f'<rect x="5" y="5" width="{w-10}" height="{h-10}" fill="#f4f7fb" stroke="#555"/><rect x="5" y="5" width="{w-10}" height="16" fill="#cfd9ea" stroke="#555"/>'+T(w/2,17,title,8,'middle',400)
    return svg(w,h,label,b+body)
def ribbon(tabs,y=30):
    b='<circle cx="22" cy="%d" r="8" fill="#d9b04a" stroke="#555"/>'%(y+5)
    for k,t in enumerate(tabs): b+=T(45+k*68,y+9,t,8,'start',700)
    return b+f'<rect x="10" y="{y+16}" width="420" height="36" fill="#e8eef8" stroke="#aaa"/>'
def btn(x,y,w,t,sz=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="16" fill="#eee" stroke="#555"/>'+T(x+w/2,y+11,t,sz,'middle',700)
def wiz(question,desc,inner,back=True,nxt=True,fin_=True,h=230):
    b='<rect x="5" y="5" width="420" height="%d" fill="#f6efc4" stroke="#555"/><rect x="5" y="5" width="420" height="16" fill="#fff" stroke="#555"/>'%h+T(12,17,'Command Button Wizard',9,'start',700)
    b+='<rect x="12" y="28" width="120" height="%d" fill="#3a3a2a" stroke="#555"/><rect x="40" y="70" width="60" height="45" fill="#fff" stroke="#999"/>'%(h-70)
    b+=T(145,42,question,9,'start',700)+T(145,56,desc,8,'start',400)+inner
    y=h-25
    b+=btn(150,y,60,'Cancel')+btn(220,y,55,'< Back')+btn(285,y,55,'Next >')+btn(350,y,60,'Finish')
    return svg(430,h+12,'Command Button Wizard dialog box: '+question,b)
# ---------- scan 285 (printed 276) ----------
s=page(285,U,'276','Figure 8.24 Command Button Wizard – 1; steps 3 and 4; Figure 8.25','شکل ۸.۲۴ کمانڈ بٹن ویزرڈ – ۱؛ مراحل ۳ اور ۴؛ شکل ۸.۲۵','انځور ۸.۲۴ د حکم تڼۍ مرستندوی – ۱؛ ۳ او ۴ ګامونه؛ انځور ۸.۲۵','p276')
F=Flow(s)
inner1=T(145,85,'Categories:',8,'start',700)+'<rect x="145" y="90" width="115" height="70" fill="#fff" stroke="#555"/><rect x="146" y="91" width="113" height="10" fill="#6a1a2a"/>'
for k,t in enumerate(['Record Operations','Form Operations','Report Operations','Application','Miscellaneous']): inner1+=T(150,110+k*10,t,7,'start',400)
inner1+=T(280,85,'Actions:',8,'start',700)+'<rect x="280" y="90" width="130" height="70" fill="#fff" stroke="#555"/><rect x="281" y="91" width="128" height="10" fill="#6a1a2a"/>'
for k,t in enumerate(['Find Next','Find Record','Go To First Record','Go To Last Record','Go To Next Record','Go To Previous Record']): inner1+=T(285,99+k*10,t,7,'start',400)
inner2=T(145,80,'If you choose Text, you can type the text to display. If you choose Picture, you can click Browse to find a picture to display.',6,'start',400)+'<circle cx="150" cy="115" r="4" fill="#fff" stroke="#111"/>'+T(160,118,'Text:',8,'start',700)+'<rect x="190" y="108" width="160" height="14" fill="#fff" stroke="#555"/>'+T(195,118,'Find Next',8,'start',400)+'<circle cx="150" cy="140" r="4" fill="#111" stroke="#111"/>'+T(160,143,'Picture:',8,'start',700)+'<rect x="190" y="130" width="160" height="55" fill="#fff" stroke="#555"/>'+btn(360,132,50,'Browse...')+T(190,200,'Show All Pictures',7,'start',400)
s['figures']=[dict(svg=wiz('What action do you want to happen when the button is pressed?','Different actions are available for each category.',inner1),id='cs11-s285-fig1',caption='Figure 8.24 Command Button Wizard – 1',captionUrdu='شکل ۸.۲۴ کمانڈ بٹن ویزرڈ – ۱',captionPashto='انځور ۸.۲۴ د حکم تڼۍ مرستندوی – ۱',labels=[lab('Categories','زمرے','ډلې'),lab('Actions','ایکشنز','کړنې'),lab('Cancel','منسوخ','لغوه'),lab('Next','اگلا','راتلونکی'),lab('Finish','مکمل','پای')]),
 dict(svg=wiz('Do you want text or a picture on the button?','',inner2),id='cs11-s285-fig2',caption='Figure 8.25 Command Button Wizard – 2',captionUrdu='شکل ۸.۲۵ کمانڈ بٹن ویزرڈ – ۲',captionPashto='انځور ۸.۲۵ د حکم تڼۍ مرستندوی – ۲',labels=[lab('Text','متن','متن'),lab('Picture','تصویر','انځور'),lab('Browse','براؤز','لټون'),lab('Show All Pictures','تمام تصاویر دکھائیں','ټول انځورونه وښيه')])]
F.fg(0)
add(s,'a','3. In the next step, as shown in Figure 8.25.','۳۔ اگلے مرحلے میں، جیسا کہ شکل ۸.۲۵ میں دکھایا گیا ہے۔','۳. په راتلونکي ګام کې، لکه څنګه چې ۸.۲۵ انځور کې ښودل شوی.')
L(s,[('a1','If user wants text to appear on the button, enter it in the Text box.','اگر صارف چاہتا ہے کہ بٹن پر متن ظاہر ہو تو اسے ٹیکسٹ باکس میں درج کریں۔','که کاروونکی غواړي چې په تڼۍ متن ښکاره شي، هغه د Text بکس کې دخل کړئ.'),('a2','If user wants a picture to appear on the button, select one using the Browse button.','اگر صارف چاہتا ہے کہ بٹن پر تصویر ظاہر ہو تو براؤز بٹن کے ذریعے ایک منتخب کریں۔','که کاروونکی غواړي چې په تڼۍ انځور ښکاره شي، د Browse تڼۍ په کارولو یو وټاکئ.'),('a3','Click Next.','نیکسٹ پر کلک کریں۔','د Next تڼۍ کلیک کړئ.')],'w3')
F.fg(1)
add(s,'b','4. In this step, as shown in Figure 8.26.','۴۔ اس مرحلے میں، جیسا کہ شکل ۸.۲۶ میں دکھایا گیا ہے۔','۴. پدې ګام کې، لکه څنګه چې ۸.۲۶ انځور کې ښودل شوی.')
L(s,[('b1','Give the button a meaningful name.','بٹن کو بامعنی نام دیں۔','تڼۍ ته مانادار نوم ورکړئ.')],'w4')
F.done()
fin(s,'Printed page 276: Figure 8.24 Command Button Wizard – 1 (the wizard dialog with the Categories list: Record Navigation, Record Operations, Form Operations, Report Operations, Application, Miscellaneous, and the Actions list: Find Next, Find Record, Go To First Record, Go To Last Record, Go To Next Record, Go To Previous Record; the first entry of Categories is partly illegible), step 3 with three sub-steps and Figure 8.25 Command Button Wizard – 2 (text or picture; both redrawn as simplified coded SVG), and the start of step 4 (the figure follows on the next page).')
# ---------- scan 286 (printed 277) ----------
s=page(286,U,'277','Figure 8.26 Command Button Wizard – 3; step 5; Figure 8.27 Command button','شکل ۸.۲۶ کمانڈ بٹن ویزرڈ – ۳؛ مرحلہ ۵؛ شکل ۸.۲۷ کمانڈ بٹن','انځور ۸.۲۶ د حکم تڼۍ مرستندوی – ۳؛ ۵ ګام؛ انځور ۸.۲۷ د حکم تڼۍ','p277')
F=Flow(s)
inner3=T(145,80,'A meaningful name will help you to refer to the button later.',8,'start',400)+'<rect x="145" y="90" width="260" height="14" fill="#fff" stroke="#555"/><rect x="147" y="92" width="60" height="10" fill="#223"/>'+T(147,100,'Command13',7,'start',700)+T(145,130,'That’s all the information the wizard needs to create your command button. Note: This wizard creates embedded macros that cannot run or be edited in Access 2003 and earlier versions.',7,'start',400)
dv=ribbon(['Home','Create','External Data','Database Tools','Design'])+'<rect x="10" y="95" width="95" height="105" fill="#fff" stroke="#888"/>'+T(15,108,'All Tables',8,'start',700)+T(15,124,'Student',8,'start',700)+T(30,136,'Student : Table',8,'start',400)+T(30,148,'Student Data entry form',7,'start',400)+T(15,162,'Exam',8,'start',700)+'<rect x="110" y="95" width="320" height="105" fill="#fff" stroke="#888"/>'+T(125,122,'Form Header',6,'start',700)+T(150,138,'Student',14,'start',700)+T(125,155,'Detail',6,'start',700)+T(125,168,'Roll No:   Roll No',7,'start',400)+T(125,178,'St Name:   St Name',7,'start',400)+T(125,188,'Class:   Class      Section:  Section',7,'start',400)+'<rect x="345" y="165" width="30" height="20" fill="#fff" stroke="#c22"/>'+T(335,215,'Command button',8,'start',700)
s['figures']=[dict(svg=wiz('What do you want to name the button?','',inner3),id='cs11-s286-fig1',caption='Figure 8.26 Command Button Wizard – 3',captionUrdu='شکل ۸.۲۶ کمانڈ بٹن ویزرڈ – ۳',captionPashto='انځور ۸.۲۶ د حکم تڼۍ مرستندوی – ۳',labels=[lab('Command13','کمانڈ۱۳','حکم۱۳')]),
 dict(svg=shell(445,225,'Student : Database (Access 2007) — Microsoft Access',dv,'Form Design View with a new command button placed on the form'),id='cs11-s286-fig2',caption='Figure 8.27 Command button',captionUrdu='شکل ۸.۲۷ کمانڈ بٹن',captionPashto='انځور ۸.۲۷ د حکم تڼۍ',labels=[lab('Command button','کمانڈ بٹن','د حکم تڼۍ')])]
F.fg(0)
L(s,[('n1','Access will give your button a default name. Renaming it with a more useful name will help you later.','ایکسیس آپ کے بٹن کو ایک طے شدہ نام دے گا۔ اسے زیادہ مفید نام سے بدلنا آپ کو بعد میں مدد دے گا۔','Access به ستاسو تڼۍ ته ډیفالټ نوم ورکړي. په ډیر ګټور نوم یې بدلول به تاسو سره وروسته مرسته وکړي.')],'w4b')
add(s,'a','5. Click Finish, the command button appears as shown in Figure 8.27.','۵۔ فنش پر کلک کریں، کمانڈ بٹن ظاہر ہو جاتا ہے جیسا کہ شکل ۸.۲۷ میں دکھایا گیا ہے۔','۵. د Finish تڼۍ کلیک کړئ، د حکم تڼۍ راښکاره کېږي لکه څنګه چې ۸.۲۷ انځور کې ښودل شوی.')
F.fg(1)
F.done()
fin(s,'Printed page 277: Figure 8.26 Command Button Wizard – 3 (the wizard dialog asking “What do you want to name the button?” with the default name Command13 and the note on embedded macros; redrawn as simplified coded SVG), the note on the default name, step 5 and Figure 8.27 Command button (the form Design View with the callout “Command button”; redrawn as simplified coded SVG). The word Finish is printed in bold.')
# ---------- scan 287 (printed 278) ----------
s=page(287,U,'278','Command button (end); b. Adding a Logo; Figure 8.28 Form Icon','کمانڈ بٹن (اختتام)؛ ب۔ لوگو شامل کرنا؛ شکل ۸.۲۸ فارم آئیکن','د حکم تڼۍ (پای)؛ ب. لوګو زیاتول؛ انځور ۸.۲۸ د فورم انځورن','p278')
F=Flow(s)
add(s,'a','The command button should be operational and appear on the form in Form View.','کمانڈ بٹن کو فعال ہونا چاہیے اور فارم ویو میں فارم پر ظاہر ہونا چاہیے۔','د حکم تڼۍ باید فعاله وي او په فورم لید کې په فورم کې ښکاره شي.')
H(s,'h1','b. Adding a Logo','ب۔ لوگو شامل کرنا','ب. لوګو زیاتول')
add(s,'b','Access automatically puts a form icon, like the one shown in Figure 8.28, in the header area of every form that you create.','ایکسیس آپ کے بنائے ہوئے ہر فارم کے ہیڈر ایریا میں خود بخود فارم آئیکن رکھتا ہے، جیسا کہ شکل ۸.۲۸ میں دکھایا گیا ہے۔','Access په اتوماتیک ډول ستاسو د جوړ شوي هر فورم د سرلیک په سیمه کې د فورم انځورن ږدي، لکه هغه چې ۸.۲۸ انځور کې ښودل شوی.')
fi=T(10,15,'Form icon',9,'start',700)+'<rect x="5" y="22" width="410" height="215" fill="#f4f7fb" stroke="#555"/><rect x="5" y="22" width="410" height="45" fill="#8fb4d8" stroke="#555"/><circle cx="55" cy="45" r="16" fill="none" stroke="#c22" stroke-width="2"/><rect x="45" y="38" width="20" height="14" fill="#fff" stroke="#555"/>'+T(85,52,'Student',14,'start',700)
for k,(a,b_) in enumerate([('Roll No:','1'),('St Name:','Ahmed'),('Class:','XI'),('Section:','B')]): fi+=T(40,92+k*25,a,8,'start',700)+'<rect x="90" y="%d" width="300" height="16" fill="#fff" stroke="#888"/>'%(80+k*25)+T(95,92+k*25,b_,8,'start',400)
fi+=T(25,190,'Exam ID    Exam Type    Marks obtained',7,'start',700)+T(35,203,'1  First Term   450',7,'start',400)+T(35,214,'2  Second Term   470',7,'start',400)+T(25,230,'Record: 1 of 4    No Filter    Search',7,'start',400)
s['figures']=[dict(svg=svg(430,245,'Form with the form icon circled beside the title Student, fields Roll No, St Name, Class and Section and the related Exam records',fi),id='cs11-s287-fig1',caption='Figure 8.28 Form Icon',captionUrdu='شکل ۸.۲۸ فارم آئیکن',captionPashto='انځور ۸.۲۸ د فورم انځورن',labels=[lab('Form icon','فارم آئیکن','د فورم انځورن'),lab('Student','اسٹوڈنٹ','زده کوونکی')])]
F.fg(0)
add(s,'c','One way to customize the look of forms is to remove that icon and replace it with a logo. This is very easy to do using the Logo command.','فارمز کی شکل کو حسبِ ضرورت بنانے کا ایک طریقہ اس آئیکن کو ہٹانا اور اس کی جگہ لوگو لگانا ہے۔ لوگو کمانڈ استعمال کر کے یہ کرنا بہت آسان ہے۔','د فورمونو د بڼې د دودیز کولو یوه لار دا ده چې دا انځورن لېرې کړئ او په ځای یې لوګو کېږدئ. د Logo حکم په کارولو سره دا کول ډیر اسان دي.')
add(s,'d','The following steps are used to replace the form icon with a logo of choice.','فارم آئیکن کو پسندیدہ لوگو سے بدلنے کے لیے درج ذیل اقدامات استعمال ہوتے ہیں۔','د فورم انځورن د خوښې لوګو سره د بدلولو لپاره لاندې ګامونه کارول کېږي.')
L(s,[('l1','Delete the form icon.','فارم آئیکن حذف کریں۔','د فورم انځورن حذف کړئ.'),('l2','Select the Logo command from the Controls group on the Ribbon.','ربن پر کنٹرولز گروپ سے لوگو کمانڈ منتخب کریں۔','په ربن د Controls ډلې نه د Logo حکم وټاکئ.'),('l3','Use the Insert Picture dialog box to locate the picture file to use as the logo. Then, click Ok. The new logo should appear.','لوگو کے طور پر استعمال کرنے والی تصویر کی فائل تلاش کرنے کے لیے انسرٹ پکچر ڈائیلاگ باکس استعمال کریں۔ پھر ٹھیک ہے پر کلک کریں۔ نیا لوگو ظاہر ہو جانا چاہیے۔','د لوګو په توګه د کارولو لپاره د انځور فایل موندلو لپاره د Insert Picture خبرې اترې بکس وکاروئ. بیا Ok کلیک کړئ. نوی لوګو باید ښکاره شي.')],'lg')
F.done()
fin(s,'Printed page 278: the closing sentence of the command button steps, “b. Adding a Logo” with its paragraph, Figure 8.28 Form Icon (a form screenshot with the form icon circled and labelled “Form icon”; redrawn as simplified coded SVG), the paragraph on the Logo command and three steps. The words Logo, Controls, Ribbon, Insert Picture and Ok are printed in bold or special type.')
# ---------- scan 288 (printed 279) ----------
s=page(288,U,'279','Logo (end); c. Applying a Style with AutoFormat; Figure 8.29 AutoFormat Options','لوگو (اختتام)؛ ج۔ آٹو فارمیٹ کے ساتھ انداز لاگو کرنا؛ شکل ۸.۲۹ آٹو فارمیٹ آپشنز','لوګو (پای)؛ ج. د AutoFormat سره سټایل پلي کول؛ انځور ۸.۲۹ د AutoFormat اختیارونه','p279')
F=Flow(s)
add(s,'a','User can move and re-size the logo, as well. Moving and re-sizing objects on a form is covered later in this lesson.','صارف لوگو کو منتقل اور اس کا سائز بھی تبدیل کر سکتا ہے۔ فارم پر آبجیکٹس کو منتقل اور ان کا سائز بدلنا اس سبق میں بعد میں بیان کیا گیا ہے۔','کاروونکی کولای شي لوګو هم حرکت ورکړي او کچه یې بدله کړي. په فورم د څیزونو حرکت او د کچې بدلول په دې درس کې وروسته پوښل شوي.')
H(s,'h1','c. Applying a Style with AutoFormat','ج۔ آٹو فارمیٹ کے ساتھ انداز لاگو کرنا','ج. د AutoFormat سره سټایل پلي کول')
add(s,'b','Another simple way to dramatically change the way the form looks is to apply a style with the AutoFormat command. User can modify the color for each part of the form, but Microsoft Access has already combined colors in several attractive styles. These styles are available under the AutoFormat command. To apply a pre-set format to the form:','فارم کی شکل کو ڈرامائی طور پر بدلنے کا ایک اور سادہ طریقہ آٹو فارمیٹ کمانڈ کے ساتھ انداز لاگو کرنا ہے۔ صارف فارم کے ہر حصے کا رنگ بدل سکتا ہے، لیکن مائیکروسافٹ ایکسیس نے پہلے ہی رنگوں کو کئی پرکشش انداز میں ملا دیا ہے۔ یہ انداز آٹو فارمیٹ کمانڈ کے تحت دستیاب ہیں۔ فارم پر پہلے سے طے شدہ فارمیٹ لاگو کرنے کے لیے:','د فورم د ښکارېدو د ډرامایي بدلولو بله ساده لار دا ده چې د AutoFormat حکم سره سټایل پلي کړئ. کاروونکی کولای شي د فورم د هرې برخې رنګ بدل کړي، خو مایکروسافټ Access مخکې له مخکې رنګونه په څو زړه راښکونکو سټایلونو کې یوځای کړي. دا سټایلونه د AutoFormat حکم لاندې شته. فورم ته د مخکې ټاکل شوې بڼې د پلي کولو لپاره:')
L(s,[('a1','Click on the AutoFormat command on the Format Ribbon, as shown in Figure 8.29','ربن کے فارمیٹ ٹیب پر آٹو فارمیٹ کمانڈ پر کلک کریں، جیسا کہ شکل ۸.۲۹ میں دکھایا گیا ہے','په ربن د Format ټب کې د AutoFormat حکم کلیک کړئ، لکه څنګه چې ۸.۲۹ انځور کې ښودل شوی'),('a2','Select the desired format. The changes will appear when the mouse button is released.','مطلوبہ فارمیٹ منتخب کریں۔ ماؤس بٹن چھوڑنے پر تبدیلیاں ظاہر ہو جائیں گی۔','غوښتل شوې بڼه وټاکئ. بدلونونه به د موږک د تڼۍ خوشې کېدو سره ښکاره شي.')],'af2')
af=ribbon(['Home','Create','External Data','Database Tools','Format'])+'<rect x="10" y="95" width="110" height="105" fill="#fff" stroke="#888"/>'+T(15,108,'All Tables',8,'start',700)+T(15,124,'Student',8,'start',700)+T(30,136,'Student : Table',8,'start',400)+T(30,148,'Student Data entry form',7,'start',400)+T(15,162,'Exam',8,'start',700)+'<rect x="125" y="95" width="305" height="105" fill="#fff" stroke="#888"/><rect x="125" y="95" width="305" height="22" fill="#6a2a2a"/>'+T(160,110,'Student',11,'start',700,'#fff')+T(140,135,'Exam ID   Exam Type   Marks obtained',7,'start',400)+T(140,147,'1 First Term  450    2 Second Term  470',7,'start',400)
af+='<rect x="265" y="45" width="165" height="115" fill="#fff" stroke="#555"/>'
cols=['#e8e8e8','#b8c8e0','#d8b8c8','#4a5a7a','#2a2a6a']
for r in range(4):
    for k in range(5): af+='<rect x="%d" y="%d" width="28" height="22" fill="%s" stroke="#888"/>'%(270+k*31,50+r*27,cols[(k+r)%5])
af+=T(275,170,'AutoFormat Wizard…',7,'start',700)
s['figures']=[dict(svg=shell(445,225,'Student : Database (Access 2007) — Microsoft Access',af,'Form Layout View with the AutoFormat gallery of pre-set styles'),id='cs11-s288-fig1',caption='Figure 8.29 AutoFormat Options',captionUrdu='شکل ۸.۲۹ آٹو فارمیٹ آپشنز',captionPashto='انځور ۸.۲۹ د AutoFormat اختیارونه',labels=[lab('AutoFormat Wizard','آٹو فارمیٹ ویزرڈ','د AutoFormat مرستندوی')])]
F.fg(0)
F.done()
fin(s,'Printed page 279: the closing sentence of the logo steps, “c. Applying a Style with AutoFormat” with its paragraph and two steps, and Figure 8.29 AutoFormat Options (a Layout View screenshot with the AutoFormat gallery of twenty small style tiles and the entry “AutoFormat Wizard…”; redrawn as simplified coded SVG, the individual tile colours are approximate). The words AutoFormat command and Format are printed in bold.')
