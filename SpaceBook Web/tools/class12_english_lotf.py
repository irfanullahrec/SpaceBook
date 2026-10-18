"""Shared helper for 'Lord of the Flies' summary pages (Unit 19)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
NOTE = 'Modern copyrighted novel (William Golding, 1954), printed as a textbook abridgement; paragraph-wise summary in the app, not verbatim. Printed pp. {}.'


def page(pdf, printed, parts, issues=None, photo=None):
    """parts: list of (rid, heading_or_None, [(en,ur,ps)...], title triple)."""
    recs = []
    for rid, head, paras, title in parts:
        b = Builder()
        if head: b.h(*head)
        for x in paras: b.p(*x)
        r = BOOK.record(b, rid, title[0], title[1], title[2], pdf, printed)
        r['sourceGap'] = NOTE.format('–'.join(map(str, printed)) if len(printed) > 1 else printed[0])
        if photo: r['sourceCoverIllustrationReview'] = photo
        recs.append((19, r))
    BOOK.save(pdf, recs, issues=issues)


def CH(n):
    words = {1: ('1', 'لومړی'), 2: ('2', 'دویم'), 3: ('3', 'درېیم'), 4: ('4', 'څلورم'), 5: ('5', 'پنځم'), 6: ('6', 'شپږم'), 7: ('7', 'اووم'), 8: ('8', 'اتم'), 9: ('9', 'نهم'), 10: ('10', 'لسم'), 11: ('11', 'یوولسم'), 12: ('12', 'دولسم')}
    return (f'CHAPTER {n}', f'باب {words[n][0]}', f'{words[n][1]} څپرکی')


def T(label_en, label_ur, label_ps):
    return (f'Lord of the Flies — {label_en}', f'لارڈ آف دی فلائیز — {label_ur}', f'لارډ آف دي فلایز — {label_ps}')
