# -*- coding: utf-8 -*-
"""Apply rebuilt poem text for lessons 12-15 (source PDF 102-114) to urdu_data.js."""
import os, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T, poems

NAZIR = ('نظیر اکبر آبادی\nولادت ۱۷۳۵ء ، وفات ۱۸۳۰ء\n\n'
         'نظیر اکبر آبادی کا اصل نام ولی محمد تھا۔ وہ دلی میں پیدا ہوئے۔ ان کے والد کا نام سید محمد فاروق تھا۔ نظیر پیشے کے لحاظ سے معلم تھے۔ انھیں عوامی شاعر کہا جاتا ہے۔ '
         'موجودہ دور کے نقاد انھیں پہلا ترقی پسند شاعر تسلیم کرتے ہیں۔ انھوں نے دنیا کو جس حقیقت پسندانہ نظر سے دیکھا ہے، اس کی مثال اردو شاعری میں نہیں ملتی۔ '
         'ان کے مشاہدے میں گہرائی اور تجربے میں وسعت تھی۔ اُن کی شاعری اس دور کی سیاسی افراتفری، معاشی بد حالی، اخلاقی اقدار کی بے قدری اور لوگوں کی ذہنی پریشانیوں کی آئینہ دار ہے۔ '
         'وہ مقامی زندگی کی عکاسی کرنے میں بے مثال ہیں۔ ان کا کلام اردو شاعری میں ایک منفرد حیثیت رکھتا ہے۔\n\n'
         'انھوں نے جو کچھ اپنے ماحول میں دیکھا اس کی بے لاگ عکاسی کی ہے۔ وہ نظم کے شاعر ہیں، مگر غزلیں بھی لکھی ہیں۔ منظر نگاری ان کے کلام کی نمایاں خوبی ہے۔ '
         'نظیر کا کلام پڑھنے سے اُن کے زمانے کی سچی تصویر نگاہوں کے سامنے آجاتی ہے۔ مذہبی تہوار ہوں یا میلے، بندر والے کا تماشا ہو یا ریچھ والے کا، سماجی محفلیں ہوں یا شادی بیاہ کی مجلسیں، '
         'پتنگ بازی، کبوتر بازی، جوانی، بڑھاپا، لڑکپن غرض ہر موضوع پر خوب لکھا ہے۔ نظیر سے پہلے اردو شاعری مجازی محبوب کے حسن و جمال ہی کا طواف کرتی تھی، مگر نظیر نے اس روایت کو '
         'توڑ کر عوامی زندگی کو اپنی شاعری کا موضوع بنایا۔ ان کا ذخیرہ الفاظ بہت وسیع اور ان کی زبان عوامی ہے۔ آخری عمر میں ان پر فالج کا حملہ ہوا جس سے اگست ۱۸۳۰ء کو فوت ہوئے۔ '
         '"کلیاتِ نظیر" ان کے کلام کی یادگار ہے۔')
IQBAL = ('علامہ محمد اقبال\nولادت ۱۸۷۷ء ، وفات ۱۹۳۸ء\n\n'
         'علامہ محمد اقبال کو شاعرِ مشرق، قومی شاعر، ترجمانِ حقیقت، حکیم الامت جیسے شاندار القابات سے یاد کیا جاتا ہے۔ وہ سیالکوٹ میں پیدا ہوئے۔ ان کے والد کا نام شیخ نور محمد تھا۔ '
         'اقبال نے ایف اے تک تعلیم سیالکوٹ میں حاصل کی۔ پنجاب یونیورسٹی سے فلسفے میں ایم اے کیا۔ یورپ سے پی ایچ ڈی اور بیرسٹری کی تعلیم حاصل کی۔ کچھ عرصہ لاہور میں پروفیسر رہے، '
         'پھر وکالت کا پیشہ اختیار کر لیا۔ پاکستان کا تصور اقبال نے پیش کیا۔ حکومتِ برطانیہ کی طرف سے ان کو علمی اور ادبی خدمات کے صلے میں ”سر“ کا خطاب دیا گیا۔\n\n'
         'اقبال نے اپنے کلام میں حرکت اور عمل کا وہ نمونہ پیش کیا ہے کہ آنے والے شاعروں کے رجحانات کا رخ مڑ گیا اور اردو شاعری کا مزاج بدل گیا۔ محرومی اور یاس انگیزی کی وہ روش جو قدیم زمانے سے چلی آرہی تھی، امید میں بدل گئی۔ '
         'اقبال نے آزادی اور مردِ مومن کا تصور اس طرح پیش کیا کہ اقبال کا قاری اپنے زمانے کے کسی فرعون کے سامنے جھکنا اپنی عزتِ نفس کے خلاف سمجھتا ہے۔ '
         'عشقِ رسول صلی اللہ علیہ وعلی آلہ واصحابہ وسلم اقبال کی سوچ کا محور ہے۔ ان کے فکر و نظر کے زاویے رسولِ پاک صلی اللہ علیہ وعلی آلہ واصحابہ وسلم کی محبت سے تپش، سوز اور نکھار حاصل کرتے ہیں۔ '
         'ان کے کلام کی سب سے بڑی خصوصیت ان کا فلسفۂ خودی ہے۔ شاہین اقبال کا پسندیدہ پرندہ ہے۔ وہ بلند پرواز، خلوت پسند اور خوددار پرندہ ہے۔ یہی خوبیاں اقبال اپنے دور کے مسلمانوں میں بھی دیکھنا چاہتے تھے۔\n\n'
         'بانگِ درا، بالِ جبریل، ضربِ کلیم، ارمغانِ حجاز، اسرارِ خودی، رموزِ بے خودی، پس چہ باید کرد اے اقوامِ شرق، پیامِ مشرق، زبورِ عجم اور جاوید نامہ ان کی مایہ ناز تصانیف ہیں۔\n\n'
         'یہ عظیم شاعر ۲۱ اپریل ۱۹۳۸ء کو اس جہانِ فانی سے رخصت ہوئے۔ ان کا مزار بادشاہی مسجد لاہور کے پہلو میں ہے۔')
