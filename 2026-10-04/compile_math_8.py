# -*- coding: utf-8 -*-
"""
Compiles all 11 Units of Class 8 Mathematics into D:\SpaceBook\SpaceBook Web\js\math_8_data.js
"""

import json
import os
import sys

from build_math_u1 import get_unit_1
from build_math_u2_u4 import get_unit_2, get_unit_3, get_unit_4
from build_math_u5_u7 import get_unit_5, get_unit_6, get_unit_7
from build_math_u8_u11 import get_unit_8, get_unit_9, get_unit_10, get_unit_11

all_units = [
    get_unit_1(),
    get_unit_2(),
    get_unit_3(),
    get_unit_4(),
    get_unit_5(),
    get_unit_6(),
    get_unit_7(),
    get_unit_8(),
    get_unit_9(),
    get_unit_10(),
    get_unit_11()
]

target_path = r"D:\SpaceBook\SpaceBook Web\js\math_8_data.js"

js_content = "// Class 8 Mathematics — Comprehensive KPTBB Single National Curriculum 2022\n"
js_content += "// Complete units with verbatim theory, solved examples, step-by-step exercise solutions, formulas, and SLO assessments.\n"
js_content += "const MATH_8_DATA = " + json.dumps(all_units, indent=2, ensure_ascii=False) + ";\n"

if "window" in js_content or True:
    js_content += "\nif (typeof window !== 'undefined') { window.MATH_8_DATA = MATH_8_DATA; }\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully compiled {len(all_units)} units into {target_path}")
print(f"File size: {os.path.getsize(target_path):,} bytes")
