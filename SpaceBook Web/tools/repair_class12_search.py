"""Preserve search result closures and tolerate the supported chapter/topic shapes."""
from pathlib import Path
import os
root=Path(__file__).resolve().parents[1]
lock=root/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'Class12 search repair');os.close(fd);fd=None
 p=root/'js/app.js';text=p.read_text(encoding='utf-8')
 start=text.index('function handleGlobalSearch(query) {')
 end=text.index('function clearGlobalSearch() {',start)
 section=text[start:end]
 if 'spaceBookSearchActions' not in section:
  section=section.replace('  const q = (query || "").trim().toLowerCase();','  const q = String(query || "").trim().toLowerCase();\n  const searchText = value => String(value ?? "").toLowerCase();\n  window.spaceBookSearchActions = [];')
  for old,new in [
   ('b.title.toLowerCase()', 'searchText(b.title)'),
   ('b.subject.toLowerCase()', 'searchText(b.subject)'),
   ('b.className.toLowerCase()', 'searchText(b.className)'),
   ('ch.name.toLowerCase()', 'searchText(ch.name || ch.title)'),
   ('ch.title.toLowerCase()', 'searchText(ch.title || ch.name)'),
   ('t.title.toLowerCase()', 'searchText(typeof t === "string" ? t : t.title || t.name)'),
  ]:section=section.replace(old,new)
  section=section.replace('DATA.chapters[subjKey].forEach(ch => {','DATA.chapters[subjKey].forEach((ch, chapterIndex) => {\n          const chapterNumber = ch.num ?? ch.number ?? chapterIndex + 1;\n          const chapterName = ch.name || ch.title || "Untitled unit";')
  section=section.replace('`${subName} · Ch ${ch.num}: ${ch.name}`','`${subName} · Ch ${chapterNumber}: ${chapterName}`')
  section=section.replace('`${ch.topics} · Class 12 KPK Syllabus`','`${Array.isArray(ch.topics) ? ch.topics.length + " topics" : ch.topics || "Textbook content"} · Class 12 KPK Syllabus`')
  section=section.replace('openGenericChapterDetails("cls12", subjKey, subName, ch.num);','openGenericChapterDetails("cls12", subjKey, subName, chapterNumber);')
  section=section.replace('  dropdown.innerHTML = `\n    <div style="padding:0.4rem','  window.spaceBookSearchActions = results.slice(0, 15).map(result => result.action);\n  dropdown.innerHTML = `\n    <div style="padding:0.4rem')
  section=section.replace('onclick="(${r.action.toString()})()"','onclick="runGlobalSearchResult(${i})"')
  section+='function runGlobalSearchResult(index) {\n  const action = (window.spaceBookSearchActions || [])[index];\n  if (typeof action === "function") action();\n}\n\n'
  assert 'r.action.toString()' not in section
  text=text[:start]+section+text[end:]
  text=text.replace('function clearGlobalSearch() {','function clearGlobalSearch() {\n  window.spaceBookSearchActions = [];',1)
  temp=p.with_suffix('.js.search.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,p)
 p=root/'index.html';text=p.read_text(encoding='utf-8')
 text=text.replace('js/app.js?v=20261014_ws3_math12v1','js/app.js?v=20261014_ws3_math12v2')
 temp=p.with_suffix('.html.search.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,p)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print('Search repair applied without replacing saved textbook content.')
