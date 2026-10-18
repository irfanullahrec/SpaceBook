from pathlib import Path
import os

root = Path(r'D:\SpaceBook\SpaceBook Web')
lock = root / 'tmp/class-content-shared.lock'
lock.parent.mkdir(exist_ok=True)
try:
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
except FileExistsError:
    raise SystemExit('Shared lock occupied; retry later without removing it.')
try:
    os.write(fd, f'class-11 pid={os.getpid()}'.encode())
    def patch(relative, old, new):
        p = root / relative
        text = p.read_text(encoding='utf-8')
        if new in text:
            return
        if text.count(old) != 1:
            raise ValueError(f'Ambiguous patch: {relative}')
        p.write_text(text.replace(old, new, 1), encoding='utf-8', newline='\n')
    patch('index.html', '  <script src="js/phys_12_data.js?v=20261005_1"></script>',
          '  <script src="js/phys_11_data.js?v=20261009_1"></script>\n  <script src="js/phys_12_data.js?v=20261005_1"></script>')
    patch('js/app.js', "subjId === 'cls10-phy' || subjId === 'cls12-phy') {",
          "subjId === 'cls10-phy' || subjId === 'cls11-phy' || subjId === 'cls12-phy') {")
    patch('js/app.js', "  if (subjKey === 'phys') {\n    if (classId === 'cls12'",
          "  if (subjKey === 'phys') {\n    if (classId === 'cls11' && typeof PHYS_11_DATA !== 'undefined') return PHYS_11_DATA;\n    if (classId === 'cls12'")
    patch('js/app.js', "  if (classId === 'cls11' && subjKey === 'phys') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = tabId === 'lesson'\n      ? renderPhysics11Source(ch)\n      : tabId === 'slos' && ch.id !== 'phys11-front-matter'\n        ? renderPhysics11Source({ sections: ch.sections.filter(sec => sec.layout === 'outcomes') })\n        : ch.id === 'phys11-front-matter'\n          ? '<p>This front matter contains no textbook exercises, formulas, or worked examples.</p>'\n          : '<p>No source-reviewed material has been added to this tab yet. This unit is still being transcribed.</p>';",
          "  if (classId === 'cls11' && subjKey === 'phys') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderPhysics11Tab(ch, tabId);")
    patch('js/app.js', '<span class="math-sidebar-sub">${chList.length} Complete Units</span>',
          '<span class="math-sidebar-sub">${classId === \'cls11\' && subjKey === \'phys\' ? \'Source review in progress\' : `${chList.length} Complete Units`}</span>')
    patch('js/data.js', '"id": "cls11-phy",\n        "name": "Physics",\n        "emoji": "⚡",\n        "chapters": 11',
          '"id": "cls11-phy",\n        "name": "Physics",\n        "emoji": "⚡",\n        "chapters": 10')
    patch('js/app.js', '  // 6. Search Class 12 Chapters',
          "  // Class 11 Physics: use the same source records as the active lesson.\n  if (typeof PHYS_11_DATA !== 'undefined') {\n    PHYS_11_DATA.forEach((ch, idx) => {\n      if (!physics11SourceSearchText(ch).toLowerCase().includes(q)) return;\n      results.push({ type: 'Chapter', badge: '⚛️ Class 11 Physics', title: `${ch.number}: ${ch.title}`,\n        sub: 'Source-reviewed pages and aligned translations · review in progress',\n        action: () => { clearGlobalSearch(); openSubject('cls11', 'cls11-phy'); selectSubjectChapter('phys', idx, 'cls11'); } });\n    });\n  }\n\n  // 6. Search Class 12 Chapters")
    patch('js/app.js', "  const theme = SUBJECT_THEMES[subjKey] || SUBJECT_THEMES.math;\n  const chList = getSubjectChapterList(subjKey, classId);\n  const subjName =",
          "  const theme = SUBJECT_THEMES[subjKey] || SUBJECT_THEMES.math;\n  const chList = getSubjectChapterList(subjKey, classId);\n  if (classId === 'cls11' && subjKey === 'phys' && !chList[state.selectedSubjChapter]) state.selectedSubjChapter = 0;\n  const subjName =")
    patch('js/app.js', "  const pdfFile = (subjObj && subjObj.pdf) ? subjObj.pdf : (matchedBook && matchedBook.pdfPath ? matchedBook.pdfPath : `assets/books/${cls.name.replace(' ', '-')}-${subjName}-KPK.pdf`);",
          "  const pdfFile = classId === 'cls11' && subjKey === 'phys'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20physics/pdf/physicsfull.pdf'\n    : (subjObj && subjObj.pdf) ? subjObj.pdf : (matchedBook && matchedBook.pdfPath ? matchedBook.pdfPath : `assets/books/${cls.name.replace(' ', '-')}-${subjName}-KPK.pdf`);")
    patch('js/app.js', "  const subjObj = subs.find(s => s.id === state.activeSubject || s.id === 'cls12-' + subjKey",
          "  const subjObj = subs.find(s => (classId === 'cls11' && subjKey === 'phys' && s.id === 'cls11-phy') || s.id === state.activeSubject || s.id === 'cls12-' + subjKey")
finally:
    os.close(fd)
    lock.unlink()
