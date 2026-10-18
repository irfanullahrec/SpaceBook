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
# ---------- scan 265 (printed 256) ----------
s=page(265,U,'256','b. Adding Fields to a Table; i. Adding Fields in Datasheet View; Figures 8.6 and 8.7','ب۔ ٹیبل میں فیلڈز شامل کرنا؛ i۔ ڈیٹا شیٹ ویو میں فیلڈز شامل کرنا؛ شکلیں ۸.۶ اور ۸.۷','ب. جدول ته ساحې زیاتول؛ i. په ډېټا شیټ لید کې ساحې زیاتول؛ انځورونه ۸.۶ او ۸.۷','p256')
F=Flow(s)
H(s,'h1','b. Adding Fields to a Table','ب۔ ٹیبل میں فیلڈز شامل کرنا','ب. جدول ته ساحې زیاتول')
add(s,'a','Access offers two ways to add fields to a Table.','ایکسیس ٹیبل میں فیلڈز شامل کرنے کے دو طریقے پیش کرتا ہے۔','Access جدول ته د ساحو زیاتولو دوه لارې وړاندې کوي.')
L(s,[('w1','Working in Datasheet View, which looks like a spreadsheet','ڈیٹا شیٹ ویو میں کام کرنا، جو اسپریڈ شیٹ جیسا لگتا ہے','په ډېټا شیټ لید کې کار کول، چې د سپریډ شیټ غوندې ښکاري'),('w2','Working in Design View, where users are able to set more controls for the fields.','ڈیزائن ویو میں کام کرنا، جہاں صارفین فیلڈز کے لیے مزید کنٹرولز ترتیب دے سکتے ہیں۔','په ډیزاین لید کې کار کول، چېرته چې کاروونکي کولای شي د ساحو لپاره نور کنټرولونه وټاکي.')],'wy')
H(s,'h2','i. Adding Fields in Datasheet View','i۔ ڈیٹا شیٹ ویو میں فیلڈز شامل کرنا','i. په ډېټا شیټ لید کې ساحې زیاتول')
add(s,'b','By default, Access creates one field in each new table, the ID field, which can be renamed as required by the user.','پہلے سے طے شدہ طور پر ایکسیس ہر نئے ٹیبل میں ایک فیلڈ بناتا ہے، آئی ڈی فیلڈ، جس کا نام صارف ضرورت کے مطابق بدل سکتا ہے۔','په ډیفالټ توګه Access په هر نوي جدول کې یوه ساحه جوړوي، د ID ساحه، چې نوم یې کاروونکی د اړتیا سره سم بدلولای شي.')
def idf():
    b='<rect x="5" y="5" width="240" height="95" fill="#fff" stroke="#999"/><rect x="5" y="5" width="240" height="14" fill="#6a8ac8" stroke="#555"/>'+T(25,16,'Books',8,'start',700)+T(60,38,'ID',9,'start',700)+T(110,38,'Add New Field',9,'start',700)+T(90,58,'(New)',9,'start',700)+'<line x1="80" y1="62" x2="80" y2="95" stroke="#c22" stroke-width="2"/>'+T(35,112,'ID automatically appears as first field',9,'start',700)
    return svg(260,120,'A Books table showing the ID field automatically as the first field',b)
