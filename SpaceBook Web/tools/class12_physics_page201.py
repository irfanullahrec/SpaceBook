from class12_source_review import ROOT,upsert,section,checkpoint,shared_class_data_lock
import json
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def ref():return {"pdfPage":201,"printedPage":None,"sourcePdf":SOURCE}
def p(e,u,s):return e,u,s
ur=["قومی ترانہ","پاک سرزمین شاد باد","کشور حسین شاد باد","تو نشان عزم عالی شان","ارض پاکستان","مرکز یقین شاد باد","پاک سرزمین کا نظام","قوت اخوت عوام","قوم، ملک، سلطنت","پائندہ تابندہ باد","شاد باد منزل مراد","پرچم ستارہ و ہلال","رہبر ترقی و کمال","ترجمان ماضی شان حال","جان استقبال","سایہ خدائے ذوالجلال"]
en=["National anthem","Blessed be the sacred land","May the beautiful realm be blessed","You are the symbol of high resolve","Land of Pakistan","May the center of faith be blessed","The order of the sacred land","The strength of the people’s brotherhood","The nation, country and state","Everlasting and flourishing","Blessed be the cherished goal","Flag with star and crescent","Leader of progress and perfection","Interpreter of the past, glory of the present","Future’s welcome","May it remain under the shadow of God, the Majestic"]
ps=["ملي سرود","مقدسه خاوره دې اباده وي","ښکلی هېواد دې اباد وي","ته د لوړ عزم نښه یې","د پاکستان خاوره","د ایمان مرکز دې اباد وي","د سپېڅلې خاورې نظام","د ولس د ورورولۍ ځواک","ملت، هېواد او دولت","تلپاتې او ودان","د هیلو منزل دې اباد وي","د ستوري او هلال بیرغ","د پرمختګ او کمال لارښود","د تېر وخت ژباړن، د حال ویاړ","د راتلونکي هرکلی","د لوی خدای تر سیوري لاندې دې وي"]
T=[(en[i],ur[i],ps[i]) for i in range(len(ur))]
originals=ur+["Leading Books Publishers, Jamrud Road, Peshawar. Code No. PSP/NBP-57-208-2122(O). Quantity: 50285. Printed by Naqvi Brothers Printing Press."]
T.append(("Publisher: Leading Books Publishers, Jamrud Road, Peshawar. Code No. PSP/NBP-57-208-2122(O). Quantity 50285. Printed by Naqvi Brothers Printing Press.",originals[-1],"خپرندوی: Leading Books Publishers، Jamrud Road، Peshawar. Code No. PSP/NBP-57-208-2122(O). شمېر 50285. چاپ: Naqvi Brothers Printing Press."))
record={"id":"phys12-back-cover-national-anthem-publisher-201","title":"Back-cover national anthem and publisher imprint","kind":"book_front_matter","pdfPage":201,"printedPage":None,"sourcePdf":SOURCE,"paragraphs":originals}
layout=[{"type":"quotation","indices":list(range(16))},{"type":"explanation","indices":[16]}]
sec=section(record,T,layout,("ملي سرود او خپرندوی","National anthem and publisher"),source_language="ur");sec["kind"]="book_front_matter";sec["sourceReferences"]=[ref()]
with shared_class_data_lock():
 upsert([record],[sec],chapter_index=9)
 pr=json.loads((ROOT/"docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
 if pr["nextPage"]==201:checkpoint(201,"corrected_verified",[record["id"]],"Inspected PDF page 201 (back cover, no printed number). Transcribed Urdu national anthem title/lines and publisher imprint, code, quantity and printer; supplied aligned English and Pashto translations. Cover photograph/emblem excluded as decoration.",printed_pages=[],chapter_number=20)
