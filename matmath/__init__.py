"""matmath - A simple and efficient module for matrix and vector manipulation with C extensions."""

import warnings

try:
    from matmath._vector import Vector
    from matmath._matrix import Matrix
except ImportError:
    warnings.warn(
        "C extensions not available. Falling back to pure Python implementation. "
        "Performance may be reduced. Run: pip install -e . to build C extensions.",
        ImportWarning,
        stacklevel=2,
    )
    from matmath.legacy.vector import Vector
    from matmath.legacy.matrix import Matrix

__version__ = "4.0.0"
__all__ = ["Vector", "Matrix"]
