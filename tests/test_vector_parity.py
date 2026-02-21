"""Test vector parity between Python and C implementations."""

import unittest
from matmath.vector import Vector


class TestVectorParity(unittest.TestCase):
    def test_bool_zero_vector(self):
        """Test that a zero vector evaluates to False."""
        v = Vector([0, 0])
        self.assertFalse(bool(v), "Zero vector should be False")

    def test_bool_nonzero_vector(self):
        """Test that a non-zero vector evaluates to True."""
        v = Vector([1, 0])
        self.assertTrue(bool(v), "Non-zero vector should be True")

    def test_bool_all_nonzero(self):
        """Test that a vector with all non-zero elements evaluates to True."""
        v = Vector([1, 2, 3])
        self.assertTrue(bool(v), "Vector with all non-zero elements should be True")

    def test_rmul_scalar_vector(self):
        """Test reflected multiplication: scalar * vector."""
        v = Vector([1, 2])
        result = 2 * v
        expected = Vector([2, 4])
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_mul_vector_scalar(self):
        """Test normal multiplication: vector * scalar."""
        v = Vector([1, 2])
        result = v * 2
        expected = Vector([2, 4])
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_rmul_float(self):
        """Test reflected multiplication with float."""
        v = Vector([1.5, 2.5])
        result = 2.0 * v
        expected = Vector([3.0, 5.0])
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")


if __name__ == "__main__":
    unittest.main()
