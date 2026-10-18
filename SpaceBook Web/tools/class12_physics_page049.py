"""Sequential source correction for PDF page 49 of Class 12 Physics."""
import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions, shared_class_data_lock

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(p): return {'pdfPage':49,'printedPage':p,'sourcePdf':SOURCE}

OUTCOMES=[
 pair('explain that magnetic field is an example of a field of force produced either by current-carrying conductors or by permanent magnets.', 'وضاحت کریں کہ مقناطیسی میدان قوت کا ایسا میدان ہے جو کرنٹ بردار موصلوں یا مستقل مقناطیسوں سے پیدا ہوتا ہے۔','تشریح کړئ چې مقناطیسي ساحه د قوې یوه ساحه ده چې د جریان لرونکو هادیانو یا دایمي مقناطیسونو له خوا تولیدېږي.'),
 pair('describe magnetic effect of current.','برقی رو کے مقناطیسی اثر کو بیان کریں۔','د جریان مقناطیسي اغېز بیان کړئ.'),
 pair('describe and sketch field lines pattern due to a long straight wire.','لمبی سیدھی تار کی وجہ سے بننے والی میدانی خطوط کی ترتیب بیان کریں اور اس کا خاکہ بنائیں۔','د اوږده نېغ سیم له امله د ساحې د کرښو بڼه بیان او رسم کړئ.'),
 pair('explain that a force might act on a current-carrying conductor placed in a magnetic field.','وضاحت کریں کہ مقناطیسی میدان میں رکھے کرنٹ بردار موصل پر قوت عمل کر سکتی ہے۔','تشریح کړئ چې په مقناطیسي ساحه کې پراته جریان‌لرونکي هادي باندې قوه عمل کولای شي.'),
 pair('Investigate the factors affecting the force on a current carrying conductor in a magnetic field.','مقناطیسی میدان میں کرنٹ بردار موصل پر قوت کو متاثر کرنے والے عوامل کی تحقیق کریں۔','په مقناطیسي ساحه کې پر جریان‌لرونکي هادي د قوې اغېزمنوونکي عوامل وڅېړئ.'),
 pair('solve problems involving the use of F = BIL sin θ.','F = BIL sin θ کے استعمال پر مبنی مسائل حل کریں۔','د F = BIL sin θ د کارونې مسئلې حل کړئ.'),
 pair('define magnetic flux density and its units.','مقناطیسی بہاؤ کی کثافت اور اس کی اکائیاں بیان کریں۔','مقناطیسي فلوکس کثافت او واحدونه یې تعریف کړئ.'),
 pair('describe the concept of magnetic flux (Φ) as scalar product of magnetic field (B) and area (A) using the relation Φ_B = B⊥A = B·A.', 'مقناطیسی بہاؤ (Φ) کے تصور کو مقناطیسی میدان (B) اور رقبے (A) کے عددی ضرب کے طور پر، تعلق Φ_B = B⊥A = B·A کی مدد سے بیان کریں۔','د مقناطیسي فلوکس (Φ) مفهوم د مقناطیسي ساحې (B) او مساحت (A) د سکالر ضرب په توګه د Φ_B = B⊥A = B·A اړیکې په کارولو بیان کړئ.'),
 pair('state Ampere’s law.','ایمپیئر کا قانون بیان کریں۔','د امپېر قانون بیان کړئ.'),
 pair('apply Ampere’s law to find magnetic flux density around a wire and inside a solenoid.', 'تار کے گرد اور سولینائڈ کے اندر مقناطیسی بہاؤ کی کثافت معلوم کرنے کے لیے ایمپیئر کا قانون استعمال کریں۔','د سیم شاوخوا او د سولینایډ دننه د مقناطیسي فلوکس کثافت موندلو لپاره د امپېر قانون وکاروئ.'),
 pair('describe quantitatively the path followed by a charged particle shot into a magnetic field in a direction perpendicular to the field.', 'مقداری طور پر اس راستے کو بیان کریں جس پر بار دار ذرہ مقناطیسی میدان کے عموداً داخل کیا جائے تو چلتا ہے۔','په کمیتي ډول هغه لاره بیان کړئ چې چارج لرونکی ذره یې د مقناطیسي ساحې پر لوري د عمود په توګه د ننوتلو پر مهال تعقیبوي.'),
 pair('explain that a force may act on a charged particle in a uniform magnetic field.', 'وضاحت کریں کہ یکساں مقناطیسی میدان میں بار دار ذرّے پر قوت عمل کر سکتی ہے۔','تشریح کړئ چې په یوشان مقناطیسي ساحه کې پر چارج لرونکې ذرې قوه عمل کولای شي.'),
 pair('describe a method to measure the e/m of an electron by applying magnetic field and electric field on a beam of electrons.', 'الیکٹرانوں کی شعاع پر مقناطیسی اور برقی میدان لگا کر الیکٹران کے e/m کی پیمائش کا طریقہ بیان کریں۔','د الکترونونو پر وړانګې د مقناطیسي او برېښنايي ساحو په لګولو سره د الکترون د e/m د اندازه کولو طریقه بیان کړئ.'),
 pair('predict the turning effect on a current carrying coil in a magnetic field and use this principle to understand the construction and working of a galvanometer.', 'مقناطیسی میدان میں کرنٹ بردار کوائل پر گھماؤ کے اثر کی پیش گوئی کریں اور اس اصول سے گیلوانومیٹر کی ساخت اور کام سمجھیں۔','په مقناطیسي ساحه کې پر جریان‌لرونکي کویل د تاوېدو اغېز اټکل کړئ او د دې اصل له مخې د ګالوانومیتر جوړښت او کار درک کړئ.'),
 pair('explain how a given galvanometer can be converted into a voltmeter or ammeter of a specified range.', 'وضاحت کریں کہ کسی گیلوانومیٹر کو مقررہ حد کے وولٹ میٹر یا ایمیٹر میں کیسے بدلا جا سکتا ہے۔','تشریح کړئ چې یو ورکړل شوی ګالوانومیتر څنګه د ټاکلې اندازې ولټ‌متر یا امیتر ته اړول کېدای شي.'),
 pair('describe the use of avometer / multimeter (analogue and digital).','ایوومیٹر / ملٹی میٹر (اینالاگ اور ڈیجیٹل) کا استعمال بیان کریں۔','د ایوومیټر / ملټي‌متر (انالوګ او ډیجیټل) کارونه بیان کړئ.'),
]
CONTENT=[
 pair('UNIT 13 ELECTROMAGNETISM','یونٹ 13 برقی مقناطیسیت','۱۳م یونټ برېښنا-مقناطیسیت'),
 pair('How electromagnetism is used in imaging inside the human body?','انسانی جسم کے اندر تصویربرداری میں برقی مقناطیسیت کیسے استعمال ہوتا ہے؟','د انسان د بدن دننه په انځور اخیستنه کې برېښنا-مقناطیسیت څنګه کارول کېږي؟'),
 pair('LEARNING OUTCOMES','حاصلاتِ تعلم','د زده‌کړې پایلې'),
 pair('After studying this unit the students will be able to:','اس یونٹ کے مطالعے کے بعد طلبہ یہ کر سکیں گے:','د دې یونټ له زده‌کړې وروسته زده‌کوونکي به وکولای شي:'),
 *OUTCOMES,
 pair('A magnet (from Greek “Magnesian stone”) is a material or object that produces a magnetic field. This magnetic field is invisible but is responsible for the most notable property of a magnet: a force that pulls on other ferromagnetic materials, such as iron, and attracts or repels other magnets.', 'مقناطیس (یونانی لفظ “Magnesian stone” سے) ایسا مادہ یا جسم ہے جو مقناطیسی میدان پیدا کرتا ہے۔ یہ میدان دکھائی نہیں دیتا، مگر مقناطیس کی نمایاں خاصیت کا سبب ہے: ایسی قوت جو لوہے جیسے دوسرے فرو مقناطیسی مادوں کو کھینچتی ہے اور دوسرے مقناطیسوں کو اپنی طرف کھینچتی یا دور دھکیلتی ہے۔','مقناطیس (د یوناني “Magnesian stone” له کلمې) هغه ماده یا څیز دی چې مقناطیسي ساحه تولیدوي. دا ساحه نه لیدل کېږي، خو د مقناطیس د پام وړ ځانګړنې لامل ده: داسې قوه چې د اوسپنې په څېر نور فرومقناطیسي مواد راکاږي او نور مقناطیسونه جذبوي یا یې شړي.'),
 pair('A permanent magnet is an object made from a material that is magnetized and creates its own persistent magnetic field. An everyday example is a refrigerator magnet used to hold notes on a refrigerator door.', 'مستقل مقناطیس ایسا جسم ہے جو مقناطیس شدہ مادے سے بنا ہو اور اپنا مستقل مقناطیسی میدان پیدا کرے۔ اس کی روزمرہ مثال فریج کا مقناطیس ہے، جس سے فریج کے دروازے پر نوٹس لگائے جاتے ہیں۔','دایمي مقناطیس له مقناطیسي شوې مادې جوړ څیز دی چې خپله تلپاتې مقناطیسي ساحه تولیدوي. د ورځني ژوند یوه بېلګه یې د یخچال مقناطیس دی چې د یخچال پر دروازه د یادښتونو د نښلولو لپاره کارېږي.'),
 pair('For your information','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره'),
 pair('Recording media and swipe cards','ریکارڈنگ میڈیا اور سوائپ کارڈ','د ثبت رسنۍ او مقناطیسي کارتونه'),
 pair('Magnetic recording media: VHS (Video Home System) tapes contain a reel of magnetic tape. The information that makes up the video and sound is encoded on the magnetic coating on the tape. Common audio cassettes also rely on magnetic tape. Similarly, in computers, floppy disks and hard disks record data on a thin magnetic coating.', 'مقناطیسی ریکارڈنگ میڈیا: VHS (Video Home System) ٹیپس میں مقناطیسی ٹیپ کا ایک ریل ہوتا ہے۔ ویڈیو اور آواز کی معلومات ٹیپ کی مقناطیسی تہہ پر کوڈ کی جاتی ہیں۔ عام آڈیو کیسٹیں بھی مقناطیسی ٹیپ استعمال کرتی ہیں۔ اسی طرح کمپیوٹروں میں فلاپی ڈسک اور ہارڈ ڈسک باریک مقناطیسی تہہ پر ڈیٹا محفوظ کرتی ہیں۔','مقناطیسي ثبت رسنۍ: د VHS (Video Home System) ټېپونو کې د مقناطیسي ټېپ یو رول وي. د ویډیو او غږ معلومات د ټېپ پر مقناطیسي پوښ لیکل کېږي. عادي غږیز کېسټونه هم پر مقناطیسي ټېپ تکیه لري. همدارنګه په کمپیوټرونو کې فلاپي ډیسکونه او هارډ ډیسکونه معلومات پر نري مقناطیسي پوښ ثبتوي.'),
 pair('Credit, debit, and ATM cards: All of these cards have a magnetic strip on one side. This strip encodes the information to contact an individual’s financial institution and connect with their account(s).', 'کریڈٹ، ڈیبٹ اور اے ٹی ایم کارڈ: ان سب کارڈوں کے ایک طرف مقناطیسی پٹی ہوتی ہے۔ یہ پٹی متعلقہ مالی ادارے سے رابطہ کرنے اور صارف کے کھاتے تک رسائی کی معلومات محفوظ کرتی ہے۔','کریډېټ، ډېبېټ او ATM کارتونه: د دغو ټولو کارتونو پر یوه خوا مقناطیسي پټه وي. دا پټه د شخص له مالي ادارې سره د اړیکې او د هغه حساب یا حسابونو ته د لاسرسي معلومات کوډوي.'),
]

