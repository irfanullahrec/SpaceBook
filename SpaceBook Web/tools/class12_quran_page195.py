"""Mutalia-e-Quran XII PDF195: p.192 — Lesson 20 exercise Q1 items 5–7, Q2, Q3 (1–3a). Run: python class12_quran_page195.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p195():
    b = Builder()
    MCQ(b, 5, words(59, 9, 26, 32), ('— in this there are glad tidings of success for those people who were saved:', 'میں فلاح کی خوش خبری ہے ان لوگوں کے لیے جو بچا لیے گئے:', '— په دې کې د هغو خلکو لپاره د بریا زېری دی چې وژغورل شول:'),
        [('from the deception of the self', 'نفس کے دھوکے سے', 'د نفس له دوکې'), ('from the scheming of the self', 'نفس کے مکر سے', 'د نفس له چل'), ('from the desire of the self for fame', 'نفس کی شہرت سے', 'د نفس له شهرته'), ('from the miserliness of the self', 'نفس کے بخل سے', 'د نفس له بخل')])
    MCQ(b, 6, words(59, 21, 14, 19), ('— according to this, Allah Almighty states parables for people so that they:', 'کی رو سے اللہ تعالیٰ لوگوں کے لیے مثالیں اس لیے بیان فرماتا ہے تاکہ وہ:', '— له دې سره سم الله تعالی خلکو ته مثالونه ځکه بیانوي تر څو هغوی:'),
        [('use their reason', 'عقل سے کام لیں', 'له عقل کار واخلي'), ('obtain guidance', 'ہدایت حاصل کریں', 'هدایت ترلاسه کړي'), ('take advice', 'نصیحت حاصل کریں', 'نصیحت واخلي'), ('reflect and ponder', 'غور و فکر کریں', 'غور او فکر وکړي')])
    MCQ(b, 7, 'ٱلْقُدُّوسُ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('the Dominant Being', 'غالب ذات', 'غالب ذات'), ('the Merciful Being', 'مہربان ذات', 'مهربان ذات'), ('the Pure (Holy) Being', 'پاک ذات', 'پاک ذات'), ('the Being of peace', 'سلامتی والی ذات', 'د سلامتۍ ذات')])
    b.p(*Q2)
    AR(b, f'(1) {words(59, 3)}', 'According to the verse, what would have been the end of the Jews if there had been no exile?', 'آیت کریمہ کے مطابق جلاوطنی نہ ہونے کی صورت میں یہود کا کیا انجام ہوتا؟', 'د آیت له مخې که جلاوطني نه وای، د یهودو پایله به څه وه؟')
    AR(b, f'(2) {words(59, 4)}', 'What reason for the punishment of the Jews has been stated in the verse?', 'آیت کریمہ میں یہود کی سزا کی کیا وجہ بیان کی گئی ہے؟', 'په آیت کې د یهودو د سزا کوم لامل بیان شوی؟')
    AR(b, f'(3) {words(59, 12)}', 'Of what conduct of the hypocrites has news been given in the verse?', 'آیت کریمہ میں منافقین کے کس طرزِ عمل کی خبر دی گئی ہے؟', 'په آیت کې د منافقانو د کوم چلند خبر ورکړل شوی؟')
    AR(b, f'(4) {words(59, 13)}', 'What state of the fear of the Jews has been stated in the verse?', 'آیت کریمہ میں یہود کے ڈر کی کیا کیفیت بیان کی گئی ہے؟', 'په آیت کې د یهودو د وېرې کوم حالت بیان شوی؟')
    AR(b, f'(5) {words(59, 14, 1, 11)}', 'According to the verse, what manner of the Jews fighting the Muslims has been stated?', 'آیت کریمہ کی رو سے یہود کی مسلمانوں کے ساتھ قتال کی کیا کیفیت بیان کی گئی ہے؟', 'د آیت له مخې له مسلمانانو سره د یهودو د جګړې کوم حالت بیان شوی؟')
    AR(b, f'(6) {words(59, 18)}', 'What advice has been given to the people of faith in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا نصیحت کی گئی ہے؟', 'په آیت کې مؤمنانو ته څه نصیحت شوی؟')
    AR(b, f'(7) {words(59, 20)}', 'In the verse, which two groups have been compared, and which group is the one that will be successful?', 'آیت کریمہ میں کن دو گروہوں کا تقابل بیان ہوا ہے اور کون سا گروہ کامیاب ہونے والا ہے؟', 'په آیت کې د کومو دوو ډلو پرتله شوې او کومه ډله بریالۍ کېدونکې ده؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(59, 5)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Hashr.', 'سُوْرَةُ الْحَشْرِ کا تعارف تحریر کریں۔', 'د سورة الحشر پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(59, 6)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Hashr.', 'سُوْرَةُ الْحَشْرِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الحشر ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(59, 11)}', *TR)
    BOOK.save(195, [(20, rec(b, 20, 195, 195, kind='exercise'))], issues=[{'id': 'mq12-pdf195', 'unit': 20, 'printedPage': 192,
               'description': 'Q3 3b is printed on p.193 and recorded there. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p195()
