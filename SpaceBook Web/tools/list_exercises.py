import json
from pathlib import Path
p=Path(r"D:\SpaceBook\SpaceBook Web\js\math_12_data.js")
s=p.read_text(encoding="utf-8")
a=s.index("const MATH_12_DATA = ")+len("const MATH_12_DATA = ")
b=s.rfind("];", a)+1
units=json.loads(s[a:b])
for unit in units:
    print(unit["number"], unit["title"], [(e["id"],e["title"],len(e.get("problems",[])),e.get("pageStart")) for e in unit.get("exercises",[])])
