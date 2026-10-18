"""Source-led descending Biology pass. Original Books files stay read-only."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def para(en,ur,ps):return {'text':en,'urdu':ur,'pashto':ps}
INTRO=[
para('Energy is the most important requirement of life.','توانائی زندگی کی سب سے اہم ضرورت ہے۔','انرژي د ژوند تر ټولو مهمه اړتیا ده.'),
para('All systems require energy to work.','تمام نظاموں کو کام کرنے کے لیے توانائی درکار ہوتی ہے۔','ټول سیسټمونه د کار کولو لپاره انرژۍ ته اړتیا لري.'),
para('The various processes carried out by body, such as movement, growth and reproduction, all require the expenditure of energy.','جسم کے مختلف عمل، مثلاً حرکت، نشوونما اور تولید، سب توانائی کے استعمال کے محتاج ہیں۔','د بدن بېلابېلې پروسې، لکه حرکت، وده او تکثر، ټولې د انرژۍ لګولو ته اړتیا لري.'),
para('In animals this energy can be obtained only from the food they eat.','جانوروں میں یہ توانائی صرف ان کی کھائی ہوئی غذا سے حاصل ہو سکتی ہے۔','په حیواناتو کې دا انرژي یوازې له هغه خوراک څخه ترلاسه کېدای شي چې هغوی یې خوري.'),
para('In the processes of cellular respiration this food energy is made available for the body activities.','خلوی تنفس کے عمل میں غذا کی یہ توانائی جسمانی سرگرمیوں کے لیے دستیاب ہوتی ہے۔','د حجروي تنفس په پروسو کې د خوراک دا انرژي د بدن د فعالیتونو لپاره چمتو کېږي.'),
para('Aerobic respiration involves the use of oxygen and the production of carbon dioxide.','ہوائی تنفس میں آکسیجن استعمال ہوتی ہے اور کاربن ڈائی آکسائیڈ پیدا ہوتی ہے۔','په هوازي تنفس کې اکسیجن کارول کېږي او کاربن ډای اکسایډ تولیدېږي.'),
para("Oxygen enters into animal's body from air or water surrounding it.",'آکسیجن جانور کے اردگرد کی ہوا یا پانی سے اس کے جسم میں داخل ہوتی ہے۔','اکسیجن د حیوان شاوخوا له هوا یا اوبو څخه د هغه بدن ته ننوځي.'),
para('In the less complex animals the oxygen is absorbed over the entire exposed surface of the body.','کم پیچیدہ جانوروں میں جسم کی پوری کھلی سطح سے آکسیجن جذب ہوتی ہے۔','په لږ پېچلو حیواناتو کې اکسیجن د بدن له ټولې څرګندې سطحې جذبېږي.'),
para('In higher animals, however, there are special respiratory organs such as gills or lungs.','تاہم اعلیٰ جانوروں میں گلپھڑوں یا پھیپھڑوں جیسے مخصوص تنفسی اعضا موجود ہوتے ہیں۔','خو په لوړو حیواناتو کې ځانګړي تنفسي غړي، لکه ګېلې یا سږي، شته.'),
para('Excess carbon dioxide is usually eliminated from the same organ.','اضافی کاربن ڈائی آکسائیڈ عموماً اسی عضو سے خارج کی جاتی ہے۔','اضافي کاربن ډای اکسایډ عموماً له هماغه غړي څخه ایستل کېږي.')]
SURFACES=[
para('The area where gaseous exchange with the environment actually takes place is called the respiratory surface.','وہ حصہ جہاں ماحول کے ساتھ گیسوں کا تبادلہ حقیقتاً ہوتا ہے، تنفسی سطح کہلاتا ہے۔','هغه برخه چې له چاپېریال سره د ګازونو تبادله په کې ترسره کېږي، تنفسي سطحه بلل کېږي.'),
para('Gaseous exchange takes place in all organisms by the physical process of diffusion.','تمام جانداروں میں گیسوں کا تبادلہ انتشار کے طبعی عمل سے ہوتا ہے۔','په ټولو ژوندیو موجوداتو کې د ګازونو تبادله د خپرېدو د فزیکي پروسې له لارې کېږي.'),
para('For effective diffusion the respiratory surface must have the following properties.','مؤثر انتشار کے لیے تنفسی سطح میں درج ذیل خصوصیات ہونی چاہییں۔','د اغېزمن خپرېدو لپاره تنفسي سطحه باید لاندې ځانګړنې ولري.'),
para('• It must be permeable, so that gases can pass through it.','• یہ نفوذ پذیر ہونی چاہیے تاکہ گیسیں اس میں سے گزر سکیں۔','• باید د تېرېدو وړ وي، څو ګازونه ترې تېر شي.'),
para('• It must be thin for efficient diffusion, because diffusion is only efficient over distance of 1 mm or less.','• مؤثر انتشار کے لیے یہ پتلی ہونی چاہیے، کیونکہ انتشار صرف 1 ملی میٹر یا اس سے کم فاصلے پر مؤثر ہوتا ہے۔','• د اغېزمن خپرېدو لپاره باید نرۍ وي، ځکه خپرېدل یوازې د 1 ملي متر یا تر دې لږ واټن کې اغېزمن وي.'),
para("• It should possess a large surface area so that sufficient amounts of gases are able to be exchanged according to the organism's need.",'• اس کا سطحی رقبہ بڑا ہونا چاہیے تاکہ جاندار کی ضرورت کے مطابق کافی مقدار میں گیسوں کا تبادلہ ہو سکے۔','• باید لویه سطحي ساحه ولري، څو د ژوندي موجود د اړتیا سره سم په کافي اندازه ګازونه تبادله شي.'),
para('• It should possess a good blood supply.','• اسے خون کی اچھی فراہمی ہونی چاہیے۔','• باید د وینې ښه رسونه ولري.'),
para('• There should be a good ventilation mechanism to maintain a steep diffusion gradient across the respiratory surface.','• تنفسی سطح کے دونوں طرف انتشار کا تیز ارتکازی فرق برقرار رکھنے کے لیے ہوا کی آمدورفت کا اچھا نظام ہونا چاہیے۔','• د تنفسي سطحې په دواړو خواوو کې د خپرېدو د لوی غلظتي توپیر د ساتلو لپاره باید د هوا د تګ راتګ ښه میکانیزم وي.')]
SYSTEM=[para('Respiratory system provides the fundamental ability to breath.','تنفسی نظام سانس لینے کی بنیادی صلاحیت فراہم کرتا ہے۔','تنفسي سیسټم د ساه اخیستلو بنسټیزه وړتیا برابروي.'),para('This system consists of nose and nasal cavities, pharynx, larynx, trachea, bronchi, bronchioles, and alveoli in the lungs.','یہ نظام ناک، ناک کی گہاوں، حلق، حنجرے، ہوا کی نالی، شعبوں، چھوٹے شعبوں اور پھیپھڑوں کے ہوائی تھیلوں پر مشتمل ہے۔','دا سیسټم له پوزې او د پوزې له جوفونو، حلق، حنجرې، د هوا نل، برانشونو، برانشیولونو او د سږو له الویولونو جوړ دی.')]
REVISIONS=[('14.0 Introduction','تعارف','پېژندنه',INTRO,[2]),('14.1 PROPERTIES OF RESPIRATORY SURFACES','تنفسی سطحوں کی خصوصیات','د تنفسي سطحو ځانګړنې',SURFACES,[2]),('14.2 HUMAN RESPIRATORY SYSTEM','انسان کا تنفسی نظام','د انسان تنفسي سیسټم',SYSTEM,[2])]
NOSE=[
para('The nose is only externally visible part of the respiratory system.','ناک تنفسی نظام کا واحد حصہ ہے جو باہر سے نظر آتا ہے۔','پوزه د تنفسي سیسټم یوازینۍ برخه ده چې له بهر څخه ښکاري.'),
para('The structure of a human nose is composed of bones, cartilage and fibro fatty tissues.','انسان کی ناک کی ساخت ہڈیوں، غضروف اور ریشے دار چربی کے بافتوں سے بنی ہے۔','د انسان د پوزې جوړښت له هډوکو، غضروف او فایبري شحمي نسجونو جوړ دی.'),
para('The external feature of a nose depends upon the ethmoid bone and the cartilages.','ناک کی بیرونی شکل ایتھموئڈ ہڈی اور غضروفوں پر منحصر ہے۔','د پوزې بهرنۍ بڼه په اېتمویډ هډوکي او غضروفونو پورې اړه لري.'),
para('Hairs are present inside the nostrils that help in the filtration of air.','نتھنوں کے اندر بال موجود ہوتے ہیں جو ہوا چھاننے میں مدد دیتے ہیں۔','د پوزې د سوریو دننه وېښتان شته چې د هوا په چاڼولو کې مرسته کوي.'),
para('Hence, nose hair serve as a defense mechanism against the harmful pathogens and solid particulate matter present in the air.','اس لیے ناک کے بال ہوا میں موجود نقصان دہ بیماری پیدا کرنے والے عوامل اور ٹھوس ذرات کے خلاف دفاع کرتے ہیں۔','نو د پوزې وېښتان په هوا کې د زیانمنو ناروغي جوړوونکو او جامدو ذرو پر وړاندې دفاع کوي.'),
para('Both the nostrils and nasal cavities are lined by mucous membranes along with cilia.','نتھنوں اور ناک کی گہاوں کی اندرونی سطح پر مخاطی جھلیاں اور سیلیا موجود ہوتے ہیں۔','د پوزې سوري او جوفونه له دننه په مخاطي پردو او سیلیا پوښل شوي دي.'),
para('The mucous membrane secretes a sticky substance called mucus.','مخاطی جھلی ایک چپچپا مادہ خارج کرتی ہے جسے میوکس کہتے ہیں۔','مخاطي پرده یوه سریښناکه ماده ترشح کوي چې میوکس بلل کېږي.'),
para('The mucus and cilia filter the air and prevent the entry of foreign particles such as microorganisms, dust and particulate matter inside the respiratory system.','میوکس اور سیلیا ہوا چھانتے ہیں اور خرد جانداروں، گرد اور دوسرے بیرونی ذرات کو تنفسی نظام میں داخل ہونے سے روکتے ہیں۔','میوکس او سیلیا هوا چاڼوي او د کوچنیو ژوندیو موجوداتو، دوړو او نورو بهرنیو ذرو د تنفسي سیسټم دننه د ننوتلو مخه نیسي.'),
para('The mucus also helps in moistening the air.','میوکس ہوا کو نم کرنے میں بھی مدد دیتا ہے۔','میوکس د هوا په لندولو کې هم مرسته کوي.'),
para('Cilia move the trapped substances to the pharynx for their removal.','سیلیا پھنسے ہوئے مادوں کو خارج کرنے کے لیے حلق کی طرف منتقل کرتے ہیں۔','سیلیا بندې شوې مادې د ایستلو لپاره حلق ته لېږدوي.'),
para('Underneath the mucous membrane, there are blood capillaries that help to warm the air to about 30 °C, depending upon the external temperature.','مخاطی جھلی کے نیچے خون کی باریک نالیاں ہوتی ہیں جو بیرونی درجۂ حرارت کے مطابق ہوا کو تقریباً 30 °C تک گرم کرنے میں مدد دیتی ہیں۔','د مخاطي پردې لاندې د وینې نرۍ رګونه شته چې د بهرني تودوخې سره سم هوا نږدې تر 30 °C پورې تودوي.')]
PHARYNX=[
para('Pharynx is cone-shaped passageway leading from the oral and nasal cavities to the oesophagus and larynx.','حلق مخروطی شکل کی گزرگاہ ہے جو منہ اور ناک کی گہاوں سے غذائی نالی اور حنجرے کی طرف جاتی ہے۔','حلق مخروط ته ورته لاره ده چې د خولې او پوزې له جوفونو څخه د خوړو نل او حنجرې ته ځي.'),
para('The pharynx is part of both the digestive and respiratory systems.','حلق ہاضمے اور تنفس دونوں نظاموں کا حصہ ہے۔','حلق د هاضمې او تنفس دواړو سیسټمونو برخه ده.'),
para('The interconnection of the oral and nasal regions is extremely beneficial in humans.','انسانوں میں منہ اور ناک کے حصوں کا باہمی اتصال بہت مفید ہے۔','په انسانانو کې د خولې او پوزې د برخو خپلمنځي اتصال ډېر ګټور دی.'),
para('It allows them to breathe through either the nose or the mouth and, when medically necessary, allows food to be passed to the esophagus by nasal tubes.','یہ انہیں ناک یا منہ سے سانس لینے دیتا ہے اور طبی ضرورت کے وقت ناک کی نالیوں کے ذریعے غذا کو غذائی نالی تک پہنچانے کی سہولت دیتا ہے۔','دا هغوی ته د پوزې یا خولې له لارې د ساه اخیستلو اجازه ورکوي او د طبي اړتیا پر مهال د پوزې د نلونو له لارې د خوړو نل ته د خوراک د تېرولو اسانتیا برابروي.')]
REVISIONS.extend([('14.2.1 Nose','ناک','پوزه',NOSE,[2,3]),('14.2.2 Pharynx','حلق','حلق',PHARYNX,[3])])
from biology12_airways import REVISIONS as AIRWAYS
REVISIONS.extend(AIRWAYS)
from biology12_lungs import REVISIONS as LUNG_REVISION
REVISIONS.extend(LUNG_REVISION)
from biology12_breathing import REVISIONS as BREATHING
REVISIONS.extend(BREATHING)
from biology12_gas_transport import REVISIONS as GAS_TRANSPORT
REVISIONS.extend(GAS_TRANSPORT)
from biology12_carbon_dioxide import REVISIONS as CARBON_TRANSPORT
REVISIONS.extend(CARBON_TRANSPORT)
from biology12_pigments import REVISIONS as PIGMENT_REVISION
REVISIONS.extend(PIGMENT_REVISION)
from biology12_sinusitis import REVISIONS as SINUSITIS_REVISION
REVISIONS.extend(SINUSITIS_REVISION)
from biology12_otitis import REVISIONS as OTITIS_REVISION
REVISIONS.extend(OTITIS_REVISION)
from biology12_pneumonia_tb import REVISIONS as PNEUMONIA_TB
REVISIONS.extend(PNEUMONIA_TB)
from biology12_lung_disorders import REVISIONS as LUNG_DISORDERS
REVISIONS.extend(LUNG_DISORDERS)
from biology12_unit14_close import REVISIONS as UNIT14_CLOSE, SUMMARY
from biology12_unit14_exercise import EXERCISE
REVISIONS.extend(UNIT14_CLOSE)
target=ROOT/'js/biology_12_data.js'
marker='// BEGIN SOURCE-LED BIOLOGY12 REVISION'
text=target.read_text(encoding='utf-8').split(marker)[0]
text=text.replace('// Complete Class 12 Biology Textbook Dataset (KPTBB)','// Class 12 Biology textbook dataset — source reconciliation in progress').replace('// Extracted verbatim from official textbook DOCX, OCR noise cleaned','// Draft companion text with scanned-source revisions below; no whole-book completion claim.')
text+='\n'+marker+'\n'
for heading,ur,ps,paras,numbers in REVISIONS:
 payload={'heading':heading,'title':heading,'headingUrdu':ur,'urduTitle':ur,'headingPashto':ps,'text':'\n\n'.join(p['text'] for p in paras),'paras':paras,'urdu':'\n\n'.join(p['urdu'] for p in paras),'pashto':'\n\n'.join(p['pashto'] for p in paras),'sourceReferences':[{'printedPage':n,'jpg':f'Biology Book for 12 class KPTBB_page_{n+4:03}.jpg','status':'source transcribed'} for n in numbers],'translationStatus':'aligned Urdu and Pashto sentences supplied; manual review pending'}
 text+='{const reviewedBioSection='+json.dumps(payload,ensure_ascii=False)+';const sections=BIOLOGY_12_DATA[0].sections;const current=sections.find(s=>s.heading===reviewedBioSection.heading);if(current)Object.assign(current,reviewedBioSection);else{const order=h=>(h.match(/^\\d+(?:\\.\\d+)*/)||[""])[0].split(".").map(n=>n.padStart(4,"0")).join(".");const next=/^\\d/.test(reviewedBioSection.heading)?sections.findIndex(s=>order(s.heading)>order(reviewedBioSection.heading)):-1;sections.splice(next<0?sections.length:next,0,reviewedBioSection);}}\n'
from PIL import Image
assets=ROOT/'assets/biology12';assets.mkdir(exist_ok=True)
Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_007.jpg').crop((210,60,570,330)).save(assets/'figure14-1-nasal-passage.jpg')
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.2.1 Nose").diagramSvg=`<figure><img src="assets/biology12/figure14-1-nasal-passage.jpg" alt="Nasal cavity, nostril, mouth, pharynx and larynx labelled in the source diagram" style="max-width:100%;height:auto;"><figcaption>Fig:14.1 Nasal passage through face</figcaption></figure>`;\n'
Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_008.jpg').crop((410,53,659,269)).save(assets/'figure14-2-larynx.jpg')
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.2.3 Larynx").diagramSvg=`<figure><img src="assets/biology12/figure14-2-larynx.jpg" alt="Source larynx diagram with epiglottis, supraglottis, vocal cord, glottis, subglottis, oesophagus and trachea" style="max-width:100%;height:auto;"><figcaption>Fig: 14.2 Larynx is the upper part of the respiratory system.</figcaption></figure>`;\n'
text+='BIOLOGY_12_DATA[0].sourceStatus="in_progress";\n'
text+='BIOLOGY_12_DATA[0].unreviewedExercise=BIOLOGY_12_DATA[0].exercise;BIOLOGY_12_DATA[0].exercise='+json.dumps(EXERCISE,ensure_ascii=False)+';BIOLOGY_12_DATA[0].unreviewedSloBank=BIOLOGY_12_DATA[0].sloBank;BIOLOGY_12_DATA[0].sloBank=BIOLOGY_12_DATA[0].exercise;\n'
for key,lang in [('englishSummary','text'),('urduSummary','urdu'),('pashtoSummary','pashto')]:text+='BIOLOGY_12_DATA[0]['+json.dumps(key)+']='+json.dumps('\n\n'.join(item[lang] for item in SUMMARY),ensure_ascii=False)+';\n'
for heading,jpg,rectangle,name,caption in [('14.2.6 Bronchioles',9,(175,177,578,470),'figure14-3-airways','Fig:14.3 Branching of trachea leads to a network of airway passages.'),('14.2.7 Alveoli',10,(135,175,612,445),'figure14-4-alveoli','Fig:14.4 Capillaries form a network over the surface of alveoli.')]:
 Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rectangle).save(assets/(name+'.jpg'))
 text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.2.8 Lungs").callouts=[{title:"SpaceBook activity answer — air pathway",content:"Nostrils → nasal cavities → pharynx → larynx → trachea → bronchi → bronchioles → alveoli. Exhaled air travels back along the same route; the mouth provides an alternative entry to the pharynx."}];\n'
Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_012.jpg').crop((86,548,590,799)).save(assets/'figure14-5-breathing.jpg')
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.4.1 Involuntary control").diagramSvg=`<figure><img src="assets/biology12/figure14-5-breathing.jpg" alt="Source inhalation and exhalation diagram showing ribs, sternum, lungs and diaphragm" style="max-width:100%;height:auto;"><figcaption>Fig:14.5 Inhalation and exhalation mechanism.</figcaption></figure>`;\n'
oxygen_figures=[]
for jpg,rect,name,caption in [(13,(426,625,704,814),'figure14-6-haemoglobin','Fig: 14.6 Haemoglobin in red blood cells carry oxygen in the blood.'),(14,(49,204,634,480),'figure14-7-rest','Fig: 14.7 — Oxygen release in resting tissues'),(15,(98,55,663,329),'figure14-8-exercise','Fig: 14.8 — Oxygen release in exercising tissues')]:
 Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(assets/(name+'.jpg'))
 oxygen_figures.append(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.5.1 Transport of oxygen in blood:").diagramSvg='+json.dumps(''.join(oxygen_figures))+';\n'
Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_016.jpg').crop((126,438,671,800)).save(assets/'figure14-9-carbon-dioxide.jpg')
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.5.2 Transport of Carbon dioxide:").diagramSvg=`<figure><img src="assets/biology12/figure14-9-carbon-dioxide.jpg" alt="Source tissue and alveolar capillary diagram of bicarbonate formation and chloride shift" style="max-width:100%;height:auto;"><figcaption>Fig: 14.9 Mechanism of transport of carbondioxide.</figcaption></figure>`;\n'
text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.5.2 Transport of Carbon dioxide:").callouts=[{title:"SpaceBook answers — blood colour questions",content:"Haemoglobin gives human blood its red colour. Oxygenated blood is brighter red; deoxygenated venous blood is darker red. Blue in circulation diagrams is a drawing convention."}];\n'
for heading,jpg,rect,name,caption in [('14.6.1 Haemoglobin:',18,(333,415,676,828),'figure14-10-haeme','Fig: 14.10 Chemical structure of haeme group is haemoglobin.'),('14.6.2 Myoglobin',19,(423,70,593,180),'figure14-11-myoglobin','Fig:14.11 Myoglobin')]:
 Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(assets/(name+'.jpg'))
 text+='BIOLOGY_12_DATA[0].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
target.write_text(text,encoding='utf-8',newline='\n')
sinus_figure=assets/'figure14-12-sinusitis.jpg'
if not sinus_figure.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_019.jpg').crop((369,578,659,805)).save(sinus_figure)
with target.open('a',encoding='utf-8') as output:
 output.write('BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.7.1 Sinusitis:").diagramSvg=`<figure><img src="assets/biology12/figure14-12-sinusitis.jpg" alt="Source sinusitis diagram with eye, nose and throat symptom labels" style="max-width:100%;height:auto;"><figcaption>Fig:14.12 Some of the symptoms of sinusitis</figcaption></figure>`;\n')
 for jpg,rect,name,caption in [(20,(236,388,580,618),'figure14-13-ear','Fig:14.13 Internal structure of ear showing region of middle ear.'),(21,(366,169,559,328),'otoscope-information','Otoscope, ear canal and eardrum — source information-box diagram')]:
  asset=assets/(name+'.jpg')
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  output.write('BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.7.2 Otitis Media").diagramSvg=(BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.7.2 Otitis Media").diagramSvg||"")+'+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n')
jpgs=sorted((ROOT.parent/'Books/12th/12th Biology/JPG').glob('*.jpg'))
pneumonia_figure=assets/'figure14-14-pneumonia.jpg'
if not pneumonia_figure.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_022.jpg').crop((334,480,677,774)).save(pneumonia_figure)
with target.open('a',encoding='utf-8') as output:
 output.write('BIOLOGY_12_DATA[0].sections.find(s=>s.heading==="14.7.3 Pneumonia").diagramSvg=`<figure><img src="assets/biology12/figure14-14-pneumonia.jpg" alt="Source normal and pneumonia air-sac comparison with fluid-filled alveoli" style="max-width:100%;height:auto;"><figcaption>Fig:14.14 In pneumonia body is unable to get proper amount of oxygen due to Fluid in the air sacs.</figcaption></figure>`;\n')
 for heading,jpg,rect,name,caption in [('14.7.4 Tuberculosis',24,(130,43,607,364),'figure14-15-tuberculosis','Fig:14.15 Steps in the primary tuberculosis infection.'),('14.8 Disorders of Lungs',25,(151,110,615,400),'figure14-16-emphysema','Fig:4.16 Emphysema results in damaging the bronchiole and alveoli.'),('14.8.2 Lung cancer',26,(209,130,514,416),'figure14-17-lung-cancer','Fig:4.17 Tumor in the lungs can develop at any place causing lung cancer.')]:
  asset=assets/(name+'.jpg')
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  output.write('BIOLOGY_12_DATA[0].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n')
ledger={'class':12,'subject':'Biology','direction':'12 to 1','status':'in_progress','sourceCount':len(jpgs),'currentUnit':15,'nextSource':'Biology Book for 12 class KPTBB_page_033.jpg','scope':'Unit14 source text through printed28 represented with 17 key points, ten native MCQs, four short/four long progressive answers, five connections and five source skills. Urdu/Pashto lesson translations supplied; full exercise/word/audio coverage remains pending. Frontmatter and chapter opener pending. Page23 skill final noun indistinct; third-party MDCAT logo excluded. No completed-work recheck.','pages':[{'jpg':p.name,'status':'source_transcribed' if 6<=int(p.stem[-3:])<=32 and int(p.stem[-3:])!=27 else 'partial_source_legibility' if p.name.endswith('027.jpg') else 'source_viewed' if p.name.endswith('005.jpg') else 'pending'} for p in jpgs]}
ledger['sourceDefects']=['Printed page23 X-ray comparison final noun is indistinct; exact activity crop pending.','No X-ray film pair accompanies the comparison activity.','Source uses carboxyhaemoglobin in carbon-dioxide overview/key points, but carbaminohaemoglobin in its subsection.','Source puts carbonic anhydrase over the oxygen-binding arrow. Original retained; learning answers distinguish carbon-dioxide chemistry.','Figure numbers on21–22 are printed4.16/4.17.']
(ROOT/'docs/source-verification/biology12.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Class 12 Biology started: source-aligned Respiration introduction, surface properties and system opening with Urdu/Pashto translations added.')
