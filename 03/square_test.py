import unittest

from .square import overlap
from common.file import read_file_lines


class TestSquare(unittest.TestCase):

    def test_simple_overlap(self):
        test_input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEqual(overlap(test_input), 4)

    def test_checksum_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(overlap(test_input), 111326)
