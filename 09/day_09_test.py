import unittest

from common.file import read_file
from .day_09 import day_09_task_1


class TestDay09Task1(unittest.TestCase):

    def test_day_09x_task_1_simple_1(self):
        test_input = "9 players; last marble is worth 25 points"
        self.assertEqual(32, day_09_task_1(test_input))

    def test_day_09x_task_1_simple_2(self):
        test_input = "10 players; last marble is worth 1618 points"
        self.assertEqual(8317, day_09_task_1(test_input))

    def test_day_09x_task_1_simple_3(self):
        test_input = "13 players; last marble is worth 7999 points"
        self.assertEqual(146373, day_09_task_1(test_input))

    def test_day_09x_task_1_simple_4(self):
        test_input = "17 players; last marble is worth 1104 points"
        self.assertEqual(2764, day_09_task_1(test_input))

    def test_day_09x_task_1_simple_5(self):
        test_input = "21 players; last marble is worth 6111 points"
        self.assertEqual(54718, day_09_task_1(test_input))

    def test_day_09x_task_1_simple_6(self):
        test_input = "30 players; last marble is worth 5807 points"
        self.assertEqual(37305, day_09_task_1(test_input))

    def test_day_09_task_1__input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(367634, day_09_task_1(test_input))
