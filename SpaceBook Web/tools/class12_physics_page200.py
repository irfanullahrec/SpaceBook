from class12_source_review import ROOT,upsert,section,checkpoint,shared_class_data_lock
import json
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def ref(n):return {"pdfPage":200,"printedPage":None,"sourcePdf":SOURCE}
originals=["مومن تو آپس میں بھائی بھائی ہیں، پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحمت کی جائے۔ (سورۃ الحجرات: 10)","اے ایمان والو! ان پاک چیزوں میں سے کھاؤ جو ہم نے تم کو دی ہیں۔ (سورۃ البقرۃ: 172)"]
T=[("Believers are brothers to one another; therefore make peace between your two brothers and fear Allah so that you may receive mercy.",originals[0],"مؤمنان له یو بل سره وروڼه دي؛ نو د خپلو دوو وروڼو ترمنځ سوله وکړئ او له الله ووېرېږئ، ښايي رحم درباندې وشي."),("O you who believe, eat of the pure things We have provided for you.",originals[1],"اې مؤمنانو، له هغو پاکو شیانو وخورئ چې موږ درکړي دي.")]
record={"id":"phys12-back-cover-urdu-verses-380","title":"Back-cover verses on reconciliation and lawful provision","kind":"book_front_matter","pdfPage":200,"printedPage":None,"sourcePdf":SOURCE,"paragraphs":originals}
sec=section(record,T,[{"type":"quotation","indices":[0]},{"type":"quotation","indices":[1]}],("د قرآن کریم لارښوونې","Qur’anic guidance"),source_language="ur");sec["kind"]="book_front_matter";sec["sourceReferences"]=[ref(0)];sec["diagramSvg"]="";sec["diagramSvgUrdu"]="";sec["diagramSvgPashto"]="";sec["content"]="".join('<p>'+x[0]+'</p>' for x in T)
with shared_class_data_lock():
 upsert([record],[sec],chapter_index=9)
 pr=json.loads((ROOT/"docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
 if pr["nextPage"]==200:checkpoint(200,"corrected_verified",[record["id"]],"Inspected PDF page 200 (back-cover page, no printed number). Transcribed both Urdu quotations and surah/verse citations; paired English and Pashto translations. Floral borders and watermark are decorative, not instructional.",printed_pages=[],chapter_number=20)
