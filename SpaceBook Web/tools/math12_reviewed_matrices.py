"""Printed pages 19–24, manually compared with JPGs and full PDF spreads."""
from math12_reviewed_unit1 import heading, paragraph, command, page

LINALG = '[BlockDiagonal, GramSchmidt, JordanBlock, LUdecomp, QRdecomp, Wronskian, addcol, addrow, adj, adjoint, angle, augment, backsub, band, basis, bezout, blockmatrix, charmat, charpoly, cholesky, col, coldim, colspace, colspan, companion, concat, cond, copyinto, crossprod, curl, definite, delcols, delrows, det, diag, diverge, dotprod, eigenvals, eigenvalues, eigenvectors, eigenvects, entermatrix, equal, exponential, extend, ffgausselim, fibonacci, forwardsub, frobenius, gausselim, gaussjord, geneqns, genmatrix, grad, hadamard, hermite, hessian, hilbert, htranspose, ihermite, indexfunc, innerprod, intbasis, inverse, ismith, issimilar, iszero, jacobian, jordan, kernel, laplacian, leastsqrs, linsolve, matadd, matrix, minor, minpoly, mulcol, mulrow, multiply, norm, normalize, nullspace, orthog, permanent, pivot, potential, randmatrix, randvector, rank, ratform, row, rowdim, rowspace, rowspan, rref, scalarmul, singularvals, smith, stackmatrix, submatrix, subvector, subbasis, swapcol, swaprow, sylvester, toeplitz, trace, transpose, vandermonde, vecpotent, vectdim, vector, wronskian]'

def matrix(text, label, rows, number=None):
    return {'type':'matrix', 'text':text, 'label':label, 'rows':rows, 'number':number}

