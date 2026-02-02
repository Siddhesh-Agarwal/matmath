"""matmath - A simple and efficient module for matrix and vector manipulation with C extensions."""

try:
    from matmath._vector import Vector
    from matmath._matrix import Matrix
except ImportError as e:
    raise ImportError(
        "Failed to import C extensions. "
        "Please ensure the package is properly built. "
        "Run: pip install -e . or python setup.py build_ext --inplace"
    ) from e

__version__ = "4.0.0"
__all__ = ["Vector", "Matrix"]
