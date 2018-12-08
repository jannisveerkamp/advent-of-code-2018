import unittest

from common.file import read_file_lines
from .day_08 import day_08_task_1


class TestDay08Task1(unittest.TestCase):

    def test_day_08_task_1_simple(self):
        test_input = ["2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"]
        self.assertEqual(138, day_08_task_1(test_input))

    def test_day_08_task_1__input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(0, day_08_task_1(test_input))
