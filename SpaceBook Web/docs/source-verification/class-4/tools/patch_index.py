import os
import sys

LOCK_FILE = r"D:\SpaceBook\SpaceBook Web\tmp\class-content-shared.lock"
HTML_FILE = r"D:\SpaceBook\SpaceBook Web\index.html"

if os.path.exists(LOCK_FILE):
    print("Locked by another process.")
    sys.exit(1)

with open(LOCK_FILE, "w", encoding="utf-8") as f:
    f.write("class4-agent")

try:
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    target_data = '<script src="js/math_5_data.js?v=20261007_1"></script>'
    entry_data = '<script src="js/math_4_data.js?v=20261011_1"></script>\n  '

    target_reader = '<script src="js/cls6_book_reader.js?v=20261010_33"></script>'
    entry_reader = '<script src="js/cls4_book_reader.js?v=20261011_1"></script>\n  '

    changed = False
    if "js/math_4_data.js" not in content and target_data in content:
        content = content.replace(target_data, entry_data + target_data)
        changed = True

    if "js/cls4_book_reader.js" not in content and target_reader in content:
        content = content.replace(target_reader, entry_reader + target_reader)
        changed = True

    if changed:
        with open(HTML_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated index.html successfully.")
    else:
        print("No change needed.")
finally:
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
