# -*- coding: utf-8 -*-
"""
Builds D:\SpaceBook\SpaceBook Web\js\english_8_data.js from Units 1 to 8.
With cross-compatibility aliases for all SpaceBook renderers.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from unit1_data import UNIT_1
from unit2_data import UNIT_2
from unit3_data import UNIT_3
from unit4_data import UNIT_4
from unit5_data import UNIT_5
from unit6_data import UNIT_6
from unit7_data import UNIT_7
from unit8_data import UNIT_8

all_units = [UNIT_1, UNIT_2, UNIT_3, UNIT_4, UNIT_5, UNIT_6, UNIT_7, UNIT_8]

# Add aliases for full compatibility with all app.js extraction routines
for u in all_units:
    if "exercise" in u:
        ex = u["exercise"]
        if "mcqs" in ex and "textbookMcqs" not in ex:
            ex["textbookMcqs"] = ex["mcqs"]
        if "shortQuestions" in ex and "comprehension" not in ex:
            ex["comprehension"] = ex["shortQuestions"]
        if "dictionaryWords" not in ex and "words" in u:
            ex["dictionaryWords"] = u["words"]

output_file = r'D:\SpaceBook\SpaceBook Web\js\english_8_data.js'

js_content = """/**
 * TuitionHub - Class 8 English Comprehensive Dataset (KPK Textbook Board)
 * Unabridged Units with full verbatim texts, Urdu & Pashto line-by-line translations,
 * complete textbook exercises, grammar activities, and Board SLO Suites.
 */
const ENGLISH_8_DATA = """ + json.dumps(all_units, ensure_ascii=False, indent=2) + """;

if (typeof window !== 'undefined') {
  window.ENGLISH_8_DATA = ENGLISH_8_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ENGLISH_8_DATA };
}
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully wrote {len(all_units)} units to {output_file}!")
file_size = os.path.getsize(output_file)
print(f"File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
