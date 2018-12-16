import unittest

from common.file import read_file_lines
from .day_16 import day_16_task_1


class TestDayXXTask1(unittest.TestCase):

    @unittest.skip("speedy!")
    def test_day_16_task_1_simple(self):
        test_input = ["Before: [3, 2, 1, 1]",
                      "9 2 1 2",
                      "After:  [3, 2, 2, 1]"]
        self.assertEqual(1, day_16_task_1(test_input))

    def test_day_16_task_1_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(0, day_16_task_1(test_input[:3128]))
