import unittest

from common.file import read_file_lines
from .coordinates import size_largest_area, get_array_size, parse_coordinates, size_safe_area, manhattan_distance


class TestLargestArea(unittest.TestCase):

    def test_parse_coordinates(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(parse_coordinates(test_input), [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]])

    def test_get_array_size(self):
        # size has to be one bigger than the biggest x/y coordinate
        test_input = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]
        self.assertEqual(get_array_size(test_input), (9, 10))

    def test_simple_size_largest_area(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(size_largest_area(test_input), 17)

    def test_size_largest_area_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(size_largest_area(test_input), 4284)


class TestSafeArea(unittest.TestCase):

    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance(0, 0, 0, 0), 0)
        self.assertEqual(manhattan_distance(5, 5, 5, 5), 0)
        self.assertEqual(manhattan_distance(1, 1, 0, 0), 2)
        self.assertEqual(manhattan_distance(0, 0, 1, 1), 2)
        self.assertEqual(manhattan_distance(5, 5, 0, 0), 10)
        self.assertEqual(manhattan_distance(0, 0, 5, 5), 10)
        self.assertEqual(manhattan_distance(1, 2, 3, 4), 4)
        self.assertEqual(manhattan_distance(5, 13, 21, 3), 26)
        self.assertEqual(manhattan_distance(-1, -5, 3, -7), 6)

    def test_simple_safe_area(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(size_safe_area(test_input, 32), 16)

    def test_size_largest_area_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(size_safe_area(test_input, 10000), 35490)
