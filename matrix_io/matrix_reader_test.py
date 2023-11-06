import unittest
import io
import sys
from fractions import Fraction
from numpy import array

from unittest.mock import patch

from .matrix_reader import read_matrix

string_of_ints = "1,2 3,4 END"


class TestMatrixReader(unittest.TestCase):
    @patch("builtins.input", side_effect=["1 2", "3 4", "END"])
    def test_read_matrix_2x2(self, mock_input):
        matrix = read_matrix()
        expected = array([[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]])
        self.assertSequenceEqual(matrix.tolist(), expected.tolist())

    @patch("builtins.input", side_effect=["1 2 3", "4 5 -6", "7 8 9", "END"])
    def test_read_matrix_3x3(self, mock_input):
        matrix = read_matrix()
        expected = [[1, 2, 3], [4, 5, -6], [7, 8, 9]]
        self.assertSequenceEqual(matrix.tolist(), expected)

    @patch("builtins.input", side_effect=["1,2,3,4", "5,6, a, b", "END"])
    def test_read_matrix_2x4_letter_error(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        expected = "Invalid input. Please try again:\n"
        matrix = read_matrix()
        sys.stdout = sys.__stdout__
        self.assertTrue(capturedOutput.getvalue().find(expected) != -1)
        self.assertTrue(len(matrix) == 0)

    @patch("builtins.input", side_effect=["1 2 3 4", "5 6 7", "END"])
    def test_read_matrix_2x4_3x3_error(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        expected = "Invalid input. The matrix must have the same number of columns in each row. Please try again:\n"
        read_matrix()
        sys.stdout = sys.__stdout__
        self.assertTrue(capturedOutput.getvalue().find(expected) != -1)
