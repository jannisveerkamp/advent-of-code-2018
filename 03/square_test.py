import unittest

from .square import overlap, no_overlap
from common.file import read_file_lines


class TestOverlap(unittest.TestCase):

    def test_simple_overlap(self):
        test_input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEqual(overlap(test_input), 4)

    def test_checksum_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(overlap(test_input), 111326)


class TestNoOverlap(unittest.TestCase):

    def test_simple_overlap(self):
        test_input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEqual(no_overlap(test_input), 3)

    def test_checksum_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(no_overlap(test_input), 1019)
