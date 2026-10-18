# One-time generic wiring for additional Class 11 source readers (js/<key>_11_data.js registering into window.CLASS11_BOOKS).
# Holds tmp/class-content-shared.lock only while patching app.js. Safe to rerun.
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
    os.write(fd, f'class-11 registry pid={os.getpid()}'.encode())
    p = root / 'js/app.js'
    text = p.read_text(encoding='utf-8')
    def patch(old, new):
        global text
        if new in text:
            return
        if text.count(old) != 1:
            raise ValueError(f'Ambiguous or missing patch target: {old[:80]!r} (count={text.count(old)})')
        text = text.replace(old, new); print('patched', old[:50].replace('\n', ' '))
    ANY = "(window.CLASS11_BOOKS && Object.values(window.CLASS11_BOOKS).some(b => b.subjectId === %s))"
    # helpers + chapter list
    patch("function getSubjectChapterList(subjKey, classId) {\n  if (subjKey === 'math') return getMathChapterList(classId);",
          "function class11BookByKey(key) { const r = window.CLASS11_BOOKS || {}; return r[key] || null; }\nfunction class11BookBySubject(id) { const r = window.CLASS11_BOOKS || {}; return Object.values(r).find(b => b.subjectId === id) || null; }\n\nfunction getSubjectChapterList(subjKey, classId) {\n  if (subjKey === 'math') return getMathChapterList(classId);\n  { const _b11 = class11BookByKey(subjKey); if (_b11 && (classId === 'cls11' || state.selectedClass === 'cls11')) return _b11.data; }")
    patch("  const hasClass11Reader = classId === 'cls11' && (", "  const hasClass11Reader = classId === 'cls11' && (Object.keys(window.CLASS11_BOOKS || {}).length > 0 || ")
    patch("(s.id === 'cls11-eng' && typeof ENG_11_DATA !== 'undefined'))\n    : subs;",
          "(s.id === 'cls11-eng' && typeof ENG_11_DATA !== 'undefined') || " + (ANY % 's.id') + ")\n    : subs;")
    patch("|| subjId === 'cls11-stat' || subjId === 'cls11-eng')) && classId !== 'cls1'",
          "|| subjId === 'cls11-stat' || subjId === 'cls11-eng' || " + (ANY % 'subjId') + ")) && classId !== 'cls1'")
    patch("  if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio' || subjId === 'cls11-bio' || subjId === 'cls12-bio') {",
          "  if (classId === 'cls11' && class11BookBySubject(subjId)) {\n    state.activeSubject = subj.id;\n    openSubjectWorkspace(classId, class11BookBySubject(subjId).key, subj);\n    return;\n  }\n  if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio' || subjId === 'cls11-bio' || subjId === 'cls12-bio') {")
    patch("(subjKey === 'phys' || subjKey === 'bio' || subjKey === 'stat' || subjKey === 'eng') && !chList[state.selectedSubjChapter]",
          "(subjKey === 'phys' || subjKey === 'bio' || subjKey === 'stat' || subjKey === 'eng' || class11BookByKey(subjKey)) && !chList[state.selectedSubjChapter]")
    patch("    : (subjObj && subjObj.pdf) ? subjObj.pdf :",
          "    : (classId === 'cls11' && class11BookByKey(subjKey) && class11BookByKey(subjKey).pdf) ? class11BookByKey(subjKey).pdf\n    : (subjObj && subjObj.pdf) ? subjObj.pdf :")
    patch("subjKey === 'stat' || subjKey === 'eng') ? 'Source review in progress'",
          "subjKey === 'stat' || subjKey === 'eng' || class11BookByKey(subjKey)) ? 'Source review in progress'")
    patch("  let tabs = [];\n  if (isEng) {",
          "  let tabs = [];\n  if (classId === 'cls11' && class11BookByKey(subjKey)) {\n    tabs = class11BookByKey(subjKey).tabs;\n  } else if (isEng) {")
    patch("  if (classId === 'cls11' && subjKey === 'phys') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderPhysics11Tab(ch, tabId);",
          "  if (classId === 'cls11' && class11BookByKey(subjKey)) {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = class11BookByKey(subjKey).render(ch, tabId);\n  } else if (classId === 'cls11' && subjKey === 'phys') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderPhysics11Tab(ch, tabId);")
    patch("  // Class 11 English: search the same source records as the active lesson.",
          "  // Class 11 registry books (Islamiat, HPE, Urdu, ...): search their source records.\n  Object.values(window.CLASS11_BOOKS || {}).forEach(book => {\n    (book.data || []).forEach((ch, idx) => {\n      if (!book.searchText(ch).toLowerCase().includes(q)) return;\n      results.push({ type: 'Chapter', badge: book.badge, title: `${ch.number}: ${ch.title}`,\n        sub: 'Source-reviewed pages and aligned translations · review in progress',\n        action: () => { clearGlobalSearch(); openSubject('cls11', book.subjectId); selectSubjectChapter(book.key, idx, 'cls11'); } });\n    });\n  });\n\n  // Class 11 English: search the same source records as the active lesson.")
    p.write_text(text, encoding='utf-8', newline='\n')
    print('registry wiring complete')
finally:
    os.close(fd)
    lock.unlink()
