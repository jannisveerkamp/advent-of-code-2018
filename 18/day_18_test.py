import unittest

from common.file import read_file_lines
from .day_18 import day_18_task_1, day_18_task_2


class TestDay18Task1(unittest.TestCase):
    def test_day_18_task_1_simple(self):
        test_input = [".#.#...|#.",
                      ".....#|##|",
                      ".|..|...#.",
                      "..|#.....#",
                      "#.#|||#|#|",
                      "...#.||...",
                      ".|....|...",
                      "||...#|.#|",
                      "|.||||..|.",
                      "...#.|..|."]
        self.assertEqual(1147, day_18_task_1(test_input, 10))

    def test_day_18_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(588436, day_18_task_1(test_input, 10))

    def test_day_18_task_2_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(195290, day_18_task_2(test_input, 1000000000))
