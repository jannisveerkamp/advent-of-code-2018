import unittest

from common.file import read_file_lines
from .sleigh import sort_instructions, parse_instructions


class TestLargestArea(unittest.TestCase):

    def test_parsing(self):
        test_input = ["Step C must be finished before step A can begin.",
                      "Step C must be finished before step F can begin.",
                      "Step A must be finished before step B can begin.",
                      "Step A must be finished before step D can begin.",
                      "Step B must be finished before step E can begin.",
                      "Step D must be finished before step E can begin.",
                      "Step F must be finished before step E can begin."]
        self.assertEqual(parse_instructions(test_input),
                         [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')])

    def test_simple_dummy(self):
        test_input = ["Step C must be finished before step A can begin.",
                      "Step C must be finished before step F can begin.",
                      "Step A must be finished before step B can begin.",
                      "Step A must be finished before step D can begin.",
                      "Step B must be finished before step E can begin.",
                      "Step D must be finished before step E can begin.",
                      "Step F must be finished before step E can begin."]
        self.assertEqual("CABDFE", sort_instructions(test_input))

    def test_size_largest_area_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(sort_instructions(test_input), "GKCNPTVHIRYDUJMSXFBQLOAEWZ")
