import unittest
from matmath import Vector, Matrix


class TestImport(unittest.TestCase):
    """Test suite for matmath module import and basic instantiation."""
    
    def test_import_matmath_module(self):
        """Verify matmath module imports Vector and Matrix successfully."""
        self.assertTrue(callable(Vector))
        self.assertTrue(callable(Matrix))
    
    def test_vector_creation(self):
        """Verify Vector instantiates with coordinate list."""
        v = Vector([1, 2, 3])
        self.assertIsInstance(v, Vector)
    
    def test_vector_string_representation(self):
        """Verify Vector has valid string representation."""
        v = Vector([1, 2, 3])
        s = str(v)
        self.assertIsInstance(s, str)
        self.assertGreater(len(s), 0)
    
    def test_matrix_creation(self):
        """Verify Matrix instantiates with 2D array."""
        m = Matrix([[1, 2], [3, 4]])
        self.assertIsInstance(m, Matrix)
    
    def test_matrix_string_representation(self):
        """Verify Matrix has valid string representation."""
        m = Matrix([[1, 2], [3, 4]])
        s = str(m)
        self.assertIsInstance(s, str)
        self.assertGreater(len(s), 0)
    
    def test_vector_and_matrix_creation(self):
        """Integration test: create both Vector and Matrix."""
        v = Vector([1, 2, 3])
        m = Matrix([[1, 2], [3, 4]])
        self.assertIsInstance(v, Vector)
        self.assertIsInstance(m, Matrix)


if __name__ == '__main__':
    unittest.main()