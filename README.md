# [matmath module](https://github.com/Siddhesh-Agarwal/matmath)

A simple and efficient module for matrix manipulation.

___________________________________________________________________________

## Installing under Python

When installing the **matmath module** for python, it is recommended that you check if you have **python 3.6 or above**.

___________________________________________________________________________

## General usage notes

* This module is meant for matrix manipulation and can carry out various operations. The **matmath mmodule** can carry various mathematical operations like addition, subtraction, multiplication and exponentiation along with Matrix-defined function like inverse, rotation, transpose, etc.
* It can also be used in finding determinant, inverse, transpose and adjoin of a matrix.
* The matrix/matrices should contain **only numbers** (i.e. `<class 'int'>`, `<class 'float'>` or `<class 'complex'>`) and not letters (i.e `<class 'str'>`) in order to avoid error.
* a few functions (example - `matAdd()`, `matSub()`, `matMul()`, `adj()`, `det()` and `inverse()`) may throw an error due to incompatibility of the matrices with the function.

___________________________________________________________________________

## Functions and their uses

| Functions       | Description                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| adj             | Returns the adjoint of the matrix multiplied by the multiplication factor. Default value of mul(multiplication factor) is 1.                                                                      |
| compatAS        | Returns True if matrices are compatible for addition/subtraction else returns False.                                                                                                              |
| compatM         | Returns True if matrices are compatible for multiplication else returns False.                                                                                                                    |
| cut             | Returns a smaller matrix by removing the required row and column. The default of row and column is 0.                                                                                             |
| det             | Returns the determinant of the matrix (if and only if the matrices are compatible for multiplication) multiplied by the multiplication factor. Default value of mul (multiplication factor) is 1. |
| Identity        | Returns an identity matrix of order N x N multiplied by the multiplication factor. Default value of mul (multiplication factor) is 1.                                                             |
| inv             | Returns the inverse of the matrix (if and only if the matrices are compatible) multiplied by the multiplication factor. Default value of mul (multiplication factor) is 1.                        |
| isDiagonal      | Returns True if matrix is a diagonal matrix else returns False.                                                                                                                                   |
| isIdentity      | Returns True if matrix is an identity matrix else returns False.                                                                                                                                  |
| isLTriangular   | Returns True if matrix is a lower triangular matrix else returns False.                                                                                                                           |
| isMatrix        | Returns True if matrix is a valid matrix else returns False.                                                                                                                                      |
| isNull          | Returns True if matrix is a null matrix else returns False.                                                                                                                                       |
| isSkewSymmetric | Returns True if matrix is a skew symmetric matrix else returns False.                                                                                                                             |
| isSquare        | Returns True if matrix is a square matrix else returns False.                                                                                                                                     |
| isSymmetric     | Returns True if matrix is a symmetric matrix else returns False.                                                                                                                                  |
| isUTriangular   | Returns True if matrix is an upper triangular matrix else returns False.                                                                                                                          |
| matAdd          | Returns the sum matrix (i.e. A + B), provided the matrices are compatible.                                                                                                                        |
| matMul          | Returns the product matrix (i.e. AB), provided the matrices are compatible.                                                                                                                       |
| matSub          | Returns the difference matrix (i.e. A - B), provided the matrices are compatible.                                                                                                                 |
| Null            | Returns a null matrix of order N x M. If only 1 parameter is given returns a null matrix of order N x N.                                                                                          |
| order           | Returns the order of the matrix as a tuple of the form (rows, columns).                                                                                                                           |
| power           | Returns the matrix representing the n<sup>th</sup> power of matrix A, provided the matrix is square matrix.                                                                                       |
| rotate          | Returns a matrix which is formed by rotating the given matrix, n times, in clockwise sense.                                                                                                       |
| scalarMul       | Returns the scalar product of A and n (i.e. nA).                                                                                                                                                  |
| trace           | Returns the trace of the matrix (i.e the product of elements on the diagonal) if possible.                                                                                                        |
| transpose       | Returns the transpose of the matrix.                                                                                                                                                              |

___________________________________________________________________________

## Contact

Please Feel Free to Reach Out if You Have Any Questions:

* Name: Siddhesh Agarwal
* E-mail: Siddhesh.agarwal@gmail.com

___________________________________________________________________________

## License

MIT License

Copyright (c) 2021 [Siddhesh-Agarwal](https://www.github.com/Siddhesh-Agarwal)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
