from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Poem couplets: the two printed lines are stored with a line break.'
# scan 120 = printed 113
s=page(120,'n01','113','Section title: Hissa-e-Nazm (Poetry part)','سیکشن عنوان: حصۂ نظم','د برخې سرلیک: د نظم برخه','divider')
F=Flow(s)
H(s,'حصۂ نظم','Hissa-e-Nazm (Poetry part)','د نظم برخه')
F.done()
s['sourceNote']='Printed page 113 (scan 120): section-divider page with the calligraphic title “حصۂ نظم” in a decorative emblem (not reproduced); no other text.'+NOTE
s['vocabulary']={}
save(s)
# scan 121 = printed 114
s=page(121,'n01','114','Maher-ul-Qadri (poet profile)','ماہر القادری (شاعر کا تعارف)','ماهر القادري (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'ماہر القادری','Maher-ul-Qadri','ماهر القادري')
P(s,'پیدایش: ۳۰؍ جولائی ۱۹۰۶ء — وفات: ۱۲؍ مئی ۱۹۷۸ء','Born: 30 July 1906 — Died: 12 May 1978','زېږېدنه: ۳۰ جولای ۱۹۰۶ز — وفات: ۱۲ مۍ ۱۹۷۸ز')
P(s,'منظور حسین نام اور ماہرؔ تخلص تھا لیکن ماہر القادری کے نام سے شہرت پائی۔ اُتر پردیش کے ضلع بُلند شہر میں پیدا ہوئے۔ ابتدائی تعلیم علی گڑھ سے حاصل کی۔ حیدر آباد دکن میں ان کی ادبی شہرت بامِ عروج پر تھی۔ پاکستان بننے پر کراچی آ گئے۔ ہندوستان میں کچھ عرصہ روزنامہ «مدینہ» سے وابستہ رہے۔ ۱۹۴۹ء میں رسالہ «فاران» نکالا۔ جدّہ کے ایک مشاعرے میں حرکتِ قلب بند ہونے کے باعث انتقال کر گئے اور وصیّت کے مطابق مکّہ معظّمہ میں دفن کیے گئے۔','His name was Manzoor Hussain and his pen-name Maher, but he gained fame under the name Maher-ul-Qadri. He was born in Bulandshahr district of Uttar Pradesh. He received his early education at Aligarh. In Hyderabad Deccan his literary fame was at its peak. When Pakistan was created he came to Karachi. In India for some time he was attached to the daily “Madina”. In 1949 he brought out the magazine “Faran”. He died of heart failure at a mushaira in Jeddah and, according to his will, was buried in Makkah al-Mukarramah.','نوم یې منظور حسین او تخلص یې ماهر و خو د ماهر القادري په نوم یې شهرت وموند. د اترپردېش د بلند شهر په ولسوالۍ کې زېږېدلی دی. لومړنۍ زده‌کړه یې له علي ګړه نه ترلاسه کړه. په حیدر آباد دکن کې د هغه ادبي شهرت په لوړه څوکه و. د پاکستان له جوړېدو سره کراچۍ ته راغی. په هندوستان کې څه موده د ورځپاڼې «مدینه» سره تړلی و. په ۱۹۴۹ز کې یې مجله «فاران» وایستله. د جدې په یوه مشاعره کې د زړه د درېدو له امله مړ شو او د وصیت له مخې په مکه معظمه کې ښخ شو.')
P(s,'ماہر القادری نے تمام اصنافِ سخن میں طبع آزمائی کی، لیکن اُن کی اصل شہرت نعت گوئی کی وجہ سے ہے۔ اُن کی شاعری کی نمایاں خصوصیّت سادگی اور بے تکلفی ہے۔ چوں کہ اُن کی شاعری کا محور حضور (ﷺ) کی ذاتِ گرامی ہے، اس لیے موضوع کی مناسبت سے اُن کی زبان پاکیزہ اور شستہ ہے۔ اُن کا دل عشقِ رسول (ﷺ) سے معمور تھا۔ حضرت محمد رسول اللہ خاتم النبیین (ﷺ) کی محبّت ہی اصلِ ایمان ہے اور یہی عشق اُن کی نعتوں کا محور و مرکز ہے۔ اسی جذبے سے سرشار ہو کر جب آپ نعت لکھتے ہیں تو سماں بندھ جاتا ہے۔ نبی اکرم (ﷺ) سے والہانہ محبّت آپ کا سرمایۂ حیات ہے۔','Maher-ul-Qadri tried his talent in all genres of poetry, but his real fame is due to composing naats. The prominent feature of his poetry is simplicity and informality. Since the axis of his poetry is the revered person of the Prophet (peace be upon him), in keeping with the subject his language is pure and refined. His heart was filled with love of the Messenger (peace be upon him). Love of Hazrat Muhammad, Messenger of Allah, Seal of the Prophets (peace be upon him) is the very root of faith, and this same love is the axis and centre of his naats. When, overflowing with this feeling, he writes a naat, the atmosphere is bound. Passionate love for the Noble Prophet (peace be upon him) is the capital of his life.','ماهر القادري په ټولو شعري ډولونو کې طبع ازمایي وکړه، خو د هغه اصلي شهرت د نعت ګویۍ له امله دی. د هغه د شاعرۍ څرګنده ځانګړتیا سادګي او بې تکلفي ده. ځکه چې د هغه د شاعرۍ محور د حضور (ﷺ) ګرانه ذات دی نو د موضوع له مناسبت د هغه ژبه پاکه او ښه شوې ده. د هغه زړه د رسول (ﷺ) په عشق ډک و. د حضرت محمد رسول الله خاتم النبیین (ﷺ) مینه د ایمان اصل دی او همدا عشق د هغه د نعتونو محور او مرکز دی. د همدې جذبې سره سرشار کېدو سره کله چې نعت لیکي نو فضا ټینګېږي. له نبي اکرم (ﷺ) سره والهانه مینه د هغه د ژوند پانګه ده.')
P(s,'مجموعہ ہائے کلام: محسوساتِ ماہر، نغماتِ ماہر، جذباتِ ماہر، ذکرِ جمیل وغیرہ۔','Poetry collections: Mahsusat-e-Maher, Naghmat-e-Maher, Jazbat-e-Maher, Zikr-e-Jameel, etc.','د شعري ټولګې: محسوسات ماهر، نغمات ماهر، جذبات ماهر، ذکر جمیل او نور.')
F.done()
s['sourceNote']='Printed page 114 (scan 121): ornamental title “ماہر القادری”, portrait (not reproduced), birth/death boxes (30 July 1906 and 12 May 1978), biography and the list of collections. The benedictions after the Prophet’s name are small calligraphic marks in print.'+NOTE
s['vocabulary']={}
save(s)
# scan 122 = printed 115
s=page(122,'n01','115','Hamd (Maher-ul-Qadri)','حمد (ماہر القادری)','حمد (ماهر القادري)','poem1')
F=Flow(s)
H(s,'حمد','Hamd','حمد')
V(s,'فکر و دانش کی ہے معراج خدا کا اِقرار','یہی وجدان کی آواز ہے، فطرت کی پکار','The zenith of thought and knowledge is the acknowledgement of God.','This is the voice of intuition, the call of nature.','د فکر او پوهې معراج د خدای اقرار دی','همدا د وجدان غږ دی، د فطرت ږغ')
V(s,'ذرّے ذرّے کی شہادت کہ خدا ہے موجود','پتّے پتّے کو ہے صانع کی صفت کا اِقرار','The testimony of every particle that God exists;','every leaf has acknowledgement of the Maker’s attribute.','د هرې ذرې شهادت چې خدای موجود دی','د هرې پاڼې ته د جوړوونکي د صفت اقرار دی')
V(s,'اُسی خَلّاق نے جوہر کو توانائی دی','پھول پتّوں کو عطا جس نے کیے نقش و نگار','That same Creator gave energy to the atom;','He who bestowed on flowers and leaves their patterns and designs.','همدې خالق جوهر ته ځواک ورکړ','چې ګلونو او پاڼو ته یې نقش او نګار ورکړل')
V(s,'اُسی خالق، اُسی مالک کی ہے سب حمد و ثنا','آبشاروں کا ترنّم ہو کہ گلِ بانگِ ہزار','All praise and glory belong to that same Creator, that same Master,','whether the melody of waterfalls or the nightingale’s song to the rose.','د همدې خالق، همدې مالک ده ټوله حمد او ثنا','د اوبو د غورځېدو ترنم وي که د ګل بلبل بانګ')
V(s,'یہ سب آیاتِ الٰہی ہیں، ذرا غور سے دیکھ','اُس کی پھر حمد بیاں کر، اُسی خالق کو پکار','All these are the signs of God; look carefully;','then express His praise; call upon that same Creator.','دا ټول د الله آیتونه دي، لږ په غور وګوره','بیا د هغه حمد بیان کړه، همدې خالق ته غږ کړه')
V(s,'اس کی صنعت کے نمونے ہیں وہ نکہت ہو کہ رنگ','اُس کی قدرت کے کرشمے ہیں، خزاں ہو کہ بہار','Whether fragrance or colour, they are samples of His craftsmanship;','they are marvels of His power, whether autumn or spring.','د هغه د صنعت نمونې دي که عطر وي که رنګ','د هغه د قدرت کرشمې دي، که مني وي که پسرلی')
F.done()
s['sourceNote']='Printed page 115 (scan 122): title “حمد” in an ornamental frame and six couplets in a two-line, centre-aligned layout (spaced lettering as printed). The poet is Maher-ul-Qadri per the contents page.'+NOTE
s['vocabulary']={}
save(s)
