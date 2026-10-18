# Wires js/stat_11_data.js into the shared SpaceBook files. Holds tmp/class-content-shared.lock only while patching.
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
    os.write(fd, f'class-11 statistics pid={os.getpid()}'.encode())
    def patch(relative, old, new, count=1):
        p = root / relative
        text = p.read_text(encoding='utf-8')
        if new in text:
            return
        if text.count(old) != count:
            raise ValueError(f'Ambiguous or missing patch target in {relative}: {old[:80]!r} (count={text.count(old)})')
        p.write_text(text.replace(old, new), encoding='utf-8', newline='\n')
        print('patched', relative, old[:50])

    patch('index.html', '  <script src="js/bio_11_data.js?v=20261012_1"></script>',
          '  <script src="js/bio_11_data.js?v=20261012_1"></script>\n  <script src="js/stat_11_data.js?v=20261012_1"></script>')
    patch('js/app.js', "typeof BIO_11_DATA !== 'undefined');\n  if (!['cls1'", "typeof BIO_11_DATA !== 'undefined' || typeof STAT_11_DATA !== 'undefined');\n  if (!['cls1'")
    patch('js/app.js', "(s.id === 'cls11-bio' && typeof BIO_11_DATA !== 'undefined'))",
          "(s.id === 'cls11-bio' && typeof BIO_11_DATA !== 'undefined') || (s.id === 'cls11-stat' && typeof STAT_11_DATA !== 'undefined'))")
    patch('js/app.js', "subjId === 'cls11-chem' || subjId === 'cls11-bio')) && classId !== 'cls1'",
          "subjId === 'cls11-chem' || subjId === 'cls11-bio' || subjId === 'cls11-stat')) && classId !== 'cls1'")
    patch('js/app.js', "  } else if (subjId === 'cls12-stat') {", "  } else if (subjId === 'cls12-stat' || subjId === 'cls11-stat') {")
    patch('js/app.js', '    "cls11-eng": "Books/11th/Gemini_Generated_Image_ol8qruol8qruol8q.jfif",\n',
          '    "cls11-eng": "Books/11th/Gemini_Generated_Image_ol8qruol8qruol8q.jfif",\n    "cls11-stat": "Books/12th/Statistics.jpg",\n')
    patch('js/app.js', "  if (subjKey === 'stat' && classId === 'cls12' && typeof STAT_12_DATA !== 'undefined') return STAT_12_DATA;",
          "  if (subjKey === 'stat' && classId === 'cls11' && typeof STAT_11_DATA !== 'undefined') return STAT_11_DATA;\n  if (subjKey === 'stat' && classId === 'cls12' && typeof STAT_12_DATA !== 'undefined') return STAT_12_DATA;")
    patch('js/app.js', "    container.innerHTML = renderBiology11Tab(ch, tabId);\n  } else if (tabId === 'booktext'",
          "    container.innerHTML = renderBiology11Tab(ch, tabId);\n  } else if (classId === 'cls11' && subjKey === 'stat') {\n    if (subBar) { subBar.style.display = 'none'; subBar.innerHTML = ''; }\n    container.innerHTML = renderStatistics11Tab(ch, tabId);\n  } else if (tabId === 'booktext'")
    patch('js/app.js', "subjKey === 'chem' || subjKey === 'bio') ? 'Source review in progress'",
          "subjKey === 'chem' || subjKey === 'bio' || subjKey === 'stat') ? 'Source review in progress'")
    patch('js/app.js', "(subjKey === 'phys' || subjKey === 'bio') && !chList[state.selectedSubjChapter]",
          "(subjKey === 'phys' || subjKey === 'bio' || subjKey === 'stat') && !chList[state.selectedSubjChapter]")
    patch('js/app.js', "    ? 'file:///D:/SpaceBook/Books/11th/11th%20bio/pdf/bio1.pdf'\n    :",
          "    ? 'file:///D:/SpaceBook/Books/11th/11th%20bio/pdf/bio1.pdf'\n    : classId === 'cls11' && subjKey === 'stat'\n    ? 'file:///D:/SpaceBook/Books/11th/11th%20stastic/pdf/Statistics%20book%2011th%20KPK_part_01_of_08.pdf'\n    :")
    p = root / 'js/app.js'
    text = p.read_text(encoding='utf-8')
    old = "(classId === 'cls11' && subjKey === 'bio' && s.id === 'cls11-bio') ||"
    new = old + " (classId === 'cls11' && subjKey === 'stat' && s.id === 'cls11-stat') ||"
    if new not in text:
        if text.count(old) < 1:
            raise ValueError('subjObj fragment not found')
        p.write_text(text.replace(old, new), encoding='utf-8', newline='\n'); print('patched js/app.js subjObj')
    patch('js/app.js', "  // Class 11 Biology: search the same source records as the active lesson.",
          "  // Class 11 Statistics: search the same source records as the active lesson.\n  if (typeof STAT_11_DATA !== 'undefined') {\n    STAT_11_DATA.forEach((ch, idx) => {\n      if (!statistics11SourceSearchText(ch).toLowerCase().includes(q)) return;\n      results.push({ type: 'Chapter', badge: '📊 Class 11 Statistics', title: `${ch.number}: ${ch.title}`,\n        sub: 'Source-reviewed pages and aligned translations · review in progress',\n        action: () => { clearGlobalSearch(); openSubject('cls11', 'cls11-stat'); selectSubjectChapter('stat', idx, 'cls11'); } });\n    });\n  }\n\n  // Class 11 Biology: search the same source records as the active lesson.")

    patch('js/data.js', '"id": "cls11-bio",\n        "name": "Biology",\n        "emoji": "🧬",\n        "chapters": 13\n      },\n',
          '"id": "cls11-bio",\n        "name": "Biology",\n        "emoji": "🧬",\n        "chapters": 13\n      },\n      {\n        "id": "cls11-stat",\n        "name": "Statistics",\n        "emoji": "📊",\n        "chapters": 13\n      },\n')
    patch('js/data.js', '      "action": "cls11-bio"\n    },\n',
          '      "action": "cls11-bio"\n    },\n    {\n      "id": "b-cls11-stat",\n      "classId": "cls11",\n      "className": "Class 11",\n      "subject": "Statistics",\n      "title": "Statistics 11th Class (HSSC-I)",\n      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",\n      "size": "Source review in progress",\n      "pages": "9 Units",\n      "pdfPath": "",\n      "color": "#7c3aed",\n      "icon": "📊",\n      "available": true,\n      "action": "cls11-stat"\n    },\n')

    js = root / 'js/stat_11_data.js'
    jt = js.read_text(encoding='utf-8')
    if 'function statistics11SourceSearchText' not in jt:
        jt = jt.rstrip('\n') + "\n\nfunction statistics11SourceSearchText(ch) {\n  return [ch.title, ch.titleUrdu, ch.titlePashto, ...(ch.sections || []).flatMap(sec => [\n    sec.title, sec.headingUrdu, sec.headingPashto,\n    ...(sec.paras || []).flatMap(p => [p.original, p.urdu, p.pashto]),\n    ...(sec.figures || []).flatMap(f => [f.caption, f.captionUrdu, f.captionPashto]),\n    ...(sec.tables || []).flatMap(t => [t.caption, ...(t.rows || []).flat().map(c => typeof c === 'string' ? c : c.en)])\n  ])].filter(Boolean).join(' ');\n}\n"
        js.write_text(jt, encoding='utf-8', newline='\n'); print('added search function')
    print('wiring complete')
finally:
    os.close(fd)
    lock.unlink()
