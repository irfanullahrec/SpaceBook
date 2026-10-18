"""PDF75 (printed 137–138): Unit 14 Oral; Vocabulary A abstract nouns 1–10; B word forms 1–11; C third conditional 1–12; D sentence-type tick table (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('The teacher should divide students into various groups wherein they will discuss their daily responsibilities in home. Teacher should guide them in their course of discussion.', 'استاد طلبہ کو مختلف گروہوں میں تقسیم کرے جہاں وہ گھر میں اپنی روزمرہ ذمہ داریوں پر بحث کریں۔ استاد بحث کے دوران ان کی رہنمائی کرے۔', 'ښوونکی دې زده کوونکي په بېلابېلو ډلو ووېشي چې پکې به په کور کې د خپلو ورځنیو مسؤلیتونو په اړه بحث وکړي. ښوونکی دې د بحث پر مهال د هغوی لارښوونه وکړي.')
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. Fill in the blanks with suitable abstract nouns. The adjectives, verbs or nouns given in the brackets should offer clues.', 'A. خالی جگہیں موزوں مجرد اسماء سے پُر کریں۔ قوسین میں دی گئی صفات، افعال یا اسماء اشارے کا کام دیں گے۔', 'A. تش ځایونه په مناسبو مجردو نومونو ډک کړئ. په قوسونو کې ورکړل شوي صفتونه، فعلونه یا نومونه به نښې ورکړي.')
A = ['He is a man of ........ (strong)', 'The people in this part of the country live in ........ (poor).', '........ to animals is a punishable offence. (cruel)', 'He is on a ........ to Mecca. (pilgrim)', 'I have great ........ to welcome you. (please).',
     "........ is the best period of one's life. (child)", '........ should always be avoided. (waste).', "As a parent my children's ........ is of utmost importance to me. (safe).", 'As the sun went below the horizon ........ enveloped the planet. (dark).', 'There is no end to his ........ (wicked)']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(A, 1)])
w.p('B. Fill in the blanks with the appropriate form of the word given in the brackets.', 'B. قوسین میں دیے گئے لفظ کی موزوں شکل سے خالی جگہیں پُر کریں۔', 'B. تش ځایونه په قوسونو کې د ورکړل شوې کلمې په مناسبه بڼه ډک کړئ.')
Bw = ['My friend did not ........ to my letter. (response)', 'He behaved ........ (strange)', "Teacher's ........ had great effect on students. (exhort)", 'He ........ his point with valid arguments. (substance)', 'Greedy people will never get any ........ in life. (satisfy)',
      "I don't think that there is any ........ for you to come again. (necessary)", 'Though his early attempts were not ........ he did not lose heart. (success)', 'I have ........ that song. (memory)', 'The teacher ........ her to go home early. (permission)', 'Hubble made many astronomical ........ (discover)']
w.group('lines', [(f'{n}. {s}',) * 3 for n, s in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], Bw)])
w.p('C. Complete the following sentences using conditional sentences type three. Change the form of verb if required.', 'C. تیسری قسم کے شرطیہ جملے استعمال کرتے ہوئے درج ذیل جملے مکمل کریں۔ ضرورت ہو تو فعل کی شکل بدلیں۔', 'C. د درېیم ډول شرطي جملو په کارولو لاندې جملې بشپړې کړئ. که اړینه وي د فعل بڼه بدله کړئ.')
C = ['If you ____ asked me,I ____ told you the truth.', 'We ____ got lost if we ____ a map.', 'If you ____ had a daughter, I ____ called her chubby doll?', 'If the shops ____ been open, they ____ bought something.', 'If Ambreen ____ known that,she ____ come back early.',
     'We ____ sung a song if somebody ____ played the hormonica.', 'If I ____ (live )in Spain,I ____ (learn )Spanish.', 'If it ____ (rain) yesterday,we ____ ( stay) at home.', 'I ____ ( go) if Amer ____ (invite) me.', 'If my son ____ (study) medicine he ____ (become) a doct',
     'If you ____ (come) early you ____ ( see ) a comet.', 'What Mary ____ ( do ) if she ____ ( be) late for school?']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(C, 1)])
for p in w.paras:
    if p['text'][:3].strip().rstrip('.').isdigit(): p['untranslatedByDesign'] = True
w.p('D. Tick (✓) the appropriate box', 'D. موزوں خانے پر نشان (✓) لگائیں', 'D. مناسب بکس په (✓) نښه کړئ')
D = ['The children wore their dirty boots.', 'It was time for bed, yet it was still light outside.', 'The front door was locked, so she entered through the back.', 'They took a lot of pictures when they visited Swat.', 'After the show began, he sat very quietly.',
     'The girl was wearing a red dress.', 'He was playing on his computer.', 'Yahya Khan would like to play, for he is the best player on the team.', 'Before the bell rings, the student lined up at the door.', 'We turned off the lights.']
R = [[s, '', '', ''] for s in D]
w.table('eng12-u14-sentence-tick', ['Sentences', 'simple', 'compound', 'complex'], R, ['جملے', 'سادہ', 'مرکب', 'پیچیدہ'], ['جملې', 'ساده', 'مرکبه', 'پېچلې'], R, R)
rec = BOOK.record(w, 'eng12-u14-vocab', 'Oral; Vocabulary A–D', 'زبانی ابلاغ؛ ذخیرۂ الفاظ A–D', 'د خولې اړیکه؛ لغات A–D', 75, [137, 138])
issues = [{'id': 'eng12-p137-138', 'unit': 14, 'printedPage': 137, 'description': 'Printed numbering retained: exercise B jumps from 9 to 11 (no item 10). Also retained: “hormonica”, “a doct” (doctor, cut), “What Mary ___ (do) if she ___ (be) late”, “Before the bell rings, the student lined up”. Grammar drills shown in English in all views.'}]

if __name__ == '__main__':
    BOOK.save(75, [(14, rec)], issues=issues, complete_units=[14])
