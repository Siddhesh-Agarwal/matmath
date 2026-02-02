import unittest
from matmath import Matrix


class TestMatrix(unittest.TestCase):
    def test_matrix_init(self):
        mat = [[1, 2], [3, 4]]
        matrix = Matrix(mat)
        self.assertEqual(matrix.to_list(), mat)
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.cols, 2)

    def test_matrix_invalid_init(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2], [3]])

    def test_matrix_add(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 + m2
        self.assertEqual(result.to_list(), [[6, 8], [10, 12]])

    def test_matrix_sub(self):
        m1 = Matrix([[5, 6], [7, 8]])
        m2 = Matrix([[1, 2], [3, 4]])
        result = m1 - m2
        self.assertEqual(result.to_list(), [[4, 4], [4, 4]])

    def test_matrix_mul_scalar(self):
        m1 = Matrix([[1, 2], [3, 4]])
        result = m1 * 2
        self.assertEqual(result.to_list(), [[2, 4], [6, 8]])

    def test_matrix_mul_elementwise(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 2], [2, 2]])
        result = m1 * m2
        self.assertEqual(result.to_list(), [[2, 4], [6, 8]])

    def test_matrix_matmul(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 0], [1, 2]])
        # [1*2+2*1, 1*0+2*2] = [4, 4]
        # [3*2+4*1, 3*0+4*2] = [10, 8]
        result = m1 @ m2
        self.assertEqual(result.to_list(), [[4, 4], [10, 8]])

    def test_matrix_transpose(self):
        m1 = Matrix([[1, 2], [3, 4]])
        result = m1.transpose()
        self.assertEqual(result.to_list(), [[1, 3], [2, 4]])

    def test_matrix_determinant(self):
        m1 = Matrix([[1, 2], [3, 4]])
        # 1*4 - 2*3 = -2
        self.assertAlmostEqual(m1.determinant(), -2.0)

    def test_matrix_trace(self):
        m1 = Matrix([[1, 2], [3, 4]])
        self.assertEqual(m1.trace(), 5)

    def test_matrix_properties(self):
        m_id = Matrix([[1, 0], [0, 1]])
        self.assertTrue(m_id.is_square())
        self.assertTrue(m_id.is_identity())
        self.assertTrue(m_id.is_diagonal())
        self.assertTrue(m_id.is_symmetric())

        m_sym = Matrix([[1, 2], [2, 1]])
        self.assertTrue(m_sym.is_symmetric())
        self.assertFalse(m_sym.is_diagonal())

    def test_matrix_order(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m1.order, (2, 3))
        self.assertEqual(m1.size, (2, 3))


if __name__ == "__main__":
    unittest.main()
