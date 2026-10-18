from ishisthelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,g='q',**m): add(s,f'q{len(s["paras"])+1}',en,ur,ps,listGroup=g,exerciseId='ishist11-bookq',tab='exercise',role='question',**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting, page-edge shadows, a thumb at the page edge and ornamental borders excluded. Scan n = printed page n-1 (file = {p//2+1:03d}_page_2 for even printed page p, {(p-1)//2+1:03d}_page_1 for odd p).'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
SA='صلی اللہ علیہ و علیٰ آلہ واصحابہ وسلم'
RA='رضی اللہ عنہ'
B='........'
# scan 339 = file 170_page_2, printed 338
s=page(339,'ch20','338','Chapter 20: the military system (ranks, battle order, navy)','بیسواں باب: فوجی نظام (عہدے، صف آرائی، بحری فوج)','شلم باب: پوځي نظام (رتبې، صف ترتیب، سمندري پوځ)','ch20p338')
F=Flow(s)
P(s,'فوجی اضلاع قائم کیے گئے۔ کوفہ اور بصرہ کی نئی چھاؤنیاں بنائی گئیں۔ بنو امیہ کی فتوحات کا سہرا بھی ان کی اعلیٰ فوج کے سر ہے۔ انہوں نے بھی یہی طریقہ جاری رکھا البتہ فوج کی تعداد میں دن بدن اضافہ ہوتا تھا۔ واسط اور قیروان کی نئی چھاؤنیاں قائم کی گئیں۔ فوج کے لیے اس دور کے مطابق جدید اسلحہ فراہم کیا جاتا تھا۔ پیادہ فوج کے علاوہ سوار فوج اور توپ خانہ بھی ہوتا تھا جن کا کام قلعہ اور شہر کی دیواریں توڑنا ہوتا تھا۔ فوج میں عام طور پر یہ عہدے تھے۔','Military districts were established. New cantonments of Kufah and Basrah were built. The credit for the conquests of Banu Umayyah also goes to their excellent army. They too continued the same method, but the number of the army went on increasing day by day. New cantonments of Wasit and Qayrawan were established. Modern weapons suited to that period were provided for the army. Besides the infantry there were also cavalry and artillery, whose work was to break the walls of forts and cities. In the army generally these ranks existed.','پوځي سیمې جوړې شوې. د کوفې او بصرې نوې چاونۍ جوړې شوې. د بنو امیه د فتوحاتو سهرا هم د هغوی پر لوړ پوځ ده. هغوی هم همدا طریقه روانه وساتله خو د پوځ شمېر ورځ تر بلې زیاتېده. د واسط او قیروان نوې چاونۍ جوړې شوې. د پوځ لپاره د دې دورې سره سم عصري وسلې برابرېدې. د پیاده پوځ سربېره سپور پوځ او توپخانه هم وه چې کار یې د کلاګانو او ښار د دېوالونو ماتول و. په پوځ کې عموماً دا رتبې وې.')
H(s,'۱۔ امیر العشر (عارف):','1. Amir al-Ashr (the arif):','۱. امیر العشر (عارف):')
P(s,'اس کے ماتحت دس سپاہی ہوتے تھے۔','Ten soldiers were under him.','د هغه تر واک لاندې لس سرتېري وو.')
H(s,'۲۔ نائب:','2. The na\'ib (deputy):','۲. نایب:')
P(s,'اس کے ماتحت سو سپاہی اور دس عارف ہوتے تھے۔','Under him were a hundred soldiers and ten arifs.','د هغه تر واک لاندې سل سرتېري او لس عارفان وو.')
H(s,'۳۔ قائد:','3. The qa\'id (commander):','۳. قائد:')
P(s,'اس کے زیر نگرانی دس نائب اور ہزار سپاہی ہوتے تھے۔ اس سے اوپر امیر اور سپہ سالار ہوتا تھا۔ فوج کی ترتیب چار بڑے حصوں میں کی جاتی تھی۔ یہ ترتیب میدان جنگ میں صف آرائی کے مطابق مندرجہ ذیل طریقہ سے کی جاتی تھی۔','Under his supervision were ten deputies and a thousand soldiers. Above him were the amir and the commander-in-chief. The army was arranged in four big parts. This arrangement was made, in accordance with the battle array on the battlefield, in the following way.','د هغه تر څارنې لاندې لس نایبان او زرګونه سرتېري وو. له هغه پورته امیر او سپه سالار و. پوځ په څلورو لویو برخو ترتیبېده. دا ترتیب په جګړه ډګر کې د صف ترتیب سره سم په لاندې ډول کېده.')
H(s,'۱۔ ہراول دستہ:','1. The vanguard:','۱. مخکښ دله:')
P(s,'یہ دستہ سب سے آگے ہوتا تھا۔','This detachment was at the very front.','دا دله تر ټولو مخکې وه.')
H(s,'۲۔ میمنہ:','2. The maymanah (right wing):','۲. میمنه (ښي اړخ):')
P(s,'دائیں طرف کا حصہ ہوتا تھا اس کا سربراہ امیر ہوتا تھا۔','It was the part on the right side; its head was an amir.','د ښي لوري برخه وه، مشر یې امیر و.')
H(s,'۳۔ میسرہ:','3. The maysarah (left wing):','۳. میسره (کیڼ اړخ):')
P(s,'بائیں طرف کا فوجی دستہ ہوتا تھا۔ اس کا سربراہ بھی امیر ہوتا تھا۔','It was the military detachment on the left side. Its head too was an amir.','د کیڼ لوري پوځي دله وه. مشر یې هم امیر و.')
H(s,'۴۔ قلب:','4. The qalb (centre):','۴. قلب (مرکز):')
P(s,'یہ تمام صف آراء فوج کا مرکزی حصہ ہوتا تھا۔ اس کا سربراہ سپہ سالار بذات خود ہوتا تھا۔','This was the central part of the whole army in battle array. Its head was the commander-in-chief himself.','دا د ټول صف ترتیب شوي پوځ مرکزي برخه وه. مشر یې سپه سالار پخپله و.')
H(s,'بحری فوج:','The navy:','سمندري پوځ:')
P(s,f'حضرت عمر {RA} نے بحری فوج قائم کرنے کی ممانعت کر دی تھی۔ حضرت','Hazrat Umar (may Allah be pleased with him) had forbidden the establishment of a navy. Hazrat','حضرت عمر رضي الله عنه د سمندري پوځ جوړولو منع کړې وه. حضرت',cont=True)
F.done()
fin(s,'Printed page 338: the military system (continuing from page 337 — the top of the page begins “military districts were established”; the join with the last words of page 337 is not clear in the scan) with ranks 1–3, the four parts of the army 1–4 and the beginning of the section on the navy (continues on the next page).')
# scan 340 = file 170_page_1, printed 339
s=page(340,'back-matter','339','Chapter 20: the navy (end); important questions (1–8)','بیسواں باب: بحری فوج (اختتام)؛ اہم سوالات (۱ تا ۸)','شلم باب: د سمندري پوځ پای؛ مهم پوښتنې (۱ تر ۸)','bmp339')
F=Flow(s)
P(s,f'عثمان {RA} کے دور میں بحری فوج کا آغاز ہوا۔ حضرت امیر معاویہ {RA} نے اسے کافی ترقی دی کیونکہ رومیوں کے مقابلے کے لیے بحری فوج کا ہونا بہت ضروری تھا۔ بنو امیہ کے دور میں بحری فتوحات میں مزید اضافہ ہوا۔ ساحلوں پر بحری جہاز بنانے کی فیکٹریاں قائم کی گئیں۔ بحری بیڑے کو مزید طاقتور بنایا گیا، اس سے فتوحات کا سلسلہ سپین تک پھیل گیا۔','Uthman (may Allah be pleased with him), the navy began. Hazrat Amir Mu\'awiyah (may Allah be pleased with him) developed it considerably, because to face the Romans it was very necessary to have a navy. In the period of Banu Umayyah naval conquests increased further. Factories for building ships were established on the coasts. The fleet was made still more powerful, and by this the series of conquests spread as far as Spain.','عثمان رضي الله عنه په دوره کې سمندري پوځ پیل شو. حضرت امیر معاویه رضي الله عنه ورته ښه پرمختګ ورکړ ځکه چې د رومیانو په مقابل کې د سمندري پوځ شتون ډېر ضروري و. د بنو امیه په دوره کې سمندري فتحې نورې هم زیاتې شوې. په ساحلونو د بېړیو جوړولو فابریکې جوړې شوې. بحري بیړۍ نوره هم پیاوړې شوه، له دې د فتوحاتو لړۍ تر اسپانیا ورسېده.')
H(s,'اہم سوالات','Important questions','مهم پوښتنې')
for u,e,p in [
 (f'۱۔ حضرت محمد رسول اللہ خاتم النبیین {SA} سے قبل عرب کے معاشرتی، سیاسی، اقتصادی اور مذہبی حالت پر تبصرہ کریں۔','1. Comment on the social, political, economic and religious condition of the Arabs before Hazrat Muhammad, the Messenger of Allah, the Seal of the Prophets (peace be upon him).','۱. له حضرت محمد رسول الله خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم مخکې د عربو د ټولنیزې، سیاسي، اقتصادي او دیني حالت باندې تبصره وکړئ.'),
 (f'۲۔ آنحضرت {SA} کی مکی زندگی کے چیدہ چیدہ واقعات بیان کریں۔','2. Describe the main events of the Makkan life of the Holy Prophet (peace be upon him).','۲. د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د مکې د ژوند مهمې پېښې بیان کړئ.'),
 ('۳۔ جنگ بدر کے اسباب، واقعات اور نتائج بیان کریں۔ نیز مسلمانوں کی فتح کے اسباب بھی لکھیں۔','3. Describe the causes, events and results of the Battle of Badr. Also write the causes of the victory of the Muslims.','۳. د بدر د جګړې لاملونه، پېښې او پایلې بیان کړئ. همداراز د مسلمانانو د فتحې لاملونه هم ولیکئ.'),
 ('۴۔ میثاق مدینہ کی شرائط اور اہمیت تحریر کریں۔','4. Write the terms and the importance of the Charter of Madinah.','۴. د میثاق مدینې شرطونه او اهمیت ولیکئ.'),
 ('۵۔ صلح حدیبیہ کے متعلق آپ کیا جانتے ہیں؟ اس کی سیاسی اہمیت بیان کریں۔','5. What do you know about the Treaty of Hudaybiyah? Describe its political importance.','۵. د صلح حدیبیه په اړه تاسو څه پوهېږئ؟ د هغې سیاسي اهمیت بیان کړئ.'),
 ('۶۔ فتح مکہ کے اسباب، واقعات اور نتائج لکھیں۔','6. Write the causes, events and results of the conquest of Makkah.','۶. د مکې د فتحې لاملونه، پېښې او پایلې ولیکئ.'),
 ('۷۔ خطبۃ الوداع پر مفصل نوٹ لکھیں۔ اس خطبے کی تاریخی اہمیت پر روشنی ڈالیں۔','7. Write a detailed note on the Farewell Sermon. Throw light on the historical importance of this sermon.','۷. په خطبة الوداع باندې مفصل یادښت ولیکئ. د دې خطبې په تاریخي اهمیت رڼا واچوئ.'),
 (f'۸۔ حضرت ابو بکر صدیق {RA} کی ابتدائی مشکلات لکھیں۔ (فتنہ ارتداد) آپ نے ان مشکلات پر کیسے قابو پایا؟','8. Write the early difficulties of Hazrat Abu Bakr Siddiq (may Allah be pleased with him) (the apostasy trouble). How did he overcome these difficulties?','۸. د حضرت ابوبکر صدیق رضي الله عنه لومړنۍ ستونزې (د ارتداد فتنه) ولیکئ. هغه پر دغو ستونزو څنګه بریالی شو؟')]:
    Q(s,u,e,p,g='q')
F.done()
fin(s,'Printed page 339: the end of the section on the navy (continuing from page 338; the first word “Hazrat” of the sentence is on page 338) and the first eight of the “Important questions” at the end of the book. The number of question 8 is covered by a handwritten tick and is taken from the sequence. A thumb at the lower left is excluded.')
# scan 341 = file 171_page_2, printed 340 (cropped at the top)
s=page(341,'back-matter','340','Important questions (10–20; the top of the page is cropped)','اہم سوالات (۱۰ تا ۲۰؛ صفحے کا اوپر کا حصہ کٹا ہوا ہے)','مهم پوښتنې (۱۰ تر ۲۰؛ د مخ پورتنۍ برخه پرې شوې ده)','bmp340')
F=Flow(s)
for u,e,p in [
 (f'۱۰۔ … (اوپر کی سطر اسکین میں کٹی ہوئی ہے) … عثمان غنی {RA} پر لگائے گئے الزامات کا بھی تجزیہ کریں۔','10. … (the upper line is cut off in the scan) … Also analyse the allegations made against Uthman Ghani (may Allah be pleased with him).','۱۰. … (پورتنی کرښه په سکین کې پرې شوې ده) … همداراز د عثمان غني رضي الله عنه پر ضد لګول شوي تورونه تحلیل کړئ.'),
 (f'۱۱۔ حضرت علی {RA} کے دور خلافت میں خانہ جنگی کا حال تفصیلاً لکھیں۔','11. Write in detail the account of the civil war in the period of the caliphate of Hazrat Ali (may Allah be pleased with him).','۱۱. د حضرت علي رضي الله عنه د خلافت په دوره کې د کورنۍ جګړې حال په تفصیل سره ولیکئ.'),
 ('۱۲۔ خلفائے راشدین رضوان اللہ علیہم کے انتظام سلطنت پر روشنی ڈالیے۔','12. Throw light on the administration of the empire of the Rightly Guided Caliphs (may Allah be pleased with them).','۱۲. د خلفاء راشدینو رضوان الله علیهم د سلطنت په نظم رڼا واچوئ.'),
 (f'۱۳۔ حضرت امیر معاویہ {RA} کی سیرت اور کارنامے بیان کریں۔','13. Describe the biography and the achievements of Hazrat Amir Mu\'awiyah (may Allah be pleased with him).','۱۳. د حضرت امیر معاویه رضي الله عنه سیرت او کارنامې بیان کړئ.'),
 ('۱۴۔ سانحہ کربلا پر تفصیلی نوٹ لکھیں۔','14. Write a detailed note on the tragedy of Karbala.','۱۴. د کربلا په پېښه تفصیلي یادښت ولیکئ.'),
 (f'۱۵۔ حضرت عبد اللہ بن زبیر {RA} کے دور حکومت کے مشہور واقعات تحریر کریں۔ نیز ان کی سیاسی غلطیوں پر بھی تبصرہ کریں۔','15. Write the famous events of the period of rule of Hazrat Abdullah bin Zubayr (may Allah be pleased with him). Also comment on his political mistakes.','۱۵. د حضرت عبدالله بن زبیر رضي الله عنه د حکومت مشهورې پېښې ولیکئ. همداراز د هغه پر سیاسي غلطیو تبصره وکړئ.'),
 ('۱۶۔ عبد الملک کی انتظامی اصلاحات تحریر کریں۔','16. Write the administrative reforms of Abd al-Malik.','۱۶. د عبدالملک اداري اصلاحات ولیکئ.'),
 ('۱۷۔ ولید بن عبد الملک کے دور کو سنہرا دور کیوں کہا جاتا ہے؟ ان کے دور کی فتوحات بیان کریں۔','17. Why is the period of Walid bin Abd al-Malik called the golden period? Describe the conquests of his period.','۱۷. د ولید بن عبدالملک دوره ولې زرینه دوره بلل کېږي؟ د هغه د دورې فتوحات بیان کړئ.'),
 ('۱۸۔ حضرت عمر بن عبد العزیز رحمۃ اللہ علیہ کو پانچواں خلیفہ راشد کیوں کہا جاتا ہے؟ ان کی اصلاحات لکھیں۔','18. Why is Hazrat Umar bin Abd al-Aziz (may Allah have mercy on him) called the fifth Rightly Guided Caliph? Write his reforms. (The honorific after the name is a small glyph in the scan.)','۱۸. حضرت عمر بن عبدالعزیز رحمة الله علیه ولې پنځم خلیفه راشد بلل کېږي؟ د هغه اصلاحات ولیکئ.'),
 ('۱۹۔ ہشام بن عبد الملک کی سیرت اور کارنامے سپرد قلم کیجیے۔','19. Put down in writing the biography and the achievements of Hisham bin Abd al-Malik.','۱۹. د هشام بن عبدالملک سیرت او کارنامې ولیکئ.'),
 ('۲۰۔ اموی دور کے مرکزی نظام حکومت پر مفصل نوٹ تحریر کریں۔','20. Write a detailed note on the central system of government of the Umayyad period.','۲۰. د اموي دورې د حکومت په مرکزي نظام باندې مفصل یادښت ولیکئ.')]:
    Q(s,u,e,p,g='q')
F.done()
fin(s,'Printed page 340: questions 10–20 of the “Important questions” at the end of the book. The top of the scan is cropped (question 9 and the first line of question 10 are not visible) and the left edge has a ruled margin of handwriting, which is excluded. The honorific after Umar bin Abd al-Aziz is a very small glyph and is read here as “rahimahu Allah”.')
# scan 342 = file 171_page_1, printed 341 (cropped at the top)
s=page(342,'back-matter','341','Important questions (end of question 22) and question 23: fill in the blanks (i)–(xii); the top of the page is cropped','اہم سوالات (سوال ۲۲ کا اختتام) اور سوال ۲۳: خالی جگہیں پُر کریں (i) تا (xii)؛ صفحے کا اوپر کا حصہ کٹا ہوا ہے','مهم پوښتنې (د ۲۲ پوښتنې پای) او ۲۳ پوښتنه: تشې ځایونه ډک کړئ (i) تر (xii)','bmp341')
F=Flow(s)
Q(s,'… مختار ثقفی، ابو مسلم خراسانی، عباسی تحریک۔','… Mukhtar Thaqafi, Abu Muslim Khurasani, the Abbasid movement. (The beginning of this question is cut off in the scan.)','… مختار ثقفي، ابومسلم خراساني، عباسي خوځښت.')
Q(s,'۲۳۔ مندرجہ ذیل خالی جگہوں کو پُر کیجیے۔','23. Fill in the following blanks.','۲۳. لاندې تشې ځایونه ډک کړئ.')
for u,e,p in [
 (f'(i) خلفائے راشدین کے دور میں خلیفہ کی حیثیت {B} کی ہوتی تھی۔',f'(i) In the period of the Rightly Guided Caliphs the position of the caliph was that of a {B}.',f'(i) د خلفاء راشدینو په دوره کې د خلیفه حیثیت د {B} و.'),
 (f'(ii) بنو امیہ کے حکمرانوں نے خلافت کو {B} میں بدل دیا۔',f'(ii) The rulers of Banu Umayyah changed the caliphate into {B}.',f'(ii) د بنو امیه حاکمانو خلافت په {B} بدل کړ.'),
 (f'(iii) بنو امیہ کے حکمرانوں نے بیت المال کو اپنے ذاتی {B} میں بدل دیا۔',f'(iii) The rulers of Banu Umayyah changed the public treasury into their personal {B}.',f'(iii) د بنو امیه حاکمانو بیت المال په خپل شخصي {B} بدل کړ.'),
 (f'(iv) بنو امیہ کے دور میں باقاعدہ وزارت کا عہدہ {B} تھا۔',f'(iv) In the period of Banu Umayyah the regular office of ministry was {B}.',f'(iv) د بنو امیه په دوره کې د وزارت منظمه عهده {B} وه.'),
 (f'(v) بنو امیہ کا بڑا وزیر {B} کہلاتا تھا۔',f'(v) The chief minister of Banu Umayyah was called {B}.',f'(v) د بنو امیه لوی وزیر {B} بلل کېده.'),
 (f'(vi) عبد الملک نے تمام زبانوں کی جگہ {B} کو سرکاری زبان کی حیثیت دی۔',f'(vi) Abd al-Malik, in place of all languages, gave {B} the position of the official language.',f'(vi) عبدالملک د ټولو ژبو پر ځای {B} ته د رسمي ژبې حیثیت ورکړ.'),
 (f'(vii) غیر مسلموں کے فیصلے ان کی {B} اور {B} کے مطابق ہوتے تھے۔',f'(vii) The decisions of the non-Muslims were according to their {B} and {B}.',f'(vii) د غیر مسلمانانو پرېکړې د هغوی د {B} او {B} سره سم کېدې.'),
 (f'(viii) بنو امیہ میں انتظام سلطنت چلانے کے لیے {B} تھے۔',f'(viii) In Banu Umayyah, to run the administration of the empire there were {B}.',f'(viii) په بنو امیه کې د سلطنت د نظم چلولو لپاره {B} وو.'),
 (f'(ix) دیوان الجند {B} کا انتظام کرتا تھا۔',f'(ix) Diwan al-Jund managed {B}.',f'(ix) دیوان الجند د {B} نظم کاوه.'),
 (f'(x) دیوان الخراج کے ذمے {B} تھے۔',f'(x) The responsibility of Diwan al-Kharaj was {B}.',f'(x) د دیوان الخراج په غاړه {B} وو.'),
 (f'(xi) مالیاتی سربراہ {B} کہلاتا تھا۔',f'(xi) The head of finance was called {B}.',f'(xi) مالي مشر {B} بلل کېده.'),
 (f'(xii) پولیس کا سربراہ {B} کہلاتا تھا۔',f'(xii) The head of the police was called {B}.',f'(xii) د پولیسو مشر {B} بلل کېده.')]:
    Q(s,u,e,p,g='q23')
F.done()
fin(s,'Printed page 341: the end of the list of the final “Important questions” (the top of the scan is cropped, so only the last words of question 22 are visible) and question 23, blanks (i)–(xii). Handwritten answers in the blanks, pencil marks and the ruled margin are excluded; the blanks are left empty. Question 21 and the start of question 22 are not visible in any scan.')
