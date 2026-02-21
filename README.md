# [matmath module](https://github.com/Siddhesh-Agarwal/matmath)

A high-performance and efficient module for matrix and vector manipulation, powered by **C extensions**.

![Downloads](https://static.pepy.tech/personalized-badge/matmath?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)
[![PyPI version](https://badge.fury.io/py/matmath.svg)](https://badge.fury.io/py/matmath)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Performance

`matmath` 4.0.0+ uses CPython extensions to provide near-native performance for all mathematical operations. This makes it suitable for applications ranging from simple geometry to complex numerical simulations where speed is critical.

## Installing

To install the **matmath module**, ensure you have **Python 3.9 or above**.

```sh
pip install matmath
```

To upgrade:

```sh
pip install --upgrade matmath
```

---

## Features and Usage

### Vector Operations
The `Vector` class represents an N-dimensional vector and supports a wide range of operations.

#### Operator Support
| Operation | Description |
| :--- | :--- |
| **Addition** | Element-wise addition (`v1 + v2`) |
| **Subtraction** | Element-wise subtraction (`v1 - v2`) |
| **Multiplication** | Scalar multiplication (`v1 * scalar`) |
| **Multiplication** | Element-wise multiplication (`v1 * v2`) |
| **Division** | Scalar division (`v1 / scalar`) |
| **Division** | Element-wise division (`v1 / v2`) |
| **Cross Product** | Uses `@` operator for cross product (2D/3D) (`v1 @ v2`) |
| **Modulus** | Returns the magnitude of the vector (`abs(v1)`) |
| **Indexing** | Access elements by index (`v1[i]`) |
| **Length** | Returns the number of elements (`len(v1)`) |
| **Comparison** | Equality checks (`v1 == v2`, `v1 != v2`) |
| **Truth Value** | `bool(v1)` returns `False` if all elements are zero |
| **Hashing** | Vectors are hashable and can be used as dictionary keys |
| **Copy** | Returns a copy of the vector (`v1.copy()`) |

#### Vector Methods
| Method | Description |
| :--- | :--- |
| `.modulus()` | Returns the magnitude of the vector. |
| `.argument()` | Returns the argument (angles) of the vector. |
| `.unit_vector()` | Returns a unit vector in the same direction. |
| `.magnify(m)` | Magnifies the vector by factor `m`. |
| `.rotate_2d(theta, radians=True)` | Rotates a 2D vector by `theta`. |
| `.rotate_3d(theta, axis, radians=True)` | Rotates a 3D vector around an `axis` using Rodrigues' formula. |
| `.dot_product(v)` | Returns the dot product with vector `v`. |
| `.cross_product(v)` | Returns the cross product with vector `v`. |
| `.is_unit()` | Checks if the magnitude is 1. |
| `.is_parallel(v)` | Checks if the vector is parallel to `v`. |
| `.is_orthogonal(v)` | Checks if the vector is orthogonal to `v`. |
| `.copy()` | Returns a copy of the vector. |
| `.to_list()` | Converts the vector to a Python list. |

#### Vector Aliases
| Original Method | Alias |
| :--- | :--- |
| `.modulus()` | `.mod()` |
| `.argument()` | `.arg()` |
| `.dot_product(v)` | `.dot(v)` |
| `.cross_product(v)` | `.cross(v)` |

### Matrix Operations
The `Matrix` class represents an M x N matrix.

#### Operator Support
| Operation | Description |
| :--- | :--- |
| **Addition** | Matrix addition (`m1 + m2`) |
| **Subtraction** | Matrix subtraction (`m1 - m2`) |
| **Scalar Mul** | Multiplies all elements by scalar (`m1 * scalar`) |
| **Element-wise** | Hadamard (element-wise) multiplication (`m1 * m2`) |
| **Matrix Mul** | Standard matrix multiplication (`m1 @ m2`) |
| **Division** | Scalar division (`m1 / scalar`) |
| **Division** | Element-wise division (`m1 / m2`) |
| **Floor Div** | Element-wise floor division (`m1 // m2`) |
| **Indexing** | Access rows by index (`m1[i]`) |
| **Iteration** | Iterate over rows (`for row in m1`) |
| **Length** | Returns the number of rows (`len(m1)`) |
| **Comparison** | Equality checks (`m1 == m2`, `m1 != m2`) |

#### Matrix Methods
| Method | Description |
| :--- | :--- |
| `.transpose()` | Returns the transpose of the matrix. |
| `.determinant()` | Returns the determinant of a square matrix. |
| `.trace()` | Returns the sum of diagonal elements. |
| `.order` (property) | Returns `(rows, cols)` of the matrix. |
| `.is_square()` | Returns `True` if rows == cols. |
| `.is_symmetric()` | Checks if the matrix is symmetric. |
| `.is_diagonal()` | Checks if the matrix is diagonal. |
| `.is_identity()` | Checks if the matrix is identity. |
| `.is_invertible()` | Checks if the matrix is invertible. |
| `.is_null()` | Checks if the matrix is a null matrix. |
| `.is_skew_symmetric()` | Checks if the matrix is skew-symmetric. |
| `.is_lower_triangular()` | Checks if the matrix is lower triangular. |
| `.is_upper_triangular()` | Checks if the matrix is upper triangular. |
| `.cut(i, j)` | Returns a new matrix after removing row `i` and/or column `j`. |
| `.minor(i, j)` | Returns the minor of element `(i, j)`. |
| `.cofactor(i, j)` | Returns the cofactor of element `(i, j)`. |
| `.adjoint()` | Returns the adjoint of the matrix. |
| `.inverse()` | Returns the inverse of the matrix. |
| `.pow(p)` | Returns the matrix raised to the power `p`. |
| `.rotate(turns)` | Rotates the matrix clockwise by 90-degree `turns`. |
| `.copy()` | Returns a copy of the matrix. |
| `.to_list()` | Converts the matrix to a list of lists. |

#### Matrix Static Methods
| Method | Description |
| :--- | :--- |
| `Matrix.identity(n)` | Returns an `n x n` identity matrix. |
| `Matrix.zero(order)` | Returns a zero matrix of the given `order` (r, c). |
| `Matrix.fill(val, order)` | Returns a matrix of the given `order` filled with `val`. |

#### Matrix Aliases
| Original Method | Alias |
| :--- | :--- |
| `.determinant()` | `.det()` |
| `.order` | `.size` |
| `.adjoint()` | `.adj()` |
| `.inverse()` | `.inv()` |
| `.is_diagonal()` | `.is_diagonal_dominant()` |
| `.is_lower_triangular()` | `.is_lower_hessenberg()` |
| `.is_upper_triangular()` | `.is_upper_hessenberg()` |

---

## Contact

Please feel free to reach out if you have any questions:

- **Name**: Siddhesh Agarwal
- **Email**: [siddhesh.agarwal@gmail.com](mailto:siddhesh.agarwal@gmail.com)
- **GitHub**: [Siddhesh-Agarwal](https://www.github.com/Siddhesh-Agarwal)

---

## License

```plaintext
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
```