s['figures']=[dict(svg=idf(),id='cs11-s265-fig1',caption='Figure 8.6 Automatic ID Field',captionUrdu='شکل ۸.۶ خودکار آئی ڈی فیلڈ',captionPashto='انځور ۸.۶ ځانګړتیا ID ساحه',labels=[lab('ID automatically appears as first field','آئی ڈی خود بخود پہلی فیلڈ کے طور پر ظاہر ہوتی ہے','ID په اتوماتیک ډول لومړۍ ساحه ښکاري'),lab('Add New Field','نیا فیلڈ شامل کریں','نوې ساحه زیاته کړئ')])]
F.fg(0)
add(s,'c','To add more fields to a table in Datasheet View, double click on the Add New Field header. As shown in Figure 8.7','ڈیٹا شیٹ ویو میں ٹیبل میں مزید فیلڈز شامل کرنے کے لیے نیا فیلڈ شامل کریں ہیڈر پر ڈبل کلک کریں۔ جیسا کہ شکل ۸.۷ میں دکھایا گیا ہے','په ډېټا شیټ لید کې جدول ته د نورو ساحو د زیاتولو لپاره د نوې ساحه زیاتولو سرلیک دوه ځله کلیک کړئ. لکه څنګه چې ۸.۷ انځور کې ښودل شوی')
def addf():
    body=ribbon(['Home','Create','External Data','Database Tools','Datasheet'])+'<rect x="10" y="95" width="115" height="95" fill="#fff" stroke="#888"/>'+T(15,108,'All Tables',8,'start',700)+T(15,124,'Student',8,'start',700)+T(30,138,'Student : Table',8,'start',400)+'<rect x="130" y="95" width="300" height="95" fill="#fff" stroke="#888"/>'+T(135,107,'Student',8,'start',700)+T(160,125,'Roll No',8,'start',700)+T(230,125,'Name',8,'start',700)+T(160,140,'(New)',8,'start',400)
    return shell(445,205,'Database : Database (Access 2007) — Table Tools',body,'Access window with a Student table having the Roll No field and a new field being named')
s['figures'].append(dict(svg=addf(),id='cs11-s265-fig2',caption='Figure 8.7 Add New Field',captionUrdu='شکل ۸.۷ نیا فیلڈ شامل کریں',captionPashto='انځور ۸.۷ نوې ساحه زیاته کړئ',labels=[lab('Roll No','رول نمبر','رول شمېره'),lab('Name','نام','نوم')]))
F.fg(1)
F.done()
fin(s,'Printed page 256: “b. Adding Fields to a Table” with two ways, “i. Adding Fields in Datasheet View”, Figure 8.6 Automatic ID Field (a Books table with the label “ID automatically appears as first field”; redrawn as coded SVG) and Figure 8.7 Add New Field (an Access window with the Student table, Roll No and a new field being named; redrawn as simplified coded SVG). The words Datasheet View, Design View, Access, ID and Add New Field are printed in bold or special type.')
# ---------- scan 266 (printed 257) ----------
s=page(266,U,'257','Datasheet steps (end); ii. Adding Fields in Design View; Figure 8.8','ڈیٹا شیٹ کے اقدامات (اختتام)؛ ii۔ ڈیزائن ویو میں فیلڈز شامل کرنا؛ شکل ۸.۸','د ډېټا شیټ ګامونه (پای)؛ ii. په ډیزاین لید کې ساحې زیاتول؛ انځور ۸.۸','p257')
F=Flow(s)
L(s,[('d1','The Add New Field text will disappear from the header. Name the field by typing the name directly into the header.','نیا فیلڈ شامل کریں کا متن ہیڈر سے غائب ہو جائے گا۔ ہیڈر میں براہِ راست نام ٹائپ کر کے فیلڈ کو نام دیں۔','د نوې ساحه زیاتولو متن به له سرلیک نه ورک شي. په سرلیک کې په مستقیم ډول نوم ټایپ کولو سره ساحې ته نوم ورکړئ.'),('d2','Press the tab key on the keyboard to move to the next field.','اگلی فیلڈ میں جانے کے لیے کی بورڈ پر ٹیب کی دبائیں۔','بلې ساحې ته د تللو لپاره په کیبورډ د ټب کیلي فشار کړئ.')],'dv')
H(s,'h1','ii. Adding Fields in Design View','ii۔ ڈیزائن ویو میں فیلڈز شامل کرنا','ii. په ډیزاین لید کې ساحې زیاتول')
add(s,'a','In Design View, the field names are along the left-hand column instead of across the top like in Datasheet View, as shown in Figure 8.8.','ڈیزائن ویو میں فیلڈ کے نام ڈیٹا شیٹ ویو کی طرح اوپر کی بجائے بائیں کالم میں ہوتے ہیں، جیسا کہ شکل ۸.۸ میں دکھایا گیا ہے۔','په ډیزاین لید کې د ساحو نومونه د ډېټا شیټ لید غوندې په سر کې پر ځای په کیڼ ستون کې وي، لکه څنګه چې ۸.۸ انځور کې ښودل شوی.')
def design(types=True):
    body=ribbon(['Home','Create','External Data','Database Tools','Design'])+'<rect x="10" y="95" width="100" height="105" fill="#fff" stroke="#888"/>'+T(15,108,'All Tables',8,'start',700)+T(15,124,'Student',8,'start',700)+T(30,138,'Student : Table',8,'start',400)+'<rect x="115" y="95" width="315" height="60" fill="#fff" stroke="#888"/>'+T(120,107,'Student',8,'start',700)+T(135,122,'Field Name',8,'start',700)+T(235,122,'Data Type',8,'start',700)+T(340,122,'Description',8,'start',700)+T(120,138,'Roll No',8,'start',700)
    body+='<rect x="115" y="160" width="140" height="40" fill="#fff" stroke="#888"/>'+T(120,172,'General  Lookup',7,'start',400)+T(120,184,'Field Size  New Values  Format  Caption',7,'start',400)
    if types:
        body+='<rect x="235" y="125" width="85" height="85" fill="#fff" stroke="#555"/>'
        for k,t in enumerate(['Text','Memo','Number','Date/Time','Currency','AutoNumber','Yes/No','OLE Object','Hyperlink','Attachment','Lookup Wizard…']): body+=T(240,136+k*7,t,6,'start',400)
    return shell(445,225,'Student : Database (Access 2007) — Microsoft Access',body,'Access Design View for the Student table with the Data Type drop-down list')
