import unittest
from matmath import Vector


class TestVector(unittest.TestCase):
    # Ways to create a Vector
    def test_vector_1(self):
        vec = Vector()  # defaults to <0, 0>
        self.assertEqual(vec, Vector(0, 0))

    def test_vector_2(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector([1, 2, 3])
        self.assertEqual(vec1, vec2)

    # Check that the declaration fails when a non-number argument is passed
    def failed_declaration_1(self):
        with self.assertRaises(ValueError):
            vec = Vector(1, "a", 2)

    def failed_declaration_2(self):
        with self.assertRaises(ValueError):
            vec = Vector([1, "a", 2])

    def failed_declaration_3(self):
        with self.assertRaises(ValueError):
            vec = Vector(1, 2, [1, 2, 3])

    def test_getitem(self):
        vec = Vector(1, 2, 3)
        # positive indexing
        self.assertEqual(vec[0], 1)
        self.assertEqual(vec[1], 2)
        self.assertEqual(vec[2], 3)
        # negative indexing
        self.assertEqual(vec[-1], 3)
        self.assertEqual(vec[-2], 2)
        self.assertEqual(vec[-3], 1)

    # Test support for built-in functions
    def test_len(self):
        vec = Vector(1, 2, 3)
        self.assertEqual(len(vec), 3)

    def test_str(self):
        vec = Vector(1, 2, 3)
        self.assertEqual(str(vec), "<1, 2, 3>")

    def test_repr_1(self):
        vec = Vector(1, 2, 3)
        self.assertEqual(repr(vec), "Vector(1, 2, 3)")

    def test_repr_2(self):
        vec = Vector([1, 2, 3])
        self.assertEqual(repr(vec), "Vector(1, 2, 3)")

    # Test support for math operations
    def test_add(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(4, 5, 6)
        self.assertEqual(vec1 + vec2, Vector(5, 7, 9))

    def test_sub(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(4, 5, 6)
        self.assertEqual(vec1 - vec2, Vector(-3, -3, -3))

    def test_mul(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(4, 5, 6)
        self.assertEqual(vec1 * vec2, Vector(4, 10, 18))

    def test_div(self):
        vec1 = Vector(2, 4, 6)
        self.assertEqual(vec1 / 2, Vector(1, 2, 3))

    def test_matmul(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(4, 5, 6)
        self.assertEqual(vec1 @ vec2, Vector(-3, 6, -3))

    def test_eq(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(1, 2, 3)
        self.assertTrue(vec1 == vec2)

    def test_ne(self):
        vec1 = Vector(1, 2, 3)
        vec2 = Vector(1, 2, 3)
        self.assertFalse(vec1 != vec2)

    # Test component retrieval
    def test_component_retrieval(self):
        vec1 = Vector(1, 2, 3)
        self.assertEquals(vec1.x, vec1[0], 1)
        self.assertEquals(vec1.y, vec1[1], 2)
        self.assertEquals(vec1.z, vec1[2], 3)

    def test_modulus(self):
        vec1 = Vector(2, 3, 6)
        self.assertEqual(vec1.modulus(), 7)


if __name__ == "__main__":
    unittest.main()
