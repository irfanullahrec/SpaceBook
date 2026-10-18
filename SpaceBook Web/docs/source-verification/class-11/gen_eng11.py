"""Generate js/eng_11_data.js (reader + empty chapters) from the Statistics 11 reader code. Safe to rerun only while no pages are installed."""
import re, pathlib
root = pathlib.Path(r'D:\SpaceBook\SpaceBook Web')
target = root / 'js/eng_11_data.js'
assert not target.exists(), 'eng_11_data.js already exists; do not regenerate over installed pages'
text = (root / 'js/stat_11_data.js').read_text(encoding='utf-8')
a = text.index('function stat11AddSection')
b = text.index('// BEGIN STATISTICS SOURCE SCAN 1')
code = text[a:b]
code = code.replace('stat11', 'eng11').replace('STAT_11', 'ENG_11').replace('Statistics', 'English').replace('renderEnglish11Tab', 'renderEnglish11Tab')
code = code.replace('renderStatistics11Tab', 'renderEnglish11Tab').replace('statistics11', 'english11')
code = re.sub(r'const eng11WordVocabulary = \{.*?\};\n', 'const eng11WordVocabulary = {};\n', code, count=1, flags=re.S)
code = code.replace('Scan ${sec.source.pdfPage}', 'Scan ${sec.source.pdfPage}')
chapters = [
 ('front-matter','FM','Front matter and Foreword','ابتدائی صفحات اور پیش لفظ','لومړنۍ پاڼې او سریزه','Scans 1–?'),
 ('u01','1','Responsibilities of the Youth','نوجوانوں کی ذمہ داریاں','د ځوانانو مسؤولیتونه',''),
 ('u02','2','His First Flight','اس کی پہلی پرواز','د هغه لومړنی الوتنه',''),
 ('u03','3','Good Timber (Poem)','اچھی لکڑی (نظم)','ښه لرګی (نظم)',''),
 ('u04','4','From Mother With Love','ماں کی طرف سے محبت کے ساتھ','له مور څخه په مینه',''),
 ('u05','5','Its Country for Me','یہ میرے لیے ملک ہے','دا زما لپاره هېواد دی',''),
 ('u06','6','Mother to Son (Poem)','ماں کا بیٹے کے نام (نظم)','مور له زوی ته (نظم)',''),
 ('u07','7','Choice of Career','پیشے کا انتخاب','د مسلک غوراوی',''),
 ('u08','8','Wasteland','بنجر زمین','ویجاړه ځمکه',''),
 ('u09','9','The White Lamb','سفید برہ','سپینه وری',''),
 ('u10','10','The World is Too Much With Us','دنیا ہم پر بہت غالب ہے','نړۍ زموږ سره ډېره ده',''),
 ('u11','11','The Importance of Family','خاندان کی اہمیت','د کورنۍ اهمیت',''),
 ('u12','12','The Blanket','کمبل','کمبله',''),
 ('u13','13','Ozymandias','اوزیمنڈیاس','اوزیمانډیاس',''),
 ('u14','14','A Long Walk Home','گھر تک ایک لمبی پیدل مسافت','کور ته اوږده پیاده سفر',''),
 ('u15','15','University Days','یونیورسٹی کے دن','د پوهنتون ورځې',''),
 ('u16','16','School VS Education','اسکول بمقابلہ تعلیم','ښوونځی په مقابل کې زده کړه',''),
 ('u17','17','What You Do Is What You Are','آپ جو کرتے ہیں وہی آپ ہیں','هغه څه چې تاسو یې کوئ هغه یاست',''),
 ('u18','18','A Dream Within A Dream','خواب کے اندر ایک خواب','په خوب کې یو خوب',''),
 ('u19','19','Drug Abuse in the Youth of Pakistan','پاکستان کے نوجوانوں میں منشیات کا غلط استعمال','د پاکستان په ځوانانو کې د مخدره توکو ناوړه کارونه',''),
 ('u20','20','How to Take a Job Interview','ملازمت کا انٹرویو کیسے دیں','د دندې مرکه څنګه ورکړو',''),
 ('u21','21','The Road Not Taken','وہ راستہ جو نہیں لیا گیا','هغه لار چې نه وه اخیستل شوې',''),
 ('u22','22','The Progress','ترقی','پرمختګ',''),
 ('back-matter','BM','Back matter','آخری صفحات','وروستۍ پاڼې',''),
]
rows = []
for cid, num, t, tu, tp, pr in chapters:
    rows.append("  { id: 'eng11-%s', number: %s, title: %s, titleUrdu: %s, titlePashto: %s, pageRange: %s, verificationStatus: 'draft: exact source comparison pending', sections: [] }" % (
        cid, repr(num) if not num.isdigit() else num, repr(t), repr(tu), repr(tp), repr(pr)))
head = ("// Class 11 English: page-by-page source records transcribed from the KPTBB scans\n"
        "// (D:\SpaceBook\Books\11th\11english\jpg, 240 half-page photographs NNN_page_H.jpg).\n"
        "// Scan number n = 2*(NNN-1)+H (001_page_1 = scan 1, 001_page_2 = scan 2). Section source.pdfPage holds the scan number.\n"
        "const ENG_11_DATA = [\n" + ',\n'.join(rows) + "\n];\n\n")
tail = "\nfunction english11SourceSearchText(ch) {\n  return [ch.title, ch.titleUrdu, ch.titlePashto, ...(ch.sections || []).flatMap(sec => [\n    sec.title, sec.headingUrdu, sec.headingPashto,\n    ...(sec.paras || []).flatMap(p => [p.original, p.urdu, p.pashto]),\n    ...(sec.figures || []).flatMap(f => [f.caption, f.captionUrdu, f.captionPashto]),\n    ...(sec.tables || []).flatMap(t => [t.caption, ...(t.rows || []).flat().map(c => typeof c === 'string' ? c : c.en)])\n  ])].filter(Boolean).join(' ');\n}\n"
target.write_text(head + code.rstrip() + '\n' + tail, encoding='utf-8', newline='\n')
print('written', target)
