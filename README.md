# [matmath module](https://github.com/Siddhesh-Agarwal/matmath)

A simple and efficient module for matrix manipulation.

[![Downloads](https://pepy.tech/badge/matmath)](https://pepy.tech/project/matmath)

---

## Installing under Python

When installing the **matmath module** for python, it is recommended that you check if you have **python 3.6 or above**. To install matmath, goto a terminal and run:

    pip install matmath

To upgrade matmath, run:

    pip install --upgrade matmath

---

## Functions and their uses

The `Matrix` and `Vector` classes support all mathematical operations like addition, subtraction, multiplication, division, matrix multiplication, etc. Apart from that, the `Matrix` class also supports the following functions:

### Matrix related functions

| Functions                | Description                                                                                              |
| :----------------------- | -------------------------------------------------------------------------------------------------------- |
| `.adjoint()`             | Returns the adjoint of the matrix.                                                                       |
| `.adj()`                 | Alias of `.adjoint()`                                                                                    |
| `.cofactor()`            | Returns the cofactor of the matrix.                                                                      |
| `.copy()`                | Returns a copy of the matrix.                                                                            |
| `.cut()`                 | Returns a smaller matrix by removing the required row and column. The default of row and column is None. |
| `.determinant()`         | Returns the determinant of the matrix (if mathematically possible).                                      |
| `.det()`                 | Alias of `.determinant()`.                                                                               |
| `.inverse()`             | Returns the inverse of the matrix (if mathematically possible) multiplied by the multiplication factor.  |
| `.inv()`                 | Alias of `.inverse()`.                                                                                   |
| `.is_diagonal()`         | Tells if input is a diagonal matrix.                                                                     |
| `.is_identity()`         | Tells if input is an identity matrix.                                                                    |
| `.is_lower_triangular()` | Tells if input is a lower triangular matrix.                                                             |
| `.is_null()`             | Tells if input is a null matrix.                                                                         |
| `.is_skew_symmetric()`   | Tells if input is a skew symmetric matrix.                                                               |
| `.is_square()`           | Tells if input is a square matrix.                                                                       |
| `.is_symmetric()`        | Tells if input is a symmetric matrix.                                                                    |
| `.is_upper_triangular()` | Tells if input is an upper triangular matrix.                                                            |
| `.order()`               | Returns the order of the matrix as a tuple of the form (rows, columns).                                  |
| `.rotate()`              | Returns a matrix which is formed by rotating the given matrix, n times, in clockwise sense.              |
| `.trace()`               | Returns the trace of the matrix, if mathematically possible.                                             |
| `.transpose()`           | Returns the transpose of the matrix.                                                                     |
| `identity()`             | Returns an identity matrix of order N x N multiplied by the multiplication factor.                       |
| `zero()`                 | Returns a null matrix of order N x M. If only 1 parameter is given returns a null matrix of order N x N. |

### Vector related functions

| Method          | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `argument`      | Returns the argument of the vector.                         |
| `cross_product` | Cross product of the vector with respect to another vector. |
| `dot_product`   | Dot product of the vector with respect to another vector.   |
| `is_parellel`   | Tells whether the two vectors are parellel or not.          |
| `is_unit`       | Tells whether the vector is a unit vector or not.           |
| `magnify`       | Magnifies a vector.                                         |
| `modulus`       | Returns the modulus of the vector.                          |
| `rotate`        | Rotates the 2d vector in 2D space.                          |
| `unit_vector`   | Returns the unit vector in the direction of the vector.     |
| `x`             | Returns the 1st component of the vector.                    |
| `y`             | Returns the 2nd component of the vector.                    |
| `z`             | Returns the 3rd component of the vector.                    |

---

## Contact

Please feel free to reach out if you have any questions:

- **Name**: Siddhesh Agarwal
- **E-mail**: [siddhesh.agarwal@gmail.com](mailto:siddhesh.agarwal@gmail.com)

---

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
