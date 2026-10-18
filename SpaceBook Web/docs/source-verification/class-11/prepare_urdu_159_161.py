from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n11',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 159 = printed 152
s=page(159,'n11','152','Exercise (Mashq) on Yeh Sarkain; box on Mukhammas','مشق: «یہ سڑکیں» پر سوالات؛ مخمّس','تمرین: «دا سړکونه» پوښتنې؛ مخمس','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ نظم میں شہر کی سڑکوں کا نقشہ کس طرح کھینچا گیا ہے؟','1. How is the picture of the city’s roads drawn in the poem?','۱. په نظم کې د ښار د سړکونو انځور څنګه کښل شوی دی؟')
Q(s,'2۔ نظم «یہ سڑکیں» کا خلاصہ لکھیں۔','2. Write a summary of the poem “Yeh Sarkain”.','۲. د «دا سړکونه» نظم لنډیز ولیکئ.')
Q(s,'3۔ تلمیح سے مراد شاعری میں کسی تاریخی واقعہ یا کردار کا ذکر ہوتا ہے۔ اس نظم میں شاعر نے کون کون سی تلمیحات بیان کی ہیں؟','3. Talmeeh means mention in poetry of some historical event or character. Which allusions has the poet stated in this poem?','۳. د تلمیح مراد په شاعرۍ کې د کوم تاریخي پېښې یا کردار یادونه ده. پدې نظم کې شاعر کومې کومې تلمیحات بیان کړې دي؟')
Q(s,'4۔ مصرعے کی وضاحت کریں: «پرانے وقت کے بغداد کی اولاد یہ سڑکیں»۔','4. Explain the line: “these roads, the offspring of the Baghdad of old times.”','۴. مصرعه تشریح کړئ: «د زړې زمانې د بغداد اولاد دا سړکونه».')
Q(s,'5۔ درج ذیل کے چار چار ہم قافیہ الفاظ لکھیں۔ ایجاد، گرداب، نگر، قلم، خار۔','5. Write four rhyming words for each of the following: ijaad, girdaab, nagar, qalam, khaar.','۵. د لاندې هر یوه لپاره څلور څلور هم قافیه الفاظ ولیکئ. ایجاد، ګرداب، نګر، قلم، خار.')
Q(s,'6۔ «گلوں سے خار بہتر ہیں، جو دامن تھام لیتے ہیں» شاعر نے یہ مصرع واین میں کیوں لکھا ہے؟ وضاحت کریں۔','6. “Thorns are better than roses, for they hold the skirt.” Why has the poet written this line within quotation marks? Explain. (the printed word “واین” is read as “ان/inverted commas”)','۶. «له ګلانو نه خاره ښه دي چې لمن نیسي» شاعر دا مصرعه په نقل قول کې ولې لیکلې ده؟ تشریح کړئ.')
H(s,'مخمّس:','Mukhammas:','مخمس:')
P(s,'جس نظم کے ہر بند میں پانچ مصرعے ہوں، اُسے «مخمّس» کہتے ہیں۔','A poem in each band of which there are five lines is called a “mukhammas”.','هغه نظم چې په هر بند کې یې پنځه مصرعې وي «مخمس» بلل کېږي.',boxed=True)
F.done()
s['sourceNote']='Printed page 152 (scan 159): “Mashq” title, questions 1–6 (question 5 lists words in blue; question 6 quotes the line in blue) and the blue box “مخمّس”.'+NOTE
s['vocabulary']={}
save(s)
# scan 160 = printed 153
s=page(160,'n12','153','Mirza Mahmood Sarhadi (poet profile)','مرزا محمود سرحدی (شاعر کا تعارف)','مرزا محمود سرحدي (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'مرزا محمود سرحدی','Mirza Mahmood Sarhadi','مرزا محمود سرحدي')
P(s,'پیدایش: ۱۹۱۳ء — وفات: ۱۹۶۸ء','Born: 1913 — Died: 1968','زېږېدنه: ۱۹۱۳ز — وفات: ۱۹۶۸ز')
P(s,'مرزا محمود سرحدی پشاور میں پیدا ہوئے۔ وہ اوائلِ زندگی ہی سے غمِ روزگار کے چکر میں پڑ گئے۔ انھیں زندگی گزارنے کے لیے بڑے جتن کرنے پڑے۔ فوجی نوکری سے لے کر اسکول میں مدرسی تک اور کلرکی سے مزدوری تک کئی مراحل سے گزرنا پڑا۔','Mirza Mahmood Sarhadi was born in Peshawar. From the very beginning of his life he fell into the whirl of worldly cares. He had to make great efforts to pass his life. From army service to teaching in school, and from clerkship to labour, he had to pass through several stages.','مرزا محمود سرحدي په پېښور کې زېږېدلی دی. هغه د ژوند له پیله د روزګار په غم کې اخته شو. هغه ته د ژوند تېرولو لپاره ډېرې هڅې کول پکار شول. له پوځي نوکرۍ نه تر په ښوونځي کې ښوونکي پورې او له کلرکۍ نه تر مزدورۍ پورې یې څو پړاوونه تېر کړل.')
P(s,'اُنھوں نے اکبر الٰہ آبادی کے طنزیہ و مزاحیہ انداز کی تقلید کی ہے اور اسی وجہ سے انھیں «اکبرِ سرحد» بھی کہا جاتا ہے۔ مرزا کے مزاح میں لفظوں کی ہیرا پھیری نہیں ملتی، بل کہ اُن کا مزاح ایک حقیقت پسند مزاح تھا، جو وہ حالات و واقعات اور اُن کے نتائج سے پیدا کرتے ہیں۔ انھوں نے اپنے لیے، جس میدان کا انتخاب کیا، وہ فن کے اعتبار سے دشوار ترین رہ گزار سے کم نہیں۔ طنز اور مزاح کی تمام تر لطافتوں کو برقرار رکھتے ہوئے انتہائی مختصر پیرائے میں جامع اور مکمل بات کا اظہار کرنا بے حد مشکل کام ہے۔ اس میں ایک طرف شاعر سنجیدگی سے دامن بچاتا ہے، تو دوسری طرف پھکّڑ پن کی حدود سے دُور رہتا ہے۔','He imitated the satirical and humorous manner of Akbar Allahabadi and for this reason he is also called “Akbar-e-Sarhad”. In Mirza’s humour there is no trickery of words; rather his humour was a realist humour, which he created from circumstances and events and their results. The field which he chose for himself is no less than the most difficult path in terms of art. To express a comprehensive and complete matter in an extremely brief form, preserving all the delicacies of satire and humour, is an extremely hard task. In it the poet on the one hand keeps his skirt from seriousness, and on the other keeps away from the limits of vulgarity.','هغه د اکبر الله اباد د طنزیه او مزاحیه انداز تقلید وکړ او همدا لامل دی چې هغه «اکبر سرحد» هم بلل کېږي. د مرزا په مزاح کې د الفاظو الټا پلټا نه موندل کېږي بلکې د هغه مزاح یو حقیقت غوښتونکی مزاح و چې هغه یې له حالاتو او پېښو او د هغو له پایلو نه پیدا کوي. هغه چې د خپل ځان لپاره کوم میدان غوره کړ هغه د فن له مخې له ډېر ستونزمنې لارې نه کم نه دی. د طنز او مزاح د ټولو نرمیو ساتلو سره په ډېر لنډ انداز کې جامع او بشپړه خبره څرګندول ډېر ستونزمن کار دی. پدې کې یو لور شاعر له جدیت نه ځان ساتي نو بل لور ته له سپکوالي له حدودو نه لرې پاتې کېږي.')
P(s,'مرزا محمود سرحدی نے ہر موضوع پر طبع آزمائی کی، لیکن اُن کا اصل میدان «قطعات» ہیں۔ اُنھوں نے چھوٹے چھوٹے معاشرتی مسائل کو بڑی خوب صورتی سے اپنے قطعات میں سمویا ہے۔ مثلاً: چوری، رہزنی، ذخیرہ اندوزی، گراں فروشی، ملاوٹ، جھوٹ اور مکر و فریب وغیرہ۔ ان کا طنز سماجی ناسوروں کے لیے کسی نشتر سے کم نہیں۔ مرزا محمود سرحدی نے ساری عمر شادی نہیں کی زندگی کے آخری ایّام میں دمے کے مرض کی وجہ سے علیل رہنے لگے تھے۔ اُنھوں نے پشاور میں وفات پائی۔','Mirza Mahmood Sarhadi tried his hand at every subject, but his real field is “qitaat” (quatrains). He has woven small social problems very beautifully into his qitaat, for example: theft, highway robbery, hoarding, profiteering, adulteration, lies and deceit, etc. His satire is no less than a lancet for social ulcers. Mirza Mahmood Sarhadi did not marry all his life; in the last days of his life he began to be ill because of asthma. He died in Peshawar.','مرزا محمود سرحدي په هر موضوع طبع ازمایي وکړه خو د هغه اصلي میدان «قطعات» دي. هغه وړې وړې ټولنیزې ستونزې په ډېره ښکلا خپلو قطعاتو کې ځای کړې دي. مثلاً: غلا، رهزني، زخیره اندوزي، ګرانه پلورنه، ملاوټ، دروغ او مکر او فریب او نور. د هغه طنز د ټولنیزو ناسورونو لپاره له کوم نشتر نه کم نه دی. مرزا محمود سرحدي ټول عمر واده ونه کړ د ژوند په وروستیو ورځو کې د دمې د ناروغۍ له امله ناروغ پاتې کېدل پیل کړل. هغه په پېښور کې وفات شو.')
P(s,'مجموعہ ہائے کلام: سنگینے، اندیشۂ شہر۔','Poetry collections: Sangeene, Andesha-e-Shehr.','د شعري ټولګې: سنګینې، اندېښنه ښار.')
F.done()
s['sourceNote']='Printed page 153 (scan 160): ornamental title “مرزا محمود سرحدی”, birth/death boxes (1913/1914 and 1968 — the year of birth is read approximately as 1913), biography and the names of the poetry collections; no portrait on this page.'+NOTE
s['vocabulary']={}
save(s)
# scan 161 = printed 154
s=page(161,'n12','154','Qitaat (Mirza Mahmood Sarhadi)','قطعات (مرزا محمود سرحدی)','قطعات (مرزا محمود سرحدي)','poem1')
F=Flow(s)
H(s,'قطعات','Qitaat (Quatrains)','قطعات')
for r in [
('کبھی تو ان کی حسینوں سے شکل ملتی ہے','کبھی پناہ گزینوں سے شکل ملتی ہے','Sometimes their face resembles beauties,','sometimes their face resembles refugees;','کله د هغوی مخ ښکلو سره ورته وي','کله د پناه ګزینانو سره مخ ورته وي'),
('خدا کی شان ہے، وہ ہیں مرے وطن کے جواں','کہ جن کی پردہ نشینوں سے شکل ملتی ہے','it is God’s glory: these are the youths of my homeland,','whose faces resemble those who sit behind the veil.','د خدای شان دی، دا زما د وطن ځوانان دي','چې مخونه یې د پرده نشینانو سره ورته دي'),
('کیا بتائیں آپ کو کیا ہے ہمارا ہسپتال','انتظام ایسا کہ بس دل کی کلی کھل جائے ہے','What shall we tell you of what our hospital is?','the arrangement is such that the bud of the heart simply opens up;','تاسو ته څه ووایو زموږ روغتون څه دی','انتظام داسې دی چې بس د زړه غوټۍ خلاصېږي'),
('حادثاتِ اتفاقی کا بھی ہے اک ڈاکٹر','اتفاقی طور پر مل جائے، تو مل جائے ہے','there is a doctor also for accidental accidents;','if met by chance, he is met.','د ناڅاپي پېښو یو ډاکټر هم دی','په اتفاق سره ومومې نو مومې'),
('اگر کوچوں میں بھنگی رات کو جاروب کش پاؤ','غلاظت جس سڑک پر جا بجا بکھری ہوئی دیکھو','If you find sweepers with brooms in the lanes at night,','if you see filth scattered here and there on a road,','که په کوڅو کې د شپې جاروب وهونکي ومومې','که چېرې پر سړک ټوله ګند وینې'),
('تو جانو یہ بھی ہے اک شانِ بیداری کمیٹی کی','تو سمجھو اس طرف سے گزری ہے لاری کمیٹی کی','know that this too is a glory of the awakeness of the Committee;','understand that the Committee’s lorry has passed this way.','نو پوه شئ دا هم د بیدارۍ د کمېټۍ شان دی','نو پوه شئ چې دې لور ته د کمېټۍ لاري تېره شوې'),
('کالے چشمے بھی ایک نعمت ہیں','جو نگاہیں ملا نہیں سکتے','Dark glasses too are a blessing','for those who cannot meet gazes;','تور عینکې هم یوه نعمت دی','د هغو لپاره چې نظرونه نشي ملولای'),
('دھوپ میں خوب کام دیتے ہیں','رات دن ان سے کام لیتے ہیں','they serve well in the sun;','day and night they are used.','په لمر کې ښه کار ورکوي','شپه او ورځ ترې کار اخلي'),
('محتسب سے کہوں، تو کیا جا کر','پہلے ہوتا تھا دودھ میں پانی','What shall I go and say to the inspector?','Earlier there used to be water in the milk;','محتسب ته چې ووایم نو څه','مخکې به په شیدو کې اوبه وې'),
('آج پانی میں دودھ ہوتا ہے','میری مانند وہ بھی روتا ہے','today there is milk in the water;','like me, he too weeps.','نن په اوبو کې شیدې دي','زما په څېر هغه هم ژاړي')]:
    V(s,*r)
P(s,'(اندیشۂ شہر)','(Andesha-e-Shehr)','(اندېښنه ښار)')
F.done()
s['sourceNote']='Printed page 154 (scan 161): title “قطعات” in an ornamental frame, running head “مرزا محمود سرحدی”, and five quatrains (each of four half-lines in two rows, right-hand half-line before left-hand), separated by dotted rules with stars; source line “(اندیشۂ شہر)”. In the third quatrain the second row reads “اتفاقی طور پر مل جائے، تو مل جائے ہے”.'+NOTE
s['vocabulary']={}
save(s)
