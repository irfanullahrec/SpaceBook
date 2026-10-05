path = r'D:\SpaceBook\SpaceBook Web\tools\validate.js'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update line 89 to check all 15 Class 12 subjects
old_l89 = "check('Class 12 Maths, Physics, Chemistry and Statistics registered', ['cls12-math','cls12-phy','cls12-chem','cls12-stat'].every(id => D.subjects.cls12.some(s => s.id === id)));"
new_l89 = "check('Class 12 all 15 subjects registered', D.subjects && D.subjects.cls12 && D.subjects.cls12.length === 15 && ['cls12-math','cls12-phy','cls12-chem','cls12-stat','cls12-eng','cls12-urdu','cls12-bio','cls12-pak','cls12-comp','cls12-civics','cls12-econ','cls12-hpe','cls12-islopt','cls12-islhist','cls12-quran'].every(id => D.subjects.cls12.some(s => s.id === id)));"
c = c.replace(old_l89, new_l89)

# 2. Update line 90 to check all 15 Class 12 PDF links
old_l90 = "check('Class 12 textbook PDF links available', ['b-cls12-math','b-cls12-phys','b-cls12-chem','b-cls12-stat'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath)));"
new_l90 = "check('Class 12 textbook PDF links available for all 15 books', ['b-cls12-math','b-cls12-phys','b-cls12-chem','b-cls12-stat','b-cls12-eng','b-cls12-urdu','b-cls12-bio','b-cls12-pak','b-cls12-comp','b-cls12-civics','b-cls12-econ','b-cls12-hpe','b-cls12-islopt','b-cls12-islhist','b-cls12-quran'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath)));"
c = c.replace(old_l90, new_l90)

# 3. Add checks for all 11 new datasets after line 341
checks_to_add = """
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

lookup_str = "check('lookupEngWord()', typeof sb.lookupEngWord === 'function');"
if lookup_str in c:
    c = c.replace(lookup_str, lookup_str + "\n" + checks_to_add)

# 4. Update index.html check for 12th textbooks
old_index_check = "check('index.html loads all Class 12 textbooks before app.js', ['js/math_12_data.js','js/phys_12_data.js','js/chem_12_data.js','js/stat_12_data.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));"
new_index_check = "check('index.html loads all 15 Class 12 textbooks before app.js', ['js/math_12_data.js','js/phys_12_data.js','js/chem_12_data.js','js/stat_12_data.js','js/english_12_data.js','js/pakstudy_12_data.js','js/urdu_12_data.js','js/biology_12_data.js','js/computer_12_data.js','js/civics_12_data.js','js/economics_12_data.js','js/hpe_12_data.js','js/islamiat_ikhtiari_12_data.js','js/islamic_history_12_data.js','js/quran_12_data.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));"
c = c.replace(old_index_check, new_index_check)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated validate.js successfully")
