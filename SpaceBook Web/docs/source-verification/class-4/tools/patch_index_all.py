import os
import sys

LOCK_FILE = r"D:\SpaceBook\SpaceBook Web\tmp\class-content-shared.lock"
HTML_FILE = r"D:\SpaceBook\SpaceBook Web\index.html"

if os.path.exists(LOCK_FILE):
    print("Locked by another process.")
    sys.exit(1)

with open(LOCK_FILE, "w", encoding="utf-8") as f:
    f.write("class4-agent-all")

try:
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # The scripts to register
    cls4_scripts = [
        '<script src="js/english_4_data.js?v=20261011_1"></script>',
        '<script src="js/general_science_4_data.js?v=20261011_1"></script>',
        '<script src="js/social_studies_4_data.js?v=20261011_1"></script>',
        '<script src="js/islamiat_4_data.js?v=20261011_1"></script>',
        '<script src="js/pashto_4_data.js?v=20261011_1"></script>'
    ]

    target = '<script src="js/math_4_data.js?v=20261011_1"></script>'
    insertion = "\n  ".join(cls4_scripts)

    if target in content and "js/english_4_data.js" not in content:
        content = content.replace(target, target + "\n  " + insertion)
        with open(HTML_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Registered remaining Class 4 scripts in index.html.")
    else:
        print("Already registered or target not found.")
finally:
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
