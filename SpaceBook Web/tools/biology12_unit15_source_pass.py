"""Append Unit 15 source lessons; preserve earlier chapter work."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def p(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto)
REVISIONS=[
('15.0 Introduction','تعارف','پېژندنه',[
p('Animals have really two environments: an external environment in which the organism is situated, and an internal environment in which the tissue of the body live.','حیوانوں کے دراصل دو ماحول ہوتے ہیں: بیرونی ماحول جس میں جاندار موجود ہوتا ہے، اور اندرونی ماحول جس میں جسم کے بافتے رہتے ہیں۔','حیوانات په حقیقت کې دوه چاپېریالونه لري: بهرنی چاپېریال چې ژوندی موجود پکې وي، او داخلي چاپېریال چې د بدن نسجونه پکې ژوند کوي.'),
p('The external environment consists of varying conditions of environment.','بیرونی ماحول مختلف بدلتے ہوئے ماحولیاتی حالات پر مشتمل ہوتا ہے۔','بهرنی چاپېریال د چاپېریال له بدلېدونکو شرایطو جوړ دی.'),
p('The internal environment is formed by the circulating organic liquid called lymph or plasma which surrounds and bathes all the tissues.','اندرونی ماحول گردش کرنے والے نامیاتی سیال، جسے لمف یا پلازما کہتے ہیں، سے بنتا ہے جو تمام بافتوں کو گھیرتا اور تر رکھتا ہے۔','داخلي چاپېریال له ګرځېدونکي عضوي مایع څخه جوړېږي چې لمف یا پلازما بلل کېږي او ټول نسجونه چاپېروي او لمدوي.'),
p('Homeostasis is the tendency of an organism or cell to regulate its internal conditions, such as the chemical composition of its body fluids, so as to maintain health and functioning, regardless of outside conditions.','ہومیوسٹیسس جاندار یا خلیے کا وہ رجحان ہے جس کے تحت وہ بیرونی حالات سے قطع نظر صحت اور کارکردگی برقرار رکھنے کے لیے اپنے اندرونی حالات، مثلاً جسمانی سیالات کی کیمیائی ترکیب، کو منظم کرتا ہے۔','هومیوستاسس د ژوندي موجود یا حجرې هغه تمایل دی چې خپل داخلي شرایط، لکه د بدني مایعاتو کیمیاوي ترکیب، تنظیموي څو له بهرنیو شرایطو پرته روغتیا او فعالیت وساتي.'),
p('The organism or cell maintains homeostasis by monitoring its internal conditions and responding appropriately when these conditions deviate from their normal state.','جاندار یا خلیہ اپنے اندرونی حالات کی نگرانی کرکے اور معمول کی حالت سے انحراف پر مناسب ردعمل دے کر ہومیوسٹیسس برقرار رکھتا ہے۔','ژوندی موجود یا حجره د خپلو داخلي شرایطو په څارلو او له عادي حالت څخه د انحراف پر مهال په مناسب غبرګون سره هومیوستاسس ساتي.')],[30]),
('15.1 MECHANISM OF HOMEOSTASIS','ہومیوسٹیسس کا طریقۂ کار','د هومیوستاسس میکانیزم',[
p('Homeostatic mechanism operates just like physical control system having three components; receptors, control center and effectors.','ہومیوسٹیسس کا طریقۂ کار طبیعی کنٹرول نظام کی طرح کام کرتا ہے جس کے تین اجزا ہیں: رسیپٹرز، کنٹرول مرکز اور ایفیکٹرز۔','د هومیوستاسس میکانیزم د فزیکي کنټرول سیسټم په څېر کار کوي چې درې برخې لري: اخیستونکي، د کنټرول مرکز او اغېز کوونکي.'),
p('Receptor (sensor) detects changes in variable and feeds that information back to the control center (integrator).','رسیپٹر (حساسہ) متغیر میں تبدیلیوں کا پتہ لگاتا ہے اور یہ معلومات کنٹرول مرکز (انٹیگریٹر) کو واپس دیتا ہے۔','اخیستونکی یا حس کوونکی په متغیر کې بدلونونه معلوموي او دا معلومات د کنټرول مرکز یا یوځای کوونکي ته بېرته لېږي.'),
p('Control center (integrator) integrates (puts together) data from sensor and stored "set point" data.','کنٹرول مرکز (انٹیگریٹر) حساسے سے آنے والے اعداد اور محفوظ شدہ مقررہ نقطے کے اعداد کو یکجا کرتا ہے۔','د کنټرول مرکز د حس کوونکي معلومات او د ټاکلي حد ساتل شوي معلومات یوځای کوي.'),
p('Effector is the mechanism (heating coil in this example) that has an "effect" on the variable.','ایفیکٹر وہ نظام ہے (اس مثال میں حرارتی کوائل) جو متغیر پر اثر ڈالتا ہے۔','اغېز کوونکی هغه میکانیزم دی (په دې بېلګه کې د تودولو کویل) چې پر متغیر اغېز کوي.'),
p('In a common lab incubator, if temperature is decreased from set point, the thermometer (receptor) detects the change in temperature and signals the thermostat (control center), which in turn activates the heating coil (effector).','عام تجربہ گاہی انکیوبیٹر میں درجۂ حرارت مقررہ نقطے سے کم ہو تو تھرمامیٹر (رسیپٹر) تبدیلی معلوم کرکے تھرموسٹیٹ (کنٹرول مرکز) کو اشارہ دیتا ہے، جو حرارتی کوائل (ایفیکٹر) کو فعال کرتا ہے۔','په عادي لابراتواري انکیوبېټر کې که تودوخه له ټاکلي حد کمه شي، ترمامیتر بدلون معلوموي او ترموستات ته نښه لېږي، چې بیا د تودولو کویل فعالوي.'),
p('Similarly if temperature is increased from the set point again thermometer detects the change and signals the thermostat to switch off heating.','اسی طرح درجۂ حرارت مقررہ نقطے سے بڑھ جائے تو تھرمامیٹر تبدیلی معلوم کرکے تھرموسٹیٹ کو حرارت بند کرنے کا اشارہ دیتا ہے۔','همدارنګه که تودوخه له ټاکلي حد زیاته شي، ترمامیتر بدلون معلوموي او ترموستات ته د تودولو د بندولو نښه لېږي.'),
p('Likewise, in human body thermoreceptors are involved in the detection of temperature change.','اسی طرح انسانی جسم میں حرارت کے رسیپٹرز درجۂ حرارت کی تبدیلی معلوم کرتے ہیں۔','همداسې په انساني بدن کې د تودوخې اخیستونکي د تودوخې بدلون معلوموي.'),
p('Hypothalamus in fore brain is a body thermostat.','پیش دماغ میں ہائپوتھیلمس جسم کا تھرموسٹیٹ ہے۔','په مخکني مغز کې هایپوتالاموس د بدن ترموستات دی.'),
p('Stimulated once, hypothalamus acts on effectors for cooling (e.g. sweat glands) or heating (e.g. muscles) the body to reverse the change to the set point.','تحریک ملنے پر ہائپوتھیلمس جسم کو ٹھنڈا کرنے والے (مثلاً پسینے کے غدود) یا گرم کرنے والے (مثلاً عضلات) ایفیکٹرز پر عمل کرتا ہے تاکہ تبدیلی کو مقررہ نقطے پر واپس لایا جائے۔','تر تحریک وروسته هایپوتالاموس د بدن د سړولو (لکه د خولو غدې) یا تودولو (لکه عضلې) پر اغېز کوونکو عمل کوي څو بدلون بېرته ټاکلي حد ته راوګرځوي.'),
p('After receiving the signal, a change occurs to correct the deviation either by depressing it with negative feedback or enhancing it with positive feedback.','اشارہ ملنے کے بعد انحراف درست کرنے کے لیے تبدیلی واقع ہوتی ہے، یا منفی فیڈبیک سے اسے کم کیا جاتا ہے یا مثبت فیڈبیک سے بڑھایا جاتا ہے۔','د نښې تر ترلاسه کولو وروسته د انحراف د سمولو لپاره بدلون راځي، یا په منفي فیډبک کمېږي یا په مثبت فیډبک زیاتېږي.')],[30,31]),
('15.1.1 Negative Feedback','منفی فیڈبیک','منفي فیډبک',[
p('Negative feedback is mainly how homeostasis is maintained.','ہومیوسٹیسس بنیادی طور پر منفی فیڈبیک سے برقرار رہتا ہے۔','هومیوستاسس تر ډېره د منفي فیډبک له لارې ساتل کېږي.'),
p('This feedback results in a reversal of the direction of change.','اس فیڈبیک سے تبدیلی کی سمت پلٹ جاتی ہے۔','دا فیډبک د بدلون لوری اړوي.'),
p('Negative feedback tends to stabilize a system, correcting deviations from the normal state.','منفی فیڈبیک معمول کی حالت سے انحراف درست کرکے نظام کو مستحکم کرتا ہے۔','منفي فیډبک له عادي حالت څخه انحرافونه سموي او سیسټم باثباته کوي.'),
p('In example, negative feedback mechanism is applied to control water content in the body.','مثال کے طور پر جسم میں پانی کی مقدار منظم کرنے کے لیے منفی فیڈبیک کام کرتا ہے۔','د بېلګې په توګه، په بدن کې د اوبو د مقدار د کنټرول لپاره منفي فیډبک کار کوي.'),
p('When body is deficient in water, hypothalamus stimulates posterior pituitary lobe to release antidiuretic hormone (ADH).','جب جسم میں پانی کم ہو تو ہائپوتھیلمس پچوٹری کے پچھلے حصے کو اینٹی ڈائیوریٹک ہارمون (ADH) خارج کرنے کی تحریک دیتا ہے۔','کله چې په بدن کې اوبه کمې شي، هایپوتالاموس د نخامیه غدې شاتنۍ برخه د ادرار ضد هورمون (ADH) خوشې کولو ته هڅوي.'),
p('ADH makes collecting tubules and distal convoluted tubules of nephrons permeable to water, thus more water is absorbed, and maximum amount of water is retained in the body.','ADH نیفرون کی جمع کرنے والی نالیوں اور دور کی پیچ دار نالیوں کو پانی کے لیے نفوذ پذیر بناتا ہے؛ یوں زیادہ پانی جذب ہوتا ہے اور جسم میں زیادہ سے زیادہ پانی محفوظ رہتا ہے۔','ADH د نیفرونونو راټولوونکي نلونه او لرې تاو شوي نلونه اوبو ته د تېرېدو وړ ګرځوي؛ نو زیاتې اوبه جذبېږي او په بدن کې ډېرې اوبه ساتل کېږي.'),
p('The blood water content rises, which is sensed by hypothalamus, so ADH secretion slows down.','خون میں پانی کی مقدار بڑھتی ہے، ہائپوتھیلمس اسے محسوس کرتا ہے، اس لیے ADH کا اخراج کم ہو جاتا ہے۔','په وینه کې د اوبو مقدار لوړېږي، هایپوتالاموس یې احساسوي، نو د ADH ترشح ورو کېږي.')],[31]),
('15.1.2 Positive Feedback','مثبت فیڈبیک','مثبت فیډبک',[
p('In contrast to negative feedback, positive-feedback involves a change in some variable that triggers mechanisms that amplify rather than reverse the change.','منفی فیڈبیک کے برعکس مثبت فیڈبیک میں کسی متغیر کی تبدیلی ایسے طریقے فعال کرتی ہے جو اس تبدیلی کو پلٹانے کے بجائے بڑھاتے ہیں۔','د منفي فیډبک پر خلاف، په مثبت فیډبک کې د متغیر بدلون داسې میکانیزمونه فعالوي چې بدلون د بېرته اړولو پر ځای زیاتوي.'),
p("During childbirth, for instance, the pressure of the baby's head against sensors near the opening of the uterus stimulates; uterine contractions, which cause greater pressure against the uterine opening, heightening the contractions which causes still greater pressure.",'مثلاً ولادت کے دوران رحم کے دہانے کے قریب حساسوں پر بچے کے سر کا دباؤ رحم کے سکڑاؤ کو تحریک دیتا ہے؛ اس سے دہانے پر دباؤ بڑھتا ہے، سکڑاؤ زیادہ ہوتا ہے اور دباؤ مزید بڑھتا ہے۔','د بېلګې په توګه، د زېږون پر مهال د رحم خولې ته نږدې پر حس کوونکو د ماشوم د سر فشار د رحم انقباضونه هڅوي؛ دا د رحم پر خوله فشار زیاتوي، انقباضونه پیاوړي کوي او فشار نور هم زیاتېږي.'),
p('Positive feedback brings childbirth to completion, a very different sort of process from maintaining a physiological steady state.','مثبت فیڈبیک ولادت کو مکمل کرتا ہے، جو فعلیاتی مستحکم حالت برقرار رکھنے سے بہت مختلف عمل ہے۔','مثبت فیډبک زېږون بشپړوي، چې د فزیولوژیکي ثابت حالت له ساتلو ډېر توپیر لري.')],[31]),
('15.1.3 Harmful Positive Feedback','نقصان دہ مثبت فیڈبیک','زیانمن مثبت فیډبک',[
p('Although Positive Feedback is needed within homeostasis, it also can be harmful at times.','اگرچہ ہومیوسٹیسس میں مثبت فیڈبیک کی ضرورت ہوتی ہے، لیکن بعض اوقات یہ نقصان دہ بھی ہو سکتا ہے۔','که څه هم په هومیوستاسس کې مثبت فیډبک ته اړتیا وي، خو کله ناکله زیانمن هم کېدای شي.'),
p('When you have a high fever it causes a metabolic change that can push the fever higher and higher.','تیز بخار ایسی استحالہ جاتی تبدیلی پیدا کرتا ہے جو بخار کو مزید بڑھا سکتی ہے۔','لوړه تبه میتابولیک بدلون رامنځته کوي چې تبه نوره هم لوړولای شي.'),
p('In rare cases the body temperature reaches 113° F and the cellular proteins stop working and the metabolism stops, resulting in death.','نادر صورتوں میں جسم کا درجۂ حرارت 113° F تک پہنچ جاتا ہے، خلیاتی پروٹین کام چھوڑ دیتے ہیں اور استحالہ رک جاتا ہے، جس سے موت واقع ہوتی ہے۔','په نادرو حالاتو کې د بدن تودوخه 113° F ته رسېږي، حجروي پروټینونه کار پرېږدي او میتابولیزم درېږي، چې د مړینې لامل کېږي.'),
p('If a person breathes air that has very high carbon dioxide content, this produces a high concentration of carbon dioxide in blood.','اگر کوئی شخص ایسی ہوا میں سانس لے جس میں کاربن ڈائی آکسائیڈ بہت زیادہ ہو تو خون میں کاربن ڈائی آکسائیڈ کا ارتکاز بڑھ جاتا ہے۔','که یو کس داسې هوا تنفس کړي چې کاربن ډای اکسایډ پکې ډېر زیات وي، په وینه کې یې غلظت لوړېږي.'),
p('This is sensed by carbon dioxide receptors, which cause the breathing rate to increase.','کاربن ڈائی آکسائیڈ کے رسیپٹرز اسے محسوس کرکے سانس کی رفتار بڑھاتے ہیں۔','د کاربن ډای اکسایډ اخیستونکي دا احساسوي او د تنفس چټکتیا زیاتوي.'),
p('So the person breathes faster, taking in more carbon dioxide, which stimulates the receptors even more, so they breathe faster and faster.','یوں شخص تیزی سے سانس لے کر مزید کاربن ڈائی آکسائیڈ اندر لیتا ہے، رسیپٹرز کو مزید تحریک ملتی ہے اور سانس مسلسل تیز ہوتا جاتا ہے۔','نو کس په چټکۍ ساه اخلي او ډېر کاربن ډای اکسایډ دننه کوي، چې اخیستونکي نور هم تحریکوي او ساه لا چټکېږي.'),
p('Skills — Interpreting and Communicating: Draw a flow chart to show negative feedback of homeostasis mechanisms by taking an example of hormone.','مہارتیں — تشریح اور ابلاغ: کسی ہارمون کی مثال سے ہومیوسٹیسس کے منفی فیڈبیک کا فلوچارٹ بنائیں۔','مهارتونه — تفسیر او اړیکې: د یوه هورمون په بېلګه د هومیوستاسس د منفي فیډبک بهیر انځور کړئ.')],[31]),
]
from biology12_osmoregulation import REVISIONS as OSMOREGULATION
REVISIONS.extend(OSMOREGULATION)
from biology12_excretion import REVISIONS as EXCRETION
REVISIONS.extend(EXCRETION)
from biology12_urinary_system import REVISIONS as URINARY_SYSTEM
REVISIONS.extend(URINARY_SYSTEM)
from biology12_nephron import REVISIONS as NEPHRON
REVISIONS.extend(NEPHRON)
from biology12_filtration import REVISIONS as FILTRATION
REVISIONS.extend(FILTRATION)
from biology12_kidney_regulation import REVISIONS as REGULATION
REVISIONS.extend(REGULATION)
from biology12_stones import REVISIONS as STONES
REVISIONS.extend(STONES)
from biology12_renal_failure import REVISIONS as RENAL_FAILURE
REVISIONS.extend(RENAL_FAILURE)
from biology12_dialysis import REVISIONS as DIALYSIS
REVISIONS.extend(DIALYSIS)
from biology12_transplant import REVISIONS as TRANSPLANT
REVISIONS.extend(TRANSPLANT)
from biology12_thermoregulation import REVISIONS as THERMOREGULATION
REVISIONS.extend(THERMOREGULATION)
from biology12_heat_balance import REVISIONS as HEAT_BALANCE
REVISIONS.extend(HEAT_BALANCE)
from biology12_unit15_close import REVISIONS as CLOSE, SUMMARY
REVISIONS.extend(CLOSE)
from biology12_unit15_exercise import EXERCISE

def main():
 target=ROOT/'js/biology_12_data.js'
 marker='// BEGIN SOURCE-LED BIOLOGY12 UNIT15 REVISION'
 text=target.read_text(encoding='utf-8').split(marker)[0]+'\n'+marker+'\n'
 for heading,ur,ps,paras,pages in REVISIONS:
  payload=dict(heading=heading,title=heading,headingUrdu=ur,urduTitle=ur,headingPashto=ps,paras=paras,text='\n\n'.join(x['text'] for x in paras),urdu='\n\n'.join(x['urdu'] for x in paras),pashto='\n\n'.join(x['pashto'] for x in paras),sourceReferences=[dict(printedPage=n,jpg=f'Biology Book for 12 class KPTBB_page_{n+4:03}.jpg',status='source transcribed') for n in pages],translationStatus='aligned Urdu and Pashto sentences supplied; manual review pending')
  text+='{const incoming='+json.dumps(payload,ensure_ascii=False)+';const sections=BIOLOGY_12_DATA[1].sections;const current=sections.find(s=>s.heading===incoming.heading);if(current)Object.assign(current,incoming);else{const order=h=>(h.match(/^\\d+(?:\\.\\d+)*/)||[""])[0].split(".").map(n=>n.padStart(4,"0")).join(".");const next=/^\\d/.test(incoming.heading)?sections.findIndex(s=>order(s.heading)>order(incoming.heading)):-1;sections.splice(next<0?sections.length:next,0,incoming);}}\n'
 from PIL import Image
 assets=ROOT/'assets/biology12'
 for heading,jpg,rect,name,caption in [
  ('15.11.4 Role of the hypothalamus',56,(452,233,666,442),'figure15-20-hypothalamus','Fig:15.20 Hypothalamus in the brain.'),
  ('15.11.2 Heat loss',55,(468,292,601,398),'heat-loss-information','Insulating body covering — source information-box photograph'),
  ('15.11 THERMOREGULATION',54,(462,296,655,441),'figure15-19-white-shark','Fig:15.19 Great white shark an endothermic animal.'),
  ('15.10 KIDNEY TRANSPLANTATION',52,(247,604,541,817),'figure15-17-transplant','Fig:15.14 Recipient non functioning kidney is replaced by donor functioning kidney.'),
  ('15.10.1 Donor-Recipient Match',53,(201,117,597,340),'figure15-18-transplant-location','Fig:15.18 Location where the healthy kidney is placed in the patient body.'),
  ('15.9.1 Peritoneal Dialysis',50,(369,527,647,813),'figure15-14-peritoneal-dialysis','Fig:15.14 Peritoneal dialysis'),
  ('15.9.2 Haemodialysis',51,(121,344,318,605),'figure15-15-haemodialysis-patient','Fig:15.15 Patient being treated by haemodialysis.'),
  ('15.9.2 Haemodialysis',51,(322,342,681,607),'figure15-16-haemodialysis','Fig:15.16 Mechanism of haemodialysis.'),
  ('15.7.3 Causes:',48,(133,533,622,686),'figure15-12-kidney-stones','Fig:15.12 Kidney stones'),
  ('15.7.4 Treatment of urinary stones',49,(539,96,649,232),'figure15-13-staghorn','Fig:15.13 Staghorn stone'),
  ('15.7.1 Symptoms/Indications',47,(133,544,640,809),'figure15-11-kidney-stones','Fig:15.11 Formation of Kidney stones in various places in the urinary system.'),
  ('15.5.9 Excretory Function of Nephron',44,(120,501,596,765),'figure15-9-ultrafiltration','Fig:15.9 Mechanism of ultrafiltration.'),
  ('15.5.9 Excretory Function of Nephron',45,(361,392,688,808),'figure15-10-urine-formation','Fig:15.10 An overview of the process of urine formation'),
  ('15.5.8 Types of Nephron',43,(446,544,674,775),'figure15-8-nephron-types','Fig:15.8 Types of nephron.'),
  ('15.5 HUMAN EXCRETORY SYSTEM',41,(390,163,681,468),'figure15-5-urinary-system','Fig:15.5 Human urinary system'),
  ('15.5.1 Kidneys',41,(86,549,475,797),'figure15-6-kidney','Fig:15.6 Human Kidney'),
  ('15.5.5 Nephron',42,(356,532,662,797),'figure15-7-nephron','Fig:15.7 Structure of nephron'),
  ('15.4 EXCRETION',39,(209,264,555,754),'figure15-4-nitrogenous-waste','Fig:15.4 Different types of nitrogenous wastes excreted by animals according to their habitat.'),
  ('15.1 MECHANISM OF HOMEOSTASIS',34,(62,610,662,841),'figure15-1-homeostasis','Fig:15.1 Mechanism of homeostasis.'),
  ('15.3.2 Marine animals:',38,(117,41,607,358),'figure15-2-osmoregulation','Fig:15.2 Osmoregulation in marine animals.'),
  ('15.3.3 Terrestrial animals:',38,(432,653,635,793),'figure15-3-kangaroo-rat','Fig:15.3 Kangroo rat; master of water conservation in the desert.')]:
  asset=assets/(name+'.jpg')
  if not asset.exists():Image.open(ROOT.parent/f'Books/12th/12th Biology/JPG/Biology Book for 12 class KPTBB_page_{jpg:03}.jpg').crop(rect).save(asset)
  figure=json.dumps(f'<figure><img src="assets/biology12/{name}.jpg" alt="{caption}" style="max-width:100%;height:auto;"><figcaption>{caption}</figcaption></figure>')
  selected='BIOLOGY_12_DATA[1].sections.find(s=>s.heading==='+json.dumps(heading)+')'
  text+=selected+'.diagramSvg='+('('+selected+'.diagramSvg||"")+' if name in ('figure15-10-urine-formation','figure15-16-haemodialysis') else '')+figure+';\n'
 for key,language in [('englishSummary','text'),('urduSummary','urdu'),('pashtoSummary','pashto')]:
  text+='BIOLOGY_12_DATA[1]['+json.dumps(key)+']='+json.dumps('\n\n'.join(p[language] for p in SUMMARY),ensure_ascii=False)+';\n'
 text+='BIOLOGY_12_DATA[1].unreviewedExercise=BIOLOGY_12_DATA[1].exercise;BIOLOGY_12_DATA[1].exercise='+json.dumps(EXERCISE,ensure_ascii=False)+';BIOLOGY_12_DATA[1].unreviewedSloBank=BIOLOGY_12_DATA[1].sloBank;BIOLOGY_12_DATA[1].sloBank=BIOLOGY_12_DATA[1].exercise;\n'
 text+='BIOLOGY_12_DATA[1].sourceStatus="in_progress";\n'
 target.write_text(text,encoding='utf-8',newline='\n')
 ledger_path=ROOT/'docs/source-verification/biology12.json'
 ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
 ledger['currentUnit']=15
 ledger['currentUnit']=16
 ledger['nextSource']='Biology Book for 12 class KPTBB_page_063.jpg'
 ledger['unit15Scope']='Lessons and22 source key points through printed58 represented with Urdu/Pashto and isolated figures15.1–15.20;11 MCQs,10 short and7 extensive progressive answers,2 society connections and3 skills. Full exercise translations, word/audio coverage and opener pending; no completed-work recheck. Printed heading5.5.9 represented as15.5.9; transplant figure printed15.14 retained.'
 for page in ledger['pages']:
  if 34<=int(page['jpg'][-7:-4])<=62:page['status']='source_transcribed'
  elif page['jpg'].endswith('033.jpg'):page['status']='source_viewed'
 ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Unit15 introduction and feedback lessons added.')
if __name__=='__main__':main()
