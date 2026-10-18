from pathlib import Path
import os, time
root = Path(r'D:\SpaceBook\SpaceBook Web')
lock = root / 'tmp/class-content-shared.lock'
for attempt in range(60):
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
    except FileExistsError:
        time.sleep(2)
else:
    raise SystemExit('lock busy')
try:
    p = root / 'js/data.js'
    t = p.read_text(encoding='utf-8')
    old = '"id": "cls11-eng",\n        "name": "English",\n        "emoji": "📖",\n        "chapters": 9\n'
    new = old.replace('"chapters": 9', '"chapters": 24')
    if new not in t:
        assert t.count(old) == 1
        t = t.replace(old, new)
    anchor = '      "action": "cls11-stat"\n    },\n'
    entry = '    {\n      "id": "b-cls11-eng",\n      "classId": "cls11",\n      "className": "Class 11",\n      "subject": "English",\n      "title": "English 11th Class (HSSC-I)",\n      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",\n      "size": "Source review in progress",\n      "pages": "22 Units",\n      "pdfPath": "",\n      "color": "#0ea5e9",\n      "icon": "📖",\n      "available": true,\n      "action": "cls11-eng"\n    },\n'
    if '"id": "b-cls11-eng"' not in t:
        assert t.count(anchor) == 1
        t = t.replace(anchor, anchor + entry)
    p.write_text(t, encoding='utf-8', newline='\n')
    print('data.js ok')
finally:
    os.close(fd); lock.unlink()
