from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n12',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 162 = printed 155
s=page(162,'n12','155','Exercise (Mashq) on Qitaat; teachers’ instruction','مشق: «قطعات» پر سوالات؛ ہدایت برائے اساتذہ','تمرین: «قطعات» پوښتنې؛ د ښوونکو لارښوونه','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ شاعر کو نو جوان نسل سے کیا شکایت ہے؟','1. What is the poet’s complaint against the young generation?','۱. شاعر ته له ځوانې نسل نه کومه ګیله ده؟')
Q(s,'2۔ ان قطعات میں کن معاشرتی برائیوں کی نشان دہی کی گئی ہے۔','2. Which social evils have been pointed out in these quatrains?','۲. پدې قطعاتو کې د کومو ټولنیزو بدیو نښه ښودل شوې ده؟')
Q(s,'3۔ مصرعے مکمل کریں۔','3. Complete the lines.','۳. مصرعې بشپړې کړئ.')
for t in [('الف) انتظام ایسا کہ بس ____________','(a) “Intizam aisa ke bas ____________”','(الف) انتظام داسې چې بس ____________'),
('ب) اگر کوچوں میں بھنگی رات کو ____________','(b) “Agar koochon mein bhangi raat ko ____________”','(ب) که په کوڅو کې بهنګي د شپې ____________'),
('ج) کالے چشمے بھی ____________','(c) “Kaale chashme bhi ____________”','(ج) تورې عینکې هم ____________'),
('د) آج پانی میں ____________','(d) “Aaj pani mein ____________”','(د) نن په اوبو کې ____________')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-3')
Q(s,'4۔ جملوں میں استعمال کریں: دل کی کلی کھلنا، نعمت، نگاہیں ملانا، محتسب، مانند۔','4. Use in sentences: dil ki kali khilna, naimat, nigahen milana, muhtasib, manind.','۴. په جملو کې وکاروئ: د زړه غوټۍ خلاصېدل، نعمت، نظرونه ملول، محتسب، ماننده.')
Q(s,'5۔ قطعہ کسے کہتے ہیں؟ کسی شاعر کا قطعہ لکھیں جس میں شگفتہ پیرائے میں کسی سماجی برائی کا ذکر کیا گیا ہو۔','5. What is a qita? Write a qita of some poet in which a social evil is mentioned in a lively manner.','۵. قطعه ته څه وايي؟ د کوم شاعر قطعه ولیکئ چې په هغې کې په ژوندي ډول کومه ټولنیزه بدي یاده شوې وي.')
P(s,'طلبہ کو اقبالؒ اور اکبرؔ کے چند قطعات لکھوائیں۔','Have the students write some quatrains of Iqbal and Akbar.','زده‌کوونکو ته د اقبال او اکبر څو قطعات ولیکوئ.',boxed=True)
F.done()
s['sourceNote']='Printed page 155 (scan 162): “Mashq” title, questions 1–5 (question 3 has four half-lines with dotted rules; question 4 lists words in blue) and a boxed instruction whose blue label is too faint to read (the instruction reads “طلبہ کو اقبالؒ اور اکبرؔ کے چند قطعات لکھوائیں”).'+NOTE
s['vocabulary']={}
save(s)
# scan 163 = printed 156
s=page(163,'n13','156','Abdur Rahman Baba (poet profile)','عبدالرحمن باباؒ (شاعر کا تعارف)','عبدالرحمن بابا (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'عبدالرحمن باباؒ','Abdur Rahman Baba','عبدالرحمن بابا')
P(s,'پیدایش: ۱۶۵۳ء — وفات: ۱۷۱۱ء','Born: 1653 — Died: 1711','زېږېدنه: ۱۶۵۳ز — وفات: ۱۷۱۱ز')
P(s,'سترھویں صدی پشتو زبان و ادب کا دورِ زرّیں تھا۔ اس عرصے میں پشتو زبان و ادب کے بے شمار مستند اور معتبر شاعر و ادیب گزرے ہیں۔ جن میں خوشحال خان خٹک، عبدالحمید مومند، عبدالقادر خٹک، اشرف خان ہجری اور معزّ اللہ مومند کے ساتھ ساتھ عبدالرحمن باباؒ قابلِ ذکر ہیں۔','The seventeenth century was the golden age of the Pashto language and literature. In this period countless authentic and reliable poets and writers of Pashto language and literature lived, among whom Khushal Khan Khattak, Abdul Hameed Momand, Abdul Qadir Khattak, Ashraf Khan Hijri and Moazzullah Momand, along with Abdur Rahman Baba, are worthy of mention.','اوولسمه پېړۍ د پښتو ژبې او ادب زرینه دوره وه. پدې موده کې د پښتو ژبې او ادب بې شمېره معتبر شاعران او ادیبان تېر شوي دي. په هغو کې خوشحال خان خټک، عبدالحمید مومند، عبدالقادر خټک، اشرف خان هجري او معز الله مومند سره سره عبدالرحمن بابا د یادونې وړ دي.')
P(s,'عبدالرحمن باباؒ نے ساری زندگی اپنے آبائی گاؤں (بہادر کلے) ہزار خوانی پشاور میں گزاری۔ اُن کی شاعری پر فطرت اور حقیقت کا رنگ غالب ہے۔ ایسا لگتا ہے کہ وہ ہر دور اور ہر زمانے کے شاعر ہیں۔ اُن کے اشعار میں ماضی کی تاریخ، حال کا تذکرہ اور مستقبل کا پیغام جھلکتا ہے۔ اُن کا دیوان اگر چہ مختصر ہے لیکن علم و ادب کے لحاظ سے جامع اور مکمل ہے۔ پختون فطرت کی ترجمانی جس طرح عبدالرحمن باباؒ نے کی ہے کسی اور شاعر نے نہیں کی۔ اسی لیے جو مقبولیّت اُن کو حاصل ہے، کسی دوسرے شاعر کو نصیب نہیں ہوئی۔ اُن کے اشعار نہ صرف عشقِ حقیقی اور تصوّف کے آئینہ دار ہیں، بل کہ ابدی زندگی میں کام یابی کے لیے پند نامہ بھی ہیں۔ قرآن و احادیث کی تشریح و توضیح اُن کی شاعری کا خاصہ ہے۔ اُن کی شاعرانہ عظمت کا اندازہ اس بات سے لگایا جا سکتا ہے کہ اُن کے دیوان کے تراجم دنیا کی مختلف زبانوں میں ہو چکے ہیں اور لوگ اُن کی تعلیمات سے مستفید ہو رہے ہیں۔ اُن کی شاعری کے موضوعات محنت کی عظمت، رزقِ حلال، اسلامی اُصول، علم کی اہمیّت و افادیّت اور دنیا کی بے ثباتی جیسے حقائق پر مبنی ہیں۔','Abdur Rahman Baba spent all his life in his ancestral village (Bahadur Kallay), Hazar Khwani, Peshawar. The colour of nature and reality predominates in his poetry. It seems that he is a poet of every age and every time. In his verses the history of the past, the account of the present and the message of the future are reflected. Although his divan is brief, it is comprehensive and complete in terms of knowledge and literature. The way Abdur Rahman Baba has represented Pakhtun nature no other poet has done. That is why the popularity he has attained has not fallen to any other poet. His verses are not only mirrors of true love and Sufism but are also books of counsel for success in eternal life. The explanation and elucidation of the Qur’an and ahadith is a speciality of his poetry. His poetic greatness can be judged from the fact that translations of his divan have been made in various languages of the world and people are benefiting from his teachings. The themes of his poetry are based on facts like the greatness of labour, lawful livelihood, Islamic principles, the importance and usefulness of knowledge and the transience of the world.','عبدالرحمن بابا ټول ژوند په خپل پلرني کلي (بهادر کلی) هزار خوانۍ پېښور کې تېر کړ. د هغه په شاعرۍ د فطرت او حقیقت رنګ غالب دی. داسې ښکاري چې هغه د هر دور او هر زمانې شاعر دی. د هغه په شعرونو کې د ماضي تاریخ، د حال یادونه او د راتلونکي پیغام ځلېږي. د هغه دیوان که څه هم لنډ دی خو د علم او ادب له لحاظه جامع او بشپړ دی. د پښتون فطرت ترجمانی چې عبدالرحمن بابا څنګه کړې بل شاعر نه ده کړې. ځکه هغه مقبولیت چې هغه ته ترلاسه دی بل شاعر ته نصیب نه شو. د هغه شعرونه نه یوازې د حقیقي عشق او تصوف آئینه دي بلکې په ابدي ژوند کې د بریالیتوب لپاره پند نامه هم دي. د قرآن او احادیثو تشریح او توضیح د هغه د شاعرۍ ځانګړتیا ده. د هغه د شاعرانه عظمت اندازه له دې خبرې کېدای شي چې د هغه د دیوان ژباړې د نړۍ په بېلابېلو ژبو شوې دي او خلک د هغه له ښوونو ګټه اخلي. د هغه د شاعرۍ موضوعات د زحمت عظمت، حلال روزي، اسلامي اصول، د علم اهمیت او ګټه او د نړۍ بې ثباتي غوندې حقایقو ولاړ دي.')
P(s,'مجموعۂ کلام: دیوانِ عبدالرحمن باباؒ۔','Poetry collection: Diwan-e-Abdur Rahman Baba.','د شعري ټولګه: دیوان عبدالرحمن بابا.')
F.done()
s['sourceNote']='Printed page 156 (scan 163): ornamental title “عبدالرحمن بابا ؒ”, portrait (not reproduced), birth/death boxes (1653 and 1711), biography and the collection name.'+NOTE
s['vocabulary']={}
save(s)
# scan 164 = printed 157
s=page(164,'n13','157','Ikhlas (Abdur Rahman Baba, translated by Taha Khan)','اخلاص (عبدالرحمن بابا / مترجم: طٰہٰ خان)','اخلاص (عبدالرحمن بابا / ژباړن: طه خان)','poem1')
F=Flow(s)
H(s,'اِخلاص','Ikhlas (Sincerity)','اخلاص')
for r in [
('ہم دوشِ ثریّا ہے مقامِ اخلاص','جو ملتا ہے، ملتا ہے غلامِ اخلاص','The station of ikhlas is on a par with the shoulder of the Pleiades;','whatever is gained is gained by the slave of ikhlas.','د اخلاص مقام د ثریا په اوږه برابر دی','چې څه مومي، د اخلاص غلام مومي'),
('گو فرش سے تا عرش سفر ہے دشوار','طے کرتی ہے بہ یک جنبشِ گامِ اخلاص','Though the journey from the floor to the Throne is hard,','the step of ikhlas covers it in a single movement.','که څه هم له فرش نه تر عرش سفر ستونزمن دی','د اخلاص ګام یې په یو حرکت کې وهي'),
('فانی ہے ہر اک چیز، ہر اک رسم و رواج','باقی ہے، مگر ایک دوامِ اخلاص','Everything is perishable, every custom and tradition;','only one thing remains: the perpetuity of ikhlas.','هر شی فاني دی، هر دود او رواج','پاتې دی خو یو دوام اخلاص'),
('اسلام ہے پابندیِ اخلاص کا نام','اور نام ہے اسلام کا نامِ اخلاص','Islam is the name of the observance of ikhlas,','and the name of Islam is the name of ikhlas.','اسلام د اخلاص د پابندۍ نوم دی','او د اسلام نوم د اخلاص نوم دی'),
('صیّاد کو ممکن ہے ہُما ہاتھ لگے','پھیلائے محبّت سے جو دامِ اخلاص','It is possible for the hunter to catch the Huma,','if he spreads the net of ikhlas with love.','ښکارچي ته ممکنه ده هما په لاس ورشي','که په مینه د اخلاص جال وغوړوي')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 157 (scan 164): title “اخلاص” in an ornamental frame, running head “عبدالرحمن بابا / مترجم: طٰہٰ خان”, and five couplets (each two lines as printed, spaced lettering). The poem continues on the next page (the last printed page in this section of the scans).'+NOTE
s['vocabulary']={}
save(s)
