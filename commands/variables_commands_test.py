import unittest
from sympy import Matrix

from commands.variables_commands import print_value, read_variable, set_variable_command
from unittest.mock import patch

from .variables import Variable, set_variable, variable_list


class TestReadVariable(unittest.TestCase):
    @patch("builtins.input", side_effect=["1 2", "3 4", "END"])
    def test_read_variable(self, mock_input):
        variable_list.clear()
        params = ["A"]
        value, error = read_variable(params)
        self.assertIsNone(error)
        self.assertIsNotNone(value)
        self.assertEqual(value, Matrix([[1, 2], [3, 4]]))

    @patch("builtins.input", side_effect=["1 2", "3 4", "END"])
    def test_read_variable_invalid_name(self, mock_input):
        variable_list.clear()
        params = ["APt"]
        value, error = read_variable(params)
        self.assertEqual(error, "Invalid variable name: " + params[0])
        self.assertIsNone(value)


class TestPrintValue(unittest.TestCase):
    @patch("sympy.pprint")
    def test_print_value_valid_variable(self, mock_pprint):
        variable_list.clear()
        set_variable("A", Matrix([[1, 2], [3, 4]]))
        params = ["A"]
        value, error = print_value(params)
        self.assertIsNone(error)
        self.assertIsNone(value)
        mock_pprint.assert_called_with(Matrix([[1, 2], [3, 4]]))

    @patch("sympy.pprint")
    def test_print_value_invalid_variable(self, mock_pprint):
        variable_list.clear()
        params = ["INVALID"]
        value, error = print_value(params)
        self.assertEqual(error, "Variable '" + params[0] + "' is not defined.")
        self.assertIsNone(value)
        mock_pprint.assert_not_called()

    @patch("sympy.pprint")
    def test_print_value_matrix(self, mock_pprint):
        variable_list.clear()
        params = [Matrix([[1, 2], [3, 4]])]
        value, error = print_value(params)
        self.assertIsNone(error)
        self.assertIsNone(value)
        mock_pprint.assert_called_with(Matrix([[1, 2], [3, 4]]))


class TestSetVariableCommand(unittest.TestCase):
    def test_set_variable_command_variable(self):
        variable_list.clear()
        variable_list.append(Variable("B", Matrix([[1, 2], [3, 4]])))
        params = ["A", "B"]
        value, error = set_variable_command(params)
        self.assertIsNone(error)
        self.assertEqual(variable_list[1].name, "A")
        self.assertEqual(variable_list[1].value, Matrix([[1, 2], [3, 4]]))
        self.assertEqual(value, Matrix([[1, 2], [3, 4]]))

    def test_set_variable_command_invalid_name(self):
        variable_list.clear()
        params = ["Apt", Matrix([[1, 2], [3, 4]])]
        value, error = set_variable_command(params)
        self.assertEqual(error, "Invalid variable name: " + params[0])
        self.assertIsNone(value)

    def test_set_variable_command_invalid_value(self):
        variable_list.clear()
        params = ["A", "INVALID"]
        value, error = set_variable_command(params)
        self.assertEqual(error, "Variable '" + params[1] + "' is not defined.")
        self.assertIsNone(value)

    def test_set_variable_command_matrix(self):
        variable_list.clear()
        params = ["A", Matrix([[1, 2], [3, 4]])]
        value, error = set_variable_command(params)
        self.assertIsNone(error)
        self.assertEqual(variable_list[0].name, "A")
        self.assertEqual(variable_list[0].value, Matrix([[1, 2], [3, 4]]))
        self.assertEqual(value, Matrix([[1, 2], [3, 4]]))