s['figures']=[dict(svg=design(),id='cs11-s266-fig1',caption='Figure 8.8 Fields in Design View',captionUrdu='شکل ۸.۸ ڈیزائن ویو میں فیلڈز',captionPashto='انځور ۸.۸ په ډیزاین لید کې ساحې',labels=[lab('Field Name','فیلڈ نام','د ساحې نوم'),lab('Data Type','ڈیٹا ٹائپ','د ډېټا ډول'),lab('Description','تفصیل','تشریح'),lab('Roll No','رول نمبر','رول شمېره')])]
F.fg(0)
add(s,'b','To add a new field in a table in Design View:','ڈیزائن ویو میں ٹیبل میں نیا فیلڈ شامل کرنے کے لیے:','په ډیزاین لید کې جدول ته د نوې ساحې د زیاتولو لپاره:')
L(s,[('n1','Click in the cell where the user want the new field and type the field name.','اس سیل میں کلک کریں جہاں صارف نیا فیلڈ چاہتا ہے اور فیلڈ کا نام ٹائپ کریں۔','په هغه حجره کې کلیک کړئ چېرته چې کاروونکی نوې ساحه غواړي او د ساحې نوم ټایپ کړئ.'),('n2','Press Tab key on the keyboard to move from one column to the other.','ایک کالم سے دوسرے میں جانے کے لیے کی بورڈ پر ٹیب کی دبائیں۔','له یوه ستون نه بل ته د تللو لپاره په کیبورډ د ټب کیلي فشار کړئ.'),('n3','Give appropriate data type and description if required. As shown in Figure 8.9.','اگر ضرورت ہو تو مناسب ڈیٹا ٹائپ اور تفصیل دیں۔ جیسا کہ شکل ۸.۹ میں دکھایا گیا ہے۔','که اړتیا وي مناسب د ډېټا ډول او تشریح ورکړئ. لکه څنګه چې ۸.۹ انځور کې ښودل شوی.')],'dn')
F.done()
fin(s,'Printed page 257: the end of the Datasheet View steps (continuing from page 256), “ii. Adding Fields in Design View” with its paragraph, Figure 8.8 Fields in Design View (a screenshot of the Design View of the Student table with the Data Type drop-down list: Text, Memo, Number, Date/Time, Currency, AutoNumber, Yes/No, OLE Object, Hyperlink, Attachment, Lookup Wizard; redrawn as simplified coded SVG, some entries of the list are illegible) and the three steps to add a field.')
# ---------- scan 267 (printed 258) ----------
s=page(267,U,'258','Figure 8.9 Design view of Added Field; c. Switching Views; Figure 8.10','شکل ۸.۹ شامل کردہ فیلڈ کا ڈیزائن ویو؛ ج۔ ویوز تبدیل کرنا؛ شکل ۸.۱۰','انځور ۸.۹ د زیاتې شوې ساحې ډیزاین لید؛ ج. لیدونه بدلول؛ انځور ۸.۱۰','p258')
F=Flow(s)
def design2():
    body=ribbon(['Home','Create','External Data','Database Tools','Design'])+'<rect x="10" y="95" width="100" height="85" fill="#fff" stroke="#888"/>'+T(15,108,'All Tables',8,'start',700)+T(15,124,'Student',8,'start',700)+T(30,138,'Student : Table',8,'start',400)+'<rect x="115" y="95" width="315" height="60" fill="#fff" stroke="#888"/>'+T(120,107,'Field Name',8,'start',700)+T(235,107,'Data Type',8,'start',700)+T(340,107,'Description',8,'start',700)
    for k,(n,t) in enumerate([('Roll No','Number'),('St Name','Text'),('Class','Text'),('Section','Text')]): body+=T(120,120+k*10,n,7,'start',700)+T(235,120+k*10,t,7,'start',400)
    body+=T(120,170,'Field Properties',8,'start',700)+'<rect x="115" y="160" width="140" height="30" fill="#fff" stroke="#888"/>'
    return shell(445,205,'Student : Database (Access 2007) — Microsoft Access',body,'Access Design View of the Student table with the added fields Roll No, St Name, Class and Section')
