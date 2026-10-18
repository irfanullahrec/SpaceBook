# Wires js/eng_11_data.js into the shared SpaceBook files. Holds tmp/class-content-shared.lock only while patching.
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
    os.write(fd, f'class-11 english pid={os.getpid()}'.encode())
    def patch(relative, old, new, count=1):
        p = root / relative
        text = p.read_text(encoding='utf-8')
        if new in text:
            return
        if text.count(old) != count:
            raise ValueError(f'Ambiguous or missing patch target in {relative}: {old[:80]!r} (count={text.count(old)})')
        p.write_text(text.replace(old, new), encoding='utf-8', newline='\n')
        print('patched', relative, old[:50])
    patch('index.html', '  <script src="js/stat_11_data.js?v=20261012_1"></script>',
          '  <script src="js/stat_11_data.js?v=20261012_1"></script>\n  <script src="js/eng_11_data.js?v=20261012_1"></script>')
    patch('js/app.js', "typeof STAT_11_DATA !== 'undefined');\n  if (!['cls1'", "typeof STAT_11_DATA !== 'undefined' || typeof ENG_11_DATA !== 'undefined');\n  if (!['cls1'")
    patch('js/app.js', "(s.id === 'cls11-stat' && typeof STAT_11_DATA !== 'undefined'))\n    : subs;",
          "(s.id === 'cls11-stat' && typeof STAT_11_DATA !== 'undefined') || (s.id === 'cls11-eng' && typeof ENG_11_DATA !== 'undefined'))\n    : subs;")
    patch('js/app.js', "subjId === 'cls11-bio' || subjId === 'cls11-stat')) && classId !== 'cls1'",
          "subjId === 'cls11-bio' || subjId === 'cls11-stat' || subjId === 'cls11-eng')) && classId !== 'cls1'")
    patch('js/app.js', "subjId === 'cls3-eng' || subjId === 'cls12-eng') {\n    state.activeSubject = \"eng\";",
          "subjId === 'cls3-eng' || subjId === 'cls12-eng' || subjId === 'cls11-eng') {\n    state.activeSubject = \"eng\";")
    patch('js/app.js', "function getSubjectChapterList(subjKey, classId) {\n  if (subjKey === 'math') return getMathChapterList(classId);\n  if (subjKey === 'eng') {\n",
          "function getSubjectChapterList(subjKey, classId) {\n  if (subjKey === 'math') return getMathChapterList(classId);\n  if (subjKey === 'eng') {\n    if ((classId === 'cls11' || state.selectedClass === 'cls11') && typeof ENG_11_DATA !== 'undefined') return ENG_11_DATA;\n")
    patch('js/app.js', "    container.innerHTML = renderStatistics11Tab(ch, tabId);\n  } else if (tabId === 'booktext'",
          "    container.innerHTML = renderStatistics11Tab(ch, tabId);\n  } else if (classId === 'cls11' && subjKey === 'eng') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderEnglish11Tab(ch, tabId);\n  } else if (tabId === 'booktext'")
    patch('js/app.js', "|| subjKey === 'stat') ? 'Source review in progress'", "|| subjKey === 'stat' || subjKey === 'eng') ? 'Source review in progress'")
    patch('js/app.js', "(subjKey === 'phys' || subjKey === 'bio' || subjKey === 'stat') && !chList[state.selectedSubjChapter]",
          "(subjKey === 'phys' || subjKey === 'bio' || subjKey === 'stat' || subjKey === 'eng') && !chList[state.selectedSubjChapter]")
    patch('js/app.js', "    : classId === 'cls11' && subjKey === 'stat'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20stastic/pdf/Statistics%20book%2011th%20KPK_part_01_of_08.pdf'\n    :",
          "    : classId === 'cls11' && subjKey === 'stat'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20stastic/pdf/Statistics%20book%2011th%20KPK_part_01_of_08.pdf'\n    : classId === 'cls11' && subjKey === 'eng'\n    ? 'file:///D:/SpaceBook/Books/11th/11english/pdf/english1.pdf'\n    :")
    p = root / 'js/app.js'
    text = p.read_text(encoding='utf-8')
    old = "(classId === 'cls11' && subjKey === 'stat' && s.id === 'cls11-stat') ||"
    new = old + " (classId === 'cls11' && subjKey === 'eng' && s.id === 'cls11-eng') ||"
    if new not in text:
        if text.count(old) < 1:
            raise ValueError('subjObj fragment not found')
        p.write_text(text.replace(old, new), encoding='utf-8', newline='\n'); print('patched js/app.js subjObj')
    patch('js/app.js', "  // Class 11 Statistics: search the same source records as the active lesson.",
          "  // Class 11 English: search the same source records as the active lesson.\n  if (typeof ENG_11_DATA !== 'undefined') {\n    ENG_11_DATA.forEach((ch, idx) => {\n      if (!english11SourceSearchText(ch).toLowerCase().includes(q)) return;\n      results.push({ type: 'Chapter', badge: '📖 Class 11 English', title: `${ch.number}: ${ch.title}`,\n        sub: 'Source-reviewed pages and aligned translations · review in progress',\n        action: () => { clearGlobalSearch(); openSubject('cls11', 'cls11-eng'); selectSubjectChapter('eng', idx, 'cls11'); } });\n    });\n  }\n\n  // Class 11 Statistics: search the same source records as the active lesson.")
    print('wiring complete')
finally:
    os.close(fd)
    lock.unlink()
