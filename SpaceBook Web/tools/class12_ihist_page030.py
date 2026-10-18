"""Islamic History XII PDF30: p.52 — Lessons 6–7 exercise Q4 (end); p.53 — Lesson 8 Mu'tasim billah (start). Run: python class12_ihist_page030.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L


def p30():
    b = Builder()
    b.p('4. Put a (✓) mark on the correct answer.', '۴۔ درست جواب پر (✓) کا نشان لگائیے۔', '۴. پر سم ځواب (✓) نښه ولګوئ.')
    L(b, [('a. Ma\'mun made ______ his prime minister. (Fadl bin Rabi\', Fadl bin Sahl, Abd al-Burhan)', 'الف: مامون نے اپنا وزیرِ اعظم ______ کو بنایا۔ (فضل بن ربیع، فضل بن سہل، عبدالبرہان)', 'الف. مامون ______ خپل لومړی وزیر کړ. (فضل بن ربیع، فضل بن سهل، عبدالبرهان)'),
          ('b. ______, because of rare books and high knowledge, is called the Philosopher of the Arabs. (Ya\'qub bin Ishaq, Husayn bin Ishaq, Qusta)', 'ب: ______ نادر کتابوں اور اعلیٰ علم کی وجہ سے فیلسوفِ عرب کہلاتا ہے۔ (یعقوب بن اسحاق، حسین بن اسحاق، قسطا)', 'ب. ______ د نادرو کتابونو او لوړ علم له امله «فیلسوف عرب» بلل کېږي. (یعقوب بن اسحاق، حسین بن اسحاق، قسطا)'),
          ('c. ______ advised Amin to make Ma\'mun and Mu\'taman withdraw. (Tahir bin Husayn, Fadl bin Rabi\', Ali bin \'Isa)', 'ج: ______ نے امین کو مشورہ دیا کہ مامون اور مؤتمن کو دستبردار کرے۔ (طاہر بن حسین، فضل بن ربیع، علی بن عیسیٰ)', 'ج. ______ امین ته مشوره ورکړه چې مامون او مؤتمن تېر کړي. (طاهر بن حسین، فضل بن ربیع، علي بن عیسی)'),
          ('d. ______ was Ma\'mun\'s slave. (Tahir, Ali, \'Isa)', 'د: ______ مامون کا غلام تھا۔ (طاہر، علی، عیسیٰ)', 'د. ______ د مامون غلام و. (طاهر، علي، عیسی)'),
          ('e. The people of Baghdad killed ______. (Ahmad, Burhan, Husayn)', 'ہ: اہلِ بغداد نے ______ کا قتل کر دیا۔ (احمد، برہان، حسین)', 'ه. د بغداد خلکو ______ ووژلو. (احمد، برهان، حسین)'),
          ('f. ______ did Ma\'mun\'s upbringing. (Fadl, Yahya, Ja\'far)', 'و: ______ نے مامون کی تربیت کی تھی۔ (فضل، یحییٰ، جعفر)', 'و. ______ د مامون روزنه کړې وه. (فضل، یحیی، جعفر)'),
          ('g. Ma\'mun threw ______ into jail. (Harthamah, Tahir, Ishaq)', 'ز: ______ کو مامون نے جیل میں ڈال دیا۔ (ہرثمہ، طاہر، اسحاق)', 'ز. مامون ______ زندان ته واچاوه. (هرثمه، طاهر، اسحاق)'),
          ('h. Ma\'mun married his daughter ______. (to Imam Rida, to Fadl, to Ibrahim)', 'ح: مامون نے اپنی بیٹی کی شادی ______ کرا دی۔ (امام رضا سے، فضل سے، ابراہیم سے)', 'ح. مامون خپله لور ______ ته واده کړه. (امام رضا، فضل، ابراهیم)')])
    r1 = rec(b, 7, 52, 30, [52], kind='exercise')
    t = Builder()
    t.p('Chapter: 4', 'باب: 4', 'باب: ۴')
    t.h('Abu Ishaq Muhammad bin Harun al-Mu\'tasim billah', 'ابواسحاق محمد بن ہارون معتصم باللہ', 'ابواسحاق محمد بن هارون معتصم بالله')
    t.p('833 CE to 842 CE', '۸۳۳ء تا ۸۴۲ء', '۸۳۳ع تر ۸۴۲ع')
    S(t, [(None, ('Ma\'mun, while dying, appointed his brother Muhammad bin Harun as his heir-apparent. Although his own son \'Abbas bin Ma\'mun was a military general of high degree, Ma\'mun selected Muhammad himself for the government. The army too wanted to make \'Abbas heir-apparent, but \'Abbas, respecting his father\'s testament, gave allegiance to Mu\'tasim billah.', 'مامون نے مرتے وقت اپنے بھائی محمد بن ہارون کو اپنا ولی عہد مقرر کیا۔ اگرچہ اس کا اپنا بیٹا عباس بن مامون اعلیٰ درجہ کا فوجی جرنیل تھا، لیکن مامون نے حکومت کے لئے محمد کو ہی منتخب کیا۔ فوج نے بھی عباس کو ولی عہد بنانا چاہا، لیکن عباس نے باپ کی وصیت کا لحاظ رکھتے ہوئے معتصم باللہ کی بیعت کر لی۔', 'مامون د مرګ پر مهال خپل ورور محمد بن هارون خپل ولیعهد وټاکه. که څه هم خپل زوی عباس بن مامون د لوړې درجې پوځي جنرال و، خو مامون د حکومت لپاره محمد وټاکه. پوځ هم غوښتل عباس ولیعهد کړي، خو عباس د پلار وصیت ته په درناوي د معتصم بالله بیعت وکړ.')),
          (('The end of Babak Khurrami:', 'بابک خرمی کا خاتمہ:', 'د بابک خرمي ختمېدل'),
           ('Babak\'s activities had begun from Ma\'mun\'s era. Mu\'tasim\'s general Afshin arrested him and presented him before the caliph. The caliph had his hands and feet cut off and had him killed. His brother Abdullah too was hanged in Baghdad.', 'بابک کی سرگرمیاں مامون کے دور سے شروع ہو چکی تھیں۔ معتصم کے جرنیل افشین نے اسے گرفتار کر کے خلیفہ کے سامنے پیش کیا۔ خلیفہ نے اس کے ہاتھ پاؤں کٹوا کر قتل کروا دیا۔ اس کے بھائی عبداللہ کو بھی بغداد میں پھانسی دی گئی۔', 'د بابک فعالیتونه د مامون له دورې پیل شوي وو. د معتصم جنرال افشین هغه ونیو او خلیفه ته یې وړاندې کړ؛ خلیفه یې لاسونه او پښې پرې کړې او ووژلو. ورور یې عبدالله هم په بغداد کې په دار وځړول شو.')),
          (('Revolts:', 'بغاوتیں:', 'بغاوتونه'),
           ('Maziyar, ruler of Tabaristan, revolted. According to Mas\'udi\'s account, Mu\'tasim\'s general Afshin, who was his co-religionist, had incited him to revolt. His own relatives handed him over to Mu\'tasim. Mu\'tasim gave him the punishment of lashes. He died of this very shock. His men also killed his brother Nawhayar.', 'مازیار والیٔ طبرستان نے بغاوت کی۔ مسعودی کے بیان کے مطابق معتصم کے جرنیل افشین جو کہ اس کا ہم مذہب تھا نے اسے بغاوت پر اکسایا تھا۔ اس کے اپنے ہی رشتہ داروں نے اسے معتصم کے حوالے کیا۔ معتصم نے اسے کوڑوں کی سزا دی۔ وہ اسی صدمے سے مر گیا۔ اس کے آدمیوں نے اس کے بھائی نوہیار کو بھی قتل کر دیا۔', 'د طبرستان والي مازیار بغاوت وکړه. د مسعودي د بیان له مخې، د معتصم جنرال افشین — چې د هغه هم‌مذهبه و — هغه بغاوت ته هڅولی و. د هغه خپلو خپلوانو هغه معتصم ته وسپاره؛ معتصم د کوړو سزا ورکړه؛ د همدې غم له امله مړ شو. د هغه کسانو ورور یې نوهیار هم ووژه.'))])
    BOOK.save(30, [(7, r1), (8, rec(t, 8, 53, 30, [53], first=True))], complete_units=[7], issues=[{'id': 'ihist12-pdf030', 'unit': 7, 'printedPage': 52,
               'description': 'p.52: blanks filled and options ticked by a student in handwriting — excluded; no printed key. Lesson 8 (Mu\'tasim) opens on p.53 under the book heading "باب: 4". Student marks (dates "833/842", "①", underlining) excluded.'}])


if __name__ == '__main__':
    p30()
