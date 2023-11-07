import unittest
from commands.command_list import command_list

from commands.core import is_valid_command, validate_input
from commands.tokens import get_tokens


class TestIsValidCommand(unittest.TestCase):
    def test_is_valid_command_true(self):
        command = "rref"
        is_valid, cmd = is_valid_command(command)
        self.assertTrue(is_valid)
        self.assertEqual(cmd.name, "rref")

        command = "det"
        is_valid, cmd = is_valid_command(command)
        self.assertTrue(is_valid)
        self.assertEqual(cmd.name, "det")

        command = "dot"
        is_valid, cmd = is_valid_command(command)
        self.assertTrue(is_valid)
        self.assertEqual(cmd.name, "dot")

    def test_is_valid_command_true2(self):
        for cmd in command_list:
            is_valid, cmd_result = is_valid_command(cmd.name)
            self.assertTrue(is_valid)
            self.assertEqual(cmd_result.name, cmd.name)

    def test_is_valid_command_false(self):
        command = "rref2"
        is_valid, _ = is_valid_command(command)
        self.assertFalse(is_valid)

        command = "det2"
        is_valid, _ = is_valid_command(command)
        self.assertFalse(is_valid)

        command = "something"
        is_valid, _ = is_valid_command(command)
        self.assertFalse(is_valid)


class TestValidatInput(unittest.TestCase):
    def test_valid_input_valid(self):
        command = "det A"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid2(self):
        command = "dot [A B]"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid3(self):
        command = "dot (dot A B) inv C"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid4(self):
        command = ""
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_invalid(self):
        command = "det"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Too few parameters for command: det")

    def test_valid_input_invalid2(self):
        command = "det A B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Too many parameters for command: det")

    def test_valid_input_invalid3(self):
        command = "det dott A B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Invalid token: dott")

    def test_valid_input_invalid4(self):
        command = "dot inv A B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Too many parameters for command: inv")

    def test_valid_input_invalid5(self):
        command = "dot inv B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Too few parameters for command: dot")

    def test_valid_input_invalid6(self):
        command = "A dot B C"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "A is not a valid command")


class TestExecuteCommand(unittest.TestCase):
    def test_execute_command_read(self):
        pass
