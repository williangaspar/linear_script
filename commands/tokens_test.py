import unittest

from commands.tokens import get_tokens


class TestGetTokens(unittest.TestCase):
    def test_get_tokens_simple(self):
        command = "rref A"
        tokens = get_tokens(command)
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0], "rref")
        self.assertEqual(tokens[1], "A")

    def test_get_tokens_with_paranteses(self):
        command = "rref (A)"
        tokens = get_tokens(command)
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0], "rref")
        self.assertEqual(tokens[1], "A")

    def test_get_tokens_with_paranteses2(self):
        command = "dot (A B)"
        tokens = get_tokens(command)
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0], "dot")
        self.assertEqual(tokens[1], "A")
        self.assertEqual(tokens[2], "B")

    def test_get_tokens_with_complex(self):
        command = "set P dot (dot A [inv dot transp A A]) transp A"
        tokens = get_tokens(command)
        self.assertEqual(len(tokens), 12)
        self.assertEqual(tokens[0], "set")
        self.assertEqual(tokens[1], "P")
        self.assertEqual(tokens[2], "dot")
        self.assertEqual(tokens[3], "dot")
        self.assertEqual(tokens[4], "A")
