import os
import sys

LOCK_FILE = r"D:\SpaceBook\SpaceBook Web\tmp\class-content-shared.lock"
APP_FILE = r"D:\SpaceBook\SpaceBook Web\js\app.js"

if os.path.exists(LOCK_FILE):
    print("Locked by another process.")
    sys.exit(1)

with open(LOCK_FILE, "w", encoding="utf-8") as f:
    f.write("class4-agent-app")

try:
    with open(APP_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update goToSubjects check to include cls4
    old_check = "if (!['cls1', 'cls2', 'cls3', 'cls5', 'cls6', 'cls7', 'cls8', 'cls9', 'cls10', 'cls12'].includes(classId) && !hasClass11Reader) {"
    new_check = "if (!['cls1', 'cls2', 'cls3', 'cls4', 'cls5', 'cls6', 'cls7', 'cls8', 'cls9', 'cls10', 'cls12'].includes(classId) && !hasClass11Reader) {"

    # 2. Update openSubject check to include cls4
    old_router = "if (classId !== 'cls9' && classId !== 'cls10' && classId !== 'cls5' && classId !== 'cls6' && classId !== 'cls7' && classId !== 'cls8' && !(classId === 'cls11' && (subjId === 'cls11-phy' || subjId === 'cls11-chem')) && classId !== 'cls1' && classId !== 'cls2' && classId !== 'cls3' && classId !== 'cls12') {"
    new_router = "if (classId !== 'cls9' && classId !== 'cls10' && classId !== 'cls4' && classId !== 'cls5' && classId !== 'cls6' && classId !== 'cls7' && classId !== 'cls8' && !(classId === 'cls11' && (subjId === 'cls11-phy' || subjId === 'cls11-chem')) && classId !== 'cls1' && classId !== 'cls2' && classId !== 'cls3' && classId !== 'cls12') {"

    changed = False
    if old_check in content:
        content = content.replace(old_check, new_check)
        changed = True

    if old_router in content:
        content = content.replace(old_router, new_router)
        changed = True

    if changed:
        with open(APP_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated app.js router to include cls4!")
    else:
        print("Target patterns not found in app.js.")
finally:
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
