import unittest

from common.file import read_file_lines
from .day_12 import day_12, parse_instructions


class TestDay12Task1(unittest.TestCase):

    def test_day_12_parse_instructions(self):
        test_input = ["initial state: #..#.#..##......###...###",
                      "",
                      "...## => #",
                      "..#.. => ."]
        state, instructions = parse_instructions(test_input)
        self.assertEqual("#..#.#..##......###...###", state)
        self.assertEqual({"...##": "#", "..#..": "."}, instructions)

    def test_day_12_task_1_simple(self):
        test_input = ["initial state: #..#.#..##......###...###",
                      "",
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
        self.assertEqual(325, day_12(test_input, 20))

    def test_day_12_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(2571, day_12(test_input, 20))

    def test_day_12_task_2_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(3100000000655, day_12(test_input, 50000000000))
