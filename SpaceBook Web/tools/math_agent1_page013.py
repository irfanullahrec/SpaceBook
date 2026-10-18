from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
def m(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
blocks=[p('f) Diagonal matrix'),p('A square matrix in which all elements are zero except the diagonal elements is known as diagonal matrix. For example'),
 m([[1,0],[0,3]],'A =','is a diagonal matrix of order 2.'),m([[2,0,0],[0,3,0],[0,0,-5]],'B =','is a diagonal matrix of order 3.'),
 p('Remember: Main diagonal'),p('Start at the top left and goes to the bottom right in the matrix.'),m([[1,0],[0,3]],'A ='),
 p('g) Scalar matrix'),p('A square matrix in which all the elements lying on the main diagonal of the matrix are equal and the remaining elements off the main diagonal are all zero is called scalar matrix.'),
 p('Equivalently scalar matrix can also be defined as under:'),p('A diagonal matrix in which all the diagonal elements are equal is said to be a scalar matrix.'),p('For instance'),
 dict(type='matrixProduct',matrices=[[[1,0],[0,1]],[[7,0,0],[0,7,0],[0,0,7]],[['1/2',0,0],[0,'1/2',0],[0,0,'1/2']]],operators=[',',','],suffix='are scalar matrices of order 2 and 3 respectively.'),
 p('Tid-Bit: Scalar matrix is a special case of a diagonal matrix.')]
save(dict(pdfPage=13,printedPage=9,page=9,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='Diagonal matrix / Scalar matrix',sections=[dict(id='1.2',title='1.2 Types of Matrices',blocks=blocks)],
 visualStatus='All matrices and main-diagonal explanation structured; decorative rings omitted'))
render(14)
