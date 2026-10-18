"""Small locked insertions for the Class 12 mathematics study view."""
from pathlib import Path
import os,re
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 os.write(fd,b'Class12 Mathematics view parity');os.close(fd);fd=None
 path=ROOT/'js/app.js';text=path.read_text(encoding='utf-8')
 changes=[
 ("function renderMathTopicSubContent(sec, ch, subTab, topicIdx) {\n", "function renderMathTopicSubContent(sec, ch, subTab, topicIdx) {\n  if (state.selectedClass === 'cls12' && typeof renderMath12TopicContent === 'function') {\n    const content = renderMath12TopicContent(sec, ch, subTab);\n    if (content !== null) return content;\n  }\n"),
 ("${state.selectedClass === 'cls12' || state.selectedClass === 'cls7'\n            ? `<button", "${state.selectedClass === 'cls12' && typeof renderMath12TopicTabs === 'function'\n            ? renderMath12TopicTabs(sec)\n            : state.selectedClass === 'cls7'\n            ? `<button"),
 ("if (state.selectedClass === 'cls12') return (ch && ch.slos) || {};", "if (state.selectedClass === 'cls12') return typeof getMath12StudyBank === 'function' ? getMath12StudyBank(ch) : (ch && ch.slos) || {};"),
 ("target.innerHTML = renderMathTopicSubContent(sec, ch, subTab, topicIdx >= 0 ? topicIdx : 0);", "target.innerHTML = renderMathTopicSubContent(sec, ch, subTab, topicIdx >= 0 ? topicIdx : 0);\n  if (state.selectedClass === 'cls12') typesetChapterMath(target);"),
 (": `Topic ${sec.id}`}</span>", ": state.selectedClass === 'cls12' ? `Topic ${(String(sec.title).match(/^\\d+(?:\\.\\d+)*/) || [idx + 1])[0]}` : `Topic ${sec.id}`}</span>"),
 ("const totalExercises = ch.exercises ? ch.exercises.length : 0;", "const totalExercises = ch.exercises ? (state.selectedClass === 'cls12' ? ch.exercises.filter(ex => ex.problems?.length || ex.sourceContextBlocks?.length).length : ch.exercises.length) : 0;")
 ]
 for before,after in changes:
  if after in text:continue
  assert text.count(before)==1, 'Missing or ambiguous insertion: '+before[:80]
  text=text.replace(before,after,1)
 temp=path.with_suffix('.js.math12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,path)
 path=ROOT/'index.html';text=path.read_text(encoding='utf-8')
 scripts='  <script src="js/math12_answer_repairs.js?v=20261018_1"></script>\n  <script src="js/math12_study_views.js?v=20261018_1"></script>\n  <script src="js/math12_class9_view.js?v=20261018_1"></script>\n'
 if 'js/math12_class9_view.js' not in text:
  anchor='  <script src="js/math12_translation_reader.js?v=20261008_1"></script>\n';assert anchor in text;text=text.replace(anchor,anchor+scripts)
 if 'js/math12_translation_completions.js' not in text:
  anchor='  <script src="js/math12_translation_reader.js?v=20261008_1"></script>'
  text=text.replace(anchor,'  <script src="js/math12_translation_completions.js?v=20261018_1"></script>\n'+anchor)
 if 'js/math12_unit9_practice.js' not in text:
  anchor='  <script src="js/math12_study_views.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,'  <script src="js/math12_unit9_practice.js?v=20261018_1"></script>\n'+anchor)
 for unit in [2,3,4,5,7,8,10,11,12]:
  filename=f'js/math12_unit{unit}_translations.js'
  if (ROOT/filename).exists() and filename not in text:
   anchor='  <script src="js/math12_translation_reader.js?v=20261008_1"></script>'
   assert anchor in text
   text=text.replace(anchor,f'  <script src="{filename}?v=20261018_1"></script>\n'+anchor)
 if (ROOT/'js/math12_unit6_source_recovery.js').exists() and 'js/math12_unit6_source_recovery.js' not in text:
  anchor='  <script src="js/math12_translation_completions.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,'  <script src="js/math12_unit6_source_recovery.js?v=20261018_1"></script>\n'+anchor)
 if (ROOT/'js/math12_unit6_exercise61_recovery.js').exists() and 'js/math12_unit6_exercise61_recovery.js' not in text:
  anchor='  <script src="js/math12_study_views.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,'  <script src="js/math12_unit6_exercise61_recovery.js?v=20261018_1"></script>\n'+anchor)
 if 'js/math12_legibility_recovery.js' not in text:
  anchor='  <script src="js/math12_answer_repairs.js?v=20261018_1"></script>'
  assert anchor in text
  text=text.replace(anchor,anchor+'\n  <script src="js/math12_legibility_recovery.js?v=20261018_1"></script>')
 if 'css/math12_class9_view.css' not in text:text=text.replace('</head>','  <link rel="stylesheet" href="css/math12_class9_view.css?v=20261018_1">\n</head>',1)
 text=re.sub(r'(js/app\.js\?v=[^"\s]+)(?=")',lambda m:m.group(1) if '_math12v' in m.group(1) else m.group(1)+'_math12v1',text)
 temp=path.with_suffix('.html.math12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,path)
finally:
 if fd is not None:os.close(fd)
 lock.unlink()
print('Class12 mathematics study hooks wired; shared surrounding content preserved.')
