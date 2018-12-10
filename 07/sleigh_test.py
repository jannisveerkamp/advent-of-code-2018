import unittest

from common.file import read_file_lines
from .sleigh import sort_instructions, parse_instructions, work_time, letter_offset


class TestInstructionSorting(unittest.TestCase):

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

    def test_simple_sort_instructions(self):
        test_input = ["Step C must be finished before step A can begin.",
                      "Step C must be finished before step F can begin.",
                      "Step A must be finished before step B can begin.",
                      "Step A must be finished before step D can begin.",
                      "Step B must be finished before step E can begin.",
                      "Step D must be finished before step E can begin.",
                      "Step F must be finished before step E can begin."]
        self.assertEqual("CABDFE", sort_instructions(test_input))

    def test_size_sort_instructions_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual("GKCNPTVHIRYDUJMSXFBQLOAEWZ", sort_instructions(test_input))


class TestWorker(unittest.TestCase):

    def test_letter_offset(self):
        self.assertEqual(1, letter_offset("A"))
        self.assertEqual(2, letter_offset("B"))
        self.assertEqual(3, letter_offset("C"))
        self.assertEqual(4, letter_offset("D"))

    def test_simple_instructions_work_time(self):
        test_input = ["Step C must be finished before step A can begin.",
                      "Step C must be finished before step F can begin.",
                      "Step A must be finished before step B can begin.",
                      "Step A must be finished before step D can begin.",
                      "Step B must be finished before step E can begin.",
                      "Step D must be finished before step E can begin.",
                      "Step F must be finished before step E can begin."]
        self.assertEqual(15, work_time(test_input, 2, 0))

    def test_instructions_input_work_time(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(1265, work_time(test_input, 5, 60))
