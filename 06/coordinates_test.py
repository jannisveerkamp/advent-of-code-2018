import unittest

from common.file import read_file
from .coordinates import size_largest_area, get_array_size, parse_coordinates


class TestLargestArea(unittest.TestCase):

    def test_parse_coordinates(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(parse_coordinates(test_input), [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]])

    def test_get_array_size(self):
        test_input = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]
        self.assertEqual(get_array_size(test_input), (8, 9))

    def test_simple_size_largest_area(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(size_largest_area(test_input), 17)

    def test_size_largest_area_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(size_largest_area(test_input), 0)
