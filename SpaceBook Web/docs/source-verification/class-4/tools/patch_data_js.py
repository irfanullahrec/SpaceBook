import os
import sys

LOCK_FILE = r"D:\SpaceBook\SpaceBook Web\tmp\class-content-shared.lock"
DATA_FILE = r"D:\SpaceBook\SpaceBook Web\js\data.js"

if os.path.exists(LOCK_FILE):
    print("Locked by another process.")
    sys.exit(1)

with open(LOCK_FILE, "w", encoding="utf-8") as f:
    f.write("class4-agent-data")

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacement for cls4 in data.js to align with exact KPK textbooks
    old_cls4 = """    "cls4": [
      { "id": "cls4-eng",  "name": "English",         "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 14 },
      { "id": "cls4-urdu", "name": "Urdu",            "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 14 },
      { "id": "cls4-math", "name": "Mathematics",     "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 10 },
      { "id": "cls4-sci",  "name": "General Science", "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 10 },
      { "id": "cls4-sst",  "name": "Social Studies",  "nameUrdu": "معاشرتی علوم",   "emoji": "🗺️", "chapters": 8 },
      { "id": "cls4-isl",  "name": "Islamyat",        "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 10 }
    ],"""

    new_cls4 = """    "cls4": [
      { "id": "cls4-math",   "name": "Mathematics",     "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 10, "hasMath": true },
      { "id": "cls4-eng",    "name": "English",         "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 13, "hasEng": true },
      { "id": "cls4-sci",    "name": "General Science", "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 10, "hasGenSci": true },
      { "id": "cls4-sst",    "name": "Social Studies",  "nameUrdu": "معاشرتی علوم",   "emoji": "🗺️", "chapters": 6,  "hasSst": true },
      { "id": "cls4-isl",    "name": "Islamyat",        "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 7,  "hasIsl": true },
      { "id": "cls4-pashto", "name": "Pashto",          "nameUrdu": "پښتو لازمي",     "emoji": "📚", "chapters": 18, "hasPashto": true }
    ],"""

    if old_cls4 in content:
        content = content.replace(old_cls4, new_cls4)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated cls4 subjects in data.js.")
    else:
        print("Target pattern not found in data.js.")
finally:
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
