"""Retire only fully source-audited legacy unit sections after rebucketing."""
import json
from class12_source_review import ROOT,sync_companions,shared_class_data_lock

OUT=ROOT/"docs/source-verification/class-12"
plans={15:[f"15.{n}" for n in range(1,19)],16:[f"16.{n}" for n in range(1,12)],17:[f"17.{n}" for n in range(1,11)]}
for unit,retired in plans.items():
    path=OUT/f"physics-companions-unit{unit}.json"
    data=json.loads(path.read_text(encoding="utf-8"))
    data["retireSections"]=retired
    data["trimSections"]=[]
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
path=OUT/"physics-companions-unit18.json"
data=json.loads(path.read_text(encoding="utf-8"))
data["retireSections"]=[]
data["trimSections"]=[]
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
with shared_class_data_lock():
    for unit in (15,16,17,18):
        sync_companions(chapter_index=unit-11)
print("Unit 15–17 legacy lesson sections now defer to their fully audited replacements; Unit 18 awaits page 154 before retiring its legacy sections.")
