import unittest
import sympy as sp
from commands.linear_algebra_commands import mult, sub, add
from commands.variables import Variable, set_variable, variable_list


class TestLinearAlgebraCommands(unittest.TestCase):
    
    def setUp(self):
        """Clear variable list before each test"""
        variable_list.clear()
        
    def tearDown(self):
        """Clear variable list after each test"""
        variable_list.clear()

    def test_mult_matrix_matrix(self):
        """Test matrix multiplication"""
        # Create test matrices
        A = sp.Matrix([[1, 2], [3, 4]])
        B = sp.Matrix([[2, 0], [1, 2]])
        
        # Set variables
        set_variable("A", A)
        set_variable("B", B)
        
        # Test multiplication
        result, error = mult(["A", "B"])
        
        expected = A * B  # Matrix multiplication
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_mult_scalar_matrix(self):
        """Test scalar multiplication: scalar * matrix"""
        # Create test matrix
        A = sp.Matrix([[1, 2], [3, 4]])
        
        # Set variable
        set_variable("A", A)
        
        # Test scalar multiplication (scalar first)
        result, error = mult(["5", "A"])
        
        expected = 5 * A
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_mult_matrix_scalar(self):
        """Test scalar multiplication: matrix * scalar"""
        # Create test matrix
        A = sp.Matrix([[1, 2], [3, 4]])
        
        # Set variable
        set_variable("A", A)
        
        # Test scalar multiplication (matrix first)
        result, error = mult(["A", "10"])
        
        expected = A * 10
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_mult_scalar_scalar(self):
        """Test scalar multiplication: scalar * scalar"""
        result, error = mult(["5", "3"])
        
        self.assertIsNone(error)
        self.assertEqual(result, 15)

    def test_mult_float_scalar(self):
        """Test multiplication with float scalars"""
        A = sp.Matrix([[2, 4], [6, 8]])
        set_variable("A", A)
        
        # Test float scalar multiplication
        result, error = mult(["A", "2.5"])
        
        expected = A * 2.5
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_mult_negative_scalar(self):
        """Test multiplication with negative scalars"""
        A = sp.Matrix([[1, 2], [3, 4]])
        set_variable("A", A)
        
        # Test negative scalar multiplication
        result, error = mult(["-3", "A"])
        
        expected = -3 * A
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_mult_undefined_variable(self):
        """Test multiplication with undefined variable"""
        result, error = mult(["A", "5"])
        
        self.assertIsNotNone(error)
        self.assertEqual(error, "Variable 'A' is not defined.")
        self.assertIsNone(result)

    def test_sub_matrix_matrix(self):
        """Test matrix subtraction"""
        # Create test matrices
        A = sp.Matrix([[5, 7], [3, 9]])
        B = sp.Matrix([[2, 3], [1, 4]])
        
        # Set variables
        set_variable("A", A)
        set_variable("B", B)
        
        # Test subtraction
        result, error = sub(["A", "B"])
        
        expected = A - B
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_sub_square_matrices(self):
        """Test subtraction of square matrices"""
        A = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        B = sp.Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        
        set_variable("A", A)
        set_variable("B", B)
        
        result, error = sub(["A", "B"])
        
        expected = A - B
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_sub_single_element_matrices(self):
        """Test subtraction of 1x1 matrices"""
        A = sp.Matrix([[10]])
        B = sp.Matrix([[3]])
        
        set_variable("A", A)
        set_variable("B", B)
        
        result, error = sub(["A", "B"])
        
        expected = A - B
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_sub_undefined_variable(self):
        """Test subtraction with undefined variable"""
        A = sp.Matrix([[1, 2], [3, 4]])
        set_variable("A", A)
        
        result, error = sub(["A", "B"])
        
        self.assertIsNotNone(error)
        self.assertEqual(error, "Variable 'B' is not defined.")
        self.assertIsNone(result)

    def test_sub_incompatible_dimensions(self):
        """Test subtraction with incompatible matrix dimensions"""
        A = sp.Matrix([[1, 2], [3, 4]])  # 2x2
        B = sp.Matrix([[1, 2, 3]])       # 1x3
        
        set_variable("A", A)
        set_variable("B", B)
        
        # This should raise an exception due to incompatible dimensions
        with self.assertRaises(Exception):
            sub(["A", "B"])

    def test_add_matrix_matrix(self):
        """Test matrix addition for comparison with mult behavior"""
        A = sp.Matrix([[1, 2], [3, 4]])
        B = sp.Matrix([[5, 6], [7, 8]])
        
        set_variable("A", A)
        set_variable("B", B)
        
        result, error = add(["A", "B"])
        
        expected = A + B
        self.assertIsNone(error)
        self.assertEqual(result, expected)

    def test_vector_operations(self):
        """Test operations on column vectors"""
        # Column vectors
        v1 = sp.Matrix([[1], [2], [3]])
        v2 = sp.Matrix([[4], [5], [6]])
        
        set_variable("V", v1)
        set_variable("W", v2)
        
        # Test subtraction
        result_sub, error_sub = sub(["V", "W"])
        expected_sub = v1 - v2
        self.assertIsNone(error_sub)
        self.assertEqual(result_sub, expected_sub)
        
        # Test scalar multiplication
        result_mult, error_mult = mult(["V", "3"])
        expected_mult = v1 * 3
        self.assertIsNone(error_mult)
        self.assertEqual(result_mult, expected_mult)

    def test_row_vector_operations(self):
        """Test operations on row vectors"""
        # Row vectors
        r1 = sp.Matrix([[1, 2, 3]])
        r2 = sp.Matrix([[4, 5, 6]])
        
        set_variable("P", r1)
        set_variable("Q", r2)
        
        # Test subtraction
        result_sub, error_sub = sub(["P", "Q"])
        expected_sub = r1 - r2
        self.assertIsNone(error_sub)
        self.assertEqual(result_sub, expected_sub)
        
        # Test scalar multiplication
        result_mult, error_mult = mult(["2", "P"])
        expected_mult = 2 * r1
        self.assertIsNone(error_mult)
        self.assertEqual(result_mult, expected_mult)


if __name__ == '__main__':
    unittest.main()