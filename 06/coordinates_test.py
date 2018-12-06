import unittest

from .coordinates import size_largest_area, get_array_size, parse_coordinates, size_safe_are


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

    def test_simple_safe_area(self):
        test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        self.assertEqual(size_safe_are(test_input, 32), 16)
