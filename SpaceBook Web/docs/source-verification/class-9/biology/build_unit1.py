# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 1 from verified source pages PDF 7-28 (printed 1-22)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit1_a, unit1_b, unit1_c, unit1_d, unit1_ex

secs = unit1_a.sections()
unit1_b.extend_1_3(secs[-1])
secs += unit1_b.sections() + unit1_c.sections() + unit1_d.sections() + [unit1_ex.keypoints_section()]
data = T.load_bio()
old = next(u for u in data if u['number'] == 1)
fields = dict(
    title='Introduction to Biology', titleUrdu='حیاتیات کا تعارف', titlePashto='بیولوژي ته پېژندنه',
    pageRange='Pages 1–22', badge='Source-verified (PDF 7–28)', status='completed',
    sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(7, 29)), sourcePrintedPages=list(range(1, 23)),
    keyPoints=[k[0] for k in unit1_ex.KEY_POINTS],
    exercise=unit1_ex.exercise(old['exercise']),
    practicals=[],
    sourceReview=dict(complete=True, lastPdfPage=28, note='Unit 1 rebuilt verbatim from source; earlier paraphrased text, invented MCQs, invented activities and the non-source microscope practical were replaced.'),
)
T.upsert_unit(1, secs, fields)
d2 = T.load_bio(); u = next(x for x in d2 if x['number'] == 1); u.pop('introQuran', None); T.save_bio(d2)  # verses live verbatim in 1.6
print('sections', [s.id for s in secs])
print('ok' if T.check_js() else 'CHECK FAILED')
