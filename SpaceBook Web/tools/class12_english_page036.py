"""PDF36 (printed 59–60): Unit 6 intonation exercise 1–15; D noun phrases (definition, examples, head, pronoun heads) + activity 1–13 (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.p('Identify the correct intonation pattern in the following sentences:', 'درج ذیل جملوں میں لہجے کا درست انداز پہچانیں:', 'په لاندې جملو کې د اهنګ سمه بڼه وپېژنئ:')
S = ["You already!", "You shouldn't have.", "It's unbelievable!", "That's not very nice!", "I don't think I will.", 'How could you?', 'Why should I tell you?', 'You must be joking!', 'So what?', 'Well, I never!',
     "You know best, don't you?", 'How do you do?', 'How long have you been building flutes?', 'Can I see one of your flutes?', 'Is this your flute?']
SU = ['تم پہلے ہی!', 'تمہیں ایسا نہیں کرنا چاہیے تھا۔', 'ناقابلِ یقین ہے!', 'یہ زیادہ اچھا نہیں!', 'میرا نہیں خیال کہ میں کروں گا۔', 'تم ایسا کیسے کر سکتے ہو؟', 'میں تمہیں کیوں بتاؤں؟', 'تم مذاق کر رہے ہو!', 'تو کیا ہوا؟', 'اچھا، کبھی نہیں سنا!',
      'تم بہتر جانتے ہو، ہے نا؟', 'آپ کیسے ہیں؟', 'آپ کب سے بانسریاں بنا رہے ہیں؟', 'کیا میں آپ کی ایک بانسری دیکھ سکتا ہوں؟', 'کیا یہ آپ کی بانسری ہے؟']
SP = ['ته دمخه!', 'تا باید داسې نه وای کړي.', 'د باور وړ نه ده!', 'دا ډېره ښه نه ده!', 'فکر نه کوم چې وبه یې کړم.', 'ته دا څنګه کولی شې؟', 'ولې درته ووایم؟', 'ته ټوکې کوې!', 'نو څه؟', 'ښه، هېڅکله!',
      'ته ښه پوهېږې، داسې نه ده؟', 'څنګه یاست؟', 'څومره وخت کېږي چې شپېلۍ جوړوئ؟', 'ایا ستاسو یوه شپېلۍ لیدلی شم؟', 'ایا دا ستاسو شپېلۍ ده؟']
w.group('lines', [(f'{i}. {e}', f'{i}. {e} — ({u})', f'{i}. {e} — ({p})') for i, (e, u, p) in enumerate(zip(S, SU, SP), 1)])
w.h('D. Noun Phrases', 'D. اسمی فقرے', 'D. نومي عبارتونه')
w.p('A noun phrase is a group of words that serves the same purpose as a noun. A noun phrase can be the subject or object of a verb.It can also be the object of a preposition.', 'اسمی فقرہ الفاظ کا ایسا گروہ ہے جو اسم کا کام کرتا ہے۔ اسمی فقرہ فعل کا فاعل یا مفعول ہو سکتا ہے۔ یہ حرفِ جار کا مفعول بھی ہو سکتا ہے۔', 'نومي عبارت د کلمو داسې ډله ده چې د نوم کار کوي. نومي عبارت د فعل فاعل یا مفعول کېدای شي. د اضافې مفعول هم کېدای شي.')
w.h('Examples :', 'مثالیں:', 'بېلګې:')
E = [('I hope to stand first in the class.', 'to stand first in the class'), ('He wished to talk to his teacher.', 'to talk to his teacher'), ('The poor man wanted to pay back every penny he owed.', 'to pay back every penny he owed'),
     ('Horses prefer living in dark stables.', 'living in dark stables'), ('Have you ever tried to climb a tree?', 'to climb a tree'), ('Dont touch those books.', 'touch those books'),
     ('She came with her older sister.', 'with her older sister'), ('She gave him a big sweet piece of cake.', 'him a big sweet piece of cake'), ('They are both excellent teachers.', 'both excellent teachers')]
w.group('list', [(f'{s} [underlined: {u}]', f'{s} [خط کشیدہ: {u}]', f'{s} [لاندې کرښه: {u}]') for s, u in E])
w.p('All the underlined group of words in the above sentences are noun phrases.', 'مندرجہ بالا جملوں میں تمام خط کشیدہ الفاظ کے گروہ اسمی فقرے ہیں۔', 'په پورتنیو جملو کې د لاندې کرښې لرونکو کلمو ټولې ډلې نومي عبارتونه دي.')
w.p('THE HEAD of a noun phrase is the noun being described or referred to in the phrase:', 'اسمی فقرے کا ’’سر‘‘ (HEAD) وہ اسم ہے جس کی فقرے میں صفت بیان کی جا رہی ہو یا جس کا حوالہ دیا جا رہا ہو:', 'د نومي عبارت "سر" (HEAD) هغه نوم دی چې په عبارت کې یې صفت بیانېږي یا ورته اشاره کېږي:')
w.p('For example,', 'مثال کے طور پر،', 'د بېلګې په توګه،')
w.group('list', [('Her older sister', 'Her older sister — (اس کی بڑی بہن)', 'Her older sister — (د هغې مشره خور)'), ('A big piece of cake', 'A big piece of cake — (کیک کا ایک بڑا ٹکڑا)', 'A big piece of cake — (د کېک یوه لویه ټوټه)'), ('Many pleasant days', 'Many pleasant days — (بہت سے خوشگوار دن)', 'Many pleasant days — (ډېرې خوندورې ورځې)')])
w.p('Sometimes a pronoun can be the head of a noun phrase:', 'کبھی کبھی ضمیر بھی اسمی فقرے کا سر ہو سکتا ہے:', 'کله کله ضمیر هم د نومي عبارت سر کېدای شي:')
PR = [("That's a big one", 'یہ ایک بڑا ہے', 'دا یو لوی دی'), ('I would like those read ones', 'مجھے وہ سرخ والے چاہییں', 'زه هغه سره غواړم'), ('They both know the truth', 'وہ دونوں سچ جانتے ہیں', 'دوی دواړه رښتیا پېژني'), ('Are all this for me?', 'کیا یہ سب میرے لیے ہے؟', 'ایا دا ټول زما لپاره دي؟'), ('Have you anything new to tell me?', 'کیا تمہارے پاس مجھے بتانے کو کچھ نیا ہے؟', 'ایا ماته د ویلو لپاره څه نوي لرې؟')]
w.group('list', [(e, f'{e} — ({u})', f'{e} — ({p})') for e, u, p in PR])
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p('Identify the noun phrases in the following sentences:', 'درج ذیل جملوں میں اسمی فقرے پہچانیں:', 'په لاندې جملو کې نومي عبارتونه وپېژنئ:')
A = ['The wicked man loves getting poor people into trouble.', 'He hates having to punish his servants.', 'He refused to answer my question.', 'The boy denied stealing the money.', 'The accused refused to answer the question.',
     'I dislike having to punish my kids.', 'I will hate to do such a thing.', 'To write such a rubbish is disgraceful.', 'He promised to get me something.', 'Why do you want to meet him?',
     'Your doing such a thing surprises me', 'He is such a kind man.', 'They are in the back garden.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(A, 1)])
for p in w.paras[-len(A):]: p['untranslatedByDesign'] = True
rec = BOOK.record(w, 'eng12-u06-vocab-b', 'Intonation exercise; Noun Phrases and activity', 'لہجے کی مشق؛ اسمی فقرے اور سرگرمی', 'د اهنګ تمرین؛ نومي عبارتونه او فعالیت', 36, [59, 60])
issues = [{'id': 'eng12-p59-60', 'unit': 6, 'printedPage': 59, 'description': 'Printed text retained: “You already!”, “Dont touch”, “those read ones” (red ones), “Are all this for me?”, “such a rubbish”. Some textbook examples (infinitive/gerund phrases) are labelled noun phrases as printed. Activity sentences are grammar items and are shown in English in all views (marked untranslatedByDesign).'}]

if __name__ == '__main__':
    BOOK.save(36, [(6, rec)], issues=issues, complete_units=[6])
