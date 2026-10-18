from ishisthelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting, page-edge shadows, a thumb at the page edge and ornamental borders excluded. Scan n = printed page n-1 (file = {p//2+1:03d}_page_2 for even printed page p, {(p-1)//2+1:03d}_page_1 for odd p).'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
SA='صلی اللہ علیہ و آلہ وسلم'
# scan 343 = file 172_page_2, printed 342 (page number not shown)
s=page(343,'back-matter','342','Back matter: two framed sayings (bribery; unlawful wealth)','آخری صفحات: دو فریم شدہ اقوال (رشوت؛ حرام مال)','وروستي مخونه: دوه چوکاټ لرونکي قولونه (رشوت؛ حرام مال)','bmp342')
F=Flow(s)
P(s,'’’رشوت دینے اور لینے والے پر اللہ تعالیٰ کی لعنت ہے۔‘‘ (ابن ماجہ)','“Allah the Exalted curses the one who gives a bribe and the one who takes it.” (Ibn Majah)','«په رشوت ورکوونکي او رشوت اخیستونکي د الله تعالیٰ لعنت دی.» (ابن ماجه)')
P(s,'حرام مال سے اللہ تعالیٰ صدقہ قبول نہیں کرتا۔ (احمد)','Allah the Exalted does not accept charity from unlawful wealth. (Ahmad)','له حرام مال نه الله تعالیٰ صدقه نه قبلوي. (احمد)')
F.done()
fin(s,'Scan 343 (printed page number not shown): two sayings in ornamental frames, each with its source in brackets (Ibn Majah; Ahmad). The book binding at the left edge and the frame ornaments are excluded.')
# scan 344 = file 172_page_1, printed 343
s=page(344,'back-matter','343','Back matter: two framed texts on the finality of prophethood','آخری صفحات: ختمِ نبوت پر دو فریم شدہ عبارتیں','وروستي مخونه: د ختم نبوت په اړه دوه چوکاټ لرونکي متنونه','bmp343')
F=Flow(s)
P(s,f'اللہ تعالیٰ کا ارشاد ہے: ’’(سیدنا) محمد {SA} تمھارے مردوں میں سے کسی کے باپ نہیں بلکہ اللہ تعالیٰ کے رسول اور خاتم الانبیاء ہیں۔‘‘ (الاحزاب: ۴۰)','Allah the Exalted says: “(Our master) Muhammad (peace be upon him) is not the father of any of your men, but he is the Messenger of Allah the Exalted and the Seal of the Prophets.” (Al-Ahzab: 40)','الله تعالیٰ فرمایي: «(سیدنا) محمد صلی الله علیه وآله وسلم ستاسو د سړو له جملې نه د هیچا پلار نه دی بلکې د الله تعالیٰ رسول او خاتم الانبیاء دی.» (الاحزاب: ۴۰)')
P(s,f'حضرت محمد رسول اللہ خاتم النبیین {SA} کا ارشاد ہے: ’’میں آخری نبی ہوں۔ میرے بعد کوئی نبی نہیں ہے۔‘‘ (جامع ترمذی: ابواب الفتن)','Hazrat Muhammad, the Messenger of Allah, the Seal of the Prophets (peace be upon him) said: “I am the last prophet. There is no prophet after me.” (Jami\' al-Tirmidhi: Abwab al-Fitan)','حضرت محمد رسول الله خاتم النبیین صلی الله علیه وآله وسلم فرمایي: «زه وروستی نبي یم. زما وروسته هیڅ نبي نشته.» (جامع ترمذي: ابواب الفتن)')
F.done()
fin(s,'Scan 344 = printed page 343: two texts in ornamental frames on the finality of prophethood (Qur\'an, Al-Ahzab 33:40, and a hadith from Jami\' al-Tirmidhi). A thumb at the lower left and the frame ornaments are excluded.')
