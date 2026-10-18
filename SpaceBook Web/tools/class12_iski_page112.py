"""Islamiat (Ikhtiari) XII PDF112: p.214 — activity chart (end ch.5); p.215 — Chapter 6 Arabic language and literature opening. Run: python class12_iski_page112.py"""
from class12_iski_common import BOOK, Builder, rec, P

C = [('Pakistan', 'پاکستان', 'پاکستان'), ('Iran', 'ایران', 'ایران'), ('Afghanistan', 'افغانستان', 'افغانستان'), ('Saudi Arabia', 'سعودی عرب', 'سعودي عربستان'),
     ('Turkey', 'ترکی', 'ترکیه'), ('United Arab Emirates', 'متحدہ عرب امارات', 'متحده عربي امارات'), ('Indonesia', 'انڈونیشیا', 'اندونیزیا'),
     ('Bangladesh', 'بنگلہ دیش', 'بنګله‌دېش'), ('Sudan', 'سوڈان', 'سوډان'), ('Egypt', 'مصر', 'مصر')]


def p112():
    b = Builder()
    b.h('Activity: Complete the following chart.', 'سرگرمی: مندرجہ ذیل چارٹ کو مکمل کریں۔', 'فعالیت: لاندې چارټ بشپړ کړئ.')
    rows_e, rows_u, rows_p = [], [], []
    for i, (e, u, p) in enumerate(C, 1):
        if i == 1:
            rows_e.append([str(i), e, 'approximately 18 crore', 'Rupee', 'Islamabad'])
            rows_u.append([str(i), u, 'تقریباً 18 کروڑ', 'روپیہ', 'اسلام آباد'])
            rows_p.append([str(i), p, 'نږدې ۱۸ کروړه', 'روپۍ', 'اسلام‌اباد'])
        else:
            rows_e.append([str(i), e, '', '', ''])
            rows_u.append([str(i), u, '', '', ''])
            rows_p.append([str(i), p, '', '', ''])
    b.table('iski12-chart-ch5', ['No.', 'Name of Islamic country', 'Population', 'Currency', 'Capital'], rows_e,
            ['نمبر شمار', 'نام اسلامی ملک', 'آبادی', 'کرنسی', 'دار الحکومت'], ['شمېره', 'د اسلامي هېواد نوم', 'نفوس', 'اسعار', 'پلازمېنه'], rows_u, rows_p)
    r1 = rec(b, 5, 214, 112, [214], kind='exercise')
    t = Builder()
    t.h('Chapter Six: Arabic language and literature', 'بابِ ششم: عربی زبان و ادب', 'شپږم څپرکی: عربي ژبه او ادب')
    t.h('Teaching objectives', 'تدریسی مقاصد', 'تدریسي موخې')
    t.p('The purpose of this lesson is to enable the students that they: acquire so much skill in the Arabic language that they can read and understand Islamic teachings in the Arabic text.', 'اس سبق کا مقصد طلبہ اور طالبات کو اس قابل بنانا ہے کہ وہ: عربی زبان میں اس قدر مہارت حاصل کر لیں تاکہ اسلامی تعلیمات عربی متن میں پڑھ اور سمجھ سکیں۔', 'د دې لوست موخه دا ده چې زده‌کوونکي دې ته وړ کړي چې: په عربي ژبه کې دومره مهارت ترلاسه کړي چې اسلامي لارښوونې په عربي متن کې ولولي او پوه شي.')
    t.h('Study of the Arabic language', 'عربی زبان کا مطالعہ', 'د عربي ژبې مطالعه')
    t.p('Before the sun of Islam rose, Arabic literature was at its peak. Especially in poetry the Arabs had attained perfection, and every tribe used to take pride in its poets. And if some tribe had no poet, it was considered a cause of shame for it. The Arabs considered themselves more eloquent than all other people. One meaning of \'Arab is also one possessing a clear and lucid tongue, and in contrast to it they used to call non-Arabs \'Ajam, whose meaning is dumb. In these circumstances Allah the Exalted sent His last Messenger ﷺ and sent down the Holy Quran upon him, which made the tongues of the Arabs, who used to call themselves very eloquent, dumb. They began to say, "Is it the poetry of some poet, or the sorcery of some sorcerer, or the rhymed speech of some soothsayer?" (Tarikh al-Adab al-\'Arabi, Ahmad Hasan al-Zayyat, p.67, al-Maktabah al-\'Ilmiyyah)', 'اسلام کا سورج طلوع ہونے سے پہلے عربی ادب اپنے عروج پر تھا۔ خصوصاً شاعری میں عربوں کو کمال حاصل تھا اور ہر قبیلہ اپنے شاعروں پر فخر کیا کرتا تھا۔ اور اگر کسی قبیلے کا شاعر نہ ہوتا تو اس کو باعثِ عار سمجھا جاتا تھا۔ عرب اپنے آپ کو باقی تمام لوگوں سے فصیح سمجھتے تھے۔ عرب کا ایک معنی صاف اور واضح زبان والا ہونا بھی ہے اور اس کے مقابلے میں وہ غیر عربوں کو عجم کہتے تھے جس کا معنی ہے گونگا۔ ان حالات میں اللہ تعالیٰ نے اپنے آخری رسول صلی اللہ علیہ وآلہٖ وسلم کو بھیج کر ان پر قرآن مجید نازل فرمایا جس نے عربوں کی زبانوں کو گنگ کر دیا جو اپنے آپ کو بڑا فصیح کہا کرتے تھے وہ کہنے لگے کہ ”یہ کسی شاعر کی شاعری یا جادوگر کی جادوگری یا کاہن کی سجع ہے“ (تاریخ الادب العربی، احمد حسن الزیات، ص 67 المکتبۃ العلمیہ)', 'د اسلام لمر له راختو مخکې عربي ادب په خپل عروج کې و. په ځانګړي ډول په شاعرۍ کې عربانو کمال درلود، او هرې قبیلې په خپلو شاعرانو ویاړ کاوه؛ او که کومه قبیله شاعر نه درلود، د شرم سبب ګڼل کېده. عربانو ځانونه تر نورو ټولو خلکو فصیح ګڼل. د «عرب» یوه مانا د روښانه او ښکاره ژبې خاوند هم ده، او د دې پر وړاندې یې غیرعربانو ته «عجم» ویل چې مانا یې ګونګ ده. په دې حالاتو کې الله تعالی خپل وروستی رسول ﷺ ولېږه او پر هغه یې قرآن مجید نازل کړ، چې د هغو عربانو ژبې یې ګونګې کړې چې ځانونه یې ډېر فصیح بلل؛ هغوی ویل پیل کړل: «دا د کوم شاعر شعر دی، یا د کوم کوډګر کوډې، یا د کوم کاهن سجع؟» (تاریخ الادب العربي، احمد حسن الزیات، ۶۷ مخ، المکتبه العلمیه)')
    BOOK.save(112, [(5, r1), (6, rec(t, 6, 215, 112, [215], first=True))], complete_units=[5], issues=[{'id': 'iski12-pdf112', 'unit': 5, 'printedPage': 214,
               'description': 'End of Chapter 5: activity chart reproduced as a structured table with only the printed sample row (Pakistan) filled. Heavy student scribbles over the heading of p.214 and a handwritten line "مندرجہ ذیل چارٹ کو مکمل کریں" below the table excluded. p.215 opens Chapter 6; the reference to al-Zayyat\'s Tarikh al-Adab al-\'Arabi is printed partly in bold and partly obscured at the edge — read as given.'}])


if __name__ == '__main__':
    p112()