PAGES = [
    page('014_page_1.jpg', 19, [
        heading('1.4 Matrices'),
        paragraph('The command will show you full information about matrices on line by typing: [ > ?matrices'),
        heading('1.4.1 Recognition of matrix and vector entry arrangement'), heading('(a) Command'),
        command('with(linalg);', LINALG, 1),
        matrix('X := matrix(3, 3, [1, 4, 2, 2, 3, 4, 5, 4, 6]);', 'X :=', [[1,4,2],[2,3,4],[5,4,6]], 2),
        matrix('Y := matrix(3, 3, [5, 3, 4, 1, 2, 0, 9, 3, 7]);', 'Y :=', [[5,3,4],[1,2,0],[9,3,7]], 3),
        matrix('Z := matrix(3, 3, [1, 0, 1, 2, 3, 1, 0, 5, 1]);', 'Z :=', [[1,0,1],[2,3,1],[0,5,1]], 4),
        matrix('c := ⟨1, 2, 3⟩;', 'c :=', [[1],[2],[3]], 5),
        matrix('r := ⟨1 | 2 | 3⟩;', 'r :=', [[1,2,3]], 6)
    ]),
    page('014_page_2.jpg', 20, [
        heading('(b) Using Palettes'),
        paragraph('Use cursor button to select matrix palette. Click- “matrix” <click-choose(for the umber of rows and columns of a required matrix) <click-data type (to select integers entries of the rows and columns of a required matrix), then finally click-“insert matrix” and press ENTER key to obtain a required matrix.'),
        matrix(None, '', [[1,4,2],[2,3,4],[5,4,6]]),
        matrix(None, '', [[1,4,2],[2,3,4],[5,4,6]], 7),
        heading('1.4.2 Applying matrix operations'), heading('(a) Matrix addition'),
        command('with(linalg);', LINALG, 1),
        matrix('X := Matrix([[1, 2, 3], [1, 3, 0], [1, 4, 3]]);', 'X :=', [[1,2,3],[1,3,0],[1,4,3]], 2),
        matrix('Y := Matrix([[1, 2, 5], [6, 3, 0], [1, 4, 3]]);', 'Y :=', [[1,2,5],[6,3,0],[1,4,3]], 3),
        matrix('matadd(X, Y);', '', [[2,4,8],[7,6,0],[2,8,6]], 4)
    ]),
    page('015_page_1.jpg', 21, [
        heading('(b) Matrix multiplication'), command('with(linalg);', LINALG, 1),
        matrix('X := Matrix([[1, 2, 3], [1, 3, 0], [1, 4, 3]]);', 'X :=', [[1,2,3],[1,3,0],[1,4,3]], 2),
        matrix('Y := Matrix([[1, 2, 5], [6, 3, 0], [1, 4, 3]]);', 'Y :=', [[1,2,5],[6,3,0],[1,4,3]], 3),
        matrix('multiply(X, Y);', '', [[16,20,14],[19,11,5],[28,26,14]], 4),
        heading('(c) Using Palettes'),
        paragraph('To obtain the result simply right click on the last “matrix” then click simplify or press ENTER.'),
        {'type':'matrixExpression', 'operands':[[[1,2,3],[1,3,0],[1,4,3]], [[1,2,5],[6,3,0],[1,4,3]]], 'operator':'+', 'rows':[[2,4,8],[7,6,0],[2,8,6]], 'number':1},
        matrix('simplify(Matrix(%id = 18446744074594159542)+Matrix(%id = 18446744074594159662));', '', [[2,4,8],[7,6,0],[2,8,6]], 2)
    ]),
    page('015_page_2.jpg', 22, [
        heading('1.4.3 Inverse and transpose of a matrix'), heading('(a) Inverse of a matrix'),
        command('with(linalg);', LINALG, 1),
        matrix('X := Matrix([[1, 2, 3], [1, 3, 0], [1, 4, 3]]);', 'X :=', [[1,2,3],[1,3,0],[1,4,3]], 2),
        matrix('Y := Matrix([[1, 2, 5], [6, 3, 0], [1, 4, 3]]);', 'Y :=', [[1,2,5],[6,3,0],[1,4,3]], 3),
        matrix('inv := inverse(X);', 'inv :=', [[r'\(\frac{3}{2}\)',1,r'\(-\frac{3}{2}\)'],[r'\(-\frac{1}{2}\)',0,r'\(\frac{1}{2}\)'],[r'\(\frac{1}{6}\)',r'\(-\frac{1}{3}\)',r'\(\frac{1}{6}\)']], 4),
        matrix('inv := inverse(Y);', 'inv :=', [[r'\(\frac{3}{26}\)',r'\(\frac{7}{39}\)',r'\(-\frac{5}{26}\)'],[r'\(-\frac{3}{13}\)',r'\(-\frac{1}{39}\)',r'\(\frac{5}{13}\)'],[r'\(\frac{7}{26}\)',r'\(-\frac{1}{39}\)',r'\(-\frac{3}{26}\)']], 5)
    ]),
    page('016_page_1.jpg', 23, [
        heading('(b) Transport of a matrix'), command('with(linalg);', LINALG, 1),
        matrix('X := Matrix([[1, 2, 3], [1, 3, 0], [1, 4, 3]]);', 'X :=', [[1,2,3],[1,3,0],[1,4,3]], 2),
        matrix('Y := Matrix([[1, 2, 5], [6, 3, 0], [1, 4, 3]]);', 'Y :=', [[1,2,5],[6,3,0],[1,4,3]], 3),
        matrix('trans := transpose(X);', 'trans :=', [[1,1,1],[2,3,4],[3,0,3]], 4),
        matrix('trans := transpose(Y);', 'trans :=', [[1,6,1],[2,3,4],[5,0,3]], 5)
    ]),
    page('016_page_2.jpg', 24, [
        heading('(c) Using Palettes'), heading('Inverse of a matrix'),
        paragraph('To obtain the result through context menu. Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “inverse” to obtained the inverse of a matrix.'),
        matrix(None, '', [[1,2],[3,4]]),
        matrix('LinearAlgebra:-MatrixInverse(Matrix(%id = 18446744074459087686));', '', [[-2,1],[r'\(\frac{3}{2}\)',r'\(-\frac{1}{2}\)']], 1),
        paragraph('Similarly,'), heading('Transpose of a matrix'),
        paragraph('To obtain the result through context menu. Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “transpose” to obtained the inverse of a matrix.'),
        matrix(None, '', [[1,2,3],[4,2,6],[3,5,1]]),
        matrix('LinearAlgebra:-Transpose(Matrix(%id = 18446744073883260558));', '', [[1,4,3],[2,2,5],[3,6,1]], 2),
        heading('Determinant of a matrix'),
        paragraph('To obtain the result through context menu. Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “determinant” to obtained the inverse of a matrix.'),
        matrix(None, '', [[3,2,5],[1,5,7],[2,9,4]]),
        command('LinearAlgebra:-Determinant(Matrix(%id = 18446744073883262118));', '-114', 3),
        {'type':'clarification', 'text':'The heading on page 23 prints “Transport”; the command computes a transpose. On this page the transpose and determinant instructions repeat “inverse”. The transpose returns the matrix with rows and columns exchanged; the determinant returns a scalar. The original wording above is preserved.'}
    ])
]
for source in PAGES:
    source['visualStatus'] = 'Matrix and vector entries rendered as digital tables; commands and results transcribed digitally'
    if source['page'] >= 21:
        source['alternateVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf', 'pdfPage':15 if source['page'] <= 22 else 16, 'side':'left' if source['page'] % 2 else 'right', 'reason':'Sharper full-PDF spread used to confirm fractions, commands and internal matrix identifiers.'}
PAGES[-2]['sourceNotes'] = ['Printed heading says Transport; preserved rather than silently changed to Transpose.']
PAGES[-1]['sourceNotes'] = ['Transpose and determinant instructions repeat inverse; original wording retained with separately labelled clarification.']
