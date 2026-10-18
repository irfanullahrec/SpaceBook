"""Generate js/stat_11_data.js (reader + empty chapters) from the Chemistry 11 reader code. Safe to rerun only while no pages are installed."""
import re, pathlib
root = pathlib.Path(r'D:\SpaceBook\SpaceBook Web')
target = root / 'js/stat_11_data.js'
assert not target.exists(), 'stat_11_data.js already exists; do not regenerate over installed pages'
lines = (root / 'js/chem_11_data.js').read_text(encoding='utf-8').split('\n')
def L(a, b): return lines[a - 1:b]
start_add = next(i for i, l in enumerate(lines, 1) if l.startswith('function chem11AddSection'))
start_pair = next(i for i, l in enumerate(lines, 1) if l.startswith('function chem11Pair'))
vocab_line = next(i for i, l in enumerate(lines, 1) if l.startswith('const chem11WordVocabulary'))
cell_line = next(i for i, l in enumerate(lines, 1) if l.startswith('function chem11TableCell'))
reader = L(start_add, start_add + 7) + [''] + L(start_pair, vocab_line - 1) + ['__VOCAB__'] + L(vocab_line + 1, cell_line)
code = '\n'.join(reader)
code = code.replace('chem11', 'stat11').replace('CHEM_11', 'STAT_11').replace('Chemistry', 'Statistics')
code = code.replace('PDF page ${sec.source.pdfPage}', 'Scan ${sec.source.pdfPage}')
code = code.replace("return '<p>Source comparison is in progress for this section.</p>';",
  "return `<p class=\"stat11-source-note\">${ch.sourceGap ? '<strong>Source gap:</strong> ' + stat11SourceText(ch.sourceGap) : 'Source comparison is in progress for this section.'}</p>`;")
assert 'Scan ${sec.source.pdfPage}' in code and 'Source gap' in code
chapters = [
 ('front-matter','FM','Front matter','ابتدائی صفحات','لومړنۍ پاڼې','Scans 1–8; unnumbered and roman-numbered'),
 ('collection-presentation','1','Collection and Presentation of Data','اعداد و شمار کا اکٹھا کرنا اور پیشکش','د معلوماتو راټولول او وړاندې کول','Printed pages 1–53'),
 ('central-tendency','2','Measures of Central Tendency (MCT)','مرکزی رجحان کے پیمانے','د مرکزي تمایل اندازې','Printed pages 54–89'),
 ('dispersion-skewness-kurtosis','3','Measures of Dispersion, Skewness and Kurtosis','انتشار، کجی اور نوکیلاپن کے پیمانے','د خپراوي، کوړوالي او تېزوالي اندازې','Printed pages 90–144'),
 ('index-numbers','4','Index Numbers','اشاریہ اعداد','شاخصي شمېرې','Printed pages 145–172'),
 ('regression-correlation','5','Simple Linear Regression and Correlation','سادہ خطی تانتجہ (ریگریشن) اور ہم رشتگی','ساده خطي ریګرېشن او اړیکه','Printed pages 173–194'),
 ('time-series','6','Time Series','وقتی سلسلہ','د وخت لړۍ','Printed pages 195–214'),
 ('vital-statistics','7','Vital Statistics','حیاتی شماریات','حیاتي احصایې','Printed pages 215–238'),
 ('interpolation','8','Interpolation','درمیان یابی','منځګړیتوب (انټرپولېشن)','Printed pages 239–250'),
 ('linear-programming','9','Linear Programming','خطی پروگرامنگ','خطي پروګرامېنګ','Printed pages 251–284'),
 ('answers','A','Answers','جوابات','ځوابونه','Printed pages 285–290'),
 ('glossary','G','Glossary','فرہنگ','وییپانګه','Printed pages 291–296'),
 ('index','I','Index','اشاریہ','لړلیک','Printed page 297 onward'),
]
gap = 'The local source set (jpg scans 1–247 and the eight derivative PDFs) ends at printed page 237 (scan 247); this unit is not present in the local sources and could not be transcribed.'
rows = []
for cid, num, t, tu, tp, pr in chapters:
    after7 = cid in ('interpolation', 'linear-programming', 'answers', 'glossary', 'index')
    rows.append("  { id: 'stat11-%s', number: %s, title: %s, titleUrdu: %s, titlePashto: %s, pageRange: %s, verificationStatus: %s, sections: []%s }" % (
        cid, repr(num) if not num.isdigit() else num, repr(t), repr(tu), repr(tp), repr(pr),
        "'not in local sources'" if after7 else "'draft: exact source comparison pending'",
        (', sourceGap: ' + repr(gap)) if after7 else ''))
head = ("// Class 11 Statistics: page-by-page source records transcribed from the KPTBB scans\n"
        "// (D:\\SpaceBook\\Books\\11th\\11th stastic\\jpg, 244 files numbered 1–247; scans 2, 3 and 238 are absent).\n"
        "// Printed page = scan − 8 at the start (scan 9 = page 1); the offset grows later where scans are missing.\n"
        "// Section source.pdfPage holds the scan number (used as the page key). auditStatus distinguishes drafts from source-checked records.\n"
        "const STAT_11_DATA = [\n" + ',\n'.join(rows) + "\n];\n\n")
vocab = "const stat11WordVocabulary = {\"statistics\":{\"ur\":\"شماریات\",\"ps\":\"احصایه\"},\"data\":{\"ur\":\"اعداد و شمار\",\"ps\":\"معلومات\"},\"population\":{\"ur\":\"مجموعہ (آبادی)\",\"ps\":\"ټولنه (نفوس)\"},\"sample\":{\"ur\":\"نمونہ\",\"ps\":\"نمونه\"},\"variable\":{\"ur\":\"متغیر\",\"ps\":\"متغیر\"},\"frequency\":{\"ur\":\"تعدد (تکرار)\",\"ps\":\"فریکونسي (تکرار)\"}};"
target.write_text(head + code.replace('__VOCAB__', vocab) + '\n', encoding='utf-8', newline='\n')
print('written', target)
