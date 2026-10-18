"""Pak Studies XII PDF3 (spread): right = framed hadith; left = title page."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
b = Builder()
b.p('Allah the Exalted does not accept charity from unlawful (ḥarām) wealth. (Aḥmad)', 'حرام مال سے اللہ تعالیٰ صدقہ قبول نہیں کرتا۔ (احمد)', 'الله تعالیٰ له حرام مال نه صدقه نه مني. (احمد)')
b.h('Pakistan Studies — for Class Twelve', 'مطالعۂ پاکستان — بارہویں جماعت کیلئے', 'د پاکستان مطالعه — د دولسم ټولګي لپاره')
b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
rec = BOOK.record(b, 'pak12-fm-title', 'Hadith and title page', 'حدیث اور سرِ ورق', 'حدیث او سرلیک مخ', 3, [None, None])
rec['sourceCoverIllustrationReview'] = 'Floral frame around the hadith and the Board logo are decorative; not reproduced.'

if __name__ == '__main__':
    BOOK.save(3, [('FM', rec)])
