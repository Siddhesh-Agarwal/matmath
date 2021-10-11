# [matmath module](https://github.com/Siddhesh-Agarwal/matmath)

A simple and efficient module for matrix manipulation.
___________________________________________________________________________

## Installing under Python

When installing the **matmath module** for python, it is recommended that you check if you have **python 3.6 or above**.
To install matmath, goto a terminal and run:

    pip3 install matmath
___________________________________________________________________________

## Functions and their uses

### Matrix related functions

| Functions         | Description                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| `adj`             | Returns the adjoint of the matrix multiplied by the multiplication factor.                                 |
| `compatAS`        | Tells if the addition/subtractition of the matrices is mathematically possible.                            |
| `compatM`         | Tells if the multiplication of the matrices is mathematically possible.                                    |
| `cut`             | Returns a smaller matrix by removing the required row and column. The default of row and column is 0.      |
| `det`             | Returns the determinant of the matrix (if mathematically possible).                                        |
| `Identity`        | Returns an identity matrix of order N x N multiplied by the multiplication factor.                         |
| `inv`             | Returns the inverse of the matrix (if mathematically possible) multiplied by the multiplication factor.    |
| `isDiagonal`      | Tells if input is a diagonal matrix.                                                                       |
| `isIdentity`      | Tells if input is an identity matrix.                                                                      |
| `isLTriangular`   | Tells if input is a lower triangular matrix.                                                               |
| `isMatrix`        | Tells if input is actually a matrix.                                                                       |
| `isNull`          | Tells if input is a null matrix.                                                                           |
| `isSkewSymmetric` | Tells if input is a skew symmetric matrix.                                                                 |
| `isSquare`        | Tells if input is a square matrix.                                                                         |
| `isSymmetric`     | Tells if input is a symmetric matrix.                                                                      |
| `isUTriangular`   | Tells if input is an upper triangular matrix.                                                              |
| `matAdd`          | Returns the sum matrix (i.e. A + B), if mathematically possible.                                           |
| `matMul`          | Returns the product matrix (i.e. AB), if mathematically possible.                                          |
| `matSub`          | Returns the difference matrix (i.e. A - B), if mathematically possible.                                    |
| `Null`            | Returns a null matrix of order N x M. If only 1 parameter is given returns a null matrix of order N x N.   |
| `order`           | Returns the order of the matrix as a tuple of the form (rows, columns).                                    |
| `power`           | Returns the n<sup>th</sup> power of matrix A, if mathematically possible.                                  |
| `rotate`          | Returns a matrix which is formed by rotating the given matrix, n times, in clockwise sense.                |
| `scalarMul`       | Returns the scalar product of A and n (i.e. nA).                                                           |
| `trace`           | Returns the trace of the matrix (i.e the product of elements on the diagonal), if mathematically possible. |
| `transpose`       | Returns the transpose of the matrix.                                                                       |

**NOTE**: Default value of mul (multiplication factor) is always 1.

### Vector related functions

| Functions       | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `__add__`       | Adds the 2 vectors                                          |
| `__eq__`        | Tells whether the 2 vectors are equal or not.               |
| `getitem__`     | Returns the vector at the given index.                      |
| `__len__`       | Returns the length of the vector.                           |
| `__mul__`       | Alias of `cross_product()`.                                 |
| `__setitem__`   | changes the value of the vector using the key.              |
| `__sub__`       | Subtracts the second vector from the first vector.          |
| `argument`      | Returns the argument of the vector.                         |
| `cross_product` | Cross product of the vector with respect to another vector. |
| `dot_product`   | Dot product of the vector with respect to another vector.   |
| `is_parellel`   | Tells whether the two vectors are parellel or not.          |
| `is_unit`       | Tells whether the vector is a unit vector or not.           |
| `magnify`       | Magnifies a vector.                                         |
| `modulus`       | Returns the modulus of the vector.                          |
| `rotate`        | Rotates the 2d vector in 2D space.                          |
| `unitVector`    | Returns the unit vector in the direction of the vector.     |
S
___________________________________________________________________________

## Contact

Please feel free to reach out if you have any questions:

* **Name**: Siddhesh Agarwal
* **E-mail**: siddhesh.agarwal@gmail.com

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
