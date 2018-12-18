import unittest

from common.file import read_file_lines
from .day_18 import day_18_task_1


@unittest.skip("speedy!")
class TestDayXXTask1(unittest.TestCase):

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
        self.assertEqual(0, day_18_task_1(test_input, 10))