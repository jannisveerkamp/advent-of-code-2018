import unittest

from common.file import read_file_lines
from .day_17 import day_17_task_1


@unittest.skip("speedy!")
class TestDay17Task1(unittest.TestCase):

    def test_day_17_task_1_simple(self):
        test_input = ["x=495, y=2..7",
                      "y=7, x=495..501",
                      "x=501, y=3..7",
                      "x=498, y=2..4",
                      "x=506, y=1..2",
                      "x=498, y=10..13",
                      "x=504, y=10..13",
                      "y=13, x=498..504"]
        self.assertEqual(57, day_17_task_1(test_input))

    def test_day_17_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(0, day_17_task_1(test_input))
