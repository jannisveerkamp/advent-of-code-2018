import unittest

from .calibration import frequency, frequency_twice
from common.file import read_file_lines


class TestFrequency(unittest.TestCase):

    def test_simple_frequency_1(self):
        self.assertEqual(frequency(["+1", "+1", "+1"]), 3)

    def test_simple_frequency_2(self):
        self.assertEqual(frequency(["+1", "+1", "-2"]), 0)

    def test_simple_frequency_3(self):
        self.assertEqual(frequency(["-1", "-2", "-3"]), -6)

    def test_simple_frequency_4(self):
        self.assertEqual(frequency(["+1", "-2", "+3", "+1"]), 3)

    def test_frequency_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(frequency(test_input), 595)


class TestFrequencyTwice(unittest.TestCase):

    def test_simple_frequency_1(self):
        self.assertEqual(frequency_twice(["+1", "-1"]), 0)

    def test_simple_frequency_2(self):
        self.assertEqual(frequency_twice(["+3", "+3", "+4", "-2", "-4"]), 10)

    def test_simple_frequency_3(self):
        self.assertEqual(frequency_twice(["-6", "+3", "+8", "+5", "-6"]), 5)

    def test_simple_frequency_4(self):
        self.assertEqual(frequency_twice(["+7", "+7", "-2", "-7", "-4"]), 14)

    def test_simple_frequency_5(self):
        self.assertEqual(frequency_twice(["+1", "-2", "+3", "+1"]), 2)

    def test_frequency_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(frequency_twice(test_input), -1)
