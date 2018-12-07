import unittest

from common.file import read_file_lines
from .sleigh import sort_instructions


class TestLargestArea(unittest.TestCase):

    def test_simple_dummy(self):
        self.begin__ = ["Step C must be finished before step A can begin.",
                        "Step C must be finished before step F can begin.",
                        "Step A must be finished before step B can begin.",
                        "Step A must be finished before step D can begin.",
                        "Step B must be finished before step E can begin.",
                        "Step D must be finished before step E can begin.",
                        "Step F must be finished before step E can begin."]
        test_input = self.begin__
        self.assertEqual(sort_instructions(test_input), 0)

    def test_size_largest_area_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(sort_instructions(test_input), 0)