s['figures']=[dict(svg=design2(),id='cs11-s267-fig1',caption='Figure 8.9 Design view of Added Field',captionUrdu='شکل ۸.۹ شامل کردہ فیلڈ کا ڈیزائن ویو',captionPashto='انځور ۸.۹ د زیاتې شوې ساحې ډیزاین لید',labels=[lab('Roll No','رول نمبر','رول شمېره'),lab('St Name','طالب علم کا نام','د زده کوونکي نوم'),lab('Class','کلاس','ټولګی'),lab('Section','سیکشن','برخه')])]
F.fg(0)
add(s,'a','In Design View, there are many field property options that users can set to ensure that data can only be entered in certain formats.','ڈیزائن ویو میں فیلڈ پراپرٹی کے کئی اختیارات ہوتے ہیں جنہیں صارفین ترتیب دے سکتے ہیں تاکہ یقینی بنایا جا سکے کہ ڈیٹا صرف مخصوص شکلوں میں درج ہو۔','په ډیزاین لید کې د ساحې د ملکیت ډیر اختیارونه شته چې کاروونکي کولای شي وټاکي ترڅو ډاډ ترلاسه شي چې ډېټا یوازې په ځانګړو بڼو کې دخل کېدای شي.')
H(s,'h1','c. Switching Views','ج۔ ویوز تبدیل کرنا','ج. لیدونه بدلول')
add(s,'b','To switch views:','ویوز تبدیل کرنے کے لیے:','د لیدونو د بدلولو لپاره:')
L(s,[('v1','Select the Views command group from either the Home tab (As shown in Figure 8.10) or the Datasheet tab on the Ribbon.','ربن پر ہوم ٹیب (جیسا کہ شکل ۸.۱۰ میں دکھایا گیا ہے) یا ڈیٹا شیٹ ٹیب سے ویوز کمانڈ گروپ منتخب کریں۔','په ربن کې له Home ټب (لکه څنګه چې ۸.۱۰ انځور کې ښودل شوی) یا Datasheet ټب نه د لیدونو د حکمونو ډله وټاکئ.'),('v2','Select the view option from the menu.','مینو سے ویو کا اختیار منتخب کریں۔','له مېنو نه د لید اختیار وټاکئ.')],'sw')
def sv():
    b='<rect x="5" y="5" width="330" height="170" fill="#f4f7fb" stroke="#555"/><circle cx="22" cy="22" r="8" fill="#d9b04a" stroke="#555"/>'+T(60,26,'Home',8,'start',700)+T(110,26,'Create',8,'start',700)+T(160,26,'External Data',8,'start',700)+T(225,26,'Databa',8,'start',700)
    b+='<rect x="10" y="32" width="320" height="45" fill="#e8eef8" stroke="#aaa"/>'+T(15,72,'View',8,'start',700)+T(55,72,'Primary Key',7,'start',400)+T(105,72,'Builder',7,'start',400)+T(150,72,'Test Validation Rules',7,'start',400)+T(250,50,'Insert Rows',7,'start',400)+T(250,62,'Delete Rows',7,'start',400)+T(250,74,'Lookup Column',7,'start',400)
    b+='<rect x="15" y="82" width="125" height="85" fill="#fff" stroke="#555"/>'
    for k,t in enumerate(['Datasheet View','PivotTable View','PivotChart View','Design View']): b+=T(40,98+k*20,t,8,'start',700)
    b+=T(190,100,'Student',8,'start',700)+T(190,120,'Roll No',8,'start',700)+T(190,135,'St Name',8,'start',700)
    return svg(345,185,'Views command group menu with Datasheet View, PivotTable View, PivotChart View and Design View',b)
