from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
def gtable(title_en,title_ur,title_ps,rows,note):
    n=len(rows)
    return table(f'Glossary: {title_en} ({n} words with meanings)',f'فرہنگ: {title_ur} ({n} الفاظ مع معانی)',f'فرهنګ: {title_ps} ({n} ټکي له معنا سره)',[c('Word','الفاظ','ټکي'),c('Meaning','معنی','معنا')],[[c(a,a,a),c(m,u,p)] for a,u,m,p in rows],sourceGap=dict(note='Printed as a four-column table (words, meanings, words, meanings). Listed as one word-meaning pair per row: right-hand pair first, then the left-hand pair. '+note))
