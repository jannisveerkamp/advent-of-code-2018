import unittest

from .dummy import string_sum
from common.file import read_file_lines


class TestCaptcha(unittest.TestCase):

    def test_simple_sum(self):
        self.assertEqual(string_sum("1", "2"), 3)

    def test_simple_sum_test_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(string_sum(test_input[0], test_input[1]), 3)
