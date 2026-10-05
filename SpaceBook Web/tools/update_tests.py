import re

# --- 1. Update tools/validate.js ---
val_path = r'D:\SpaceBook\SpaceBook Web\tools\validate.js'
with open(val_path, 'r', encoding='utf-8') as f:
    val_content = f.read()

# Add 11 files to DATA_FILES
old_data_files = """  'islamyat_3_data.js', 'nazira_3_data.js', 'english_3_data.js', 'gk_3_data.js', 'pashto_3_data.js',
  'math_12_data.js', 'phys_12_data.js', 'chem_12_data.js', 'stat_12_data.js'
];"""

new_data_files = """  'islamyat_3_data.js', 'nazira_3_data.js', 'english_3_data.js', 'gk_3_data.js', 'pashto_3_data.js',
  'math_12_data.js', 'phys_12_data.js', 'chem_12_data.js', 'stat_12_data.js',
  'english_12_data.js', 'pakstudy_12_data.js', 'urdu_12_data.js',
  'biology_12_data.js', 'computer_12_data.js', 'civics_12_data.js',
  'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js',
  'islamic_history_12_data.js', 'quran_12_data.js'
];"""

val_content_norm = val_content.replace('\r\n', '\n')
if old_data_files in val_content_norm:
    val_content_norm = val_content_norm.replace(old_data_files, new_data_files)
    print("Updated DATA_FILES in validate.js")
else:
    print("WARNING: old_data_files not found in validate.js!")

# Update books count check from 24 to 35
val_content_norm = val_content_norm.replace(
    "check('books = ' + D.books.length, D.books.length === 24, 'got ' + D.books.length);",
    "check('books = ' + D.books.length, D.books.length === 35, 'got ' + D.books.length);"
)

# Update Class 12 registration check
val_content_norm = val_content_norm.replace(
    "check('Class 12 Maths, Physics, Chemistry and Statistics registered', ['cls12-math','cls12-phy','cls12-chem','cls12-stat'].every(id => D.subjects.cls12.some(s => s.id === id)));",
    "check('Class 12 all 15 subjects registered', D.subjects && D.subjects.cls12 && D.subjects.cls12.length === 15 && ['cls12-math','cls12-phy','cls12-chem','cls12-stat','cls12-eng','cls12-urdu','cls12-bio','cls12-pak','cls12-comp','cls12-civics','cls12-econ','cls12-hpe','cls12-islopt','cls12-islhist','cls12-quran'].every(id => D.subjects.cls12.some(s => s.id === id)));"
)

# Update Class 12 PDF links check
val_content_norm = val_content_norm.replace(
    "check('Class 12 textbook PDF links available', ['b-cls12-math','b-cls12-phys','b-cls12-chem','b-cls12-stat'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath)));",
    "check('Class 12 textbook PDF links available for all 15 books', ['b-cls12-math','b-cls12-phys','b-cls12-chem','b-cls12-stat','b-cls12-eng','b-cls12-urdu','b-cls12-bio','b-cls12-pak','b-cls12-comp','b-cls12-civics','b-cls12-econ','b-cls12-hpe','b-cls12-islopt','b-cls12-islhist','b-cls12-quran'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath)));"
)

