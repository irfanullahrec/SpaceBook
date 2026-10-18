"""PDF93 (printed 173–174): Direct-Indirect speech — reflexive pronoun table; auxiliary verbs; adverbs; interrogative; exclamatory and imperative; worked example (Sophia)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
H = {'en': ['Person', 'Singular', 'Plural', 'Emphatic and Reflexive'], 'ur': ['شخص', 'واحد', 'جمع', 'تاکیدی اور انعکاسی'], 'ps': ['شخص', 'مفرد', 'جمع', 'ټینګاري او انعکاسي']}
R = [['1st', 'myself', 'ourselves', ''], ['2nd', 'yourself', 'yourselves', ''], ['3rd', 'himself, herself itself', 'themselves', '']]
w.table('eng12-u17-person-4', H['en'], R, H['ur'], H['ps'])
for x in [
    ("So in sentence [1] above we change the pronoun from 1st person `I` to 3rd person `He'.", "چنانچہ اوپر جملہ [1] میں ہم ضمیر کو پہلے شخص `I` سے تیسرے شخص `He' میں بدلتے ہیں۔", "نو پورته په جمله [1] کې ضمیر له لومړي شخص `I` څخه درېیم شخص `He' ته بدلوو."),
]: w.p(*x)
w.h('Auxiliary Verbs', 'امدادی افعال', 'مرستندوی فعلونه')
for x in [
    ('There are two forms of the auxiliary verb: the primary auxiliaries and the modal auxiliaries.', 'امدادی فعل کی دو صورتیں ہیں: بنیادی امدادی افعال اور موڈل امدادی افعال۔', 'د مرستندوی فعل دوه بڼې دي: لومړني مرستندوي او موډل مرستندوي.'),
    ("The primary auxiliaries are: `to be`- is, am, are, was and were. `to do`- do, does and did. `to have`- have, has and had.", "بنیادی امدادی افعال یہ ہیں: `to be` - is, am, are, was اور were۔ `to do` - do, does اور did۔ `to have` - have, has اور had۔", "لومړني مرستندوي دا دي: `to be` - is, am, are, was او were. `to do` - do, does او did. `to have` - have, has او had."),
    ('The modal auxiliaries are: can could, will would, shall should, may might, must, need and dare.', 'موڈل امدادی افعال یہ ہیں: can could, will would, shall should, may might, must, need اور dare۔', 'موډل مرستندوي دا دي: can could, will would, shall should, may might, must, need او dare.'),
    ("A regular verb like `sit` has the present tense form `sit` and the past tense form `sat`. Just as a regular verb has these two forms, the auxiliaries also have two forms.", "باقاعدہ فعل جیسے `sit` کی حال کی شکل `sit` اور ماضی کی شکل `sat` ہے۔ جیسے باقاعدہ فعل کی یہ دو شکلیں ہیں، اسی طرح امدادی افعال کی بھی دو شکلیں ہیں۔", "یو منظم فعل لکه `sit` د حال بڼه `sit` او د تېر بڼه `sat` لري. لکه څنګه چې منظم فعل دا دوه بڼې لري، مرستندوي هم دوه بڼې لري."),
    ("The present tense forms of `to be` are: is, am and are. The past tense forms are: was, were.", "`to be` کی حال کی شکلیں ہیں: is, am اور are۔ ماضی کی شکلیں ہیں: was, were۔", "د `to be` د حال بڼې دا دي: is, am او are. د تېر بڼې دا دي: was, were."),
    ("We can compare two sentences to find out the `tense` of an auxiliary verb", 'کسی امدادی فعل کا ’’زمانہ‘‘ معلوم کرنے کے لیے ہم دو جملوں کا موازنہ کر سکتے ہیں', 'د یو مرستندوي فعل د "زمان" موندلو لپاره دوه جملې پرتله کولی شو'),
    ('Form simple sentences using the auxiliaries:', 'امدادی افعال استعمال کر کے سادہ جملے بنائیں:', 'د مرستندویو په کارولو ساده جملې جوړې کړئ:'),
]: w.p(*x)
w.group('list', [('{1}I am here, and',) * 3, ('{2}I was here.',) * 3])
for p in w.paras[-2:]: p['untranslatedByDesign'] = True
for x in [
    ('We see that the second sentence is in the past tense and the first sentence is in the present tense.', 'ہم دیکھتے ہیں کہ دوسرا جملہ ماضی میں اور پہلا جملہ حال میں ہے۔', 'وینو چې دویمه جمله په تېر او لومړۍ جمله په حال زمان کې ده.'),
    ('Similarly, by forming simple sentences, we can find out the tense of any of the auxiliaries.', 'اسی طرح سادہ جملے بنا کر ہم کسی بھی امدادی فعل کا زمانہ معلوم کر سکتے ہیں۔', 'همداسې، د ساده جملو په جوړولو کولی شو د هر مرستندوي زمان معلوم کړو.'),
    ('So, we change from the present tense to the past tense when changing to Indirect speech in sentence [2] above.', 'چنانچہ اوپر جملہ [2] میں بالواسطہ کلام میں بدلتے وقت ہم حال سے ماضی میں بدلتے ہیں۔', 'نو پورته په جمله [2] کې غیرمستقیمې وینا ته د بدلولو پر مهال له حال څخه تېر ته بدلوو.'),
]: w.p(*x)
w.h('[Heading box printed blank — the section is about adverbs]', '[سرخی کا خانہ درسی کتاب میں خالی چھپا ہے — یہ حصہ متعلق فعل کے بارے میں ہے]', '[د سرلیک بکس په چاپي کتاب کې تش دی — دا برخه د قیدونو په اړه ده]')
w.p("Adverbs are words showing `where` and `when` something happened. Some adverbs are `here` which is changes to `there`, `today` which becomes `that day`, `tomorrow` which becomes `the next day` and so on.",
    "متعلق فعل وہ الفاظ ہیں جو بتاتے ہیں کہ کوئی بات ’’کہاں‘‘ اور ’’کب‘‘ ہوئی۔ کچھ متعلق فعل یہ ہیں: `here` جو `there` میں بدلتا ہے، `today` جو `that day` بن جاتا ہے، `tomorrow` جو `the next day` بن جاتا ہے، وغیرہ۔",
    "قیدونه هغه کلمې دي چې ښيي یو کار \"چېرته\" او \"کله\" وشو. ځینې قیدونه دا دي: `here` چې په `there` بدلېږي، `today` چې `that day` کېږي، `tomorrow` چې `the next day` کېږي، او داسې نور.")
w.p('In short, we change the pronouns, the verbs and the adverbs when we change from Direct to Indirect speech.', 'مختصراً، براہِ راست سے بالواسطہ کلام میں بدلتے وقت ہم ضمائر، افعال اور متعلق افعال بدلتے ہیں۔', 'په لنډه توګه، کله چې له مستقیمې څخه غیرمستقیمې وینا ته بدلوو، ضمیرونه، فعلونه او قیدونه بدلوو.')
a = BOOK.record(w, 'eng12-u17-vocab-d', 'Direct–Indirect speech (3): reflexive pronouns, auxiliaries, adverbs', 'براہِ راست/بالواسطہ کلام (3): انعکاسی ضمائر، امدادی افعال، متعلق فعل', 'مستقیمه/غیرمستقیمه وینا (3): انعکاسي ضمیرونه، مرستندوي، قیدونه', 93, [173, 174])

x = Builder()
x.h('Interrogative sentences:', 'استفہامیہ جملے:', 'پوښتنیزې جملې:')
x.p('Look at the following question:', 'درج ذیل سوال کو دیکھیں:', 'لاندې پوښتنې ته وګورئ:')
x.p('He said,” Are you here?”', 'He said,” Are you here?”', 'He said,” Are you here?”'); x.paras[-1]['untranslatedByDesign'] = True
for t in [
    ("In this sentence, the auxiliary verb `are` comes first and then the subject `you`.", 'اس جملے میں امدادی فعل `are` پہلے آتا ہے اور پھر فاعل `you`۔', 'په دې جمله کې مرستندوی فعل `are` لومړی راځي او بیا فاعل `you`.'),
    ('When we change the sentence into Indirect speech the positions of subject and verb are interchanged, as in:', 'جب ہم جملے کو بالواسطہ کلام میں بدلتے ہیں تو فاعل اور فعل کی جگہیں بدل جاتی ہیں، جیسے:', 'کله چې جمله غیرمستقیمې وینا ته بدلوو، د فاعل او فعل ځایونه بدلېږي، لکه:'),
]: x.p(*t)
x.p('He asked whether he was there.', 'He asked whether he was there.', 'He asked whether he was there.'); x.paras[-1]['untranslatedByDesign'] = True
for t in [
    ('Once again the pronoun is changed to third person and the verb is changed to the past tense.', 'ایک بار پھر ضمیر تیسرے شخص میں اور فعل ماضی میں بدل جاتا ہے۔', 'یو ځل بیا ضمیر درېیم شخص ته او فعل تېر زمان ته بدلېږي.'),
    ('The reporting verb can be asked or inquired to name but two.', 'بیانیہ فعل asked یا inquired ہو سکتا ہے، صرف دو کا نام لیں تو۔', 'د راپور فعل asked یا inquired کېدای شي، که یوازې دوه یاد کړو.'),
    ("The word `whether` is placed after the reporting verb. It can also be replaced with its equivalent `if`.", "لفظ `whether` بیانیہ فعل کے بعد رکھا جاتا ہے۔ اسے اس کے ہم معنی `if` سے بھی بدلا جا سکتا ہے۔", "کلمه `whether` د راپور فعل وروسته ایښودل کېږي. د هغې ورته `if` سره هم بدلېدای شي."),
]: x.p(*t)
x.h('Exclamatory and Imperative sentences:', 'ندائیہ اور امریہ جملے:', 'ندايي او امري جملې:')
x.p("An exclamatory sentence shows strong emotion. A reporting verb for an exclamatory sentence can be `exclaimed`. For an Imperative sentence which shows a command or a request, the reporting verbs can be `ordered`, `requested` etc. Often the subject is implied in Imperative sentences:",
    "ندائیہ جملہ شدید جذبہ ظاہر کرتی ہے۔ ندائیہ جملے کے لیے بیانیہ فعل `exclaimed` ہو سکتا ہے۔ امریہ جملے کے لیے، جو حکم یا درخواست ظاہر کرتا ہے، بیانیہ افعال `ordered`، `requested` وغیرہ ہو سکتے ہیں۔ امریہ جملوں میں اکثر فاعل مضمر ہوتا ہے:",
    "ندايي جمله قوي احساس ښيي. د ندايي جملې لپاره د راپور فعل `exclaimed` کېدای شي. د امري جملې لپاره، چې امر یا غوښتنه ښيي، د راپور فعلونه `ordered`، `requested` او نور کېدای شي. په امري جملو کې ډېری وخت فاعل پټ وي:")
x.p('“Sit!” said the teacher to the students. Here the subject is: [You] Sit. So the sentences in Indirect becomes, The teacher told them to sit.', '“Sit!” said the teacher to the students. یہاں فاعل یہ ہے: [You] Sit۔ چنانچہ بالواسطہ میں جملہ بنتا ہے: The teacher told them to sit.', '“Sit!” said the teacher to the students. دلته فاعل دا دی: [You] Sit. نو په غیرمستقیمه کې جمله کېږي: The teacher told them to sit.')
x.p('So, let us look at some sentences which are changed into Indirect speech using the above rules:', 'تو آئیے کچھ جملے دیکھیں جو اوپر کے قواعد کے مطابق بالواسطہ کلام میں بدلے گئے ہیں:', 'نو راځئ ځینې جملې وګورو چې د پورته قواعدو په کارولو غیرمستقیمې وینا ته بدلې شوې دي:')
for t in ['“ You’re going to write, aren’t you? ` asked Sophia.',
          "`Is that nothing? I’ve promised myself that you’re going to write your stories and become famous. And while you’re writing, I’ll stand behind you and read over your shoulder.” he said to her.",
          'Sophia asked whether he was going to write. He asked her if that was nothing? He had promised himself that she was going to write her stories and become famous. And while she was writing, he would stand behind her and read over her shoulder']:
    x.p(t, t, t); x.paras[-1]['untranslatedByDesign'] = True
b = BOOK.record(x, 'eng12-u17-vocab-e', 'Direct–Indirect speech (4): interrogative, exclamatory, imperative; example', 'براہِ راست/بالواسطہ کلام (4): استفہامیہ، ندائیہ، امریہ؛ مثال', 'مستقیمه/غیرمستقیمه وینا (4): پوښتنیزې، ندايي، امري؛ بېلګه', 93, [174])
issues = [{'id': 'eng12-p173-174', 'unit': 17, 'printedPage': 173, 'description': 'The heading box before the adverbs paragraph is printed blank (p.173); shown with a note. Reflexive table: “itself” printed on its own line under the 3rd-person singular; column “Emphatic and Reflexive” empty. Retained: “which is changes to”, “name but two”, mismatched quotation marks in the Sophia example, and the worked indirect version “Sophia asked whether he was going to write” (should be “she … I/you”).'}]

if __name__ == '__main__':
    BOOK.save(93, [(17, a), (17, b)], issues=issues)
