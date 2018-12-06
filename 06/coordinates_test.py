import unittest

from common.file import read_file
from .coordinates import size_largest_area


class TestLargestArea(unittest.TestCase):

    def test_simple_size_largest_area(self):
        test_input = ["1, 1",
                      "1, 6",
                      "8, 3",
                      "3, 4",
                      "5, 5",
                      "8, 9"]
        self.assertEqual(size_largest_area(test_input), 17)

    def test_size_largest_area_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(size_largest_area(test_input), 0)
