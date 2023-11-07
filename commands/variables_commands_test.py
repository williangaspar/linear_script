import unittest

from commands.variables_commands import set_variable

from .variables import variable_list


class TestSetVariable(unittest.TestCase):
    def test_set_variable_valid(self):
        variable_list.clear()

        value = set_variable(["a"])

        pass
