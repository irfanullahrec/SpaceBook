"""Small Class 11-only changes to the existing shared Mathematics workspace."""
from pathlib import Path
import os,re
APP=Path(__file__).resolve().parents[4]
lock=APP/'tmp'/'class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'Class 11 Mathematics view alignment\n')
    file=APP/'js'/'app.js';text=file.read_text(encoding='utf-8');before=text
    replacements=[
      ("function getComprehensiveChapterSLOBank(ch) {",
       "function getComprehensiveChapterSLOBank(ch) {\n  if (state.selectedClass === 'cls11') return typeof window.getMath11QuestionBank === 'function' ? window.getMath11QuestionBank(ch) : {};"),
      ("DOLLAR{classId === 'cls12' || classId === 'cls7' ? BACKTICKDOLLAR{chList.length} textbook unitsBACKTICK : BACKTICKDOLLAR{chList.length} Complete Solved UnitsBACKTICK}",
       "DOLLAR{classId === 'cls12' || classId === 'cls7' || classId === 'cls11' ? BACKTICKDOLLAR{chList.length} textbook unitsBACKTICK : BACKTICKDOLLAR{chList.length} Complete Solved UnitsBACKTICK}"),
      (": classId === 'cls9'\n              ? BACKTICK<div class=\"math-pdf-btn\" aria-label=\"Class 9 mathematics lessons use typeset equations\">",
       ": classId === 'cls9' || classId === 'cls11'\n              ? BACKTICK<div class=\"math-pdf-btn\" aria-label=\"Mathematics lessons use typeset equations\">"),
      ("|| ((state.selectedClass === 'cls12' || state.selectedClass === 'cls7') ? 0 : 63);",
       "|| ((state.selectedClass === 'cls12' || state.selectedClass === 'cls7' || state.selectedClass === 'cls11') ? 0 : 63);")
    ]
    for old,new in replacements:
        old=old.replace('BACKTICK',chr(96)).replace('DOLLAR','$');new=new.replace('BACKTICK',chr(96)).replace('DOLLAR','$')
        if new in text:continue
        assert text.count(old)==1,old
        text=text.replace(old,new,1)
    assert file.read_text(encoding='utf-8')==before,'Concurrent controller edit'
    if text!=before:file.write_text(text,encoding='utf-8',newline='\n')
    file=APP/'index.html';text=file.read_text(encoding='utf-8');before=text
    for name in ['math_11_data.js','math11_reader.js']:
        text,n=re.subn(r'(src="js/'+re.escape(name)+r')(?:\?[^"]*)?(")',r'\1?v=20261018_answers1\2',text)
        assert n==1,(name,n)
    assert file.read_text(encoding='utf-8')==before,'Concurrent shell edit'
    if text!=before:file.write_text(text,encoding='utf-8',newline='\n')
finally:
    os.close(fd)
    lock.unlink()
reader=APP/'js'/'math11_reader.js';original=reader.read_text(encoding='utf-8')
text=original.replace('m8-','m11-').replace('m8ShowAll','m11ShowAll').replace('math8_reader\\.js','math11_reader\\.js')
assert reader.read_text(encoding='utf-8')==original
if text!=original:reader.write_text(text,encoding='utf-8',newline='\n')
print('Class 11 workspace uses its own bank, correct unit label, and scoped reader styles.')
