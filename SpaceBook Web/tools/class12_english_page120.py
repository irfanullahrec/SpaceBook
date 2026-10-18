"""PDF120 (printed 227–228): Unit 19 Oral; Vocabulary A synonym/antonym 1–12; B sentence types 1–10; C strongest word 1–8; D pronoun-change reported speech table 1–9."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
v.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
v.p("Make two large groups of the class students; one of them to act as the Ralph's group and the other as Jack's band. Give them an issue or some issues to be resolved by them. Each group should forward its suggestions and proposals regarding the issue(s).",
    'جماعت کے طلبہ کے دو بڑے گروہ بنائیں؛ ایک رالف کے گروہ اور دوسرا جیک کی ٹولی کا کردار ادا کرے۔ انہیں حل کرنے کے لیے ایک یا چند مسائل دیں۔ ہر گروہ مسئلے/مسائل کے بارے میں اپنی تجاویز اور سفارشات پیش کرے۔',
    'د ټولګي زده کوونکي په دوو لویو ډلو ووېشئ؛ یوه دې د رالف د ډلې او بله د جیک د ډلې رول ولوبوي. هغوی ته د حل لپاره یوه یا څو ستونزې ورکړئ. هره ډله دې د ستونزې/ستونزو په اړه خپل وړاندیزونه وړاندې کړي.')
v.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
v.p('A. Look for in a Thesaurus and tell whether each pair of words are synonyms or antonyms.', 'A. تھیسارس میں دیکھیں اور بتائیں کہ الفاظ کا ہر جوڑا مترادف ہے یا متضاد۔', 'A. په تیسارس کې وګورئ او ووایئ چې د کلمو هره جوړه مترادف ده که متضاد.')
A = ['agree, disagree', 'cold, freezing', 'easy, difficult', 'argue, squabble', 'guess, estimate', 'bottom, top', 'tired, energetic', 'huge, gigantic', 'sink, float', 'windy, calm', 'noisy, quiet', 'unhappy, sad']
v.group('lines', [(f'{i}. {s} ____',) * 3 for i, s in enumerate(A, 1)])
v.p('B. Identify the following sentences as Simple, Compound and Complex.', 'B. درج ذیل جملوں کو سادہ، مرکب اور پیچیدہ کے طور پر پہچانیں۔', 'B. لاندې جملې د ساده، مرکبې او پېچلې په توګه وپېژنئ.')
B = ['We were playing in the garden when the guests arrived.', 'She put on her coat and went out.', 'I can’t figure out what he wants.', 'You don’t look happy to see me.', 'The cat saw the puppies playing in the garden.', 'She leaned out of the window.', 'You shouldn’t have done this to me.', 'They tried very hard but they couldn’t win the match.', 'Who let the cat in?', 'Although it was raining, we went for a walk.']
v.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(B, 1)])
v.p('C. Write the strongest word of the pair given in the parenthesis in the given blank of each sentence.', 'C. ہر جملے کی خالی جگہ میں قوسین میں دیے گئے جوڑے کا زیادہ زور دار لفظ لکھیں۔', 'C. د هرې جملې په تش ځای کې په قوسونو کې د ورکړل شوې جوړې قوي کلمه ولیکئ.')
C = ['The flowers were ____ in the garden. (beautiful, pretty)', 'We had a ____ dinner at the restaurant. (good, delicious)', 'The glass plated ____ to the ground. (fell, crashed)', 'She ____ hello to the teacher. (said, whispered)', 'The ____ cat sat on the fence. (starving, hungry)',
     'He slept on the ____ bed. (hard, firm)', 'The children will ____ out the door when the bell rings. (dash, march)', 'Salim was ____ with his brother. (cross, furious)']
v.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(C, 1)])
for p in v.paras:
    if p['text'][:3].strip().rstrip('.').isdigit(): p['untranslatedByDesign'] = True
v.p("D. Write the indirect narration in the 'Indirect Speech column' for the sentences given in 'Direct Speech column'.", 'D. ’’براہِ راست کلام‘‘ کے کالم میں دیے گئے جملوں کا بالواسطہ بیان ’’بالواسطہ کلام‘‘ کے کالم میں لکھیں۔', 'D. د "مستقیمې وینا" په ستون کې ورکړل شویو جملو غیرمستقیم بیان د "غیرمستقیمې وینا" په ستون کې ولیکئ.')
D = ['1. He said, "I am working hard for the upcoming tests"', '2. She said, "My only wish is to become a good man"', '3. He said, "I am learning the rules of new language"', '4. I said to her, "You seem to be a nice', '5. He said to me, "You should be responsible in your duty"',
     '6. Asad said, "It is a rule to obey the master"', '7. They said, "We are waiting for our brothers"', '8. I said, "I am the winner in this game"', '9. They said, "We are learning English by ourselves"']
R = [[d, ''] for d in D]
v.table('eng12-u19-reported-1', ['Direct Speech', 'Indirect Speech'], R, ['براہِ راست کلام', 'بالواسطہ کلام'], ['مستقیمه وینا', 'غیرمستقیمه وینا'],
        caption='Pronoun change-Reported speech Exercise', captionUrdu='ضمیر کی تبدیلی — بالواسطہ کلام کی مشق', captionPashto='د ضمیر بدلون — د غیرمستقیمې وینا تمرین')
rec = BOOK.record(v, 'eng12-u19-vocab', 'Oral; Vocabulary A–D', 'زبانی ابلاغ؛ ذخیرۂ الفاظ A–D', 'د خولې اړیکه؛ لغات A–D', 120, [227, 228])
issues = [{'id': 'eng12-p227-228', 'unit': 19, 'printedPage': 227, 'description': 'Printed text retained: “Look for in a Thesaurus”, “each pair of words are”, “The glass plated” (plate), “My only wish is to become a good man” (She said), item D4 “You seem to be a nice” (cut off, no closing quote).'}]

if __name__ == '__main__':
    BOOK.save(120, [(19, rec)], issues=issues)
