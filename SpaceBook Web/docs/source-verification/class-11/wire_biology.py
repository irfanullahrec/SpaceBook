# Wires js/bio_11_data.js into the shared SpaceBook files. Holds tmp/class-content-shared.lock only while patching.
from pathlib import Path
import os, time

root = Path(r'D:\SpaceBook\SpaceBook Web')
lock = root / 'tmp/class-content-shared.lock'
lock.parent.mkdir(exist_ok=True)
for attempt in range(60):
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
    except FileExistsError:
        time.sleep(2)
else:
    raise SystemExit('Shared lock occupied for 2 minutes; retry later without removing it.')
try:
    os.write(fd, f'class-11 biology pid={os.getpid()}'.encode())
    def patch(relative, old, new):
        p = root / relative
        text = p.read_text(encoding='utf-8')
        if new in text:
            return
        if text.count(old) != 1:
            raise ValueError(f'Ambiguous or missing patch target in {relative}: {old[:80]!r} (count={text.count(old)})')
        p.write_text(text.replace(old, new, 1), encoding='utf-8', newline='\n')
        print('patched', relative)

    patch('index.html', '  <script src="js/chem_11_data.js?v=20261011_class11"></script>',
          '  <script src="js/chem_11_data.js?v=20261011_class11"></script>\n  <script src="js/bio_11_data.js?v=20261012_1"></script>')

    patch('js/app.js', "const hasClass11Reader = classId === 'cls11' && (typeof CHEM_11_DATA !== 'undefined' || typeof PHYS_11_DATA !== 'undefined');",
          "const hasClass11Reader = classId === 'cls11' && (typeof CHEM_11_DATA !== 'undefined' || typeof PHYS_11_DATA !== 'undefined' || typeof BIO_11_DATA !== 'undefined');")
    patch('js/app.js', "? subs.filter(s => (s.id === 'cls11-chem' && typeof CHEM_11_DATA !== 'undefined') || (s.id === 'cls11-phy' && typeof PHYS_11_DATA !== 'undefined'))",
          "? subs.filter(s => (s.id === 'cls11-chem' && typeof CHEM_11_DATA !== 'undefined') || (s.id === 'cls11-phy' && typeof PHYS_11_DATA !== 'undefined') || (s.id === 'cls11-bio' && typeof BIO_11_DATA !== 'undefined'))")
    patch('js/app.js', "!(classId === 'cls11' && (subjId === 'cls11-phy' || subjId === 'cls11-chem'))",
          "!(classId === 'cls11' && (subjId === 'cls11-phy' || subjId === 'cls11-chem' || subjId === 'cls11-bio'))")
    patch('js/app.js', "if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio' || subjId === 'cls12-bio') {",
          "if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio' || subjId === 'cls11-bio' || subjId === 'cls12-bio') {")
    patch('js/app.js', "  if (subjKey === 'bio') {\n    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');",
          "  if (subjKey === 'bio') {\n    if (classId === 'cls11' && typeof BIO_11_DATA !== 'undefined') return BIO_11_DATA;\n    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');")
    patch('js/app.js', "  } else if (classId === 'cls11' && subjKey === 'chem') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderChemistry11Tab(ch, tabId);",
          "  } else if (classId === 'cls11' && subjKey === 'chem') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderChemistry11Tab(ch, tabId);\n  } else if (classId === 'cls11' && subjKey === 'bio') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderBiology11Tab(ch, tabId);")
    patch('js/app.js', "${classId === 'cls11' && (subjKey === 'phys' || subjKey === 'chem') ? 'Source review in progress'",
          "${classId === 'cls11' && (subjKey === 'phys' || subjKey === 'chem' || subjKey === 'bio') ? 'Source review in progress'")
    patch('js/app.js', "  if (classId === 'cls11' && subjKey === 'phys' && !chList[state.selectedSubjChapter]) state.selectedSubjChapter = 0;",
          "  if (classId === 'cls11' && (subjKey === 'phys' || subjKey === 'bio') && !chList[state.selectedSubjChapter]) state.selectedSubjChapter = 0;")
    patch('js/app.js', "  const pdfFile = classId === 'cls11' && subjKey === 'phys'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20physics/pdf/physicsfull.pdf'\n    :",
          "  const pdfFile = classId === 'cls11' && subjKey === 'phys'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20physics/pdf/physicsfull.pdf'\n    : classId === 'cls11' && subjKey === 'bio'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20bio/pdf/bio1.pdf'\n    :")
    # subjObj matching appears in openSubjectWorkspace and selectSubjectChapter (two identical fragments).
    p = root / 'js/app.js'
    text = p.read_text(encoding='utf-8')
    old = "subs.find(s => (classId === 'cls11' && subjKey === 'phys' && s.id === 'cls11-phy') ||"
    new = "subs.find(s => (classId === 'cls11' && subjKey === 'phys' && s.id === 'cls11-phy') || (classId === 'cls11' && subjKey === 'bio' && s.id === 'cls11-bio') ||"
    if new not in text:
        if text.count(old) < 1:
            raise ValueError('subjObj fragment not found')
        p.write_text(text.replace(old, new), encoding='utf-8', newline='\n'); print('patched js/app.js subjObj')
    patch('js/app.js', "  // 6. Search Class 12 Chapters",
          "  // Class 11 Biology: search the same source records as the active lesson.\n  if (typeof BIO_11_DATA !== 'undefined') {\n    BIO_11_DATA.forEach((ch, idx) => {\n      if (!biology11SourceSearchText(ch).toLowerCase().includes(q)) return;\n      results.push({ type: 'Chapter', badge: '🧬 Class 11 Biology', title: `${ch.number}: ${ch.title}`,\n        sub: 'Source-reviewed pages and aligned translations · review in progress',\n        action: () => { clearGlobalSearch(); openSubject('cls11', 'cls11-bio'); selectSubjectChapter('bio', idx, 'cls11'); } });\n    });\n  }\n\n  // 6. Search Class 12 Chapters")

    patch('js/data.js', '"id": "cls11-bio",\n        "name": "Biology",\n        "emoji": "🧬",\n        "chapters": 10',
          '"id": "cls11-bio",\n        "name": "Biology",\n        "emoji": "🧬",\n        "chapters": 13')
    patch('js/data.js', '      "action": "cls11-phy"\n    },\n',
          '      "action": "cls11-phy"\n    },\n    {\n      "id": "b-cls11-bio",\n      "classId": "cls11",\n      "className": "Class 11",\n      "subject": "Biology",\n      "title": "Biology 11th Class (HSSC-I) Test Edition",\n      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",\n      "size": "Source review in progress",\n      "pages": "13 Chapters",\n      "pdfPath": "",\n      "color": "#15803d",\n      "icon": "🧬",\n      "available": true,\n      "action": "cls11-bio"\n    },\n')

    css = root / 'css/style.css'
    ctext = css.read_text(encoding='utf-8')
    if '/* ===== Class 11 Biology source reader ===== */' not in ctext:
        block = (Path(__file__).parent / 'bio11.css').read_text(encoding='utf-8')
        ctext = ctext.rstrip('\n') + '\n\n' + block.strip('\n') + '\n'
        css.write_text(ctext, encoding='utf-8', newline='\n'); print('patched css/style.css')
    print('wiring complete')
finally:
    os.close(fd)
    lock.unlink()
