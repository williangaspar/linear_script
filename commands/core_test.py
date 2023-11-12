import unittest
from unittest.mock import patch
from commands.command import Command
import io
import sys

from commands.command_list import command_list
from commands.core import execute_commands, is_valid_command, validate_input
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

    def test_valid_input_valid5(self):
        command = "set P dot A transp A"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid6(self):
        command = "set P dot (dot A [inv dot transp A A]) transp A"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid7(self):
        command = "quit"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_valid8(self):
        command = "print A"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_input_invalid(self):
        command = "det"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Not enough parameters for command: det")

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
        command = "inv A B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Too many parameters for command: inv")

    def test_valid_input_invalid5(self):
        command = "dot inv B"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Not enough parameters for command: dot")

    def test_valid_input_invalid6(self):
        command = "A dot B C"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "A is not a valid command")

    def test_valid_input_invalid7(self):
        command = "set A print C"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(
            error, "print is a void command and cannot be used as a parameter"
        )

    @patch("commands.core.MAX_STACK_DEPTH", 2)
    def test_valid_input_invalid_stack_over_flow(self):
        command = "set P dot (dot A [inv dot transp A A]) transp A"
        tokens = get_tokens(command)
        is_valid, error = validate_input(tokens)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Stack overflow")


class TestExecuteCommand(unittest.TestCase):
    @patch("commands.core.MAX_STACK_DEPTH", 2)
    def test_execute_command_stack_overflow(self):
        command = "set P dot (dot A [inv dot transp A A]) transp A"
        tokens = get_tokens(command)

        with self.assertRaises(Exception) as e:
            execute_commands(tokens)
            assert str(e.value) == "Stack overflow"

    def test_execute_command_not_enough_params(self):
        command = "det"
        tokens = get_tokens(command)

        with self.assertRaises(Exception) as e:
            execute_commands(tokens)
            assert str(e.value) == "Not enough parameters for command: det"

    def test_excute_command_call_command(self):
        command = "TEST A B"
        params_passed = []

        def test_command(params):
            params_passed.extend(params)
            return None, None

        command_list.append(Command("TEST", "Test command", 2, test_command))
        tokens = get_tokens(command)
        execute_commands(tokens)
        self.assertEqual(params_passed, ["A", "B"])
        command_list.pop()

    def test_execute_command_return_value(self):
        command = "TEST A B"
        params_passed = []

        def test_command(params):
            params_passed.extend(params)
            return "Test", None

        command_list.append(Command("TEST", "Test command", 2, test_command))
        tokens = get_tokens(command)
        result = execute_commands(tokens)
        self.assertEqual(result, "Test")
        command_list.pop()

    def test_execute_command_print_error(self):
        command = "TEST A B"
        params_passed = []

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        def test_command(params):
            params_passed.extend(params)
            return None, "Error 123"

        command_list.append(Command("TEST", "Test command", 2, test_command))
        tokens = get_tokens(command)
        result = execute_commands(tokens)
        self.assertIsNone(result)
        self.assertTrue(capturedOutput.getvalue().find("Error 123") != -1)
        command_list.pop()