HALI_NOTE = 'الطاف حسین حالی (حالی کا تعارف درسی کتاب میں سبق ۲ "اسلام میں گداگری کی مذمت" کے ساتھ دیا گیا ہے۔)'

NOTES = {
    12: ['Stored Hamd held only 2 couplets with wording that differed from the book ("اور سوا", "نافرمان", "کیسے"); replaced with all 10 couplets as printed (PDF 102-103).'],
    13: ['Stored Naat displayed the Hamd\'s couplets; replaced with the 7 Naat couplets printed on PDF 105.', 'urduText named the poet as "حفیظ جالندھری"; corrected to امیر مینائی (PDF 104).'],
    14: ['Stored poem displayed the Hamd\'s couplets; replaced with the 6 bands of "برسات کی بہاریں" printed on PDF 108-109 (PDF 108 is printed sideways).',
         'Band 4 keeps the printed "قمری پکارے: لو لو" (other editions read "کو کو").', 'Generic author note replaced with the printed biography (PDF 107).'],
    15: ['Stored poem displayed the Hamd\'s couplets; replaced with the 16 couplets of "طلوعِ اسلام" printed on PDF 112-114 (PDF 113 printed sideways).',
         'The first line of couplet 15 is cut at the top of PDF 114; the visible letters match the Bang-e-Dra line, shown with a visible note.', 'Generic author note replaced with the printed biography (PDF 111).'],
}
POETS = {12: 'الطاف حسین حالی', 13: 'امیر مینائی', 14: 'نظیر اکبر آبادی', 15: 'علامہ محمد اقبال'}

if os.path.exists(T.LOCK):
    sys.exit('shared lock held')
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent urdu poems {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    for n in (12, 13, 14, 15):
        u = T.lesson(data, n)
        u['sections'] = poems.sections(n)
        u['urduSections'] = [s['urdu'] for s in u['sections']]
        u['urduText'] = poems.full_text(n, u['title'], POETS[n])
        if n == 12:
            u['authorInfo'] = HALI_NOTE
        if n == 14:
            u['authorInfo'] = NAZIR
        if n == 15:
            u['authorInfo'] = IQBAL
        u['sourceReview'] = dict(sourcePdf='D:/SpaceBook/Books/9th/9th urdu/PDF/9th Urdu.pdf', pdfPages=poems.LESSONS[n]['pdf'],
                                 printedPages=[T.printed_of(p) for p in poems.LESSONS[n]['pdf']], notes=NOTES[n],
                                 tashreeh='Couplet explanations and English/Pashto renderings are SpaceBook-authored.',
                                 reviewedAt=datetime.date.today().isoformat())
    T.save(data)
finally:
    os.remove(T.LOCK)
entries = []
for n in (12, 13, 14, 15):
    for p in poems.LESSONS[n]['pdf']:
        entries.append((p, 'corrected', f'Lesson {n}: compared with page image; ' + ' '.join(NOTES[n])[:350]))
print(T.record_pages(entries)['counts'])
