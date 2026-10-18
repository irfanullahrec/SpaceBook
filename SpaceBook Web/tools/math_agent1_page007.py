from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
def matrix(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
blocks=[
 p('1.1.1 Matrix'),
 p('A matrix is a rectangular array (arrangements) of real numbers enclosed in square brackets. Each number in a matrix is called an element or entry of the matrix. For example'),
 dict(type='matrixProduct',matrices=[[[2,3],[6,5]],[[-1,1,2],[3,4,5]],[[3,4,2],[-1,1,-2],[-4,-3,-3]]],operators=[',','and'],suffix='are all matrices.'),
 matrix([[2,3],[6,5]],'In the matrix','the number 2, 3, 6, 5 are the elements or entries of the matrix.'),
 matrix([[3,4,2],[-1,1,-2],[-4,-3,-3]],'Similarly in the matrix'),
 p('the numbers 3, 4, 2, −1, 1, −2, −4, −3, −5 are the elements or entries of the given matrix. Matrices are frequently denoted by capital letters such as A, B, C and so on. Thus we can write'),
 matrix([[2,3],[6,5]],'A ='),matrix([[-1,1,2],[3,4,5]],'B ='),matrix([[3,4,2],[-1,1,-2],[-4,-3,-3]],'C ='),
 p('1.1.2 Rows and Columns of Matrix'),
 p('The rows of a matrix run horizontally, and the columns of a matrix run vertically. To make the idea more clear, let us consider the following matrix.'),
 matrix([[4,3,-2],[1,5,2],[3,1,1]],'A ='),
 p('The numbers 4, 3, −2 are arranged horizontally, so they continue the first row.'),
 p('The numbers 1, 5, 2 are arranged horizontally, so they continue second row.'),
 p('The numbers 3, 1, 1 are arranged horizontally so they continue third row.'),
 matrix([[4,3,-2],[1,5,2],[3,1,1]],'Again consider the same matrix, A ='),
 p('The numbers 4, 1, 3 run vertically, so they constitute the first column.'),
 p('The numbers 3, 5, 1 run vertically, so they constitute the second column.'),
 p('The numbers −2, 2, 1 run vertically, so they constitute the third column.')
]
save(dict(pdfPage=7,printedPage=3,page=3,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='1.1.1 Matrix / 1.1.2 Rows and Columns of Matrix',sections=[dict(id='1.1',title='1.1 Introduction to Matrices',blocks=blocks)],
 sourceErrata=[dict(kind='printed inconsistency',text='The entries sentence ends in −5, while the displayed matrix ends in −3. Both preserved as printed.'),
 dict(kind='printed wording',text='Row annotations use “continue”; preserved as printed.')],
 visualStatus='All matrices rebuilt as structured arrays; each row/column arrow annotation transcribed separately'))
render(8)
