# Changelog
_______________________________

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