if __name__=='__main__':
 layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'list','indices':list(range(4,4+len(OUTCOMES)))}]
 # Outcomes use a single continuous source-ordered list across printed pages 88–89.
 start=4+len(OUTCOMES)
 layout += [{'type':'paragraph','indices':[start]},{'type':'paragraph','indices':[start+1]},{'type':'heading','indices':[start+2]},{'type':'heading','indices':[start+3]},{'type':'paragraph','indices':[start+4]},{'type':'paragraph','indices':[start+5]}]
 r={'id':'phys13-unit-opening-and-outcomes88-89','title':'Unit 13 Electromagnetism — opening, outcomes and magnetic-media information','kind':'lesson','pdfPage':49,'printedPage':88,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in CONTENT]}
 s=section(r,CONTENT,layout,('یونٹ 13 برقی مقناطیسیت — تعارف، حاصلات اور مقناطیسی میڈیا','۱۳م یونټ برېښنا-مقناطیسیت — سریزه، پایلې او مقناطیسي رسنۍ'))
 s['kind']='lesson';s['sourceReferences']=[ref(88),ref(89)]
 with shared_class_data_lock():
  upsert([r],[s],chapter_index=2)
  sync_companions(chapter_index=2,trim_sections=[{'id':'13.1','startsAt':'13.1 MAGNETIC FIELD','title':'Unit 13 — first unchecked section 13.1'}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==49:
  checkpoint(49,'corrected_verified',[r['id']],'Rendered and inspected PDF page 49, printed pages 88–89. Compared the Unit 13 cover title/prompt, all 16 learning outcomes across both pages, magnet and permanent-magnet explanation, and the complete recording-media/swipe-card information panel. Paired all source text in English/Urdu/Pashto, omitted only noninstructional cover and stock-photo artwork, and trimmed the legacy OCR extract at the first unchecked section heading 13.1.',printed_pages=[88,89],chapter_number=13)
