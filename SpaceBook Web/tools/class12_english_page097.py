"""PDF97 (printed 181–182): Unit 18 synonyms 4–12; B direct→indirect table 1–10; 'Reported speech Exercise: Past Tense' table 11–20."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
S = [('The painting had brilliant shades of blue.', 'brilliant'), ('The dog curled up under the table.', 'under'), ('My dad knows a lot of funny jokes.', 'funny'), ('The burglar stole the diamonds and gold.', 'burglar'),
     ('I went home early because I felt sick.', 'sick'), ('You will need to mix the eggs and flour.', 'mix'), ('The cost of the toy was too high.', 'cost'), ('The fisherman stared out at the blue waters.', 'blue'), ('Max made a mistake on his math test.', 'mistake')]
v.group('lines', [(f'{i}. {s} [underlined: {u}] ____',) * 3 for i, (s, u) in enumerate(S, 4)])
for p in v.paras: p['untranslatedByDesign'] = True
v.p("B. Write the Indirect narration in the 'Indirect Speech column' for the sentences given in 'Direct Speech column'!", 'B. ’’براہِ راست کلام‘‘ کے کالم میں دیے گئے جملوں کا بالواسطہ بیان ’’بالواسطہ کلام‘‘ کے کالم میں لکھیں!', 'B. د "مستقیمې وینا" په ستون کې ورکړل شویو جملو غیرمستقیم بیان د "غیرمستقیمې وینا" په ستون کې ولیکئ!')
D1 = ['1. He said,"I work in a small company"', '2. She said, "I am waiting for my salary"', '3. Alex said to me, "It have worked very hard for this project"', '4. I said to him, "I do not care about small issues"', '5. She said to me, "I am making good progress on this project"',
      '6. We said, "You have better future than us"', '7. They said, "It is getting on very boring here"', '8. She said, "You have to decide by tomorrow"', '9. Alex said, "I have been writing this paragraph"', '10. They said, "We do not listen to their advice"']
R1 = [[d, ''] for d in D1]
v.table('eng12-u18-reported-1', ['Direct Speech', 'Indirect Speech'], R1, ['براہِ راست کلام', 'بالواسطہ کلام'], ['مستقیمه وینا', 'غیرمستقیمه وینا'])
D2 = ['11. He said, "I worked very hard but failed"', '12. She said to me, "It did not work for me"', '13. Alex said, "I was listening Indian music"', '14. "We were going to a new mission" they said.', '15. "I had collected ancient books" he said.',
      '16. They said, "We had better alternative than this"', '17. He said to me, "We watched a wonderful movie."', '18. Alex said, "I was writing codes for a new program"', '19. She said to him, "I had no intention to marry you."', '20. He said, "I wasted my time after her."']
R2 = [[d, ''] for d in D2]
v.table('eng12-u18-reported-2', ['Direct Speech', 'Indirect Speech'], R2, ['براہِ راست کلام', 'بالواسطہ کلام'], ['مستقیمه وینا', 'غیرمستقیمه وینا'],
        caption='Reported speech Exercise: Past Tense', captionUrdu='بالواسطہ کلام کی مشق: زمانۂ ماضی', captionPashto='د غیرمستقیمې وینا تمرین: تېر زمان')
rec = BOOK.record(v, 'eng12-u18-vocab-b', 'Vocabulary A (4–12); B Direct → Indirect tables', 'ذخیرۂ الفاظ A (4–12)؛ B براہِ راست ← بالواسطہ جدول', 'لغات A (4–12)؛ B مستقیمه ← غیرمستقیمه جدولونه', 97, [181, 182])
issues = [{'id': 'eng12-p181-182', 'unit': 18, 'printedPage': 181, 'description': 'Printed text retained: “It have worked very hard” (item 3), “It is getting on very boring”, “I was listening Indian music”, “after her”. The B instruction and item numbers 4–12 are faint in the scan but legible. Indirect Speech column is left blank for the student as printed.'}]

if __name__ == '__main__':
    BOOK.save(97, [(18, rec)], issues=issues)
