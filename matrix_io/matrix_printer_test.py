import unittest
import io
import sys
from numpy import array
from unittest.mock import patch

from .matrix_printer import get_matrix_pad, pad_number, print_augumented_matrix, print_matrix

class TestPadNumber(unittest.TestCase):
    def test_pad_number_pad_3_number_1(self):
        number = 1
        pad = 3
        expected = "  1"
        self.assertEqual(pad_number(number, pad), expected)

    def test_pad_number_pad_5_number_1(self):
        number = 1
        pad = 5
        expected = "    1"
        self.assertEqual(pad_number(number, pad), expected)

    def test_pad_number_pad_3_number_10(self):
        number = 10
        pad = 3
        expected = " 10"
        self.assertEqual(pad_number(number, pad), expected)

    def test_pad_number_pad_2_number_10(self):
        number = 10
        pad = 2
        expected = "10"
        self.assertEqual(pad_number(number, pad), expected)

    def test_pad_number_pad_3_number_100(self):
        number = 100
        pad = 3
        expected = "100"
        self.assertEqual(pad_number(number, pad), expected)

    def test_pad_number_pad_5_number_100(self):
        number = 100
        pad = 5
        expected = "  100"
        self.assertEqual(pad_number(number, pad), expected)

class TestGetMatrixPad(unittest.TestCase):
    def test_get_matrix_pad_1x1(self):
        matrix = [[1]]
        expected = 1
        self.assertEqual(get_matrix_pad(matrix), expected)

    def test_get_matrix_pad_2x2(self):
        matrix = [[1, 2], [3, 4]]
        expected = 1
        self.assertEqual(get_matrix_pad(matrix), expected)
    
    def test_get_matrix_pad_2x2_2digit(self):
        matrix = [[10, 2], [3, 4]]
        expected = 2
        self.assertEqual(get_matrix_pad(matrix), expected)

    def test_get_matrix_pad_2x2_3digit(self):
        matrix = [[10, 2], [3, 100]]
        expected = 3
        self.assertEqual(get_matrix_pad(matrix), expected)

    def test_get_matrix_pad_2x2_4digit(self):
        matrix = [[10, 2], [3, 1000]]
        expected = 4
        self.assertEqual(get_matrix_pad(matrix), expected)

class TestMatrixPrint(unittest.TestCase):
    def test_print_matrix_1x1(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[1]])
        expected = "| 1 |\n"

        print_matrix(matrix)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)

    def test_print_matrix_2x2(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[1, 2], [3, 4]])
        expected = "| 1 2 |\n| 3 4 |\n"

        print_matrix(matrix)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)

    def test_print_matrix_2x2_2digit(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[10, 2], [3, 4]])
        expected = "| 10  2 |\n|  3  4 |\n"

        print_matrix(matrix)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)

    def test_print_matrix_3x3_2digit(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[10, 2, 3], [3, 4, 5], [6, 7, 8]])
        expected = "| 10  2  3 |\n|  3  4  5 |\n|  6  7  8 |\n"

        print_matrix(matrix)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)


    def test_print_matrix_augumented_3x3(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
        expected = "| 1 2 :3 |\n| 3 4 :5 |\n| 6 7 :8 |\n"

        print_matrix(matrix, True)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)

    def test_print_matrix_augumented_3x3_2digit(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[10, 2, 3], [3, 4, 5], [6, 7, 8]])
        expected = "| 10  2 : 3 |\n|  3  4 : 5 |\n|  6  7 : 8 |\n"

        print_matrix(matrix, True)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)

    def test_print_matrix_augumented_3x3_digit_negative(self):
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput 

        matrix = array([[1, 2, -3], [3, 4, -5], [6, 7, 8]])
        expected = "|  1  2 :-3 |\n|  3  4 :-5 |\n|  6  7 : 8 |\n"

        print_matrix(matrix, True)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), expected)


class TestPrintAugumentedMatrix(unittest.TestCase):
    @patch('matrix_io.matrix_printer.print_matrix')
    def test_print_augumented_matrix_calls_print_matrix(self, print_matrix):
        matrix = array([[1, 2, 3],[4, 5, 6]])
        print_augumented_matrix(matrix)
        self.assertTrue(print_matrix.calledWith(matrix, True))
