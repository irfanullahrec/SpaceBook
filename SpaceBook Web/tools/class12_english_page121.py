"""PDF121 (printed 229–230): Unit 19 'Imperative sentences-Reported Speech Exercise' tables 10–19 and 20–30."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
D1 = ['10. He said to his servant, "Clean the tables again"', '11. Mother said to her daughter, "Shut up! go into your room"', '12. He said to the waiter, "Bring me the detailed bill"', '13. He said, "Close the door, Raja"', '14. Father said to his son, "Get ready, we will leave quickly"',
      '15. I said to policemen, "please, help the poor lady"', '16. The old man said, "Please, release my son this time"', '17. She said to him, "Don\'t ever try to talk me"', '18. Teacher said to students, "Stand up all"', '19. He said to his son, "Avoid sitting with bad guys"']
H = (['Direct Speech', 'Indirect Speech'], ['براہِ راست کلام', 'بالواسطہ کلام'], ['مستقیمه وینا', 'غیرمستقیمه وینا'])
v.table('eng12-u19-reported-2', H[0], [[d, ''] for d in D1], H[1], H[2], caption='Imperative sentences-Reported Speech Exercise', captionUrdu='امریہ جملے — بالواسطہ کلام کی مشق', captionPashto='امري جملې — د غیرمستقیمې وینا تمرین')
D2 = ['20. The doctor said to him, “Stay away from junk food”', '21. I said, "Let him sleep before we leave"', '22. She said to him, "Let\'s meet her parents somewhere"', '23. I said to her, "Let me think before I give you any proposal."', '24. She said to her father, "Let me buy some books for Alex"',
      '25. I said, "Let\'s start reading this novel together"', '26. The teacher said, "Let\'s start over a new chapter."', '27. She said, "let me to be more prepared for the task."', '28. I said, "Let me find a best solution to solve this issue permanently."', '29. They said, "Let\'s play a game where the winner will win a gold."', '30. She said to me, "Please, let me stay here until my brother comes."']
v.table('eng12-u19-reported-3', H[0], [[d, ''] for d in D2], H[1], H[2], caption='Imperative Sentences – Reported Speech Exercise', captionUrdu='امریہ جملے — بالواسطہ کلام کی مشق', captionPashto='امري جملې — د غیرمستقیمې وینا تمرین')
rec = BOOK.record(v, 'eng12-u19-vocab-b', 'Imperative sentences — reported speech tables', 'امریہ جملے — بالواسطہ کلام کے جدول', 'امري جملې — د غیرمستقیمې وینا جدولونه', 121, [229, 230])
issues = [{'id': 'eng12-p229-230', 'unit': 19, 'printedPage': 229, 'description': 'Numbering continues from table D (1–9) on p.228. The second table (20–30) repeats the caption with different capitalisation; items 21–30 are “let”-sentences rather than strict imperatives. Retained: “Don\'t ever try to talk me”, “let me to be”, “a best solution”, “win a gold”.'}]

if __name__ == '__main__':
    BOOK.save(121, [(19, rec)], issues=issues)
