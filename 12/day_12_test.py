import unittest

from common.file import read_file_lines
from .day_12 import day_12_task_1


class TestDay12Task1(unittest.TestCase):

    def test_day_12_task_1_simple(self):
        test_input = ["initial state: #..#.#..##......###...###",
                      ""
                      "...## => #",
                      "..#.. => #",
                      ".#... => #",
                      ".#.#. => #",
                      ".#.## => #",
                      ".##.. => #",
                      ".#### => #",
                      "#.#.# => #",
                      "#.### => #",
                      "##.#. => #",
                      "##.## => #",
                      "###.. => #",
                      "###.# => #",
                      "####. => #"]
        self.assertEqual(325, day_12_task_1(test_input, 20))

    def test_day_12_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(0, day_12_task_1(test_input, 20))
