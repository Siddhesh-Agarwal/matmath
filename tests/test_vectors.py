import unittest
from matmath import Vector


class TestVector(unittest.TestCase):
    # Ways to create a Vector
    def test_vector_init_default(self):
        vec = Vector()  # defaults to <0, 0>
        self.assertEqual(vec.to_list(), [0.0, 0.0])

    def test_vector_init_list(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([1, 2, 3])
        self.assertEqual(vec1, vec2)

    def test_vector_init_none(self):
        vec = Vector(None)
        self.assertEqual(vec.to_list(), [0.0, 0.0])

    def test_vector_inequality(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([1, 2])
        self.assertNotEqual(vec1, vec2)

    def test_getitem(self):
        vec = Vector([1, 2, 3])
        self.assertEqual(vec[0], 1.0)
        self.assertEqual(vec[1], 2.0)
        self.assertEqual(vec[2], 3.0)

    def test_len(self):
        vec = Vector([1, 2, 3])
        self.assertEqual(len(vec), 3)

    def test_str(self):
        vec = Vector([1, 2, 3])
        self.assertEqual(str(vec), "<1, 2, 3>")

    def test_repr(self):
        vec = Vector([1, 2, 3])
        self.assertEqual(repr(vec), "Vector(1, 2, 3)")

    def test_add(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        self.assertEqual(vec1 + vec2, Vector([5, 7, 9]))

    def test_sub(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        self.assertEqual(vec1 - vec2, Vector([-3, -3, -3]))

    def test_mul_scalar(self):
        vec1 = Vector([1, 2, 3])
        self.assertEqual(vec1 * 2, Vector([2, 4, 6]))
        self.assertEqual(2 * vec1, Vector([2, 4, 6]))

    def test_mul_vector(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        self.assertEqual(vec1 * vec2, Vector([4, 10, 18]))

    def test_div_scalar(self):
        vec1 = Vector([2, 4, 6])
        self.assertEqual(vec1 / 2, Vector([1, 2, 3]))

    def test_matmul(self):
        # Note: @ is cross product in this library
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        # Cross product of [1,2,3] and [4,5,6] is [-3, 6, -3]
        self.assertEqual(vec1 @ vec2, Vector([-3, 6, -3]))

    def test_modulus(self):
        vec1 = Vector([2, 3, 6])
        self.assertEqual(vec1.modulus(), 7.0)
        self.assertEqual(abs(vec1), 7.0)

    def test_dot_product(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
        self.assertEqual(vec1.dot_product(vec2), 32.0)

    def test_unit_vector(self):
        vec = Vector([3, 4])
        unit = vec.unit_vector()
        self.assertEqual(unit.to_list(), [0.6, 0.8])
        self.assertAlmostEqual(unit.modulus(), 1.0)

    def test_is_unit(self):
        self.assertTrue(Vector([1, 0]).is_unit())
        self.assertFalse(Vector([1, 1]).is_unit())


if __name__ == "__main__":
    unittest.main()

