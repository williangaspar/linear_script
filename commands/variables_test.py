import unittest

from .variables import (
    is_valid_variable_name,
    get_variable_index,
    set_variable,
    get_variable,
    Variable,
    variable_list,
)


class TestIsValidVariableName(unittest.TestCase):
    def test_is_valid_name(self):
        self.assertTrue(is_valid_variable_name("a"))
        self.assertTrue(is_valid_variable_name("A"))
        self.assertTrue(is_valid_variable_name("B"))
        self.assertTrue(is_valid_variable_name("c"))
        self.assertTrue(is_valid_variable_name("Z"))
        self.assertTrue(is_valid_variable_name("z"))

    def test_is_invalid_name(self):
        self.assertFalse(is_valid_variable_name(""))
        self.assertFalse(is_valid_variable_name("1"))
        self.assertFalse(is_valid_variable_name("2"))
        self.assertFalse(is_valid_variable_name("3"))
        self.assertFalse(is_valid_variable_name("AA"))
        self.assertFalse(is_valid_variable_name("aA"))
        self.assertFalse(is_valid_variable_name("Var"))


class TestGetVariableIndex(unittest.TestCase):
    def test_get_variable_index(self):
        variable_list.clear()
        variable_list.append(Variable("a", 1))

        self.assertEqual(get_variable_index("a"), 0)

    def test_get_variable_index_not_found(self):
        variable_list.clear()
        variable_list.append(Variable("a", 1))

        self.assertEqual(get_variable_index("b"), -1)


class TestSetVariable(unittest.TestCase):
    def test_set_variable(self):
        variable_list.clear()
        self.assertTrue(set_variable("a", 1))
        self.assertEqual(variable_list[0].name, "a")
        self.assertEqual(variable_list[0].value, 1)
        self.assertIsNone(variable_list[0].det)

    def test_set_variable_invalid_name(self):
        variable_list.clear()
        self.assertFalse(set_variable("1", 1))
        self.assertEqual(len(variable_list), 0)

    def test_set_variable_already_exists(self):
        variable_list.clear()
        variable_list.append(Variable("a", 1))
        self.assertTrue(set_variable("a", 2))
        self.assertEqual(variable_list[0].name, "a")
        self.assertEqual(variable_list[0].value, 2)
        self.assertIsNone(variable_list[0].det)


class TestGetVariable(unittest.TestCase):
    def test_get_variable_exists(self):
        variable_list.clear()
        variable_list.append(Variable("a", 1))
        actual = get_variable("a")
        expected = Variable("a", 1)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.value, expected.value)

    def test_get_variable_not_exists(self):
        variable_list.clear()
        self.assertIsNone(get_variable("a"))
        atual = get_variable("b")
        expected = None
        self.assertEqual(atual, expected)