s['figures'].append(dict(svg=sv(),id='cs11-s267-fig2',caption='Figure 8.10 Switching Views',captionUrdu='شکل ۸.۱۰ ویوز تبدیل کرنا',captionPashto='انځور ۸.۱۰ لیدونه بدلول',labels=[lab('Datasheet View','ڈیٹا شیٹ ویو','د ډېټا شیټ لید'),lab('PivotTable View','پیوٹ ٹیبل ویو','د پیوټ جدول لید'),lab('PivotChart View','پیوٹ چارٹ ویو','د پیوټ چارټ لید'),lab('Design View','ڈیزائن ویو','د ډیزاین لید')]))
F.fg(1)
F.done()
fin(s,'Printed page 258: Figure 8.9 Design view of Added Field (the Design View of the Student table with the fields Roll No, St Name, Class and Section; redrawn as simplified coded SVG; the field properties area and the help text are illegible and are not reproduced), “c. Switching Views” with two steps and Figure 8.10 Switching Views (the Views menu with Datasheet View, PivotTable View, PivotChart View and Design View; redrawn as coded SVG). The first line of the page is cut at the top.')
# ---------- scan 268 (printed 259) ----------
s=page(268,U,'259','d. To Close a Table; e. To Open a Table; f. Adding More Tables to the Database; Figure 8.11','د۔ ٹیبل بند کرنا؛ ہ۔ ٹیبل کھولنا؛ و۔ ڈیٹا بیس میں مزید ٹیبلز شامل کرنا؛ شکل ۸.۱۱','د. جدول تړل؛ ه. جدول پرانیستل؛ و. ډېټابېس ته نور جدولونه زیاتول؛ انځور ۸.۱۱','p259')
F=Flow(s)
H(s,'h1','d. To Close a Table','د۔ ٹیبل بند کرنا','د. جدول تړل')
add(s,'a','There are several ways to close an active table.','فعال ٹیبل بند کرنے کے کئی طریقے ہیں۔','د فعال جدول د تړلو څو لارې شته.')
L(s,[('c1','Users can right click on the Table tab and choose Close from the menu. OR','صارفین ٹیبل ٹیب پر رائٹ کلک کر کے مینو سے کلوز منتخب کر سکتے ہیں۔ یا','کاروونکي کولای شي د جدول ټب په ښي کلیک وکړي او له مېنو نه Close وټاکي. یا'),('c2','A more common method is to click X that appears in the upper right hand corner of the active database object window.','زیادہ عام طریقہ ایکس پر کلک کرنا ہے جو فعال ڈیٹا بیس آبجیکٹ ونڈو کے اوپری دائیں کونے میں ظاہر ہوتا ہے۔','یوه ډیره عامه طریقه دا ده چې X کلیک کړئ چې د فعال ډېټابېس څیز کړکۍ په پورتنۍ ښي کنج کې ښکاري.')],'cl')
H(s,'h2','e. To Open a Table','ہ۔ ٹیبل کھولنا','ه. جدول پرانیستل')
add(s,'b','To open a table:','ٹیبل کھولنے کے لیے:','د جدول د پرانیستلو لپاره:')
L(s,[('o1','Right click the Table name of the table to open in the Navigation Pane. Then, choose Open from the menu. OR','نیویگیشن پین میں کھولنے والے ٹیبل کے نام پر رائٹ کلک کریں۔ پھر مینو سے اوپن منتخب کریں۔ یا','په لارښوونې پټه کې د پرانیستلو وړ جدول نوم ښي کلیک کړئ. بیا له مېنو نه Open وټاکئ. یا'),('o2','Double click the table name in the Navigation Pane. The selected table will open in the active database object window.','نیویگیشن پین میں ٹیبل کے نام پر ڈبل کلک کریں۔ منتخب ٹیبل فعال ڈیٹا بیس آبجیکٹ ونڈو میں کھل جائے گا۔','په لارښوونې پټه کې د جدول نوم دوه ځله کلیک کړئ. ټاکل شوی جدول به په فعال ډېټابېس څیز کړکۍ کې پرانیستل شي.')],'op')
H(s,'h3','f. Adding More Tables to the Database','و۔ ڈیٹا بیس میں مزید ٹیبلز شامل کرنا','و. ډېټابېس ته نور جدولونه زیاتول')
add(s,'c','By default, Access starts out with one table. To add more tables to the database:','طے شدہ طور پر ایکسیس ایک ٹیبل کے ساتھ شروع ہوتا ہے۔ ڈیٹا بیس میں مزید ٹیبلز شامل کرنے کے لیے:','په ډیفالټ توګه Access له یوه جدول سره پیلېږي. ډېټابېس ته د نورو جدولونو د زیاتولو لپاره:')
L(s,[('a1','Click on the Create tab on the Ribbon, as shown in Figure 8.11','ربن پر کریٹ ٹیب پر کلک کریں، جیسا کہ شکل ۸.۱۱ میں دکھایا گیا ہے','په ربن د Create ټب کلیک کړئ، لکه څنګه چې ۸.۱۱ انځور کې ښودل شوی'),('a2','Select Table from the Tables command group. A new table will open in the active database object window.','ٹیبلز کمانڈ گروپ سے ٹیبل منتخب کریں۔ ایک نیا ٹیبل فعال ڈیٹا بیس آبجیکٹ ونڈو میں کھل جائے گا۔','له جدولونو د حکمونو ډلې نه Table وټاکئ. نوی جدول به په فعال ډېټابېس څیز کړکۍ کې پرانیستل شي.')],'ad')
def cr():
    b='<rect x="5" y="5" width="245" height="165" fill="#f4f7fb" stroke="#555"/><circle cx="22" cy="22" r="8" fill="#d9b04a" stroke="#555"/>'+T(60,26,'Home',8,'start',700)+T(105,26,'Create',8,'start',700)+T(155,26,'External Da',8,'start',400)
    b+='<rect x="10" y="32" width="235" height="45" fill="#e8eef8" stroke="#aaa"/>'+T(15,60,'Table',8,'start',700)+T(55,60,'Table Templates',7,'start',400)+T(120,60,'SharePoint Lists',7,'start',400)+T(185,60,'Table Design',7,'start',400)+T(100,73,'Tables',7,'start',700)
    b+='<rect x="10" y="85" width="170" height="75" fill="#fff" stroke="#555"/>'+T(15,98,'Table',8,'start',700)+T(15,112,'Create a new blank table. You can',7,'start',400)+T(15,122,'define the fields directly in the new',7,'start',400)+T(15,132,'table, or open the table in Design view.',7,'start',400)+T(15,150,'Press F1 for more help.',7,'start',700)
    return svg(260,180,'Create tab with the Tables command group: Table, Table Templates, SharePoint Lists and Table Design, with the Table tooltip',b)
s['figures']=[dict(svg=cr(),id='cs11-s268-fig1',caption='Figure 8.11 Create New Table',captionUrdu='شکل ۸.۱۱ نیا ٹیبل بنائیں',captionPashto='انځور ۸.۱۱ نوی جدول جوړ کړئ',labels=[lab('Table','ٹیبل','جدول'),lab('Table Templates','ٹیبل ٹیمپلیٹس','د جدول کېنډونه'),lab('SharePoint Lists','شیئر پوائنٹ لسٹس','د SharePoint لیستونه'),lab('Table Design','ٹیبل ڈیزائن','د جدول ډیزاین'),lab('Tables','ٹیبلز','جدولونه')])]
F.fg(0)
F.done()
fin(s,'Printed page 259: “d. To Close a Table”, “e. To Open a Table” and “f. Adding More Tables to the Database” with their bulleted steps and Figure 8.11 Create New Table (the Create tab with the Tables command group and the tooltip text “Create a new blank table. You can define the fields directly in the new table, or open the table in Design view. Press F1 for more help.”; redrawn as simplified coded SVG). The key words in the steps are printed in bold.')
