from math_agent1_sequential import save, render
objectives = [
 'Define a matrix with real entries and relate its rectangular layout (formation) with real life.',
 'Define rows and columns of a matrix.', 'Define the order of a matrix.', 'Define equality of two matrices.',
 'Define and identify row matrix, column matrix, rectangular matrix, square matrix, zero/null matrix, identity matrix, scalar matrix, diagonal matrix, transpose of a matrix, symmetric and skew-symmetric matrices.',
 'Know whether the given matrices are conformable for addition/subtraction.', 'Add and subtract matrices.',
 'Multiply a matrix by a real number.', 'Verify commutative and associative laws under addition.',
 'Define additive identity of a matrix.', 'Find additive inverse of a matrix.',
 'Know whether the given matrices are conformable for multiplication.', 'Multiply two (or three) matrices.',
 'Verify associative law under multiplication.', 'Verify distributive laws.',
 'Show with the help of an example that commutative law under multiplication does not hold in general (i.e. AB ≠ BA).',
 'Define multiplicative identity of a matrix.', 'Verify the result (AB)ᵗ = BᵗAᵗ.',
 'Define the determinant of a square matrix.', 'Evaluate determinant of a matrix.',
 'Define singular and non-singular matrices.', 'Define adjoint of a matrix.',
 'Find multiplicative inverse of a non-singular matrix A and verify that AA⁻¹ = I = A⁻¹A where I is the identity matrix.',
 'Use adjoint method to calculate inverse of a non-singular matrix.', 'Verify the result (AB)⁻¹ = B⁻¹A⁻¹.',
 'Solve a system of two linear equations and related real life problems in two unknowns using\n• Matrix inversion method,\n• Cramer’s rule.'
]
save(dict(pdfPage=5, printedPage=1, page=1, chapter='Unit 1: Matrices', status='completed-educational-content',
 title='UNIT 01 MATRICES', objectives=objectives, sections=[dict(id='source-u1-objectives', title='Unit 1: Matrices — Learning Objectives',
 blocks=[dict(type='paragraph',text='After reading this unit, the students will be able to:')]+[dict(type='paragraph',text='• '+text) for text in objectives])],
 visualStatus='Learning objectives; decorative arrows and border do not carry additional lesson content'))
render(6)