# Add checks for 11 datasets before the end of datasets check
new_dataset_checks = """
check('ENGLISH_12_DATA units = 19', Array.isArray(sb.ENGLISH_12_DATA) && sb.ENGLISH_12_DATA.length === 19 && sb.ENGLISH_12_DATA.every(ch => ch.sections && ch.exercise));
check('PAKSTUDY_12_DATA chapters = 11', Array.isArray(sb.PAKSTUDY_12_DATA) && sb.PAKSTUDY_12_DATA.length === 11 && sb.PAKSTUDY_12_DATA.every(ch => ch.sections && ch.exercise));
check('URDU_12_DATA chapters = 22', Array.isArray(sb.URDU_12_DATA) && sb.URDU_12_DATA.length === 22 && sb.URDU_12_DATA.every(ch => ch.sections && ch.exercise));
check('BIOLOGY_12_DATA units = 14', Array.isArray(sb.BIOLOGY_12_DATA) && sb.BIOLOGY_12_DATA.length === 14 && sb.BIOLOGY_12_DATA.every(ch => ch.sections && ch.exercise));
check('COMP_12_DATA units = 9', Array.isArray(sb.COMP_12_DATA) && sb.COMP_12_DATA.length === 9 && sb.COMP_12_DATA.every(ch => ch.sections && ch.exercise));
check('CIVICS_12_DATA chapters = 8', Array.isArray(sb.CIVICS_12_DATA) && sb.CIVICS_12_DATA.length === 8 && sb.CIVICS_12_DATA.every(ch => ch.sections && ch.exercise));
check('ECON_12_DATA chapters = 12', Array.isArray(sb.ECON_12_DATA) && sb.ECON_12_DATA.length === 12 && sb.ECON_12_DATA.every(ch => ch.sections && ch.exercise));
check('HPE_12_DATA chapters = 6', Array.isArray(sb.HPE_12_DATA) && sb.HPE_12_DATA.length === 6 && sb.HPE_12_DATA.every(ch => ch.sections && ch.exercise));
check('ISLAMIAT_OPT_12_DATA chapters = 6', Array.isArray(sb.ISLAMIAT_OPT_12_DATA) && sb.ISLAMIAT_OPT_12_DATA.length === 6 && sb.ISLAMIAT_OPT_12_DATA.every(ch => ch.sections && ch.exercise));
check('ISLAMIC_HISTORY_12_DATA chapters = 6', Array.isArray(sb.ISLAMIC_HISTORY_12_DATA) && sb.ISLAMIC_HISTORY_12_DATA.length === 6 && sb.ISLAMIC_HISTORY_12_DATA.every(ch => ch.sections && ch.exercise));
check('QURAN_12_DATA chapters = 8', Array.isArray(sb.QURAN_12_DATA) && sb.QURAN_12_DATA.length === 8 && sb.QURAN_12_DATA.every(ch => ch.sections && ch.exercise));
"""

val_content_norm = val_content_norm.replace(
    "console.log('--- index.html ---');",
    new_dataset_checks + "\nconsole.log('--- index.html ---');"
)

with open(val_path, 'w', encoding='utf-8') as f:
    f.write(val_content_norm)
print("Saved validate.js")

# --- 2. Update tools/smoke.js ---
smoke_path = r'D:\SpaceBook\SpaceBook Web\tools\smoke.js'
with open(smoke_path, 'r', encoding='utf-8') as f:
    smoke_content = f.read()

smoke_content_norm = smoke_content.replace('\r\n', '\n')

old_smoke_files = "'stat_12_data.js'];"
new_smoke_files = "'stat_12_data.js', 'english_12_data.js', 'pakstudy_12_data.js', 'urdu_12_data.js', 'biology_12_data.js', 'computer_12_data.js', 'civics_12_data.js', 'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js', 'islamic_history_12_data.js', 'quran_12_data.js'];"

if old_smoke_files in smoke_content_norm:
    smoke_content_norm = smoke_content_norm.replace(old_smoke_files, new_smoke_files)
    print("Updated files list in smoke.js")
else:
    print("WARNING: old_smoke_files not found in smoke.js!")

