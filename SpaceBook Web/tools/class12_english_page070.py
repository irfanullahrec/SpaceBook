"""PDF70 (printed 127–128): Unit 13 connotation exercise 8–19; B third conditional 1–13."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
q = Builder()
CN = [
    ('8. plant, sweatshop, factory, manufacturing, workshop', f'{B} and {B} are synonyms. {B} has a negative connotation and communicates that people work long hours for little pay. A {B} is smaller than a {B}. Also, a {B} is a place where things might be manufactured and/or repaired.'),
    ('9. warranty, guarantee', f'A {B} is a written document stating that a product will be repaired or replaced if it becomes defective. A {B} is not always written and usually not as specific as a warranty. A more complete explanation of the difference can be found here.'),
    ('10. Ashamed, embarrassed, mortified', f'Someone {B} has done something morally wrong and feels guilty about it. Someone {B} has done something that will cause others to think less of him (but not something morally wrong). {B} is a stronger version of embarrassed.'),
    ('11. Manager, supervisor, boss', f'{B} has a negative connotation whereas {B} and {B} do not. Also, a {B} is in charge of people whereas a {B} may have additional responsibilities, such as meeting the financial objectives of the company.'),
    ('12. expense, cost, investment, price', f'{B} and {B} have a neutral connotation. {B} has a negative connotation. {B} has a positive connotation as it suggests that the benefit of the purchase will outweigh the cost.'),
    ('13. Plenty, sufficient, adequate,', f'{B} has a more positive connotation than {B}. {B} communicates that there is "barely enough." {B} communicates that there is enough. {B} communicates that there is much more than what is needed.'),
    ('14. to come up short, to fail, to miss the mark', f'{B} has a negative connotation. {B} and {B} have a more positive connotation.'),
    ('15. youthful, immature, young', f'{B} has a neutral connotation, {B} has a positive connotation, and {B} has a negative connotation.'),
    ('16. to stare, to glare, to look, to watch,', f"We typically use {B} to communicate that someone is visually focusing on something that is not moving ({B} at the screen, {B} at me, {B} at the picture, {B} at the chart/graph, etc.). We use {B} to communicate that someone is visually focusing on something that is moving ({B} the game, {B} the race, etc.). To {B} means to look at someone without averting one's eyes. {B} means to stare at someone with hatred or disapproval."),
    ('17. Sincere, honest', f'If someone is being {B}, they are telling the truth. If someone is being {B}, they are being genuine and their actions and words reflect how they really feel. As this page points out, sometimes the words can be used as synonyms.'),
    ('18. thrifty, frugal, stingy, cheap', f'{B} and {B} have negative connotations. {B} and {B} have positive connotations. Also, {B} refers to not wanting to part with money, but {B} refers to not wanting to part with something of value (money, time, food, etc.).'),
    ('19. unique, odd strange, weird, unusual', f'{B} is neutral. {B}, {B}, and {B} have a negative connotation. {B} has a positive connotation.'),
]
for head, body in CN:
    q.p(head, head, head); q.paras[-1]['untranslatedByDesign'] = True
    q.p(body, body, body); q.paras[-1]['untranslatedByDesign'] = True
q.p('B. Put in the correct third conditional verb form:', 'B. تیسرے شرطیہ کے فعل کی درست شکل لکھیں:', 'B. د درېیم شرطي د فعل سمه بڼه ولیکئ:')
TC = ['If you ____ (not / be) late, we ____ (not / miss) the bus.', 'If she ____ (study), she ____ (pass) the exam.', 'If we ____ (arrive) earlier, we ____ (see) Ajmal.', 'If they ____ (go) to bed early, they ____ (not / wake) up late.',
      'If he ____ (become) a musician, he ____ (record) a CD.', 'If she ____ (go) to art school, she ____ (become) a painter.', 'If I ____ (be) born in a different country, I ____ (learn) to speak a different language.',
      'If she ____ (go) to university, she ____ (study) English.', 'If we ____ (not / go) to the party, we ____ (not / meet) them.', 'If he ____ (take) the job, he ____ (not / go) travelling.',
      'He ____ (be) happier if he ____ (stay) at home.', 'She ____ (pass) the exam if she ____ (study) harder.', 'We ____ (not / get) married if we ____ (not / go) to the same university.']
q.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(TC, 1)])
for p in q.paras[-len(TC):]: p['untranslatedByDesign'] = True
rec = BOOK.record(q, 'eng12-u13-vocab-b', 'Vocabulary A (connotation 8–19); B third conditional', 'ذخیرۂ الفاظ A (ضمنی معنی 8–19)؛ B تیسرا شرطیہ', 'لغات A (ضمني مانا 8–19)؛ B درېیم شرطي', 70, [127, 128])
issues = [{'id': 'eng12-p127-128', 'unit': 13, 'printedPage': 127, 'description': 'Printed text retained: item 9 “can be found here.” and item 17 “As this page points out” (references to a web page the exercise was taken from), “odd strange” (missing comma), “Strategy” capitalised; right edge of p127 slightly clipped (“repaired or replaced”, “usually not”), completed from context.'}]

if __name__ == '__main__':
    BOOK.save(70, [(13, rec)], issues=issues)
