from ikhtiarihelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,ur,en,ps,g,**m): add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g,**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 6 (scans 1–29), scan − 5 from scan 30.'
def toc(s,rows,note):
    hd=[c('Chapter / section','باب / حصہ','څپرکی / برخه'),c('Contents','مضامین','مضامین'),c('Page','صفحہ نمبر','د پاڼې شمېره')]
    body=[[c(ch,ch_u,ch_p),c(en,ur,ps),c(str(pg))] for ch,ch_u,ch_p,ur,en,ps,pg in rows]
    return table('Table of contents','فہرستِ عنوانات','د سرلیکونو فهرست',hd,body,sourceGap=dict(note=note))
def R(ch,chu,chp,ur,en,ps,pg): return (ch,chu,chp,ur,en,ps,pg)
# scan 1 = file 1
s=page(1,'front-matter','','Front cover','سرورق','پوښ','cover')
F=Flow(s)
H(s,'اسلامیات (اختیاری)','Islamiat (Elective)','اسلامیات (اختیاري)')
P(s,'برائے گیارھویں جماعت','For the eleventh class','د یوولسم ټولګي لپاره')
P(s,'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','Khyber Pakhtunkhwa Textbook Board, Peshawar','د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
F.done()
s['sourceNote']='Front cover: title, class and board name over a picture of the Kaaba; the picture and board emblem are not reproduced (no raster images). Website watermark and “NOT FOR SALE” stamps excluded.'+NOTE
s['vocabulary']={}
save(s)
# scan 2 = file 3
s=page(2,'front-matter','','Two sayings (Quran 49:10 and a call against bribery)','دو اقوال (الحجرات: ۱۰ اور رشوت کے خلاف)','دوه وینا (الحجرات: ۱۰ او د رشوت پر ضد)','sayings')
F=Flow(s)
P(s,'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔ (سورۃ الحجرات: ۱۰)','The believers are but brothers. So make peace between your two brothers, and fear Allah that you may receive mercy. (Surah Al-Hujurat: 10)','مومنان خو یو بل ته وروڼه دي. نو خپلو دوو وروڼو ترمنځ سوله وکړئ او له الله نه ووېرېږئ چې پر تاسو رحم وشي. (سورة الحجرات: ۱۰)',boxed=True)
P(s,'رشوت اور بد عنوانی قومی معیشت کو کھوکھلا کر دیتی ہے۔ قومی معیشت کو کھوکھلا ہونے سے بچانے میں اپنا کردار ادا کرو۔','Bribery and corruption hollow out the national economy. Play your part in saving the national economy from being hollowed out.','رشوت او فساد ملي اقتصاد کوڼدی کوي. د ملي اقتصاد د کوڼدي کېدو څخه د ژغورلو لپاره خپل رول ولوبوئ.',boxed=True)
F.done()
s['sourceNote']='Page with two boxed texts in decorative frames: Quran 49:10 and a slogan against bribery and corruption. Handwriting excluded.'+NOTE
s['vocabulary']={}
save(s)
# scan 3 = file 4
s=page(3,'front-matter','','Title page','عنوانی صفحہ','د سرلیک پاڼه','title')
F=Flow(s)
H(s,'اسلامیات (اختیاری)','Islamiat (Elective)','اسلامیات (اختیاري)')
P(s,'برائے گیارھویں جماعت','For the eleventh class','د یوولسم ټولګي لپاره')
P(s,'Published by: Leading Books Publisher','Published by: Leading Books Publisher','Published by: Leading Books Publisher')
P(s,'Khyber Pakhtunkhwa Textbook Board Peshawar','Khyber Pakhtunkhwa Textbook Board Peshawar','Khyber Pakhtunkhwa Textbook Board Peshawar')
F.done()
s['sourceNote']='Title page in a blue frame: title, class, publisher and board name; the publisher seal and board emblem are not reproduced.'+NOTE
s['vocabulary']={}
save(s)
# scan 4 = file 5
s=page(4,'front-matter','','Rights, approval, authors, reviewers, editor, supervision','حقوق، منظوری، مصنفین، نظر ثانی، تدوین، نگرانی','حقونه، منظوري، لیکوالان، بیاکتنه، ترتیب، څارنه','credits')
F=Flow(s)
H(s,'جملہ حقوق بحق لیڈنگ بکس پبلشر محفوظ ہیں','All rights reserved by Leading Books Publisher','ټول حقونه د لیډنګ بکس پبلشر سره خوندي دي')
P(s,'منظور کردہ: نظامتِ نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد','Approved by: Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','منظور شوی: د خیبر پښتونخوا د نصاب او د استادانو د زده کړې رياست، ابیټ اباد')
P(s,'بمطابق: قومی نصاب 2006','In accordance with: National Curriculum 2006','سره سم: ملي نصاب ۲۰۰۶')
P(s,'مراسلہ نمبر 6173-75/SS-II مؤرخہ 30-10-2012ء','Letter No. 6173-75/SS-II dated 30-10-2012','مراسله شمېره 6173-75/SS-II، نېټه 30-10-2012')
P(s,'مصنفین: پروفیسر ڈاکٹر آصف محمود، مسز ناصرہ حمید، شمس الحق ظہیر، محترمہ پروین اختر، محترمہ عنبر نوریز','Authors: Professor Dr. Asif Mahmood, Mrs. Nasira Hameed, Shams-ul-Haq Zaheer, Ms. Parveen Akhtar, Ms. Amber Nowrez','لیکوالان: پروفیسر ډاکټر آصف محمود، مسز ناصره حمید، شمس الحق ظهیر، محترمه پروین اختر، محترمه عنبر نوریز')
P(s,'نظرِ ثانی: پروفیسر ڈاکٹر مفتی عبد الوہاب، گورنمنٹ ڈگری کالج منڈیاں ایبٹ آباد؛ پروفیسر عبد الصبور انیس، گورنمنٹ کالج نمبر 1 ایبٹ آباد؛ صفدر رحمان، لائبریرین ڈی۔ سی۔ ٹی۔ ای، ایبٹ آباد؛ سید رفاقت علی شاہ، ماہر مضمون ٹیکسٹ بک بورڈ پشاور','Review: Professor Dr. Mufti Abdul Wahab, Government Degree College Mandian, Abbottabad; Professor Abdul Sabur Anis, Government College No. 1, Abbottabad; Safdar Rahman, Librarian, DCTE, Abbottabad; Syed Rafaqat Ali Shah, Subject Specialist, Textbook Board Peshawar','بیاکتنه: پروفیسر ډاکټر مفتي عبدالوهاب، دولتي ډګري کالج منډیان ابیټ اباد؛ پروفیسر عبدالصبور انیس، دولتي کالج شمېره ۱ ابیټ اباد؛ صفدر رحمان، کتابتون وال، ډي سي ټي اي، ابیټ اباد؛ سید رفاقت علي شاه، د مضمون ماهر، د درسي کتابونو بورډ پېښور')
P(s,'تدوین: علامہ سید قاضی محمد وجیہ الدین چشتی (تنگی)، ماہر مضمون اسلامیات، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','Compilation: Allama Syed Qazi Muhammad Wajeeh-ud-Din Chishti (Tangi), Subject Specialist for Islamiat, Khyber Pakhtunkhwa Textbook Board Peshawar','ترتیب: علامه سید قاضي محمد وجیه الدین چشتي (تنګي)، د اسلامیاتو د مضمون ماهر، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور')
P(s,'زیر نگرانی و رہنمائی: ظریف المعانی (چیئرمین)؛ عبدالولی خان (ممبر ای اینڈ پی)، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','Under supervision and guidance of: Zareef-ul-Maani (Chairman); Abdul Wali Khan (Member E&P), Khyber Pakhtunkhwa Textbook Board Peshawar','تر څارنې او لارښوونې لاندې: ظریف المعاني (رئیس)؛ عبدالولي خان (ممبر ای اینډ پي)، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور')
P(s,'تعلیمی سال 2023-24ء۔ ویب سائٹ: www.kptbb.gov.pk، ای میل: membertbb@yahoo.com، فون نمبر 091-9217159-60','Academic year 2023-24. Website: www.kptbb.gov.pk, e-mail: membertbb@yahoo.com, phone: 091-9217159-60','تعلیمي کال ۲۰۲۳-۲۴. ویب پاڼه: www.kptbb.gov.pk، ای میل: membertbb@yahoo.com، تلیفون: 091-9217159-60')
F.done()
s['sourceNote']='Credits page: rights notice in a rounded box, approval letter, authors, reviewers, editor, supervision and board contact details. Blurred strips at the left edge and the faint board logo are not reproduced.'+NOTE
s['vocabulary']={}
save(s)
# scan 5 = file 6
s=page(5,'front-matter','','Preface (Pesh lafz)','پیش لفظ','سریزه','preface')
F=Flow(s)
P(s,'بسم اللہ الرحمٰن الرحیم','In the name of Allah, the Most Gracious, the Most Merciful','د الله په نوم چې ډیر مهربان او بې حده رحم کوونکی دی')
H(s,'پیش لفظ','Preface','سریزه')
P(s,'پاکستان ایک نظریاتی ملک ہے جس کی بنیاد اسلام ہے اس لحاظ سے یہاں اسلامیات کا مضمون خصوصی اہمیت کا حامل ہے۔ اس کے دوہرے مقاصد ہیں۔ ایک تو طلباء اور طالبات کا معیارِ تعلیم بلند ہو اور دوسرا ان کے اندر صحیح معنوں میں اسلامی روح پیدا ہو تا کہ وہ بہتر مسلمان اور اچھے پاکستانی کی حیثیت سے اپنی وسیع تر ذمہ داریوں کو کما حقہ پورا کر سکیں۔ اس مضمون کا مطالعہ محض امتحانی نقطۂ نظر ہی سے نہیں کرنا چاہیے بلکہ یہ پہلو بھی پیشِ نظر رکھنا چاہیے کہ ایک مسلمان کی حیثیت سے دین کا فہم حاصل کرنا اور اس پر عمل کرنا ہمارے فرائض میں شامل ہے۔','Pakistan is an ideological country whose foundation is Islam; in that respect the subject of Islamiat holds special importance here. It has a twofold purpose: first, that the standard of education of students be raised, and second, that a true Islamic spirit be created in them so that, as better Muslims and good Pakistanis, they can fully discharge their wider responsibilities. This subject should not be studied merely from the point of view of examination, but one should also keep in mind that, as a Muslim, acquiring an understanding of religion and acting upon it is part of our duties.','پاکستان یو نظریاتي هېواد دی چې بنسټ يې اسلام دی، په دې لحاظ دلته د اسلامیاتو مضمون ځانګړې اهمیت لري. دا دوه ګونې موخې لري: یو دا چې د زده کوونکو د زده کړې کچه لوړه شي او بل دا چې په دوی کې په سم مانا اسلامي روحیه پیدا شي ترڅو د ښه مسلمان او ښه پاکستاني په توګه خپلې پراخې مسؤلیتونه په سمه توګه ادا کړای شي. د دې مضمون مطالعه یوازې د امتحان له نظره نه بلکې دا اړخ هم باید پام کې ونیول شي چې د یو مسلمان په توګه د دین پوهه ترلاسه کول او پر هغه عمل کول زموږ په دندو کې شامل دي.')
P(s,'اسلامیات اگرچہ نسبتاً آسان مضمون ہے لیکن اس میں طلباء اور طالبات کو ایک بڑی دقت یہ پیش آتی ہے کہ اکثر موضوعات تشنہ ہوتے ہیں اور خاص طور پر سورتوں، آیاتِ قرآنی، احادیث اور قواعد کی تشریح بہت کم کی گئی ہوتی ہے۔ اسی طرح دیگر موضوعات پر بھی خاطر خواہ معیاری مواد دستیاب نہیں ہوتا۔ زیرِ نظر کتاب میں اسی دقت کو رفع کرنے کی کوشش کی گئی ہے اور مختلف موضوعات پر مفصل، معیاری، جامع اور مستند مواد فراہم کیا گیا ہے۔ آیاتِ قرآنی، احادیث اور دیگر موضوعات کو پیش کرتے ہوئے اس امر کو ملحوظ رکھا گیا ہے کہ گویا موضوع کا تعین کر کے اس پر ایک مختصر سا مضمون لکھنا ہے۔','Although Islamiat is a relatively easy subject, students face one great difficulty in it: most topics are left unsatisfying, and especially the explanation of surahs, Quranic verses, hadiths and rules is very scanty. Likewise, satisfactory standard material is not available on other topics either. In this book an effort has been made to remove this difficulty, and detailed, standard, comprehensive and authentic material has been provided on different topics. While presenting Quranic verses, hadiths and other topics, care has been taken as if, having fixed the topic, a short essay is to be written on it.','که څه هم اسلامیات نسبتاً اسانه مضمون دی خو زده کوونکو ته پکې یوه لویه ستونزه دا ده چې ډیر موضوعات نیمګړي وي او په ځانګړې توګه د سورتونو، قرآني آیتونو، حدیثونو او قواعدو تشریح ډیره لږه شوې وي. همدارنګه په نورو موضوعاتو هم کافي معیاري مواد نه شته. په دې کتاب کې همدا ستونزه لرې کولو هڅه شوې او په مختلفو موضوعاتو مفصل، معیاري، جامع او معتبر مواد برابر شوي. د قرآني آیتونو، حدیثونو او نورو موضوعاتو په وړاندې کولو کې دا خبره په پام کې نیول شوې چې ګواکې موضوع ټاکل شوې او پر هغې یو لنډ مضمون لیکل دي.')
P(s,'ان شاء اللہ یہ کتاب طلباء اور طالبات میں علومِ دینیہ کے حصول کا شوق پیدا کر کے مزید اعلیٰ کتب کے مطالعے کا ذریعہ بنے گی۔ اگر اس کتاب میں کوئی خوبی ہے تو اللہ تعالیٰ کی طرف سے ہے اور اگر کوئی خامی ہے تو وہ ہماری طرف سے ہے۔','God willing, this book will create in students the desire to acquire religious sciences and become a means of studying further higher books. If there is any merit in this book it is from Allah, and if there is any fault it is from us.','ان شاء الله دا کتاب به په زده کوونکو کې د دیني علومو د زده کړې شوق پیدا کړي او د نورو لوړو کتابونو د مطالعې وسیله به شي. که په دې کتاب کې کومه ښېګڼه وي د الله تعالی له لوري ده او که کومه کمي وي نو هغه زموږ له لوري ده.')
P(s,'دُعا ہے کہ اللہ تعالیٰ ہماری اس معمولی کوشش کو شرفِ قبولیت بخشے اور اسے نونہالانِ ملت کے لیے مفید اور کارآمد بنائے۔ (آمین)','It is our prayer that Allah accept this humble effort of ours and make it useful and beneficial for the children of the nation. (Amen)','دعا ده چې الله تعالی زموږ دغه ناچیزه هڅه ومني او دا د ملت د ماشومانو لپاره ګټوره او کارنده کړي. (آمین)')
F.done()
s['sourceNote']='Preface page. The Bismillah is printed in Arabic script with vowel marks at the top. The scan is clean; blue marks in the margin excluded.'+NOTE
s['vocabulary']={}
save(s)
# scan 6 = file 7 contents
s=page(6,'front-matter','','Table of contents (Fehrist unwanat)','فہرستِ عنوانات','د سرلیکونو فهرست','toc')
F=Flow(s)
H(s,'فہرستِ عنوانات','Table of contents','د سرلیکونو فهرست')
F.tb(0)
F.done()
rows=[R('باب اول','Chapter 1','لومړی باب','قرآن مجید','The Holy Quran','قرآن مجید','1'),
R('الف','(a)','الف','کتابتِ قرآن','Writing down of the Quran','د قرآن لیکل','3'),
R('ب','(b)','ب','ترجمہ و تفسیرِ قرآن','Translation and exegesis of the Quran','د قرآن ژباړه او تفسیر','16'),
R('ج','(c)','ج','قرآن مجید کے اساسی مباحث','Fundamental topics of the Holy Quran','د قرآن مجید اساسي مباحث','22'),
R('د','(d)','د','عبادات','Acts of worship','عبادتونه','58'),
R('ہ','(e)','ه','سیرتِ رسول ﷺ کا قرآن مجید کی روشنی میں مطالعہ','Study of the Prophet’s biography in the light of the Quran','د قرآن په رڼا کې د رسول ﷺ د سیرت مطالعه','79'),
R('و','(f)','و','منتخب آیاتِ قرآن: ترجمہ و تفسیر','Selected Quranic verses: translation and exegesis','ټاکل شوي قرآني آیتونه: ژباړه او تفسیر','107'),
R('باب دوم','Chapter 2','دوهم باب','حدیث','Hadith','حدیث','124'),
R('','','','منتخب احادیث کا ترجمہ و تشریح','Translation and explanation of selected hadiths','د ټاکل شويو حدیثونو ژباړه او تشریح','137'),
R('باب سوم','Chapter 3','دریم باب','علمی پیش رفت میں مسلمانوں کی خدمات','Services of Muslims in scientific progress','په علمي پرمختګ کې د مسلمانانو خدمتونه','164'),
R('باب چہارم','Chapter 4','څلورم باب','اسلام کا نظامِ حکومت و ریاست','Islam’s system of government and state','د اسلام د حکومت او دولت نظام','189'),
R('باب پنجم','Chapter 5','پنځم باب','عصرِ حاضر اور اسلامی ریاستیں','The present age and Islamic states','اوسنی عصر او اسلامي دولتونه','235'),
R('باب ششم','Chapter 6','شپږم باب','عربی زبان و ادب','Arabic language and literature','عربي ژبه او ادب','257')]
s['tables']=[toc(s,rows,'Contents page with a page-number column; the order of rows follows the printed layout (chapter at right, page numbers at left). Chapter 1 is divided into six lettered parts (الف–و). Handwriting excluded.')]
s['sourceNote']='Contents page (“فہرستِ عنوانات”) in a blue frame: chapter column, titles and printed page numbers.'+NOTE
s['vocabulary']={}
save(s)
# scan 7 = file 8, printed 1
s=page(7,'ch1','1','Chapter 1: The Holy Quran — chapter opener and teaching objectives','باب اول: قرآن مجید — تدریسی مقاصد','لومړی باب: قرآن مجید — د تدریس موخې','ch1open')
F=Flow(s)
P(s,'بِسْمِ اللّٰہِ الرَّحْمٰنِ الرَّحِیْمِ۔ شروع کرتا ہوں اللہ تعالیٰ کے نام سے جو بڑا مہربان نہایت رحم والا ہے۔','In the name of Allah, the Most Gracious, the Most Merciful. I begin with the name of Allah who is very kind and ever merciful.','د الله تعالی په نوم چې ډیر مهربان او بې حده رحم کوونکی دی.')
H(s,'باب اول: قرآن مجید','Chapter One: The Holy Quran','لومړی باب: قرآن مجید')
H(s,'تدریسی مقاصد','Teaching objectives','د تدریس موخې')
P(s,'اس سبق کے پڑھنے کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After reading this lesson students will be able to:','د دې درس له لوستلو وروسته به زده کوونکي دې ته وړ شي چې:')
I(s,'۱۔ قرآن مجید میں توحید، رسالت، آخرت، ملائکہ، عبادت اور نبی کریم صلی اللہ علیہ و آلہ و اصحابہ و سلم کے مقام و منصب کے حوالے سے آیات کا تفصیلی مطالعہ کرنے کی استعداد پا سکیں اور مجوزہ آیاتِ قرآنیہ کا ترجمہ اور تشریح کر سکیں۔','1. acquire the ability to study in detail the verses of the Holy Quran about monotheism, prophethood, the hereafter, angels, worship and the status and office of the Holy Prophet (peace and blessings be upon him, his family and companions), and be able to translate and explain the prescribed Quranic verses.','۱. په قرآن مجید کې د توحید، رسالت، آخرت، ملایکو، عبادت او د نبي کریم صلی الله علیه و آله و اصحابه و سلم د مقام او منصب په اړه د آیتونو تفصیلي مطالعې وړتیا ترلاسه کړي او ټاکل شوي قرآني آیتونه ژباړه او تشریح کړای شي.','obj')
I(s,'۲۔ قرآن مجید کے اساسی مباحث جو عقائد، غور و فکر اور سماج و تمدن سے متعلق ہیں، کے بارے میں قرآن مجید کی منتخب آیات کا مطالعہ کر سکیں اور اپنی زندگی کو انفرادی اور اجتماعی سطح پر ان تعلیمات کے مطابق بنا سکیں۔','2. study selected verses of the Holy Quran on its fundamental topics relating to beliefs, reflection and society and civilisation, and shape their lives at the individual and collective level according to these teachings.','۲. د قرآن مجید د هغو اساسي مباحثو په اړه چې له عقایدو، غور او فکر او ټولنې او تمدن سره تړاو لري د قرآن مجید ټاکلي آیتونه مطالعه کړای شي او خپل ژوند په انفرادي او ټولنیز کچه د دغو تعلیماتو سره سم جوړ کړای شي.','obj')
I(s,'۳۔ قرآنی آیات کے تناظر میں سیرتِ نبی اکرم صلی اللہ علیہ و آلہ و اصحابہ و سلم کے مختلف پہلوؤں سے روشناس ہو سکیں اور عملی زندگی میں ان کی اہمیت جان کر اپنی زندگی کے مطابق بنا سکیں۔','3. become familiar with the different aspects of the biography of the Holy Prophet (peace and blessings be upon him, his family and companions) in the context of Quranic verses, and, knowing their importance in practical life, adapt their lives accordingly.','۳. د قرآني آیتونو په شرایطو کې د نبي اکرم صلی الله علیه و آله و اصحابه و سلم د سیرت له مختلفو اړخونو سره بلد شي او په عملي ژوند کې د هغو اهمیت پېژندلو سره خپل ژوند ورسره برابر کړای شي.','obj')
F.done()
s['sourceNote']='Printed page 1: chapter opener with a mosque-dome drawing (not reproduced), the Bismillah with an Urdu translation line, the chapter banner “باب اول — قرآن مجید” and a light-blue box “تدریسی مقاصد” with three numbered objectives.'+NOTE
s['vocabulary']={}
save(s)
# scan 8 = file 9, printed 2
s=page(8,'ch1','2','The Holy Quran: introduction; (a) Writing down of the Quran — start','قرآن مجید: تمہید؛ الف۔ کتابتِ قرآن کا آغاز','قرآن مجید: سریزه؛ الف. د قرآن لیکل پیل','ch1p2')
F=Flow(s)
H(s,'قرآن مجید','The Holy Quran','قرآن مجید')
P(s,'قرآن مجید اللہ تعالیٰ کی وہ مقدس کتاب ہے جو اس نے اپنے پیارے رسول حضرت محمد رسول اللہ خاتم النبیین صلی اللہ علیہ و آلہ و اصحابہ و سلم پر نازل کی۔ قرآن مجید تمام انسانوں کے لیے ہدایت اور راہنمائی کا ذریعہ ہے۔ ارشادِ ربانی ہے:','The Holy Quran is the sacred book of Allah which He sent down upon His beloved Messenger Hazrat Muhammad, the Messenger of Allah, the Seal of the Prophets (peace and blessings be upon him, his family and companions). The Holy Quran is a means of guidance and direction for all human beings. The divine saying is:','قرآن مجید د الله تعالی هغه سپېڅلی کتاب دی چې هغه خپل ګران رسول حضرت محمد رسول الله خاتم النبیین صلی الله علیه و آله و اصحابه و سلم ته نازل کړ. قرآن مجید د ټولو انسانانو لپاره د هدایت او لارښوونې وسیله ده. ربانی ارشاد دی:')
P(s,'قَدْ جَآءَكُمْ مِّنَ اللّٰهِ نُوْرٌ وَّكِتٰبٌ مُّبِيْنٌ (المائدہ: ۱۵)','Indeed, there has come to you from Allah a light and a clear Book. (Al-Ma’idah: 15)','په یقین سره ستاسو سره د الله له لوري نور او روښانه کتاب راغلی دی. (المائده: ۱۵)',boxed=True)
P(s,'ترجمہ: تحقیق تمہارے پاس اللہ کی طرف سے نور (روشنی) اور کھلی کتاب آئی ہے۔','Translation: Indeed, there has come to you from Allah light and a clear book.','ژباړه: په یقین سره ستاسو سره د الله له لوري رڼا او خلاص کتاب راغلی دی.')
P(s,'قرآن مجید ہماری انفرادی اور اجتماعی زندگی کے ہر مسئلے کا حل بتاتا ہے اور ہماری رہنمائی کرتا ہے۔','The Holy Quran shows the solution to every problem of our individual and collective life and guides us.','قرآن مجید زموږ د انفرادي او ټولنیز ژوند هره ستونزه حل ښيي او زموږ لارښوونه کوي.')
P(s,'قرآن مجید کے مختلف نام ہیں جن میں الکتاب (کامل کتاب یعنی اللہ تعالیٰ کی کتاب)، الفرقان (حق و باطل میں فرق کرنے والا)، الذکر (نصیحت)، الشفا (تندرستی، صحت)، النور (روشنی) وغیرہ شامل ہیں۔','The Holy Quran has various names, among them al-Kitab (the complete book, i.e. the book of Allah), al-Furqan (that which distinguishes truth from falsehood), al-Dhikr (admonition), al-Shifa (healing, health), al-Nur (light) and so on.','قرآن مجید مختلف نومونه لري چې په هغو کې الکتاب (بشپړ کتاب یعنې د الله تعالی کتاب)، الفرقان (د حق او باطل ترمنځ توپیر کوونکی)، الذکر (نصیحت)، الشفا (روغتیا، صحت)، النور (رڼا) او نور شامل دي.')
P(s,'قرآن مجید میں تیس پارے، ۱۱۴ سورتیں اور سات منزلیں ہیں۔','The Holy Quran has thirty parts (paras), 114 surahs and seven stages (manzils).','په قرآن مجید کې دېرش پارې، ۱۱۴ سورتونه او اووه منزلونه دي.')
H(s,'الف۔ کتابتِ قرآن','(a) Writing down of the Quran','الف. د قرآن لیکل')
P(s,'آنحضرت صلی اللہ علیہ و آلہ و اصحابہ و سلم نے شروع ہی سے اس بات کا اہتمام کیا کہ کلامِ الٰہی کو خود اپنی عام بات چیت سے الگ محفوظ اور ممتاز کر دیا جائے۔ آپ صلی اللہ علیہ و آلہ و اصحابہ و سلم خود تو اُمی تھے اس لیے نزولِ وحی کے بعد کسی پڑھے لکھے','From the very beginning the Holy Prophet (peace and blessings be upon him, his family and companions) took care that the Word of Allah be kept safe and distinct from his own ordinary speech. He himself being unlettered (ummi), after the revelation came down, some literate','نبي کریم صلی الله علیه و آله و اصحابه و سلم له پیله دې خبرې ته پاملرنه وکړه چې د الله کلام د هغه له خپلو عامو خبرو بېل او خوندي ساتل شي. هغه پخپله امي و، نو د وحې له نازلېدو وروسته به يې یو لیکلی لوستی',cont=True)
F.done()
s['sourceNote']='Printed page 2: the heading “قرآن مجید”, an introduction, the verse Al-Ma’idah 15 in a decorated box, its Urdu translation, the sub-heading “الف۔ کتابتِ قرآن” and the first two lines of its text; the last sentence continues on the next page. Page number 2 is in a blue disc at the foot.'+NOTE
s['vocabulary']={}
save(s)
