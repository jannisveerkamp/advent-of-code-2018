import unittest

from common.file import read_file_lines
from .day_13 import day_13_task_1


class TestDay13Task1(unittest.TestCase):

    def test_day_13_task_1_simple(self):
        test_input = read_file_lines(__file__, "simple_input.txt")
        self.assertEqual((7, 3), day_13_task_1(test_input))

    def test_day_13_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual((100, 21), day_13_task_1(test_input))
