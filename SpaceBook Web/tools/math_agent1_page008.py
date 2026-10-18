from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
blocks=[p('1.1.3 Order (or dimension) of a Matrix'),
 p('A matrix with m rows and n columns has order m × n (read “m by n”).'),
 p('If a matrix has order m × n then m represents the number of rows and n represents the number of columns.'),
 p('For example, consider'),
 dict(type='matrixProduct',prefix='A =',matrices=[[[-3,2,1],[2,1,3]]]),
 dict(type='matrixProduct',prefix='and B =',matrices=[[[2,1],[-4,3]]]),
 p('The order of the matrix A is 2-by-3 or A is a 2-by-3 matrix. Similarly the order of the matrix B is 2-by-2 or B is a 2-by-2 matrix.'),
 p('Do You Know?'),
 dict(type='matrixProduct',prefix='Matrix',matrices=[[[6,10],[5,3],[5,2]]]),
 p('Row 1: 6, 10. Row 2: 5, 3. Row 3: 5, 2. Column 1: 6, 5, 5. Column 2: 10, 3, 2. An element of the matrix: 3 (row 2, column 2).'),
 p('Dimension of this matrix is 3 × 2.'),
 p('Remember: Sometimes we will prefer to write the order of a matrix as m-by-n or sometimes (m × n).'),
 p('Note: Order of a matrix m × n does not mean to multiply m & n.'),
 p('Tid-Bit: Order of a matrix is also called dimension or size.')]
save(dict(pdfPage=8,printedPage=4,page=4,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='1.1.3 Order (or dimension) of a Matrix',sections=[dict(id='1.1',title='1.1 Introduction to Matrices',blocks=blocks)],
 visualStatus='Order diagram and matrix labels represented by their exact row/column relationships; all callouts retained'))
render(9)
