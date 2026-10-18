from urduhelp import *
c=cell
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def D(s,lab,t,e,p): add(s,f'p{len(s["paras"])+1}',e,f'{lab}: {t}',f'{lab}: {p}',speaker=lab)
def V(s,ur,en,ps): add(s,f'p{len(s["paras"])+1}',en,ur,ps,boxed=True,kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Drama dialogue; verse lines are printed in blue.'
# scan 75 = printed 67
s=page(75,'p09','67','Khoobsurat Bala, part 5','خوب صورت بلا (حصہ پنجم)','ښکلې بلا (پنځمه برخه)','l5')
F=Flow(s)
for lab,t,e,p in [('توفیق','نیکی کیا چیز ہے؟ نیکی ایک پاک نور ہے، نیکی خدا کے ہاتھ کا بنایا ہوا ایک قلعہ ہے جس میں پاک انسان بیٹھ کر شیطان کی فوج کا مقابلہ کرتا ہے۔','What is goodness? Goodness is a pure light; goodness is a fortress made by the hand of God in which the pure human sits and fights the army of Satan.','نېکي څه شی دی؟ نېکي یوه پاکه رڼا ده، نېکي د خدای د لاس جوړ شوی یو کلا ده چې په هغې کې پاک انسان کېني او د شیطان له لښکر سره مقابله کوي.'),
('شمسہ','پاگل ہو گیا ہے۔','He has gone mad.','لېونی شوی دی.'),
('توفیق','ہاں ہاں! میں پاگل ہو گیا ہوں مگر خدا کا شکر ہے، خدا کا باغی، حرص کا بندہ، شیطان کا غلام، بے رحم، خونی اور نمک حرام نہیں ہوں۔','Yes, yes! I have gone mad, but thank God I am not a rebel against God, a slave of greed, a slave of Satan, merciless, bloodthirsty and ungrateful.','هو هو! زه لېونی شوی یم خو د خدای شکر دی، د خدای یاغي، د حرص بنده، د شیطان غلام، بې رحمه، وینه تویونکی او نمک حرام نه یم.'),
('شمسہ','او نمک حرام! ہمارے سامنے یہ گستاخانہ کلام؟','You ingrate! This insolent speech before us?','ای نمک حرامه! زموږ مخې ته دا ګستاخانه خبرې؟'),
('توفیق','میں ان لوگوں میں سے نہیں ہوں جو پیٹھ پیچھے برائی کا اظہار کرتے ہیں۔ میں بہادر ہوں اور بہادر ہمیشہ سامنے آ کر وار کرتے ہیں۔','I am not among those who express evil behind one’s back. I am brave, and the brave always strike coming face to face.','زه له هغو خلکو نه نه یم چې شاته بدي څرګندوي. زه زړور یم او زړور تل مخې ته راتلو سره وار کوي.')]:
    D(s,lab,t,e,p)
V(s,'صاف دل اس طرح کہتے ہیں برابر صاف صاف / جس طرح آئینہ کہہ دیتا ہے مُنھ پر صاف صاف','The pure-hearted speak thus, plainly and directly, / just as the mirror says plainly to one’s face.','پاک زړي داسې پرله پسې په ښکاره ښکاره وايي / لکه څنګه چې هینداره پر مخ ښکاره ښکاره وايي')
for lab,t,e,p in [('قتلو','اگر تو ضد چھوڑ دے تو میں ایمان سے کہتا ہوں ………','Qatlu: If you give up your stubbornness, I tell you on my faith …','قتلو: که ته ضد پرېږدې نو زه په ایمان وایم ………'),
('توفیق','چُپ بد معاش! اس مقدّس چیز کا نام نہ لے جس کا ایک ذرّہ بھی تیرے ناپاک تن میں نہیں ہے۔ تم دونوں شیطان سے زیادہ ایمان کے دشمن ہو۔','Tawfeeq: Silence, rascal! Do not take the name of that holy thing of which not a particle is in your impure body. You two are greater enemies of faith than Satan.','توفیق: چوپ شه بدمعاشه! د هغه پاک شي نوم مه اخله چې یو ذره هم ستا په ناپاک تن کې نشته. تاسو دواړه له شیطان نه زیات د ایمان دښمنان یاست.'),
('شمسہ','بے شک ہیں اور اس لیے ہیں کہ بہادر کو نا مراد اور سرخ رُو کو زرد بنانے والا یہی ہے۔','Shamsa: Certainly they are, and they are so because it is this that makes the brave disappointed and the red-faced pale.','شمسه: بې شکه یو او ځکه یو چې دا بهادر ناکام او سرخ مخي ژیړ جوړوي.'),
('توفیق','جس طرح خدا نے جسم کے لیے جان کا لیمپ جلایا ہے، اسی طرح جان کے لیے ایمان کا چراغ بنایا ہے۔','Tawfeeq: Just as God has lit the lamp of life for the body, so He has made the lamp of faith for life.','توفیق: لکه څنګه چې خدای د جسم لپاره د ساه لیمپ بل کړی دی همداسې یې د ساه لپاره د ایمان څراغ جوړ کړی دی.'),
('شمسہ','مگر میں ہوں، تو ضرور اس چراغ کی روشنی بجھاؤں گی۔','Shamsa: But if I am here, I shall surely extinguish the light of that lamp.','شمسه: خو که زه یم نو ضرور به د دې څراغ رڼا ړنګه کړم.'),
('توفیق','اری! تو کیا، اگر تمام دنیا کے شیطان مل کر کوشش کریں پھر بھی یہ خدائی چراغ ہمیشہ جگمگاتا رہے گا اور جہاں میں رحم اور انصاف کی روشنی پھیلاتا رہے گا۔','Tawfeeq: Hey! What are you? Even if all the devils of the world together try, this divine lamp will still go on glittering and will go on spreading the light of mercy and justice in the world.','توفیق: ای! ته څه یې؟ که د ټولې نړۍ شیطانان یو ځای هڅه وکړي بیا هم دا خدايي څراغ به تل ځلېږي او په نړۍ کې به د رحم او انصاف رڼا خپروي.'),
('شمسہ','توفیق! تُو جانتا ہے میں کیسی عورت ہوں؟','Shamsa: Tawfeeq! Do you know what sort of woman I am?','شمسه: توفیقه! ته پوهېږې زه کومه ښځه یم؟'),
('توفیق','ذلّت کی پُتلی! تجھے عورت کون کہتا ہے؟ عورت وہ ہے جس میں رحم ہو، شرم ہو، سچّائی ہو، باوفائی ہو، پارسائی ہو، جس نے فرشتوں کی طینت اور حور کی عصمت پائی ہو۔ تُو کبھی عورت نہیں ہو سکتی۔ جس طرح تُو نے معصوم شہزادے کا دغا سے حق چھینا ہے، اسی طرح عورت کے نام پر بھی زبردستی قبضہ کر لیا ہے۔','Tawfeeq: You puppet of disgrace! Who calls you a woman? A woman is one who has mercy, modesty, truthfulness, faithfulness, piety, who has received the nature of angels and the chastity of a houri. You can never be a woman. Just as you snatched the right of the innocent prince by deceit, so you have forcibly taken possession of the name of woman too.','توفیق: د سپکاوي کوکی! تا ته ښځه څوک وايي؟ ښځه هغه ده چې رحم، شرم، رښتینولي، وفا او پارسايي ولري، چې د فرښتو طینت او د حورې عصمت یې موندلی وي. ته هیڅکله ښځه نشې کېدای. لکه څنګه چې تا د معصوم شهزاده حق په دغا ایستلی دی همداسې د ښځې په نوم هم په زوره قبضه کړې ده.')]:
    D(s,lab,t,e,p)
F.done()
s['sourceNote']='Printed page 67 (scan 75): continuation of the drama (speaker labels in blue: توفیق, شمسہ, قتلو); a verse in blue. The last speech of Tawfeeq continues on the next page.'+NOTE
s['vocabulary']={}
save(s)
# scan 76 = printed 68
s=page(76,'p09','68','Khoobsurat Bala, part 6','خوب صورت بلا (حصہ ششم)','ښکلې بلا (شپږمه برخه)','l6')
F=Flow(s)
D(s,'شمسہ','توفیق! سُن۔','Shamsa: Tawfeeq! Listen.','شمسه: توفیقه! واوره.')
V(s,'سانس سے آگ، جو برساؤں وہ اُژدر ہوں میں / ضد میں طوفان، تو غصے میں سمندر ہوں میں / پیس ڈالوں گی، مٹا دوں گی، فنا کر دوں گی / یاد رکھنا! تری تقدیر کا چکر ہوں میں','From my breath fire, what I rain — I am a dragon; / in stubbornness a storm, in rage a sea am I. / I will grind you, erase you, annihilate you; / remember! I am the wheel of your fate.','له ساه نه اور، چې وورېږم هغه ازدها یم زه / په ضد کې طوفان، په غصه کې سمندر یم زه / وبه یې شندم، له منځه به یې یوسم، فنا به کړم / یاد ساته! ستا د برخلیک ګردش یم زه')
D(s,'توفیق','دل کا جوش ایسے ڈراوے سے کہیں گھٹتا ہے / موم سے پنجۂ فولاد کہیں دبتا ہے / مت سمجھ دل سے مرے زہرِ دغا نکلے گا / چیر کر دیکھ شرافت سے بھرا نکلے گا','Tawfeeq: Does the heart’s zeal ever lessen with such threats? / Does a steel hand ever yield to wax? / Do not think poison of treachery will come from my heart; / cut it open and see: it will come out full of nobility.','توفیق: د زړه جوش له داسې ویرولو نه کله کمېږي / له موم نه د فولادو پنجه کله ټیټېږي / مه ګڼه زما له زړه به د دغا زهر راوځي / ورته چاک کړه او وګوره له شرافت به ډک راوځي')
V(s,'روتے روتے کی زباں پر یہ سخن جاری ہے / جان پیاری نہیں، دنیا سے وفا پیاری ہے','On the lips of the weeping this saying flows: / life is not dear; fidelity to the world is dear.','د ژړا په ژبه دا خبره جاري ده / ساه ګرانه نه ده، له نړۍ سره وفا ګرانه ده')
D(s,'قتلو','دیوانے! کیوں جان کر دنیا کی خوشیوں سے بے زار ہے۔ تیری ایک ہاں پر شاہی مہربانیوں کا بادل عزت، دولت اور رحم کی بارش برسانے کے لیے تیار ہے۔','Qatlu: Madman! Why do you knowingly turn away from the joys of the world? On your one “yes” the cloud of royal favours is ready to rain honour, wealth and mercy.','قتلو: لېوني! ولې پوهېدلو سره د نړۍ له خوښیو بې زاره یې. ستا په یو هو شاهي مهربانیو وریځ د عزت، دولت او رحم باران ورولو ته چمتو ده.')
D(s,'توفیق','مجھے کوئی ایسی مہربانی نہیں چاہیے۔ اُو حرص کے غلام! یاد رکھ یہ کلام','Tawfeeq: I want no such favour. O slave of greed! Remember this saying:','توفیق: ماته داسې مهرباني نه ده په کار. ای د حرص غلامه! دا خبره یاده ساته')
V(s,'چار دن ہے شان و شوکت کا خمار / موت کی تُرشی نشہ دے گی اُتار / جب اٹھائیں گے جنازہ مل کے یار / ہاتھ مل مل کے کہے گا بار بار','The intoxication of pomp and grandeur lasts four days; / the sourness of death will strip away the intoxication. / When friends carry the bier together, / (the dead) will say again and again, wringing hands:','د شان او شوکت خمار څلور ورځې دی / د مرګ ترخوالی به نشه راښکته کړي / کله چې ملګري جنازه یو ځای پورته کړي / لاسونه ملي ملي به بیا بیا ووايي')
V(s,'«کس لیے آئے تھے ہم کیا کر چلے / جو یہاں پایا یہیں سب دھر چلے»','“For what had we come, and what did we do; / whatever we got here we all left here.”','«د څه لپاره راغلي وو موږ او څه کړل / څه چې دلته مو ترلاسه کړل ټول دلته مو پرېښودل»')
D(s,'شمسہ','بس بس یہ وعظ پاگلوں کے لیے رکھ چھوڑ۔ سہیل کو ہمارے حوالے کر۔ تاج کا تابع دار ہو، ورنہ خوف ناک','Shamsa: Enough, enough! Keep this sermon for madmen. Hand over Suhail to us. Be a subject of the crown, otherwise a terrible','شمسه: بس بس دا وعظ لېونیانو لپاره ساته. سهیل موږ ته وسپاره. د تاج تابع شه، که نه ویروونکی')
F.done()
s['sourceNote']='Printed page 68 (scan 76): continuation of the drama (speaker labels in blue: شمسہ, توفیق, قتلو); several verse passages (in blue). The last line continues on the next page. “اُژدر”, “ترشی” are read as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 77 = printed 69
s=page(77,'p09','69','Khoobsurat Bala, end','خوب صورت بلا (اختتام)','ښکلې بلا (پای)','l7')
F=Flow(s)
P(s,'انجام کی پیشوائی کے لیے تیّار ہو۔','end must be awaited and prepared for.','انجام ته د پېښو لپاره چمتو شه.')
for lab,t,e,p in [('توفیق','کیا معصوم شہزادے کو تم قصابوں کے پنجے میں ذبح ہونے کے لیے دے دوں؟ رحم اور انصاف کے گلے پر چھری پھیر دوں؟ تخت و تاج کے لٹیروں کو تعظیم کروں؟ شیطان کو بہشت کا مالک و وارث تسلیم کروں؟ نہیں! او وفادار توفیق سے ایسا کبھی نہیں ہوگا۔','Tawfeeq: Shall I give the innocent prince into the butchers’ claws to be slaughtered? Run a knife across the throat of mercy and justice? Honour the robbers of throne and crown? Acknowledge Satan as master and heir of Paradise? No! From the loyal Tawfeeq this will never happen.','توفیق: آیا معصوم شهزاده تاسو قصابانو په منګولو کې د ذبحې لپاره ورکړم؟ د رحم او انصاف په ستوني چاړه کېږدم؟ د تخت او تاج غلو ته تعظیم وکړم؟ شیطان د جنت مالک او وارث وګڼم؟ نه! له وفادار توفیق نه به داسې هیڅکله نه کېږي.'),
('قتلو','مگر تم کو ایسا ضرور کرنا پڑے گا۔','Qatlu: But you will certainly have to do so.','قتلو: خو تاسو ته به داسې ضرور کول پکار شي.'),
('توفیق','کیوں؟','Tawfeeq: Why?','توفیق: ولې؟'),
('شمسہ','ہمارا حکم۔','Shamsa: Our command.','شمسه: زموږ حکم.'),
('توفیق','تیرا حکم کوئی خدا کا حکم نہیں ہے۔','Tawfeeq: Your command is not the command of God.','توفیق: ستا حکم د خدای حکم نه دی.'),
('شمسہ','میں شاہی حکم دیتی ہوں۔','Shamsa: I give a royal command.','شمسه: زه شاهي حکم ورکوم.'),
('توفیق','میں تیری شاہی سے بھی منکر ہوں۔','Tawfeeq: I deny even your royalty.','توفیق: زه ستا له شاهۍ نه هم منکر یم.')]:
    D(s,lab,t,e,p)
V(s,'تیر و تلوار و تبر نیزہ و خنجر برسیں / زہر، خوں، آگ، مصیبت کے سمندر برسیں / بجلیاں چرخ سے اور کوہ سے پتھر برسیں / ساری دنیا کی بلائیں مرے سر پر برسیں','Let arrows, swords, axes, spears and daggers rain; / let poison, blood, fire, seas of calamity rain; / let lightning rain from the heavens and stones from the mountain; / let all the calamities of the world rain on my head.','غشي، تورې، تبر، نیزې او خنجرونه دې ورېږي / زهر، وینه، اور، د مصیبت سمندرونه دې ورېږي / ورېځې له اسمانه او له غره دې ډبرې ورېږي / د ټولې نړۍ بلاګانې دې زما پر سر ورېږي')
V(s,'ختم ہو جائے ہر اک رنج و مصیبت مجھ پر / مگر ایمان کو جنبش ہو، تو لعنت مجھ پر','May every grief and calamity end upon me; / but if my faith should waver, a curse upon me.','هر رنځ او مصیبت دې پر ما ختم شي / خو که د ایمان ځای بدلېږي نو پر ما لعنت دی')
D(s,'شمسہ','غور کر پھر غور کر ورنہ اجل تیّار ہے / تیرا سر ہے اور اس جلاد کی تلوار ہے','Shamsa: Think, think again, otherwise death is ready; / there is your head and the executioner’s sword.','شمسه: غور وکړه بیا غور وکړه که نه مرګ چمتو دی / ستا سر دی او د دې جلاد تور ده')
D(s,'توفیق','مصیبت کے ڈر، رنج کے ہول سے / بہادر بدلتے نہیں قول سے','Tawfeeq: For fear of calamity, from the terror of grief, / the brave do not change their word.','توفیق: د مصیبت له ویرې، د رنځ له وېرې / زړورو خپل قول نه بدلوي')
V(s,'خدا لے کہ تو لے، یہ جان ایک ہے / مگر بات ایک اور زبان ایک ہے','Whether God take it or you, this life is one; / but the word is one and the tongue is one.','خدای یې واخلي که ته، دا ساه یوه ده / خو خبره یوه او ژبه یوه ده')
D(s,'شمسہ','مجھ پہ لعنت ہے جو تجھ کو اب میں زندہ چھوڑ دوں / کاٹ لاسر، تاکہ اس کو ٹھوکروں سے پھوڑ دوں','Shamsa: A curse upon me if I now leave you alive: / bring the head cut off, so that I may break it with kicks.','شمسه: پر ما لعنت دی چې تا اوس ژوندی پرېږدم / سر پرې کړه راوله، ترڅو هغه په ټکرونو مات کړم')
P(s,'(جانا) سین ختم','(Exit.) End of the scene.','(تلل) سین پای')
F.done()
s['sourceNote']='Printed page 69 (scan 77): end of the drama excerpt (stage direction “(جانا) سین ختم” at the foot); speaker labels in blue; the first line continues the previous page; verse lines in blue and black.'+NOTE
s['vocabulary']={}
save(s)
