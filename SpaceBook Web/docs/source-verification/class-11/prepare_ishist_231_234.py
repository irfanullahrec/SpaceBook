from ishisthelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,g='q',**m): add(s,f'q{len(s["paras"])+1}',en,ur,ps,listGroup=g,exerciseId='ishist11-ch13-q',tab='exercise',role='question',**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting, page-edge shadows, a thumb at the page edge and ornamental borders excluded. Scan n = printed page n-1 (file = {p//2+1:03d}_page_2 for even printed page p, {(p-1)//2+1:03d}_page_1 for odd p).'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
SA='صلی اللہ علیہ و علیٰ آلہ واصحابہ وسلم'
SP='صلی الله علیه وعلی آله واصحابه وسلم'
RA='رضی اللہ عنہ'
KH='رضی اللہ عنہا'
TF='(درست / غلط)'
TFE='(true / false)'
TFP='(سم / ناسم)'
# scan 231 = file 116_page_2, printed 230
s=page(231,'ch13','230','Chapter 13 exercise questions (start)','مشقی سوالات (آغاز) — تیرہواں باب','تمرین پوښتنې (پیل) — دیارلسم باب','ch13p230')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
Q(s,f'۱۔ حضرت امام حسین {RA} کی شہادت کے اسباب کیا تھے؟ سانحہ کربلا کے نتائج بیان کیجیے۔','1. What were the causes of the martyrdom of Hazrat Imam Husayn? Describe the results of the tragedy of Karbala.','۱. د حضرت امام حسین رضی الله عنه د شهادت لاملونه څه وو؟ د کربلا د حادثې پایلې بیان کړئ.')
Q(s,'۲۔ سانحہ کربلا پر تفصیلی نوٹ لکھیں۔','2. Write a detailed note on the tragedy of Karbala.','۲. د کربلا په حادثه مفصل یادښت ولیکئ.')
Q(s,'۳۔ واقعہ کربلا کے تاریخِ اسلام پر اثرات بیان کیجیے۔','3. Describe the effects of the incident of Karbala on the history of Islam.','۳. د اسلام په تاریخ د کربلا د پېښې اغېز بیان کړئ.')
Q(s,'۴۔ خالی جگہیں پُر کریں۔','4. Fill in the blanks.','۴. تشې ځایونه ډک کړئ.')
for u,e,p in [
 ('(i) یزید ........ کا بہت شوقین تھا۔','(i) Yazid was very fond of ........','(i) یزید د ........ ډېر شوقین و.'),
 (f'(ii) یزید نے حاکمِ مدینہ ........ کو حضرت امام حسین {RA} سے بیعت لینے کے لیے لکھا۔','(ii) Yazid wrote to the governor of Madinah, ........, to take the pledge from Hazrat Imam Husayn.','(ii) یزید د مدینې حاکم ........ ته ولیکل چې له حضرت امام حسین رضی الله عنه بیعت واخلي.'),
 ('(iii) مسلم بن عقیل نے اپنے ........ ساتھیوں کے ساتھ ابنِ زیاد کا محاصرہ کر لیا۔','(iii) Muslim bin Aqil, with his ........ companions, besieged Ibn Ziyad.','(iii) مسلم بن عقیل خپلو ........ ملګرو سره د ابن زیاد محاصره وکړه.'),
 ('(iv) ابنِ زیاد نے مسلم اور ........ کو قتل کرنے کا حکم دیا۔','(iv) Ibn Ziyad ordered the killing of Muslim and ........','(iv) ابن زیاد د مسلم او ........ د وژلو حکم وکړ.'),
 (f'(v) شیعانِ علی {RA} کوفہ میں اپنے سردار ........ کے گھر جمع ہو گئے۔','(v) The Shi’an-i-Ali gathered in Kufah at the house of their chief ........','(v) شیعان علي رضی الله عنه په کوفه کې د خپل مشر ........ په کور کې راټول شول.')]:
    Q(s,u,e,p,g='q4')
Q(s,'۵۔ درست/غلط میں جواب دیجیے۔','5. Answer in true/false.','۵. په سم / ناسم ځواب ورکړئ.')
Q(s,f'(i) یزید نے 60 ہجری تا 64 ہجری حکومت کی۔ {TF}',f'(i) Yazid ruled from 60 AH to 64 AH. {TFE}',f'(i) یزید له ۶۰ هجري تر ۶۴ هجري حکومت وکړ. {TFP}',g='q5')
Q(s,f'(ii) یزید حضرت امیر معاویہ {RA} کا بیٹا تھا۔ {TF}',f'(ii) Yazid was the son of Hazrat Amir Mu’awiyah. {TFE}',f'(ii) یزید د حضرت امیر معاویه رضی الله عنه زوی و. {TFP}',g='q5')
F.done()
fin(s,'Printed page 230: the exercise of Chapter 13 (questions 1–3, blanks (i)–(v) of question 4 and the first two true/false items of question 5; the list continues on the next page). The handwritten marks and pencil scribbles at the right edge are excluded; the blanks are left empty. The thumb is excluded.')
# scan 232 = file 116_page_1, printed 231
s=page(232,'ch13','231','Chapter 13 exercise: true/false (iii)–(xvii)','مشقی سوالات: درست/غلط (iii) تا (xvii)','تمرین پوښتنې: سم / ناسم (iii) تر (xvii)','ch13p231')
F=Flow(s)
for u,e,p in [
 ('(iii) یزید کو شکار اور شعر گوئی کا شوق تھا۔','(iii) Yazid was fond of hunting and of composing poetry.','(iii) یزید ښکار او شعر ویلو ته شوق درلود.'),
 ('(iv) یزید نے تین سال حکومت کی۔','(iv) Yazid ruled for three years.','(iv) یزید درې کاله حکومت وکړ.'),
 (f'(v) حضرت امام حسین {RA} نے بیعت سے انکار کیا۔',f'(v) Hazrat Imam Husayn refused to pledge allegiance.','(v) حضرت امام حسین رضی الله عنه له بیعت انکار وکړ.'),
 (f'(vi) عبد اللہ بن عمر {RA} نے آخر تک بیعت نہیں کی۔','(vi) Abdullah bin Umar did not pledge allegiance till the end.','(vi) عبدالله بن عمر رضی الله عنه تر پایه بیعت ونه کړ.'),
 ('(vii) مدینہ کا حاکم ولید بن عقبہ تھا۔','(vii) The governor of Madinah was Walid bin Uqbah.','(vii) د مدینې حاکم ولید بن عقبه و.'),
 ('(viii) ولید نے مروان سے مشورہ کیا۔','(viii) Walid consulted Marwan.','(viii) ولید له مروان سره مشوره وکړه.'),
 (f'(ix) حضرت امام حسین {RA} مکہ چلے گئے۔','(ix) Hazrat Imam Husayn went to Makkah.','(ix) حضرت امام حسین رضی الله عنه مکې ته ولاړ.'),
 (f'(x) حضرت امام حسین {RA} نے مسلم بن عقیل کو بغداد روانہ کیا۔','(x) Hazrat Imam Husayn sent Muslim bin Aqil to Baghdad.','(x) حضرت امام حسین رضی الله عنه مسلم بن عقیل بغداد ته ولېږه.'),
 ('(xi) کوفہ کا حاکم نعمان بن بشیر تھا۔','(xi) The ruler of Kufah was Nu’man bin Bashir.','(xi) د کوفې حاکم نعمان بن بشیر و.'),
 ('(xii) ابنِ زیاد کے پاس صرف 10 آدمی تھے۔','(xii) Ibn Ziyad had only 10 men.','(xii) د ابن زیاد سره یوازې ۱۰ کسان وو.'),
 ('(xiii) حر 6 ہزار کا لشکر لے کر آیا۔','(xiii) Hurr came with an army of 6 thousand.','(xiii) حر د ۶ زره لښکر سره راغی.'),
 ('(xiv) عمر بن سعد 60 ہزار کا لشکر لے کر آیا۔','(xiv) Umar bin Sa’d came with an army of 60 thousand.','(xiv) عمر بن سعد د ۶۰ زره لښکر سره راغی.'),
 (f'(xv) حضرت امام حسین {RA} نے تین شرائط پیش کیں۔','(xv) Hazrat Imam Husayn presented three conditions.','(xv) حضرت امام حسین رضی الله عنه درې شرطونه وړاندې کړل.'),
 ('(xvi) ابنِ زیاد نے شمر کو ایک دستہ دے کر روانہ کیا۔','(xvi) Ibn Ziyad sent Shimr with a detachment.','(xvi) ابن زیاد شمر د یوې دستې سره ولېږه.'),
 (f'(xvii) حضرت امام حسین {RA} نے ایک رات کی مہلت مانگی۔','(xvii) Hazrat Imam Husayn asked for a night’s respite.','(xvii) حضرت امام حسین رضی الله عنه د یوې شپې مهلت وغوښت.')]:
    Q(s,f'{u} {TF}',f'{e} {TFE}',f'{p} {TFP}',g='q5')
F.done()
fin(s,'Printed page 231: true/false items (iii)–(xvii) of question 5 of the exercise of Chapter 13 (the print shows “(درست/غلط)” after each item; the item numbers are in the print in Latin numerals). The handwritten answers are excluded. The statements are given as printed, including the false ones (for example (x) “Baghdad”, (xii) “10 men”, (xiii) “6 thousand” and (xiv) “60 thousand”), because the textbook asks the student to judge them.')
# scan 233 = file 117_page_2, printed 232
s=page(233,'ch13','232','Chapter 13 exercise (end): true/false (xviii)–(xx)','مشقی سوالات (اختتام): درست/غلط (xviii) تا (xx)','تمرین پوښتنې (پای): سم / ناسم (xviii) تر (xx)','ch13p232')
F=Flow(s)
for u,e,p in [
 (f'(xviii) حضرت امام حسین {RA} نے اپنے 72 جانبازوں کو میدانِ جنگ میں صف آرا کیا۔','(xviii) Hazrat Imam Husayn arrayed his 72 brave men on the battlefield.','(xviii) حضرت امام حسین رضی الله عنه خپل ۷۲ ننګیالي د جګړې په میدان کې صف آرا کړل.'),
 ('(xix) کربلا میں صرف زین العابدین زندہ بچے۔','(xix) In Karbala only Zayn al-Abidin survived.','(xix) په کربلا کې یوازې زین العابدین ژوندی پاتې شو.'),
 (f'(xx) عرب میں حضرت عبد اللہ بن زبیر {RA} نے حکومت قائم کر لی۔','(xx) In Arabia Hazrat Abdullah bin Zubayr established a government.','(xx) په عربو کې حضرت عبدالله بن زبیر رضی الله عنه حکومت جوړ کړ.')]:
    Q(s,f'{u} {TF}',f'{e} {TFE}',f'{p} {TFP}',g='q5')
F.done()
fin(s,'Printed page 232: true/false items (xviii)–(xx) of question 5 of the exercise of Chapter 13, followed by a row of three stars; the rest of the page is blank (faint show-through of the other side). A thumb at the lower left and pencil scribbles at the right edge are excluded.')
# scan 234 = file 117_page_1, printed 233
s=page(234,'ch14','233','Chapter 14: Hazrat Abdullah bin Zubayr (64–73 AH / 683–692 CE) — introduction','چودھواں باب: حضرت عبد اللہ بن زبیر (64ھ تا 73ھ بمطابق 683ء تا 692ء) — تعارف','څوارلسم باب: حضرت عبدالله بن زبیر (۶۴ تر ۷۳ هـ د ۶۸۳ تر ۶۹۲ ز) — پېژندنه','ch14p233')
F=Flow(s)
H(s,'چودھواں باب','Chapter 14','څوارلسم باب')
H(s,f'حضرت عبد اللہ بن زبیر {RA}','Hazrat Abdullah bin Zubayr','حضرت عبدالله بن زبیر رضی الله عنه')
H(s,'(64ھ تا 73ھ بمطابق 683ء تا 692ء)','(64 AH to 73 AH, corresponding to 683 CE to 692 CE)','(۶۴ تر ۷۳ هجري د ۶۸۳ تر ۶۹۲ زېږدیز سره سم)')
P(s,f'تعارف: حضرت عبد اللہ بن زبیر {RA} حضرت زبیر بن عوام {RA} کے صاحبزادے تھے۔ حضرت عائشہ صدیقہ {KH} آپ {RA} کی خالہ تھیں۔ آپ {RA} نیک، متقی اور پرہیز گار تھے۔ حضرت امیر معاویہ {RA} کے دورِ حکومت میں آپ {RA} نے کئی معرکوں میں حصہ لیا۔ قسطنطنیہ کے حملے میں آپ {RA} پیش پیش رہے۔ حضرت امیر معاویہ {RA} نے جب یزید کے لیے بیعت کا سلسلہ شروع کیا تو آپ {RA} حاکمِ مدینہ سے اجازت لے کر مکہ چلے گئے۔ واقعہ کربلا کے بعد آپ {RA} نے خلافت کا اعلان کیا۔ جب یزید کو عبد اللہ بن زبیر {RA} کے اعلان کا پتہ چلا تو اس نے مسلم بن عقبہ کو دس ہزار کا لشکر دے کر روانہ کیا۔ تین دن تک مدینہ میں خونریز جنگ ہوئی۔ فضل بن عباس، عبد اللہ بن حنظلہ {RA}، عبد اللہ بن مطیع اور دوسرے کئی سردار مارے گئے، شامی فوجیں تین دن تک حضور {SA} کی بستی کو لوٹتی رہیں۔ اس کے بعد مسلم بن عقبہ مکہ روانہ ہوا لیکن راستے میں فوت ہو گیا۔ مدینہ تباہ ہو گیا، حصین نے خانہ کعبہ کا محاصرہ ختم کر کے عبد اللہ بن زبیر {RA} کے ساتھ مذاکرات شروع کیے۔ عبد اللہ بن زبیر {RA} کو دمشق جانے کی دعوت دی، عبد اللہ بن زبیر {RA} نے جانے سے صاف انکار کر دیا جبکہ مروان، اس کے','Introduction: Hazrat Abdullah bin Zubayr was the son of Hazrat Zubayr bin al-Awwam. Hazrat Aisha Siddiqah was his maternal aunt. He was good, God-fearing and pious. In the period of rule of Hazrat Amir Mu’awiyah he took part in several battles. In the attack on Constantinople he was at the front. When Hazrat Amir Mu’awiyah began the series of pledges for Yazid, he took permission from the governor of Madinah and went to Makkah. After the incident of Karbala he announced the caliphate. When Yazid learnt of the announcement of Abdullah bin Zubayr he sent Muslim bin Uqbah with an army of ten thousand. For three days a bloody battle took place in Madinah. Fadl bin Abbas, Abdullah bin Hanzalah, Abdullah bin Muti’ and several other chiefs were killed; the Syrian armies went on plundering the settlement of the Holy Prophet for three days. After this Muslim bin Uqbah set out for Makkah but died on the way. Madinah was ruined. Husayn ended the siege of the Ka’bah and began talks with Abdullah bin Zubayr. He invited Abdullah bin Zubayr to go to Damascus; Abdullah bin Zubayr refused plainly to go, while Marwan, his',f'پېژندنه: حضرت عبدالله بن زبیر رضی الله عنه د حضرت زبیر بن عوام رضی الله عنه زوی و. حضرت عائشه صدیقه رضی الله عنها د هغه خاله وه. هغه نېک، متقي او پرهېزګار و. د حضرت امیر معاویه رضی الله عنه په دوره کې هغه په ډېرو معرکو کې برخه واخیسته. د قسطنطنیې په برید کې هغه مخکې و. کله چې حضرت امیر معاویه رضی الله عنه د یزید لپاره د بیعت لړۍ پیل کړه نو هغه د مدینې له حاکم نه اجازه اخیستلو سره مکې ته ولاړ. د کربلا له پېښې وروسته هغه خلافت اعلان کړ. کله چې یزید ته د عبدالله بن زبیر رضی الله عنه د اعلان خبر ورسېد نو هغه مسلم بن عقبه د لسو زرو لښکر سره ولېږه. درې ورځې په مدینه کې وینې توکونکې جګړه وشوه. فضل بن عباس، عبدالله بن حنظله رضی الله عنه، عبدالله بن مطیع او ډېر نور مشران ووژل شول، شامي لښکرو درې ورځې د حضرت {SP} کلی لوټ کړ. له دې وروسته مسلم بن عقبه مکې ته روان شو خو په لار کې وفات شو. مدینه تباه شوه، حصین د خانه کعبې محاصره ختمه کړه او له عبدالله بن زبیر رضی الله عنه سره یې خبرې اترې پیل کړې. عبدالله بن زبیر رضی الله عنه یې دمشق ته د تللو بلنه ورکړه، عبدالله بن زبیر رضی الله عنه د تللو څرګند انکار وکړ حال دا چې مروان، د هغه',cont=True)
F.done()
fin(s,'Printed page 233: the title page of Chapter 14 (“چودھواں باب — حضرت عبد اللہ بن زبیر رضی اللہ عنہ (64ھ تا 73ھ بمطابق 683ء تا 692ء)”), the introduction of Abdullah bin Zubayr (the sentence continues on the next page). The handwritten circled numerals near the heading are excluded; the dates are read from the print. A thumb at the lower edge is excluded.')
