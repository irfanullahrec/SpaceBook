from enghelp import *
c=cell
U='back-matter'
# ---------- scan 239 (unnumbered back page: feedback form) ----------
s=page(239,U,'—','Textbook feedback form (Khyber Pakhtunkhwa Textbook Board)','نصابی کتاب کا فیڈبیک فارم (خیبر پختونخوا ٹیکسٹ بک بورڈ)','د درسي کتاب د نظر فورمه (د خیبر پښتونخوا د درسي کتابونو بورډ)','feedback-form')
F=Flow(s)
add(s,'b1','Khyber Pakhtunkhwa Textbook Board','خیبر پختونخوا ٹیکسٹ بک بورڈ','د خیبر پښتونخوا د درسي کتابونو بورډ',kind='heading')
add(s,'b2','Phase – V, Hayatabad Peshawar','فیز – V، حیات آباد پشاور','فیز – V، حیات‌اباد پېښور')
add(s,'b3','Phone: 091-9217714-15  Fax: 091-9217163, Website: www.kptbb.gov.pk','فون: 091-9217714-15 فیکس: 091-9217163، ویب سائٹ: www.kptbb.gov.pk','تلیفون: 091-9217714-15 فکس: 091-9217163، ویب‌پاڼه: www.kptbb.gov.pk')
add(s,'t','TEXTBOOK FEEDBACK FORM','نصابی کتاب کا فیڈبیک فارم','د درسي کتاب د نظر فورمه',kind='heading')
S=[('Overall the book is interesting and user friendly.','مجموعی طور پر کتاب دلچسپ اور استعمال میں آسان ہے۔','په ټوله کې کتاب په زړه پورې او د کارونې لپاره اسانه دی.'),
('The language and content of the book is age / grade appropriate and the content is free of grammatical and punctuation errors.','کتاب کی زبان اور مواد عمر/جماعت کے لحاظ سے موزوں ہے اور مواد گرامر اور رموزِ اوقاف کی غلطیوں سے پاک ہے۔','د کتاب ژبه او منځپانګه د عمر/ټولګي له مخې مناسبه ده او منځپانګه د ګرامر او د ټکو نښو له تېروتنو پاکه ده.'),
('Content is supported with examples from real life / culture.','مواد کو حقیقی زندگی/ثقافت کی مثالوں سے تقویت دی گئی ہے۔','منځپانګه د ریښتینې ژوند/کلتور له بېلګو سره ملاتړ شوې ده.'),
('Contents / texts are authentic and updated.','مندرجات/متن مستند اور تازہ ترین ہیں۔','منځپانګې/متنونه معتبر او نوي شوي دي.'),
('Pictures / diagrams / graphs / illustrations are informative, relevant and clear if not, then identify them.','تصاویر/خاکے/گراف/مثالی تصاویر معلوماتی، متعلقہ اور واضح ہیں، اگر نہیں تو ان کی نشاندہی کریں۔','انځورونه/ډیاګرامونه/ګرافونه/روښانونې معلوماتي، اړوند او روښانه دي، که نه نو هغوی وپېژنئ.'),
('Activities, projects and additional work is suggested for reinforcement of concepts.','تصورات کی مضبوطی کے لیے سرگرمیاں، منصوبے اور اضافی کام تجویز کیے گئے ہیں۔','د مفکورو د پیاوړتیا لپاره فعالیتونه، پروژې او اضافي کار وړاندیز شوی دی.'),
('Assessment achievements are thought provoking and comprise cognitive, psychomotor and effective skills.','تشخیصی کامیابیاں غور و فکر پر اکسانے والی ہیں اور ادراکی، نفسی حرکی اور جذباتی (affective) مہارتوں پر مشتمل ہیں۔','د ارزونې لاسته‌راوړنې فکر راپارونکې دي او ادراکي، رواني‌حرکي او احساسي مهارتونه لري.'),
('The textbook is easy to be covered within academic year.','نصابی کتاب تعلیمی سال کے اندر پوری کرنا آسان ہے۔','درسي کتاب د تعلیمي کال په ترڅ کې پوره کول اسانه دي.')]
rows=[[c(str(i),str(i),str(i)),c(a,b,d),c('','','')] for i,(a,b,d) in enumerate(S,1)]
rows2=[[c('','',''),c('','',''),c('','','')] for _ in range(5)]
s['tables']=[table('Textbook feedback — statements','فیڈبیک — بیانات','د نظر — بیانونه',[c('S#','نمبر شمار','لړ'),c('Statement','بیان','بیان'),c('Remarks','ریمارکس','نظر')],rows),
             table('Textbook feedback — page comments','فیڈبیک — صفحہ وار تبصرے','د نظر — د پاڼو څرګندونې',[c('Page No.','صفحہ نمبر','د پاڼې شمېره'),c('Observation/comments','مشاہدہ/تبصرے','کتنه/څرګندونې'),c('Suggested amendment along with rationale','مجوزہ ترمیم بمع جواز','وړاندیز شوې ترمیم له دلیل سره')],rows2)]
