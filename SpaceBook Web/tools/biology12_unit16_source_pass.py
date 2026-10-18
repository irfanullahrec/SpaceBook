"""Unit16 incremental source pass; preserves Unit14/15 generated content."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def p(text,urdu,pashto):return dict(text=text,urdu=urdu,pashto=pashto)
REVISIONS=[
('16.0 Introduction','تعارف','پېژندنه',[
p('Some support in living organisms is necessary to uphold and sustain the body against gravity and other external forces.','جانداروں میں جسم کو کششِ ثقل اور دوسری بیرونی قوتوں کے مقابل قائم رکھنے کے لیے کچھ سہارا ضروری ہے۔','په ژوندیو موجوداتو کې د جاذبې او نورو بهرنیو ځواکونو پر وړاندې د بدن د ټینګ ساتلو لپاره ملاتړ اړین دی.'),
p('As the living organisms increased in size through the process of evolution, the need for support became greater.','ارتقا کے دوران جانداروں کا حجم بڑھا تو سہارے کی ضرورت بھی زیادہ ہوئی۔','د تکامل په بهیر کې چې ژوندي موجودات لوی شول، د ملاتړ اړتیا هم زیاته شوه.'),
p('This was particularly true once living organisms left water and colonized land.','یہ خاص طور پر اس وقت ہوا جب جاندار پانی چھوڑ کر خشکی پر آباد ہوئے۔','دا په ځانګړي ډول هغه وخت رښتیا وه چې ژوندیو موجوداتو اوبه پرېښودې او په وچه مېشت شول.'),
p('The skeleton in animals contributes to this support.','حیوانوں میں ڈھانچا یہ سہارا فراہم کرتا ہے۔','په حیواناتو کې اسکلېټ په دې ملاتړ کې ونډه لري.')],[60]),
('16.1 HUMAN SKELETON','انسانی ڈھانچا','د انسان اسکلېټ',[
p('The vertebrate skeleton is composed either of cartilage or bone.','فقاریوں کا ڈھانچا غضروف یا ہڈی سے بنا ہوتا ہے۔','د فقاریه حیواناتو اسکلېټ له غضروف یا هډوکي جوړ دی.'),
p('Both tissues provide an internal supporting framework of the body.','دونوں بافتے جسم کا اندرونی سہارا دینے والا ڈھانچا بناتے ہیں۔','دواړه نسجونه د بدن داخلي ملاتړی چوکاټ برابروي.'),
p('Human adults have bony skeleton, but cartilage is also present in some regions.','بالغ انسانوں کا ڈھانچا ہڈیوں کا ہوتا ہے، لیکن کچھ حصوں میں غضروف بھی ہوتا ہے۔','بالغ انسانان هډوکین اسکلېټ لري، خو په ځینو سیمو کې غضروف هم شته.')],[60]),
('16.1.1 Cartilage:','غضروف','غضروف',[
p('Cartilage is a type of connective tissue consisting of cells called chondrocytes and a tough, flexible matrix made of type II collagen.','غضروف رابط بافت کی ایک قسم ہے جو کونڈروسائٹس نامی خلیوں اور ٹائپ II کولیجن کے مضبوط، لچک دار میٹرکس سے بنتی ہے۔','غضروف یو ډول نښلوونکی نسج دی چې د کونډروسایټونو په نوم حجرې او له دوهم ډول کولاژن څخه جوړ کلک، انعطاف منونکی ماتریکس لري.'),
p('Unlike other connective tissues, cartilage does not contain blood vessels and the chondrocytes are supplied by diffusion.','دوسرے رابط بافتوں کے برعکس غضروف میں خون کی نالیاں نہیں ہوتیں اور کونڈروسائٹس کو انتشار سے رسد ملتی ہے۔','د نورو نښلوونکو نسجونو پر خلاف غضروف د وینې رګونه نه لري او کونډروسایټونو ته د خپرېدو له لارې مواد رسېږي.'),
p('Because of this, it heals very slowly.','اسی وجہ سے یہ بہت آہستہ مندمل ہوتا ہے۔','له همدې امله دا ډېر ورو رغېږي.'),
p('Although the human skeleton is initially made up of cartilages and fibrous membranes, most of these early supports are soon replaced by bones.','اگرچہ انسانی ڈھانچا ابتدا میں غضروفوں اور ریشے دار جھلیوں سے بنتا ہے، ان ابتدائی سہاروں کی زیادہ تر جگہ جلد ہڈیاں لے لیتی ہیں۔','که څه هم د انسان اسکلېټ په پیل کې له غضروفونو او فایبري پردو جوړ وي، د دغو لومړنیو ملاتړونو ډېره برخه ژر په هډوکو بدلېږي.'),
p('A few cartilages that remain in adults are found mainly in regions where flexible skeletal support is needed.','بالغوں میں باقی رہنے والے چند غضروف بنیادی طور پر ان جگہوں پر ہوتے ہیں جہاں لچک دار ڈھانچائی سہارا چاہیے۔','په بالغو کې پاتې څو غضروفونه تر ډېره په هغو سیمو کې وي چې انعطاف منونکي اسکلېټي ملاتړ ته اړتیا لري.'),
p('There are three types of cartilage tissue in human body: hyaline, elastic, and fibrocartilage.','انسانی جسم میں غضروفی بافت کی تین اقسام ہیں: ہائیلین، لچک دار اور ریشے دار غضروف۔','په انساني بدن کې د غضروفي نسج درې ډولونه دي: هایلین، ارتجاعي او فایبري غضروف.')],[60]),
]
from biology12_bone import REVISIONS as BONE, TABLE
REVISIONS.extend(BONE)
from biology12_skeleton_divisions import REVISIONS as DIVISIONS, TABLES
REVISIONS.extend(DIVISIONS)
from biology12_axial_skeleton import REVISIONS as AXIAL
REVISIONS.extend(AXIAL)
from biology12_joints import REVISIONS as JOINTS
REVISIONS.extend(JOINTS)
from biology12_skeletal_disorders import REVISIONS as DISORDERS
REVISIONS.extend(DISORDERS)
from biology12_fractures import REVISIONS as FRACTURES
REVISIONS.extend(FRACTURES)
from biology12_joint_injuries import REVISIONS as INJURIES
REVISIONS.extend(INJURIES)
from biology12_muscle_types import REVISIONS as MUSCLE_TYPES
REVISIONS.extend(MUSCLE_TYPES)
from biology12_muscle_structure import REVISIONS as MUSCLE_STRUCTURE
REVISIONS.extend(MUSCLE_STRUCTURE)
from biology12_muscle_problems import REVISIONS as MUSCLE_PROBLEMS
REVISIONS.extend(MUSCLE_PROBLEMS)
from biology12_unit16_close import REVISIONS as CLOSE, SUMMARY
REVISIONS.extend(CLOSE)
from biology12_unit16_exercise import EXERCISE

def main():
 target=ROOT/'js/biology_12_data.js'
 marker='// BEGIN SOURCE-LED BIOLOGY12 UNIT16 REVISION'
 text=target.read_text(encoding='utf-8').split(marker)[0]+'\n'+marker+'\n'
 for heading,ur,ps,paras,pages in REVISIONS:
  payload=dict(heading=heading,title=heading,headingUrdu=ur,urduTitle=ur,headingPashto=ps,paras=paras,text='\n\n'.join(x['text'] for x in paras),urdu='\n\n'.join(x['urdu'] for x in paras),pashto='\n\n'.join(x['pashto'] for x in paras),sourceReferences=[dict(printedPage=n,jpg=f'Biology Book for 12 class KPTBB_page_{n+4:03}.jpg',status='source transcribed') for n in pages],translationStatus='aligned Urdu and Pashto supplied; manual review pending')
  text+='{const incoming='+json.dumps(payload,ensure_ascii=False)+';const sections=BIOLOGY_12_DATA[2].sections;const current=sections.find(s=>s.heading===incoming.heading);if(current)Object.assign(current,incoming);else{const order=h=>(h.match(/^\\d+(?:\\.\\d+)*/)||[""])[0].split(".").map(n=>n.padStart(4,"0")).join(".");const next=/^\\d/.test(incoming.heading)?sections.findIndex(s=>order(s.heading)>order(incoming.heading)):-1;sections.splice(next<0?sections.length:next,0,incoming);}}\n'
 from PIL import Image
 from html import escape
 asset=ROOT/'assets/biology12/figure16-1-bone-cells.jpg'
 if not asset.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_064.jpg').crop((147,724,562,839)).save(asset)
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.1.2 Bone").diagramSvg=`<figure><img src="assets/biology12/figure16-1-bone-cells.jpg" alt="Osteoblast, osteocyte and osteoclast" style="max-width:100%;height:auto;"><figcaption>Fig:16.1 Different types of bone cells.</figcaption></figure>`;\n'
 table='<div style="overflow-x:auto"><table><caption>Table:16.1 Comparison between bone and cartilage</caption><thead><tr><th>Bone</th><th>Cartilage</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(c)+'</td>' for c in row)+'</tr>' for row in TABLE)+'</tbody></table></div>'
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.1.2 Bone and cartilage comparison").diagramSvg='+json.dumps(table)+';\n'
 skeleton=ROOT/'assets/biology12/figure16-2-human-skeleton.jpg'
 if not skeleton.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_066.jpg').crop((104,293,595,828)).save(skeleton)
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.1.3 Main divisions of human skeleton").diagramSvg=`<figure><img src="assets/biology12/figure16-2-human-skeleton.jpg" alt="Labelled human skeleton" style="max-width:100%;height:auto;"><figcaption>Fig:16.2 Human Skeleton</figcaption></figure>`;\n'
 for heading,caption,columns,rows in TABLES:
  table='<div style="overflow-x:auto"><table><caption>'+escape(caption)+'</caption><thead><tr>'+''.join('<th>'+escape(c)+'</th>' for c in columns)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'
  text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==='+json.dumps(heading)+').diagramSvg='+json.dumps(table)+';\n'
 for jpg,rect,name,caption,append in [(68,(168,263,600,520),'figure16-3-skull','Fig:16.3 Major bones of human skull.',False),(68,(455,542,668,827),'figure16-4-vertebral-column','Fig:16.4 Vertebral column of the human skeleton (side view)',True),(69,(364,32,669,350),'figure16-5-ribs','Fig:16.5 Human Ribs',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.1.3 Axial Skeleton")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for jpg,rect,name,caption,append in [(70,(453,216,646,424),'figure16-6-fibrous-joints','Fig:16.6 Fibrous joints in skull.',False),(70,(448,451,668,668),'figure16-7-cartilaginous-joints','Fig:16.7 Cartilaginous joints in vertebral column.',True),(71,(100,37,369,212),'figure16-8-hinge-joint','Fig:16.8 Hinge joint between trochlea of humerus and trochlear notch of ulna at the elbow.',True),(71,(379,39,658,214),'figure16-9-ball-socket','Fig:16.9 Ball-and-socket joint between head of the femur and acetabulum of the hip bone.',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.1.4 Joints")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 asset=ROOT/'assets/biology12/figure16-10-spondylosis.jpg'
 if not asset.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_072.jpg').crop((449,197,645,295)).save(asset)
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.2.1 Disorders of human skeleton:").diagramSvg=`<figure><img src="assets/biology12/figure16-10-spondylosis.jpg" alt="Source vertebral spondylosis illustration" style="max-width:100%;height:auto;"><figcaption>Fig:16.10 Spondylosis.</figcaption></figure>`;\n'
 asset=ROOT/'assets/biology12/figure16-11-fracture-repair.jpg'
 if not asset.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_073.jpg').crop((79,570,679,808)).save(asset)
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.2.2 Bone fractures").diagramSvg=`<figure><img src="assets/biology12/figure16-11-fracture-repair.jpg" alt="Hematoma, fibrocartilaginous callus, bony callus and bone remodeling" style="max-width:100%;height:auto;"><figcaption>Fig:16.11 Steps in the repair of fractured bone.</figcaption></figure>`;\n'
 asset=ROOT/'assets/biology12/figure16-12-ankle-ligaments.jpg'
 if not asset.exists():Image.open(ROOT.parent/'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_074.jpg').crop((455,581,657,703)).save(asset)
 text+='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.2.3 Joint injuries:").diagramSvg=`<figure><img src="assets/biology12/figure16-12-ankle-ligaments.jpg" alt="Ankle ligaments in the source illustration" style="max-width:100%;height:auto;"><figcaption>Fig:16.12 Ligaments in the ankle.</figcaption></figure>`;\n'
 for jpg,rect,name,caption,append in [(75,(182,477,564,636),'figure16-13-skeletal-muscle','Fig:16.13 Structure of skeletal muscle.',False),(76,(264,44,653,190),'figure16-14-cardiac-muscle','Fig:16.14 Structure of cardiac muscle',True),(76,(125,339,589,495),'figure16-15-smooth-muscle','Fig:16.15 Structure of smooth muscle.',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.3.1 Types of muscles")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for jpg,rect,name,caption,append in [(77,(145,133,626,480),'figure16-16-muscle-fibre','Fig:16.16 Section through a muscle fibre.',False),(78,(95,68,625,348),'figure16-17-sarcomere','Fig:16.17 Composition of sarcomere.',True),(79,(115,39,633,454),'figure16-18-filaments','Fig:16.18 Each sarcomere has a series of dark and light bands which are evident along the length of each myofibril.',True),(80,(133,57,650,470),'figure16-19-contraction','Fig:16.19 Sarcomere exhibiting contraction movement',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.3.2 Structure of Skeletal Muscles")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for jpg,rect,name,caption,append in [(81,(177,638,576,811),'figure16-20-cramps','Fig:16.20 Cramps are involuntary contractions or spasms in one or more muscles.',False),(82,(272,659,480,812),'figure16-21-tetani','Fig:16.21 Clostridium tetani',True)]:
  asset=ROOT/f'assets/biology12/{name}.jpg'
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  selector='BIOLOGY_12_DATA[2].sections.find(s=>s.heading==="16.3.5 Muscle problems")'
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  text+=selector+'.diagramSvg='+('('+selector+'.diagramSvg||"")+' if append else '')+figure+';\n'
 for key,language in [('englishSummary','text'),('urduSummary','urdu'),('pashtoSummary','pashto')]:
  text+='BIOLOGY_12_DATA[2]['+json.dumps(key)+']='+json.dumps('\n\n'.join(p[language] for p in SUMMARY),ensure_ascii=False)+';\n'
 text+='BIOLOGY_12_DATA[2].unreviewedExercise=BIOLOGY_12_DATA[2].exercise;BIOLOGY_12_DATA[2].exercise='+json.dumps(EXERCISE,ensure_ascii=False)+';BIOLOGY_12_DATA[2].unreviewedSloBank=BIOLOGY_12_DATA[2].sloBank;BIOLOGY_12_DATA[2].sloBank=BIOLOGY_12_DATA[2].exercise;\n'
 text+='BIOLOGY_12_DATA[2].sourceStatus="in_progress";\n'
 import time
 for attempt in range(4):
  try:
   target.write_text(text,encoding='utf-8',newline='\n')
   break
  except OSError as error:
   if error.errno!=22 or attempt==3:raise
   time.sleep(0.5)
 ledger_path=ROOT/'docs/source-verification/biology12.json'
 ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
 ledger['currentUnit']=17
 ledger['nextSource']='Biology Book for 12 class KPTBB_page_088.jpg'
 ledger['unit16Scope']='Lessons and23 key points through printed83 represented with Urdu/Pashto, figures16.1–16.21 and native tables16.1–16.3;8 MCQs,3 visible short questions,7 long progressive answers with sarcomere schematic and10 activities. Full exercise translations, word/audio and opener pending. Source ratios65/35 and70/30,350 birth bones and8 ankle bones retained; short numbering skipsiii. No completed-work recheck.'
 for page in ledger['pages']:
  if 64<=int(page['jpg'][-7:-4])<=87:page['status']='source_transcribed'
  elif page['jpg'].endswith('063.jpg'):page['status']='source_viewed'
 ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Unit16 source lessons added.')
if __name__=='__main__':main()
