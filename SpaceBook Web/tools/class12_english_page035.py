"""PDF35 (printed 57–58): Unit 6 Vocabulary A (end); B thesaurus matching table; C Latin plurals + activity; Intonation (rising/falling)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
W = ['Quarrel', 'Bubble', 'Teeth', 'Pipe']
R = [[x, ''] for x in W]
w.table('eng12-u06-dict-b', ['Word', 'Phonetic Transcription'], R, ['لفظ', 'صوتی نقل'], ['کلمه', 'غږیز لیکدود'], R, R)
w.p('B. Look for the given words in the Thesaurus and match the words given in column A and B with relevant synonyms.', 'B. دیے گئے الفاظ تھیسارس میں تلاش کریں اور کالم A اور B کے الفاظ کو متعلقہ مترادفات سے ملائیں۔', 'B. ورکړل شوې کلمې په تیسارس کې ولټوئ او د A او B ستونونو کلمې له اړوندو مترادفاتو سره برابرې کړئ.')
A = ['select', 'raise', 'accurate', 'able', 'considerate', 'divide', 'apparant', 'exceptional', 'busy', 'brave', 'clarify', 'aid', 'diminish', 'convenient', 'beneficial', 'approve', 'conscious', 'brief', 'authentic', 'average']
Bc = ['correct, right', 'aware', 'occupied, active', 'thoughtful, caring', 'real, genuine', 'lift', 'courageous, bold', 'help, assist', 'normal, ordinary', 'handy,useful', 'lesson,decrease', 'choose', 'explain, simplify', 'accept, endorse', 'short', 'remarkable, outstanding', 'capable, qualified', 'separate, split', 'helpful, useful', 'obvious']
R = [[a, b] for a, b in zip(A, Bc)]
w.table('eng12-u06-thesaurus', ['Column A', 'Column B'], R, ['کالم A', 'کالم B'], ['ستون A', 'ستون B'], R, R)
w.p('C. Make plural forms of the Latin nouns by changing the suffixes.', 'C. لاحقے بدل کر لاطینی اسماء کی جمع بنائیں۔', 'C. د وروستاړو په بدلولو د لاتیني نومونو جمع جوړه کړئ.')
w.p('Latin nouns ending in:', 'لاطینی اسماء جن کا اختتام ہو:', 'هغه لاتیني نومونه چې پای یې وي:')
L = [['-a', 'change to -ae', 'antenna changes to antennae'], ['-is', 'change to -es', 'thesis changes to theses'], ['-us', 'change to -i', 'stimulus changes to stimuli'], ['-urn', 'change to -a', 'medium changes to media']]
LU = [['-a', '-ae میں بدلیں', 'antenna بدل کر antennae'], ['-is', '-es میں بدلیں', 'thesis بدل کر theses'], ['-us', '-i میں بدلیں', 'stimulus بدل کر stimuli'], ['-urn', '-a میں بدلیں', 'medium بدل کر media']]
LP = [['-a', 'په -ae بدل کړئ', 'antenna په antennae بدلېږي'], ['-is', 'په -es بدل کړئ', 'thesis په theses بدلېږي'], ['-us', 'په -i بدل کړئ', 'stimulus په stimuli بدلېږي'], ['-urn', 'په -a بدل کړئ', 'medium په media بدلېږي']]
w.table('eng12-u06-latin', ['Ending', 'Rule', 'Example'], L, ['اختتام', 'قاعدہ', 'مثال'], ['پای', 'قاعده', 'بېلګه'], LU, LP)
w.h('Activity', 'سرگرمی', 'فعالیت')
W = ['alumna', 'analysis', 'synopsis', 'cactus', 'crisis', 'cranium', 'curriculum', 'datum', 'focus', 'formula', 'fungus', 'larva', 'nucleus', 'referendum', 'syllabus']
R = [[x, ''] for x in W]
w.table('eng12-u06-latin-activity', ['Singular', 'Plural'], R, ['واحد', 'جمع'], ['مفرد', 'جمع'], R, R)
w.h('Intonation', 'لہجہ (انٹونیشن)', 'اهنګ (انټونېشن)')
w.p('Intonation is about how we say things, rather than what we say. There are two basic intonation patterns: Rising and Falling. With rising intonation you have to raise slightly the pitch at the end of the sentence, whereas with falling intonation you go down a bit.', 'لہجہ (انٹونیشن) اس بارے میں ہے کہ ہم بات کیسے کہتے ہیں، نہ کہ ہم کیا کہتے ہیں۔ لہجے کے دو بنیادی انداز ہیں: چڑھتا اور اترتا۔ چڑھتے لہجے میں جملے کے آخر میں آواز کی بلندی تھوڑی بڑھانی ہوتی ہے، جبکہ اترتے لہجے میں آپ تھوڑا نیچے جاتے ہیں۔', 'اهنګ د دې په اړه دی چې موږ خبرې څنګه کوو، نه دا چې څه وایو. د اهنګ دوه بنسټیزې بڼې دي: پورته کېدونکی او ښکته کېدونکی. په پورته کېدونکي اهنګ کې باید د جملې په پای کې غږ لږ لوړ کړئ، په داسې حال کې چې په ښکته کېدونکي اهنګ کې لږ ښکته ځئ.')
w.p('We use falling intonation with:', 'ہم اترتا لہجہ استعمال کرتے ہیں:', 'موږ ښکته کېدونکی اهنګ کاروو د:')
w.group('list', [('Statements', 'بیانات', 'بیانونو'), ('Wh- questions', 'Wh- سوالات', 'Wh- پوښتنو'), ('Commands or invitations', 'احکامات یا دعوتیں', 'امرونو یا بلنو'), ('Exclamations', 'ندائیہ کلمات', 'ندایي کلمو'), ('Alternative questions', 'متبادل سوالات', 'بدیلو پوښتنو')])
w.p('We use rising intonation with:', 'ہم چڑھتا لہجہ استعمال کرتے ہیں:', 'موږ پورته کېدونکی اهنګ کاروو د:')
w.group('list', [('Yes / No questions', 'ہاں / نہیں والے سوالات', 'هو / نه پوښتنو'), ('Offers', 'پیشکشیں', 'وړاندیزونو'), ('Enumerations', 'گنتی / شمار', 'شمېرنو')])
rec = BOOK.record(w, 'eng12-u06-vocab-a', 'Vocabulary A (end), B thesaurus, C Latin plurals; Intonation', 'ذخیرۂ الفاظ A (اختتام)، B تھیسارس، C لاطینی جمع؛ لہجہ', 'لغات A (پای)، B تیسارس، C لاتیني جمع؛ اهنګ', 35, [57, 58])
issues = [{'id': 'eng12-p57-58', 'unit': 6, 'printedPage': 57, 'description': 'Printed text retained: “apparant” (apparent), “lesson,decrease” (lessen), Latin ending “-urn” (should be -um). Column B is printed in a different order from column A (matching exercise).'}]

if __name__ == '__main__':
    BOOK.save(35, [(6, rec)], issues=issues)
