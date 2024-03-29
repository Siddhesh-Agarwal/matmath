# Changelog

---

## 16 June 2021 - v1.0.0

- Initial Release.

## 18 June 2021 - v1.0.1

- Renamed `mmath.py` to `matmath.py`.
- Corrected spelling error.
- Fixed `showwarning()`.

## 24 June 2021 - v1.1.0

- Replaced warnings with errors (ValueError).
- Improved efficiency of `Null()`, `Identity()` and `matSub()`.
- Reduced SLOC.

## 24 June 2021 - v1.1.1

- Fixed `order()` function.

## 21 July 2021 - v2.0.0

- Added vector support by creating class `Vector`.

## 11 October 2021 - v2.1.0

- Added `__eq__` and `__setitem__` methods to `Vector` class.
- Improved time complexity of `__len__` and `modulus` method.
- Rectified error in `__add__` and `__sub__` method.
- `__init__` can now handle lists and arrays apart from numbers as an arguement.
- Improvised `__repr__` method. A vector now looks like this `<1, 0, 0>` instead of `[1, 0, 0]`.
- Added `is_unit` and `is_parellel` methods.
- Improved comments in `matmath.py` which can be accessed by using `help()` method.

## 12 October 2021 - v2.1.1

- Corrected `arguement()` in `Vector` class.
- Changed `unitVector()` to `unit_vector()` in `Vector` class.
- Now call `Vector(n)` to generate a n-dimensional zero vector. n defaults to 2.
- Corrected problem in `rotate()` in `Vector` class.

## 15 February 2022 - v3.0.0

- Made multiple corrections that solved a few significant bugs.
- `matmath.py` has been converted into from a simple function definitions into a full fledge function class called `Matrix`.
- Removed `compatM()` and `compatAS()` from `Vector` class.
- Improved `__init__`, `__iter__`, `__next__`, `__repr__` and `__str__` methods in `Vector` class.
- Added support for `__matmul__` method and made changes to `__mul__` method to `Vector` class.
- removed `__radd__`, `__rsub__` and `__rmul__` methods from vector class (methods were not needed).
- Added support for `!=` and `==` operator to `Vector` class.
- Created alias for `arguement` - `arg` in `Vector` class.
- Added support for `__radd__` and `__rsub__` methods to `Vector` class.
- Added `minor()` and `cofactor()` methods to `Matrix` class.
- `__setitem__` method in `Vector` class has ben deprecated.
- `x()`, `y()` and `z()` methods in `Vector` class have ben deprecated. (using indexing instead)
- improved importing.

Now you can use:

    from matmath import Matrix, Vector

instead of importing like this:

    from matmath.matmath import Matrix, Vector


## 2 January 2024 - v.3.2.0

- Completely moved away from [twine](https://twine.readthedocs.io/en/stable/) in favour of [poetry](https://python-poetry.org/).
- Rename `__pow__` method to `pow` in `Vector` class.
- Type hints added to all methods of both `Matrix` and `Vector` classes.
- Refactored multiple methods across both classes to improve time/space complexity.
- Added better type checking to `__init__` method of `Matrix` class.
- Better support for `__matmul__` method in `Vector` and `Matrix` classes.

NOTE: Python 3.6 and 3.7 are still supported even though they have reached [EOL](https://endoflife.date/python).