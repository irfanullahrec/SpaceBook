from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
sq=[
 tr('How technology is shaped by physics?','طبیعیات ٹیکنالوجی کو کیسے تشکیل دیتی ہے؟','فزیک ټکنالوژي څنګه جوړوي؟'),
 tr('Physics and biology are considered different branches of science, how physics links with biology?','طبیعیات اور حیاتیات سائنس کی مختلف شاخیں سمجھی جاتی ہیں؛ طبیعیات کا حیاتیات سے کیا تعلق ہے؟','فزیک او بیولوژي د ساینس بېلابېلې څانګې ګڼل کېږي؛ فزیک له بیولوژۍ سره څنګه تړاو لري؟'),
 tr('Why are measurements important?','پیمائشیں کیوں اہم ہیں؟','اندازې ولې مهمې دي؟'),
 tr('Why area is a derived quantity?','رقبہ ماخوذ مقدار کیوں ہے؟','مساحت ولې مشتق کمیت دی؟'),
 tr('Name any four derived units and write them as their base units.','کوئی چار ماخوذ اکائیاں نام دیں اور انہیں ان کی بنیادی اکائیوں کی صورت میں لکھیں۔','د هر ډول څلورو مشتق واحدونو نومونه واخلئ او د هغوی د بنسټیزو واحدونو په بڼه یې ولیکئ.'),
 tr('Why in physics we need to write in scientific notation?','طبیعیات میں سائنسی علامتی صورت میں لکھنے کی ضرورت کیوں ہوتی ہے؟','په فزیک کې په علمي نښان لیکلو ته ولې اړتیا لرو؟'),
 tr('What is least count? How least count for vernier calliper and screw gauge are defined?','کم ترین شمار کیا ہے؟ ورنیئر کیلیپر اور سکرو گیج کے کم ترین شمار کی تعریف کیسے کی جاتی ہے؟','تر ټولو کوچنۍ اندازه څه ده؟ د ورنییر کالیپر او سکرو ګېج تر ټولو کوچنۍ اندازه څنګه تعریفېږي؟'),
 tr('How can we find the volume of a small pebble with the help of measuring cylinder?','پیمائشی سلنڈر کی مدد سے چھوٹے کنکر کا حجم کیسے معلوم کیا جا سکتا ہے؟','د پیمایشي استوانې په مرسته د یوې کوچنۍ تیږې حجم څنګه معلومولای شو؟')
]
lq=[
 tr('Define physics. How physics play a crucial role in science technology and society?','طبیعیات کی تعریف کریں۔ طبیعیات سائنس، ٹیکنالوجی اور معاشرے میں اہم کردار کیسے ادا کرتی ہے؟','فزیک تعریف کړئ. فزیک په ساینس، ټکنالوژۍ او ټولنه کې مهم رول څنګه لوبوي؟'),
 tr('What is SI? Name SI base quantities and their units.','SI کیا ہے؟ SI کی بنیادی مقداروں اور ان کی اکائیوں کے نام دیں۔','SI څه دی؟ د SI د بنسټیزو کمیتونو او د هغوی د واحدونو نومونه واخلئ.'),
 tr('What are physical quantities? Distinguish between base and derived physical quantities.','طبعی مقداریں کیا ہیں؟ بنیادی اور ماخوذ طبعی مقداروں میں فرق کریں۔','فزیکي کمیتونه څه دي؟ د بنسټیزو او مشتق فزیکي کمیتونو ترمنځ توپیر وکړئ.'),
 tr('What is standard form or scientific notation?','معیاری صورت یا سائنسی علامتی صورت کیا ہے؟','معیاري بڼه یا علمي نښان څه دی؟'),
 tr('What are prefixes? Explain with examples.','سابقے کیا ہیں؟ مثالوں سے وضاحت کریں۔','مختاړي څه دي؟ په بېلګو یې تشریح کړئ.'),
 tr('Describe the construction and use for measurement of the following instruments:','درج ذیل آلات کی ساخت اور پیمائش کے لیے استعمال بیان کریں:','د لاندې وسایلو جوړښت او د اندازه کولو لپاره استعمال تشریح کړئ:'),
 tr('a. Vernier Callipers     b. Screw gauge','a. ورنیئر کیلیپر     b. سکرو گیج','a. ورنییر کالیپر     b. سکرو ګېج'),
 tr('What is meant by the significant figures of measurement? What are the main points to be kept in mind while determining the significant figures of a measurement?','پیمائش کے بامعنی ہندسوں سے کیا مراد ہے؟ کسی پیمائش کے بامعنی ہندسے معلوم کرتے وقت کن بنیادی نکات کو ذہن میں رکھنا چاہیے؟','د اندازې له بامعنی شمېرو څخه څه مراد دی؟ د یوې اندازې د بامعنی شمېرو د ټاکلو پر مهال کوم اساسي ټکي باید په پام کې ونیول شي؟')
]
def structured(p,num): return dict(num=num,q=p['text'],urdu=p['urdu'],pashto=p['pashto'],ans='No answer is printed with this question in the textbook.',answerOrigin='No source solution provided',sourcePdfPage=32,sourcePrintedPage=27)
short=[structured(p,i+1) for i,p in enumerate(sq)]
long=[structured(p,i+1) for i,p in enumerate(lq[:6])]+[structured(lq[7],7)]
long[5].update(subquestions=[dict(label='a',q='Vernier Callipers'),dict(label='b',q='Screw gauge')],q=lq[5]['text']+'\n'+lq[6]['text'])
paras=[tr('Give a brief response to the following questions.','درج ذیل سوالات کے مختصر جواب دیں۔','لاندې پوښتنو ته لنډ ځوابونه ورکړئ.')]+[tr(str(i+1)+'. '+p['text'],str(i+1)+'. '+p['urdu'],str(i+1)+'. '+p['pashto']) for i,p in enumerate(sq)]
extended=[tr('Give an extended response to the following questions.','درج ذیل سوالات کے تفصیلی جواب دیں۔','لاندې پوښتنو ته مفصل ځوابونه ورکړئ.')]
for i,p in enumerate(lq):
 number=str(i+1) if i<6 else '' if i==6 else '7'
 extended.append(tr((number+'. ' if number else '')+p['text'],(number+'. ' if number else '')+p['urdu'],(number+'. ' if number else '')+p['pashto']))
save(dict(pdfPage=32,printedPage=27,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Conceptual questions 1–8 / comprehensive questions 1–7',textbookExercise=dict(sq=short,lq=long),sections=[dict(code='source-u1-exercise-conceptual',heading='Conceptual Questions',paras=paras,blocks=[dict(type='question',number=q['num'],question=q['q'],answerProvidedInSource=False) for q in short]),dict(code='source-u1-exercise-comprehensive',heading='Comprehensive Questions',paras=extended,blocks=[dict(type='question',number=q['num'],question=q['q'],subquestions=q.get('subquestions',[]),answerProvidedInSource=False) for q in long])],comparison='Corrected technology question formerly misread as ecology; eight conceptual and seven comprehensive questions with subparts and instructions structured; no invented textbook solutions'))
render(33)
