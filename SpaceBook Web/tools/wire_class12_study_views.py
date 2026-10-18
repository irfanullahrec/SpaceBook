"""Minimal shared shell hooks. All Class12 behavior lives in its addon."""
from pathlib import Path
import os
root=Path(__file__).resolve().parents[1]
lock=root/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'Class12 study view wiring');os.close(fd);fd=None
 p=root/'js/app.js';text=p.read_text(encoding='utf-8')
 anchor="  const activeTab = state.activeSubjTab || tabs[0].id;"
 insert="  if (classId === 'cls12' && typeof getClass12SubjectTabs === 'function') tabs = getClass12SubjectTabs(subjKey, tabs);\n\n"
 if insert not in text:
  assert text.count(anchor)==1
  text=text.replace(anchor,insert+anchor,1)
 temp=p.with_suffix('.js.class12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,p)
 p=root/'index.html';text=p.read_text(encoding='utf-8')
 if 'js/class12_study_views.js' not in text:
  anchor='  <script src="js/math12_class9_view.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,anchor+'\n  <script src="js/class12_study_views.js?v=20261018_1"></script>')
 if 'css/class12_study_views.css' not in text:
  text=text.replace('</head>','  <link rel="stylesheet" href="css/class12_study_views.css?v=20261018_1">\n</head>',1)
 if 'js/chem12_unit13_study.js' not in text:
  anchor='  <script src="js/class12_study_views.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,'  <script src="js/chem12_unit13_study.js?v=20261018_1"></script>\n'+anchor)
 if 'js/phys12_unit11_study.js' not in text:
  anchor='  <script src="js/class12_study_views.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,'  <script src="js/phys12_unit11_study.js?v=20261018_1"></script>\n'+anchor)
 temp=p.with_suffix('.html.class12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,p)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print('Class12 subject view hooks wired.')
