import unittest

from common.file import read_file_lines
from .day_15 import day_15_task_1


class TestDay15Task1(unittest.TestCase):

    def test_day_15_task_1_simple_1(self):
        test_input = ["#######",
                      "#.G...#",
                      "#...EG#",
                      "#.#.#G#",
                      "#..G#E#",
                      "#.....#",
                      "#######"]
        self.assertEqual(27730, day_15_task_1(test_input))

    def test_day_15_task_1_simple_2(self):
        test_input = ["#######",
                      "#G..#E#",
                      "#E#E.E#",
                      "#G.##.#",
                      "#...#E#",
                      "#...E.#",
                      "#######"]
        self.assertEqual(36334, day_15_task_1(test_input))

    def test_day_15_task_1_simple_3(self):
        test_input = ["#######",
                      "#E..EG#",
                      "#.#G.E#",
                      "#E.##E#",
                      "#G..#.#",
                      "#..E#.#",
                      "#######"]
        self.assertEqual(39514, day_15_task_1(test_input))

    def test_day_15_task_1_simple_4(self):
        test_input = ["#######",
                      "#E.G#.#",
                      "#.#G..#",
                      "#G.#.G#",
                      "#G..#.#",
                      "#...E.#",
                      "#######"]
        self.assertEqual(27755, day_15_task_1(test_input))

    def test_day_15_task_1_advanced(self):
        test_input = ["#########",
                      "#G......#",
                      "#.E.#...#",
                      "#..##..G#",
                      "#...##..#",
                      "#...#...#",
                      "#.G...G.#",
                      "#.....G.#",
                      "#########"]
        self.assertEqual(18740, day_15_task_1(test_input))

    def test_day_15_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(0, day_15_task_1(test_input))
