"""PDF51 (printed 89–90): Unit 9 weather sentences 9–15; B shades of meaning (table, stronger/weaker); C first conditional 1–13."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
WS = [(f"The {B} bay can be dangerous if you aren't careful.", f'اگر آپ محتاط نہ ہوں تو {B} خلیج خطرناک ہو سکتی ہے۔', f'که پام ونه کړئ، {B} خلیج خطرناک کېدای شي.'),
      (f"It's so {B} today that I can't see any of the mountains.", f'آج اتنا {B} ہے کہ مجھے کوئی پہاڑ نظر نہیں آ رہا۔', f'نن دومره {B} ده چې هېڅ غر نه وینم.'),
      (f'The weather in Murree is often {B}.', f'مری میں موسم اکثر {B} ہوتا ہے۔', f'په مري کې هوا اکثرا {B} وي.'),
      (f'Spring weather often features {B} days followed by a few days of sunshine.', f'موسمِ بہار میں اکثر {B} دن ہوتے ہیں جن کے بعد چند دن دھوپ نکلتی ہے۔', f'د پسرلي هوا اکثرا {B} ورځې لري چې وروسته یې څو لمرینې ورځې راځي.'),
      (f"If you are a skier, you'll be happy to know that it will be {B} next week.", f'اگر آپ اسکیئر ہیں تو یہ جان کر خوش ہوں گے کہ اگلے ہفتے {B} ہو گا۔', f'که ته سکي‌کوونکی یې، دا په خبرېدو به خوشاله شې چې راتلونکې اونۍ به {B} وي.'),
      (f'The {B} weather put him into a foul mood.', f'{B} موسم نے اس کا موڈ خراب کر دیا۔', f'{B} هوا د هغه مزاج خراب کړ.'),
      (f'Winter is usually very {B} in the North.', f'شمال میں سردیاں عموماً بہت {B} ہوتی ہیں۔', f'په شمال کې ژمی معمولاً ډېر {B} وي.')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(WS, 9)])
w.p("B. 'Shades of meanings' is a phrase used to describe the small differences in meaning between similar words.", 'B. ’’معنی کے رنگ‘‘ ایک فقرہ ہے جو ملتے جلتے الفاظ کے معنی کے درمیان چھوٹے فرق کو بیان کرنے کے لیے استعمال ہوتا ہے۔', 'B. "د مانا رنګونه" یو عبارت دی چې د ورته کلمو د مانا ترمنځ د کوچنیو توپیرونو د بیانولو لپاره کارول کېږي.')
w.p('i. Match words with same shade of meanings in the following table.', 'i. درج ذیل جدول میں ایک جیسے معنوی رنگ والے الفاظ کو ملائیں۔', 'i. په لاندې جدول کې د یو شان معنوي رنګ کلمې سره برابرې کړئ.')
SH = [['Big', 'shout', 'bellow'], ['Misting', 'throw', 'enormous'], ['Nibble', 'frightened', 'gobble'], ['Scared', 'eat', 'pouring'], ['Toss', 'sprinkling', 'slam'], ['Yell', 'large', 'terrified']]
w.table('eng12-u09-shades', ['Light', 'Medium', 'strong'], SH, ['ہلکا', 'درمیانہ', 'شدید'], ['سپک', 'منځنی', 'قوي'], SH, SH)
w.p('ii. Fill in the blank in each sentence with a word that has a stronger meaning from the words given in the parenthesis.', 'ii. ہر جملے میں خالی جگہ قوسین میں دیے گئے الفاظ میں سے زیادہ شدید معنی والے لفظ سے پُر کریں۔', 'ii. په هره جمله کې تش ځای په قوسونو کې له ورکړل شویو کلمو د قوي مانا لرونکې کلمې سره ډک کړئ.')
S1 = [(f'She {B}, "Don\'t answer the phone." (said, scream)', f'اس نے {B}، ’’فون کا جواب مت دو۔‘‘ (said, scream)', f'هغې {B}، "تلیفون ته ځواب مه ورکوه." (said, scream)'),
      (f'Carl liked to stay inside during the {B} weather. (cold, freezing)', f'کارل {B} موسم میں اندر رہنا پسند کرتا تھا۔ (cold, freezing)', f'کارل خوښوله چې د {B} هوا پر مهال دننه پاتې شي. (cold, freezing)'),
      (f'The man was {B} about the long line at the store. (angry, furious)', f'دکان پر لمبی قطار کی وجہ سے آدمی {B} تھا۔ (angry, furious)', f'سړی په پلورنځي کې د اوږدې کتار له امله {B} و. (angry, furious)'),
      (f'When she woke up, it was {B}. (raining, pouring)', f'جب وہ جاگی تو {B} تھا۔ (raining, pouring)', f'کله چې راویښه شوه، {B} و. (raining, pouring)'),
      (f'The {B} dog growled at the postman. (large, gigantic)', f'{B} کتا ڈاکیے پر غرایا۔ (large, gigantic)', f'{B} سپي پر پوسټمین وغپل. (large, gigantic)')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(S1, 1)])
w.p('iii. Fill in the blank in each sentence with a word that has a weaker meaning from the words given in the parenthesis.', 'iii. ہر جملے میں خالی جگہ قوسین میں دیے گئے الفاظ میں سے کم شدید معنی والے لفظ سے پُر کریں۔', 'iii. په هره جمله کې تش ځای په قوسونو کې له ورکړل شویو کلمو د کمزورې مانا لرونکې کلمې سره ډک کړئ.')
S2 = [(f'She {B}, "Don\'t answer the phone." (said, whispered)', f'اس نے {B}، ’’فون کا جواب مت دو۔‘‘ (said, whispered)', f'هغې {B}، "تلیفون ته ځواب مه ورکوه." (said, whispered)'),
      (f'Carl liked to stay inside during the {B} weather. (cold, cool)', f'کارل {B} موسم میں اندر رہنا پسند کرتا تھا۔ (cold, cool)', f'کارل خوښوله چې د {B} هوا پر مهال دننه پاتې شي. (cold, cool)'),
      (f'The man was {B} about the long line at the store. (angry, cross)', f'دکان پر لمبی قطار کی وجہ سے آدمی {B} تھا۔ (angry, cross)', f'سړی په پلورنځي کې د اوږدې کتار له امله {B} و. (angry, cross)'),
      (f'When she woke up, it was {B}. (raining, sprinkling)', f'جب وہ جاگی تو {B} تھا۔ (raining, sprinkling)', f'کله چې راویښه شوه، {B} و. (raining, sprinkling)'),
      (f'The {B} dog growled at the postman. (big, large)', f'{B} کتا ڈاکیے پر غرایا۔ (big, large)', f'{B} سپي پر پوسټمین وغپل. (big, large)')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(S2, 1)])
w.p('C. Put the verb into the correct first conditional form', 'C. فعل کو پہلے شرطیہ کی درست شکل میں لکھیں', 'C. فعل د لومړي شرطي په سمه بڼه کې ولیکئ')
FC = ['If I ____ (go) out tonight, I ____ (go) to the cinema.', 'If you ____ (get) back late, I ____ (be) angry.', 'If we ____ (not / see) each other tomorrow, we ____ (see) each other next week.', 'If he ____ (come), I ____ (be) surprised.',
      'If we ____ (wait) here, we ____ (be) late.', 'If we ____ (go) on holiday this summer, we ____ (go) to Spain.', 'If the weather ____ (not / improve), we ____ (not / have) a picnic.', 'If I ____ (not / go) to bed early, I ____ (be) tired tomorrow.',
      'If we ____ (eat) all this cake, we ____ (feel) sick.', 'If you ____ (not / want) to go out, I ____ (cook) dinner at home.', 'I ____ (come) early if you ____ (want).', 'They ____ (go)to the party if they ____ (be)invited.', 'She ____ (stay)in London if she ____ (get)a job.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(FC, 1)])
for p in w.paras[-len(FC):]: p['untranslatedByDesign'] = True
rec = BOOK.record(w, 'eng12-u09-vocab-b', 'Weather sentences 9–15; Shades of meaning; First conditional', 'موسمی جملے 9–15؛ معنی کے رنگ؛ پہلا شرطیہ', 'د هوا جملې 9–15؛ د مانا رنګونه؛ لومړی شرطي', 51, [89, 90])
issues = [{'id': 'eng12-p89-90', 'unit': 9, 'printedPage': 89, 'description': 'Printed text retained: table cell “Misting” (light shade of “sprinkling/pouring”), header “strong” in lower case, “(go)to”, “(be)invited”, “(stay)in”, “(get)a job”. First-conditional items are grammar drills shown in English in all views.'}]

if __name__ == '__main__':
    BOOK.save(51, [(9, rec)], issues=issues)
