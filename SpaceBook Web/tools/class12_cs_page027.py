"""Computer Science XII PDF27 (spread): printed pp.42–43 — design list (end); three architectures; i. algorithms (example as code); ii. flowcharts; Fig 2.2 symbols; Fig 2.3 flowchart (coded)."""
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_2_2, fig_2_3

t = Builder()
P = t.p
H = t.h
t.group('list', [('Defining major subsystems and their inputs and outputs.', 'بڑے ذیلی نظاموں اور ان کے ان پٹ اور آؤٹ پٹ کا تعین۔', 'د لویو فرعي سیسټمونو او د هغوی د ننوتو او وتو ټاکل.'),
                 ('Allocating processes to resources.', 'پراسیسز کو وسائل تفویض کرنا۔', 'سرچینو ته د پروسو سپارل.')])
P('The design phase normally consists of three different architectures. These are:', 'ڈیزائن کا مرحلہ عام طور پر تین مختلف ساختوں پر مشتمل ہوتا ہے۔ یہ ہیں:', 'د ډیزاین پړاو عموماً درې بېلابېل جوړښتونه لري. دا دي:')
t.group('list', [('Algorithms', 'الگورتھمز', 'الګوریتمونه'), ('Flow chart', 'فلو چارٹ', 'فلوچارټ'), ('Pseudo code', 'سوڈو کوڈ', 'شبه کوډ')])
H('i. Algorithms', 'i. الگورتھمز', 'i. الګوریتمونه')
P('An algorithm is a specific set of instructions for carrying out a procedure or solving a problem.', 'الگورتھم کسی طریقۂ کار کو انجام دینے یا کسی مسئلے کو حل کرنے کے لیے ہدایات کا ایک مخصوص مجموعہ ہے۔', 'الګوریتم د یوې کړنلارې د ترسره کولو یا د یوې ستونزې د حل لپاره د لارښوونو یوه ټاکلې ټولګه ده.')
P('For Example the following algorithm will find average of the 5 numbers.', 'مثال کے طور پر درج ذیل الگورتھم 5 اعداد کی اوسط معلوم کرے گا۔', 'د بېلګې په توګه لاندې الګوریتم د ۵ عددونو اوسط پیدا کوي.')
code(t, '''Sum = 0, Average = 0
Read a, b, c, d, e
Sum = a+b+c+d+e
Average = Sum/5
Print Average''')
H('ii. Flowcharts', 'ii. فلو چارٹس', 'ii. فلوچارټونه')
P('A flowchart is a type of diagram that represents an algorithm or a process. It shows the steps of the algorithms with the help of boxes and their order by arrows connecting the boxes. This diagrammatic representation of the algorithm gives a step-by-step solution to a given problem. The operations are represented in these boxes, and the flow of control on the arrows. These flowcharts are used for analyzing, designing, documenting or managing a process or program in various fields.',
  'فلو چارٹ ایک قسم کی تصویر ہے جو کسی الگورتھم یا عمل کی نمائندگی کرتی ہے۔ یہ خانوں کی مدد سے الگورتھم کے مراحل اور خانوں کو جوڑنے والے تیروں سے ان کی ترتیب دکھاتا ہے۔ الگورتھم کی یہ تصویری نمائندگی کسی مسئلے کا مرحلہ وار حل پیش کرتی ہے۔ عمل ان خانوں میں اور کنٹرول کا بہاؤ تیروں پر دکھایا جاتا ہے۔ یہ فلو چارٹس مختلف شعبوں میں کسی عمل یا پروگرام کے تجزیے، ڈیزائن، دستاویز بندی یا انتظام کے لیے استعمال ہوتے ہیں۔',
  'فلوچارټ یو ډول انځور دی چې یو الګوریتم یا بهیر ښيي. د بکسونو په مرسته د الګوریتم ګامونه او د بکسونو د نښلوونکو غشو په مرسته یې ترتیب ښيي. د الګوریتم دا انځوري ښودنه د یوې ستونزې ګام په ګام حل وړاندې کوي. عملیې په دې بکسونو کې او د کنټرول بهیر پر غشو ښودل کېږي. دا فلوچارټونه په بېلابېلو برخو کې د یوې پروسې یا پروګرام د تحلیل، ډیزاین، اسنادو یا ادارې لپاره کارول کېږي.')
P('Some most commonly used flowchart symbols are shown in Figure 2.3.', 'کچھ سب سے زیادہ استعمال ہونے والی فلو چارٹ کی علامات شکل 2.3 میں دکھائی گئی ہیں۔', 'د فلوچارټ ځینې تر ټولو ډېرې کارېدونکې نښې په ۲.۳ شکل کې ښودل شوې.')
en, ur, ps, ratio = fig_2_2()
t.visual('cs12-fig-2-2', en, ur, ps, ratio)
P('Example: Flowchart for the above algorithm will be as follows.', 'مثال: اوپر والے الگورتھم کا فلو چارٹ یوں ہوگا۔', 'بېلګه: د پورته الګوریتم فلوچارټ به داسې وي.')
en, ur, ps, ratio = fig_2_3()
t.visual('cs12-fig-2-3', en, ur, ps, ratio)
rec = BOOK.record(t, 'cs12-u2-text-6', 'Unit 2 text (6)', 'یونٹ 2 — متن (۶)', '۲ څپرکی — متن (۶)', 27, [42, 43])
rec['sourceNote'] = 'The first list continues the design-phase list from p.41. Figures 2.2 and 2.3 are reproduced as coded diagrams; the flowchart labels stay in English (program text) in all language views.'
issues = [{'id': 'cs12-pdf027', 'unit': 2, 'printedPage': 43,
           'description': 'The text on p.43 says the symbols “are shown in Figure 2.3” but the symbol table is captioned “Figure 2.2” (Figure 2.3 is the example flowchart). Retained as printed. Owner bracket marks around the algorithm and flowchart excluded.'}]

if __name__ == '__main__':
    BOOK.save(27, [(2, rec)], issues=issues)
