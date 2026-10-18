"""Move the completed PDF-page audit additions into their assigned unit buckets."""
import json
from class12_source_review import ROOT,upsert,sync_companions,shared_class_data_lock

OUT=ROOT/"docs/source-verification/class-12"
progress=json.loads((OUT/"progress.json").read_text(encoding="utf-8"))
move_ids={identity for page in progress["pages"] if 84<=page["pdfPage"]<=153 for identity in page["recordIds"]}
records_path=OUT/"physics-corrections-unit14.json"
sections_path=OUT/"physics-sections-unit14.json"
records=json.loads(records_path.read_text(encoding="utf-8"))
sections=json.loads(sections_path.read_text(encoding="utf-8"))
if len(move_ids)!=70 or not move_ids.issubset({item["id"] for item in records}) or not move_ids.issubset({item["id"] for item in sections}):
    raise RuntimeError("The Unit 14 bucket does not contain exactly the expected PDF pages 84–153 records.")
records=[item for item in records if item["id"] not in move_ids]
sections=[item for item in sections if item["id"] not in move_ids]
companions_path=OUT/"physics-companions-unit14.json"
companions=json.loads(companions_path.read_text(encoding="utf-8"))
def moved(item):
    return any(84<=ref.get("pdfPage",-1)<=153 for ref in item.get("sourceReferences",[]))
for key in ("formulas","definitions","workedExamples","exercises"):
    companions[key]=[item for item in companions[key] if not moved(item)]
companions["retireSections"]=[identity for identity in companions["retireSections"] if identity in {"14.1","14.2","14.11"}]
companions["trimSections"]=[item for item in companions["trimSections"] if item["id"].startswith("14.") or item["id"].startswith("phys14-")]
records_path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
sections_path.write_text(json.dumps(sections,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
companions_path.write_text(json.dumps(companions,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
with shared_class_data_lock():
    upsert([],[],chapter_index=3)
    sync_companions(chapter_index=3)
print(f"Removed {len(move_ids)} Unit 15–18 records from the Unit 14 bucket; retained {len(records)} Unit 14 records.")
