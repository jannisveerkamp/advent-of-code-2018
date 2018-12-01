import unittest

from .calibration import frequency
from common.file import read_file_lines


class TestFrequency(unittest.TestCase):

    def test_simple_frequency_1(self):
        self.assertEqual(frequency(["+1", "+1", "+1"]), 3)

    def test_simple_frequency_2(self):
        self.assertEqual(frequency(["+1", "+1", "-2"]), 0)

    def test_simple_frequency_3(self):
        self.assertEqual(frequency(["-1", "-2", "-3"]), -6)

    def test_frequency_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(frequency(test_input), -1)