F.tb(0)
add(s,'g','General Remarks: ____________________________','عمومی ریمارکس: ____________________________','عمومي نظر: ____________________________')
add(s,'n1','Name & Address: ____________________________','نام اور پتہ: ____________________________','نوم او پته: ____________________________')
add(s,'n2','Contact No. & Email: ____________________________','رابطہ نمبر اور ای میل: ____________________________','د اړیکې شمېره او بریښنالیک: ____________________________')
F.tb(1)
F.done()
s['sourceNote']='Back page (unnumbered, scan 239): the Khyber Pakhtunkhwa Textbook Board "Textbook Feedback Form" (printed on a separate form sheet): the board letterhead (emblem not reproduced), a table of eight statements with a Remarks column, a second table with columns Page No. / Observation-comments / Suggested amendment along with rationale (five blank rows) and lines for General Remarks, Name & Address and Contact No. & Email. The right edge of the scan clips the last letters of some cells (e.g. "rationale"). The printed word is "effective skills" (for "affective skills"); kept as printed. The form\'s blank lines and cells are shown as blanks. The Urdu and Pashto texts are translations by us. The watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 240 (unnumbered: Quran verse) ----------
s=page(240,U,'—','Quranic verse (Surah Al-Hujurat 49:10) — Urdu translation','قرآنی آیت (سورۃ الحجرات 49:10) — اردو ترجمہ','قرآني آیت (سورة الحجرات ۴۹:۱۰) — اردو ژباړه','quran-verse')
F=Flow(s)
add(s,'q1','The believers are brothers to one another.','مومن تو آپس میں بھائی بھائی ہیں۔','مومنان خو یو له بل سره وروڼه دي.')
add(s,'q2','So make peace between two of your brothers.','تو اپنے دو بھائیوں میں صلح کرا دیا کرو۔','نو د خپلو دوو وروڼو ترمنځ سوله وکړئ.')
add(s,'q3','And keep fearing Allah.','اور اللہ سے ڈرتے رہو۔','او له الله نه ویره ولرئ.')
add(s,'q4','So that mercy may be shown to you.','تاکہ تم پر رحمت کی جائے۔','ترڅو پر تاسو رحمت وشي.')
add(s,'q5','(Surah Al-Hujurat: 10)','(سورۃ الحجرات: 10)','(سورة الحجرات: ۱۰)')
F.done()
s['sourceNote']='Back page (unnumbered, scan 240): a framed Urdu translation of Qur\'an 49:10 (Surah Al-Hujurat) in a floral border: "مومن تو آپس میں بھائی بھائی ہیں۔ / تو اپنے دو بھائیوں میں صلح کرا دیا کرو۔ / اور اللہ سے ڈرتے رہو۔ / تاکہ تم پر رحمت کی جائے۔ / (سورۃ الحجرات: ۱۰)". The printed text is Urdu only; the Urdu column here repeats it as printed (the verse number is printed in Eastern Arabic digits "۱۰"), and the English and Pashto columns are renderings of that Urdu by us. The left edge of the scan shows a strip of the feedback form (ignored). The floral border is not reproduced. The watermark and the "Whatsapp" strip are excluded.'
s['vocabulary']={}
save(s)
