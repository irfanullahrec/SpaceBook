"""Unit17 source pass; earlier chapter tails are preserved."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def p(text,urdu,pashto):return dict(text=text,urdu=urdu,pashto=pashto)
REVISIONS=[
('17.0 Introduction','تعارف','پېژندنه',[
p('The body of an animal frequently exposed to variety of stimuli in its daily life.','حیوان کا جسم روزمرہ زندگی میں اکثر مختلف محرکات سے دوچار ہوتا ہے۔','د حیوان بدن په ورځني ژوند کې ډېر ځله له بېلابېلو محرکونو سره مخ کېږي.'),
p('For an appropriate response to a particular stimulus, usually more than one body parts are involved, their activities are coordinated either by nervous system or endocrine system or both.','کسی خاص محرک کے مناسب ردعمل میں عموماً جسم کے ایک سے زیادہ حصے شامل ہوتے ہیں؛ اعصابی، درون افرازی یا دونوں نظام ان کی سرگرمیوں میں ہم آہنگی پیدا کرتے ہیں۔','یوه ځانګړي محرک ته په مناسب غبرګون کې عموماً د بدن له یوې زیاتې برخې برخه اخلي؛ عصبي یا اندوکرین سیسټم یا دواړه یې فعالیتونه همغږي کوي.'),
p('These two types of coordination you also have studied in class 10 to some extent, but in this chapter we are mainly focusing the human nervous system.','آپ جماعت دہم میں ان دونوں اقسام کی ہم آہنگی کچھ پڑھ چکے ہیں، مگر اس باب میں بنیادی توجہ انسانی اعصابی نظام پر ہے۔','تاسو په لسم ټولګي کې د همغږۍ دا دواړه ډولونه تر یوې کچې لوستي، خو په دې څپرکي کې زموږ اصلي تمرکز د انسان پر عصبي سیسټم دی.')],[85]),
('17.1 STEPS INVOLVED IN NERVOUS COORDINATION','اعصابی ہم آہنگی کے مراحل','د عصبي همغږۍ پړاوونه',[
p('Nervous coordination mainly comprises highly specialized cells, called the neurons.','اعصابی ہم آہنگی میں بنیادی طور پر نہایت مخصوص خلیے، نیورون، شامل ہیں۔','عصبي همغږي تر ډېره له ډېرو ځانګړو حجرو، نیورونونو، جوړه ده.'),
p('The function of a neuron is to detect and receive stimuli from different sensory organs (receptors) and then, integrate them to determine the mode of response of the living organism, and then commands for an appropriate response are transmitted to the other organ (effectors).','نیورون مختلف حسی اعضا (رسیپٹرز) سے محرکات معلوم اور وصول کرتا، انہیں یکجا کرکے جاندار کا ردعمل طے کرتا، پھر مناسب ردعمل کی ہدایات دوسرے اعضا (ایفیکٹرز) تک پہنچاتا ہے۔','د نیورون دنده له بېلابېلو حسي غړو (اخیستونکو) محرکونه معلومول او اخیستل، بیا یې د ژوندي موجود د غبرګون د ټاکلو لپاره یوځای کول دي؛ وروسته مناسبې لارښوونې نورو غړو (اغېز کوونکو) ته لېږل کېږي.'),
p('Nervous coordination in higher animals is therefore consists of following steps.','لہٰذا اعلیٰ حیوانوں میں اعصابی ہم آہنگی کے یہ مراحل ہیں۔','نو په لوړو حیواناتو کې عصبي همغږي لاندې پړاوونه لري.'),
p('Reception of stimulus:','محرک کا وصول کرنا:','د محرک اخیستل:'),
p('Processing/analysis of information:','معلومات کی پردازش یا تجزیہ:','د معلوماتو پروسس یا شننه:'),
p('Response to stimulus:','محرک کا ردعمل:','محرک ته غبرګون:')],[85]),
('17.1.1 Reception of stimulus:','محرک کا وصول کرنا','د محرک اخیستل',[
p('Those parts of the body that receive stimuli from internal or external environment are called receptors or transducers.','جسم کے وہ حصے جو اندرونی یا بیرونی ماحول سے محرکات وصول کرتے ہیں رسیپٹرز یا ٹرانسڈیوسرز کہلاتے ہیں۔','د بدن هغه برخې چې له داخلي یا بهرني چاپېریال محرکونه اخلي، اخیستونکي یا ټرانسډیوسرونه بلل کېږي.'),
p('A receptor may be a complete organ or a cell or just neuron endings.','رسیپٹر مکمل عضو، خلیہ یا صرف نیورون کے سرے ہو سکتے ہیں۔','اخیستونکی بشپړ غړی، حجره یا یوازې د نیورون پایونه کېدای شي.'),
p('The information collected by the receptor is transmitted to the central nervous system (CNS) through sensory neurons.','رسیپٹر کی جمع کردہ معلومات حسی نیورونوں سے مرکزی اعصابی نظام (CNS) تک پہنچتی ہیں۔','د اخیستونکي راټول شوي معلومات د حسي نیورونونو له لارې مرکزي عصبي سیسټم (CNS) ته لېږدېږي.'),
p('Classification of receptors:','رسیپٹرز کی درجہ بندی:','د اخیستونکو وېش:'),
p('Receptors are classified into different types on the basis of stimuli.','محرکات کے لحاظ سے رسیپٹرز مختلف اقسام میں تقسیم ہوتے ہیں۔','اخیستونکي د محرکونو له مخې په بېلابېلو ډولونو وېشل کېږي.'),
p('Photoreceptors detect light stimuli.','فوٹورسیپٹرز روشنی کے محرکات معلوم کرتے ہیں۔','فوتواخیستونکي د رڼا محرکونه معلوموي.'),
p('For example rods and cone cells in the retina of eye.','مثلاً آنکھ کے شبکیے کے راڈ اور کون خلیے۔','لکه د سترګې په شبکیه کې راډ او کون حجرې.'),
p('Chemoreceptors detect ions or molecules (chemical).','کیمورسیپٹرز آئن یا کیمیائی سالمے معلوم کرتے ہیں۔','کیمواخیستونکي ایونونه یا کیمیاوي مالیکولونه معلوموي.'),
p('For example receptors found in nasal epithelium for detection of smell (olfaction) and those, found in tongue for taste (gustation).','مثلاً بو محسوس کرنے کے لیے ناک کی اپی تھیلیم اور ذائقے کے لیے زبان کے رسیپٹرز۔','لکه د بوی د معلومولو لپاره د پوزې په اپیتیلیم او د خوند لپاره په ژبه کې اخیستونکي.'),
p('Chemoreceptors are also found in hypothalamus, called osmoreceptors that detect changes in osmotic pressure of blood.','ہائپوتھیلمس میں بھی کیمورسیپٹرز ہیں، جنہیں اوسمورسیپٹرز کہتے ہیں؛ یہ خون کے اوسموسی دباؤ کی تبدیلی معلوم کرتے ہیں۔','په هایپوتالاموس کې هم کیمواخیستونکي شته، چې اوسمواخیستونکي بلل کېږي او د وینې د اوسموسي فشار بدلون معلوموي.'),
p("Mechanoreceptors detect changes in pressure, position, or acceleration; include receptors for touch (Meissner’s corpuscles in skin), stretch or pressure (Pacinian’s corpuscle in skin & baroreceptor in the wall of blood vessels), hearing and equilibrium (ear).",'میکانورسیپٹرز دباؤ، مقام یا تعجیل کی تبدیلی معلوم کرتے ہیں؛ ان میں لمس (جلد کے مائس نر جسمچے)، کھنچاؤ یا دباؤ (جلد کے پیسینین جسمچے اور خون کی نالیوں کی دیوار کے بیورورسیپٹرز)، سماعت اور توازن (کان) کے رسیپٹرز شامل ہیں۔','میکانواخیستونکي د فشار، موقعیت یا تعجیل بدلونونه معلوموي؛ پکې د لمس اخیستونکي (په پوستکي کې د مایسنر جسمونه)، د غځېدو یا فشار اخیستونکي (په پوستکي کې د پاسیني جسمونه او د رګونو په دېوال کې بارواخیستونکي)، د اورېدو او توازن اخیستونکي (غوږ) شامل دي.'),
p('Thermoreceptors detect temperatures stimuli.','تھرمورسیپٹرز درجۂ حرارت کے محرکات معلوم کرتے ہیں۔','حرارتي اخیستونکي د تودوخې محرکونه معلوموي.'),
p('They are mostly found in the skin.','یہ زیادہ تر جلد میں ہوتے ہیں۔','دا تر ډېره په پوستکي کې وي.'),
p('Nociceptors detect pain.','نوسی سیپٹرز درد معلوم کرتے ہیں۔','نوسیسېپټرونه درد معلوموي.')],[85,86]),
('17.1.2 Processing/analysis of information:','معلومات کی پردازش اور تجزیہ','د معلوماتو پروسس او شننه',[
p('Sensory inputs from various receptors are received by CNS (brain & spinal cord) that act as coordinating center of the body.','مختلف رسیپٹرز سے حسی معلومات CNS (دماغ اور حرام مغز) وصول کرتا ہے، جو جسم کا مرکزِ ہم آہنگی ہے۔','له بېلابېلو اخیستونکو حسي معلومات CNS (مغز او شوکي نخاع) اخلي، چې د بدن د همغږۍ مرکز دی.'),
p('This collected information is further processed/analyzed for an appropriate response by special type of neurons called associative or intermediate neurons.','مناسب ردعمل کے لیے ان معلومات کا مزید تجزیہ خاص رابط یا درمیانی نیورون کرتے ہیں۔','دا راټول شوي معلومات د مناسب غبرګون لپاره د ځانګړو رابطو یا منځنیو نیورونونو له خوا نور پروسس او شنل کېږي.')],[86]),
('17.1.3 Response to stimulus:','محرک کا ردعمل','محرک ته غبرګون',[
p('Those parts of the body which produce an appropriate response are called effectors (muscles and glands).','جسم کے وہ حصے جو مناسب ردعمل پیدا کرتے ہیں ایفیکٹرز (عضلات اور غدود) کہلاتے ہیں۔','د بدن هغه برخې چې مناسب غبرګون جوړوي اغېز کوونکي (عضلې او غدې) بلل کېږي.'),
p('An effector organ, on receiving signal from CNS by motor neuron, provides an appropriate response either by producing movements (muscles) or secretions (glands).','ایفیکٹر عضو حرکی نیورون سے CNS کا اشارہ پا کر حرکت (عضلات) یا رطوبتوں (غدود) کے ذریعے مناسب ردعمل دیتا ہے۔','اغېز کوونکی غړی د حرکي نیورون له لارې له CNS څخه نښه اخلي او د حرکت (عضلې) یا ترشحاتو (غدې) په جوړولو مناسب غبرګون ورکوي.')],[86]),
]
from biology12_neurons import REVISIONS as NEURONS
REVISIONS.extend(NEURONS)
from biology12_reflex import REVISIONS as REFLEX
REVISIONS.extend(REFLEX)
from biology12_resting_potential import REVISIONS as RESTING
REVISIONS.extend(RESTING)
from biology12_action_potential import REVISIONS as ACTION
REVISIONS.extend(ACTION)
from biology12_synapse import REVISIONS as SYNAPSE
REVISIONS.extend(SYNAPSE)
from biology12_nervous_system import REVISIONS as SYSTEM
REVISIONS.extend(SYSTEM)
from biology12_brain import REVISIONS as BRAIN
REVISIONS.extend(BRAIN)
from biology12_peripheral import REVISIONS as PERIPHERAL
REVISIONS.extend(PERIPHERAL)
from biology12_drugs import REVISIONS as DRUGS
REVISIONS.extend(DRUGS)
from biology12_drugs_more import REVISIONS as MORE_DRUGS
REVISIONS.extend(MORE_DRUGS)

def main():
 target=ROOT/'js/biology_12_data.js'
 marker='// BEGIN SOURCE-LED BIOLOGY12 UNIT17 REVISION'
 text=target.read_text(encoding='utf-8').split(marker)[0]+'\n'+marker+'\n'
 text+='BIOLOGY_12_DATA[3].sections=BIOLOGY_12_DATA[3].sections.filter(s=>s.heading!=="17.1.3 Response to stimulus: Receptors present in the skin.");\n'
 for heading,ur,ps,paras,pages in REVISIONS:
  payload=dict(heading=heading,title=heading,headingUrdu=ur,urduTitle=ur,headingPashto=ps,paras=paras,text='\n\n'.join(x['text'] for x in paras),urdu='\n\n'.join(x['urdu'] for x in paras),pashto='\n\n'.join(x['pashto'] for x in paras),sourceReferences=[dict(printedPage=n,jpg=f'Biology Book for 12 class KPTBB_page_{n+(4 if n<=103 else 1):03}.jpg',status='source transcribed') for n in pages],translationStatus='aligned Urdu/Pashto supplied; manual review pending')
  text+='{const incoming='+json.dumps(payload,ensure_ascii=False)+';const sections=BIOLOGY_12_DATA[3].sections;const current=sections.find(s=>s.heading===incoming.heading);if(current)Object.assign(current,incoming);else{const order=h=>(h.match(/^\\d+(?:\\.\\d+)*/)||[""])[0].split(".").map(n=>n.padStart(4,"0")).join(".");const next=/^\\d/.test(incoming.heading)?sections.findIndex(s=>order(s.heading)>order(incoming.heading)):-1;sections.splice(next<0?sections.length:next,0,incoming);}}\n'
 from PIL import Image
 for jpg,rect,name,caption,append in [(89,(499,565,681,702),'figure17-1-photoreceptors','Fig:17.1 Photoreceptors present in the eye.',False),(90,(445,52,659,281),'figure17-2-skin-receptors','Fig:17.2 Receptors present in the skin.',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==="17.1.1 Reception of stimulus:")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for heading,jpg,rect,name,caption,append in [('17.2 NEURONS',91,(132,39,664,303),'figure17-3-neuron','Fig:17.3 Structure of a typical neuron.',False),('17.2 NEURONS',91,(364,483,666,785),'figure17-4-neuron-types','Fig:17.4 Basic neuron types',True),('17.2.1 Sensory Neuron:',92,(153,237,573,613),'figure17-5-functional-neurons','Fig:17.5 Three types of neurons based upon functions.',False)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+')'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for heading,jpg,rect,name,caption in [('17.2.4 Reflex Arc',93,(78,358,678,708),'figure17-6-reflex-arc','Fig:17.6 The pathway of nerve impulse during reflex action makes a reflex arc.'),('17.3 NERVE IMPULSE',94,(144,600,609,786),'figure17-7-membrane-potential','Fig:17.7 Negative and positive ion act as charges and the charge separating barrier is neuron membrane.')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
 asset=ROOT/'assets/biology12/figure17-8-resting-potential.jpg'
 if not asset.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_095.jpg').crop((141,431,679,788)).save(asset)
 text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==="17.3.2 Distribution and active movement of Na⁺ and K⁺ ions:").diagramSvg=`<figure><img src="assets/biology12/figure17-8-resting-potential.jpg" alt="Sodium-potassium pump and potassium channels with printed ion concentrations" style="max-width:100%;height:auto;"><figcaption>Fig:17.8 Resting membrane potential.</figcaption></figure>`;\n'
 for heading,jpg,rect,name,caption in [('17.3.5 Development of active membrane potential:',96,(129,525,591,790),'figure17-9-active-potential','Fig:17.9 Active membrane potential'),('17.3.6 Threshold stimulus:',97,(108,162,612,470),'figure17-10-action-potential','Fig:17.10 Action Potential in a Neuron.'),('17.3.9 Types of Nerve Impulse',98,(389,236,674,359),'figure17-11-myelinated-neuron','Fig:17.11 Myelinated neuron')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
 figures=[]
 for jpg,rect,name,caption in [(99,(387,443,672,727),'figure17-12-synapse','Fig:17.12 Synapse'),(100,(112,325,604,632),'figure17-13-neurotransmitters','Fig:17.13 Neurotransmitters at synapse.')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  figures.append(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
 text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==="17.4.3 Transmission of nerve impulse across synapse:").diagramSvg='+json.dumps(''.join(figures))+';\n'
 for heading,jpg,rect,name,caption in [('17.5.1 Divisions of human nervous system:',101,(84,262,682,659),'figure17-14-nervous-system','Fig:17.14 Main division of nervous system'),('17.5.3 Protection of brain and spinal cord:',102,(382,43,653,268),'figure17-15-brain-protection','Fig:17.15 Side way view of human brain.')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
 figures=[]
 for jpg,rect,name,caption in [(103,(90,376,637,601),'figure17-16-limbic-reticular','Fig:17.16 (a) The limbic system extends through several brain regions. (b) The reticular formation.'),(104,(359,68,661,332),'figure17-17-brain-section','Fig:17.17 Cross Section of human brain.'),(104,(94,413,346,650),'figure17-18-brain-lobes','Fig:17.18 Different lobes of brain.'),(104,(349,412,665,649),'figure17-19-sensory-regions','Fig:17.19 Location of various sensations perceived by different parts of brain.')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  figures.append(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
 text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==="17.5.4 Structure and function of brain:").diagramSvg='+json.dumps(''.join(figures))+';\n'
 for heading,jpg,rect,name,caption,append in [('17.5.4 Spinal Cord',105,(134,249,653,508),'figure17-20-spinal-cord','Fig:17.20 Spinal cord',False),('17.5.4 Spinal Cord',106,(188,50,570,343),'figure17-21-disc','Fig:17.21 Location of intervertebral disk in the spinal cord.',True),('17.5.4 Peripheral Nervous System:',107,(405,37,655,451),'figure17-22-spinal-nerves','Fig:17.22 Spinal nerves.',False)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+')'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for heading,jpg,rect,name,caption in [('17.7.1 Heroine:',108,(660,535,903,731),'figure17-26-poppy','Fig:17.26 Poppy plant'),('17.7.2 Cannabis',109,(634,29,880,220),'figure17-27-cannabis','Fig:17.27 Cannabis sativa')]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  text+='BIOLOGY_12_DATA[3].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')+';\n'
 text+='BIOLOGY_12_DATA[3].sourceStatus="in_progress";\n'
 import time
 for attempt in range(4):
  try:target.write_text(text,encoding='utf-8',newline='\n');break
  except OSError as error:
   if error.errno!=22 or attempt==3:raise
   time.sleep(0.5)
 ledger_path=ROOT/'docs/source-verification/biology12.json'
 ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
 ledger['currentUnit']=17
 ledger['nextSource']='Biology Book for 12 class KPTBB_page_111.jpg'
 ledger['unit17Scope']='Printed85–103 plus107–109 through nicotine, alcohol and inhalants transcribed with Urdu/Pashto; figures17.1–17.22 and17.26–17.27. Printed104–106 and figures17.23–17.25 pending source recovery. Original medical claims retained as textbook text, not independently updated advice. No completed-work recheck.'
 ledger['unit17SourceGap']={'printedPages':[104,105,106],'evidence':'JPG107 ends printed103; JPG108 and full-PDF physical108 show drug-effects page107. No missing content invented.'}
 for page in ledger['pages']:
  if 89<=int(page['jpg'][-7:-4])<=110:page['status']='source_transcribed'
  elif page['jpg'].endswith('088.jpg'):page['status']='source_viewed'
 ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Unit17 source lessons added.')
if __name__=='__main__':main()