# Add Class 12 smoke tests for the 11 new subjects
new_smoke_runs = """
run("CLASS 12 English opens 19 units with lessons and exercises", `openSubject('cls12','cls12-eng'); if (getSubjectChapterList('eng','cls12').length!==19) throw new Error('English 12 units missing'); switchSubjectTab('eng','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('English 12 lesson empty'); switchSubjectTab('eng','exercise',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('English 12 exercise empty'); selectSubjectChapter('eng',18,'cls12');`);
run("CLASS 12 Urdu opens 22 lessons with prose and poetry", `openSubject('cls12','cls12-urdu'); if (getSubjectChapterList('urdu','cls12').length!==22) throw new Error('Urdu 12 lessons missing'); switchSubjectTab('urdu','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Urdu 12 lesson empty'); selectSubjectChapter('urdu',21,'cls12');`);
run("CLASS 12 Biology opens 14 units", `openSubject('cls12','cls12-bio'); if (getSubjectChapterList('bio','cls12').length!==14) throw new Error('Biology 12 units missing'); switchSubjectTab('bio','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Bio 12 lesson empty'); selectSubjectChapter('bio',13,'cls12');`);
run("CLASS 12 Pak Studies opens 11 chapters", `openSubject('cls12','cls12-pak'); if (getSubjectChapterList('pakstudy','cls12').length!==11) throw new Error('Pak Studies 12 chapters missing'); switchSubjectTab('pakstudy','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('PakStudy 12 lesson empty'); selectSubjectChapter('pakstudy',10,'cls12');`);
run("CLASS 12 Computer Science opens 9 units", `openSubject('cls12','cls12-comp'); if (getSubjectChapterList('comp','cls12').length!==9) throw new Error('Computer Science 12 units missing'); switchSubjectTab('comp','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Comp 12 lesson empty'); selectSubjectChapter('comp',8,'cls12');`);
run("CLASS 12 Civics opens 8 chapters", `openSubject('cls12','cls12-civics'); if (getSubjectChapterList('civics','cls12').length!==8) throw new Error('Civics 12 chapters missing'); switchSubjectTab('civics','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Civics 12 lesson empty'); selectSubjectChapter('civics',7,'cls12');`);
run("CLASS 12 Economics opens 12 chapters", `openSubject('cls12','cls12-econ'); if (getSubjectChapterList('econ','cls12').length!==12) throw new Error('Economics 12 chapters missing'); switchSubjectTab('econ','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Economics 12 lesson empty'); selectSubjectChapter('econ',11,'cls12');`);
run("CLASS 12 HPE opens 6 chapters", `openSubject('cls12','cls12-hpe'); if (getSubjectChapterList('hpe','cls12').length!==6) throw new Error('HPE 12 chapters missing'); switchSubjectTab('hpe','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('HPE 12 lesson empty'); selectSubjectChapter('hpe',5,'cls12');`);
run("CLASS 12 Islamiat Ikhtiari opens 6 chapters", `openSubject('cls12','cls12-islopt'); if (getSubjectChapterList('islopt','cls12').length!==6) throw new Error('Islamiat Opt 12 chapters missing'); switchSubjectTab('islopt','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Islamiat Opt 12 lesson empty'); selectSubjectChapter('islopt',5,'cls12');`);
run("CLASS 12 Islamic History opens 6 chapters", `openSubject('cls12','cls12-islhist'); if (getSubjectChapterList('islhist','cls12').length!==6) throw new Error('Islamic History 12 chapters missing'); switchSubjectTab('islhist','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Islamic History 12 lesson empty'); selectSubjectChapter('islhist',5,'cls12');`);
run("CLASS 12 Mutalia-e-Quran opens 8 chapters", `openSubject('cls12','cls12-quran'); if (getSubjectChapterList('quran','cls12').length!==8) throw new Error('Quran 12 chapters missing'); switchSubjectTab('quran','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Quran 12 lesson empty'); selectSubjectChapter('quran',7,'cls12');`);
"""

# Place after line 169
target_after = "run(\"CLASS 12 Chemistry and Statistics open their textbook units\", `openSubject('cls12','cls12-chem'); if (getSubjectChapterList('chem','cls12').length!==12) throw new Error('Chemistry unit list missing'); openSubject('cls12','cls12-stat'); if (getSubjectChapterList('stat','cls12').length!==9) throw new Error('Statistics unit list missing'); switchSubjectTab('stat','lesson',0,'cls12'); if (!/<svg/.test($('subjTabContent').innerHTML)) throw new Error('Statistics chart missing'); switchSubjectTab('stat','formulas',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Statistics summary empty');`);"

if target_after in smoke_content_norm:
    smoke_content_norm = smoke_content_norm.replace(target_after, target_after + "\n" + new_smoke_runs)
    print("Added Class 12 smoke tests to smoke.js")
else:
    print("WARNING: target_after not found in smoke.js!")

with open(smoke_path, 'w', encoding='utf-8') as f:
    f.write(smoke_content_norm)
print("Saved smoke.js")
