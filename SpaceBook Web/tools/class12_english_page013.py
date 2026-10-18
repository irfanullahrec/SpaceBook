"""PDF13 (printed 13–14): diphthongs 39–44; Activity A (phonetic transcription → spelling tables); Activity B (opposite verbs) items 1–11."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
D = [['39', '/oʊ/', 'o, oa, o_e, oe, ow, ough, eau, oo, ew', 'open, moat, bone, toe, sow, dough, beau, brooch, sew'], ['40', '/ɔɪ/', 'oi, oy, uoy', 'join, boy, buoy'],
     ['41', '/aʊ/', 'ow, ou, ough', 'now, shout, bough'], ['42', '/eə/', 'air, are, ear, ere, eir, ayer', 'chair, dare, pear, where, their, prayer'],
     ['43', '/ɪə/', 'ear, eer, ere, ier', 'ear, steer, here, tier'], ['44', '/ʊə/', 'ure, our', 'Cure, tourist']]
v.table('eng12-u01-diphthongs-b', ['Phoneme', 'IPA Symbols', 'Grapheme', 'Examples'], D, ['صوتیہ', 'IPA علامت', 'گریفیم', 'مثالیں'], ['غږ‌پوړی', 'IPA نښه', 'ګرافیمونه', 'بېلګې'], D, D)
v.h('Activity', 'سرگرمی', 'فعالیت')
v.p('A. Read the phonetic transcription of the words given in the table below and write their spellings in front of them.', 'A. نیچے جدول میں دیے گئے الفاظ کی صوتی نقل پڑھیں اور ان کے سامنے ان کے ہجے لکھیں۔', 'A. په لاندې جدول کې د ورکړل شویو کلمو غږیز لیکدود ولولئ او د هغوی مخې ته یې املا ولیکئ.')
BODY = ['/ɑ:m/', '/ɪə /', '/aɪ /', '/feɪs /', '/fʊt /', '/heə /', '/hænd/', '/maʊθ/', '/nəʊz /', "/'ʃəʊldə/"]
BATH = ['kəʊm', "ʃæm'pu:", "'neɪlfaɪl", "pə'fju:m", "'taʊəl", "'ʃeɪvə", 'səʊp', "heə'draɪə", "'tu:θpeɪst", 'spreɪ']
R1 = [[a, '', b, ''] for a, b in zip(BODY, BATH)]
v.table('eng12-u01-ipa-activity-a', ['Body Parts — Phonetic Transcription', 'Spelling', 'Things used in the Bathroom — Phonetic Transcription', 'Spelling'], R1,
        ['جسم کے اعضاء — صوتی نقل', 'ہجے', 'غسل خانے میں استعمال ہونے والی اشیاء — صوتی نقل', 'ہجے'], ['د بدن غړي — غږیز لیکدود', 'املا', 'په تشناب کې کارېدونکي توکي — غږیز لیکدود', 'املا'], R1, R1)
HOUSE = ['/flɔ: /', "/'bɑ:θru:m /", "/'kɪtʃɪn/", "/'selə /", "/ˌʌp'steəz/", "/'si:lɪŋ /", "/'tʃɪmni/", '/ru:f/', '/steəz/', "/'ætɪk/"]
NUM = ['/faɪv/', '/wʌn /', '/naɪn/', '/θri:/', '/fɔ:/', '/tu:/', '/eɪt/', "/fɔ:'ti:n/", "/fɪf'ti:n/", "/θɜ:'ti:n/"]
R2 = [[a, '', b, ''] for a, b in zip(HOUSE, NUM)]
v.table('eng12-u01-ipa-activity-b', ['Things used in bathroom — Phonetic Transcription', 'Spelling', 'Numbers — Phonetic Transcription', 'Spelling'], R2,
        ['غسل خانے میں استعمال ہونے والی اشیاء — صوتی نقل', 'ہجے', 'اعداد — صوتی نقل', 'ہجے'], ['په تشناب کې کارېدونکي توکي — غږیز لیکدود', 'املا', 'شمېرې — غږیز لیکدود', 'املا'], R2, R2)
v.p('B. Complete the sentences by using the opposite of the verbs in brackets at the end of each sentence. Use the words in the box. You may need to change the forms of these verbs.', 'B. ہر جملے کے آخر میں قوسین میں دیے گئے افعال کے متضاد استعمال کر کے جملے مکمل کریں۔ خانے میں دیے گئے الفاظ استعمال کریں۔ آپ کو ان افعال کی شکلیں بدلنے کی ضرورت پڑ سکتی ہے۔', 'B. د هرې جملې په پای کې په قوسونو کې د ورکړل شویو فعلونو د ضد په کارولو جملې بشپړې کړئ. په بکس کې ورکړل شوې کلمې وکاروئ. کېدای شي د دې فعلونو بڼې بدلولو ته اړتیا ولرئ.')
v.p('admit, ban, defend, destroy, empty, fail, fall, forget, laugh, leave, lend, loosen, lose, miss, punish, receive, reject, spend, succeed, teach', 'admit, ban, defend, destroy, empty, fail, fall, forget, laugh, leave, lend, loosen, lose, miss, punish, receive, reject, spend, succeed, teach', 'admit, ban, defend, destroy, empty, fail, fall, forget, laugh, leave, lend, loosen, lose, miss, punish, receive, reject, spend, succeed, teach')
v.paras[-1]['untranslatedByDesign'] = True
B = '________'
v.group('lines', [
    (f'1. She tripped over the carpet and everyone {B}. (cry)', f'1. وہ قالین سے ٹھوکر کھا گئی اور سب نے {B}۔ (cry — رونا)', f'1. هغه په غالۍ ټکر وخوړ او ټولو {B}. (cry — ژړل)'),
    (f'2. He {B} the bottle of spoilt milk into the sink. (fill)', f'2. اس نے خراب دودھ کی بوتل سنک میں {B}۔ (fill — بھرنا)', f'2. هغه د خراب شوي شیدو بوتل په سینک کې {B}. (fill — ډکول)'),
    (f"3. Don't {B} to come to our party tomorrow. (remember)", f'3. کل ہماری پارٹی میں آنا {B} مت۔ (remember — یاد رکھنا)', f'3. سبا زموږ مېلمستیا ته راتلل مه {B}. (remember — یادول)'),
    (f'4. We have {B} in stopping the spread of the illness. (fail)', f'4. ہم بیماری کے پھیلاؤ کو روکنے میں {B} ہیں۔ (fail — ناکام ہونا)', f'4. موږ د ناروغۍ د خپرېدو په مخنیوي کې {B} یو. (fail — ناکامېدل)'),
    (f'5. When does your train {B}? (arrive)', f'5. آپ کی ٹرین کب {B}؟ (arrive — پہنچنا)', f'5. ستاسو اورګاډی کله {B}؟ (arrive — رسېدل)'),
    (f"6. We {B} too much money on unimportant things we really don't need. (s…)", f'6. ہم غیر اہم چیزوں پر بہت زیادہ پیسہ {B} جن کی ہمیں واقعی ضرورت نہیں۔ (s…)', f'6. موږ پر داسې بې‌اهمیته شیانو ډېرې پیسې {B} چې واقعاً ورته اړتیا نه لرو. (s…)'),
    (f'7. The dollar has {B} against the euro recently (rise).', f'7. حال ہی میں ڈالر یورو کے مقابلے میں {B} ہے (rise — چڑھنا)۔', f'7. ډالر پدې وروستیو کې د یورو پر وړاندې {B} (rise — لوړېدل).'),
    (f'8. The car {B} the tree and crashed into a telephone pole instead. (…)', f'8. گاڑی درخت سے {B} اور اس کے بجائے ٹیلی فون کے کھمبے سے جا ٹکرائی۔ (…)', f'8. موټر له ونې {B} او پر ځای یې د ټیلیفون له پایې سره ټکر شو. (…)'),
    (f'9. The exam was very difficult. As a result, most of the students {B} (pass)', f'9. امتحان بہت مشکل تھا۔ نتیجتاً زیادہ تر طلبہ {B} (pass — پاس ہونا)', f'9. ازموینه ډېره سخته وه. په پایله کې ډېری زده کوونکي {B} (pass — بریالي کېدل)'),
    (f"10. We don't expect our team to {B} tomorrow. (win)", f'10. ہمیں توقع نہیں کہ ہماری ٹیم کل {B}۔ (win — جیتنا)', f'10. موږ تمه نه لرو چې زموږ ټیم سبا {B}. (win — ګټل)'),
    (f'11. She {B} being the source of the rumours. (deny)', f'11. اس نے افواہوں کا ذریعہ ہونے کو {B}۔ (deny — انکار کرنا)', f'11. هغې د اوازو د سرچینې کېدل {B}. (deny — انکار کول)'),
])
ex = BOOK.record(v, 'eng12-u01-activities-a', 'Diphthongs (end); Activities A and B', 'دوہرے مصوتے (اختتام)؛ سرگرمیاں A اور B', 'دوه‌غږیز (پای)؛ فعالیتونه A او B', 13, [13, 14])
issues = [{'id': 'eng12-p13-14-cut', 'unit': 1, 'printedPage': 14, 'description': 'Activity B: the brackets of items 6 and 8 are cut off at the binding edge of the scan (“(s…”, “(…”); shown as cut. The second activity table is headed “Things used in bathroom” although it lists parts of a house (floor, bathroom, kitchen, cellar…); printed heading retained. “change th forms” (OCR) is printed “the forms”.'}]

if __name__ == '__main__':
    BOOK.save(13, [(1, ex)], issues=issues)
